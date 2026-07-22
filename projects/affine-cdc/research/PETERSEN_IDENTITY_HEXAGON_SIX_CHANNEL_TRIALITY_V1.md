# Petersen identity hexagons as six-channel triality carriers

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `be8e7a3ebaae8f04854a53c6fc0e5c2de4b25dac`  
**Parents:**

- `projects/affine-cdc/research/PETERSEN_IDENTITY_HEXAGON_HALF_TURN_MATCHING_PLANE_V1.md`;
- `projects/affine-cdc/research/PETERSEN_IDENTITY_HEXAGON_HALF_DISCREPANCY_V1.md`;
- `projects/affine-cdc/research/QUADRATIC_CHANNEL_PROJECTION_V1.md`;
- `projects/affine-cdc/research/DDD_COHOMOLOGY_GENERATOR_V1.md`.

**Status:** exact finite/support identification. The ten Petersen identity hexagons are precisely the ten six-channel carriers attached to the ten roots. Their three antipodal half splits are exactly the three nonzero `K_{2,3}` channel-cohomology classes, and every half-turn quotient defect has the canonical DDD triality code `000,011,101,110`.

**Not implied:** physical side-attachment functoriality, admissible route surgery, strict Type-T descent, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Root channel graph

Let

\[
E_5=\{x\in\mathbf F_2^5:\sum_i x_i=0\},
\]

and identify its ten roots with the edges of `K5`.

Fix a root

\[
r=uv.
\]

Its six repair channels are the roots meeting `r`:

\[
S_r=\{uw,vw:w\in[5]\setminus\{u,v\}\}.
\]

With

\[
W=[5]\setminus\{u,v\},
\]

these are the six edges of

\[
K_r=K_{\{u,v\},W}\cong K_{2,3}.
\]

Two channels in `S_r` are disjoint as roots exactly when they are nonincident as edges of `K_r`.

### Lemma 1.1 — channel disjointness graph

The graph on vertex set `S_r` joining disjoint roots is a six-cycle.

### Proof

Each edge `uw` of `K_{2,3}` is disjoint from exactly the two edges `vw'` with `w' != w`. Hence the disjointness graph is 2-regular on six vertices. It is connected, for example

\[
ux,\ vy,\ uz,\ vx,\ uy,\ vz,\ ux
\]

for `W={x,y,z}`. Thus it is `C6`. ∎

---

## 2. The canonical identity hexagon of a root

Choose one cyclic ordering

\[
p_0,p_1,\ldots,p_5,p_0
\]

of the channel-disjointness cycle of `S_r`. Define six Petersen states

\[
F_j=\{p_{j-1},p_j\}
\qquad(j\bmod 6).
\]

Consecutive states share the pivot `p_j`, so

\[
C_r=(F_0,F_1,\ldots,F_5,F_0)
\]

is a six-cycle in the full Petersen state graph `L(P)`.

Changing the cyclic ordering by rotation or reversal gives the same unoriented state cycle.

### Theorem 2.1 — root/identity-hexagon bijection

The map

\[
\boxed{r\longmapsto C_r}
\]

is a bijection between the ten roots of `E5` and the ten Petersen identity hexagons.

For `C_r`:

1. its six pivot roots are exactly `S_r`;
2. its antipodal support half-turn is the transposition
   \[
   \alpha_r=(u\ v);
   \]
3. `alpha_r` sends the first pivot half to the second pivot half term by term.

### Proof

For the representative `r=13`, the channel-disjointness cycle may be written

\[
12,35,14,23,15,34,12.
\]

The corresponding state cycle is

\[
(\{12,34\},\{12,35\},\{14,35\},\{14,23\},\{15,23\},\{15,34\}).
\]

This is an identity hexagon. Its half-turn is `(13)`, and `(13)` sends the first three pivots `12,35,14` to the last three `23,15,34`.

The `S5` orbit of the representative has size ten, one for each root. Exact enumeration of `L(P)` gives exactly ten identity hexagons, and their half-turn roots are pairwise distinct. Hence the construction is bijective. ∎

