# Corrected transcript for recording 12

Sources:

- `Math/stochana/transcript_original/Erwin-Schrödinger-Zentrum 12.txt`
- `Math/stochana/lecture notes/Chapter3.pdf`

Style note: this is a cleaned transcript from the updated recording 12, generated with the repository transcription script. Repetitions, false starts, break chatter, and unusable Whisper artifacts have been removed. Mathematical notation and exercise numbers are corrected against Chapter 3.

## Summary

This lecture is an exercise/review session for Chapter 3.

The first part reviews Exercise 25 on continuous quadratic variation and covariation: existence of the covariation is equivalent to existence of the quadratic variation of the sum, the covariation is bilinear, the polarization identity holds, and Cauchy-Schwarz follows from the finite-dimensional Cauchy-Schwarz inequality on the increment vectors.

The second part reviews Exercise 26: a real-valued function is of bounded variation if and only if it can be written as the difference of two non-decreasing functions. The lecturer emphasizes the standard decomposition using the variation function and points out a small real-analysis subtlety about additivity of variation over subintervals and the role of partitions.

The last part discusses Exercises 29, 30, and 33. Exercise 29 shows that a non-negative local martingale is a supermartingale by localization and Fatou's lemma. Exercise 30 shows that certain right-continuous submartingales are of class DL, using optional sampling, Doob's maximal inequality, and, in the second case, the Doob-Meyer decomposition. Exercise 33 begins the argument that if a continuous square-integrable local martingale has integrable terminal bracket, then it is a uniformly integrable martingale and its terminal second moment is determined by the terminal bracket. The raw transcript ends during this discussion.

## Transcript-to-note correspondence

| Raw transcript lines | Lecture-note location | Content |
|---:|---|---|
| 1-65 | Chapter 3, Exercise 25 | Covariation, polarization identity, bilinearity, Cauchy-Schwarz |
| 66-180 | Chapter 3, Exercise 26 | Bounded variation iff difference of two non-decreasing functions |
| 183-219 | Chapter 3, Exercise 29 | Non-negative local martingale is a supermartingale |
| 220-360 | Chapter 3, Exercise 30, first bullet | Non-negative right-continuous submartingale is of class DL |
| 373-497 | Chapter 3, Exercise 30, second bullet | Doob-Meyer decomposition implies class DL |
| 538-657 | Chapter 3, Exercise 33 | Integrable bracket, uniform integrability, and terminal second moment |

## Corrected transcript

We are back in the deterministic setting: continuous functions with continuous quadratic variation. Recall that quadratic variation is always considered along a fixed sequence of partitions. In general, the limit does not have to be the same along every possible sequence of partitions.

The first exercise asks about covariation. Let \(X,Y : [0,T] \to \mathbb R\) be continuous and of continuous quadratic variation along a common sequence of partitions \(\Pi_n\). The covariation process is defined by taking limits of sums of products of increments:

$$
V_t^2(X,Y,\Pi_n)
=
\sum_{t_i \le t}
(X_{t_i}-X_{t_{i-1}})
(Y_{t_i}-Y_{t_{i-1}}).
$$

The question is when this limit exists. The point is that it exists if and only if the quadratic variation of \(X+Y\) exists along the same sequence of partitions.

Indeed, for a fixed partition, expand the square:

$$
(\Delta_i X+\Delta_i Y)^2
=
(\Delta_i X)^2
+2\Delta_i X\Delta_i Y
+(\Delta_i Y)^2.
$$

Therefore

$$
\sum_i \Delta_i X\Delta_i Y
=
\frac12
\left(
\sum_i(\Delta_i X+\Delta_i Y)^2
-
\sum_i(\Delta_i X)^2
-
\sum_i(\Delta_i Y)^2
\right).
$$

Since \(X\) and \(Y\) already have quadratic variation along the chosen partitions, the only new term is the quadratic variation of \(X+Y\). Thus the covariation exists exactly when \(\langle X+Y\rangle\) exists.

Passing to the limit gives the polarization identity:

$$
\langle X,Y\rangle
=
\frac12
\left(
\langle X+Y\rangle
-\langle X\rangle
-\langle Y\rangle
\right).
$$

This is also the reason why covariation processes are of bounded variation: they are differences of non-decreasing quadratic variation processes.

