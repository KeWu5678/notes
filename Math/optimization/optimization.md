### General
- what is adjoint?

- The most basic method of all is the steepest gradient method. What are the drawbacks and what variants do we invent to address it. 
1. the zig-zage behavior. 

2. the problem is not smooth (but convex).
- why does the generalized derivative (Hessian) exists?
The derivative may not be continuous, but nevertheless they may admit explicit form, like the soft thresholding. 


### LP
the linear constraints defines a simplex. The simplex method moves around the extremal points and find the optimal one. 


### Nonsmooth optimization




### MILP
First we see the solver in the most naive way: 
#### relax-and-approximate
1. for all possible configurations (vector of binaries), we assign a weight. the weights are nonnegative and sum-up-to-1. 
2. we now optimize w.r.t. the alpha, and the optimization problem becomes continuous (not necessarily convex). 
3. **CIAP**: after solving the optimal alpha, we need to recover the control combination that satisfies the discrete constraints. 
We calculate the discrepency of the each combination and optimal alpha and integrate over entire time interval. 
The combination with minimal value is choosen. 
4. **dwell-time** constraint: the switch can not be on/off too often, therefore we should test if the combination satisfies this constraints. 

The prolem being: The CIAP solves the optimal solution near the **continuous profile**, i.e., it convexify the constraints and find the nearest feasible point in the **Euclidean sense**. 
But local structure of the constraint problem can be very nonconvex or steep. 


**In general, we resolve the integrality constraints using some form of tree-search strategy**. We create a min **heap**, each node stores: 
1. the discrete control to split. 
2. 

#### branch-and-bound. 
- branching: 
branching is 
1. strong branching: 
2. pseudocost branching: 
- bound: 
1. global-uppper-bound:
2. node-lower-bound:


### multitree methods
The problem of the branch-and-cut is that it involves solving a lot of NLP problems

#### outer approximation. 
The idea is to replace the NLP with a sequence of MLIP, such that we can warm-start.  In the outer



 
