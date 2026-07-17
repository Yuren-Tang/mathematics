# Root-admissible linearization of interior holonomy

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level local reduction plus exact finite root-image classification; global cycle-consistent avoidance remains open  
**Parent:** `FIVE_CDC_INTERIOR_AFFINE_HOLONOMY_NORM_V1.md`

## 1. Purpose

The ambient interior-holonomy theorem shows that a zero norm defect satisfies

\[
z=(1+\pi)y
\]

in the cycle tensor module. This ambient solution need not preserve the nonlinear root-valued condition defining a five-support cover.

This packet isolates that nonlinearity exactly at one edge.

Let

\[
E_5=\{v\in F_2^5:\sum_i v_i=0\},
\qquad
R_5=\{e_i+e_j:i<j\}.
\]

If the current edge label is `x\in R_5`, changing affine origin by `y\in E_5` remains root-valued precisely when

\[
x+y\in R_5.
\]

Write

\[
Q_\pi=1+\pi.
\]

The local question is:

> which values `z\in im Q_pi` have a solution `Q_pi y=z` with both `x` and `x+y` in `R_5`?

The answer reduces to one image of the ten-root orbit and yields a sharp four-type table.

## 2. Root-to-root displacement identity

For fixed `x\in R_5`, define the local root-admissible defect set

\[
\mathcal A_\pi(x)
=
\{Q_\pi y:
y\in E_5,\ x+y\in R_5\}.
\]

### Theorem 2.1 — affine root-image formula

\[
\boxed{
\mathcal A_\pi(x)
=
Q_\pi x+Q_\pi(R_5).
}
\]

#### Proof

The condition `x+y\in R_5` is equivalent to writing

\[
y=x+r
\]

for some `r\in R_5`. Therefore

\[
Q_\pi y
=Q_\pi(x+r)
=Q_\pi x+Q_\pi r.
\]

As `r` runs over `R_5`, the displayed set is obtained. ∎

### Corollary 2.2 — the local obstruction is independent of the current root up to translation

\[
\operatorname{im}Q_\pi
\setminus
\mathcal A_\pi(x)
=
Q_\pi x+
\bigl(
\operatorname{im}Q_\pi
\setminus Q_\pi(R_5)
\bigr).
\]

Thus one finite set

\[
\boxed{
\mathcal F_\pi
:=
\operatorname{im}Q_\pi
\setminus Q_\pi(R_5)
}
\]

controls root admissibility at every edge. The current root merely translates the forbidden set by `Q_pi x`.

## 3. Exact root-image classification

Use the same four permutation types as the rainbow monodromy theorem.

Let

\[
R_5^{(4)}
=
\{v\in E_5:|v|=4\}
\]

be the five weight-four vectors.

For type `3 2`, let `k_pi` be the unique weight-two root fixed by `pi`, namely the root supported on the transposed pair.

### Computational Theorem 3.1 — four local admissibility types

The exact images and forbidden sets are

\[
\begin{array}{c|c|c|c}
\text{type}
&|\operatorname{im}Q_\pi|
&Q_\pi(R_5)
&\mathcal F_\pi
\\
\hline
2^2 1
&4
&\operatorname{im}Q_\pi
&\varnothing
\\
4 1
&8
&\operatorname{im}Q_\pi\setminus\{0\}
&\{0\}
\\
3 2
&8
&\operatorname{im}Q_\pi\setminus\{k_\pi\}
&\{k_\pi\}
\\
5
&16
&Q_\pi(R_5)
&Q_\pi(\{0\}\cup R_5^{(4)}).
\end{array}
\]

For a five-cycle, `Q_pi` is invertible on `E_5`, so the last forbidden set has exactly six elements.

#### Proof status

The affine formula is Theorem 2.1. The four images are verified by exact dependency-free Wolfram enumeration and can also be checked directly from the action on two-subsets of `[5]`.

- For `(12)(34)`, the roots map onto all four values of `im Q_pi`.
- For `(1234)`, no root is fixed, so zero is omitted; the other seven image values occur.
- For `(123)(45)`, the fixed root `{4,5}` maps to zero, while the unique omitted value is that same fixed root `k_pi`; all other seven image values occur.
- For `(12345)`, `Q_pi` is invertible, so the ten roots have ten distinct images. The six nonroots in `E_5` are zero and the five weight-four vectors, giving the displayed complement. ∎

## 4. Edgewise forbidden values

Combining Theorem 2.1 with the table gives the exact local criteria.

### Type `2^2 1`

For every current root `x` and every ambient value

