# Corrected lecture notes for recording 11

Sources:

- `Chapter3.pdf`
- `recording/Erwin-Schrödinger-Zentrum 11.txt`

Style note: corrected into coherent lecture notes rather than a verbatim transcript. Mathematical notation is kept in plain text / Unicode style.

## PDF location

### Recording 11

Main PDF range:

- `Chapter3.pdf`, printed pages 76-81, PDF pages 16-21.
- Main sections:
  - Section 3.3.2, "The quadratic variation process"
  - Covariation process and orthogonality of martingales
  - Proposition 3.3.8
  - Remark 3.3.9
  - Lemma 3.3.10
  - Start of Section 3.3.3, "Proof of Theorem 3.3.5 for bounded martingales"
  - Lemma 3.3.11 and Corollary 3.3.12
  - Beginning of the construction of the bracket process for bounded martingales

The lecture starts by recalling Theorem 3.3.5 and the bracket process. It then discusses covariation, orthogonality, the fact that bounded-variation local martingales are constant, and begins the proof of existence of the bracket for bounded martingales.

Approximate endpoint:

- Around the construction of `A^n_t` and `N^n_t = M_t^2 - A^n_t` in Section 3.3.3.
- The lecture ends before the proof is fully finished.

## Corrected notes
### 1. Recap: bracket process

The lecture begins by recalling the aim of Section 3.3.2.

For a continuous local square-integrable martingale `M` starting at zero, we want to construct a process `<M>` such that:

- `<M>_0 = 0`
- `<M>` is continuous and non-decreasing
- `M_t^2 - <M>_t` is a continuous local martingale
- sums of squared increments of `M` converge to `<M>` uniformly on compact time intervals in probability

The process `<M>` is called the bracket process, compensator, or quadratic variation process.

The intuition is that `M^2` is usually a submartingale. The bracket `<M>` compensates for the increasing part, so that `M^2 - <M>` becomes a local martingale.

For Brownian motion, the bracket is just `<B>_t = t`. For a general continuous local martingale, the bracket still exists, but the convergence of quadratic sums is weaker: in general it is convergence in probability, uniformly on compact time intervals.

### 2. Covariation and polarization

Given two continuous square-integrable local martingales `M` and `N`, their covariation is defined by polarization:

`<M,N> = (1/4)(<M+N> - <M-N>)`.

This definition makes sense because sums and differences of continuous square-integrable local martingales are again continuous square-integrable local martingales.

The covariation is symmetric and bilinear. It is the limit, in the ucp sense, of sums of products of increments:

`sum_i (M_{t_{i+1}} - M_{t_i})(N_{t_{i+1}} - N_{t_i}) -> <M,N>_t`.

The product of two martingales is usually not a martingale. The correction term is the covariation:

`M_t N_t - <M,N>_t`

is a continuous local martingale.

This follows from polarization because:

`M N - <M,N> = (1/4)((M+N)^2 - <M+N>) - (1/4)((M-N)^2 - <M-N>)`.

Each term on the right is a continuous local martingale.

### 3. Orthogonality of martingales

Two continuous local martingales `M` and `N` are called orthogonal if:

`<M,N> = 0`.

In that case:

`M_t N_t`

is itself a continuous local martingale.

For square-integrable martingales, this also means their increments are conditionally uncorrelated:

`E[(M_t - M_s)(N_t - N_s) | F_s] = 0`

for `s <= t`.

The lecture emphasized the distinction between ordinary orthogonality and this martingale notion of orthogonality. Here orthogonality is expressed through the covariation process.

Conversely, if the product `M N` is a local martingale, then `M N - <M,N>` is also a local martingale. Subtracting gives `<M,N>` as a local martingale. But `<M,N>` is of bounded variation, since it is a difference of two increasing bracket processes. A local martingale of bounded variation must be constant. Since `<M,N>` starts at zero, it must vanish. Hence:

`M N is a local martingale` iff `<M,N> = 0`.

This equivalence uses the lemma that continuous local martingales of bounded variation are constant.

### 4. Lemma: bounded-variation local martingales are constant

Lemma 3.3.10 says:

If `M` is a continuous local martingale starting at zero and has bounded variation on compact intervals, then:

`P[M_t = 0 for all t >= 0] = 1`.

The lecture proves this in steps.

#### Step 1: square-integrable martingale with uniformly bounded variation

Assume first that `M` is a continuous square-integrable martingale and its total variation up to time `t` is bounded by a deterministic constant `C`.

For a partition of `[0,t]`, the martingale property gives:

`E[M_t^2] = E[sum_i (Delta_i M)^2]`.

The sum of squared increments can be bounded by:

`sum_i (Delta_i M)^2 <= sup_i |Delta_i M| * sum_i |Delta_i M|`.

