# Flat Möbius Tait networks: orientation-preserving response compression

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `d75f7b1571e8e6ff9eaf4cbdb6df23cd83e4c351`  
**Parents:**

- `projects/affine-cdc/research/TAIT_MULTIPOLE_TRIANGLE_SURFACE_CURVATURE_V1.md`;
- `projects/affine-cdc/research/FLAT_ANNULUS_TAIT_RESPONSE_REDUCTION_V1.md`;
- `projects/affine-cdc/research/DDD_ROUTE_ORIENTATION_COVER_V1.md`;
- `projects/affine-cdc/research/NONCROSSING_SIDE_SIGNATURE_WINDOW_V1.md`.

**Status:** exact reduction of the completely flat Möbius Tait branch after adjoining one topological orientation bit to the ordered Tait boundary response. If `b` is the number of boundary semiedges and `n` the source-vertex count, then `n>=b+2`; every ordered response with Möbius orientation has an explicit `b+2`-vertex representative. Equality is the unique minimal crossed-splice serial strip. A long equality strip localises to an at-most-eight-vertex return cell. Thus the unbounded Möbius branch reduces to finite calibration of the equality between the surface orientation bit and the physical `D_8` cocycle.  
**Not implied:** the equality of those two bits, preservation of bridgelessness under every replacement, full five-support boundary-profile equivalence, contraction of every bounded return cell, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Why ordinary Tait response is insufficient

Let `T` be a connected properly three-edge-coloured cubic multipole with flat triangle surface

\[
S_T
\]

homeomorphic to a Möbius band.

As in the annular case, every boundary semiedge has one common colour `x`. The other two bicoloured systems induce perfect matchings

\[
M_y=M_{xy},
\qquad
M_z=M_{xz}
\]

on the ordered boundary ports.

The ordinary ordered Tait response

\[
(\operatorname{col}_B,M_y,M_z)
\]

does not remember orientability. The same boundary matchings may be realised by a disk multipole.

### Definition 1.1 — enhanced flat response

Define

\[
\boxed{
\mathfrak R^{\mathrm{or}}(T)
=
(\operatorname{col}_B,M_y,M_z,\omega_T),}
\]

where

\[
\omega_T=
\begin{cases}
0,&S_T\text{ orientable},\\
1,&S_T\text{ nonorientable}.
\end{cases}
\]

For the present branch,

\[
\omega_T=1.
\]

This is a topological response bit. Its equality with the physical support-label `D_8` class is not assumed.

---

## 2. One boundary response cycle

The flat boundary develops to one straight line modulo a glide reflection, so all boundary semiedges have colour `x`.

### Theorem 2.1 — Möbius boundary cycle

\[
\boxed{M_y\cup M_z=C_B,}
\]

where `C_B` is one alternating even cycle on all boundary ports.

### Proof

As in the annular boundary dictionary, `M_y` and `M_z` pair the two `x`-semiedges meeting at each boundary surface vertex. Following alternating matching edges therefore follows the unique boundary component of the Möbius band. ∎

### Corollary 2.2

Any simultaneous noncrossing linear or circular order for `M_y,M_z` is the cycle order of `C_B` up to reversal.

---

## 3. Euler lower bound

Let

\[
c=|\mathcal C(T)|
\]

be the number of closed bicoloured components, equivalently the number of interior vertices of the triangle surface.

The exact Euler formula gives

\[
0=\chi(S_T)=c+\frac{b-n}{2}.
\]

Hence

\[
\boxed{n=b+2c.}
\]

A Möbius band has nonempty interior, so `c>=1`.

### Theorem 3.1 — Möbius size floor

\[
\boxed{n\ge b+2.}
\]

Equality holds exactly when the triangle surface has one interior vertex, equivalently when all internal bicoloured closed links form one component.

---

## 4. Crossed-splice construction

Start with the boundary corolla on the `b` ordered ports:

- one boundary vertex per `x`-port;
- `y`-edges given by `M_y`;
- `z`-edges given by `M_z`.

By Theorem 2.1 this is one connected alternating cycle. Its triangle surface is a disk and has ordinary response `(M_y,M_z)` but orientation bit zero.

Choose one `y`-edge

\[
a_1a_2
\]

and one `z`-edge

\[
b_1b_2.
\]

Delete them. Add two vertices `u,v`, one `x`-edge `uv`, and replace the deleted edges by

\[
a_1\mathbin{-_y}u,
\qquad
v\mathbin{-_y}a_2,
\]

\[
b_1\mathbin{-_z}v,
\qquad
u\mathbin{-_z}b_2.
\]

The endpoint assignment is chosen crosswise relative to the two arcs of the cut boundary cycle. Denote the resulting multipole by

\[
M(M_y,M_z).
\]

### Lemma 4.1 — crossed smoothing

The `yz` subgraph of `M(M_y,M_z)` is one closed cycle.

