# Level-sensitive terminal collapse and outermost unwind

## Research Lead result-semantics correction v1.2

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Original parent head:** `6246ef4965724765f09a2e1eddef7d9e8d7456a9`

**Parents:**

- simultaneous strong induction `Q_N` then `P_N`;
- child-context fidelity after root cancellation;
- witnessed innermost-bubble compression and full-labelled genealogy;
- the complete inverse-insertion endpoint table;
- `TARGET_TOPOLOGY_ARBORESCENCE_FIXED_ORDER_V1.md`;
- the v6.2 cellwise fixed-order no-neutral-recurrence theorem;
- `ROUTE_CHANGE_TERMINAL_CONTEXTUAL_TRANSFER_V1.md`;
- `BOUNDED_DIRECT_PAIRING_CAP_TERMINAL_V1.md`;
- `FULL_DEFECT_TREE_NNI_DESCENT_V1.md`;
- `GLOBAL_SMALL_CUT_COMPLETION_AND_GLUING_V1.md`;
- `R2_TO_R1_CAP_RESTORATION_AND_OUTER_SHELL_INTERFACE_V1.md`.

**Corrects:**

- `TERMINAL_UNWIND_FROM_CHILD_SEPARATOR_SOLUTION_V1.md` insofar as an intermediate child/ancestor exit was allowed to stop the outer proof;
- the external result type of `Q_N` insofar as `P_N` later treated a naked accepted exit as a root flow on the original graph;
- v1 of this file insofar as it did not justify why the remaining parent prefix is fixed-order;
- v1.1 of this file insofar as it unwound every nested frame separately and thereby failed to record the fixed-order child prefixes lying between successive cancellation frames.

**Status:** exact authorial correction of terminal result semantics. Continuing child results carry witnessed histories. If any terminal result occurs at any depth inside the first live order-lowering call of an order-`N` execution, abandon the entire lower-order child execution, including all nested frames and inter-frame prefixes. Invoke the already available ordinary proposition on the exact outermost live child target of order at most `N-2`. Pop only that outermost frame using the actual returned roots. Every earlier completed call in the order-`N` parent prefix already has a continuing witness and is compressed to a fixed-order replacement. The remaining inverse transfer is therefore purely order `N`. Its exact route/bounded/two-cut terminal census is consumed to a root flow on the original graph. No naked accepted-exit constructor survives.

No PDL completion, independent assurance, or global five-CDC theorem is claimed.

---

## 1. The result-type mismatch

The earlier proposition had the schematic output

\[
Q_N(\lambda)=
\text{witnessed cap return}
\quad\text{or}\quad
\text{accepted exit}.
\]

The proof of ordinary solubility then used `Q_N` as though both branches supplied a root flow on the original graph.

That is false without a consumer.

- A route change on a surgery descendant is only a cap-compatible descendant root state.
- A child separator need not persist through ancestor insertion.
- A bounded child graph is not the parent graph.
- An internal category flag is not a theorem endpoint.

---

## 2. Correct external proposition

Let `G=P union cap_i` be a connected loopless bridgeless cubic graph of order at most `N`. Let `G_j=P union E_j` be one valid selected cross closure and let `lambda` be any specified inherited root flow on `G_j`.

### Proposition `Q_N^solve`

There exists a root-valued `E_5` flow on `G`.

The proof certificate is exactly one of:

1. **continuing witnessed certificate:** a finite decorated contextual history begins at `lambda` and reaches an original-cap-compatible root state;
2. **terminal outer-collapse certificate:** one live lower-order child execution is abandoned, the exact outermost live child target is solved by lower-order ordinary existence, its single parent frame is popped source-faithfully, and the already witnessed parent prefix is transferred back at fixed order to a root solution of `G`.

A route/bounded/separator/category token may occur internally but is never an external result.

---

## 3. The first live order-lowering call

Run the specified order-`N` inherited-flow strategy.

If no cancellation call is live, every terminal is already an order-`N` terminal and is consumed by Section 8 below.

Otherwise let

\[
\mathcal F
\]

be the first still-live cancellation frame encountered from the order-`N` parent execution. Its data are:

- parent cancellation state `C` of order `N`;
- exact connected loopless bridgeless cubic child target `H` of order `n\le N-2`;
- inherited child root flow `mu`;
- ordered child edge lineages `e,f`;
- labelled parent vertex slots;
- complete cap, route, support, side-output, incidence, and surviving/suspended-mark boundary data.

Inside the child execution there may be arbitrary nested calls and fixed-order prefixes.

### Continuing child outcome

If the child returns a decorated history beginning at `mu`, use source-faithful generator lifts and witnessed bubble compression. The parent strategy resumes.

### Terminal child outcome

If any descendant inside that child execution becomes terminal, abandon the whole child execution rooted at `H`.

Discard:

- every nested frame;
- every inter-frame child prefix;
- every child route, cut, bounded, or category label;
- every child-only mark.

