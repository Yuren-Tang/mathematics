# Scope correction: a child-prefix decrease is not a parent-frame decrease

## Research Lead stack-order correction v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Corrects the Type-IV reading of:**

- `projects/affine-cdc/proof-development/AC_PD_5CDC_EQ_RETURN_5_NESTED_STACK_ORDER.md`.

**New source inputs:**

- `WELD_ACTIVE_DIAGONAL_SIX_LEAF_LIFT_V1.md`;
- `WELD_SUPPORT_SWITCH_SOURCE_POP_V1.md`;
- `WELD_RELATION_FIRST_EXIT_V1.md`;
- `NO_HIDDEN_GENEALOGY_FINITE_STATE_V1.md`.

**Status:** material theorem-engineering correction. The PDL bounded-depth stack idea and its push/successful-pop mechanism are sound in principle, but Type IV is not proved by the comparison written there. The strict child-history inequality

\[
m'<m_{\rm child}
\]

does not imply that the new parent-frame prefix is smaller than the stored parent continuation. These are coordinates of different frames. A returned zero/co-root state cannot be inserted into the parent key by renaming the child prefix.

The source-level first-exit theorems remain exact: the child step has genuinely been crossed and the returned atom lies on a strict child prefix. What remains is a correct continuation-machine order. One sufficient repair is a finite call-cut local rank together with a suspended-return phase. Under that additional rank, successful and first-`A/C` pops are strict without identifying child and parent prefix coordinates.

R2.7 remains blocked until that rank is supplied and reconstructed.

---

## 1. The invalid comparison

Let the stack immediately before one child pop be

\[
S=(\tau_0,\ldots,\tau^-_{\rm par},\sigma_{\rm child}).
\]

The stored parent continuation has numerical key

\[
k(\tau^-_{\rm par})=(N_{\rm par},m_{\rm par},a_{\rm par},r_{\rm par}).
\]

The child first-exit theorem gives a strict prefix

\[
m'_{\rm child}<m_{\rm child}.
\]

If the child is deleted and the stored parent is replaced by a new parent atom state, the stack comparison occurs at the parent position. Therefore one must compare the new parent key with

\[
k(\tau^-_{\rm par}),
\]

not with the deleted child key.

The inequality

\[
m'_{\rm child}<m_{\rm child}
\]

contains no comparison with `m_par` and cannot establish

