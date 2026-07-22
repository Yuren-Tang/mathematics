# Private-root edges eliminate the disconnected equality two-rail terminal

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `7d4b202f731b902ff321660ac2a77bceae0ce10f`  

**Parents:**

- `projects/affine-cdc/research/EQUALITY_LOCK_PRIVATE_MATCHING_TAIT_DECOMPOSITION_V1.md`;
- `projects/affine-cdc/research/EQUALITY_LOCK_IDENTITY_HEXAGON_CORE_V1.md`;
- `projects/affine-cdc/research/FULL_DEFECT_TREE_NNI_DESCENT_V1.md`;
- `projects/affine-cdc/research/SIX_LEAF_NNI_ROOT_EXCHANGE_V1.md`;
- the category-safe NNI and dipole-cancellation lemmas.

**Status:** exact source-surgery theorem for the disconnected two-rail branch of a pure-gauge equality lock. The complement of the adjacent-channel Tait difference is one private-root matching. If no private edge joins the two marked Tait rails, the marked reconnection edges form a two-edge cut. If a private edge joins the rails, its endpoint types are either aligned or crossed. In the crossed case one root-valued NNI replaces the private edge by a Tait edge, lowers the private-matching size by one, and joins the rails. In the aligned case equal-label dipole cancellation removes two vertices and joins the rails by two root-labelled reconnection edges. Category failure in either surgery exposes the already handled two-/three-cut or bounded-degeneration branch. Therefore the disconnected direct-pairing terminal is not an irreducible equality carrier.

**Not implied:** universal transfer of every root cover through the surgery, elimination of the resulting connected matching--Tait carrier, strict decrease in the final cover-independent global induction, canonical acceptance, independent audit, Lean verification, manuscript integration, or the global five-support theorem.

---

## 1. Equality decomposition and notation

Let

