# First cancellation terminalises the one-cross cap problem

## Research Lead ordinary-induction simplification v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `a6c9440f1e0c840307d45a3e5508a9ac852f44d8`

**Primary inputs:**

- `ONE_CROSS_SINGULAR_FIXED_ROUTE_REDUCTION_V1.md`;
- `EQUALITY_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md` read with `DDD_BOUNDED_RESIDUAL_ELIMINATION_V1.md`;
- `ROOT_SURGERY_AUTOMATIC_CATEGORY_SAFETY_V1.md`;
- `CHILD_CONTEXT_FIDELITY_AFTER_ROOT_CANCELLATION_V1.md`;
- `ARBITRARY_EDGE_THREE_RECONNECTION_CATEGORY_V1.md`;
- `ROOT_VALUED_ALTERNATIVE_INVERSE_CANCELLATION_INSERTION_V1.md`;
- `QUADRUPLE_EQUALITY_THREE_VERTEX_BORROWING_ROOTIFICATION_V1.md`;
- `DOUBLED_DISJOINT_THREE_VERTEX_BORROWING_DICHOTOMY_V1.md`;
- the inverse root/zero/co-root `2--2` table;
- R2.4--R2.6 fixed-order one-atom disposition, read through
  `CELLWISE_ROOT_SEAM_AND_CONSTANT_RUN_TRACK_ERASURE_V1.md` and
  `R2_6_CELLWISE_SEAM_RUN_INTERFACE_AUDIT_AND_PDL_HANDOFF_V2.md`;
- `GLOBAL_SMALL_CUT_COMPLETION_AND_GLUING_V1.md`;
- `BOUNDED_DIRECT_PAIRING_CAP_TERMINAL_V1.md`;
- the loop/bridge outer shell.

**Status:** authorial proof simplification. In the controlling one-cross proof, lower-order witnessed contextual recursion is unnecessary. Starting from the blocked equality or DDD lock, follow only route-preserving potential-lowering root NNIs until the first equal-face cancellation. At every step inspect the parallel cap target. A target-invalid NNI already exposes a two-cut or bounded branch. At the first target-valid cancellation, ordinary lower-order solubility applies directly to the actual smaller target cap closure, not merely to the inherited cross closure. Any root flow on that smaller cap target may be inserted back by the exact inverse-cancellation table. The finite prefix before the first cancellation is pure fixed-order root-NNI topology, so R2.4--R2.6 returns the resulting root/one-atom state to the original target. Thus the order-lowering layer is one ordinary strong-induction step, with no nested `Q` call, variable-order bubble compression, resolved-call SCC, or stack rank.

This is an authorial candidate. It requires PDL reconstruction and independent audit. It does not by itself establish the five-CDC theorem.

---

## 1. Parallel one-cross context

Let `P_0` be an ordered cubic four-pole with outer terminals

\[
t_1,t_2,t_3,t_4.
\]

Fix:

- the original two-vertex cap `C_i` of matching `M_i`;
- one valid cross reconnection `E_j`, `j\ne i`;
- the target cap closure
  \[
  \widehat G_0=P_0\cup C_i;
  \]
- the selected cross closure
  \[
  G_{j,0}=P_0\cup E_j;
  \]
- one specified root-valued flow `lambda_0` on `G_{j,0}`.

Assume both closures are connected, loopless, bridgeless, and cubic, and let

\[
N=|V(\widehat G_0)|.
\]

The one-cross boundary reduction gives exactly one of:

1. the selected boundary state lies in `K_i`, so the original cap glues;
2. a separating equality/DDD Kempe component gives the horizontal rescue;
3. the selected flow enters an equality or DDD fixed-route lock with physical route `M_i`.

Only Case 3 remains below.

---

## 2. The synchronized source sequence

At stage `r` retain:

- an ordered four-pole `P_r`;
- the cross closure
  \[
  G_{j,r}=P_r\cup E_j
  \]
  carrying a root flow `lambda_r`;
- the parallel target closure
  \[
  \widehat G_r=P_r\cup C_i;
  \]
- the same ordered outer terminals, cap block, and route record.

The cross flow determines the equality or DDD triangle labels and the monotone potential.

### Important asymmetry

The root flow `lambda_r` is a flow on `G_{j,r}`. It need not glue `C_i`, so no root flow on `\widehat G_r` is assumed.

