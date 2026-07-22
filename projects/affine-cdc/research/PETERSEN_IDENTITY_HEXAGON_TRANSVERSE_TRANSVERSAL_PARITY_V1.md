# Petersen identity hexagons: transverse profiles as oriented channel transversals

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `78be97af2dbdf7aa22139fceb4dcdb484ac9d892`  
**Parents:**

- `projects/affine-cdc/research/PETERSEN_IDENTITY_HEXAGON_QUADRATIC_SINGULAR_FIBRES_V1.md`;
- `projects/affine-cdc/research/QUADRATIC_CHANNEL_PROJECTION_V1.md`;
- `projects/affine-cdc/research/DDD_ROUTE_ORIENTATION_COVER_V1.md`.

**Status:** exact finite/quadratic classification of the transverse identity-return branch. Its eight singleton quadratic profiles are exactly the eight transversals choosing one channel from each of the three resolution pairs. After orienting the active root, they carry one explicit parity bit, identical to the index-two oriented-route transversal parity.

**Not implied:** physical calibration of the coefficient cut with actual route choices, Type-T/Type-H closure, strict descent, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Ordered active root and resolution pairs

Fix an ordered active root

\[
r=uv
\]

and put

\[
W=[5]\setminus\{u,v\}=\{x,y,z\}.
\]

The six repair channels are

\[
S_r=\{uw,vw:w\in W\}.
\]

For each `w in W`, the two channels

\[
P_w=\{uw,vw\}
\]

form one oriented resolution pair. The unordered three-class system is canonical; choosing the order `u,v` chooses which member of each pair is called the `u`- or `v`-orientation.

Let

\[
\Delta\in E_5
\]

be a Type-X identity displacement, so

\[
b(\Delta,r)=1.
\]

Define its quadratic potential

\[
p=\Psi_r(\Delta)=\Delta+q(\Delta)r
\]

and its six-channel cut profile

\[
U_r(\Delta)=\delta p.
\]

---

## 2. Transversal theorem

For a channel edge `ij in S_r`, membership in the cut is

\[
1_{ij\in\delta p}=p_i+p_j.
\]

### Lemma 2.1 — endpoint parity

For `r=uv`,

\[
\boxed{b(\Delta,r)=\Delta_u+\Delta_v.}
\]

Since `p` differs from `Delta` by a multiple of `r`,

\[
\boxed{p_u+p_v=\Delta_u+\Delta_v=b(\Delta,r)=1.}
\]

### Theorem 2.2 — one channel from every resolution pair

For every `w in W`,

\[
\boxed{
|U_r(\Delta)\cap P_w|=1.}
\]

Hence `U_r(Delta)` is a three-edge transversal of the three resolution pairs.

### Proof

The two membership bits satisfy

\[
(p_u+p_w)+(p_v+p_w)=p_u+p_v=1.
\]

Therefore exactly one of `uw,vw` lies in the cut. ∎

### Theorem 2.3 — all eight transversals occur uniquely

The map

\[
\boxed{
\Delta\longmapsto U_r(\Delta)
}
\]

is a bijection from the eight Type-X displacements

\[
E_5\setminus r^\perp
\]

onto the eight transversals of the three pairs `P_x,P_y,P_z`.

### Proof

There are eight Type-X displacements and eight transversals. The quadratic singular-fibre theorem shows that `Psi_r` is injective on `E5 \ r^perp`, and the cut map has a unique even potential on the connected graph `K_(2,3)`. Thus distinct Type-X displacements give distinct transversals. Theorem 2.2 gives inclusion, so cardinality gives bijectivity. ∎

### Exact finite certificate

For a representative `r=12`, enumeration verifies:

- eight Type-X displacements;
- every cut has size three;
- every cut contains exactly one channel from each pair;
- all eight transversals are distinct.

---

## 3. Orientation word and parity

For `w in W`, define

\[
\epsilon_w(\Delta)
=
1_{vw\in U_r(\Delta)}.
\]

Thus

\[
\epsilon(\Delta)
=(\epsilon_x,\epsilon_y,\epsilon_z)
\in\mathbf F_2^3
\]

