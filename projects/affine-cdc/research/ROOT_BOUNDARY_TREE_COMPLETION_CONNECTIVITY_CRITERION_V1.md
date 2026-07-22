# Root-valued tree completion is equivalent to connected boundary support

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `a776ab019315c176e6a1ce9aaa156179f7307056`  

**Parents:**

- `projects/affine-cdc/research/SIX_ROOT_BOUNDARY_BRIDGELESS_TREE_REPLACEMENT_V1.md`;
- `projects/affine-cdc/research/SIX_LEAF_NNI_ROOT_EXCHANGE_V1.md`;
- the four-root pairing-sum classification;
- the defect-minimal forest and root-flow lifting framework.

**Status:** exact all-port coefficient theorem. A finite multiset of roots of `E_5` with total sum zero admits a root-valued unrooted cubic-tree completion if and only if the support multigraph formed by those roots has exactly one nontrivial connected component and that component contains at least three support vertices. The sufficiency proof is constructive: regard the boundary roots as the edges of a connected Eulerian multigraph, repeatedly split off two consecutive distinct-neighbour edges of an Euler circuit, reduce to a triangle, and reverse the reductions as root-valued cherries. The necessity proof uses parity inside boundary support components and the fact that every cubic root vertex is a triangle of `K_5`.

**Not implied:** that an arbitrary root-valued tree completion can always be chosen to preserve bridgelessness for every exterior component partition; that every residual defect-tree component has connected boundary support; elimination of the disconnected matching-plus-Tait/equality/DDD sectors; a completed global proof DAG; canonical acceptance; independent audit; Lean verification; manuscript integration; or the global five-support theorem.

---

## 1. Boundary roots as an Eulerian multigraph

Let

\[
R_5=\{ij:1\le i<j\le5\}
\]

be the ten roots, identified with the edges of `K_5`.

Let

\[
\mathbf r=(r_1,\ldots,r_n)
\]

be a finite ordered boundary word of roots satisfying

\[
\boxed{
\sum_{h=1}^n r_h=0
\quad\text{in }E_5.
}
\]

Construct the loopless edge multigraph

\[
H(\mathbf r)
\]

on support vertex set `[5]` by inserting one edge copy for every occurrence of a root in `\mathbf r`.

### Lemma 1.1 — conservation is Euler parity

\[
\boxed{
\sum_h r_h=0
\iff
H(\mathbf r)\text{ has even degree at every support vertex}.}
\]

### Proof

The coordinate of the sum at support vertex `i` is the parity of the number of boundary roots containing `i`, which is exactly the parity of the degree of `i` in the edge multigraph. ∎

Thus every conserved root boundary is an Eulerian multigraph, possibly with several nontrivial connected components and isolated support vertices.

---

## 2. Root-valued cubic-tree completion

An unrooted cubic tree with `n` labelled leaves has

\[
n-2
\]

internal cubic vertices and

\[
n-3
\]

internal edges.

Attach the boundary roots `r_1,\ldots,r_n` to its labelled leaves. Conservation uniquely forces the value of every internal edge: for an internal split

\[
A\mid A^c
\]

its value is

\[
\lambda(A)=\sum_{h\in A}r_h.
\]

### Definition 2.1

A **root-valued tree completion** of `\mathbf r` is an unrooted cubic tree for which every forced internal edge value belongs to `R_5`.

At every internal cubic vertex the three incident nonzero roots sum to zero. Hence they are three distinct roots forming one triangle of `K_5`.

---

## 3. Necessity of connected boundary support

Let the nontrivial connected components of the boundary multigraph be

\[
C_1,\ldots,C_m.
\]

### Lemma 3.1 — a root sum cannot cross boundary components

Let `S` be any submultiset of the boundary root copies. If

\[
\sum_{r\in S}r
\]

is a root, then both endpoints of that root lie in one common component `C_j`.

### Proof

Inside every graph component, the number of odd-degree vertices of the submultigraph induced by `S` is even. The binary sum of the roots in `S` is precisely the incidence vector of all odd-degree vertices of that submultigraph.

If this sum is a root, it has exactly two support coordinates. Those two odd vertices therefore cannot be split one-and-one between different components, since each component contributes an even number. Hence both lie in one component. ∎

### Corollary 3.2

Every internal root label of a root-valued tree completion belongs to one boundary support component.

Indeed an internal value is the sum of the boundary roots on one shore of the corresponding tree edge.

### Theorem 3.3 — necessity

If `\mathbf r` has a root-valued cubic-tree completion, then:

1. `H(\mathbf r)` has exactly one nontrivial connected component;
2. that component contains at least three support vertices.

### Proof

At one internal cubic vertex, its three incident labels form a support triangle, and by Corollary 3.2 all three roots belong to the same boundary component.

