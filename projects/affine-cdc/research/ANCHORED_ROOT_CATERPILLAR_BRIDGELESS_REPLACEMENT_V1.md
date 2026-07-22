# Anchored root caterpillars give arbitrary-port bridgeless replacements

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `e629ca90428a3bb3676c93ed1d19421c8710a2be`  

**Parents:**

- `projects/affine-cdc/research/ROOT_BOUNDARY_TREE_COMPLETION_CONNECTIVITY_CRITERION_V1.md`;
- `projects/affine-cdc/research/SIX_ROOT_BOUNDARY_BRIDGELESS_TREE_REPLACEMENT_V1.md`;
- `projects/affine-cdc/research/BRIDGELESS_ROOT_STAR_REPLACEMENT_V1.md`;
- the physical cut/separator and secondary-defect-minimality framework.

**Status:** exact arbitrary-port source-category theorem. Let a conserved root boundary have connected nontrivial support on at least three support vertices, and distinguish any two boundary edge copies `alpha,beta`, possibly carrying the same root value. There is a root-valued caterpillar completion in which `alpha,beta` are the two end leaves, so every internal tree edge separates them. Consequently, for every partition of the boundary incidences into exterior connected components with no singleton block, choosing `alpha,beta` in one common block gives a same-size connected bridgeless root-valued tree replacement. Thus the arbitrary-port bridgeless-choice problem is completely solved in the connected-support sector.

**Not implied:** transfer of an arbitrary root cover from the replacement graph through the original defect-tree topology as a root cover; elimination of the resulting unique global defect component; complete peeling of the disconnected-support matching-plus-Tait/equality/DDD sectors; global proof-DAG closure; canonical acceptance; independent audit; Lean verification; manuscript integration; or the global five-support theorem.

---

## 1. Protected boundary copies

Let

\[
\mathbf r=(r_1,\ldots,r_n)
\]

be a conserved boundary root word:

\[
\sum_{i=1}^n r_i=0.
\]

Regard its root copies as the edges of the Eulerian boundary multigraph

\[
H=H(\mathbf r)
\]

on support set `[5]`.

Assume the nonisolated support of `H` is connected and contains at least three vertices.

Choose two distinct boundary incidences

\[
\alpha,
\qquad
\beta.
\]

They are distinct edge copies, but their root labels may coincide.

The objective is stronger than an arbitrary root tree: construct a completion in which every internal edge separates the leaves `alpha` and `beta`.

---

## 2. Protected splitting-off state

During the construction retain:

1. a distinguished aggregate edge copy
   \[
   p;
   \]
2. the untouched terminal copy
   \[
   \beta;
   \]
3. the remaining unused original boundary copies.

Initially

\[
p=\alpha.
\]

At every stage the current multigraph `J` is connected and Eulerian. Its edge set consists of `p`, `beta`, and the unused copies.

Suppose an unused edge copy

\[
e=uw
\]

shares exactly one support endpoint with

\[
p=uv.
\]

Then

\[
p+e=vw
\]

is a root. The **protected splitting-off move** is

\[
\boxed{
(uv,uw)
\longmapsto
vw.
}
\]

The new root `vw` becomes the next aggregate edge `p'`; the terminal copy `beta` remains untouched.

This consumes one original boundary copy and preserves Euler parity.

---

## 3. Protected splitting-off lemma

### Lemma 3.1

Let `J` be a connected Eulerian loopless multigraph whose nonisolated support contains at least three vertices. Mark two distinct edge copies `p,beta`. If `J` has another edge copy besides `p,beta`, then there is an unused edge `e` such that:

1. `e` meets `p` in exactly one endpoint;
2. splitting off `p,e` gives a root aggregate `p'=p+e`;
3. the resulting multigraph `J'` is connected on its nonisolated support and Eulerian;
4. if `J'` has more than the two protected copies `p',beta`, its active support still has at least three vertices.

### Proof

Choose an Euler circuit of `J` and mark the occurrence of the protected edge `p`.

Because the active support contains at least three vertices, one may choose the Euler transition at one endpoint of `p` so that the edge paired consecutively with `p` leaves that endpoint toward a support vertex different from the other endpoint of `p`. If the current Euler circuit pairs `p` with a parallel edge, perform the standard transition switch at that endpoint with the first nonparallel departure in the same Euler circuit. The switch preserves one Euler circuit while replacing the local pairing of `p` by a nonparallel incidence. Such a nonparallel departure exists: if both endpoints of `p` were incident only with parallel copies of `p`, the nonisolated support component would have two vertices.

The chosen consecutive segment of the Euler circuit has the form

\[
v-u-w,
\qquad v\ne w,
\]

with `p=uv` and `e=uw`. Replace this two-edge segment by the single edge `vw`. The shortened cyclic sequence is an Euler circuit of the split graph. Hence `J'` is connected on its nonisolated support and Eulerian.

