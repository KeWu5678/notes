---
name: causal-1-causal-graph
description: Build or audit the DAG and the identification argument behind an effect estimate — which assumption buys identification (unconfoundedness, exclusion restriction, parallel trends), whether overlap holds, whether a covariate is a confounder, a collider or post-treatment, whether units interfere with each other. Use when deciding what to control for, when covariates were picked by feature importance or a Lasso, when spillover between treated and control units is possible, when asked "is this effect identified", or before trusting any adjusted comparison from observational data.
---

# 1. Causal graph and identification

**Deliverable** — a DAG over $(Y, D, X)$ plus a named identification assumption,
and the verdict on whether the step-0 estimand is recoverable at all.

Causality comes from identification, which comes from assumptions — not from the
estimator and not from better predictions. `src: [Recap] p.4`

## Inputs required

Ask for these; do not guess:

1. The estimand, $D$, $Y$, population, and randomized-or-observational, from step 0.
2. The candidate covariates $X$, and for each: **when it is measured** relative to
   treatment assignment.
3. What the user believes drives assignment to treatment.
4. What is known to be unmeasured.

If the covariate timing is not supplied, ask. It decides several blockers below.

## Procedure

1. **Draw the graph.** Nodes $Y$, $D$, $X$, and any unobserved $U$. The canonical
   observational structure is $X \to D$, $X \to Y$, $D \to Y$; confounding is the
   $X$ (or $U$) that points at both. `src: [Intro] p.15, [Sens] p.7`
2. **Name the identification assumption.** One of:
   - **Independence** — randomized assignment, $D \perp\!\!\!\perp Y(0), Y(1)$
   - **Unconfoundedness** (selection-on-observables, conditional exogeneity) —
     $$
     D \perp\!\!\!\perp Y(0), Y(1) \mid X
     $$
   - **Exclusion restriction** — IV settings
   - **Parallel trends** — DiD settings

   `src: [Recap] p.4, [Intro] p.15`
3. **State the intuition and check it holds.** Under unconfoundedness, comparing
   units with the same $X$ makes any outcome difference attributable to treatment
   — "apples to apples". Ask whether that is credible here. `src: [Intro] p.15`
4. **Classify every covariate.** $X$ must be **pre-treatment**, so that the
   outcome cannot feed back into it. `src: [DiD] p.17, [D2] 02:15` For each one,
   state the paths it sits on — pointing at $D$, at $Y$, or at both. A covariate
   that points only at $D$ is not a confounder and carries a cost; see the
   failure modes. `src: [D1] 01:54`
5. **Check overlap.** For units with covariates $X$, both treatment states must
   occur with positive probability — formally, the propensity of being treated
   stays bounded away from $1$ (and from $0$). `src: [DiD] p.23`
6. **Check that treating one unit does not change another's outcome.** Shared
   inventory, substitutable products, a fixed pool of demand, or a social network
   all break this. `src: [D2] 02:37–02:38`
7. **Decide whether DML applies at all** — the exits below.
8. **Note residual unobserved confounding.** Whatever remains unmeasured is the
   subject of step 8's sensitivity analysis, and should be flagged here so it is
   not forgotten. `src: [Sens] p.4, p.7`

Nothing downstream checks any of this. DoubleML fits and returns an estimate
whether or not the assumption holds — add a collider and the model still runs,
it just answers a different question. `src: [D2] 02:45–02:46, [D1] 01:39`

## Exits — when DML is the wrong tool

The DoubleML model table is itself the map of alternatives. If unconfoundedness
does not hold, say so and route:

| Situation | Where it goes |
|---|---|
| Unconfoundedness fails, a valid instrument exists (exclusion restriction) | Instrumental variables — LATE `src: [Intro] p.28` |
| Panel or repeated cross-sections, parallel trends more credible than unconfoundedness | Difference-in-Differences — ATT `src: [Intro] p.28, [DiD] p.13` |
| Tempted to forecast the counterfactual from the control group's own pre-period | Still DiD (or synthetic control). A time-series extrapolation carries no time fixed effects, so any common shock lands in the estimate as treatment effect. `src: [D2] 02:04` |
| Treatment switches at a cutoff $S = c$ | Regression discontinuity — LATE at the cutoff `src: [Intro] p.28, [Het] p.46` |
| Outcome observed only for a selected subgroup | Sample selection model — ATE (selected) `src: [Intro] p.28` |
| Unconfoundedness fails and none of the above applies | Stop. No estimator recovers the estimand. `src: [Recap] p.4` |

