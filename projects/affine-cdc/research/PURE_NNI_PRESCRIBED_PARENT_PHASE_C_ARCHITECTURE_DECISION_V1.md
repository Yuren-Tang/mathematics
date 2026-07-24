# Prescribed-parent Phase C architecture decision

## Research Lead bounded-epoch verdict v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-01`  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `4b020b7bd3d47c3df1d54b8d967ab1c9da4ecd18`  
**Parents:**

- `PURE_NNI_PRESCRIBED_PARENT_STATE_INTERFACE_NORMAL_FORM_V1.md`;
- `PURE_NNI_PRESCRIBED_PARENT_PHASE_A_MINIMAL_AMBIENT_EMBEDDING_V1.md`;
- `PURE_NNI_PRESCRIBED_PARENT_PHASE_B_SUPPORT_CHANNEL_TRANSITION_OBJECT_V1.md`;
- `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `EQUALITY_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- the exact PDL prescribed-parent obstruction at `698bcf752b637ba0ac31d4d0e8b348ed6eaf79aa`.

**Phase-C verdict:** the prescribed-parent blocker is reduced to one exact same-order physical theorem: pure-NNI escape from an oriented DDD full-channel lock. The existing sources neither prove this theorem nor give a complete counterexample to it. Consequently v7.2 remains blocked at one named frontier. The arbitrary-flow first-cancellation architecture is not yet disproved, but it is not repaired.

---

## 1. What Phases A and B decide

### Phase A

The boundary witness

\[
(12,34,13,24)
\]

has complete prime ambient embeddings. It is not automatically a route, cyclic `2/3/4`-cut, or bounded terminal.

### Phase B

Every nonlocked embedding is repaired by:

\[
\text{zero or one crossed root NNI}
\to
\text{one separating channel switch}
\to
\text{one root NNI to the prescribed parent}.
\]

The unique horizontal failure is the four-channel DDD lock:

\[
D_i\in L_i=C_j-D_i-C_k,
\]

with all relevant physical channels routed by the prescribed parent matching `M_i` and joining the two marked roots.

A fourteen-vertex prime example realizes this node. Its complete horizontal state component has `240` labelled root states and no parent realization.

Thus the local `(4,2,2)` word has been fully consumed; the remaining datum is global component connectivity.

---

## 2. Why no rank is presently available

The following quantities fail as strict ranks on the Phase-B horizontal SCC:

- prescribed-parent central weight: constantly four;
- support-unordered boundary state: constantly `D_i`;
- uncoloured target distance: alternates between the two crossed neighbours of the parent;
- atom count: zero on root sheets and one only in the comparison presentation;
- track length: may be erased without realizing the parent;
- number of support components: need not change monotonically;
- finite-state recurrence count: repetition is exactly the SCC phenomenon.

The `240`-state certificate rules out any claim that one of these already displayed quantities decreases on every horizontal transition.

No replacement rank is defined.

---

## 3. What the DDD potential does prove

For a root-labelled DDD four-pole with boundary multiset

\[
12,12,34,34,
\]

the established potential

\[
\mathcal P_{\mathrm{DDD}}=(\Omega,|V|)
\]

has the following exact local alternative:

1. a strictly `Omega`-lowering root `2--2` Pachner flip;
2. an equal-face `2--0` cancellation.

Following these moves finitely gives route/profile escape, a named separator/category result, a bounded direct matching, or a bounded residual carrier.

This is a valid **mixed root-surgery** descent.

It is not a pure-NNI prescribed-parent theorem because the strict decrease at an equal-face pair may use the second coordinate only after deleting two vertices.

---

## 4. Equal-face obstruction to a pure-NNI rank

Let two adjacent vertices carry the same root triangle

\[
\{a,b,a+b\}.
\]

The four exterior branch word is a doubled intersecting word. Its three binary pairings have type

\[
(0,2,2).
\]

There are two root crossed placements and one zero placement.

The ordinary root NNI between the two crossed placements:

- preserves graph order;
- preserves the unordered pair of equal source triangles;
- preserves `Omega`;
- is reversible.

The established strict DDD/equality potential uses equal-face cancellation, not this reversible root NNI, to decrease the surgery measure.

Therefore no strict pure-NNI rank follows from the existing potential tables. A new theorem must show that one crossed placement changes the physical channel route, exposes a named terminal, or decreases some new complete-state coordinate. None is currently proved.

---

## 5. Smallest remaining implication

### Target `FC-PURE-NNI-ESCAPE`

Let

\[
S=(N,G,\delta,\lambda,\chi,P,\mathfrak B,\kappa,\mathscr H,\mathfrak a,\tau,\alpha)
\]

be a complete prime fixed-order prescribed-parent state satisfying:

1. the active ordered boundary has support-unordered class `D_i`;
2. `P` is the nonroot pairing `M_i`;
3. the two other pairings are root-valued crossed sheets;
4. on both crossed sheets, every one of the four DDD rescue channels joins the two marked parent roots;
5. `kappa` is the oriented fixed route `M_i`;
6. no named route, cyclic `2/3/4`-cut, or bounded terminal is present.

