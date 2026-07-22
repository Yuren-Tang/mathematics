# Connected-cycle flexible switches: Kempe and octahedral antipodal normal forms

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `9831b1f6796c9b58b0f4aedf0d7539b551eceb9e`  
**Parents:**

- `projects/affine-cdc/research/CONNECTED_CYCLE_CORRECTION_RIGIDITY_V1.md`;
- `projects/affine-cdc/research/CONNECTED_KEMPE_CYCLE_ROOT_LIFT_CERTIFICATE_V1.md`;
- `projects/affine-cdc/five-support/gauge-and-reconfiguration.md`;
- `projects/affine-cdc/research/OCTAHEDRAL_OVERLAP_TRANSPORT_V1.md`.

**Status:** exact coefficient/source-cover normal form for every nonzero root-valued correction supported on one connected cycle. A root shift is exactly an ordinary two-support Kempe component switch. A co-root shift is exactly the antipodal involution on one four-support octahedral sector. Together with the rigidity theorem, this gives a complete coefficient-level trichotomy for connected cycles.  
**Not implied:** strict progress from either flexible switch in every four-pole context, compatibility with external side attachments, bounded localisation of a rigid certificate, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Setup

Let

\[
\lambda:E(G)\to R_5
\]

be a root-valued `E5` flow, equivalently an indexed five-support cover

\[
(F_1,\ldots,F_5).
\]

Let

\[
C
\]

be one connected binary cycle. By connected-cycle correction rigidity, every flow correction supported on `C` is

\[
s1_C
\]

for one coefficient

\[
s\in E_5.
\]

Every nonzero element of `E5` is either:

- one of the ten roots;
- one of the five co-roots.

Thus only two flexible switch types can occur.

---

## 2. Root shift is an ordinary support-pair Kempe switch

Let

\[
s=ab=e_a+e_b\in R_5.
\]

### Theorem 2.1 — root-shift admissibility

For a root label

\[
x\in R_5,
\]

one has

\[
x+s\in R_5
\]

if and only if `x` contains exactly one of the support indices `a,b`.

### Proof

If `x=s`, the sum is zero. If `x` contains neither `a` nor `b`, the two roots are disjoint and the sum is a co-root. If `x` contains exactly one of `a,b`, the two roots meet in one support coordinate and their sum is the third root of the corresponding `K5` triangle. A distinct root cannot contain both `a,b`. ∎

### Corollary 2.2 — component characterisation

The shift

\[
\lambda'=\lambda+s1_C
\]

is root-valued if and only if every edge of `C` belongs to exactly one of the two supports

\[
F_a,\ F_b.
\]

Equivalently,

\[
\boxed{C\subseteq F_a\triangle F_b.}
\]

Because `F_a triangle F_b` is an even subgraph and `C` is a connected cycle, one has:

\[
\boxed{
C\text{ is a connected component of }F_a\triangle F_b.}
\]

### Proof

The first statement is Theorem 2.1 translated into support membership. At every vertex of `C`, both cycle edges lie in the even subgraph `F_a triangle F_b`; its degree there is already two, so the third cubic edge does not lie in the symmetric difference. Hence no edge of the same symmetric-difference component leaves `C`. ∎

### Theorem 2.3 — exact Kempe meaning

Adding

\[
s=e_a+e_b
\]

on `C` exchanges the two support memberships `a,b` on every edge of `C` and leaves all other support coordinates unchanged.

Therefore:

\[
\boxed{
\lambda\longmapsto\lambda+s1_C
}
\]

is exactly the ordinary support-pair Kempe switch on the component `C` of

\[
F_a\triangle F_b.
\]

There is no additional root-shift mechanism.

---

## 3. Co-root shift is an octahedral antipodal switch

Fix a support index

\[
i\in[5]
\]

and let

\[
q_i=\mathbf1+e_i
\]

be the co-root supported on

\[
J=[5]\setminus\{i\}.
\]

The six roots avoiding `i` are the six edges of

\[
K_J\cong K_4.
\]

### Theorem 3.1 — co-root-shift admissibility

For a root label `x`,

\[
x+q_i\in R_5
\]

if and only if

\[
i\notin x.
\]

Thus

\[
\lambda'=\lambda+q_i1_C
\]

is root-valued if and only if every cycle label lies in

\[
E(K_J).
\]

### Proof

If `x` avoids `i`, it is a two-subset of the four-set `J`. Adding the all-one vector on `J` replaces that two-subset by its complementary two-subset, again a root. If `x` contains `i`, the sum has weight four. ∎