The source move selected on `P_r` nevertheless defines a parallel topology move on both closures because `C_i` and `E_j` are exterior gadgets and every surgery is internal to `P_r`.

---

## 3. Root-NNI step and parallel-target test

Assume no equal adjacent source triangles are present. The equality or DDD potential theorem supplies a root-valued `2--2` NNI on the cross flow which strictly lowers the corresponding same-order potential.

Apply the same local topology replacement to the parallel target `\widehat G_r`.

### Cross side

Because the NNI is root-valued under `lambda_r`, the new cross closure `G_{j,r+1}` is connected and bridgeless and carries the new root flow `lambda_{r+1}`.

### Target side

No root-valuedness is assumed on `\widehat G_r`. Use the purely topological NNI category alternative.

Exactly one of:

1. `\widehat G_{r+1}` is connected, loopless, bridgeless, and cubic;
2. `\widehat G_r` has a cyclic two-cut;
3. `\widehat G_r` has a bounded acyclic/parallel/low-port degeneration.

In Cases 2--3, solve `\widehat G_r` by the established small-cut or bounded theorem, then return through the already accumulated pure NNI prefix by the fixed-order theorem of Section 8. The branch is complete.

In Case 1, continue.

### Route test

If the selected root move changes the physical route/profile away from the blocked `M_i` sector, the route table produces a `K_i` boundary root state on the current four-pole. Glue `C_i` to obtain a root flow on the current target `\widehat G_{r+1}` and return through the pure NNI prefix by Section 8.

Thus an internal continuation step is exactly:

\[
\boxed{
\text{route-preserving root NNI on the cross flow}
\;+
\text{valid parallel target NNI}.}
\]

---

## 4. Finite arrival at the first cancellation

On an internal continuation, the relevant potential strictly decreases:

- equality:
  \[
  \mathcal P_{\rm eq}=(E,\Phi,|V|),
  \]
  with the first two coordinates decreasing under root NNIs;
- DDD:
  \[
  \mathcal P_{\rm DDD}=(\Omega,|V|),
  \]
  with `Omega` decreasing under root NNIs.

At fixed vertex order these are nonnegative integer potentials. Therefore a route-preserving, target-valid root-NNI sequence cannot continue indefinitely.

The no-local-minimum theorems say that every nonempty carrier with no equal adjacent pair has another strictly decreasing root NNI. Consequently finite termination before a route/target-category exit occurs exactly when an equal adjacent support-triangle pair appears.

Let

\[
P_0\to P_1\to\cdots\to P_s
\]

be the resulting finite prefix and let the first equal-face cancellation be selected in `P_s`.

### Theorem 4.1 — pure-prefix property

The strict prefix

\[
P_0\to\cdots\to P_s
\]

contains only root-valued `2--2` NNIs on the cross flow. It contains:

- no earlier cancellation;
- no lower-order call;
- no nonterminal support switch;
- no raw zero/co-root state;
- no variable-order episode.

The cap and cross gadgets are unchanged throughout.

---

## 5. Parallel disposition of the first cancellation

Cancel the equal-face pair in the cross closure. Let the resulting four-pole be `P^-` and define the parallel descendants

\[
G_j^-=P^-\cup E_j,
\qquad
\widehat G^-=P^-\cup C_i.
\]

The cancellation preserves the ordered outer terminals, cap index, cap block, and route data and satisfies

\[
|V(\widehat G^-)|=N-2.
\]

The inherited cross output is root-valued and componentwise bridgeless.

Use the child-context category theorem.

### Case 5.1 — disconnected cross output

Then the current parent target `\widehat G_s` already has:

- a two-edge cut;
- a cyclic four-cut;
- or a bounded acyclic low-port shore.

Solve `\widehat G_s` by the exact cut/bounded theorem and return through the pure NNI prefix.

### Case 5.2 — connected cross output but invalid parallel target

The simultaneous three-reconnection category theorem gives on `\widehat G_s`:

- a cyclic cut of size at most four;
- or a bounded loop/parallel/triangle/theta/acyclic/low-port degeneration.

Solve that current target and return through the pure NNI prefix.

### Case 5.3 — route change at cancellation

The descendant cross root state enters the cap profile `K_i`. Gluing `C_i` gives a root flow on `\widehat G^-`. Use it as the returned lower target flow in Section 6.

