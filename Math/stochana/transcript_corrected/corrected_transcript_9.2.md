# Clean transcript for recording 9.2

Sources:

- `transcript_original/Erwin-Schrödinger-Zentrum 9.2.txt`
- `lecture notes/Chapter3.pdf`

Style note: this is a cleaned transcript, not a word-for-word transcript. Repetitions, false starts, and unrecoverable filler have been removed. Mathematical terms and notation have been corrected against the lecture notes and written in LaTeX.

## Transcript-to-note correspondence

This table is based on `transcript_original/Erwin-Schrödinger-Zentrum 9.2.txt`. The recording starts with the bracket/compensator discussion, then moves through covariation, orthogonality, bounded-variation local martingales, and the bounded-martingale construction of the bracket process.

| Raw `9.2` transcript lines | Corrected section below | Chapter 3 location |
|---:|---|---|
| 1-17 | Recap of the bracket/compensator and its intended quadratic-variation interpretation | Section 3.3.2, Theorem 3.3.5 |
| 18-60 | Definition of covariation by polarization and convergence of product increments | Proposition 3.3.8 and Remark 3.3.9 |
| 61-160 | Product martingales, orthogonality, and why bounded-variation local martingales are trivial | Discussion after Proposition 3.3.8 and Lemma 3.3.10 |
| 161-356 | Proof strategy for Lemma 3.3.10 by stopping/localization | Lemma 3.3.10 |
| 357-444 | Transition back to proving existence of the bracket; bounded martingale reduction | Section 3.3.3, proof of Theorem 3.3.5 for bounded martingales |
| 445-503 | Definition of quadratic variation sums $A^n$ and compensating processes $N^n=M^2-A^n$ | Section 3.3.3, "Construction of the bracket process" |
| 504-732 | First a priori estimate for $V_t^2(M,\Pi)$ | Lemma 3.3.11 |
| 733-802 | Fourth-increment estimate | Corollary 3.3.12 |
| 803-971 | Cauchy argument for $N^n$, definition of $\langle M\rangle$, and deferred martingale-limit point | Section 3.3.3, "Construction of the bracket process" |

## Corrected transcript

**Source: raw `9.2` lines 1-17. Lecture note: Chapter 3, Section 3.3.2, Theorem 3.3.5.**

We continue with the bracket, or compensator, of a continuous local martingale. The object we want is a process $\langle M\rangle$ which starts at zero, is non-decreasing, and compensates the submartingale behavior of $M^2$:

$$M_t^2-\langle M\rangle_t$$

should be a continuous local martingale.

For Brownian motion this bracket is just

$$\langle B\rangle_t=t.$$

For a general continuous local martingale, the bracket should still be related to quadratic variation, but the convergence is weaker. Instead of pathwise almost-sure convergence along fixed partitions, the quadratic variation sums will converge to the bracket uniformly on compact time intervals in probability.

Throughout this part we assume that the local martingales are continuous and locally square-integrable. In particular, for each fixed time $t$,

$$\mathbb{E}[M_t^2]<\infty$$

after localization. We do not assume global $L^2$ boundedness or uniform integrability unless explicitly stated.

**Source: raw `9.2` lines 18-60. Lecture note: Chapter 3, Proposition 3.3.8 and Remark 3.3.9.**

Assume for the moment that the bracket process has already been constructed. Then we can define the covariation process of two continuous locally square-integrable martingales $M$ and $N$ by polarization:

$$
\langle M,N\rangle
:=
\frac{1}{4}
\bigl(
\langle M+N\rangle-\langle M-N\rangle
\bigr).
$$

This is the stochastic analogue of recovering an inner product from a norm. The map

$$
(M,N)\mapsto \langle M,N\rangle
$$

is bilinear and symmetric.

The covariation also appears as the limit of products of increments. If $\Pi_n$ is a sequence of partitions of $[0,t]$ with mesh going to zero, then

$$
\sum_i
\bigl(M_{t_{i+1}^n}-M_{t_i^n}\bigr)
\bigl(N_{t_{i+1}^n}-N_{t_i^n}\bigr)
\to
\langle M,N\rangle_t
$$

uniformly on compact time intervals in probability.

The covariation explains the martingale property of products. A direct algebraic calculation gives

$$
M_tN_t-\langle M,N\rangle_t
=
\frac{(M_t+N_t)^2-\langle M+N\rangle_t}{4}
-
\frac{(M_t-N_t)^2-\langle M-N\rangle_t}{4}.
$$

Each term on the right-hand side is a continuous local martingale. Therefore

$$
MN-\langle M,N\rangle
$$

is a continuous local martingale.

**Source: raw `9.2` lines 61-160. Lecture note: Chapter 3, orthogonality discussion following Proposition 3.3.8.**

We call two continuous local martingales $M$ and $N$ orthogonal if

$$
\langle M,N\rangle=0.
$$

If $M$ and $N$ are orthogonal, then $MN$ itself is a continuous local martingale. Moreover, for $s\le t$, orthogonality implies that the increments are conditionally uncorrelated:

