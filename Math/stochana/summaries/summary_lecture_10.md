# Corrected lecture notes for recording 10

Sources:

- `Chapter3.pdf`
- `recording/Erwin-Schrödinger-Zentrum 10.txt`

Style note: corrected into coherent lecture notes rather than a verbatim transcript. Mathematical notation is written in LaTeX.

## PDF location

### Recording 10

Main PDF range:

- `Chapter3.pdf`, printed pages 70-76, PDF pages 10-16.
- Main sections:
  - End of Theorem 3.2.6 / Corollary 3.2.7, basic Ito formula
  - Corollary 3.2.8, product rule
  - Example 3.2.9, smooth functions of Brownian motion
  - Example 3.2.10, geometric Brownian motion
  - Section 3.2.2, "The quadratic variation of Ito integrals"
  - Proposition 3.2.11
  - Corollary 3.2.12
  - Example 3.2.13
  - Definition 3.2.14 and Exercises 27-28 on MLEs for geometric Brownian motion
  - Start of Section 3.3, "Quadratic variation of continuous local martingales"
  - Section 3.3.1, "Local martingales"
  - Definition 3.3.1
  - Lemma 3.3.2
  - Definition 3.3.3
  - Proposition 3.3.4
  - Start of Section 3.3.2, "The quadratic variation process"
  - Theorem 3.3.5
  - Corollaries 3.3.6 and 3.3.7

The lecture starts by emphasizing why Ito sums use left endpoints rather than arbitrary Riemann-Stieltjes sample points. It then computes quadratic variations of smooth transformations and Ito integrals, applies this to geometric Brownian motion and volatility estimation, and begins the theory of continuous local martingales and their bracket processes.

Approximate endpoint:

- Around Corollary 3.3.7 in `Chapter3.pdf`, printed page 76.
- The lecture stops just before the covariation and orthogonality discussion, which is continued in recording 11.

## Corrected notes

### 1. Left endpoints and the Ito convention

The lecture begins by returning to the construction of stochastic integrals from sums.

For a partition

$$0 = t_0 < t_1 < \cdots < t_n = T,$$

the Ito integral uses left endpoint evaluations:

$$\sum_i H_{t_i}\,(B_{t_{i+1}} - B_{t_i}).$$

This looks similar to a Riemann-Stieltjes sum, but it is not the same as the classical deterministic object. In an ordinary Riemann-Stieltjes sum, one may choose any sample point in $[t_i, t_{i+1}]$. For Ito integration, the left endpoint is part of the definition.

The left endpoint is important because it prevents anticipation. If $X$ is a stock price and $H_{t_i}$ is the number of shares held during $[t_i, t_{i+1}]$, then $H_{t_i}$ must be based on information available at time $t_i$. Using a right endpoint would allow today's trading decision to depend on tomorrow's price.

This also explains the difference between the two Brownian examples discussed earlier:

- left endpoint sums lead to the Ito integral and have expectation $0$
- right endpoint sums lead to a different correction and expectation $T$

The right endpoint convention is related to the Stratonovich integral. In this course the Ito convention is the main one.

### 2. Outlook: bracket processes

For Brownian motion, the quadratic variation exists pathwise along suitable deterministic partitions:

$$\langle B \rangle_t = t.$$

This gives:

$$B_t^2 - t$$

as a martingale.

The interpretation is that $B_t^2$ has increasing expectation, and the bracket process compensates for that increase.

The aim is to generalize this to continuous local martingales. For a general continuous local martingale $M$, one wants a process $\langle M \rangle$ such that:

$$M_t^2 - \langle M \rangle_t$$

is a local martingale.

For Brownian motion, quadratic variation sums converge almost surely under suitable partition assumptions. For general continuous local martingales, the pathwise construction no longer works in the same form. The quadratic variation sums still converge, but generally only in probability, uniformly on compact intervals.

### 3. Quadratic variation of smooth transformations

Let $X$ be real-valued, continuous, and of continuous quadratic variation. Let $f \in C^1$.

Proposition 3.2.11 states:

