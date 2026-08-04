---
name: causal-8-inference
description: Produce or audit the inference stage — confint(), multiplier bootstrap and joint intervals, GATE/CATE heterogeneity, DiD aggregation and placebo tests, and sensitivity analysis to unobserved confounding via cf_y / cf_d / rho, robustness values and benchmarking. Use when reporting confidence intervals for an effect estimate, when several effects or subgroups are reported at once, when reading a DiD event study or its pre-treatment periods, or when asked how robust a result is to an omitted confounder.
---

# 8. Inference

**Deliverable** — intervals that are valid for the number of quantities reported,
plus a statement of how robust the result is to unobserved confounding.

## Inputs required

Ask for these; do not guess:

1. From step 7: the estimate, standard error, and the estimand.
2. How many quantities are being reported — one effect, several treatment
   variables, a GATE table, a CATE curve, an ATT grid.
3. From step 1: the named unobserved confounder $U$ and a benchmark covariate.
4. From step 5: whether trimming was applied.
5. Whether the data is observational or randomized (step 0).

If the benchmark covariate was never named, ask for it before running sensitivity
analysis — the sensitivity parameters are otherwise uncalibrated.

## Procedure

### Confidence intervals

```python
dml_irm_rf.confint(level=0.95).round(2)
```

`src: [Intro] p.38`

### Joint / simultaneous inference

Where several quantities are reported together, use the multiplier bootstrap and
ask for joint intervals. `src: [Intro] p.39`

```python
_ = dml_irm_rf.bootstrap()
dml_irm_rf.confint(joint=True)
```

The same applies to DiD event studies (`bootstrap(n_rep_boot=5000)`, then
`plot_effects(joint=True)`), to `DoubleMLAPOS`, to GATEs, and to quantile treatment
effects. `src: [DiD] p.38, [Het] p.6, p.16, p.44`

### Heterogeneity

The variables the effect is allowed to vary with are a **separate choice** from
the confounders. They are *effect modifiers*: a confounder need not modify the
effect, an effect modifier need not be causal, and heterogeneity with respect to
one is a correlational statement about who responds — not a claim about
mechanism. `src: [D2] 00:25–00:26, 00:30`

- **GATE** — $\tau_{GATE} = \mathbb{E}[Y(1) - Y(0) \mid G = 1]$ for a group
  indicator $G$, via `gate()` on the already-fitted model; no re-estimation needed.
  `src: [Het] p.11, p.14`
- **CATE** — $\tau(x) = \mathbb{E}[Y(1) - Y(0) \mid X = x]$, approximated on a
  basis: linear, polynomial, or spline. Then `confint(grid, joint=True,
  n_rep_boot=...)` for values at new points. `src: [Het] p.19–21, p.23, p.27`
- **CAPO / APO contrasts** — `causal_contrast(reference_levels=[...])` on a
  `DoubleMLAPOS` object. `src: [Het] p.7`

### DiD aggregation

Aggregated effects take the form
$$
\theta_0 = \sum_{g}\sum_{t \ge 2} \omega_{g,t}\,\mathrm{ATT}(g,t),
$$
with weighting schemes: group aggregation, calendar-time aggregation, or event-study
aggregation by event time $e = t - g$. `src: [DiD] p.41–42`

The event-study plot's pre-treatment side is a set of **placebo tests**: cells
whose evaluation period precedes treatment, which should sit near zero if trends
were parallel. Read them for drift as well as for significance, and read them
jointly — see the failure modes. `src: [DiD] p.38, [D2] 02:12, 02:49–02:51`

### Sensitivity analysis

Observational identification rests on an assumption about what is *not* observed;
this is where that assumption is stressed. The framework generalises Cinelli and
Hazlett (2020) to nonlinear, ML-estimated models via the Riesz–Fréchet
representation. `src: [Sens] p.16, p.18`

```python
dml_irm_rf.sensitivity_analysis(cf_y=..., cf_d=..., rho=...)
print(dml_irm_rf.sensitivity_summary)
dml_irm_rf.sensitivity_plot(grid_bounds=...)
```

- `cf_y` — share of residual variation of the outcome explained by the omitted
  confounder(s), given the observed covariates
- `cf_d` — share of residual variation of the treatment explained by the omitted
  confounder(s), given the observed covariates
- `rho` — degree of adversity of the confounding scenario

`src: [Sens] p.10, p.22, p.33`

The interpretation of `cf_d` and `cf_y` **depends on the causal model** — partial
nonparametric $R^2$ measures in the PLR, an average gain in predictive quality in
the IRM. `src: [Sens] p.22–23`

Report the **robustness value** (`RV`, `RVa`) from `sensitivity_summary`, and
calibrate the scenario by **benchmarking**: mimic omitting an important observed
covariate, recompute the sensitivity parameters at that covariate's values, and use
domain expertise to judge whether a confounder of that strength is plausible.
`src: [Sens] p.11, p.12–13, p.24–25`

## Failure modes