$$
\mathbb{E}\bigl[(M_t-M_s)(N_t-N_s)\mid\mathcal{F}_s\bigr]=0.
$$

Indeed,

$$
\mathbb{E}\bigl[M_tN_t-M_sN_s\mid\mathcal{F}_s\bigr]
=
\mathbb{E}\bigl[
\langle M,N\rangle_t-\langle M,N\rangle_s
\mid\mathcal{F}_s
\bigr],
$$

and the right-hand side vanishes if $\langle M,N\rangle=0$.

The converse is also true under the usual conditions on the filtration. If $MN$ is a local martingale, then both

$$MN$$

and

$$MN-\langle M,N\rangle$$

are local martingales. Subtracting them shows that $\langle M,N\rangle$ is itself a continuous local martingale. But $\langle M,N\rangle$ is a difference of increasing processes, hence is of bounded variation. A continuous local martingale of bounded variation must be constant. Since the covariation starts at zero, it must be identically zero. Thus

$$
MN \text{ is a local martingale}
\quad\Longleftrightarrow\quad
\langle M,N\rangle=0.
$$

**Source: raw `9.2` lines 161-356. Lecture note: Chapter 3, Lemma 3.3.10.**

We now prove the key lemma used in this argument.

Let $M$ be a continuous local martingale with respect to a filtration satisfying the usual conditions, and assume $M_0=0$. If $M$ is of bounded variation, then

$$
P(M_t=0\text{ for all }t\ge 0)=1.
$$

The proof is by reduction.

First suppose $M$ is a continuous square-integrable martingale and that its total variation on $[0,t]$ is uniformly bounded by a deterministic constant $C$:

$$
V_t(M)\le C.
$$

For a partition $\Pi=\{0=t_0<t_1<\cdots<t_m=t\}$, write

$$
\Delta_iM:=M_{t_i}-M_{t_{i-1}}.
$$

Since $M_0=0$ and martingale increments are orthogonal in $L^2$,

$$
\mathbb{E}[M_t^2]
=
\mathbb{E}\left[\sum_i(\Delta_iM)^2\right].
$$

Pathwise,

$$
\sum_i(\Delta_iM)^2
\le
\left(\sup_i|\Delta_iM|\right)
\sum_i|\Delta_iM|
\le
C\sup_i|\Delta_iM|.
$$

Because $M$ is continuous, the maximum increment tends to zero as the mesh of the partition tends to zero. To pass the limit through expectation, we need domination. This is supplied by Doob's maximal inequality, applied to $M^2$, giving an integrable bound in terms of $\mathbb{E}[M_t^2]$. Hence dominated convergence yields

$$
\mathbb{E}[M_t^2]=0.
$$

Therefore $M_t=0$ almost surely for each fixed $t$. By continuity, $M$ is identically zero.

Second, suppose $M$ is a continuous square-integrable martingale of bounded variation, but the variation need not be bounded by a deterministic constant. Define

$$
\tau_n:=\inf\{t\ge 0:V_t(M)>n\}.
$$

Under the usual conditions, this optional time is a stopping time. The stopped process $M^{\tau_n}$ is a martingale, and its variation is bounded by $n$. By the first step,

$$
M_{t\wedge\tau_n}=0
$$

for each $n$. Since $\tau_n\uparrow\infty$, we get $M_t=0$.

Finally, if $M$ is only a continuous local martingale, localize once more. We may choose a localizing sequence so that the stopped processes are bounded martingales. Applying the previous step to each stopped process and then letting the stopping times increase to infinity gives the result.

This lemma is useful because it says that a non-trivial continuous local martingale must have genuine oscillation. A continuous local martingale cannot move by finite variation unless it is constant.

**Source: raw `9.2` lines 357-503. Lecture note: Chapter 3, Section 3.3.3, proof of Theorem 3.3.5 for bounded martingales.**

We now return to the construction of the bracket process. The main theorem is first proved for bounded continuous martingales. Assume that $M$ is a continuous martingale with

$$
|M_t|\le K
$$

for all $t$, and $M_0=0$.

The idea is to define the quadratic variation along finer and finer partitions, and then prove that the associated compensating martingales form a Cauchy sequence.

Let

$$
\Pi^n=\{0=t_0^n<t_1^n<\cdots<t_{m_n}^n=T\}
$$

be an increasing sequence of partitions whose mesh tends to zero. For $t\in[0,T]$, define

$$
A_t^n
:=
\sum_{t_i^n\le t}
\bigl(M_{t_i^n}-M_{t_{i-1}^n}\bigr)^2
+
\bigl(M_t-M_{t_{k_n(t)}^n}\bigr)^2,
$$

where $t_{k_n(t)}^n$ is the last partition point before or at $t$. This is the continuous version of the quadratic variation sum along $\Pi^n$.

Set

$$
N_t^n:=M_t^2-A_t^n.
$$

The goal is to show that $(N^n)_n$ is Cauchy in

$$
L^2\bigl(\Omega;C([0,T],\mathbb{R})\bigr),
$$

where $C([0,T],\mathbb{R})$ is equipped with the supremum norm. If $N^n$ converges to some continuous process $N$, then we define

