# Secondary defect minimality localises the final branch to three edges

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `9eb87498ac0a2421159fbed7c7ac781897d89c3c`  

**Parents:**

- `projects/affine-cdc/research/BRIDGELESS_ROOT_STAR_REPLACEMENT_V1.md`;
- `projects/affine-cdc/research/PIVOT_CHANGE_SIX_PORT_STAR_COMPLETION_V1.md`;
- the defect-minimal forest theorem;
- the vertex-minimal three-/four-cut reductions.

**Status:** exact conditional global localisation theorem. Refine the minimal-counterexample choice by first minimising source vertices and then minimising the number of non-root edges in an `E_5` flow. If the final residual branch contains the standard four-vertex co-root pivot path with six distinct exterior attachments, one root-valued star replacement is bridgeless and carries an `E_5` flow with three fewer defects. Hence that replacement graph cannot still be a counterexample. Pulling a root cover of the star graph back across the original path gives an `E_5` flow on the original graph with at most three defects. Since the selected defect-minimal flow already contains the three co-root path edges, the global defect minimum is exactly three and the complete defect support is precisely that path.  

**Not implied:** elimination of this three-edge normal form, handling of repeated exterior attachment vertices, transfer of the replacement root cover as a root cover of the original path, completion of the global induction, canonical acceptance, Lean verification, manuscript integration, or the global five-support theorem.

---

## 1. Global defect number

Let

\[
E_5=\{x\in\mathbf F_2^5:\sum_i x_i=0\},
\qquad
R_5=\{e_i+e_j:i<j\}.
\]

For a finite cubic graph `G`, let

\[
Z_1(G;E_5)
\]

be its `E_5`-valued flow space. Zero values are allowed.

For

\[
\lambda\in Z_1(G;E_5)
\]

define

\[
\delta(\lambda)
=
|\{e\in E(G):\lambda(e)\notin R_5\}|.
\]

Put

\[
\boxed{
\delta(G)
=
\min_{\lambda\in Z_1(G;E_5)}\delta(\lambda).
}
\]

A five-support root flow exists exactly when

\[
\delta(G)=0.
\]

Thus a five-support counterexample has

\[
\delta(G)>0.
\]

The minimum exists because the graph and coefficient space are finite.

---

## 2. Refined minimal-counterexample choice

Among all connected bridgeless cubic counterexamples, choose `G` lexicographically minimal for

\[
\boxed{
\bigl(|V(G)|,\delta(G)\bigr).
}
\]

Choose an `E_5` flow

\[
\lambda
\]

on `G` with

\[
\delta(\lambda)=\delta(G).
\]

All conclusions obtained from vertex minimality remain valid, because vertex count is the first coordinate. In particular, after the existing three-/four-cut reductions, `G` may be assumed cyclically five-edge-connected in the relevant minimal-counterexample regime.

The standard cycle-toggle argument applies to `lambda`, so its defect support is an induced forest with the established zero/co-root local grammar.

---

## 3. Final pivot-path hypothesis

Assume the residual defect forest contains one four-vertex path

\[
P=v_0v_1v_2v_3
\]

such that:

1. its three internal edges are co-root-valued;
2. its six exterior boundary edges are root-valued;
3. the local endpoint/transport grammar is the pivot-change cell;
4. the six exterior attachment vertices are distinct.

After support permutation its boundary and internal values may be written

\[
(12,35,45\mid25,34,15)
\]

and

\[
1235,
\qquad1234,
\qquad1345.
\]

Thus `P` contributes exactly three defect edges to `lambda`.

There may a priori be other defect components elsewhere in `G`.

---

## 4. Root-valued star replacement

The six-port star theorem gives four three-cherry star topologies carrying the same six boundary roots and having all three internal labels root-valued.

The bridgeless-star theorem gives at least one such topology `S` for which the replacement graph

\[
G_S
\]

is connected and bridgeless.

Retain `lambda` on every edge outside `P` and use the root-valued completion on `S`. This gives an `E_5` flow

\[
\lambda_S\in Z_1(G_S;E_5).
\]

No exterior value changes, and the three co-root edges are replaced by three root edges. Hence

\[
\boxed{
\delta(\lambda_S)=\delta(\lambda)-3.
}
\]

Consequently

\[
\delta(G_S)\le\delta(G)-3.
\]

The two graphs have the same number of vertices:

\[
|V(G_S)|=|V(G)|.
\]

---

## 5. The star graph is soluble

### Theorem 5.1

The bridgeless replacement graph `G_S` is not a five-support counterexample.

### Proof

If `G_S` were a counterexample, then

\[
\bigl(|V(G_S)|,\delta(G_S)\bigr)
<
\bigl(|V(G)|,\delta(G)\bigr),
\]

because the vertex counts agree and

\[
\delta(G_S)\le\delta(G)-3.
\]

This contradicts the refined minimal choice of `G`. ∎

Therefore `G_S` has a root-valued flow