Two adjacent cubic vertices share one internal root edge. Therefore their two support triangles belong to the same boundary component. Since the cubic tree is connected, propagation across its internal edges shows that every internal and boundary root belongs to one common component of `H(\mathbf r)`.

That component contains at least three support vertices because every cubic root vertex carries a genuine triangle. A component on only two support vertices has only one possible root label and cannot support three nonzero roots summing to zero. ∎

Thus disconnected boundary support and the doubled single-edge sector are genuine coefficient obstructions to a root-valued tree.

---

## 4. Splitting off an Euler-circuit turn

Assume now that `H=H(\mathbf r)` has one nontrivial connected component on at least three vertices. By Lemma 1.1, this component is connected and Eulerian.

Choose an Euler circuit

\[
v_0,e_1,v_1,e_2,\ldots,e_m,v_m=v_0.
\]

Because the active support contains at least three vertices, the cyclic vertex word has an occurrence

\[
\boxed{u,v,w\quad\text{with }u\ne w.}
\]

Indeed, if every length-two step returned to its previous vertex, then

\[
v_{i-1}=v_{i+1}
\]

for every `i`, so the circuit would alternate between at most two support vertices.

Let the corresponding two edge copies be

\[
uv,
\qquad
vw.
\]

Delete these two copies and insert one new edge copy

\[
uw.
\]

Call the resulting multigraph `H'`.

### Lemma 4.1 — Euler preservation

`H'` is Eulerian, and its nonisolated support is connected.

### Proof

At `v`, two incidences are removed; at `u,w`, one incidence is removed and one is added. Thus every degree parity is preserved.

In the Euler circuit, replace the consecutive trail segment

\[
u-v-w
\]

by the single edge `u-w`. The resulting cyclic edge sequence traverses every edge of `H'` exactly once. Hence all nonisolated edges of `H'` lie in one Euler circuit and its nonisolated support is connected. ∎

The operation lowers the edge count by one and is exactly the coefficient identity

\[
uv+vw=uw.
\]

---

## 5. Avoiding the two-vertex terminal state

When the active support has at least four vertices, the splitting operation can remove at most the middle degree-two support vertex `v`. Hence the new active support still contains at least three vertices.

It remains to treat the case of exactly three active support vertices.

Write the three edge multiplicities as

\[
x=m_{12},
\qquad
y=m_{13},
\qquad z=m_{23}.
\]

Euler parity gives

\[
\boxed{x\equiv y\equiv z\pmod2.}
\]

### Lemma 5.1 — three-support reduction

If

\[
x+y+z>3,
\]

one can split off two incident edges with distinct other endpoints so that the resulting Eulerian multigraph still has all three support vertices active.

### Proof

If `x,y,z` are all even, connectedness implies at least two are positive, and every positive one is at least two. Choose two positive edge classes sharing one support vertex, remove one copy from each, and add one copy of the third class. The two chosen classes remain nonzero and the third becomes or remains nonzero.

If `x,y,z` are all odd and the total exceeds three, at least one multiplicity is at least three. Choose one edge from that heavy class and one edge from an adjacent positive class. After splitting, the heavy class remains positive, the third class increases, and the remaining class is nonnegative; at least two classes remain and all three support vertices stay active.

In both cases the new multigraph is connected Eulerian on the same three active vertices. ∎

Repeated splitting therefore cannot fall into an even parallel bundle on two vertices. It eventually reaches

\[
(x,y,z)=(1,1,1),
\]

the support triangle.

---

## 6. Constructive sufficiency

### Theorem 6.1 — connected-support completion

If `H(\mathbf r)` has exactly one nontrivial connected component on at least three support vertices, then `\mathbf r` has a root-valued cubic-tree completion.

### Proof

Induct on the number `m` of boundary edge copies.

#### Base case

The smallest connected Eulerian loopless multigraph on at least three support vertices has three edges and is a triangle. One cubic vertex with the three boundary roots is the required completion.

#### Inductive step

Use Sections 4–5 to choose a split

\[
uv,\ vw
\longmapsto
uw
\]

such that the resulting multigraph `H'` remains connected Eulerian on at least three active support vertices.

By induction, the boundary word of `H'` has a root-valued cubic-tree completion. Mark the boundary leaf corresponding to the newly inserted edge copy `uw`.

Replace that leaf by one new cubic cherry vertex carrying:

- the old internal incidence labelled `uw`;
- one new boundary leaf labelled `uv`;
- one new boundary leaf labelled `vw`.

At the new vertex,

\[
uv+vw+uw=0,
\]

so it is a root triangle. Every old internal edge remains unchanged and root-valued. This reconstructs a root-valued completion of the original boundary word. ∎

The proof is algorithmic: an Euler circuit supplies the sequence of splitting operations, and reversing them supplies the labelled cubic tree.

---

## 7. Complete criterion

Combining Theorems 3.3 and 6.1:

