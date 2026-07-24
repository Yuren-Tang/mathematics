# AC-PD-5CDC v7.3 — zero prescribed-parent reinsertion obstruction

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Frozen Research Lead input:** `research/affine-cdc-five-cdc-v1@212d789a5967813e7277fb3e269060926c99cb0e`  
**Classification:** `BLOCKED-PROOF / SMALLEST ROW NOT COVERED BY THE FIXED-CHANNEL XI THEOREM`.

The v7.3 fixed-channel theorem correctly closes the live co-root/DDD
prescribed-parent sector.  The complete inverse root-NNI table, however, also
contains a zero prescribed-parent row.  No controlling frozen theorem supplies
a pure-NNI return from that row to the literal parent topology or to an exact
terminal.

This is not the quadruple-equality row of an inverse cancellation.  The latter
is already removed by the five-leaf borrowing theorem.  The obstruction below
arises when reversing one stored root-valued `2--2` NNI.

---

## 1. Exact zero-parent fibre

Let `a,b` be distinct intersecting roots and expose the ordered four-root word

\[
(A,B,C,D)=(a,a,b,b).
\]

The three binary pairings have central values

\[
\begin{array}{c|c}
AB\mid CD&0,\\
AC\mid BD&a+b,\\
AD\mid BC&a+b.
\end{array}
\]

Since `a+b` is a root, the exact pattern is

\[
\boxed{(0,2,2).}
\]

Take the prescribed parent to be

\[
P=AB\mid CD.
\]

The two crossed labelled topologies

\[
R_0=AC\mid BD,
\qquad
R_1=AD\mid BC
\]

are fully root-valued and are exchanged by one ordinary root NNI.  The parent
central value remains zero as long as the ordered exterior word is fixed.
Thus:

- `R_0 -> P` fails and exposes `R_1`;
- `R_1 -> P` fails and exposes `R_0`;
- the prescribed topology has no root flow with the fixed exterior word.

This is a zero analogue of the earlier crossed-state co-root cycle, but it is
not a co-root state and carries no DDD frame.

A concrete normal form is

\[
(A,B,C,D)=(13,13,23,23),
\]

with crossed central root `12` and parent central value zero.

---

## 2. Why existing zero theorems do not close this interface

### 2.1 Inverse-cancellation quadruple equality

`QUADRUPLE_EQUALITY_THREE_VERTEX_BORROWING_ROOTIFICATION_V1.md` treats a
zero edge whose **both** endpoints are `(0,a,a)`.  It borrows a third root
vertex and replaces that inverse-cancellation atom by a neighbouring
root-valued five-leaf topology.

In the present inverse-NNI row the hypothetical parent zero edge has endpoints

\[
(0,a,a)
\qquad\text{and}\qquad
(0,b,b),
\]

with `a != b`.  The five-leaf quadruple-equality theorem does not apply.

### 2.2 “Use the other crossed root NNI”

The other crossed NNI removes the zero coefficient from the **current root
state**, but it does not realize the stored predecessor topology.  It merely
moves from `R_0` to `R_1` while leaving the parent obligation live.  Repeating
the same instruction returns to `R_0`.

Therefore the phrase “zero normalization remains root-NNI/local” proves local
root-valuedness, not target success.

### 2.3 Equality current-flow potential

`EQUALITY_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md` gives a well-founded forward
surgery measure using root NNIs and equal-face `2--0` cancellation.  Its own
scope leaves inverse transfer open.  V7.2/v7.3 fixed-order return explicitly
forbids reopening cancellation.  That potential is therefore not a pure-NNI
prescribed-parent theorem for the row above.

### 2.4 Fixed-channel `Xi`

The `Xi` frame assumes two marked disjoint roots with sum `Q_m`, an unused
support index, and a rescue root meeting both.  Here the live parent value is
zero and the two equal pairs are formed from distinct intersecting roots.
There is no canonical DDD datum

\[
(p,q,m,h_*).
\]

