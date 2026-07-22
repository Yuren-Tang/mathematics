# Global minimal-counterexample closure for five indexed supports

## Research dossier v1 — complete candidate proof synthesis

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `1dd3aa809c1baaa7bcbe75a9b3eeca1ac7e36864`.

**Parents:**

- `five-support/root-flow-lifting.md`;
- `five-support/cuts-four-poles-and-routing.md`;
- `TYPE_T_PHYSICAL_COMMUTATION_ELIMINATION_V1.md`;
- `TYPE_H_PHYSICAL_COMMUTATION_ELIMINATION_V1.md`;
- `ARBITRARY_EDGE_THREE_RECONNECTION_CATEGORY_V1.md`;
- `ORIENTED_FULL_CHANNEL_LOCK_ELIMINATION_SYNTHESIS_V1.md`;
- the explicit theta and `K_4` base flows;
- the bounded loop/parallel/acyclic degeneration lemmas.

**Status:** complete research-branch candidate proof. Every finite connected bridgeless cubic multigraph admits a nowhere-zero `E_5`-flow whose values are the ten roots `R_5`, equivalently an indexed cycle double cover with five even supports. The proof is by vertex-minimal counterexample: cyclic cuts of sizes two, three, and four glue; bounded multigraph degenerations are explicit; at an arbitrary remaining edge all three reconnection closures are smaller bridgeless soluble graphs; the full-channel lock-elimination theorem then forces the original two-vertex cap to lift root-valuedly. This contradicts minimality.

**Assurance boundary:** this is not yet an accepted theorem of the project or of the mathematical literature. It has not received independent audit, Lean verification, manuscript integration, peer review, release, arXiv, DOI, or publication status. Its most delicate imported component is the contextual equality/DDD inverse-transfer synthesis, including the Ptolemy-groupoid and history-space root-tube arguments. No canonical or public theorem status is claimed here.

---

## 1. Statement

Let `G` be a finite connected bridgeless cubic multigraph. Loops are counted twice in the degree convention; parallel edges are allowed.

Put

\[
E_5=\left\{x\in\mathbf F_2^5:\sum_{i=1}^5x_i=0\right\}
\]

and

\[
R_5=\{e_i+e_j:1\le i<j\le5\}.
\]

### Theorem 1.1 — five-support candidate theorem

There exists a flow

\[
\boxed{
\lambda:E(G)\longrightarrow R_5
}
\]

satisfying Kirchhoff conservation at every vertex.

Equivalently, `G` has five indexed even edge sets

\[
(F_1,F_2,F_3,F_4,F_5)
\]

such that every edge belongs to exactly two of them.

The equivalence is the root-flow theorem: the two support coordinates containing an edge are exactly its root label.

---

## 2. Minimal-counterexample setup

Assume the theorem false and choose a counterexample `G` with minimum vertex number.

Every connected bridgeless cubic graph of smaller order has a root-valued `E_5` flow.

### Lemma 2.1 — no loops

A connected cubic graph containing a loop has a bridge.

### Proof

At the loop vertex the loop contributes degree two, so there is exactly one nonloop incident edge. That edge is the unique connection of the vertex/loop to the rest of the connected graph and is a bridge. ∎

Hence `G` is loopless.

---

## 3. Explicit bounded bases

### Theta graph

The two-vertex cubic multigraph with three parallel edges has the root flow

\[
12,\quad13,\quad23.
\]

Their sum is zero at both vertices.

### `K_4`

Use its standard proper three-edge-colouring by the three perfect matchings. Assign the roots

\[
12,\quad13,\quad23
\]

to the three colours. Every vertex sees the root triangle and satisfies conservation.

### Lemma 3.1 — parallel-edge reduction

If `G` has exactly two parallel edges between two vertices, their two remaining incident edges form a two-edge cut. Unless the graph is the theta base, the graph decomposes across that cut.

### Lemma 3.2 — triangle reduction

