---
name: causal-3-model-class
description: Choose or audit the DoubleML model class and the estimand it targets — PLR vs IRM vs APO/APOS vs IIVM vs DIDMulti vs QTE — against treatment type and data structure. Use when picking between DoubleMLPLR and DoubleMLIRM, when a multi-valued treatment is being squeezed into a binary one, or when checking that the requested estimand is actually available from the chosen class.
---

# 3. Model class

**Deliverable** — the `DoubleML*` class, the score it will use, and the estimand it
targets, justified against treatment type and data structure.

This is what the decks call "Causal Model" in the workflow. It is the **estimator**
choice, not the structural model — that was step 1. See `CONTEXT.md`.

## Inputs required

Ask for these; do not guess:

1. The estimand from step 0.
2. Treatment type: binary, categorical/multi-valued, or continuous.
3. Data structure: cross-sectional, panel, or repeated cross-sections.
4. The identification assumption from step 1 (it constrains the row below).
5. Whether effect heterogeneity is of interest, or only an average.

## Procedure

Match all three of treatment type, data structure and estimand against the model
table. `src: [Intro] p.28, p.31`

| Model type | Treatment | Data structure | Estimands |
|---|---|---|---|
| Partially Linear (`DoubleMLPLR`) | Continuous / Binary | Cross-sectional | ATE, CATE, GATE |
| Interactive Regression (`DoubleMLIRM`) | Binary | Cross-sectional | ATE, ATTE, CATE, GATE |
| Potential Outcome Models (`DoubleMLAPO`, `DoubleMLAPOS`) | Binary / Categorical | Cross-sectional | APO, CAPO, GAPO |
| Instrumental Variables (`DoubleMLIIVM`) | Continuous / Binary | Cross-sectional | ATE, LATE |
| Difference-in-Differences (`DoubleMLDIDMulti`) | Binary | Panel / Repeated CS | ATT |
| Sample Selection | Binary | Cross-sectional | ATE (selected) |
| Regression Discontinuity | Binary | Cross-sectional | LATE (at cutoff) |

Extensions: quantile treatment effects (`DoubleMLQTE`), conditional value at risk,
weighted treatment effects. `src: [Intro] p.28, [Het] p.43`

Outcome type is not in the table but constrains it: most classes take a binary or
a continuous $Y$, none takes a multivariate one, and the PLR needs care with a
binary $Y$ — see the failure modes. `src: [D1] 01:18–01:22`

### What the class commits you to

- **PLR** imposes the partially linear form
  $$
  Y = D\theta_0 + g_0(X) + \zeta, \quad \mathbb{E}[\zeta \mid D, X] = 0,
  $$
  $$
  D = m_0(X) + V, \quad \mathbb{E}[V \mid X] = 0.
  $$
  A single $\theta_0$ enters linearly. Nuisances are
  $\eta_0 = (\ell_0(X), m_0(X)) = (\mathbb{E}[Y \mid X], \mathbb{E}[D \mid X])$,
  and the score is the partialling-out (Frisch–Waugh–Lovell) score.
  `src: [Recap] p.7, p.12, p.15`
- **IRM** uses the doubly robust score, with separate outcome regressions for the
  two arms:
  $$
  \psi(\cdot) = g(1,X) - g(0,X) + \frac{D(Y - g(1,X))}{m(X)} - \frac{(1-D)(Y - g(0,X))}{1 - m(X)} - \theta.
  $$
  No linear-in-$D$ restriction. `src: [Recap] p.15`
- **APO** targets $\theta_d = \mathbb{E}[Y(d)]$ per treatment level, with
  $g(d,X) = \mathbb{E}[Y \mid D=d, X]$ and $m_d(X) = \mathbb{E}[\mathbf{1}\{D=d\} \mid X]$.
  `DoubleMLAPOS` combines levels and produces differences through
  `causal_contrast()`. `src: [Het] p.4–7`
- **DiD** targets $\mathrm{ATT}(g,t)$ and needs two further choices at construction:
  `control_group` (`never_treated` or `not_yet_treated`) and `anticipation_periods`.
  `src: [DiD] p.20, p.22, p.34`

The orthogonal score comes with the class — you do not derive it.
`src: [Intro] p.22`

## Failure modes

### Treatment type incompatible with the class `[BLOCKER]`
- **Symptom** `DoubleMLIRM` with a continuous treatment, or a categorical
  treatment passed to a binary-only class.
- **Why** IRM, DiD, sample selection and RDD are binary-treatment models; PLR and
  IIVM accept continuous or binary; potential-outcome models accept
  binary/categorical.
- **Fix** Move to a row of the table that admits the treatment type.
- `src: [Intro] p.28`

### Data structure incompatible with the class `[BLOCKER]`
- **Symptom** A cross-sectional class chosen for panel data, or DiD chosen for a
  single cross-section.
- **Why** DiD is the only panel / repeated-cross-section row; every other row is
  cross-sectional.
- **Fix** Match the row to the structure recorded at step 2.
- `src: [Intro] p.28`

### Estimand not available from the chosen class `[BLOCKER]`
- **Symptom** ATTE requested from PLR; APO/CAPO/GAPO requested from IRM; ATT
  requested from a cross-sectional class.
- **Why** Each row supports a specific estimand set. PLR gives ATE, CATE, GATE;
  ATTE requires IRM; potential-outcome estimands require the APO models; ATT
  requires DiD.
- **Fix** Change class, or change the estimand at step 0 and re-run this step.
- `src: [Intro] p.28`

