# Corrected lecture notes for recording 12

Sources:

- `Chapter3.pdf`
- `Chapter 4.pdf`
- `recording/Erwin-Schrödinger-Zentrum 12.txt`

Style note: corrected into coherent lecture notes rather than a verbatim transcript. Mathematical notation is kept in plain text / Unicode style.

## PDF location

### Recording 12

Main PDF range:

- `Chapter3.pdf`, printed pages 81-83, PDF pages 21-23.
- `Chapter 4.pdf`, printed pages 85-89, PDF pages 1-5.

Main sections:

- End of Section 3.3.3, "Proof of Theorem 3.3.5 for bounded martingales"
- Section 3.3.4, "Proof of Theorem 3.3.5"
- Remark 3.3.13
- Chapter 4 introduction, "The Stochastic Integral"
- Section 4.1, "Stochastic integration with respect to Brownian motion"
- Definition 4.1.1
- Lemma 4.1.2, Ito isometry for elementary processes
- Proposition 4.1.3
- Definition 4.1.4
- Proposition 4.1.5, proof up to the density argument and progressive modifications
- Remark 4.1.6

The lecture finishes the construction and uniqueness of the bracket process, explains why the general local martingale case only gives ucp convergence, and then begins Chapter 4 by constructing the Ito integral with respect to Brownian motion.

Approximate endpoint:

- Around Remark 4.1.6 in `Chapter 4.pdf`, printed page 89.
- The lecture does not substantially cover Proposition 4.1.7 yet, except as a preview.

## Corrected notes
### 1. Recap and completion of the bracket construction

The lecture starts by recalling the previous construction.

For a bounded continuous martingale `M` starting at zero, we constructed:

`A^n_t = quadratic variation sum along Pi^n`,

and

`N^n_t = M_t^2 - A^n_t`.

The sequence `N^n` is Cauchy in `L2(Omega; C[0,T])`, so it converges to a continuous process `N`.

Then define:

`<M>_t = M_t^2 - N_t`.

This gives the bracket process in the bounded martingale case.

The convergence of `A^n` to `<M>` is strong in this bounded case: it is L2 convergence in the space of continuous functions on compact time intervals.

### 2. Uniqueness of the bracket process

Suppose there are two candidates `A` and `A'`, both continuous, non-decreasing, starting at zero, such that:

`M^2 - A`

and

`M^2 - A'`

are continuous local martingales.

Subtracting gives:

`A - A'`

as a continuous local martingale. But `A - A'` is also of bounded variation, since it is the difference of two non-decreasing processes.

By Lemma 3.3.10, a continuous local martingale of bounded variation is constant. Since `A_0 = A'_0 = 0`, the constant is zero. Therefore:

`A = A'`.

This proves uniqueness.

The normalization `A_0 = 0` is important. Without fixing the starting value, the compensator would only be unique up to an additive constant.

### 3. General continuous local martingales

The proof then moves from bounded martingales to general continuous local martingales.

Let `M` be a continuous local martingale. Choose a localizing sequence `tau_n` such that the stopped process:

`M^n_t = M_{t ∧ tau_n}`

is a bounded martingale. If needed, refine the stopping times by stopping when `|M_t| >= n`.

For each stopped process `M^n`, the bracket `<M^n>` exists by the bounded case.

The brackets are consistent:

on `[0, tau_m]`, the processes `M^n` and `M^m` agree for `n >= m`, so their brackets agree there as well.

Therefore one can define the bracket of `M` by patching these stopped brackets together:

`<M>_t = lim_n <M^n>_t`.

This process is continuous, starts at zero, and is non-decreasing.

Moreover, for each `m`,

`(M^2 - <M>) stopped at tau_m`

is a martingale, because it coincides with:

`(M^m)^2 - <M^m>`.

Thus:

`M^2 - <M>`

is a continuous local martingale.

### 4. Why the convergence weakens to ucp

In the bounded case, the quadratic variation sums converge in L2 in the space of continuous functions.

In the general local martingale case, we only get convergence in probability, uniformly on compact time intervals.

Reason:

- For each stopped process `M^n`, we have L2 convergence of quadratic variation sums to `<M^n>`.
- On the event `{tau_n > T}`, the original process `M` and stopped process `M^n` coincide on `[0,T]`.
- The probability of `{tau_n <= T}` goes to zero as `n -> infinity`.