### Several quantities reported with pointwise intervals `[BLOCKER]`
- **Symptom** Multiple treatment variables, an ATT grid, a GATE table, a CATE
  curve or a set of quantile effects — each with its own 95% interval, read as if
  all were simultaneously valid.
- **Why** Joint validity requires the multiplier bootstrap; pointwise intervals do
  not cover the collection.
- **Fix** `bootstrap()` then `confint(joint=True)`, and say which kind of interval
  is being reported.
- `src: [Intro] p.39, [DiD] p.38, [Het] p.16, p.44`

### Subgroups searched until one is significant `[BLOCKER]`
- **Symptom** Many groupings tried and the significant one reported; an
  experiment sliced repeatedly; results monitored until they cross the threshold;
  a heterogeneity story assembled after seeing which cut worked.
- **Why** Run enough comparisons and something will be significant by chance —
  the failure mode large-scale experimentation programmes are criticised for, and
  it worsens as the true effects get smaller, because there is less signal to
  distinguish from the noise. The interval reported at the end prices in one
  comparison, not the search.
- **Fix** Fix the groups before looking, report every one you examined, and use
  joint intervals over the whole set. If the grouping was found in the data, say
  so and treat it as a hypothesis for the next experiment rather than a result.
- `src: [D2] 00:59–01:00`

### GATE groups not mutually exclusive `[BLOCKER]`
- **Symptom** Overlapping group indicators passed to `gate()` — several boolean
  columns a unit can satisfy at once.
- **Why** Valid interpretation requires mutually exclusive groups.
- **Fix** Define the groups from a single column so membership is exclusive by
  construction.
- `src: [Het] p.17`

### No sensitivity analysis on observational data `[BLOCKER]`
- **Symptom** An effect from observational data reported with a confidence
  interval and nothing about unobserved confounding.
- **Why** With experimental data there is good reason to believe the independence
  assumption holds; observational data has no such warrant, and sensitivity
  analysis is the seventh step of the workflow, not an optional extra.
- **Fix** Run `sensitivity_analysis()` and report the robustness values.
- `src: [Sens] p.4, p.21`

### Sensitivity parameters uncalibrated `[BLOCKER]`
- **Symptom** `cf_y` and `cf_d` set to round numbers with no justification, and
  conclusions drawn from the contour plot.
- **Why** The values are only interpretable against something: benchmarking relates
  them to an observed confounder of known importance, so domain expertise can judge
  whether the scenario is plausible.
- **Fix** Benchmark against a strong observed covariate and calibrate the plot to
  that scenario.
- `src: [Sens] p.12–13, p.33`

### Placebo tests read as validation of parallel trends `[WARNING]`
- **Symptom** Pre-treatment cells near zero, and the parallel-trends assumption
  reported as checked, tested, or confirmed.
- **Why** They are evidence about the periods before treatment, and the
  assumption is about the periods after it. Trends that ran parallel up to the
  treatment date can diverge for reasons that have nothing to do with the
  treatment — which is precisely the case the assumption rules out and the data
  cannot.
- **Fix** Report placebo results as supporting evidence and keep the assumption
  stated as an assumption. Sensitivity analysis and domain expertise remain the
  answer to "is this credible", exactly as under unconfoundedness.
- `src: [D2] 02:12, [DiD] p.14`

### Placebo grid read pointwise `[WARNING]`
- **Symptom** A row of pre-treatment estimates, each with its own 95% interval,
  and "none of them is significant" taken as a clean bill of health.
- **Why** Testing many pre-treatment periods is a multiple-testing problem in the
  ordinary direction — with enough cells, some will look fine by chance and
  others will cross zero by chance. Neither reading is reliable pointwise.
- **Fix** `bootstrap()` and read the placebo cells with joint intervals, the same
  machinery the post-treatment cells need.
- `src: [D2] 02:49`

### Heterogeneity variables taken from the confounder set `[WARNING]`
- **Symptom** GATE groups or a CATE basis built from $X$ because that is what was
  controlled for; or, from the other side, a causal-forest-style search reported
  as covering heterogeneity in general when it only split on the features it was
  given.
- **Why** The two variable sets answer different questions and are chosen
  independently. A confounder need not modify the effect; an effect modifier need
  not be a confounder, or causal at all. Heterogeneity along a dimension that was
  never in $X$ will not appear no matter how flexible the learner.
- **Fix** Name the effect modifiers deliberately, from what a decision would
  actually be targeted on. Where the dimension of interest is not in $X$,
  heterogeneity with respect to it is obtained by projection, not by refitting on
  a different covariate set.
- `src: [D2] 00:25–00:26, 00:30`

### Groups searched over many features `[WARNING]`
- **Symptom** A data-driven search for the subgroups with the largest effects,
  run over a wide feature set, returning small, very specific segments.
- **Why** With enough features the search fits noise: it finds groups whose
  estimated effect is extreme because averaging over few units leaves the
  estimate unaveraged. The reported segment effect is then mostly sampling error.
- **Fix** Restrict the search to features a policy could actually be targeted on —
  which is usually a short list known in advance — and check the effective sample
  size behind any segment before acting on it.
