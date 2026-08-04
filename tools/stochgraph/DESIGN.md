# stochgraph — design

A knowledge graph over *Stochastic Analysis* (Ulrich Horst, HU Berlin, Summer 2026),
built to be queried by an agent and read by a human.

## Purpose

**Dependency reasoning first:** *what may I cite to prove X; what breaks if lemma L
is wrong.* Precise retrieval follows from it — a question about reasoning is a
traversal, and traversal is exact where vector similarity is approximate. Study and
gap-finding come from the visualization. Formalization is kept cheaply possible
(verbatim text plus explicit hypotheses is what it would need, and what dependency
reasoning needs anyway) but is not designed for.

## Ontology

Four content labels, plus `:Source` for provenance. The reduction that gets us
there: a property is a unary relation; an external result is a statement with no
proof; a numbered equation is a statement written in symbols.

| label | is | examples |
| --- | --- | --- |
| `:Object` | a thing that exists | M, L(M), L₀, L̄(M), ⟨M⟩, Wiener measure, ℙ_M, the isometry I, (F_t) |
| `:Property` | arity-1 predicate | continuous, adapted, L²-bounded, predictable, uniformly integrable |
| `:Relation` | arity ≥2 predicate | modification, indistinguishable, subset of, dense in, isometric |
| `:Statement` | an assertion, with provenance | every numbered environment |
| `:Definition` | introduces a concept | also carries `:Statement` |

`:Object` takes an optional second label (`:FunctionSpace`, `:Process`, `:Measure`,
`:Map`, `:SigmaField`, `:Structure`). Statements take none: theorem vs lemma vs
proposition is a rhetorical distinction, not an ontological one, so the source's word
survives only as the `_kind` bookkeeping key. `:Definition` is the one exception —
it introduces rather than asserts.

Neo4j labels are flat, so `:Definition` carries `:Statement` explicitly; nothing is
inherited for free.

## Two layers

**Layer 1 — statements.** Exact, provenance-bearing, the justification for
everything else.

`CITES` · `REQUIRES` · `CONCLUDES` · `DEFINES` · `ABOUT` · `IN`

**Layer 2 — objects.** What you browse: one hop from L² to its neighbours. One edge
type per `:Relation` node, so `DENSE_IN` the edge corresponds to
`(:Relation {name:"dense in"})` the concept — an invariant the loader checks. These
edges are *derived by projection from layer 1*, never hand-authored.

Relation-to-relation structure lives among the `:Relation` nodes:
`(:Relation {name:"dense in"})-[:IMPLIES]->(:Relation {name:"subset of"})`, stated
once and inherited by traversal.

**Why statements are nodes.** Prop 1.1.4 has two hypotheses and one conclusion — a
3-place fact. An edge has two endpoints, so an edge-only encoding must demote a
hypothesis to a string property, where it is unqueryable. Edges are binary;
theorems are n-ary. The statement node is where the conjunction lives.

**Why relation *instances* are not reified.** The statement node already is that
reification. A separate `:RelationInstance` would say the same thing twice.

The cost, accepted deliberately: `REQUIRES → (:Relation {name:"modification"})` does
not record *between which* objects the relation holds. The verbatim text retains it.

### Bound and unbound conclusions

Implementation forced one refinement. A conclusion is **bound** when its arguments
are named concepts ("Brownian motion has independent increments") and **unbound**
when they are the statement's own variables ("X and Y are modifications"). Inventing
nodes for bound variables would fill the graph with per-theorem noise, so:

- bound conclusion  → object-level edge (`HAS_PROPERTY`, `DENSE_IN`, …)
- unbound conclusion → predicate-level `IMPLIES` from each hypothesis, carrying the
  remaining hypotheses in `under`

That second rule is how "modifications + left-continuous paths implies
indistinguishable" reaches layer 2 at all.

Each conclusion also carries its own `given` hypotheses. A multi-part result
("i) … ii) …") proves several implications with different antecedents, and a single
statement-level `requires` would wrongly merge them. Those per-conclusion hypotheses
still emit statement-level `REQUIRES` edges, or "which results assume
left-continuity?" would miss every multi-part theorem.

A disjunctive hypothesis ("left-continuous *or* right-continuous") is recorded as two
conclusions rather than a third invented property.

## Key discipline

`_`-prefixed keys are bookkeeping; there is exactly one, `_via`, the ref of the
justifying statement. Everything unprefixed is mathematics, declared per relation
type, and the loader fails the build on an undeclared key.

- `under[]` holds **typed refs to `:Property` nodes**, never prose. It is a
  denormalization for browsing; the queryable form is the statement's `REQUIRES`
  edges. Layer 2 is lossy by construction, layer 1 is exact.
- **No `polarity`.** Negation is its own relation, matching notation: ⊆ / ⊄, = / ≠.
  Remark 4.2.6 ("definitely not true in general that L̄(M) = L(M)") becomes a
  `NOT_EQUALS` edge. A graph that cannot say the converse fails will let an agent
  derive it.
- **No `derived` flag.** Every layer-2 edge is derived, so the flag says nothing.

