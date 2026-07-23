# A root-presented innermost cancellation bubble compresses to one predecessor-order atom path

## Research Lead variable-order compression theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `VARIABLE_ORDER_PERIODIC_EPISODE_COMPRESSION_GAP_V1.md`;
- `CENTRAL_WELD_FLIP_B_PRESERVING_ROOT_LIFT_V1.md`;
- `CENTRAL_WELD_FLIP_BAD_EXIT_ONE_ATOM_LIFT_V1.md`;
- `CENTRAL_WELD_FLIP_EQUAL_OPPOSITE_ONE_ATOM_MOVIE_V1.md`;
- `ADJACENT_WELD_FLIP_THREE_NNI_ROOT_LIFT_V1.md`;
- `WELD_INSERTION_SUPPORT_SWITCH_LIFT_V1.md` v2;
- the equality and doubled-disjoint borrowing theorems.

**Status:** exact compression theorem under a root-presentation hypothesis. Let one innermost lower-order episode contain no further `2--0` move and be explicitly presented as a finite sequence of root-valued `2--2` moves and support-pair component switches. Starting from the inherited weld-admissible pair, apply raw insertion at every lower state. Every lower move has a bounded predecessor-order lift, and every lifted state has at most one non-root central edge. Concatenation gives a predecessor-order path from the original inherited insertion to the raw returned insertion. The terminal equality/good-disjoint rows rootify in two local NNIs; the missing-index row normalizes to one co-root atom. Thus the complete variable-order birth/history/death bubble is replaced by a fixed-order root/one-atom path.

This theorem does not assert that arbitrary inherited and returned lower-order root flows admit such a root-only move presentation. That presentation problem is now the remaining interface for a general innermost bubble.

---

## 1. Innermost root-presented bubble

Let

\[
(G_0,\Lambda_0)
\xrightarrow{2--0}
(H_0,\lambda_0)
\]

be one forward equal-face cancellation. Its two output edge lineages carry roots

\[
p_0,q_0
\]

with

\[
p_0+q_0\in R_5.
\]

Assume the lower-order episode has no further cancellation and is explicitly presented as

\[
(H_0,\lambda_0)
\longrightarrow
(H_1,\lambda_1)
\longrightarrow\cdots\longrightarrow
(H_m,\lambda_m),
\]

where each step is either:

1. one root-valued ordinary `2--2` NNI; or
2. one support-pair component switch on a root-valued flow.

The two output incidence lineages are transported through the history:

\[
(e_i,f_i),
\qquad
p_i=\lambda_i(e_i),
\quad
q_i=\lambda_i(f_i).
\]

A central-diagonal crossing replaces the relevant edge lineage by the new diagonal sheet; disjoint/exterior moves preserve it; support switches preserve the edge incidences and change only values.

Assume the final lower topology and incidence lineages are those required by the paired returned `0--2` step.

---

## 2. Raw insertion at every lower state

For each `i`, split `e_i,f_i`, restore the two predecessor-order vertex slots and assign central value

\[
\boxed{x_i=p_i+q_i.}
\]

Call the resulting `E_5` flow state

\[
I_i=I(H_i,\lambda_i;e_i,f_i).
\]

Every noncentral edge of `I_i` is a root. The central edge is:

\[
\begin{array}{c|c}
(p_i,q_i)\text{ relation}&x_i\\
\hline
A&0\\
B&\text{root}\\
C&\text{co-root}.
\end{array}
\]

Hence each `I_i` has at most one atom.

The initial state `I_0` is the original inherited equal-face insertion and is fully root-valued.

---

## 3. Lift of one lower root NNI

Consider one lower root flip.

### 3.1 Neither mark active

If the flip is disjoint from both marks or both marks remain exterior branches, perform the same relative NNI on the expanded graph. The inserted central edge is unchanged, so the atom count remains at most one.

### 3.2 One mark active, second edge disjoint from the support

Let the active marked diagonal change from `p` to the disjoint root `p'`, and let the other marked root be `q`.

The ten roots `q` are exhausted by:

- `q=p` or `q=p'`: the equal/opposite five-move one-atom movie;
- four common neighbours of `p,p'`: the root-valued five/six-move movies;
- four roots adjacent to one of `p,p'` and disjoint from the other: the five-move one-atom movie or its reverse.

Thus the raw expanded states before and after are joined by a bounded NNI path with at most one atom in every state.

### 3.3 One mark active, second edge adjacent

If the second marked edge is one exterior branch of the flip, `ADJACENT_WELD_FLIP_THREE_NNI_ROOT_LIFT_V1.md` gives the root-valued triangle--square--square--triangle movie.

### Theorem 3.1 — universal root-flip raw lift

Every ordinary distinct-incidence lower root NNI lifts from `I_i` to `I_(i+1)` by a predecessor-order NNI path carrying at most one zero/co-root edge.

