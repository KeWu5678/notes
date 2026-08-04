---
name: causal-4-ml-methods
description: Choose or audit the nuisance learners — ml_l, ml_g, ml_m — for a DoubleML model: regressor vs classifier, pipelines and stacking, and whether predictive quality is good enough for the rate requirement. Use when initializing learners for a DML fit, when deciding between random forest / boosting / stacked pipelines for a propensity or outcome model, or when learner performance is in question.
---

# 4. ML methods

**Deliverable** — initialized learners for each nuisance function the model class
needs, with a stated plan for evaluating their out-of-sample quality.

## Inputs required

Ask for these; do not guess:

1. From step 3: the model class and which nuisance functions it needs.
2. Treatment type (decides classifier vs regressor for `ml_m`).
3. Sample size and covariate dimension.
4. Whether tuning (step 6) is planned — it changes how much effort belongs here.

## Procedure

1. **Identify the nuisance functions.** They are conditional expectations the
   estimator needs but does not report:
   - PLR: $\ell_0(X) = \mathbb{E}[Y \mid X]$ and $m_0(X) = \mathbb{E}[D \mid X]$
     `src: [Recap] p.12`
   - IRM / APO: $g(d,X) = \mathbb{E}[Y \mid D=d, X]$ and the propensity
     $m(X)$ `src: [Recap] p.15, [Het] p.4`
   - DiD: the conditional trend
     $g_0(X_i) = \mathbb{E}[Y_{t_{\mathrm{eval}}} - Y_{t_{\mathrm{pre}}} \mid X_i, G_i \in \mathcal{C}]$
     and the group propensity
     $m_0(X_i) = P(G_i = g \mid X_i, \ldots)$ `src: [DiD] p.25`
2. **Match learner type to target.** Regression targets take a regressor;
   probability targets take a classifier. `src: [Intro] p.32`

   ```python
   from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

   ml_l_rf = RandomForestRegressor(n_estimators=500, max_depth=7,
                                   max_features=3, min_samples_leaf=3)
   ml_m_rf = RandomForestClassifier(n_estimators=500, max_depth=5,
                                    max_features=4, min_samples_leaf=7)
   ```

   In the IRM and APO models the outcome nuisance is fitted per arm — a
   T-learner — so the treatment is effectively in the outcome regression even
   though it is not a column of $X$. `src: [D1] 01:54, 02:13`
3. **Use scikit-learn or scikit-learn-like learners.** That is the supported
   interface: anything with `fit` / `predict` (and `predict_proba` for
   classifiers) that can be cloned. A learner without it can be wrapped, and as a
   last resort its predictions can be computed outside and supplied to `fit()`,
   which treats them as if the model had produced them internally.
   `src: [Intro] p.27, [D1] 01:50, 02:34`
4. **Know the rate requirement.** Orthogonality removes the first-order effect of
   nuisance error, but the errors cannot be arbitrarily large — their product must
   shrink fast enough. `src: [Intro] p.23`
   - PLR, partialling out:
     $\|\hat m_0 - m_0\|_{P,2} \times (\|\hat m_0 - m_0\|_{P,2} + \|\hat\ell_0 - \ell_0\|_{P,2}) \le \delta_N N^{-1/2}$
   - IRM / DR score, ATE:
     $\|\hat m_0 - m_0\|_{P,2} \times \|\hat\ell_0 - \ell_0\|_{P,2} \le \delta_N N^{-1/2}$

   This is what allows learners converging slower than parametric rates — random
   forests, gradient boosting, neural networks. `src: [Recap] p.16, [Intro] p.23`
5. **Consider pipelines and stacking** where a single learner is inadequate:
   `Pipeline` with a scaler, `StackingRegressor` / `StackingClassifier` over
   several base learners. `src: [Tune] p.15, [DiD] p.32–33`
6. **Plan out-of-sample evaluation, and fix the selection rule now.** Prediction
   quality is assessed with out-of-sample metrics, via `evaluate_learners()` at
   step 7. Commit in advance: the learner with the smallest out-of-sample
   nuisance prediction error wins. `src: [Intro] p.23, [Tune] p.13, [D2] 00:40`

Note that some model classes create multiple internal learners from `ml_g` and
`ml_m` — for IRM, `params_names` is `['ml_g0', 'ml_g1', 'ml_m']`, the outcome model
for the control arm, the outcome model for the treated arm, and the propensity
score. `src: [Tune] p.10`

## Failure modes

### Regressor used where a classifier is required `[BLOCKER]`
- **Symptom** `ml_m` is a regressor while $D$ is binary; or `ml_g` / `ml_l` is a
  classifier while $Y$ is continuous.
- **Why** $m_0(X)$ is a probability — the propensity score. The outcome nuisance is
  a conditional mean. The decks pair `RandomForestRegressor` with the outcome and
  `RandomForestClassifier` with the treatment.
- **Fix** Swap in the matching learner type.
- `src: [Intro] p.32, [Tune] p.5`

### Learner chosen by the estimate it produces `[BLOCKER]`
- **Symptom** Several learners tried, and the one kept is the one whose $\theta$
  is significant, or signed as expected, or closest to a prior belief. Often
  disguised: "random forest didn't work, boosting did".
