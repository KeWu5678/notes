
# Distribution Specification
## the monotoncity constraints
## the seasonality



# Distribution Transformation
## target encoding 
For the categorical variable, there is no numerical value that indicates cardinality in a natural sense. We therefore assign it a value that indicates how strong it is correlated to the target. 
One word: For a category in a feature, it calculate the a posteriori mean of the given target within that category.
**drawbacks**: 
The feature sees the target, which induces the target leakage. 
**remedy**:
k-fold cross-encoding: taking the encoding statistics from other folds. 

## label encoding
Example: LightGBM
One word: assign the category with a integer but tell the model it is a category. So the model knows the feature doesn't have a order and split it by the subset. 

## embedding



# Feature Selection
### BERUTA
#### Different correlation concepts & Effect
- ***spurious correlation***
    - *** 1. driven by a confounder ***
    - *** 2. purely statistical ***
- *** real correlation *** 

In the tree model, the feature importance is biased by the correlation of the features. 
In particular, if features are randomly correlated, the model splits by one feature. 
So a important correlated feature may appear less important than a uncorrelated feature. 

#### Procedure
1. make a randomized copy of the original features to the dataset (Randomly shuffle (permute) the values in that copied column). 
2. evaluate the feature importance of the origina & randomized features.
3. Determine if each feature’s importance is greater than the maximum importance shown by the shadow features
4. If a feature’s importance is greater than the max of the shadow attributes a significant number of times (remember that we trained several random forests), then that feature is selected (p-value).


