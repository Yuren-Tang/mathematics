# Root-normalized contextual transfer with resolved-call recursion

## Research Lead master theorem v6 — corrected R2.7 assembly

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Supersedes for controlling Research Lead authorial use:**

- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V4.md`;
- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V5.md` in its conditional/overstated readings;
- `CONTEXTUAL_TRANSFER_REPAIR_FRONTIER_V2.md` as an open-frontier description;
- the uncorrected Type-IV stack comparison;
- the invalid inference that endpoint order restoration alone makes an episode fixed-order.

**Controlling repair inputs:**

- complete inverse-flip and inverse-cancellation source table;
- `ROOT_VALUED_ALTERNATIVE_INVERSE_CANCELLATION_INSERTION_V1.md`;
- `DOUBLED_DISJOINT_THREE_VERTEX_BORROWING_DICHOTOMY_V1.md`;
- first-failure one-edge and critical-overlap grammar;
- `WELD_ACTIVE_DIAGONAL_SIX_LEAF_LIFT_V1.md`;
- `WELD_SUPPORT_SWITCH_SOURCE_POP_V1.md`;
- `WELD_CENTRAL_MARK_CANCELLATION_POP_V1.md`;
- `CALL_FREE_CHILD_EPISODE_PARENT_LIFT_V1.md`;
- `VARIABLE_ORDER_RECURRENT_EPISODE_COMPRESSION_V2.md` v2.1;
- `RESOLVED_CALL_MACRO_ATTRACTOR_RANK_V1.md`;
- fixed-order target-arborescence, closed-track, open-strip and periodic-root-seam theorems;
- `NO_HIDDEN_GENEALOGY_FINITE_STATE_V1.md`.

**Status:** `COMPLETE AUTHORIAL R2.7 CANDIDATE / PDL RECONSTRUCTION AND INDEPENDENT ASSURANCE REQUIRED`.

Every original inverse step is crossed once. An inverse cancellation is evaluated on the actual returned lower-order roots and immediately has one of the exact source dispositions: original root insertion, root-valued alternative insertion, one missing-index atom, or accepted category exit. Nested lower-order calls are not compressed by endpoint order alone and are not ranked by comparing child and parent prefixes. Instead, lower target order gives finite child execution; completed calls form finite parent macro edges; variable-order recurrent episodes compress by innermost-call elimination; and the finite resolved parent macro graph has a shortest-distance attractor rank `d_N`. Termination is lexicographic induction on `(N,d_N)` inside each original-prefix stage.

This file does not declare PDL acceptance, independent audit, curation, Lean verification, manuscript integration, release, publication or the universal five-CDC theorem.

---

## 1. Finite original source history

Let

\[
\mathcal H:
C_0\longrightarrow C_1\longrightarrow\cdots\longrightarrow C_m
\]

be one finite source history. Every forward step is:

1. a root-valued `2--2` Pachner NNI; or
2. an equal-face `2--0` cancellation.

Fix a cap-compatible terminal root state on `C_m`.

A complete contextual state records literally:

- labelled topology and ordered incidences;
- every root label and at most one normalized atom;
- both crossed co-root resolutions;
- support transport, side-root outputs and rooted attachments;
- cap matching, distinguished cap block and route orientation;
- ordered active marks and mobile envelopes;
- target topology and bounded/category flags.

History words and genealogy are transition witnesses, not state coordinates.

---

## 2. Original-prefix induction

For

\[
0\le \ell\le m,
\]

assume the suffix from `C_m` back to `C_ell` has been consumed and the current state is a complete root/token state at the order of `C_ell`.

If `ell=0`, only same-order contextual normalization to the original target remains.

If `ell>0`, attempt the inverse of

\[
C_{\ell-1}\to C_\ell.
\]

Restore the predecessor incidence pattern before classifying the forced coefficient. Thus the original history coordinate changes immediately to

\[
\boxed{\ell-1.}
\]

The remaining obligation is a contextual normalization at the predecessor order.

---

## 3. Inverse `2--2` table