### Theorem 7.1 — root-boundary connectivity criterion

For every finite conserved root boundary word `\mathbf r`, the following are equivalent.

1. `\mathbf r` admits a root-valued unrooted cubic-tree completion.
2. The boundary support multigraph `H(\mathbf r)` has exactly one nontrivial connected component, and that component contains at least three support vertices.

Equivalently:

\[
\boxed{
\text{root tree exists}
\iff
\text{the boundary root support is connected after deleting isolated support vertices, and is not one edge}.}
\]

This criterion is valid for every number of boundary ports, not only six.

---

## 8. Hyperplane and low-rank interpretation

The span of the boundary roots is the binary incidence space of their support graph. If the active support graph has `c` connected components on `v` active vertices, then

\[
\dim\langle r_1,\ldots,r_n\rangle=v-c.
\]

For the five-support problem, failure of the connected-support criterion forces one of the following coefficient decompositions.

### One active two-vertex component

All boundary roots equal one private root. This is the equality/root-line sector.

### A `3+2` support decomposition

One component carries roots of a support triangle, and the other component carries one disjoint root direction. This is exactly

\[
\boxed{
\text{complementary Tait triangle}
\quad+\quad
\text{private matching root}.}
\]

It is the matching-plus-Tait side-network alphabet.

### A `2+2` support decomposition

The boundary uses two disjoint root directions. Their span is

\[
\{0,a,b,a+b\},
\]

the equality/DDD four-point plane.

No other disconnected support pattern exists on five support vertices once isolated vertices are ignored.

Thus every failure of arbitrary-port root-tree completion is already one of the low-rank sectors isolated elsewhere in the programme.

---

## 9. Recovery of the six-root census

For `n=6`, Theorem 7.1 immediately explains the exact exceptional families of `SIX_ROOT_BOUNDARY_BRIDGELESS_TREE_REPLACEMENT_V1.md`.

- `a^6`: one active two-vertex component;
- `a^4b^2` with `a\perp b`: a `2+2` support decomposition;
- the exceptional doubled triple represented by `12^2,13^2,45^2`: a `3+2` support decomposition.

All other conserved six-root words have connected active support on at least three vertices and therefore admit a root-valued tree.

The finite count

\[
59400+3160=62560
\]

is the six-port specialization of the structural connectivity criterion, rather than an isolated census phenomenon.

---

## 10. Consequence for an entire defect component

Let `K` be one induced tree component of the defect support of an `E_5` flow. Every edge leaving `K` is root-valued, and cubic degree counting gives

\[
|\partial K|=|V(K)|+2.
\]

Apply Theorem 7.1 to the multiset of boundary roots of `K`.

### Connected-support branch

The complete boundary admits a root-valued cubic tree with exactly

\[
|\partial K|-2=|V(K)|
\]

internal vertices. Thus the coefficient-side obstruction of the whole component can be removed without increasing source size.

The remaining source question is to choose such a completion compatibly with bridgelessness or to extract an exterior separator.

### Disconnected-support branch

The complete boundary lies in one of:

- an equality/root line;
- a private matching plus complementary Tait network;
- an equality/DDD plane.

These are precisely the existing low-rank peeling and singular-fibre branches.

Therefore an arbitrary defect-tree component has no unclassified boundary coefficient type.

---

## 11. Revised global frontier

The remaining whole-component theorem is now purely source-categorical.

> Let `K` be an induced defect-tree component whose root boundary support is connected and contains at least three support vertices. Prove that some root-valued tree completion of the same boundary and same number of internal vertices is bridgeless, or else the exterior component partition exposes a gluable separator / bounded degeneration.

For six terminals this theorem is already exact, with at least seven safe completions for every allowed exterior partition.

If the boundary support is disconnected, no general tree-completion theorem is needed: the component belongs to the matching-plus-Tait/equality/DDD sectors already equipped with peeling, Kempe rescue, and bounded-atom reductions.

Thus the coefficient classification of arbitrary defect-tree components is complete. The open datum is only the source-category realization and global well-founded packaging.

---

## 12. Reliability boundary

### Exact theorem-level results

- conservation equals Euler parity of the boundary support multigraph;
- a root internal sum cannot cross boundary support components;
- necessity of one active component on at least three support vertices;
- Euler-circuit splitting-off preservation;
- the three-support multiplicity reduction;
- constructive induction to a support triangle;
- the all-port completion criterion;
- identification of every disconnected-support failure with equality, matching-plus-Tait, or DDD coefficient sectors;
- recovery of the six-root exceptional classification.

### Still open

- arbitrary-port bridgeless choice of the root-valued completion under an exterior component partition;
- conversion of failure of such a choice into a small separator or bounded source degeneration;
- full peeling of every disconnected-support defect component in the global minimal-counterexample setting;
- global proof-DAG assembly and well-foundedness;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
