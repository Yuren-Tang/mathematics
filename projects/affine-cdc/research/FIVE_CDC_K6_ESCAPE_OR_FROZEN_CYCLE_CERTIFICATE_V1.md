# Dual K6 escape or frozen-cycle certificate

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level structural checkpoint; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_FACE_TRANSITION_OBSTRUCTION_ARRANGEMENT_V1.md`, `FIVE_CDC_GAUGE_PARTIAL_PETRIAL_CORRESPONDENCE_V1.md`

## 1. Setup

Fix a nowhere-zero Fano flow `f` on a connected cubic loopless multigraph `G`. Let

\[
B_f\leq \mathbf F_2^{E(G)}
\]

be its reduced gauge / partial-Petrial code. Fix one gauge state `\beta`, with cycle-face embedding `S_\beta` and dual closed triangulation `T_\beta`.

Let `X` be a marked six-set of dual vertices spanning a `K_6` in `T_\beta`. The vertices of `X` are six marked face-side circuits of `S_\beta`.

Define the **face zone**

\[
Z_X\subseteq E(G)
\]

to be the set of source edges traversed by at least one of these six marked faces. Equivalently, these are the primal edges whose dual edge is incident with at least one vertex of `X`.

Let

\[
\rho_X:B_f\longrightarrow \mathbf F_2^{Z_X},
\qquad
\rho_X(\lambda)=\lambda|_{Z_X},
\]

and put

\[
r_X:=\operatorname{rank}\rho_X.
\]

Call a source edge `e` **untwistable** for `f` when

\[
\lambda_e=0
\qquad\text{for every }\lambda\in B_f.
\]

Equivalently, the coordinate functional at `e` vanishes on `B_f`, or the unit coordinate vector `1_e` belongs to `B_f^\perp`.

## 2. Pointwise escape versus rigidity

### Theorem 2.1 — marked K6 escape-or-rigidity

Exactly one of the following holds.

1. **Gauge-exposed core:** `r_X>0`. Then there is an admissible gauge word `\lambda\in B_f` such that the six old face-side circuits do not all persist. Hence the marked copy `X` of `K_6` is destroyed.
2. **Pointwise-rigid core:** `r_X=0`. Then every source edge in `Z_X` is untwistable, and the same six face-side circuits, with all their mutual dual adjacencies, persist in every state of the gauge fibre.

#### Proof

By the marked-face stabilizer theorem, the occurrence locus of the same six face-side circuits is

\[
\beta+\ker\rho_X.
\]

If `r_X>0`, choose `\lambda\in B_f` with `\rho_X(\lambda)\neq0`. At some source edge traversed by one of the marked faces, the edge transition is crossed, so that old face-side dart set is no longer invariant. Thus the marked six-face system and hence the marked `K_6` disappear.

If `r_X=0`, then `\rho_X=0`; every gauge word vanishes on all of `Z_X`. All edge transitions used by the six marked faces are unchanged, so the six circuits and their witnessing dual edges persist pointwise throughout the fibre. ∎

This theorem concerns one marked core. A move may destroy it while creating a different `K_6`; the fixed thirty-vertex obstruction exhibits exactly this clique-renewal phenomenon.

## 3. Topological refinement

For a `K_6` on vertex set `X` in a connected simplicial closed triangulation, call a clique edge `xy` **externally exposed** when one incident triangular face is `xyz` with `z\notin X`.

Let `H_X` be the graph on `X` formed by the externally exposed clique edges.

The projective-core lemma gives:

- either `T_\beta` has exactly the six vertices `X`, in which case it is the unique six-vertex triangulation of `\mathbb{RP}^2` and its cellular dual is the Petersen graph;
- or `H_X` contains a cycle.

### Theorem 3.1 — K6 escape or frozen exposed cycle

For every marked dual `K_6` on `X`, exactly one of the following alternatives holds.

1. `r_X>0`, and some admissible partial Petrial destroys the marked `K_6`;
2. `T_\beta` is the six-vertex projective-plane triangulation and `r_X=0`, so the whole Petersen/projective core is rigid throughout the gauge fibre;
3. `T_\beta` has more than six vertices, and there is a cycle
   \[
   Q\subseteq H_X
   \]
   all of whose dual edges correspond to untwistable source edges.

#### Proof

If `r_X>0`, apply Theorem 2.1. Assume `r_X=0`. Then every edge in the complete face zone `Z_X` is untwistable.

If `T_\beta` has only the six vertices of `X`, the projective-core lemma gives Alternative 2.

Otherwise the exposed-edge graph `H_X` contains a cycle `Q`. Every edge of `H_X` is dual to a source edge incident with a face in `X`, hence belongs to `Z_X`, and is therefore untwistable. This gives Alternative 3. The alternatives are mutually exclusive. ∎

The cycle in Alternative 3 is a concrete dual-code obstruction certificate: its edge-coordinate functionals lie in `B_f^\perp`, so no fixed-flow gauge move can alter any of those face-side identifications.

## 4. Acyclic frozen-edge criterion

Let

\[
U_f:=\{e\in E(G):\lambda_e=0\text{ for every }\lambda\in B_f\}
\]

be the untwistable edge set. In a gauge state `\beta`, regard the dual edges `U_f^*` as a subgraph of `T_\beta`.

### Corollary 4.1

Assume

\[
B_f\neq0
\]

and the dual subgraph `U_f^*` is acyclic. Then every marked `K_6` in `T_\beta` has positive exposure rank.

#### Proof

Suppose a marked `K_6` had `r_X=0`. If the triangulation had more than six vertices, Theorem 3.1 would give a cycle in `U_f^*`, contradiction.

If the triangulation had exactly six vertices, its face zone is all of `E(G)`. Since `B_f\neq0`, some gauge word has a nonzero coordinate on that zone, so `r_X>0`, again a contradiction. ∎

Thus acyclicity of the frozen dual edges rules out every pointwise-rigid `K_6`. It does not by itself rule out clique renewal.

## 5. Quantitative fibre escape

Let `\mathfrak K_f` be the finite set of all marked `K_6` cores occurring anywhere in the gauge fibre, and let `r(C)` be their exposure ranks.

### Corollary 5.1

If

\[
\sum_{C\in\mathfrak K_f}2^{-r(C)}<1,
\]

then some gauge state has a `K_6`-free dual triangulation.

In particular, if every marked core has exposure rank at least `r` and

\[
|\mathfrak K_f|<2^r,
\]

then the fibre contains a `K_6`-free state.

#### Proof

Each marked core occurs on an affine subspace of relative density `2^{-r(C)}`. Apply the union bound to the complete marked-core arrangement. ∎

Combining Corollaries 4.1 and 5.1 gives a usable two-stage strategy:

1. topology and the dual gauge code eliminate rigid local cores;
2. arrangement density or exact Möbius inversion eliminates global clique renewal.

## 6. Mechanism exposed

The visible `K_6` obstruction now has a strict hierarchy.

1. **Local point obstruction:** one marked clique.
2. **Frozen topological obstruction:** a projective Petersen core or an untwistable exposed dual cycle.
3. **Renewal obstruction:** every marked clique is individually destructible, but their affine occurrence loci cover the whole gauge torsor.

The fixed thirty-vertex example lies at Level 3: all nine marked cliques in its two-state fibre have exposure rank one, yet their singleton occurrence loci cover both gauge states.

The next problem is therefore not merely to twist one visible clique. It is to prove that the complete marked-core arrangement cannot cover the gauge fibre, or else to convert a minimal irredundant cover into a coherent family of frozen cycles / projective cores and then into a graph decomposition or gluing theorem.

No statement here proves that every fixed-flow fibre has a `K_6`-free state, that every `K_6`-free compatible dual maps to `\mathscr A_5`, or that every cubic graph has a five-support cycle double cover.
