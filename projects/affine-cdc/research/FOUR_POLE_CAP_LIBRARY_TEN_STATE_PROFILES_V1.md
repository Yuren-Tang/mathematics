# The dipole--square cap library and its complete ten-state profiles

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `39984983e2189836b14b35ca18ea68d813a56859`  
**Parents:**

- `projects/affine-cdc/research/FOUR_ROOT_INTERFACE_TYPE_T_SQUARE_V1.md`;
- `projects/affine-cdc/five-support/cuts-four-poles-and-routing.md`;
- `projects/affine-cdc/five-support/finite-laboratories-and-certificates.md`.

**Status:** exact state-set computation for the three standard two-vertex caps and the three cyclic orientations of the four-vertex square. A cap of matching `M_i` has complete profile `K_i`; a square whose diagonal matching is `M_i` has complete profile `S\{B_i}`. The six gadgets cover all ten support-unordered boundary states and, at the ordered root level, all `640` conserved four-root boundaries.  
**Not implied:** that one fixed reducer lifts through an arbitrary physical Type-T interval, that every four-pole contains one of these gadgets as a state-set retract, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. The ten-state boundary map

Let the ordered terminals be `1,2,3,4`. A root-valued four-pole flow gives ordered boundary roots

\[
(r_1,r_2,r_3,r_4)\in R_5^4,
\qquad
r_1+r_2+r_3+r_4=0.
\]

For every support coordinate `j`, define the even boundary trace

\[
S_j=\{p\in\{1,2,3,4\}:j\in r_p\}.
\]

The multiset

\[
\{S_1,\ldots,S_5\}
\]

is one of the ten support-unordered states

\[
\mathcal S=\{A,B_i,C_i,D_i:i=0,1,2\}.
\]

For the three matchings `M_i=X_i|Y_i`, put

\[
q_i(S)=|S\cap X_i|\pmod2,
\qquad
\omega_i=\frac12\sum_{j=1}^5q_i(S_j).
\]

The injective coordinate table is

\[
\begin{array}{c|c}
A&(0,0,0)\\
B_0&(0,1,1)\\
B_1&(1,0,1)\\
B_2&(1,1,0)\\
C_0&(0,2,2)\\
C_1&(2,0,2)\\
C_2&(2,2,0)\\
D_0&(2,1,1)\\
D_1&(1,2,1)\\
D_2&(1,1,2).
\end{array}
\]

---

## 2. Standard two-vertex caps

Fix one matching `M_i`. The standard cubic two-vertex cap groups the four boundary semiedges according to the two blocks of `M_i` and has one internal edge.

A boundary root state extends across this cap exactly when the common forced pairing sum is a root.

### Theorem 2.1 — cap profile

\[
\boxed{
\Sigma(\operatorname{cap}_i)
=
\mathcal K_i
=
\{B_j,D_j:j\ne i\}.}
\]

This is the exact cap set from the four-pole forcing theorem.

### Root-level count

For a fixed matching, the cap realises precisely the ordered conserved root quadruples for which the selected route sum has weight two.

---

## 3. The cyclic square

Let `\square` be the cubic four-pole consisting of a four-cycle with one boundary semiedge at each cycle vertex. Fix the cyclic terminal order

\[
1,2,3,4.
\]

Let its diagonal matching be

\[
M_1=13\mid24.
\]

For internal cycle roots

\[
e_1,e_2,e_3,e_4
\]

in cyclic order, the boundary roots are

\[
r_i=e_{i-1}+e_i
\]

with indices modulo four. Root-valuedness requires every adjacent pair `e_{i-1},e_i` to be distinct intersecting roots.

Conversely, for a conserved boundary word, after choosing `e_1=x` the remaining internal labels are forced:

\[
e_2=x+r_2,
\]

\[
e_3=x+r_2+r_3,
\]

\[
e_4=x+r_1.
\]

Thus square extension is an exact ten-choice root test for `x`.

---

## 4. Complete square solvability criterion

### Theorem 4.1

The cyclic square realises every ordered conserved four-root boundary except the states

\[
\boxed{a,b,a,b}
\]

with `a,b` distinct intersecting roots.

Equivalently, among the `640` ordered conserved root quadruples, the square realises exactly `580`.

### Proof by the four-root orbit table

The conserved boundary types are:

1. `a,a,a,a`;
2. `a,a,b,b` with `a,b` intersecting;
3. `a,a,b,b` with `a,b` disjoint;
4. four distinct roots forming a `K5` four-cycle.

For each type the forced-label formula above reduces extension to a finite representative check under `S5` and the dihedral symmetry of the terminal cycle.

- The quadruple-root type extends by an alternating internal pair `x,y` with `x+y=a`.
- Every ordering of a disjoint doubled pair extends by a cross-root construction.
- Every ordering of a four-cycle boundary extends.
- For an intersecting doubled pair, four of the six orderings extend. The two failures are precisely the alternating words `a,b,a,b` and `b,a,b,a`.