If `G` contains a triangle, its three outgoing edges form a three-edge cut. If the opposite shore contains a cycle, this is a cyclic three-cut. If the opposite shore is acyclic, cubic degree counting forces it to consist of one vertex, and the graph is `K_4` or a bounded parallel degeneration.

Therefore after the cut reductions below, a minimal counterexample is simple and outside all bounded bases.

---

## 4. Cyclic two-edge-cut gluing

Suppose a cyclic two-edge cut separates shores `A,B`. Complete each shore by joining its two boundary semiedges with one new edge. The two completed graphs are connected bridgeless cubic multigraphs of smaller order.

By minimality they have root flows. Let the two completion edges have roots

\[
r_A,r_B\in R_5.
\]

The group `S_5` acts transitively on roots. Permute the five support indices on the `B`-flow so that

\[
r_B=r_A.
\]

Delete the two completion edges and reconnect the original cut edges. Both new cut edges receive the common root, and the vertex equations on both shores remain unchanged.

### Theorem 4.1 — two-cut gluing

Five-support root flows glue across every cyclic two-edge cut.

Hence `G` has no cyclic two-edge cut.

---

## 5. Cyclic three-edge-cut gluing

For a cyclic three-edge cut, complete each shore by one cubic vertex. By minimality both completions have root flows.

At each completion vertex, the three boundary roots form one support triangle. Permute the five supports on one shore so the two boundary triangles agree edge by edge. Delete the completion vertices and join corresponding boundary semiedges.

The established cubic local boundary law proves:

### Theorem 5.1 — three-cut gluing

Five-support root flows glue across every cyclic three-edge cut.

Hence `G` has no cyclic three-edge cut.

---

## 6. Cyclic four-edge-cut gluing

Let a cyclic four-cut have shores `P,Q`, with complete support-unordered boundary profiles

\[
\Sigma(P),\Sigma(Q)\subseteq\mathcal S.
\]

The signature-intersection theorem says the shore covers glue exactly when

\[
\Sigma(P)\cap\Sigma(Q)\ne\varnothing.
\]

Minimality and the three standard two-vertex caps force each shore profile to meet all three cap sets.

The finite disjoint-profile classification leaves only the abstract Type-T and Type-H mismatch kernels. Physical disjoint-support route invariance eliminates Type T; the physical BBD/DDD commutation theorem eliminates Type H.

Therefore the profiles intersect and the shores glue.

### Theorem 6.1 — four-cut gluing

A vertex-minimal counterexample has no cyclic four-edge cut.

Thus `G` is cyclically five-edge-connected after the bounded-base reductions.

---

## 7. Arbitrary-edge three-reconnection reduction

Choose any edge

\[
uv\in E(G).
\]

Delete `u,v`, exposing four incidences

\[
a,b\mid c,d.
\]

Form the three direct reconnection closures corresponding to

\[
ab\mid cd,\qquad ac\mid bd,\qquad ad\mid bc.
\]

The simultaneous arbitrary-edge category theorem gives the alternative:

1. all three closures are connected bridgeless cubic multigraphs with two fewer vertices;
2. `G` has a cyclic cut of size at most four;
3. `G` has a bounded loop/parallel/acyclic degeneration.

Alternatives 2--3 have already been consumed in Sections 3--6. Hence all three reconnection closures are smaller bridgeless cubic graphs.

By minimality, all three have root-valued `E_5` flows.

Let `P=G-{u,v}` be the complementary ordered four-pole. Cutting the two matching edges in the three covers gives

\[
\boxed{
\Sigma(P)\cap J_r\ne\varnothing
\qquad(r=i,j,k).}
\]

---

## 8. Restore the original cap

The deleted vertices `u,v` and their edge form the standard two-vertex cap `C_i`, whose terminal blocks are the original shores

\[
a,b\mid c,d.
\]

The complete full-channel lock-elimination theorem applies to `P` and `C_i` because all three reconnection closures are smaller soluble inputs.

