# Defect-minimal forests and the Petersen endpoint transducer

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level variational reduction of the canonical BBD defect flow; exact finite endpoint-transport model; strict graph replacement remains open  
**Parents:** `FIVE_CDC_BBD_GLOBAL_AFFINE_HOLONOMY_K6_DEFECT_STRIP_V1.md`, `FIVE_CDC_TYPE_H_LOCAL_TO_GLOBAL_HOLONOMY_STACK_V1.md`

## 1. Purpose

The BBD affine-holonomy theorem produces a canonical `E_5`-valued flow with the prescribed terminal roots.  It is root-valued exactly in the successful Tait-escape case.  The residual labels are zero or weight-four co-roots.

A first temptation is to encode every co-root strip by its finite index word and apply a pumping argument.  This is not yet legitimate: every internal strip vertex has a side root edge entering the rest of the graph, so the boundary information grows with the strip length.

The correct first reduction is variational.  Among all `E_5`-flows with the same terminal values, choose one with the minimum number of non-root edges.  This packet proves:

1. every cycle satisfies two exact defect-sparsity inequalities;
2. the complete defect support is a forest;
3. every defect-tree component is induced, with boundary size `|V|+2`;
4. the forest has a six-type local grammar;
5. co-root transport states form the line graph of the Petersen graph;
6. the DDD group is exactly the stabiliser of one endpoint state;
7. state repetition alone does not yet justify strip deletion, because the Petersen walk emits an unbounded side-root word.

No five-cycle double cover or strict replacement theorem is claimed.

## 2. The affine flow fibre and defect energy

Let

\[
E_5=\{x\in F_2^5:\sum_i x_i=0\},
\qquad
R_5=\{e_i+e_j:i<j\}.
\]

Fix the terminal root values inherited from the original cover.  The set of all `E_5`-flows with these terminal values is an affine space

\[
\mathcal A=r_0+Z_1(P;F_2)\otimes E_5.
\]

For `r in A`, define

\[
\delta(r)=|\{e:r(e)\notin R_5\}|.
\]

Choose

\[
\boxed{r_*\in\mathcal A\text{ with }\delta(r_*)\text{ minimum}.}
\]

Write an edge of a cycle as:

- `R` if its value is a root, of weight two;
- `Z` if its value is zero;
- `D` if its value is a co-root, of weight four.

For a graph cycle `C`, denote the three counts by

\[
R(C),\qquad Z(C),\qquad D(C).
\]

## 3. Cycle toggles and the exact cost table

For every internal graph cycle `C` and coefficient `a in E_5`, the cycle toggle

\[
 r_*\longmapsto r_*+a\,1_C
\]

remains in `A`.  Minimality therefore gives

\[
\Delta_a(C):=
\sum_{e\in C}
\left(
1_{r_*(e)+a\notin R_5}
-
1_{r_*(e)\notin R_5}
\right)
\ge0.
\]

### Lemma 3.1 — sum over root coefficients

Summing the local defect change over the ten root coefficients gives:

\[
\sum_{a\in R_5}\Delta_a(e)=
\begin{cases}
-10,&r_*(e)=0,\\
4,&r_*(e)\in R_5,\\
-6,&r_*(e)\text{ is a co-root}.
\end{cases}
\]

Hence every graph cycle satisfies

\[
\boxed{4R(C)-10Z(C)-6D(C)\ge0,}
\]

or equivalently

\[
\boxed{2R(C)\ge5Z(C)+3D(C).}
\]

### Lemma 3.2 — sum over co-root coefficients

Summing over the five co-roots gives:

\[
\sum_{a\text{ co-root}}\Delta_a(e)=
\begin{cases}
0,&r_*(e)=0,\\
2,&r_*(e)\in R_5,\\
-4,&r_*(e)\text{ is a co-root}.
\end{cases}
\]

Therefore

\[
\boxed{2R(C)-4D(C)\ge0,}
\]

or

\[
\boxed{R(C)\ge2D(C).}
\]

Both tables were independently checked by exact Wolfram enumeration of the sixteen vectors of `E_5`.

## 4. The defect support is a forest

Define

\[
N=\{e:r_*(e)\notin R_5\}.
\]

### Theorem 4.1 — defect-forest theorem

\[
\boxed{N\text{ contains no graph cycle}.}
\]

#### Proof

If a cycle `C` were contained in `N`, then `R(C)=0` while `Z(C)+D(C)>0`.  The first cycle inequality would give

\[
0\ge5Z(C)+3D(C)>0,
\]

which is impossible.  Equivalently, the average defect change over the ten root toggles is strictly negative, so some toggle improves `r_*`. ∎

Thus every component of `N` is a tree.

## 5. No root chord inside a defect tree

### Theorem 5.1 — induced-tree theorem

No root-valued edge joins two vertices of the same component of `N`.

#### Proof

Suppose a root edge `e=uv` joined two vertices of one defect tree.  The unique `N`-path from `u` to `v`, together with `e`, would form a graph cycle with exactly one root edge and at least one defect edge.

- If the path contains a co-root edge, `R>=2D` fails because `R=1` and `D>=1`.
- If it contains only zero edges, `2R>=5Z+3D` fails because `2>=5`.

Contradiction. ∎

Hence every defect component `K` is an induced tree.  If it has `k` vertices, cubic degree counting gives

\[
\boxed{|\delta(V(K))|=3k-2(k-1)=k+2.}
\]

This is the first exact size-versus-interface relation for the residual BBD obstruction.

