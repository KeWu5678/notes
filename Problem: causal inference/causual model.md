# General framework
## The Problem Fromulation
- Define the outcome (estimator), the treatment, and the confounders
- causal estimand ->  statistical estimand -> statistical estimator
                    (ATE in a RCT )

## causal assumptions and the DAG graph: 
1. (most important) selection-on-observables 
2. 0verlapping
3. no-unobserved-confounding

**the confounder**
**the mediator**
**the instrument variable**
**the post-treatment variable**


# Estimation approch
## A. Double Machine Learning
### modelling: Partial linear model
$$  Y = D \cdot \theta_0 + g_0(X) + \epsilon$$
$$  D = m_0(X) + V$$ 

Estimator: 
- $ g_0(X)$: baseline outcome
- $ m_0(X), V$: the treatment assignment
- $\theta_0$: treatment effect
 
We need learners for two nuisance functions:
- `ml_l`: Predicts $\mathbb{E}[Y|X]$ (outcome regression)
- `ml_m`: Predicts $\mathbb{E}[D|X]$ (treatment regression)

#### Bad control (too many confounders for ml_m)
The asymmetry between ml_l and ml_m:
- ml_l (predicts Y): more accurate is always better. Bias in g_hat propagates directly into u = Y - g_hat. No downside beyond overfitting, which cross-fitting handles.
- ml_m (predicts D): accuracy reduces bias, but the *choice of features* affects identification through Var(V).

Decompose D = m(X) + V, where V is the true exogenous residual. Then:
    v_hat = D - m_hat(X) -> V    (not zero)
    u_hat -> theta*V + epsilon
    Var(theta_hat) ~ Var(epsilon) / (n * E[V^2])

So SE depends on Var(V) — a property of the DGP, not the estimator. Adding a feature that strongly predicts D but is NOT a true confounder (does not affect Y except through D):
- Bias: unchanged (it was not a confounder)
- Var(V): shrinks (more of D is explained away)
- SE of theta_hat: grows

This is the "bad control" / near-instrument depletion problem.

Rule: include features that are confounders (affect both D and Y). Avoid features that strongly predict D without affecting Y — they only erode identification.

┌────────────────────┬──────────────────────────┬──────────────────────────┐
│      Concern       │     ml_l (predicts Y)    │     ml_m (predicts D)    │
├────────────────────┼──────────────────────────┼──────────────────────────┤
│ Better predictions │ Lower bias in theta_hat  │ Lower bias in theta_hat  │
│ Too many features  │ Only overfitting risk    │ Shrinks Var(V) -> wide CI│
└────────────────────┴──────────────────────────┴──────────────────────────┘

### model selection & cross fitting

### Inference

# Different estimation appoach
1. machine learning model 
what matters: the predictive power is what matters to the asymptotics. 
linear model baseline. 
#### orthogonality
orhogonal score. 
score function.?
#### good ML estimation
nuisance function. 
#### cross-fitting
all data is used for both training and estimation
2. inference


### work flow
#### 0. problem formulation
causal discovery step.
identification for the observational data (tool) -> unconfoundedness not hold -> IV. 
unconfoundedness (not testable)


#### 1. data-backend
#### 2. causal model selection
plot the distribution

group over covaraite:   more helpful to include many features. 
covariate selection:    look at the your standard error. 
                        normally 4 would be too many.
                        how to choose basis function: oracle version and cate version should be close. 
#### 3. ml method
#### 5. hyperparameter tuning
#### 6. estimation
#### 7. inference
sensitivity analysis




## Causal Random Forrest

### The random forrest (CART-tree)
training set:   subset of the samples by bootstrapping
loss:           
splitting:      greedy search
weights of the tree:    none

random forrest: not having the point prediction to all features. 


## Difference in Difference
### Assumption
- conditional parallel trends
#### causal esitmand
ATT(g, t) 

### Identification


### estimation