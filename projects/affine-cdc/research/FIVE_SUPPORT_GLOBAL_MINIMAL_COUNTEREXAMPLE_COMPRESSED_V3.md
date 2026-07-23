# Global five-support minimal-counterexample closure — compressed theorem

## Research dossier v3 — controlling architectural endpoint

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `cf9f3c6ffd35a4b97bebd6e7783fbb804253d3e3`.

**Supersedes for controlling architectural use:**

- `FIVE_SUPPORT_GLOBAL_MINIMAL_COUNTEREXAMPLE_CLOSURE_V1.md`;
- `FIVE_SUPPORT_GLOBAL_MINIMAL_COUNTEREXAMPLE_REPAIRED_V2.md`.

**Load-bearing theorem packages:**

- root-flow equivalence and root triality;
- cyclic two-/three-cut completion and gluing;
- `FOUR_TERMINAL_MATCHING_CLOSURE_PRINCIPLE_V1.md`;
- `TEN_STATE_BOUNDARY_GRAPH_RIGIDITY_V1.md`;
- `ORIENTED_FULL_CHANNEL_LOCK_ELIMINATION_REPAIRED_V2.md`;
- `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V1.md`;
- `GENERAL_BRIDGELESS_FIVE_CDC_OUTER_SHELL_V1.md`.

**Status:** complete compressed authorial candidate. The proof of the cubic theorem requires no cyclic four-cut reduction. Type T/Type H four-cut mismatch elimination remains an independent strengthening, not a controlling dependency. The deep local theorem is singular contextual confluence for one fixed-route defect, not a collection of independent equality, DDD, Ptolemy, and Petersen global mechanisms.

**Assurance boundary:** authorial research candidate only. This document does not establish that the concrete hypotheses of the compressed packages have survived PDL reconstruction, independent audit, curation, Lean verification, manuscript integration, release, or peer review.

---

## 1. Natural theorem

Put

\[
E_5=\left\{x\in\mathbf F_2^5:\sum_{i=1}^5x_i=0\right\}
\]

and

\[
R_5=\{e_i+e_j:1\le i<j\le5\}.
\]

### Theorem 1.1 — cubic root-flow candidate

Every finite connected loopless bridgeless cubic multigraph `G` admits

\[
\lambda:E(G)\to R_5
\]

satisfying Kirchhoff conservation at every vertex.

Equivalently, `G` has five indexed even edge sets

\[
F_1,\ldots,F_5
\]

such that every edge belongs to exactly two of them.

At every cubic vertex the three root labels are the three edges of one triangle of `K_5`.

---

## 2. Minimal counterexample and bounded bases

Assume Theorem 1.1 false and choose a connected counterexample `G` with minimum vertex number.

A loop cannot occur in a connected bridgeless cubic graph: at a loop vertex the unique nonloop incident edge is a bridge.

The explicit bounded bases include:

- the two-vertex theta multigraph, with root triangle `12,13,23`;
- `K_4`, with the same root triangle on its three perfect-matching classes;
- the local parallel, triangle, and acyclic two-/three-port gadgets arising in low-cut reductions.

Every smaller connected loopless bridgeless cubic multigraph has a root-valued flow.

---

## 3. Only two- and three-cut reduction is required

### Cyclic two-cut

Complete each shore by one edge. Minimality gives root flows on the two completions. One global `S_5` support permutation aligns the two completion-edge roots; delete those edges and glue.

Hence `G` has no cyclic two-edge cut.

### Cyclic three-cut

Complete each shore by one cubic vertex. At the completion vertex the three roots form one support triangle. A global `S_5` permutation aligns the two ordered boundary triangles; delete the completion vertices and glue.

Hence `G` has no cyclic three-edge cut.

A connected acyclic cubic shore with `k` boundary incidences has

\[
n=k-2
\]

vertices. Thus the noncyclic two-/three-port cases are precisely the explicit bounded gadgets already removed.

### Important deletion

No cyclic four-cut theorem is used from this point onward.

---

## 4. Delete one arbitrary edge

Choose any edge

\[
uv\in E(G).
\]

Delete `u,v`, exposing four ordered terminal incidences

\[
a,b\mid c,d.
\]

Let

\[
P=G-\{u,v\}.
\]

The three perfect matchings of the terminals are