So for large `n`, with high probability, the stopped and unstopped processes agree on `[0,T]`. This lets us transfer the convergence from the bounded stopped process to the original process, but only in probability.

This proves the ucp convergence:

`V^2_t(M, Pi^m) -> <M>_t`

uniformly for `t` in compact intervals, in probability.

### 5. Why the bracket matters

The bracket process is not only a quadratic variation object. It gives the correct measure for defining stochastic integrals.

For Brownian motion:

`<B>_t = t`,

so the natural integrability condition involves ordinary time integration:

`E integral_0^T f_s^2 ds < infinity`.

For a general continuous local martingale `M`, the bracket is random, and the natural integrability condition becomes:

`E integral_0^T f_s^2 d<M>_s < infinity`.

So the bracket tells us which integrands are square-integrable with respect to the martingale.

The lecture then transitions into Chapter 4: stochastic integration.

## Chapter 4 begins: stochastic integration

### 6. Overall goal

We fix:

- a probability space `(Omega, F, P)`
- a filtration `(F_t)` satisfying the usual conditions
- a continuous local martingale `M`

The goal is to define:

`integral_0^t f_s dM_s`

for a large class of processes `f`.

The lecture emphasizes an important point:

We do not start with Riemann sums as the definition. Instead, stochastic integration is first constructed by functional-analytic methods. Only later do we prove that the integral can also be obtained as a limit of Riemann sums, in probability.

This is one of Ito's key insights: in general, stochastic integrals cannot be built path by path. They need a probabilistic Hilbert-space construction.

The first case studied is Brownian motion, where `M = B`.

### 7. Elementary/simple processes

A simple or elementary process has the form:

`phi_t(omega) = sum_j e_j(omega) 1_(t_j,t_{j+1}](t)`.

Here:

- `0 = t_0 < t_1 < t_2 < ...`
- each `e_j` is `F_{t_j}`-measurable
- the `e_j` are uniformly bounded

The condition `e_j is F_{t_j}`-measurable is crucial. It means the value of the integrand on `(t_j,t_{j+1}]` only depends on information available at the left endpoint.

For such simple processes, the stochastic integral with respect to Brownian motion is defined by:

`integral_0^T phi_t dB_t = sum_j e_j (B_{t_{j+1}} - B_{t_j})`,

with the usual convention that the final interval is stopped at `T`.

The class of simple processes is denoted `L0`.

### 8. Ito isometry for simple processes

The main result is the Ito isometry:

`E[(integral_0^T phi_t dB_t)^2] = E[integral_0^T phi_t^2 dt]`.

This is the key identity that makes the construction work.

Interpretation:

- The left side is the L2 norm of the stochastic integral as a random variable.
- The right side is the L2 norm of the integrand on `[0,T] x Omega`, with respect to `dt x P`.

So the integral map preserves the relevant L2 norm.

Proof idea:

When expanding the square of the stochastic integral, one gets terms:

`E[e_i e_j Delta_i B Delta_j B]`.

If `i = j`, then:

`E[(Delta_j B)^2 | F_{t_j}] = t_{j+1} - t_j`.

This gives the diagonal contribution:

`E[e_j^2] (t_{j+1} - t_j)`.

If `i < j`, then condition on `F_{t_j}`. The factor `Delta_j B` has conditional expectation zero, so the cross term vanishes:

`E[Delta_j B | F_{t_j}] = 0`.

Thus only the diagonal terms remain, and they are exactly the time integral of `phi^2`.

### 9. Stochastic integrals of simple processes are martingales

For a simple process `phi`, define:

`I_t(phi) = integral_0^t phi_s dB_s`.

Then `I(phi)` is:

- continuous
- adapted
- square-integrable
- a martingale
- starting at zero

Starting at zero and adaptedness follow directly from the construction. Square-integrability follows from the Ito isometry.

The martingale property follows by conditioning on `F_t`. Future Brownian increments have conditional expectation zero, and the coefficients are measurable with respect to the appropriate past sigma-field.

Thus the stochastic integral defines a linear map:

`I : L0 -> M^c,0_2`,

where `M^c,0_2` is the space of continuous square-integrable martingales starting at zero.

### 10. Which processes can be approximated?

The next goal is to extend the integral from simple processes to a larger class.