### Files carry detail; the graph carries what is used

The two stores have different economics. Detail in the vault files is free — nobody
reads them raw. Every property loaded into Neo4j appears in the browser's node panel,
so it is noise unless a query or a reader uses it.

A key is therefore loaded only if it earns its place:

| kept | why |
| --- | --- |
| `id`, `ref` | identity, and what a citation names |
| `_kind` | you cite "Lemma 3.3.11", not "statement 3.3.11" |
| `_page` | the jump back to the PDF |
| `proved_here` | the gaps view depends on it |
| `statement_text` | the content itself |

Dropped from the graph, retained in the files: `_section` (redundant with the `IN`
edge), `_chapter` (the head of `ref`), `_top` and the region rectangle (only needed
to crop the page, which nothing does yet). `provenance` is written only when it
differs from `verbatim`, so the first agent-written node stands out instead of
hiding among 155 identical labels.

Nothing is lost: page and ref locate any statement in the PDF in seconds, and the
full record stays in `statements/*.md`.

## Trust

Files in the vault are the source of truth; Neo4j is rebuilt from them. A graph
database is a binary blob with no diffs and no review; these files sit in git beside
the notes they describe.

Fully writable, gated by **provenance tiers** rather than a verifier:
`verbatim` (read off the PDF) / `user` / `agent`, each with a source anchor, plus
cascade revocation. The invariant: **proofs cite only the verbatim and user tiers.**

`statement_text` is tier `verbatim`; LLM-produced LaTeX will be tier `transcribed`
and carried *alongside* it, never replacing it, with the page region anchor kept so a
bad transcription is always checkable against the original pixels.

Unmappable content is flagged into a review queue, never dropped.

## Pipeline

| stage | how | output |
| --- | --- | --- |
| 0 | mechanical | statements with ref/kind/page/verbatim text; `CITES` from PDF link annotations; `:Source` |
| 1 | LLM, per section | `REQUIRES`/`CONCLUDES`/`DEFINES`/`ABOUT` → candidate concepts |
| 2 | growing registry | reuse-or-propose against `concepts.yaml`; proposals to a review queue; coverage check fails the build on an unresolvable concept |
| 3 | projection | layer-2 edges with `under[]`, `_via` |
| 4 | loader | Neo4j rebuild + ontology checks |

Scope: chapters 1–3 (pages 5–86), run as three sequential passes with review between,
since chapter 1's vocabulary is what makes chapter 2 cheap. Source is the PDF only —
the lecture transcripts are speech and are excluded.

### What stage 0 exploits

Three exact typographic signals, no inference:

- **Declarations** are runs in the bold theorem font (`CMBX10`). 273 across the book,
  with no in-text "…follows from Theorem 4.2.2" misread as a declaration.
- **Statement extent** is the italic (`CMTI10`) run block following the header; the
  notes set statement bodies in italic and narrative, proofs and headings in roman.
  This is what keeps multi-part statements ("i) … ii) …") and trailing display
  formulas whole.
- **Citations** are real PDF link annotations, so the DAG is ground truth.

Two views of the PDF are needed because neither suffices alone: `pdftotext -layout`
has the reading order, `pdftohtml -xml` has the fonts, positions and links.

Known limits, by design:
- Symbols flatten in the text layer (`M_t²` → `Mt2`). Prose is verbatim.
- The explicit link DAG is **high precision, low recall** — about 0.2 edges per
  statement in chapters 1–3, because mathematicians cite in prose ("by Doob's
  maximal inequality", with no link). Stage 1 closes that gap.
- Anchors that poppler split mid-number are **rejected and reported**, never turned
  into edges: a wrong edge in the verbatim tier is worse than a missing one.

## Relation to Danus

`math-agent/Danus/danus/core` solves an adjacent problem (a research agent's memory)
with files, not a graph: local JSONL scratch → typed findings → a content-addressed
fact DAG with one edge type (`predecessors`), cascade revoke, and a BM25 index
rebuilt on demand.

**Adopted:** the layered glossary with a coverage check (becomes the concept
registry); the invariant that you may only build on the trusted tier; cascade
revocation; files as truth with the index rebuilt on demand; *wrap only what the LLM
cannot do reliably* (which is why an MCP tool is deferred until the recurring queries
are known).

**Improved on:** Danus has one edge type and no ontology — adequate for a research
log, useless for "which theorems assume left-continuity". We add typed concepts,
first-class negation, and a browse/exact split. Our provenance is *mechanical*,
extracted from link annotations, where every Danus fact is agent-authored.

**Deliberately different:** no verifier gate. Danus needs one because it produces
novel mathematics. We transcribe a published course, where the failure mode is
misextraction, not false mathematics — provenance plus a source anchor catches that
at a fraction of the cost.

## Open

- **The write path.** Fully writable, files-as-truth and Neo4j-as-derived together
  imply agent writes go to files and trigger a rebuild. The mechanics (incremental
  vs full rebuild, the shape of the write tool) are not designed.
- **Exercises** are `:Statement` with `proved_here: false` — asserted, proof absent.
  34 of the 155 in chapters 1–3.
