# Level-sensitive terminal collapse and outermost unwind

## Research Lead result-semantics correction v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `6246ef4965724765f09a2e1eddef7d9e8d7456a9`

**Parents:**

- simultaneous strong induction `Q_N` then `P_N`;
- `CHILD_CONTEXT_FIDELITY_AFTER_ROOT_CANCELLATION_V1.md` and the PDL reconstruction;
- the complete inverse-insertion endpoint table;
- `TARGET_TOPOLOGY_ARBORESCENCE_FIXED_ORDER_V1.md`;
- the cellwise R2.6 fixed-order no-sink consumer;
- `ROUTE_CHANGE_TERMINAL_CONTEXTUAL_TRANSFER_V1.md`;
- `BOUNDED_DIRECT_PAIRING_CAP_TERMINAL_V1.md`;
- `GLOBAL_SMALL_CUT_COMPLETION_AND_GLUING_V1.md`;
- `R2_TO_R1_CAP_RESTORATION_AND_OUTER_SHELL_INTERFACE_V1.md`.

**Corrects:**

- `TERMINAL_UNWIND_FROM_CHILD_SEPARATOR_SOLUTION_V1.md` insofar as it allowed an accepted route/bounded/separator/category exit at an intermediate ancestor frame to stop the outward proof without first producing a solution of the current target;
- the conclusion of `Q_N` in `AC_PD_5CDC_R2_7_MUTUAL_INDUCTION_HISTORY_WITNESS.md` insofar as a naked accepted exit was returned while the proof of `P_N` immediately treated every `Q_N` outcome as a root flow on the original graph;
- any claim that child exits propagate to the outer target merely because the outer cap shore is unchanged.

**Status:** exact authorial correction of the terminal result type. A continuing child result must carry a witnessed history. Once any descendant branch becomes terminal, the inherited continuation is abandoned. One invokes ordinary lower-order solubility on the outermost still-live child target, performs the single stored top insertion, and unwinds the remaining finite original prefix without further recursive calls. Intermediate exits are never returned naked. At the outermost order, every terminal certificate is consumed by an exact cap, bounded, or small-cut theorem. Thus `Q_N` returns a root solution of its original target, with either a continuing witness or a terminal-unwind certificate.

No global five-support theorem is declared.

---

## 1. The mismatch in the old result type

The strengthened witnessed proposition was stated schematically as

\[
Q_N(\lambda)=
\text{witnessed cap return}
\quad\text{or}\quad
\text{accepted exit}.
\]

The subsequent proof of ordinary solubility used

\[
P_{N-2}+Q_N\Longrightarrow P_N
\]

and said that the terminal history supplies a root flow on the original target.

That implication is not valid if `accepted exit` is an uninterpreted return constructor.

In particular:

- a route change on a surgery descendant is only a cap-compatible descendant root state;
- a separator in a lower child is not the same separator on an ancestor graph;
- a bounded child graph restored through ancestor insertions is not literally the same graph;
- an intermediate category label is not yet a root flow on the outermost target.

The proof therefore needs a result consumer, not a broader exit vocabulary.

---

## 2. Correct external statement of `Q_N`

Fix a connected loopless bridgeless cubic target `G` of order at most `N`, a selected valid cross closure, and any specified inherited root flow `lambda` on that closure.

### Proposition `Q_N^solve` — witnessed-or-terminally-solved cap restoration

There exists a root-valued flow on the original cap closure `G`. Moreover the proof returns exactly one of two certificates.

1. **Continuing witnessed certificate.** A finite decorated history begins at `lambda`, crosses every selected source move, and ends at a cap-compatible root state on the original four-pole.
2. **Terminal-unwind certificate.** At some descendant depth the inherited continuation is abandoned; an ordinary root solution is selected on the outermost still-live lower-order child target; a finite source-faithful no-call unwind returns that solution through the stored top interface and the remaining original prefix to a root flow on `G`, or consumes an exact outermost bounded/small-cut terminal which itself supplies such a flow.

A naked route/bounded/separator/category label is an internal control result only. It is not an external conclusion of `Q_N^solve`.

---

## 3. Continuing and terminal child branches

Let a selected outer cancellation at one stage of the order-`N` history produce a connected admissible child target

\[
H
\]

of order

\[
n\le N-2
\]

with inherited root flow `mu`. The stored frame records the two ordered child edge lineages and the complete outer boundary data.