The chosen edge can be taken different from the protected copy `beta`. If `beta` is the only currently displayed nonparallel incidence at one endpoint, Euler parity and absence of bridges in the Eulerian component supply another copy or a nonparallel incidence at the other endpoint; otherwise `beta` would be the unique edge joining the parallel bundle of `p` to the remainder, contradicting Eulerian bridgelessness.

A split can reduce the number of active support vertices only when the common endpoint `u` had degree two. If the active support has at least four vertices, at least three remain. For exactly three active vertices, write the edge multiplicities as

\[
x=m_{12},\quad y=m_{13},\quad z=m_{23}.
\]

They have common parity. The same three-support case analysis as in the unprotected splitting theorem chooses a nonprotected adjacent edge so that all three support vertices remain active unless the split leaves exactly the two protected parallel copies. In the latter case the construction has reached its terminal state. ∎

### Trust note

The only graph-theoretic input is the elementary Euler-transition switch: in one Euler circuit, the pairing of incidences at a visited vertex may be switched with another visit so that a specified incident nonparallel edge follows `p`, while the two circuit segments are rejoined into one Euler circuit. No edge-connectivity theorem stronger than connected Eulerianity is used.

---

## 4. Complete protected reduction

Apply Lemma 3.1 repeatedly. Each move consumes one unused original edge copy, so the process terminates.

The terminal connected Eulerian multigraph contains only the current aggregate edge `p_*` and the protected copy `beta`. Therefore they are parallel copies of the same root:

\[
\boxed{p_*=\beta.}
\]

Record the successive identities

\[
p_{j+1}=p_j+e_j,
\]

where every `p_j,e_j,p_(j+1)` is a root triangle.

---

## 5. Reversing the reductions

Begin with the terminal two-edge state consisting of the parallel copies

\[
p_*,\beta.
\]

Reverse the final splitting move. Replace the aggregate copy `p_(j+1)` by one new cubic vertex incident with:

- the previous aggregate edge `p_j`;
- the consumed boundary leaf `e_j`;
- the continuing edge `p_(j+1)`.

Since

\[
p_j+e_j+p_(j+1)=0,
\]

the new vertex is root-valued.

Repeating this reversal constructs an unrooted cubic caterpillar. Its two end leaves are:

\[
\alpha=p_0
\qquad\text{and}\qquad
\beta.
\]

Every intermediate aggregate edge lies on the unique path between those two leaves.

### Theorem 5.1 — anchored root caterpillar

For any two distinguished boundary incidences `alpha,beta`, a conserved connected-support root boundary admits a root-valued cubic-tree completion `T_(alpha,beta)` such that

\[
\boxed{
\text{every internal edge of }T_(alpha,beta)
\text{ separates }\alpha\text{ from }\beta.
}
\]

Equivalently, `T_(alpha,beta)` is a root-valued caterpillar with `alpha,beta` at its two ends.

The construction preserves the labels and multiplicities of all boundary copies, including the case where `alpha` and `beta` carry the same root.

### Independent finite check

Exact dynamic enumeration for every conserved root multiset of sizes `4` through `10`, every connected-support instance, and every admissible choice of the two distinguished edge-copy values found no counterexample to the anchored theorem.

The finite calculation is a check only; the Euler splitting proof is the theorem.

---

## 6. Exterior component partitions

Let a connected tree region be removed from a connected bridgeless cubic multigraph. Its terminal incidences are partitioned by the connected components of the exterior graph:

\[
\Pi=\{B_1,\ldots,B_m\}.
\]

No block is a singleton. Otherwise the unique terminal edge incident with that exterior component would be a bridge in the original graph.

Choose any block

\[
B\in\Pi
\]

and two distinct terminal incidences

\[
\alpha,\beta\in B.
\]

Construct the anchored root caterpillar `T_(alpha,beta)`.

For every internal edge `f` of this caterpillar, its two terminal shores separate `alpha` and `beta`. Therefore neither shore can be a union of complete blocks of `Pi`, because `alpha,beta` belong to the same block `B`.

By the general internal bridge criterion, no internal edge of the replacement tree is a bridge.

Every terminal edge is also nonbridging, since its exterior component contains another terminal incidence.

---

## 7. Arbitrary-port bridgeless replacement theorem

### Theorem 7.1

Let `R` be any cubic tree region with root-valued boundary incidences. Assume the boundary support multigraph is connected on at least three support vertices. Attach the boundary incidences to an arbitrary exterior graph such that the original closed cubic graph is connected and bridgeless; terminal endpoints may coincide.

Then there exists a root-valued cubic-tree replacement `T` satisfying:

1. `T` has the same labelled boundary incidences;
2. `T` has the same number of internal vertices as `R`;
3. the replacement graph is connected and bridgeless;
4. no assumption of distinct exterior attachment vertices is required.

### Proof

Choose two incidences in one exterior component block and use Theorem 5.1. Every internal split separates those two incidences and hence cuts their common block. Therefore no internal edge is a bridge. Terminal edges are nonbridging by the no-singleton property. The replacement tree connects all exterior components, so the resulting graph is connected. ∎

