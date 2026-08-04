"""Build the Neo4j graph from the vault files.

Neo4j is a derived index, never the source of truth, so this emits a script that
drops and rebuilds the graph from scratch. A rebuild is cheap at this size and it
removes any possibility of the database drifting away from the files.

Only the statement layer exists at stage 0. The concept layer (`:Object`,
`:Property`, `:Relation`) and the projected object-to-object edges arrive with
stages 1-3; the constraints below are written now so the shape is fixed before
anything is inferred.
"""

from __future__ import annotations

from pathlib import Path
from typing import List

from .annotate import Annotation, ProjectedEdge
from .concepts import Registry
from .extract import Statement
from .emit import label_for

SCHEMA = """
// --- constraints -----------------------------------------------------------
// Identity is by `id` on every content node, so a rebuild is idempotent and a
// concept proposed twice under different names cannot silently become two nodes.
CREATE CONSTRAINT statement_id IF NOT EXISTS
  FOR (n:Statement) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT definition_id IF NOT EXISTS
  FOR (n:Definition) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT object_id IF NOT EXISTS
  FOR (n:Object) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT property_id IF NOT EXISTS
  FOR (n:Property) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT relation_id IF NOT EXISTS
  FOR (n:Relation) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT source_id IF NOT EXISTS
  FOR (n:Source) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT fact_id IF NOT EXISTS
  FOR (n:Fact) REQUIRE n.id IS UNIQUE;

// --- indexes ---------------------------------------------------------------
CREATE INDEX statement_ref IF NOT EXISTS FOR (n:Statement) ON (n.ref);
CREATE INDEX object_name IF NOT EXISTS FOR (n:Object) ON (n.name);
CREATE INDEX property_name IF NOT EXISTS FOR (n:Property) ON (n.name);
CREATE INDEX relation_name IF NOT EXISTS FOR (n:Relation) ON (n.name);
""".strip()


def _q(value: object) -> str:
    """Cypher literal."""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value).replace("\\", "\\\\").replace("'", "\\'")
    return f"'{text}'"


def concept_parts(registry: Registry, edges: List[ProjectedEdge],
                  annotations) -> List[str]:
    """Cypher for the concept layer and the derived object-to-object edges."""
    parts: List[str] = [
        "",
        "// --- concepts --------------------------------------------------------",
    ]
    for concept in sorted(registry.concepts.values(), key=lambda c: c.id):
        labels = f":{concept.label}"
        if concept.refine:
            # Refinement is a second label: `MATCH (o:Object)` must still match.
            labels += f":{concept.refine}"
        props = [f"id: {_q(concept.id)}", f"name: {_q(concept.name)}"]
        if concept.symbol:
            props.append(f"symbol: {_q(concept.symbol)}")
        if concept.arity:
            props.append(f"arity: {concept.arity}")
        if concept.aliases:
            props.append("aliases: [" + ", ".join(_q(a) for a in concept.aliases) + "]")
        parts.append(f"CREATE (n{labels} {{" + ", ".join(props) + "});")

    parts += ["", "// --- statement -> concept (layer 1) -----------------------------------"]
    for statement_id, annotation in sorted(annotations.items()):
        # Hypotheses declared per conclusion count as hypotheses of the statement:
        # without this, "which results assume left-continuity?" silently misses
        # every multi-part theorem, which is the exact failure the concept layer
        # exists to prevent.
        hypotheses = list(annotation.requires)
        for conclusion in annotation.concludes:
            hypotheses.extend(conclusion.given)
        for cid in dict.fromkeys(hypotheses):
            parts.append(_link(statement_id, cid, "REQUIRES"))
        for cid in annotation.about:
            parts.append(_link(statement_id, cid, "ABOUT"))
        for cid in annotation.defines:
            parts.append(_link(statement_id, cid, "DEFINES"))
        for conclusion in annotation.concludes:
            extra = ""
            if conclusion.negated:
                extra = " {negated: true}"
            parts.append(
                _link(statement_id, conclusion.predicate, "CONCLUDES", extra)
            )

    parts += [
        "",
        "// --- reified facts (only where an edge must end on an assertion) ------",
    ]
    for statement_id, annotation in sorted(annotations.items()):
        for fact in annotation.facts:
            fid = fact.node_id(statement_id)
            props = [f"id: {_q(fid)}"]
            if fact.gloss:
                props.append(f"gloss: {_q(fact.gloss)}")
            if fact.negated:
                props.append("negated: true")
            parts.append("CREATE (:Fact {" + ", ".join(props) + "});")
            parts.append(
                f"MATCH (f:Fact {{id: {_q(fid)}}}), (p {{id: {_q(fact.predicate)}}}) "
                f"CREATE (f)-[:PREDICATE]->(p);"
            )
            for i, arg in enumerate(fact.args, start=1):
                parts.append(
                    f"MATCH (f:Fact {{id: {_q(fid)}}}), (a {{id: {_q(arg)}}}) "
                    f"CREATE (f)-[:ARG {{i: {i}}}]->(a);"
                )
            parts.append(
                f"MATCH (s:Statement {{id: {_q(statement_id)}}}), "
                f"(f:Fact {{id: {_q(fid)}}}) CREATE (s)-[:CONCLUDES]->(f);"
            )
        for eq in annotation.equivalences:
            left = next(f for f in annotation.facts if f.local == eq.left)
            right = next(f for f in annotation.facts if f.local == eq.right)
            props = [f"_via: {_q(statement_id)}"]
            if eq.under:
                props.append("under: [" + ", ".join(_q(u) for u in eq.under) + "]")
            parts.append(
                f"MATCH (a:Fact {{id: {_q(left.node_id(statement_id))}}}), "
                f"(b:Fact {{id: {_q(right.node_id(statement_id))}}}) "
                f"CREATE (a)-[:EQUIVALENT {{" + ", ".join(props) + "}]->(b);"
            )

    parts += [
        "",
        "// --- layer 2: derived concept-to-concept edges ------------------------",
        "// Generated by projection from layer 1. `_via` is the justifying",
        "// statement; `under` lists the other hypotheses as Property ids.",
    ]
    for edge in edges:
        props = [f"_via: {_q(edge.via)}"]
        if edge.under:
            props.append("under: [" + ", ".join(_q(u) for u in edge.under) + "]")
        parts.append(
            f"MATCH (a {{id: {_q(edge.source)}}}), (b {{id: {_q(edge.target)}}}) "
            f"CREATE (a)-[:{edge.type} {{" + ", ".join(props) + "}]->(b);"
        )
    return parts


