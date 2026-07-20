# Octahedral face curvature and bounded odd-return normal forms

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parents:**

- `projects/affine-cdc/research/OCTAHEDRAL_OVERLAP_TRANSPORT_V1.md`;
- `projects/affine-cdc/research/DDD_ROUTE_LOCK_TRANSGRESSION_V1.md`;
- `projects/affine-cdc/research/DDD_ROUTE_ORIENTATION_COVER_V1.md`.

**Status:** exact finite connection/curvature theorem; physical face moves and bounded source replacement remain open.  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. The octahedral connection

Let

\[
\mathcal O=L(K_4)
\]

be the oriented fixed-co-root overlap-state graph. Its six vertices are the edges of `K_4`, and adjacent states `y,y'` meet in one endpoint.

For an oriented transition

\[
y\longrightarrow y',
\]

put

\[
w=y+y'
\]

and let

\[
T_{y,y'}=\tau_w
\]

be the transposition of the two endpoints of `w`. Then

\[
\tau_w(y)=y',
\qquad
\tau_w(y+c)=y'+c,
\qquad
\tau_w(w)=w.
\]

For a path

\[
\gamma=(y_0,y_1,\ldots,y_n)
\]

define

\[
\pi_\gamma
=
T_{y_{n-1},y_n}\cdots T_{y_0,y_1}.
\]

This is the canonical `S_4` overlap transport.

The graph `mathcal O` is the one-skeleton of the octahedron. Its eight triangular faces are of two `S_4`-equivalent geometric kinds:

1. three `K_4` edges incident with one vertex;
2. the three edges of a triangle in `K_4`.

---

## 2. Face holonomy

Fix one state

\[
y=12
\]

with antipode

\[
z=34=y+c.
\]

The four triangular faces through `y` are represented by

\[
(12,13,14),
\qquad
(12,23,24),
\]

and

\[
(12,13,23),
\qquad
(12,14,24).
\]

### Theorem 2.1 — triangular face holonomy

The transport around an oriented triangular face based at `y` returns to the same oriented state and has holonomy equal to an endpoint flip inside exactly one of the two bad roots `y,z`.

For the representatives above:

\[
\pi_{12,13,14,12}=(34),
\]

and

\[
\pi_{12,13,23,12}=(12).
\]

The other two faces give the same two flip types. By `S_4`-equivariance this exhausts all octahedral faces.

Hence every triangular face has

\[
\boxed{\kappa(\pi_F)=1,
\qquad
\chi(\pi_F)=0.}
\]

### Proof

For the first representative the side roots are

\[
23,34,24,
\]

so

\[
\pi=(24)(34)(23)=(34).
\]

For the second they are

\[
23,12,13,
\]

so

\[
\pi=(13)(12)(23)=(12).
\]

Both are internal endpoint flips with no exchange of the two bad root sheets.

---

## 3. Opposite-root affine curvature

Let the local bad matching be

\[
M=\{y,z\},
\qquad z=y+c.
\]

Use the explicit DDD cocycle in the corresponding local frame.

### Theorem 3.1 — opposite-root face law

If the triangular face holonomy flips the endpoints inside `y`, then its affine translation is `z`. If it flips the endpoints inside `z`, then its affine translation is `y`.

Equivalently,

\[
\boxed{
\alpha(\pi_F)
=
\text{the bad matching root not internally flipped by }\pi_F.
}
\]

### Proof

In the standard frame `y=r_1`, `z=r_2`, the explicit cocycle satisfies

\[
\alpha((12))=r_2,
\qquad
\alpha((34))=r_1.
\]

The general statement follows by conjugating the local DDD frame.

### Interpretation

Each octahedral triangular face carries one unit of DDD affine curvature. The scalar curvature records that an internal twist occurred; the vector curvature is the opposite bad root.

This gives a local geometric origin for the opposite-root formula in the explicit cocycle.

---

## 4. Scalar Gauss law on the octahedron

Every edge transport is a transposition. Therefore, for any path of length `n`,

\[
\operatorname{sgn}(\pi_\gamma)=(-1)^n.
\]

For a return to the same bad matching,

\[
\operatorname{sgn}(\pi_\gamma)=(-1)^{\kappa(\pi_\gamma)}.
\]

Hence

\[
\kappa(\pi_\gamma)=n\pmod2.
\]

This admits an intrinsic face formulation.

Let `gamma` be a closed oriented-state walk, regarded modulo two as a one-cycle in the octahedral sphere. Choose any two-chain `D` of triangular faces with

\[
\partial D=\gamma.
\]

### Theorem 4.1 — octahedral area parity

\[
\boxed{
\kappa(\pi_\gamma)
=|\gamma|
=|D|\pmod2.
}
\]

### Proof

Every triangular face has three boundary edges. Summing face boundaries modulo two cancels internal edges, so

\[
|\partial D|\equiv3|D|\equiv|D|\pmod2.
\]

Also `|gamma| mod 2` equals the sign character of the product of its transposition transports, which is `kappa` on the return group.

The parity does not depend on the filling. Two fillings differ by the full octahedral sphere, which has eight faces.

### Consequence 4.2

The DDD internal-twist character is the mod-two face curvature of the octahedral connection. This is a canonical state-space Gauss law, not a comparison by dimension.

---

## 5. Flat equatorial squares

An equatorial square of the octahedron alternates between two pairs of antipodal side-root labels. A representative is

\[
12\to13\to34\to24\to12.
\]

Its side-root word is

\[
23,14,23,14,
\]

and its transport product is the identity.

### Theorem 5.1 — square flatness

Every equatorial four-cycle has

\[
\boxed{\pi_\square=1,
\qquad
\alpha(\pi_\square)=0.}
\]

It separates four triangular faces from the complementary four, so its scalar curvature is also zero.

### Mechanistic dichotomy

At the finite connection level:

- triangular faces are the elementary nonflat DDD curvature cells;
- equatorial squares are flat commutator cells.

This is the octahedral state-space shadow of the DDD-versus-flat-potential split.

---

## 6. Three-step normal forms for every odd return

Return to the base oriented state `12`, with antipode `34`. The four return elements with

\[
\kappa=1
\]

are

\[
a,\quad b,\quad ap,\quad bp.
\]

They admit the following three-step overlap words:

\[
\begin{array}{c|c|c}
\text{return element}&\text{state word}&\text{endpoint}\\
\hline
a&(12,13,23,12)&12\\
b&(12,13,14,12)&12\\
ap&(12,13,14,34)&34\\
bp&(12,13,23,34)&34.
\end{array}
\]

### Theorem 6.1 — bounded odd-return normal form

Every octahedral overlap return with nonzero internal-twist parity has the same endpoint and transport element as one of the four three-step words above, after relabelling the local `K_4` frame.

### Proof

The odd-return elements of the `D_8` stabiliser are exactly the four elements with `epsilon_1+epsilon_2=1`. Direct multiplication of the canonical transpositions along the displayed words gives `a,b,ap,bp` respectively.

### Corollary 6.2 — holonomy core plus flat kernel

Let `gamma` be any odd return and let `gamma_pi` be the corresponding three-step normal word. Then

\[
\gamma_\pi^{-1}\gamma
\]

has identity transport.

Thus every odd overlap return decomposes at the finite transport level into

\[
\boxed{
\text{one bounded three-step curvature core}
+
\text{an identity-holonomy remainder}.
}
\]

This is an exact groupoid decomposition. It does not yet assert a physical graph replacement, because the original and normal-form words may carry different side attachments.

---

## 7. Twisted discrete Stokes principle

A combinatorial filling of a closed state walk may be shelled by triangular faces. Each face contributes an internal-flip holonomy and the opposite-root affine translation of Theorem 3.1, conjugated into the base frame by the transport to that face.

### Theorem 7.1 — finite affine Stokes formula

For any chosen shelling of a state-space filling, the boundary affine holonomy is the ordered product of the transported affine face holonomies. Applying the cocycle identity gives the boundary translation as the corresponding twisted sum of transported opposite-root face labels.

In particular, its scalar internal-twist shadow is the untwisted face parity of Theorem 4.1.

### Trust boundary

This is a theorem about the finite octahedral connection and the explicit `D_8` affine cocycle. A physical graph-level Stokes theorem still requires a functor from face moves in state space to admissible transformations or separated replacement regions in the source graph.

---

## 8. Revised localisation frontier

The finite holonomy of an odd return is already represented by one triangular curvature cell. The unresolved issue is not the size of the state-space obstruction, but whether the physical side semantics can be separated from the identity-holonomy remainder.

### Target 8.1 — curvature-core separation

Given a support-minimal physical overlap word with odd return, compare it with its three-step normal form and prove one of:

1. the identity-holonomy remainder is root-admissibly removable;
2. it is separated by a smaller cyclic cut or four-pole interface;
3. it is a flat zero/co-root equality unit;
4. the three-step core itself realises a bounded DDD blossom.

### Target 8.2 — flat-kernel generation

Show that identity-holonomy overlap words are generated, under composition-safe operations, by:

- immediate backtracks;
- equatorial flat squares;
- paired triangular curvature cells whose affine translations cancel after transport.

This would reduce transfer sufficiency to finitely many bounded physical relations.

### Target 8.3 — regional curvature map

Map the transported opposite-root face labels to the common-cut/full-channel curvature word and prove compatibility with physical boundary summation. This is the graph-level completion of the quadratic transgression.

---

## 9. Trust boundary

### Exact here

- triangular face holonomy classification;
- opposite-root affine face law;
- scalar area-parity/Gauss law;
- flatness of equatorial squares;
- three-step normal forms for all odd `D_8` returns;
- decomposition of any odd return into a bounded curvature core and identity-transport remainder;
- finite twisted Stokes formula.

### Still open

- composition-safe realisation of state-space face moves in the physical source graph;
- generation and elimination of the identity-holonomy physical kernel;
- bounded localisation of the three-step curvature core;
- graph-level comparison with common-cut curvature;
- Type T/Type H composition, horizontal/global induction, and the global five-support theorem.
