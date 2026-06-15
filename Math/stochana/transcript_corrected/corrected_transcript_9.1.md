# Clean transcript for recording 9.1

Sources:

- `transcript_original/Erwin-Schrödinger-Zentrum 9.1.txt`
- `lecture notes/Chapter3.pdf`

Style note: this is a cleaned transcript, not a word-for-word transcript. Repetitions, false starts, and unrecoverable filler have been removed. Mathematical terms and notation have been corrected against the lecture notes and written in LaTeX.

## Source warning

The source files labeled `9.1` do not appear to be the intended chronological lecture 9.1. I verified the audio directly:

- `recordings/Erwin-Schrödinger-Zentrum 9.1.m4a` and `recordings/Erwin-Schrödinger-Zentrum 10.m4a` have the same decoded audio hash:

  ```text
  MD5=12abd8d4f7f2ba8b0ea9e7af44f83906
  ```

- A fresh Whisper snippet from `9.1.m4a` starts with the Ito left-endpoint discussion.
- A fresh Whisper snippet from `10.m4a` starts with the same Ito left-endpoint discussion.
- `recordings/Erwin-Schrödinger-Zentrum 9.m4a` is different audio and starts with the Donsker/rescaled-random-walk material.

Therefore, the cleaned transcript below is a correction of the provided file `transcript_original/Erwin-Schrödinger-Zentrum 9.1.txt`, but that raw transcript comes from audio duplicated with lecture 10. It should not be treated as the real chronological lecture 9.1 unless the source recording is replaced.

## Transcript-to-note correspondence

This table is based on `transcript_original/Erwin-Schrödinger-Zentrum 9.1.txt`. The line ranges refer to that raw transcript and mark where each part of the cleaned transcript appears in `Chapter3.pdf`.

| Raw `9.1` transcript lines | Corrected section below | Chapter 3 location |
|---:|---|---|
| 1-43 | Ito left-endpoint convention, comparison with right endpoints / Stratonovich, trading interpretation | Section 3.2.1, setup for the basic Ito formula and Example 3.2.9 |
| 44-122 | Brownian quadratic variation, $B_t^2-\langle B\rangle_t$, outlook toward martingale brackets | Section 3.2 and beginning of Section 3.3 |
| 123-278 | Quadratic variation of smooth transformations and Ito integrals | Section 3.2.2, Proposition 3.2.11 and Corollary 3.2.12 |
| 279-704 | Geometric Brownian motion, observable quadratic variation, volatility/drift estimation | Example 3.2.13 and the following estimation discussion/exercises |
| 705-747 | Definition of local martingale and localizing sequence | Section 3.3.1, Definition 3.3.1 |
| 748-780 | Running supremum condition for a local martingale to be true | Section 3.3.1, Lemma 3.3.2 |
| 781-847 | Class $D$, class $DL$, and optional sampling criterion | Section 3.3.1, Definition 3.3.3 and Proposition 3.3.4 |
| 848-926 | Statement of the bracket theorem for continuous local square-integrable martingales | Section 3.3.2, Theorem 3.3.5 |
| 927-959 | Brackets and stopping | Corollary 3.3.7 |

## Corrected transcript

**Source: raw `9.1` lines 1-122. Lecture note: Chapter 3, Section 3.2.1, setup for the basic Ito formula and Example 3.2.9.**

There is one important difference between the stochastic sums we are using and ordinary Riemann-Stieltjes sums. We take a partition

$$0 = t_0 < t_1 < \cdots < t_n = T,$$

and we approximate the integrand by evaluating it at the left endpoint of each interval. This is almost a Riemann-Stieltjes sum, but only almost. In a classical Riemann-Stieltjes sum, one could evaluate the function at any point between $t_i$ and $t_{i+1}$. Here the left endpoint is built into the definition.

This matters. At the beginning of the section we compared two approximations of a Brownian sample path. One approximation used left endpoints, the other used right endpoints. The expectations came out differently. In the left-endpoint case the expectation was zero, while in the right-endpoint case it was $T$. The left-endpoint convention gives the Ito integral. The right-endpoint convention is related to the Stratonovich integral.

The Ito integral is the more common object in this course, and in many applications there are good reasons for using it. For example, if $X$ is a stock price process, then at time $t_i$ we decide how many shares to hold until the next trading time. If we chose a right endpoint, our decision at time $t_i$ would depend on the future stock price at $t_{i+1}$. That is not a reasonable trading strategy. So the left-endpoint evaluation is essential.

