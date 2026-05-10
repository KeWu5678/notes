# General framework
## The Problem Fromulation
- Define the outcome (estimator), the treatment, and the confounders
- causal estimand ->  statistical estimand -> statistical estimator
                    (ATE in a RCT )

## causal assumptions: 
1. (most important) selection-on-observables 
2. 0verlapping
3. no-unobserved-confounding

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