### PLR with a binary outcome `[BLOCKER]`
- **Symptom** `DoubleMLPLR` where $Y$ is 0/1 — converted, churned, clicked.
- **Why** The PLR's additive form makes $\theta_0$ a constant shift in the
  *probability* of $Y$, the same shift at every covariate profile. That is a
  linear probability model, and for most applied problems it is not a sensible
  restriction. The residual-on-residual reading of the estimator goes with it: it
  is a consequence of the additive structure, not a general property of DML.
- **Fix** Use the IRM, whose doubly robust score models each arm separately and
  imposes no additivity, or the logistic version of the partially linear model.
- `src: [D1] 01:19–01:22`

### Identification strategy and class disagree `[BLOCKER]`
- **Symptom** Step 1 concluded that unconfoundedness fails and an instrument
  carries identification, but a PLR or IRM model is specified.
- **Why** PLR and IRM rest on selection-on-observables; the exclusion restriction
  is used by the IV row.
- **Fix** Use `DoubleMLIIVM`, or revisit step 1.
- `src: [Recap] p.4, [Intro] p.28`

### PLR chosen where heterogeneity matters `[WARNING]`
- **Symptom** A single $\theta_0$ is estimated, but the question is about who
  benefits, or the treatment is binary with plausibly different responses by arm.
- **Why** PLR writes the effect as $D\theta_0$ entering linearly with a common
  $g_0(X)$; IRM's doubly robust score models $g(1,X)$ and $g(0,X)$ separately. In
  learner terms this is S-learner versus T-learner: the PLR fits one outcome
  model with $D$ as a feature, the IRM fits one per arm — equivalent to
  interacting every covariate with the treatment. The S-learner's known weakness
  is exactly the one that matters here: where $X$ predicts the *level* of $Y$ far
  better than it modulates the effect of $D$, a single model spends its capacity
  on the level and captures little heterogeneity.
- **Fix** Use IRM for a binary treatment, and take heterogeneity through
  CATE/GATE at step 8.
- `src: [Recap] p.7, p.15, [D1] 02:11–02:15`

### Multi-valued treatment collapsed to binary `[WARNING]`
- **Symptom** Three or more treatment levels or types — no training / basic /
  advanced, drug A / B / C, email / SMS / phone — recoded as treated vs untreated.
- **Why** Collapsing discards the level structure; APOs give the expected outcome
  at each level, and `causal_contrast()` recovers pairwise differences.
- **Fix** Use `DoubleMLAPO` for one level, `DoubleMLAPOS` for several.
- `src: [Het] p.3–7`

### DiD control group and anticipation left at defaults silently `[WARNING]`
- **Symptom** `DoubleMLDIDMulti` constructed without a stated reason for
  `control_group` or `anticipation_periods`.
- **Why** The conditional-parallel-trends assumption is stated *relative to* the
  chosen control group — never-treated or not-yet-treated — and the anticipation
  window $\delta$ changes which pre-periods are admissible. The default is
  `anticipation_periods=0`, i.e. no anticipation.
- **Fix** Choose both deliberately and record the reasoning. `never_treated` is
  the wider pool but not automatically the better one: if units are never treated
  *for a reason* — they respond to nothing, they differ structurally in behaviour
  — that reason is also a reason their trend differs. Units treated later are
  often the more comparable control precisely because they were eventually
  treatable.
- `src: [DiD] p.20, p.22, p.34, [D2] 02:26`

### Effects requested far after treatment `[WARNING]`
- **Symptom** `gt_combinations` reaching several periods past treatment, with the
  long-horizon cells read the same way as the short-horizon ones.
- **Why** Every $\mathrm{ATT}(g,t)$ needs a pre-treatment baseline, and the
  baseline cannot move forward past the treatment date — so estimating an effect
  four periods out assumes trends stayed parallel across that whole span. The
  effect depends on the group and the evaluation period; the *strength of the
  assumption* depends on the pre-period, which is why the default takes the
  shortest one available. Short-horizon effects are the credible ones; the far
  cells of the grid are not more informative, they are more assumed.
- **Fix** Keep the default shortest baseline, and when reporting distant periods
  say that they rest on a longer parallel-trends span. Do not read a
  non-significant long-horizon cell as an effect fading.
- `src: [D2] 01:52, 02:29–02:32`

### Score function not recorded `[NOTE]`
- **Symptom** The class is named but the score is not.
- **Why** The score is what defines the estimand — the printed object reports
  `Score function:` (e.g. `ATE`, `observational`) and it should match step 0.
- **Fix** Record it now; step 7 checks the printed value against it.
- `src: [Intro] p.36, [DiD] p.36`

## Check mode — report format

```
**VERDICT** — n blockers, m warnings        (PASS | PROCEED WITH CAUTION | BLOCKED)

① <failure mode>                    [SEVERITY]
   observed   <what in the deliverable triggered it>
   fix        <what to do about it>

**Carry forward to step 4**
 • <facts step 4 needs>
```

Report only the modes that fired, most severe first.

## Carry forward to step 4 (`causal-4-ml-methods`)

- The model class and the score it uses
- The estimand it targets, and which estimands are now off the table
- Which nuisance functions it needs — this determines the learners:
  - PLR: `ml_l` for $\mathbb{E}[Y \mid X]$ (regression), `ml_m` for $\mathbb{E}[D \mid X]$
  - IRM / APO / DiD: `ml_g` (regression), `ml_m` (classification)
- For DiD: `control_group` and `anticipation_periods`

## Output style

Report in **Unicode math**, never LaTeX — write θ₀, ψ, η = (ℓ₀(X), m₀(X)), g(1,X),
𝔼[Y | X], ATT(g,t), not `\theta_0` or `$...$`. The LaTeX in this file is for reading
it in Obsidian; it must not appear in your output. Define every symbol on first use.
Bold the verdict. Keep it short.