## 6. Complete local forest grammar

At a cubic vertex the three `E_5` labels sum to zero.  The possible weight patterns and their degrees in `N` are exactly:

\[
\begin{array}{c|c|c}
\text{weights}&\deg_N&\text{role}\\
\hline
(2,2,2)&0&K_5\text{ root triangle}\\
(0,2,2)&1&\text{zero equality leaf}\\
(2,2,4)&1&K_6\text{ one-factor leaf}\\
(2,4,4)&2&\text{co-root transport vertex}\\
(0,4,4)&3&\text{mixed zero/co-root branch}\\
(0,0,0)&3&\text{all-zero branch}.
\end{array}
\]

The classification follows directly:

- if one label is zero, the other two labels are equal;
- if all labels are nonzero, the `K_6` completion gives either a triangle or a perfect matching.

Consequently:

- every leaf of a defect tree is either an equality gate or a one-factor state;
- every degree-two vertex belongs to a co-root strip;
- every degree-three branch contains a zero edge.

The co-root subgraph is therefore a disjoint union of paths, now with endpoints at one-factor leaves or mixed branches.  The zero subgraph is a forest joining equality leaves, mixed branches, and all-zero branches.

## 7. The fifteen endpoint states

Let `P` be the Petersen graph in its Kneser model

\[
V(P)=\binom{[5]}2,
\]

with two vertices adjacent when the corresponding two-subsets are disjoint.

A `K_6` one-factor containing the co-root edge `\{\infty,i\}` has form

\[
F=\{\infty i,A,B\},
\]

where `A` and `B` are disjoint two-subsets and

\[
[5]=\{i\}\sqcup A\sqcup B.
\]

Therefore

\[
\boxed{
F\longleftrightarrow AB\in E(P).
}
\]

The fifteen one-factor endpoint states are exactly the fifteen edges of the Petersen graph.

The natural `S_5` action is transitive.  The stabiliser of one endpoint state has order eight and is dihedral:

\[
\boxed{
\mathcal F\cong S_5/D_8.
}
\]

The four DDD boundary monodromies generate exactly the stabiliser of the state

\[
\{\infty1,25,34\}.
\]

Thus the previously isolated DDD group is the intrinsic endpoint-state stabiliser.

## 8. Co-root strip transport is `L(Petersen)`

Consider a degree-two defect vertex with incident co-roots

\[
q_i,\qquad q_j,
\]

and side root

\[
e_i+e_j.
\]

Let the incoming virtual one-factor state be

\[
F=\{\infty i,A,B\}.
\]

The index `j` lies in exactly one of `A,B`; write `A=\{j,k\}`.  Moving the distinguished infinity partner from `i` to `j` acts by the transposition `(ij)`:

\[
F'=(ij)F=\{\infty j,\{i,k\},B\}.
\]

Under the Petersen-edge model,

\[
F\longleftrightarrow AB,
\qquad
F'\longleftrightarrow A'B,
\]

so the two endpoint states are adjacent in the line graph `L(P)`.

Conversely every adjacent pair of Petersen edges arises in this way.  Therefore:

### Theorem 8.1 — Petersen transport theorem

\[
\boxed{
\text{the endpoint-state transport graph is }L(\mathrm{Petersen}).
}
\]

It has:

\[
15\text{ states},\qquad
30\text{ transitions},\qquad
\deg=4,
\]

and exact computation gives diameter three and automorphism group `S_5`.

### Side-root output

Suppose the two consecutive Petersen edges are

\[
AB\quad\text{and}\quad A'B.
\]

The three neighbours of `B` in the Petersen graph are

\[
A,\qquad A',\qquad \{i,j\}.
\]

Hence the side root `e_i+e_j` is the third Petersen neighbour at the turn.  A co-root strip is therefore not merely a walk in `L(P)`; it is a finite-state transducer:

\[
\boxed{
\text{state walk in }L(P)
\quad+
\text{one emitted Petersen vertex at every turn}.
}
\]

## 9. Why state repetition is not yet pumping

A walk of length at least fifteen repeats an endpoint state.  The intervening segment therefore has transport in a conjugate of the endpoint stabiliser `D_8`.

However, deleting the segment is not yet justified.  Every turn emits a side root entering the rest of the graph.  Two repeated endpoint states can carry different side-output words and different attached root components.

Thus:

\[
\boxed{
\text{repeated }L(P)\text{ state}
\not\Rightarrow
\text{replaceable strip segment}.
}
\]

The correct enriched semantic state must include the behaviour of the root-side attachments.  The finite Petersen transducer identifies the missing datum precisely; it does not by itself prove a replacement theorem.

## 10. Updated composition target

The residual BBD object is now:

\[
\boxed{
\begin{array}{c}
\text{an induced defect forest}\\
\downarrow\\
\text{equality and one-factor leaves}\\
\downarrow\\
\text{co-root paths carrying }L(\mathrm{Petersen})\text{ transport}\\
\downarrow\\
\text{zero branches coupling those paths}.
\end{array}
}
\]

The next strict theorem should prove one of the following.

1. A leaf-pruning move strictly decreases the graph while preserving the enriched boundary semantics.
2. A root-side component identifies two emitted Petersen labels and creates a smaller cyclic separator.
3. A repeated Petersen state with equivalent side semantics yields a bounded replacement.
4. Failure of all three produces the unique DDD `D_8` affine class on a closed complement cycle.

This is the current composition/termination interface.