### Corollary 7.2 — six-port theorem as a special case

For six terminals, Theorem 7.1 implies the universal safe-replacement statement of `SIX_ROOT_BOUNDARY_BRIDGELESS_TREE_REPLACEMENT_V1.md` without enumerating the `41` exterior partitions.

The exact finite lower bound of seven safe six-leaf topologies remains additional quantitative information, but existence is now an arbitrary-port theorem.

---

## 8. Whole defect-component application

Let `K` be one induced tree component of the defect support of an `E_5` flow on a connected bridgeless cubic graph.

Every edge leaving `K` is root-valued, and

\[
|\partial K|=|V(K)|+2.
\]

Assume its boundary root support is connected on at least three support vertices.

Theorem 7.1 gives a root-valued replacement tree with exactly

\[
|\partial K|-2=|V(K)|
\]

internal vertices and produces a connected bridgeless graph of the same order.

### Corollary 8.1 — category-safe component rootification

\[
\boxed{
\text{connected boundary support}
\Longrightarrow
\text{same-order bridgeless rootification of the whole defect component}.}
\]

Thus no exterior attachment pattern can block coefficient rootification of a connected-support defect component.

---

## 9. Secondary-defect localisation

Choose a counterexample lexicographically minimal for

\[
\boxed{(|V(G)|,\delta(G)).}
\]

Let `lambda` be a defect-minimal `E_5` flow, and let `K` be a defect component with connected boundary support.

Rootify `K` by Theorem 7.1, obtaining a same-order bridgeless graph `G_K` and an inherited `E_5` flow with strictly fewer defects.

Hence `G_K` cannot be a counterexample. It has a root-valued flow.

Pull that root flow back through the original tree `K`. A flow on a tree is uniquely determined by its boundary values, so all exterior edges remain roots and only the

\[
|E(K)|=|V(K)|-1
\]

internal edges of `K` may be non-root.

Therefore

\[
\boxed{
\delta(G)\le |V(K)|-1.
}
\]

Since the selected flow already has every internal edge of `K` defective,

\[
\delta(G)\ge |V(K)|-1.
\]

Consequently:

### Theorem 9.1 — one-component localisation

If a defect-minimal flow contains a defect component `K` with connected boundary support, then

\[
\boxed{
\delta(G)=|V(K)|-1,
}
\]

and `K` is the complete defect support. No second defect component exists.

This generalises the earlier `delta(G)=3` localisation for the four-vertex pivot path.

### Trust note

The theorem localises all defects to one tree component but does not yet eliminate an arbitrary topology of that component. Elimination still requires profile transfer, a strict internal reduction, or the disconnected-support low-rank modules after a horizontal change.

---

## 10. Disconnected-support complement

If the boundary support of a defect component is not connected, the coefficient criterion gives only:

1. one equality/root line;
2. one private matching root plus a complementary Tait triangle;
3. one equality/DDD plane.

These are exactly the existing:

- scalar-cycle/equality branch;
- shift-matching plus route-Tait peeling branch;
- DDD singular-fibre and pivot-resolution branch.

Thus arbitrary exterior attachment complexity has been removed from both sides:

- connected boundary support: anchored bridgeless rootification;
- disconnected boundary support: already classified low-rank networks.

---

## 11. Revised final global target

The remaining theorem is no longer a bridgeless replacement theorem.

After Theorem 9.1, a minimal counterexample may be reduced to one of:

1. a single induced defect tree `K` carrying every non-root edge and having connected boundary support;
2. a disconnected-support equality/matching-plus-Tait/DDD carrier.

For Branch 1, every alternative same-boundary root tree gives a soluble same-order graph, but its root cover need not lift root-valuedly through the original topology `K`. One must prove that the resulting all-defect pullbacks admit:

- an internal NNI/equality/DDD reduction;
- a dipole cancellation;
- a horizontal defect-decreasing toggle;
- or a bounded pivot-path normal form.

For Branch 2, consume the existing low-rank peeling modules and verify strict decrease in the global measure.

This is now the exact proof-DAG frontier.

---

## 12. Reliability boundary

### Exact theorem-level results

- protected splitting-off with two distinguished edge copies;
- termination at two parallel protected roots;
- reverse construction of an anchored root caterpillar;
- every internal split separates the two anchors;
- arbitrary-port bridgeless root-tree replacement for every exterior partition without singleton blocks;
- arbitrary attachment coincidences;
- whole-component category-safe rootification;
- secondary-defect localisation to one complete defect component.

### Finite check

- exhaustive verification of the anchored completion statement for conserved root multisets of sizes `4` through `10` and every admissible distinguished edge-copy value pair.

### Still open

- elimination of the one-component all-defect pullback normal form for an arbitrary tree topology;
- complete global consumption of the disconnected-support low-rank branches;
- proof-DAG assembly and well-foundedness;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