For the forced old diagonal:

\[
\begin{array}{c|c}
\text{value}&\text{source disposition}\\
\hline
\text{root}&\text{retain the restored root topology}\\
0&\text{use the other crossed root NNI}\\
\text{co-root}&\text{retain one oriented one-atom discrepancy state}.
\end{array}
\]

The first-failure theorem gives exactly one non-root edge. Critical overlaps normalize to at most one atom or an accepted exit.

No graph-order recursion occurs in this table.

---

## 4. Inverse equal-face cancellation table

Let the actual returned lower-order output roots be `a,b`.

\[
\begin{array}{c|c}
\text{returned relation}&\text{source disposition at predecessor order}\\
\hline
\text{distinct intersecting}&\text{original root insertion}\\
a=b&\text{direct alternative root insertion}\\
a\perp b,\ \text{good borrow}&\text{direct alternative root insertion}\\
a\perp b,\ \text{missing index}&\text{one normalized }(Q_i,Q_j,ij)\text{ atom}.
\end{array}
\]

Loop, parallel, insufficient-borrow and separator identifications are accepted bounded/category exits.

### Theorem 4.1 — no automatic lower-order state

The smaller graph is a child-call state and a common contraction witness; it is not declared an automatically completed order-`N-2` exit. Every nonexit return produces a concrete predecessor-order root/atom state by the displayed table.

---

## 5. Source fidelity through a finite child history

Transport the ordered cancellation boundary through the actual finite child strategy.

### Root `2--2` step

- disjoint/exterior contact: strict relative commutation;
- active marked diagonal: bounded six-leaf lift, root-valued or one standard first-exit atom.

### Support-pair switch

Use

\[
r'=r+(\epsilon_p+\epsilon_q)h.
\]

A `B`-preserving switch lifts root-valuedly; a first `A/C` exit returns one central atom.

### Equal-face overlap

- external ordered incidences transport canonically and preserve `B`;
- central marked edge is consumed before the lower child call and is not automatically resurrected.

### First exit

The child step which changes `B` to `A/C` has already been crossed. The returned parent state has exactly one ordinary atom. The strict child prefix is a finite source witness, not a parent numerical rank.

---

## 6. Innermost-call and variable-order compression

A finite child episode with no nested cancellation has the fixed parent-order lift of `CALL_FREE_CHILD_EPISODE_PARENT_LIFT_V1.md`.

For a finite episode with nested calls, induct on the call count:

1. choose an innermost call;
2. replace it by its call-free parent-order lift;
3. preserve physical boundary data and surviving-frame marks;
4. discard only auxiliary marks local to the eliminated call;
5. lower the call count by one.

After finitely many replacements, the episode is fixed-order.

### Theorem 6.1 — legitimate fixed-order reduction

Every finite variable-order repeated physical complete-state episode has a fixed-order root/one-token replacement with the same outer physical boundary.

Only after this compression are the fixed-order closed/open/periodic track theorems applied.

---

## 7. Fixed-order disposition

At one literal order `N`, use the finite complete state semantics.

### Root sector

Choose the target-rooted ordinary topology arborescence. Every successful root parent edge lowers

\[
d_{\rm top}
\]

by one. A failed edge gives one atom or an accepted exit.

### Internal closed singular track

Resolve constant-pivot runs, delete source-faithful backtracks, exclude odd `C5/C9`, and replace even `C6/C8` by a root annulus.

### Open track with normalized endpoints

Use the root-strip replacement.

### Repeated unresolved outer endpoint

Close the repeated complete collars, erase the fixed-order closed track, take a genuine root-history crosscut in the root cylinder and cut back to a root rectangle.

Thus no neutral fixed-order complete-state recurrence survives.

---

## 8. Resolved-call parent macro graph

Fix one target order `N` and assume every lower target order is already solved.

Build the finite parent graph `M_N`:

- fixed-order source macros are ordinary edges;
- a selected cancellation, complete lower-order solve and inverse/source pop are one resolved macro edge;
- accepted target/route/profile/bounded/separator states are terminal.