Since the variation is bounded by `C`, this gives:

`E[M_t^2] <= C * E[sup_i |Delta_i M|]`.

As the mesh of the partition tends to zero, continuity of `M` implies:

`sup_i |Delta_i M| -> 0`

almost surely.

To pass the limit through expectation, use dominated convergence. Doob's maximal inequality gives the needed domination because `M` is square-integrable. Therefore:

`E[M_t^2] = 0`,

so `M_t = 0` almost surely.

#### Step 2: square-integrable martingale with finite, but not uniformly bounded, variation

Now assume `M` is square-integrable and has finite variation, but the variation is not bounded by a deterministic constant.

Stop the martingale when its variation becomes too large:

`tau_n = inf{t >= 0 : V_t(M) > n}`.

Because `M` is continuous and the variation process is adapted, `tau_n` is an optional time, hence a stopping time under the usual conditions.

The stopped process `M^{tau_n}` has variation bounded by `n`, so Step 1 applies. Therefore:

`M_{t ∧ tau_n} = 0`.

Letting `n -> infinity` gives `M_t = 0`.

#### Step 3: local martingale

Finally, for a continuous local martingale, use a localizing sequence. One may stop both when the process itself becomes large and when the variation becomes large. The stopped process is then a bounded martingale, hence square-integrable, and the previous steps apply.

Letting the stopping times tend to infinity proves the result for the original local martingale.

The lecture stressed that this localization pattern is recurring: stop the process when either the martingale or the compensating/variation process becomes too large.

### 5. Start of existence proof for the bracket

The lecture then returns to Theorem 3.3.5 and begins the proof of existence of the bracket process.

The key case is:

`M` is a bounded continuous martingale starting at zero.

Assume `|M_t| <= K`.

For a partition of `[0,t]`, define the quadratic variation sum:

`A^n_t = sum_i (Delta_i M)^2`,

with an extra terminal term if `t` is not exactly a partition point.

The idea is to show that `A^n` converges to the bracket `<M>`.

Instead of proving convergence of `A^n` directly, define:

`N^n_t = M_t^2 - A^n_t`.

The process `N^n` is a continuous martingale. It has the structure of a discrete stochastic integral:

`N^n_t = 2 sum_i M_{t_i} (M_{t_{i+1}} - M_{t_i})`

up to the usual endpoint convention.

So the task becomes showing that the sequence `N^n` is Cauchy in `L2(Omega; C[0,T])`, where `C[0,T]` has the supremum norm.

Once `N^n -> N`, define:

`<M>_t = M_t^2 - N_t`.

Then `M^2 - <M>` is the limiting martingale, and `A^n -> <M>`.

### 6. A priori estimates

The proof needs estimates for bounded martingales.

First estimate:

For a bounded martingale `|M| <= K`, the second moment of the quadratic variation sum is bounded:

`E[(V^2_t(M, Pi))^2] <= C K^4`

for a universal constant `C` such as `6` in the lecture notes.

The exact constant is not important. What matters is the uniform `K^4` bound.

The proof expands the square:

`(sum_i (Delta_i M)^2)^2`

into fourth-moment terms and cross terms. Martingale orthogonality of increments and conditional expectations allow the cross terms to telescope.

Second estimate:

The sum of fourth powers of increments tends to zero:

`E[sum_i |Delta_i M|^4] -> 0`

as the mesh of the partition tends to zero.

Reason:

`sum_i |Delta_i M|^4 <= (sup_i |Delta_i M|^2) * sum_i |Delta_i M|^2`.

Continuity of `M` gives `sup_i |Delta_i M| -> 0`, while the previous estimate gives uniform L2 control of the quadratic variation sum.

### 7. Cauchy argument for the bracket construction

Choose an increasing sequence of partitions, so that each partition refines the previous one. This is useful because two approximations `N^n` and `N^m` can then be expressed using a common finer partition.

For `Pi^n subset Pi^m`, compare:

`N^n_t - N^m_t`.

Inside each coarse interval, the finer partition adds intermediate points. The difference can be rewritten as a sum over fine increments multiplied by the difference between the coarse left endpoint value and the fine left endpoint value.

Martingale increment orthogonality removes cross terms when taking expectations. The remaining terms are controlled by:

- the maximum oscillation of `M` on small intervals, which tends to zero by continuity
- the quadratic variation sums, which are uniformly bounded in L2

Doob's maximal inequality then upgrades pointwise L2 control to supremum-in-time L2 control:

`E[sup_{s <= t} |N^n_s - N^m_s|^2] -> 0`.

Thus `N^n` is Cauchy in `L2(Omega; C[0,T])`.

The lecture ended around this point, indicating that the remaining proof would be finished in the next lecture.

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
