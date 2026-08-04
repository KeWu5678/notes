---
description: Workflow map for the causal-inference skill set — nine numbered guardrails for a DoubleML analysis.
---

# Causal Inference — workflow map

Nine skills, one per step of a DoubleML analysis. Each is a **guardrail**, not a
pipeline stage: you invoke the one you are standing at, and it either **checks** a
deliverable you bring or **produces** that deliverable from your prompt. Nothing
advances on its own — the human decides when to move on.

This file is documentation, not a skill.

## The steps

| # | Skill | Deliverable |
|---|---|---|
| 0 | `causal-0-problem-formulation` | The causal question as an estimand: $Y$, $D$, population, and what the number will mean |
| 1 | `causal-1-causal-graph` | A DAG and the identification assumptions it commits you to — plus the "DML is the wrong tool" exit |
| 2 | `causal-2-data-backend` | A `DoubleMLData` / `DoubleMLPanelData` object with roles declared |
| 3 | `causal-3-model-class` | The `DoubleML*` model class and the estimand it targets |
| 4 | `causal-4-ml-methods` | Learners for the nuisance functions |
| 5 | `causal-5-dml-specification` | Score, `n_folds`, `n_rep`, trimming — the DML object |
| 6 | `causal-6-tuning` | Tuned hyperparameters via `tune_ml_models()` |
| 7 | `causal-7-estimation` | A fitted model, a coefficient, and learner diagnostics |
| 8 | `causal-8-inference` | Confidence intervals, joint inference, sensitivity analysis |

## Mapping to the lecture decks

The decks number the workflow 0–7. We use 0–8 because the deck's step 0 carries
two different jobs — stating the estimand and drawing the graph — and the deck's
step 2 "Causal Model" means the `DoubleML*` **class**, not the structural model.
Splitting them gives each guardrail one failure mode to police. See
[CONTEXT.md](./CONTEXT.md) for the term.

| Deck step ([Intro] p.29–39) | Our step |
|---|---|
| 0. Problem Formulation | 0 + 1 |
| 1. Data-Backend | 2 |
| 2. Causal Model | 3 |
| 3. ML Methods | 4 |
| 4. DML Specification | 5 |
| 5. Hyperparameter Tuning | 6 |
| 6. Estimation | 7 |
| 7. Inference | 8 |

## Sources

Every claim in every skill traces to the workshop material in
`DataScience/Problem: causal inference/DoubleML/lecture note/` — the seven lecture
PDFs, or the transcripts of the two sessions that presented them. Nothing else is
a source: not the notebooks, not the reference papers, not other notes in this
vault. See [docs/adr/0001-deck-only-sourcing.md](./docs/adr/0001-deck-only-sourcing.md)
for the original rule and what it leaves out, and
[docs/adr/0002-workshop-transcripts-as-source.md](./docs/adr/0002-workshop-transcripts-as-source.md)
for why the transcripts were added.

Citation keys used in the `src:` lines:

| Key | Deck | Locator |
|---|---|---|
| `[Intro]` | DoubleML - Introduction and Workflow | slide page |
| `[Recap]` | DoubleML - Recap | slide page |
| `[Sens]` | DoubleML - Sensitivity Analysis | slide page |
| `[DiD]` | DoubleML Difference-in-Differences | slide page |
| `[Tune]` | DoubleML Hyperparameter Tuning with Optuna | slide page |
| `[Het]` | DoubleML Multiple Treatment Levels and Treatment Effect Heterogeneity | slide page |
| `[Closing]` | Closing | slide page |
| `[D1]` | Workshop transcript, Day 1 (27 Feb 2026) | timestamp |
| `[D2]` | Workshop transcript, Day 2 (6 Mar 2026) | timestamp |

Page numbers are PDF pages, which match the slide footer numbers. Timestamps are
the nearest preceding `### hh:mm:ss` heading in the transcript file.

## Install

Each step folder is symlinked individually into `~/.claude/skills/`, same pattern
as `p-math`:

```bash
cd ~/Documents/Repos/notes/skills/causal-inference
for d in [0-8]-*; do
  ln -sfn "$PWD/$d" ~/.claude/skills/"causal-${d}"
done
```

Gives `/causal-0-problem-formulation` … `/causal-8-inference`. Edits in the vault
take effect immediately — the symlinks point at the working tree.

## Severity levels

| Level | Meaning |
|---|---|
| `[BLOCKER]` | Do not proceed to the next step until resolved |
| `[WARNING]` | Proceed if you accept it knowingly; record the decision |
| `[NOTE]` | Awareness only; no action forced |
