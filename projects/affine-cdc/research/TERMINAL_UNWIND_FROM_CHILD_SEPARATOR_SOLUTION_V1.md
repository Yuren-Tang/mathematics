# A child separator exit unwinds by ordinary lower-order solubility, not cut persistence

## Research Lead witnessed-result consumer v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- the simultaneous strong induction on ordinary solubility `P_n` and witnessed return `Q_n`;
- `CHILD_CONTEXT_FIDELITY_AFTER_ROOT_CANCELLATION_V1.md`;
- the complete inverse-insertion endpoint table;
- `TARGET_TOPOLOGY_ARBORESCENCE_FIXED_ORDER_V1.md`;
- the fixed-order no-sink consumer;
- `ANCESTOR_INCIDENCE_GENEALOGY_GLUING_V1.md`.

**Status:** exact terminal-result consumer. If a lower witnessed child exits through a separator/category branch, one must not assume that the numerical cut size persists through ancestor insertions. Instead use the already available ordinary lower-order proposition `P_n` to obtain one root flow on the child target. Lift that root flow through the stored two-edge insertion interface by the local endpoint table and fixed-order consumer. This gives a root flow or accepted exit on the parent target. Repeat outward through the finite frame stack. The branch therefore terminates globally without a history back to the inherited child flow and without transporting the separator itself.

---

## 1. Mutual-induction setting

At target order `N`, the witnessed proposition `Q_N` is proved under the strong induction hypotheses

\[
P_n,\ Q_n
\qquad(n<N),
\]

where:

- `P_n` asserts ordinary root solubility of every admissible target of order at most `n`;
- `Q_n` asserts the witnessed relative return statement from one inherited cross flow.

Let one parent cancellation frame have child target

\[
H
\]

of order

\[
n<N.
\]

The frame stores two ordered child edge lineages

\[
e,f
\]

whose raw insertion restores the parent vertex slots, together with all outer cap, route and incidence data.

---

## 2. Separator/category child outcome

Suppose the child witnessed execution does not return to its inherited starting flow but exposes an accepted separator/category branch.

This branch supplies a proof that the child target lies in the ordinary theorem domain. By the already assumed proposition `P_n`, choose a root-valued flow

\[
\nu:E(H)\to R_5.
\]

No relation between `nu` and the inherited child flow is asserted or required.

### Why arbitrary choice is now legitimate

The parent continuation will not resume after this branch. We are constructing a terminal solution of the parent target and then unwinding terminally through every ancestor. Therefore no history from the inherited child state to `nu` is needed.

This is categorically different from a successful child pop, which must return a witnessed history in order to resume the parent search.

---

## 3. Lift one ordinary child solution to the parent

Let

\[
p=\nu(e),
\qquad
q=\nu(f).
\]

Raw insertion on the stored interface restores the two parent vertex slots and assigns central value

\[
x=p+q.
\]

Apply the complete endpoint table.

### Intersecting pair

If `p,q` are distinct intersecting roots, the stored inverse insertion is root-valued.

### Equal pair

If `p=q`, the raw insertion has one zero edge. The equality borrowing movie gives a root-valued alternative predecessor-order insertion, unless a bounded identification is already an accepted exit.

### Disjoint pair

If `p perpendicular q`, the borrowing dichotomy gives:

- a root-valued alternative insertion in the good case;
- one standard missing-index co-root state in the exceptional case;
- a bounded/category exit in the degenerate cases.

Thus the parent-order output is:

\[
\boxed{
\text{root state}
\quad\text{or}\quad
\text{one normalized co-root state}
\quad\text{or}\quad
\text{accepted exit}.}
\]

---

## 4. Restore the required parent topology

A root-valued alternative insertion need not be the exact topology expected by the parent continuation. This is harmless in a terminal unwind.

Use the fixed ordinary topology arborescence rooted at the required parent target.

- Every successful root parent move lowers topology-tree distance.
- A failed parent move creates one normalized co-root state or an accepted category/route exit.
- Every normalized co-root state is discharged by the fixed-order no-sink consumer.

### Theorem 4.1 — one-frame terminal lift

From any root flow on the child target, the stored parent interface yields, after finitely many fixed-order moves, exactly one of:

1. a root flow on the required parent target;
2. a route/profile terminal;
3. a bounded direct/theta terminal;
4. a separator/category exit at the parent level.

No lower-order recursive call and no history from the inherited child flow is used.

---

## 5. Outward terminal unwind

Suppose the parent itself is the child of an enclosing frame. If Theorem 4.1 gives a root flow on the current parent target, use it as the ordinary child solution for the next stored interface and apply the same theorem again.

If an accepted route/bounded/category exit appears at any level, the branch terminates there.

The live frame stack is finite.

### Theorem 5.1 — terminal stack unwind

A separator/category exit at any descendant depth produces, after finitely many outward interface lifts, either:

- a root flow on the outermost target context; or
- an accepted route, bounded, separator or category exit at some ancestor level.

Hence the descendant separator is a valid terminal result of the outer witnessed proposition.

### Proof

Induct on the number of enclosing frames. The base case is Theorem 4.1 at the outermost frame. For one more frame, first obtain a root solution or exit on the immediate parent, then apply the induction hypothesis. Each step removes one frame. ∎

---

## 6. No cut-persistence assumption

The theorem does not transport the child shore through insertion.

Indeed, if the four endpoints of the two stored output edges have side pattern

\[
(0,0;1,1)
\quad\text{or}\quad
(1,1;0,0),
\]

reinserting the two parent vertices increases the minimum extension of the child cut by two. A child three-/four-cut may therefore become an ancestor five-/six-cut.

This does not obstruct terminal unwind because the proof transports a root solution, not the separator boundary.

---

## 7. Interaction with witnessed returns

The result type of `Q_N` has two genuinely different branches.

### Continuing branch

A successful child return supplies an explicit history from the inherited child flow. Witnessed bubble compression lifts it and resumes the parent continuation.

### Terminal branch

A separator/category child result invokes `P_n`, chooses an ordinary child root flow, and terminally unwinds through all ancestors. It never resumes the inherited continuation.

Confusing these branches was the source of the apparent need for ancestor cut persistence.

---

## 8. Consequence for child-context fidelity

Combine with `CHILD_CONTEXT_FIDELITY_AFTER_ROOT_CANCELLATION_V1.md`.

- valid connected descendants are literal `Q_(N-2)` instances;
- successful root/route/direct returns lift witnessedly;
- separator/category outcomes terminate by Theorem 5.1.

### Classification

\[
\boxed{
\texttt{CHILD EXIT RESULT SEMANTICS CLOSED}
}
\]

No naked descendant separator is silently promoted to an ancestor cut.

---

## 9. Assurance boundary

### Exact here

- legitimate use of ordinary `P_n` only on terminal branches;
- complete one-frame root/atom insertion table;
- fixed-order restoration of the required parent topology;
- finite outward terminal unwind;
- removal of any cut-persistence assumption;
- separation of continuing witnessed returns from terminal existential solutions.

### Imported authorial mathematics

- mutual strong-induction order (`Q_N` before `P_N`);
- ordinary lower-order solubility;
- local insertion/borrowing theorems;
- fixed-order topology and atom consumer;
- labelled frame genealogy.

### Not claimed

- independent PDL reconstruction of this result-type split;
- unconditional R2.7 or global cap restoration;
- independent audit, Lean verification, manuscript integration, curation, release or publication.
