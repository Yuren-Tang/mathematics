# Reciprocal mass, denominator family, weights, and variance

## 1. Three denominator roles

The construction uses a disjoint finite family

$$
E=E_{\mathrm{ctrl}}\dot\cup E_{\mathrm{aux}}\dot\cup E_{\mathrm{mass}}.
$$

- $E_{\mathrm{ctrl}}$ realizes the quadratic control energy.
- $E_{\mathrm{aux}}$ supplies denominator-sensitive damping for sibling frequencies.
- $E_{\mathrm{mass}}$ completes the reciprocal load without changing the previously fixed control or reservoir data.

All denominators are distinct products of two different primes and avoid the finite obstruction set $T$.

## 2. Pair-pool principle

Let

$$
S_1=\sum_{p\in\mathcal P(k_0)}\frac1p,
\qquad
S_2=\sum_{p\in\mathcal P(k_0)}\frac1{p^2}.
$$

Then

$$
\sum_{p<q}\frac1{pq}
=
\frac{S_1^2-S_2}{2}.
$$

For a fixed $\mu>1$, eventual $S_1\ge\mu$ and $S_2\to0$ give a positive pair-pool margin. The released choice $\mu=21/20$ yields the certificate $\sum_{p<q}1/(pq)\ge1/2$.

Distinct ordered prime pairs have distinct products.

## 3. Exact forbidden-load cancellation

Let

$$
E_{\mathrm{base}}=E_{\mathrm{ctrl}}\dot\cup E_{\mathrm{aux}},
\qquad
\Lambda_{\mathrm{base}}=\sum_{e\in E_{\mathrm{base}}}\frac1e.
$$

The residual target is the desired lower load minus $\Lambda_{\mathrm{base}}$.

Removing pair products already used by the fixed components loses at most the reciprocal load already counted in $\Lambda_{\mathrm{base}}$. The external finite set $T$ is below the bottom pair scale after the final scale is chosen.

Thus no hidden positive surplus is required: the pair-pool lower bound and the already-spent base load exactly account for the exclusions.

## 4. Greedy reciprocal completion

If a finite positive family has total at least $t$ and every term is smaller than $g$, a minimal-cardinality subfamily reaching $t$ has sum in $[t,t+g)$.

Use the coherent normalization

$$
\alpha=\frac32.
$$

Complete the family to

$$
\frac{\alpha}{b}
\le
\Lambda:=\sum_{e\in E}\frac1e
<
\frac{2\alpha}{b}.
$$

For $b\ge3$, this lies below $1$.

## 5. Uniform weight and optimal compact interval

Define

$$
\theta=\frac{1/b}{\Lambda}.
$$

For $\alpha=3/2$,

$$
\frac13<\theta\le\frac23
$$

and

$$
\sum_{e\in E}\frac{\theta}{e}=\frac1b.
$$

Among $1<\alpha\le3/2$, this normalization uniquely balances the two endpoint variances and maximizes the worst-case Bernoulli variance:

$$
v_*=\min\theta(1-\theta)=\frac29.
$$

This is one coherent normalization, not five unrelated constants.

## 6. Variance comparison

Set

$$
\sigma_E^2
=
\sum_{e\in E}\frac{\theta(1-\theta)}{e^2}.
$$

Because control denominators are included,

$$
\sigma_E
\ge
\sqrt{v_*}\,\sigma_{\mathrm{ctrl}}.
$$

The noncontrol inverse-square contribution is bounded by a finite comparison constant $C_2$:

$$
\sum_{e\in E}\frac1{e^2}
\le
C_2\sigma_{\mathrm{ctrl}}^2.
$$

Choose

$$
K_\sigma>\sqrt{C_2/4}.
$$

Then

$$
\sqrt{v_*}\,\sigma_{\mathrm{ctrl}}
\le
\sigma_E
\le
K_\sigma\sigma_{\mathrm{ctrl}}.
$$

The released finite instantiation is

$$
C_2=1000001,
\qquad
K_\sigma=501.
$$

Finiteness of $C_2$ and $K_\sigma$ is structural. The displayed integers are certificates.

## 7. Reservoir order

After the Gaussian cutoff $C$ is fixed, choose one common set of exactly $G$ high-block primes, outside the prime support of $b$, large enough that $2N<s$.

Include every product $rs$, where $r\mid b$ is prime and $s$ belongs to that common reservoir.

The reservoir is selected before $E_{\mathrm{mass}}$. The mass batch never changes a parameter used to choose the reservoir or bottom scale.
