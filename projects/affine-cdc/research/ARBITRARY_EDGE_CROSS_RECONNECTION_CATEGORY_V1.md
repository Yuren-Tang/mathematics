# Every prime cubic edge has a category-safe cross reconnection

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `93683934a95a6baa13cbb917ce5543982274b85c`.

**Parents:**

- the cyclic three-cut gluing theorem;
- `TYPE_T_PHYSICAL_COMMUTATION_ELIMINATION_V1.md`;
- `TYPE_H_PHYSICAL_COMMUTATION_ELIMINATION_V1.md`;
- the category-safe dipole cancellation lemmas used in the Tait and route-Tait peeling dossiers.

**Status:** exact graph-category theorem. Let `uv` be any edge of a connected bridgeless cubic loopless multigraph. Delete `u,v` and cross-reconnect their four remaining incidences. Unless the original graph already has a two-/three-/four-edge decomposition or a bounded acyclic/triangle degeneration, at least one cross reconnection is a connected bridgeless cubic multigraph with exactly two fewer vertices. Consequently every edge of a cyclically five-edge-connected prime graph admits a strict category-safe reduction suitable for vertex-minimal induction.

**Not implied:** root-valued inverse expansion across the deleted edge, elimination of equality/DDD full-channel locks, final global five-support theorem, canonical acceptance, independent audit, Lean verification, manuscript integration, release, or publication.

---

## 1. Edge smoothing setup

Let `G` be a finite connected bridgeless cubic loopless multigraph. Parallel edges are allowed.

Fix one edge

\[
e=uv.
\]

Write the other incidences of `u` as

\[
ua,\qquad ub
\]

and those of `v` as

\[
vc,\qquad vd.
\]

The outside endpoints `a,b,c,d` need not be distinct.

Delete `u,v` and their five incident edge interiors. Let

\[
H=G-\{u,v\}
\]

with four exposed incidences labelled `a,b,c,d` according to their old shores.

There are two cross matchings:

\[
M_0=ac\mid bd,
\qquad
M_1=ad\mid bc.
\]

For `k=0,1`, let

\[
G_k=H\cup M_k
\]

be the corresponding cross-reconnection graph whenever the two new edges are nonloops.

Every `G_k` is cubic and has

\[
\boxed{|V(G_k)|=|V(G)|-2.}
\]

---

## 2. Components of the deleted graph

### Lemma 2.1 — every outside component has at least two incidences

Every connected component of `H` is incident with at least two of the four exposed half-edges.

### Proof

If a component met exactly one exposed half-edge, the corresponding original edge from that component to `u` or `v` would be the unique edge connecting the component to the rest of `G`; it would be a bridge, contrary to hypothesis. ∎

### Corollary 2.2 — at most two outside components

The graph `H` has at most two connected components.

If it has two, each receives exactly two exposed incidences.

### Lemma 2.3 — disconnected outside gives a small decomposition

Suppose `H` has two components `A,B`.

- If both contain cycles, the two original attachment edges incident with either component form a cyclic edge cut of size two, or the four exposed incidences form an equivalent cyclic four-pole decomposition after restoring `u,v`.
- If one component is acyclic, it is a bounded tree appendage attached through two incidences.

Thus a prime cyclically five-edge-connected instance may assume

\[
\boxed{H\text{ connected}.}
\]

### Proof

By Corollary 2.2, each component has exactly two attachments to `{u,v}`. Removing those two original edges separates that component. If both shores contain cycles this is a cyclic cut of size two, hence already below the three-/four-cut gluing threshold. Otherwise the separated shore is acyclic. ∎

---

## 3. New reconnection edges are not bridges

Assume `H` connected and a chosen cross matching creates no loop.

### Lemma 3.1

Neither new reconnection edge of `G_k` is a bridge.

### Proof

Each new edge joins two vertices already connected by a path in `H`. Hence it lies on a cycle in `G_k`. ∎

---

## 4. An old bridge gives a three-cut

Assume `H` connected and let one old edge

\[
h\in E(H)
\]

be a bridge of `G_k`.

Write

\[
H-h=A\sqcup B.
\]

Since neither new edge crosses between `A,B`, every pair of the chosen cross matching lies entirely in one shore.

### Lemma 4.1 — shore distribution

Exactly one new reconnection edge lies in `A` and the other lies in `B`.

### Proof

