# All three reconnection closures of a prime cubic edge are smaller soluble inputs

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `8b6297a2c6a03d149bd5072ea511c7f3fa49504f`.

**Parent:** `ARBITRARY_EDGE_CROSS_RECONNECTION_CATEGORY_V1.md`.

**Status:** exact simultaneous category theorem. In the notation obtained by deleting the endpoints of one cubic edge, the earlier bridge argument applies to every perfect matching of the four exposed incidences, not only to the two cross matchings. Hence, unless a cyclic cut of size at most four or a bounded loop/parallel/acyclic degeneration is already present, all three direct reconnection closures are connected bridgeless cubic multigraphs with two fewer vertices. This supplies the full three-reconnection hypothesis needed by the cap-profile forcing theorem at an arbitrary edge of a prime minimal counterexample.

**Not implied:** root-valued cap expansion, equality/DDD lock elimination, global five-support theorem, canonical acceptance, independent audit, Lean verification, manuscript integration, release, or publication.

---

## 1. Three terminal matchings

Use the notation of the cross-reconnection theorem. After deleting the endpoints `u,v` of one edge, the four exposed incidences are

\[
a,b\mid c,d,
\]

where `a,b` came from `u` and `c,d` from `v`.

The three perfect matchings are

\[
M_i=ab\mid cd,
\qquad
M_j=ac\mid bd,
\qquad
M_k=ad\mid bc.
\]

The last two are the cross reconnections. The first is the direct shore matching.

For each `r in {i,j,k}`, let

\[
G_r=H\cup M_r,
\qquad
H=G-\{u,v\}.
\]

Every loopless `G_r` is cubic and has two fewer vertices than `G`.

---

## 2. Connectedness

If `H` is disconnected, the component-incidence theorem from the parent dossier gives a cyclic cut of size at most four or a bounded acyclic appendage. Thus in the prime branch `H` is connected.

Adding any two matching edges to connected `H` preserves connectedness. Therefore every loopless `G_r` is connected.

---

## 3. New edges are never bridges

For any matching `M_r`, each new edge joins two vertices already connected by a path in `H`. Hence every new edge lies on a cycle in `G_r` and is not a bridge.

This argument is independent of whether the matching is direct or crossed.

---

## 4. Old bridges for an arbitrary matching

Suppose an old edge

\[
h\in E(H)
\]

is a bridge of `G_r`. Write

\[
H-h=A\sqcup B.
\]

Since no new matching edge crosses the partition, each of the two pairs of `M_r` lies entirely in one shore.

Neither shore can contain both matching pairs, because then the other shore would meet the original graph only through `h`, making `h` a bridge of `G`. Therefore one matching pair lies in `A` and one in `B`.

### Cross matchings

For `M_j` or `M_k`, each shore contains one old `u`-incidence and one old `v`-incidence. Thus one shore has exactly three leaving edges in `G`:

\[
h,\quad \text{one edge to }u,\quad \text{one edge to }v.
\]

### Direct matching

For `M_i=ab|cd`, one shore contains the pair `a,b` and hence the two old edges to `u`; the other contains `c,d` and the two old edges to `v`. Again one shore has exactly three leaving edges:

\[
h,\quad ua,\quad ub
\]

or

\[
h,\quad vc,\quad vd.
\]

### Theorem 4.1 — universal old-bridge certificate

For every one of the three matchings, an old bridge in `G_r` yields a three-edge cut in the original graph. If both shores contain cycles it is a cyclic three-cut; otherwise one shore is a bounded acyclic appendage.

Consequently, in the prime branch no `G_r` has an old bridge.

---

## 5. Loop coincidences

A matching edge becomes a loop only when its two exposed endpoints coincide. Such a coincidence means that one outside vertex was adjacent to two of the deleted incidences.

- If the coincident incidences came from opposite shores, `u,v` and the outside vertex form a triangle.
- If they came from the same shore, the original graph has a parallel pair or a two-port neighbourhood at `u` or `v`.

In either case the remaining incidences expose a three-/four-edge boundary, a parallel-edge degeneration, or a bounded theta/triangle base.

### Theorem 5.1 — simultaneous loop alternative

If any of the three reconnection closures contains a loop, then the original graph is already in an established bounded or small-cut branch. Therefore a prime minimal counterexample has all three reconnection closures loopless.

---

## 6. Simultaneous category theorem

### Theorem 6.1

Let `G` be a connected bridgeless cubic loopless multigraph and let `uv` be any edge. Exactly one of the following structural alternatives is available.

1. All three direct reconnection closures
   \[
   G_i,G_j,G_k
   \]
   are connected bridgeless cubic multigraphs with
   \[
   |V(G_r)|=|V(G)|-2.
   \]
2. `G` has a cyclic edge cut of size at most four.
3. `G` has a bounded acyclic, loop, parallel-edge, triangle, theta, or low-port degeneration.

### Corollary 6.2 — three soluble inputs in a minimal counterexample

Let `G` be a vertex-minimal counterexample after the established cut and bounded-base reductions. Then for every edge `uv`, all three reconnection graphs are valid smaller bridgeless cubic inputs and therefore have root-valued `E_5` flows by minimality.

Equivalently, for the complementary four-pole `P=G-{u,v}`, its complete physical profile satisfies

\[
\boxed{
\Sigma(P)\cap J_r\ne\varnothing
\qquad(r=i,j,k),}
\]

which is precisely the three-reconnection hypothesis of the fixed-route cap-blocking theorem.

---

## 7. Trust boundary

### Exact here

- extension of the bridge proof to the direct shore matching;
- connectedness and nonbridge status for all three closures;
- three-cut extraction from every old bridge for every matching;
- simultaneous loop/coincidence disposition;
- all-three-reconnection category theorem;
- exact interface with the three cap-profile sets `J_i,J_j,J_k`.

### Still open

- synthesis with equality/DDD full-channel elimination;
- final minimal-counterexample contradiction;
- independent mathematical audit;
- canonical acceptance, Lean verification, manuscript integration, release, publication;
- the global five-support theorem.
