# Properly nested cancellation bubbles compress by innermost induction

## Research Lead variable-order compression theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `VARIABLE_ORDER_PERIODIC_EPISODE_COMPRESSION_GAP_V1.md`;
- `FIXED_ORDER_SUCCESSFUL_RETURN_ROOT_PRESENTATION_V1.md`;
- `INNERMOST_CANCELLATION_BUBBLE_RAW_INSERTION_LIFT_V1.md`;
- `THETA_ROOT_FLOW_SUPPORT_SWITCH_CONNECTIVITY_V1.md`;
- fixed-order closed/open/periodic track theorems.

**Status:** `COMPLETE AUTHORIAL VARIABLE-ORDER COMPRESSION CANDIDATE / PDL RECONSTRUCTION REQUIRED`.

A recursive contextual execution has a properly nested call structure: a forward equal-face cancellation opens a lower-order frame and its returned original/alternative insertion closes the most recently opened frame. Choose an innermost frame. Its child execution contains no further cancellation. If the child exits, the whole branch is accepted. If it returns a root state, the fixed-order presentation theorem replaces the child by a fully root-valued history. The raw-insertion lift then replaces the opening cancellation, child history and closing insertion by one predecessor-order root/one-atom path. This removes one birth/death pair. Induction on the finite number of frames removes every variable-order bubble and supplies the fixed-order episode compression hypothesis of contextual-transfer v5.3.

---

## 1. Well-bracketed execution traces

A recursive execution trace consists of finite source-history segments and frame operations:

### Push

A root-valued equal-face cancellation

\[
(G,\Lambda)
\xrightarrow{2--0}
(H,\lambda)
\]

opens one child frame of order two less. The two reconnecting output incidence pairs are retained as the child-to-parent interface.

### Child execution

The child performs a finite contextual execution at its own order. It may itself open and close lower-order frames.

### Pop

A successful child return supplies a root-valued state on its current lower-order source. The local inverse table restores parent order by:

- original root insertion;
- alternative root insertion;
- one missing-index co-root insertion state;
- or accepted exit.

Because a child must return before its parent continuation resumes, pushes and pops are last-in-first-out. Hence the call intervals form a properly nested finite family.

Let

\[
b(\mathcal X)
\]

be the number of paired push/pop frames in one finite execution `mathcal X`.

---

## 2. Innermost frame

If

\[
b(\mathcal X)>0,
\]

choose an innermost paired frame

\[
G\xrightarrow{2--0}H
\quad[\text{child execution}]\quad
H\xrightarrow{0--2}G'.
\]

By innermostness the child execution contains no further push/pop pair. It is fixed-order.

Exactly one of two branches occurs.

### Child exit

The fixed-order child exposes a route/profile, bounded direct/theta bridge, or separator/category exit. Then the complete parent branch is already accepted; no bubble compression is required.

### Successful child return

The child begins and ends at root-valued complete states on its fixed lower-order incidence universe.

By `FIXED_ORDER_SUCCESSFUL_RETURN_ROOT_PRESENTATION_V1.md`, its supplied successful execution has a boundary-equivalent fully root-valued history presentation. Bounded theta recolouring is represented by ordinary support switches using `THETA_ROOT_FLOW_SUPPORT_SWITCH_CONNECTIVITY_V1.md`.

Thus the child history satisfies the root-presentation hypothesis of `INNERMOST_CANCELLATION_BUBBLE_RAW_INSERTION_LIFT_V1.md`.

---

## 3. Compress one innermost bubble

Apply raw insertion to the two child-to-parent interface lineages throughout the root-valued child history.

The local lift theorems give:

- disjoint/exterior root flips: strict relative lift;
- active diagonal with disjoint second mark: complete ten-root root/one-atom movies;
- active diagonal with adjacent second mark: three root NNIs;
- support-pair switches: universal raw insertion lift;
- bounded incidence identifications: accepted bounded/category exits.

Concatenation gives one parent-order path with at most one central atom.

Normalize the returned pair:

- `B`: root insertion;
- equality: two-NNI root alternative insertion;
- good doubled-disjoint: two-NNI root alternative insertion;
- missing-index: one standard co-root transport state after local defect-tree normalization;
- bounded identification: accepted exit.

### Theorem 3.1 — innermost frame elimination

A successful innermost push/child/pop interval is boundary-equivalent to one finite parent-order history segment containing no `2--0/0--2` frame operation and at most one persistent co-root atom.

The replacement preserves:

