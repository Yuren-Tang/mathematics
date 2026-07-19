# AC-PD-A0 — foundational multigraph, parity, circuit, and multiplicity semantics

**Proof-development state:** `COMPLETE-DRAFT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Depends on:** none  
**Immediate consumers:** `AC-PD-A1`, `A2`, `A7`, `A9`, `A10`  
**External mathematical inputs:** none

## 0. Purpose and boundary

This unit closes the foundational interface used by the complete Cycle Double Cover spine. It fixes:

- the multigraph and finite-active-edge model;
- loops, parallel edge objects, active vertices, components, and cuts;
- intrinsic mod-two boundary parity and cut-even supports;
- the relation to the current loopless once-per-edge incidence convention;
- circuits, including singleton loops and parallel-edge digons;
- singleton cuts and bridges;
- indexed-family and multiset multiplicity semantics;
- empty, isolated-vertex, disconnected, and loop-only edge cases.

This unit proves the **characterization** of a circuit. It does **not** prove that every finite cut-even support decomposes into circuits; that termination/decomposition theorem is `AC-PD-A9`.

The theorem layer identifies the graph with its active edges. An implementation may use larger ambient vertex and edge carriers together with active predicates, but inactive edge objects play no mathematical role.

## 1. Multigraph model

### Definition 1.1 — multigraph

A multigraph is a triple

\[
G=(V,E,\partial),
\]

where `V` is a vertex set, `E` is the set of active edge objects, and

\[
\partial:E\longrightarrow \operatorname{Sym}^2(V)
\]

assigns to each edge an unordered pair of endpoints with repetition allowed.
Equivalently, one may choose endpoint maps `s,t:E -> V` and regard two choices differing by an edgewise swap as the same unoriented datum.

For an edge `e` with endpoint multiset `{u,v}`:

- `e` is a **loop** when `u=v`;
- `e` is a **nonloop edge** when `u\ne v`;
- two distinct edge objects are **parallel** when they have the same endpoint multiset.

Parallel edges are always counted separately. No support or cover operation identifies equal endpoint pairs.

### Definition 1.2 — finite active edge set

The natural finiteness hypothesis is

\[
E(G)\text{ is finite}.
\]

The ambient vertex set may be infinite. Define the active vertex set

\[
V_+(G):=\{v\in V(G):v\text{ is an endpoint of some }e\in E(G)\}.
\]

Vertices outside `V_+(G)` are isolated.

### Lemma 1.3 — active vertices are finite

If `E(G)` is finite, then `V_+(G)` is finite and

\[
|V_+(G)|\le 2|E(G)|.
\]

#### Proof

Every active vertex occurs among the two endpoints of an active edge. Hence `V_+(G)` is contained in the union of `|E(G)|` sets of size at most two. ∎

### Definition 1.4 — deletion and support subgraph

For `A\subseteq E(G)`, the spanning edge-deletion subgraph `G[A]` has vertex set `V(G)`, active edge set `A`, and the restricted endpoint map. We write `G-e` for `G[E(G)\setminus\{e\}]`.

The active vertices of `G[A]` are the endpoints of edges in `A`; all other vertices are harmless isolated vertices.

## 2. Cuts

### Definition 2.1 — active cut

For `S\subseteq V(G)`, define

\[
\delta_G(S)
:=
\{e\in E(G):\text{ exactly one endpoint occurrence of }e\text{ lies in }S\}.
\]

Thus:

- a nonloop edge `uv` lies in `\delta_G(S)` exactly when one of `u,v` lies in `S` and the other does not;
- a loop never lies in any cut;
- `\delta_G(S)=\delta_G(V(G)\setminus S)`.

Since `E(G)` is finite, every cut is finite.

### Lemma 2.2 — cuts see only active vertices

For every `S\subseteq V(G)`,

\[
\delta_G(S)=\delta_G(S\cap V_+(G)).
\]

#### Proof

Every endpoint of every active edge lies in `V_+(G)`. Membership of an edge in the cut therefore depends only on membership of its endpoints in `S\cap V_+(G)`. ∎

Consequently, although cuts are quantified over all subsets of a possibly infinite vertex carrier, only subsets of the finite set `V_+(G)` matter.

### Definition 2.3 — singleton-cut and bridgeless conditions

A **singleton cut** is a cut of cardinality one. We write

\[
\operatorname{NoSingletonCut}(G)
\iff
\forall S\subseteq V(G),\quad |\delta_G(S)|\ne1.
\]

A nonloop edge `e=uv` is a **bridge** when `u` and `v` lie in different connected components of `G-e`. A loop is not a bridge.

Connectivity is by finite edge paths. Isolated vertices form singleton components but are irrelevant to the edge-bearing theorem.

### Proposition 2.4 — singleton cut equals bridge

For a nonloop edge `e=uv`, the following are equivalent:

1. `e` is a bridge;
2. there exists `S\subseteq V(G)` with `\delta_G(S)=\{e\}`.

Hence `G` has no singleton cut if and only if it has no bridge.

#### Proof

If `\delta_G(S)=\{e\}`, the endpoints of `e` lie on opposite sides of `S`, and after deleting `e` no edge crosses from one side to the other. Thus the endpoints are disconnected in `G-e`.

Conversely, suppose `u` and `v` are disconnected in `G-e`. Let `S` be the set of vertices reachable from `u` in `G-e`. Then `u\in S`, `v\notin S`, and no edge of `G-e` crosses `S`. Therefore the only edge of `G` crossing `S` is `e`. ∎

### Corollary 2.5 — componentwise bridge condition

`G` has no singleton cut if and only if every edge-bearing connected component has no bridge. Loops and isolated vertices do not affect this condition.

## 3. Intrinsic parity of a support

### Definition 3.1 — finite support

A **support** is a subset `F\subseteq E(G)`. Under the finite-active-edge hypothesis every support is finite. In later interfaces where the ambient active edge set need not be finite, the word support in parity and decomposition theorems will explicitly mean a finite edge subset.

### Definition 3.2 — half-edge degree and mod-two boundary

For a finite support `F` and a vertex `v`, let

\[
\deg_F(v)
\]

be the number of endpoint occurrences at `v` among edges of `F`. Thus a nonloop edge incident with `v` contributes one and a loop at `v` contributes two.

Define the mod-two boundary

\[
\partial_G F
:=
\{v\in V(G):\deg_F(v)\equiv1\pmod2\}.
\]

Only finitely many vertices have nonzero `F`-degree.

We call `F` **boundary-even** when `\partial_GF=\varnothing`.

### Definition 3.3 — cut-even support

A finite support `F\subseteq E(G)` is **cut-even** when

\[
\operatorname{CutEven}_G(F)
\iff
\forall S\subseteq V(G),\quad
|F\cap\delta_G(S)|\equiv0\pmod2.
\]

### Lemma 3.4 — cut parity identity

For every finite support `F` and every `S\subseteq V(G)`,

\[
|F\cap\delta_G(S)|
\equiv
\sum_{v\in S}\deg_F(v)
\pmod2.
\]

The sum is finite because only endpoints of edges of `F` contribute.

#### Proof

Count endpoint occurrences of selected edges at vertices of `S`.

- a nonloop selected edge internal to `S` contributes two;
- a selected edge outside `S` contributes zero;
- a selected crossing edge contributes one;
- a selected loop in `S` contributes two.

Modulo two, only crossing edges remain. ∎

### Theorem 3.5 — intrinsic boundary-even/cut-even equivalence

For every multigraph and every finite support `F`,

\[
\boxed{
\operatorname{CutEven}_G(F)
\iff
\partial_GF=\varnothing.
}
\]

#### Proof

If `F` is cut-even, apply the definition to the singleton set `S=\{v\}`. By Lemma 3.4,

\[
\deg_F(v)\equiv |F\cap\delta_G(\{v\})|\equiv0\pmod2
\]

for every vertex `v`. Hence `\partial_GF=\varnothing`.

Conversely, if every `F`-degree is even, Lemma 3.4 gives even intersection with every cut. ∎

### Remark 3.6 — relation to the current companion incidence API

The intrinsic degree counts a loop twice. The companion AffineCDC formalization currently uses a once-per-edge incidence set. On a loopless graph,

\[
\deg_F(v)=|F\cap\operatorname{Inc}_G(v)|,
\]

so its vertex-even predicate agrees with intrinsic boundary-evenness and therefore with cut-evenness.

With loops present, once-per-edge incidence parity is different: a loop contributes one there but zero to the intrinsic mod-two boundary. No proof may silently transport the loopless once-per-edge predicate across loops. The full mathematical theorem uses cut-even supports (or, equivalently, half-edge boundary parity); the current loopless formal API is a representation-specific corollary.

### Corollary 3.7 — componentwise parity

Let `G_j` be the edge-bearing connected components of `G`, and put `F_j=F\cap E(G_j)`. Then

\[
F\text{ is cut-even in }G
\iff
F_j\text{ is cut-even in }G_j\text{ for every }j.
\]

#### Proof

The `F`-degree of a vertex depends only on the support inside its component. Apply Theorem 3.5. ∎

## 4. Circuits

### Definition 4.1 — circuit

A **circuit** of `G` is a nonempty finite support `C\subseteq E(G)` which is cut-even and is inclusion-minimal among nonempty cut-even supports:

\[
C\ne\varnothing,
\qquad
\operatorname{CutEven}_G(C),
\]

and no nonempty proper subset of `C` is cut-even.

Minimality is with respect to edge objects. Two parallel edges are distinct and may form a two-edge circuit.

### Definition 4.2 — polygonal cycle support

A **polygonal cycle support** is an edge set `C=\{e_0,\dots,e_{n-1}\}` with `n\ge1` for which there are vertices `v_0,\dots,v_{n-1}` such that:

- the edge objects `e_i` are pairwise distinct;
- `e_i` has endpoints `v_i` and `v_{i+1}` with indices modulo `n`;
- for `n\ge2`, the vertices `v_0,\dots,v_{n-1}` are pairwise distinct.

The small cases are interpreted literally:

- `n=1`: `e_0` is a loop at `v_0`;
- `n=2`: `e_0,e_1` are two distinct parallel edges between `v_0,v_1`;
- `n\ge3`: the ordinary simple cycle edge set.

### Lemma 4.3 — every polygonal cycle support is a circuit

#### Proof

Every vertex on the polygonal cycle has support degree two, and every other vertex has degree zero. Hence the support is cut-even by Theorem 3.5.

For `n=1`, there is no nonempty proper subset.

For `n\ge2`, let `A` be a nonempty proper subset of the cyclic edge set. Around the cyclic ordering there is a transition from an edge in `A` to an adjacent edge outside `A`. Their common vertex has exactly one incident edge from `A`, so `A` has nonempty boundary and is not cut-even. Thus the full support is inclusion-minimal. ∎

### Lemma 4.4 — every nonempty finite boundary-even support contains a polygonal cycle support

#### Proof

Let `F` be nonempty and boundary-even. Every active vertex of `G[F]` has positive even degree, hence degree at least two.

Choose a path in `G[F]` with pairwise distinct vertices and with as many vertices as possible. If the path consists of one vertex supporting a loop, that loop is already a polygonal cycle. Otherwise let `v` be an endpoint of the maximal path and let `e` be its last path edge. Since `\deg_F(v)\ge2`, there is an incident edge `e'\ne e`.

