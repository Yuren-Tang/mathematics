# The unique bad active weld diagonal has a five-move one-atom source lift

## Research Lead innermost-bubble local theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `CENTRAL_WELD_FLIP_B_PRESERVING_ROOT_LIFT_V1.md`;
- `MARKED_WELD_PACHNER_OVERLAP_SCOPE_V1.md`;
- `WELD_RELATION_FIRST_EXIT_V1.md`.

**Status:** exact source-level lift of the unique central-diagonal `B`-exit. Let the old weld pair `(p,q)` be distinct intersecting, and let a lower-order root flip transport the marked diagonal from `p` to the disjoint root `p'`. If `q` is disjoint from `p'`, then insertion after the flip has one co-root central value. The expanded predecessor-order source before the flip and the one-atom expanded source after the flip are joined by five relative NNIs. The first four source states are fully root-valued; the final two carry exactly one co-root edge. No second defect or new coefficient type appears.

The theorem assumes the second marked edge has endpoints disjoint from the active flip support. Endpoint-identification degenerations remain a separate bounded table.

---

## 1. Standard support coordinates

Write the disjoint old/new flip diagonals as

\[
p=ab,
\qquad
p'=cd,
\]

with fifth support index `e`.

The bad transported weld condition is

\[
q\sim p,
\qquad
q\perp p'.
\]

Up to exchanging `a,b`, write

\[
\boxed{q=ae.}
\]

Choose the four flip branches

\[
\boxed{
A=ac,
\quad
B=bc,
\quad
C=ad,
\quad
D=bd.
}
\]

Then

\[
A+B=C+D=ab=p,
\]

and

\[
A+C=B+D=cd=p'.
\]

At the two endpoints of the second marked edge choose arbitrary ordered root-triangle decompositions

\[
E+F=q,
\qquad
G+H=q.
\]

---

## 2. Before and after expanded topologies

Insertion on the old pair `p,q` gives

\[
\Sigma_0=\{AB,ABEF,CD,EF,GH\},
\]

with internal values

\[
p,\ p+q,\ p,\ q,\ q.
\]

All are roots because `q sim p`.

Insertion after the lower-order flip gives

\[
\Sigma_5=\{AC,ACEF,BD,EF,GH\}.
\]

Its internal values are

\[
p',\ p'+q,\ p',\ q,\ q.
\]

The unique non-root value is

\[
\boxed{
p'+q=cd+ae=Q_b.
}
\]

Thus the target expanded topology has exactly one co-root central edge.

---

## 3. Five-move source movie

Use the same split sequence as the five-move good-central movie:

\[
\begin{aligned}
\Sigma_0&=\{AB,ABEF,CD,EF,GH\},\\
\Sigma_1&=\{ABEF,AEF,CD,EF,GH\},\\
\Sigma_2&=\{AEF,BCD,CD,EF,GH\},\\
\Sigma_3&=\{AEF,BCD,BD,EF,GH\},\\
\Sigma_4&=\{ACEF,AEF,BD,EF,GH\},\\
\Sigma_5&=\{AC,ACEF,BD,EF,GH\}.
\end{aligned}
\]

Consecutive systems differ by one ordinary NNI split.

The changing split values are:

\[
\begin{array}{c|c}
\text{split}&\text{value}\\
\hline
ABEF&p+q\\
AEF&A+q=ac+ae=ce\\
BCD&B+C+D=B+p=A\\
BD&p'\\
ACEF&p'+q=Q_b\\
AC&p'.
\end{array}
\]

Therefore:

- `Sigma_0,Sigma_1,Sigma_2,Sigma_3` are fully root-valued;
- `Sigma_4,Sigma_5` carry exactly one co-root, on the `ACEF` split;
- every other internal edge remains a root.

### Theorem 3.1 — one-atom central-exit movie

The unique bad active-diagonal weld transition has a predecessor-order five-NNI source lift with defect-count sequence

\[
\boxed{0,0,0,0,1,1.}
\]

The co-root is exactly the standard missing-index atom `Q_b` predicted by the coefficient first-exit table.

---

## 4. Complete generic active-diagonal disposition

Combine this theorem with `CENTRAL_WELD_FLIP_B_PRESERVING_ROOT_LIFT_V1.md`.

Let a weld edge be the active diagonal of a lower-order root flip, with the second weld edge disjoint from the flip support.

Exactly one of:

1. the transported pair remains in `B`, and there is a root-valued source movie of length at most six;
2. the transported pair leaves `B`, and there is a five-move source movie with exactly one terminal co-root atom.

There is no generic central-overlap branch requiring two defects or an enlarged source alphabet.

---

## 5. Finite certificate

Normalize

\[
p=12,
\qquad
p'=34.
\]

The bad second roots are

\[
q=15
\quad\text{or}\quad
q=25.
\]

There are four ordered flip-boundary assignments and six ordered decompositions of `q` at each marked-edge endpoint, giving

\[
4\cdot2\cdot6\cdot6=288
\]

support-labelled cases.

For every case all `10,395` labelled eight-leaf trees were enumerated. In the induced graph of topologies carrying at most one zero/co-root internal edge:

\[
\boxed{
288/288\text{ cases have shortest distance }5.
}
\]

Every shortest representative has defect-count sequence

\[
0,0,0,0,1,1.
\]

The structural split proof is controlling; the census is supplementary.

---

## 6. Consequence for innermost bubble compression

For a pure lower-order `2--2` step whose active diagonal is one weld lineage and whose second marked edge is disjoint from the support, the predecessor-order lift is now complete:

\[
\boxed{
B\to B:
\text{root movie};
\qquad
B\to C:
\text{one-atom movie}.}
\]

Together with strict commutation for disjoint and exterior-branch moves, this removes every generic root-flip obstruction to lifting an innermost lower-order history.

Still open:

- the adjacent second-mark overlap;
- support-pair component switches or other flow-changing horizontal moves;
- assembly of successive local lifts into one complete innermost bubble strip;
- nested cancellation bubbles.

---

## 7. Assurance boundary

### Exact here

- standard support normal form;
- five explicit split moves;
- root validity of the first four states;
- exactly one `Q_b` edge in the final two states;
- exhaustive 288-case finite certificate;
- complete generic bad-central source lift.

### Not claimed

- adjacent-mark degenerations;
- complete innermost bubble compression;
- variable-order episode compression;
- R2.7 closure, cap restoration or global five-support closure;
- PDL reconstruction, audit, Lean, manuscript, curation, release or publication.
