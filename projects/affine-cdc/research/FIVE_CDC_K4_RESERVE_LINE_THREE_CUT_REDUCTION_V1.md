# K4 reserve lines are cyclic three-cut decomposition certificates

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level structural reduction; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_HORIZONTAL_RENEWAL_NEIGHBOURHOOD_V1.md`, `FIVE_CDC_RENEWAL_SKELETON_AND_RESERVE_CODE_CENSUS_V1.md`, `gauge/gauge-modes-and-circuits.md`

## 1. Purpose

The exact renewal censuses found only two kinds of local marked-`K_6` occurrence loci:

1. singleton point cores;
2. affine lines whose direction is a weight-six gauge circuit with harmonic quotient `K_4`.

The line loci initially appeared to be a second genuine obstruction atom. This packet proves that they are instead decomposition certificates.

The central result is:

\[
\boxed{
\text{a connected marked face core admitting a }K_4\text{ reserve direction}
\text{ lies behind a cyclic three-edge cut.}
}
\]

Five-support cycle double covers glue across cyclic three-edge cuts. Consequently a vertex-minimal bridgeless cubic counterexample cannot contain any `K_4` reserve line.

Thus, after the standard minimal-counterexample reduction, the renewal programme becomes a **pure point-renewal problem**.

## 2. Indexed five-support cycle double covers

An indexed five-support cycle double cover of a finite graph is a family

\[
\mathcal F=(F_1,\ldots,F_5)
\]

of even edge sets such that every graph edge belongs to exactly two of the `F_i`.

The supports may be empty and need not be connected. This is the support-level object equivalent to a five-cycle double cover for the present programme.

## 3. Local boundary pattern at a cubic vertex

Let `v` be a cubic vertex with incident edges

\[
e_1,e_2,e_3.
\]

For each pair `ij`, let `n_{ij}` be the number of supports using exactly the two local edges `e_i,e_j` at `v`.

Every support has even local degree, so it uses either zero or two of the three incident edges. Since each edge is covered exactly twice,

\[
\begin{aligned}
n_{12}+n_{13}&=2,\\
n_{12}+n_{23}&=2,\\
n_{13}+n_{23}&=2.
\end{aligned}
\]

### Lemma 3.1 — cubic boundary pair lemma

At every cubic vertex in an indexed five-support cycle double cover,

\[
\boxed{
n_{12}=n_{13}=n_{23}=1.
}
\]

Hence exactly three distinct support indices occur locally, one for each incident-edge pair, and the remaining two supports are locally absent.

#### Proof

Subtracting any two displayed equations gives equality of the three `n_{ij}`. Their common value is then one. ∎

This local pattern is independent of any colouring, root lift, or embedding.

## 4. Gluing across a three-edge cut

Let `G` be a connected cubic loopless multigraph with a three-edge cut

\[
\delta(A)=\{e_1,e_2,e_3\}
\]

separating shores `A` and `B`.

Construct the cubic completions `G_A` and `G_B`:

- retain the subgraph induced by one shore;
- add one new cubic boundary vertex;
- attach its three incident edges to the three dangling endpoints of the cut.

### Lemma 4.1 — bridgeless completion

If `G` is bridgeless and both shores contain cycles, then `G_A` and `G_B` are bridgeless cubic loopless multigraphs.

#### Proof

Cubicity and looplessness are immediate; parallel edges are allowed.

Every original edge lies on a cycle of `G`. If such a cycle leaves the shore, it crosses the three-edge cut an even number of times and hence uses exactly two cut edges. Replace the outside segment by the two-edge path through the new boundary vertex. This gives a cycle in the completion containing the chosen original edge.

For a newly added boundary edge, take a cycle of `G` containing the corresponding original cut edge. It uses at least one other cut edge, and the shore segment together with the new boundary vertex gives a cycle containing the new edge. Thus no edge of either completion is a bridge. ∎

### Theorem 4.2 — five-support three-cut gluing

If both completions `G_A` and `G_B` have indexed five-support cycle double covers, then `G` has one.

#### Proof

Choose indexed covers

\[
(F^A_1,\ldots,F^A_5),
\qquad
(F^B_1,\ldots,F^B_5).
\]

At each new boundary vertex, Lemma 3.1 gives a unique support index for each pair

\[
12,
\qquad13,
\qquad23,
\]

of boundary edges. Permute the five support indices on side `B` so that the three pair-supports agree with those on side `A`; send the two locally absent indices to the two locally absent indices arbitrarily.

Delete the two added boundary vertices. For each support index `j`, take the union of its restrictions on the two shores and include the original cut edge `e_i` exactly when the aligned local support uses boundary edge `i`.

Evenness at every original vertex is inherited from the two completed covers. Each internal edge remains covered twice. Each cut edge belongs to exactly the same two aligned supports on both shores, and therefore is also covered exactly twice after gluing. ∎

### Corollary 4.3 — minimal-counterexample connectivity

A vertex-minimal bridgeless cubic loopless multigraph without a five-support cycle double cover has no cyclic edge cut of size three.

Indeed, both cyclic shores have at least two vertices, so both bridgeless cubic completions have fewer vertices; minimality and Theorem 4.2 give a contradiction.

Equivalently, a vertex-minimal counterexample may be assumed cyclically four-edge-connected.

## 5. K4 harmonic supports

Fix a nowhere-zero Fano flow `f` on `G`. Let

\[
0\ne\lambda\in B_f
\]

be a weight-six gauge word with support

\[
S=\operatorname{supp}\lambda.
\]

Assume its harmonic cut quotient is

\[
Q_S\cong K_4.
\]

Thus `G-S` has exactly four connected components, and the six edges of `S` join every pair of components exactly once.

Fix a gauge state and a connected marked core `C` in the dual triangulation. Its vertices are marked support-cycle faces. Let

\[
Z_C
\]

be their face zone and

\[
R_C=E(G)\setminus Z_C
\]

its reserve.

The gauge word `\lambda` is a direction of the occurrence locus of `C` exactly when

\[
S\subseteq R_C,
\]

that is, when every marked face avoids every edge of `S`.

## 6. The reserve-line separation theorem

### Theorem 6.1 — K4 reserve direction produces a cyclic three-cut

Assume:

1. `Q_S\cong K_4`;
2. `C` is a nonempty connected marked face core;
3. `S\subseteq R_C`.

Then all marked faces of `C` lie in one component `H` of `G-S`, and

\[
\boxed{
|\delta_G(H)|=3.
}
\]

Moreover both shores of this cut contain cycles. Hence `\delta_G(H)` is a cyclic three-edge cut.

#### Proof

Every marked face is a face-boundary cycle avoiding `S`. It is therefore contained in one connected component of `G-S`.

If two marked faces are adjacent in the dual core, their adjacency is witnessed by a source edge traversed by both faces. That edge is not in `S`, so it lies inside one component of `G-S`; hence the two faces lie in the same component. Since `C` is connected, all its faces lie in one component, call it `H`.

The quotient `Q_S` is `K_4`. Therefore exactly one edge of `S` joins `H` to each of the other three components, and no edge outside `S` joins different components. Hence

\[
\delta_G(H)
\]

consists of exactly three edges.

The shore `H` contains every marked face and therefore contains a cycle.

Let the other components be `H_1,H_2,H_3`. The quotient contains the triangle

\[
H_1H_2H_3H_1.
\]

Inside each connected `H_i`, choose a path joining the endpoints of its two quotient-triangle edges; a zero-length path is allowed when the endpoints coincide. The three paths together with the three intercomponent edges form a cycle in the complementary shore. Thus the cut is cyclic. ∎

### Corollary 6.2 — K4 reserve lines are reducible

If a marked core has an affine occurrence line whose direction is a weight-six `K_4` gauge circuit, then `G` has a cyclic three-edge cut.

Consequently no such line occurs in any root-lift gauge fibre of a vertex-minimal bridgeless cubic counterexample to the five-support cycle double cover statement.

This conclusion does not depend on the reserve having size six or seven. Every `K_4` reserve line, with an arbitrarily large reserve, is excluded in the minimal-counterexample regime.

## 7. The small-reserve triangular cap

The exact census found only reserves of size six and seven. The general three-cut theorem gives an additional concrete description in these cases.

Let `H` be the core component from Theorem 6.1, and let `X` be any of the three other components of `G-S`. Since `X` has three boundary edges and `G` is cubic,

\[
3|V(X)|=2|E(X)|+3.
\]

If `X` is not a singleton, then `|V(X)|\ge3` and

\[
|E(X)|\ge3.
\]

Every internal edge of `X` lies outside the marked face zone and therefore belongs to `R_C\setminus S`.

### Corollary 7.1 — six- and seven-edge reserves force a triangle cap

If

\[
|R_C\setminus S|\le2,
\]

then the three components outside `H` are single vertices. They form a triangle, and each has one spoke into `H`.

Equivalently, `G` is obtained by attaching the cubic three-pole

\[
K_4-v
\]

—a triangle with one dangling edge at each vertex—to the core shore `H`.

In particular:

- if `R_C=S`, every non-`S` edge of the core shore is traversed by the marked core;
- if `|R_C|=7`, the unique extra reserve edge lies inside `H`, not in the external triangle cap.

This explains the exact six-versus-seven reserve observation without making essentiality itself a purely local theorem.

## 8. Direct triangle contraction as a special case

The triangular cap also admits a direct reduction.

Contract its triangle to one cubic vertex. Given a five-support cycle double cover of the contracted graph, Lemma 3.1 gives one support for each pair of incident spokes.

Expand the support using spokes `i,j` along the two-edge triangle path through the third triangle vertex, rather than along the direct triangle edge `ij`. Then:

- every support remains even at all three new triangle vertices;
- each triangle edge lies in exactly two of the three pair-supports;
- all other edge multiplicities are unchanged.

Hence a five-support cover of the triangle contraction lifts to the original graph.

This is the one-shore specialization of Theorem 4.2.

## 9. Reinterpretation of the exact censuses

The complete horizontal bad-neighbour census found:

- `3574` pure point-renewal arrangements;
- `79` arrangements with positive-dimensional loci;
- exactly `96` line loci;
- every line generated by a weight-six `K_4` harmonic circuit.

Theorem 6.1 now changes their interpretation.

The `96` lines are not an independent obstruction family. Every one certifies a cyclic three-edge decomposition of the underlying graph. In a minimal-counterexample analysis they disappear before the renewal dynamics is considered.

Thus the finite evidence, after structural reduction, becomes:

\[
\boxed{
\text{minimal-counterexample renewal geometry is pure point geometry.}
}
\]

This is a conditional structural statement: it combines the theorem-level minimal-counterexample reduction with the exact fact that the displayed positive-dimensional loci are all `K_4` lines.

## 10. Updated mechanism map

### Layer A — local half-cube obstruction

A marked dual `K_6` obstructs

\[
T_g\longrightarrow\mathscr A_5.
\]

### Layer B — reserve-shortened gauge code

Its occurrence direction is

\[
B_f\cap\mathbf F_2^{R_C}.
\]

A nonzero `K_4` direction does not create an irreducible persistence mode. It exposes a cyclic three-edge cut.

### Layer C — decomposition gate

Before studying renewal, split and glue across every cyclic three-edge cut. In a minimal counterexample this removes all `K_4` reserve lines.

### Layer D — irreducible renewal

The remaining marked cores are private points:

\[
B_f\cap\mathbf F_2^{R_C}=0.
\]

Every nonzero gauge word destroys the current core, but another private core appears at the new state.

### Layer E — horizontal transport

Connected-cycle flow switches usually create an uncovered good state. The residual irreducible question is whether pure point-renewal modules can remain closed under all horizontal moves.

The mechanism has therefore simplified from

\[
\text{points plus lines}
\]

to

\[
\boxed{
\text{pure private-point renewal after three-cut reduction}.
}
\]

## 11. Refined next targets

### 11.1 Pure point-renewal theorem

For a cyclically four-edge-connected cubic graph, analyze a wholly bad gauge fibre in which every marked obstruction core is private.

Every private core `C` satisfies

\[
B_f\cap\mathbf F_2^{R_C}=0,
\]

so its face zone is a coordinate information set for the entire gauge code. Convert this injectivity into an incompatibility among the state-indexed `K_6` zones.

### 11.2 Point-core transition law

Derive how the private core assigned to `\beta` changes under

\[
\beta\mapsto\beta+\lambda.
\]

The universal three- and six-dimensional modules provide exact templates, but a conceptual update rule remains open.

### 11.3 Four-edge harmonic interfaces

The universal three-cube is driven at minimum weight by a `2K_3` harmonic quotient. Each quotient component has boundary size four. After eliminating the `K_4` three-cut atom, the next decomposition question is whether repeated `2K_3` interfaces produce a controlled four-edge-sum theorem or a genuinely irreducible four-pole obstruction.

### 11.4 Horizontal escape-or-decomposition

The new desired dichotomy is:

\[
\boxed{
\text{some horizontal move breaks pure point coverage}
}

or

\[
\boxed{
\text{persistent private-point renewal forces a bounded four-pole decomposition}.
}
\]

## 12. Trust boundary

The cubic boundary lemma, three-cut gluing theorem, K4 reserve separation theorem, triangular-cap corollary, and triangle expansion are elementary graph-theoretic results proved in this packet.

The historical literature status of these precise formulations has not yet been audited. They are presented as programme theorems, not as claims of novelty.

The numerical reinterpretation uses the exact previously recorded census that all positive-dimensional loci in the displayed neighbourhood are weight-six `K_4` lines.

No statement here proves that every compatible bad dual contains `K_6`, that every pure point-renewal module is horizontally escapable, or that every bridgeless cubic graph has a five-cycle double cover.
