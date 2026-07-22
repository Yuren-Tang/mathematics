# Petersen identity hexagons and the singular fibres of the quadratic channel projection

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `72aa8a52e74d8a1cc917801726d5b13b5ad0390a`  
**Parents:**

- `projects/affine-cdc/research/PETERSEN_IDENTITY_HEXAGON_SIX_CHANNEL_TRIALITY_V1.md`;
- `projects/affine-cdc/research/PETERSEN_IDENTITY_HEXAGON_HALF_TURN_MATCHING_PLANE_V1.md`;
- `projects/affine-cdc/research/QUADRATIC_CHANNEL_PROJECTION_V1.md`.

**Status:** exact finite/quadratic classification. The three antipodal matching planes of the identity hexagon attached to a root `r` are precisely the three planes through the four singular fibres of the quadratic channel projection `Psi_r`. Their simultaneous compatibility pattern gives a `2+6+8` decision theorem: zero/root, unique DDD root–co-root fibre, or transverse singleton profile.

**Not implied:** physical calibration of a source-side channel word with `Psi_r`, admissible route surgery, strict descent, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. The three split planes

Fix a root

\[
r=uv\in R_5
\]

and write the complementary support set as

\[
W=\{x,y,z\}.
\]

The three roots disjoint from `r` are

\[
d_1=xy,\qquad d_2=xz,\qquad d_3=yz,
\]

with

\[
d_1+d_2+d_3=0.
\]

The identity hexagon `C_r` has three antipodal half splits. By the six-channel triality theorem, their common half monodromies are exactly `d1,d2,d3`.

For each split define the matching plane

\[
M_j=\langle r,d_j\rangle
=\{0,r,d_j,r+d_j\}.
\]

Each `M_j` is Lagrangian for the polar form `b` on `E5`.

### Theorem 1.1 — plane arrangement

\[
\boxed{
M_1\cap M_2
=M_1\cap M_3
=M_2\cap M_3
=\langle r\rangle
=\{0,r\}.}
\]

Moreover

\[
\boxed{
M_1\cup M_2\cup M_3=r^\perp.}
\]

### Proof

The classes of `d1,d2,d3` are the three nonzero elements of the two-dimensional quotient

\[
r^\perp/\langle r\rangle.
\]

Thus the three planes are the inverse images of the three one-dimensional subspaces of that quotient. Distinct inverse-image lines meet exactly in the kernel `<r>`, and their union is the full preimage `r^perp`. ∎

### Exact finite certificate

For a representative `r=12`, direct enumeration gives:

- pairwise intersection size `2`;
- union equal to `r^perp`;
- two elements contained in all three planes;
- six elements contained in exactly one plane;
- eight elements contained in no plane.

By `S5` equivariance this holds for every root.

---

## 2. Quadratic channel projection

Recall

\[
q(x)=|x|/2\pmod2
\]

on `E5`, and define

\[
\Psi_r(x)=x+q(x)r.
\]

The quadratic-channel theorem identifies the unsafe six-channel profile of `x` with the cut potential `Psi_r(x)`.

### Theorem 2.1 — complete fibre criterion

If

\[
\Psi_r(x)=\Psi_r(y),
\]

then either

\[
y=x
\]

or

\[
y=x+r
\quad\text{and}\quad
b(x,r)=0.
\]

Consequently:

1. `Psi_r` is injective on `E5 \ r^perp`;
2. every point of `r^perp` belongs to a two-element fibre parallel to `<r>`.

### Proof

Equality gives

\[
y=x+\epsilon r,
\qquad
\epsilon=q(x)+q(y).
\]

If `epsilon=0`, then `x=y`. If `epsilon=1`, then `y=x+r`. Polarisation gives

\[
q(x+r)=q(x)+q(r)+b(x,r)
=q(x)+1+b(x,r).
\]

For `q(x)+q(y)=1` one must have `b(x,r)=0`. Conversely, if `b(x,r)=0`, then

\[
\Psi_r(x+r)=\Psi_r(x).
\]

This proves both statements. ∎

---

## 3. The four singular fibres

The four cosets of `<r>` in `r^perp` are

\[
\langle r\rangle,
\qquad
d_1+\langle r\rangle,
\qquad
d_2+\langle r\rangle,
\qquad
d_3+\langle r\rangle.
\]

### Theorem 3.1 — exact singular-fibre list

The non-singleton fibres of `Psi_r` are exactly

\[
\boxed{
\Psi_r^{-1}(0)=\{0,r\},}
\]

and

\[
\boxed{
\Psi_r^{-1}(d_j+r)=\{d_j,d_j+r\}
\qquad(j=1,2,3).}
\]

