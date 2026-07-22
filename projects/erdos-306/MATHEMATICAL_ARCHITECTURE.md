# Erdős 306 mathematical architecture

## 1. Ontology

The proof is organized around six natural mathematical objects.

### 1.1 Representation object

For a finite obstruction set $T$, an avoiding representation of $r$ is a finite set $S$ of distinct squarefree semiprimes such that

$$
S\cap T=\varnothing,
\qquad
\sum_{n\in S}\frac1n=r.
$$

The obstruction parameter is part of the theorem mechanism: it is what permits numerator induction without repeating denominators.

### 1.2 Analytic supply object

For dyadic prime blocks

$$
\mathcal P_k=\{p:2^k\le p<2^{k+1}\},
\qquad
A_k=\sum_{p\in\mathcal P_k}\frac1p,
$$

the construction consumes one common-threshold supply:

$$
|\mathcal P_k|
\ge
\frac{2^k}{2\log(2^k)}
\quad(k_0\le k\le3k_0)
$$

and

$$
\sum_{k=k_0}^{3k_0}A_k\ge\mu
$$

for one fixed $1<\mu<\log3$.

This is a handoff interface, not an assertion that no other proof could use weaker analytic data.

### 1.3 Control object

A finite block system carries:

- residue assignments $a_p\in\mathbf Z/p\mathbf Z$;
- internal and adjacent-block control pairs;
- centred CRT representatives $H_{pq}(a)$;
- control energy
  $$
  Q_{\mathrm{ctrl}}(a)
  =
  \sum_{(p,q)}
  \left(\frac{H_{pq}(a)}{pq}\right)^2;
  $$
- deviation scale
  $$
  \sigma_{\mathrm{ctrl}}^2
  =
  \sum_{(p,q)}\frac1{(pq)^2}.
  $$

The exact centred convention is load-bearing because it identifies the finite Fourier phase with the real quadratic energy.

### 1.4 Denominator/weight object

The denominator family is a disjoint union

$$
E=E_{\mathrm{ctrl}}\dot\cup E_{\mathrm{aux}}\dot\cup E_{\mathrm{mass}}.
$$

It is completed to a reciprocal-load interval and assigned one uniform Bernoulli weight $\theta$ satisfying

$$
\sum_{e\in E}\frac{\theta}{e}=\frac1b.
$$

The equality is the main-arc centring condition.

### 1.5 Spectral object

For a period $L$ divisible by every $e\in E$,

$$
F(h)=
\prod_{e\in E}
\bigl((1-\theta)+\theta e^{2\pi ih/e}\bigr)
e^{-2\pi ih/b}.
$$

Finite Fourier inversion turns a positive weighted subset count into the target reciprocal representation.

### 1.6 Arithmetic closure object

The avoiding construction for $1/b$, $b\ge3$, is closed under:

- $b=2$ via $1/2=1/3+1/6$;
- $b=1$ via $1=1/2+1/3+1/6$;
- numerator induction with a growing obstruction set;
- increasing enumeration and the community tuple interface.

## 2. Principle/handoff architecture

### P1 — analytic provider principle

A prime-distribution theorem is used only to prove the common-threshold supply.

**Handoff:** `AnalyticInputs(mu)`.

### P2 — finite spectral selection principle

Character orthogonality computes the weighted count of subset sums in one finite cyclic group.

**Handoff:** real main sum greater than total minor norm implies a positive subset count.

### P3 — local rigidity principle

A low-energy residue assignment on one dense prime block has one dominant small integer label, except for quantitatively charged exceptions.

**Handoff:** hot/cold classification, dominant label, exception budget, and quantitative label bounds.

### P4 — boundary rigidity principle

Distinct adjacent cold labels force energy only under the exact size, cardinality, residue-agreement, and exception hypotheses.

**Handoff:** the corrected boundary floor $\Pi_k$.

### P5 — global localisation principle

Hot blocks, mismatch boundaries, shells, and segment labels encode every bounded-energy assignment. Below the forcing floor, an off-main assignment is globally diagonal.

**Handoff:** high-floor Laplace tail plus one-dimensional Gaussian diagonal tail.

### P6 — reciprocal-mass completion principle

A positive pair pool and a greedy interval lemma complete the fixed control/auxiliary family to the desired reciprocal load.

**Handoff:** uniform $\theta$, exact mean $1/b$, no-wrap, and variance comparison.

### P7 — major-arc principle

Nonvanishing Bernoulli factors, a principal logarithm, exact linear cancellation, and a uniform cubic remainder yield a Gaussian lower bound.

**Handoff:** $c_{\mathrm{maj}}/\sigma_E$.

### P8 — two-minor principle

Minor frequencies split inside the genuine Fourier-minor set into:

1. nonmain block assignments, controlled by global localisation and a fibre factor $b$;
2. main-assignment siblings, controlled by a squarefree mismatch prime and one common prime reservoir, with count factor $b(2N+1)$.

**Handoff:** three separately budgeted minor contributions.

### P9 — finite positivity principle

If the three minor budgets total less than the major allowance, the weighted count is positive.

**Handoff:** a finite subset satisfying the target congruence; total load below $1$ converts it to equality.

## 3. Preferred exposition order

The natural paper-level linearization is:

```text
theorem and avoiding reduction
-> analytic interface and preferred PNT provider
-> finite Fourier principle
-> control geometry
-> local rigidity and corrected boundary theorem
-> global localisation
-> reciprocal mass, weights, variance
-> major arcs
-> two minor classes
-> symbolic terminal budget
-> arithmetic closure.
```

This order is not required to coincide with any Lean module or PDL dossier order.

## 4. Formalization projection

The released Lean proof uses the same downstream construction but a different analytic provider. It packages several long explicit finite closures as declarations.

The frozen refactor offers a more natural prospective module decomposition:

```text
Core
Analytic
Spectral
LocalEnergy
GlobalControl
ResonantConstruction
Public
Audit.
```

That decomposition is architectural influence only. It does not change the release theorem, release assumptions, or current formal status.

## 5. Theorem boundary

The corpus controls the mathematical theorem and its architecture. It does not control:

- public article style or section numbering;
- bibliography;
- TeX/PDF;
- final author metadata or disclosure;
- release engineering;
- canonical branch movement;
- publication or submission.