Retain only the exact graph `H`, the stored outer frame `F`, and the order-`N` parent prefix preceding `C`.

Since `n<N`, the simultaneous strong-induction hypothesis already contains ordinary solubility `P_n`. Choose one root flow

\[
\nu:E(H)\to R_5.
\]

No history from `mu` to `nu` is required because the inherited continuation is abandoned permanently.

### Theorem 3.1 — outermost live child collapse

Every terminal result at arbitrary nested depth inside the first live order-lowering call may be replaced by one arbitrary root flow on that call's exact child target `H`.

There is no need to pop inner frames or transport their terminal data.

---

## 4. Why the remaining parent prefix is fixed-order

Let

\[
\Pi:C_0\rightsquigarrow C
\]

be the order-`N` parent execution before the live cancellation at `C`.

Every order-lowering call occurring strictly before `C` has already returned successfully; otherwise it would be an earlier live frame. Each such completed call therefore has:

- an inherited child history witness;
- source-faithful generator lifts;
- complete labelled seam equality;
- a witnessed fixed-order bubble replacement.

Compress all these completed bubbles innermost-first.

### Lemma 4.1 — fixed-order parent-prefix normal form

The entire parent prefix `Pi` has a complete boundary-equivalent order-`N` replacement whose internal persistent cells are only:

- root `2--2` NNIs;
- bounded zero/one-atom normalization macros;
- switch--pop endpoint collars;
- explicitly suspended surviving ancestor marks;
- literal complete-state seam gluings.

There is no live lower-order call in this replacement.

This is exactly the normalized FOC supplied by witnessed bubble compression. It is the missing justification in v1.

---

## 5. One actual outer-frame pop

Evaluate the selected lower-order root flow `nu` on the stored lineages:

\[
p=\nu(e),\qquad q=\nu(f).
\]

Apply the exact insertion table.

- Distinct intersecting: original root insertion.
- Equal: direct alternative root insertion.
- Good disjoint: direct alternative root insertion.
- Missing index: one normalized `(Q_i,Q_j,ij)` atom.
- Loop, parallel, insufficient-borrow, or separator identification: exact order-`N` category outcome.

Thus the parent-order output is

\[
\boxed{
\text{root state}
\quad\text{or}\quad
\text{one normalized atom}
\quad\text{or}\quad
\text{exact order-}N\text{ terminal}.}
\]

The actual roots of `nu` are used. No generic weld attainability and no relation between `mu` and `nu` is assumed.

---

## 6. Pure fixed-order transfer through the compressed prefix

Starting at the normalized parent-order output of Section 5, transfer backward through the fixed-order replacement of `Pi`.

Use only:

- the inverse root/zero/co-root `2--2` table;
- target-rooted ordinary `2--2` arborescence moves;
- local zero normalization;
- one-atom first-failure grammar;
- cellwise pivot-change seams;
- constant-run identity strips;
- normalized endpoint collars;
- periodic root crosscut.

No new cancellation call is opened.

Every successful arborescence edge lowers topology distance. Every one-atom recurrence is removed by v6.2. The finite compressed prefix coordinate decreases when a source macro is crossed.

### Theorem 6.1 — fixed-order terminal return

The outer-frame pop followed by transfer through the compressed parent prefix finitely yields:

1. a root flow on the original target `C_0`;
2. a cap-compatible root state on an order-`N` descendant, which continues through the remaining fixed-order prefix while preserving its ordered `K_i` boundary word;
3. an exact order-`N` bounded/two-cut/outer-shell terminal.

A descendant route change is not a naked endpoint; it is a root state carried to the original topology.

---

## 7. Exact fixed-order category census

The actual fixed-order sources give a narrower terminal list than the generic word `category` suggests.

### NNI category failure

By `FULL_DEFECT_TREE_NNI_DESCENT_V1.md`, a local NNI in a connected bridgeless cubic graph gives exactly:

1. another connected bridgeless cubic graph;
2. a two-edge cut in the original graph;
3. a bounded acyclic or parallel-edge degeneration attached through at most two edges.

### Quadruple equality borrowing

The only bounded exception is the two-vertex singular theta, or a loop/parallel local identification.

### Doubled-disjoint borrowing

Good borrowing rootifies. Missing-index borrowing becomes the standard one-atom transport state. It introduces no new recursive or category row beyond the NNI census.

### Disconnected equal-face cancellation

Child-context fidelity gives an original two-edge cut.

### Direct zero-vertex terminal

Closing by the cap gives bridge plus two loops or the root-soluble theta graph.

### Route change

The exact route table gives a descendant `K_i` root boundary state; fixed-order transfer preserves the ordered boundary word until the original topology is reached.

### Theorem 7.1 — scheduler terminal census

Every terminal produced by the controlling fixed-order scheduler is one of:

- original-cap-compatible root state;
- cyclic two-cut;
- bounded acyclic one-/two-vertex shore;
- theta or parallel local degeneration;
- loop/bridge/singleton-cut outer-shell case.

