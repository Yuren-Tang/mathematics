# Fixed-order call-cut dynamics has a finite attractor rank

## Research Lead local-rank theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `TARGET_TOPOLOGY_ARBORESCENCE_FIXED_ORDER_V1.md`;
- `NO_HIDDEN_GENEALOGY_FINITE_STATE_V1.md`;
- `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md`;
- `OPEN_TRACK_ROOT_STRIP_ENDPOINT_SCOPE_CORRECTION_V1.md` and the retained open-strip theorem;
- `PERIODIC_OUTER_ENDPOINT_ROOT_SEAM_DISCHARGE_V1.md` in its fixed-order scope;
- `WELD_ACTIVE_DIAGONAL_SIX_LEAF_LIFT_V1.md`;
- `WELD_SUPPORT_SWITCH_SOURCE_POP_V1.md`;
- `NESTED_STACK_FIRST_EXIT_SCOPE_CORRECTION_V1.md`.

**Status:** exact construction of the finite local rank required after cutting genuine recursive cancellations at the parent boundary. At fixed labelled order and fixed target context, treat every cancellation only up to the moment at which one concrete parent local step has been consumed; do not execute the lower-order child inside the local graph. Such a cut cancellation is a suspension exit. Every complete fixed-order state reaches either the target root state, an accepted route/profile/bounded/separator exit, or a suspension exit. Since the complete state set is finite, shortest distance to this exit set gives a finite call-cut attractor rank.

The theorem is existential/strategic: at each state choose an edge on a shortest exit path. It does not claim that every arbitrary nondeterministic sequence terminates. It also does not execute or rank the lower-order child; that is the separate stack induction.

---

## 1. Fixed complete context

Fix:

- one labelled vertex order `N`;
- one ordered exterior incidence universe;
- one target topology `T_*`;
- one cap matching, distinguished cap block and physical route convention;
- five literal support labels;
- the finite bounded/category flags used by the established local exits.

A complete active state records:

1. the labelled cubic topology;
2. every root label and, when present, one normalized zero/co-root atom;
3. both crossed resolutions of a co-root atom;
4. support transport, side-root outputs and rooted attachments;
5. ordered weld incidences and any mobile six-port envelope currently required;
6. cap block, route orientation and target data.

History words and edge genealogy are not state coordinates.

By `NO_HIDDEN_GENEALOGY_FINITE_STATE_V1.md`, the active state set

\[
\boxed{\mathcal S_N}
\]

is finite.

---

## 2. The call-cut transition graph

Form a finite directed graph

\[
\mathcal G_N^{\rm cut}
\]

with the following vertices.

### Active vertices

All complete states in `S_N` which have not yet reached an accepted exit.

### Terminal vertices

1. the target root state on `T_*`;
2. cap-compatible root terminals;
3. route/profile exits;
4. bounded direct/theta exits;
5. separator/category exits;
6. **suspension terminals** for genuine equal-face cancellations.

A suspension terminal records:

- the parent continuation after the selected local step has been crossed;
- the four ordered cancellation output incidences;
- the current weld/cap/route data needed to launch the lower-order child;
- no child history.

The lower-order solve is not an edge of `G_N^cut`.

---

## 3. Allowed noncall edges

The graph contains exactly the established source-faithful fixed-order macros required by one chosen strategy.

### Root scheduling

At a fully root-valued state whose topology is not `T_*`, attempt the unique parent edge of `TARGET_TOPOLOGY_ARBORESCENCE_FIXED_ORDER_V1.md`.

The outcome is:

- a root parent move, lowering `d_top` by one;
- one normalized zero/co-root first failure;
- an accepted category/route exit.

### Local zero normalization

Use only the direct root-valued alternatives:

- inverse-flip zero uses the other crossed root NNI;
- inverse-cancellation equality uses the alternative root insertion;
- good doubled-disjoint uses the alternative root insertion.

Persistent zero occurs only as the one ordinary atom inside a bounded first-failure macro.

### Co-root transport

Use the full-labelled one-token grammar:

- constant-pivot root sections;
- normalized immediate-backtrack deletion;
- forced pivot-change cells;
- prescribed support-switch rescue/exchange macros;
- the active-diagonal six-leaf lift;
- bounded critical-overlap normalization.

### Cancellation cut

When the chosen local macro exposes a genuine equal-face cancellation, perform the concrete parent-side step through the cancellation boundary and stop at its suspension terminal. No lower-order state is inserted into `G_N^cut`.

Thus every edge of the call-cut graph is fixed-order, except that a cancellation edge terminates before order changes.

---

## 4. Root states cannot trap

Let `x` be fully root-valued.

- If its topology is `T_*`, it is terminal.
- Otherwise attempt the arborescence parent edge.

Every root-success edge strictly lowers the nonnegative integer

\[
d_{\rm top}.
\]

Hence a sequence of root-success states reaches `T_*` after finitely many steps unless it first enters a normalized singular state or an accepted exit.

### Lemma 4.1

Every root state reaches the terminal set or a singular state.

No free support-switch loop is part of the strategy: support switches are used only inside a prescribed singular rescue/exchange macro.

---

## 5. Singular states cannot form a call-free trap

