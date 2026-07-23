# Mobile weld transport has one first `B`-exit and no new defect alphabet

## Research Lead relative first-failure dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `930999dc09d9520876bda389a8273359113312ae`.

**Parents:**

- `WELD_B_ORBIT_SWITCH_AND_MOBILE_MARK_GRAPH_V1.md`;
- `MARKED_WELD_PACHNER_OVERLAP_SCOPE_V1.md`;
- `PACHNER_HISTORY_FIRST_FAILURE_ONE_EDGE_ATOM_V1.md`;
- `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`.

**Status:** exact finite relative first-failure theorem for the coefficient relation needed by inverse weld. Transport two distinguished reconnecting edges through root-valued `2--2` flips by the canonical diagonal lineage and through support-pair switches by their unchanged edge identities. As long as their roots remain distinct intersecting, inverse equal-face insertion is root-valued. At the unique first transition leaving that orbit, the pair becomes equal or disjoint and inverse insertion produces exactly one zero or co-root edge atom. The failing transition has already been crossed, so the residual atom lies on a strictly shorter history prefix. No new coefficient type or multi-edge defect is created.

This theorem does not yet close cancellation re-entry: a global nested-history rank must still show that repeated cancellation, lower-order return and first-`B`-exit cannot reset an equally large parent frame.

---

## 1. Mobile weld state

A **mobile weld state** consists of:

1. two ordered distinguished edge lineages `e,f`;
2. their current roots
   \[
   p,q\in R_5;
   \]
3. the complete source incidence data needed to transport a central edge through a root-valued Pachner flip;
4. the current cap and route data.

It is **weld-admissible** when

\[
\boxed{
p\ne q,
\qquad
|p\cap q|=1.
}
\]

Equivalently `(p,q)` belongs to the `B` orbit.

At a weld-admissible stage, inserting two equal triangles with central root

\[
r=p+q
\]

is root-valued.

---

## 2. Central-flip transition table

Write a weld-admissible state as

\[
p=ab,
\qquad
q=ac,
\]

where `a,b,c` are distinct and let

\[
\{d,e\}=[5]\setminus\{a,b,c\}.
\]

The three roots disjoint from `p=ab` are

\[
cd,
\qquad
ce,
\qquad
de.
\]

Transporting the first marked edge through a central Pachner flip therefore gives:

\[
\begin{array}{c|c}
\text{new first root}&\text{relation to }q=ac\\
\hline
cd&B\\
ce&B\\
de&C.
\end{array}
\]

The unique bad successor is the complement root

\[
\boxed{de=[5]\setminus(p\cup q).}
\]

The symmetric statement holds when the second coordinate moves.

### Theorem 2.1 — exact central-move census

Across all sixty ordered `B` states there are 360 ordered one-coordinate central moves. Their outcomes are:

\[
\boxed{
240\text{ remain in }B,
\qquad
120\text{ enter }C,
\qquad
0\text{ enter }A.
}
\]

For every state the six moves have multiset

\[
\boxed{B,B,B,B,C,C.}
\]

Thus each marked coordinate has exactly one central flip which destroys inverse-weld admissibility.

### Co-root produced at the bad move

If the first coordinate moves from `ab` to `de`, while the second remains `ac`, then

\[
de+ac=Q_b.
\]

The missing support index is the nonshared endpoint `b` of the moved old root. Hence the bad central move produces the standard one-co-root inverse-weld atom, with no new coefficient label.

---

## 3. Support-pair switch table

Let `h` be a support-pair channel for which both `p,q` are eligible. For

\[
p=ab,
\qquad q=ac,
\]

the three common eligible channels are

\[
\boxed{bc,\ ad,\ ae.}
\]

Switching both marked edges or neither preserves `B`.

If only the first marked edge is switched, then:

\[
\begin{array}{c|c}
\text{channel}&p+h\text{ versus }q\\
\hline
bc&A\text{ (equal)}\\
ad&C\text{ (disjoint)}\\
ae&C\text{ (disjoint)}.
\end{array}
\]

The symmetric table holds for switching only the second edge.

### Theorem 3.1 — exact one-sided switch grammar

For each ordered `B` state and each choice of switched side:

\[
\boxed{
1\text{ eligible channel gives }A,
\qquad
2\text{ give }C.
}
\]

Globally, over both switched sides:

\[
\boxed{
120\text{ equal outcomes},
\qquad
240\text{ disjoint outcomes},
\qquad
0\text{ intersecting outcomes}.
}
\]

The equality channel is canonically

\[
\boxed{h=p+q,}
\]

the third root of the current root triangle.

---

## 4. First `B`-exit along a finite history

Let

