# Petersen cycle monodromy and the odd-rotation / even-flat split

## Research dossier v2 — dihedral affine correction integrated

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Original parent head:** `4257e01ff0bbf72ec3c5e6c9222146abba7c17ba`  
**Correction parent:** `projects/affine-cdc/research/DDD_DIHEDRAL_REFLECTION_CLASS_V1.md`  
**Parents:**

- `projects/affine-cdc/research/PETERSEN_PIVOT_RESOLUTION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_BACKTRACK_TYPE_T_REDUCTION_V1.md`;
- the retained Petersen transport theorem;
- the retained cyclic affine-holonomy classification.

**Status:** exact finite classification of the support monodromy of every simple reduced Petersen pivot cycle. Odd cycles supply the rotation half of one DDD stabiliser; the affine `D8` class additionally requires a reflection comparison.  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, physical reflection realisation, or the global five-support theorem.

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

The switch state on edge `s_j s_(j+1)` is

\[
F_j=\{s_j,s_{j+1}\}.
\]

Because consecutive pivots are disjoint two-subsets of `[5]`, there is one omitted support index

\[
i_j=[5]\setminus(s_j\cup s_{j+1}).
\]

At pivot `s_(j+1)`, transport from `F_j` to `F_(j+1)` moves the distinguished infinity partner from `i_j` to `i_(j+1)`. The support permutation of this turn is

\[
\tau_j=(i_j\ i_{j+1})\in S_5.
\]

### Definition 1.1 — cycle support monodromy

With indices read modulo `n`, define

\[
\boxed{
\Pi(C)=\tau_{n-1}\cdots\tau_1\tau_0.
}
\]

Changing the initial edge conjugates the product; reversing orientation replaces it by a conjugate of its inverse. Hence its cycle type is intrinsic to the unoriented simple pivot cycle.

### Side-root word

The side root emitted between `F_j` and `F_(j+1)` is

\[
e_{i_j}+e_{i_{j+1}}.
\]

Consequently

\[
\sum_{j=0}^{n-1}(e_{i_j}+e_{i_{j+1}})=0.
\]

This is necessary for a closed coefficient core, but does not determine its affine side-sheet class.

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

Exact enumeration gives one orbit at each length, so one representative product determines the monodromy class for the complete orbit.

---

## 3. Representative certificates

Use support indices `1,...,5`.

### Length five

The pivot cycle

\[
12,34,15,23,45
\]

has omitted-index word

\[
5,2,4,1,3
\]

and monodromy of cycle type `41`.

### Length six

The cycle

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

The cycle

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

The cycle

\[
12,34,15,23,14,25,13,24,35
\]

has omitted-index word

\[
5,2,4,5,3,4,5,1,4
\]

and monodromy of cycle type `41`.

---

## 4. Odd/even support-monodromy split

### Theorem 4.1

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

There is one `S5` orbit at each possible length. The representative products give identity for lengths six and eight and type `41` for lengths five and nine. ∎

---

## 5. The odd branch is a DDD rotation

Let `C` be an odd simple pivot cycle. Then `Pi(C)` fixes one support index `i` and cyclically permutes the complementary four-set.

### Theorem 5.1 — canonical invariant DDD state

The four-cycle preserves the unique perfect matching formed by its opposite pairs. Together with `infinity i`, this matching defines one DDD/Petersen-edge state `F_C`.

Therefore

\[
\boxed{
\Pi(C)\in D_8=\operatorname{Stab}_{S_5}(F_C),
}
\]

and `Pi(C)` is an order-four rotation in that dihedral stabiliser.

### Affine correction

This identifies the linear support rotation and invariant DDD state. It does not detect the nontrivial class in

\[
H^1(D_8,E_5)\cong\mathbf F_2.
\]

Indeed the rotation subgroup `R=<Pi(C)> ~= C4` satisfies

\[
H^1(R,E_5)=0.
\]

The unique nonzero `D8` class is inflated from the reflection quotient and is zero on `R` after canonical normalisation. Thus an odd cycle is rotation data, not a complete affine DDD calibration.

---

## 6. The even branch is an identity return

For a simple cycle of length six or eight,

\[
\Pi(C)=1.
\]

Any residual obstruction is a pure affine/side-semantic displacement.

An even simple core must enter one of:

1. removable rank-two/Type-T composition;
2. flat affine-`A3` translation residue;
3. common-cut or side-sheet discrepancy;
4. bounded zero/co-root defect interface.

Identity support monodromy alone does not authorise deletion.

---

## 7. Reduced-core normal form

Combine the Type-T backtrack reduction with Theorem 4.1.

### Theorem 7.1 — support-monodromy normal form

Every co-root strip reduces coefficientwise to:

- rank-two constant-pivot runs;
- Type-T `abba` backtracks;
- one reduced core of one of two kinds:
  - **odd core:** a bounded simple Petersen cycle with type-`41` rotation in a canonical DDD stabiliser;
  - **even core:** a bounded simple Petersen cycle with identity support monodromy and purely affine/side-semantic residual data.

For an open reduced skeleton with no cycle, at most nine DDD switch states remain.

No further support-monodromy type occurs in a minimal simple reduced core.

---

## 8. Correct next obligations

### Odd core — reflection realisation

For the canonical DDD state `F_C`:

1. retain the exact order-four rotation `Pi(C)`;
2. construct a compatible bounded reflection of the same physical core, or return failure as a route/fibre/separator/defect obstruction;
3. normalise the rotation cocycle to zero;
4. compute the reflection value
   \[
   c(\sigma)\in\{0,q_i\}.
   \]

The two values distinguish the trivial and nontrivial affine `D8` classes.

A physical comparison between a cycle and its reflected or reversed realisation is the natural first candidate. One rotation loop alone is insufficient.

### Even core — projective displacement

Compute the identity-return physical displacement and prove:

1. zero/complement gauge;
2. nonzero matching/Type-T descent;
3. or a common-cut/separator certificate.

### Open path — bounded transfer

Use the coefficient bound together with the four-port interval semantics to obtain a finite transfer state or a strict separator.

---

## 9. Reliability boundary

### Exact here

- the omitted-index transposition formula;
- zero total sum of the emitted side-root word on a closed pivot cycle;
- the complete simple-cycle length/count/orbit table;
- identity monodromy for lengths six and eight;
- type-`41` monodromy for lengths five and nine;
- the canonical invariant DDD state for every odd simple core;
- the odd-rotation / even-identity support-monodromy dichotomy;
- rotation blindness of the affine `D8` class.

### Still open

- physical bounded reflection realisation;
- its translation value `0` or `q_i`;
- affine displacement of even cores;
- graph-side replacement or contraction;
- separator extraction from attached semantics;
- strict Type-T/Type-H descent, horizontal induction, and the global five-support theorem.
