# Low-port Tait core gluing and the complete dipole-lift table

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `316661fa4af3aeb72a463c1653e3a763c26423a3`  
**Parents:**

- `projects/affine-cdc/research/NEGATIVE_EULER_TAIT_DIPOLE_REDUCTION_V1.md`;
- `projects/affine-cdc/research/TAIT_FOUR_PORT_RESPONSE_COMPRESSION_V1.md`;
- `projects/affine-cdc/research/RELATIVE_WITNESS_SUBTRACTION_V1.md`;
- `projects/affine-cdc/five-support/cuts-four-poles-and-routing.md`;
- `projects/affine-cdc/five-support/holonomy-defects-and-atoms.md`.

**Status:** exact composition theorem for the low-port contracted cores and exact local lifting table for the inverse of a coloured one-dipole cancellation. Two-port and three-port Tait cores realise every admissible root boundary state up to one global support permutation and therefore glue universally across the corresponding cuts. Re-expanding a cancelled dipole either succeeds uniquely with one root, or localises a zero/equality unit, or localises the existing co-root/DDD atom. Thus the negative-Euler dipole branch has no new lift-failure alphabet.  
**Not implied:** elimination of every finite four-port atom in the locked environment, preservation of bridgelessness for every proposed graph reduction without a separator branch, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Root boundary conservation

Let `P` be a cubic multipole carrying a root-valued flow

\[
\lambda:E(P)\to R_5.
\]

Summing Kirchhoff conservation over all internal vertices cancels every ordinary internal edge and gives

\[
\boxed{
\sum_{e\in\partial P}\lambda(e)=0.}
\]

This elementary boundary law completely determines the admissible two- and three-port root states.

---

## 2. Two ports

Let the two ordered boundary roots be

\[
r_1,r_2\in R_5.
\]

Boundary conservation gives

\[
r_1+r_2=0,
\]

hence

\[
\boxed{r_1=r_2.}
\]

### Theorem 2.1 — universal two-port profile

Suppose one connected two-port multipole has one root-valued flow with boundary state

\[
(s,s).
\]

Then it realises every admissible two-port root boundary state

\[
(r,r),
\qquad r\in R_5,
\]

by one global support permutation.

### Proof

The symmetric group `S_5` acts transitively on the ten roots. Choose a support permutation sending `s` to `r` and apply it to the complete internal root flow. ∎

### Corollary 2.2 — two-cut gluing

Five-support root flows glue across every cyclic two-edge cut.

### Proof

Complete each shore by one new edge joining its two degree-two boundary vertices. In every root-valued cover, that completion edge has one root value. Permute the support names on one shore so that the two completion-edge roots agree. Delete the completion edges and restore the two cut edges, assigning both the common root. The cubic triangle law holds at all four restored endpoints.

If one completion fails to be bridgeless, the failure itself exposes a smaller bridge/separator branch rather than a new boundary state. ∎

---

## 3. Three ports

Let the three boundary roots be

\[
r_1,r_2,r_3\in R_5.
\]

Boundary conservation gives

\[
r_1+r_2+r_3=0.
\]

No two can be equal, since that would force the third to be zero. Three distinct roots sum to zero exactly when they are the three edges of one triangle of `K_5`.

### Theorem 3.1 — universal three-port profile

Every admissible three-port root boundary state is one root triangle, and all root triangles form one `S_5` orbit.

Hence any connected three-port Tait core carrying one fixed boundary triangle realises every admissible three-port state by one global support permutation.

### Corollary 3.2 — three-cut gluing

The existing cyclic three-edge-cut gluing theorem applies directly to every contracted three-port topology core. Internal genus or nonorientability contributes no additional boundary-profile obstruction.

---

## 4. Consequence for contracted negative-Euler cores

The dipole-free theorem leaves only boundary types

\[
(2,0,0)
\qquad\text{and}\qquad
(1,1,1).
\]

Their complete admissible root boundary profiles are universal by Theorems 2.1 and 3.1.

### Theorem 4.1 — low-port topology is compositionally invisible

Let `T` be a connected dipole-free rank-two Tait core attached to the rest of the source graph through two or three boundary edges.

Then the internal triangle-surface topology of `T` does not restrict gluing of five-support root flows beyond the ordinary two-/three-cut boundary law.

### Proof