Invoke the lower witnessed proposition on `(H,mu)`.

### Continuing branch

If the child returns a decorated history beginning at `mu`, use witnessed bubble compression and the source-pop tables. The parent continuation resumes.

No unrelated child flow may be substituted here.

### Terminal branch

If any descendant inside the child execution reaches a terminal route/bounded/separator/category result, do **not** attempt to propagate that certificate through every nested frame and do not resume the inherited parent continuation.

Instead collapse the entire terminal child episode to the original top child target `H`.

Since

\[
n<N,
\]

the simultaneous strong-induction hypothesis already contains ordinary solubility

\[
P_n.
\]

Choose one root-valued flow

\[
\nu:E(H)\to R_5.
\]

No history from `mu` to `nu` is required, because the continuing branch has been abandoned permanently.

### Theorem 3.1 — terminal collapse to the outermost live child

Any terminal result at arbitrary nested depth may be replaced by one ordinary root flow on the outermost still-live lower-order child target `H`.

All inner frames and their terminal labels are discarded together with the abandoned continuation. Only the stored top insertion interface and the remaining order-`N` original prefix survive.

This is the unique legitimate place where an arbitrary lower-order root flow is selected inside the proof of `Q_N`.

---

## 4. One source-faithful top pop

Let `e,f` be the two stored ordered child edge lineages on `H`, and put

\[
p=\nu(e),\qquad q=\nu(f).
\]

Evaluate the actual top insertion.

- If `p,q` are distinct intersecting roots, use the original root insertion.
- If `p=q`, use the direct alternative root insertion.
- If `p,q` are disjoint with a good borrow, use the direct alternative root insertion.
- In the missing-index case, produce one standard `(Q_i,Q_j,ij)` atom.
- Loop, parallel, insufficient-borrow, or separator identifications produce one exact outer-frame category certificate.

Thus the top pop yields

\[
\boxed{
\text{root state}
\quad\text{or}\quad
\text{one normalized atom}
\quad\text{or}\quad
\text{exact outer-frame terminal}.}
\]

This is a source-faithful evaluation on the actual selected flow `nu`; it is not generic simultaneous weld attainability.

---

## 5. No-call terminal restoration of the remaining prefix

After the top pop, do not restart the equality/DDD search and do not make another lower-order call.

Cross the finite remaining original source prefix toward the original target.

### Inverse root `2--2` step

Use the exact root/zero/co-root table. A co-root output is one normalized atom and is consumed by the fixed-order cellwise no-sink theorem.

### Inverse equal-face step

Evaluate the actual two returned roots and use the same insertion table. Since the proof is now terminal, any alternative root insertion is followed by the fixed topology arborescence rather than by a resumed inherited search.

### Fixed-order restoration

At each order-`N` stage:

- root states move along the target topology arborescence;
- one-atom failures are consumed by local seams, constant-run identity strips, normalized endpoint collars, and the periodic crosscut;
- cap-compatible descendant root states remain root states and continue through the shorter original prefix;
- no lower-order call is opened.

The original-prefix coordinate decreases strictly whenever an original inverse step is crossed. The fixed-order rank decreases inside each normalization. Hence this terminal restoration is finite.

### Theorem 5.1 — no-call outer-prefix unwind

A root flow on the outermost live child target, after one source-faithful top pop, yields after finitely many no-call inverse steps exactly one of:

1. a cap-compatible root state on the original four-pole;
2. an exact bounded direct/theta terminal on the outermost target;
3. an exact outermost two-/three-/four-cut or acyclic-low-port terminal;
4. a singleton-cut/loop/bridge outer-shell terminal.

A route/profile event on a nonoriginal descendant is not absorbing. It is a cap-compatible root state which continues through the remaining original prefix.

---

## 6. Outermost terminal consumption

Only terminals on the outermost order-`N` target may end the proof. They are consumed immediately.

### Cap-compatible root state

A boundary state in the original cap profile `K_i` glues the cap and gives a root flow on `G`.

### Zero-vertex direct matching

Closing by the cap gives either:

- the bridge-plus-two-loops graph, consumed by the loop/singleton-cut outer shell; or
- the theta multigraph, with explicit roots `12,13,23`.

### Cyclic two-cut

Complete both shores by one edge, solve the smaller completions by lower `P`, align the completion roots by one support permutation, and glue.

