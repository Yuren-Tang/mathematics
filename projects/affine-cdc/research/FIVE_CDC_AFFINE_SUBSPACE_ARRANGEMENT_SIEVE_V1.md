# Root avoidance as an affine-subspace arrangement sieve

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level structural checkpoint; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_ROOT_LIFT_CONTROLLABILITY_STRESS_FOURIER_V1.md`, `FIVE_CDC_HALFCUBE_SUBGRAPH_CLASSIFICATION_V1.md`

## 1. Purpose

The Fourier/stress formula for root-fibre avoidance has a completely equivalent
Fourier-free form. Each forbidden root value cuts out an affine subspace of the
root-lift evaluation code. The existence of an avoiding lift is therefore the
non-emptiness of the complement of a finite affine-subspace arrangement.

The exact count is obtained by inclusion-exclusion, or more economically by
Möbius inversion on the arrangement intersection poset. The only deviations from
the uniform-orbit main term are joint controllability defects, equivalently
relative-stress circuits.

Thus the spectral language packages the same mechanism but is not logically
essential.

## 2. Evaluation code and bad flats

Let

\[
C\leq Q_F:=\bigoplus_{e\in F}Q_e
\]

be a root-fibre evaluation code, where every `Q_e` is a finite binary vector
space. In the rank-three application,

\[
Q_e\cong\mathbf F_2^2.
\]

Fix a base lift. After translating by its fibre coordinates, let

\[
B_e\subseteq Q_e
\]

be the set of forbidden changes on coordinate `e`.

For every `b\in B_e`, define the bad flat

\[
H_{e,b}:=\{c\in C:c_e=b\}.
\]

It is either empty or an affine coset of

\[
\ker(\pi_e|_C).
\]

A codeword avoids all forbidden values exactly when it lies outside

\[
\bigcup_{e\in F}\bigcup_{b\in B_e}H_{e,b}.
\]

Hence root avoidance is an affine-subspace arrangement complement problem.

## 3. Exact intersection sizes

Let `I` be a finite set of bad-flat indices `(e,b)`. If `I` contains two
different values on the same coordinate, then

\[
\bigcap_{(e,b)\in I}H_{e,b}=\varnothing.
\]

Otherwise let `S(I)\subseteq F` be its coordinate set and let

\[
b_I\in Q_{S(I)}:=\bigoplus_{e\in S(I)}Q_e
\]

be the prescribed partial assignment. Put

\[
C_{S(I)}:=\pi_{S(I)}(C),
\qquad
r(I):=\dim C_{S(I)},
\qquad
d:=\dim C.
\]

### Theorem 3.1 — affine intersection formula

One has

\[
\boxed{
\left|\bigcap_{(e,b)\in I}H_{e,b}\right|
=
\begin{cases}
2^{d-r(I)},&b_I\in C_{S(I)},\\
0,&b_I\notin C_{S(I)}.
\end{cases}}
\]

#### Proof

The intersection is the fibre of the linear map

\[
\pi_{S(I)}|_C:C\to C_{S(I)}
\]

above `b_I`. A nonempty fibre is a coset of its kernel, whose dimension is
`d-r(I)`. ∎

The consistency condition is dual:

\[
\boxed{
b_I\in C_{S(I)}
\iff
y(b_I)=0\quad\text{for every }y\in C_{S(I)}^\perp.}
\]

Thus an empty intersection has an exact relative-stress certificate.

## 4. Inclusion-exclusion without Fourier

Suppose first that exactly one value `a_e\in Q_e` is forbidden on every
coordinate. Put

\[
H_e:=\{c\in C:c_e=a_e\}.
\]

For `S\subseteq F`, write

\[
a_S=(a_e)_{e\in S},
\qquad
C_S=\pi_S(C),
\qquad
r(S)=\dim C_S.
\]

### Theorem 4.1 — Fourier-free avoidance formula

The number of avoiding codewords is

\[
\boxed{
N(a)
=
\sum_{S\subseteq F}
(-1)^{|S|}
\mathbf1_{a_S\in C_S}
2^{d-r(S)}.}
\]

#### Proof

Apply inclusion-exclusion to the bad flats and use Theorem 3.1 on every
intersection. ∎

For several forbidden values per coordinate, ordinary inclusion-exclusion over
the indexed family `(H_{e,b})` gives the analogous formula.

Equivalently, if `L(\mathscr H)` is the intersection poset of the affine
arrangement, with the ambient code `C` adjoined as its minimum element, then

\[
\boxed{
|C-\bigcup\mathscr H|
=
\sum_{X\in L(\mathscr H)}
\mu(C,X)|X|.}
\]

This is the compressed Möbius form of the sieve.

## 5. The block-rank mechanism behind main term and fluctuation

The function

\[
r(S):=\dim\pi_S(C)
\]

is a binary block polymatroid rank function: it is monotone and submodular, and
in the rank-three application each added coordinate increases rank by at most
two.

If

\[
r(S)=2|S|
\]

for a set `S`, then `\pi_S:C\to Q_S` is surjective. Consequently every prescribed
assignment on `S` is realizable and

\[
|\{c\in C:c_e=a_e\ (e\in S)\}|
=
|C|4^{-|S|}.
\]

Thus the forbidden events on `S` are exactly independent under the uniform
measure on `C`.

### Theorem 5.1 — stress-cluster correction formula

Assume `Q_e\cong\mathbf F_2^2` and one value is forbidden on each coordinate.
Then

\[
\boxed{
N(a)
=
|C|\left(\frac34\right)^{|F|}
+
\sum_{S\subseteq F}(-1)^{|S|}
\left(
\mathbf1_{a_S\in C_S}2^{d-r(S)}
-
|C|4^{-|S|}
\right).}
\]

Every summand in the correction term vanishes whenever `\pi_S` is surjective.
Therefore all deviations from the uniform main term are supported on coordinate
sets containing a nonzero relative stress.

In particular, the inclusion-minimal supports of words in `C^\perp` are exactly
the minimal joint-controllability failures. They are the dependency clusters of
the arrangement sieve.

This is the Fourier-free interpretation of the previous statement:

- zero frequency = independent uniform main term;
- nonzero frequencies = relative-stress dependency clusters.

## 6. Four-flat threshold

Let `C` be any finite binary vector space. Suppose

\[
\rho_i:C\twoheadrightarrow\mathbf F_2^2
\qquad(1\leq i\leq m)
\]

are surjective linear maps and let

\[
H_i:=\rho_i^{-1}(a_i).
\]

Every bad flat has cardinality

\[
|H_i|=|C|/4.
\]

### Proposition 6.1 — minimum full-rank cover

If

\[
C=\bigcup_{i=1}^m H_i,
\]

then

\[
\boxed{m\geq4.}
\]

If `m=4`, then the four flats are pairwise disjoint and form a partition of `C`.

#### Proof

The union bound gives

\[
|C|\leq\sum_i|H_i|=m|C|/4.
\]

Hence `m\geq4`. Equality forces equality in the union bound, so no two flats
intersect. ∎

### Proposition 6.2 — pair stresses at equality

Under the hypotheses of Proposition 6.1, assume `m=4` and the four flats cover
`C`. For every pair `i\neq j`, the prescribed pair `(a_i,a_j)` is not in

\[
\operatorname{im}(\rho_i,\rho_j).
\]

Therefore there is a nonzero dual obstruction supported on exactly the two
coordinates `i,j` and taking value one on `(a_i,a_j)`.

#### Proof

The flats are disjoint, so their pairwise intersection is empty. The affine
intersection/stress criterion gives a dual obstruction supported on those two
coordinates. Single-coordinate surjectivity rules out support one. ∎

Thus the first possible full-rank cancellation mechanism is a four-flat affine
partition accompanied by six pair-supported relative stresses.

## 7. Explicit minimal cancellation certificate

Let `C\leq(\mathbf F_2^2)^4` be the row space of

\[
G=
\begin{pmatrix}
0&1&1&0&0&0&1&0\\
0&1&0&1&1&1&0&1\\
1&0&0&1&0&1&0&0
\end{pmatrix}.
\]

The four coordinate blocks are consecutive pairs of columns. Every block
projection has rank two. Forbid

\[
a_1=(1,0),
\quad a_2=(0,0),
\quad a_3=(1,1),
\quad a_4=(1,0).
\]

Identify codewords with coefficient vectors `x\in\mathbf F_2^3`. The four bad
flats are

\[
\begin{aligned}
H_1&=\{001,111\},\\
H_2&=\{000,011\},\\
H_3&=\{010,110\},\\
H_4&=\{100,101\}.
\end{aligned}
\]

They are pairwise disjoint and partition `\mathbf F_2^3`. Hence

\[
\boxed{N(a)=0}
\]

although every single coordinate is fully controllable and the uniform main
term is

\[
|C|\left(\frac34\right)^4
=8\cdot\frac{81}{256}
=\frac{81}{32}>0.
\]

The inclusion-exclusion mechanism is simply

\[
8-4\cdot2=0;
\]

all pair and higher intersections vanish. By Proposition 6.2, every pair of bad
flats carries a weight-two relative-stress inconsistency certificate.

This example proves that single-fibre surjectivity is insufficient. Joint
controllability, encoded by the block rank function and affine consistency data,
is the essential invariant.

## 8. Strategic consequence for five-support compression

For a compression template

\[
P\in\{3K_2,\ K_3\sqcup K_2,\ K_4\},
\]

and a fixed projected Fano flow, every root in `P` produces bad flats on the
source edges of the corresponding direction. An all-lifts obstruction is exactly
a cover of the root-lift evaluation code by this template-induced affine
arrangement.

The next problem is therefore not merely to bound a Fourier spectrum. It is to
classify or exclude affine covers whose bad flats arise from:

1. root fibres of a common Fano flow;
2. the three finite target templates;
3. the source graph's paired-triangle topology;
4. relative stresses coming from the affine pair complex.

A positive theorem may be obtained by proving that at least one template-induced
arrangement has nonempty complement. A negative fixed-flow certificate would be
a finite affine cover together with its minimal stress-supported intersection
poset.

## 9. Reliability boundary

All formulas through Proposition 6.2 are elementary finite linear algebra and
set-theoretic inclusion-exclusion. The explicit four-flat example is a directly
checkable finite certificate. Wolfram Language was used only as an independent
cross-check of the code enumeration, intersection pattern, and dual block-weight
spectrum; no theorem above depends on opaque computation.
