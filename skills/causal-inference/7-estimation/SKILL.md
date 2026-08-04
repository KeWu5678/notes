---
name: causal-7-estimation
description: Run or audit the fit itself — fit(), coef, se, summary, print() and evaluate_learners() — and check the fitted object reports what was intended. Use after calling fit() on a DoubleML model, when reading a coefficient and standard error off a DML summary, or when nuisance learner performance needs to be verified before the result is trusted.
---

# 7. Estimation

**Deliverable** — a fitted model, a coefficient with its standard error, and the
learner diagnostics that say whether the fit is worth reading.

What this step cannot tell you is whether the design was right. A fit completes
and returns a number under a violated identification assumption exactly as it
does under a satisfied one. `src: [D2] 02:45–02:46`

## Inputs required

Ask for these; do not guess:

1. From step 3: the model class, its score, and the target estimand.
2. From step 5: `n_folds`, `n_rep`, trimming, seed.
3. From step 6: what was tuned and the best scores.
4. The output of `print(model)` and `model.evaluate_learners()`.

If the learner evaluation is not supplied, ask for it. The coefficient alone is not
enough to judge the fit.

## Procedure

1. **Fit** and read the coefficient. `src: [Intro] p.35`

   ```python
   dml_irm_rf.fit()
   dml_irm_rf.coef              # array([8135.69243711])
   dml_irm_rf.se                # array([1113.93596101])
   dml_irm_rf.summary.round(2)  # coef, std err, t, P>|t|, 2.5 %, 97.5 %
   ```

2. **Print the object** and check every block against what was decided upstream:
   `src: [Intro] p.36`
   - *Data Summary* — outcome, treatment, covariates, instruments, observations
   - *Score & Algorithm* — the score function (e.g. `ATE`); for DiD also the control
     group, anticipation periods, treatment group and pre/evaluation periods
     `src: [DiD] p.36, p.39`
   - *Machine Learner* — the learners actually used, with their hyperparameters
3. **Evaluate the learners** out-of-sample. `src: [Intro] p.37`

   ```python
   print(dml_irm_rf.evaluate_learners())
   # {'ml_g0': array([[47704.17]]), 'ml_g1': array([[63905.21]]), 'ml_m': array([[0.44310813]])}
   ```

   Compare against the untuned baseline if one exists — the deck's tuned run
   improves every component. `src: [Tune] p.13`
4. **Interpret the sampling error.** Under regularity conditions the estimator
   concentrates in a $1/\sqrt{N}$ neighbourhood of $\theta_0$ with
   $$
   \sqrt{N}(\tilde\theta_0 - \theta_0) \sim N(0, \sigma^2),
   $$
   where $\sigma^2 = J_0^{-2}\,\mathbb{E}[\psi^2(W;\theta_0,\eta_0)]$ and
   $J_0 = \mathbb{E}[\psi^a(W;\eta_0)]$. `src: [Intro] p.25, [Recap] p.18`

## Failure modes

### Learner performance never evaluated `[BLOCKER]`
- **Symptom** A coefficient reported with no `evaluate_learners()` output and no
  other out-of-sample metric.
- **Why** The estimate's validity rests on the nuisance functions being estimated
  well enough. Learner evaluation is the additional diagnostic the workflow calls
  for, and it is the only visible evidence on that.
- **Fix** Run `evaluate_learners()`; read it next to the estimate.
- `src: [Intro] p.23, p.37`

### Printed score does not match the target estimand `[BLOCKER]`
- **Symptom** `Score function:` in the printed object differs from what step 3
  recorded — e.g. `ATE` where ATTE was intended.
- **Why** The score defines what the coefficient estimates. A mismatch means the
  number answers a different question than the one asked at step 0.
- **Fix** Re-specify the model with the intended score and refit.
- `src: [Intro] p.36`

### Printed data summary disagrees with steps 1–2 `[BLOCKER]`
- **Symptom** The covariate list, treatment variable or observation count in the
  printed summary differs from what was declared — a column silently dropped, a
  different $n$ than the dataframe holds.
