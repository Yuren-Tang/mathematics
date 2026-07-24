# Level-sensitive terminal collapse and outermost unwind

## Research Lead result-semantics correction v1.1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Original parent head:** `6246ef4965724765f09a2e1eddef7d9e8d7456a9`

**Parents:**

- simultaneous strong induction `Q_N` then `P_N`;
- child-context fidelity after root cancellation;
- the complete inverse-insertion endpoint table;
- `TARGET_TOPOLOGY_ARBORESCENCE_FIXED_ORDER_V1.md`;
- the v6.2 cellwise fixed-order no-neutral-recurrence theorem;
- `ROUTE_CHANGE_TERMINAL_CONTEXTUAL_TRANSFER_V1.md`;
- `BOUNDED_DIRECT_PAIRING_CAP_TERMINAL_V1.md`;
- `GLOBAL_SMALL_CUT_COMPLETION_AND_GLUING_V1.md`;
- `R2_TO_R1_CAP_RESTORATION_AND_OUTER_SHELL_INTERFACE_V1.md`.

**Corrects:**

- `TERMINAL_UNWIND_FROM_CHILD_SEPARATOR_SOLUTION_V1.md` insofar as it allowed an accepted route/bounded/separator/category label at an intermediate ancestor frame to stop the outward proof;
- the external result type of `Q_N` in `AC_PD_5CDC_R2_7_MUTUAL_INDUCTION_HISTORY_WITNESS.md` insofar as the subsequent proof of `P_N` treated every accepted exit as though it were already a root flow on the original graph;
- v1 of this file insofar as it spoke of one top pop followed by a completely unstratified no-call traversal of the whole remaining prefix.

**Status:** exact authorial correction of terminal result semantics. Continuing child results carry witnessed histories. Once any nested branch becomes terminal, the inherited continuation is abandoned. Terminal unwinding then proceeds outward through the finite stored call stack. At each proper lower-order parent level `m<N`, any root/atom/category outcome is replaced, when necessary, by an arbitrary root flow on that exact parent target using the already available ordinary proposition `P_m`. Only the final order-`N` frame cannot use `P_N`; there every result is consumed by the exact cap, route, bounded, or small-cut theorem. Therefore the external proposition `Q_N` returns an actual root flow on its original target, together with either a continuing history certificate or a terminal-unwind certificate. No naked accepted-exit constructor survives.

This file does not claim PDL reconstruction, independent assurance, or a global five-CDC theorem.

---

## 1. The result-type mismatch

The earlier witnessed proposition had the form

\[
Q_N(\lambda)
=
\text{witnessed cap return}
\quad\text{or}\quad
\text{accepted exit}.
\]

The proof of ordinary solubility then used

\[
P_{N-2}+Q_N\Longrightarrow P_N
\]

as though both outputs supplied a root flow on the original graph.

That coercion is invalid.

- A route change on a surgery descendant is only a cap-compatible descendant root state.
- A child separator need not persist with the same size through reinsertions.
- A bounded child graph is not literally the ancestor graph.
- An intermediate category label is not a root flow on the outer target.

The proof needs a level-sensitive consumer.

---

## 2. Correct external proposition

Let `G` be a connected loopless bridgeless cubic target of order at most `N`. Fix one valid selected cross closure and any specified inherited root flow `lambda` on it.

### Proposition `Q_N^solve` — witnessed-or-terminally-solved cap restoration

There exists a root-valued flow on the original cap closure `G`.

The construction returns one of two certificates.

1. **Continuing witnessed certificate.** A finite decorated source history starts at `lambda` and ends at a cap-compatible root state on the original four-pole.
2. **Terminal-unwind certificate.** At some descendant depth the inherited continuation is abandoned. The finite stored call stack is then unwound level by level, using lower-order ordinary solubility at every proper ancestor level and an exact terminal theorem at the final order-`N` level, until a root flow on `G` is produced.

Route/bounded/separator/category labels are internal control values only. They are not external conclusions of `Q_N^solve`.

---

## 3. Continuing versus terminal child results

Suppose an order-`m` parent cancellation creates a connected admissible child target `H` of order

\[
n=m-2
\]

with inherited root flow `mu` and a stored ordered insertion interface.

### Continuing result

If the child supplies a decorated history beginning at `mu`, use the labelled bubble-compression and source-pop theorems. The parent continuation resumes.

No unrelated child flow may be substituted.

### Terminal result

If any descendant of the child execution reaches a route, bounded, separator, or category terminal, abandon the inherited continuation permanently.

At the outer proof level `N`, every target order occurring inside this child is strictly less than `N`. Hence the simultaneous strong-induction hypotheses already contain the ordinary propositions `P_k` for all those orders.

One may therefore discard the nested terminal execution and choose an arbitrary root flow on the exact child target immediately below the next stored frame.

