# stochgraph

Knowledge graph over `Math/stochana/lecture notes/StochAna.pdf`.

Files in `Math/stochana/graph/` are the source of truth. Neo4j is a derived index,
rebuilt from them — if the database is lost, rebuild it. See [DESIGN.md](DESIGN.md)
for the ontology and the reasoning behind it.

## Requirements

- Python 3.10+ (no third-party packages for stage 0)
- poppler (`pdftotext`, `pdftohtml`) — `brew install poppler`
- Docker, for Neo4j

## Use

All `make` targets run from this directory:

```sh
cd tools/stochgraph

make rebuild        # extract from the PDF, start Neo4j, load the graph
make browser        # open Neo4j Browser — http://localhost:7474, neo4j / stochgraph
make report         # what the last extraction produced
```

Or step by step:

```sh
make extract        # PDF -> Math/stochana/graph/  (no LLM, no network)
make up             # start Neo4j and wait for it
make load           # rebuild the graph from the vault files
make clean          # drop the database; vault files untouched
```

Chapters 1–3 (pages 5–86) are the current scope:

```sh
python3 -m stochgraph extract --first 5 --last 86
```

## Output

```
Math/stochana/graph/
  statements/01-01-04.md   one file per statement, YAML frontmatter + verbatim text
  manifest.json            counts, dangling refs, rejected anchors
  graph.cypher             generated Neo4j rebuild script
```

A statement file:

```yaml
---
id: s/1.1.4
label: Statement
ref: 1.1.4
provenance: verbatim
proved_here: true
cites: []
_kind: Proposition
_page: 6
---

## statement

If X and Y are modifications and all trajectories are left-continuous ...
```

Keys prefixed `_` are bookkeeping; everything else is mathematics or identity.

## Queries

`queries/views.cypher` holds the four views, to paste into Neo4j Browser: object
neighbourhood, statement dependency tree (and blast radius), chapter concept map,
and gaps. Some need the concept layer, which arrives with stage 1.

What a statement rests on, transitively:

```cypher
MATCH path = (s:Statement {ref: '3.3.6'})-[:CITES*1..6]->(dep:Statement)
RETURN path;
```

## Pipeline

```sh
python3 -m stochgraph extract              # stage 0 — mechanical, reads the PDF
python3 -m stochgraph task --section 1.2   # stage 1 — work order for a section
python3 -m stochgraph check                # stage 2 — concept coverage gate
python3 -m stochgraph build                # stages 3+4 — project, emit graph.cypher
```

`check` fails when an annotation references a concept the registry does not define.
`build` refuses to emit anything until it passes.

A stage-1 pass writes two things: new concepts into `concepts.json` (reusing existing
ids wherever possible — that reuse is the whole mechanism) and one annotation per
statement under `annotations/`. `seed_1_1.py` is the worked example for section 1.1.

## Status

- **Stage 0** — done for chapters 1–3: 155 statements, 27 `CITES`, 24 sections. All
  tier `verbatim`, read straight off the PDF.
- **Stages 1–3** — machinery built and exercised on **section 1.1 only**: 26 concepts
  (9 objects, 14 properties, 3 relations), 18 annotations, 29 projected edges.
  Sections 1.2 onward are not annotated.

The `CITES` count is low because the notes cite in prose as often as by link; the
explicit link DAG is ground truth but sparse, and stage 1 closes the gap.
