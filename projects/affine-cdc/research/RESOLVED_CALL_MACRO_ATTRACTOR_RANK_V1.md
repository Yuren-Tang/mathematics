# Resolved child calls give a finite parent macro attractor rank

## Research Lead recursive rank theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Supersedes as controlling rank architecture:**

- the uncorrected Type-IV use of `AC_PD_5CDC_EQ_RETURN_5_NESTED_STACK_ORDER.md`;
- suspended-phase bookkeeping as a necessary global proof device.

**Parents:**

- `FINITE_CALL_CUT_LOCAL_ATTRACTOR_RANK_V1.md`;
- `VARIABLE_ORDER_RECURRENT_EPISODE_COMPRESSION_V2.md` v2.1;
- `WELD_ACTIVE_DIAGONAL_SIX_LEAF_LIFT_V1.md`;
- `WELD_SUPPORT_SWITCH_SOURCE_POP_V1.md`;
- `WELD_CENTRAL_MARK_CANCELLATION_POP_V1.md`;
- `NO_HIDDEN_GENEALOGY_FINITE_STATE_V1.md`;
- fixed-order closed/open/periodic/arborescence theorems.

**Status:** exact recursive construction of a finite parent-order strategy rank. Assume all lower target orders have already been solved. Replace each parent cancellation together with its complete lower-order solve and inverse return by one finite **resolved-call macro edge**. The parent complete state graph is finite. A nonexit sink component would contain a cycle; expanding its call edges gives a finite variable-order recurrent episode, which compresses by innermost-call elimination to a fixed-order recurrence and is then removed by the established track/arborescence theorems. Hence every parent state reaches an exit. Directed shortest distance to the exit set gives a finite rank `d_N`. Induction on target order executes every resolved-call edge, and `d_N` decreases after the edge completes.

This theorem avoids the invalid comparison of a child prefix with a stored parent prefix. It is an existence/strategy theorem, not termination of arbitrary nondeterministic schedules.

---

## 1. Induction statement

For every nonnegative target order `N`, let `P(N)` be:

> For every fixed literal labelled context of order `N` and every complete root/token/cap/route/mark state in that context, there is a finite source-faithful strategy reaching a target root state or an accepted route/profile/bounded/separator outcome. Every recursive cancellation call is completed at strictly smaller target order and returns by one of the established source-pop theorems.

The induction is on `N`.

At orders below the finite cubic base range, `P(N)` is given by the accepted direct/theta/bounded tables.

Assume `P(M)` for every

\[
M<N.
\]

We prove `P(N)`.

---

## 2. Finite parent state set

Fix one order-`N` context:

- labelled vertex/dart universe;
- target topology;
- literal support names;
- cap block and route convention;
- ordered active marks;
- bounded/category flags.

Let

\[
\mathcal S_N
\]

be the complete parent active state set.

By `NO_HIDDEN_GENEALOGY_FINITE_STATE_V1.md`,

\[
\boxed{|\mathcal S_N|<\infty.}
\]

No child history word is a parent state coordinate.

---

## 3. Resolved-call macro edges

Build a finite directed parent graph

\[
\mathcal M_N
\]

on `S_N` plus accepted terminal vertices.

### Fixed-order edges

Include the chosen source-faithful fixed-order macros:

- target-arborescence parent moves;
- direct zero/equality/good-disjoint alternatives;
- one-token critical-overlap and full-channel moves;
- active-diagonal six-leaf lifts;
- support-switch rescue/exchange moves;
- fixed-order closed/open/periodic replacements;
- accepted exits.

### Resolved cancellation edge

Suppose the parent strategy selects a genuine equal-face cancellation.

1. Cross the concrete parent-side cancellation step and retain its ordered output boundary.
2. Launch the lower-order child at order at most `N-2`.
3. By the induction hypothesis `P(N-2)`, execute a finite child strategy to a return/exit state.
4. Transport the weld boundary through the finite child history using:
   - strict exterior commutation;
   - active-diagonal six-leaf lift;
   - support-switch source pop;
   - ordered `2--0` incidence semantics.
5. Apply the complete inverse-return table:
   - original root insertion;
   - equality/good-disjoint alternative insertion;
   - missing-index one-atom return;
   - central-mark-consuming return;
   - accepted child/category exit.
6. Record the resulting order-`N` parent state or accepted exit as the endpoint of one macro edge.

Every resolved-call edge has a finite nested source witness by the induction hypothesis.

### Finiteness

The source and target parent states belong to finite `S_N`, and the chosen lower-order strategy selects one finite outcome. Therefore `M_N` is finite even though the expanded witness of one edge may be long.

---

## 4. No nonexit sink component

Assume a reachable sink strongly connected component

\[
K\subseteq\mathcal M_N
\]

contains no accepted terminal.