## Failure modes

### No identification assumption named `[BLOCKER]`
- **Symptom** The plan lists covariates to control for but never states which
  assumption makes the estimand identified.
- **Why** Causal interpretation comes from identification, which is obtained from
  assumptions. Adjustment without a stated assumption is a regression, not a
  causal estimate.
- **Fix** Name one of independence, unconfoundedness, exclusion restriction, or
  parallel trends, and argue it.
- `src: [Recap] p.4`

### Post-treatment variable among the covariates `[BLOCKER]`
- **Symptom** A covariate is measured after, or simultaneously with, treatment
  assignment — a downstream metric, a consequence of $D$.
- **Why** $X$ is defined as pre-treatment covariates. Conditioning on a
  consequence of treatment is not covariate adjustment.
- **Fix** Drop it, or replace it with its pre-treatment value.
- `src: [DiD] p.17`

### Treating one unit changes another unit's outcome `[BLOCKER]`
- **Symptom** Units compete for a fixed pool — substitutable products, shared
  inventory, limited demand, a marketplace, a social graph — and some are treated
  while others serve as controls.
- **Why** The control group absorbs part of the treatment. The identification
  argument says the controls show what would have happened without treatment, and
  under interference they do not. The direction is knowable: if the spillover
  pushes control outcomes the same way as the treatment, the effect is
  underestimated; if the opposite way, overestimated.
- **Fix** Randomize or compare at the level the interference is contained in
  (market, region, cluster) so that spillover happens *within* a unit. Where the
  spillover is argued to be small, say plainly that it is being assumed
  negligible and give the sign of the bias if it is not — modelling it properly
  needs far more structure on the problem than this workflow carries.
- `src: [D2] 02:36–02:38`

### Covariate set produced by a feature-selection procedure `[BLOCKER]`
- **Symptom** $X$ comes from feature importances, a shadow/permuted-feature
  comparison, Lasso selection, or "we threw everything in and let the model
  decide".
- **Why** Every one of those ranks variables by association with the outcome, and
  the conditioning set is not an association question. Two distinct failures
  follow. It *admits* variables that should be excluded — colliders and mediators
  are often excellent predictors, and conditioning on them opens paths rather
  than closing them. And it *drops* variables that must be included: a confounder
  that predicts $D$ strongly but $Y$ only weakly is exactly what an
  outcome-driven selector discards, and dropping it is an omitted-variable bias
  that no amount of orthogonality repairs.
- **Fix** Choose $X$ from the graph — each variable admitted because of the paths
  it sits on. Use selection procedures, if at all, only to prune within a set
  already justified structurally.
- `src: [D2] 00:05–00:11, 00:43, [D1] 00:51`

### Overlap / common support fails `[BLOCKER]`
- **Symptom** For some covariate profiles, treatment is effectively certain or
  impossible — the estimated propensity sits at $0$ or $1$ for part of the sample.
- **Why** Identification requires that a comparable control unit could exist for
  each treated unit; without it there is nothing to compare against.
- **Fix** Restrict to the region of common support, or retarget to an estimand
  defined on the treated (ATTE, available from IRM). Carry the diagnosis to step 5,
  where trimming is decided.
- `src: [DiD] p.23`

### Better ML expected to repair identification `[BLOCKER]`
- **Symptom** The plan answers "what about confounding?" with a more flexible
  learner, more features, or more tuning.
- **Why** Naive ML use can produce systematic bias *even when identification
  holds*; conversely no learner produces identification when the assumption fails.
  The two are separate concerns.
- **Fix** Settle identification first. Learner quality is step 4.
- `src: [Recap] p.4–5`

### Strong predictor of $D$ that does not affect $Y$ `[WARNING]`
- **Symptom** A variable is in $X$ because it sharpens the propensity model —
  near-deterministic of assignment, but with no path to the outcome. An
  instrument, or something close to one.
- **Why** It is not a confounder, so it removes no bias; and it costs precision.
  What identifies $\theta_0$ is the variation in $D$ that survives conditioning on
  $X$. Conditioning on a strong predictor of $D$ consumes that variation, and the
  standard error grows as it shrinks. The estimate stays valid and gets noisier —
  which is worse than it sounds, because nothing in the output flags it.