### Definition 3.2 — opposite root

For

\[
x\in E(K_J),
\]

write

\[
x^{\mathrm{opp}}=J\setminus x.
\]

This is the unique `K4` edge disjoint from `x`.

### Theorem 3.3 — antipodal formula

For every root `x` avoiding `i`,

\[
\boxed{
x+q_i=x^{\mathrm{opp}}.}
\]

Hence the co-root cycle switch acts on the six `K4` roots by the fixed-point-free involution

\[
\boxed{x\longmapsto x^{\mathrm{opp}}.}
\]

### Octahedral interpretation

The line graph

\[
L(K_4)
\]

is the octahedral root graph. Opposite `K4` edges are antipodal octahedral vertices. Therefore translation by `q_i` is the central antipodal involution of the octahedral root set.

The six roots split into the three perfect matchings of `K4`, and the involution exchanges the two roots inside each matching simultaneously.

### Theorem 3.4 — support-cover meaning

On every edge of `C`, the support pair is replaced by its complement inside the four support indices `J`; support `i` remains absent.

Thus the co-root shift is an exact four-support complement switch, not an ordinary two-support Kempe switch.

It is the finite octahedral/DDD complement direction already present in the affine translation and route-lock quotients.

---

## 4. Complete flexible-switch dichotomy

### Theorem 4.1 — no third flexible cycle switch

Let `lambda'` be a root-valued flow agreeing with `lambda` off one connected cycle `C` and differing from it on `C`. Then exactly one of the following holds.

#### Root/Kempe case

There are support indices `a != b` such that

\[
\lambda'=\lambda+(e_a+e_b)1_C,
\]

and `C` is a component of

\[
F_a\triangle F_b.
\]

The move is the ordinary support-pair Kempe switch.

#### Co-root/antipodal case

There is one support index `i` such that

\[
\lambda'=\lambda+q_i1_C,
\]

all cycle labels avoid `i`, and the move replaces each `K4` root by its opposite root.

### Proof

The correction is constant by connected-cycle rigidity. Every nonzero coefficient of `E5` is root or co-root, and Sections 2 and 3 give the two exact normal forms. ∎

---

## 5. Connected-cycle coefficient trichotomy

Combine Theorem 4.1 with the four minimal rigidity geometries from

`CONNECTED_CYCLE_CORRECTION_RIGIDITY_V1.md`.

### Theorem 5.1 — complete connected-cycle coefficient trichotomy

For every connected cycle in a root-valued flow, exactly one of the following holds.

1. **Kempe-flexible:** an ordinary two-support component switch exists;
2. **antipodal-flexible:** a four-support octahedral complement switch exists;
3. **rigid:** no nonzero correction exists, and at most five distinct cycle root labels contain one of
   \[
   K_{1,4},
   \qquad
   K_3\sqcup K_2,
   \qquad
   \text{bull},
   \qquad
   C_5.
   \]

There is no additional coefficient-level connected-cycle mechanism.

---

## 6. Relation to route/profile progress

### Kempe-flexible branch

The switch is already a genuine indexed-cover Kempe operation. Its external boundary traces are unchanged because `C` is closed. Its internal effect may:

- change the route of a scalar component;
- alter side-component incidence;
- reduce a laminar interval;
- expose a profile-changing relative switch after composition.

These are graph-side consequences, not automatic from coefficient admissibility.

### Antipodal-flexible branch

The move simultaneously exchanges the two roots in all three perfect matchings of one `K4` sector. It is therefore the natural cycle-level representative of the flat-complement/DDD sheet-swap direction.

The remaining theorem must decide whether this involution:

- is a removable gauge on a separated region;
- changes the four-pole route profile;
- localises a DDD orientation obstruction;
- or exposes a cyclic separator.

### Rigid branch

The four bounded root-label geometries are the only coefficient obstruction. Their source positions and attachments remain the unbounded datum.

---

## 7. Trust boundary

### Exact here

- every flexible connected-cycle correction is root or co-root;
- a root shift is exactly an ordinary support-pair Kempe component switch;
- a co-root shift is exactly the octahedral antipodal involution on one `K4` root sector;
- the complete flexible-switch dichotomy;
- the combined flexible/rigid coefficient trichotomy.

### Still open

- strict route/profile progress from every flexible switch;
- composition compatibility with a prescribed four-port exterior;
- localisation of the four rigid geometries on bounded source intervals;
- minimal laminar interval replacement and separator extraction;
- strict side-signature descent;
- horizontal/global induction and the global five-support theorem.