$$\langle f(X) \rangle_t = \int_0^t \bigl(f'(X_s)\bigr)^2 \, d\langle X \rangle_s.$$

The proof is deterministic and based on Taylor expansion.

For a partition, write:

$$\Delta_i X = X_{t_{i+1}} - X_{t_i}.$$

Then:

$$f(X_{t_{i+1}}) - f(X_{t_i}) = f'(X_{t_i})\,\Delta_i X + \mathrm{remainder}_i.$$

Squaring and summing gives the main term:

$$\sum_i \bigl(f'(X_{t_i})\bigr)^2 (\Delta_i X)^2.$$

This converges to:

$$\int_0^t \bigl(f'(X_s)\bigr)^2 \, d\langle X \rangle_s.$$

The remainder terms vanish because:

- $X$ is uniformly continuous on compact intervals
- $f'$ is continuous
- $\sum_i (\Delta_i X)^2$ converges to $\langle X \rangle_t$

Thus smooth transformations of a process with continuous quadratic variation again have continuous quadratic variation.

### 4. Quadratic variation of Ito integrals

Let $g \in C^1$, and let $G' = g$. Define:

$$Y_t = \int_0^t g(X_s) \, dX_s.$$

By the pathwise Ito formula:

$$Y_t = G(X_t) - G(X_0) - \frac{1}{2} \int_0^t g'(X_s) \, d\langle X \rangle_s.$$

The last term is of bounded variation because $\langle X \rangle$ is increasing. Adding or subtracting a bounded-variation process does not change quadratic variation.

Therefore:

$$\langle Y \rangle = \langle G(X) \rangle.$$

Using Proposition 3.2.11 with $f = G$ gives Corollary 3.2.12:

$$\langle Y \rangle_t = \int_0^t g(X_s)^2 \, d\langle X \rangle_s.$$

So the quadratic variation of an Ito integral is obtained by squaring the integrand and integrating with respect to the quadratic variation of the integrator.

### 5. Geometric Brownian motion

For geometric Brownian motion,

$$\frac{dS_t}{S_t} = \mu \, dt + \sigma \, dB_t,$$

or equivalently:

$$dS_t = \mu S_t \, dt + \sigma S_t \, dB_t.$$

The finite-variation drift part does not contribute to quadratic variation. The martingale part is:

$$\int_0^t \sigma S_s \, dB_s.$$

Since $\langle B \rangle_t = t$, Corollary 3.2.12 gives:

$$\langle S \rangle_t = \int_0^t \sigma^2 S_s^2 \, ds.$$

The drift $\mu$ drops out entirely. This is the key point: quadratic variation sees volatility, not drift.

If the price path $S$ is observed at high frequency, then in principle $\langle S \rangle_t$ is observable through sums of squared increments. The integral $\int_0^t S_s^2 \, ds$ is also observable from the price path. Thus:

$$\sigma^2 = \frac{\langle S \rangle_t}{\int_0^t S_s^2 \, ds}.$$

This explains why volatility is easier to estimate from high-frequency data than drift.

### 6. Maximum likelihood estimation for geometric Brownian motion

Assume both $\mu$ and $\sigma$ are unknown and observe:

$$S_{t_0}, S_{t_1}, \ldots, S_{t_n},$$

with equal spacing $\Delta = t_i - t_{i-1}$.

Define logarithmic returns:

$$R_i = \log\!\left(\frac{S_{t_i}}{S_{t_{i-1}}}\right).$$

From the explicit solution:

$$R_i = \left(\mu - \tfrac{1}{2}\sigma^2\right)\Delta + \sigma\,(B_{t_i} - B_{t_{i-1}}).$$

Equivalently:

$$R_i = \left(\mu - \tfrac{1}{2}\sigma^2\right)\Delta + \sigma\sqrt{\Delta}\,Z_i,$$

where $Z_i$ are independent standard normal random variables.

The MLEs have the form:

$$\hat{\sigma}^2 = \frac{1}{n\Delta} \sum_i (R_i - \bar{R})^2,$$

and

$$\hat{\mu} = \frac{1}{2}\hat{\sigma}^2 + \frac{\bar{R}}{\Delta}.$$

Here:

$$\bar{R} = \frac{1}{n} \sum_i R_i.$$

There are two different asymptotic regimes.

#### Fixed sampling frequency, long observation period

If $\Delta$ is fixed and $n \to \infty$, then the observation horizon grows. The Brownian average satisfies a law of large numbers:

$$\frac{B_{t_n} - B_{t_0}}{t_n - t_0} \to 0.$$

In this regime:

- $\hat{\sigma}^2 \to \sigma^2$
- $\hat{\mu} \to \mu$

Both estimators are consistent.

#### Fixed observation period, increasing sampling frequency

If the observation period $[0,T]$ is fixed and only the sampling frequency increases, then the volatility estimator is still consistent:

$$\hat{\sigma}^2 \to \sigma^2.$$

But the drift estimator keeps an unavoidable Brownian noise term:

$$\frac{\sigma\,(B_T - B_0)}{T}.$$

This does not vanish for fixed $T$. Hence the drift cannot be consistently estimated from one finite sample path simply by sampling more frequently.

The practical takeaway is:

- volatility is visible through quadratic variation
- drift is much harder to identify from finite-horizon data

### 7. Local martingales

The lecture then begins Section 3.3 on quadratic variation of continuous local martingales.

A stochastic process $M$ is a local martingale if there exists a localizing sequence of stopping times $\tau_n$ such that:

- $\tau_n \to \infty$ almost surely
- each stopped process $M^{\tau_n}$ is a martingale

The stopped process is:

$$M^{\tau_n}_t = M_{t \wedge \tau_n}.$$

Every martingale is a local martingale, by taking $\tau_n = \infty$. But a local martingale need not be a true martingale. Usually, proving that something is a local martingale is easier than proving that it is a true martingale.

### 8. When is a local martingale a true martingale?

Lemma 3.3.2 gives a useful sufficient condition.

Let:

$$M_t^* = \sup_{s \le t} |M_s|.$$

If $M$ is a local martingale and $M_t^* \in L^1$ for all $t$, then $M$ is a true martingale.

Proof idea:

Take a localizing sequence $\tau_n$. For $s \le t$,

$$\mathbb{E}\!\left[M_{t \wedge \tau_n} \mid \mathcal{F}_s\right] = M_{s \wedge \tau_n}.$$

As $n \to \infty$, the stopped variables converge to $M_t$ and $M_s$. The domination

$$|M_{t \wedge \tau_n}| \le M_t^*$$

allows dominated convergence. Hence:

$$\mathbb{E}\!\left[M_t \mid \mathcal{F}_s\right] = M_s.$$

In particular, every bounded local martingale is a true martingale.

### 9. Class D and class DL

The lecture then introduces uniform-integrability criteria.

Let $\mathcal{T}$ be the set of all finite stopping times, and let $\mathcal{T}_T$ be the set of all stopping times bounded by a fixed deterministic time $T$.

A process $X$ is of class $D$ if:

$$\{X_\tau : \tau \in \mathcal{T}\}$$

is uniformly integrable.

It is of class $DL$ if, for every $T > 0$,

$$\{X_\tau : \tau \in \mathcal{T}_T\}$$

is uniformly integrable.

Every uniformly integrable martingale is of class $D$, hence of class $DL$.

Conversely, a local martingale of class $DL$ is a true martingale. The reason is again that uniform integrability allows limits to pass through conditional expectations:

$$M_{s \wedge \tau_n} = \mathbb{E}\!\left[M_{t \wedge \tau_n} \mid \mathcal{F}_s\right].$$

For continuous local martingales, Proposition 3.3.4 gives the exact criterion:

$$M \text{ is a martingale} \iff M \text{ is of class } DL.$$

The implication from martingale to class $DL$ uses optional sampling:

$$M_\tau = \mathbb{E}\!\left[M_T \mid \mathcal{F}_\tau\right], \quad \text{for } \tau \le T.$$

Families of conditional expectations of a fixed integrable random variable are uniformly integrable.

### 10. The bracket theorem for continuous local martingales

The main theorem introduced at the end of the lecture is Theorem 3.3.5.

Let $M$ be a continuous local square-integrable martingale with respect to a filtration satisfying the usual conditions, and assume $M_0 = 0$.

Then there exists an almost surely unique continuous process $\langle M \rangle$, called the bracket process, compensator, or quadratic variation process, such that:

- $\langle M \rangle_0 = 0$
- $\langle M \rangle$ is non-decreasing
- $M_t^2 - \langle M \rangle_t$ is a continuous local martingale
- for any sequence of partitions with mesh tending to zero,

$$V_t^2(M, \Pi_n) \to \langle M \rangle_t$$

uniformly on compact time intervals in probability.

The convergence mode is abbreviated $\mathrm{ucp}$, meaning uniformly on compact intervals in probability:

$$\sup_{s \le T} \bigl| V_s^2(M, \Pi_n) - \langle M \rangle_s \bigr| \to 0$$

in probability.

For Brownian motion, the bracket is $\langle B \rangle_t = t$. For a general continuous local martingale, the bracket exists, but the quadratic variation sums need not converge almost surely pathwise; ucp convergence is the general statement.

### 11. Consequences and stopping

If $M$ is a true square-integrable continuous martingale, then:

$$M^2 - \langle M \rangle$$

is a true martingale, and therefore:

$$\mathbb{E}\!\left[M_t^2\right] = \mathbb{E}\!\left[\langle M \rangle_t\right].$$

This identity is useful for deriving square-integrability and uniform-integrability estimates.

If $A$ is of bounded variation and $M$ is a continuous local martingale starting at zero, then:

$$\langle M + A \rangle = \langle M \rangle.$$

The bounded-variation part has no quadratic variation.

Finally, brackets are compatible with stopping. For a stopping time $\tau$,

$$\langle M^\tau \rangle_t = \langle M \rangle_{\tau \wedge t}.$$

This follows from optional sampling applied to $M^2 - \langle M \rangle$ and uniqueness of the bracket process.

The lecture ends at this point, before the discussion of covariation and orthogonality.

## Main corrections made to the transcript

The transcript repeatedly misrecognized key terms. The following corrections were applied throughout:

- "Kito", "E2", "Eto" -> Ito
- "Stratonovitjti" -> Stratonovich
- "brown example", "browning", "crony motion" -> Brownian motion
- "marting game", "martiquet", "marking here" -> martingale / local martingale
- "quadratic permeation", "chromatic variation" -> quadratic variation
- "Lehmann sum" -> Riemann sum
- "pass-wise" -> pathwise
- "vulnerability case" -> Brownian case / bounded-variation case, depending on context
- "engraved", "anti-reversive of cabbage" -> antiderivative
- "option of sampling" -> optional sampling
- "local lighting sequence" -> localizing sequence
- "running surface" -> running supremum / running maximum
- "class Deo / class DL" -> class D / class DL
- "uniform infinity" -> uniform integrability
- "usual conditions", sometimes garbled, kept as usual conditions
- `UCP` -> uniformly on compact intervals in probability
