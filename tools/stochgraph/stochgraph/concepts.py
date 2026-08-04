"""The concept registry — stage 2's canonical identity for objects and predicates.

This is the part of the design most directly borrowed from Danus, whose fact graph
keeps a layered glossary plus a coverage check that flags any symbol used but
defined nowhere reachable. The failure it prevents is quiet: if an extractor emits
"left-continuous trajectories", "all paths left-continuous" and "left-continuity of
paths" as three concepts, then "which results assume left-continuity?" returns a
third of the answer and looks perfectly healthy doing it.

So identity is explicit and centralized. An extraction pass may only *reuse* an
existing concept id or *propose* a new one; a proposal is not a concept until it is
accepted into the registry.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional

# The four content labels. `Definition` is a statement label, not a concept one.
CONCEPT_LABELS = ("Object", "Property", "Relation")

# Optional second label on an object. Extensible by design: the stable layer is
# `:Object`, so adding a refinement never invalidates an existing query.
OBJECT_REFINEMENTS = (
    "FunctionSpace", "Process", "Measure", "Map", "SigmaField", "Space",
)

ID_RE = re.compile(r"^(obj|prop|rel)/[a-z0-9][a-z0-9-]*$")

ID_PREFIX = {"Object": "obj", "Property": "prop", "Relation": "rel"}


@dataclass
class Concept:
    """One canonical node of the concept layer."""

    id: str
    label: str                                   # Object | Property | Relation
    name: str                                    # display name, as the notes write it
    refine: str = ""                             # second label, objects only
    symbol: str = ""                             # notation, when there is one
    aliases: List[str] = field(default_factory=list)
    arity: int = 0                               # 1 for Property, >=2 for Relation
    defined_by: str = ""                         # statement id, when the notes define it
    # Edge type this relation projects to. Defaults to the slug of `name`; set it
    # when the name is a noun and the edge wants a verb ("modification" ->
    # MODIFICATION_OF), so layer 2 reads as mathematics rather than as labels.
    edge: str = ""
    note: str = ""

    def validate(self) -> List[str]:
        problems: List[str] = []
        if not ID_RE.match(self.id):
            problems.append(f"{self.id}: malformed id")
        if self.label not in CONCEPT_LABELS:
            problems.append(f"{self.id}: unknown label {self.label!r}")
        elif not self.id.startswith(ID_PREFIX[self.label] + "/"):
            problems.append(
                f"{self.id}: id prefix does not match label {self.label!r}"
            )
        if self.refine and self.label != "Object":
            problems.append(f"{self.id}: only objects take a refinement label")
        if self.refine and self.refine not in OBJECT_REFINEMENTS:
            problems.append(f"{self.id}: unknown refinement {self.refine!r}")
        if not self.name.strip():
            problems.append(f"{self.id}: empty name")
        # Arity is what distinguishes a property from a relation; without it the
        # two collapse and the projection cannot tell a unary assertion from a
        # binary one.
        if self.label == "Property" and self.arity != 1:
            problems.append(f"{self.id}: a property has arity 1, got {self.arity}")
        if self.label == "Relation" and self.arity < 2:
            problems.append(f"{self.id}: a relation has arity >= 2, got {self.arity}")
        return problems


class Registry:
    """The accepted concepts, plus the queue of proposals awaiting review."""

    def __init__(self, concepts: Optional[Dict[str, Concept]] = None,
                 proposals: Optional[List[dict]] = None) -> None:
        self.concepts: Dict[str, Concept] = concepts or {}
        self.proposals: List[dict] = proposals or []

    # ------------------------------------------------------------------- io
    @classmethod
    def load(cls, root: Path) -> "Registry":
        concepts: Dict[str, Concept] = {}
        path = root / "concepts.json"
        if path.exists():
            raw = json.loads(path.read_text(encoding="utf-8"))
            for cid, body in raw.items():
                concepts[cid] = Concept(id=cid, **body)

        proposals: List[dict] = []
        queue = root / "review" / "proposals.json"
        if queue.exists():
            proposals = json.loads(queue.read_text(encoding="utf-8"))

        return cls(concepts, proposals)

    def save(self, root: Path) -> None:
        body = {
            cid: {
                k: v for k, v in vars(c).items()
                if k != "id" and v not in ("", 0, [], None)
            }
            for cid, c in sorted(self.concepts.items())
        }
        (root / "concepts.json").write_text(
            json.dumps(body, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        review = root / "review"
        review.mkdir(parents=True, exist_ok=True)
        (review / "proposals.json").write_text(
            json.dumps(self.proposals, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    # --------------------------------------------------------------- lookup
    def __contains__(self, cid: str) -> bool:
        return cid in self.concepts

    def get(self, cid: str) -> Optional[Concept]:
        return self.concepts.get(cid)

    def resolve(self, text: str) -> Optional[Concept]:
        """Find a concept by name or alias, case-insensitively.

        This is what an extraction pass consults before proposing anything new;
        it is the mechanism by which the registry actually gets reused rather
        than re-invented per section.
        """
        needle = text.strip().lower()
        for concept in self.concepts.values():
            if needle == concept.name.lower() or needle == concept.symbol.lower():
                return concept
            if any(needle == a.lower() for a in concept.aliases):
                return concept
        return None

    def by_label(self, label: str) -> List[Concept]:
        return sorted(
            (c for c in self.concepts.values() if c.label == label),
            key=lambda c: c.id,
        )

    # ---------------------------------------------------------------- write
    def accept(self, concept: Concept) -> List[str]:
        """Add a concept to the registry, or explain why it cannot be added."""
        problems = concept.validate()
        if concept.id in self.concepts:
            problems.append(f"{concept.id}: already registered")
        clash = self.resolve(concept.name)
        if clash and clash.id != concept.id:
            problems.append(
                f"{concept.id}: name {concept.name!r} already resolves to {clash.id}"
            )
        if not problems:
            self.concepts[concept.id] = concept
        return problems

    def propose(self, proposal: dict) -> None:
        """Queue a new concept for review. Never silently accepted."""
        self.proposals.append(proposal)

    # ------------------------------------------------------- coverage check
    def undefined(self, ids: Iterable[str]) -> List[str]:
        """Referenced concept ids that are not in the registry.

        The build fails on a non-empty result. That is the whole point: an
        annotation may not reference a concept nobody has defined, exactly as a
        Danus fact may not use a symbol with no definition in scope.
        """
        return sorted({cid for cid in ids if cid not in self.concepts})

    def validate_all(self) -> List[str]:
        problems: List[str] = []
        for concept in self.concepts.values():
            problems.extend(concept.validate())
        return problems


def suggest_id(label: str, name: str) -> str:
    """A stable, readable id from a concept's name: ``prop/right-continuous``."""
    slug = re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    return f"{ID_PREFIX.get(label, 'obj')}/{slug}"