Let `x` carry one normalized co-root atom. Follow the established full-channel continuation strategy, stopping immediately at:

- rootification;
- route/profile escape;
- bounded/separator exit;
- suspension at a genuine cancellation.

Assume for contradiction that no such outcome is reachable.

Because `S_N` is finite, an infinite call-free continuation repeats one complete state. Choose a finite repeated-state segment with minimal complete singular complexity.

All transitions in this segment are fixed-order. Therefore its contextual lift is a legitimate fixed-order history diagram; no lower-order child is hidden inside it.

### Internal closed component

`PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md` removes it while preserving the complete labelled boundary and strictly lowering singular complexity.

### Open component with normalized/accepted short sides

The retained open-strip theorem replaces it by a root-valued rectangle and lowers the number of singular edges.

### Outer unresolved endpoint recurrence

The repeated complete endpoint collars form a fixed-order history cylinder. `PERIODIC_OUTER_ENDPOINT_ROOT_SEAM_DISCHARGE_V1.md` replaces the episode by a root-valued rectangle and removes the two unresolved endpoint occurrences.

In every possible recurrent case, the alleged minimal call-free segment has a source-faithful replacement with smaller singular/boundary complexity. Iterating leaves a fully root-valued segment.

The root segment is then consumed by the arborescence strategy of Section 4, contradicting the assumption that the recurrent set has no route to the terminal set.

### Theorem 5.1 — no call-free singular sink

Every singular state reaches, by a finite fixed-order source history, one of:

\[
\boxed{
\text{root state},
\quad
\text{accepted exit},
\quad
\text{suspension terminal}.
}
\]

The theorem uses the periodic result only in the present fixed-order call-free scope. It does not compress a variable-order child episode.

---

## 6. Reachability of the terminal set

Combine Lemma 4.1 and Theorem 5.1.

### Theorem 6.1 — call-cut attractor

Every vertex of `G_N^cut` reaches the terminal set

\[
\mathcal X_N
\]

consisting of target/root/accepted/suspension terminals.

### Proof

From a root vertex, Section 4 reaches a terminal or singular vertex. From a singular vertex, Section 5 reaches a root vertex, accepted exit or suspension. Repeating this alternative in the finite graph cannot avoid the terminal set: any nonterminal recurrent strongly connected component would contain a call-free root/singular recurrence excluded by Sections 4--5. ∎

---

## 7. Shortest-distance rank

For every active state `x`, define

\[
\boxed{
b_N(x)=\operatorname{dist}_{\mathcal G_N^{\rm cut}}(x,\mathcal X_N),}
\]

where distance is directed shortest-path length.

Theorem 6.1 makes this a finite nonnegative integer.

Choose at every active state one outgoing edge lying on a shortest path to `X_N`. Then

\[
\boxed{b_N(x')=b_N(x)-1}
\]

for the chosen successor `x'`.

Since `S_N` is finite, there is a uniform bound

\[
B_N=\max_{x\in\mathcal S_N} b_N(x)<\infty.
\]

### Theorem 7.1 — finite call-cut local rank

The function `b_N` is the finite call-cut rank required by `NESTED_STACK_FIRST_EXIT_SCOPE_CORRECTION_V1.md`.

Every chosen cancellation push reaches a suspension terminal only after one strict rank step has been consumed. Every chosen noncall transition also strictly lowers `b_N` until a terminal is reached.

---

## 8. Interaction with child pops

At a suspension terminal, launch the lower-order child under the separate target-order induction/stack mechanism.

After the child finishes, source-level pop is supplied by:

- ordinary root inverse insertion;
- alternative equality/good-disjoint insertion;
- `WELD_ACTIVE_DIAGONAL_SIX_LEAF_LIFT_V1.md`;
- `WELD_SUPPORT_SWITCH_SOURCE_POP_V1.md`;
- ordered-incidence `2--0` overlap semantics.

The returned parent state is one element of the same finite state set `S_N`. Its rank may be any value at most `B_N`; it is not compared with the child history length.

Use the suspended-return phase of `NESTED_STACK_FIRST_EXIT_SCOPE_CORRECTION_V1.md`:

\[
\mathrm{suspended}\to\mathrm{active}.
\]

This phase decrease permits reinitialization of `b_N` after either a successful or first-`A/C` pop without resetting an earlier frame coordinate.

---

## 9. What this theorem does and does not solve

### Closed here

- finite fixed-order complete state alphabet;
- target-directed exclusion of pure-root loops;
- elimination of call-free singular recurrent components;
- reachability of root/accepted/suspension terminals;
- finite shortest-distance call-cut rank;
- strict rank consumption before every chosen cancellation push;
- compatibility with suspended successful and `A/C` pops.

### Still required

1. a complete source theorem for central-mark-consuming `2--0` transitions and their reactivation after the lower child returns;
2. assembly of the corrected stack key with the rank `b_N` at every target order;
3. PDL reconstruction and independent audit of all imported fixed-order track theorems;
4. downstream R2.7, cap restoration and five-CDC consequences.

### Not claimed

- termination of every arbitrary nondeterministic scheduler;
- variable-order episode compression into one fixed-order cylinder;
- completed R2.7 or universal five-CDC;
- Lean verification, manuscript integration, curation, release or publication.