The bilinearity of \(\langle \cdot,\cdot\rangle\) follows directly from the bilinearity of the finite sums before passing to the limit.

The Cauchy-Schwarz inequality also follows from the finite-dimensional Cauchy-Schwarz inequality. For each partition,

$$
\left|
\sum_i \Delta_i X \Delta_i Y
\right|
\le
\left(\sum_i(\Delta_i X)^2\right)^{1/2}
\left(\sum_i(\Delta_i Y)^2\right)^{1/2}.
$$

Taking limits yields

$$
|\langle X,Y\rangle_t|
\le
\sqrt{\langle X\rangle_t\langle Y\rangle_t}.
$$

There was a question whether the first statement can be obtained directly from the polarization identity. The answer is: conceptually yes, but one must first know that both sides are well-defined. Since the covariation was defined as a limit of partition sums, we first check the finite-sum identity and only then pass to the limit.

The next exercise says that a real-valued function is of bounded variation if and only if it can be represented as the difference of two non-decreasing functions.

One direction is immediate. If

$$
f = f^+ - f^-,
$$

where \(f^+\) and \(f^-\) are non-decreasing, then \(f\) is of bounded variation. The variation is bounded by the sum of the variations of \(f^+\) and \(f^-\).

For the converse, assume \(f\) is of bounded variation. Define the variation function

$$
g(t) = V_{[0,t]}(f).
$$

This function is non-decreasing. The candidate decomposition is

$$
f = g - (g-f).
$$

So it remains to show that

$$
h(t) := g(t)-f(t)
$$

is also non-decreasing.

Take \(s \le t\). We want

$$
h(s) \le h(t),
$$

which is equivalent to

$$
f(t)-f(s) \le g(t)-g(s).
$$

But

$$
f(t)-f(s)
\le
|f(t)-f(s)|
\le
V_{[s,t]}(f).
$$

Using additivity of variation over adjacent intervals,

$$
V_{[s,t]}(f)
=
V_{[0,t]}(f)-V_{[0,s]}(f)
=
g(t)-g(s).
$$

Therefore \(h\) is non-decreasing, and \(f\) is the difference of two non-decreasing functions.

The small subtlety is the additivity of variation:

$$
V_{[a,b]}(f)
=
V_{[a,c]}(f)+V_{[c,b]}(f),
\qquad a \le c \le b.
$$

For a fixed partition this is clear once \(c\) is inserted into the partition. But when one defines variation using limits over partitions, one has to justify that inserting such points and passing to finer partitions does not change the value. This is a standard real-analysis point. The lecturer notes that we usually suppress this detail, but it is the reason for mentioning increasing sequences of partitions or nets of partitions.

The next exercise is Exercise 29: a non-negative local martingale is a supermartingale.

Let \(X\) be a non-negative local martingale, and let \(\tau_n\) be a localizing sequence. For each \(n\), the stopped process

$$
X^{\tau_n}_t = X_{t\wedge\tau_n}
$$

is a martingale. Hence, for \(s \le t\),

$$
E[X_{t\wedge\tau_n}\mid \mathcal F_s]
=
X_{s\wedge\tau_n}.
$$

Since \(\tau_n \uparrow \infty\), we have

$$
X_{t\wedge\tau_n} \to X_t,
\qquad
X_{s\wedge\tau_n} \to X_s
$$

almost surely. We do not necessarily have \(L^1\) convergence. This is exactly where non-negativity is used. By conditional Fatou's lemma,

$$
E[X_t\mid \mathcal F_s]
=
E[\liminf_n X_{t\wedge\tau_n}\mid \mathcal F_s]
\le
\liminf_n E[X_{t\wedge\tau_n}\mid \mathcal F_s]
=
\liminf_n X_{s\wedge\tau_n}
=
X_s.
$$

Thus \(X\) is a supermartingale.

Now consider Exercise 30. Let \(X\) be a right-continuous submartingale. We want to show that under either of the two stated assumptions the family

$$
\{X_\tau : \tau \le T\}
$$

is uniformly integrable for every fixed \(T\). This means that \(X\) is of class DL.

First assume \(X_t \ge 0\) almost surely for all \(t\). Let \(\tau \le T\). Optional sampling for right-continuous submartingales and bounded stopping times gives

$$
E[X_\tau] \le E[X_T] < \infty.
$$