### Exact finite certificate

Enumeration of all seventy six-cycles of `L(P)` verifies for the ten identity hexagons:

- ten distinct half-turn roots;
- each pivot set equals the six roots meeting that half-turn root;
- the half-turn maps each first-half pivot to the corresponding second-half pivot.

---

## 3. Three antipodal splits and three disjoint roots

Write

\[
W=\{x,y,z\}.
\]

The roots disjoint from `r=uv` are

\[
d_{xy}=xy,
\qquad
d_{xz}=xz,
\qquad
d_{yz}=yz.
\]

They satisfy

\[
d_{xy}+d_{xz}+d_{yz}=0.
\]

An identity hexagon has three unoriented antipodal decompositions into two three-transition halves. For each split, let `sigma` be the common support monodromy of the two halves.

### Theorem 3.1 — split-monodromy triality

For `C_r`, the three antipodal half monodromies are exactly

\[
\boxed{d_{xy},d_{xz},d_{yz}.}
\]

Each occurs once.

### Proof

For the representative `r=13`, the three splits have half monodromies

\[
24,25,45,
\]

which are precisely the three roots on the complementary support set `{2,4,5}`. The claim follows by `S5` equivariance. Exact enumeration verifies distinctness and completeness for all ten identity hexagons. ∎

Thus one identity hexagon does not carry one preferred DDD direction. It simultaneously carries the complete three-direction triality around its active root `r`; choosing an antipodal split chooses one direction.

---

## 4. Canonical identification with channel cohomology

For a disjoint root

\[
d=xy\subset W,
\]

define the four-cycle in `K_r=K_{2,3}`

\[
\Gamma_d
=
\{ux,uy,vx,vy\}.
\]

This is the unique four-cycle using the two right-side vertices in `d`.

### Theorem 4.1 — support/cohomology isomorphism

The assignment

\[
[d]\longmapsto [\Gamma_d]
\]

extends to a canonical linear isomorphism

\[
\boxed{
r^\perp/\langle r\rangle
\cong
H^1(K_r;\mathbf F_2).}
\]

Its three nonzero elements are exactly:

\[
[d_{xy}], [d_{xz}], [d_{yz}]
\]

and

\[
[\Gamma_{d_{xy}}], [\Gamma_{d_{xz}}], [\Gamma_{d_{yz}}].
\]

### Proof

The roots disjoint from `r` lie in `r^perp`, and their classes are the three nonzero elements of the two-dimensional quotient `r^perp/<r>`. The three four-cycles are the three nonzero elements of the two-dimensional cycle space of `K_{2,3}`. Moreover

\[
d_{xy}+d_{xz}=d_{yz}
\]

and

\[
\Gamma_{d_{xy}}+\Gamma_{d_{xz}}=\Gamma_{d_{yz}}.
\]

Hence the nonzero bijection is additive and extends uniquely to a linear isomorphism. ∎

### Corollary 4.2 — identity hexagon is the universal six-channel carrier

The three antipodal splits of `C_r` canonically enumerate

\[
H^1(K_r;\mathbf F_2)^\times.
\]

Therefore the Petersen identity-hexagon sector and the quadratic six-channel triality are the same finite support object, not merely analogous structures.

---

## 5. The three matching planes through a root

For one split direction `d` disjoint from `r`, define

\[
M_{r,d}=\langle r,d\rangle
=\{0,r,d,r+d\}.
\]

Because `r` and `d` are disjoint,

\[
b(r,d)=0.
\]

The bilinear form `b` on `E5` is nondegenerate, so `M_(r,d)` is a two-dimensional Lagrangian plane:

\[
M_{r,d}^\perp=M_{r,d}.
\]

### Theorem 5.1 — three split planes

The three antipodal splits of `C_r` select exactly the three Lagrangian planes containing `r`:

\[
\boxed{
M_{r,d_{xy}},
M_{r,d_{xz}},
M_{r,d_{yz}}.
}
\]

Modulo `<r>`, these three planes are the three one-dimensional subspaces of