Cyclic three- and four-cut theorems remain valid global outer-shell tools but are not required to classify a local fixed-order NNI failure unless an upstream source theorem explicitly returns them.

---

## 8. Outermost consumption

Only order-`N` terminals may end the terminal branch.

- **Original `K_i` root state:** glue the cap.
- **Cyclic two-cut:** solve the two strictly smaller edge completions by lower `P`, align roots, and glue.
- **Theta:** use an explicit root triangle.
- **Parallel local degeneration:** either theta, or the two external third edges form a two-cut; use the preceding cases.
- **Acyclic low-port shore:** use the exact one-vertex/two-vertex classification.
- **Loop/bridge/singleton cut:** use loop deletion/reinsertion or the outer-shell decomposition.

If a separately imported outer source theorem returns a cyclic three- or four-cut, use `GLOBAL_SMALL_CUT_COMPLETION_AND_GLUING_V1.md`; those outcomes are also exact lower-order constructions.

### Theorem 8.1 — no naked outer terminal

Every order-`N` terminal produced by the controlling strategy yields a root flow on the original graph.

---

## 9. Termination

Continuing mode is controlled by the resolved-call rank `(N,d_N)` and original-prefix induction.

Terminal mode has no live lower-order call after Theorem 3.1. It is ranked by:

\[
(\ell,\rho_{\rm fix}),
\]

where `ell` is the number of compressed parent-prefix macros still to cross and `rho_fix` is the fixed-order topology/one-atom rank inside the current macro.

Both are finite and lexicographically decrease.

### Theorem 9.1 — terminal outer-collapse termination

Terminal mode finitely produces a root flow on the original target and never returns to continuing mode.

---

## 10. Correct mutual induction

Assume `P_n` and `Q_n^solve` for every `n<N`.

### Prove `Q_N^solve`

- Run the specified inherited-flow strategy.
- Continuing lower calls use the witnessed branch of lower `Q_n^solve` and resume.
- Any terminal child result triggers Theorem 3.1.
- Use one actual outer-frame pop, fixed-order parent-prefix transfer, and Theorem 8.1.

Every branch gives a root flow on the original target.

### Prove `P_N`

- Theta is explicit when there is no simple edge.
- Otherwise R1 supplies a valid smaller cross closure.
- Lower `P` supplies one inherited root flow on it.
- `Q_N^solve` supplies a root flow on the original graph.

There is no exit-to-solution coercion.

---

## 11. Relation to prior versions

`TERMINAL_UNWIND_FROM_CHILD_SEPARATOR_SOLUTION_V1.md` retains:

- the continuing/terminal distinction;
- legitimate arbitrary lower-order flow selection after abandonment;
- the actual insertion endpoint table;
- the warning against cut persistence.

Its intermediate-exit propagation is superseded.

v1.1's framewise algorithm is also superseded. It was unnecessarily strong and did not explicitly account for fixed-order child prefixes between nested frames.

The controlling rule is:

> abandon the complete outermost live child execution, solve its exact child target by lower `P`, pop its one stored parent frame, compress all earlier completed parent calls, and return through the resulting fixed-order order-`N` prefix.

---

## 12. PDL reconstruction obligations

PDL must verify:

1. the external result of `Q_N` is an actual root flow;
2. continuing and terminal modes are disjoint;
3. the first live order-lowering frame and its exact child target are well-defined;
4. every earlier order-lowering call in the parent prefix has a continuing witness;
5. those earlier calls compress to the fixed-order alphabet of Lemma 4.1;
6. lower `P_n` is invoked only after abandonment and on the exact outermost live child target;
7. the actual roots on the stored lineages are used in the single pop;
8. the remaining transfer opens no cancellation call;
9. v6.2 consumes every fixed-order one-atom recurrence;
10. descendant `K_i` states continue to the original topology;
11. the scheduler terminal census of Section 7 is complete;
12. every outer terminal has a named root-solution construction;
13. terminal rank `(ell,rho_fix)` is well founded;
14. `Q_N^solve -> P_N` is literal.

Return either a complete-draft theorem or one exact obstruction.

---

## 13. Classification and trust boundary

### Closed at Research Lead authorial level

- result-type mismatch and correction;
- continuing/terminal split;
- outermost live child collapse;
- fixed-order parent-prefix compression;
- one actual source-faithful pop;
- pure fixed-order terminal return;
- exact scheduler terminal census;
- outermost terminal consumption;
- corrected mutual induction and R2-to-R1 output.

### Required before promotion

- PDL reconstruction;
- final integration with v6--v6.3;
- independent audit of FOC, v6.2, the terminal census, and the complete dependency DAG.

### Not claimed

- present PDL completion;
- independently assured R2.7 or cap restoration;
- universal five-support/five-CDC theorem;
- Lean, manuscript, curation, release, arXiv, DOI, peer review, or publication status.
