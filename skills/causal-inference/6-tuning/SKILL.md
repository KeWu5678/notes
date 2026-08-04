---
name: causal-6-tuning
description: Run or audit hyperparameter tuning of nuisance learners with tune_ml_models() and Optuna — parameter spaces as callables, search-space types, optuna_settings, pipeline parameter paths, and reading the resulting studies. Use when tuning ml_g / ml_m before a DML fit, when writing an Optuna trial callable, or when tuned and untuned estimates differ and the tuning needs checking.
---

# 6. Hyperparameter tuning

**Deliverable** — tuned hyperparameters set on the model, with the tuning results
inspected rather than assumed.

Predictive performance of the nuisance learners directly affects the bias of the
causal estimate, its standard errors, and the width of the confidence intervals.
Default hyperparameters are rarely optimal for a specific dataset.
`src: [Tune] p.3`

## Inputs required

Ask for these; do not guess:

1. From step 5: the instantiated model object and its `params_names`.
2. From step 4: the learners, and whether they are plain estimators or pipelines.
3. The compute budget — it sets `n_trials`.
4. Whether an untuned baseline fit exists to compare against.

## Procedure

1. **Define parameter spaces as callables** taking an Optuna `trial` object and
   returning a dict, one per learner. `src: [Tune] p.6`

   ```python
   def ml_g_params(trial):
       return {
           'n_estimators': 100,
           'learning_rate': trial.suggest_float('learning_rate', 0.001, 0.1, log=True),
           'min_child_samples': trial.suggest_int('min_child_samples', 20, 50, step=10),
           'lambda_l1': trial.suggest_float('lambda_l1', 1e-2, 10.0, log=True),
           'lambda_l2': trial.suggest_float('lambda_l2', 1e-2, 10.0, log=True),
       }
   ```

2. **Pick the right search-space type.** `src: [Tune] p.7`

   | Method | Values | Example |
   |---|---|---|
   | `suggest_float` | continuous | `trial.suggest_float('lr', 0.001, 0.1, log=True)` |
   | `suggest_int` | integer | `trial.suggest_int('depth', 2, 10)` |
   | `suggest_categorical` | categorical | `trial.suggest_categorical('kernel', ['rbf', 'linear'])` |

   Use `log=True` for parameters varying over orders of magnitude; `step` for
   discrete increments.

3. **Tune.** `src: [Tune] p.8`

   ```python
   param_space = {'ml_g': ml_g_params, 'ml_m': ml_m_params}
   optuna_settings = {'n_trials': 100, 'show_progress_bar': True,
                      'verbosity': optuna.logging.WARNING}

   dml_obj_tuned.tune_ml_models(
       ml_param_space=param_space,
       optuna_settings=optuna_settings,
   )
   ```

4. **Fit.** Best hyperparameters are set automatically; proceed with the standard
   `fit()` call. `src: [Tune] p.9`

   The search itself runs on its own cross-validated splits, separate from the
   folds `fit()` later cross-fits over — so tuning does not leak the estimation
   folds' data into the hyperparameter choice. `src: [D1] 02:07`
5. **Inspect.** `dml_obj.params_names` shows the internal learners — for IRM,
   `['ml_g0', 'ml_g1', 'ml_m']`: outcome model for control ($D=0$), outcome model
   for treated ($D=1$), and the propensity score. Each is tuned separately with the
   same parameter space, and identical hyperparameters are set for every
   cross-fitting fold — deliberately. `src: [Tune] p.10–11, [D1] 02:13`
6. **Read the results.** Pass `return_tune_res=True` to get the studies; inspect
   best score and parameters, `study.trials_dataframe()`, and the Optuna plots
   (optimization history, parameter importances, parallel coordinates).
   `src: [Tune] p.19–24`
7. **Compare tuned against untuned** on `evaluate_learners()` and on the estimate
   itself. `src: [Tune] p.12–13`

### Settings reference `src: [Tune] p.27`

| Setting | Description | Default |
|---|---|---|
| `n_trials` | number of optimization trials | 100 |
| `show_progress_bar` | display progress | False |
| `verbosity` | logging level | WARNING |
| `sampler` | sampling strategy | `TPESampler` |
| `pruner` | early stopping strategy | `MedianPruner` |

For pipelines, use double-underscore notation for nested parameters, and
learner-specific overrides in `optuna_settings` (more specific settings win).
`src: [Tune] p.16–17`

## Failure modes

### Parameter space not a callable `[BLOCKER]`
- **Symptom** A plain dict of values or lists passed as `ml_param_space`.
- **Why** Parameter spaces are defined as callables using Optuna's `trial` object;
  a static dict defines no search.