Choose a directed cycle in `K` and expand every resolved-call macro edge into its finite nested source witness. The result is a finite variable-order episode whose two outer endpoint states are literally equal.

Apply `VARIABLE_ORDER_RECURRENT_EPISODE_COMPRESSION_V2.md` v2.1. It removes all order-changing calls by induction on their finite number and gives a fixed-order physical recurrence with the same complete outer boundary.

The fixed-order recurrence has the established exhaustive disposition:

1. pure root segment: target arborescence gives strict `d_top` progress;
2. internal closed singular component: root-annulus/closed-track erasure;
3. normalized-endpoint open component: root-strip replacement;
4. unresolved outer endpoint recurrence: periodic root-seam discharge;
5. route/profile/bounded/separator event: accepted terminal.

Every nonterminal case supplies a source-faithful replacement leaving the alleged sink component or strictly lowering the recurrence complexity. Hence a minimal nonexit cycle cannot exist.

### Theorem 4.1 — no nonexit macro SCC

Every reachable sink strongly connected component of `M_N` contains an accepted target/exit vertex.

---

## 5. Parent attractor rank

Let

\[
\mathcal X_N
\]

be the terminal set of `M_N`.

Theorem 4.1 implies every reachable parent state has a directed path to `X_N`.

Define

\[
\boxed{
d_N(x)=\operatorname{dist}_{\mathcal M_N}(x,\mathcal X_N).}
\]

Because `M_N` is finite, `d_N(x)` is a finite nonnegative integer.

At every nonterminal state choose one outgoing macro edge on a shortest path. If its endpoint is `y`, then

\[
\boxed{d_N(y)=d_N(x)-1.}
\]

### Theorem 5.1 — finite resolved-call rank

The rank `d_N` strictly decreases after every chosen parent macro, including a completed cancellation/child/return macro.

No comparison with the child history length is made.

---

## 6. Execution of one macro

### Fixed-order macro

Execute its finite local source movie. The endpoint rank drops by one.

### Resolved-call macro

Execute the lower-order child witness. Every live child call has target order below `N`, so it terminates by the induction hypothesis. Apply the source-pop table and return to the recorded parent endpoint. Then `d_N` drops by one.

Thus the expanded execution of one macro is finite, even though the numerical rank is measured only at parent macro boundaries.

---

## 7. Completion of the induction

### Theorem 7.1 — recursive macro termination

`P(N)` holds for every target order `N`.

### Proof

Induct on `N`.

At order `N`, use the finite rank `d_N`.

- If `d_N=0`, the state is terminal.
- If `d_N>0`, execute the chosen macro edge.
  - Fixed-order execution is finite directly.
  - A resolved-call execution is finite by the induction hypothesis at lower order.

The macro endpoint has rank `d_N-1`. Induct on this finite integer.

Therefore the strategy reaches `d_N=0` after finitely many parent macros. ∎

Equivalently, the proof is lexicographic induction on

\[
\boxed{(N,d_N).}
\]

---

## 8. Why the old Type-IV comparison is unnecessary

The old attempted stack proof wanted to infer

\[
m'_{\rm child}<m_{\rm child}
\Longrightarrow
m'_{\rm parent}<m_{\rm parent}.
\]

The implication is not meaningful without an embedding theorem.

The resolved-call proof does not perform it.

- The child history belongs entirely to the finite witness of one parent macro edge.
- Its termination is justified by lower target order.
- Its returned root/atom state is the endpoint of that macro.
- Parent progress is measured by `d_N`, which decreases after the complete macro.

Thus arbitrary child history length and child-prefix data never enter the parent numerical key.

---

## 9. Relation to call-cut rank

`FINITE_CALL_CUT_LOCAL_ATTRACTOR_RANK_V1.md` remains useful for constructing and understanding parent-side strategy before a call.

The controlling global rank is now the resolved macro distance `d_N`, because it includes the actual lower-order return relation supplied by induction. Variable-order cycle compression proves that the resolved graph has no neutral nonexit SCC.

Suspended-phase bookkeeping may still be used operationally by an implementation, but it is not needed in the mathematical well-foundedness proof.

---

## 10. Assurance boundary

### Exact here

- recursive definition of finite resolved-call parent graph;
- finite witness for every child macro by lower-order induction;
- exclusion of nonexit parent SCCs by variable-order episode compression;
- finite shortest-distance parent rank;
- lexicographic `(N,d_N)` termination;
- elimination of the child/parent prefix-coordinate mismatch.

### Imported authorial mathematics

- finite complete state semantics;
- all local source-pop tables;
- innermost-call episode compression;
- fixed-order closed/open/periodic/arborescence disposition.

### Not yet claimed

- PDL reconstruction or independent audit;
- final R2.7 master assembly;
- one-cross cap restoration or universal five-CDC acceptance;
- Lean verification, manuscript integration, curation, release or publication.
