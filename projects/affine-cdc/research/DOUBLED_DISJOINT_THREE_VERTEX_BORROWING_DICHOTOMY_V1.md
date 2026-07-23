# Doubled-disjoint inverse cancellation has one borrowing dichotomy

## Research Lead local classification v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parents:**

- `PACHNER_HISTORY_FIRST_FAILURE_ONE_EDGE_ATOM_V1.md`;
- `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`;
- `FULL_DEFECT_TREE_NNI_DESCENT_V1.md`;
- `DOUBLED_DISJOINT` / Type-T one-edge grammar;
- `QUADRUPLE_EQUALITY_THREE_VERTEX_BORROWING_ROOTIFICATION_V1.md`.

**Status:** exact local classification of the inverse-cancellation row with two disjoint reconnecting roots. The local four-root fibre `(a,a,b,b)` with `a perpendicular b` has pairing-sum pattern `(0,4,4)` and no direct root NNI. Borrowing one adjacent root vertex gives a five-leaf problem. In two thirds of the support cases, the same two-step pentagon movie reaches the unique root topology. In the remaining one third, the borrowed triangle uses the missing support index of the co-root; the first move creates exactly one adjacent two-co-root transport state, already covered by the full-defect-tree/forced-backbone grammar. No new coefficient state or recursive equality problem occurs.

---

## 1. The doubled-disjoint atom

Let the failed inverse cancellation restore a central edge

\[
c=uv
\]

with co-root value

\[
Q=a+b,
\]

where

\[
a,b\in R_5,
\qquad
a\cap b=\varnothing.
\]

At both endpoints the other two incident roots are `a,b`:

\[
(Q,a,b)
\qquad\text{and}\qquad
(Q,a,b).
\]

The four exterior branch multiset is

\[
(a,a,b,b).
\]

Its three pairing sums have weights

\[
\boxed{(0,4,4).}
\]

Hence the two-vertex atom has no root-valued NNI topology.

---

## 2. Borrow one adjacent `a`-vertex

Choose one `a`-edge at one endpoint and let its other endpoint be a root-valued vertex with remaining roots

\[
d,e,
\]

so that

\[
\boxed{a=d+e.}
\]

Take the three-vertex region consisting of:

- the second co-root endpoint as a cherry with branches `a,b`;
- the first co-root endpoint as the central singleton branch `b`;
- the borrowed root vertex as a cherry with branches `d,e`.

Use the five-leaf notation

\[
A=b,
\quad B=a,
\quad C=b,
\quad D=d,
\quad E=e.
\]

The initial topology is

\[
T_0=BC\mid A\mid DE.
\]

Its internal values are

\[
B+C=a+b=Q,
\]

and

\[
D+E=a.
\]

Thus `T_0` has exactly one co-root internal edge.

---

## 3. Support normal form

By support permutation normalize

\[
a=12,
\qquad
b=34,
\qquad
Q=Q_5=1234.
\]

Every root decomposition of `a` has the form

\[
d=1k,
\qquad
e=2k,
\]

where

\[
k\in\{3,4,5\}.
\]

There are two cases.

### Good borrowing

\[
k\in b=\{3,4\}.
\]

Then both `d,e` meet `b` in one support.

### Missing-index borrowing

\[
k=5.
\]

Then `d,e` both contain the missing index of `Q` and are disjoint from `b`.

This dichotomy is support-invariant.

---

## 4. Good borrowing rootifies in two moves

Use the same pentagon path

\[
T_0\longrightarrow T_4\longrightarrow T_3,
\]

where

\[
T_4=AE\mid D\mid BC,
\qquad
T_3=AE\mid C\mid BD.
\]

In the good case:

\[
A+E=b+e\in R_5,
\]

because `b,e` are distinct intersecting roots.

Also

\[
B+D=a+d=e\in R_5.
\]

Therefore `T_3` has internal roots

\[
b+e,
\qquad e,
\]

and central singleton `b`; these form one root triangle.

### Theorem 4.1 — good doubled-disjoint borrowing

If the borrowed adjacent triangle avoids the missing-index case, the two-step five-leaf movie replaces the doubled-disjoint co-root atom by a fully root-valued topology preserving all exterior incidences.

As in the quadruple-equality theorem, the final connected root-valued graph is automatically bridgeless.

---

## 5. Missing-index borrowing gives the standard transport state

Assume

\[
k=5.
\]

Then

\[
d=15,
\qquad e=25.
\]

At the intermediate topology `T_4`, the two internal non-root values are:

\[
B+C=12+34=Q_5,
\]

and

\[
A+E=34+25=Q_1.
\]

The central singleton is

\[
D=15.
\]

Hence the middle vertex carries exactly

\[
\boxed{(Q_1,Q_5,15).}
\]

This is the established degree-two co-root transport state

\[
(Q_i,Q_j,ij).
\]

The defect support is one three-vertex full-defect tree with two adjacent co-root edges. The full-defect-tree NNI theorem reduces it immediately to at most one co-root atom or an accepted separator/bounded exit.

### Theorem 5.1 — bad borrowing is not a new obstruction

The missing-index case does not rootify inside the same five-leaf topology sector. It produces exactly one standard co-root transport unit and no other defect.

After normalization, the doubled-disjoint atom has become one ordinary forced-backbone co-root state.

---

## 6. Exact finite certificate

Enumerate all ordered data

\[
(b,a,b,d,e)
\]

with

\[
a=d+e,
\qquad a\perp b.
\]

There are

\[
\boxed{180}
\]

ordered cases.

For the five pentagon topologies the complete validity census is:

\[
\boxed{
120\text{ cases with }(0,0,0,1,0),
}
\]

and

\[
\boxed{
60\text{ cases with }(0,0,0,0,0).
}
\]

The first `120` are exactly the two good common-index choices. The last `60` are exactly the unique missing-index choice.

No exceptional pattern occurs.

---

## 7. Unified inverse-cancellation table

The inverse equal-face cancellation rows now have the following exact same-order dispositions.

\[
\begin{array}{c|c}
\text{relation of reconnecting roots }a,b&\text{disposition}\\
\hline
\text{distinct intersecting}&\text{direct root insertion}\\
a=b&\text{quadruple-equality two-NNI rootification}\\
a\perp b&\text{good two-NNI rootification or one normalized co-root transport atom}.
\end{array}
\]

There is no lower-order recursive row.

---

## 8. Correction to root-normalized transfer v4

In `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V4.md`, the co-root inverse-cancellation row must not be read as an immediate crossed root resolution of the original two-vertex atom.

The correct sequence is:

1. identify the `(0,4,4)` doubled-disjoint fibre;
2. borrow one adjacent root triangle;
3. if the common index meets the opposite root, rootify in two NNIs;
4. if it is the missing index, normalize the resulting two-co-root three-vertex tree to one forced-backbone atom;
5. consume any closed recurrence by the full-state track and root-annulus theorems.

---

## 9. Assurance boundary

### Exact here

- the five-leaf model of a doubled-disjoint atom plus one borrowed root vertex;
- the support normal form and `2/3` versus `1/3` dichotomy;
- the good two-NNI rootification;
- the exact missing-index transport state `(Q_i,Q_j,ij)`;
- reduction to the existing one-token forced-backbone grammar;
- the `180=120+60` finite certificate;
- elimination of doubled-disjoint inverse cancellation as a recursive branch.

### Not proved here

- global termination of an open forced-backbone track;
- complete repaired contextual transfer;
- cap restoration or global five-support closure;
- PDL reconstruction, independent audit, Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.
