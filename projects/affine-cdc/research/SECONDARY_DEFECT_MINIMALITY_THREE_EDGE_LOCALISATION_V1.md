# Secondary defect minimality localises the final branch to three edges

## Research dossier v2

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Original parent head:** `9eb87498ac0a2421159fbed7c7ac781897d89c3c`  
**v2 correction:** consumes `BRIDGELESS_ROOT_STAR_REPLACEMENT_V1.md` v2, with arbitrary exterior attachment coincidences.  

**Parents:**

- `projects/affine-cdc/research/BRIDGELESS_ROOT_STAR_REPLACEMENT_V1.md`;
- `projects/affine-cdc/research/PIVOT_CHANGE_SIX_PORT_STAR_COMPLETION_V1.md`;
- the defect-minimal forest theorem;
- the vertex-minimal three-/four-cut reductions.

**Status:** exact conditional global localisation theorem with no distinct-attachment hypothesis. Refine the minimal-counterexample choice by first minimising source vertices and then minimising the number of non-root edges in an `E_5` flow. If the final residual branch contains the standard four-vertex co-root pivot path, one root-valued star replacement is bridgeless and carries an `E_5` flow with three fewer defects. Hence that replacement graph cannot still be a counterexample. Pulling a root cover of the star graph back across the original path gives an `E_5` flow on the original graph with at most three defects. Since the selected defect-minimal flow already contains the three co-root path edges, the global defect minimum is exactly three and the complete defect support is precisely that path.  

**Not implied:** elimination of this three-edge normal form by this dossier alone, transfer of the replacement root cover as a root cover of the original path, completion of the full proof DAG before the pivot-path hypothesis is reached, canonical acceptance, Lean verification, manuscript integration, or the global five-support theorem.

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

be its `E_5`-valued flow space; zero values are allowed.

For

\[
\lambda\in Z_1(G;E_5)
\]

define

\[
\delta(\lambda)
=
|\{e\in E(G):\lambda(e)\notin R_5\}|,
\]

and put

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

Thus a five-support counterexample has positive defect minimum.

---

## 2. Refined minimal-counterexample choice

Among all connected bridgeless cubic counterexamples, choose `G` lexicographically minimal for

\[
\boxed{
\bigl(|V(G)|,\delta(G)\bigr).
}
\]

Choose

\[
\lambda\in Z_1(G;E_5)
\]

with

\[
\delta(\lambda)=\delta(G).
\]

All vertex-minimal conclusions remain valid because vertex count is the first coordinate. The cycle-toggle argument gives the established induced defect-forest grammar for `lambda`.

---

## 3. Final pivot-path hypothesis

Assume the residual defect forest contains one four-vertex path

\[
P=v_0v_1v_2v_3
\]

such that:

1. its three internal edges are co-root-valued;
2. its six exterior boundary incidences are root-valued;
3. the local endpoint/transport grammar is the pivot-change cell.

The six terminal incidences may meet arbitrary exterior vertices; coincidences are allowed.

After support permutation, the boundary and internal values may be written

\[
(12,35,45\mid25,34,15)
\]

and

\[
1235,
\qquad1234,
\qquad1345.
\]

Thus `P` contributes exactly three defects to `lambda`. There may a priori be other defect components elsewhere in `G`.

---

## 4. Root-valued star replacement

The six-port star theorem gives four three-cherry star topologies carrying the same six boundary roots and having all three internal labels root-valued.

The bridgeless-star theorem v2 applies to terminal incidences, not exterior vertices. Hence at least one such star `S` gives a connected bridgeless replacement graph

\[
G_S.
\]

Retain `lambda` outside `P` and use the root-valued completion on `S`. This gives

\[
\lambda_S\in Z_1(G_S;E_5)
\]

with

\[
\boxed{
\delta(\lambda_S)=\delta(\lambda)-3.
}
\]

The two graphs have equal vertex count.

---

## 5. The star graph is soluble

### Theorem 5.1

The bridgeless replacement graph `G_S` is not a five-support counterexample.

### Proof

If it were, then

\[
\delta(G_S)\le\delta(\lambda_S)=\delta(G)-3,
\]

while

\[
|V(G_S)|=|V(G)|.
\]

This contradicts the refined lexicographic choice of `G`. ∎

Therefore `G_S` has a root-valued flow

\[
\rho:E(G_S)\to R_5.
\]

---

## 6. Pulling the root cover back as an `E_5` flow

Restrict `rho` to the common exterior graph. Its six terminal values are roots with total sum zero.

A flow on a tree is uniquely determined by its boundary values. Hence the six boundary roots extend uniquely across the original path `P` to an `E_5` flow

\[
\widetilde\rho
\]

on `G`.

Every exterior edge remains root-valued. Only the three internal path edges may be zero or co-root. Thus

\[
\boxed{
\delta(\widetilde\rho)\le3,
}
\]

and therefore

\[
\boxed{
\delta(G)\le3.
}
\]

---

## 7. Exact three-defect localisation

The selected flow `lambda` already has the three co-root internal edges of `P`. Hence

\[
\delta(G)=\delta(\lambda)\ge3.
\]

Combining with the preceding upper bound:

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

There are no zero or co-root defects outside the pivot path.

### Corollary 7.2

Every root cover of the chosen bridgeless star graph, when pulled back across the original path, has exactly three non-root internal values. A pullback with at most two defects would contradict `delta(G)=3`.

---

## 8. Consequence for the old unbounded frontier

Before secondary minimality, the defect forest could contain multiple zero branches, several co-root strips, arbitrary side-root attachments, and several pivot changes.

Under the final pivot-path hypothesis, the entire residual defect object is

\[
\boxed{
\text{one induced four-vertex path}
+
\text{three co-root internal edges}
+
\text{six root boundary incidences}.}
\]

All exterior graph data are carried by a genuine root-valued flow.

This is consumed by

`THREE_CO_ROOT_PATH_ENDPOINT_EQUALISATION_ELIMINATION_V1.md`,

which eliminates the normal form by a zero-cost endpoint relocation followed by a two-vertex dipole cancellation.

---

## 9. Trust boundary

### Exact here

- the refined minimal-counterexample order;
- the three-defect decrease under a root-valued star replacement;
- applicability with arbitrary exterior attachment coincidences;
- solubility of the bridgeless star graph by secondary minimality;
- unique `E_5` pullback across the original tree;
- the upper bound `delta(G)<=3`;
- equality `delta(G)=3` under the pivot-path hypothesis;
- localisation of the complete defect support to that path.

### Conditional input

- the preceding reductions must produce the final four-vertex co-root pivot path in the chosen defect-minimal flow.

### Still open

- verification that the complete earlier proof DAG reaches the pivot-path hypothesis with no omitted branch;
- global well-founded packaging;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
