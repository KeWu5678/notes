# Corrected transcript for recording 10

Sources:

- `math/stochana/transcript_original/Erwin-Schrödinger-Zentrum 10.txt`
- `math/stochana/lecture notes/Chapter3.pdf`
- `math/stochana/lecture notes/Chapter4.pdf`

Style note: this is a cleaned transcript based on the renewed recording 10. Repetitions, false starts, and unusable background-noise spans have been removed. Mathematical terminology and notation have been corrected against the lecture notes. The raw transcript remains the audit source.

## Summary

This lecture finishes the construction of the bracket process for continuous local martingales and then begins Chapter 4 on stochastic integration.

The first part completes Theorem 3.3.5. For bounded martingales the bracket is obtained as an L2 limit of sums of squared increments. Uniqueness follows because the difference of two candidate brackets is both a local martingale and a bounded-variation process, hence is constant. For general continuous local martingales one localizes, constructs brackets for the stopped bounded martingales, checks consistency on overlapping stopped intervals, and defines the full bracket by a limit. The price of localization is that the quadratic variation sums converge only in probability, uniformly on compact time intervals, rather than in L2.

The second part explains why the bracket is useful for stochastic integration. The bracket defines the measure with respect to which integrability of the integrand is tested. The lecture then starts with the Brownian case, defines elementary left-continuous adapted processes, proves the Ito isometry for them, shows their stochastic integrals are square-integrable continuous martingales, defines the space L2 of jointly measurable adapted integrands, and proves that elementary processes are dense in L2. The proof of density uses step-function approximation, smoothing by time integration, progressively measurable modifications, Fubini's theorem, and truncation.

## Transcript-to-note correspondence

| Raw transcript lines | Lecture-note location | Content |
|---:|---|---|
| 1-22 | Chapter 3, Theorem 3.3.5 and Section 3.3.3 | Recap: bracket process for bounded martingales and L2 convergence of squared increments |
| 24-43 | Chapter 3, uniqueness part after construction | Uniqueness of the bracket via bounded variation local martingales |
| 44-199 | Chapter 3, Section 3.3.4 | General proof of Theorem 3.3.5 by localization; loss of L2 convergence |
| 200-253 | Transition to Chapter 4 | Why the bracket gives the right measure for stochastic integration |
| 261-302 | Chapter 4 opening and Section 4.1 | Goal of stochastic integration; functional-analytic construction |
| 303-340 | Chapter 4, Definition 4.1.1 and Lemma 4.1.2 | Elementary processes and statement of the Ito isometry |
| 341-421 | Chapter 4, proof of Lemma 4.1.2 | Diagonal terms give time increments; cross terms vanish |
| 423-456 | Chapter 4, Proposition 4.1.3 | Stochastic integrals of elementary processes are martingales |
| 458-519 | Chapter 4, Definition 4.1.4 | The space L2, its metric, and equivalence-class caveat |
| 520-704 | Chapter 4, Proposition 4.1.5 and Remark 4.1.6 | Density of elementary processes; progressive modifications and truncation |
| 705-732 | End-of-lecture questions | Why progressive measurability appears in the proof although L2 assumes adaptedness |

## Corrected transcript

We now start talking about stochastic integration. Before doing that, let us recall how we constructed bracket processes.

We considered a continuous local martingale M starting at zero. First we treated the bounded martingale case. In that case there exists a bracket process, denoted

$$
\langle M \rangle,
$$

with the key property that

$$
M_t^2 - \langle M \rangle_t
$$

is a continuous martingale. Moreover, the sums of squared increments along partitions converge to this bracket process in L2, uniformly on compact time intervals.

More concretely, we introduced discrete stochastic integrals built from increments of M. They look like sums of the form

$$
\sum_i H_{t_i}(M_{t_{i+1}} - M_{t_i}).
$$

Using these sums, we proved that the quadratic sums are Cauchy in L2 and hence have a limit. This limit gives the bracket process.

In the general statement of the theorem, the convergence is only in ucp, meaning uniformly on compact time intervals in probability. In the bounded martingale case we have the stronger L2 convergence.

We also proved an important auxiliary fact: if a continuous local martingale has bounded variation, then it must be constant. This gives uniqueness of the bracket almost for free.

Indeed, suppose A and A' are two continuous non-decreasing processes starting at zero such that

$$
M^2 - A
\quad\text{and}\quad
M^2 - A'
$$

are continuous local martingales. Then

$$
A - A' = (M^2 - A') - (M^2 - A)
$$

