# AC-PD-A6 — graph-level indexed even-support extraction

**Proof-development state:** `COMPLETE-DRAFT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Depends on:** `AC-PD-A4`, `AC-PD-A5`  
**Immediate consumers:** `AC-PD-A7`, `AC-PD-A8`  
**External mathematical inputs:** none  
**Formal anchor inspected:** `Yuren-Tang/affine-cdc@ebd7098a7a8b824e8c0a511d3c71f61705672aa8`

## 0. Main output

Let `G` be a finite loopless cubic multigraph, not necessarily connected, carrying a nowhere-zero flow

\[
f:E(G)\longrightarrow\Gamma\setminus\{0\},
\qquad
\Gamma=\mathbf F_2^3.
\]

Choose a globally compatible collection of local affine even families, whose existence is A5. Then there is a finite `Γ`-indexed family

\[
\mathcal F=(F_s)_{s\in\Gamma},
\qquad
F_s\subseteq E(G),
\]

such that:

1. each `F_s` is vertex-even in the current loopless once-per-edge incidence sense;
2. every edge belongs to exactly two indexed members;
3. empty supports and equal supports at different indices are retained;
4. forgetting index names gives a finite multiset of vertex-even supports with exact double coverage.

This is the natural graph-level output of the affine core. No circuit decomposition occurs here.

## 1. Compatible incidence lines

At every incidence `(v,e)`, the chosen local family assigns an affine line

\[
\mathcal L_{v,e}\subseteq\Gamma
\]

of direction `f(e)`. Concretely, if its quotient label in

\[
Q_e=\Gamma/\langle f(e)\rangle
\]

is represented by `p`, then

\[
\mathcal L_{v,e}=p+\langle f(e)\rangle
=
\{p,p+f(e)\}.
\]

### Lemma 1.1 — every assigned line has exactly two points

For every incidence `(v,e)`,

\[
|\mathcal L_{v,e}|=2.
\]

#### Proof

The direction `f(e)` is nonzero. Therefore the two points `p` and `p+f(e)` are distinct, and `\langle f(e)\rangle=\{0,f(e)\}`. ∎

Global compatibility means that for every edge `e=uv`,

\[
\mathcal L_{u,e}=\mathcal L_{v,e}.
\]

Hence there is a well-defined edge line

\[
\mathcal L_e
\]

independent of endpoint.

### Retained dart formulation

Equivalently, let `Δ=I(G)` be the dart set and let `σ` exchange the two darts of each edge. For `s\in Γ`, define

\[
M_s:=\{(v,e)\in\Delta:s\in\mathcal L_{v,e}\}.
\]

Compatibility is exactly the `σ`-closure law

\[
d\in M_s\iff\sigma d\in M_s.
\]

Thus each `M_s` descends to a set of edge objects. This descent uses the retained graph/dart pairing; it cannot be reconstructed from a bare abstract pair complex.

## 2. Definition of graph-level supports

For each `s\in Γ`, define

\[
\boxed{
F_s:=\{e\in E(G):s\in\mathcal L_e\}.
}
\]

Equivalently, `e\in F_s` when either, hence both, endpoint darts of `e` lie in `M_s`.

Since `E(G)` is finite, every `F_s` is finite. Since `Γ=F_2^3` has eight elements, the indexed family itself is finite.

## 3. Local vertex parity

Fix a vertex `v` and a point `s\in Γ`. The three incident edge lines are exactly the three members of the chosen local affine family at `v`.

### Lemma 3.1 — incidence correspondence

The map sending an incident edge object `e` to its local line gives a bijection between

\[
F_s\cap\operatorname{Inc}_G(v)
\]

and the directions in the local family whose assigned line contains `s`.

#### Proof

At a cubic nowhere-zero binary-flow vertex, the three incident edge values are pairwise distinct and are the three nonzero directions of the local plane. Hence distinct incident edge objects correspond to distinct direction slots. By definition,

\[
e\in F_s
\iff
s\in\mathcal L_e
\iff
s\in\mathcal L_{v,e}.
\]

This proves the claimed bijection. Parallel edges cause no collision: if two parallel edge objects meet the same vertex, the cubic flow injectivity at that vertex forces their flow values, and hence their direction slots, to be distinct. ∎

### Theorem 3.2 — vertex-even support

For every `s\in Γ` and every vertex `v`,

\[
|F_s\cap\operatorname{Inc}_G(v)|
\equiv0\pmod2.
\]

Indeed the cardinality is either zero or two.

#### Proof

The chosen local family is even: every point of `Γ` lies on an even number of its three lines. The only even cardinalities between zero and three are zero and two. Apply Lemma 3.1. ∎

Thus every `F_s` is vertex-even in the current loopless once-per-edge incidence representation. A7 will prove the exact equivalence of this condition with intrinsic cut-evenness.

## 4. Exact edge multiplicity two

### Theorem 4.1 — exact double coverage

For every edge `e\in E(G)`,

\[
\boxed{
\left|\{s\in\Gamma:e\in F_s\}\right|=2.
}
\]

#### Proof

By definition,

\[
e\in F_s
\iff
s\in\mathcal L_e.
\]

Therefore

\[
\{s\in\Gamma:e\in F_s\}=\mathcal L_e.
\]

Lemma 1.1 says that `\mathcal L_e` has exactly two points. ∎

This counts **index occurrences**. It does not require the two containing supports to be distinct as subsets of `E(G)`.

## 5. Indexed family and multiset flattening

Let the index set be the eight-element set `Γ` itself. Define

\[
\mathcal F:=(F_s)_{s\in\Gamma}.
\]

Its coverage multiplicity is

\[
\mu_{\mathcal F}(e)
:=
|\{s\in\Gamma:e\in F_s\}|.
\]

By Theorem 4.1,

\[
\mu_{\mathcal F}(e)=2
\]

for every active edge.

### Definition 5.1 — multiset flattening

The associated multiset is the image multiset

\[
[\,F_s:s\in\Gamma\,].
\]

If `F_s=F_t` for `s\ne t`, both occurrences remain. If `F_s=\varnothing`, that empty occurrence remains unless a later consumer deliberately removes it and proves that removal harmless.

### Proposition 5.2 — flattening preserves coverage multiplicity

For every edge `e`, the number of multiset occurrences containing `e` is exactly

\[
|\{s\in\Gamma:e\in F_s\}|=2.
\]

#### Proof

Multiset image preserves one occurrence for every index. Filtering the image multiset by the predicate `e\in(-)` therefore counts precisely the source indices satisfying `e\in F_s`, including different indices with equal image support. ∎

### Corollary 5.3 — natural affine output

The compatible family yields a finite multiset of vertex-even edge supports with exact double coverage.

This is an even-support cover, not yet a cycle double cover. A7 converts vertex parity to intrinsic cut parity; A9 later decomposes the collapsed supports into circuits.

## 6. Dart-level structural refinement

The retained dart construction contains more data than the graph-level family requires.

For fixed `s`, every selected dart `d\in M_s` has a unique distinct selected dart at the same vertex. This follows either from local evenness plus cubicity or from the explicit Fano partner formula. Crossing the edge by `σ` and then taking the vertex partner defines a permutation

\[
\rho_s
\]

of `M_s`; its finite orbits trace closed dart walks.

This rotation witness is valid but is deliberately not consumed by the complete theorem spine. Decomposing at the dart level before collapse would create cycle structure that the collapse map need not preserve. The canonical route retains only:

- `σ`-closure, to descend darts to edge supports;
- same-vertex evenness, to prove support parity;
- exact two-point membership, to prove edge multiplicity two.

The generic circuit decomposition is postponed to A9 after collapse.

## 7. Components and degenerate cases

### Disconnected graph

The construction is global but splits componentwise. A support `F_s` is the disjoint union of its restrictions to the edge-bearing components. Vertex parity and edge multiplicity are checked independently on each component.

### Empty graph

Every `F_s` is empty. The eight-index family has no edge multiplicity obligations and is vertex-even. It may later be replaced by the empty multiset after proving invariance under deletion of empty occurrences.

### Empty indexed members

A point `s` may lie on no selected edge line, so `F_s=\varnothing`. This is compatible with all parity and multiplicity conditions.

### Repeated indexed members

Different points may define equal supports. They remain distinct indexed occurrences and distinct multiset occurrences. Collapsing equal values to a set of supports would generally destroy exact coverage counts.

### Parallel edges

They remain distinct edge objects in every `F_s`; local incidence slots and global multiplicity count them separately.

### Loops

The affine graph is loopless. Loop support semantics belong to A1 and are reintroduced only after the loopless core has received its CDC.

## 8. Exact formal correspondence

The inspected companion Lean checkpoint provides the following machine-checked pieces.

1. `Msupp m s` is the dart set whose assigned local line contains `s`.
2. For a glued gauge, `Msupp_sigma` proves `σ`-closure.
3. `setOf_mem_Msupp` and `ncard_setOf_mem_Msupp` prove that every dart belongs to exactly the two point-indexed supports of its assigned affine line.
4. `Msupp_vertex_unique` proves the unique distinct selected partner at a vertex.
5. `exists_indexed_dart_cover` packages the indexed dart family, exact double coverage, partner, and rotation data.
6. `Port.cubic_flow_cdc` constructs graph edge supports by taking the image of selected darts, proves endpoint-dart membership equivalence, vertex evenness, and exact edge coverage two, and then immediately applies generic decomposition.

The graph-level factorization in this dossier is therefore not merely suggested by the Lean code; its essential support and counting statements already occur inside the checked macro-Port proof. The invariant paper presentation and the decision to stop before circuit decomposition are proof-development reorganizations, not claims that the entire current theorem spine is machine-checked.

## 9. Exported interface

A7 and A8 may cite:

1. a finite `Γ`-indexed family `(F_s)_{s\in Γ}` of graph edge supports;
2. each support is finite and vertex-even;
3. every graph edge lies in exactly two indexed members;
4. endpoint choice is irrelevant because the dart support is `σ`-closed;
5. the associated multiset retains empty and repeated supports;
6. flattening preserves exact edge multiplicity;
7. no circuit decomposition has yet been used;
8. all graph, edge-object, incidence, and dart pairing data remain explicit.

## 10. Completion assessment

`AC-PD-A6` is `COMPLETE-DRAFT`. No contradiction, source gap, or new-mathematics problem arose. The next dependency-respecting unit is `AC-PD-A7`: prove the exact equivalence, on the finite loopless graph used here, between the once-per-edge vertex-even predicate and intrinsic half-edge boundary parity, hence cut-evenness.
