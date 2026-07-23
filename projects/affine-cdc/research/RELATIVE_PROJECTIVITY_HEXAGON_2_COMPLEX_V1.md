# The oriented Petersen projectivity cover has a collapsible hexagon core

## Research Lead theorem dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `6804f413aa05efd3b3f98e4737d5cf8e04fd1032`.

**Parents:**

- `ROOT_SUPPORT_TRANSPORT_PROJECTIVITY_GROUPOID_V1.md`;
- `ORIENTED_ODD_PETERSEN_SUBTRACK_EXCLUSION_V1.md`;
- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `PETERSEN_C8_TWO_C6_HISTORY_FILLING_REDUCTION_V1.md`.

**Purpose:** replace the appearance that admissible projectivity recurrence requires a primitive `C6/C8` cycle list by one finite two-complex. The orientation double cover of the Petersen pivot graph becomes simply connected after attaching the primitive `C6` projectivity cells; in fact eleven selected hexagons form a collapsible core containing the complete one-skeleton. Every lifted `C8` boundary is already the oriented sum of two lifted `C6` boundaries.

**Status:** exact finite projectivity theorem with a reproducible Wolfram certificate. It is a theorem about the abstract full-labelled projectivity state cover. It does **not** by itself prove that an arbitrary cellular null-homotopy lifts to a composition-safe sequence of source-graph surgeries with all side attachments retained.

---

## 1. Petersen projectivity graph and its orientation cover

Let

\[
P=KG(5,2)
\]

be the Petersen graph on the ten roots

\[
R_5=\binom{[5]}2,
\]

with two roots adjacent exactly when they are disjoint.

The forced co-root token at one step is one Petersen edge. The cap-distinguished route block gives one orientation bit which toggles at every pivot edge. Therefore the natural oriented projectivity graph is the bipartite double cover

\[
\widetilde P=P\times\mathbf F_2,
\]

with

\[
(r,b)\sim(s,b+1)
\qquad(rs\in E(P)).
\]

It has

\[
|V(\widetilde P)|=20,
\qquad
|E(\widetilde P)|=30,
\]

is connected and bipartite, and has cycle rank

\[
30-20+1=11.
\]

A physical pivot-closed path satisfying the oriented-cap condition lifts to a closed path in `\widetilde P`. Conversely every closed path in `\widetilde P` projects to an even closed Petersen walk.

---

## 2. Primitive projectivity hexagons

The Petersen graph has exactly ten simple `C6` cycles. In the source interpretation each is the identity hexagon for one active root. Every even cycle lifts to two cycles in the orientation cover, so `\widetilde P` has exactly twenty lifted primitive hexagons.

For every lifted `C6` attach one two-cell along its boundary. Denote the resulting two-complex by

\[
\boxed{X_6.}
\]

Thus

\[
X_6^{(1)}=\widetilde P,
\qquad
f_2(X_6)=20.
\]

The main theorem is stronger than simple connectivity: only eleven of these twenty cells are needed to obtain a collapsible subcomplex with the same one-skeleton.

---

## 3. A spanning-tree presentation

Choose the deterministic spanning tree returned by the finite certificate in Section 9. Collapse that tree. The graph fundamental group becomes the free group on the eleven non-tree edges

\[
g_1,\ldots,g_{11}.
\]

With the corresponding deterministic enumeration of the twenty lifted hexagons, the complete `C6` relator list is:

\[
\begin{aligned}
&(1,7,-11,-6),\\
&(-2),\\
&(-8,-2,6),\\
&(-11,-6,4),\\
&(9,10,4),\\
&(-6),\\
&(-8),\\
&(10,8,-3),\\
&(-3),\\
&(-10),\\
&(7,9,-5),\\
&(-1,4,9,-5),\\
&(-1,2,-10,-5),\\
&(3,-8,-2,1),\\
&(3,11,-7),\\
&(-5),\\
&(4),\\
&(11),\\
&(7),\\
&(-9).
\end{aligned}
\]

Here `(a_1,\ldots,a_k)` denotes the group word

\[
g_{|a_1|}^{\operatorname{sgn}(a_1)}\cdots
 g_{|a_k|}^{\operatorname{sgn}(a_k)}.
\]