The core already carries one fixed root-valued Tait flow. Given a root-valued cover of the complementary shore, its two-port state is `(r,r)` or its three-port state is one root triangle. A global support permutation of the fixed core flow aligns its boundary roots with that state. Coordinatewise gluing then gives a root-valued flow on the original graph. ∎

### Corollary 4.2

A negative-Euler contracted core with nonempty boundary is a genuine separator/decomposition certificate, not a new irreducible holonomy atom.

---

## 5. Inverse dipole expansion

Let an `i`-dipole cancellation reconnect one `j`-coloured edge and one `k`-coloured edge in the smaller graph. Suppose a root-valued flow on the smaller graph gives those two edges root values

\[
p,q\in R_5.
\]

To reinsert the two dipole vertices, keep value `p` on the two new `j` segments and value `q` on the two new `k` segments. Kirchhoff conservation at either inserted cubic vertex forces the new `i`-edge value to be

\[
\boxed{r=p+q.}
\]

### Theorem 5.1 — complete dipole-lift table

Exactly one of the following occurs.

1. **Root branch.**  
   `p` and `q` are distinct and meet in one support index. Then
   \[
   r=p+q\in R_5,
   \]
   and the root-valued flow expands uniquely across the original dipole.

2. **Equality branch.**  
   `p=q`. Then
   \[
   r=0.
   \]
   The lift failure is the bounded zero/equality two-vertex unit.

3. **DDD branch.**  
   `p` and `q` are disjoint roots. Then
   \[
   r=p+q
   \]
   is the co-root supported on their four support indices. The lift failure is exactly the known one-co-root-edge/one-factor DDD atom. Its two crossed root-valued resolutions are the two endpoints of the corresponding Petersen edge.

### Proof

The sum of two roots is:

- zero when they are equal;
- the third root of a `K_5` triangle when they meet;
- a weight-four co-root when they are disjoint.

These are the only possibilities. The local geometry of the disjoint case is precisely the established `K_6` one-factor/co-root atom. ∎

### Corollary 5.2 — no new inverse-lift obstruction

Every cover of the dipole-cancelled graph either expands to the original graph or localises one of the already known bounded atoms:

\[
\boxed{
\text{zero/equality}
\quad\text{or}\quad
\text{co-root/DDD}.}
\]

There is no fourth local failure state.

---

## 6. Open-open dipoles and the four-port interface

When the two complementary bicoloured residues of a dipole are both open paths, cancellation flips their four endpoint pairing.

The inverse-lift table applies to the two reconnected root values on this four-port carrier.

### Theorem 6.1 — bounded composition trichotomy

An open-open dipole produces exactly one of:

1. a root-valued expansion preserving the selected incidence;
2. a zero/equality bounded cell;
3. a co-root DDD cell with two crossed root resolutions.

Thus the matching flip is already contained in the finite Type-T/Type-H and DDD four-port alphabet.

---

## 7. Revised negative-Euler closure

Combining coloured dipole reduction with low-port gluing gives:

### Theorem 7.1 — negative-topology composition reduction

Every connected negative-Euler rank-two Tait side multipole with nonempty boundary enters one of:

1. **strict dipole descent:** cancel two source vertices; every smaller-graph cover either expands or yields a bounded zero/DDD atom;
2. **four-port matching flip:** one open-open dipole changes exactly one terminal matching and returns to the finite Type-T/Type-H transfer problem;
3. **two-/three-cut decomposition:** a dipole-free core has universal low-port profile and glues across its separator.

No unbounded negative-genus boundary-composition language remains.

### Remaining burden

What remains is finite and source-categorical:

- ensure the chosen reduction stays in the bridgeless minimal-counterexample category, or record the exposed separator;
- resolve the finite zero/DDD/four-port cells;
- combine the local decreases in one global well-founded complexity.

---

## 8. Trust boundary

### Exact here

- complete two-port and three-port root boundary classification;
- universality under `S_5` support permutations;
- two-cut and three-cut gluing for the contracted Tait cores;
- forced inverse-dipole value `p+q`;
- exact root/equality/DDD lift table;
- reduction of every open-open matching flip to the same bounded atom alphabet;
- elimination of low-port internal topology as a boundary-profile obstruction.

### Still open

- a single theorem packaging bridgelessness preservation or separator extraction for every dipole cancellation;
- elimination of every finite zero/DDD/four-port atom in the locked route environment;
- equality of the flat Möbius orientation bit with the physical `D_8` class;
- a global well-founded descent measure and horizontal induction;
- the global five-support theorem.