If both new edges lay in `A`, then `B` would meet `{u,v}` through no exposed incidence or through only the old bridge `h`; in the original graph `h` would already be a bridge. The same holds with `A,B` exchanged. ∎

Therefore one exposed `u`-incidence and one exposed `v`-incidence lie in each shore.

### Theorem 4.2 — old bridge certificate

The edge `h` together with the two original attachment edges from one shore to `u,v` forms a three-edge cut in `G`.

If both shores contain cycles, it is a cyclic three-cut and the established gluing theorem applies. If one shore is acyclic, the configuration is a bounded appendage.

### Proof

For one shore, the only edges leaving it in the original graph are `h` and its one attachment to each of `u,v`. Removing these three edges separates the shore. ∎

### Corollary 4.3

If `G` has no cyclic three-cut and no bounded acyclic appendage, every nonloop cross reconnection `G_k` with connected `H` is bridgeless.

---

## 5. Coincident endpoints and loops

A cross reconnection creates a loop exactly when one paired outside endpoint is repeated, for example `a=c`.

Then the outside vertex `a` was adjacent to both `u` and `v`. Together with `uv`, the vertices `u,v,a` form a triangle, allowing parallel incidences when one of the remaining endpoints also coincides.

### Lemma 5.1 — loop degeneration

If one cross matching creates a loop, then exactly one of:

1. the other cross matching is loopless;
2. the triangle `uva` has a three-edge boundary and forms a bounded three-port neighbourhood;
3. a parallel-edge/two-port degeneration or an edge cut of size at most four is exposed.

### Proof

The triangle has three remaining incidences to the rest of the graph, counted with multiplicity. If they are distinct, they form its three-edge boundary. Further coincidences give a parallel-edge or two-port degeneration. If the alternative cross pairing does not pair equal endpoints, it is loopless. ∎

Thus loops never block both cross reconnections without simultaneously yielding an established bounded or small-cut exit.

---

## 6. Main category theorem

### Theorem 6.1 — arbitrary-edge cross reconnection

Let `G` be a connected bridgeless cubic loopless multigraph and let `uv` be any edge. At least one of the following holds.

1. One cross reconnection gives a connected bridgeless cubic multigraph `G'` with
   \[
   |V(G')|=|V(G)|-2.
   \]
2. `G` has a cyclic edge cut of size at most four.
3. `G` contains a bounded acyclic, triangle, loop, parallel-edge, or low-port degeneration.

### Proof

If `H=G-{u,v}` is disconnected, apply Lemma 2.3. Assume it is connected. Choose a loopless cross matching; if none exists, Lemma 5.1 gives Alternative 2 or 3. The resulting graph is connected. Its new edges are nonbridges by Lemma 3.1. Any old bridge gives a three-cut or bounded appendage by Theorem 4.2. Hence in the absence of Alternatives 2--3 the reconnection graph is bridgeless. ∎

### Corollary 6.2 — prime category-safe reduction

If `G` is cyclically five-edge-connected and has no bounded degeneration, then every edge `uv` admits at least one loopless cross reconnection producing a connected bridgeless cubic multigraph with two fewer vertices.

---

## 7. Inverse expansion interface

Let the two new reconnection edges of the smaller graph receive root values

\[
p,q\in R_5
\]

in an arbitrary five-support cover. Reinsert `u,v` and the edge `uv`. At both restored cubic vertices, conservation forces

\[
r=p+q
\]

on `uv`.

Exactly one of:

1. `p,q` are distinct and intersecting: `r` is a root and expansion succeeds;
2. `p=q`: `r=0`, the equality inverse-dipole cell;
3. `p,q` are disjoint: `r` is a co-root, the DDD inverse-dipole cell.

Thus the category theorem interfaces exactly with the established equality/DDD full-channel programme.

---

## 8. Trust boundary

### Exact here

- component structure of `G-{u,v}`;
- small-cut/acyclic outcome when the outside is disconnected;
- nonbridge status of new reconnection edges;
- three-cut extraction from every old bridge;
- loop/coincidence disposition;
- category-safe cross reconnection at an arbitrary edge;
- exact root/equality/DDD inverse-expansion interface.

### Still open

- invocation and audit of the complete equality/DDD inverse-lift consumer in the global minimal-counterexample proof;
- final closure theorem;
- independent mathematical audit;
- canonical acceptance, Lean verification, manuscript integration, release, publication;
- the global five-support theorem.
