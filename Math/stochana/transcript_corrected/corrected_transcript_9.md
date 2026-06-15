# Clean transcript for recording 9

Sources:

- `original_transcript/Erwin-Schrödinger-Zentrum 9.txt`
- `lecture notes/Chapter2-updated.pdf`

Style note: this is a cleaned transcript, not a word-for-word transcript. Repetitions, false starts, and unrecoverable filler have been removed. Mathematical terms and notation have been corrected against the lecture notes and written in LaTeX.

## Summary and lecture-note correspondence

This recording explains Donsker's invariance principle as a construction of Brownian motion from rescaled random walks. Starting with i.i.d. random variables $(X_k)$ with mean $0$ and variance $1$, we form

$$S_n(t)=\frac{1}{\sqrt n}\sum_{k=1}^{\lfloor nt\rfloor}X_k.$$

The finite-dimensional distributions converge by the central limit theorem. Since $S_n$ is a step function, it is replaced by its linear interpolation $S_n^*$, which takes values in $C([0,1],\mathbb{R})$. Slutsky's theorem shows that this interpolation does not change the finite-dimensional limit. The remaining task is tightness of the laws of $S_n^*$ on $C([0,1],\mathbb{R})$.

The core technical tools are:

1. Prohorov's theorem: weak relative compactness is equivalent to tightness on Polish spaces.
2. Arzela-Ascoli: compactness in $C(K,S)$ is controlled by pointwise compactness and the modulus of continuity.
3. The tightness criterion:

   $$\lim_{h\downarrow 0}\sup_n \mathbb{E}[w(X_n,h)\wedge 1]=0.$$

4. Ottaviani's inequality: running maxima of random walks can be controlled by the tail of the final value.

Together these show

$$S_n^* \Rightarrow B$$

in $C([0,1],\mathbb{R})$, where $B$ is Brownian motion and the limiting law is the Wiener measure.

This recording corresponds to the end of `Chapter2-updated.pdf`, not to `Chapter3.pdf`. The relevant lecture-note parts are:

1. Section 2.3.2, "Weak convergence of probability measures on $C([0,1],\mathbb{R})$": weak convergence on path space, finite-dimensional distributions, Arzela-Ascoli, and the tightness criterion

   $$\lim_{h\downarrow 0}\sup_n \mathbb{E}[w(X_n,h)\wedge 1]=0.$$

2. Section 2.3.3, "Donsker's invariance principle": the rescaled random walk $S_n$, the linearly interpolated process $S_n^*$, Ottaviani's inequality, and the proof that $S_n^*$ is tight.

`Chapter3.pdf` starts after this construction. It assumes Brownian motion is already available and begins the next topic: quadratic variation and the basic Ito formula. So the relation is sequential in the lecture notes:

$$
\text{Chapter 2: construct Brownian motion as the weak limit of } S_n^*
\quad\longrightarrow\quad
\text{Chapter 3: study quadratic variation and Ito calculus for Brownian paths}.
$$

## Corrected transcript

We continue with the construction of Brownian motion from rescaled random walks. Let $(X_k)_{k \ge 1}$ be i.i.d. real-valued random variables on some probability space $(\Omega,\mathcal{F},P)$, normalized by

$$\mathbb{E}[X_k] = 0, \qquad \mathbb{E}[X_k^2] = 1.$$

Define the rescaled random walk

$$S_n(t) := \frac{1}{\sqrt{n}}\sum_{k=1}^{\lfloor nt \rfloor} X_k,$$

where

$$\lfloor x \rfloor := \max\{k \in \mathbb{Z}: k \le x\}$$

is the Gauss bracket. Thus $S_n$ is constant on intervals of length $1/n$ and jumps at the grid points $k/n$.

The central limit theorem already tells us what happens to increments. For times

$$0 \le t_0 < t_1 < \cdots < t_N,$$

the vector

$$\bigl(S_n(t_1)-S_n(t_0),\ldots,S_n(t_N)-S_n(t_{N-1})\bigr)$$

converges in distribution to

$$\bigl(B(t_1)-B(t_0),\ldots,B(t_N)-B(t_{N-1})\bigr),$$

where $B$ is Brownian motion. This is just the central limit theorem applied to sums of independent increments. So the finite-dimensional distributions have the right Brownian limit.

However, $S_n$ itself is not continuous. Since we want probability measures on the space of continuous functions, we linearly interpolate the random walk. Define

$$S_n^*(t) := S_n(t) + \frac{nt-\lfloor nt\rfloor}{\sqrt{n}}X_{\lfloor nt\rfloor+1}.$$