Every call edge has a finite witness by lower-order induction.

If a nonexit sink SCC existed, expand one of its cycles into a finite nested episode. Compress all calls by Theorem 6.1. The resulting fixed-order cycle is excluded by Section 7.

Therefore every parent state reaches a terminal.

Define

\[
\boxed{
d_N(x)=\operatorname{dist}_{M_N}(x,\mathcal X_N).}
\]

Choose one shortest-path macro at every state.

### Theorem 8.1 — resolved-call rank

After every completed parent macro,

\[
\boxed{d_N\mapsto d_N-1.}
\]

A child history length is never inserted into the parent key.

---

## 9. Recursive contextual normalization

### Theorem 9.1 — order-`N` normalization

Every complete order-`N` root/token state reaches a target root state or an accepted route/profile/bounded/separator exit after finitely many resolved macros.

### Proof

Induct lexicographically on

\[
(N,d_N).
\]

- A fixed-order macro is finite directly.
- A call macro executes only lower target orders and is finite by the `N` induction hypothesis.
- Its parent endpoint has smaller `d_N`.

Thus the macro strategy terminates. ∎

---

## 10. Contextual inverse transfer

Return to the finite original history.

At each `ell>0`:

1. cross the next original inverse step, lowering `ell`;
2. apply Sections 3--4;
3. normalize the resulting predecessor-order state by Theorem 9.1;
4. continue to the next original step or leave through an accepted exit.

### Theorem 10.1 — root-normalized contextual transfer v6

Every cap-compatible terminal root state on `C_m` transfers through the finite mixed Pachner/cancellation history to a cap-compatible root state on `C_0`, or leaves through an accepted route/profile, bounded direct/theta or separator/category branch.

### Proof

Induct on the finite original-prefix coordinate `ell`. The inner normalization at each predecessor order terminates by Theorem 9.1. No branch restores a larger original-prefix coordinate. ∎

---

## 11. Exact resolution of cancellation re-entry

The invalid macro was

\[
\text{cancel}
\to
N-2
\to
\text{choose arbitrary flow}
\to
\text{attempt weld}
\to
N\text{ token reset}.
\]

The v6 proof replaces it by:

\[
\begin{aligned}
&\text{actual cancellation boundary}\\
&\to\text{finite lower-order strategy}\\
&\to\text{source-faithful active-flip/switch/}2\!-\!0\text{ transport}\\
&\to\text{root/alternative/one-atom parent return}\\
&\to\text{one resolved parent macro with lower }d_N.
\end{aligned}
\]

Variable-order cycles are compressed by innermost-call induction before fixed-order periodic arguments are used.

No arbitrary-flow inverse weld, generic Kempe connectivity, hidden genealogy or child/parent prefix identification appears.

---

## 12. R2.7 classification

### Closed at Research Lead authorial level

- complete inverse-move source table;
- direct elimination of persistent zero rows;
- exact missing-index atom;
- active-diagonal six-leaf source lift;
- support-switch successful/first-exit source pop;
- central-mark-consuming cancellation semantics;
- finite call-free child lift;
- finite nested episode compression;
- fixed-order closed/open/periodic/root disposition;
- finite resolved-call parent rank;
- recursive contextual transfer without cancellation reset.

### Required before promotion

PDL must independently reconstruct:

1. every local source table and six-leaf split path;
2. support-switch component parity and central formula;
3. one-token finite-prefix lift;
4. innermost-call elimination and call-local mark semantics;
5. fixed-order track replacements with complete cap/route data;
6. resolved-call macro graph finiteness and SCC argument;
7. the simultaneous `(N,d_N)` and original-prefix induction.

An independent auditor must then verify the full dependency graph and all imported fixed-order theorems.

### Not established here

- PDL completion or independent audit;
- unconditional promotion of one-cross cap restoration beyond its R2 consumer interface;
- global simple-edge extension or universal five-CDC acceptance;
- Lean verification;
- manuscript integration;
- curation, release, arXiv, DOI, peer review or publication.
