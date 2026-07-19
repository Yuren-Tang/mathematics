# AC-PD-A2 — exact loopless cubic port-cycle expansion and collapse data

**Proof-development state:** `COMPLETE-DRAFT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Depends on:** `AC-PD-A0`, `AC-PD-A1`  
**Immediate consumers:** `AC-PD-A3`, `AC-PD-A4`, `AC-PD-A8`  
**External mathematical inputs:** none

## 0. Theorem package

Let `G` be a loopless multigraph with finite active edge set and no singleton cut. This unit constructs a finite loopless cubic multigraph `H` together with exact collapse data

\[
\pi:V(H)\to V(G),
\qquad
\lambda:E(G)\hookrightarrow E(H),
\]

such that:

- active fibres of `\pi` are port cycles;
- all inter-fibre edges are exactly the lifted original edges;
- all auxiliary edges lie inside fibres;
- degree-two fibres use two distinct parallel auxiliary edge objects;
- edge-bearing connected components correspond exactly;
- `H` has no singleton cut;
- `|V(H)|=2|E(G)|` and `|E(H)|=3|E(G)|`;
- collapsing every active fibre recovers the active part of `G` exactly.

No flow theorem is used. The binary-flow input begins only in `AC-PD-A3`.

## 1. Incidence ports and degree cases

For a vertex `v`, define the loopless incidence set

\[
\operatorname{Inc}_G(v):=\{e\in E(G):v\text{ is an endpoint of }e\}.
\]

Because `G` is loopless, each edge occurs in the incidence sets of exactly two distinct vertices.

### Lemma 1.1 — active degrees

Every active vertex has finite degree at least two.

#### Proof

Finiteness follows from `\operatorname{Inc}_G(v)\subseteq E(G)`. If an active vertex `v` had degree one with unique incident edge `e`, then

\[
\delta_G(\{v\})=\{e\},
\]

contrary to the no-singleton-cut hypothesis. ∎

Thus the only fibre cases are:

- degree zero: no port and an empty fibre;
- degree two: two ports and two distinct parallel internal edges;
- degree at least three: an ordinary cycle on the ports.

In particular, no degree-one fibre is created and no auxiliary loop is required.

## 2. Choice of cyclic orders

For each active vertex `v`, choose a cyclic permutation

\[
\sigma_v:\operatorname{Inc}_G(v)\to\operatorname{Inc}_G(v)
\]

consisting of one cycle. Such a choice exists because the finite incidence set has cardinality at least two.

The construction is noncanonical but entirely local. Choices at different vertices are independent.

## 3. Construction of the expanded graph

### Vertices

Define

\[
V(H):=\{(v,e):v\in V_+(G),\ e\in\operatorname{Inc}_G(v)\}.
\]

The vertex `(v,e)` is the port at `v` belonging to original edge `e`.

### External edges

For every original edge object `e=uv`, create one new edge object `\lambda(e)` with endpoints

\[
(u,e),\qquad (v,e).
\]

Because `G` is loopless, these endpoints lie in distinct fibres.

### Internal edges

For every active vertex `v` and every port edge label `e\in\operatorname{Inc}_G(v)`, create an internal edge object

\[
a_{v,e}
\]

joining

\[
(v,e)
\quad\text{to}\quad
(v,\sigma_v(e)).
\]

The internal edge objects are indexed by the source ports and therefore remain distinct even when they have the same endpoints.

When `\deg_G(v)=2`, the cyclic permutation swaps the two incidence labels. The two objects `a_{v,e_1}` and `a_{v,e_2}` consequently have the same endpoint pair but are distinct parallel edges. When `\deg_G(v)\ge3`, the internal edges form the ordinary simple cycle associated with `\sigma_v`.

### Collapse map

Define

\[
\pi:V(H)\to V(G),
\qquad
\pi(v,e)=v.
\]

An isolated vertex of `G` has empty inverse image. Surjectivity is neither required nor true in general.

## 4. Exact edge partition and collapse laws

Let

\[
E_{\mathrm{ext}}(H):=\lambda(E(G)),
\qquad
E_{\mathrm{int}}(H):=\{a_{v,e}:v\in V_+(G),\ e\in\operatorname{Inc}_G(v)\}.
\]

### Proposition 4.1 — edge partition

\[
E(H)=E_{\mathrm{ext}}(H)\sqcup E_{\mathrm{int}}(H).
\]

The map `\lambda` is injective. Every external edge joins two distinct `\pi`-fibres, and every internal edge lies in one `\pi`-fibre.

#### Proof

The two classes are created with disjoint edge-object tags. Original edge objects index the external class, so `\lambda` is injective. Endpoint definitions give the fibre assertions. ∎

### Proposition 4.2 — every inter-fibre edge is original

If an edge of `H` has endpoints in distinct `\pi`-fibres, it is `\lambda(e)` for a unique `e\in E(G)`.

#### Proof

Internal edges have both endpoints over one vertex. Hence an inter-fibre edge is external, and uniqueness follows from injectivity of `\lambda`. ∎

### Proposition 4.3 — endpoint preservation

If an original edge `e` has endpoints `u,v`, then `\lambda(e)` has endpoints in `\pi^{-1}(u)` and `\pi^{-1}(v)`. Conversely, every edge joining those distinct fibres and corresponding to that original edge is `\lambda(e)`.

### Proposition 4.4 — fibre shape

For every vertex `v`:

- if `v` is isolated, `\pi^{-1}(v)=\varnothing`;
- if `v` is active of degree `d\ge2`, the induced internal fibre is a polygonal cycle of length `d`, with `d=2` interpreted as two distinct parallel edges.

In particular every active fibre is connected.

## 5. Finiteness, cubicity, and looplessness

### Theorem 5.1 — exact expansion structure

The graph `H` is finite-active-edge, loopless, and cubic.

#### Proof

There is one port for each incidence of an original loopless edge. Since each original edge has two distinct endpoint incidences,

\[
|V(H)|
=
\sum_{v\in V_+(G)}\deg_G(v)
=
2|E(G)|.
\]

At a port `(v,e)`:

- exactly one external edge, namely `\lambda(e)`, is incident;
- exactly two internal edge objects are incident, namely `a_{v,e}` and `a_{v,\sigma_v^{-1}(e)}`.

When the fibre has degree two these are the two distinct parallel internal edges. Thus every vertex of `H` has degree three.

An external edge has endpoints over the two distinct endpoints of a loopless original edge, so it is not a loop. An internal edge joins two distinct ports because every cyclic permutation on a set of size at least two has no fixed point when it is one cycle. Hence `H` is loopless.

Both vertex and edge sets are finite because they are indexed by finitely many original incidences. ∎

### Corollary 5.2 — exact size formulae

\[
\boxed{
|V(H)|=2|E(G)|,
\qquad
|E(H)|=3|E(G)|.
}
\]

#### Proof

The vertex formula was proved above. There is one external edge per original edge. There is one internal edge per incidence port, hence `2|E(G)|` internal edges. Therefore

\[
|E(H)|=|E(G)|+2|E(G)|=3|E(G)|.
\]

The formula includes the empty graph case. ∎

## 6. Connected components

### Theorem 6.1 — edge-bearing component correspondence

The map `\pi` induces a bijection between the edge-bearing connected components of `H` and those of `G`.

More precisely, if `C` is an edge-bearing component of `G`, then the subgraph of `H` consisting of all ports over vertices of `C`, all internal edges in those fibres, and all lifted edges of `E(C)` is connected; these subgraphs are exactly the edge-bearing components of `H`.

#### Proof

No edge of `H` joins fibres over distinct components of `G`: an internal edge stays in one fibre, while an external edge lifts an original edge and therefore stays over one original component.

Conversely, let `u,v` be active vertices in one component of `G`. Choose a finite original path from `u` to `v`. Lift its edges externally. At each path vertex, the endpoints of successive lifted edges lie in one connected fibre cycle, so they can be joined by an internal fibre path. The same fibre connectivity joins any chosen port over `u` or `v` to the lifted path. Hence all ports and edges over the original component lie in one connected component of `H`. ∎

Isolated vertices of `G` have empty fibres and therefore no corresponding component in the active expanded graph.

## 7. Preservation of the no-singleton-cut condition

### Lemma 7.1 — internal edges are nonbridges

Every internal edge of `H` has an alternate path between its endpoints avoiding that edge.

#### Proof

An internal edge lies on its fibre cycle. If the fibre has length at least three, the complementary arc of the cycle is an alternate path. In a degree-two fibre, the other parallel internal edge is the alternate path. ∎

### Lemma 7.2 — external edges are nonbridges

Every external edge `\lambda(e)` has an alternate path between its endpoints avoiding `\lambda(e)`.

#### Proof

Let the original nonloop edge be `e=uv`. Since `G` has no singleton cut, A0 Proposition 4.7 implies that `e` is not a bridge. Hence there is a finite `u`-to-`v` path

\[
P=(e_1,\dots,e_k)
\]

in `G-e`.

Lift every `e_i` to `\lambda(e_i)`. At `u`, join the port `(u,e)` to the port of `e_1` by a path inside the connected fibre over `u`. At each internal vertex of `P`, join the incoming and outgoing ports by a fibre path. At `v`, join the final path port to `(v,e)` inside the fibre over `v`.

Concatenating these fibre paths and lifted external edges gives a walk between the endpoints of `\lambda(e)` that does not use `\lambda(e)`. Removing closed subwalks if necessary gives an alternate path. ∎

### Theorem 7.3 — bridgelessness of the expansion

`H` has no singleton cut.

#### Proof

By Lemmas 7.1 and 7.2, no edge of `H` is a bridge. By A0 Proposition 2.4, `H` has no singleton cut. ∎

No connectedness hypothesis was used. The argument applies independently on every edge-bearing component.

## 8. Exact collapse recovery

Contract every active fibre cycle `\pi^{-1}(v)` to one vertex labelled `v` and delete the internal edge objects. Under this operation:

- each external edge `\lambda(e)` becomes one edge with the same endpoint multiset as `e`;
- distinct original edge objects remain distinct because `\lambda` is injective;
- no other inter-fibre edge survives;
- isolated vertices of `G` may be adjoined afterward as empty fibres.

### Theorem 8.1 — recovery of the active original graph

The quotient active graph obtained from `H` by collapsing all active fibres and deleting internal edges is canonically isomorphic to `G[V_+(G),E(G)]`, the original graph with isolated vertices omitted. Re-adjoining the isolated vertex carrier recovers `G` exactly.

#### Proof

Propositions 4.1–4.3 identify the surviving edge set bijectively with `E(G)` and preserve every endpoint pair. Fibre labels identify quotient vertices with `V_+(G)`. ∎

## 9. Cut pullback identity exported for A8

Although the parity proof belongs to `AC-PD-A8`, the structural set identity follows already from the collapse laws.

### Proposition 9.1 — cut pullback

For every `S\subseteq V(G)` and every original edge `e`,

\[
\boxed{
e\in\delta_G(S)
\iff
\lambda(e)\in\delta_H(\pi^{-1}(S)).
}
\]

Moreover no internal edge belongs to `\delta_H(\pi^{-1}(S))`.

#### Proof

The endpoints of `\lambda(e)` lie over the endpoints of `e`, so exactly one lies in `\pi^{-1}(S)` exactly when exactly one original endpoint lies in `S`. Both endpoints of an internal edge have the same `\pi`-image and therefore lie on the same side. ∎

Hence `\lambda` restricts to a bijection

\[
\delta_G(S)
\xrightarrow{\sim}
\delta_H(\pi^{-1}(S)).
\]

This statement does not yet mention support parity or cover multiplicity.

## 10. Degenerate and boundary cases

### Empty active graph

If `E(G)=\varnothing`, then `V(H)=E(H)=\varnothing`, both size formulae hold, and the no-singleton-cut condition is vacuous.

### Degree two

The internal fibre consists of two distinct parallel edge objects. Treating it as one edge would make the ports degree two rather than cubic and would destroy the exact edge count; treating it as a loop would violate looplessness. The two-object convention is forced.

### Degree three

The fibre is a triangle, not an identity gadget. This keeps every expanded vertex equal to an incidence port and makes the construction uniform in all degrees.

### Disconnected graph

Components are neither joined nor supplied with artificial connector edges. Component correspondence is exact by Theorem 6.1.

### Parallel original edges

Distinct original edge objects yield distinct external edges even when their endpoint pairs coincide. Their ports are also distinct because ports are indexed by edge objects.

### Isolated vertices

They have empty fibres and do not affect active finiteness, cuts, cubicity, components, or collapse. Surjectivity of `\pi` is intentionally absent.

## 11. Exported interface

Downstream units may cite:

1. existence of arbitrary local cyclic orders on all active incidence sets;
2. the exact finite loopless cubic graph `H`;
3. injective original-edge lift `\lambda` and vertex collapse map `\pi`;
4. the external/internal edge partition and complete inter-fibre-edge characterization;
5. connected port-cycle fibres, including the degree-two parallel case;
6. exact size formulae;
7. edge-bearing component correspondence;
8. preservation of the no-singleton-cut condition;
9. exact recovery of the original active graph under collapse;
10. the cut pullback bijection for `\pi^{-1}(S)`.

## 12. Corpus mapping and assurance

This dossier expands Theorems 3.1 and 3.2 of `reduction/outer-shell-and-binary-flow.md` into a closed dependency interface. It uses the A0 bridge/circuit semantics and A1 loopless reduction but no Seymour, Tutte, affine, or finite-computation input.

The construction is mathematical paper proof, not a Lean mutation. No controlling contradiction or source gap was found.

## 13. Completion assessment

`AC-PD-A2` is `COMPLETE-DRAFT`. The next dependency-respecting unit is `AC-PD-A3`, the exact `BinaryEightFlow` external boundary: componentwise finite reduction, Seymour's nowhere-zero six-flow theorem, literal conversion to an integer eight-flow, Tutte's equal-order group-flow existence theorem, characteristic-two orientation forgetting, and exact primary source localization.
