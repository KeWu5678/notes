# Two-layer networks with the $\mathrm{ReLU}^k$ activation function: Barron spaces and derivative approximation

Reading notes for Li, Lu, Mathé, and Pereverzev, *Numerische Mathematik* 156, 319--344 (2024).

We need the higher order of ReLU function for derivative approximation. The derivative approximation is intrinsically ill-posed and we need to regularize if we are approximating with measured data. 

## 2.1 Barron spaces and Barron norms
This section defines the Barron norm. For the LQ loss we mainly interested in p = 2, we are basically approximating in the H2 space. 


**Q1. User:**

Why on page 326 do we have
$$
\|f\|_{B^k_{p,0}}
\leq c_{k,\rho}(f)
\left(
\int_{\{-1,1\}\times S_d}
|\bar a|^p(\|\bar b\|_1+|\bar c|)^{pk}
\,d\bar\rho
\right)^{1/p}
\leq c_{k,\rho}(f)?
$$

**Codex:**

Lemma 2 normalizes the parameters so that
$$
\bar a\in\{-1,1\},\qquad
(\bar b,\bar c)\in S_d,\qquad
\|\bar b\|_1+|\bar c|=1.
$$
Therefore
$$
|\bar a|^p=1,\qquad
(\|\bar b\|_1+|\bar c|)^{pk}=1.
$$
Since $\bar\rho$ is a probability measure,
$$
\int_{\{-1,1\}\times S_d}
|\bar a|^p(\|\bar b\|_1+|\bar c|)^{pk}
\,d\bar\rho
=1.
$$
The scalar $c_{k,\rho}(f)$ contains the scale removed from $(a,b,c)$.

**Q2. User:**

What does the combinatorial number in front of the partial derivative with multi-index mean?

**Codex:**

It is the falling factorial from repeated differentiation:
$$
\frac{k!}{(k-|\alpha|)!}
=k(k-1)\cdots(k-|\alpha|+1).
$$
For $u=b\cdot x+c$,
$$
\partial^\alpha u^k_+
=
\frac{k!}{(k-|\alpha|)!}\,
b^\alpha u^{k-|\alpha|}_+.
$$
The coefficient comes from the power rule. The multi-index contributes $b^\alpha$, while the total order $|\alpha|$ determines how much the exponent drops.

## 2.2 Approximation properties of extended Barron spaces

**Q1. User:**

Does Theorem 7 work only for bounded domains?

**Codex:**

Yes. As stated, Theorem 7 is a bounded-domain result. The proof needs a uniform bound for
$$
\|(\bar b\cdot x+\bar c)^j_+\|_{L^2(\Omega)}
$$
over normalized $(\bar b,\bar c)$ with $\|\bar b\|_1+|\bar c|=1$. This is true when $\Omega$ is bounded. On an unbounded domain, a ridge function can grow polynomially on a half-space and need not be in $L^2$.

**Q2. User:**

What if the domain is locally compact?

**Codex:**

Then the local statement holds:
$$
B^k_1 \subset H^k_{\mathrm{loc}}(\Omega).
$$
For every compact $K\subset\Omega$, the same proof gives an $H^m(K)$ bound. But global membership in $H^k(\Omega)$ need not hold if $\Omega$ is unbounded.

**Q3. User:**

On page 328, why can they move from
$$
\left(
\int_\Omega
\left(
\int_{\{-1,1\}\times S_d} |g_\theta(x)|\,d\bar\rho(\theta)
\right)^2 dx
\right)^{1/2}
$$
to
$$
\int_{\{-1,1\}\times S_d}
\left(
\int_\Omega |g_\theta(x)|^2\,dx
\right)^{1/2}
d\bar\rho(\theta)?
$$

**Codex:**

This is Minkowski's integral inequality:
$$
\left\|
\int g_\theta\,d\bar\rho(\theta)
\right\|_{L^2_x}
\leq
\int
\|g_\theta\|_{L^2_x}
\,d\bar\rho(\theta).
$$
It is the triangle inequality in $L^2$, not a separate Jensen argument for the square and square root.

**Q4. User:**

On page 330, why are the functions $g_i$ independent?

**Codex:**

The parameters
$$
(\bar a_i,\bar b_i,\bar c_i)
$$
are sampled i.i.d. from $\bar\rho$, and $g_i$ is a function only of the $i$-th sampled parameter. Therefore the random functions $g_i$ are independent as $H^m(\Omega)$-valued random variables.