is itself a continuous local martingale. But A - A' is also of bounded variation, since it is the difference of two non-decreasing processes. By the bounded-variation lemma, A - A' is constant. Since both processes start at zero, this constant is zero, and therefore A = A' almost surely.

Now we turn from bounded martingales to the general local martingale case.

Let M be a continuous local martingale. Choose a localizing sequence of stopping times tau_n increasing to infinity. If necessary, refine the sequence by also stopping when M becomes too large:

$$
\tau_n' = \tau_n \wedge \inf\{t \ge 0 : |M_t| \ge n\}.
$$

After this refinement, the stopped process

$$
M^n_t = M_{t \wedge \tau_n}
$$

is a bounded martingale. Therefore the bounded case gives us a bracket

$$
\langle M^n \rangle
$$

for each n.

These brackets are consistent. If n >= m, then on the interval up to tau_m the stopped processes M^n and M^m coincide. Therefore, by uniqueness of the bracket,

$$
\langle M^n \rangle_t = \langle M^m \rangle_t
\quad\text{for } t \le \tau_m.
$$

This consistency lets us define the bracket of M by a limiting procedure:

$$
\langle M \rangle_t = \lim_{n \to \infty} \langle M^n \rangle_t.
$$

The sequence is increasing in n because increasing the stopping time can only add possible squared increments. The limit is finite on every stopped interval [0, tau_m], and on that interval it agrees with the already constructed bracket of M^m.

We now check the martingale property. For each n,

$$
(M^n_t)^2 - \langle M^n \rangle_t
$$

is a martingale. Also, the bracket of the stopped process is the stopped bracket:

$$
\langle M^{\tau_n} \rangle_t
= \langle M \rangle_{t \wedge \tau_n}.
$$

Hence

$$
(M_{t \wedge \tau_n})^2 - \langle M \rangle_{t \wedge \tau_n}
$$

is a martingale. This says exactly that

$$
M^2 - \langle M \rangle
$$

is a continuous local martingale. By construction, the bracket starts at zero and is non-decreasing.

It remains to show convergence of the quadratic variation sums to the bracket in ucp. For the stopped bounded martingales M^n, we already know L2 convergence:

$$
V^2(M^n,\Pi_m) \to \langle M^n \rangle.
$$

Also, on the event {tau_n > T}, the original process M and the stopped process M^n coincide on [0,T], and therefore their quadratic sums coincide on [0,T]. Likewise,

$$
\langle M \rangle = \langle M^n \rangle
\quad\text{on } [0,T]
$$

on the same event. Since tau_n increases to infinity, for fixed T the probability of {tau_n <= T} goes to zero.

This is the point where we lose L2 convergence. For bounded martingales we had L2 convergence directly. For local martingales we use the localization event {tau_n > T}, which only has probability close to one. Therefore the final convergence is in probability, uniformly over t in [0,T].

Equivalently, for every epsilon > 0 we first choose n so large that tau_n > T with probability at least 1 - epsilon/3. Then, for this fixed n, choose the partition fine enough so that the stopped quadratic sums are within epsilon/3 of the stopped bracket with high probability. Combining the three errors gives

$$
\sup_{0 \le t \le T}
\left|V^2_t(M,\Pi_m) - \langle M \rangle_t\right|
\to 0
\quad\text{in probability}.
$$

That completes the proof of Theorem 3.3.5.

The bracket is useful because it provides the measure with respect to which stochastic integrands should be square integrable. For a continuous local martingale M, the increasing process

$$
\langle M \rangle
$$

defines a measure. Given a jointly measurable process f(t, omega), we may first integrate in time with respect to

$$
d\langle M \rangle_t(\omega)
$$

and then integrate over omega. This gives the natural quantity

$$
E\left[\int_0^T f_t(\omega)^2\,d\langle M \rangle_t(\omega)\right].
$$

For Brownian motion B, the bracket is deterministic:

$$
\langle B \rangle_t = t.
$$

So the above measure reduces to the familiar product measure

$$
P(d\omega)\,dt.
$$

This is why the Brownian case is the transparent starting point.

Previously, when we had an integrand of the form f(s,B_s) and f was smooth, we could define the integral pathwise by using the basic Ito formula. But in general we cannot define stochastic integrals path by path. Ito's key insight is that stochastic integration should be constructed by Hilbert-space methods.

We now begin Chapter 4.

Fix a probability space

$$
(\Omega,\mathcal F,P)
$$

