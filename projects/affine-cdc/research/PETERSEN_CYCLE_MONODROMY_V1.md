# Petersen cycle monodromy and the odd-DDD / even-flat split

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `4257e01ff0bbf72ec3c5e6c9222146abba7c17ba`  
**Parents:**

- `projects/affine-cdc/research/PETERSEN_PIVOT_RESOLUTION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_BACKTRACK_TYPE_T_REDUCTION_V1.md`;
- the retained Petersen transport theorem;
- the retained cyclic affine-holonomy classification.

**Status:** exact finite classification of the support monodromy of every simple reduced Petersen pivot cycle; affine translation/side-sheet class and graph-side composition remain open.  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, the physical DDD cohomology identification, or the global five-support theorem.

---

## 1. Support transport along a pivot cycle

Let

\[
C=(s_0,s_1,\ldots,s_{n-1},s_0)
\]

be a simple cycle in the Petersen pivot graph

\[
P=KG(5,2).
\]

The switch state on the edge `s_j s_(j+1)` is the Petersen edge

\[
F_j=\{s_j,s_{j+1}\}.
\]

Because `s_j` and `s_(j+1)` are disjoint two-subsets of `[5]`, there is one omitted support index

\[
i_j=[5]\setminus(s_j\cup s_{j+1}).
\]

At the next pivot `s_(j+1)`, transport from state `F_j` to state `F_(j+1)` moves the distinguished infinity partner from `i_j` to `i_(j+1)`. By the Petersen transport theorem, the support permutation of this turn is

\[
\tau_j=(i_j\ i_{j+1})\in S_5.
\]

### Definition 1.1 — cycle support monodromy

With indices read modulo `n`, define

\[
\boxed{
\Pi(C)=	au_{n-1}\cdots\tau_1\tau_0.
}
\]

Changing the initial edge conjugates the product; reversing orientation replaces it by a conjugate of its inverse. Hence its cycle type is intrinsic to the unoriented simple pivot cycle.

### Side-root word

The side root emitted at the pivot between `F_j` and `F_(j+1)` is

\[
e_{i_j}+e_{i_{j+1}}.
\]

Consequently the complete emitted coefficient word has zero sum:

\[
\sum_{j=0}^{n-1}(e_{i_j}+e_{i_{j+1}})=0.
\]

This is necessary for a closed coefficient core, but it does not determine its affine side-sheet class.

---

## 2. Exact cycle-orbit census

### Theorem 2.1 — simple-cycle classification

The Petersen graph has simple cycles only of lengths

\[
\boxed{5,6,8,9.}
\]

Their exact counts are

\[
\begin{array}{c|cccc}
 n&5&6&8&9\\
\hline
\#C_n&12&10&15&20.
\end{array}
\]

For each admissible length, `S5=Aut(P)` acts transitively on the corresponding simple cycles.

### Finite verification

The graph is constructed from the ten two-subsets of `[5]`, joining disjoint pairs. A depth-first enumeration records a cycle only when its first vertex is the least vertex in the cycle and then quotients by reversal. Applying all 120 support permutations to one representative of each length produces respectively 12, 10, 15, and 20 distinct cycles, equal to the exhaustive counts.

Thus one representative computation determines the monodromy conjugacy class for every cycle of that length.

---

## 3. Representative certificate table

Use support indices `1,...,5`. The following table lists one pivot cycle, its omitted-index word `(i_j)`, and the resulting support monodromy.

### Length five

\[
12,34,15,23,45
\]

has omitted-index word

\[
5,2,4,1,3
\]

and

\[
\Pi(C)\sim(1\ 4\ 2\ 3),
\]

of cycle type `41`.

### Length six

\[
12,34,15,23,14,35
\]

has omitted-index word

\[
5,2,4,5,2,4
\]

and

\[
\Pi(C)=1.
\]

### Length eight

\[
12,34,15,23,14,25,13,45
\]

has omitted-index word

\[
5,2,4,5,3,4,2,3
\]

and

\[
\Pi(C)=1.
\]

### Length nine

\[
12,34,15,23,14,25,13,24,35
\]

has omitted-index word

\[
5,2,4,5,3,4,5,1,4
\]

and

\[
\Pi(C)\sim(1\ 4\ 2\ 3),
\]

again of cycle type `41`.

Each product is obtained directly from

\[
\Pi(C)=
(i_{n-1}\ i_0)
(i_{n-2}\ i_{n-1})\cdots
(i_0\ i_1),
\]