1. the complete labelled parent boundary before the push;
2. the complete returned parent state after the pop;
3. cap block, route, support transport and exterior attachments;
4. every surrounding history incidence used to glue the interval back into the parent execution.

It removes exactly one paired frame.

---

## 4. Induction on bubble count

### Theorem 4.1 — nested bubble compression

Every finite well-bracketed successful execution `mathcal X` is boundary-equivalent to a finite execution `mathcal X^flat` with

\[
\boxed{b(\mathcal X^\flat)=0.}
\]

All states of `mathcal X^flat` live at the original frame order of the execution being compressed, and every singular state carries at most one normalized co-root atom.

### Proof

Induct on `b(mathcal X)`.

- If `b=0`, nothing is required.
- If `b>0`, choose an innermost frame.
  - If its child exits, the branch is accepted.
  - If it returns, Theorem 3.1 replaces the frame interval by a parent-order segment and lowers `b` by one.

The replacement introduces no new frame. Apply the induction hypothesis. Since `b` is a finite nonnegative integer, the process terminates. ∎

---

## 5. Supply of fixed-order episode compression

The flattened execution `mathcal X^flat` consists of fixed-order full-state history cells:

- root-valued relative NNIs and identity steps;
- root-valued support-pair switches;
- bounded one-atom NNI cells from active-diagonal transport;
- one-atom raw support-switch cells;
- local equality/good-disjoint rootification cells;
- normalized missing-index co-root cells.

No lower-order source state and no unmatched birth/death cell remains.

### Corollary 5.1 — fixed-order compression hypothesis

Every finite successful variable-order continuation episode admits a boundary-preserving fixed-order full-state replacement with at most one nonbranching co-root track.

This supplies Hypothesis FOC of `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V5.md` v5.3, read with the allowed fixed-order support-switch/one-atom cells listed above.

---

## 6. No circularity

The dependency is strictly one-way.

1. Fixed-order closed/open/periodic track theorems do not use variable-order compression.
2. `FIXED_ORDER_SUCCESSFUL_RETURN_ROOT_PRESENTATION_V1.md` acts only on a supplied execution with `b=0`.
3. The innermost raw-insertion theorem uses that root presentation to remove one frame.
4. Bubble-count induction supplies FOC.
5. Only then may contextual-transfer v5.3 invoke FOC for the complete mixed-order process.

Thus nested compression is not used to prove the fixed-order theorem on which its innermost step depends.

---

## 7. Interaction with accepted exits

The theorem is required only for a branch which successfully returns to its parent.

If an innermost or later child reaches:

- route/profile escape;
- same-matching bridge/loop terminal;
- separator/category exit;
- another already accepted bounded branch,

then the global branch terminates and no pop must be compressed.

A cross-matching theta terminal is not an exit merely by recolouring choice; its root states are connected by at most three support switches, so a successful return remains root-presented.

---

## 8. Consequence for the former gap

`VARIABLE_ORDER_PERIODIC_EPISODE_COMPRESSION_GAP_V1.md` isolated the absence of a theorem replacing

\[
(G,\lambda)
\to(H,\mu)
\rightsquigarrow(H,\nu)
\to(G',\nu')
\]

by one predecessor-order history.

Theorem 4.1 now supplies that replacement by innermost-frame induction. The lower flow change `mu rightsquigarrow nu` is first root-presented at fixed child order, then lifted through raw insertion.

Hence the variable-order compression interface is authorially closed, subject to reconstruction of every parent local theorem.

---

## 9. Assurance boundary

### Exact here

- proper nesting of recursive cancellation frames;
- existence and fixed-order nature of an innermost frame;
- root presentation of a successful innermost child;
- parent-order elimination of one frame;
- strict decrease of frame count;
- finite induction to a frame-free history;
- supply of fixed-order episode compression.

### Imported authorial mathematics

- fixed-order successful-return root presentation;
- complete raw root-NNI and support-switch lifts;
- terminal equality/DDD normalization;
- theta root-flow switch connectivity;
- bounded/category exits.

### Still requires PDL and independent assurance

- exact execution-frame semantics and well-bracketing in the controlling contextual construction;
- full-labelled preservation under each local lift;
- fixed-order track theorems and cap-block orientation;
- integration with the original-prefix induction.

### Not claimed

- PDL completion or independent audit;
- cap restoration or global five-support acceptance;
- Lean verification, manuscript integration, curation, release, arXiv, DOI, peer review or publication.