- **Fix** Wrap it in a function of `trial` returning the dict.
- `src: [Tune] p.6`

### Pipeline parameters addressed without `__` paths `[BLOCKER]`
- **Symptom** `'learning_rate'` given for a learner that is a `Pipeline` or
  stacked estimator.
- **Why** Nested parameters are reached through double-underscore notation, e.g.
  `'stacking__lgbm__learning_rate'`, `'stacking__final_estimator__alpha'`.
- **Fix** Write the full parameter path.
- `src: [Tune] p.16`

### Hyperparameters retuned inside each cross-fitting fold `[WARNING]`
- **Symptom** A hand-rolled loop tuning per fold, or an expectation that each
  fold should get its own best parameters because that would be "more optimal".
- **Why** It is possible and is explicitly not recommended. Per-fold tuning makes
  the learner a different function on each fold, so the pooled nuisance
  predictions no longer come from one model, and each fold's parameters are fitted
  to that fold's noise — added variance bought with no reduction in bias.
- **Fix** Tune once through `tune_ml_models()` and let the chosen parameters apply
  to every fold.
- `src: [D1] 02:13`

### Untuned defaults carried into the estimate `[WARNING]`
- **Symptom** `fit()` called with bare learners on a dataset where defaults were
  never checked.
- **Why** The deck's own comparison, on data with a true effect of 0.5: untuned
  gives $\hat\theta = 0.062$ with $\mathrm{se} = 0.878$ and a confidence interval
  spanning zero; tuned gives $\hat\theta = 0.464$ with $\mathrm{se} = 0.148$. Same
  model, same data.
- **Fix** Tune, or record that defaults were checked and accepted.
- `src: [Tune] p.3, p.12`

### Order-of-magnitude parameters searched on a linear scale `[WARNING]`
- **Symptom** Learning rates or regularization strengths sampled with
  `suggest_float(..., 0.001, 10.0)` and no `log=True`.
- **Why** `log=True` exists for parameters that vary over orders of magnitude;
  without it the search concentrates on the top of the range.
- **Fix** Add `log=True`.
- `src: [Tune] p.7`

### Tuning results never inspected `[WARNING]`
- **Symptom** `tune_ml_models()` run, `fit()` called, results reported — no best
  score, no trials examined, no learner evaluation.
- **Why** The tuning result is evidence about nuisance quality, which is what the
  causal estimate depends on. `return_tune_res=True` exposes the studies; the
  optimization history shows whether the search converged, and the parameter
  importances show whether the space was worth searching.
- **Fix** Inspect the studies and compare `evaluate_learners()` before and after.
- `src: [Tune] p.13, p.19–24`

### Trial budget cut without saying so `[NOTE]`
- **Symptom** `n_trials` well below the default of 100, or key parameters pinned to
  fixed values.
- **Why** The decks pin `n_estimators` explicitly to keep slide execution fast — a
  presentation convenience, not a recommendation.
- **Fix** Note the budget alongside the result, and do not read a truncated search
  as evidence that the space was explored.
- `src: [Tune] p.6, p.27`

### One space reused across internal learners `[NOTE]`
- **Symptom** A single `ml_g` space, unaware that it applies to both `ml_g0` and
  `ml_g1`.
- **Why** Each internal learner is tuned separately but with the same parameter
  space; the control-arm and treated-arm outcome models get the same search range.
  Under unbalanced assignment they are fitted on very differently sized
  subsamples, so a range that suits the large arm can be wrong for the small one —
  the tuner will return quite different parameters for each, which is the intended
  behaviour, but only if the shared range covers both.
- **Fix** Informational — but if the arms differ substantially in size, widen the
  range so it spans both, and check both fits at step 7 rather than assuming the
  shared space suited each.
- `src: [Tune] p.10, [D1] 02:13`

## Check mode — report format

```
**VERDICT** — n blockers, m warnings        (PASS | PROCEED WITH CAUTION | BLOCKED)

① <failure mode>                    [SEVERITY]
   observed   <what in the deliverable triggered it>
   fix        <what to do about it>

**Carry forward to step 7**
 • <facts step 7 needs>
```

Report only the modes that fired, most severe first.

## Carry forward to step 7 (`causal-7-estimation`)

- Which learners were tuned, over which spaces, with what `n_trials`
- Best scores and the scoring method per learner
- The untuned baseline, if one exists, for comparison
- Anything pinned rather than searched

## Output style

Report in **Unicode math**, never LaTeX — write θ̂, se, ml_g0, ml_g1, ml_m, not
`\hat\theta` or `$...$`. The LaTeX in this file is for reading it in Obsidian; it
must not appear in your output. Define every symbol on first use. Bold the verdict.
Keep it short.
