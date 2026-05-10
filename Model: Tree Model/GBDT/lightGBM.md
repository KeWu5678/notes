LightGBM


# Theory
## ensemble method 
In LightGBM (and gradient boosting in general), the model is an ensemble of many decision trees, not a single tree.

Tiny example:
- Start with an initial prediction (e.g., the average target).
- Tree 1 is trained to reduce current errors; its output is added to the model.
- Tree 2 is trained to reduce the remaining errors; added to the model.
- Repeat for many trees until you hit num_iterations or early stopping.

# API
### lightgbm.train
1. `fobj(preds, train_data) -> (grad,hess)`: to customize the loss

2. `learning rate`: Tree model is like the conditional gradient method. Each iteration it finds a best weak learner. The learning rate is the parameter we put before the weak learner. 

3. `num_iterations`
The maximam number of trees (weak learner).

4. `early_stopping_round = 330`
prevent overfitting and save computation effort. stop if the validation score hasn’t improved for 330 rounds.
*** Remark ***: This is not a model parameter; it only works when you pass a validation set to the training API and use the correct argument name (early_stopping_rounds in most LightGBM/Sklearn wrappers). A patience of 330 is fairly large and can prolong training after the best score.

*** num_leaves ***
number of the *** terminal *** prediction a tree can have, the main control of tree complexity in LightGBM’s leaf-wise growth. It leads to overfitting sometimes. 

num_leaves = 104
  -  104 is moderately high and allows fairly complex trees (subject to min_child_samples).

*** max_depth ***
*** each weak learner can use all the features ***. This parameter controls the maxiam depth of each weak learner. 

max_depth = 141
  - This is effectively “no limit” (LightGBM uses -1 for unlimited). In practice, num_leaves and min_child_samples will constrain depth more than this large value.

*** bagging_fraction ***
 bagging_fraction = 0.86498
  - Fraction of rows sampled when bagging is applied (row subsampling).
  - Reasonable; helps generalization when used regularly.

### LightGBM specific
*** min_child_samples ***
minimum number of samples in each prediction, a strong regularizer. It may not be strictly specific to LightGBM model, but lightGBM does only choose the data with steepest gradient. 

min_child_samples = 1500
    -Rough rule: the maximum possible leaves per tree is at most floor(n_samples / min_child_samples), additionally capped by num_leaves.

*** feature_fraction ***
For each tree the LightGBM only choose a fraction of features. 

feature_fraction = 0.34055
  - Fraction of features randomly sampled for each tree (column sampling).
  - Quite low, which reduces variance and speeds training but can underfit if many features are informative.


*** max_cat_threshold (255), max_bin (13) *** 

*** bagging_freq = 97 ***
  - Apply bagging every k-th tree; 0 disables bagging.
  - 97 means bagging is used only once every 97 trees, so the effect is very weak. Common values are 1–10 if you want consistent subsampling.


*** lambda_l1, lambda_l2 ***
regularization on leaf weights.

### effectiveness of the sample configuration
How this configuration is likely to behave:
1. Strong regularization from min_child_samples and low feature_fraction; very weak L1/L2.
2. Very slow learning (tiny learning_rate) with many rounds; training can be long, and early stopping patience is high.
3. Bagging is configured but rarely applied (bagging_freq=97), so you’re mostly training on all rows.
4. Appropriate if you have a very large dataset and want to avoid overfitting; on smaller datasets it will likely underfit and train longer than necessary.





## Questions 

USER: so the model tries to find a new tree that reduces the loss by the learning rate? if a new tree is found, then after 15000 iteration is loss is already zero long before, it shouldn't be right

USER: how many feature does a new tree contain to split

USER: what does bagging mean



"bagging_fraction": 0.8649757526645387,
"bagging_freq": 97,
"early_stopping_round": 330,
"feature_fraction": 0.3405503430211517,
"lambda_l1": 0.0005851323746090346,
"lambda_l2": 0.17780260727766548,
"learning_rate": 0.00840536045226818,
"max_bin": 271,
"max_cat_threshold": 13,
"max_depth": 141,
"min_child_samples": 1500,
"num_iterations": 15000,
"num_leaves": 104

"importance_type": "split" or "gain". While split means the number of split 