- **Fix** Drop it. If it is a genuine instrument and unconfoundedness is in doubt,
  that is an argument for the IV row of the exits table, not for putting it in $X$.
- `src: [D1] 01:54`

### Identification delegated to the package `[WARNING]`
- **Symptom** The plan expects DoubleML to handle confounding, or asks whether
  the DiD class "takes care of" parallel trends — the question is whether an
  unsuitable control group or an extra covariate would harm the estimate.
- **Why** It would, silently. The model class assumes its identification
  assumption and estimates under it; a violated assumption produces no error, no
  warning and no diagnostic — just a different number. A completed fit is
  evidence that the code ran, not that the design was sound.
- **Fix** Settle the assumption here, on subject-matter grounds, and record what
  would violate it. The only downstream instruments are the step 8 sensitivity
  analysis and, for DiD, placebo tests — both of which need this step's output to
  be interpretable.
- `src: [D2] 02:45–02:46, [D1] 01:39`

### Unconfoundedness asserted as if testable `[WARNING]`
- **Symptom** The deliverable claims the assumption was "checked" or "validated"
  against the data.
- **Why** Identification assumptions restrict counterfactuals, which are not
  observed. The decks' own answer to "is this assumption reasonable?" is
  sensitivity analysis and domain expertise, not a test.
- **Fix** State it as an assumption, note what would violate it, and plan the
  step 8 sensitivity analysis.
- `src: [DiD] p.14, [Sens] p.12`

### Plausible unobserved confounder with no plan `[WARNING]`
- **Symptom** A driver of both $D$ and $Y$ is known to be unmeasured, and nothing
  downstream addresses it.
- **Why** Observational identification is exactly the claim that no such $U$
  exists. If one is plausible, the estimate's credibility rests on how large its
  influence would have to be.
- **Fix** Name $U$ now, and name a **benchmark covariate** of comparable strength
  for step 8's benchmarking.
- `src: [Sens] p.7, p.12–13`

### Covariate justified by predictive power alone `[NOTE]`
- **Symptom** A variable is in $X$ because it predicts $D$ or $Y$ well.
- **Why** The role of $X$ in the graph is what licenses adjustment. Predictive
  strength is not that argument.
- **Fix** State each covariate's path: does it point at both $D$ and $Y$?
- `src: [Intro] p.15`

### Comparison group chosen by matching pre-treatment outcomes `[NOTE]`
- **Symptom** Controls picked because their outcome history tracks the treated
  group's most closely, with no reference to covariates.
- **Why** Outcomes are noisy, so the closest-tracking units are partly the ones
  whose noise happened to line up — the selection overfits. Matching on
  covariates instead picks units alike in background characteristics, which is
  what makes it plausible that they would have gone on behaving alike.
- **Fix** Select on covariates; use outcome history as a check afterwards, not as
  the selection criterion. With a large donor pool both are available — the point
  is which one decides.
- `src: [D2] 02:10`

## Check mode — report format

```
**VERDICT** — n blockers, m warnings        (PASS | PROCEED WITH CAUTION | BLOCKED)

① <failure mode>                    [SEVERITY]
   observed   <what in the deliverable triggered it>
   fix        <what to do about it>

**Carry forward to step 2**
 • <facts step 2 needs>
```

Report only the modes that fired, most severe first.

## Carry forward to step 2 (`causal-2-data-backend`)

- The identification assumption, named
- The final covariate set $X$, each confirmed pre-treatment, each with its path
- Whether the design is cross-sectional, panel, or repeated cross-sections
- Any overlap problem found, for the trimming decision at step 5
- Whether interference between units was ruled out, or assumed away and with
  which sign of bias
- Named unobserved confounder $U$ and a benchmark covariate, for step 8
- If an exit fired: which alternative design, and that the DML workflow stops here

## Output style

Report in **Unicode math**, never LaTeX — write D ⊥⊥ Y(0), Y(1) | X, θ₀, 𝔼[·], m₀(X),
not `\perp` or `$...$`. The LaTeX in this file is for reading it in Obsidian; it must
not appear in your output. Define every symbol on first use. Bold the verdict. Keep
it short.
