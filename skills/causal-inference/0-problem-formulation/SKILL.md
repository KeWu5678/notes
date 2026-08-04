---
name: causal-0-problem-formulation
description: Define or audit the target estimand of an effect study — which potential-outcome contrast, for which population, with treatment, outcome and measurement horizon pinned down. Use when starting an effect-estimation project, when choosing between ATE / ATT / APO / CATE / LATE, when the treatment is an offer whose take-up is the unit's own choice (intent-to-treat), when a stated goal may really be a prediction or interpretability question, or when someone reports "the effect" without saying of what on whom over what horizon.
---

# 0. Problem formulation

**Deliverable** — one sentence naming the estimand, the treatment $D$, the outcome
$Y$, and the population, such that the eventual number has an unambiguous meaning.

## Inputs required

Ask for these; do not guess:

1. The question in the user's own words.
2. The treatment $D$ — what it is, **who assigns it**, and its type (binary,
   multi-valued, continuous).
3. The outcome $Y$, and **over what horizon** it is measured relative to treatment.
4. The population the answer is supposed to describe — and, separately, the
   population the data was collected on.
5. Whether assignment was randomized (A/B test, RCT) or observational.

If any is missing, ask for it and stop. A misformulated estimand cannot be
repaired downstream.

## Procedure

1. **Separate the causal question from the prediction question.** Predictive
   modelling asks how well $f(X)$ predicts $Y$. Causal modelling asks what the
   effect of $D$ on $Y$ is. "Which variables predict churn?" and "why do customers
   churn?" are different projects. `src: [Intro] p.6`
2. **Write the potential outcomes.** For binary $D$, define $Y(1)$ and $Y(0)$ as
   the outcome under each arm for the *same* unit. If you cannot state them, the
   treatment is not well defined. `src: [Intro] p.11`
   - **Set $D$ to the thing you can actually assign.** Where a unit chooses
     whether to take up what it was offered, and that choice depends on
     unobserved characteristics, the assignable thing is the offer. The estimand
     is then an **intent-to-treat** effect — of eligibility, not of
     participation. Say which one you mean. `src: [D1] 01:40–01:42`
   - **Fix the outcome horizon.** Clicks in the next 24 hours, conversions in
     three weeks, and lifetime customer value are three different estimands from
     the same project. `src: [D2] 00:13`
3. **Name the estimand as a contrast of potential outcomes**, e.g.
   $$
   \mathrm{ATE} = \mathbb{E}[Y(1)] - \mathbb{E}[Y(0)]
   $$
   `src: [Intro] p.13`
4. **Fix the population** the expectation is taken over — everyone, the treated
   only, a subgroup, or a covariate profile. This distinguishes ATE from ATT/ATTE,
   GATE and CATE. `src: [Intro] p.28` Then check it against the population the
   data actually covers: an intervention run on existing customers says nothing
   about non-customers, so "the ATE" is an ATE on a specific subgroup.
   `src: [D2] 01:01`
5. **Record whether assignment was randomized.** Under randomization
   $D \perp\!\!\!\perp Y(0), Y(1)$ and identification is immediate; without it,
   identification must be argued at step 1. `src: [Intro] p.14`
6. **Check the estimand is one DoubleML targets** — ATE, ATTE, CATE, GATE, APO,
   CAPO, GAPO, LATE, and the extensions (quantile treatment effects, conditional
   value at risk, weighted effects). `src: [Intro] p.28`

## Failure modes

### The question is predictive, not causal `[BLOCKER]`
- **Symptom** The goal is phrased as accuracy, ranking, or "which features
  matter" — feature importance, AUC, a scoring model.
- **Why** Predictive and causal modelling answer different questions; a good
  predictor of $Y$ need not be a cause of $Y$.
- **Fix** Either restate as an effect of a specific intervention $D$, or stop —
  this is not a causal project.
- `src: [Intro] p.6`

### An individual causal effect is the target `[BLOCKER]`
- **Symptom** The deliverable asks for the effect *on a given unit* —
  $\Delta = Y(1) - Y(0)$ for a named customer or patient.
- **Why** Only one potential outcome is observed per unit; the other is
  counterfactual. Individual effects are not identified in general.
- **Fix** Retarget to an average that is identifiable — ATE, or a conditional
  average (CATE/GATE) if heterogeneity is the real interest.
- `src: [Intro] p.11–12`

### Treatment not well defined `[BLOCKER]`
- **Symptom** $D$ is a state, a score, or an outcome rather than something that
  could be assigned; $Y(1)$ and $Y(0)$ cannot be written down.
- **Why** Potential outcomes are defined relative to an intervention. Without one
  there is no contrast to estimate.
- **Fix** Name the concrete intervention and who administers it.
- `src: [Intro] p.11`

### Take-up used as the treatment where only the offer is assignable `[BLOCKER]`
- **Symptom** $D$ is *participated*, *redeemed*, *enrolled*, *clicked* — something
  the unit decided — while what the business can act on is *was offered* or
  *was eligible*.
- **Why** Take-up depends on unobserved characteristics of the unit (the deck's
  example: saving preferences driving whether an eligible employee joins the
  pension plan). Those characteristics also drive $Y$, so the contrast on take-up
  is confounded by construction, and it is not a contrast anyone can implement.