Our typical application so far was $X$ equal to a Brownian sample path. We showed that Brownian motion has quadratic variation pathwise, for almost every $\omega$. Therefore, for almost every path, we can plug the path into the deterministic Ito formula developed for continuous functions with continuous quadratic variation. In that formula, the correction term is an ordinary integral with respect to the quadratic variation. For Brownian motion this becomes a usual $dt$ integral, since $\langle B \rangle_t = t$.

For Brownian motion, we first proved convergence of the sums of squared increments in $L^2$. This required essentially only the distributional properties of Brownian increments: independent, stationary, normally distributed increments. Then, with a stronger assumption on the partitions, we upgraded the convergence to almost sure convergence. We also saw that

$$B_t^2 - \langle B \rangle_t$$

is a martingale. Since $\langle B \rangle_t = t$, the process $B_t^2 - t$ is a martingale. The bracket compensates for the increasing expected value of $B_t^2$.

The outlook is that for a general continuous martingale we will still be able to define a bracket process $\langle M \rangle$ such that

$$M_t^2 - \langle M \rangle_t$$

is a martingale or local martingale. But in general we cannot define the bracket pathwise in the same way as for Brownian motion. Instead, sums of squared increments still converge, but only in probability, uniformly on compact time intervals.

**Source: raw `9.1` lines 123-278. Lecture note: Chapter 3, Section 3.2.2, Proposition 3.2.11 and Corollary 3.2.12.**

Before proving this general result, we discuss the quadratic variation of Ito integrals.

Suppose $X$ is continuous and has continuous quadratic variation. We know from the Ito formula when an integral of the form

$$Y_t = \int_0^t g(X_s) \, dX_s$$

is defined by the pathwise construction. Namely, we need $g$ to be a derivative: $g = G'$ for some function $G$. Since the Ito formula involves a second derivative of $G$, we assume $g$ is $C^1$.

The question is: what is the quadratic variation of $Y$?

We begin with a simple deterministic proposition. Let $X$ be real-valued, continuous, and of continuous quadratic variation. Let $f$ be $C^1$. Then $f(X)$ also has continuous quadratic variation, and

