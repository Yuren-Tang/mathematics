# Petersen star triangles as the minimal DDD reflection loops

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `d2cce501ba1f800347795ef33351034399c76376`  
**Parents:**

- `projects/affine-cdc/research/PETERSEN_PIVOT_RESOLUTION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_CYCLE_MONODROMY_V1.md`;
- `projects/affine-cdc/research/DDD_DIHEDRAL_REFLECTION_CLASS_V1.md`;
- `projects/affine-cdc/research/PETERSEN_FIVE_CYCLE_REFLECTION_V1.md`.

**Status:** exact minimal support/coefficient reflection theorem. Every DDD state has a three-turn constant-pivot star loop whose monodromy is a reflection in its `D8` stabiliser and whose coefficient word has a unique rank-two root resolution. Physical side-semantic realisability remains open.  
**Not implied:** graph-side contraction, affine reflection value, canonical acceptance, Lean verification, or the global five-support theorem.

---

## 1. Base DDD state

Let

\[
P=KG(5,2)
\]

be the Petersen graph. Fix one DDD/Petersen-edge state

\[
F_0=\{s,t\}\in E(P),
\]

where the disjoint roots `s,t` omit one support index

\[
i=[5]\setminus(s\cup t).
\]

The associated `K6` one-factor is

\[
\{\infty i,s,t\}.
\]

Its support stabiliser is

\[
D=\operatorname{Stab}_{S_5}(F_0)\cong D_8.
\]

---

## 2. The star clique at one pivot

Fix the pivot endpoint `s`. Its three Petersen neighbours are exactly the three roots on the complementary three-set

\[
Q=[5]\setminus s.
\]

Write

\[
Q=\{a,b,c\},
\]

and choose the notation

\[
t=bc,
\qquad
u=ca,
\qquad
v=ab.
\]

The three Petersen edges incident with `s` are

\[
F_0=\{s,bc\},
\qquad
F_1=\{s,ca\},
\qquad
F_2=\{s,ab\}.
\]

They form one triangle in the line graph `L(P)`.

### Definition 2.1 — star triangle

The closed state walk

\[
\boxed{
F_0\longrightarrow F_1\longrightarrow F_2\longrightarrow F_0
}
\]

is the **star triangle at pivot `s` based at `F_0`**.

Every transition has the same pivot `s`, so this is one constant-pivot run.

---

## 3. Emitted root word and unique resolution

The transition

\[
\{s,x\}\to\{s,y\}
\]

emits the third Petersen neighbour of `s` distinct from `x,y`.

Therefore the three transitions of the star triangle emit, in order,

\[
\boxed{ab,\ bc,\ ca}
\]

up to cyclic orientation.

These are the three roots of the triangle on `Q`, and

\[
ab+bc+ca=0.
\]

### Theorem 3.1 — closed rank-two resolution

The star triangle has the unique simultaneous root resolution

\[
\boxed{bc,\ ca,\ ab}
\]

at its three Petersen-edge states.

All chosen state resolutions and all emitted side roots lie in the binary plane

\[
W_s=\{0,ab,bc,ca\}\cong\mathbf F_2^2.
\]

Hence the complete coefficient loop is a closed rank-two/Tait loop.

### Proof

The constant-pivot criterion gives the unique resolution obtained by choosing, at each state `{s,x}`, the nonpivot endpoint `x`. The local root-triangle theorem verifies every turn. ∎

---

## 4. Support monodromy of the star triangle

The omitted index of state `{s,bc}` is `a`; that of `{s,ca}` is `b`; that of `{s,ab}` is `c`.

Thus the omitted-index word is

\[
a,b,c,a.
\]

The support transport around the triangle is

\[
\sigma_s
=
(c\ a)(b\ c)(a\ b),
\]

with the opposite multiplication convention giving the same transposition up to orientation.

### Theorem 4.1 — star reflection

\[
\boxed{
\sigma_s=(b\ c).
}
\]

In particular:

- `sigma_s` fixes the two support indices of `s`;
- it fixes the omitted index `a=i`;
- it fixes the root `t=bc` setwise;
- it fixes both endpoints `s,t` of the base DDD state separately.

Therefore

\[
\boxed{
\sigma_s\in D\setminus\langle\rho\rangle
}
\]