This use of arbitrary existence is legitimate precisely because the branch will never resume the inherited child search.

---

## 4. The stored call stack

Write the live cancellation frames from inner to outer as

\[
\mathcal F_r,\mathcal F_{r-1},\ldots,\mathcal F_1.
\]

For frame `F_j` let:

- `H_j` be its child target of order `n_j`;
- `G_j` be its required parent target of order `n_j+2`;
- `e_j,f_j` be the two ordered child edge lineages whose insertion restores the labelled parent vertex slots;
- the frame store all cap, route, incidence, support, side-output, and surviving-mark data.

The outermost frame has parent order `N`. Every other parent target has order strictly less than `N`.

After a terminal event, the proof no longer needs the nested source histories. It needs only:

1. one root flow on the current child target;
2. the next stored frame;
3. fixed-order restoration to that frame's required parent target.

---

## 5. One frame of terminal unwind

Assume a root flow

\[
\nu:E(H_j)\to R_5
\]

is available on the child target of frame `F_j`.

Put

\[
p=\nu(e_j),\qquad q=\nu(f_j).
\]

### 5.1 Actual insertion table

Evaluate the stored insertion on these actual roots.

- Distinct intersecting `p,q`: original root insertion.
- Equal `p=q`: direct alternative root insertion.
- Disjoint with good borrow: direct alternative root insertion.
- Missing-index case: one normalized `(Q_i,Q_j,ij)` atom.
- Loop, parallel, insufficient-borrow, or separator identification: an exact category outcome at the parent level.

Thus the immediate parent-order result is

\[
\boxed{
\text{root state}
\quad\text{or}\quad
\text{one normalized atom}
\quad\text{or}\quad
\text{exact parent-level category outcome}.}
\]

No simultaneous-weld attainability is assumed.

### 5.2 Pure fixed-order restoration

Restore the exact required topology `G_j` using only the fixed-order alphabet:

- target-rooted ordinary `2--2` arborescence moves;
- local zero normalization;
- one-atom first-failure grammar;
- cellwise pivot-change seams;
- constant-run identity strips;
- normalized switch--pop endpoint collars already contained in the frame boundary;
- periodic root crosscut if a complete fixed-order endpoint repeats.

No new equal-face cancellation call is opened during this restoration. The only order change is the stored insertion which pops the existing frame.

Every successful root arborescence edge lowers `d_top`. Every nonroot attempt enters the fixed-order one-atom consumer. The v6.2 no-neutral-recurrence theorem excludes an infinite fixed-order loop.

### Lemma 5.1 — one-frame output

One frame of terminal unwind finitely produces exactly one of:

1. a root flow on the required parent target `G_j`;
2. a cap-compatible root state on a parent-order descendant topology;
3. an exact bounded, separator, or category outcome at the parent order.

In Case 2 the boundary roots already lie in the required cap profile. Since all subsequent restoration moves are internal and preserve the ordered boundary word, continue fixed-order restoration rather than treating the descendant state as an external terminal.

---

## 6. Proper lower-order parent levels

Suppose the parent order of frame `F_j` is

\[
m<N.
\]

The strong-induction hypothesis contains `P_m` for the exact required parent target `G_j`.

### Theorem 6.1 — lower-level reset

At a proper lower-order parent level:

- if Lemma 5.1 gives a root flow on `G_j`, retain it;
- if it gives a descendant cap-compatible state or any bounded/separator/category outcome, abandon that local restoration and invoke `P_m` to choose one root flow on `G_j`.

Then use that root flow as the child solution for the next enclosing frame.

This does not propagate the terminal certificate, route, shore, or cut through the stack. It propagates only an ordinary root flow on the exact graph required by the next stored interface.

The arbitrary replacement is legitimate because the whole branch is already terminal and will never resume its inherited continuation.

---

## 7. Final order-`N` frame

At the outermost frame the required parent target is the original order-`N` graph `G`. The proposition `P_N` is not yet available, so no lower-level reset is allowed.

Apply Lemma 5.1 and consume the result exactly.

### Root flow on `G`

Done.

### Cap-compatible descendant root state

Continue the finite internal fixed-order restoration to the original topology. The ordered boundary root word remains in `K_i`; glue the original cap when `G` is reached.

### Zero-vertex direct matching

Closing by the cap gives either:

- two loops joined by a bridge, consumed by the singleton-cut/loop outer shell; or
- the root-soluble theta graph with roots `12,13,23`.

### Cyclic two-cut

Complete both shores by one edge, solve the strictly smaller completions by lower `P`, align the completion roots by one support permutation, and glue.

### Cyclic three-cut

Complete each shore by one cubic vertex, solve by lower `P`, align the boundary root triangles, and glue.

### Cyclic four-cut

Use the three strictly smaller cap completions, exact physical profile intersection, and the proved Type-T/Type-H elimination.