Two questions must be answered:

1. Which processes can be approximated by simple processes?
2. If `phi_n -> f`, do the integrals `I(phi_n)` converge?

The Ito isometry answers the second question. If the integrands converge in the correct L2 norm, then the stochastic integrals converge in L2.

For Brownian motion, define `L2` as the class of jointly measurable and adapted processes `f_t(omega)` such that, for every finite `T`,

`E integral_0^T f_t(omega)^2 dt < infinity`.

A metric is introduced to combine the L2 norms over all finite time intervals.

The lecture notes that, strictly speaking, one should work with equivalence classes. Changing a process on a null set can affect adaptedness or progressive measurability, so the issue is subtle. The course postpones the full technical treatment until the general martingale case.

### 11. Density of simple processes

Proposition 4.1.5 says that simple processes are dense in this `L2` space.

The proof proceeds in steps.

#### Step 1: bounded and pathwise continuous

Assume `f` is uniformly bounded and `t -> f_t(omega)` is continuous for almost every `omega`.

Approximate `f` by left endpoint step functions:

`phi^n_t = sum_j f_{t_j} 1_(t_j,t_{j+1}](t)`.

By continuity, these converge pointwise. By boundedness, dominated convergence gives convergence in L2 on `[0,T]`.

#### Step 2: bounded and progressively measurable

Now drop continuity but keep boundedness and progressive measurability.

Smooth `f` in time by averaging:

`f^m_t = m integral_{(t - 1/m)+}^t f_s ds`.

This is a moving average. It is bounded and continuous in `t`.

Progressive measurability is preserved because time integration of a progressively measurable process remains progressively measurable.

By Step 1, each `f^m` can be approximated by simple processes.

Then use the fundamental theorem of calculus and Fubini's theorem to show:

`f^m -> f`

almost everywhere with respect to `dt x P`, and hence in L2 by boundedness.

#### Step 3: bounded, adapted, jointly measurable

Now assume `f` is bounded, jointly measurable, and adapted, but not necessarily progressively measurable.

Use the result from Chapter 1: under the usual conditions, such a process has a progressively measurable modification `g`.

Since `f` and `g` agree for each fixed time almost surely, their time integrals agree up to indistinguishability. More concretely, Fubini gives:

`E integral_0^T 1_{f_s != g_s} ds = 0`.

Therefore the integrated process built from `g` is a modification of the one built from `f`.

Because the integrated process is continuous and adapted, it is progressively measurable. Then the previous approximation argument can be applied.

#### Step 4: remove boundedness

For a general square-integrable process, truncate:

`h^n_t = max(-n, min(f_t, n))`.

The truncated processes are bounded, and they converge to `f` in L2 by dominated convergence. Combining this with the previous steps gives density of simple processes.

### 12. What was actually proved

The formal statement says:

`L0 is dense in L2`.

But the proof actually shows something slightly more informative:

Simple processes approximate through progressively measurable representatives.

This distinction becomes important later, when the integrator is a general continuous local martingale and the bracket process is random. Then predictability, progressiveness, and equivalence classes have to be handled more carefully.

The lecture ends by previewing the next step:

Using the Ito isometry, the integral map on simple processes extends uniquely to all of `L2`. This gives the Ito integral with respect to Brownian motion for all square-integrable adapted integrands.

## Main corrections made to the transcript
The transcript repeatedly misrecognized key terms. The following corrections were applied throughout:

- "Bracken process", "Bracket", "compensator" -> bracket process / compensator
- "martling", "martingate", "marking here", "multicore" -> martingale / local martingale
- "square interoperability" -> square integrability
- "foreground emotion", "brownie motion" -> Brownian motion
- "co-variation", "crossvariation" -> covariation / cross-variation
- "option of sampling" -> optional sampling
- "usual conditions", sometimes transcribed as "integral conditions" -> usual conditions
- "E2", "equal isometry" -> Ito isometry
- "L back times P" -> Lebesgue measure times probability measure, `dt x P`
- "central functions" -> simple functions
- "progressively measured" -> progressively measurable
- "jointly measurable plus adaptability" -> jointly measurable and adapted
- "UCP" -> uniformly on compact time intervals in probability

Some parts of recording 12 contain long stretches of unrecoverable repeated or garbled audio. Those stretches were omitted when they did not add mathematical content.
