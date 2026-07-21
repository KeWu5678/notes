# Corrected transcript for recording 11

Sources:

- `Math/stochana/transcript_original/Erwin-Schrödinger-Zentrum 11.txt`
- `Math/stochana/lecture notes/Chapter4.pdf`

Style note: this is a cleaned transcript from the updated recording 11, generated with the MLX Whisper transcription path. Repetitions, false starts, and unusable ASR artifacts have been removed. Mathematical notation and theorem/exercise references are corrected against Chapter 4. Places where the board content is not fully recoverable from the audio are marked conservatively.

## Summary

This lecture continues Chapter 4 on stochastic integration with respect to Brownian motion.

The first part finishes the construction of the Ito integral for integrands in \(L^2\). Starting from simple processes, the lecturer uses the Ito isometry to define the integral first at fixed times, then proves that the definition is independent of the approximating simple processes, that the resulting process is a martingale, and that it has a continuous modification.

The second part proves the Ito isometry for general \(L^2\)-integrands, including the conditional covariance formula. The proof reduces the covariance identity to the case \(f=g\), then uses an auxiliary lemma about convergence of conditional second moments.

The third part identifies the bracket of a Brownian stochastic integral:

$$
\left\langle \int_0^\cdot f_s\,dB_s \right\rangle_t
= \int_0^t f_s^2\,ds.
$$

The lecture then discusses Tanaka's formula and Brownian local time at zero, using a smoothed version of the absolute value function. The final part introduces the next topic: stochastic integration with respect to continuous martingales, beginning with the Hilbert space \(\mathcal M\) of \(L^2\)-bounded continuous martingales starting at zero.

## Transcript-to-note correspondence

| Raw transcript lines | Lecture-note location | Content |
|---:|---|---|
| 1-164 | Proposition 4.1.7 | Extension of the stochastic integral from \(L^0\) to \(L^2\) |
| 165-298 | Lemma 4.1.8 and Lemma 4.1.9 | Ito isometry and conditional covariance formula |
| 299-377 | Corollary 4.1.10 | Bracket of a Brownian stochastic integral |
| 378-519 | Exercise 39 | Tanaka formula and Brownian local time |
| 520-588 | Section 4.2.1, Definition 4.2.1 and Theorem 4.2.2 | The Hilbert space \(\mathcal M\) |

## Corrected transcript

We continue the construction of the stochastic integral. Last time we introduced the class of simple processes and the larger space \(L^2\). The space \(L^2\) consists of real-valued adapted processes for which, for every finite \(T\),

$$
E\left[\int_0^T f_t^2\,dt\right] < \infty.
$$

The key point was the Ito isometry for simple processes:

$$
E\left[
\left(
\int_0^T \phi_t\,dB_t
\right)^2
\right]
=
E\left[
\int_0^T \phi_t^2\,dt
\right].
$$

This isometry is the basic reason we can extend the stochastic integral from simple processes to all \(L^2\)-integrands.

For simple processes \(\phi\), we already have a map

$$
I : L^0 \to \mathcal M_{2}^{c,0},
$$

where \(\mathcal M_{2}^{c,0}\) denotes the continuous square-integrable martingales starting at zero. The proposition says that this map extends uniquely to a continuous map

$$
J : L^2 \to \mathcal M_{2}^{c,0}.
$$

For \(f \in L^2\), we write

$$
J_t(f)
=
\int_0^t f_s\,dB_s.
$$

Let \(f \in L^2\), and choose a sequence of simple processes \(\phi^n\) such that

$$
\phi^n \to f
\quad\text{in } L^2([0,T]\times\Omega)
$$

for every finite \(T\).

First, fix a time \(t\). By the Ito isometry,

$$
E\left[
\left(
I_t(\phi^n)-I_t(\phi^m)
\right)^2
\right]
=
E\left[
\int_0^t
(\phi_s^n-\phi_s^m)^2\,ds
\right].
$$

Since \(\phi^n\) is Cauchy in \(L^2\), the right-hand side goes to zero. Hence \(I_t(\phi^n)\) is Cauchy in the usual \(L^2(\Omega)\). Completeness of \(L^2(\Omega)\) gives a random variable \(Y_t\) such that

$$
I_t(\phi^n) \to Y_t
\quad\text{in } L^2(\Omega).
$$

At this point this is only a definition at a fixed time \(t\). We have not yet proved continuity in \(t\).

The next point is uniqueness. Suppose \(\psi^n\) is another sequence of simple processes approximating the same \(f\). Again by the Ito isometry,

