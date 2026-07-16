# Source-dependent half-cube compression of AffineCDC root covers

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level research checkpoint; not canonical pending literature audit  
**Parents:** `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`, `FIVE_CDC_K5_COGRAPHIC_MAP_V1.md`, `FIVE_CDC_NO_UNIVERSAL_K8_TO_K5_COMPRESSION_V1.md`

## 1. Why coordinate omission is too restrictive

Let

\[
g:E(G)\longrightarrow E(K_8)
\]

be the root-flow labelling associated with an eight-index AffineCDC even double
cover. Requiring three of the original eight coordinate supports to be empty is
equivalent to requiring the image of `g` to lie in one induced `K_5⊂K_8`.

A general five-support cover need not arise by deleting three original
coordinates. The five new support indicators may be binary sums of the eight old
ones. At the root-label level this is a source-dependent cut-continuous relabelling
of the actually used `K_8` edges.

## 2. The used-label graph

Define the **used-label graph** `J_g` to be the simple spanning subgraph of `K_8`
whose edge set is

\[
E(J_g):=g(E(G)).
\]

The edge map

\[
g:E(G)\longrightarrow E(J_g)
\]

pulls every cut of `J_g` back to an even support of `G`. Indeed, for
`S⊆V(J_g)⊆V(K_8)`,

\[
g^{-1}(\delta_{J_g}(S))
=
g^{-1}(\delta_{K_8}(S)),
\]

and the latter is the binary sum of the original coordinate supports indexed by
`S`.

Thus

\[
M(G)\longrightarrow M^*(J_g)
\]

is cycle-continuous.

## 3. The five-dimensional distance-two graph

Let

\[
\mathscr A_5
\]

be the graph with vertex set `F_2^5` in which two words are adjacent exactly when
their Hamming distance is two. It has two connected components, according to
weight parity. Translating by a fixed word identifies the two components, so one
may equivalently use the even-weight component

\[
H_5=\{z∈F_2^5:\sum_i z_i=0\}.
\]

Two vertices of `H_5` are adjacent exactly when their difference is one of the
ten anisotropic weight-two roots of the minus-type quadratic space
`(H_5,q_5)`. Thus `\mathscr A_5` is the anisotropic Cayley graph of the
five-support alphabet.

## 4. Cut-continuity as a half-cube homomorphism

### Theorem 4.1 — half-cube encoding theorem

For a finite graph `J`, the following are equivalent.

1. There is a cut-continuous edge map
   \[
   \rho:E(J)\longrightarrow E(K_5).
   \]
2. There is a graph homomorphism
   \[
   a:V(J)\longrightarrow\mathscr A_5.
   \]
3. There is a vertex potential
   \[
   a:V(J)\longrightarrow F_2^5
   \]
   such that for every edge `uv∈E(J)`, the difference
   \[
   a(u)+a(v)
   \]
   has Hamming weight exactly two.

Under this equivalence,

\[
\boxed{
\rho(uv)=\operatorname{supp}(a(u)+a(v))∈\binom{[5]}2.
}
\]

#### Proof

`(1)⇒(3)`: for each target vertex `i∈[5]`, the inverse image of the star
`δ_{K_5}(i)` is a cut `δ_J(S_i)`. Put

\[
a(v)_i:=\mathbf1_{v∈S_i}.
\]

For an edge `uv`, its `i`th difference coordinate is one exactly when
`ρ(uv)` is incident with `i`. A target edge has exactly two endpoints, so
`a(u)+a(v)` has weight two and its support is `ρ(uv)`.

`(3)⇒(1)`: define `ρ(uv)` by the displayed formula. For each `i`, let
`S_i={v:a(v)_i=1}`. Then

\[
\rho^{-1}(\delta_{K_5}(i))=\delta_J(S_i),
\]

so the inverse image of each star is a cut. Since the stars generate the cut
space of `K_5`, every target cut pulls back to a cut.

The equivalence of `(2)` and `(3)` is the definition of `\mathscr A_5`. ∎

For each connected component of `J`, translation of all potentials by one word
preserves edge differences, so the image may be placed inside the even component
`H_5`.

## 5. Compression theorem for a fixed root flow

### Theorem 5.1 — source-dependent root compression

Let `g:E(G)→E(K_8)` be an AffineCDC root flow and let `J_g` be its used-label
graph. If

\[
J_g\longrightarrow\mathscr A_5
\]

admits a graph homomorphism, then `G` has a five-support double cover.

