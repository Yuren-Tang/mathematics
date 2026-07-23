# AC-PD-5CDC-R1 — one-cross structural reduction

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Standing issue:** `Yuren-Tang/research-workbench#37`  
**Owned branch:** `proof-development/affine-cdc-rigour-v1`  
**Triggering RL branch:** `research/affine-cdc-five-cdc-v1`  
**Controlling RL inputs:**

- `ONE_CROSS_RECONNECTION_EXISTENCE_V1.md`;
- `SIMPLE_EDGE_FIVE_SUPPORT_REDUCIBILITY_V1.md`;
- `FIVE_SUPPORT_GLOBAL_ONE_CROSS_CLOSURE_V6.md`;
- `ONE_CROSS_PROOF_DAG_AND_SUPERSESSION_INDEX_V3.md`.

**Classification:** `COMPLETE-DRAFT / R1 CLOSED / R2 ACTIVE`.

This dossier independently reconstructs the purely graph-theoretic half of the new five-support proof. It does not consume the RL statement as accepted mathematics.

---

## 1. Graph convention and terminal incidences

Let `G` be a finite connected loopless bridgeless cubic multigraph. Parallel edges are allowed. Let

\[
e=uv
\]

be a simple edge, meaning that it is the unique edge between `u` and `v`.

Write the two other edge incidences at `u` as `a,b` and the two other incidences at `v` as `c,d`. The letters denote labelled incidences, not necessarily four distinct exterior vertices. Let their exterior endpoints be

\[
x_a,x_b,x_c,x_d.
\]

Delete `u,v` and all five incident edges and denote the remaining graph by

\[
H=G-\{u,v\}.
\]

For the two cross pairings

\[
M_j=ac\mid bd,
\qquad
M_k=ad\mid bc,
\]

form `G_j,G_k` by adding one new edge for each paired incidence. If the two paired incidences have the same exterior endpoint, the new edge is a loop. Multiplicity is retained.

Every exterior vertex loses exactly the number of terminal incidences located there and receives exactly the same number of new incidences under either pairing. A new loop contributes two incidences. Hence both closures are cubic as multigraphs, possibly with loops, and

\[
|V(G_r)|=|V(G)|-2.
\]

---

## 2. Exterior component structure

### Lemma 2.1

Every connected component of `H` contains at least two of the four terminal incidences.

### Proof

Every component contains at least one terminal incidence because `G` is connected. If a component `C` contained exactly one terminal incidence, the corresponding original edge from `u` or `v` to `C` would be the only edge joining `C` to the rest of `G`; it would therefore be a bridge, contrary to the hypothesis. ∎

### Corollary 2.2

Exactly one of the following holds.

1. `H` is connected and contains all four terminal incidences.
2. `H` has exactly two components and each contains exactly two terminal incidences.

In the second case the component partition of the labelled incidences is one of

\[
ab\mid cd,
\qquad
ac\mid bd,
\qquad
ad\mid bc.
\]

---

## 3. Connectedness and the new edges

### Lemma 3.1

If `H` is connected, both cross closures are connected.

If `H` has two components, a cross closure is disconnected exactly when its matching is the component partition. Hence at least one of `G_j,G_k` joins the two exterior components by two new edges.

### Proof

The connected case is immediate. In the disconnected case each matching block is internal to a component exactly when the matching equals the component partition; otherwise both matching edges cross between the two components. ∎

### Lemma 3.2

Every nonloop new edge in a connected cross closure is nonbridging.

### Proof

If `H` is connected, the endpoints of the new edge are already joined by a path in `H`, so the new edge lies on a cycle.

If `H=C\sqcup D` and the selected matching joins the components, both new edges run from `C` to `D`. Internal paths in `C` and `D`, together with the other new edge, give a cycle containing the chosen new edge. ∎

### Lemma 3.3 — looplessness in the disconnected case

If `H` has two components, every cross matching that joins the components is loopless.

### Proof

The two endpoints of a joining matching edge lie in different components of `H` and therefore cannot be the same exterior vertex. ∎

This point is required for the simultaneous connected/loopless choice and is not supplied merely by the fact that the two closures cannot both contain loops.

---

## 4. Old edges when the exterior is disconnected

Assume `H=C\sqcup D` and the selected cross matching joins `C,D` by two edges.

### Lemma 4.1

No old edge of `H` is a bridge of the selected closure.

### Proof

It is enough to consider an edge `h` of `C` that is a bridge of `C`. Let the two shores of `C-h` be `C_0,C_1`.

The component `C` contains exactly two terminal incidences.

- If the terminals lie on opposite shores, each shore has one new edge to `D`. A path in `D` between the two new-edge endpoints gives a route from `C_0` to `C_1` avoiding `h`.
- If both terminals lie on one shore, the other shore has no terminal incidence. In the original graph `G` that shore meets the rest of the graph only through `h`, so `h` would be a bridge of `G`, impossible.

Thus `h` is bypassed. The same argument applies in `D`. ∎

### Proposition 4.2

If `H` is disconnected, at least one cross closure is connected, loopless, bridgeless, cubic, and has two fewer vertices.

### Proof