This process agrees with $S_n$ at the grid points and connects consecutive values by straight lines. Hence

$$S_n^* \in C([0,1],\mathbb{R}).$$

Equivalently, $S_n^*$ is a random element of the space $C([0,1],\mathbb{R})$ equipped with the supremum norm and its Borel sigma-algebra. The original probability measure $P$ induces a probability measure

$$P_n := P \circ (S_n^*)^{-1}$$

on $C([0,1],\mathbb{R})$. This is the law of the linearly interpolated rescaled random walk.

The interpolation error is small. By Chebyshev's inequality,

$$P\bigl(|S_n^*(t)-S_n(t)| \ge \varepsilon\bigr) \to 0.$$

Therefore, by Slutsky's theorem, the finite-dimensional distributions of $S_n^*$ have the same Brownian limit as those of $S_n$.

Here one must be a little careful. Weak convergence is not generally additive: from

$$Y_n \Rightarrow Y, \qquad Z_n \Rightarrow Z$$

one cannot conclude in general that

$$Y_n+Z_n \Rightarrow Y+Z.$$

Slutsky's theorem gives a useful exception: if one of the limiting variables is deterministic, then the conclusion is valid. In our case the interpolation error converges to the deterministic constant zero, so the passage from $S_n$ to $S_n^*$ is harmless for finite-dimensional distributions.

At this point we know that the finite-dimensional distributions converge to those of Brownian motion. To prove weak convergence of the laws $P_n$ on $C([0,1],\mathbb{R})$, it remains to prove tightness.

If the sequence $(P_n)$ is tight, then every subsequence has a weakly convergent further subsequence. Since the finite-dimensional distributions of any possible limit are already identified as the Brownian finite-dimensional distributions, the limit must be the Wiener measure. Under this measure, the canonical process

$$\omega \mapsto \omega(t)$$

is continuous by construction and has independent, normally distributed increments. Thus the canonical process is Brownian motion. In this way, Donsker's theorem also gives another construction of Brownian motion.

We now recall the compactness criterion needed for tightness in spaces of continuous functions.

Let $(K,d)$ and $(S,\rho)$ be metric spaces, with $K$ compact. For a function $x \in C(K,S)$, define the modulus of continuity

$$w(x,h) := \sup\{\rho(x(t),x(s)): d(t,s)\le h\}.$$

This measures the largest oscillation of $x$ over time intervals of size at most $h$.

The version of the Arzela-Ascoli theorem we use is the following. Let $S$ be complete and let $D \subset K$ be dense. A set

$$A \subset C(K,S)$$

is relatively compact if and only if:

1. for every $t \in D$, the set

   $$\{x(t): x \in A\}$$

   is relatively compact in $S$;

2. the functions in $A$ are uniformly equicontinuous, in the sense that

   $$\lim_{h\downarrow 0}\sup_{x\in A} w(x,h)=0.$$

In the special case $S=\mathbb{R}$, the first condition is essentially pointwise boundedness on a dense set, and the second condition is uniform equicontinuity.

This compactness criterion becomes a tightness criterion for random elements in $C(K,S)$. Let $(X_n)$ be random elements in $C(K,S)$, where $K$ is compact and $S$ is separable and complete. Then

$$X_n \Rightarrow X$$

if and only if the finite-dimensional distributions converge and

$$\lim_{h\downarrow 0}\sup_n \mathbb{E}\bigl[w(X_n,h)\wedge 1\bigr]=0.$$

The truncation by $1$ is important. Tightness can control the probability that the modulus of continuity is nonzero or large, but without truncation an exceptional set of small probability could still carry very large values. The expression $w(X_n,h)\wedge 1$ turns this into a bounded quantity.

Let us briefly discuss why this criterion is true.

First suppose the sequence $(X_n)$ is tight. Then, for every $\varepsilon>0$, there is a compact set

$$B \subset C(K,S)$$

such that

$$\sup_n P(X_n \notin B)<\varepsilon.$$

By Arzela-Ascoli, compactness of $B$ implies uniform equicontinuity on $B$. Thus we can choose $h>0$ so small that

$$w(x,h)<\varepsilon \qquad \text{for all } x\in B.$$

Therefore

$$\sup_n P(w(X_n,h)>\varepsilon)<\varepsilon,$$

and the truncated expectation condition follows.

Conversely, suppose the finite-dimensional distributions converge and

