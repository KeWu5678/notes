---
name: causal-5-dml-specification
description: Set or audit the DML object's estimation settings — n_folds, n_rep, cross-fitting, propensity trimming, random seed — when instantiating a DoubleML model. Use when constructing DoubleMLIRM / DoubleMLPLR / DoubleMLDIDMulti with its learners, when choosing how many folds or repetitions to cross-fit over, or when propensity scores are making results unstable.
---

# 5. DML specification

**Deliverable** — the instantiated `DoubleML*` object: data backend, learners, and
the sample-splitting settings, fixed and recorded.

This step is thin by design. The decks specify the object and give a short list of
general recommendations; that is what is here.

## Inputs required

Ask for these; do not guess:

1. From step 3: the model class and, for DiD, `control_group` and
   `anticipation_periods`.
2. From step 4: the learner objects.
3. From step 1: any overlap problem found — it decides trimming.
4. Whether results need to be reproducible across runs.

## Procedure

1. **Instantiate the model** with the data backend and the learners.
   `src: [Intro] p.33`

   ```python
   import numpy as np
   from doubleml import DoubleMLIRM

   np.random.seed(42)
   dml_irm_rf = DoubleMLIRM(
       dml_data,
       ml_g=ml_l_rf,
       ml_m=ml_m_rf,
   )
   ```

   For panel DiD, the same step carries the design choices from step 3:
   `src: [DiD] p.34`

   ```python
   from doubleml.did import DoubleMLDIDMulti

   dml_obj = DoubleMLDIDMulti(
       dml_panel_data,
       ml_g=pipeline_g,
       ml_m=pipeline_m,
       gt_combinations="standard",
       control_group="never_treated",
       n_folds=5,
   )
   ```

2. **Confirm cross-fitting is in force.** Split into $K$ folds; for each fold, train
   the learners on the others and predict on the held-out fold; combine the
   out-of-sample predictions for the causal estimation. Predictions are then always
   out-of-sample, all data is used for both training and estimation, and it is more
   efficient than a single train/test split. `src: [Intro] p.24, [Recap] p.17`
3. **Apply the general recommendations:** `src: [Sens] p.35`
   - repeat the cross-fitting procedure several times — `n_rep`
   - use multiple folds — `n_folds`
   - in the IRM, propensity score predictions can render results unstable, so
     propensity score trimming may help
4. **Set a seed** if the run needs to be reproducible. `src: [Intro] p.33`

## Failure modes

### Cross-fitting bypassed `[BLOCKER]`
- **Symptom** Nuisance functions fitted on the full sample and the predictions
  reused for the causal estimation; or a hand-rolled single train/test split.
- **Why** Using the same data for ML fitting and causal estimation creates bias —
  overfitting errors become correlated with the estimation errors. Sample splitting
  at the stage of producing $\hat\theta_0$ is one of the three DML ingredients.
- **Fix** Use the model class's own cross-fitting.
- `src: [Intro] p.24, [Recap] p.17`

### Single cross-fitting repetition `[WARNING]`
- **Symptom** `n_rep` left at one; the estimate is reported from a single random
  fold assignment.
- **Why** The recommendation is to repeat the cross-fitting procedure several
  times, so the result does not depend on one particular split.
- **Fix** Raise `n_rep` and report across repetitions.
- `src: [Sens] p.35`

### Too few folds `[WARNING]`
- **Symptom** `n_folds` at 2, or unstated.
- **Why** The recommendation is to use multiple folds; the DiD example uses
  `n_folds=5`.
- **Fix** Set it explicitly and record the value.
- `src: [Sens] p.35, [DiD] p.34`

### No trimming despite unstable propensities `[WARNING]`
- **Symptom** An IRM fit where the propensity scores are extreme, or where step 1
  already flagged an overlap problem, and no trimming is applied. Also fires on a
  small sample with a boosted `ml_m`, whose predictions crowd 0 and 1 whether or
  not overlap genuinely fails.
- **Why** In the IRM, the propensity score predictions can render results — and
  the sensitivity analysis at step 8 — unstable. The score divides by
  $\hat m(X)$ and $1 - \hat m(X)$, so extreme predictions give a few observations
  extreme weight.
- **Fix** Apply propensity score trimming. Record the threshold — step 8 reports it
  alongside the estimate. Distinguish the two causes: genuine non-overlap is a
  step 1 problem that trimming redefines rather than solves, while a poorly
  calibrated learner is a step 4 problem.
- `src: [Sens] p.35, [D1] 00:57`

### Seed not set `[NOTE]`
- **Symptom** No `np.random.seed(...)`; fold assignment and learner randomness vary
  run to run.
- **Why** The worked examples set a seed before instantiating the model.
- **Fix** Set one, and record it alongside the estimate.
- `src: [Intro] p.33`

## Check mode — report format

```
**VERDICT** — n blockers, m warnings        (PASS | PROCEED WITH CAUTION | BLOCKED)

① <failure mode>                    [SEVERITY]
   observed   <what in the deliverable triggered it>
   fix        <what to do about it>

**Carry forward to step 6**
 • <facts step 6 needs>
```

Report only the modes that fired, most severe first.

## Carry forward to step 6 (`causal-6-tuning`)

- The instantiated object, with `n_folds`, `n_rep` and the seed recorded
- The trimming decision and threshold, if any — step 8 must report it
- Which learners are to be tuned
- The model's `params_names`, if already known (e.g. `ml_g0`, `ml_g1`, `ml_m`)

## Output style

Report in **Unicode math**, never LaTeX — write θ̂₀, m(X), K folds, n_rep, n_folds,
not `\hat\theta` or `$...$`. The LaTeX in this file is for reading it in Obsidian; it
must not appear in your output. Define every symbol on first use. Bold the verdict.
Keep it short.
