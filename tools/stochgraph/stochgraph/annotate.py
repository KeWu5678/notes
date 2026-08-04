"""Stage 1 — the concept layer attached to statements, and stage 3's projection.

An annotation records what a statement *assumes*, what it *asserts*, and what it
*introduces*, in terms of registry concept ids. It is the only part of the pipeline
an LLM writes, so it is also the only part that is validated before it is trusted:
every concept id must resolve, every conclusion must be well-formed.

Hypotheses are unbound — ``requires: ["prop/left-continuous"]`` records that a
statement assumes left-continuity but not of which object. Conclusions carry their
arguments, because layer 2 is object-to-object and there is otherwise nothing to
project an edge between. That asymmetry is deliberate: binding every hypothesis
would roughly triple the node count for queries nobody asked for.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional

from . import ontology
from .concepts import Registry


@dataclass
class Conclusion:
    """One asserted fact: a predicate, optionally applied to named arguments.

    ``args`` are concept ids in argument order — used when the statement asserts
    something about *named* objects ("L0 is dense in L(M)"). Leave it empty when
    the arguments are the statement's own bound variables ("X and Y are
    modifications"): those variables are not concepts and inventing nodes for them
    would fill the graph with per-theorem noise.

    The distinction drives the projection. A bound conclusion yields an
    object-level edge; an unbound one yields a predicate-level implication from
    each hypothesis, which is how "modifications + left-continuous paths implies
    indistinguishable" reaches layer 2 at all.
    """

    predicate: str                        # prop/... or rel/...
    args: List[str] = field(default_factory=list)
    # Hypotheses for *this* conclusion. A multi-part result ("i) ... ii) ...")
    # proves several implications with different antecedents, so a single
    # statement-level `requires` would wrongly merge them. Empty means "use the
    # statement's `requires`".
    given: List[str] = field(default_factory=list)
    under: List[str] = field(default_factory=list)   # extra conditions, concept ids
    negated: bool = False                 # "does not hold in general"

    def validate(self, registry: Registry, where: str) -> List[str]:
        problems: List[str] = []
        concept = registry.get(self.predicate)
        if concept is None:
            problems.append(f"{where}: unknown predicate {self.predicate!r}")
            return problems
        if concept.label not in ("Property", "Relation"):
            problems.append(
                f"{where}: {self.predicate} is an {concept.label}, not a predicate"
            )
        # An empty `args` is the unbound form and always legal; a non-empty one
        # must match the predicate's arity exactly.
        if self.args and concept.arity and len(self.args) != concept.arity:
            problems.append(
                f"{where}: {self.predicate} has arity {concept.arity}, "
                f"got {len(self.args)} argument(s)"
            )
        for arg in self.args:
            if arg not in registry:
                problems.append(f"{where}: unknown argument {arg!r}")
        for cond in self.under:
            if cond not in registry:
                problems.append(f"{where}: unknown condition {cond!r}")
        # A hypothesis must be a predicate. An object in `given` would project an
        # edge whose source is a thing rather than an assertion — type-wrong, and
        # a resolve-only check would wave it through.
        for field_name, ids in (("hypothesis", self.given), ("condition", self.under)):
            for cid in ids:
                other = registry.get(cid)
                if other is not None and other.label not in ("Property", "Relation"):
                    problems.append(
                        f"{where}: {field_name} {cid!r} is an {other.label}, "
                        "not a predicate"
                    )
        for hyp in self.given:
            if hyp not in registry:
                problems.append(f"{where}: unknown hypothesis {hyp!r}")
        return problems


@dataclass
class ReifiedFact:
    """An assertion given its own identity, so an edge can end on it.

    Local to the statement that declares it: ``local`` is unique within the
    annotation, and the global node id is derived from the pair. Created only when
    something points at the assertion — see the `:Fact` label in `ontology.py`.
    """

    local: str                            # e.g. "a"
    predicate: str
    args: List[str] = field(default_factory=list)
    negated: bool = False
    gloss: str = ""                       # how the notes phrase it

    def node_id(self, statement_id: str) -> str:
        return "fact/" + statement_id.replace("/", "-") + "-" + self.local

    def validate(self, registry: Registry, where: str) -> List[str]:
        problems: List[str] = []
        concept = registry.get(self.predicate)
        if concept is None:
            problems.append(f"{where}: unknown predicate {self.predicate!r}")
        elif concept.label not in ("Property", "Relation"):
            problems.append(
                f"{where}: {self.predicate} is an {concept.label}, not a predicate"
            )
        elif concept.arity and len(self.args) != concept.arity:
            problems.append(
                f"{where}: {self.predicate} has arity {concept.arity}, "
                f"got {len(self.args)}"
            )
        for arg in self.args:
            if arg not in registry:
                problems.append(f"{where}: unknown argument {arg!r}")
        return problems


@dataclass
class Equivalence:
    """Two assertions of the same statement that hold under the same circumstances."""

    left: str                             # local fact id
    right: str
    under: List[str] = field(default_factory=list)


@dataclass
class Annotation:
    """The concept layer for one statement."""

    statement_id: str
    requires: List[str] = field(default_factory=list)     # unbound predicates
    concludes: List[Conclusion] = field(default_factory=list)
    defines: List[str] = field(default_factory=list)      # concept ids introduced
    about: List[str] = field(default_factory=list)        # subject objects
    facts: List[ReifiedFact] = field(default_factory=list)
    equivalences: List[Equivalence] = field(default_factory=list)
    statement_latex: str = ""                             # tier: transcribed
    note: str = ""

    def concept_ids(self) -> List[str]:
        ids = list(self.requires) + list(self.defines) + list(self.about)
        for fact in self.facts:
            ids.append(fact.predicate)
            ids.extend(fact.args)
        for conclusion in self.concludes:
            ids.append(conclusion.predicate)
            ids.extend(conclusion.args)
            ids.extend(conclusion.under)
            ids.extend(conclusion.given)
        return ids

    def validate(self, registry: Registry) -> List[str]:
        where = self.statement_id
        problems = [
            f"{where}: unknown concept {cid!r}"
            for cid in registry.undefined(self.requires + self.defines + self.about)
        ]
        for i, conclusion in enumerate(self.concludes):
            problems.extend(conclusion.validate(registry, f"{where}#concludes[{i}]"))
        locals_seen = set()
        for fact in self.facts:
            problems.extend(fact.validate(registry, f"{where}#fact[{fact.local}]"))
            if fact.local in locals_seen:
                problems.append(f"{where}: duplicate fact id {fact.local!r}")
            locals_seen.add(fact.local)
        for eq in self.equivalences:
            for side in (eq.left, eq.right):
                if side not in locals_seen:
                    problems.append(f"{where}: equivalence names unknown fact {side!r}")
            for cond in eq.under:
                other = registry.get(cond)
                if other is None:
                    problems.append(f"{where}: unknown condition {cond!r}")
                elif other.label not in ("Property", "Relation"):
                    problems.append(
                        f"{where}: condition {cond!r} is an {other.label}, "
                        "not a predicate"
                    )
        return problems


# --------------------------------------------------------------------------- #
# storage                                                                     #
# --------------------------------------------------------------------------- #

def annotations_dir(root: Path) -> Path:
    return root / "annotations"


def _filename(statement_id: str) -> str:
    return statement_id.replace("/", "_") + ".json"


def save_annotation(annotation: Annotation, root: Path) -> Path:
    target = annotations_dir(root)
    target.mkdir(parents=True, exist_ok=True)
    body = {
        "statement_id": annotation.statement_id,
        "requires": annotation.requires,
        "concludes": [
            {k: v for k, v in vars(c).items() if v not in ([], False, "")}
            for c in annotation.concludes
        ],
        "defines": annotation.defines,
        "about": annotation.about,
        "facts": [
            {k: v for k, v in vars(f).items() if v not in ([], False, "")}
            for f in annotation.facts
        ],
        "equivalences": [
            {k: v for k, v in vars(e).items() if v not in ([], "")}
            for e in annotation.equivalences
        ],
        "statement_latex": annotation.statement_latex,
        "note": annotation.note,
        "provenance": "agent",
    }
    body = {k: v for k, v in body.items() if v not in ([], "")}
    path = target / _filename(annotation.statement_id)
    path.write_text(json.dumps(body, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")
    return path


def load_annotations(root: Path) -> Dict[str, Annotation]:
    target = annotations_dir(root)
    if not target.exists():
        return {}
    out: Dict[str, Annotation] = {}
    for path in sorted(target.glob("*.json")):
        raw = json.loads(path.read_text(encoding="utf-8"))
        conclusions = [Conclusion(**c) for c in raw.get("concludes", [])]
        facts = [ReifiedFact(**f) for f in raw.get("facts", [])]
        equivalences = [Equivalence(**e) for e in raw.get("equivalences", [])]
        out[raw["statement_id"]] = Annotation(
            statement_id=raw["statement_id"],
            requires=raw.get("requires", []),
            concludes=conclusions,
            defines=raw.get("defines", []),
            about=raw.get("about", []),
            facts=facts,
            equivalences=equivalences,
            statement_latex=raw.get("statement_latex", ""),
            note=raw.get("note", ""),
        )
    return out


# --------------------------------------------------------------------------- #
# stage 3 — projection to layer 2                                             #
# --------------------------------------------------------------------------- #

@dataclass
class ProjectedEdge:
    """A concept-to-concept edge, derived from a statement's conclusion.

    The edge type is the relation's own name, so ``DENSE_IN`` the edge corresponds
    to ``(:Relation {name: "dense in"})`` the concept — an invariant the loader
    checks. Negation is expressed by the relation itself (``NOT_EQUALS``) rather
    than by a flag, matching the notation the mathematics already uses.
    """

    source: str
    target: str
    type: str
    via: str                                  # justifying statement ref
    under: List[str] = field(default_factory=list)
    predicate_id: str = ""


def edge_type_for(concept, negated: bool) -> str:
    """The layer-2 edge type a relation projects to.

    Uses the concept's explicit ``edge`` when set, so a noun-named relation can
    still yield a verb-shaped edge ("modification" -> MODIFICATION_OF).
    """
    raw = getattr(concept, "edge", "") or getattr(concept, "name", str(concept))
    slug = "".join(ch if ch.isalnum() else "_" for ch in raw.strip().upper())
    slug = "_".join(part for part in slug.split("_") if part)
    return f"NOT_{slug}" if negated else slug


def project(
    annotations: Dict[str, Annotation],
    registry: Registry,
    statement_refs: Dict[str, str],
) -> List[ProjectedEdge]:
    """Derive layer-2 edges from every binary (or higher) conclusion.

    Unary conclusions become ``HAS_PROPERTY``. Conclusions of arity > 2 are skipped:
    an edge has two endpoints, and forcing a ternary relation into one would be the
    same mistake the statement layer exists to avoid.
    """
    edges: List[ProjectedEdge] = []
    for statement_id, annotation in sorted(annotations.items()):
        via = statement_refs.get(statement_id, statement_id)
        for conclusion in annotation.concludes:
            concept = registry.get(conclusion.predicate)
            if concept is None:
                continue

            if not conclusion.args:
                # Unbound: the statement says "these hypotheses imply this
                # conclusion" of its own variables. Each hypothesis becomes an
                # IMPLIES edge whose `under` carries the remaining ones, so no
                # hypothesis is silently dropped and the qualifier travels with
                # the edge.
                hypotheses = [
                    h for h in (conclusion.given or annotation.requires)
                    if h != conclusion.predicate
                ]
                for hypothesis in hypotheses:
                    others = sorted(
                        (set(hypotheses) - {hypothesis}) | set(conclusion.under)
                    )
                    # IMPLIES asserts sufficiency, so it may only be used when the
                    # hypothesis really is sufficient on its own. "Adapted and
                    # right-continuous implies progressively measurable" must NOT
                    # produce `adapted IMPLIES progressively measurable` with the
                    # rest tucked into a key — that edge is simply false read on
                    # its own, and edges have to be true read on their own.
                    base = (
                        ontology.SUFFICIENT_FOR_GIVEN if others
                        else ontology.SUFFICIENT_FOR
                    )
                    edges.append(ProjectedEdge(
                        source=hypothesis,
                        target=conclusion.predicate,
                        type=("NOT_" + base) if conclusion.negated else base,
                        via=via,
                        under=others,
                        predicate_id=conclusion.predicate,
                    ))
                continue

            if concept.label == "Property" and len(conclusion.args) == 1:
                edges.append(ProjectedEdge(
                    source=conclusion.args[0],
                    target=conclusion.predicate,
                    type=(ontology.NOT_HAS_PROPERTY if conclusion.negated
                          else ontology.HAS_PROPERTY),
                    via=via, under=list(conclusion.under),
                    predicate_id=conclusion.predicate,
                ))
            elif concept.label == "Relation" and len(conclusion.args) == 2:
                edges.append(ProjectedEdge(
                    source=conclusion.args[0],
                    target=conclusion.args[1],
                    type=edge_type_for(concept, conclusion.negated),
                    via=via, under=list(conclusion.under),
                    predicate_id=conclusion.predicate,
                ))
    return edges