If `e'` is a loop at `v`, it is a one-edge polygonal cycle. Otherwise let its other endpoint be `w`. Maximality of the vertex-simple path forces `w` to be a vertex already on the path; otherwise the path could be extended. The edge `e'` together with the segment of the path from `w` to `v` forms a polygonal cycle support. If `w` is the preceding vertex, the result is the two parallel-edge case. ∎

### Theorem 4.5 — circuit characterization

For a finite support `C`, the following are equivalent:

1. `C` is a circuit;
2. `C` is a polygonal cycle support;
3. the support subgraph `G[C]` has exactly one edge-bearing connected component and every active vertex has degree two, with loops counted twice.

#### Proof

`(2) => (1)` is Lemma 4.3. A polygonal cycle plainly satisfies `(3)`.

Assume `(1)`. By Lemma 4.4, `C` contains a polygonal cycle support `C'`. By Lemma 4.3, `C'` is nonempty and cut-even. Inclusion-minimality of `C` forces `C'=C`, proving `(2)`.

Assume `(3)`. Start from any edge. Since every active vertex has degree two and the edge-bearing support is connected and finite, following the uniquely available continuation edge produces one closed polygonal cycle containing every edge; otherwise a vertex or edge outside that cycle would require a connection vertex of degree greater than two. Hence `(2)`. ∎

