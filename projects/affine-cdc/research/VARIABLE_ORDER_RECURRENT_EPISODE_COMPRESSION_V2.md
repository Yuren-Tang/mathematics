# Finite variable-order recurrent episodes compress by innermost-call elimination

## Research Lead episode-compression theorem v2

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Repairs the gap isolated by:**

- `VARIABLE_ORDER_EPISODE_COMPRESSION_SCOPE_CORRECTION_V1.md`.

**Parents:**

- `CALL_FREE_CHILD_EPISODE_PARENT_LIFT_V1.md`;
- `WELD_CENTRAL_MARK_CANCELLATION_POP_V1.md`;
- `NO_HIDDEN_GENEALOGY_FINITE_STATE_V1.md`;
- fixed-order closed/open/periodic track replacement theorems.

**Status:** exact induction on the finite number of genuine cancellation calls in one finite repeated-complete-state episode. The invalid shortcut was to infer fixed order merely because every inverse return eventually restores parent order. The repaired proof instead chooses an innermost call, whose child history contains no further cancellation, replaces that whole child episode by the fixed parent-order root/one-token history of `CALL_FREE_CHILD_EPISODE_PARENT_LIFT_V1.md`, and thereby removes exactly one order-changing call. Iteration removes all calls. Central-mark consumption is retained as a strict state change, not silently reversed. Consequently every variable-order repeated complete-state episode either contains accepted/mark progress or reduces to a fixed-order recurrence, where the established track theorems apply.

This theorem is the missing bridge allowing periodic endpoint and call-cut arguments to be used after, not before, variable-order normalization.

---

## 1. Finite nested episodes

A **finite nested episode** is a finite source-history diagram with:

- one outer labelled order `N`;
- root-valued states and at most one normalized atom at every active order;
- genuine forward equal-face cancellations which launch lower-order child histories;
- inverse return expansions governed by the complete root/equality/good-disjoint/missing-index table;
- ordered incidence, cap, route, support and mark data retained at every boundary;
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

- both endpoint source states;
- every exterior ordered incidence;
- cap, route and side-root data;
- surviving active marks;
- the final root or first-exit atom returned by the child.

It contains no lower-order history vertex and no new cancellation call.

### Central-mark-consuming call

If the cancelled central edge carried an active mark, first apply the exact mark-deletion semantics:

\[
a\longrightarrow a-1.
\]

Then apply the same physical call-free child lift to the cancellation outputs and returned roots.

The fixed-order replacement begins at the marked parent state and ends at the correct root/atom parent state with that mark absent. A newly inserted central edge remains unmarked, as required by `WELD_CENTRAL_MARK_CANCELLATION_POP_V1.md`.

Thus mark consumption is preserved as a complete-state change while the order-changing bubble is removed.

### Lemma 3.1 — one-call elimination

Replacing an innermost call:

1. preserves the complete boundary state of its containing episode;
2. introduces no new call;
3. changes no history outside the call collar;
4. lowers the call count by exactly one:
   \[
   \boxed{\kappa(\mathcal E')=\kappa(\mathcal E)-1.}
   \]

---

## 4. Induction on call count

### Theorem 4.1 — finite episode compression

Every finite nested episode has a fixed-outer-order replacement with the same complete outer boundary and no genuine cancellation call.

The replacement uses root-valued states and at most one normalized atom, together with any strict mark-consumption changes already present in the original episode.

### Proof

Induct on `kappa(E)`.

- If `kappa(E)=0`, the episode is already fixed-order.
- If `kappa(E)>0`, choose an innermost call and apply Lemma 3.1. The resulting episode has one fewer call and the same outer boundary. Apply the induction hypothesis.

The process terminates because `kappa(E)` is a finite nonnegative integer. ∎

This proof never assumes that a lower-order history is pointwise weld-relative. The needed active-diagonal and support-switch overlaps are supplied by the bounded source lifts inside the call-free theorem.

---

## 5. Repeated complete states

Assume the outer boundary consists of two occurrences of the same literal complete state

\[
\Xi_{\rm out}^{-}=\Xi_{\rm out}^{+}.
\]

Complete equality includes:

- labelled topology and root/token data;
- ordered cap and route data;
- every active ordered mark lineage;
- support transport and side attachments.

Apply Theorem 4.1 to obtain a fixed-order replacement with the same equal endpoints.

### Lemma 5.1 — no net mark consumption in a recurrence

The compressed recurrence contains no surviving central-mark deletion.

### Proof

A central-mark deletion strictly lowers the set/count of literal active marks, and no inverse move automatically resurrects the deleted incidences. Since the endpoint complete mark data are equal, the total net deletion is zero. The mark count never increases by the allowed overlap rules, so no deletion can occur on the recurrent segment. ∎

Thus a repeated complete-state episode compresses to an ordinary fixed-order root/one-token recurrence with unchanged marked boundary.

---

## 6. Fixed-order disposition

After compression, apply the existing fixed-order alternatives.

### Internal closed track

Use `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md`.

### Open track with normalized endpoint sides

Use the retained open-strip theorem.

### Repeated unresolved outer endpoint

Use `PERIODIC_OUTER_ENDPOINT_ROOT_SEAM_DISCHARGE_V1.md`.

### Pure root segment

Use the target topology arborescence; successful parent moves strictly lower `d_top`.

### Theorem 6.1 — no neutral variable-order recurrence

A finite repeated complete-state episode containing nested cancellation calls admits one of:

1. an accepted route/profile/bounded/separator exit;
2. strict central-mark progress;
3. a fixed-order root/one-token replacement with strictly smaller singular/boundary complexity;
4. a root-valued target-directed replacement.

In particular, variable-order nesting cannot support a neutral return to the same complete state.

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
&\text{fixed-order episode}\\
&\Downarrow\\
&\text{closed/open/periodic/root disposition}.
\end{aligned}
\]

Thus fixed-order track theorems are applied only after all order-changing calls have been removed by a proved finite induction.

---

## 8. Consequence for call-cut local rank

A cycle in the fully resolved parent macro graph may contain completed child calls. Apply Theorem 4.1 to the finite cycle segment and remove all such calls. The result is a fixed-order cycle with the same complete endpoints.

Theorem 6.1 excludes a nonexit neutral cycle. Therefore the finite parent macro graph has no nonexit sink strongly connected component after accepted and strict-mark-progress terminals are included.

This supplies the variable-order justification missing from the initial version of `FINITE_CALL_CUT_LOCAL_ATTRACTOR_RANK_V1.md`.

---

## 9. Assurance boundary

### Exact here

- induction on the finite number of nested calls;
- source-faithful elimination of one innermost call;
- preservation of central-mark consumption without mark resurrection;
- fixed-order compression of every finite repeated complete-state episode;
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