is the oriented transversal word.

Because exactly one channel in each pair is chosen,

\[
\epsilon_w
=1+p_u+p_w.
\]

### Theorem 3.1 — exact transversal parity

Define

\[
\vartheta_r(\Delta)
=\epsilon_x+\epsilon_y+\epsilon_z.
\]

Then

\[
\boxed{
\vartheta_r(\Delta)=p_u=\Delta_u+q(\Delta).}
\]

### Proof

Summing the three orientation bits gives

\[
\sum_{w\in W}\epsilon_w
=1+p_u+\sum_{w\in W}p_w.
\]

Since `p in E5`,

\[
p_u+p_v+\sum_{w\in W}p_w=0.
\]

Type X gives `p_u+p_v=1`, hence

\[
\sum_{w\in W}p_w=1.
\]

Therefore the orientation parity is `p_u`. Finally

\[
p_u=\Delta_u+q(\Delta).
\]

∎

### Corollary 3.2 — balanced parity split

Exactly four Type-X profiles have

\[
\vartheta_r=0,
\]

and exactly four have

\[
\vartheta_r=1.
\]

### Corollary 3.3 — reversal of the active-root orientation

Swapping `u` and `v` replaces every orientation bit by its complement:

\[
\epsilon\longmapsto\epsilon+111,
\]

and therefore

\[
\vartheta_r\longmapsto\vartheta_r+1.
\]

Thus the parity is naturally attached to an oriented active root; for an unordered root it is a two-point torsor rather than an absolute bit.

---

## 4. Identification with the index-two route transversal parity

The three resolution pairs `P_x,P_y,P_z` have the same abstract structure as the three pairs of opposite edges of `K4`. A transversal chooses one member of each pair, so the eight oriented channel transversals form

\[
\mathbf F_2^3.
\]

Under any orientation-preserving identification with the opposite-edge pairs of `K4`, the eight transversals split into:

- four triangle transversals;
- four star transversals.

The quotient map in the oriented-route exact sequence

\[
1\longrightarrow S_4
\longrightarrow C_2^3\rtimes S_3
\xrightarrow{\epsilon_1+\epsilon_2+\epsilon_3}
C_2
\longrightarrow1
\]

is exactly the parity

\[
\boxed{\vartheta_r.}
\]

Which parity value is called `triangle` or `star` depends on the initial orientation convention, but the index-two partition is canonical.

### Consequence 4.1

The Type-X identity branch does not carry eight unrelated singleton obstructions. It carries:

1. one explicit oriented resolution transversal;
2. one residual index-two triangle/star class.

This is the same binary obstruction already isolated in the oriented route-lifting problem.

---

## 5. Refined identity-return trichotomy

Combining the singular-fibre and transversal theorems gives:

### Type Z

\[
\Delta\in\{0,r\}.
\]

Zero/root equality-wire branch.

### Type D

\[
\Delta\in\{d_j,d_j+r\}
\]

for one unique disjoint root `d_j`. One DDD root/co-root singular fibre.

### Type X

\[
b(\Delta,r)=1.
\]

The six-channel profile is one of the eight oriented transversals, and its only orbit-level residual datum is

\[
\vartheta_r(\Delta)\in C_2.
\]

Thus the complete finite identity-return alphabet is now:

\[
\boxed{
\text{zero/root}
\quad\sqcup\quad
\text{DDD root–co-root fibre}
\quad\sqcup\quad
\text{oriented transversal with one parity bit}.}
\]

---

## 6. Revised physical target

The transverse branch now requires one concrete source theorem.

Construct the actual three resolution-pair choices induced by the physical six-channel side attachments and prove that they agree with the quadratic cut transversal `U_r(Delta)`. Then:

1. parity-preserving local identifications should lie in the `S4` route-lifting image and yield an admissible route transition, serial reduction, or smaller separator;
2. parity-reversing identification carries the unique index-two exceptional class and should localise to a Type-H/DDD blossom, common cut, or defect unit.

The statement above is still a physical lifting target, not yet a theorem. What is exact is that no additional Type-X finite invariant remains beyond the transversal and its single orientation parity.