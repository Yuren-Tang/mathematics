# Finite variable-order recurrent episodes compress by innermost-call elimination

## Research Lead episode-compression theorem v2.1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Repairs the gap isolated by:**

- `VARIABLE_ORDER_EPISODE_COMPRESSION_SCOPE_CORRECTION_V1.md`.

**Parents:**

- `CALL_FREE_CHILD_EPISODE_PARENT_LIFT_V1.md`;
- `WELD_CENTRAL_MARK_CANCELLATION_POP_V1.md`;
- `NO_HIDDEN_GENEALOGY_FINITE_STATE_V1.md`;
- fixed-order closed/open/periodic track replacement theorems.

**Status:** exact induction on the finite number of genuine cancellation calls in one finite repeated-complete-state episode. The invalid shortcut was to infer fixed order merely because every inverse return eventually restores parent order. The repaired proof instead chooses an innermost call, whose child history contains no further cancellation, replaces that whole child episode by the fixed parent-order root/one-token history of `CALL_FREE_CHILD_EPISODE_PARENT_LIFT_V1.md`, and thereby removes exactly one order-changing call. Iteration removes all calls.

Central-mark consumption is preserved correctly at the call collar. A mark belonging to a still-live containing frame remains a genuine state change; a mark created only for the eliminated call is auxiliary call-local data and is discarded with that call frame. No conclusion is drawn from equality of outer endpoint mark counts about such temporary internal marks.

Consequently every variable-order repeated physical complete-state episode reduces to a fixed-order recurrence with the same physical outer boundary, where the established track theorems apply.

This theorem is the missing bridge allowing periodic endpoint and call-cut arguments to be used after, not before, variable-order normalization.

---

## 1. Finite nested episodes

A **finite nested episode** is a finite source-history diagram with:

- one outer labelled order `N`;
- root-valued states and at most one normalized atom at every active order;
- genuine forward equal-face cancellations which launch lower-order child histories;
- inverse return expansions governed by the complete root/equality/good-disjoint/missing-index table;
- ordered incidence, cap, route, support and mark data retained at every live frame boundary;
- finite nesting depth and finitely many total call occurrences.

Let

\[
\kappa(\mathcal E)
\]

be the number of genuine order-changing cancellation calls in the episode.

A call is **innermost** when its child subepisode contains no further genuine cancellation call.

Every nonempty finite call tree has an innermost call.

---

## 2. Boundary of an innermost call

Let one innermost call occur at physical parent order `M`.

Forward cancellation gives a lower-order child at order `M-2` with two ordered output edges and the complete surviving contextual data.

Because the call is innermost, the complete child solve/return segment contains only:

- root `2--2` flips;
- support-pair switches;
- fixed-order local normalization;
- identity and accepted exit cells.

It contains no further `2--0` call.

Therefore `CALL_FREE_CHILD_EPISODE_PARENT_LIFT_V1.md` applies.

---

## 3. Replacing one innermost call

### Ordinary external-mark call

Replace the complete

\[
M\to M-2\to M
\]

subepisode by the finite order-`M` root/one-token history supplied by the call-free lift theorem.

The replacement preserves:

- both physical endpoint source states;
- every exterior ordered incidence;
- cap, route and side-root data;
- every mark which belongs to a still-live containing frame;
- the final root or first-exit atom returned by the child.

It contains no lower-order history vertex and no new cancellation call.

### Central-mark-consuming call

If the cancelled central edge carried an active mark of the current call frame, first apply the exact mark-deletion semantics:

\[
a\longrightarrow a-1.
\]

Then apply the same physical call-free child lift to the cancellation outputs and returned roots.

The fixed-order replacement begins at the marked call-boundary state and ends at the correct root/atom call-boundary state with that call-local mark absent. A newly inserted central edge remains unmarked, as required by `WELD_CENTRAL_MARK_CANCELLATION_POP_V1.md`.

There are two bookkeeping cases.

1. **Persistent containing-frame mark.** If the consumed mark is part of a containing frame which remains live after the innermost call is removed, its deletion is retained as a strict complete-state change.
2. **Call-local mark.** If the mark exists only as the inverse-weld boundary of the eliminated call, the entire call frame is removed. Its creation, transport and deletion are auxiliary witness data and do not appear in the outer physical boundary of the replacement.

No mark is resurrected or duplicated in either case.

### Lemma 3.1 — one-call elimination

Replacing an innermost call:

1. preserves the complete **physical** boundary state of its containing episode;
2. preserves every ordered mark belonging to a surviving frame;
3. records any deletion of a surviving-frame mark;
4. discards only marks local to the eliminated call frame;
5. introduces no new call;
6. changes no history outside the call collar;
7. lowers the call count by exactly one:
   \[
   \boxed{\kappa(\mathcal E')=\kappa(\mathcal E)-1.}
   \]

---

## 4. Induction on call count

### Theorem 4.1 — finite episode compression

Every finite nested episode has a fixed-outer-order replacement with the same complete physical outer boundary and no genuine cancellation call.

The replacement uses root-valued states and at most one normalized atom. Marks of surviving frames are retained literally; call-local marks disappear with their eliminated frames.

### Proof

Induct on `kappa(E)`.

- If `kappa(E)=0`, the episode is already fixed-order.
- If `kappa(E)>0`, choose an innermost call and apply Lemma 3.1. The resulting episode has one fewer call and the same physical outer boundary. Apply the induction hypothesis.

The process terminates because `kappa(E)` is a finite nonnegative integer. ∎

This proof never assumes that a lower-order history is pointwise weld-relative. The needed active-diagonal and support-switch overlaps are supplied by the bounded source lifts inside the call-free theorem.

---

## 5. Repeated complete physical states

Assume the outer boundary consists of two occurrences of the same literal physical complete state

\[
\Xi_{\rm out}^{-}=\Xi_{\rm out}^{+}.
\]

Complete equality includes:

- labelled topology and root/token data;
- ordered cap and route data;
- every active ordered mark lineage of the surviving outer frame;
- support transport and side attachments.

Apply Theorem 4.1 to obtain a fixed-order replacement with the same equal physical endpoints.

### Lemma 5.1 — surviving marks are preserved; temporary marks are irrelevant

In the compressed recurrence:

1. every mark belonging to the outer surviving frame has the same endpoint data as before;
2. any deletion of such a mark would be a strict nonrecurrent state change and therefore cannot survive in a repeated complete outer state;
3. marks created only inside eliminated calls are not outer state coordinates and may have been created and consumed internally.

### Proof

Items 1--2 follow from literal equality of the outer complete state and the no-resurrection theorem. Item 3 follows because call-local marks are auxiliary data of a frame removed by the innermost-call replacement; they do not belong to either outer endpoint. ∎

Thus the compressed physical recurrence has unchanged surviving marked boundary, without the false claim that no temporary internal mark was ever consumed.

---

## 6. Fixed-order disposition

After compression, forget eliminated call-local bookkeeping and apply the existing fixed-order alternatives to the physical root/token history.

### Internal closed track

Use `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md`.

### Open track with normalized endpoint sides

Use the retained open-strip theorem.

### Repeated unresolved outer endpoint

Use `PERIODIC_OUTER_ENDPOINT_ROOT_SEAM_DISCHARGE_V1.md`.

### Pure root segment

Use the target topology arborescence; successful parent moves strictly lower `d_top`.

### Theorem 6.1 — no neutral variable-order recurrence

A finite repeated physical complete-state episode containing nested cancellation calls admits one of:

1. an accepted route/profile/bounded/separator exit;
2. strict progress in a mark belonging to a surviving frame;
3. a fixed-order root/one-token replacement with strictly smaller singular/boundary complexity;
4. a root-valued target-directed replacement.

Temporary call-local mark creation/consumption is absorbed inside the compression and is neither declared global progress nor treated as an obstruction.

In particular, variable-order nesting cannot support a neutral return to the same physical complete state.

---

## 7. Repair of the previous scope correction

The earlier invalid implication was

\[
\text{every return endpoint has order }N
\Longrightarrow
\text{the whole episode is a fixed-order cylinder}.
\]

The repaired chain is

\[
\begin{aligned}
&\text{finite nested episode}\\
&\Downarrow\quad\text{choose innermost call}\\
&\text{call-free child parent lift}\\
&\Downarrow\quad\kappa\mapsto\kappa-1\\
&\text{fixed-order physical episode}\\
&\Downarrow\\
&\text{closed/open/periodic/root disposition}.
\end{aligned}
\]

Thus fixed-order track theorems are applied only after all order-changing calls have been removed by a proved finite induction.

---

## 8. Consequence for call-cut local rank

A cycle in the fully resolved parent macro graph may contain completed child calls. Apply Theorem 4.1 to the finite cycle segment and remove all such calls. The result is a fixed-order physical cycle with the same complete outer endpoints.

Theorem 6.1 excludes a nonexit neutral cycle. Therefore the finite parent macro graph has no nonexit sink strongly connected component after accepted exits and strict surviving-mark progress are included.

This supplies the variable-order justification missing from the initial version of `FINITE_CALL_CUT_LOCAL_ATTRACTOR_RANK_V1.md`.

---

## 9. Assurance boundary

### Exact here

- induction on the finite number of nested calls;
- source-faithful elimination of one innermost call;
- correct distinction between surviving-frame and call-local marks;
- preservation of physical outer boundary data;
- fixed-order compression of every finite repeated physical complete-state episode;
- legitimate application of the fixed-order track theorems after compression;
- exclusion of neutral variable-order recurrence.

### Imported authorial mathematics

- call-free child episode parent lift;
- complete local inverse table;
- central-mark cancellation semantics;
- fixed-order closed/open/periodic/root replacements.

### Not yet claimed

- final corrected stack/master assembly;
- PDL reconstruction or independent audit;
- R2.7, one-cross cap restoration or universal five-CDC acceptance;
- Lean verification, manuscript integration, curation, release or publication.