$$
E\left[
\left(
I_t(\phi^n)-I_t(\psi^n)
\right)^2
\right]
=
E\left[
\int_0^t
(\phi_s^n-\psi_s^n)^2\,ds
\right].
$$

Since both \(\phi^n\) and \(\psi^n\) converge to \(f\), the right-hand side goes to zero. Thus the limit \(Y_t\) does not depend on the approximating sequence.

Now we prove the martingale property. For simple processes, \(I(\phi^n)\) is a martingale, so for \(s\ge t\),

$$
E[I_s(\phi^n)\mid\mathcal F_t]
=
I_t(\phi^n).
$$

We know \(I_s(\phi^n)\to J_s(f)\) and \(I_t(\phi^n)\to J_t(f)\) in \(L^2\). Jensen's inequality gives

$$
E\left[
\left(
E[I_s(\phi^n)-J_s(f)\mid\mathcal F_t]
\right)^2
\right]
\le
E\left[
(I_s(\phi^n)-J_s(f))^2
\right],
$$

which goes to zero. Therefore

$$
E[J_s(f)\mid\mathcal F_t]
=
J_t(f).
$$

So the extension is a martingale.

It remains to obtain continuous sample paths. The process \(Y_t\) was defined separately for each \(t\), so continuity is not automatic. For simple processes, \(I(\phi^n)\) has continuous sample paths. We use Doob's maximal inequality on the martingale

$$
I(\phi^n)-I(\phi^m).
$$

For every \(T>0\) and \(\varepsilon>0\),

$$
P\left(
\sup_{0\le t\le T}
|I_t(\phi^n)-I_t(\phi^m)|>\varepsilon
\right)
\le
\frac{1}{\varepsilon^2}
E\left[
|I_T(\phi^n)-I_T(\phi^m)|^2
\right].
$$

The right-hand side goes to zero by the Ito isometry. Thus the integral processes are Cauchy in probability with respect to the supremum norm on \([0,T]\).

To upgrade this to almost sure uniform convergence along a subsequence, choose a subsequence \(\phi^{n_k}\) such that

$$
P\left(
\sup_{0\le t\le T}
|I_t(\phi^{n_k})-I_t(\phi^{n_{k+1}})|>2^{-k}
\right)
\le
2^{-k}.
$$

By Borel-Cantelli, this event happens only finitely often. Hence for almost every \(\omega\), the sequence

$$
t \mapsto I_t(\phi^{n_k})(\omega)
$$

is Cauchy in \(C[0,T]\) with the supremum norm. Since \(C[0,T]\) is complete, it converges to a continuous function. This gives a continuous modification of \(Y\).

This proves the construction of the stochastic integral for all \(f\in L^2\).

The important properties of the integral now follow by approximation from the corresponding properties for simple processes:

1. Linearity.
2. Additivity over intervals:

$$
\int_0^T f_s\,dB_s
=
\int_0^c f_s\,dB_s
+
\int_c^T f_s\,dB_s.
$$

3. Centering:

$$
E\left[\int_0^T f_s\,dB_s\right]=0.
$$

4. Adaptedness:

$$
\int_0^t f_s\,dB_s
\quad\text{is }\mathcal F_t\text{-measurable}.
$$

Next we extend the Ito isometry from simple processes to arbitrary \(L^2\)-integrands. For \(f\in L^2\),

$$
E\left[
\left(
\int_0^t f_s\,dB_s
\right)^2
\right]
=
E\left[
\int_0^t f_s^2\,ds
\right].
$$

More generally, for \(f,g\in L^2\) and \(0\le s\le t\),

$$
E\left[
\left(\int_s^t f_u\,dB_u\right)
\left(\int_s^t g_u\,dB_u\right)
\mid \mathcal F_s
\right]
=
E\left[
\int_s^t f_u g_u\,du
\mid \mathcal F_s
\right].
$$

This is the conditional covariance formula.

The first identity follows immediately from the construction and the isometry for simple processes. For the second identity, use polarization:

$$
ab
=
\frac14\left((a+b)^2-(a-b)^2\right).
$$

So it is enough to prove the formula for \(f=g\).

Choose simple processes \(\phi^n\to f\) in \(L^2\), and set

$$
F_n
=
\int_s^t \phi_u^n\,dB_u,
\qquad
F
=
\int_s^t f_u\,dB_u.
$$

Then \(F_n\to F\) in \(L^2(\Omega)\). We want to pass from convergence of \(F_n\) to convergence of conditional second moments:

$$
E[F_n^2\mid\mathcal F_s]
\to
E[F^2\mid\mathcal F_s]
\quad\text{in }L^1.
$$

The auxiliary lemma says exactly this: if \(X_n\to X\) in \(L^2\), then

$$
E[X_n^2\mid\mathcal G]
\to
E[X^2\mid\mathcal G]
\quad\text{in }L^1
$$

for every sub-\(\sigma\)-field \(\mathcal G\).

The proof is a conditional Holder estimate:

$$
|E[X_n^2-X^2\mid\mathcal G]|
\le
E[|X_n-X||X_n+X|\mid\mathcal G].
$$

Then conditional Cauchy-Schwarz gives

$$
E[|X_n-X||X_n+X|\mid\mathcal G]
\le
E[|X_n-X|^2\mid\mathcal G]^{1/2}
E[|X_n+X|^2\mid\mathcal G]^{1/2}.
$$

Taking expectations and applying Cauchy-Schwarz again gives convergence to zero in \(L^1\), since \(X_n-X\to0\) in \(L^2\) and \(X_n+X\) is bounded in \(L^2\).

For simple processes the conditional isometry is already known:

$$
E[F_n^2\mid\mathcal F_s]
=
E\left[
\int_s^t (\phi_u^n)^2\,du
\mid\mathcal F_s
\right].
$$

Letting \(n\to\infty\) yields the conditional formula for \(f\). By polarization, this also gives the formula for \(f\) and \(g\).

Now we compute the bracket of a Brownian stochastic integral. Let

$$
M_t
=
\int_0^t f_u\,dB_u.
$$

We expect, from the quadratic variation calculation in Chapter 3, that

$$
\langle M\rangle_t
=
\int_0^t f_u^2\,du.
$$

Indeed, by the defining property of the bracket, we need to show that

$$
M_t^2-\int_0^t f_u^2\,du
$$

is a martingale.

For \(s\le t\), compute

$$
E\left[
M_t^2-\int_0^t f_u^2\,du
\mid\mathcal F_s
\right].
$$

Write

$$
M_t
=
M_s+(M_t-M_s).
$$

Then

$$
M_t^2
=
M_s^2
+2M_s(M_t-M_s)
+(M_t-M_s)^2.
$$

The conditional expectation of the cross term is zero because \(M\) is a martingale:

$$
E[M_t-M_s\mid\mathcal F_s]=0.
$$

By the conditional Ito isometry,

$$
E[(M_t-M_s)^2\mid\mathcal F_s]
=
E\left[
\int_s^t f_u^2\,du
\mid\mathcal F_s
\right].
$$

Therefore

$$
E\left[
M_t^2-\int_0^t f_u^2\,du
\mid\mathcal F_s
\right]
=
M_s^2-\int_0^s f_u^2\,du.
$$

So \(M^2-\int f^2\,du\) is a martingale, and hence

$$
\left\langle \int_0^\cdot f_u\,dB_u \right\rangle_t
=
\int_0^t f_u^2\,du.
$$

There was a question about the notation in Lemma 4.1.8: whether it should be \(L^2\) or \(L_2\). The point is that this is the space of square-integrable adapted processes introduced earlier in Chapter 4. The superscript/subscript convention in the notes may contain a typographical inconsistency, but the intended space is the \(L^2\)-integrability class of admissible integrands.

The lecturer then discusses an exercise related to Tanaka's formula. The usual Ito formula applies to \(C^2\) functions. But the function

$$
g(x)=|x|
$$

is not \(C^2\) at the origin. The question is what happens if we try to apply Ito's formula to \(g(B_t)\).

We approximate \(g\) by a smoothed function \(g_\varepsilon\). Outside the interval \((-\varepsilon,\varepsilon)\), define

$$
g_\varepsilon(x)=|x|.
$$

Inside the interval, smooth it by setting

$$
g_\varepsilon(x)
=
\frac{\varepsilon}{2}
+
\frac{x^2}{2\varepsilon},
\qquad |x|<\varepsilon.
$$

This function is \(C^1\), and it is \(C^2\) except possibly at the two points \(\pm\varepsilon\). Exercise 38 allows us to apply the Ito formula to such a function.

Applying Ito's formula gives

$$
g_\varepsilon(B_t)
=
g_\varepsilon(B_0)
+
\int_0^t g_\varepsilon'(B_s)\,dB_s
+
\frac12\int_0^t g_\varepsilon''(B_s)\,ds.
$$

