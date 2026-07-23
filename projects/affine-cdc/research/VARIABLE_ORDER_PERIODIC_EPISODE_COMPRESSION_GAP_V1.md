# Variable-order periodic episodes are not yet fixed-order Ptolemy cylinders

## Research Lead material scope correction v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Corrects the completion classification of:**

- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V5.md` v5.0--v5.2;
- the unsupported fixed-order sentence in `CONTEXTUAL_TRANSFER_REPAIR_FRONTIER_V2.md`, Section 4;
- any reading of `PERIODIC_OUTER_ENDPOINT_ROOT_SEAM_DISCHARGE_V1.md` without its fixed-order normalization hypothesis.

**Status:** `MATERIAL GAP / R2.7 REMAINS BLOCKED`.

The periodic root-cylinder crosscut theorem is exact **once** a repeated endpoint episode is represented by a fixed-order lifted Ptolemy/history cylinder. The order-restoring local inverse table does not by itself construct that cylinder. A continuation episode may descend through one or more equal-face cancellations, change the root flow on the smaller graph, and only later return by original or alternative insertions. Restoring predecessor order at the return endpoint does not lift the intervening lower-order flow evolution through the deleted pair.

This is the sole newly exposed interface between the local cancellation normalization and the fixed-order closed/open/periodic track theorems.

---

## 1. Exact episode schema

Let a forward episode contain an equal-face cancellation

\[
(G,\lambda)
\xrightarrow{2--0}
(H,\mu).
\]

The episode then performs a finite lower-order history and terminal recolouring, producing a returned root flow

\[
(H,\nu).
\]

When the cancellation is reversed, the local table gives one of:

\[
(H,\nu)
\xrightarrow{0--2}
(G',\nu'),
\]

where `G'` is:

- the original insertion topology;
- an alternative root insertion topology;
- or one missing-index co-root discrepancy topology.

The local theorems prove that `G'` has predecessor order and that its contraction is `H`. They do not compare `lambda` and `nu`, and do not produce a root-valued fixed-order history

\[
(G,\lambda)ightsquigarrow(G',\nu').
\]

---

## 2. Why local alternative insertion is insufficient

In the equality and good-disjoint rows, the original predecessor topology `G` and alternative insertion topology `G'` differ by a two-step ordinary five-leaf NNI path.

But the root labels on their common exterior branches are taken from different times:

- `G` carries the forward inherited flow `lambda`;
- `G'` carries the returned flow `nu` on the smaller graph.

The ordinary topology path alone does not transport `lambda` to `nu`. To realise the path as a fixed-order root history, one must lift the lower-order flow deformation

\[
\mu\rightsquigarrow\nu
\]

while retaining a compatible insertion interface. That is a relative-history theorem, not a consequence of endpoint vertex counting.

The missing-index row has the same issue with one co-root transport cell retained.

---

## 3. Proper nesting does not automatically solve it

Forward cancellations and reverse insertions are paired in last-in-first-out order. This gives a properly nested family of lower-order bubbles.

However, an innermost bubble may still contain a finite lower-order `2--2` history and a terminal root-state change. Eliminating the topological birth/death pair requires lifting that lower-order comparison through one inserted equal-face pair or replacing the complete bubble by a same-order source movie.

Proper nesting supplies an induction architecture, but not the required local lifting theorem.

---

## 4. Scope of the existing diagrammatic theorems

`PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md` begins with a finite Ptolemy van Kampen diagram for a **fixed marked-surface flip comparison**. Its cells are involutions, disjoint squares and five-leaf pentagons at fixed order.

`PETERSEN_OPEN_TRACK_ROOT_STRIP_REPLACEMENT_V1.md` and the root-annulus theorem likewise operate on fixed-order relative NNI histories.

They do not presently contain `2--0/0--2` birth/death cells or a theorem commuting arbitrary lower-order flow changes through such cells.

Therefore a raw variable-order periodic episode cannot be fed directly into those theorems.