Prove that there is a finite source-faithful history using only:

- root-valued ordinary `2--2` NNIs;
- legal closed support-component switches;
- bounded one-atom normalization and the repaired seam/run macros;
- exact route/cut/bounded terminal moves;

and **no** `2--0` cancellation or lower-order call, which ends in exactly one of:

1. a separating DDD channel and hence the Phase-B parent repair;
2. a cap-compatible `K_i` route state;
3. a named `2/3/4`-cut or bounded terminal;
4. a root flow on the prescribed parent topology.

This is the smallest missing implication.

It is strictly stronger than:

- finiteness of the complete-state graph;
- absence of an unbounded DDD local minimum when cancellation is allowed;
- track erasure;
- the ten-state route table;
- horizontal one-switch rescue.

---

## 6. Why the fourteen-vertex certificate is not yet a counterexample

The `240`-state component is closed under:

- all closed support-component switches;
- the active NNI between the two crossed cap topologies.

It is not proved closed under every root NNI supported elsewhere in the ambient graph. Such an NNI can alter the four channel-component partitions while preserving the external `D_i` word and may create an escape or terminal.

Therefore the certificate proves:

- horizontal local repair is insufficient;
- an ambient theorem is indispensable.

It does not prove `FC-PURE-NNI-ESCAPE` false.

No `[COUNTEREXAMPLE]` disposition is justified.

---

## 7. Why an architecture change is not yet proved

A genuine architecture-change verdict would require one of:

1. a complete prime SCC closed under the entire allowed pure-NNI/support-switch alphabet;
2. an invariant forbidding prescribed-parent realization and every named terminal;
3. a theorem that every full-channel escape necessarily uses a new cancellation or lower-order call.

None has been established.

The existing DDD potential shows that cancellation is a sufficient escape mechanism, not that it is necessary.

Thus it would be premature to replace the arbitrary-flow first-cancellation proposition merely because the current local package is incomplete.

No `[ARCHITECTURE-CHANGE]` disposition is justified.

---

## 8. Conditional replacement proposition if the frontier fails

If `FC-PURE-NNI-ESCAPE` is disproved, the smallest plausible replacement for arbitrary lower-flow selection is not the old witnessed `Q_N` machinery. It is the profile-valued existential statement:

### `P_N^{\mathrm{pop}}`

For every valid first-cancellation child target together with its two stored output lineages and prescribed parent cap, there exists a root flow on the child target whose single-pop complete state is:

1. immediately parent-rootifiable;
2. horizontally separable after at most one crossed-sheet change;
3. or equipped with a named terminal certificate.

This proposition constrains the selected lower flow but does not demand a history from an inherited child flow.

No proof of `P_N^{pop}` or its induction closure is presently available. It is recorded only as the smallest architecture candidate conditional on failure of the pure-NNI escape theorem.

---

## 9. Effect on v7.2

### Retained reconstructed units

- R1 valid cross closure;
- one-cross boundary/fixed-route reduction;
- target-synchronized first-cancellation prefix;
- actual smaller target cap closure;
- arbitrary-flow single-pop table;
- missing-index source normalization;
- one-atom state-walk/seam/run/backtrack layer;
- exact terminal ledger;
- Phase-B horizontal prescribed-parent repair outside full-channel locks.

### Still conditional

- pure-NNI return through every stored prefix;
- exhaustiveness of terminal reachability;
- ordinary induction `P_{<N}=>P_N`;
- cubic five-support and downstream bridgeless five-CDC conclusions.

The symbols `rho_atom`, `d_top`, and finite SCC distance may not be used as completed ranks.

---

## 10. Final bounded-epoch classification

\[
\boxed{
\text{[BLOCKED-FRONTIER AC-RL-PURE-NNI-01]}}
\]

The smallest remaining implication is `FC-PURE-NNI-ESCAPE` of Section 5.

This is a same-order physical channel theorem. It neither reopens the old mixed-order architecture by default nor claims that a local repair exists.

---

## 11. Trust boundary

### Completed in this epoch

- exact state/interface normal form;
- complete Phase-A ambient realization and minimal prime witness;
- complete horizontal support-channel transition object;
- source-faithful repair of every nonlocked `(4,2,2)` state;
- explicit prime full-channel lock and `240`-state horizontal SCC;
- exact rejection of unsupported ranks;
- exact smallest remaining theorem and conditional architecture alternative.

### Not completed

- `FC-PURE-NNI-ESCAPE`;
- a complete pure-NNI SCC counterexample;
- profile-valued lower-flow induction;
- v7.2 ordinary induction closure;
- five-support or five-CDC theorem.

### No status change

No Lean theorem, Curator/canonical movement, manuscript, release, tag, arXiv, DOI, peer review, or publication status is asserted.
