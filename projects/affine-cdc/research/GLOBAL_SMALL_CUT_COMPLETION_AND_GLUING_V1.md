# Two-, three-, and four-cut completions are exact smaller bridgeless inputs

## Research dossier v1 — global cut-interface hardening

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `5f837f2067d7340dc0429c6ecaa35083166cd3c4`.

**Parents:**

- `five-support/cuts-four-poles-and-routing.md`;
- `TYPE_T_PHYSICAL_COMMUTATION_ELIMINATION_V1.md`;
- `TYPE_H_PHYSICAL_COMMUTATION_ELIMINATION_V1.md`;
- `FOUR_POLE_CAP_LIBRARY_TEN_STATE_PROFILES_V1.md`;
- `FIVE_SUPPORT_GLOBAL_MINIMAL_COUNTEREXAMPLE_CLOSURE_V1.md`;
- `GLOBAL_CAP_LIFT_INTERFACE_COMPATIBILITY_V1.md`.

**Status:** exact graph-category and gluing theorem for every cut of size at most four used by the final minimal-counterexample proof. A connected acyclic cubic shore with `k` boundary semiedges has exactly `k-2` vertices. Hence every noncyclic three-/four-cut shore is the explicit one-vertex or two-vertex bounded gadget, and a nonempty two-cut shore is automatically cyclic. For a proper cyclic shore, the standard two-, three-, or four-cap completion is connected, bridgeless, cubic, and strictly smaller. Minimality therefore applies exactly. Two- and three-cut boundary flows align by one global support permutation. Four-cut failure would give a pair of disjoint cap-forced physical profiles; the exact finite classification leaves only Type T or Type H, both eliminated by disjoint-support route invariance.

**Not implied:** independent verification of the imported finite mismatch classification, canonical acceptance, Lean verification, manuscript integration, release, publication, or DOI status.

---

## 1. Cubic shore degree formula

Let `P` be a connected shore of a finite cubic graph. Regard every cut edge leaving `P` as one boundary semiedge. Let

\[
k=|\partial P|
\]

and let

\[
n=|V(P)|,
\qquad
m=|E(P)|
\]

count internal vertices and internal edges.

Cubic degree counting gives

\[
\boxed{3n=2m+k.}
\]

If `P` is acyclic, then

\[
m=n-1.
\]

Therefore

\[
3n=2n-2+k
\]

and hence

\[
\boxed{n=k-2.}
\]

### Theorem 1.1 — complete acyclic low-port classification

A nonempty connected acyclic cubic shore with at most four boundary semiedges is exactly one of:

1. `k=3`, `n=1`: one cubic vertex with three boundary semiedges;
2. `k=4`, `n=2`: two cubic vertices joined by one internal edge, with two boundary semiedges at each vertex.

There is no nonempty connected acyclic cubic shore with `k=2`.

### Proof

The formula `n=k-2` gives `n=0,1,2` for `k=2,3,4`. The `n=1` and `n=2` tree types are unique under cubic degree. ∎

The four-port acyclic shore is precisely a standard two-vertex cap. Thus every low-port acyclic exit is an explicit bounded gadget, not an unbounded residual category.

---

## 2. Connectedness of small-cut shores

Let `G` be connected and bridgeless. Every connected component of a proper shore has at least two cut edges leaving it; a component with exactly one leaving edge would make that edge a bridge of `G`.

### Two-edge cut

A shore of a two-edge cut has only one component and is connected.

### Three-edge cut

A disconnected shore would have at least two components and hence at least four leaving edges, impossible. Thus it is connected.

### Four-edge cut

A disconnected shore has exactly two components, each incident with exactly two cut edges. By Theorem 1.1 neither component is acyclic. Hence each contains a cycle and each itself defines a cyclic two-edge cut.

Consequently, after cyclic two-cut reduction, every shore of a remaining cyclic four-edge cut is connected.

### Proposition 2.1

In the cut order used by the minimal-counterexample proof:

1. every two-cut shore is connected;
2. every three-cut shore is connected;
3. after two-cut reduction, every cyclic four-cut shore is connected.

---

## 3. Cyclic two-edge-cut completion

Let a two-edge cut separate connected shores `P,Q`. By Theorem 1.1 every nonempty shore contains a cycle.

Let the two boundary semiedges of `P` be incident with vertices `x,y`.

### Lemma 3.1 — distinct boundary vertices

\[
x\ne y.
\]

### Proof