---

## 5. Exact conditional theorem retained

### Theorem 5.1 — fixed-order periodic discharge

Assume a repeated complete endpoint episode admits a boundary-preserving replacement by a fixed-order lifted history cylinder with one closed nonbranching co-root track. Then:

1. closed-track erasure gives a finite connected root-valued history cylinder;
2. its legal root-history `1`-skeleton contains a proper crosscut between the two boundary histories;
3. cutting along the crosscut gives a fully root-valued rectangle;
4. unresolved endpoint count decreases by two.

This is exactly `PERIODIC_OUTER_ENDPOINT_ROOT_SEAM_DISCHARGE_V1.md` v1.2.

The theorem is retained. Only the unconditional supply of its fixed-order hypothesis is open.

---

## 6. Correct status of the arborescence and finite-state theorems

`TARGET_TOPOLOGY_ARBORESCENCE_FIXED_ORDER_V1.md` remains exact inside one fixed-order macro layer.

`FINITE_COMPLETE_STATE_NO_HIDDEN_GENEALOGY_V1.md` remains exact for normalized predecessor-order states and proves that no arbitrary history word is needed as a state coordinate.

Neither theorem compresses a variable-order continuation edge into a fixed-order edge. They become applicable after, not before, the missing compression theorem.

---

## 7. Repair targets

Exactly one of the following would close the gap.

### Route A — variable-order bubble compression

For every paired forward cancellation and returned original/alternative insertion, replace the complete intervening lower-order history bubble by a boundary-equivalent predecessor-order Ptolemy/history diagram. The replacement must retain complete root, cap, route and side data and may carry at most one co-root track.

### Route B — stratified closed-track theorem

Extend the singular-diagram theory to history complexes containing `2--0/0--2` birth/death cells. Prove that a periodic full-state singular component in such a stratified cylinder is impossible or has a fully root-valued stratified-cylinder replacement.

### Route C — history-coherent terminal selection

Choose every terminal root state so that each cancellation interface returns in the root-success orbit, making every lower-order bubble invert exactly and eliminating the need for relative lifting.

### Route D — nested continuation rank

Use the PDL bounded-depth stack architecture, but prove a concrete parent-continuation rank which strictly decreases before every lower-order call and survives failed return. This avoids compressing the complete episode to fixed order.

---

## 8. Minimal new target

### Target 8.1 — one innermost bubble

Let

\[
G\xrightarrow{2--0}H
\]

be one equal-face cancellation. Let `P,Q` be two root-valued fixed-order histories on `H` with the same source topology and prescribed complete exterior context, representing the inherited and returned lower-order states of one innermost bubble.

Prove one of:

1. `P,Q` lift through a common root-valued insertion to a predecessor-order history;
2. their endpoint relation gives the equality/good-disjoint alternative insertion and a predecessor-order Ptolemy strip;
3. the missing-index relation gives one predecessor-order co-root strip;
4. route/profile, bounded or separator exit;
5. a strictly smaller relative bubble remains.

A proof of Target 8.1 compatible with nesting would supply Route A.

---

## 9. Assurance correction

### Retained exact mathematics

- complete local inverse table;
- root-valued alternative insertions;
- missing-index transport state;
- fixed-order topology arborescence;
- finite complete predecessor-order state semantics;
- fixed-order closed/open track theorems;
- conditional periodic root-cylinder crosscut.

### Withdrawn

- `COMPLETE AUTHORIAL R2.7 CANDIDATE` classification;
- unconditional fixed-order representation of every outer continuation episode;
- unconditional no-sink conclusion for the complete variable-order process;
- unconditional contextual inverse transfer v5.2.

### Current classification

\[
\boxed{
\text{R2.7 BLOCKED AT VARIABLE-ORDER EPISODE COMPRESSION}.}
\]

No cap restoration, global five-support, Lean, manuscript, curation, release or publication status follows.