$$
\langle M\rangle_t:=M_t^2-N_t.
$$

Then $A^n\to\langle M\rangle$ in $L^2$ uniformly on compact time intervals, so the bracket is obtained as the limit of quadratic variation sums.

**Source: raw `9.2` lines 504-802. Lecture note: Chapter 3, Lemma 3.3.11 and Corollary 3.3.12.**

We need two a priori estimates.

First, for every partition $\Pi$ of $[0,t]$,

$$
\mathbb{E}\bigl[V_t^2(M,\Pi)^2\bigr]\le 6K^4,
$$

where

$$
V_t^2(M,\Pi):=\sum_i(\Delta_iM)^2.
$$

The exact constant is not important. The point is that the second moment of the quadratic variation sum is bounded uniformly over all partitions.

To see the structure of the estimate, expand

$$
\left(\sum_i(\Delta_iM)^2\right)^2
=
\sum_i(\Delta_iM)^4
+
2\sum_{k<j}(\Delta_kM)^2(\Delta_jM)^2.
$$

Since $|M|\le K$, one factor of $(\Delta_iM)^2$ can be bounded by a constant times $K^2$, and the remaining sum telescopes in expectation using the martingale property. The cross terms are handled by conditioning on the earlier sigma-algebra and using the same martingale-increment identity. This gives a bound of order $K^4$.

Second, the sum of fourth powers of increments goes to zero as the mesh goes to zero:

$$
\mathbb{E}\left[\sum_i(\Delta_iM)^4\right]\to 0.
$$

Indeed, write

$$
\sum_i(\Delta_iM)^4
\le
\left(\sup_i|\Delta_iM|^2\right)
\sum_i(\Delta_iM)^2.
$$

The first factor tends to zero pathwise by continuity of $M$ on compact intervals. The second factor is uniformly $L^2$-bounded by the previous estimate. Holder's inequality then gives the convergence to zero.

**Source: raw `9.2` lines 803-971. Lecture note: Chapter 3, Section 3.3.3, "Construction of the bracket process".**

Now we use the increasing sequence of partitions. For each $n$,

$$
N_t^n=M_t^2-A_t^n
$$

can be written as a discrete stochastic integral:

$$
N_t^n
=
2\sum_i M_{t_{i-1}^n}
\bigl(M_{t_i^n}-M_{t_{i-1}^n}\bigr),
$$

with the obvious final partial increment if $t$ is not itself a partition point. This representation shows that $N^n$ is a continuous martingale.

If $\Pi^n\subset \Pi^m$, then $N^n-N^m$ is also a continuous martingale. By Doob's maximal inequality,

$$
\mathbb{E}\left[\sup_{0\le s\le t}|N_s^n-N_s^m|^2\right]
\le
C\mathbb{E}\left[|N_t^n-N_t^m|^2\right].
$$

So it is enough to estimate the terminal second moment.

Between two neighboring points of the coarser partition $\Pi^n$, the finer partition $\Pi^m$ has additional points. Rewriting both $N^n$ and $N^m$ in terms of the finer increments gives

$$
N_t^n-N_t^m
=
2\sum_i\sum_j
\bigl(M_{t_{i-1}^n}-M_{t_{j-1}^m}\bigr)\Delta_j^mM,
$$

where the inner sum ranges over the fine subintervals inside the $i$-th coarse interval.

The summands are martingale increments over non-overlapping intervals, so cross terms vanish when taking expectations of squares. We obtain an estimate of the form

$$
\mathbb{E}[|N_t^n-N_t^m|^2]
\le
C
\left(
\mathbb{E}\left[
\sup_{i,j}|M_{t_{i-1}^n}-M_{t_{j-1}^m}|^4
\right]
\right)^{1/2}
\left(
\mathbb{E}\left[
\left(\sum_j(\Delta_j^mM)^2\right)^2
\right]
\right)^{1/2}.
$$

The second factor is bounded by the first a priori estimate. The first factor tends to zero because $M$ is continuous and the meshes of the partitions go to zero. Hence

$$
\mathbb{E}\left[\sup_{0\le s\le t}|N_s^n-N_s^m|^2\right]\to 0.
$$

Thus $(N^n)$ is Cauchy in

$$
L^2\bigl(\Omega;C([0,T],\mathbb{R})\bigr).
$$

Let $N$ be the limit. Define

$$
\langle M\rangle_t:=M_t^2-N_t.
$$

By construction, $A^n\to\langle M\rangle$ in $L^2$ uniformly on compact time intervals. This proves the existence of the bracket process in the bounded continuous martingale case, up to the point that one still has to justify that the limit $N$ is again a martingale. The lecturer notes that this martingale-preservation argument is deferred until later, where it follows from a more general result.

The important conclusion of this lecture is the strategy:

1. define quadratic variation sums $A^n$ along refining partitions;
2. subtract them from $M^2$ to form martingales $N^n=M^2-A^n$;
3. prove that $(N^n)$ is Cauchy in a strong path-space $L^2$ sense;
4. define the bracket by

   $$\langle M\rangle=M^2-N;$$

5. later extend from bounded martingales to local martingales by localization.
