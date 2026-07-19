# The three affine orbits of unused root matchings

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level finite-geometry checkpoint; not canonical pending review  
**Parent:** `FIVE_CDC_UNUSED_MATCHING_COMPRESSION_V1.md`

## 1. Setup

Identify the eight support indices with

\[
\Gamma=\mathbf F_2^3.
\]

A root label is an unordered edge `{s,t}` of the affine complete graph `K_8`, and
its **direction** is

\[
\partial\{s,t\}:=s+t\in\Gamma\setminus\{0\}.
\]

Let `\mathfrak M_3` be the set of three-edge matchings in `K_8`. There are

\[
|\mathfrak M_3|
=
\binom86\frac{6!}{2^3 3!}
=
28\cdot15
=
420.
\]

The affine group

\[
\operatorname{AGL}(3,2)
=
\Gamma\rtimes\operatorname{GL}(3,2)
\]

acts on `\mathfrak M_3`.

## 2. Direction patterns

Let

\[
M=\{e_1,e_2,e_3\}\in\mathfrak M_3,
\qquad
h_i:=\partial e_i.
\]

Because the three edges are disjoint, the following are the only possible
patterns.

1. `h_1=h_2=h_3`.
2. Exactly two of the `h_i` are equal; the third is different.
3. The three `h_i` are distinct and linearly independent.

The apparently possible fourth pattern—three distinct directions spanning a
plane—cannot occur.

### Lemma 2.1

If `h_1,h_2,h_3` are distinct, then they are linearly independent.

#### Proof

If they spanned a plane, then

\[
h_1+h_2+h_3=0.
\]

The xor-sum of the six endpoints of the matching is also

\[
h_1+h_2+h_3=0.
\]

The xor-sum of all eight points of `Γ` is zero, so the two unmatched points would
also have xor-sum zero. They would therefore be equal, a contradiction. ∎

## 3. Orbit classification

### Theorem 3.1 — three matching orbits

The action of `AGL(3,2)` on `\mathfrak M_3` has exactly three orbits, represented
by the three direction patterns above.

Their sizes are:

\[
\boxed{
28,\qquad168,\qquad224.
}
\]

#### Proof

The direction multiplicity pattern is affine-invariant, so the three classes are
disjoint.

For the all-parallel class, choose the common nonzero direction `h` in seven
ways. The four affine `h`-lines partition `Γ`; choose three of them. Hence

\[
7\binom43=28.
\]

For the exactly-two-parallel class, choose the repeated direction `h` in seven
ways and choose two of its four parallel edges in `\binom42=6` ways. Four points
remain. Among the six edges on those four points, exactly two have direction
`h`; choosing either would give the all-parallel class. The other four choices
give exactly-two-parallel matchings. Hence

\[
7\binom42\cdot4=168.
\]

The remaining

\[
420-28-168=224
\]

matchings have three distinct, hence independent, directions.

Affine transitivity within each class follows by translating one chosen endpoint
to zero and using `GL(3,2)` to send the resulting direction data to a fixed
standard form. In the double-parallel case the residual stabilizer of the
repeated direction acts transitively on the admissible cross-edge choices; in
the independent case the three directions form a basis and the disjointness data
determines one affine configuration up to basis permutation. ∎

## 4. Standard representatives

Using binary integers for the points of `F_2^3`, one may take:

1. **parallel type**
   \[
   \{05,14,23\},
   \]
   with three copies of direction `5`;
2. **double-parallel type**
   \[
   \{23,67,15\},
   \]
   with directions `1,1,4`;
3. **independent type**
   \[
   \{07,45,13\},
   \]
   with directions `7,1,2`.

The exact representatives are unimportant; the three orbit types are intrinsic.

## 5. Consequence for the compression programme

The unused-matching criterion says that an AffineCDC root lift compresses to five
supports if it avoids all three roots of some matching `M∈\mathfrak M_3`.
Instead of treating 420 forbidden triples separately, it is enough to understand
three orbit-level restricted lifting problems:

\[
\boxed{
\text{parallel},\qquad
\text{double-parallel},\qquad
\text{independent}.
}
\]

These three types should have different algebraic behaviour.

- A parallel forbidden matching removes three of the four roots above one fixed
  Fano direction, leaving only one allowed lift on edges of that direction.
- A double-parallel matching imposes a strong restriction on one direction and a
  single forbidden root on another.
- An independent matching removes one root in each of three independent
  directions and is the most balanced type.

The next step is to derive, for each orbit, the exact affine-incidence obstruction
to a compatible root lift avoiding the three forbidden labels. A theorem for any
one orbit that applies to every cubic Fano flow would already prove five-support
CDC through the unused-matching compression criterion.