# The canonical reflection of a based Petersen five-cycle

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `ea53b2a5e46852e4ffbb358e533e5b9a3c4514fb`  
**Parents:**

- `projects/affine-cdc/research/PETERSEN_CYCLE_MONODROMY_V1.md`;
- `projects/affine-cdc/research/PETERSEN_RESOLUTION_PARITY_V1.md`;
- `projects/affine-cdc/research/DDD_DIHEDRAL_REFLECTION_CLASS_V1.md`;
- `projects/affine-cdc/research/SIX_OUTPUT_RETURN_CELL_NORMAL_FORM_V1.md`.

**Status:** exact support-side construction of the unique reflection attached to a based Petersen five-cycle. The required dihedral calibration pair exists canonically at the coefficient/support level; physical boundary-preserving realisation remains open.  
**Not implied:** source-graph reflection, affine cocycle value, graph replacement, canonical acceptance, Lean verification, or the global five-support theorem.

---

## 1. Based five-cycle

Let

\[
C=(s_0,s_1,s_2,s_3,s_4,s_0)
\]

be an oriented Petersen five-cycle. Choose the initial switch state

\[
F_0=\{s_0,s_1\}.
\]

Let

\[
\rho=\Pi(C)\in S_5
\]

be its support monodromy based at `F_0`.

The Petersen cycle theorem gives:

- `rho` has cycle type `41`;
- the state walk returns to `F_0`, so `rho` stabilises `F_0`;
- `F_0` is the unique DDD/Petersen-edge state invariant under `rho`;
- `rho` is the order-four rotation in
  \[
  D=\operatorname{Stab}_{S_5}(F_0)\cong D_8.
  \]

---

## 2. Setwise stabiliser of the five-cycle

The twelve Petersen five-cycles form one `S5` orbit. Therefore the setwise stabiliser

\[
H_C=\operatorname{Stab}_{S_5}(C)
\]

has order

\[
|H_C|=120/12=10.
\]

The induced action on the five vertices of `C` is faithful: a support permutation fixing every pivot root on the cycle fixes the support indices and is the identity.

Hence:

### Theorem 2.1 — cycle stabiliser

\[
\boxed{H_C\cong D_{10}=\operatorname{Aut}(C_5).}
\]

It contains five cycle rotations and five cycle reflections.

---

## 3. Reflection fixing the based switch state

In the abstract five-cycle, a chosen edge has a unique nontrivial automorphism fixing that edge setwise: the reflection exchanging its two endpoints and reversing the remaining path of length three.

By Theorem 2.1 this automorphism is induced by a unique support permutation

\[
\sigma_C\in H_C.
\]

### Theorem 3.1 — canonical based reflection

There is a unique nonidentity support permutation `sigma_C` such that:

1. `sigma_C(F_0)=F_0` setwise;
2. `sigma_C(s_0)=s_1` and `sigma_C(s_1)=s_0`;
3. `sigma_C` reverses the oriented five-cycle based at `F_0`;
4. `sigma_C^2=1`.

This is the **canonical reflection of the based five-cycle**.

---

## 4. Dihedral relation with support monodromy

Support monodromy is equivariant under support relabelling:

\[
\Pi(\sigma C)=\sigma\Pi(C)\sigma^{-1}.
\]

Reversing the based cycle replaces its monodromy by the inverse. Since `sigma_C` reverses `C`, one obtains:

### Theorem 4.1 — rotation/reflection relation

\[
\boxed{
\sigma_C\rho\sigma_C^{-1}=\rho^{-1}.
}
\]

Moreover `sigma_C` stabilises `F_0`, so

\[
\sigma_C\in D=\operatorname{Stab}_{S_5}(F_0).
\]

Since `sigma_C` has order two and is not a power of the order-four rotation `rho`,

\[
\boxed{
\langle\rho,\sigma_C\rangle=D\cong D_8.
}
\]

Thus every based Petersen five-cycle canonically supplies the complete abstract dihedral pair required by the corrected affine-cohomology theorem.

---

## 5. Representative certificate

Take the representative pivot cycle

\[
C=(12,34,15,23,45,12)
\]

with based switch state

\[
F_0=\{12,34\}.
\]

Its omitted-index word is

\[
5,2,4,1,3,
\]

and direct multiplication gives

\[
\rho=(1\ 4\ 2\ 3),
\]

fixing support index `5`.

The canonical reflection is

\[
\boxed{
\sigma_C=(1\ 4)(2\ 3).
}
\]

It acts on the five pivot vertices by

\[
(12,34,15,23,45)
\longmapsto
(34,12,45,23,15),
\]

which is the reversal fixing the base edge setwise.

One checks

\[
\sigma_C\rho\sigma_C=\rho^{-1}.
\]

The canonical invariant DDD state is

\[
\{\infty5,12,34\},
\]

and the reflection-supported coefficient is

\[
q_5=(1,1,1,1,0).
\]

---

## 6. Correct affine detector

Let

\[
c:D\to E_5
\]

be the physical affine cocycle on the DDD stabiliser, assuming both the rotation and reflection have been physically realised with compatible boundary semantics.

Because

\[
H^1(\langle\rho\rangle,E_5)=0,
\]

change affine origin so that

\[
c(\rho)=0.
\]

Then the reflection-support theorem gives

\[
\boxed{
c(\sigma_C)\in\{0,q_i\}.}
\]

For the representative:

\[
\boxed{
c((14)(23))\in\{0,11110\}.}
\]

These two values distinguish the trivial and nontrivial physical `D8` affine classes.

---

## 7. What remains physical

The abstract support reflection is automatic. The unresolved statement is not existence of a reflection in `S5`; it is source-graph realisability with the required incidence data.

### Target 7.1 — physical reflected-cycle comparison

For a six-output return cell whose reduced core is `C`, compare:

1. the original physical realisation of the based cycle;
2. the support-reflected realisation obtained from `sigma_C`;
3. the reversed traversal of the same source interval.

Prove one of:

- the reflected and reversed objects have the same four-port boundary semantics and define a physical reflection loop;
- a route pairing changes, giving profile escape;
- an edge fibre or vertex relation becomes empty;
- the discrepancy separates through a smaller cyclic cut/four-pole;
- the discrepancy localises to one bounded DDD/co-root atom.

If the physical reflection loop exists, compute its normalised translation `0` or `q_i`.

---

## 8. Strategic consequence

The corrected odd-core programme has only one missing bridge:

\[
\boxed{
\text{canonical abstract reflection}
\longrightarrow
\text{boundary-preserving physical reflection or strict obstruction}.
}
\]

No additional search through `D8`, no further Petersen-cycle census, and no second support-theoretic symmetry construction are required.

The six-output bound makes the entire comparison finite at the coefficient and route-interface levels.

---

## 9. Trust boundary

### Exact here

- `Stab_(S5)(C) ~= D10` for every Petersen five-cycle;
- uniqueness of the cycle reflection fixing a chosen base edge setwise;
- support realisation `sigma_C` of that reflection;
- `sigma_C rho sigma_C^(-1)=rho^(-1)`;
- generation of the canonical DDD stabiliser `D8` by `rho,sigma_C`;
- the explicit representative `rho=(1 4 2 3)`, `sigma_C=(1 4)(2 3)`;
- reduction of the affine detector to `c(sigma_C) in {0,q_i}` after rotation normalisation.

### Still open

- equality of support reflection and a boundary-preserving physical source operation;
- the reflection translation value;
- strict separator/defect progress when physical reflection fails;
- source-graph contraction and gluing;
- horizontal induction and the global five-support theorem.
