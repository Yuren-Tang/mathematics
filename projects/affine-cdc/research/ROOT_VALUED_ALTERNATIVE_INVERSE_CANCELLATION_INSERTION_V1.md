# Zero and good doubled-disjoint rows admit root-valued alternative inverse insertions

## Research Lead source realisation theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parents:**

- `QUADRUPLE_EQUALITY_THREE_VERTEX_BORROWING_ROOTIFICATION_V1.md`;
- `DOUBLED_DISJOINT_THREE_VERTEX_BORROWING_DICHOTOMY_V1.md`;
- the equal-face cancellation dictionary.

**Status:** exact strengthening of the two borrowing theorems. In the quadruple-equality row and the good doubled-disjoint row, the final root-valued five-leaf topology contains an equal-face pair whose cancellation is exactly the current smaller root-valued source topology. Therefore one need not traverse the displayed singular intermediate topologies. The repair can be performed directly as an alternative root-valued inverse `2--0` insertion on the current smaller graph. Zero never appears as a state or as an endpoint of the global discrepancy track.

---

## 1. Current smaller topology after one cancellation

Let an equal-face pair be cancelled in the forward history. On the smaller graph, the cancellation reconnects two equal-labelled incidence pairs into two root-valued edges.

To reverse the cancellation under an arbitrary returned root flow, the original insertion may fail. The borrowing theorems enlarge the local region by one adjacent root vertex and exhibit a root-valued five-leaf topology

\[
T_3=AE\mid C\mid BD.
\]

The key question is whether `T_3` is merely reachable through singular moves, or is itself a legal alternative inverse insertion of one equal-face pair into the current smaller topology.

---

## 2. Quadruple equality

Use the boundary

\[
A=B=C=a,
\qquad
D=d,
\qquad
E=e,
\qquad
a=d+e.
\]

In

\[
T_3=AE\mid C\mid BD,
\]

the two internal edge values are

\[
A+E=a+e=d,
\]

and

\[
B+D=a+d=e.
\]

The three internal vertices carry the root triangles:

\[
\begin{aligned}
L&=(a,e,d),\\
M&=(d,a,e),\\
R&=(a,d,e).
\end{aligned}
\]

Thus all three vertices have the same unordered support triangle

\[
\boxed{\{a,d,e\}.}
\]

In particular, `L` and `M` form an equal-face pair joined along `d`.

Cancel `L,M`. Their remaining incidence labels are:

- at `L`: `A=a` and `E=e`;
- at `M`: `C=a` and the edge of value `e` leading to `R`.

The cancellation reconnects:

\[
A\longleftrightarrow C
\]

as one direct `a`-edge, and

\[
E\longleftrightarrow R
\]

as the `e`-edge of the borrowed root vertex. The remaining vertex `R` has exterior roots

\[
B=a,
\qquad D=d,
\qquad E=e,
\]

and is exactly the borrowed current vertex `(a,d,e)`.

Therefore the cancelled output is precisely the smaller source neighbourhood which existed before attempting the failed inverse cancellation: one direct `a`-edge plus the adjacent root vertex `(a,d,e)`.

### Theorem 2.1 — direct alternative insertion for quadruple equality

The root-valued topology `T_3` is obtained from the current smaller root graph by one legal root-valued inverse equal-face insertion.

No zero edge or singular intermediate topology is needed.

---

## 3. Good doubled-disjoint row

Let

\[
a\perp b,
\qquad a=d+e,
\]

and use the five-leaf boundary

\[
A=b,
\quad B=a,
\quad C=b,
\quad D=d,
\quad E=e.
\]

Assume the good borrowing condition, so

\[
b+e\in R_5.
\]

In

\[
T_3=AE\mid C\mid BD,
\]

the internal values are

\[
x=A+E=b+e,
\]

and

\[
y=B+D=a+d=e.
\]

The three internal triangles are:

\[
\begin{aligned}
L&=(b,e,b+e),\\
M&=(b+e,b,e),\\
R&=(a,d,e).
\end{aligned}
\]