with a filtration

$$
(\mathcal F_t)_{t \ge 0}
$$

satisfying the usual conditions. We also fix a continuous local martingale M. The goal is to define

$$
\int_0^t f_s\,dM_s
$$

for a suitable class of processes f. We first do this for Brownian motion, so for now M = B.

The construction is not by first defining Riemann sums and then taking pathwise limits. Instead, we first define the integral on elementary processes, then extend it by an isometry. Only afterwards do we interpret the integral as a limit of Riemann-type sums.

An elementary, or simple, process is a left-continuous step process of the form

$$
\phi_t(\omega)
= \sum_j e_j(\omega)\,1_{(t_j,t_{j+1}]}(t),
$$

where

$$
0 = t_0 < t_1 < t_2 < \cdots,
$$

each e_j is \mathcal F_{t_j}-measurable, and the e_j are uniformly bounded.

The left endpoint is important: e_j is known at time t_j and is used on the interval (t_j,t_{j+1}]. This is the predictable, or non-anticipating, convention.

For such a process phi, define the stochastic integral with respect to Brownian motion by

$$
I_T(\phi)
= \int_0^T \phi_t\,dB_t
:= \sum_{t_j \le T}
e_j\left(B_{t_{j+1}\wedge T} - B_{t_j\wedge T}\right).
$$

This is just a finite or locally finite sum of Brownian increments weighted by random variables known at the left endpoint.

The key result is the Ito isometry for elementary processes:

$$
E\left[\left(\int_0^T \phi_t\,dB_t\right)^2\right]
=
E\left[\int_0^T \phi_t^2\,dt\right].
$$

This equality identifies the norm of the stochastic integral with the L2 norm of the integrand.

The proof is almost immediate from the properties of Brownian increments. Write

$$
\Delta_j B = B_{t_{j+1}} - B_{t_j}.
$$

When we square the stochastic integral, we obtain terms

$$
E[e_i e_j \Delta_i B\,\Delta_j B].
$$

For the diagonal terms i = j, since e_j is \mathcal F_{t_j}-measurable,

$$
E[e_j^2(\Delta_j B)^2]
= E\left[e_j^2\,E\left[(\Delta_j B)^2\mid \mathcal F_{t_j}\right]\right].
$$

The conditional second moment of the Brownian increment is the length of the interval:

$$
E\left[(\Delta_j B)^2\mid \mathcal F_{t_j}\right]
= t_{j+1}-t_j.
$$

Thus the diagonal terms are

$$
E[e_j^2](t_{j+1}-t_j),
$$

which are exactly the terms in

$$
E\left[\int_0^T \phi_t^2\,dt\right].
$$

For the cross terms, assume for example i < j. Then e_i, e_j, and \Delta_i B are measurable with respect to \mathcal F_{t_j}. Hence

$$
E[e_i e_j \Delta_i B\,\Delta_j B]
=
E\left[
e_i e_j \Delta_i B\,
E[\Delta_j B\mid \mathcal F_{t_j}]
\right]
=0,
$$

because Brownian increments have conditional mean zero. Therefore all cross terms vanish, and the Ito isometry follows.

Next, stochastic integrals of elementary processes are martingales. For phi in L0, the process

$$
I_t(\phi) = \int_0^t \phi_s\,dB_s
$$

starts at zero, is adapted, has continuous paths, and is square integrable by the Ito isometry. The martingale property follows by conditioning future Brownian increments on the present sigma-field: the future increment has conditional expectation zero. Therefore

$$
I : L^0 \to \mathcal M^{2,c}_0
$$

maps elementary processes into the space of square-integrable continuous martingales starting at zero.

Now we ask two questions.

First, which processes can be approximated by elementary processes?

Second, if phi_n approximates f, do the stochastic integrals I(phi_n) converge?

The Ito isometry answers the second question once we have convergence of the integrands in the right L2 norm. Therefore we define the relevant integrand space.

Let L2 be the class of jointly measurable and adapted processes f such that, for every T > 0,

$$
\|f\|_{L^2_T(P\otimes \lambda)}^2
:=
E\left[\int_0^T f_t(\omega)^2\,dt\right]
<\infty.
$$

This is the Brownian version of the bracket-integrability condition, because for Brownian motion \(d\langle B\rangle_t = dt\).

On L2 we use a metric such as

$$
d(f,g)
=
\sum_{n=1}^\infty 2^{-n}
\min\left\{1,\|f-g\|_{L^2_n(P\otimes\lambda)}\right\}.
$$

