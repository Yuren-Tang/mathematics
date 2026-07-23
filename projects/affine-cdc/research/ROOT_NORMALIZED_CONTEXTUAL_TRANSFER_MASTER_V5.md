# Root-normalized contextual transfer after the variable-order correction

## Research Lead master theorem v5.3 — conditional fixed-order assembly

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Supersedes:** v5.0--v5.2 of this file.

**Controlling correction:** `VARIABLE_ORDER_PERIODIC_EPISODE_COMPRESSION_GAP_V1.md`.

**Status:** `CONDITIONAL FIXED-ORDER THEOREM / VARIABLE-ORDER EPISODE COMPRESSION OPEN / R2.7 BLOCKED`.

The local inverse-cancellation table, fixed-order topology arborescence, finite complete state semantics, closed/open track theorems and periodic root-cylinder crosscut are retained. What is withdrawn is the claim that every outer continuation episode is automatically represented by a fixed-order lifted Ptolemy cylinder. An episode may descend through equal-face cancellations, change the lower-order root flow, and only later return by original or alternative insertions. Restoring predecessor order at the endpoint does not lift the intervening lower-order flow evolution through the deleted pair.

Accordingly this file proves contextual transfer only under an explicit **fixed-order episode compression hypothesis**.

---

## 1. Exact local inverse table retained

For an inverse `2--2` step:

\[
\begin{array}{c|c}
\text{forced old diagonal}&\text{disposition}\\
\hline
\text{root}&\text{direct inverse flip}\\
0&\text{the other crossed root NNI}\\
\text{co-root}&\text{one oriented discrepancy atom}.
\end{array}
\]

For an inverse equal-face cancellation with returned reconnecting roots `a,b`:

\[
\begin{array}{c|c}
\text{relation of }a,b&\text{endpoint disposition}\\
\hline
\text{distinct intersecting}&\text{original root insertion}\\
a=b&\text{root-valued alternative insertion}\\
a\perp b,\ \text{good borrow}&\text{root-valued alternative insertion}\\
a\perp b,\ \text{missing-index borrow}&\text{one }(Q_i,Q_j,ij)\text{ co-root transport state}.
\end{array}
\]

Every displayed output has predecessor vertex order. Thus no inverse step requires a recursive equality call or an automatically completed order-lowering exit.

### Important limitation

This table controls the **returned endpoint** of one cancellation. It does not transport an arbitrary lower-order history between the inherited post-cancellation flow and the returned flow through a fixed inserted pair.

---

## 2. Fixed-order layer retained

Assume one transfer obligation has already been represented on a fixed predecessor-order labelled incidence universe.

Then the following are exact.

### 2.1 Target topology arborescence

By `TARGET_TOPOLOGY_ARBORESCENCE_FIXED_ORDER_V1.md`, every local normalization output lies in the ordinary labelled `2--2` component of the required topology. Choose a rooted spanning tree. Every successful target-parent root move strictly lowers topology-tree distance; a failed parent move produces the known zero/co-root/category alternative.

### 2.2 Finite complete states

By `FINITE_COMPLETE_STATE_NO_HIDDEN_GENEALOGY_V1.md`, the current labelled topology, root assignment, one atom and its resolutions, support/attachment transport, cap block, route orientation and target pointer form a finite Markov-sufficient state. History words and edge ancestry are transition witnesses, not state coordinates.

### 2.3 Singular components

After immediate normalization every unbounded singular component is one nonbranching co-root track.

- Internal closed tracks erase by `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md`.
- Open tracks with root-normalized endpoint sides erase by the corrected open-strip theorem.
- A repeated unresolved endpoint in a fixed-order cylinder discharges by `PERIODIC_OUTER_ENDPOINT_ROOT_SEAM_DISCHARGE_V1.md` v1.2: erase the closed track to a connected root cylinder, take a shortest legal `1`-skeleton crosscut, and cut to a root rectangle.

### Theorem 2.1 — fixed-order no-sink theorem