\[
k(\tau'_{\rm par})<k(\tau^-_{\rm par}).
\]

### Proposition 1.1 — Type IV is open as written

The proof line

> the strict child-prefix result is represented as a strict parent-frame prefix coordinate

is an additional theorem, not a consequence of weld first exit. Until such an embedding is supplied, Type IV does not follow from the stated outer-to-inner lexicographic stack order.

This correction does not refute the source first-exit theorem or the possibility of a repaired stack order.

---

## 2. Source-level facts retained

The following are exact and unaffected.

### Active lower-order `2--2` step

`WELD_ACTIVE_DIAGONAL_SIX_LEAF_LIFT_V1.md` proves that an active marked diagonal is crossed at predecessor order by a bounded six-leaf movie:

- root-valuedly if `B` is preserved;
- with one standard co-root atom if it is the first `B -> C` exit.

### Lower-order support switch

`WELD_SUPPORT_SWITCH_SOURCE_POP_V1.md` proves that a legal child component switch gives:

- a root-valued expanded support switch if the output pair remains in `B`;
- one central zero/co-root atom if the switch is the first `B -> A/C` exit.

### Equal-face overlap

`WELD_MARK_EQUAL_FACE_OVERLAP_V1.md` proves:

- external ordered incidences transport canonically;
- external `2--0` overlap preserves `B`;
- a marked central edge is consumed by a genuine order-lowering cancellation.

Thus every child transition has a physical source disposition. The unresolved issue is numerical continuation rank, not local coefficient or incidence ambiguity.

---

## 3. Why a direct child-to-parent prefix identification is unnatural

The child history lives on the lower-order graph created by the parent cancellation. A first exit after `j` child steps returns an atom on the parent-order expansion of the child stage `H_j`.

The remaining strict child prefix

\[
H_0\to\cdots\to H_j
\]

is a witness for a new parent-order normalization task. It is not literally a suffix of the parent frame's pre-existing history word. In particular:

- it may have a different length;
- it may use mobile six-port lifts rather than the original parent moves;
- it may contain support-switch source pops;
- its topology labels belong to the expanded parent incidence universe.

Therefore the correct semantics is

\[
\boxed{
\text{child prefix}
\longmapsto
\text{finite parent normalization witness},
}
\]

not equality of two prefix coordinates.

---

## 4. Sufficient repaired frame semantics

Assume that for each fixed complete parent context there is a finite **call-cut local graph**:

- vertices are complete active parent states;
- accepted exits are terminal;
- a cancellation call is cut at the moment the parent continuation step has been consumed and is represented by a suspended-call terminal;
- all noncall local transitions have a finite rank.

Let

\[
b\in\{0,1,\ldots,B\}
\]

be a call-cut rank which strictly decreases before every chosen cancellation push.

Let

\[
\phi\in\{\mathrm{active},\mathrm{suspended}\}
\]

be a return phase, ordered by

\[
\mathrm{active}<\mathrm{suspended}.
\]

Let

\[
r\in\{0,1,\ldots,R\}
\]

be a finite active cleanup rank. A corrected numerical frame key may be taken as

\[
\boxed{
(N,m,a,b,\phi,r),
}
\]

with lexicographic order, where `m` denotes only a genuine parent continuation coordinate and is never replaced by a child prefix.

### Type I — active local progress

At fixed phase `active`, one of

\[
m,\quad a,\quad b,\quad r
\]

strictly decreases with all earlier coordinates fixed.

### Type II — cancellation push

Before appending the lower-order child:

1. consume the selected parent call-cut step, so `b` strictly decreases;
2. store the parent in phase `suspended`;
3. append the child frame of lower target order.

The decrease of `b` occurs before the phase increase and dominates it.

### Type III — successful pop

Delete the child and change the stored parent phase

\[
\mathrm{suspended}\to\mathrm{active}.
\]

Initialize any state-specific cleanup rank `r <= R`. The phase decrease occurs before `r` and makes the pop strict.

### Type IV — first `A/C` pop

Perform exactly the same phase transition as Type III, but initialize the active parent state with the returned zero/co-root atom.

The child prefix is retained only as a finite source witness that the returned parent state is reachable. It is not inserted into `m`.

Again the phase decrease makes the pop strict independently of the child history length.

### Type V — mark-consuming cancellation

Either:

- decrease `a` at fixed order; or
- consume a call-cut step `b` and push a lower-order child in suspended phase.

No external overlap increases `a`.

---

## 5. Conditional corrected stack theorem

### Theorem 5.1 — suspended-pop descent

Suppose every fixed parent context has finite bounds `B,R` and a concrete call-cut/cleanup rank satisfying Section 4. Then every active, push, successful-pop, first-`A/C`-pop and mark-consuming transition strictly decreases the corrected outer-to-inner stack order.

### Proof

- Active transitions decrease one numerical coordinate.
- A push decreases `b` at the parent position before appending the child.
- Either pop changes `suspended` to `active` at the parent position; the arbitrary bounded cleanup rank is later in the key.
- Mark consumption decreases `a` or is a push.

The child prefix is never compared to the parent prefix. ∎

The target-order decrease still bounds the number of simultaneously live lower-order child frames. The suspended phase does not add a new child depth.

---

## 6. Exact remaining rank theorem

The corrected blocker is:

### Target 6.1 — finite call-cut local rank

For every fixed labelled parent context, construct a finite directed local strategy graph with:

1. complete current source, root/token, cap, route and ordered-mark state;
2. no hidden genealogy or history word as state data;
3. accepted root/profile/route/bounded/separator exits;
4. cancellation edges cut only after one concrete parent local step has been consumed;
5. a finite call-cut rank `b` decreasing on every chosen push;
6. a finite active cleanup rank `r` decreasing between calls;
7. returned root or `A/C` atoms reactivated from the suspended state without resetting an earlier coordinate.

`NO_HIDDEN_GENEALOGY_FINITE_STATE_V1.md` gives finiteness of the state alphabet. The new active-diagonal and support-switch source-pop theorems give the missing local physical edges. What is not yet proved is the global acyclic/strategy rank on this finite call-cut graph.

---

## 7. Consequence for current status

### Retained from the PDL stack dossier

- target order drops by at least two in a genuine child call;
- simultaneous child depth is bounded;
- a push may contain arbitrary finite child history once parent progress is stored;
- successful pop to an unchanged stored continuation is strict;
- ordered-incidence marks do not duplicate.

### Corrected

- first `A/C` pop is not proved by `m'_child < m_child` alone;
- child history length is not a parent numerical coordinate;
- a returned atom requires suspended-pop semantics or another explicitly proved ordinal construction.

### Still open

- finite call-cut local rank;
- complete mark-consuming cancellation semantics;
- corrected concrete stack instantiation;
- R2.7, one-cross cap restoration and universal five-CDC.

No assurance, Lean, manuscript, curation, release or publication status changes.