\[
M_i=ab\mid cd,
\qquad
M_j=ac\mid bd,
\qquad
M_k=ad\mid bc.
\]

For each `r`, let

\[
G_r=P\cup M_r.
\]

### Theorem 4.1 — all three smaller inputs

All three graphs `G_i,G_j,G_k` are connected loopless bridgeless cubic multigraphs with

\[
|V(G_r)|=|V(G)|-2.
\]

### Proof

Apply `FOUR_TERMINAL_MATCHING_CLOSURE_PRINCIPLE_V1.md`.

- Disconnected exterior would give a cyclic two-cut.
- Repeated terminal endpoints give one of the removed parallel/triangle bases or a cyclic two-/three-cut.
- New matching edges lie on paths in the connected exterior.
- An old bridge in a matching closure partitions the four terminals into the two matching blocks and gives a three-cut in `G`.

All alternatives were removed in Section 3. ∎

Minimality supplies a root flow on every `G_r`.

---

## 5. Three boundary profiles

Let `Sigma(P)` be the complete physical support-unordered boundary profile of the four-pole `P`.

The zero-vertex reconnection `M_r` has exact profile

\[
J_r=\{A,B_r,C_r\}.
\]

Restricting a root flow from `G_r` to `P` gives

\[
\boxed{
\Sigma(P)\cap J_r\ne\varnothing
\qquad(r=i,j,k).
}
\]

The original deleted vertices and edge form the standard two-vertex cap `cap_i`, whose exact profile is

\[
K_i=\{B_j,B_k,D_j,D_k\}.
\]

If

\[
\Sigma(P)\cap K_i\ne\varnothing,
\]

the cap and four-pole flows align after one global support permutation and glue to a root flow on `G`, contradiction.

Assume therefore that `K_i` is blocked.

---

## 6. The ten-state boundary graph fixes the route

For the fixed matching `M_i`, the complete ten-state transition graph is

\[
\boxed{
P_3\sqcup C_4\sqcup P_3
}
\]

with components

\[
J_i:\ A-B_i-C_i,
\]

\[
K_i:\ B_j-B_k-D_j-D_k-B_j,
\]

and

\[
L_i:\ C_j-D_i-C_k.
\]

By `TEN_STATE_BOUNDARY_GRAPH_RIGIDITY_V1.md`, the three-reconnection intersections and avoidance of `K_i` imply

\[
\boxed{
\Sigma(P)=J_i
\quad\text{or}\quad
\Sigma(P)=J_i\cup L_i.
}
\]

Moreover every realised complementary support-pair challenge has the same physical terminal route

\[
\boxed{M_i.}
\]

Thus equality, adjacent-root, and DDD cap failures are not separate global cases. They lie on one fixed-route outer sector.

---

## 7. One attempted cap insertion creates one singular token

Choose a root flow on one cross reconnection closure, say `G_j`.

Let its two reconnection edges carry roots

\[
p,q\in R_5.
\]

Restore the original cap topology formally. The central value is

\[
p+q.
\]

Exactly one of:

1. `p,q` are distinct and intersecting, so `p+q` is a root and the cap lifts;
2. `p=q`, so the central value is zero;
3. `p,q` are disjoint, so the central value is a co-root.

The first branch contradicts cap blocking immediately. The other two are the two singular fibres of one root triality.

There is exactly one singular edge and every other edge remains root-valued.

---

## 8. Fixed-route singular normalisation

A separating Kempe repair component converts the singular insertion into a root insertion and lifts the cap.

If every repair channel is locked, the fixed route orients the complete singular carrier. Equality and DDD current-flow potentials provide finite forward root-surgery histories. Their formulas are separate termination certificates, not separate global architectures.

A terminal root state on the reduced graph is arbitrary. Reverse transfer is governed by `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V1.md`.

Its concrete hypotheses are supplied by:

1. one-edge first-failure localisation;
2. zero-to-root triality;
3. bounded nonbranching co-root critical-overlap transport;
4. the unique full-state constant-pivot root section;
5. Petersen forced-backbone cycle reduction;
6. odd `C5,C9` resolution-parity exclusion;
7. the relative source-level `C6` star movie;
8. seam-compatible reduction of `C8` to two `C6` cells;
9. strict target-order decrease after genuine cancellation;
10. conversion of route and all direct-pairing outcomes to cap-compatible root terminals.