- **Fix** Set $D$ to eligibility or assignment and report the effect as
  intent-to-treat; or, if the effect of take-up is genuinely the target, route to
  step 1 for an instrumental-variables design with eligibility as the instrument.
- `src: [D1] 01:40–01:42`

### Outcome horizon not fixed `[BLOCKER]`
- **Symptom** The outcome is named ("engagement", "sales", "churn") without the
  window it is measured over.
- **Why** The same treatment has different, sometimes opposite-signed, effects at
  24 hours, three weeks and lifetime value. Without the window, the estimand is
  not pinned down and two analysts will produce two numbers that both look right.
- **Fix** State the measurement window as part of the estimand. If several
  horizons matter, they are several estimands — say so, and carry the count to
  step 8 for joint inference.
- `src: [D2] 00:13`

### Estimand unnamed or ambiguous `[BLOCKER]`
- **Symptom** "The effect of $D$ on $Y$" with no population and no contrast —
  it is not stated whether the answer applies to everyone or to the treated.
- **Why** ATE and ATTE are different numbers; without a named estimand the eventual
  coefficient cannot be interpreted, and step 3 cannot pick a model class.
- **Fix** Write the contrast and the conditioning set explicitly.
- `src: [Intro] p.28`

### Outcome measured before or during treatment `[WARNING]`
- **Symptom** $Y$ is recorded at or before the time $D$ is assigned.
- **Why** Potential outcomes are defined as outcomes *following* treatment; a
  contemporaneous outcome cannot reflect the intervention.
- **Fix** Fix the measurement window, or move to a panel setting and hand to
  step 3 for a DiD model class.
- `src: [Intro] p.11`

### Estimand outside the supported set `[WARNING]`
- **Symptom** The target is not one of ATE, ATTE, CATE, GATE, APO, CAPO, GAPO,
  LATE or a listed extension.
- **Why** The DoubleML model table covers a specific set of estimands; anything
  else needs a different framework.
- **Fix** Restate the target as a supported estimand, or accept that this workflow
  will not deliver it.
- `src: [Intro] p.28`

### Population of the data confused with the population of the question `[WARNING]`
- **Symptom** The answer is to guide a decision about everyone, but the treatment
  could only be delivered to a specific subgroup — existing customers, opted-in
  users, one market — and the estimand is written as if it covered the whole
  population.
- **Why** Even a clean randomized experiment estimates the effect on whoever was
  eligible to be targeted. Whom you actually reached decides what causal effect
  you are estimating at all; the untargetable remainder is not represented.
- **Fix** Write the population into the estimand as the frame the data supports,
  and state separately whether extrapolating beyond it is being assumed.
- `src: [D2] 01:01`

### Interpretability output read as a causal answer `[WARNING]`
- **Symptom** SHAP values, feature importances or an explanation of why a model
  predicted something are being used to decide what to change.
- **Why** These explain the prediction, not the intervention: they report the
  correlation pattern the model exploited. The deck's example — a model that
  predicts lung cancer from carrying a lighter will faithfully explain that it
  used the lighter, and banning lighters changes nothing.
- **Fix** If the goal is to decide what to change, this is a causal project;
  restate it as an effect of a specific $D$ and continue to step 1. A repeatedly
  refitted forecasting model that keeps selecting different variables is the same
  symptom seen from the other side.
- `src: [D2] 00:08, 01:11`

### Several outcomes handled as one model `[NOTE]`
- **Symptom** A vector of outcomes — revenue *and* retention *and* satisfaction —
  expected from a single fit.
- **Why** Every DoubleML model class assumes a single outcome; there is no
  multivariate-outcome setting.
- **Fix** One model per outcome, and treat the collection as multiple quantities
  at step 8, where joint inference applies.
- `src: [D1] 01:18`

### Randomized data treated as observational `[NOTE]`
- **Symptom** The data comes from an A/B test but the plan reasons about
  confounding.
- **Why** With randomization, identification already holds. ML is then used for
  precision, efficiency and power — not to remove confounding.
- **Fix** Keep the DML machinery if you want efficiency gains, but do not present
  the covariate adjustment as the source of identification.
- `src: [Intro] p.14, p.17`

## Check mode — report format

```
**VERDICT** — n blockers, m warnings        (PASS | PROCEED WITH CAUTION | BLOCKED)

① <failure mode>                    [SEVERITY]
   observed   <what in the deliverable triggered it>
   fix        <what to do about it>

**Carry forward to step 1**
 • <facts step 1 needs>
```

Report only the modes that fired, most severe first. Say nothing about the ones
that did not.

## Carry forward to step 1 (`causal-1-causal-graph`)

- The estimand, written as a contrast, with its population
- $D$ and its type, and whether it is the offer or the take-up
- $Y$ and its measurement window
- Randomized or observational
- The population the data covers, where it is narrower than the question
- How many quantities will eventually be reported — step 8 needs the count
- Any estimand already ruled out, and why

## Output style

Report in **Unicode math**, never LaTeX — write θ₀, ψ, η, ⊥⊥, 𝔼[·], Y(1) − Y(0),
not `\theta_0` or `$...$`. The LaTeX in this file is for reading it in Obsidian; it
must not appear in your output. Define every symbol on first use. Bold the verdict.
Keep it short.