Select the eleven cells with indices

\[
\boxed{
1,2,6,7,9,10,16,17,18,19,20.
}
\]

Their relators are

\[
\boxed{
\begin{aligned}
&g_1g_7g_{11}^{-1}g_6^{-1},\\
&g_2^{-1},\ g_6^{-1},\ g_8^{-1},\ g_3^{-1},\ g_{10}^{-1},\\
&g_5^{-1},\ g_4,\ g_{11},\ g_7,\ g_9^{-1}.
\end{aligned}}
\]

---

## 4. Collapsible eleven-cell core

Let `X_0` be the subcomplex consisting of the full one-skeleton `\widetilde P` and the eleven selected hexagonal two-cells.

### Theorem 4.1 — explicit elementary collapse

\[
\boxed{X_0\searrow * .}
\]

### Proof

In the selected cell set, the non-tree edge `g_1` occurs in only the first hexagon. It is therefore a free one-face of that two-cell. Collapse the first hexagon across `g_1`.

After that collapse, each of the ten remaining selected cells has exactly one non-tree edge, respectively

\[
g_2,g_6,g_8,g_3,g_{10},g_5,g_4,g_{11},g_7,g_9,
\]

and that edge occurs in no other remaining selected two-cell. Collapse those ten cell-edge pairs successively.

The remaining complex is precisely the chosen spanning tree. Collapse its edges to one vertex. Therefore `X_0` is collapsible. ∎

### Corollary 4.2

The eleven selected `C6` relators normally generate the complete free group

\[
\pi_1(\widetilde P)\cong F_{11}.
\]

Indeed the ten singleton relators kill `g_2,\ldots,g_{11}`, and the first relator then kills `g_1`.

---

## 5. The full hexagon complex

Since `X_0` contains the complete one-skeleton, each of the nine remaining hexagon boundaries is a loop in the contractible complex `X_0` and is therefore null-homotopic there.

### Theorem 5.1 — homotopy type

\[
\boxed{
X_6\simeq\bigvee_{1}^{9}S^2.
}
\]

In particular

\[
\boxed{\pi_1(X_6)=1.}
\]

### Proof

Attach the remaining nine two-cells one at a time to the contractible complex `X_0`. Every attaching map is null-homotopic in `X_0`, so each attachment wedges on one two-sphere. ∎

The cellular Euler characteristic agrees:

\[
\chi(X_6)=20-30+20=10
=1+9.
\]

### Integral homology certificate

The twenty oriented hexagon boundaries span the full integral cycle lattice of `\widetilde P`. Relative to the eleven non-tree coordinates, their Smith diagonal is

\[
\boxed{1,1,1,1,1,1,1,1,1,1,1.}
\]

Hence

\[
H_1(X_6;\mathbf Z)=0,
\qquad
H_2(X_6;\mathbf Z)\cong\mathbf Z^9.
\]

This agrees with the explicit collapsible-core proof and is not merely a mod-two calculation.

---

## 6. Every oriented `C8` is a two-hexagon boundary

The Petersen graph has fifteen simple `C8` cycles. They lift to thirty simple `C8` cycles in `\widetilde P`.

### Theorem 6.1 — exact two-cell decomposition

For every lifted oriented `C8` boundary `\gamma`, there are exactly two unordered pairs of lifted primitive hexagons `H,H'` with orientation signs `\epsilon,\epsilon'\in\{\pm1\}` such that

\[
\boxed{
\partial\gamma
=
\epsilon\,\partial H+
\epsilon'\,\partial H'
}
\]

as integral one-chains.

Equivalently, over `\mathbf F_2`, every lifted `C8` is the symmetric difference of two lifted `C6` cycles, again in exactly two ways.

Thus the `C8` projectivity cell is not primitive. Its source-level role is the first nontrivial composition of two primitive `C6` colored-weld cells.

---

## 7. Projectivity consequence

### Theorem 7.1 — abstract recurrence generation

Every orientation-admissible closed projectivity path is generated, up to path homotopy, by primitive lifted `C6` relations.

### Proof

An admissible closed path is a loop in `\widetilde P=X_6^{(1)}`. Since `X_6` is simply connected, the loop bounds a cellular disk whose two-cells are lifted primitive hexagons. ∎