More precisely, any such homomorphism induces a cut-continuous map

\[
M^*(J_g)\longrightarrow M^*(K_5),
\]

and composition gives

\[
M(G)\longrightarrow M^*(J_g)
\longrightarrow M^*(K_5).
\]

The five resulting supports are, for `i∈[5]`,

\[
\boxed{
D_i
=
\bigtriangleup_{\substack{s∈F_2^3\\a(s)_i=1}}F_s,
}
\]

where `(F_s)` is the original eight-index cover and `\triangle` denotes symmetric
difference. Empty or unused label vertices may be assigned arbitrary potentials.

#### Proof

Theorem 4.1 gives a cut-continuous edge map `J_g→K_5`. The root-flow map
`G→J_g` pulls cuts back to cycles. Composition therefore pulls every `K_5` cut
back to a cycle of `G`, and the `K_5` cographic-map theorem gives a five-support
double cover.

The formula for `D_i` is the pullback of the target star at `i`: an original
root edge `{s,t}` maps to a target edge incident with `i` exactly when
`a(s)_i+a(t)_i=1`. ∎

This theorem does not preserve the original projected `F_2^3`-flow. It converts
one eight-root witness into a new anisotropic `H_5`-flow and hence generally
changes the Fano-flow presentation.

## 6. Easy sufficient conditions

### Corollary 6.1

If the used-label graph `J_g` is properly five-colourable, then the root flow
compresses to five supports.

#### Proof

Choose distinct unit vectors `e_1,…,e_5` for the five vertex colours. Adjacent
vertices receive different unit vectors, whose difference has weight two. Apply
Theorem 5.1. ∎

This is only sufficient, not necessary: the anisotropic graph `\mathscr A_5` has
sixteen vertices and admits homomorphic images not arising from a five-colouring.

The original omitted-triple condition is the special case in which `J_g` is
contained in an induced `K_5` of `K_8`, and the potential `a` is the corresponding
injective unit-vector labelling.

## 7. The cube fixed-flow example revisited

For the compatible family in the cube obstruction packet, the six used support
indices are

\[
0,2,4,5,6,7.
\]

The twelve used root labels form

\[
J_g=K_6-\{05,26,47\},
\]

the octahedral graph `K_{2,2,2}` with independent parts

\[
\{0,5\},\qquad\{2,6\},\qquad\{4,7\}.
\]

Thus `J_g` is three-colourable. The symmetric-difference supports

\[
\boxed{
D_1=F_0\triangle F_5,
\qquad
D_2=F_2\triangle F_6,
\qquad
D_3=F_4\triangle F_7
}
\]

form a three-support double cover of the cube. Each is a 2-factor consisting of
two opposite square faces.

Therefore the earlier cube theorem says only:

> no compatible lift of that fixed Fano flow can omit three original affine
> indices.

It does **not** obstruct source-dependent parity recombination of the eight
supports, and it does not obstruct compression of the resulting root flow.

## 8. Strategic correction

There are now three distinct compression levels.

1. **Coordinate omission:** choose a root flow lying in an induced `K_5⊂K_8`.
   This preserves a chosen five-subset of the original support indices.
2. **Source-dependent target compression:** allow a homomorphism
   `J_g→\mathscr A_5`, equivalently a cut-continuous map `J_g→K_5`. This replaces
   the supports by symmetric-difference combinations.
3. **Universal target compression:** require one map `K_8→K_5` working for every
   root flow. The complete-cographic rigidity theorem proves this impossible.

The second level is substantially more flexible than the first and remains
compatible with the impossibility of the third.

The natural next problem is therefore:

\[
\boxed{
\text{Can every bridgeless cubic graph be given an AffineCDC root flow }g
\text{ whose used-label graph }J_g\text{ maps to }\mathscr A_5?
}
\]

A positive theorem would prove five-support CDC. A negative fixed-root example
would identify a genuinely source-dependent compression obstruction beyond mere
coordinate support size.

## 9. Next questions

1. Classify the subgraphs `J⊆K_8` that admit a homomorphism to `\mathscr A_5`.
2. Determine minimal non-homomorphic subgraphs and whether any can occur as the
   used-label graph of a cubic root flow.
3. Analyze how Hamming-gauge deformations of a root flow change `J_g`.
4. Search for structural conditions—clique number, multipartite structure, or
   triangle decompositions—that force `J_g→\mathscr A_5`.
5. Compare this half-cube encoding with known tension-continuous and
   `K_5`-flow-colouring formulations.