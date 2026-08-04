"""stochgraph — build the knowledge graph for the stochastic analysis notes.

    python -m stochgraph extract [--first 5] [--last 86]   stage 0, mechanical
    python -m stochgraph task --section 1.1                 stage 1 work order
    python -m stochgraph check                              stage 2 coverage check
    python -m stochgraph build                              stages 0+3+4 -> graph.cypher
    python -m stochgraph report

``extract`` reads the PDF; nothing else does. ``check`` is the gate: it fails when an
annotation references a concept the registry does not define, which is what keeps the
concept layer from filling up with near-duplicates nobody can query.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .annotate import load_annotations, project
from .concepts import Registry
from .cypher import write_script
from .emit import write_concepts_md, write_manifest, write_statements
from .extract import load

REPO = Path(__file__).resolve().parents[3]
PDF = REPO / "Math" / "stochana" / "lecture notes" / "StochAna.pdf"
GRAPH = REPO / "Math" / "stochana" / "graph"

# Chapters 1-3 of the notes: printed pages 5-86 (chapter 4 opens on page 87).
DEFAULT_FIRST, DEFAULT_LAST = 5, 86


def _statements(args: argparse.Namespace):
    statements, rejected = load(Path(args.pdf), args.first, args.last)
    return statements, rejected


def cmd_extract(args: argparse.Namespace) -> int:
    pdf, out = Path(args.pdf), Path(args.out)
    if not pdf.exists():
        print(f"error: source PDF not found: {pdf}", file=sys.stderr)
        return 1

    statements, rejected = _statements(args)
    if not statements:
        print("error: no statements extracted — check the page range", file=sys.stderr)
        return 1

    out.mkdir(parents=True, exist_ok=True)
    written = write_statements(statements, out)
    manifest = write_manifest(statements, out, pdf, args.first, args.last, rejected)

    counts = json.loads(manifest.read_text())["counts"]
    print(f"stage 0: pages {args.first}-{args.last} of {pdf.name}")
    print(f"  {counts['statements']} statements "
          f"({counts['definitions']} definitions, {counts['exercises']} exercises)")
    print(f"  {counts['cites']} CITES edges, "
          f"{counts['cites_equations']} equation references")
    print(f"  {len(written)} files -> {out.relative_to(REPO)}/statements/")
    if rejected:
        print(f"  {len(rejected)} unresolvable anchors -> manifest.json")
    return 0


def cmd_task(args: argparse.Namespace) -> int:
    """Print the stage-1 work order for one section.

    Deliberately a printed brief rather than an API call: the extraction is done
    by whichever agent is driving, and the registry it must reuse has to be in
    front of it. Reuse is the whole mechanism — a concept proposed afresh in each
    section is how the layer silently fragments.
    """
    statements, _ = _statements(args)
    section = args.section
    scoped = [s for s in statements if s.section == section]
    if not scoped:
        print(f"error: no statements in section {section}", file=sys.stderr)
        return 1

    registry = Registry.load(Path(args.out))
    print(f"# stage 1 — section {section} ({len(scoped)} statements)\n")
    print("## registry (reuse these ids; propose only what is genuinely new)\n")
    if registry.concepts:
        for concept in sorted(registry.concepts.values(), key=lambda c: c.id):
            alias = f"  aliases: {concept.aliases}" if concept.aliases else ""
            print(f"  {concept.id:<44} {concept.label:<8} {concept.name}{alias}")
    else:
        print("  (empty — this is the first pass)")

    print("\n## statements\n")
    for statement in scoped:
        print(f"### {statement.node_id}  [{statement.kind} {statement.ref}, "
              f"p{statement.page}, proved_here={statement.proved_here}]")
        if statement.name:
            print(f"name: {statement.name}")
        print(statement.text)
        print()
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    """The coverage gate: every referenced concept must exist."""
    out = Path(args.out)
    registry = Registry.load(out)
    annotations = load_annotations(out)

    problems = registry.validate_all()
    for annotation in annotations.values():
        problems.extend(annotation.validate(registry))

    print(f"registry: {len(registry.concepts)} concepts "
          f"({len(registry.by_label('Object'))} objects, "
          f"{len(registry.by_label('Property'))} properties, "
          f"{len(registry.by_label('Relation'))} relations)")
    print(f"annotations: {len(annotations)} statements")
    if registry.proposals:
        print(f"review queue: {len(registry.proposals)} proposals")

    if problems:
        print(f"\nFAILED — {len(problems)} problem(s):", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1
    print("\nok — every referenced concept resolves")
    return 0


def cmd_build(args: argparse.Namespace) -> int:
    """Stage 0 + stage 3 projection + stage 4 script, gated by the check."""
    out = Path(args.out)
    statements, rejected = _statements(args)
    registry = Registry.load(out)
    annotations = load_annotations(out)

    problems = registry.validate_all()
    for annotation in annotations.values():
        problems.extend(annotation.validate(registry))
    if problems:
        print("error: build blocked by the coverage check — run `check`",
              file=sys.stderr)
        for problem in problems[:10]:
            print(f"  {problem}", file=sys.stderr)
        return 1

    # `_via` carries the statement's node id, not its bare ref: an exercise's ref
    # is just "1", which says nothing on an edge and resolves to nothing.
    refs = {s.node_id: s.node_id for s in statements}
    edges = project(annotations, registry, refs)
    write_statements(statements, out)
    write_manifest(statements, out, Path(args.pdf), args.first, args.last, rejected)
    script = write_script(statements, out, args.first, args.last,
                          registry, annotations, edges)
    concepts_md = write_concepts_md(registry, out)

    print(f"build: {len(statements)} statements, {len(registry.concepts)} concepts, "
          f"{len(annotations)} annotated, {len(edges)} projected edges")
    print(f"  -> {script.relative_to(REPO)}")
    print(f"  -> {concepts_md.relative_to(REPO)}")
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    path = Path(args.out) / "manifest.json"
    if not path.exists():
        print("error: no manifest — run `extract` first", file=sys.stderr)
        return 1
    print(path.read_text().rstrip())
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="stochgraph", description=__doc__)
    parser.add_argument("--pdf", default=str(PDF), help="source PDF")
    parser.add_argument("--out", default=str(GRAPH), help="graph directory in the vault")
    parser.add_argument("--first", type=int, default=DEFAULT_FIRST)
    parser.add_argument("--last", type=int, default=DEFAULT_LAST)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("extract", help="stage 0 — mechanical extraction").set_defaults(
        func=cmd_extract)

    task = sub.add_parser("task", help="stage 1 — print a section's work order")
    task.add_argument("--section", required=True)
    task.set_defaults(func=cmd_task)

    sub.add_parser("check", help="stage 2 — concept coverage gate").set_defaults(
        func=cmd_check)
    sub.add_parser("build", help="stages 0+3+4 — emit graph.cypher").set_defaults(
        func=cmd_build)
    sub.add_parser("report", help="summarise the last extraction").set_defaults(
        func=cmd_report)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