### Proof

Deleting one `y`-edge and one `z`-edge from the original alternating cycle produces two disjoint paths on the four cut endpoints. There are two ways to pair these endpoints through the new vertices. The parallel pairing closes the two paths separately; the crossed pairing joins them into one cycle. The displayed assignment is the crossed pairing. ∎

### Theorem 4.2 — canonical Möbius representative

`M(M_y,M_z)`:

1. is connected and properly three-edge-coloured;
2. has the same ordered boundary colours and matchings `M_y,M_z`;
3. has
   \[
   b+2
   \]
   source vertices;
4. has one boundary component and one interior bicoloured component;
5. has Euler characteristic zero and is nonorientable;
6. therefore has triangle surface homeomorphic to a Möbius band.

### Proof

The colour and matching verification is the same `yxy`/`zxz` response calculation as in the annular splice. The crossed smoothing gives one closed `yz` component, so the triangle surface has

\[
V=b+1,
\qquad
F=b+2,
\qquad
\chi=0.
\]

It has one boundary component. The only compact connected surface with one boundary component and Euler characteristic zero is the Möbius band. ∎

### Corollary 4.3 — orientation-preserving strict compression

If

\[
n>b+2,
\]

then `T` has an enhanced-response-equivalent Möbius replacement with strictly fewer source vertices.

---

## 5. Equality normal form

Assume

\[
n=b+2.
\]

Then `c=1` and there is exactly one internal `x`-edge.

### Theorem 5.1 — minimal Möbius serial strip

Every equality case is boundary-order- and colour-isomorphic to one crossed-splice representative `M(M_y,M_z)`.

### Proof

The two vertices without boundary semiedges are the endpoints of the unique internal `x`-edge. Their `y,z` half-edges splice one `y`-edge and one `z`-edge of the boundary response cycle.

Because the surface has one interior bicoloured component, the smoothing of the cut `y/z` cycle must be crossed rather than parallel. This is precisely the construction of `M(M_y,M_z)`. ∎

### Definition 5.2

The equality case is the **minimal Möbius serial strip** for the enhanced response.

There is no hidden annular width or additional interior topology.

---

## 6. Bounded return-cell localisation

Place a minimal Möbius serial strip in a support-minimal pair-preserving four-port interval. If the interval order of its boundary attachments is not the cycle order of `C_B` up to reversal, one of the edges of `M_y union M_z` crosses and gives route/profile escape.

Otherwise apply the noncrossing four-port return-window theorem.

### Theorem 6.1 — six-port Möbius return cell

Exactly one of the following occurs.

1. The complete boundary side signature has at most four outputs.
2. Two boundary ports belonging to the same outside component cut off an arc of `C_B` containing at most six consecutive boundary ports.

### Corollary 6.2 — eight-vertex source ceiling

The Tait part of this return cell contains at most six boundary vertices and at most the two crossed-splice vertices. Hence it has at most

\[
\boxed{8}
\]

source vertices.

### Corollary 6.3 — finite orientation calibration

Every flat Möbius branch satisfies one of:

1. strict enhanced-response compression;
2. a globally bounded four-output signature;
3. an at-most-eight-vertex same-component return cell;
4. a crossing matching and route/profile escape.

Thus the only surviving Möbius issue is finite comparison of the return-cell orientation bit with the physical `D_8` support-label cocycle.

---

## 7. The precise `D_8` comparison target

The topological bit `omega_T` records reversal of a transverse orientation after one generator of the Möbius strip.

The physical DDD line carries the nontrivial class

\[
H^1(D_8,E_5)\cong\mathbf F_2.
\]

Both are one-dimensional orientation-reversal representations, but equality is not automatic.

### Target 7.1 — finite Möbius calibration

On the canonical crossed-splice return cells with at most eight vertices, construct the explicit comparison map

\[
\boxed{
\omega_T
\longmapsto
[\zeta]_{D_8}}
\]

and prove that the crossed splice has the nontrivial physical class.

Once this finite calibration is established, every unbounded flat Möbius branch either compresses or localises one bounded DDD atom.

---

## 8. Trust boundary

### Exact here

- the need for one orientation bit beyond ordinary ordered Tait response;
- one-cycle boundary response `M_y union M_z`;
- Euler equation `n=b+2c` and lower bound `n>=b+2`;
- explicit crossed-splice representative of size `b+2`;
- equality classification as the minimal Möbius serial strip;
- localisation to at most six boundary ports and at most eight source vertices;
- reduction of the unbounded Möbius branch to finite orientation calibration.

### Still open

- equality of the topological orientation bit with the physical `D_8` cocycle;
- preservation of the ambient bridgeless minimal-counterexample category under replacement;
- full five-support boundary-profile equivalence;
- composition-safe contraction or replacement of every bounded return cell;
- negative-Euler separator/genus descent;
- a global well-founded complexity and the five-support theorem.