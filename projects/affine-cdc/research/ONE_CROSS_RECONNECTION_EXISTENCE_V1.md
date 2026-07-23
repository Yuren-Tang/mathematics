# One cross reconnection always survives at a simple cubic edge

## Research Lead structural theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `85702cd4e36191182c124f07a56ed162480f71e6`.

**Purpose:** replace all-three reconnection plus low-cut reduction by the weakest input actually needed for cap restoration: one smaller root-soluble cross reconnection.

**Status:** exact authorial graph theorem. It uses only connectedness, bridgelessness, cubic degree, and laminarity of bridge cuts. PDL must independently verify the repeated-terminal incidence cases.

---

## 1. Simple edge and its four incidences

Let `G` be a finite connected loopless bridgeless cubic multigraph. Let

\[
uv\in E(G)
\]

be a **simple edge**, meaning that it is the only edge joining `u` and `v`.

The other two incidences at `u` are

\[
a,b,
\]

and the other two incidences at `v` are

\[
c,d.
\]

These are labelled incidences; two labels may have the same exterior endpoint.

Delete `u,v` and put

\[
H=G-\{u,v\}.
\]

The two cross matchings are

\[
M_j=ac\mid bd,
\qquad
M_k=ad\mid bc.
\]

Let

\[
G_j=H\cup M_j,
\qquad
G_k=H\cup M_k.
\]

Each loopless closure is cubic and has two fewer vertices than `G`.

---

## 2. Components of the exterior

Every connected component of `H` contains at least one terminal incidence because `G` is connected.

No component contains exactly one terminal incidence, since the corresponding edge to `u` or `v` would be a bridge of `G`.

Hence exactly one of:

1. `H` is connected;
2. `H` has exactly two components, each containing exactly two terminal incidences.

In the second case the component terminal partition is one of the three perfect matchings of

\[
\{a,b,c,d\}.
\]

### Lemma 2.1 — one cross matching connects the exterior

If `H` is disconnected, at most one of `M_j,M_k` equals its component partition. The other cross matching joins the two exterior components by two edges and therefore produces a connected closure.

If `H` is connected, both cross closures are connected.

Thus at least one cross closure is connected.

---

## 3. New cross edges are nonbridges

### Connected exterior

If `H` is connected and a new cross edge has distinct endpoints, those endpoints are already joined by a path in `H`. The new edge lies on a cycle.

### Two-component exterior

If `H` has two components and the selected cross matching joins them, both new edges run between the two components. Deleting either one leaves the other as a connection; internal paths between the two terminal endpoints in each component complete a cycle.

### Lemma 3.1

Every nonloop cross edge in a connected cross closure is nonbridging.

---

## 4. Old bridges when the exterior is connected

Assume `H` connected. Suppose an old edge

\[
h\in E(H)
\]

is a bridge of `G_r`, where `r=j` or `k`.

Then `h` is a bridge of `H`, and the two shores of

\[
H-h
\]

contain the terminal incidences in exactly the two matching blocks of `M_r`. Otherwise one new matching edge would cross the shores and bypass `h`.

Thus every old bridge of `G_r` determines the terminal bipartition `M_r` as a bridge cut of `H`.

### Lemma 4.1 — bridge cuts are laminar

The terminal bipartitions induced by two bridges of one connected graph are compatible: one of the four intersections of their shores is empty.

### Proof

Contract every two-edge-connected block of `H`. The bridges form the edges of a tree. Bipartitions induced by two tree edges are nested or disjoint and therefore compatible. ∎

The two cross matchings

\[
M_j=ac\mid bd,
\qquad
M_k=ad\mid bc
\]

are crossing bipartitions: all four pairwise shore intersections contain one terminal incidence.

### Corollary 4.2 — both cross closures cannot have old bridges

If `H` is connected, at most one of `G_j,G_k` contains an old bridge.

---

## 5. Old bridges when the exterior is disconnected

Assume `H=C\sqcup D`, with two terminals in each component, and choose the cross matching that joins `C` to `D` by two new edges.

Let `h` be an old edge in `C`.

- If the two terminals of `C` lie on opposite shores of `C-h`, the two new cross edges and a path through `D` bypass `h`.
- If both terminals lie on one shore, the other shore has no terminal incidence and meets the original graph `G` only through `h`, making `h` a bridge of `G`.

