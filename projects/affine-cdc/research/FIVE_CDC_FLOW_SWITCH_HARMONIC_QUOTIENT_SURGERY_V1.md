# Rank-one flow switches and harmonic-quotient surgery

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level structural checkpoint plus exact finite certificate; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_FIXED_FANO_ORBIT_OBSTRUCTION_V1.md`, `FIVE_CDC_GAUGE_AS_PIECEWISE_ROOT_TRANSLATION_V1.md`, canonical `gauge/gauge-modes-and-circuits.md`

## 1. Purpose

The fixed-Fano obstruction packet exhibits a connected cubic graph and a nowhere-zero

\[
f:E(G)\to \mathbf F_2^3
\]

whose complete compatible-family / root-lift torsor contains no half-cube-compressible lift.
This packet shows that the obstruction is not stable under a very small change of the
downstairs flow.

A single rank-one switch on one ten-edge binary cycle changes the unique nontrivial
harmonic quotient from the weight-six type `2K_3` to the weight-four type `4K_2`.
The switched Fano flow again has a one-dimensional reduced root-lift torsor, but both
of its two reduced lifts are half-cube compressible.

The mechanism is a general side-collapse operation on a triangular harmonic quotient.

## 2. Rank-one cycle switches

Let `G` be a finite loopless graph, let

\[
f:E(G)\to \Gamma
\]

be a binary-vector-space-valued flow, let `Z\subseteq E(G)` be a binary cycle, and
let `0\neq a\in\Gamma`.

Define

\[
f^{Z,a}(e):=f(e)+a\mathbf 1_Z(e).
\]

### Lemma 2.1 — rank-one switch lemma

The map `f^{Z,a}` is again a `\Gamma`-valued flow. If

\[
f(e)\neq a\qquad(e\in Z),
\]

then it is nowhere zero whenever `f` is nowhere zero.

#### Proof

At every vertex, the number of incident edges of `Z` is even. Hence the added
contribution to the flow sum is an even multiple of `a`, and therefore vanishes in
characteristic two. On an edge of `Z`, the new value can be zero only when the old
value was `a`. ∎

In a cubic graph, exactly zero or two incident directions change at every vertex.
If the old local plane has directions

\[
h_1,\ h_2,\ h_1+h_2
\]

and the cycle uses the first two incident edges, the new local plane has directions

\[
h_1+a,\ h_2+a,\ h_1+h_2.
\]

Thus a rank-one switch changes a local Fano plane by a rank-one shear while preserving
the unswitched direction.

## 3. Collapsing a `2K_3` harmonic quotient to `4K_2`

Suppose a nonzero gauge word for `f` has harmonic quotient `2K_3`. Equivalently,
there is a partition of the source vertices into three connected regions

\[
A,\ B,\ C
\]

with regional potentials `p_A,p_B,p_C`, such that each pair of regions is joined by
two crossing edges. Put

\[
x=p_B+p_C,
\qquad
y=p_A+p_B,
\qquad
z=p_A+p_C=x+y.
\]

The doubled sides `BC`, `AB`, and `AC` carry labels `x`, `y`, and `z`, respectively.

### Theorem 3.1 — triangular-side collapse

Assume there is a binary cycle `Z` satisfying:

1. `Z` contains the two `AB` quotient edges and no other quotient edge;
2. `f(e)\neq x` for every `e\in Z`.

Switch by `x` along `Z`:

\[
f'=f^{Z,x}.
\]

Then `f'` has a gauge word whose harmonic quotient is `4K_2`.

More precisely, assign potential `0` to region `A` and potential `z` to the merged
region `B\cup C`. Its support consists of the four edges from `A` to `B\cup C`, and
all four carry label `z` under `f'`.

#### Proof

The two `AB` labels change from

\[
y
\quad\text{to}\quad
y+x=z.
\]

The two `AC` labels remain `z`. Since the cycle contains no other quotient edge, the
two `BC` labels remain `x`; they become internal after `B` and `C` receive the same
new potential. Hence the four crossing edges between `A` and `B\cup C` all have label
`z`, and the new potential difference is exactly `z`. This is the equal-labelled
four-parallel-edge harmonic quotient. ∎

This theorem does not by itself imply five-support compression. It says that a
rank-one downstairs switch can change the geometric type of the gauge circuit while
preserving the dimension of the gauge space.

## 4. The thirty-vertex obstruction before switching

Use the graph, root lift, and Fano flow from
`FIVE_CDC_FIXED_FANO_ORBIT_OBSTRUCTION_V1.md`.

The unique nonzero reduced gauge class is represented by the regional potential field

\[
\begin{array}{c|l}
2&1,2,3,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28\\
1&25,26\\
0&4,5,6,7,29,30.
\end{array}
\]

Its six support edges form a `2K_3` quotient:

- between the `2`-region and the `0`-region: source edges `1,3`, both labelled `2`;
- between the `1`-region and the `0`-region: source edges `14,16`, both labelled `1`;
- between the `1`-region and the `2`-region: source edges `40,41`, both labelled `3`.

Thus the unique gauge bit is not numerically mysterious: before switching it is the
canonical weight-six `2K_3` circuit from the low-weight classification.

## 5. The ten-edge downstairs switch

Let `Z` be the source cycle