### Case 5.4 — genuine smaller target

`\widehat G^-` is connected, loopless, bridgeless, cubic, and has order `N-2`.

Invoke ordinary strong induction:

\[
P_{N-2}(\widehat G^-).
\]

Choose one arbitrary root flow

\[
\nu:E(\widehat G^-)\to R_5.
\]

No relation between `nu` and the inherited cross flow is required.

### Key point

The lower induction is applied to the actual child **target cap closure** `\widehat G^-`, not to the inherited child cross closure `G_j^-`.

Therefore the selected lower root flow is already cap-compatible at the physical child target. No lower witnessed proposition `Q_{N-2}` is needed.

---

## 6. One arbitrary-flow inverse cancellation

The cancelled pair created two ordered output edges in `\widehat G^-`. Let their values under `nu` be

\[
a,b\in R_5.
\]

Evaluate the exact inverse insertion table.

### Distinct intersecting roots

Use the original equal-face inverse insertion. The predecessor target `\widehat G_s` receives a root flow.

### Equal roots

Borrow one adjacent root vertex and use the direct root-valued alternative inverse insertion. No zero state is created.

### Disjoint roots, good borrow

Use the direct root-valued alternative inverse insertion. No co-root state is created.

### Disjoint roots, missing-index borrow

The inverse produces exactly one standard normalized transport atom

\[
(Q_i,Q_j,ij).
\]

No second atom and no lower-order call appears.

### Local identification

A loop, parallel, insufficient-borrow, or separator coincidence is an exact bounded/two-cut/low-port terminal on the current order-`N` target.

### Theorem 6.1 — single-pop trichotomy

Every arbitrary lower target root flow gives at the first cancellation exactly one of:

\[
\boxed{
\text{root state on }\widehat G_s,
\quad
\text{one standard co-root atom on }\widehat G_s,
\quad
\text{exact current-target terminal}.}
\]

The first two remain at order `N`; the third is solved by the named terminal theorem.

---

## 7. Narrow fixed-order inverse-prefix problem

It remains to return from the state at `\widehat G_s` through the inverse of

\[
P_0\to P_1\to\cdots\to P_s.
\]

By Theorem 4.1 this source word contains only `2--2` NNIs and all target graphs along the accepted prefix are connected, loopless, bridgeless, and cubic.

For one forced inverse NNI, the old diagonal value has exactly one of:

- root: retain the restored root topology;
- zero: use the other crossed root NNI;
- co-root: retain one oriented one-atom state.

Critical overlaps preserve the one-atom bound. No cancellation or order change is introduced.

The complete state records:

- labelled topology and ordered dart incidences;
- root labels and at most one atom;
- both crossed resolutions;
- cap block and `K_i` route orientation;
- support/side outputs and rooted attachments;
- surviving marks required by the fixed-order comparison.

---

## 8. Pure-NNI fixed-order return

Apply the fixed-order R2.4--R2.6 consumer, with R2.6 read through the cellwise seam/constant-run theorem.

### Root sector

Use the target-rooted topology arborescence.

### First failure

A failed forced inverse NNI creates at most one normalized co-root atom.

### Singular track

- put a local root seam at every pivot change;
- separate adjacent collars by identity subdivision;
- replace every constant-pivot interval by the identity product of its unique nonpivot root history;
- glue on literal complete endpoint states;
- use normalized endpoint collars and the periodic root crosscut.

Thus no closed, normalized-open, or repeated-endpoint one-atom recurrence survives.

### Route/profile event

A boundary root state in `K_i` glues the original cap.

### Category/bounded event

Use the exact two-cut, bounded shore, theta, loop/bridge, or separately returned three-/four-cut consumer.

### Theorem 8.1 — pure root-NNI contextual return

Let

\[
T_0\to T_1\to\cdots\to T_s
\]

be a finite source history consisting only of internal `2--2` NNIs, with fixed ordered cap boundary. Given at `T_s` either a root state or one normalized co-root atom, the inverse contextual procedure finitely produces:

1. a root flow on the original cap target `T_0\cup C_i`; or
2. an exact small-cut/bounded/outer-shell construction which itself produces such a root flow.

No lower-order call is opened.

---

## 9. First-cancellation terminalisation theorem

### Theorem 9.1

Assume ordinary root solubility for every connected loopless bridgeless cubic graph of order strictly less than `N`.

