# Directed hexagon rewriting and the exact source-lifting frontier

## Research Lead theorem and scope dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `38bc17a30bd47d4ae462a458f6e5dc46f0b3a85e`.

**Parents:**

- `RELATIVE_PROJECTIVITY_HEXAGON_2_COMPLEX_V1.md`;
- `ROOT_SUPPORT_TRANSPORT_PROJECTIVITY_GROUPOID_V1.md`;
- `PTOLEMY_TRACK_FORCED_BACKBONE_SINK_ELIMINATION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `PETERSEN_C8_TWO_C6_HISTORY_FILLING_REDUCTION_V1.md`;
- `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V3.md`.

**Status:** exact abstract directed-rewriting theorem, exact diagrammatic-reducibility classification of the eleven-cell core, and exact source-lifting boundary. This dossier does not replace the controlling finite-condensation proof. It identifies a strictly smaller sufficient bypass theorem than arbitrary cellular-diagram realization.

---

## 1. The two projectivity complexes must be distinguished

Let

\[
\widetilde P
\]

be the orientation double cover of the Petersen pivot graph. Let `X_6` be obtained by attaching all twenty lifted primitive `C6` cells, and let `X_0` be the eleven-cell subcomplex selected in `RELATIVE_PROJECTIVITY_HEXAGON_2_COMPLEX_V1.md`.

The exact homotopy statements are

\[
X_0\searrow *,
\qquad
X_6\simeq\bigvee_1^9 S^2.
\]

Therefore:

1. `X_0` is contractible and collapsible;
2. `X_6` is simply connected but has nonzero `H_2` and `pi_2`;
3. no argument may infer diagrammatic reducibility of `X_6` merely from simple connectivity;
4. any directed reduction must use the selected core `X_0`, not the redundant full twenty-cell complex.

---

## 2. Every two-dimensional subcomplex of the core has a free edge

Use the spanning-tree coordinates

\[
g_1,\ldots,g_{11}
\]

and the selected cell order

\[
1,2,6,7,9,10,16,17,18,19,20.
\]

The first selected cell contains the non-tree edge `g_1`, and no other selected cell contains `g_1`. After deleting that cell, the remaining ten selected cells have pairwise distinct distinguished non-tree edges

\[
g_2,g_6,g_8,g_3,g_{10},g_5,g_4,g_{11},g_7,g_9,
\]

one per cell.

### Theorem 2.1 — hereditary free-face property

Let `Y` be any subcomplex of `X_0` containing at least one two-cell. Then `Y` contains a free one-face.

### Proof

If `Y` contains Cell 1, then `g_1` is incident to exactly that two-cell and is free.

Assume Cell 1 is absent, or collapse it first. Every remaining two-cell of `Y` contains its own distinguished non-tree edge from the displayed ten-edge list. That edge occurs in no other remaining selected cell. Hence it is free in `Y`. ∎

### Corollary 2.2 — hereditary collapse to a graph

Every subcomplex of `X_0` collapses to a one-complex.

Indeed repeatedly apply Theorem 2.1 until no two-cells remain.

### Corollary 2.3 — diagrammatic reducibility of the core

The selected core `X_0` is diagrammatically reducible.

One route is the Corson--Trace characterization: a two-complex is diagrammatically reducible exactly when every finite subcomplex of its universal cover collapses to a one-complex. Since `X_0` is contractible, it is its own universal cover, and Corollary 2.2 applies.

This conclusion is deliberately restricted to `X_0`. The full `X_6` is not diagrammatically reducible because it is simply connected with

\[
\pi_2(X_6)\cong H_2(X_6;\mathbf Z)\cong\mathbf Z^9\ne0.
\]

---

## 3. A terminating directed path-rewrite system

Fix the spanning tree `T` used by the finite certificate.

For each of the ten singleton-coordinate selected cells, orient its boundary relation so that the distinguished non-tree edge is replaced by the complementary five-edge tree path around that hexagon.

For Cell 1 orient the relation

\[
g_1g_7g_{11}^{-1}g_6^{-1}=1
\]

as a rewrite eliminating `g_1` in favour of a path using only

\[
g_6,g_7,g_{11}
\]

and tree edges.

### Definition 3.1 — rewrite rank

For an edge path `gamma` in `widetilde P`, define

\[
\mathcal R(\gamma)
=
\bigl(n_1(\gamma),n_{\mathrm{low}}(\gamma),|\gamma|\bigr),
\]

lexicographically, where:

- `n_1` is the number of occurrences of `g_1^{\pm1}`;
- `n_low` is the total number of occurrences of the other ten non-tree generators;
- length is used only after free reduction.

### Theorem 3.2 — termination

Every directed hexagon rewrite followed by free edge cancellation strictly decreases `mathcal R` after at most the two-stage schedule:

1. eliminate all `g_1` occurrences;
2. eliminate all remaining non-tree generators.

Hence every path reaches the unique reduced path in the tree `T` with the same endpoints.

### Proof

A Cell-1 rewrite removes one occurrence of `g_1` and introduces no new `g_1`, so the first coordinate decreases. Once `n_1=0`, each remaining selected rewrite removes one lower generator and introduces only tree edges, so the second coordinate decreases. A reduced tree path between fixed endpoints is unique. ∎

### Corollary 3.3 — abstract closed-path contraction

Every closed projectivity path in `widetilde P` reduces by the eleven directed hexagon rules and free backtrack cancellation to the empty path.

This is a constructive strengthening of `pi_1(X_0)=1`: it gives a terminating normalisation algorithm rather than an unspecified cellular disk.

---

## 4. Why abstract rewriting is still not a source proof

Let

\[
\mathscr S_N
\]

be the complete full-labelled contextual token graph at fixed target order `N`. A vertex retains source topology, atom position, ordered incidences, side roots, support transport, cap block, and route orientation. There is a natural projection

\[
\pi:\mathscr S_N\longrightarrow\widetilde P
\]

on persistent co-root states.

The established forced-backbone theorem proves only:

1. every actual persistent token relocation maps to one edge of `widetilde P`;
2. the actual crossed-route sheet transports without an independent bit;
3. a trapped actual path projects to a reduced Petersen walk.

It does **not** prove:

1. local surjectivity of `pi` on incident Petersen edges;
2. path lifting for the complementary five-edge arc of a selected hexagon;
3. existence of all six projectivity states in one common source context;
4. a cellular lift of the selected hexagon core.

Indeed `trapped implies forced` gives uniqueness of the actual transported route sheet; it does not manufacture the five alternative critical overlaps required by an abstract edge-to-five-edge rewrite.

Thus

\[
\boxed{
\text{transport projection}
\ne
\text{graph covering}
\ne
\text{cellular fibration}.
}
\]

---

## 5. The minimal sufficient bypass property

An arbitrary source-realizable van Kampen disk is stronger than necessary. The directed core shows that it suffices to lift only eleven oriented rewrite rules.

### Definition 5.1 — directed hexagon-lift property (`DHL`)

Fix one selected oriented hexagon `H` with distinguished edge `e` and complementary five-edge path `alpha`.

A contextual occurrence of `e` satisfies `DHL(H)` if exactly one of the following is produced:

1. a full-labelled contextual path lifting `alpha` with the same endpoints as the occurrence of `e`, together with a composition-safe source movie replacing the lifted `e` by that lifted path while preserving all exterior source incidences, side roots, cap block, and route data;
2. immediate complete root transfer;
3. route/profile escape;
4. bounded direct-pairing terminal;
5. separator/category discharge;
6. genuine equal-face cancellation to target order `N-2`.

The property is required for both orientations of the distinguished edge.

### Definition 5.2 — core `DHL`

The contextual projection has core `DHL` if every occurrence, inside a nonterminal same-order sink candidate, of every distinguished edge of the eleven selected cells satisfies Definition 5.1.

By Petersen symmetry it may be possible to prove core `DHL` from one equivariant local theorem, but no such equivariant source theorem is presently established.

---

## 6. Conditional directed-rewriting no-sink theorem

### Theorem 6.1

Assume at target order `N`:

1. the complete contextual graph `mathscr S_N` is finite;
2. constant-pivot runs and immediate physical backtracks are normalized;
3. persistent same-order states project to `widetilde P`;
4. core `DHL` holds;
5. every genuine cancellation invokes already established lower-order contextual return.

Then `mathscr S_N` has no nonterminal sink strongly connected component containing a persistent co-root token.

### Proof

Assume `K` is such a sink SCC. Choose a nontrivial closed reduced token path `Gamma` in `K`. Its projection

\[
gamma=\pi(\Gamma)
\]

is a closed edge path in `widetilde P`.

Apply the terminating rewrite system of Section 3. At the first directed rewrite, core `DHL` gives either an exit from `K`, contradicting sinkness, or a source-realizable replacement path in `K` with strictly smaller rewrite rank.

Repeat. Finiteness of the rank terminates at a path contained in the tree `T`. A closed reduced tree path is empty. Pulling back the free reductions gives only constant runs and immediate physical backtracks, both removed by Hypothesis 2. This contradicts the choice of a nontrivial persistent closed token path. ∎

### Corollary 6.2

Core `DHL` would replace all of the following recurrence ingredients at once:

- shortest repeated-pivot extraction;
- the simple-cycle list `C5,C6,C8,C9`;
- separate odd-cycle exclusion;
- the special `C8` two-`C6` recurrence disposition.

The strict source movie for the selected hexagon rules would become the sole recurrence engine.

---

## 7. What the current source theorems actually supply

### Available

`PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md` proves source-realizable strict descent when an **actual closed physical token track already has a simple `C6` reduced core**. All six critical-overlap states and their common side data are then present in one annular source neighbourhood.

`PETERSEN_C8_TWO_C6_HISTORY_FILLING_REDUCTION_V1.md` proves seam-compatible realization for an **actual simple `C8` track**, using two physically present `C6` factors.

### Not available

Neither theorem proves `DHL` at an arbitrary occurrence of one projectivity edge. In particular, they do not construct the complementary five-edge critical-overlap path from the local data of that one edge.

Consequently the implication

\[
\text{abstract selected-hexagon rewrite}
\Longrightarrow
\text{source history rewrite}
\]

remains open.

The current `C6/C8` shortest-core proof therefore remains controlling.

---

## 8. Correct architectural disposition

### Controlling now

Continue to use:

- orientation-hardened exclusion of odd pivot-closed physical subtracks;
- actual shortest simple core `C6` or `C8`;
- the existing source-level `C6` movie;
- seam-compatible `C8` reduction;
- finite-condensation no-sink theorem.

### Noncontrolling but exact

Use the projectivity core to state:

1. all abstract oriented recurrence is generated by primitive hexagons;
2. eleven directed rules suffice;
3. the selected core is diagrammatically reducible;
4. a bypass requires only core `DHL`, not arbitrary diagram realization.

### Research target

The sharp next theorem is:

> **Equivariant directed hexagon lifting.** In an oriented full-channel singular lock, every contextual occurrence of the distinguished edge of one selected projectivity hexagon either lifts the complementary five-edge path with complete source data or already yields a route, terminal, category, or strict-order exit.

A proof would genuinely remove the present Petersen cycle extraction from the controlling R2 argument.

---

## 9. External theorem boundary

The diagrammatic-reducibility terminology uses:

- J. M. Corson and B. Trace, *Diagrammatically reducible complexes and Haken manifolds*, Journal of the Australian Mathematical Society 69 (2000), 116--126: characterization by collapse of every finite subcomplex of the universal cover to a one-complex;
- J. Harlander and S. Rosebrock, *Directed diagrammatic reducibility*, Topology and its Applications 282 (2020), 107307: relative/directed versions and adapted combinatorial tests.

No external theorem is used to infer source-level colored-weld realization. That remains the internal AffineCDC frontier isolated above.

---

## 10. Trust boundary

### Exact here

- hereditary free-face property of the eleven-cell core;
- diagrammatic reducibility of `X_0`;
- non-diagrammatic-reducibility of the redundant full `X_6`;
- terminating eleven-rule projectivity rewrite;
- unique tree normal form;
- exact distinction between transport projection, graph covering, and cellular lifting;
- core `DHL` as a sufficient source-level bypass hypothesis;
- conditional no-sink theorem under core `DHL`;
- proof that existing actual-`C6/C8` source movies do not yet imply arbitrary-edge `DHL`.

### Not proved

- core `DHL` or its equivariant one-cell reduction;
- local surjectivity of the full contextual projection;
- a source-realizable complementary five-edge path at every occurrence;
- replacement of the controlling `C6/C8` recurrence proof;
- PDL reconstruction, independent audit, Lean verification, manuscript integration, release, arXiv, DOI, peer review, publication, or the global five-cycle double-cover theorem.