### Corollary 4.6 — exact small and degenerate circuits

- A singleton edge set is a circuit if and only if the edge is a loop.
- Two distinct parallel nonloop edges form a circuit.
- A single nonloop edge is never cut-even.
- Every circuit lies in one edge-bearing connected component.
- Isolated vertices belong to no circuit and do not affect circuit status.

### Proposition 4.7 — circuit containment and bridges

For a nonloop edge `e`, the following are equivalent:

1. `e` is not a bridge;
2. `e` lies in a circuit.

Consequently, a finite-active-edge multigraph has no singleton cut if and only if every nonloop edge lies in a circuit.

#### Proof

If `e` lies in a circuit, Theorem 4.5 gives an alternate path in the circuit between the endpoints of `e`, so deleting `e` does not disconnect them.

Conversely, if `e=uv` is not a bridge, there is a finite `u`-to-`v` path in `G-e`. Choose one of minimum length; it has no repeated vertex. Adding `e` gives a polygonal cycle support containing `e`, hence a circuit by Lemma 4.3. The final statement follows from Proposition 2.4. ∎

## 5. Indexed families, multisets, and exact coverage multiplicity

### Definition 5.1 — finite indexed support family

A finite indexed support family is a tuple

\[
\mathcal F=(F_i)_{i\in I},
\]