The master theorem uses lexicographic induction on

\[
\boxed{
(	ext{target order},	ext{remaining history length}).
}
\]

Therefore every cap-compatible terminal root state returns to the original four-pole context.

Consequently

\[
\boxed{
\Sigma(P)\cap K_i\ne\varnothing,
}

contradicting the blocked-cap assumption.

---

## 9. Cubic contradiction

The original cap now glues to `P`, giving a root-valued flow on `G`.

This contradicts the choice of `G` as a counterexample.

Therefore Theorem 1.1 holds for every finite connected loopless bridgeless cubic multigraph.

The proof used:

- two-cut reduction;
- three-cut reduction;
- all-three matching closures;
- ten-state boundary rigidity;
- singular contextual confluence.

It did not use cyclic four-cut gluing.

---

## 10. Disconnected cubic graphs

Apply the connected theorem independently to each component and unite equal-index supports across components.

The same index set

\[
\{1,2,3,4,5\}
\]

is retained, so the result still has exactly five indexed supports.

---

## 11. General finite bridgeless multigraphs

For a finite bridgeless multigraph `X`:

1. delete loops;
2. apply the standard port-cycle expansion to obtain a loopless bridgeless cubic multigraph `H`;
3. obtain five indexed even supports on `H`;
4. project the same five supports memberwise back to the original nonloop edges;
5. insert every deleted loop into two fixed support members.

Cut parity and exact double coverage are preserved.

### Theorem 11.1 — full 5-CDC candidate

Every finite bridgeless multigraph has five even edge sets

\[
F_1,\ldots,F_5
\]

such that every edge belongs to exactly two of them.

Equivalently, every finite bridgeless multigraph has a `5`-cycle double cover in the standard even-subgraph sense.

---

## 12. Controlling dependency spine

The compressed theorem DAG is:

\[
\boxed{
\begin{array}{c}
\text{root-flow equivalence and root triality}\\
\Downarrow\\
\text{two-/three-cut reduction}\\
\Downarrow\\
\text{four-terminal matching closures}\\
\Downarrow\\
\text{ten-state boundary graph rigidity}\\
\Downarrow\\
\text{singular contextual confluence}\\
\Downarrow\\
\text{cubic contradiction}\\
\Downarrow\\
\text{general-graph outer shell}.
\end{array}
}
\]

### Noncontrolling but valid side results

The following should not appear as prerequisites in the new PDL DAG:

- cyclic four-cut cap completion and shore-profile intersection;
- Type T mismatch elimination;
- Type H BBD/DDD mismatch elimination;
- cyclically five-edge-connected reduction;
- affine `A_3` translation and flat-code programmes;
- reflection-supported `D_8` cohomology programme;
- abstract longitudinal tube-to-history claims.

They remain independent structure, alternate certificates, historical routes, or possible future simplifications.

---

## 13. PDL reconstruction order

### Package A — intrinsic language

- root-flow/support equivalence;
- `K_5` triangle law;
- four-branch root triality;
- bridge-zero lemma.

### Package B — graph reduction

- bounded bases;
- two-cut gluing;
- three-cut gluing;
- four-terminal matching-closure principle.

### Package C — finite boundary theorem

- ten boundary states;
- `J_i,K_i,L_i`;
- `P_3 sqcup C_4 sqcup P_3` transition graph;
- physical fixed-route rigidity.

### Package D — singular confluence

- horizontal repair;
- equality and DDD termination certificates;
- first-failure localisation;
- full labelled token transport;
- odd/even recurrence theorem;
- singular confluence master theorem;
- cap-compatible terminal normalisation.

### Package E — outer shell

- componentwise cubic assembly;
- port-cycle expansion/collapse;
- loop reinsertion.

PDL should not reconstruct the discovery chronology.

---

## 14. Current authorial status

### Claimed

- one compressed correction-aware candidate proof architecture;
- removal of cyclic four-cut and Type T/H dependencies from the main theorem;
- an exact abstract singular-confluence theorem governing contextual return;
- a five-package PDL reconstruction plan.

### Not claimed

- successful independent reconstruction of every package;
- absence of an undiscovered hidden dependency;
- canonical project theorem status;
- Lean verification;
- manuscript or publication status;
- established truth of the 5-CDC conjecture.