\[
H_0\longrightarrow H_1\longrightarrow\cdots\longrightarrow H_m
\]

be a finite history whose marked-edge lineages are defined through every step up to the first mark-destroying `2--0` overlap. Allow:

- root-valued `2--2` flips, with a central mark transported to the opposite diagonal;
- support-pair component switches;
- moves disjoint from both marks;
- moves for which both marks are exterior branches.

Start with a weld-admissible mobile state on `H_m` and reverse/transport the history while the pair remains in `B`.

There is a unique maximal index

\[
0\le j\le m
\]

such that the marked pair remains in `B` through

\[
H_m,H_{m-1},\ldots,H_j.
\]

If `j=0`, the weld relation transports through the complete history.

Assume `j>0`. The transition

\[
H_j\longrightarrow H_{j-1}
\]

is the first `B`-exit.

### Theorem 4.1 — relative first-exit atom

At the first `B`-exit, inverse insertion of the equal-face weld on `H_(j-1)` produces exactly one non-root central edge:

\[
\boxed{
0
\quad\text{or}\quad
Q_i.
}
\]

Every other edge remains root-valued and every exterior/cap incidence outside the insertion is unchanged.

More precisely:

1. a one-sided switch by `p+q` gives the zero/quadruple-equality row;
2. any other one-sided eligible switch gives a co-root/doubled-disjoint row;
3. the unique bad central-diagonal successor gives a co-root row;
4. no first exit produces a second persistent defect or a new coefficient type.

### Proof

Before the first exit, all marks and all nonmarked edges are root-valued. Sections 2--3 show that the first failed pair is equal or disjoint. Inserting the two cubic vertices forces their central value to be the sum of the two marked roots. This is respectively zero or one co-root. The insertion changes no other edge. ∎

---

## 5. Strict prefix localisation

The failing transition has already been crossed topologically and coefficient-wise before the inverse weld is attempted. Therefore the residual atom lies on the predecessor stage

\[
H_{j-1}
\]

with only the prefix

\[
H_0\to\cdots\to H_{j-1}
\]

remaining.

### Corollary 5.1 — shorter-history output

A failed relative weld return does not reset the complete history. It returns one ordinary zero/co-root atom with strictly fewer original history steps remaining:

\[
\boxed{j-1<m.}
\]

This is the exact history-length datum absent from a bare statement that cancellation merely returns to target order `N`.

---

## 6. Interaction with local atom normalisation

Once the first `B`-exit atom is created, the existing critical-overlap theorem applies:

- disjoint root surgeries commute;
- zero does not proliferate;
- a good co-root overlap relocates one atom;
- a bad overlap creates only one transient two-co-root tree and normalises back to at most one atom.

Hence the weld-return first failure feeds directly into the established one-token grammar.

No separate “weld defect” alphabet is required.

---

## 7. Why this is not yet the full macro-rank

Corollary 5.1 proves strict decrease relative to the particular finite weld-return history being traversed.

A complete cancellation macro theorem must still control nested behaviour:

1. an order-`N` token movie produces a cancellation;
2. a lower-order contextual call chooses or constructs a finite return history;
3. weld transport succeeds or returns an order-`N` token on a shorter prefix of that lower-order history;
4. consuming that token may itself produce another cancellation and another lower-order frame.

The missing global statement is that the stack of such history frames is well founded. A proof may use:

- a lexicographic stack order with strictly decreasing target orders down the stack and strict prefix shortening on every pop;
- an ordinal rank assigned to the nested return tree;
- or a finite recursive-state game rank.

The present theorem supplies the necessary local strictness on every failed pop.

---

## 8. Remaining local overlap

The only transition type not covered by Theorem 4.1 is a `2--0` move whose support destroys or creates one of the marked lineages before the intended inverse weld.

This requires a separate bounded table distinguishing:

1. marked edge exterior to the equal-face pair;
2. marked edge one reconnecting output of the cancellation;
3. marked edge the central edge of the cancelled pair.

That is the next finite local theorem before a nested macro rank can be claimed.

---

## 9. Trust boundary

### Exact here

- complete central-flip outcome table from a `B` pair;
- unique bad complement flip for each coordinate;
- complete one-sided support-pair switch table;
- canonical equality channel `h=p+q`;
- unique first `B`-exit along a finite marked history;
- zero/co-root localisation at that exit;
- strict remaining-prefix shortening;
- compatibility with the established one-token grammar.

### Not proved

- marked-lineage transport through overlapping `2--0` moves;
- a well-founded nested history-stack rank;
- repaired cancellation macro-return;
- unconditional `MWR` or inverse-weld selection;
- R2 global return, cap restoration, or global five-support closure;
- independent audit, curation, Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.
