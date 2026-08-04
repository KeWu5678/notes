---
description: Glossary for the causal-inference skill set — the canonical meaning of each term used across the nine skills.
---

# CONTEXT

Glossary for the `causal-inference` skill set. One meaning per term. If a skill
uses a term differently, the skill is wrong.

## Terms about the skills themselves

**Step** — one of the nine numbered guardrails, `0-problem-formulation` through
`8-inference`. A step is a place you stand in an analysis, not a stage that runs.

**Deliverable** — the single artifact a step is responsible for. Every step has
exactly one. A step with no nameable deliverable is not a step.

**Check mode** — the user brings a deliverable; the skill audits it against that
step's failure modes and reports. The skill does not produce the deliverable.

**Produce mode** — the user brings a prompt; the skill produces that step's
deliverable. It still reports the failure modes that apply to what it produced.

**Failure mode** — a named way a step's deliverable goes wrong, carrying an
observable symptom, a mechanism, a fix, and a severity. Not a general caution: if
it has no symptom you could observe, it is not a failure mode.

**Severity** — `[BLOCKER]` (do not proceed), `[WARNING]` (proceed only knowingly),
`[NOTE]` (awareness only).

**Inputs required** — facts a step needs from earlier steps before it can judge
anything. The skills hold no state between invocations, so these are asked for,
never inferred. If they are missing the skill asks and stops.

**Carry forward** — the facts the human must hand to the next step. The counterpart
of *inputs required*. State lives in the human and the conversation, not on disk.

**Source-traceable** — supported by the workshop material: one of the seven
lecture PDFs, cited as `src: [Key] p.N`, or one of the two session transcripts,
cited as `src: [D1] hh:mm`. The only admissible kind of claim in these skills.
A transcript citation claims the point was made there, not the exact wording.

## Terms about causal inference

**Causal model** — *avoid this term unqualified.* It is overloaded across the
source material and this vault. Use one of:

- **Structural model** — the DAG and the identification assumptions it encodes:
  what is a confounder, what is a mediator, what is unobserved. Lives at step 1.
  Answers "is this effect identified at all?"
- **Model class** — the `DoubleML*` object: `DoubleMLPLR`, `DoubleMLIRM`,
  `DoubleMLAPO`/`APOS`, `DoubleMLIIVM`, `DoubleMLDIDMulti`, `DoubleMLQTE`, … Lives at
  step 3. Answers "given identification, which estimator?" This is what the decks
  call "Causal Model" in the workflow list ([Intro] p.31).

Two different objects, two different failure modes, two different steps.

**Estimand** — the causal quantity you are after, defined before any estimator is
chosen: ATE, ATTE/ATT, APO, CATE, GATE, CAPO, GAPO, LATE, QTE. A number without a
stated estimand is not an answer ([Intro] p.28).

**Identification** — the argument that the estimand is recoverable from the
observed distribution under stated assumptions. Precedes estimation and is not
fixed by better ML. "Causality comes from identification" ([Recap] p.4).

**Nuisance function** — a conditional expectation the estimator needs but does not
report: $\ell_0(X) = \mathbb{E}[Y \mid X]$, $m_0(X) = \mathbb{E}[D \mid X]$,
$g_0(d, X) = \mathbb{E}[Y \mid D = d, X]$. Denoted $\eta$ collectively
([Recap] p.12, p.15).

**Score** — the moment function $\psi(W; \theta, \eta)$ whose root defines the
estimator, $\mathbb{E}[\psi(W; \theta_0, \eta_0)] = 0$ ([Recap] p.14).

**Neyman orthogonality** — the property $\partial_\eta \mathbb{E}[\psi(W; \theta_0, \eta)]\big|_{\eta=\eta_0} = 0$,
which makes the moment condition insensitive to small errors in $\hat\eta$ and
removes the first-order effect of ML regularization bias ([Recap] p.14–15).

**Cross-fitting** — sample splitting where each observation's nuisance prediction
comes from a model trained without it, with the roles of the folds swapped so all
data is used for both training and estimation ([Intro] p.24, [Recap] p.17).

**Trimming** — dropping or bounding observations with extreme propensity scores.
Recommended in the IRM, where propensity score predictions can render results —
including the sensitivity analysis — unstable ([Sens] p.35).

**Overlap / common support** — the requirement that treated and control units with
similar covariates both occur with positive probability ([DiD] p.23).

**Intent-to-treat (ITT)** — the effect of *being offered* or *being eligible for*
a treatment, rather than of taking it up. The estimand you get when $D$ is the
assignable thing and take-up is the unit's own choice ([D1] 01:40).

**Effect modifier** — a covariate the treatment effect varies with. Distinct from
a confounder: a confounder need not modify the effect, and an effect modifier
need not be causal at all — heterogeneity with respect to it is a correlational
statement ([D2] 00:25–00:26).

**Interference / spillover** — treating one unit changes another unit's outcome.
It contaminates the control group, so the identification argument no longer says
what would have happened without treatment ([D2] 02:37–02:38).

**Anticipation** — units changing behaviour before treatment is assigned, because
they know it is coming. Distinct from a parallel-trends violation, and handled
differently: shift the treatment time back, or raise `anticipation_periods`
([D2] 02:21–02:24).

**Placebo test** — an $\mathrm{ATT}(g,t)$ estimated at an evaluation period
*before* treatment, which should be near zero if trends were parallel. Evidence
about the pre-period only; it does not establish that trends stay parallel after
treatment ([D2] 02:12).
