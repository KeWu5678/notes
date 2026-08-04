---
name: causal-2-data-backend
description: Build or audit the DoubleMLData / DoubleMLPanelData object — declaring which columns are outcome, treatment, covariates, time and unit id, and checking the container matches the data structure. Use when setting up y_col / d_cols / x_cols / t_col / id_col, when a dataframe must become a DoubleML data backend, or when the printed data summary disagrees with what was intended.
---

# 2. Data-backend

**Deliverable** — a `DoubleMLData` or `DoubleMLPanelData` object whose printed
summary matches the roles agreed at steps 0 and 1.

This step is deliberately narrow: it declares roles. It does not decide which
variables belong in $X$ — that was step 1.

## Inputs required

Ask for these; do not guess:

1. From step 1: the identification assumption, the covariate set $X$, and whether
   the design is cross-sectional, panel, or repeated cross-sections.
2. The dataframe's column names.
3. For panel data: which column holds the **first treatment period** per unit,
   which holds time, and which holds the unit id.

## Procedure

### Cross-sectional

Declare the roles for treatment, outcome and controls. `src: [Intro] p.30`

```python
from doubleml.data import DoubleMLData

dml_data = DoubleMLData(
    data,
    y_col='net_tfa',
    d_cols='e401',
    x_cols=['age', 'inc', 'educ', 'fsize', 'marr',
            'twoearn', 'db', 'pira', 'hown'],
)
```

### Panel / repeated cross-sections

Data goes in **long format**, one row per unit-period. `src: [DiD] p.29`

```python
from doubleml.data import DoubleMLPanelData

dml_panel_data = DoubleMLPanelData(
    df,
    y_col="Y",
    d_cols="G",        # group variable: the period the unit is FIRST treated
    t_col="year",
    id_col="id",
    x_cols=["lpop", "lavg_pay", "region_2", "region_3", "region_4"],
)
```

Arguments: `data` (long format), `y_col`, `d_cols` (group variable indicating first
treatment period), `t_col`, `id_col`, `x_cols` (covariates for the conditional
trend). `src: [DiD] p.30`

### Then verify

Print the object and read the data summary back — outcome, treatment, covariates,
instruments, number of observations, and for panel data the time and id variables
and the unique-id count. `src: [Intro] p.36, [DiD] p.31`

## Failure modes

### Panel data in a cross-sectional container `[BLOCKER]`
- **Symptom** Unit-period observations passed to `DoubleMLData`; no `t_col` or
  `id_col` declared.
- **Why** DiD estimation requires `DoubleMLPanelData`; the panel structure is what
  the conditional-trend nuisance is defined over.
- **Fix** Rebuild as `DoubleMLPanelData` with `t_col` and `id_col`.
- `src: [DiD] p.30`

### `d_cols` set to the 0/1 treatment indicator in a panel `[BLOCKER]`
- **Symptom** In a panel setup, `d_cols` points at $D_{i,t}$ — treated-now — rather
  than at the group variable $G_i$.
- **Why** For panel DiD, `d_cols` is the **group** variable: the period in which the
  unit is first treated ($G_i = \infty$ for never-treated). It is not the
  period-by-period indicator.
- **Fix** Point `d_cols` at the first-treatment-period column.
- `src: [DiD] p.17, p.30–31`

### Panel data not in long format `[BLOCKER]`
- **Symptom** One row per unit with a column per period (wide).
- **Why** The panel backend expects unit-period observations.
- **Fix** Reshape to long before constructing the object.
- `src: [DiD] p.29`

### Roles not verified after construction `[WARNING]`
- **Symptom** The object is built and immediately used; the printed summary was
  never read.
- **Why** A mistyped or silently dropped column changes what is being estimated
  and produces no error. The summary is the only place the declared roles are
  visible.
- **Fix** `print(dml_data)` and check outcome, treatment, covariate list and
  observation count against steps 0 and 1.
- `src: [Intro] p.36, [DiD] p.31`

### Sampling is not i.i.d. `[WARNING]`
- **Symptom** Clustered, repeated, or otherwise dependent observations presented
  as a random sample. The common case is a time series in cross-sectional
  clothing: weekly spend and weekly sales, one row per week, handed to
  `DoubleMLData`.
- **Why** The cross-sectional settings assume independent units, and the panel
  setting states random sampling explicitly. Serial dependence violates it, and
  carryover in the treatment itself — a campaign whose effect is large in the
  first period and decays after, while exposure piles up — means this period's
  $D$ is not separable from previous periods'.
- **Fix** Confirm the sampling scheme, or say plainly that the assumption is
  imposed rather than met. Where the dependence is over time, take it back to
  step 0: dynamic treatment effects are a different estimand, and step 3 may need
  the panel row.
- `src: [DiD] p.19, [D2] 01:14–01:15`

### One covariate vector serves every nuisance `[NOTE]`
- **Symptom** A variable added to `x_cols` to help one nuisance model — usually
  something that sharpens the propensity score.
- **Why** `x_cols` is a single feature vector used for the outcome regression and
  the treatment regression alike. There is no per-learner feature set, so a
  variable added for one model enters both, with whatever consequences it carries
  there.
- **Fix** Justify each column against the graph (step 1), not against a
  particular nuisance fit. Where a variable predicts only $D$, step 1's
  near-instrument warning applies.
- `src: [D1] 01:51, 01:54`

## Check mode — report format

```
**VERDICT** — n blockers, m warnings        (PASS | PROCEED WITH CAUTION | BLOCKED)

① <failure mode>                    [SEVERITY]
   observed   <what in the deliverable triggered it>
   fix        <what to do about it>

**Carry forward to step 3**
 • <facts step 3 needs>
```

Report only the modes that fired, most severe first.

## Carry forward to step 3 (`causal-3-model-class`)

- The data structure: cross-sectional, panel, or repeated cross-sections
- Treatment type: binary, multi-valued, or continuous
- The estimand from step 0, unchanged
- Whether an instrument column exists

## Output style

Report in **Unicode math**, never LaTeX — write Y, D, X, G_i, 𝔼[·], not `$...$`.
The LaTeX in this file is for reading it in Obsidian; it must not appear in your
output. Define every symbol on first use. Bold the verdict. Keep it short.