Nonordinary endpoint identifications are bounded loop/parallel/triangle/cut exits.

---

## 4. Lift of one support-pair switch

By `WELD_INSERTION_SUPPORT_SWITCH_LIFT_V1.md` v2, let `delta_p,delta_q` indicate whether the switched lower component contains each marked edge.

Lift its inherited edge set and add the inserted central edge exactly when

\[
\delta_p\oplus\delta_q=1.
\]

The correction is even and sends

\[
x_i=p_i+q_i
\]

to

\[
\begin{aligned}
x_{i+1}
&=x_i+(\delta_p\oplus\delta_q)h\\
&=(p_i+\delta_p h)+(q_i+\delta_q h)\\
&=p_{i+1}+q_{i+1}.
\end{aligned}
\]

Every noncentral edge remains a root. Therefore the lifted output is exactly `I_(i+1)` and has at most one central atom.

---

## 5. Concatenated predecessor-order path

Concatenate the bounded lifts of Sections 3--4.

### Theorem 5.1 — raw bubble strip

The complete lower root-presented history lifts to a finite predecessor-order path

\[
\boxed{
I_0\rightsquigarrow I_1\rightsquigarrow\cdots\rightsquigarrow I_m
}
\]

such that:

1. every source has the vertex order of `G_0`;
2. every exterior incidence, cap shore and rooted attachment is transported exactly as in the lower history;
3. every noncentral edge is root-valued;
4. every state contains at most one zero/co-root central atom;
5. no lower-order state survives as a macro vertex.

The singular locus along this path is one nonbranching one-edge lineage, possibly born, rootified and reborn, but never duplicated.

---

## 6. Terminal normalization

Inspect the returned pair `(p_m,q_m)`.

### `B` row

If the pair is distinct intersecting, `I_m` is already a root-valued inverse insertion.

### Equality row

If `p_m=q_m`, `I_m` has one zero edge. Borrow one adjacent root vertex. The two-step five-leaf path

\[
T_0\to T_4\to T_3
\]

carries one zero in `T_0,T_4` and ends at the root-valued alternative insertion `T_3`.

### Good doubled-disjoint row

The same two-step path carries one co-root through the first two states and ends at the root-valued alternative insertion.

### Missing-index doubled-disjoint row

The first borrowing move produces the standard two-co-root three-vertex transport unit

\[
(Q_i,Q_j,ij).
\]

The full-defect-tree normalization immediately returns it to at most one co-root atom or an accepted bounded/separator exit.

### Theorem 6.1 — root/one-atom endpoint

The raw returned insertion normalizes to exactly one of:

\[
\boxed{
\text{root-valued original insertion},
\quad
\text{root-valued alternative insertion},
\quad
\text{one normalized co-root state},
\quad
\text{accepted bounded/category exit}.}
\]

---

## 7. Innermost bubble compression theorem

### Theorem 7.1

Every root-presented innermost cancellation bubble

\[
G_0\xrightarrow{2--0}H_0
\rightsquigarrow
H_m\xrightarrow{0--2}G_m
\]

admits a boundary-preserving replacement at the vertex order of `G_0` by a finite history path with at most one persistent atom.

The replacement begins at the inherited root state on `G_0` and ends at a root-valued predecessor-order insertion, one normalized co-root discrepancy state, or an accepted exit.

No graph-order recursion, arbitrary-flow weld selection or hidden history coordinate is used.

---

## 8. Exact remaining quantifier gap

The theorem assumes that the lower returned root state is connected to the inherited lower root state by an explicitly supplied history whose states are all root-valued and whose moves are root NNIs or support-pair component switches.

It does **not** prove:

\[
\boxed{
\text{every two relevant lower root states admit such a root-only presentation}.}
\]

Kempe connectivity alone is false on prime examples, and a general fixed-order contextual comparison may itself use one co-root track. Lifting such a lower singular comparison may create an additional insertion atom and requires a coupled two-defect or stratified-history theorem.

Thus the next frontier is:

### Target 8.1 — singularly presented innermost bubble

Lift one lower fixed-order history which already carries one normalized co-root track through the raw insertion, while proving rootification, coupling to one connected defect tree, or another strict relative reduction without persistent two-atom separation.

---

## 9. Assurance boundary

### Exact here

- raw insertion at every lower root state;
- universal root-NNI local lift;
- universal support-switch lift;
- concatenation with at most one atom;
- endpoint equality/good-disjoint rootification;
- missing-index normalization;
- complete compression of root-presented innermost bubbles.

### Not claimed

- root-only presentation of arbitrary lower returned flows;
- lifting of a lower history already containing one atom;
- arbitrary innermost or nested bubble compression;
- R2.7 closure, cap restoration or global five-support closure;
- PDL reconstruction, audit, Lean, manuscript, curation, release or publication.