Consequently neither the `H_14` frame nor the bad-free `12--34` route
contradiction applies.

---

## 3. Complete graph-category witness

The zero fibre is not forced into a loop, parallel edge or cyclic cut merely by
its local topology.  Use the labelled Heawood graph on vertices `1,...,14` with
edges

\[
\begin{aligned}
\{&12,16,1\,14,23,2\,11,34,38,45,4\,13,56,5\,10,67,\\
  &78,7\,12,89,9\,10,9\,14,10\,11,11\,12,12\,13,13\,14\}.
\end{aligned}
\]

Use the root flow

\[
\begin{array}{c|c@{\qquad}c|c@{\qquad}c|c}
12&23&16&12&1\,14&13\\
23&34&2\,11&24&34&13\\
38&14&45&12&4\,13&23\\
56&13&5\,10&23&67&23\\
78&24&7\,12&34&89&12\\
9\,10&13&9\,14&23&10\,11&12\\
11\,12&14&12\,13&13&13\,14&12.
\end{array}
\]

Vertices `4` and `5` both carry triangle `123` and are joined by root `12`.
The four exterior branches of the edge `4-5` are

\[
3\!-\!4:13,\quad4\!-\!13:23,\quad5\!-\!6:13,\quad5\!-\!10:23.
\]

The three labelled local topologies are:

1. current root topology
   \[
   (3,13)\mid(6,10);
   \]
2. other crossed root topology
   \[
   (3,10)\mid(13,6);
   \]
3. prescribed zero topology
   \[
   (3,6)\mid(13,10).
   \]

The first two retain central root `12`; the third forces central value zero.
The active cell is disjoint from the retained cap block on vertices `7,12`, so
all cap vertices and cap darts survive literally.

An independent exhaustive labelled subset check gives, for all three
uncoloured topologies:

- connected;
- simple and loopless;
- bridgeless, with edge connectivity three;
- no cyclic edge cut of size at most four.

Thus the zero parent is not automatically consumed by the graph-category
ledger.  This is not yet a counterexample to a universal route theorem: a
support-component or route move may still escape.  It is a complete
category-safe witness showing that such an escape requires an additional
source theorem and cannot be inferred from local category failure.

---

## 4. Missing theorem

Call the missing implication

\[
\boxed{
\texttt{FC-PURE-NNI-ZERO-PARENT-ESCAPE}.}
\]

Given a complete fixed-order state in which:

1. the live prescribed parent has forced central value zero;
2. the two crossed labelled topologies are root-valued;
3. all graph-category tests have passed and no named terminal is present;
4. cap, route, support-component and prefix identities are retained;

construct a finite source-faithful same-order history using no cancellation and
no lower-order call which ends in:

- a root flow on the literal parent topology;
- a cap-compatible route/profile state;
- a named cyclic `2/3/4`-cut or bounded terminal.

A sufficient proof could be:

1. a fixed-channel equality/support-switch rank;
2. an exact theorem that every complete `(0,2,2)` state has a separating
   boundary-changing component;
3. an ambient root-NNI descent with a strict complete-state measure;
4. a proof that a full zero-parent lock forces a named terminal.

The frozen v7.3 source contains none of these statements.

---

## 5. Effect on the v7.3 claim

The repaired inverse-parent table is currently:

\[
\begin{array}{c|c}
\text{forced parent value}&\text{PDL status}\\
\hline
\text{root}&\text{direct success}\\
\text{co-root}&\text{closed by the fixed-channel Xi theorem}\\
0&\texttt{FC-PURE-NNI-ZERO-PARENT-ESCAPE open}.
\end{array}
\]

Therefore:

- the old `(4,2,2)` obstruction is genuinely repaired;
- pure-NNI return through **every** stored prefix is not yet reconstructed;
- the terminal census is not yet exhaustive for all fixed-order executions;
- ordinary strong induction remains conditional;
- no cubic five-support or universal five-CDC theorem follows at PDL level.

This is a proof-source obstruction, not a graph counterexample to five-CDC.