**Q5. User:**

What does the paper mean by orthogonality of $g_i$ in $H^m(\Omega)$?

**Codex:**

The wording is compressed. The deterministic sampled functions are not generally orthogonal. What is used is zero cross-covariance of the centered random functions
$$
Z_i=\mathbb E g_i-g_i.
$$
Since $\mathbb E Z_i=0$ and the $Z_i$ are independent,
$$
\mathbb E\langle Z_i,Z_j\rangle_{H^m(\Omega)}=0,
\qquad i\neq j.
$$

**Q6. User:**

How do we get from equation (12) to equation (13)?

**Codex:**

Let
$$
Z_i=\mathbb E g_i-g_i.
$$
Then
$$
\mathbb E\left\|
\frac1n\sum_{i=1}^n Z_i
\right\|^2
=
\frac1{n^2}
\sum_{i,j=1}^n
\mathbb E\langle Z_i,Z_j\rangle.
$$
The cross terms vanish by independence and centering, so only the diagonal terms remain:
$$
\frac1{n^2}\sum_{i=1}^n\mathbb E\|Z_i\|^2
=
\frac1n\mathbb E\|\mathbb E g_1-g_1\|^2.
$$

**Q7. User:**

On page 331, why is
$$
f(x)=c_{k,\rho}(f)\sum_{s=1}^n
\bar\rho(P_s)\,
\mathbb E_{\mu_s}
\left[
\bar a(\bar b\cdot x+\bar c)^k_+
\right]
$$
equivalent to equation (10)?

**Codex:**

The sets $P_s$ are subsets of the parameter space
$$
\{-1,1\}\times S_d,
$$
not subsets of the physical domain $\Omega$. If they form a measurable partition, then for
$$
h_x(\theta)=\bar a(\bar b\cdot x+\bar c)^k_+,
$$
we have
$$
\int h_x\,d\bar\rho
=
\sum_s\int_{P_s} h_x\,d\bar\rho
=
\sum_s \bar\rho(P_s)\mathbb E_{\mu_s}[h_x].
$$
This is the law of total expectation.

**Q8. User:**

Does finite subcover mean each element is disjoint?

**Codex:**

No. A finite subcover may overlap. For the equality on page 331, the paper must implicitly use a disjoint measurable partition, or replace the cover by a disjoint refinement. Otherwise the integral would be double-counted.

**Q9. User:**

So in the paper are $\{P_1,\dots,P_n\}$ disjoint?

**Codex:**

They must be treated as disjoint, at least up to measure-zero overlaps, for the displayed equality to be correct. The word "covering" is imprecise there.

**Q10. User:**

Why does $N=\sum_s N_s$ satisfy $n\leq N\leq 2n$?

**Codex:**

They take
$$
N_s=\lceil n\bar\rho(P_s)\rceil.
$$
Since $\bar\rho$ is a probability measure and the $P_s$ partition the parameter space,
$$
\sum_s\bar\rho(P_s)=1.
$$
Also
$$
n\bar\rho(P_s)
\leq
\lceil n\bar\rho(P_s)\rceil
\leq
n\bar\rho(P_s)+1.
$$
Summing over $s=1,\dots,n$ gives
$$
n\leq N\leq 2n.
$$

**Q11. User:**

Why on page 332 do we get
$$
c_{k,\rho}(f)^2
\sum_{s=1}^n
\frac{\bar\rho(P_s)^2}{N_s}
\mathbb E_{\mu_s}
\left\|
\mathbb E_{\mu_s}g_{s,1}-g_{s,1}
\right\|_{L^2}^2?
$$

**Codex:**

It is the variance formula for independent stratified sample averages. For each stratum $s$, define
$$
Z_{s,t}
=
\mathbb E_{\mu_s}g_{s,1}-g_{s,t}.
$$
There are $N_s$ independent terms with weight
$$
\frac{c_{k,\rho}(f)\bar\rho(P_s)}{N_s}.
$$
Their total contribution is
$$
N_s
\left(
\frac{c_{k,\rho}(f)\bar\rho(P_s)}{N_s}
\right)^2
\mathbb E\|Z_{s,1}\|_{L^2}^2
=
c_{k,\rho}(f)^2
\frac{\bar\rho(P_s)^2}{N_s}
\mathbb E\|Z_{s,1}\|_{L^2}^2.
$$

**Q12. User:**

Does summing the constant $\mathbb E g_{s,1}$ have a name?

**Codex:**