$$\langle f(X) \rangle_t = \int_0^t \bigl(f'(X_s)\bigr)^2 \, d\langle X \rangle_s.$$

The intuition is clear. To compute quadratic variation, we sum squared increments. Since $f$ is smooth, Taylor's formula gives

$$f(X_{t_{i+1}}) - f(X_{t_i}) = f'(X_{t_i})\,\Delta_i X + \mathrm{remainder}.$$

Squaring gives the main term

$$\bigl(f'(X_{t_i})\bigr)^2 (\Delta_i X)^2,$$

and the remainder terms vanish as the mesh of the partition goes to zero. The vanishing follows from continuity of $f'$ and continuity of $X$, because the increments of $X$ become uniformly small on compact intervals. The sums of $(\Delta_i X)^2$ converge to $\langle X \rangle$.

Now consider the Ito integral

$$Y_t = \int_0^t g(X_s) \, dX_s,$$

where $g$ is $C^1$ and $G' = g$. By Ito's formula,

$$\int_0^t g(X_s) \, dX_s = G(X_t) - G(X_0) - \frac{1}{2} \int_0^t g'(X_s) \, d\langle X \rangle_s.$$

The last term is of bounded variation, because $\langle X \rangle$ is increasing. Adding or subtracting a bounded-variation process does not change quadratic variation. Therefore the quadratic variation of $Y$ is the same as the quadratic variation of $G(X)$. Applying the previous proposition gives

$$\langle Y \rangle_t = \int_0^t g(X_s)^2 \, d\langle X \rangle_s.$$

This says: the quadratic variation of an Ito integral is obtained by squaring the integrand and integrating with respect to the quadratic variation of the integrator.

**Source: raw `9.1` lines 279-704. Lecture note: Chapter 3, Example 3.2.13 and the parameter-estimation discussion following it.**

As an example, take geometric Brownian motion:

$$\frac{dS_t}{S_t} = \mu \, dt + \sigma \, dB_t.$$

Equivalently,

$$dS_t = \mu S_t \, dt + \sigma S_t \, dB_t.$$

The finite-variation part $\mu S_t \, dt$ does not contribute to quadratic variation. The martingale part is the Ito integral

$$\int_0^t \sigma S_s \, dB_s.$$

Therefore

$$\langle S \rangle_t = \int_0^t \sigma^2 S_s^2 \, ds.$$

This has an important interpretation. If $S_t$ is the stock price, then both $S$ and its quadratic variation are, at least theoretically, observable from high-frequency data. Hence

$$\sigma^2 = \frac{\langle S \rangle_t}{\int_0^t S_s^2 \, ds}.$$

The drift $\mu$ drops out of the quadratic variation, because drift is finite variation. This makes volatility much easier to estimate from a single sample path than drift.

Let us look more carefully at parameter estimation for geometric Brownian motion. Suppose both $\mu$ and $\sigma$ are unknown. We observe prices at times

$$t_0, t_1, \ldots, t_n,$$

with equal spacing $\Delta = t_i - t_{i-1}$. Define the logarithmic returns

$$R_i = \log\!\left(\frac{S_{t_i}}{S_{t_{i-1}}}\right).$$

From the explicit solution of geometric Brownian motion,

$$R_i = \left(\mu - \tfrac{1}{2}\sigma^2\right)\Delta + \sigma\,(B_{t_i} - B_{t_{i-1}}).$$

Equivalently,

$$R_i = \left(\mu - \tfrac{1}{2}\sigma^2\right)\Delta + \sigma\sqrt{\Delta}\,Z_i,$$

where the $Z_i$ are independent standard normal random variables.

The maximum likelihood estimator for the volatility is the sample variance of the log returns, scaled by $1/\Delta$:

$$\hat{\sigma}^2 = \frac{1}{n\Delta} \sum_i (R_i - \bar{R})^2.$$

The corresponding estimator for the drift is

$$\hat{\mu} = \frac{1}{2}\hat{\sigma}^2 + \frac{\bar{R}}{\Delta}.$$

To see what information about the drift is contained in the data, write $T = n\Delta$ and average the log returns under the true data-generating parameters:

$$\bar{R} = \left(\mu - \tfrac{1}{2}\sigma^2\right)\Delta + \frac{\sigma}{n}(B_T - B_0).$$

Dividing by $\Delta$ gives

$$\frac{\bar{R}}{\Delta} = \mu - \tfrac{1}{2}\sigma^2 + \frac{\sigma(B_T - B_0)}{T}.$$

Here $\sigma$ is the true volatility parameter, not the estimator. Substituting this expression into the drift estimator gives

$$\hat{\mu} = \mu + \tfrac{1}{2}(\hat{\sigma}^2 - \sigma^2) + \frac{\sigma(B_T - B_0)}{T}.$$

Thus, even when $\hat{\sigma}^2$ is well estimated from high-frequency data, the drift estimator is affected by the single Brownian displacement $B_T - B_0$ over the whole interval.

If the sampling frequency is fixed and the observation period tends to infinity, then the Brownian noise in the average return disappears by the law of large numbers. In that case both estimators converge to the true parameters.

But if the observation period is fixed and we only increase the sampling frequency, the situation changes. The volatility estimator still converges to the true volatility, because it is based on quadratic variation. However, the drift estimator still contains the term

$$\frac{\sigma\,(B_T - B_0)}{T}.$$

This term does not vanish when $T$ is fixed. Hence the drift estimate has unavoidable noise. Even if we observe the path very frequently on a finite time interval, we cannot estimate the drift consistently from that one finite sample path. This is the practical message: volatility is visible in quadratic variation, but drift is much harder to infer.

**Source: raw `9.1` lines 705-747. Lecture note: Chapter 3, Section 3.3.1, Definition 3.3.1.**

We now turn to quadratic variation of continuous local martingales.

A local martingale is a stochastic process that becomes a martingale after stopping it properly. Formally, a process $M$ is a local martingale if there exists a localizing sequence of stopping times $\tau_n$ such that

$$\tau_n \to \infty \quad \text{almost surely},$$

and each stopped process

$$M^{\tau_n}_t = M_{t \wedge \tau_n}$$

is a martingale.

Every martingale is a local martingale: just take $\tau_n = \infty$. But the converse is not always true. It is often easy to prove that a process is a local martingale, while proving it is a true martingale can require additional work. Later we will see examples of local martingales that are not true martingales.

**Source: raw `9.1` lines 748-780. Lecture note: Chapter 3, Section 3.3.1, Lemma 3.3.2.**

When is a local martingale a true martingale? One useful sufficient condition is integrability of the running maximum. Let

$$M_t^* = \sup_{s \le t} |M_s|.$$

If $M_t^*$ is integrable for every $t$, then $M$ is a martingale. Indeed, take a localizing sequence $\tau_n$. Since the stopped process is a martingale,

$$\mathbb{E}\!\left[M_{t \wedge \tau_n} \mid \mathcal{F}_s\right] = M_{s \wedge \tau_n}.$$

As $n \to \infty$, the stopped variables converge to $M_t$ and $M_s$. The running maximum gives a dominating integrable random variable, so dominated convergence allows the limit to pass through conditional expectation. Thus

$$\mathbb{E}\!\left[M_t \mid \mathcal{F}_s\right] = M_s.$$

In particular, every bounded local martingale is a true martingale.

There is also a more refined criterion involving uniform integrability and class $D$ or class $DL$.

**Source: raw `9.1` lines 781-847. Lecture note: Chapter 3, Section 3.3.1, Definition 3.3.3 and Proposition 3.3.4.**

Let $\mathcal{T}$ denote the set of finite stopping times, and let $\mathcal{T}_T$ denote the set of stopping times bounded by a deterministic time $T$. A process $X$ is of class $D$ if the family

$$\{X_\tau : \tau \in \mathcal{T}\}$$

is uniformly integrable. It is of class $DL$ if, for every deterministic $T$, the family

$$\{X_\tau : \tau \in \mathcal{T}_T\}$$

is uniformly integrable.

Every uniformly integrable martingale is of class $D$, hence also of class $DL$. Conversely, a local martingale of class $DL$ is a true martingale, because uniform integrability lets us pass to the limit in the stopped martingale property.

For continuous local martingales, the criterion is exact:

$$M \text{ is a martingale} \iff M \text{ is of class } DL.$$

One direction follows from optional sampling. If $M$ is a continuous martingale and $\tau \le T$, then

$$M_\tau = \mathbb{E}\!\left[M_T \mid \mathcal{F}_\tau\right].$$

A family of conditional expectations of a fixed integrable random variable is uniformly integrable, so the stopped values form a uniformly integrable family.

The converse is the general local martingale plus class $DL$ argument.

**Source: raw `9.1` lines 848-926. Lecture note: Chapter 3, Section 3.3.2, Theorem 3.3.5.**

Now we state the theorem we are heading toward. Let $M$ be a continuous local square-integrable martingale, starting at zero, with respect to a filtration satisfying the usual conditions. Then there exists an almost surely unique continuous process $\langle M \rangle$, called the bracket process, compensator, or quadratic variation process, such that:

$$\langle M \rangle_0 = 0,$$

$\langle M \rangle$ is non-decreasing,

$$M_t^2 - \langle M \rangle_t$$

is a continuous local martingale, and for any sequence of partitions with mesh tending to zero,

$$\sum_i (M_{t_{i+1}} - M_{t_i})^2 \to \langle M \rangle_t$$

uniformly on compact time intervals in probability.

This generalizes the Brownian result. For Brownian motion, $\langle B \rangle_t = t$. For general continuous local martingales, the bracket still compensates the square process, but the convergence of quadratic variation sums is in probability rather than almost surely.

If $M$ is actually a square-integrable continuous martingale, then $M^2 - \langle M \rangle$ is a true martingale, and

$$\mathbb{E}\!\left[M_t^2\right] = \mathbb{E}\!\left[\langle M \rangle_t\right].$$

This identity is useful for proving uniform integrability and for estimating square-integrable martingales in terms of their compensators.

**Source: raw `9.1` lines 927-959. Lecture note: Chapter 3, Corollary 3.3.7.**

Finally, brackets behave naturally under stopping. If $\tau$ is a stopping time, then

$$\langle M^\tau \rangle_t = \langle M \rangle_{t \wedge \tau}.$$

Indeed, optional sampling applied to $M^2 - \langle M \rangle$ shows that

$$M_{t \wedge \tau}^2 - \langle M \rangle_{t \wedge \tau}$$

is again a local martingale. By uniqueness of the bracket process, the bracket of the stopped martingale is the stopped bracket.

The raw transcript ends here with the lecturer noting that time is out and stopping the lecture.

## Main transcript corrections

- "Kito", "E2", "Eto" -> Ito
- "Stratonovitjti" -> Stratonovich
- "brown example", "browning", "crony motion" -> Brownian motion
- "marting game", "martiquet", "marking here" -> martingale / local martingale
- "quadratic permeation", "chromatic variation" -> quadratic variation
- "Lehmann sum" -> Riemann sum
- "pass-wise" -> pathwise
- "bracket / compensator" normalized as $\langle M \rangle$
- "option of sampling" -> optional sampling
- "local lighting sequence" -> localizing sequence
- "running surface" -> running supremum / running maximum
- "class Deo / DL" -> class D / class DL
