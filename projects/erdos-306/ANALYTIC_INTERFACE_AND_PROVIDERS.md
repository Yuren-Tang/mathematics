# Analytic interface and providers

## 1. Construction-facing interface

Fix one number

$$
1<\mu<\log3.
$$

For sufficiently large $k_0$, require simultaneously:

1. for every $k_0\le k\le3k_0$,
   $$
   |\mathcal P_k|
   \ge
   \frac{2^k}{2\log(2^k)};
   $$
2. the inclusive reciprocal window satisfies
   $$
   \sum_{k=k_0}^{3k_0}
   \sum_{p\in\mathcal P_k}\frac1p
   \ge\mu.
   $$

The inclusive union is

$$
\bigcup_{k=k_0}^{3k_0}\mathcal P_k
=
\{p:2^{k_0}\le p<2^{3k_0+1}\}.
$$

The interface contains exactly the positive prime-supply facts consumed downstream. Elementary upper estimates used by the control graph are not additional analytic-number-theory inputs.

The released certificate uses $\mu=21/20$.

## 2. Released Rosser–Schoenfeld provider

The immutable release assumes exactly:

- `RosserSchoenfeld.rosser_schoenfeld_cor3`;
- `RosserSchoenfeld.rosser_schoenfeld_thm5`.

Corollary 3 gives explicit dyadic density. Theorem 5 gives a reciprocal-prime prefix lower/upper pair; subtracting at $2^{3k_0+1}$ and $2^{k_0}$ cancels the same Mertens constant and yields the inclusive mass window.

The resulting construction-facing theorems are Lean-closed.

### Exact trust statement

Correct:

> v0.0.3 is machine checked relative to the two named Rosser–Schoenfeld assumptions.

Not yet certified here:

> an independent human has compared every symbol of both Lean axioms against the publisher scan.

The latter is `SOURCE-GATED`.

## 3. Preferred PNT/Abel provider

Assume

$$
\pi(x)\sim\frac{x}{\log x}.
$$

Abel summation on $(x,2x]$ gives

$$
\sum_{x<p\le2x}\frac1p
=
\frac{\pi(2x)}{2x}
-
\frac{\pi(x)}x
+
\int_x^{2x}\frac{\pi(t)}{t^2}\,dt.
$$

Use the tail-uniform error

$$
\varepsilon(x)
=
\sup_{t\ge x}
\left|
\frac{\pi(t)\log t}{t}-1
\right|
\longrightarrow0.
$$

Then uniformly on the interval,

$$
\sum_{x\le p<2x}\frac1p
=
\frac{\log2}{\log x}
+
o\!\left(\frac1{\log x}\right).
$$

At $x=2^k$, the power-of-two endpoints are composite and

$$
A_k=\frac1k+o(1/k).
$$

This one local law gives both required clauses at one common threshold:

- density follows from $A_k\le|\mathcal P_k|/2^k$;
- inclusive mass follows by summing $A_k\ge c_M/k$ and comparing with
  $$
  \int_{k_0}^{3k_0+1}\frac{dt}{t}>\log3.
  $$

## 4. Why ordinary Mertens subtraction is not the preferred article route

The asymptotic

$$
\sum_{p\le x}\frac1p
=
\log\log x+B+o(1)
$$

is enough for a fixed power window, but subtracting it across one dyadic block leaves two uncontrolled $o(1)$ errors while the desired local main term is $O(1/\log x)$.

The PNT/Abel local law supplies the needed scale and uniformity directly.

## 5. Provider equivalence and non-equivalence

Equivalent downstream consequence:

```text
RS provider -> AI(mu)
PNT provider -> AI(mu).
```

Not equivalent as assurance:

- the RS route is the released formal backend;
- the PNT route is the preferred human mathematical backend;
- the frozen refactor's PNT/Mertens structural axioms are an unreleased formal re-interface.

No source may claim that the preferred PNT presentation has already been formally verified at v0.0.3.

## 6. Alternative-provider frontier

Future providers may replace RS or PNT only by proving the same construction-facing interface, including:

- common threshold;
- inclusive upper endpoint;
- blockwise density;
- reciprocal mass exceeding $1$;
- parameter independence from the later bottom-scale choice.

No future provider is required for the current theorem.