where `I` is a finite index set and each `F_i\subseteq E(G)` is a finite support.

The edge-coverage multiplicity is

\[
\mu_{\mathcal F}(e)
:=
|\{i\in I:e\in F_i\}|.
\]

Two indices remain distinct even when `F_i=F_j`. Thus an indexed family is the precise witness underlying a finite multiset of supports. Passing to multiset notation forgets index names, not occurrence multiplicity.

Empty supports are allowed. They contribute zero to every `\mu_{\mathcal F}(e)` and may arise naturally under projection.

### Definition 5.2 — even double cover and cycle double cover

A finite indexed family `\mathcal F=(F_i)_{i\in I}` is an **intrinsic even double cover** of `G` when:

1. every `F_i` is cut-even;
2. `\mu_{\mathcal F}(e)=2` for every active edge `e\in E(G)`.

It is a **cycle double cover** when:

1. every `F_i` is a circuit;
2. `\mu_{\mathcal F}(e)=2` for every active edge.

Repeated circuit occurrences are allowed and are sometimes necessary, most visibly for loops.

A cycle double cover is automatically an intrinsic even double cover. The converse existence implication requires the A9 memberwise circuit-decomposition theorem.

### Lemma 5.3 — reindexing invariance

If `\sigma:J\to I` is a bijection and `F'_j=F_{\sigma(j)}`, then