for every order-four rotation `rho` of `D`, and `sigma_s` is a reflection of the DDD stabiliser.

### Proof

A direct product in `S_Q` gives `(ca)(bc)(ab)=(bc)` in the displayed naming. The fixed-set statements are immediate. The rotation subgroup of `D8` contains only identity, the central double transposition, and the two order-four elements, so a single transposition in `D` is a reflection. ∎

---

## 5. Minimality

A nontrivial reflection monodromy cannot occur on a one- or two-transition closed state walk:

- one transition cannot return to the initial state;
- two transitions form a backtrack, whose support product is identity.

### Corollary 5.1 — minimal reflection length

The three-turn star triangle is a shortest closed `L(P)` walk with reflection monodromy in the stabiliser of its base DDD state.

It is therefore the canonical minimal reflection calibration object.

---

## 6. Representative certificate

Take

\[
s=12,
\qquad
Q=\{3,4,5\},
\qquad
F_0=\{12,34\}.
\]

Use the star triangle

\[
\{12,34\}
\to
\{12,35\}
\to
\{12,45\}
\to
\{12,34\}.
\]

The omitted-index word is

\[
5,4,3,5,
\]

and the support monodromy is

\[
\boxed{\sigma_s=(3\ 4).}
\]

The emitted side-root word is

\[
45,34,35
\]

up to cyclic order, and the unique state resolution is

\[
34,35,45.
\]

For the representative five-cycle rotation

\[
\rho=(1\ 4\ 2\ 3),
\]

one checks

\[
\sigma_s\rho\sigma_s=\rho^{-1}.
\]

Thus

\[
\langle\rho,(34)\rangle
=
\operatorname{Stab}_{S_5}(\{\infty5,12,34\})
\cong D_8.
\]

---

## 7. Affine detector

Let `rho` be the five-cycle rotation based at `F_0`, and let `sigma_s` be the star reflection.

After changing affine origin so that

\[
c(\rho)=0,
\]

the reflection-support theorem gives

\[
\boxed{
c(\sigma_s)\in\{0,q_i\}.}
\]

The two values distinguish the trivial and nontrivial physical `D8` affine classes.

Thus the smallest complete coefficient-side calibration pair is:

\[
\boxed{
\text{one Petersen five-cycle rotation}
+
\text{one three-turn star reflection}.
}
\]

The five-cycle reversal symmetry remains an exact abstract reflection, but it is not the minimal reflection object and is unnecessary for coefficient-level generation of `D8`.

---

## 8. What remains physical

The star triangle is uniquely root-resolvable at coefficient level, but its emitted root edges enter the original source graph. Root resolution alone does not permit deletion or guarantee that the three physical side components close compatibly.

### Target 8.1 — physical star-reflection trichotomy

For the three-turn star loop, prove one of:

1. **reflection realised:** the rank-two resolution and side attachments define a boundary-preserving physical loop with monodromy `sigma_s`; then compute `c(sigma_s)=0` or `q_i`;
2. **Tait/profile escape:** the rank-two resolution changes the four-terminal route or exits the locked profile;
3. **localised failure:** incompatible side attachments yield an empty fibre, empty relation, smaller separator/four-pole, or bounded DDD/defect atom.

Because the loop has only three turns, this is strictly smaller than the six-output return-cell transfer problem.

---

## 9. Strategic consequence

The reflection half of the DDD affine problem is no longer an unspecified group element or an external symmetry comparison.

It is one explicit local object:

\[
\boxed{
\text{constant-pivot triangle in }L(P)
\quad\leftrightarrow\quad
\text{rank-two root loop with reflection monodromy}.
}
\]

The next physical theorem can focus entirely on the three emitted side roots of this loop.

---

## 10. Trust boundary

### Exact here

- the star triangle at every pivot/base state;
- its emitted root-triangle word;
- its unique constant-pivot rank-two resolution;
- its transposition support monodromy;
- membership as a reflection in the base DDD stabiliser;
- minimality among closed reflection walks;
- generation of `D8` with the five-cycle rotation;
- reduction of the affine detector to the star-reflection value `0` or `q_i`.

### Still open

- source-graph realisation of the star reflection with fixed four-port semantics;
- its affine translation value;
- Tait/profile escape or separator extraction on failure;
- source-graph contraction and gluing;
- horizontal induction and the global five-support theorem.