\[
22-30-29-2-9-8-1-3-28-23-22.
\]

In the edge numbering of the parent certificate,

\[
Z=\{1,3,5,6,8,13,20,24,33,45\}.
\]

Every vertex of this subgraph has degree two. None of its edges has Fano direction
`1`. Define

\[
\boxed{f'=f+\mathbf 1_Z.}
\]

By Lemma 2.1, `f'` is a nowhere-zero `\mathbf F_2^3`-flow.

The cycle meets the old `2K_3` interface exactly in edges `1,3`, the doubled side
labelled `2`. Switching by `1` changes those two labels to

\[
2+1=3.
\]

Theorem 3.1 applies with

\[
x=1,
\qquad y=2,
\qquad z=3.
\]

The new gauge field is

\[
k'_v=
\begin{cases}
3,&v\in\{4,5,6,7,25,26,29,30\},\\
0,&\text{otherwise}.
\end{cases}
\]

Its support is

\[
\{1,3,40,41\},
\]

and all four support edges have new flow label `3`. Hence its harmonic quotient is
`4K_2`.

Exact row reduction of the switched admissible-translation matrix again gives

\[
\operatorname{rank}=86,
\qquad
\dim H_{f'}^0=4.
\]

Since the source graph is connected, the reduced torsor again has dimension one and
contains exactly two lifts modulo global support translation.

## 6. An explicit switched root lift

One root lift of `f'` is specified by the following local target triangles.

| `v` | triangle | `v` | triangle | `v` | triangle |
|---:|:---:|---:|:---:|---:|:---:|
| 1 | `257` | 11 | `246` | 21 | `267` |
| 2 | `256` | 12 | `256` | 22 | `256` |
| 3 | `256` | 13 | `247` | 23 | `246` |
| 4 | `367` | 14 | `257` | 24 | `256` |
| 5 | `167` | 15 | `257` | 25 | `467` |
| 6 | `137` | 16 | `257` | 26 | `467` |
| 7 | `136` | 17 | `457` | 27 | `457` |
| 8 | `247` | 18 | `457` | 28 | `456` |
| 9 | `245` | 19 | `467` | 29 | `156` |
| 10 | `457` | 20 | `247` | 30 | `156` |

For each source edge, the unique pair in the local triangle whose xor is the edge
flow direction agrees at the two endpoints. Hence the table is a root lift of `f'`.

It uses sixteen distinct roots. Its unused-root graph is

\[
\{01,02,03,04,05,06,07,12,14,23,34,35\}.
\]

In particular it contains the matching

\[
\boxed{02,\ 14,\ 35.}
\]

Therefore it admits a five-support half-cube compression.

## 7. The second reduced lift

Translate the local triangles in the eight-vertex region

\[
\{4,5,6,7,25,26,29,30\}
\]

by `3`. This is the nontrivial gauge move `k'` from Section 5 and gives the second
reduced root lift.

It uses thirteen distinct roots. Its unused-root graph is

\[
\{01,03,06,07,12,13,14,15,16,17,23,34,35,36,37\}.
\]

It contains the matching

\[
\boxed{06,\ 12,\ 34.}
\]

and is therefore also half-cube compressible.

### Theorem 7.1 — one-switch escape from the fixed-Fano obstruction

The fixed Fano flow in the parent obstruction packet has no compressible root lift,
but the rank-one cycle switch `f'=f+\mathbf1_Z` above has exactly two reduced root
lifts and both are half-cube compressible.

Thus

\[
\boxed{
\text{the complete fixed-Fano orbit obstruction is not stable under one rank-one downstairs flow switch.}
}
\]

## 8. Strategic interpretation

The numerical pattern in the parent example separates into two kinds.

1. `90=30\cdot3` is forced by the vertex-translation variables.
2. rank `86` means exactly one non-global gauge bit; this remains true after the
   switch.
3. using `27=28-1` roots is not forced by the gauge dimension. It is a dense
   realization specific to the original flow fibre.
4. the important invariant is not merely `\dim\mathcal B_f`, but the harmonic-quotient
   geometry of its circuits. Here the unique circuit changes from `2K_3` to `4K_2`,
   and the label graph becomes sparse enough to compress.

This suggests a new intermediate programme:

> study how rank-one cycle switches act on harmonic cut quotients, and search for
> quotient-surgery moves that force some flow in the downstairs flow moduli to have
> a compressible root-lift orbit.

The present theorem does **not** prove that every fixed-flow obstruction can be
escaped by one switch, nor that every cubic graph admits an appropriate switched
flow. It supplies the first exact mechanism connecting downstairs flow moduli to
root-lift compression.

## 9. Verification boundary

The following were checked independently by a dependency-free Python verifier and a
Wolfram Language computation:

- `Z` is a binary cycle and avoids direction `1`;
- `f'` is nowhere zero and satisfies every vertex flow equation;
- the switched admissible-translation rank is `86`;
- both local-triangle tables are edge-compatible root lifts;
- their used-root counts are `16` and `13`;
- their displayed unused-root sets and matching witnesses are exact.

The standalone verifier is stored in the private research workbench. No claim in
this packet changes the canonical AffineCDC theorem, the public Lean boundary, or the
status of the 5-CDC conjecture.