\[
z\in\operatorname{im}Q_\pi,
\]

there exists a root-to-root displacement `y` satisfying

\[
Q_\pi y=z.
\]

Hence this type has no edgewise root-admissibility obstruction.

### Type `4 1`

Exactly one ambient value is forbidden at root `x`:

\[
\boxed{
z=Q_\pi x.
}
\]

Every other value of `im Q_pi` has a root-admissible local solution.

### Type `3 2`

Exactly one ambient value is forbidden at root `x`:

\[
\boxed{
z=Q_\pi x+k_\pi.
}
\]

Every other value of `im Q_pi` has a root-admissible local solution.

### Type `5`

Since `Q_pi` is invertible, the local ambient solution is unique:

\[
y=Q_\pi^{-1}z.
\]

It is root-admissible exactly when

\[
\boxed{
x+Q_\pi^{-1}z\in R_5.
}
\]

Equivalently the six forbidden values are

\[
Q_\pi x+Q_\pi(\{0\}\cup R_5^{(4)}).
\]

## 5. Global reformulation

Suppose a zero-norm lifted loop has ambient equation

\[
z=Q_\pi y
\]

with

\[
y\in Z_1(P)\otimes E_5.
\]

To realize the ambient linearization by another root-valued five-support cover, one must find a cycle tensor `y` such that for every edge `e`,

\[
Q_\pi y(e)=z(e)
\]

and

\[
x(e)+y(e)\in R_5.
\]

The local theorem converts the second condition into an edgewise forbidden-value system.

### Corollary 5.1 — list-flow form of root-admissible linearization

The root-admissible linearization problem is a finite-field cycle-space constraint problem with the following local exclusion sizes:

\[
\boxed{
0,\quad1,\quad1,\quad6
}
\]

for types

\[
2^2 1,\quad4 1,\quad3 2,\quad5.
\]

Thus the global nonlinearity is no longer unspecified. It consists of choosing a cycle-space solution to a linear equation while avoiding a prescribed translated forbidden set at every edge.

This resembles a list-flow or nowhere-zero-flow problem, but no reduction to a standard theorem is presently claimed.

## 6. Consequences for the rainbow programme

### 6.1 Double-transposition branch

The root set creates no local loss at all. Any failure of admissible linearization is purely global: cycle consistency, boundary compatibility, or the fact that the required conjugating translation is not realized in the actual reconfiguration component.

This is the cleanest branch for a first global theorem.

### 6.2 Four-cycle and `3+2` branches

Each edge forbids only one value. The global problem becomes an affine cycle-space avoidance problem with one forbidden section per edge.

A natural target is a binary/finite-field analogue of list-flow avoidance:

\[
\text{linear solution space of positive dimension}
\Longrightarrow
\text{one solution avoids all singleton exclusions},
\]

unless the exclusions form a coherent cut or decomposition certificate.

### 6.3 Five-cycle branch

The ambient norm defect always vanishes, but the local root constraint is strongest. The unique ambient conjugator at each edge must land in a ten-point allowed set inside `E_5`; six values are excluded.

Thus the five-cycle type is ambiently simplest but root-geometrically most rigid.

This reversal is important: vanishing affine cohomology does not imply easy realization in the root orbit.

## 7. Trust boundary

The following are theorem-level:

- the affine root-image formula;
- translation-independence of the forbidden pattern;
- the exact four-type root-image and forbidden-set table;
- the edgewise criteria and exclusion counts.

The following remain open:

- satisfying the local conditions simultaneously with the global cycle equations;
- proving a list-flow avoidance theorem strong enough for arbitrary minimal-counterexample shores;
- showing that failure of avoidance forces a smaller separator or serial decomposition;
- relating the conjugating cycle tensor to the fixed-flow gauge code and orientation transgression;
- proving that every zero-norm ambient loop is represented by a repeatable root-valued reconfiguration loop.

No five-cycle double cover, Tutte five-flow, or Four Colour theorem is claimed.

## 8. Next exact tasks

1. Prove a global admissible-linearization theorem for type `2^2 1`, where there is no local root obstruction.
2. Formulate the singleton-forbidden type `4 1` and `3 2` problems as explicit cycle-space list constraints and identify their minimal unsatisfiable certificates.
3. Determine whether those minimal certificates are exactly smaller cuts or tree-routing decompositions.
4. For type `5`, analyze the six-point forbidden translate as an `S_5`-orbit or matroidal object rather than enumerating edge assignments.
5. Add these local admissibility sets to the exact small-four-pole verifier before launching larger graph censuses.