If both cut edges meet one vertex `x`, then `x` has exactly one internal incident edge `h`. Since `P` contains a cycle, `P-x` is nonempty. The edge `h` is the only connection of `P-x` to the rest of `G`, hence is a bridge, contradiction. ∎

Complete `P` by adding one edge

\[
xy.
\]

Call the completed graph `P^+`.

### Theorem 3.2 — two-cut completion category

`P^+` is connected, loopless, cubic, bridgeless, and has fewer vertices than `G`.

### Proof

Connectedness and cubicity are immediate, and `x != y` excludes a loop. The new edge lies on a cycle because `P` contains an `x-y` path.

Suppose an old edge `h` is a bridge of `P^+`. In `P-h`, the two boundary vertices cannot lie in different components, because the new edge would reconnect them. Thus one component of `P-h` contains neither boundary vertex. In the original graph that component meets the rest only through `h`, so `h` is a bridge of `G`, contradiction.

The other shore `Q` is nonempty, so `P^+` has strictly fewer vertices than `G`. ∎

The same holds for `Q^+`.

---

## 4. Two-cut root-flow gluing

By vertex minimality, `P^+` and `Q^+` have root-valued `E_5` flows. Let the two completion edges have roots

\[
r_P,r_Q\in R_5.
\]

The support permutation group `S_5` is transitive on the ten roots. Apply one global support permutation to the flow on `Q^+` so that

\[
r_Q=r_P.
\]

Delete the two completion edges and restore the two original cut edges. Both restored edges receive the common root. Every old cubic vertex equation is unchanged.

### Theorem 4.1 — cyclic two-cut gluing

Root-valued five-support flows glue across every two-edge cut of a connected bridgeless cubic multigraph.

Hence a vertex-minimal counterexample has no two-edge cut.

---

## 5. Cyclic three-edge-cut completion

Let a three-edge cut have one connected shore `P` with boundary semiedges

\[
e_1,e_2,e_3.
\]

If `P` is acyclic, Theorem 1.1 says that it is one cubic vertex and is already a bounded trivial shore. Assume `P` contains a cycle.

Complete `P` by adding one new cubic vertex `z` and joining `z` to the three boundary semiedges. Call the completion `P^+`.

### Theorem 5.1 — three-cut completion category

`P^+` is connected, cubic, bridgeless, and strictly smaller than `G`.

### Proof

Connectedness and cubicity are immediate.

No new edge `ze_i` is a bridge: because `P` is connected and contains more than the single acyclic vertex, the endpoint of `e_i` is connected inside `P` to an endpoint of another boundary semiedge; together with the two corresponding new edges through `z`, this gives a cycle containing `ze_i`.

Suppose an old edge `h` is a bridge of `P^+`. If the components of `P-h` contain boundary semiedges on both sides, the new vertex `z` and its incident edges reconnect the two sides, so `h` is not a bridge. Hence one component contains no boundary semiedge. In `G` that component meets the rest only through `h`, contradicting bridgelessness.

The opposite shore contains a cycle and therefore has at least three vertices: by Theorem 1.1 an acyclic three-port shore is the only one-vertex possibility. Replacing it by one completion vertex strictly lowers graph order. ∎

---

## 6. Three-cut root-flow gluing

At the added completion vertex, the three incident roots form one support triangle. Thus on the ordered boundary semiedges the two shore completions carry two ordered edge triples of triangles in `K_5`.

Every permutation of the three edges of a support triangle is induced by a permutation of its three support vertices, and this extends to an element of `S_5`. Therefore one global support permutation on one shore aligns the three boundary roots edge by edge.

Delete the two completion vertices and join corresponding semiedges.

### Theorem 6.1 — cyclic three-cut gluing

Root-valued five-support flows glue across every cyclic three-edge cut.

A noncyclic three-cut shore is the explicit one-vertex bounded gadget of Theorem 1.1.

---

## 7. Cyclic four-edge-cut cap completion

Assume two- and three-cut reductions have already been performed. Let a cyclic four-edge cut have connected proper shore `P` with ordered boundary terminals

\[
1,2,3,4.
\]

For any terminal matching

\[
M_i=X_i\mid Y_i,
\]

attach the standard two-vertex cap `cap_i`: one new vertex joins the two terminals in `X_i`, one joins the two terminals in `Y_i`, and one central edge joins the new vertices.

Call the completed graph

\[
P_i^+=P\cup cap_i.
\]

### Theorem 7.1 — four-cut cap category

For every `i`, the graph `P_i^+` is connected, cubic, bridgeless, and strictly smaller than `G`.

### Proof

Connectedness and cubicity are immediate.