### Acyclic low-port shore

Use the exact one-vertex or two-vertex bounded classification.

### Loop, bridge, or singleton cut

Use loop deletion/reinsertion and the already closed outer-shell decomposition.

### Theorem 7.1 — outermost absorption

Every final order-`N` result produces a root flow on the original graph. No uninterpreted terminal constructor remains.

The load-bearing source condition is that every category outcome admitted by the fixed-order scheduler is accompanied by one of the exact outermost dispositions above. A generic word `category-safe` is not sufficient.

---

## 8. Finite framewise termination

The terminal unwind is ranked by

\[
\bigl(r,\rho_{\rm fix}\bigr),
\]

where:

- `r` is the number of stored frames still to pop;
- `rho_fix` is the finite fixed-order restoration rank inside the current frame, assembled from target-tree distance and the v6.2 one-atom disposition.

Inside one frame, `rho_fix` terminates. Completing or resetting that parent removes one frame, so `r` decreases by one.

### Theorem 8.1 — terminal stack unwind

A terminal event at arbitrary nested depth yields after finitely many steps a root flow on the original order-`N` target.

No child cut is transported through an insertion. No child history is required after abandonment. No call is opened inside one fixed-order frame restoration. Ordinary existence is invoked only at proper lower-order parent levels.

---

## 9. Correct mutual induction

Assume `P_n` and `Q_n^solve` for every `n<N`.

### Prove `Q_N^solve`

Run the specified inherited-flow strategy.

- Continuing child histories lift witnessedly and resume.
- A terminal child result switches irreversibly to the framewise terminal mode.
- At every proper lower parent level use Theorem 6.1 when needed.
- At the final order-`N` level use Theorem 7.1.

The continuing mode terminates by the resolved-call rank `(N,d_N)` and original-prefix induction. The terminal mode terminates by Theorem 8.1.

Thus every branch gives a root flow on the original target.

### Prove `P_N`

- If the graph has no simple edge, use the explicit theta flow.
- Otherwise use R1 to choose a valid smaller cross closure.
- Use lower `P` to choose the initial inherited root flow on that closure.
- Apply `Q_N^solve`.

The implication is now literal: `Q_N^solve` returns a root flow, not an accepted-exit token.

---

## 10. Relation to prior files

`TERMINAL_UNWIND_FROM_CHILD_SEPARATOR_SOLUTION_V1.md` retains:

- the distinction between continuing witnessed returns and terminal existential branches;
- legitimate use of lower-order ordinary solubility only after abandonment;
- the actual insertion endpoint table;
- the warning that cut size need not persist.

Its statement that an intermediate accepted exit may stop the whole proof is superseded.

The first version of this file's one-top-pop description is also superseded. The correct procedure is framewise:

\[
\text{lower }P
\to
\text{actual insertion}
\to
\text{pure fixed-order restoration}
\to
\text{lower-level reset or outermost absorption}.
\]

---

## 11. PDL reconstruction obligations

PDL must verify line by line:

1. the external result of `Q_N` is an actual root flow on the original target;
2. continuing and terminal modes are disjoint and terminal mode never resumes inherited continuation;
3. every live frame records an exact child target, required parent target, ordered insertion interface, and complete boundary data;
4. at every proper parent level `m<N`, `P_m` is already available;
5. arbitrary root-flow replacement occurs only after abandonment;
6. every frame pop evaluates the actual roots on the stored lineages;
7. fixed-order restoration uses no new cancellation call;
8. v6.2 gives termination for every one-atom fixed-order restoration;
9. descendant route states are continued as root states until the required topology is reached;
10. intermediate category outcomes are replaced by `P_m`, not propagated;
11. the outermost frame has the exact terminal census of Section 7;
12. every outermost category names a proved cap, theta, low-cut, bounded-shore, or outer-shell theorem;
13. frame count strictly decreases;
14. `Q_N^solve -> P_N` contains no hidden exit-to-solution coercion.

Return either a complete-draft theorem or one exact counterexample/interface failure.

---

## 12. Classification and trust boundary

### Closed at Research Lead authorial level

- identification of the old result-type mismatch;
- continuing versus terminal mode;
- abandonment semantics;
- level-sensitive use of lower-order `P_m`;
- actual insertion at every stored frame;
- pure fixed-order frame restoration;
- intermediate reset without cut/route propagation;
- outermost exact absorption;
- finite frame-count termination;
- corrected `Q_N^solve -> P_N` implication.

### Required before promotion

- PDL reconstruction of every frame and terminal interface;
- integration into the v6/v6.1/v6.2 master;
- independent audit of the terminal census and full dependency DAG.

### Not claimed

- present PDL completion;
- independently assured R2.7 or cap restoration;
- universal five-support/five-CDC theorem;
- Lean, manuscript, curation, release, arXiv, DOI, peer review, or publication status.
