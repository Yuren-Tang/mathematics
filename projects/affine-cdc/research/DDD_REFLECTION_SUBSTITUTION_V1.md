# DDD reflection substitution and the four-representative calibration family

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `2422ff16c8ca277585b7c695521027ad263552b4`  
**Parents:**

- `projects/affine-cdc/research/DDD_DIHEDRAL_REFLECTION_CLASS_V1.md`;
- `projects/affine-cdc/research/PETERSEN_FIVE_CYCLE_REFLECTION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_STAR_REFLECTION_V1.md`;
- `projects/affine-cdc/research/SIX_OUTPUT_RETURN_CELL_NORMAL_FORM_V1.md`.

**Status:** exact coefficient/cohomology theorem showing that every reflection in one DDD stabiliser is interchangeable after rotation normalisation. The physical calibration may use either star reflection or either five-cycle reversal axis. Simultaneous failure of all bounded representatives remains a graph-side composition problem.  
**Not implied:** physical reflection realisability, source-graph replacement, canonical acceptance, Lean verification, or the global five-support theorem.

---

## 1. Dihedral calibration setting

Fix one DDD/Petersen-edge state

\[
F=\{\infty i,X,Y\},
\]

and put

\[
D=\operatorname{Stab}_{S_5}(F)\cong D_8.
\]

Choose an order-four rotation

\[
\rho\in D,
\qquad
R=\langle\rho\rangle\cong C_4,
\]

and one reflection

\[
\sigma\in D\setminus R.
\]

Then

\[
D=R\sqcup R\sigma,
\]

and every reflection is uniquely of the form

\[
\rho^k\sigma,
\qquad k\in\mathbf Z/4.
\]

The reflection-support theorem gives

\[
H^1(D,E_5)\cong\mathbf F_2,
\qquad
H^1(R,E_5)=0,
\qquad
E_5^R=\langle q_i\rangle.
\]

---

## 2. Reflection-value constancy

Let

\[
c:D\to E_5
\]

be a one-cocycle. Since `H^1(R,E5)=0`, change affine origin so that

\[
\boxed{c(\rho)=0.}
\]

Then the cocycle vanishes on every rotation:

\[
c(\rho^k)=0.
\]

### Theorem 2.1 — reflection substitution

For every reflection `tau in D\R`,

\[
\boxed{c(\tau)=c(\sigma)\in\{0,q_i\}.}
\]

Thus all four reflections carry the same normalised affine detector.

### Proof

Write

\[
\tau=\rho^k\sigma.
\]

The cocycle identity gives

\[
c(\tau)
=c(\rho^k)+\rho^k c(\sigma)
=\rho^k c(\sigma).
\]

After rotation normalisation the reflection-support theorem gives

\[
c(\sigma)\in E_5^R=\langle q_i\rangle.
\]

Hence `rho^k` fixes `c(sigma)`, so

\[
c(\tau)=c(\sigma).
\]

The two possibilities are `0` and `q_i`, representing respectively the trivial and nontrivial classes in `H^1(D,E5)`. ∎

### Corollary 2.2 — source-adaptive calibration

To determine the physical DDD affine class it is enough to realise **any one** reflection of the stabiliser with boundary-compatible source semantics. No preferred reflection is required.

---

## 3. The four bounded representatives

Fix a based Petersen five-cycle with invariant DDD state `F`.

The preceding dossiers supply two geometrically different reflection constructions.

### 3.1 Star reflections

The two endpoints `X,Y` of the Petersen edge state `F` give two constant-pivot star triangles in `L(P)`.

Their monodromies are two single-transposition reflections

\[
\sigma_X,
\qquad
\sigma_Y.
\]

Each is represented by a three-turn rank-two root loop.

### 3.2 Cycle-axis reflections

The based five-cycle has one reversal reflection fixing the base switch edge setwise. Applying the central half-turn `rho^2` gives the opposite reversal axis.

These are two double-transposition reflections

\[
\sigma_C,
\qquad
\rho^2\sigma_C.
\]

Each is represented at support level by a reversal comparison of the bounded five-cycle core.

### Theorem 3.1 — complete bounded reflection family

The four bounded constructions above are exactly the four reflections of `D`:

\[
\boxed{
D\setminus R
=
\{\sigma_X,\sigma_Y,\sigma_C,\rho^2\sigma_C\}.
}
\]

Two are single transpositions and two are double transpositions in `S5`.

### Representative certificate

For

\[
F=\{\infty5,12,34\},
\qquad
\rho=(1\ 4\ 2\ 3),
\]

take

\[
\sigma_X=(3\ 4),
\qquad
\sigma_Y=(1\ 2),
\qquad
\sigma_C=(1\ 4)(2\ 3).
\]