Let one selected valid cross closure of an order-`N` cap context carry any specified root flow. Then the original cap closure has a root flow.

### Proof

1. Use the one-cross boundary theorem. Immediate cap compatibility or horizontal rescue is done.
2. In the fixed-route lock, repeatedly choose the monotone root NNI while synchronously testing the parallel target.
3. A route event or target-invalid NNI gives a current-target root solution or exact terminal; apply Theorem 8.1 to return.
4. Otherwise finite monotonicity reaches the first equal-face cancellation.
5. Apply the parallel cancellation disposition of Section 5.
6. A parent cut/bounded branch is solved and returned by Theorem 8.1.
7. In the genuine child branch, solve the actual smaller target cap closure by lower `P`.
8. Apply the single-pop trichotomy of Section 6.
9. Apply Theorem 8.1 to the pure NNI prefix.

Every branch yields a root flow on the original cap closure. ∎

---

## 10. Consequence for induction architecture

The controlling order induction becomes ordinary strong induction on target vertex number.

At level `N`:

1. assume `P_n` for every `n<N`;
2. R1 supplies one valid smaller cross closure;
3. lower `P` supplies the initial cross root flow;
4. Theorem 9.1 restores the original cap;
5. hence `P_N` holds.

No simultaneous `Q_N/P_N` induction is required.

---

## 11. Superseded machinery for the controlling route

The following results remain mathematically meaningful as stronger history-preserving or general mixed-history statements, but are not dependencies of Theorem 9.1:

- recursive lower witnessed `Q_n` calls;
- child-history source lifts through the weld;
- active-diagonal six-leaf weld movies;
- support-switch source-pop histories;
- suspended ancestor-mark transport through nested bubbles;
- innermost and variable-order bubble compression;
- resolved-call parent macro graph `M_N`;
- attractor rank `d_N`;
- stack or outermost-child terminal-unwind algorithms;
- v6/v6.1/v6.3 mixed-history master as the controlling cap-restoration route.

They are not declared false. They are bypassed by stopping at the first cancellation and invoking ordinary lower-order solubility on the actual smaller target cap closure.

Still controlling:

- the one-cross boundary/fixed-route theorem;
- equality and DDD monotone root-NNI potentials;
- target-parallel category tests;
- the first cancellation child-target theorem;
- arbitrary-flow inverse insertion;
- R2.4--R2.6 pure fixed-order one-atom return;
- cut/bounded/outer-shell consumers.

---

## 12. PDL reconstruction obligations

PDL must independently verify:

1. the root-NNI-only strict-prefix property;
2. strict decrease and finite arrival at route escape or the first cancellation;
3. the parallel target category test at every root NNI;
4. preservation of the ordered cap boundary along the synchronized prefix;
5. the exact four branches of the first cancellation target disposition;
6. that lower `P` is applied to `\widehat G^-`, not `G_j^-`;
7. arbitrary-flow validity of the single inverse insertion table;
8. isolation of missing-index as the sole one-atom row;
9. pure-NNI inverse-prefix transfer with no cancellation call;
10. v6.2 cellwise consumption of every fixed-order one-atom recurrence;
11. exact terminal census and named consumers;
12. ordinary strong-induction closure `P_{<N}\Rightarrow P_N`.

Return either:

- `AC-PD-5CDC FIRST-CANCELLATION RETURN — COMPLETE-DRAFT`; or
- one exact counterexample/interface failure.

---

## 13. Trust boundary

### Closed at Research Lead authorial level

- first-cancellation stopping rule;
- pure root-NNI prefix;
- synchronized parallel target test;
- ordinary lower solution of the actual child target cap closure;
- one arbitrary-flow inverse pop;
- pure fixed-order R2.4--R2.6 return;
- elimination of variable-order recursion from the controlling cap-restoration route;
- ordinary strong-induction architecture.

### Required before promotion

- PDL reconstruction;
- independent audit of the potentials, target-parallel category maps, single-pop table, fixed-order cellwise theorem, and every cut/bounded consumer;
- updated proof DAG and supersession index.

### Not claimed

- present PDL completion;
- independently accepted cap restoration;
- universal five-support/five-CDC theorem;
- Lean verification;
- Curator/canonical corpus status;
- manuscript, release, arXiv, DOI, peer review, or publication status.