This replaces the following abstract recurrence classification:

\[
C_5,C_6,C_8,C_9
\]

by one statement:

\[
\boxed{
\text{oriented projectivity recurrence is generated by the }C_6\text{ cells}.
}
\]

- `C5,C9` do not lift to closed one-lap paths because they reverse the orientation sheet;
- `C6` is primitive;
- `C8` is a two-cell composite;
- arbitrary longer recurrence is a van Kampen diagram over the same hexagons.

---

## 8. Source-realization boundary

The theorem above is exact at the projectivity level. It does **not** yet replace the concrete source proof.

A projectivity hexagon has a strict source realization only when:

1. all six root-labelled local states are realized in one common source context;
2. ordered side-root attachments are retained;
3. the cap-distinguished block is transported consistently;
4. the relative NNI to the canonical star is category-safe;
5. the equal-face cancellation is a genuine lower-order source cancellation.

The existing `C6` source movie proves this for one primitive cell. The existing `C8` theorem proves seam-compatible realization for the first two-cell composite.

The missing general compression theorem is:

> **Relative projectivity diagram realization.** Every cellular disk over the collapsible hexagon core either admits a source-realizable exposed hexagon move, or its first failure gives a route escape, bounded terminal, category discharge, or strictly smaller target context.

Until that theorem is proved, the current finite-condensation proof remains controlling. The projectivity complex supplies a conceptual and finite presentation of the recurrence mechanism, not an automatic source-level weld.

---

## 9. Wolfram finite certificate

A direct Wolfram computation gives:

\[
\begin{array}{c|c}
\text{quantity}&\text{value}\\
\hline
|V(P)|,|E(P)|&10,15\\
\#C_6(P)&10\\
\#C_8(P)&15\\
|V(\widetilde P)|,|E(\widetilde P)|&20,30\\
\#C_6(\widetilde P)&20\\
\#C_8(\widetilde P)&30\\
\dim Z_1(\widetilde P;\mathbf F_2)&11\\
\operatorname{rank}_{\mathbf F_2}\langle C_6\rangle&11.
\end{array}
\]

For every one of the thirty lifted `C8` cycles, exactly two pairs of lifted `C6` cycles give its mod-two boundary. The same count remains two for signed integral decompositions.

For the selected eleven relators, the abelianized `11\times11` matrix has

\[
\det=-1.
\]

This verifies that their boundaries form a unimodular basis of the integral cycle lattice. The nonabelian relator elimination and the explicit free-face collapse prove the stronger simple-connectivity and collapsibility statements.

The certificate uses only:

- `GraphData["PetersenGraph"]`;
- the canonical sheet-toggling double cover;
- `FindCycle[...,{6},All]` and `FindCycle[...,{8},All]`;
- one spanning tree;
- integer incidence vectors and `SmithDecomposition`.

---

## 10. Architectural consequence

The projectivity part of R2 should be presented as:

\[
\boxed{
\text{oriented cover}
+
\text{collapsible }C_6\text{ core}
+
\text{source realization of its cells}.
}
\]

Petersen cycle lengths are now a finite presentation certificate, not the intrinsic theorem statement.

What remains genuinely mathematical is not classification of abstract recurrence. It is functorial lifting from the collapsible projectivity two-complex to full source-labelled colored-weld histories.

---

## 11. Trust boundary

### Exact here

- construction of the orientation double cover;
- counts of primitive `C6` and `C8` cycles;
- cycle rank eleven;
- explicit eleven-hexagon collapsible core;
- trivial fundamental group of the full hexagon complex;
- homotopy type `\bigvee^9S^2`;
- integral and mod-two cycle-lattice generation;
- exact two-hexagon decomposition of every lifted `C8` boundary;
- identification of primitive recurrence with the lifted `C6` cells.

### Not claimed

- source-level realization of an arbitrary projectivity van Kampen diagram;
- replacement of the existing `C6/C8` source movies in the controlling proof;
- PDL reconstruction or independent audit;
- Lean formalization, manuscript integration, release, arXiv, DOI, peer review, publication;
- established truth of the five-cycle double-cover conjecture.