- **Why** Different learners genuinely give different estimates in finite samples
  — orthogonality kills the first-order effect of nuisance error, not the
  second-order terms, so better predictions still mean better estimates.
  Selecting on the estimate turns that residual sensitivity into a search over
  outcomes, and the reported standard error does not account for the search.
- **Fix** Rank candidates by out-of-sample nuisance prediction error, decided
  before looking at any coefficient. Where two learners predict comparably well,
  their estimates should come out close; if they do not, that is a finding to
  report, not a menu to choose from.
- `src: [D2] 00:40, 00:46–00:47, 00:59–01:00, [D1] 01:58`

### Learner interface unsupported and no fallback used `[BLOCKER]`
- **Symptom** A custom object without the fit/predict interface passed as a
  learner, or a modelling step (e.g. a bespoke target encoding) that will not fit
  in a `Pipeline`.
- **Why** DoubleML's high-quality-ML ingredient is provided through scikit-learn
  and scikit-learn-like learners: it clones the estimator and calls
  `fit`/`predict` per fold.
- **Fix** Wrap it in a scikit-learn compatible estimator, put the transformation
  in a `Pipeline` so the whole thing is one estimator, or compute the nuisance
  predictions externally and supply them to `fit()`. Note that the external route
  hands you responsibility for the cross-fitting the package would have done.
- `src: [Intro] p.27, [D1] 01:50, 02:34`

### Orthogonality treated as licence for poor learners `[BLOCKER]`
- **Symptom** Learner quality dismissed on the grounds that the score is
  orthogonal and cross-fitting is on.
- **Why** Orthogonality reduces bias from nuisance error, but the errors cannot be
  arbitrarily large: the *product* of ML errors must shrink fast enough. Poor
  predictions mean poor causal estimates.
- **Fix** Treat nuisance prediction quality as a requirement, and measure it.
- `src: [Intro] p.23, [Recap] p.16`

### No out-of-sample evaluation planned `[BLOCKER]`
- **Symptom** Learners chosen with no metric, or judged on in-sample fit.
- **Why** Prediction quality must be evaluated with out-of-sample metrics; the
  evaluation of nuisance learners is what tells you whether the rate requirement is
  plausibly met.
- **Fix** Commit to `evaluate_learners()` at step 7, and compare candidates on it.
- `src: [Intro] p.23, [Tune] p.13`

### Boosting for the propensity score on a small sample `[WARNING]`
- **Symptom** Gradient boosting as `ml_m` where $n$ is small, or where one arm is
  small even if the sample is not.
- **Why** Boosting produces overconfident probabilities at the extremes, pushing
  $\hat m(X)$ towards 0 and 1. Those are the values the doubly robust score
  divides by, so a handful of observations acquire enormous weight and the
  estimate — and the step 8 sensitivity analysis with it — becomes unstable.
- **Fix** Prefer a better-calibrated propensity learner at small $n$, inspect the
  fitted propensity distribution rather than only its log loss, and carry the
  concern to the trimming decision at step 5.
- `src: [D1] 00:57, [Sens] p.35`

### Default hyperparameters accepted without question `[WARNING]`
- **Symptom** Learners constructed bare, with no tuning planned.
- **Why** Default hyperparameters are rarely optimal for a specific dataset, and
  nuisance predictive performance feeds directly into the bias, the standard errors
  and the width of the confidence intervals. Several sklearn defaults are actively
  bad here — the random forest's minimum leaf size is small enough to overfit
  heavily, which is exactly the failure cross-fitting exposes as noise rather
  than repairing.
- **Fix** Either tune at step 6, or record that defaults were a deliberate choice.
- `src: [Tune] p.3, [D1] 02:02`

### One learner object shared across roles `[NOTE]`
- **Symptom** The same estimator instance passed as both `ml_g` and `ml_m`, or
  reused across quantiles/levels.
- **Why** The decks clone learners when passing them into several roles
  (`clone(class_learner)`).
- **Fix** Pass independent clones.
- `src: [Het] p.43`

## Check mode — report format

```
**VERDICT** — n blockers, m warnings        (PASS | PROCEED WITH CAUTION | BLOCKED)

① <failure mode>                    [SEVERITY]
   observed   <what in the deliverable triggered it>
   fix        <what to do about it>

**Carry forward to step 5**
 • <facts step 5 needs>
```

Report only the modes that fired, most severe first.

## Carry forward to step 5 (`causal-5-dml-specification`)

- The learner objects, per nuisance role
- Whether tuning is planned (step 6) or defaults are deliberate
- The metric that will be used to judge them at step 7, fixed before any
  coefficient is seen
- Any concern about propensity quality — it feeds the trimming decision

## Output style

Report in **Unicode math**, never LaTeX — write ℓ₀(X), m₀(X), g(1,X), ‖m̂₀ − m₀‖,
δ_N N^{-1/2}, 𝔼[Y | X], not `\ell_0` or `$...$`. The LaTeX in this file is for
reading it in Obsidian; it must not appear in your output. Define every symbol on
first use. Bold the verdict. Keep it short.