For the alternating word, the forced internal sequence would require a root `x` such that both `x+a` and `x+b` are roots and the opposite internal edges satisfy the same adjacency constraints. When `a,b` intersect, the ten possible roots split into the common triangle and the complementary incidences; direct root-intersection inspection excludes all choices. The nonalternating representatives admit explicit choices.

An exact enumeration over the ten roots verifies the orbit check and yields `580` realised ordered states. ∎

---

## 5. Identification of the missing ten-state class

Take a representative alternating adjacent word

\[
a=12,
\qquad
b=13,
\qquad
(a,b,a,b).
\]

Its five boundary support traces are:

\[
\{1,2,3,4\},
\qquad
\{1,3\},
\qquad
\{2,4\},
\qquad
\varnothing,
\qquad
\varnothing.
\]

Therefore its ten-state coordinate is

\[
B_1,
\]

where `M_1=13|24` is the diagonal matching of the square.

Every ordered root representative of `B_1` is one of these alternating adjacent words.

### Theorem 5.1 — square profile

\[
\boxed{
\Sigma(\square_1)
=
\mathcal S\setminus\{B_1\}.}
\]

By permuting the terminal matching labels,

\[
\boxed{
\Sigma(\square_i)
=
\mathcal S\setminus\{B_i\}
\qquad(i=0,1,2).}
\]

This identifies the square with one of the exact six-vertex-census profile types, now with a four-vertex minimal representative.

---

## 6. Complete local cap library

For every `i`, the missing state `B_i` of `\square_i` lies in each of the two cap profiles whose matching is not `M_i`.

More strongly:

### Theorem 6.1 — ten-state coverage

\[
\boxed{
\bigcup_{i=0}^2
\Sigma(\operatorname{cap}_i)
\ \cup\
\bigcup_{i=0}^2
\Sigma(\square_i)
=
\mathcal S.}
\]

Indeed each square alone contains nine of the ten states.

### Theorem 6.2 — ordered-root coverage

Every ordered conserved root quadruple is realised by at least one gadget in the same six-element library.

- If one pairing sum is a root, use the corresponding two-vertex cap.
- If no pairing sum is a root, the boundary is either quadruple-root or a doubled disjoint pair, and the square construction applies.

Thus no fifth local boundary-completion mechanism exists.

---

## 7. Relation to Type T and DDD

The route-sum orbits distribute as follows.

1. `(2,2,4)`: DDD triality — two dipole/root routes and one co-root route.
2. `(0,2,2)`: equality plus two dipole/root routes.
3. `(0,4,4)`: Type-T `abba` — no dipole/root route, but a square root completion.
4. `(0,0,0)`: quadruple equality — no dipole/root route, but a square root completion.

Hence the dipole and square are the exact two graph carriers required by the complete route-sum table.

---

## 8. What this does and does not solve

### Exact gain

The finite four-port boundary problem has no missing local completion state:

\[
\boxed{
\text{all conserved root boundaries}
\longrightarrow
\text{dipole or square}.}
\]

The two gadget profiles are already native to the controlling ten-state interface:

\[
\mathcal K_i,
\qquad
\mathcal S\setminus\{B_i\}.
\]

### Remaining universal-transfer burden

For an inductive replacement of a physical interval `R` by one gadget `K`, the required condition is

\[
\Sigma(K)\subseteq\Sigma(R),
\]

or another theorem guaranteeing that every reduced-graph boundary state lifts through `R`.

The present coverage theorem only states

\[
\forall\sigma\in\mathcal S\ \exists K
\quad
\sigma\in\Sigma(K).
\]

It does **not** interchange these quantifiers.

This is the precise residual distinction between complete local state coverage and a universal reducer.

---

## 9. Revised finite master target

The bounded composition problem may now be stated entirely in the ten-state language.

For every physical bounded zero/DDD/Type-T/return cell `R`, prove one of:

1. `R` contains a cap profile `K_i`;
2. `R` contains a square profile `S\{B_i}`;
3. a route/profile-changing state is realised;
4. the cell exposes a two-, three-, or four-cut;
5. its complete profile is one of the finite residual deterministic kernels and is handled by the DDD orientation switch.

No new boundary state or local graph carrier is required.

---

## 10. Trust boundary

### Exact here

- complete square solvability criterion;
- exact `580/640` ordered-root count;
- identification of the `60` missing states as adjacent alternating words;
- identification of the missing state as `B_i` for the diagonal matching;
- square profile `S\{B_i}`;
- cap profiles `K_i`;
- complete ten-state and ordered-root coverage by three caps and three squares;
- exact quantifier distinction between local coverage and universal state-set inclusion.

### Still open

- proof that every physical Type-T interval contains one square profile;
- proof that every bounded return cell contains a cap or square profile;
- universal state-set inclusion for a chosen graph reducer;
- elimination of the residual deterministic four-pole kernels;
- global well-founded descent and horizontal induction;
- the global five-support theorem.