Yes. It is called centering or mean-centering. In the context of Theorem 9, it is part of stratified sampling.

**Q13. User:**

Why can they replace $n^{-1-2/d}$ by $N^{-1-2/d}$ when $N\geq n$?

**Codex:**

Because also $N\leq 2n$. Let
$$
a=1+\frac2d.
$$
Then $n\geq N/2$, hence
$$
n^{-a}
\leq
2^aN^{-a}.
$$
The factor $2^a$ is absorbed into the generic constant.

## 3 Regularization under noisy measurements

**Q1. User:**

Why does the paper say Gaussian white noise cannot be treated by their Tikhonov functional?

**Codex:**

The paper assumes
$$
f^\delta\in L^2(\Omega),
\qquad
\|f-f^\delta\|_{L^2(\Omega)}\leq\delta.
$$
True Gaussian white noise is not an $L^2(\Omega)$ function; it is a random generalized function. Therefore $f+\delta\xi$ is generally not in $L^2(\Omega)$, and
$$
\|g-f^\delta\|_{L^2(\Omega)}^2
$$
is not defined.

**Q2. User:**

What is Gaussian white noise?

**Codex:**

Gaussian white noise is a random linear functional $\xi$ acting on test functions $\varphi\in L^2(\Omega)$ such that
$$
\xi(\varphi)\sim N(0,\|\varphi\|_{L^2(\Omega)}^2),
$$
and
$$
\mathbb E[\xi(\varphi)\xi(\psi)]
=
\langle\varphi,\psi\rangle_{L^2(\Omega)}.
$$
Formally, if $\{e_j\}$ is an orthonormal basis of $L^2(\Omega)$, then
$$
\xi=\sum_{j=1}^\infty Z_je_j,
\qquad
Z_j\sim N(0,1)
$$
with independent $Z_j$. This series does not converge in $L^2(\Omega)$.

**Q3. User:**

What is the input of white noise?

**Codex:**

The input is a test function $\varphi$, not a point $x$. For fixed $\varphi$, $\xi(\varphi)$ is one scalar Gaussian random variable. It is square-integrable as a random variable, but that does not mean $\xi$ is an $L^2(\Omega)$ function.

**Q4. User:**

For the value function $f$, what is the input of the white noise?

**Codex:**

The value function has point input $x\in\Omega$. White noise does not have a pointwise input $x$; it acts on test functions. With white-noisy observations one should interpret
$$
\langle f^\delta,\varphi\rangle
=
\langle f,\varphi\rangle+\delta\xi(\varphi),
$$
not
$$
f^\delta(x)=f(x)+\delta\xi(x).
$$

**Q5. User:**

If for every test function we get a Gaussian random variable, why is the noisy function not in $L^2$?

**Codex:**

One tested measurement is only a scalar observation. To be an $L^2(\Omega)$ function, white noise would need coefficients in an orthonormal basis with finite square sum. But for white noise,
$$
\xi(e_j)=Z_j,
\qquad
Z_j\sim N(0,1)
$$
independently, so the formal square norm would be
$$
\sum_{j=1}^\infty Z_j^2=\infty
$$
almost surely.

**Q6. User:**

On page 333, why is only the inner weight powered by $k$ in the penalty, not the outer weight?

**Codex:**

The paper uses the Barron-style penalty
$$
R(g)
=
\left(
\frac1n\sum_{i=1}^n
|a_i|(\|b_i\|_1+|c_i|)^k
\right)^2.
$$
This is scale-invariant under the $\mathrm{ReLU}^k$ homogeneity. If
$$
(b,c)\mapsto \lambda(b,c),
\qquad
a\mapsto a/\lambda^k,
$$
then
$$
\left|\frac a{\lambda^k}\right|
\bigl(\lambda(\|b\|_1+|c|)\bigr)^k
=
|a|(\|b\|_1+|c|)^k.
$$
This is different from the homogeneous weight-decay formulation in the thesis, which starts from a penalty such as
$$
|c|^p+r(\omega)^q.
$$
After optimizing over scale, that formulation gives an induced sphere penalty such as
$$
|c|^{2/(k+1)}
$$
for $p=q=2$. These are different regularizations.

**Q7. User:**

In Lemma 10, is the neuron number fixed?

**Codex:**

Yes. Lemma 10 fixes $n$ and minimizes over the fixed-width class $F_n$. It proves existence of a minimizer of
$$
J_\lambda(g),\qquad g\in F_n,
$$
not over all widths.