\[
r^\perp/\langle r\rangle
\cong H^1(K_r;\mathbf F_2).
\]

Thus:

- root `r` selects the six-channel carrier;
- an antipodal split selects one nonzero channel-cohomology class;
- the selected class lifts to one DDD root/root/co-root matching plane.

---

## 6. Quotient defect as a DDD triality code

Fix one split and abbreviate

\[
M=M_{r,d},
\qquad
q=r+d.
\]

The three nonzero elements of `M` are

\[
M^\times=\{r,d,q\}.
\]

For `x in E5`, define

\[
\tau_M(x)
=
\bigl(b(x,r),b(x,d),b(x,q)\bigr).
\]

Since `q=r+d`,

\[
b(x,q)=b(x,r)+b(x,d),
\]

so

\[
\tau_M(x)\in\{000,011,101,110\}.
\]

### Theorem 6.1 — quotient/triality isomorphism

The map `tau_M` has kernel `M` and induces an isomorphism

\[
\boxed{
E_5/M
\cong
\{000,011,101,110\}.
}
\]

### Proof

The kernel consists of vectors orthogonal to both generators `r,d`, hence

\[
\ker\tau_M=M^\perp=M.
\]

Both quotient and code have dimension two, so the induced injective map is an isomorphism. ∎

### Corollary 6.2 — distinguished-zero interpretation

Every nonzero quotient defect has one of the three forms

\[
011,
\qquad101,
\qquad110.
\]

It vanishes on exactly one element of the DDD triality set `{r,d,q}` and is nonzero on the other two. Thus a nonzero quotient defect canonically selects one distinguished DDD direction.

This is exactly the same triality code already obtained from the three nonzero classes of `H^1(K_{2,3};F2)`.

---

## 7. Application to the identity-return displacement

For a physical identity-hexagon realisation with half translations `z1,z2`, common half monodromy `d`, support half-turn `alpha_r`, and total displacement

\[
\Delta=z_2+d z_1,
\]

define the half-turn semantic defect

\[
\eta=z_2+\alpha_r z_1.
\]

The matching-plane theorem gives

\[
[\Delta]_{E_5/M_{r,d}}
=
[\eta]_{E_5/M_{r,d}}.
\]

### Theorem 7.1 — no new identity-sector obstruction alphabet

The complete quotient obstruction of an identity hexagon is

\[
\boxed{
\tau_{M_{r,d}}(\Delta)
=
\tau_{M_{r,d}}(\eta)
\in\{000,011,101,110\}.
}
\]

Therefore:

1. `000` means the return displacement lies in the selected matching plane
   \[
   \{0,r,d,r+d\};
   \]
2. a nonzero code is already one of the three DDD/channel-cohomology triality classes.

The identity sector creates no fifth finite obstruction type beyond matching-plane displacement and DDD triality.

### Corollary 7.2 — two scalar tests suffice

It is enough to control the two parities

\[
b(\eta,r),
\qquad
b(\eta,d).
\]

Full equality `z1=z2` is unnecessary. Moreover, since `alpha_r` fixes both `r` and `d`, these two parities equal the corresponding pairings of the frame-fixed half discrepancy `z2+z1`.

---

## 8. Revised physical composition target

The algebraic identity sector is now completely attached to existing six-channel/DDD machinery. The remaining source theorem is:

> Given the six physical repair-channel attachments around `C_r`, realise the channel-disjointness cycle and its chosen antipodal split functorially, or prove that failure of the left-part swap `alpha_r` forces route/profile escape, a smaller separator/common cut, or a bounded root-fibre defect.

If the swap is compatible modulo `M_(r,d)`, the return is one of `0,r,d,r+d`. If it is not, its quotient code already chooses one of the three DDD triality directions and should be routed to the existing relative-witness/DDD branch.

The only remaining bridge is physical:

\[
\text{triality code}
\longrightarrow
\text{actual route class / strict descent}.
\]

There is no remaining unclassified finite support state in the identity-hexagon sector.