At one fixed order and original-prefix level, the canonical target-directed macro-state graph has no nonterminal sink strongly connected component.

### Proof

A pure-root cycle is impossible because topology-tree distance strictly decreases. Every other cycle contains a co-root component, which is internal closed, normalized-endpoint open, or periodic outer-endpoint. The three retained diagrammatic theorems remove these cases. ∎

---

## 3. Fixed-order episode compression hypothesis

### Hypothesis FOC

Every finite outer continuation episode, after pairing each forward equal-face cancellation with its returned original/alternative insertion, admits a boundary-preserving replacement by a finite predecessor-order lifted history diagram such that:

1. every ordinary cell is a relative `2--2` Ptolemy/history cell;
2. every equality or good-disjoint birth/death pair is replaced by its root-valued alternative-insertion strip;
3. every missing-index pair contributes at most one nonbranching co-root strip;
4. complete root, incidence, support, cap, route and side data are retained;
5. no lower-order state or unmatched `2--0/0--2` cell remains.

This is exactly the variable-order bubble-compression theorem which is not yet proved.

---

## 4. Conditional contextual transfer

### Theorem 4.1 — contextual transfer under FOC

Assume Hypothesis FOC for every continuation episode arising from the finite original history. Then every cap-compatible terminal root state transfers to the original context or exits through an accepted route/profile, bounded direct/theta, or separator/category branch.

### Proof

Induct on the finite original-history prefix.

Cross one original inverse step and apply the endpoint table of Section 1. Hypothesis FOC places the resulting continuation on one fixed predecessor-order layer. Apply Theorem 2.1 to discharge its discrepancy before crossing the next original step. The prefix strictly decreases and no graph-order recursive state remains. ∎

---

## 5. Why FOC is not supplied by endpoint normalization

Consider

\[
(G,\lambda)
\xrightarrow{2--0}
(H,\mu)
\rightsquigarrow
(H,\nu)
\xrightarrow{0--2}
(G',\nu').
\]

The local insertion theorem relates `(H,nu)` to `(G',nu')`. It does not relate the forward inherited flow `mu` to the returned flow `nu` while keeping an insertion interface present. The ordinary five-leaf path between the topologies `G` and `G'` does not transport the changed exterior root data.

Thus the intervening lower-order history cannot simply be deleted or declared a fixed-order Ptolemy word. Proving such a replacement is a relative-history theorem and is the current R2.7 blocker.

---

## 6. Current repair frontier

The precise alternatives are:

1. **Variable-order bubble compression:** prove Hypothesis FOC by an innermost-bubble induction.
2. **Stratified history theorem:** extend closed-track erasure to cylinders containing `2--0/0--2` birth/death cells.
3. **History-coherent terminal selection:** choose terminal root states which invert every cancellation interface root-valuedly.
4. **Concrete nested continuation rank:** instantiate the PDL stack theorem with a strict parent rank, avoiding fixed-order compression.

The smallest immediate target is `VARIABLE_ORDER_PERIODIC_EPISODE_COMPRESSION_GAP_V1.md`, Target 8.1: one innermost cancellation bubble.

---

## 7. Correct classification

### Retained exact mathematics

- complete local inverse table;
- root-valued alternative insertions;
- missing-index co-root transport identification;
- fixed-order target topology arborescence;
- finite complete state semantics without hidden genealogy;
- fixed-order closed/open track erasure;
- conditional periodic root-cylinder crosscut;
- fixed-order no-sink theorem.

### Withdrawn

- unconditional fixed-order representation of variable-order episodes;
- unconditional no-sink theorem for the complete mixed-order process;
- unconditional contextual transfer v5.2;
- `COMPLETE AUTHORIAL R2.7 CANDIDATE` classification.

### Current status

\[
\boxed{
\text{R2.7 BLOCKED AT VARIABLE-ORDER EPISODE COMPRESSION}.}
\]

No cap restoration, global five-support, Lean, manuscript, curation, release, arXiv, DOI, audit or publication status follows.