def _link(statement_id: str, concept_id: str, rel: str, extra: str = "") -> str:
    return (
        f"MATCH (s:Statement {{id: {_q(statement_id)}}}), "
        f"(c {{id: {_q(concept_id)}}}) CREATE (s)-[:{rel}{extra}]->(c);"
    )


def build_script(statements: List[Statement], first_page: int, last_page: int,
                 registry: Registry | None = None,
                 annotations=None,
                 edges: List[ProjectedEdge] | None = None) -> str:
    """The full rebuild script: wipe, constrain, create nodes, then edges."""
    parts: List[str] = [
        "// Generated by stochgraph — do not edit.",
        "// Source of truth is Math/stochana/graph/; rebuild rather than patch.",
        "",
        "MATCH (n) DETACH DELETE n;",
        "",
        SCHEMA,
        "",
        "// --- sections --------------------------------------------------------",
    ]

    sections = sorted({s.section for s in statements if s.section})
    for section in sections:
        parts.append(
            f"CREATE (:Source {{id: {_q('sec/' + section)}, "
            f"section: {_q(section)}}});"
        )

    parts += ["", "// --- statements ------------------------------------------------------"]
    for statement in statements:
        label = label_for(statement)
        # `:Definition` also carries `:Statement`: Neo4j labels are flat, so the
        # stable layer has to be attached explicitly or `MATCH (s:Statement)`
        # would miss every definition.
        labels = ":Statement:Definition" if label == "Definition" else ":Statement"
        # Only what a query or a reader uses. The vault files keep the full
        # record (section, chapter, page region) — detail is free there and noise
        # here, where every property shows up in the browser's node panel.
        # `_section` is redundant with the IN edge, `_chapter` is the head of
        # `ref`, and `provenance` is omitted while it equals the default, so an
        # agent-written node will stand out the moment one exists.
        props = [f"id: {_q(statement.node_id)}", f"ref: {_q(statement.ref)}"]
        if statement.name:
            props.append(f"name: {_q(statement.name)}")
        props += [
            f"_kind: {_q(statement.kind)}",
            f"_page: {statement.page}",
            f"proved_here: {_q(statement.proved_here)}",
            f"statement_text: {_q(statement.text)}",
        ]
        parts.append(f"CREATE (n{labels} {{" + ", ".join(props) + "});")

    parts += ["", "// --- statement -> section --------------------------------------------"]
    for statement in statements:
        if not statement.section:
            continue
        parts.append(
            f"MATCH (s:Statement {{id: {_q(statement.node_id)}}}), "
            f"(sec:Source {{id: {_q('sec/' + statement.section)}}}) "
            f"CREATE (s)-[:IN]->(sec);"
        )

    parts += [
        "",
        "// --- citations -------------------------------------------------------",
        "// Out-of-scope targets (forward references into chapters not yet",
        "// extracted) become stubs rather than being dropped, so the DAG stays",
        "// honest about what the book actually cites.",
    ]
    known = {s.ref for s in statements if s.kind != "Exercise"}
    known_ex = {s.ref for s in statements if s.kind == "Exercise"}
    stubs: List[str] = []
    for statement in statements:
        for ref in statement.cites:
            if ref in known:
                target = f"s/{ref}"
            elif ref in known_ex:
                target = f"ex/{ref}"
            else:
                target = f"s/{ref}"
                if target not in stubs:
                    stubs.append(target)
            parts.append(
                f"MATCH (a:Statement {{id: {_q(statement.node_id)}}}), "
                f"(b:Statement {{id: {_q(target)}}}) CREATE (a)-[:CITES]->(b);"
            )

    if stubs:
        insert = parts.index(
            "// --- citations -------------------------------------------------------"
        )
        stub_lines = [
            f"CREATE (:Statement {{id: {_q(sid)}, ref: {_q(sid.split('/')[1])}, "
            f"_out_of_scope: true}});"
            for sid in stubs
        ]
        parts[insert:insert] = ["", "// --- out-of-scope citation targets -----------------------------------"] + stub_lines

    if registry and registry.concepts:
        parts += concept_parts(registry, edges or [], annotations or {})

    return "\n".join(parts) + "\n"


def write_script(statements: List[Statement], out_dir: Path,
                 first_page: int, last_page: int,
                 registry: Registry | None = None,
                 annotations=None,
                 edges: List[ProjectedEdge] | None = None) -> Path:
    path = out_dir / "graph.cypher"
    path.write_text(
        build_script(statements, first_page, last_page, registry, annotations, edges),
        encoding="utf-8",
    )
    return path
