# Equal and opposite raw weld insertions are joined by one five-move atom movie

## Research Lead innermost-bubble local theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `CENTRAL_WELD_FLIP_B_PRESERVING_ROOT_LIFT_V1.md`;
- `CENTRAL_WELD_FLIP_BAD_EXIT_ONE_ATOM_LIFT_V1.md`;
- the raw inverse-insertion equation `x=p+q`.

**Status:** exact completion of the disjoint-endpoint active-diagonal table for the cases in which the second marked root equals the old or new flip diagonal. If `q=p`, the raw insertion before the lower flip has one zero central edge and the insertion after the flip has one co-root central edge `p+p'`. They are connected by five predecessor-order NNIs with at most one non-root internal edge. The reverse movie treats `q=p'`.

---

## 1. Flip and marked-edge data

Let

\[
A+B=C+D=p,
\qquad
A+C=B+D=p'
\]

be one root-valued lower `2--2` flip, so `p,p'` are disjoint roots.

Let the second marked edge have root

\[
\boxed{q=p.}
\]

At its two endpoints choose arbitrary ordered root-triangle decompositions

\[
E+F=q,
\qquad
G+H=q.
\]

The eight exterior branch roots have total xor zero.

---

## 2. Endpoint raw insertions

The raw insertion before the flip has split system

\[
\Sigma_0=\{AB,ABEF,CD,EF,GH\}.
\]

Its internal values are

\[
p,\ p+q,\ p,\ q,\ q
=
 p,\ 0,\ p,\ p,\ p.
\]

Thus `Sigma_0` has exactly one zero edge.

The raw insertion after the flip has

\[
\Sigma_5=\{AC,ACEF,BD,EF,GH\},
\]

with internal values

\[
p',\ p'+q,\ p',\ q,\ q.
\]

Since `p,p'` are disjoint,

\[
\boxed{p'+q=p'+p}
\]

is one co-root. Thus `Sigma_5` has exactly one co-root edge.

---

## 3. Five-move movie

Use:

\[
\begin{aligned}
\Sigma_0&=\{AB,ABEF,CD,EF,GH\},\\
\Sigma_1&=\{AB,ABEF,CGH,EF,GH\},\\
\Sigma_2&=\{ABEF,AEF,CGH,EF,GH\},\\
\Sigma_3&=\{AEF,BD,CGH,EF,GH\},\\
\Sigma_4&=\{ACEF,AEF,BD,EF,GH\},\\
\Sigma_5&=\{AC,ACEF,BD,EF,GH\}.
\end{aligned}
\]

Consecutive split systems differ by one NNI.

The changing values are:

\[
\begin{array}{c|c}
\text{split}&\text{value}\\
\hline
ABEF&p+q=0\\
CGH&C+q=C+p=D\\
AEF&A+q=A+p=B\\
BD&p'\\
ACEF&p'+q=p'+p\text{ (co-root)}\\
AC&p'.
\end{array}
\]

Therefore the defect-count sequence is

\[
\boxed{1,1,1,0,1,1.}
\]

No state contains more than one non-root edge.

### Theorem 3.1 — equal-to-opposite movie

For `q=p`, the old raw zero insertion and the new raw co-root insertion are connected by five predecessor-order NNIs with at most one atom.

For `q=p'`, reverse the movie after exchanging old and new flip coordinates. It connects a co-root insertion to a zero insertion with the same bound.

---

## 4. Complete disjoint-endpoint diagonal table

For fixed disjoint flip diagonals `p,p'`, the ten possible roots `q` split as:

1. `q=p` or `q=p'`: the present zero/co-root movie;
2. four roots intersecting both `p,p'`: root movies of length five or six;
3. four roots intersecting exactly one of `p,p'`: one-atom five-move movie or its reverse.

Hence every root `q` admits a predecessor-order active-diagonal lift with at most one non-root edge throughout.

---

## 5. Assurance boundary

### Exact here

- endpoint zero/co-root classification;
- explicit five split moves;
- exact intermediate root values;
- defect sequence `1,1,1,0,1,1`;
- completion of the ten-root disjoint-endpoint table.

### Not claimed

- complete bubble assembly;
- nested variable-order compression;
- R2.7 closure, cap restoration or global five-support closure;
- PDL reconstruction, audit, Lean, manuscript, curation, release or publication.