It gives

\[
\boxed{
\Sigma(P)\cap K_i\ne\varnothing.}
\]

Choose one common boundary state. It is realised by:

- a root-valued flow on `P`;
- a root-valued flow on the cap `C_i`.

After a support permutation aligning the labelled terminal roots, glue the two flows. The result is a root-valued `E_5` flow on the original graph `G`.

This contradicts the choice of `G` as a counterexample.

---

## 9. Conclusion

No vertex-minimal counterexample exists.

Therefore every finite connected bridgeless cubic multigraph has a root-valued `E_5` flow, and hence an indexed five-support cycle double cover.

\[
\boxed{
\forall G\text{ finite connected bridgeless cubic},
\quad
\exists\lambda:E(G)\to R_5.}
\]

---

## 10. Well-foundedness and noncircularity

The proof has two nested orders.

### Outer order

Vertex number of the closed cubic graph. It is used for:

- two-/three-/four-cut shore completions;
- the three reconnection closures of one edge;
- contextual recursion after an actual two-face cancellation.

Every invocation is on a graph with strictly fewer vertices.

### Inner orders

Within one inverse-dipole cap problem:

- equality potential
  \[
  (E,\Phi,|V|);
  \]
- DDD potential
  \[
  (\Omega,|V|);
  \]
- finite same-order contextual state graph;
- first-failure track complexity and Ptolemy/backbone reduction.

These inner reductions do not invoke the global theorem at the same graph order. Matching flips, separators, and bounded terminals exit the inner recursion.

The cut-gluing theorems precede the arbitrary-edge step. The full-channel theorem uses only smaller reconnection graphs and local/finite transfer. Therefore the final contradiction does not assume Theorem 1.1.

---

## 11. Exact dependency spine

The load-bearing path is:

\[
\begin{aligned}
&\text{root-flow equivalence}\\
&\Downarrow\\
&\text{minimal counterexample}\\
&\Downarrow\\
&\text{two-/three-/four-cut gluing and bounded bases}\\
&\Downarrow\\
&\text{all-three arbitrary-edge reconnection category theorem}\\
&\Downarrow\\
&\text{three smaller root covers}\\
&\Downarrow\\
&\text{three-reconnection fixed-route forcing}\\
&\Downarrow\\
&\text{equality/DDD horizontal rescue or oriented lock}\\
&\Downarrow\\
&\text{monotone root surgery + bounded terminal/route escape}\\
&\Downarrow\\
&\text{cover-independent contextual inverse transfer}\\
&\Downarrow\\
&\text{original cap lift}\\
&\Downarrow\\
&\bot.
\end{aligned}
\]

The old dual-rank-three hyperbolic route is not used in this closure proof. It remains mathematically valuable as structural analysis and as an independent possible proof family, but it is logically bypassed by the completed arbitrary-edge inverse-dipole theorem.

---

## 12. Assurance and trust boundary

### Claimed at research-dossier level

- a complete minimal-counterexample proof synthesis;
- exact reduction of the global theorem to the full-channel cap-lift theorem;
- no remaining declared mathematical branch inside this proof architecture.

### Not yet claimed

- canonical project acceptance;
- independent verification of every local theorem and correction interaction;
- Lean formalisation;
- manuscript-quality proof;
- peer review;
- release, arXiv, DOI, or publication;
- recognition as an established theorem outside this research branch.

### Mandatory next action

Launch an independent paper-first audit that reconstructs the proof from the exact dependency spine without relying on old frontier summaries, rank-three heuristics, Lean declarations, or this dossier's conclusion. Particular attention must be paid to:

1. simultaneous validity of all three reconnection closures;
2. the three-reconnection fixed-route classification;
3. equality/DDD current-flow potentials;
4. the contextual inverse-transfer/Ptolemy tube theorem;
5. absence of circular minimality between cap transfer and the global theorem;
6. cut and bounded-category edge cases.