All eight points outside `r^perp` have singleton fibres.

### Proof

For `0` and `r`, the formula is immediate. Each disjoint root `d_j` satisfies

\[
q(d_j)=1,
\qquad
q(d_j+r)=0,
\]

so both map to `d_j+r`. Theorem 2.1 shows that there are no other non-singleton fibres. ∎

### Corollary 3.2 — matching planes are singular-fibre planes

Each split plane is the union of the base zero/equality fibre and one DDD root–co-root fibre:

\[
\boxed{
M_j
=
\{0,r\}
\sqcup
\{d_j,d_j+r\}.}
\]

Thus the three antipodal splits of the identity hexagon geometrically package all four singular fibres of `Psi_r`:

- one common zero/root fibre;
- three root/co-root DDD fibres.

This is exactly the singular-fibre classification previously obtained by direct analysis of the quadratic projection.

---

## 4. Three-split compatibility theorem

Let

\[
\Delta\in E_5
\]

be any candidate total displacement of the physical identity return `C_r`. For each antipodal split `j`, let

\[
\omega_j(\Delta)=0
\quad\Longleftrightarrow\quad
\Delta\in M_j.
\]

Equivalently, `omega_j` is zero exactly when the split quotient defect in `E5/M_j` vanishes.

### Theorem 4.1 — `2+6+8` decision theorem

Exactly one of the following occurs.

#### Type Z — common zero/root fibre

All three split quotient defects vanish:

\[
\omega_1(\Delta)=\omega_2(\Delta)=\omega_3(\Delta)=0.
\]

Then

\[
\boxed{\Delta\in\{0,r\}.}
\]

There are two such displacements.

#### Type D — unique DDD singular fibre

Exactly one split quotient defect vanishes. For a unique `j`,

\[
\Delta\in M_j\setminus\langle r\rangle,
\]

and therefore

\[
\boxed{\Delta\in\{d_j,d_j+r\}.}
\]

There are six such displacements, arranged in three root/co-root pairs.

#### Type X — transverse singleton profile

No split quotient defect vanishes:

\[
\Delta\notin M_1\cup M_2\cup M_3.
\]

Then

\[
\boxed{b(\Delta,r)=1,}
\]

so

\[
\Delta\notin r^\perp.
\]

The quadratic projection `Psi_r` is injective at `Delta`; its six-channel cut profile uniquely determines `Delta`. There are eight such displacements.

There is no pattern with exactly two vanishing split defects.

### Proof

By Theorem 1.1, the common intersection of any two planes is `<r>` and then lies in all three planes. Their union is `r^perp`. The three cases are therefore respectively:

\[
\langle r\rangle,
\qquad
r^\perp\setminus\langle r\rangle,
\qquad
E_5\setminus r^\perp.
\]

Their sizes are `2,6,8`. The explicit fibre statements follow from Theorem 3.1 and injectivity from Theorem 2.1. ∎

---

## 5. Interpretation for the identity sector

The three-split theorem removes the last apparent finite ambiguity of the identity hexagon.

### Type Z

The return is already zero/root-valued:

\[
\Delta=0\quad\text{or}\quad\Delta=r.
\]

This belongs to the equality-wire/root branch.

### Type D

A unique antipodal split is compatible. The return lies in one exact quadratic double fibre

\[
\{d_j,d_j+r\}.
\]

This is precisely the root/co-root ambiguity already isolated in the DDD channel projection. No new finite state occurs.

### Type X

Every split detects a quotient defect. The displacement is transverse to the active root and has a singleton quadratic profile. Therefore any physical channel-profile calibration cannot hide it inside a root/co-root double fibre: it is completely visible in the six-channel cut data.

The finite algebra has therefore reduced identity returns to:

\[
\boxed{
\text{zero/root}
\quad\sqcup\quad
\text{one DDD double fibre}
\quad\sqcup\quad
\text{one uniquely visible transverse profile}.}
\]

---

## 6. Revised physical composition target

The remaining graph theorem can now be stated sharply.

Construct the actual six-channel side profile of a physical identity return and calibrate it with the quadratic cut profile determined by `Psi_r(Delta)`. Then prove:

1. **Type Z:** zero/root displacement gives a gauge, equality-wire, serial reduction, or root-supported route transition;
2. **Type D:** the unique compatible split localises the corresponding DDD root/co-root fibre to a crossed route, bounded blossom, common cut, or defect unit;
3. **Type X:** singleton-profile visibility forces a profile/Kempe escape, a smaller separator, or a strict serial/four-pole reduction.

The finite problem is closed: there is no unclassified identity-return displacement. The remaining obstruction is exactly the physical calibration and strict-progress theorem.