Thus `L,M` are one equal-face pair joined along `b+e`.

Cancel `L,M`. Their remaining equal labels reconnect:

\[
A=b\longleftrightarrow C=b
\]

as one direct `b`-edge, and

\[
E=e\longleftrightarrow y=e
\]

as the `e`-edge of the borrowed root vertex `R=(a,d,e)`.

The output is exactly the current smaller neighbourhood before inverse insertion: one direct `b`-edge and one adjacent root vertex `(a,d,e)`.

### Theorem 3.1 — direct alternative insertion for the good disjoint row

Every good doubled-disjoint borrowing repair is a single root-valued alternative inverse equal-face insertion on the current smaller graph.

The original co-root insertion is bypassed without ever creating a co-root state.

---

## 4. Unified source interpretation

For the inverse-cancellation rows:

### Root-success row

The original equal-face pair inserts root-valuedly.

### Equality row

A neighbouring placement of an equal-face pair inserts root-valuedly by Theorem 2.1.

### Good doubled-disjoint row

A neighbouring placement of an equal-face pair inserts root-valuedly by Theorem 3.1.

### Missing-index doubled-disjoint row

No root-valued five-leaf topology exists. The local comparison necessarily enters the standard two-co-root transport state and then the forced-backbone grammar.

Hence:

### Theorem 4.1 — alternative-insertion trichotomy

Every inverse cancellation has one of:

1. the original root-valued insertion;
2. a root-valued alternative insertion after borrowing one adjacent root vertex;
3. the unique missing-index co-root transport branch;
4. a bounded loop/parallel or separator exit.

The first three coefficient rows of the ordinary cancellation table do not create a persistent zero atom. Only the missing-index disjoint branch contributes to the global co-root discrepancy track.

---

## 5. Category safety

Both alternative insertions are connected local three-vertex trees with the same five exterior incidences as the current smaller neighbourhood.

Every inserted edge carries a root. Therefore:

- cubicity is immediate;
- no local loop is introduced in the ordinary branch;
- connectivity is preserved because the local replacement remains connected on the same incidence set;
- a bridge would carry zero in an abelian-group flow, impossible for a root-valued edge.

Thus the alternative insertion remains in the connected loopless bridgeless cubic category, apart from the already separated bounded identifications.

---

## 6. Consequence for Ptolemy defect endpoints

A failed inverse step in either zero-valued row can be replaced immediately by a root-valued history edge:

- inverse-flip zero uses the other root NNI;
- inverse-cancellation equality uses Theorem 2.1.

Likewise the good disjoint cancellation row uses Theorem 3.1.

Therefore these rows do not initiate or terminate a persistent singular track in the lifted Ptolemy comparison.

The only unbounded singular endpoint type remaining after local normalization is the missing-index co-root transport branch.

---

## 7. Correction to contextual-transfer master v4

Read `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V4.md` with the following strengthening and correction:

1. quadruple equality is handled by one direct root-valued alternative insertion, not by a path through transient zero states;
2. good doubled-disjoint failure is handled by one direct root-valued alternative insertion;
3. the disjoint row is not uniformly an immediate crossed root resolution;
4. only the missing-index subcase enters the co-root forced-backbone track;
5. every persistent discrepancy track is consequently a co-root track.

A fully corrected master should be issued only after the boundary progress of open co-root tracks is stated explicitly.

---

## 8. Assurance boundary

### Exact here

- equality of the relevant root-triangle pairs in both final five-leaf topologies;
- exact cancellation back to the current smaller source neighbourhood;
- direct root-valued alternative insertion in the equality row;
- direct root-valued alternative insertion in the good doubled-disjoint row;
- absence of zero endpoints in the persistent discrepancy locus;
- isolation of the missing-index co-root branch as the sole unbounded singular type.

### Not proved here

- endpoint progress for open co-root tracks;
- complete corrected contextual transfer;
- cap restoration or global five-support closure;
- PDL reconstruction, independent audit, Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.
