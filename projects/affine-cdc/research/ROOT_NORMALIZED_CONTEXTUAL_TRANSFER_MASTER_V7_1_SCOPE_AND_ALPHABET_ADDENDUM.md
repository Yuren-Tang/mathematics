# Scope and alphabet addendum to first-cancellation master v7

## Research Lead master v7.1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `44e0243d0cdec37fa87d0f55cc7ae3013af1f552`

**Controls with:**

- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V7_FIRST_CANCELLATION_RETURN.md`;
- `FIRST_CANCELLATION_TARGET_CAP_TERMINALISATION_V1.md`;
- `FIRST_CANCELLATION_SINGLE_POP_TARGET_TOPOLOGY_SCOPE_CORRECTION_V1.md`;
- `FIRST_CANCELLATION_FIXED_ORDER_NO_REOPENING_V1.md`;
- `ONE_CROSS_PROOF_DAG_AND_SUPERSESSION_INDEX_V5.md`.

**Status:** exact scope hardening of v7. It makes two points controlling:

1. an alternative inverse cancellation yields a same-order contextual source topology with the original predecessor graph recorded as target; it need not literally recreate that graph in one move;
2. fixed-order target normalization and pure-prefix inversion never reopen a cancellation call, even when equal adjacent root triangles appear.

The v7 ordinary-induction architecture is unchanged.

---

## 1. Correct single-pop output

At the first cancellation, lower ordinary solubility gives a root flow on the actual child target cap closure.

Evaluating the two stored output roots yields one of:

- original root insertion on the literal predecessor topology;
- equality alternative root insertion on a neighbouring five-leaf topology;
- good-disjoint alternative root insertion on a neighbouring five-leaf topology;
- one missing-index co-root atom on a neighbouring same-order topology;
- exact bounded/small-cut terminal.

In the middle three rows, the complete exterior incidence boundary is identical to that of the required predecessor, but the internal source topology may differ.

The correct state type is:

\[
\boxed{
\text{root or one-atom contextual state at order }N
\text{ with required predecessor topology stored as target}.}
\]

The target-rooted arborescence normalizes this source topology before the next source-prefix edge is crossed.

---

## 2. Correct fixed-order coordinates

At source-prefix stage `ell`, retain:

- current same-order source topology `T`;
- required predecessor topology `C_ell`;
- target-tree distance `d_top(T,C_ell)`;
- one optional normalized co-root atom;
- complete fixed outer cap/route/incidence data.

The procedure alternates:

1. normalize `T` to `C_ell` at fixed order;
2. invert the next source NNI;
3. lower `ell` by one.

A convenient rank is

\[
\boxed{(\ell,d_{\rm top},\rho_{\rm atom})}.
\]

No coordinate is a graph-order call depth.

---

## 3. Fixed-order alphabet

The internal alphabet after the single pop is exactly:

- ordinary target-tree `2--2` NNIs;
- alternative crossed root NNIs for zero failure;
- bounded one-atom critical-overlap normalization;
- local pivot-change root seams;
- constant-pivot identity strips;
- normalized endpoint collars;
- periodic root crosscuts;
- literal complete-state identity gluings.

Excluded:

- another `2--0` cancellation;
- another inverse `0--2` insertion;
- a lower-order child call;
- a raw support-switch internal cell;
- two simultaneous atoms.

---

## 4. Equal-face adjacency is not a fixed-order generator

An equal adjacent support-triangle pair is the stopping event only in the forward monotone cross-flow phase.

During fixed-order target normalization, the next move is chosen in the uncoloured ordinary `2--2` topology arborescence. Root labels are tested after that parent edge is selected.

If the forced target diagonal is:

- root: move to the parent topology;
- zero: the other crossed topology is root-valued and supplies the local normalization;
- co-root: retain one standard atom;
- category/route: use the exact terminal.

Equal-face adjacency of some current edge does not add a cancellation row and does not alter the selected parent edge.

Thus the pure fixed-order consumer has no “failure behind another cancellation” output.

---

## 5. Exactly one order descent

V7 has exactly one graph-order descent:

\[
\widehat G_s
\longrightarrow
\widehat G^-,
\qquad
|V(\widehat G^-)|=|V(\widehat G_s)|-2,
\]

at the selected first cancellation.

All preceding accepted moves are root NNIs. All subsequent normalization moves are fixed-order NNIs/one-atom cells.

Therefore the proof uses:

1. a nonnegative equality/DDD potential before the first cancellation;
2. ordinary lower `P` once on `\widehat G^-`;
3. fixed-order rank `(ell,d_top,rho_atom)` after the single pop.

No variable-order recurrence, call SCC, child-history lift, bubble compression, or terminal frame stack is needed.

---

## 6. PDL controlling return

PDL should read v7 with the following exact corrections:

- do not identify every alternative insertion with the literal predecessor topology;
- prove complete exterior-boundary equality and target-component containment;
- normalize by the target arborescence;
- do not contract equal-face pairs during fixed-order return;
- verify that every fixed-order macro lies in the no-reopening alphabet;
- use the repaired cellwise R2.6 theorem, not the old global C6/C8 annulus.

---

## 7. Classification

\[
\boxed{
\text{R2.7-v7.1 COMPLETE AUTHORIAL CANDIDATE}
/
\text{ORDINARY STRONG INDUCTION ONLY}.}
\]

Still required:

- PDL reconstruction;
- independent mathematical audit;
- proof-DAG and terminal-consumer audit by the receiver/canonical authority.

Not claimed:

- accepted cap restoration;
- established five-support/five-CDC theorem;
- Lean, Curator, manuscript, release, arXiv, DOI, peer review, or publication status.