$$\lim_{h\downarrow 0}\sup_n \mathbb{E}\bigl[w(X_n,h)\wedge 1\bigr]=0.$$

Since $L^1$ convergence implies convergence in probability, we can choose a sequence $h_k\downarrow 0$ such that

$$\sup_n P\bigl(w(X_n,h_k)>2^{-k}\bigr) \le 2^{-(k+1)}\varepsilon.$$

Let $(t_k)_{k\ge 1}$ be dense in $K$. Convergence of the one-dimensional distributions implies tightness of the laws of $X_n(t_k)$, so for each $k$ we can find a compact set $C_k\subset S$ with

$$\sup_n P(X_n(t_k)\notin C_k)\le 2^{-(k+1)}\varepsilon.$$

Now define

$$B := \bigcap_{k\ge 1}
\{x\in C(K,S): x(t_k)\in C_k,\; w(x,h_k)\le 2^{-k}\}.$$

By Arzela-Ascoli, this set is relatively compact. Moreover,

$$\sup_n P(X_n\notin B)\le \varepsilon.$$

Thus the sequence is tight.

We now return to Donsker's invariance principle. We already have convergence of finite-dimensional distributions for $S_n^*$. The remaining task is tightness. For that we need a maximum inequality for random walks, due to Ottaviani.

Let $(\xi_k)_{k\ge 1}$ be i.i.d. with mean $0$ and variance $1$, and put

$$T_n := \sum_{k=1}^n \xi_k.$$

Let

$$T_n^* := \max_{1\le k\le n}|T_k|$$

be the running maximum. Ottaviani's inequality states that for $r>1$,

$$P(T_n^* \ge 2r\sqrt{n})
\le
\frac{P(|T_n|\ge r\sqrt{n})}{1-r^{-2}}.$$

In particular,

$$\lim_{r\to\infty} r^2 \limsup_{n\to\infty}
P(T_n^*\ge r\sqrt{n}) = 0.$$

The intuition is that the probability that the random walk ever becomes large can be controlled by the probability that its final value is large. The proof introduces the first time the walk crosses a level. Let

$$A_k := \{T_{k-1}^*\le 2r\sqrt{n},\ |T_k|>2r\sqrt{n}\}.$$

On $A_k$, the walk crosses the level $2r\sqrt{n}$ for the first time at time $k$. If, after time $k$, the future increment $T_n-T_k$ has absolute value at most $r\sqrt{n}$, then $T_n$ itself must still have absolute value at least $r\sqrt{n}$. The key point is that $A_k$ depends only on the first $k$ increments, while $T_n-T_k$ depends only on later increments, so these events are independent. Chebyshev's inequality gives the lower bound

$$\min_{1\le k\le n} P(|T_n-T_k|\le r\sqrt{n}) \ge 1-r^{-2}.$$

This yields Ottaviani's inequality.

The second statement follows from the central limit theorem and the Gaussian tail estimate. If $Z\sim N(0,1)$, then the probability

$$P(|Z|>r)$$

decays exponentially fast in $r^2$. Hence even multiplying by $r^2$ still gives a quantity tending to zero.

Finally we apply this to $S_n^*$. The tightness criterion asks us to control

$$w(S_n^*,h) = \sup_{|t-s|\le h}|S_n^*(t)-S_n^*(s)|.$$

Over a small interval of length $h$, the increments of $S_n^*$ are controlled by the running maximum of a random walk over about $nh$ steps, scaled by $1/\sqrt{n}$. Ottaviani's inequality implies that, for every $\varepsilon>0$,

$$\lim_{h\downarrow 0}
h^{-1}\limsup_{n\to\infty}\sup_{t\in[0,1]}
P\left(
\sup_{0\le r\le h}|S_n^*(t+r)-S_n^*(t)|>\varepsilon
\right)
=0.$$

To pass from local increments to the full modulus of continuity, divide $[0,1]$ into intervals of length $h$. There are about $h^{-1}$ such intervals. The previous estimate is strong enough to absorb this factor, so

$$\lim_{h\downarrow 0}\limsup_{n\to\infty}
P\bigl(w(S_n^*,h)>\varepsilon\bigr)=0.$$

This gives the tightness condition. Since the finite-dimensional distributions already converge to those of Brownian motion, we conclude that

$$S_n^* \Rightarrow B$$

in $C([0,1],\mathbb{R})$.

This is Donsker's invariance principle: the linearly interpolated, diffusively rescaled random walk converges weakly to Brownian motion. Equivalently, the laws of the random functions $S_n^*$ converge weakly to the Wiener measure.