Strictly speaking, this is really a metric on equivalence classes, not on individual processes, because changing a process on a null set does not change the L2 norm. But changing representatives can affect adaptedness or progressive measurability. For the moment we keep this issue in the background; it becomes important later.

The density result is:

$$
L^0 \subset L^2
\quad\text{is dense}.
$$

In other words, every L2-adapted measurable process can be approximated in the above metric by elementary processes.

The proof is done in steps.

Step 1: assume f is uniformly bounded and, for almost every omega, the path t -> f_t(omega) is continuous. Then we approximate f by left-endpoint step processes:

$$
\phi^n_t(\omega)
=
\sum_j f_{t_j}(\omega)\,1_{(t_j,t_{j+1}]}(t).
$$

As the mesh of the partition goes to zero, these step processes converge pointwise to f. Since f is bounded, dominated convergence gives convergence in L2 on every compact time interval.

Step 2: drop continuity, but assume f is still bounded and progressively measurable. We smooth f by time integration. Define

$$
K_t(\omega) = \int_0^{t\wedge T} f_s(\omega)\,ds
$$

and then define

$$
f^m_t(\omega)
=
m\int_{(t-1/m)^+}^{t} f_s(\omega)\,ds
=
m\left(K_t(\omega)-K_{(t-1/m)^+}(\omega)\right).
$$

The time integral smooths f. The process K is continuous in t, and progressive measurability is preserved under time integration. Hence f^m is bounded, continuous in t, and progressively measurable. Step 1 applies to each f^m.

It remains to show f^m -> f. This is a standard differentiation argument. For each fixed omega, f^m_t(omega) is a moving average of f_s(omega) over the interval ((t-1/m)^+,t]. By the differentiation theorem, this converges to f_t(omega) for almost every t. Fubini's theorem then gives convergence for (t,omega) almost everywhere. Boundedness gives L2 convergence by dominated convergence.

Step 3: now assume f is bounded, jointly measurable, and adapted, but not necessarily progressively measurable. We use the usual conditions on the filtration. Under these conditions, such a process has a progressively measurable modification g.

Define

$$
F_t = \int_0^t f_s\,ds,
\qquad
G_t = \int_0^t g_s\,ds.
$$

Since g is progressive, G is progressive and hence adapted. Because f and g are modifications of each other, F and G are also modifications. By Fubini's theorem,

$$
E\left[\int_0^T |f_s-g_s|\,ds\right]=0,
$$

so the two time integrals agree almost surely for each fixed t. Since G is adapted and the filtration satisfies the usual conditions, F is adapted as well. The process F is continuous, and continuity plus adaptedness implies progressive measurability. Therefore the argument from Step 2 can be repeated.

This is the part where the usual conditions matter: they allow us to pass adaptedness through modifications.

Step 4: remove boundedness by truncation. Define

$$
f^{(n)}_t
=
\begin{cases}
-n, & f_t < -n,\\
f_t, & -n \le f_t \le n,\\
n, & f_t > n.
\end{cases}
$$

Then f^{(n)} is bounded, adapted, and jointly measurable, and

$$
f^{(n)} \to f
$$

in L2 on compact time intervals by dominated convergence. Applying the previous steps to f^{(n)} and using a diagonal argument proves density of L0 in L2.

Actually, the proof gives something slightly stronger. Let L* denote the subset of L2 consisting of equivalence classes that contain a progressively measurable representative. The approximating elementary processes are progressively measurable, so the proof shows that L0 is dense in this progressively measurable subspace as well.

This explains a question from the end of the lecture. The statement of the density proposition uses L2, whose assumptions are joint measurability and adaptedness. Progressive measurability is not part of the statement. It appears in the proof because time-integration and smoothing preserve progressive measurability, and because the usual conditions allow us to replace an adapted measurable process by a progressively measurable modification.

This also explains why equivalence classes matter. We sometimes replace a process by a modification in order to obtain the right measurability properties. The L2 norm does not distinguish such representatives, but adaptedness, progressive measurability, and predictability can depend on the representative.

The next step is to use the Ito isometry and the density of L0 in L2 to extend the mapping

$$
I : L^0 \to \mathcal M^{2,c}_0
$$

uniquely to a continuous map

$$
J : L^2 \to \mathcal M^{2,c}_0.
$$

This extended map defines the Ito integral

$$
J_t(f)
=
\int_0^t f_s\,dB_s
$$

for every f in L2.