Then

\[
\boxed{
\sigma_C=\rho\sigma_X=\sigma_X\rho^{-1},
}
\]

and

\[
\sigma_Y=\rho^2\sigma_X.
\]

The fourth reflection is

\[
\rho^3\sigma_X.
\]

Exact Wolfram enumeration verifies the four-element reflection coset and its split into two cycle types

\[
2\,1^3,
\qquad
2^2\,1.
\]

---

## 4. Equality of star and cycle detectors

### Theorem 4.1 — star/cycle detector equality

Assume the rotation core and one star reflection or cycle reflection are physically realised with compatible boundary semantics. After normalising `c(rho)=0`,

\[
\boxed{
 c(\sigma_X)
 =c(\sigma_Y)
 =c(\sigma_C)
 =c(\rho^2\sigma_C)
 \in\{0,q_i\}.
}
\]

Therefore:

- a physically convenient star triangle may replace the canonical five-cycle reversal comparison;
- a boundary-compatible five-cycle reversal may replace a star triangle whose side attachments are inconvenient;
- the affine answer is independent of that choice.

This is an exact cohomological substitution theorem, not merely a symmetry heuristic.

---

## 5. Revised physical target

The old target asked for one particular reflected comparison. The correct source-side target is choice-based.

### Target 5.1 — one-of-four reflection realisation

For a bounded odd DDD five-cycle core, prove one of:

1. **reflection realised:** at least one of the four bounded reflection representatives preserves the required four-port boundary semantics; its normalised translation is `0` or `q_i`;
2. **profile escape:** a failed representative changes the route pairing or leaves the locked profile;
3. **root-fibre failure:** a failed representative produces an empty edge fibre or empty cubic relation;
4. **separator:** the discrepancy between original and reflected semantics factors through a smaller cyclic cut or four-pole;
5. **bounded defect:** the discrepancy localises to one zero/co-root/DDD atom.

### Target 5.2 — four-failure synthesis

If none of the four representatives is physically realisable, combine their four bounded failure certificates into one strict source obstruction.

The numerical coincidence is potentially structural:

- there are four reflections in the DDD stabiliser;
- a minimal laminar interval has at most four ordered route ports;
- a maximal minimal six-channel blocker has four fundamental-bond certificates.

No identification among these three four-element systems is asserted here. The next composition theorem should test whether the four reflection failures are the physical port/channel coordinates already isolated elsewhere.

---

## 6. Interaction with the six-output return cell

Inside a six-output same-component return cell, the only cyclic reduced pivot core is one Petersen five-cycle. Its rotation is therefore fixed up to `S5` equivalence.

The present theorem says that the reflection half of its affine calibration is not tied to one additional large comparison. It may be supplied by:

- either of the two three-turn star loops based at the invariant DDD state;
- either of the two reversal axes of the five-cycle.

Consequently the complete odd-core calibration family remains bounded by five coefficient turns, with the star alternatives using only three turns.

The remaining unbounded objects are only the named outside components attached to those bounded turns. No additional coefficient state or holonomy type is needed.

---

## 7. Wolfram certificate

An exact mod-two linear calculation for the representative stabiliser gives:

\[
\dim Z^1(D,E_5)=4,
\qquad
\dim B^1(D,E_5)=3,
\qquad
\dim H^1(D,E_5)=1.
\]

For the rotation subgroup:

\[
\dim H^1(\langle\rho\rangle,E_5)=0.
\]

After imposing `c(rho)=0`, the only possible reflection values are

\[
0,
\qquad
q_5=11110
\]

in the representative with omitted support `5`.

The exact permutation calculation gives

\[
\sigma_C=\rho\sigma_X,
\]

and enumerates four reflections with cycle types

\[
2\,1^3,
\quad
2^2\,1,
\quad
2\,1^3,
\quad
2^2\,1.
\]

These computations independently verify the algebraic proofs above; they are not used as hidden substitutes for them.

---

## 8. Trust boundary

### Exact here

- every DDD reflection is `rho^k sigma`;
- after rotation normalisation all four reflection cocycle values coincide;
- the common value is `0` or `q_i`;
- the two star triangles and two five-cycle axes exhaust the reflection coset;
- equality of star and cycle affine detectors;
- reduction of physical calibration to a one-of-four bounded choice.

### Still open

- physical boundary-preserving realisation of any reflection representative in every odd return cell;
- synthesis of four failed realisations into a strict separator/defect theorem;
- identification of the four reflection attempts with four route-port or `K_(2,3)` channel coordinates;
- source-graph contraction and gluing;
- horizontal induction and the global five-support theorem.
