# An adjacent weld edge lifts through a root flip in three root NNIs

## Research Lead innermost-bubble local theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `CENTRAL_WELD_FLIP_B_PRESERVING_ROOT_LIFT_V1.md`;
- `CENTRAL_WELD_FLIP_BAD_EXIT_ONE_ATOM_LIFT_V1.md`;
- `MARKED_WELD_PACHNER_OVERLAP_SCOPE_V1.md`.

**Status:** exact source-level disposition of the active-diagonal overlap when the second weld edge is one exterior branch of the lower-order flip. The inverse weld before the flip contains one root-labelled triangle of three equal faces and one tail vertex. The inverse weld after the flip has the analogous triangle on the new diagonal. They are connected by three boundary-preserving root-valued NNIs. Thus every generic adjacent-mark central overlap stays in the weld-admissible orbit and has a shorter root lift than the disjoint eight-port case.

Non-generic identifications in which exterior branches coincide, form loops/parallel edges, or meet the opposite flip vertex are bounded low-port/category configurations and are not asserted to be internal prime moves.

---

## 1. Lower-order flip coordinates

Let the lower-order root flip have four ordered exterior branch roots

\[
A,B,C,D\in R_5
\]

and old/new diagonals

\[
\boxed{
A+B=C+D=p,
\qquad
A+C=B+D=p'.
}
\]

Then `p,p'` are roots and are disjoint.

Assume the second weld edge is the exterior branch `A`. It shares the old-diagonal endpoint whose other exterior branch is `B`.

Because

\[
p+A=B,
\qquad
p'+A=C,
\]

both weld pairs

\[
(p,A)
\quad\text{and}\quad
(p',A)
\]

are distinct intersecting root pairs. Hence no coefficient `B`-exit can occur in this adjacent case.

The cases in which the second weld edge is `B,C` or `D` follow by relabelling the four branches and choosing the corresponding root-valued flip orientation.

---

## 2. Expanded source before the flip

Use four internal vertices

\[
u,x,y,v.
\]

The inverse weld on the adjacent edges `p` and `A` has the following internal and exterior edges:

\[
\begin{array}{c|c}
\text{edge}&\text{root value}\\
\hline
ux&p\\
uy&A\\
xy&B\\
xA&A\\
u B&B\\
yv&p\\
vC&C\\
vD&D.
\end{array}
\]

The vertices `u,x,y` form a triangle whose three edge/branch values are the root triangle

\[
\{p,A,B\}.
\]

Indeed all three vertices carry the same unordered root face. The vertex `v` is the tail vertex with root triangle

\[
\{p,C,D\}.
\]

Cancelling either appropriate equal-face pair in the triangle recovers the lower-order old flip topology with branches `A,B` on one side and `C,D` on the other.

Call this expanded graph `X_0`.

---

## 3. First NNI: perform the lower-order flip on the tail bridge

Apply an NNI to the bridge

\[
yv
\]

of value `p`, using the branch values `A` at `y` and `C` at `v` for the new pairing.

The new central value is

\[
A+C=p'\in R_5.
\]

The result `X_1` has the root-labelled four-cycle

\[
u-x-v-y-u
\]

with edge values

\[
p,\ B,\ p',\ A
\]

in cyclic order, and exterior branches:

\[
B\text{ at }u,\quad
A\text{ at }x,\quad
D\text{ at }v,\quad
C\text{ at }y.
\]

Every edge remains root-valued.

---

## 4. Second NNI: exchange the two opposite exterior branches

Apply an NNI to the four-cycle edge

\[
xv
\]

whose current value is `B`.

At `x` the other incident values are `p,A`; at `v` they are `p',D`. Choose the alternative pairing which places `p,D` together and `A,p'` together.

The new central value is

\[
\boxed{p+D=C\in R_5,}
\]

because `C+D=p`.

The resulting root four-cycle `X_2` has internal edge values

\[
p,\ C,\ p',\ A
\]

and exterior branches:

\[
B\text{ at }u,\quad
D\text{ at }x,\quad
A\text{ at }v,\quad
C\text{ at }y.
\]

---

## 5. Third NNI: close the new equal-root triangle

Apply an NNI to the edge

\[
ux
\]

of value `p` in `X_2`. Pair the `A` branch at `u` with the `C` branch at `x`.

The new central value is

\[
A+C=p'\in R_5.
\]

The output `X_3` consists of:

- a root-labelled triangle with values
  \[
  \{p',A,C\};
  \]
- one tail vertex carrying
  \[
  \{p',B,D\}.
  \]

This is exactly the inverse weld inserted on the adjacent post-flip edges `p'` and `A`.

---

## 6. Main theorem

### Theorem 6.1 — adjacent central-overlap lift

Suppose one weld edge is the active diagonal of a lower-order root-valued `2--2` flip and the other weld edge is one of its four exterior branches. In the ordinary distinct-incidence case, the inverse-weld expansions before and after the flip are joined by three root-valued relative NNIs fixing the four exterior branch incidences.

The sequence of selected central values is

\[
\boxed{p',\ C,\ p'.}
\]

No zero or co-root edge occurs.

### Proof

Sections 3--5 give the explicit source movie. Root validity follows from

\[
A+C=p',
\qquad
p+D=C.
\]

The remaining exterior-branch choices follow by the symmetries of the root flip. ∎

---

## 7. Complete active-diagonal local table

Combining the three central-overlap theorems gives:

### Disjoint second marked edge

- transported pair remains in `B`: root movie of length at most six;
- transported pair leaves `B`: five-move movie with exactly one terminal co-root atom.

### Adjacent second marked edge

- the second mark is an exterior branch of the flip;
- the transported pair automatically remains in `B`;
- there is a three-move root movie.

Thus every ordinary active-diagonal overlap in a pure lower-order `2--2` history has a bounded predecessor-order source lift. The only remaining local cases are bounded incidence identifications, not a new unbounded coefficient/source species.

---

## 8. Bounded identification boundary

The theorem assumes the four lower-order exterior branches are distinct edge incidences and that the exterior marked edge is not a loop or a second edge directly joining the two active vertices.

If these assumptions fail, the local support contains one of:

- a loop;
- parallel active edges;
- a triangle on the active vertices and one exterior endpoint;
- a two-, three-, or four-port bounded carrier;
- an immediate small edge cut.

These belong to the already declared bounded/category or triangle/cut layers. A complete PDL consumer must enumerate the identifications rather than silently treating them as the generic three-NNI movie.

---

## 9. Assurance boundary

### Exact here

- explicit adjacent inverse-weld source graph;
- the triangle--square--square--triangle movie;
- all three root-valued NNI central labels;
- automatic preservation of the `B` relation;
- complete generic adjacent-mark disposition.

### Not claimed

- internal treatment of bounded identifications;
- support-pair switch lifting;
- assembly of a complete innermost bubble strip;
- variable-order episode compression;
- R2.7 closure, cap restoration or global five-support closure;
- PDL reconstruction, audit, Lean, manuscript, curation, release or publication.
