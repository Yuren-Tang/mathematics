# Erdős 306 current-best mathematical state

## 1. Headline mathematics

Let $q>0$ be rational, written in lowest terms as $q=a/b$.

Then $q$ is a finite sum of reciprocals of distinct integers $n$ with

$$
\omega(n)=\Omega(n)=2
$$

if and only if $b$ is squarefree. Equivalently, the denominators are products of two distinct primes.

The natural proof has two parts.

1. **Necessity.** A finite reciprocal sum of squarefree integers has squarefree reduced denominator.
2. **Sufficiency.** For every squarefree $b$ and every finite obstruction set $T$, construct a representation of $1/b$ by distinct squarefree semiprimes avoiding $T$; then close under $b=1,2$, numerator induction, and finite increasing enumeration.

## 2. Current preferred architecture

```text
squarefree denominator and finite obstruction set
-> construction-facing dyadic analytic interface
-> finite denominator/control system
-> finite Fourier identity
-> local low-energy rigidity
-> global level-set and localisation theorem
-> reciprocal-mass completion and variance comparison
-> major-arc lower bound
-> block-minor and sibling-minor upper bounds
-> strict Fourier positivity
-> exact reciprocal equality
-> avoiding unit representation
-> arbitrary numerator and public tuple.
```

The proof is finite throughout. No infinite denominator sequence is asserted.

## 3. Analytic backend fork

The downstream construction consumes one common-threshold interface:

- enough primes in each dyadic block;
- reciprocal-prime mass greater than $1$ in one inclusive block window.

Two separate providers are retained.

### Released provider

Rosser–Schoenfeld Corollary 3 and Theorem 5 imply the interface with explicit thresholds. This route is Lean-closed relative to the two named external assumptions.

### Preferred article provider

PNT plus Abel summation gives

$$
\sum_{x\le p<2x}\frac1p
=
\frac{\log 2}{\log x}
+
o\!\left(\frac1{\log x}\right),
$$

hence the same common-threshold interface. This is complete human mathematics but is not a released formal provider.

## 4. Mechanism-first parameter architecture

Fix a mass target

$$
1<\mu<\log 3.
$$

Use the normalization $\alpha=3/2$, producing

$$
\frac13<\theta\le\frac23,
\qquad
v_*=\min\theta(1-\theta)=\frac29.
$$

Retain symbolic constants:

- $c_\sigma>0$ for the control deviation;
- a finite inverse-square constant $C_2$;
- $K_\sigma>\sqrt{C_2/4}$;
- Taylor data $0<r_T<1/4$, $0<\delta_T<\pi/2$;
- a positive main coefficient $c_{\mathrm{maj}}$;
- Fourier damping $c_F=8v_*=16/9$;
- sibling damping $\beta_b=\sqrt{1-8/(9b^2)}<1$.

Choose three positive minor-budget shares

$$
q_{\mathrm{blk}},q_{\mathrm{gauss}},q_{\mathrm{sib}}>0,
\qquad
q_{\mathrm{blk}}+q_{\mathrm{gauss}}+q_{\mathrm{sib}}<1.
$$

The non-circular order is

```text
fixed interfaces
-> block allowance eta
-> Gaussian cutoff C
-> sibling target D_sib
-> common reservoir size G
-> final bottom scale k0.
```

The final $k_0$ is one maximum of finitely many thresholds.

## 5. Exact reliability boundary

- The released theorem is Lean-closed relative to two named Rosser–Schoenfeld assumptions.
- The human proof spine is complete in the PDL source.
- Long constant, cast, floor, threshold, and polynomial closures may remain named finite/kernel residuals.
- The frozen refactor contributes mathematical decomposition and naming, not theorem authority.
- REV3 is a read-only manuscript projection. Its concrete constants are superseded for the next consumer by the symbolic mechanism architecture.
- The global theorem is not open; the only unresolved item affecting external source assurance is the human publisher-scan comparison of the two RS transcriptions.