\[
\rho:E(G_S)\to R_5.
\]

---

## 6. Pulling the root cover back as an `E_5` flow

Restrict `rho` to the common exterior graph

\[
G-V(P)=G_S-V(S).
\]

Its six terminal values are roots and have total sum zero.

A flow on a tree is uniquely determined by its boundary values: the value of each internal edge is the sum of the terminal values on either shore of that edge.

Hence the six boundary roots extend uniquely across the original path `P` to an `E_5` flow. Denote the resulting global flow on `G` by

\[
\widetilde\rho.
\]

Every exterior edge remains root-valued. Only the three internal edges of `P` may be zero or co-root.

Thus

\[
\boxed{
\delta(\widetilde\rho)\le3.
}
\]

Therefore

\[
\boxed{
\delta(G)\le3.
}
\]

---

## 7. Exact three-defect localisation

The selected flow `lambda` already has the three co-root internal edges of `P`. Therefore

\[
\delta(G)=\delta(\lambda)\ge3.
\]

Together with Section 6:

### Theorem 7.1 — global three-edge normal form

\[
\boxed{
\delta(G)=3.
}
\]

Moreover the complete defect support of `lambda` is exactly

\[
\boxed{E(P).}
\]

There are no zero or co-root defects outside the four-vertex pivot path.

### Proof

The inequalities give equality. Since the three internal edges of `P` already account for all three defects of `lambda`, every exterior edge is root-valued. ∎

### Corollary 7.2

Every root cover `rho` of the chosen bridgeless star graph, when pulled back to the original path, produces exactly three non-root internal values.

If one pullback had at most two defects, it would contradict

\[
\delta(G)=3.
\]

Thus the complete replacement profile is confined to the all-three-defective path sector.

---

## 8. Consequence for the old unbounded frontier

Before the secondary-minimality argument, the defect forest could contain:

- multiple zero branches;
- several co-root strips;
- arbitrary side-root attachments;
- several pivot changes.

Under the final pivot-path hypothesis, all of this disappears.

The complete residual graph-level defect object is now:

\[
\boxed{
\text{one induced four-vertex path}
\quad+
\text{three co-root internal edges}
\quad+
\text{six root boundary edges}.}
\]

All exterior graph data are carried by a genuine root-valued flow.

Thus the remaining theorem may be attacked using one repair root, one matching-plus-Tait blocker network, and the six terminal attachment pattern; no additional defect component must be tracked.

---

## 9. Why this does not yet prove root cover transfer

The root flow `rho` on `G_S` need not extend root-valuedly across the original path. Indeed Theorem 7.1 shows that every pullback remains defective on all three internal edges.

The gain is instead global localisation:

- root-cover transfer failure cannot escape into another defect component;
- every blocking cycle and side network lies in the root-valued exterior;
- all horizontal moves may be measured against one fixed three-edge defect spine;
- any new defect away from `P` contradicts the secondary minimum unless accompanied by an immediate reduction of the path defects.

This is the correct setting for the final blocker-distance / laminar-enclosure argument.

---

## 10. Repeated exterior vertices

If the six boundary semiedges do not meet six distinct exterior vertices, the bridgeless-star theorem is not directly available.

Such configurations form bounded five-or-fewer-attachment multipoles and must be discharged before consuming Theorem 7.1.

The present theorem is exact on the distinct-attachment branch.

---

## 11. Revised final target

Starting from the three-edge normal form, choose the unique root shift repairing all three co-roots. For the standard labels this is

\[
\boxed{a=13.}
\]

The root-valued exterior decomposes relative to `a` into:

- safe Kempe cycles;
- isolated `a`-matching edges;
- complementary rank-two Tait multipoles.

Defect minimality forbids a cycle consisting of the three-edge spine plus an exterior path whose blocker cost is at most two.

The remaining theorem should prove that a blocker distance of at least three yields one of:

1. a small cut or serial interval;
2. a peelable matching/Tait band;
3. a zero-cost horizontal relocation of the entire three-edge defect path;
4. a bounded equality/DDD return;
5. contradiction to cyclic five-edge connectivity.

This is now a one-spine exterior-root problem.

---

## 12. Trust boundary

### Exact here

- the refined minimal-counterexample order;
- the three-defect decrease under a root-valued star replacement;
- solubility of the bridgeless star graph by secondary minimality;
- unique `E_5` pullback across the original tree;
- the upper bound `delta(G)<=3`;
- equality `delta(G)=3` under the pivot-path hypothesis;
- localisation of the complete defect support to that path.

### Conditional inputs

- existence of the final four-vertex co-root pivot path in the chosen defect-minimal flow;
- six distinct exterior attachment vertices;
- the previously proved bridgeless root-star replacement theorem.

### Still open

- bounded repeated-attachment configurations;
- elimination of the global three-edge normal form;
- the blocker-distance / safe-cycle composition theorem;
- global horizontal induction after defect relocation;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
