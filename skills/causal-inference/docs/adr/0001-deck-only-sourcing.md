# 0001 — Deck-only sourcing, stateless skills

Date: 2026-07-26
Status: accepted, sourcing rule superseded by
[0002](./0002-workshop-transcripts-as-source.md)

> **Amended 2026-07-28.** The sourcing decision below — decks only — was widened
> to admit the two workshop session transcripts. The stateless-skills decision
> and the consequences around it still stand. Several costs listed here have
> since been paid off; see 0002.

## Context

The `causal-inference` skill set audits the steps of a DoubleML analysis. Its value
rests entirely on whether its failure modes are trustworthy, so where they come
from is the central design question.

Available source material in this vault:

- **7 lecture PDFs** — the Economic AI DoubleML workshop decks (Feb/Mar 2026)
- **3 notebooks** — `tutorial.ipynb`, `roas.ipynb`, `panel_did_framework_dml_solution.ipynb`
- **~9 reference papers** — Chernozhukov et al. (2018), doubly robust estimation,
  GRF, causal random forest, and others
- **`causual model.md`** — this vault's own notes, including an analysis of bad
  control and near-instrument depletion via the erosion of $\mathrm{Var}(V)$
- general practitioner knowledge available to the agent

Separately: whether the skills share persistent state across steps. Most costly
DML errors are cross-step — a covariate admitted at the graph step inflates the
standard error at the inference step, with nothing locally wrong at either end.
Catching those mechanically requires a shared artifact the steps both write and
read.

## Decision

**Sources: the 7 lecture PDFs only.** Every failure mode carries `src: [Key] p.N`
pointing at a slide. Notebooks, reference papers, this vault's own notes, and
agent-supplied practitioner knowledge are all excluded.

**Gaps are silent.** Where the decks say nothing, the skills say nothing. No
"not covered" stubs, no placeholders.

**Skills are stateless, with a human in the loop.** No shared analysis document.
Each skill declares *Inputs required* (asks, never guesses) and *Carry forward*
(what the human hands to the next step). State lives in the human and the
conversation.

## Consequences

Accepted costs, in the order they will bite:

- **Bad control / near-instrument depletion is absent**, despite being the
  sharpest analysis in `causual model.md`. The mechanism — adding a strong
  predictor of $D$ that does not affect $Y$ leaves bias unchanged but shrinks
  $\mathrm{Var}(V)$, inflating $\mathrm{Var}(\hat\theta) \approx \mathrm{Var}(\varepsilon)/(n\,\mathbb{E}[V^2])$
  — is nowhere on a slide. A future reader will notice the omission; this is the
  reason.
- **Steps 2 and 5 are thin.** The data-backend step rests on one slide; the
  specification step's only traceable caveat is a single trimming recommendation
  in [Sens] p.35.
- **Practitioner traps are missing** — tuning before rather than inside
  cross-fitting, covariate selection under high-dimensional $X$, trimming
  threshold choice.
- **A passing check overstates.** Because gaps are silent, "no findings" means
  "nothing the decks warn about fired", not "this step is sound". Read verdicts
  accordingly.
- **Cross-step errors are the human's job.** The machinery cannot see them. The
  *Inputs required* / *Carry forward* blocks are the mitigation: step 8 asks for
  the step 1 covariate justification rather than deducing it.

Gained:

- Every line is checkable against a slide, in a domain where confident
  fabrication is both easy and expensive.
- The skills stay bounded to material actually studied, rather than drifting into
  a general causal-inference textbook.
- No document to keep in sync, and the skills work on someone else's analysis with
  zero setup.

## Alternatives considered

- **Decks + notebooks + this vault's notes**, tagged by tier. Would have kept the
  bad-control analysis. Rejected: widens the trust surface for material not
  covered in the workshop.
- **Everything including the reference papers.** Richest failure-mode lists, still
  cited. Rejected: paper-level caveats outrun what the workflow needs, and
  verification cost rises sharply.
- **Named gap stubs** listing missing topics with no content. Rejected in favour
  of silence; the ADR records the gaps instead.
- **A shared `analysis.md`** written and read by all nine steps, making cross-step
  contradictions catchable. Rejected: bookkeeping burden, and it presumes an
  analysis started from step 0 inside this system.

## Revisiting

Relaxing the sourcing rule means rewriting nine failure-mode lists and introducing
a second tier of `src:` tags. If that happens, do it as a deliberate pass over all
nine skills, not by adding untagged entries to one.
