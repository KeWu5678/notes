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
---


## The Measure Theory: 

---
- what measure admits a Hahn decomposition?
```text 
The Hahn decomposition require almost nothing for the underlying topology of the measure. It only needs to be a measurable space. 
It assumes property of the measure function: it need to be signed, real-valued, and scalar-valued.
```
---

- what measure admits inner regularity?
```text
Basically all the Radon measure. If the measure is not finite, we need to be more careful
```

--
- what it the Urysohn'lemma, when do we need the tool of Urysohn function?
```text 
The Urysohn's lemma has different version. In the version we used: 
Given a locally compact Hausdorff space, K a compact with an open cover U. We can define a continuous function with compact support such that the function is constant 1 on K and 0 on U\K. 

The Urysohn functions are useful since we can construct the partition of unity (the norm) with that. 
```
