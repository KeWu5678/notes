
# BINARY TARGET 
## Target & Loss
- what is the distribution of the target. 
        1. does the target suffer from the time-shift/distribution shift. 
        2. does the target suffer from sample imbalance. 
- loss: Log loss = - [ y log(p) + (1 - y) log( 1 - p) ].

## Training
### Recalibration
ranking is unchanged, the distribution (shape and drift) can be changed. 

## Metrics
A:  It is the true positive rate (true prediction over all true labels) against the false positive rate (false positive over all the false labels).
        It measures how well the model *** ranke positive above negatives ***
PR-AUC:  It is the precision (true prediction over all prediction) over the against (true prediction over all true label).
        It measures *** the quality of the positives ***. 


# MULTICLASS TARGET     
## Target
- Loss (the cross-entropy): 
1. L_i = sum q_i log (p_i); where q_i is the true distribution (true label)p_i = log (z_i) /  sum log(z_j); z_j is the output of the model. 
2. Encoding of the target. For the ordinality agonistic targe, the one-hot encoding (the label encoding) is implied, i.e., the q_i is 1 when the lable is i and 0 otherwise. We have for (x_i, y_i) the loss: - z_i(x_i) + LSE[ z(x_i) ]