- `src: [D1] 01:24`

### CATE coefficients read as effects of the covariates `[WARNING]`
- **Symptom** A CATE basis coefficient — e.g. on age — described as the effect of
  that covariate.
- **Why** The coefficients describe only how the effect of $D$ on $Y$ varies with
  $X$. They do not mean $X$ affects $D$, or that $D$ affects $X$.
- **Fix** Phrase as effect heterogeneity with respect to $X$, not as an effect of
  $X$.
- `src: [Het] p.19`

### Sensitivity parameters interpreted without the model class `[WARNING]`
- **Symptom** `cf_d` / `cf_y` described in partial-$R^2$ language for an IRM fit.
- **Why** Their interpretation depends on the causal model — partial nonparametric
  $R^2$ in the PLR, average gain in predictive quality in the IRM.
- **Fix** State the interpretation belonging to the class used at step 3.
- `src: [Sens] p.22–23`

### Sensitivity conclusion stated as definitive `[WARNING]`
- **Symptom** "The result is robust", full stop.
- **Why** Conclusions from sensitivity analyses are generally not unambiguous —
  they depend on the context of the study and must be interpreted with domain
  expertise. The deck's own worked conclusion is conditional in both directions:
  not robust *if* a confounder as strong as the benchmark is plausible, more
  confident *if* it is not.
- **Fix** State the conclusion conditionally, naming the confounding scenario it is
  conditional on.
- `src: [Sens] p.34, p.35`

### Single fold assignment behind the reported interval `[WARNING]`
- **Symptom** Intervals from one cross-fitting repetition, especially where the
  sensitivity results move between runs.
- **Why** The recommendation is to repeat cross-fitting several times (`n_rep`) and
  use multiple folds; in the IRM, propensity predictions can render sensitivity
  results unstable, where trimming may help.
- **Fix** Increase `n_rep`, and revisit trimming at step 5.
- `src: [Sens] p.35`

### Placebo failure just before treatment diagnosed as a trend violation `[NOTE]`
- **Symptom** Pre-treatment cells near zero across the board except the one or two
  immediately preceding treatment, read as evidence that parallel trends fail and
  the design is unusable.
- **Why** That pattern is the signature of **anticipation**, not of diverging
  trends: units changed behaviour once they knew treatment was coming. A genuine
  trend violation shows up across the pre-period, not only at its end.
- **Fix** Raise `anticipation_periods`, or shift the treatment date back far
  enough that no anticipation is plausible, and refit. Both are step 3 decisions.
- `src: [D2] 02:22–02:24`

### Pre-treatment estimates judged only by significance `[NOTE]`
- **Symptom** An event-study plot whose pre-treatment cells all have intervals
  covering zero, accepted without looking at their shape.
- **Why** A run of individually non-significant pre-treatment estimates that all
  lean the same way is a visible pre-trend, and it weakens the assumption whether
  or not any single cell rejects.
- **Fix** Read the pre-period for drift as well as for significance, and say so
  when it is present.
- `src: [D2] 02:50–02:51`

### Linear CATE approximation not stress-tested `[NOTE]`
- **Symptom** A linear basis used and its shape taken as the true heterogeneity.
- **Why** The linear approximation is quite restrictive; polynomial and spline
  bases are available for a more flexible approximation.
- **Fix** Refit on a richer basis and compare.
- `src: [Het] p.23, p.27`

### Trimming applied but not reported `[NOTE]`
- **Symptom** A trimming threshold set at step 5 and absent from the write-up.
- **Why** Trimming is a recommendation for stability in the IRM, and it is part of
  how the reported number was produced.
- **Fix** Report the threshold alongside the estimate.
- `src: [Sens] p.35`

## Check mode — report format

```
**VERDICT** — n blockers, m warnings        (PASS | PROCEED WITH CAUTION | BLOCKED)

① <failure mode>                    [SEVERITY]
   observed   <what in the deliverable triggered it>
   fix        <what to do about it>

**Carry forward**
 • <what belongs in the write-up>
```

Report only the modes that fired, most severe first.

## Carry forward — into the write-up

- The estimand, the estimate, and which kind of interval (pointwise or joint)
- `n_folds`, `n_rep`, trimming threshold, seed
- How many quantities were examined, including any that were not reported
- Robustness values, the benchmark covariate used, and the confounding scenario
  the conclusion is conditional on
- The identification assumption from step 1, restated as an assumption
- For DiD: the placebo results, the anticipation window, and the fact that a
  clean pre-period is supporting evidence rather than a test

The workflow ends here. What it cannot tell you is whether the assumption at step 1
was true.

## Output style

Report in **Unicode math**, never LaTeX — write τ(x) = 𝔼[Y(1) − Y(0) | X = x],
cf_y, cf_d, ρ, ATT(g,t), θ₀ = ∑ ω_{g,t} ATT(g,t), not `\tau` or `$...$`. The LaTeX in
this file is for reading it in Obsidian; it must not appear in your output. Define
every symbol on first use. Bold the verdict. Keep it short.