with the opposite convention giving the inverse and hence the same cycle type.

---

## 4. Parity theorem

### Theorem 4.1 — odd/even monodromy split

For every simple Petersen pivot cycle `C`,

\[
\boxed{
|C|\text{ even}
\Longrightarrow
\Pi(C)=1,
}
\]

whereas

\[
\boxed{
|C|\text{ odd}
\Longrightarrow
\Pi(C)\text{ has cycle type }41.
}
\]

### Proof

By Theorem 2.1 there is one `S5` orbit at each possible length. The representative products in Section 3 give identity for lengths six and eight and type `41` for lengths five and nine. Cycle type is invariant under conjugacy. ∎

---

## 5. The odd branch is a DDD-stabiliser holonomy

Let `C` be an odd simple pivot cycle. Then `Pi(C)` fixes one support index and cyclically permutes the other four.

### Theorem 5.1 — canonical invariant DDD state

A four-cycle on four support indices preserves the unique perfect matching formed by its opposite pairs. Together with the fixed support index and the symbol `∞`, this matching defines one `K6` one-factor, hence one DDD/Petersen-edge state.

Therefore

\[
\boxed{
\Pi(C)\in D_8=\operatorname{Stab}_{S_5}(F_C)
}
\]

for a canonically determined DDD state `F_C`.

Moreover `Pi(C)` is an order-four rotation in this dihedral stabiliser.

### Trust boundary

This identifies the linear support monodromy and its invariant DDD state. It does **not** yet prove that the physical affine holonomy represents the nontrivial class in

\[
H^1(D_8,E_5)\cong\mathbf F_2.
\]

That requires the translation/side-root attachment datum, not only the permutation part.

---

## 6. The even branch is an identity return, not automatic triviality

For a simple cycle of length six or eight,

\[
\Pi(C)=1.
\]

Thus its support frame returns exactly, and any residual obstruction is a pure affine/side-semantic displacement.

### Consequence 6.1 — even-core target

An even simple pivot cycle must enter one of the already isolated identity-return mechanisms:

1. removable rank-two/Type-T composition;
2. flat affine-`A3` translation residue;
3. common-cut or side-sheet discrepancy;
4. bounded zero/co-root defect interface.

Identity support monodromy alone does not authorize deletion: the attached side-root components may still carry nonzero physical translation or separator data.

---

## 7. Revised reduced-core normal form

Combine the Type-T backtrack reduction with Theorem 4.1.

### Theorem 7.1 — three-sector coefficient normal form

Every co-root strip reduces coefficientwise to:

\[
\boxed{
\begin{array}{c}
\text{rank-two constant-pivot runs}\\
+\text{Type-T `abba` backtracks}\\
+\text{one reduced core of one of two kinds:}
\end{array}
}
\]

- **odd core:** a bounded simple Petersen cycle with type-`41` monodromy in a canonical DDD `D8` stabiliser;
- **even core:** a bounded simple Petersen cycle with identity support monodromy and purely affine/side-semantic residual data.

For an open reduced skeleton with no cycle, at most nine DDD switch states remain.

No further support-monodromy type occurs in a minimal simple reduced core.

---

## 8. Exact next obligations

### Odd core

Compute the physical affine cocycle relative to the canonical invariant DDD state `F_C`. Prove that it is:

1. the nontrivial `D8` class;
2. root-resolvable after a bounded route change;
3. or localised to a bounded DDD/defect interface.

### Even core

Compute its identity-return physical displacement in the projective matching module and prove:

1. zero/complement gauge;
2. nonzero matching/Type-T descent;
3. or a common-cut/separator certificate.

### Open path

Use the nine-edge coefficient bound together with the four-port interval semantics to obtain a finite transfer state or a strict separator.

---

## 9. Reliability boundary

### Exact here

- the omitted-index transposition formula for pivot transport;
- zero total sum of the emitted side-root word on a closed pivot cycle;
- the complete simple-cycle length/count/orbit table of the Petersen graph;
- the representative monodromy products;
- identity monodromy for lengths six and eight;
- type-`41` monodromy for lengths five and nine;
- the canonical invariant DDD state for every odd simple core;
- the odd-DDD / even-identity support-monodromy dichotomy.

### Still open

- affine translation and side-sheet monodromy of the simple cores;
- physical identification with the nontrivial `D8` cohomology class;
- graph-side replacement or contraction;
- separator extraction from attached semantics;
- strict Type-T/Type-H descent, horizontal induction, and the global five-support theorem.