### Cyclic three-cut

Complete each shore by one cubic vertex, solve by lower `P`, align the boundary root triangles by one support permutation, and glue.

### Cyclic four-cut

Use the three smaller cap completions, exact physical profile intersection, and the proved Type-T/Type-H local eliminations.

### Acyclic low-port shore

Use the exact one-vertex or two-vertex bounded classification.

### Loop/bridge/category

Delete/reinsert loops or decompose at the singleton cut using the already closed outer shell.

### Theorem 6.1 — no naked outer exit

Every outermost accepted terminal produces a root flow on `G` or enters an already proved outer-shell construction which produces one. No uninterpreted terminal constructor survives in the conclusion.

---

## 7. Correct mutual-induction proof

Assume `P_n` and `Q_n^solve` for all `n<N`.

### Prove `Q_N^solve`

Run the specified inherited-flow strategy.

- Continuing child histories lift witnessedly and resume.
- Any terminal child history collapses by Theorem 3.1 to a root flow on the outermost live lower-order child.
- Apply the top pop and no-call unwind.
- Consume the outermost terminal by Theorem 6.1.

The continuing strategy terminates by the resolved-call rank `(N,d_N)` and original-prefix induction. The terminal strategy terminates by finite prefix length and fixed-order rank.

Thus every branch gives a root flow on the original target `G`.

### Prove `P_N`

- If `G` has no simple edge, use the explicit theta flow.
- Otherwise choose the valid smaller cross closure supplied by R1.
- Use lower `P` to choose the initial inherited root flow on that closure.
- Apply `Q_N^solve`.

The conclusion is now valid because `Q_N^solve` returns a root flow, not a naked exit.

---

## 8. Relation to the old frame-by-frame unwind

`TERMINAL_UNWIND_FROM_CHILD_SEPARATOR_SOLUTION_V1.md` retains:

- the distinction between continuing witnessed returns and terminal existential branches;
- legitimate use of ordinary lower-order solubility only after continuation is abandoned;
- the actual insertion endpoint table;
- the warning that cut size need not persist through ancestor insertions.

Its outward algorithm is replaced by the stronger collapse rule:

> Once any nested child becomes terminal, discard the whole nested execution, invoke ordinary solubility on the outermost live lower-order child target, and unwind only the stored top interface plus the remaining original prefix.

Therefore no intermediate route/bounded/separator/category label needs to be transported through the frame stack.

---

## 9. PDL reconstruction obligations

PDL must replace the old external statement of `Q_N` and verify:

1. every internal accepted result is classified as continuing, cap-compatible descendant root, or terminal-collapse trigger;
2. any terminal trigger abandons the inherited continuation permanently;
3. `P_n` is invoked only on the outermost live child target of order `n<N`;
4. the top child target is connected, loopless, bridgeless, cubic, and carries the stored insertion interface;
5. one actual root flow on that target is evaluated by the exact insertion table;
6. the remaining original prefix is crossed without opening another lower-order call;
7. descendant route changes continue as cap-compatible root states rather than naked exits;
8. fixed-order atom normalization uses the v6.2 cellwise consumer;
9. only outermost exact terminals are absorbing;
10. every outermost terminal yields a root solution by a named theorem;
11. `Q_N^solve` returns a root flow on the original target;
12. the proof of `P_N` consumes that root-flow conclusion without an implicit exit-to-solution coercion.

Return either a complete-draft theorem or one exact obstruction.

---

## 10. Classification and trust boundary

### Closed at Research Lead authorial level

- identification of the result-type mismatch;
- witnessed versus terminal child semantics;
- terminal collapse to the outermost live lower-order child;
- legitimate lower-order arbitrary-flow selection only after abandonment;
- one source-faithful top pop;
- no-call fixed-order/original-prefix unwind;
- descendant route-state continuation;
- outermost-only terminal absorption;
- exact solution semantics for cap, bounded, and small-cut terminals;
- corrected `Q_N^solve -> P_N` implication.

### Required before promotion

- PDL reconstruction;
- integration with v6/v6.1/v6.2;
- independent audit of all terminal consumers and the complete dependency DAG.

### Not claimed

- present PDL completion;
- independently assured R2.7 or cap restoration;
- universal five-support/five-CDC theorem;
- Lean, manuscript, curation, release, arXiv, DOI, peer review, or publication status.
