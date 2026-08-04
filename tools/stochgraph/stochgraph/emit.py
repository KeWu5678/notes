"""Write the statement layer to the vault as one markdown file per node.

The files are the source of truth; Neo4j is rebuilt from them (see ``cypher.py``).
That ordering is deliberate: a graph database is a binary blob with no diffs and
no review, whereas these files sit in git next to the notes they describe, so a
change to an extractor shows up as a reviewable diff on the affected statements.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, Iterable, List

from . import ontology
from .concepts import Registry
from .extract import Statement

# Refinement labels were collapsed for statements: `Theorem` vs `Lemma` is a
# rhetorical distinction, not an ontological one. Only `Definition` differs in
# kind — it introduces a concept rather than asserting something — so it is the
# one refinement kept. The source's own word survives as the `_kind` bookkeeping
# key, which citation text needs ("by Lemma 3.3.11") but no query traverses.
DEFINITION_KIND = "Definition"


def label_for(statement: Statement) -> str:
    return "Definition" if statement.is_definition else "Statement"


def _yaml_scalar(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if text == "" or re.search(r"[:#\"'\[\]{}|>*&!%@`]", text) or text != text.strip():
        return json.dumps(text, ensure_ascii=False)
    return text


def _yaml_list(values: Iterable[str]) -> str:
    return "[" + ", ".join(_yaml_scalar(v) for v in values) + "]"


def serialize(statement: Statement) -> str:
    """One statement as markdown with YAML frontmatter.

    Bookkeeping keys are ``_``-prefixed; everything unprefixed is either
    mathematics or the node's identity. The loader enforces that split, which is
    what keeps engineering vocabulary from leaking into the ontology.
    """
    lines = [
        "---",
        f"id: {_yaml_scalar(statement.node_id)}",
        f"label: {label_for(statement)}",
        f"ref: {_yaml_scalar(statement.ref)}",
        *([f"name: {_yaml_scalar(statement.name)}"] if statement.name else []),
        f"provenance: verbatim",
        f"proved_here: {_yaml_scalar(statement.proved_here)}",
        f"cites: {_yaml_list(statement.cites)}",
        f"cites_equations: {_yaml_list(statement.cites_equations)}",
        f"_kind: {_yaml_scalar(statement.kind)}",
        f"_chapter: {statement.chapter}",
        f"_section: {_yaml_scalar(statement.section)}",
        f"_page: {statement.page}",
        f"_region: {{page: {statement.page}, top: {statement.top}, "
        f"end_page: {statement.end_page}, end_top: {statement.end_top}}}",
        "---",
        "",
        "## statement",
        "",
        statement.text,
        "",
    ]
    return "\n".join(lines)


def statement_filename(statement: Statement) -> str:
    """A filename that sorts in reading order.

    Exercises are numbered globally rather than per chapter, so they are prefixed
    with their chapter to keep the directory in the order of the notes.
    """
    if statement.kind == "Exercise":
        return f"{statement.chapter:02d}-ex-{int(statement.ref):03d}.md"
    parts = statement.ref.split(".")
    padded = "-".join(f"{int(p):02d}" for p in parts)
    return f"{padded}.md"


def write_statements(statements: List[Statement], out_dir: Path) -> List[Path]:
    """Write one file per statement, replacing any previous extraction."""
    target = out_dir / "statements"
    target.mkdir(parents=True, exist_ok=True)
    for stale in target.glob("*.md"):
        stale.unlink()

    written: List[Path] = []
    for statement in statements:
        path = target / statement_filename(statement)
        path.write_text(serialize(statement), encoding="utf-8")
        written.append(path)
    return written


def write_manifest(statements: List[Statement], out_dir: Path, source: Path,
                   first_page: int, last_page: int,
                   rejected: List[Dict[str, str]] | None = None) -> Path:
    """A machine-readable summary of what stage 0 produced.

    Used by the loader and by review: it makes the size and shape of an
    extraction run visible without opening 133 files.
    """
    # Exercises are numbered globally ("Exercise 12") and are cited by that bare
    # number, so they belong in the known set alongside dotted statement refs.
    refs = {s.ref for s in statements}
    dangling = sorted(
        {c for s in statements for c in s.cites if c not in refs}
    )
    manifest = {
        "stage": 0,
        "source": source.name,
        "pages": [first_page, last_page],
        "provenance": "verbatim",
        "counts": {
            "statements": len(statements),
            "definitions": sum(1 for s in statements if s.is_definition),
            "exercises": sum(1 for s in statements if s.kind == "Exercise"),
            "proved_here": sum(1 for s in statements if s.proved_here),
            "cites": sum(len(s.cites) for s in statements),
            "cites_equations": sum(len(s.cites_equations) for s in statements),
        },
        # Citations pointing outside the extracted page range (forward references
        # into later chapters). Kept, not dropped: they are real edges of the
        # book, and the loader materialises them as out-of-scope stubs.
        "dangling_refs": dangling,
        # Link anchors poppler split mid-number. Reported, never turned into
        # edges: a wrong edge in the verbatim tier is worse than a missing one.
        "rejected_anchors": rejected or [],
        "by_kind": _count_by_kind(statements),
    }
    path = out_dir / "manifest.json"
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")
    return path


def _count_by_kind(statements: List[Statement]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for statement in statements:
        counts[statement.kind] = counts.get(statement.kind, 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: -kv[1]))


def write_concepts_md(registry: Registry, out_dir: Path,
                      defined_in: Dict[str, List[str]] | None = None) -> Path:
    """The concept registry as a readable table.

    `concepts.json` is what the loader reads; this is what a person reads. Kept
    generated rather than hand-maintained so the two cannot disagree.
    """
    defined_in = defined_in or {}
    lines = [
        "# Ontology and concepts",
        "",
        "Generated by `python -m stochgraph build` — do not edit. The schema comes "
        "from `stochgraph/ontology.py`, the concepts from `concepts.json`.",
        "",
        f"{len(registry.concepts)} concepts: "
        f"{len(registry.by_label('Object'))} objects, "
        f"{len(registry.by_label('Property'))} properties, "
        f"{len(registry.by_label('Relation'))} relations.",
        "",
        "---",
        "",
        "# Part 1 — the schema",
        "",
        "## Node labels",
        "",
        "| label | definition | examples |",
        "| --- | --- | --- |",
    ]
    for spec in ontology.NODE_LABELS:
        lines.append(f"| `:{spec.name}` | {spec.definition} | {spec.examples} |")

    lines += [
        "",
        "### Object refinements",
        "",
        "A second label on an `:Object`. `MATCH (o:Object)` still matches "
        "everything, so refinements can be added without breaking a query.",
        "",
        "| label | definition | examples |",
        "| --- | --- | --- |",
    ]
    for spec in ontology.OBJECT_REFINEMENTS:
        lines.append(f"| `:{spec.name}` | {spec.definition} | {spec.examples} |")

    for layer, title, blurb in (
        ("1", "Layer 1 — statement edges",
         "Extracted from the notes. Exact, provenance-bearing, and the "
         "justification for everything in layer 2."),
        ("2", "Layer 2 — concept edges",
         "Derived by projection from layer 1, never authored by hand. This is the "
         "layer you browse: one hop from an object to its neighbours."),
    ):
        lines += ["", f"## {title}", "", blurb, "",
                  "| edge | from → to | definition | keys |",
                  "| --- | --- | --- | --- |"]
        for spec in ontology.EDGE_TYPES:
            if spec.layer != layer:
                continue
            name = spec.name if spec.name.startswith("«") else f"`{spec.name}`"
            # A literal "|" in "Property | Relation" would end the table cell.
            ends = f"{spec.source} → {spec.target}".replace("|", "\\|")
            lines.append(
                f"| {name} | {ends} | {spec.definition} | {spec.keys} |"
            )

    lines += ["", "## Edge keys", "",
              "`_`-prefixed keys are bookkeeping; everything else is mathematics.",
              "", "| key | meaning |", "| --- | --- |"]
    for spec in ontology.EDGE_KEYS:
        lines.append(f"| `{spec.name}` | {spec.definition} |")

    lines += ["", "---", "", "# Part 2 — the concepts", ""]

    sections = [
        ("Objects", "Object", "things that exist"),
        ("Properties", "Property", "arity-1 predicates — what one object can satisfy"),
        ("Relations", "Relation", "arity-2 predicates — what holds between objects"),
    ]
    for title, label, gloss in sections:
        concepts = registry.by_label(label)
        lines += [f"## {title}", "", f"*{gloss}*", ""]
        if not concepts:
            lines += ["_none yet_", ""]
            continue
        lines += [
            "| id | name | symbol | kind | defined by | also known as |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for c in concepts:
            used = defined_in.get(c.id, [])
            where = c.defined_by or (used[0] if used else "")
            lines.append(
                f"| `{c.id}` | {c.name} | {c.symbol or ''} | {c.refine or ''} | "
                f"{where} | {', '.join(c.aliases)} |"
            )
        lines.append("")

    if registry.proposals:
        lines += ["## Review queue", "",
                  f"{len(registry.proposals)} proposals awaiting triage — see "
                  "`review/proposals.json`.", ""]

    path = out_dir / "CONCEPTS.md"
    body = "\n".join(lines)

    # Refuse to silently discard a hand edit. The file says "do not edit", but a
    # generated file that overwrites your work without a word is a trap, not a
    # contract — and the schema it renders lives in `ontology.py`, which is where
    # a change has to be made to reach the graph as well as the doc.
    stamp = out_dir / ".CONCEPTS.md.generated"
    if path.exists() and stamp.exists():
        if path.read_text(encoding="utf-8") != stamp.read_text(encoding="utf-8"):
            raise RuntimeError(
                f"{path} has been edited by hand; refusing to overwrite.\n"
                "  The schema is defined in stochgraph/ontology.py and the concepts "
                "in concepts.json — edit those, then rebuild.\n"
                f"  To discard your edits: rm {stamp}"
            )

    path.write_text(body, encoding="utf-8")
    stamp.write_text(body, encoding="utf-8")
    return path
