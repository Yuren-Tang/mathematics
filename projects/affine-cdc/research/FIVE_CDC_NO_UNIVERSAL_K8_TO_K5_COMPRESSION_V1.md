# No universal complete-cographic compression from `K_8` to `K_5`

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level research checkpoint; not canonical pending literature audit  
**Parent:** `FIVE_CDC_K5_COGRAPHIC_MAP_V1.md`

## 1. Motivation

The universal orthogonal root-lift model produces, for every cubic Fano flow, a
cycle-continuous edge map

\[
M(G)\longrightarrow M^*(K_8).
\]

A tempting route to five supports would be to compose this with one fixed
cycle-continuous map

\[
M^*(K_8)\longrightarrow M^*(K_5).
\]

The theorem below shows that no such graph-independent target compression can
exist. More generally, complete cographic targets are rigid in the decreasing
direction.

## 2. Cut-continuous maps between complete graphs

Let `n,m≥2`. An edge map

\[
\rho:E(K_n)\longrightarrow E(K_m)
\]

will be called **cut-continuous** if the inverse image of every binary cut of
`K_m` is a binary cut of `K_n`. Equivalently, it is a cycle-continuous binary
matroid map

\[
M^*(K_n)\longrightarrow M^*(K_m).
\]

For each target vertex `i∈[m]`, the star `δ_{K_m}(i)` is a cut. Therefore there
is a subset `S_i⊆[n]`, unique up to complement, such that

\[
\rho^{-1}(\delta_{K_m}(i))=\delta_{K_n}(S_i).
\]

Choose one representative `S_i` for every `i` and encode each source vertex
`v∈[n]` by

\[
a(v):=(\mathbf1_{v\in S_1},\ldots,\mathbf1_{v\in S_m})\in\mathbf F_2^m.
\]

Changing `S_i` to its complement flips the `i`th coordinate of every `a(v)` and
therefore does not affect pairwise differences.

### Lemma 2.1 — distance-two encoding

For distinct source vertices `u,v`, if

\[
\rho(uv)=ij\in E(K_m),
\]

then

\[
\boxed{a(u)+a(v)=e_i+e_j.}
\]

In particular, the words `a(v)` are pairwise distinct and every two have Hamming
distance exactly two.

#### Proof

The source edge `uv` lies in the cut `δ(S_k)` exactly when its endpoints have
different `k`th membership bits, namely exactly when the `k`th coordinate of
`a(u)+a(v)` is one. By definition of `S_k`, this is equivalent to

\[
\rho(uv)\in\delta_{K_m}(k).
\]

A target edge `ij` belongs to precisely the two vertex stars at `i` and `j`.
Thus the support of `a(u)+a(v)` is exactly `{i,j}`. ∎

## 3. Binary equidistant sets of distance two

### Lemma 3.1

Let `m≥4`. If `A⊆F_2^m` has pairwise Hamming distance exactly two, then

\[
\boxed{|A|\leq m.}
\]

The bound is sharp.

#### Proof

Translate `A` so that `0∈A`. Every other word then has weight two. Identify these
words with two-element subsets of `[m]`. If two such subsets correspond to words
`x,y`, then

\[
d(x,y)=|x\triangle y|=2,
\]

so the two subsets meet in exactly one point. Thus the nonzero words form a
pairwise-intersecting family of two-subsets.

A pairwise-intersecting family of two-subsets is either:

1. contained in a star, in which case it has at most `m-1` members; or
2. the three edges of a triangle, in which case it has at most three members.

For `m≥4`, both bounds are at most `m-1`. Including the zero word gives
`|A|≤m`.

Sharpness is attained by

\[
\{0,e_1+e_2,e_1+e_3,\ldots,e_1+e_m\}.
\]

∎

For completeness, the exceptional target `m=3` admits the four-word tetrahedron

\[
\{000,110,101,011\}.
\]

The rigidity theorem below is stated in the stable range `m≥4`.

## 4. Complete-cographic rigidity

### Theorem 4.1

Let `m≥4`. If there is a cycle-continuous binary matroid map

\[
M^*(K_n)\longrightarrow M^*(K_m),
\]

then

\[
\boxed{n\leq m.}
\]

Conversely, if `n≤m`, an injective vertex map `K_n↪K_m` induces such a map.
Hence, for `m≥4`,

\[
\boxed{
M^*(K_n)\longrightarrow M^*(K_m)
\text{ cycle-continuously}
\iff n\leq m.
}
\]

#### Proof

A cycle-continuous map of the displayed cographic matroids is a cut-continuous
edge map `E(K_n)→E(K_m)`. Lemma 2.1 gives `n` pairwise-distance-two words in
`F_2^m`; Lemma 3.1 gives `n≤m`.

Conversely, embed `[n]` into `[m]` and map every source edge to the corresponding
target edge. The inverse image of a target cut is the cut induced on the embedded
source vertex set, hence is a cut of `K_n`. ∎

## 5. The `K_8` to `K_5` obstruction

### Corollary 5.1

There is no cycle-continuous map

\[
\boxed{M^*(K_8)\longrightarrow M^*(K_5).}
\]

Consequently there is no fixed edge relabelling

\[
E(K_8)\longrightarrow E(K_5)
\]

that converts every eight-support even double cover into a five-support double
cover by target composition.

In the universal root-flow language, no graph-independent map of the twenty-eight
`K_8` roots to the ten `K_5` roots can preserve all cut-to-cycle constraints.

## 6. Strategic consequence for AffineCDC

The ordinary AffineCDC theorem supplies a source-dependent cycle-continuous map

\[
M(G)\longrightarrow M^*(K_8)
\]

with additional Fano/Hamming lifting structure. The five-support conjecture asks
for some map

\[
M(G)\longrightarrow M^*(K_5).
\]

Corollary 5.1 proves that the second map cannot be obtained from the first by one
universal target morphism. Any successful compression must use information from
at least one of:

1. the particular source graph `G`;
2. the chosen root flow / compatible family;
3. a deformation that changes the root flow before selecting a five-coordinate
   slice;
4. decomposition and gluing structure of `G`.

Thus the universal `O^+(6,2)` root model is a genuine ambient existence theorem,
not a target that admits a fixed retraction onto an `O^-(4,2)` five-slice.

## 7. Relation to the distance-two alphabet

The proof also explains the rigidity directly at the support-index level. A
cut-continuous target compression would assign to each of the eight `K_8`
vertices a binary membership word on five proposed supports so that every pair
of source vertices differs in exactly two positions. Such a binary equidistant
code has at most five words. Therefore eight universal support indices cannot be
encoded by five target indices while preserving every root pair.

The obstruction is global and representation-theoretic; it is distinct from the
component-parity obstruction for one fixed Fano flow. The latter may vanish for
some source-dependent root flows even though universal target compression is
impossible.

## 8. Next questions

1. Classify cycle-continuous maps from source-dependent submatroids of
   `M^*(K_8)` into `M^*(K_5)`.
2. Determine which edge-label subsets of `K_8` admit a distance-two quotient
   alphabet of size five.
3. Use the Hamming-Lagrangian structure to characterize when an AffineCDC root
   flow can be deformed into one of the fifty-six induced `K_5` slices.
4. Compare this elementary rigidity theorem with the terminology and existing
   results on tension-continuous maps between complete graphs.