To prove uniform integrability, we need to show

$$
\sup_{\tau\le T}
E[X_\tau\,1_{\{X_\tau>K\}}]
\to 0
\qquad\text{as }K\to\infty.
$$

The event \(\{X_\tau>K\}\) is in \(\mathcal F_\tau\). By optional sampling/submartingale testing on this event,

$$
E[X_\tau\,1_{\{X_\tau>K\}}]
\le
E[X_T\,1_{\{X_\tau>K\}}].
$$

Now remove the remaining \(\tau\) from the indicator. Since \(X\) is non-negative,

$$
\{X_\tau>K\}
\subseteq
\left\{\sup_{0\le u\le T}X_u>K\right\}.
$$

Doob's maximal inequality for non-negative submartingales gives

$$
P\left(\sup_{0\le u\le T}X_u>K\right)
\le
\frac{E[X_T]}{K}
\to 0.
$$

Therefore

$$
E[X_T\,1_{\{X_\tau>K\}}]
\le
E\left[
X_T\,1_{\{\sup_{0\le u\le T}X_u>K\}}
\right]
\to 0,
$$

because \(X_T\) is a single integrable random variable and the event has probability going to zero. This proves uniform integrability of the stopped family.

The non-negativity is used twice: first to apply the relevant maximal inequality for submartingales, and second to use the running supremum without absolute values.

For the second part of Exercise 30, assume \(X\) has a Doob-Meyer decomposition

$$
X_t = M_t + A_t,
$$

where \(M\) is a martingale and \(A\) is increasing and adapted. For a bounded stopping time \(\tau \le T\),

$$
X_\tau = M_\tau + A_\tau.
$$

Since \(M\) is a martingale,

$$
M_\tau = E[M_T\mid \mathcal F_\tau].
$$

Using \(M_T=X_T-A_T\), we get

$$
X_\tau
=
E[X_T-A_T\mid \mathcal F_\tau]+A_\tau.
$$

Because \(A\) is increasing and \(\tau\le T\),

$$
A_\tau \le A_T.
$$

Thus \(X_\tau\) can be controlled by a martingale generated by the terminal value. The idea is to compare \(X_\tau\) with a uniformly integrable family of conditional expectations of a fixed terminal random variable. Conditional expectations of one integrable random variable form a uniformly integrable family. This gives the required class DL property. The transcript discussion here includes questions about whether the correct class is \(D\) or \(DL\); for bounded stopping times, the relevant conclusion is class DL.

Finally, the lecture begins Exercise 33. Let \(M\) be a continuous square-integrable local martingale starting at zero, and assume

$$
E[\langle M\rangle_\infty] < \infty.
$$

The exercise claims:

1. \(M\) is a martingale, and both \(M\) and \(M^2\) are uniformly integrable.
2. The limit \(M_\infty\) exists almost surely and

$$
E[M_\infty^2] = E[\langle M\rangle_\infty].
$$

3. A right-continuous modification of

$$
Z_t := E[M_\infty^2\mid\mathcal F_t] - M_t^2
$$

is a non-negative supermartingale with \(E[Z_t]\to0\).

The hint says that for every stopping time \(\tau\),

$$
E[M_\tau^2]
\le
E[\langle M\rangle_\tau].
$$

Take \(\tau \le T\). Since the bracket is increasing,

$$
E[M_\tau^2]
\le
E[\langle M\rangle_\tau]
\le
E[\langle M\rangle_T]
\le
E[\langle M\rangle_\infty]
<\infty.
$$

Thus the stopped family \(\{M_\tau : \tau\le T\}\) has uniformly bounded second moments. An \(L^2\)-bounded family is uniformly integrable, so \(M\) is of class DL. By Proposition 3.3.4, a continuous local martingale of class DL is a true martingale.

The same bound is the starting point for uniform integrability of \(M\) and for controlling \(M^2\). Since

$$
M^2-\langle M\rangle
$$

is a martingale, the bracket links second moments with the increasing process \(\langle M\rangle\). In particular, one expects the terminal identity

$$
E[M_\infty^2]=E[\langle M\rangle_\infty].
$$

The raw transcript ends during the discussion of how to complete the uniform integrability argument for \(M^2\), so the final details of Exercise 33 are not fully recorded here.