Choose a matching different from the component partition. By Lemma 3.1 it joins the components, by Lemma 3.3 it is loopless, by Lemma 3.2 its new edges are nonbridges, and by Lemma 4.1 its old edges are nonbridges. Cubicity and the vertex count were established in Section 1. ∎

---

## 5. Old bridges when the exterior is connected

Assume now that `H` is connected.

### Lemma 5.1 — terminal split criterion

If an old edge `h\in E(H)` is a bridge of `G_r`, then:

1. `h` is a bridge of `H`;
2. each shore of `H-h` contains terminal incidences;
3. the two shores contain exactly the two matching blocks of `M_r`.

### Proof

If `H-h` were connected, adding matching edges could not make `h` a bridge. Thus `h` is a bridge of `H`.

If one shore contained no terminal incidence, that shore would also meet the rest of the original graph `G` only through `h`, making `h` a bridge of `G`. Hence both shores contain terminals.

For `h` to remain a bridge after the two matching edges are added, neither new edge may cross the shores. Therefore each matching pair lies in one shore. Since both shores are nonempty in terminal incidences, one matching block lies in each shore. ∎

### Lemma 5.2 — compatibility of bridge splits

The labelled terminal bipartitions induced by two bridges of the connected graph `H` are compatible: at least one of the four intersections of the two pairs of shores is empty.

### Proof

Contract each two-edge-connected block of `H`. The bridges become the edges of a tree. The vertex bipartitions induced by two tree edges are nested or disjoint, hence compatible. Restricting the shores to the four labelled terminal incidences preserves compatibility. ∎

The cross partitions

\[
ac\mid bd,
\qquad
ad\mid bc
\]

are crossing: each of the four intersections contains one labelled incidence. Therefore they cannot both be induced by bridge cuts of `H`.

### Corollary 5.3

When `H` is connected, at most one of `G_j,G_k` has an old bridge.

---

## 6. Loop cases

### Lemma 6.1

The two cross closures cannot both contain loops.

### Proof

A loop in `M_j` and a loop in `M_k` force at least three of `a,b,c,d` to have the same exterior endpoint `x`. The three corresponding original edges exhaust the cubic degree of `x`. The remaining fourth terminal edge is then the unique edge leaving the vertex set `\{u,v,x\}`, hence is a bridge of `G`, contradiction. ∎

### Lemma 6.2 — the opposite closure is safe

Suppose one cross closure contains a loop. Then the other closure is loopless and has no old bridge.

### Proof

It is loopless by Lemma 6.1. Suppose, for example, that `x_a=x_c`, so the pair `ac` creates a loop in `G_j`; the opposite matching is `M_k=ad\mid bc` and separates the labelled incidences `a,c`.

- If `H` is connected, an old bridge of `G_k` would, by Lemma 5.1, induce the split `ad\mid bc`. This is impossible because two incidences based at the same vertex `x_a=x_c` cannot lie on opposite shores of `H-h`.
- If `H` is disconnected, `a,c` lie in the same exterior component. Hence the component partition cannot equal `ad\mid bc`, which separates them. Thus `M_k` joins the two components, and Lemma 4.1 excludes old bridges.

The other coincident-pair cases are identical. ∎

### Proposition 6.3

If `H` is connected, one of `G_j,G_k` is connected, loopless and bridgeless.

### Proof

Both closures are connected.

- If neither has a loop, Corollary 5.3 supplies one with no old bridge; Lemma 3.2 handles its new edges.
- If one has a loop, Lemma 6.2 shows that the other is loopless and has no old bridge; Lemma 3.2 again handles its new edges.

Both-loop is impossible by Lemma 6.1. ∎

---

## 7. One-cross survival theorem

### Theorem 7.1

Let `G` be a finite connected loopless bridgeless cubic multigraph and let `uv` be a simple edge. Of the two cross reconnection closures obtained after deleting `u,v`, at least one is a finite connected loopless bridgeless cubic multigraph and satisfies

\[
\boxed{|V(G_r)|=|V(G)|-2.}
\]

### Proof

Use Proposition 4.2 when `H` is disconnected and Proposition 6.3 when `H` is connected. ∎

---

## 8. Theta is the only no-simple-edge base

### Lemma 8.1

A connected loopless cubic multigraph with no simple edge is the two-vertex theta multigraph with three parallel edges.

### Proof

At a vertex `v`, every adjacent vertex is joined to `v` with multiplicity at least two. Cubic degree therefore permits only one neighbour: two distinct neighbours would contribute degree at least four. Hence all three incident edges join one neighbour. The two vertices form a whole connected component, and connectedness forces the graph to be exactly theta. ∎

Theta has the explicit root triangle `12,13,23`.

---

## 9. Exact consequence and boundary

The graph-theoretic induction skeleton is now rigorous:

1. theta is the base;
2. every non-theta connected loopless cubic multigraph has a simple edge;
3. that edge admits a valid smaller cross closure.

Therefore the complete cubic five-support theorem reduces exactly to the remaining extension statement:

\[
\boxed{
\text{every root-valued flow on the selected valid cross closure extends across the deleted edge.}
}
\]

This dossier proves no part of that extension statement. In particular it does not accept the singular-carrier, projectivity, Petersen recurrence, source-movie or finite-condensation hypotheses.

**Result:** `R1 CLOSED`; `R2` remains the unique load-bearing mathematical frontier of the compressed proof.