- **Why** The printed summary is the ground truth about what was actually
  estimated. Disagreement means the object is not the analysis that was designed.
- **Fix** Rebuild the data backend at step 2.
- `src: [Intro] p.36`

### Two learners give materially different estimates `[WARNING]`
- **Symptom** Random forest and boosting — or tuned and untuned versions of one
  learner — return coefficients that disagree by more than sampling noise would
  explain.
- **Why** Learners that predict comparably well should produce estimates close to
  each other, because the estimate depends on the learners only through their
  predictions. A material gap therefore says one of them is predicting worse:
  orthogonality removes the first-order effect of nuisance error but not the
  second-order terms, and in finite samples those are what moves the number.
- **Fix** Read `evaluate_learners()` for each and keep the better predictor —
  chosen on prediction error, never on which coefficient looks better. If the
  learners predict about equally well and the estimates still diverge, do not
  report either as *the* estimate without saying so.
- `src: [D1] 01:58, [D2] 00:46–00:47`

### Coefficient reported without its standard error `[WARNING]`
- **Symptom** A point estimate quoted alone.
- **Why** The estimator is asymptotically normal with a sampling error of order
  $1/\sqrt{N}$; the point estimate without its uncertainty is not a result. The
  summary reports coefficient, standard error, $t$, $p$ and the interval together.
- **Fix** Report the full summary row, and go to step 8 for intervals.
- `src: [Intro] p.25, p.35`

### Learners in the fitted object are not the ones intended `[WARNING]`
- **Symptom** The *Machine Learner* block shows default hyperparameters after a
  tuning run, or a different learner than step 4 specified.
- **Why** The printed object reports the learners actually used, including their
  hyperparameters — the place where a tuning step that silently did nothing becomes
  visible.
- **Fix** Check the tuning at step 6 before reading the estimate.
- `src: [Intro] p.36, [Tune] p.9`

### Propensity learner quality passed over `[NOTE]`
- **Symptom** `ml_g0` and `ml_g1` inspected; the `ml_m` entry ignored.
- **Why** The propensity model enters the doubly robust score directly, and in the
  IRM its predictions can destabilise downstream results.
- **Fix** Read the `ml_m` value too, and carry any concern to the trimming
  decision and to step 8.
- `src: [Intro] p.37, [Sens] p.35`

### DiD sub-model effective sample sizes not checked `[NOTE]`
- **Symptom** A grid of `ATT(g, t_pre, t_eval)` estimates read without looking at
  the individual 2×2 sub-models.
- **Why** Sub-models are reachable through `modellist`, and each prints its own
  treatment group, pre-treatment period, evaluation period and effective sample
  size — which can be far smaller than the full panel.
- **Fix** Inspect `modellist` entries behind any surprising cell.
- `src: [DiD] p.39`

## Check mode — report format

```
**VERDICT** — n blockers, m warnings        (PASS | PROCEED WITH CAUTION | BLOCKED)

① <failure mode>                    [SEVERITY]
   observed   <what in the deliverable triggered it>
   fix        <what to do about it>

**Carry forward to step 8**
 • <facts step 8 needs>
```

Report only the modes that fired, most severe first.

## Carry forward to step 8 (`causal-8-inference`)

- The coefficient and standard error, with the estimand they belong to
- The learner evaluation figures, including `ml_m`
- Whether one or several treatment variables / effects were estimated — it decides
  whether joint inference is needed
- The trimming decision from step 5, and the unobserved confounder $U$ and
  benchmark covariate named at step 1

## Output style

Report in **Unicode math**, never LaTeX — write θ̂₀, σ², √N(θ̃₀ − θ₀) ∼ N(0, σ²),
ψ(W; θ₀, η₀), not `\sqrt` or `$...$`. The LaTeX in this file is for reading it in
Obsidian; it must not appear in your output. Define every symbol on first use. Bold
the verdict. Keep it short.