\[
x:E(G')\to R_5
\]

be a root-valued flow carrying a pure-gauge equality lock at two marked reconnection edges

\[
e,f,
\qquad
x(e)=x(f)=r=uv.
\]

Choose

\[
w\in[5]\setminus\{u,v\},
\]

put

\[
s=uw,
\qquad
t=vw,
\qquad s+t=r,
\]

and write

\[
\{p,q\}=[5]\setminus\{u,v,w\}.
\]

The private root is

\[
\boxed{d=pq.}
\]

The adjacent-channel difference

\[
h=s1_{H_s}+t1_{H_t}
\]

has values in

\[
\{0,r,s,t\},
\]

and

\[
\boxed{h(a)=0\iff x(a)=d.}
\]

Hence the zero set of `h` is the root matching

\[
D=x^{-1}(d).
\]

Deleting `D` and suppressing equal-colour degree-two continuations gives a properly three-edge-coloured Tait skeleton with colours

\[
\{r,s,t\}.
\]

Cut the marked edges `e,f`. Both open bicoloured responses equal the locked cap matching

\[
M_i.
\]

---

## 2. Endpoint type of a private edge

Let

\[
g=ab\in D
\]

be one private `d`-edge. At an endpoint `a`, the local root triangle contains `d=pq`, so there is a unique

\[
z_a\in\{u,v,w\}
\]

such that the two non-`d` incidences have labels

\[
\boxed{pz_a,\ qz_a.}
\]

Likewise the endpoint `b` has a unique type

\[
z_b\in\{u,v,w\}
\]

and non-`d` labels

\[
\boxed{pz_b,\ qz_b.}
\]

The two nonzero `h`-values at a type-`z` endpoint are equal. Explicitly:

\[
\boxed{
\begin{array}{c|c}
 z&h(pz)=h(qz)\\
\hline
 w&r\\
 u&s\\
 v&t.
\end{array}}
\]

Thus `z_a=z_b` is exactly the aligned private-edge case, and `z_a\ne z_b` is exactly the crossed case.

---

## 3. Local four-root triality

Remove the interior of `g` and regard its four other incidences as an ordered four-root boundary

\[
\boxed{pz_a,\ qz_a,\ pz_b,\ qz_b.}
\]

The current two-vertex topology groups the first two and last two roots. Its central value is

\[
pz_a+qz_a=pq=d,
\]

and equally on the other shore.

### 3.1 Aligned case

Assume

\[
z_a=z_b=z.
\]

The boundary multiset is

\[
pz,pz,qz,qz,
\]

where `pz` and `qz` are distinct intersecting roots. The three pairing sums have weights

\[
\boxed{(0,2,2).}
\]

More precisely:

- pairing equal labels gives central value `0`;
- either crossed pairing gives central value
  \[
  pz+qz=d,
  \]
  a root.

Hence an aligned private edge is exactly the adjacent-doubled-root local triality: two root topologies and one equality reconnection.

### 3.2 Crossed case

Assume

\[
z_a=z,
\qquad
z_b=z',
\qquad
z\ne z'.
\]

Let `z''` be the third element of `{u,v,w}`. The three pairing sums are:

\[
\boxed{d=pq,}
\]

for the current topology,

\[
\boxed{c=zz',}
\]

for the same-`p` / same-`q` NNI, and

\[
\boxed{Q_{z''}=p+q+z+z',}
\]

for the remaining NNI. Here `d,c` are roots and `Q_(z'')` is the co-root missing `z''`.

Thus the weight pattern is

\[
\boxed{(2,2,4).}
\]

This is exactly one local DDD triality: the current private-root topology, one alternative root topology, and one co-root topology.

---

## 4. Crossed private edge: root-valued NNI

Assume `z_a\ne z_b`. Perform the NNI which pairs

\[
pz_a\text{ with }pz_b
\]

and

\[
qz_a\text{ with }qz_b.
\]

The new central edge has root value

\[
\boxed{z_a z_b.}
\]

At the two new cubic vertices the root triangles are

\[
\{pz_a,pz_b,z_a z_b\}
\]

and

\[
\{qz_a,qz_b,z_a z_b\}.
\]

Therefore the inherited flow remains root-valued on every edge.

The old private edge `d` disappears and no new `d`-edge is created in this two-vertex region. Hence

\[
\boxed{|D'|=|D|-1.}
\]

In the Tait difference `h`, the new central root `z_a z_b` has one of the nonzero colours `r,s,t`. Both new vertices are genuine Tait branch vertices. Consequently the two skeleton components incident with the old private edge become connected through the new Tait region.

### Theorem 4.1 — crossed surgery

A crossed private edge admits a same-order root-valued NNI which:

1. preserves all exterior root labels;
2. removes one private matching edge;
3. replaces two subdivision vertices by two Tait branch vertices;
4. joins the two incident Tait skeleton components.

By the category-safe NNI theorem, exactly one of:

- the modified closed cubic graph is connected and bridgeless;
- the original graph exposes a two-edge separator;
- a bounded acyclic/parallel degeneration is exposed.

No fourth source-category outcome occurs.

---

## 5. Aligned private edge: equal-label cancellation

Assume

\[
z_a=z_b=z.
\]

Delete the two endpoints of `g` and the edge `g`. Reconnect the two half-edges labelled `pz` to one new edge, and reconnect the two half-edges labelled `qz` to another new edge.

Both new edges are root-labelled, so the current flow descends root-valuedly. The operation removes two vertices:

\[
\boxed{|V(G'')|=|V(G')|-2.}
\]

At the Tait level both endpoint subdivisions had the same colour. If the two endpoints lie in distinct marked Tait rails, each new root edge joins those rails. Hence the disconnected Tait core becomes connected after cancellation.

### Theorem 5.1 — aligned surgery

An aligned private edge joining two different Tait skeleton components admits a root-compatible two-vertex cancellation which:

1. preserves every exterior root label;
2. removes the private edge and its two subdivision vertices;
3. reconnects equal root labels pairwise;
4. joins the two incident Tait components by two edges;
5. lowers the source vertex count by two.

The established dipole-category analysis gives one of:

- a smaller connected bridgeless cubic graph;
- a cyclic three-edge cut in the original graph;
- a bounded two-/three-port degeneration.

Thus an aligned cross-rail private edge is not a terminal disconnected carrier.

---

## 6. The two-rail alternative

Let `P` be the four-pole obtained by cutting the marked reconnection edges `e,f`. Suppose the support of the Tait difference `h` has exactly two marked components

\[
R_1,
\qquad
R_2,
\]

whose terminal blocks are the two blocks of the common response `M_i`.

The full four-pole `P` is obtained from the two rails by adjoining the private matching `D` and the suppressed subdivision vertices.

### Case 6.1 — no cross-rail private edge

Assume every edge of `D` has both endpoints on one common rail. Then no edge of `P` joins `R_1` to `R_2`. Hence `P` is disconnected with components carrying the two blocks of `M_i`.

Restoring the two marked reconnection edges `e,f` joins the two components twice. Therefore

\[
\boxed{\{e,f\}\text{ is a two-edge cut of }G'.}
\]

This is the established two-cut gluing / separator branch.

### Case 6.2 — a cross-rail private edge exists

Choose one private edge joining `R_1` to `R_2`.

- If its endpoint types differ, Theorem 4.1 gives a category-safe root NNI which joins the rails and lowers `|D|`.
- If its endpoint types agree, Theorem 5.1 gives a category-safe two-vertex cancellation which joins the rails and lowers `|V|`.

### Theorem 6.1 — no irreducible two-rail equality terminal

The disconnected double-equal Tait response enters exactly one of:

\[
\boxed{
\text{two-edge separator}
\quad\text{or}\quad
\text{root-valued surgery to a connected Tait core}.}
\]

In the surgery branch, category failure is already a two-/three-cut or bounded degeneration. Therefore the abstract direct-pairing two-rail terminal is not an irreducible physical equality lock.

---

## 7. Strict local surgery measure

For one root-labelled equality carrier define

\[
\mathcal M_{\mathrm{rail}}
=
\bigl(
N_{\mathrm{Tait}},
|D|,
|V|
\bigr),
\]

where:

- `N_Tait` is the number of marked Tait skeleton components after cutting `e,f`;
- `D=x^{-1}(d)` is the private-root matching;
- `|V|` is the source vertex count.

Order this lexicographically.

- A crossed cross-rail NNI lowers `N_Tait` and also lowers `|D|` by one.
- An aligned cross-rail cancellation lowers `N_Tait` and lowers `|V|` by two.
- Absence of a cross-rail edge exits to a two-cut.

Thus the disconnected branch has a genuine current-flow surgery descent. The remaining global issue is not termination of this local operation; it is transfer of an arbitrary cover back through the sequence when the final connected carrier is used in the minimal-counterexample induction.

---

## 8. Revised equality frontier

After Theorem 6.1, a support-minimal equality lock may be assumed to have a **connected** marked Tait difference core for every chosen adjacent resolution pair, unless a small separator or bounded degeneration has already been exposed.

The connected core has:

- the exact double-equal response
  \[
  (r^4;M_i,M_i,\varnothing);
  \]
- one private-root matching decorating its Tait skeleton;
- the seven branch-section states;
- the complete-profile six-vertex identity hexagon as its minimal bounded response carrier.

The remaining theorem is therefore the connected matching--Tait transfer theorem, not a two-rail category theorem.

---

## 9. Trust boundary

### Exact here

- endpoint-type classification of every private-root edge;
- exact aligned `(0,2,2)` and crossed `(2,2,4)` four-root trialities;
- root-valued crossed NNI and its central value `z_a z_b`;
- strict decrease of the private matching in the crossed surgery;
- root-compatible equal-label cancellation in the aligned case;
- joining of two Tait rails under either cross-rail surgery;
- no-cross-rail implication `\{e,f\}` is a two-edge cut;
- category-safe surgery alternatives inherited from the established NNI/dipole lemmas;
- elimination of the disconnected two-rail terminal as an irreducible local carrier.

### Still open

- cover-independent transfer through a sequence of these surgeries;
- strict elimination of the connected private-matching-decorated Tait carrier;
- regional realisation of the calibrated Type-X selector as a route/profile switch;
- aligned rank-one laminar contraction in the connected branch;
- global well-founded proof-DAG assembly;
- canonical acceptance, independent review, Lean verification, manuscript integration, release, and publication status;
- the global five-support theorem.
