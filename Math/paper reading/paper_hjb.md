- Why do we need to assume the growth condition on the activation functions. 
```text
The weak-* convergence only ensures convergence evaluated on the continuous functions vanishing in the infinity. If the derivative is not in the class, in particular, if it attains no trivial value at the infinity. The duality breaks, in particular, the weak-* limit is may not be the minimizer. 
```
---
- Why do we need to impose the no-escape condition.
```text
Observing the Gateau derivative, locally p is bounded by alpha, alpha is marginal cost of inserting a neuron that is infinitely near the existing measure. 

If the no-escape condition isn't there, we can potentially incert an neuron that escapes to infinity. 
```
---

- Why in the new setting, it is not needed anymore
```text
The new setting tests the narrow convergence. By the moment penalty we get the minimizing sequence of measure is tight. Hence, a narrowly convergence subsequence exists. 

The profile is allowed to be any continuous function a priori.  We decompose the domain into the bounded part and the tail and evaluate each. On the bounded support, the limit is attained by the narrow convergence; on the tail part, it vanishes by the growth condition. 
```
---

- why the no-flat-face condition implied the no-escape condition

```text
Observing the profile, it decompose into the interior part and the boundary part (in term of D). For the interior part, it always vanishes since we are observing the scalar product of activation and r/ Hessian r. If p vanishes at infinity, the product vanishes w-a.s., and the scalar product vanishes. What left is the boundary term. 

The ridge activation evaluates along the ridge line as a -> infinity. It intersect the boundary on a nontrivial surface measure only if the boundary is also a flat line. 
```


## The Measure Theory: 
- why is the atom set at most countable?

- what measure admits a Hahn decomposition?
```text 
The Hahn decomposition require almost nothing for the underlying topology of the measure. It only needs to be a measurable space. 
It assumes property of the measure function: it need to be signed, real-valued, and scalar-valued.
```

- which measure admits the property: contiuity from above?
```text
Every finite positive measure. Non-finite measure may not have this property.
```

- what measure admits inner regularity?
```text
Inner regularity means a set's measure can be approximated by compact sets from inside. 
Basically all the Radon measure. If the measure is not finite, we need to be more careful
```

---



---
- what it the Urysohn'lemma, when do we need the tool of Urysohn function?
```text 
The Urysohn's lemma has different version. In the version we used: 
Given a locally compact Hausdorff space, K a compact with an open cover U. We can define a continuous function with compact support such that the function is constant 1 on K and 0 on U\K. 

The Urysohn functions are useful since we can construct the partition of unity (the norm) with that. 
```

--- 
- Radon measure and continuity from above. 

- The power of separability
1. For the Banach-Alaugnu.
2. For the Bochner measurability. 


# (Functional) Analysis
## Convexity
- Does supreme perserve continuity, i.e., is sup fn continuous for fn continuous 
```text
Supreme of continuous function is not continuous in general; 

Supreme perserve instead the lower semicontinuity, i.e., for gn l.s.c., sup gn is l.s.c. .
```
- Why do we need represent the functional into a form of a supreme of finite sum of test function (to prove the weak-* l.s.c.)
```text
given un -> u weakly, we have for the **finite sum** of fj: lim_n int fj un = int fj u, which would fail if the representation is tested with a infinite sum. 

Furthermore, the supreme perserve the l.s.c.. Hence: 
sup ( Phi_F ) is l.s.c. if every Phi_F is l.s.c. 
Here Phi_F is l.s.c.

```

- What is a sufficient condition for the finite subadditivity to hold for countable sum?
```text
For the finite subadditivity to hold for the infinite sum, a sufficient condition is that limits on both sides exist. 
```

- Does finite subadditivity imply the countable subadditivity?
```text
Splitting $A=A_N+t_N$ (partial sum + tail) gives $\phi(A)\le\sum_{j\le N}\phi(a_j)+\phi(t_N)$, so the exact criterion is $\liminf_{r\downarrow0}\phi(r)=0$. It can only fail when $\phi(0+)$ does not exist: if $\phi(0+)=c>0$ then $\sum_j\phi(a_j)=\infty$ anyway.

Counterexample: $\phi=0$ on $\mathbb Q$, $\phi=1$ on $\mathbb R\setminus\mathbb Q$ is finitely subadditive. Take $a_j>0$ rational with $A=\sum_j a_j$ irrational; then $\sum_j\phi(a_j)=0<1=\phi(A)$, since every tail $t_N$ is irrational.

Under the paper's hypotheses $\phi$ is nondecreasing with $\phi(r)\le L_\phi r$, so $\phi(0+)=0$ and the countable extension is automatic.
```


## Strong measurablity
1. definition: strong measurablity assume the strong norm convergence in the Banach space. 
It means a Banach-space-valued function can be approximated by function with finitely many values (simple functions)
2. sufficient condition: Petti


## Compactness
- For continuous function vanishing at infinity, is every superlevel set compact?






# Optimization
## Measure-theoritical optimization
- The conditional gradient: how can we decide, which node (functional) to insert?


- why does the proximal algorithm solves the nonsmooth optimization problems. 

- what is the step size the proximal algorithm



# The dynamic System
- In the pendulum example， we don't have fixed time horizon, how do we solve the open-loop problem. 
```text
Generate the characteristic curve:
1. Set the equilibrium. 
2. Linearize the system (ODE) around the equilibrium
3. We get V(x) = x^T P x with P solved by the Ricatti equation and x is around that equilibrium. 
4. Solve for x with V(x) < epsilon. We get the final state x and and costate p = 2Px.
5. We backward integrate to get the characteristic curve; note that the optiaml value V is also obtained by the DP.

1. set the level of V; calculate the Contour. 
2. shift the contour by 2pi (it produces the value contour with target at 2pi). The intersection suggest the optimal value is the same from the intersect to the target 0 and pi, which suggest the costate (the gradient of V) is different. 
(Remark: the smoothness is only established numerically by the author) 
```


## NOTES
1. note where you are incorperating and where you are yourself (where you). Also in the introduction
2. numerics: comparison, also the optimal control; when the time goes to infinity? openloop cost
3. ai 