Inside \((-\varepsilon,\varepsilon)\),

$$
g_\varepsilon'(x)=\frac{x}{\varepsilon},
\qquad
g_\varepsilon''(x)=\frac{1}{\varepsilon}.
$$

Outside this interval, the second derivative is zero. Hence

$$
\frac12\int_0^t g_\varepsilon''(B_s)\,ds
=
\frac{1}{2\varepsilon}
\lambda\{s\in[0,t]: B_s\in(-\varepsilon,\varepsilon)\},
$$

where \(\lambda\) denotes Lebesgue measure.

This term measures how much time Brownian motion spends near zero, scaled by \(1/(2\varepsilon)\). If we looked only at the set where \(B_s=0\), the Lebesgue measure would be zero. The scaling and the shrinking interval produce a non-trivial limit.

The stochastic integral part near zero is

$$
\int_0^t
\frac{B_s}{\varepsilon}
1_{\{|B_s|<\varepsilon\}}
\,dB_s.
$$

By the Ito isometry,

$$
E\left[
\left(
\int_0^t
\frac{B_s}{\varepsilon}
1_{\{|B_s|<\varepsilon\}}
\,dB_s
\right)^2
\right]
=
E\left[
\int_0^t
\frac{B_s^2}{\varepsilon^2}
1_{\{|B_s|<\varepsilon\}}
\,ds
\right].
$$

On \(\{|B_s|<\varepsilon\}\), we have \(B_s^2/\varepsilon^2\le1\). Therefore the last expression is bounded by

$$
\int_0^t P(|B_s|<\varepsilon)\,ds,
$$

which goes to zero by dominated convergence. Thus the contribution from the stochastic integral near zero vanishes in \(L^2\).

Outside the small interval, \(g_\varepsilon'(B_s)\) converges to \(\operatorname{sign}(B_s)\). Hence, letting \(\varepsilon\to0\), we obtain Tanaka's formula:

$$
|B_t|
=
|B_0|
+
\int_0^t \operatorname{sign}(B_s)\,dB_s
+
L_t,
$$

where

$$
L_t
=
\lim_{\varepsilon\downarrow0}
\frac{1}{2\varepsilon}
\lambda\{s\in[0,t]: |B_s|<\varepsilon\}.
$$

This process \(L_t\) is the Brownian local time at zero.

The idea is that local time is a scaled occupation time. Brownian motion spends zero Lebesgue time exactly at zero, but the scaled time spent in a shrinking neighborhood of zero has a non-trivial limit.

The lecture then moves toward stochastic integration with respect to more general continuous martingales.

We now want to extend the integration theory from Brownian motion to continuous martingales. In the first step we consider \(L^2\)-bounded continuous martingales.

A martingale \(M\) is \(L^2\)-bounded if

$$
\sup_{t\ge0} E[M_t^2] < \infty.
$$

Let \(\mathcal M\) denote the space of all \(L^2\)-bounded continuous martingales starting at zero.

For \(M\in\mathcal M\), the martingale convergence theorem gives a terminal random variable

$$
M_\infty
=
\lim_{t\to\infty} M_t
$$

almost surely and in \(L^2\). Moreover,

$$
M_t
=
E[M_\infty\mid\mathcal F_t].
$$

Thus an element \(M\in\mathcal M\) can be identified with its terminal value \(M_\infty\).

The bracket process \(\langle M\rangle_t\) is increasing, so

$$
\langle M\rangle_\infty
=
\lim_{t\to\infty}\langle M\rangle_t
$$

exists, possibly as an extended random variable. The theorem states that it is integrable in this setting and that

$$
E[\langle M\rangle_\infty]
=
E[M_\infty^2].
$$

The space \(\mathcal M\) becomes a Hilbert space with scalar product

$$
\langle M,N\rangle_{\mathcal M}
=
E[M_\infty N_\infty].
$$

Equivalently, since \(M_t\to M_\infty\) and \(N_t\to N_\infty\) in \(L^2\),

$$
\langle M,N\rangle_{\mathcal M}
=
\lim_{t\to\infty} E[M_tN_t].
$$

This Hilbert space structure will be useful for defining stochastic integrals with respect to continuous martingales, in the same way that the \(L^2\) structure was useful for defining stochastic integrals with respect to Brownian motion.

The lecture ends at this transition point. The next step will be to connect this Hilbert space structure with the bracket process and then use it to define stochastic integrals with respect to martingales other than Brownian motion.