The second alternative is impossible.

### Lemma 5.1

Every cross closure that joins the two components of a disconnected exterior has no old bridge.

---

## 6. Loop incompatibilities

A cross closure has a loop exactly when one of its matched incidence pairs has the same exterior endpoint.

### Lemma 6.1 — both cross closures cannot have loops

If both `M_j` and `M_k` contain a coincident-endpoint pair, at least three of the four terminal incidences have one common exterior endpoint `x`.

The three corresponding edges from `u,v` exhaust the cubic degree of `x`. The remaining fourth terminal edge is then the only edge leaving the subgraph on `u,v,x`, and is a bridge of `G`, contradiction.

### Lemma 6.2 — a loop in one cross matching excludes an old bridge in the other

Suppose, for example, `a,c` have the same exterior endpoint, so `M_j` contains a loop.

The other cross partition is

\[
M_k=ad\mid bc.
\]

It places the incidences `a` and `c` in opposite shores. No bridge cut of `H` can separate two incidences at the same vertex. Hence `G_k` cannot have an old bridge induced by partition `M_k`.

The same argument applies to every coincident pair.

---

## 7. One-cross survival theorem

### Theorem 7.1

Let `G` be a finite connected loopless bridgeless cubic multigraph and let `uv` be a simple edge. Then at least one of the two cross reconnection closures

\[
G_j,
\qquad G_k
\]

is a connected loopless bridgeless cubic multigraph with

\[
\boxed{|V(G_r)|=|V(G)|-2.}
\]

### Proof

- At least one cross matching gives a connected closure by Lemma 2.1.
- New nonloop edges are nonbridges by Lemma 3.1.
- If `H` is disconnected, every connecting cross closure has no old bridge by Lemma 5.1.
- If `H` is connected, both cross closures cannot have old bridges by Corollary 4.2.
- Both cannot have loops by Lemma 6.1.
- If one has a loop, the other cannot have an old bridge by Lemma 6.2 and is connected by the component analysis.

Therefore one cross closure is simultaneously connected, loopless, and bridgeless. ∎

---

## 8. Existence of a simple edge

### Lemma 8.1

Every connected loopless cubic multigraph with more than two vertices has a simple edge.

### Proof

If no edge were simple, every adjacency would have multiplicity at least two. At a cubic vertex this leaves only two possibilities:

1. all three incident edges join one neighbour, giving a two-vertex triple-edge component;
2. two edges join one neighbour and the third joins another, but that third edge is simple, contradiction.

Connectedness therefore forces the whole graph to be the two-vertex theta multigraph. ∎

The theta multigraph has an explicit root flow. Hence every nontrivial minimal counterexample has a simple edge to which Theorem 7.1 applies.

---

## 9. Minimal-counterexample consequence

Let `G` be a vertex-minimal connected loopless bridgeless cubic counterexample other than the theta base. Choose a simple edge `uv`.

Theorem 7.1 supplies one smaller connected loopless bridgeless cross closure

\[
G_r.
\]

Minimality gives a root-valued `E_5` flow on `G_r`.

Thus the cap-restoration proof needs only one cross flow. It does not require:

- cyclic two-cut gluing;
- cyclic three-cut gluing;
- all three reconnection closures;
- cyclic four-cut gluing;
- Type T or Type H mismatch elimination.

---

## 10. PDL obligations

PDL should independently verify:

1. the component count of `H`;
2. nonbridge status of new edges in both exterior cases;
3. the bridge-cut terminal partition criterion;
4. laminarity of bridge cuts;
5. incompatibility of the two cross partitions;
6. the loop/bridge incidence arguments;
7. existence of a simple edge outside the theta base.

These are elementary graph lemmas and replace the complete low-cut reconnection package in the controlling proof.

---

## 11. Trust boundary

### Exact authorial claim

- one of the two cross reconnections at every simple cubic edge is a valid smaller bridgeless cubic graph;
- no prior two-, three-, or four-cut reduction is required;
- every non-theta connected cubic multigraph has a simple edge.

### Not claimed

- independent verification;
- cap restoration from the one cross flow;
- canonical acceptance, Lean verification, manuscript integration, release, peer review, or publication.