Every new terminal edge lies on a cycle: from its endpoint in `P`, use a path in connected `P` to any other boundary endpoint and return through the connected cap. The central cap edge also lies on a cycle because `P` contains a path between the two terminal blocks.

Suppose an old edge `h` is a bridge of `P_i^+`. If both components of `P-h` contain boundary terminals, the connected cap gives a path between them avoiding `h`. Hence one component contains no terminal. That component meets the rest of the original graph only through `h`, contradicting bridgelessness.

The opposite shore `Q` is cyclic. By Theorem 1.1 it is not the two-vertex acyclic cap; hence `|V(Q)|>2`. Replacing `Q` by the two cap vertices gives

\[
|V(P_i^+)|<|V(G)|.
\]

∎

Therefore vertex minimality gives a root-valued flow on all three cap completions.

---

## 8. Exact four-cut cap forcing

Restrict a root flow on `P_i^+` to `P`. Its boundary state lies in the exact cap profile

\[
K_i=\{B_j,D_j:j\ne i\}.
\]

Hence

\[
\boxed{
\Sigma(P)\cap K_i\ne\varnothing
\qquad(i=0,1,2).}
\]

The same holds for the opposite shore `Q`.

This proper-shore cap forcing is valid because every capped shore is strictly smaller. It is distinct from the same-order arbitrary-edge cap discussed in `GLOBAL_CAP_LIFT_INTERFACE_COMPATIBILITY_V1.md`.

---

## 9. Four-cut profile intersection

Five-support flows on `P` and `Q` glue exactly when

\[
\Sigma(P)\cap\Sigma(Q)\ne\varnothing.
\]

Indeed a common support-unordered state means the two multisets of five even boundary traces agree. One global support permutation aligns the traces coordinatewise, hence aligns every terminal root and permits gluing.

Assume the profiles were disjoint. Both are physical complete profiles meeting all three cap sets. The exact finite disjoint-profile classification leaves only four minimal kernel pairs, which reduce under matching permutation and shore exchange to:

1. Type T: `P_5|P_5`;
2. Type H: `P_4|C_3`.

`TYPE_T_PHYSICAL_COMMUTATION_ELIMINATION_V1.md` excludes Type T by two disjoint support-pair challenges whose second route is physically unchanged by the first switch.

`TYPE_H_PHYSICAL_COMMUTATION_ELIMINATION_V1.md` excludes both BBD and DDD triangle policies by the same disjoint-support route invariance.

### Theorem 9.1 — cyclic four-cut gluing

Every pair of physical cap-forced shore profiles intersects. Therefore root-valued five-support flows glue across every cyclic four-edge cut.

Hence a vertex-minimal counterexample is cyclically five-edge-connected after the explicit bounded-shore reductions.

---

## 10. Exact cut/base disposition

Every edge cut of size at most four in a connected bridgeless cubic graph is consumed as follows.

| cut size | cyclic shores | acyclic shore |
|---|---|---|
| `2` | smaller edge completions and root alignment | impossible for a nonempty shore |
| `3` | smaller one-vertex completions and triangle alignment | one cubic vertex |
| `4` | three smaller cap completions, profile intersection, Type T/H elimination | one two-vertex cap |

Together with:

- a loop in a connected cubic graph forcing its unique nonloop incident edge to be a bridge;
- the theta graph with explicit roots `12,13,23`;
- double-parallel and triangle neighbourhoods entering the table above;

this supplies the complete low-order graph-category interface used before the arbitrary-edge step.

---

## 11. Trust boundary

### Exact in this dossier

- the acyclic cubic-shore formula `n=k-2`;
- complete acyclic classification for `k<=4`;
- connectedness of all relevant cut shores in the stated reduction order;
- connected, bridgeless, cubic, strictly smaller completion for cyclic cuts of size two, three, and four;
- exact root alignment across two- and three-cuts by one support permutation;
- exact proper-shore cap forcing at four cuts;
- distinction from the same-order arbitrary-edge cap;
- four-cut signature gluing from one common state;
- applicability of Type T and Type H physical eliminations;
- complete low-port cut/base disposition.

### Imported authorial mathematics

- the exact ten-state boundary classification;
- the exact finite disjoint cap-forced kernel classification;
- the Type T and Type H physical commutation theorems.

### Outside this checkpoint

- proof-development expansion of the finite mismatch classification;
- independent mathematical audit;
- curation or canonical movement;
- Lean verification;
- manuscript integration;
- release, arXiv, DOI, peer review, or publication.