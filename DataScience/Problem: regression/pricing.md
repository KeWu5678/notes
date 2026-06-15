
# target & loss


## log transformation
*** why using the log transform of the price ***
The price is often right skewed and not symmetrically normal distributed, which voilated the assumption on SLM

### margin calculation 
margin = coeff * (price ** power)
The power is usually set to be 0.5 or lower. It flattens the profit margin for the high price cars

### the asymmetric loss
x = (pred - actual) / margin; where the margin is the error margin, the larger the margin, the less sensative we are the the erro. 

Q(x) = x^2  --> the MSE
P(x) = factor * sigmoid [ (x - pen_factor) / alpha ] 