\[
\mu_{\mathcal F'}(e)=\mu_{\mathcal F}(e)
\]

for every edge. Hence even-double-cover and cycle-double-cover status depend only on the finite multiset of occurrences, not on chosen index names.

#### Proof

The bijection restricts to a bijection between the indices whose supports contain `e`. ∎

### Lemma 5.4 — concatenation

For disjoint finite index sets `I,J`, let `\mathcal F=(F_i)_{i\in I}` and `\mathcal H=(H_j)_{j\in J}`. Their concatenation satisfies

\[
\mu_{\mathcal F\sqcup\mathcal H}(e)
=
\mu_{\mathcal F}(e)+\mu_{\mathcal H}(e).
\]

This is the multiplicity rule used for componentwise assembly, memberwise decomposition, and loop reinsertion.

### Proposition 5.5 — componentwise assembly

Suppose `G` has finitely many edge-bearing connected components `G_1,\dots,G_r`. If each `G_k` has an even double cover (respectively cycle double cover), then concatenating the component families, regarded as supports of `G`, gives an even double cover (respectively cycle double cover) of `G`.

Conversely, restricting every occurrence of a cover of `G` to one component gives an even double cover of that component. For a cycle double cover, every circuit already lies in one component, so restriction simply selects the occurrences in that component.

#### Proof

Cut-evenness is componentwise by Corollary 3.7. An edge belongs to exactly one edge-bearing component, so its global multiplicity is its component multiplicity. Circuit locality follows from Theorem 4.5. ∎

## 6. Degenerate cases

### Proposition 6.1 — empty active graph

If `E(G)=\varnothing`, the empty indexed family is both an even double cover and a cycle double cover. It is the unique cover up to insertion or deletion of empty support occurrences.

#### Proof

There are no edge multiplicity conditions to check. Every listed support in the empty family vacuously has the required property. ∎

### Proposition 6.2 — isolated vertices

Adding or deleting isolated vertices changes no cut edge set, support parity, circuit, bridge, coverage multiplicity, even double cover, or cycle double cover.

#### Proof

No active edge has an isolated vertex as endpoint. Apply Lemma 2.2 and the definitions. ∎

### Proposition 6.3 — loop-only graph

Let every active edge of `G` be a loop. Then `G` has no singleton cut, every singleton loop support is a circuit, and the family containing two occurrences of `\{e\}` for each loop edge `e` is a cycle double cover.

#### Proof

Loops cross no cut, so every cut is empty. The circuit claim is Corollary 4.6. Exact double coverage is immediate from the indexed multiplicity definition. ∎

### Proposition 6.4 — one nonloop edge

A graph whose only active edge is one nonloop edge has a singleton cut and admits no even double cover or cycle double cover.

#### Proof

The cut separating its endpoints is the singleton edge. Any support occurrence containing the edge has odd boundary at both endpoints and therefore is not cut-even. Thus the edge cannot receive positive coverage multiplicity from cut-even supports. ∎

## 7. Dependency interfaces exported by A0

Downstream units may cite the following closed facts.

1. **Finite-active reduction:** all cut and parity questions reduce to the finite active vertex set.
2. **Intrinsic parity:** a finite support is cut-even exactly when every half-edge degree is even, with loops counted twice.
3. **Loopless API bridge:** on loopless graphs, intrinsic parity equals once-per-edge incidence parity; no such equality is asserted with loops.
4. **Circuit identity:** circuits are exactly connected 2-regular finite support subgraphs, equivalently loops, parallel-edge digons, and ordinary simple cycles.
5. **Bridge identity:** singleton cuts are exactly bridges, and a nonloop edge is nonbridging exactly when it lies in a circuit.
6. **Multiplicity:** indexed occurrences, not distinct support values, control edge coverage; equal and empty supports are allowed.
7. **Components:** parity and cover assembly are componentwise; isolated vertices are inert.
8. **Degenerate endpoint:** the empty graph and loop-only graphs have explicit CDCs.

## 8. Corpus mapping and correction boundary

This dossier consolidates and sharpens material distributed in the baseline chapters:

- `reduction/outer-shell-and-binary-flow.md` for active-edge finiteness, active vertices, cuts, components, loops, and parallel-edge conventions;
- `reduction/even-cover-and-collapse.md` for cut-even supports, circuits, indexed/multiset even covers, and loop behavior;
- `FORMAL_STATUS.md` for the distinction between the natural loop-aware theorem and the earlier loopless once-per-edge Lean checkpoint;
- `THEOREM_DEPENDENCY_MAP.md` and `MATHEMATICAL_ARCHITECTURE.md` for the downstream place of collapse, decomposition, and loop reinsertion.

No controlling claim is contradicted. The principal clarification is that the general mathematical vertex-parity object is half-edge boundary parity, not the current once-per-edge incidence predicate. The latter remains correct and sufficient on the loopless core.

## 9. Completion assessment

`AC-PD-A0` is `COMPLETE-DRAFT` because every foundational object, equivalence, multiplicity convention, component convention, and degenerate case required by its completion test has been stated and proved without external input.

The next dependency-respecting unit is `AC-PD-A1`: exact deletion of all loops, preservation of the no-singleton-cut hypothesis on the loopless core, lifting of core circuits back to the original graph, and reinsertion of exactly two singleton-loop circuit occurrences.
