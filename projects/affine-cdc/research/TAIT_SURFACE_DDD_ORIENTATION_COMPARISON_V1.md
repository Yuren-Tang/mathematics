# Tait-surface orientation equals the DDD crossed-route orientation class

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `b71bcd89c4198da17ced0c1cf3009ddacf20d138`  
**Parents:**

- `projects/affine-cdc/research/TAIT_MULTIPOLE_TRIANGLE_SURFACE_CURVATURE_V1.md`;
- `projects/affine-cdc/research/FLAT_MOBIUS_TAIT_ORIENTATION_REDUCTION_V1.md`;
- `projects/affine-cdc/research/DDD_ROUTE_ORIENTATION_COVER_V1.md`;
- `projects/affine-cdc/research/PETERSEN_PIVOT_RESOLUTION_V1.md`.

**Status:** exact comparison theorem. For the complementary rank-two Tait side network emitted by one private root shift, the orientation double cover of its triangle surface is canonically the crossed-route orientation cover of the corresponding constant-pivot DDD/Petersen transport. On every closed physical Tait transport walk, the surface first Stiefel--Whitney character and the DDD route character are both the path-length parity. Thus the flat Möbius orientation bit is exactly the nontrivial physical DDD orientation-descent class, not merely an isomorphic `C_2` representation.  
**Not implied:** automatic contraction of every odd return, elimination of every bounded DDD blossom, simultaneous trivialisation of both crossed routes in the presence of bad-sheet exchange, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Private-shift Tait sector

Fix a private root shift

\[
s=ab.
\]

Let

\[
W=[5]\setminus\{a,b\}
=\{u,v,w\}.
\]

The complementary Tait side network has the three root colours

\[
uv,
\qquad
vw,
\qquad
wu.
\]

For every Tait edge colour

\[
d\in E(K_W),
\]

the roots `s,d` are disjoint. Hence

\[
F_d=\{s,d\}
\]

is an edge of the Petersen graph in its Kneser model, equivalently one co-root/DDD atom state.

---

## 2. Tait turns are constant-pivot Petersen transitions

Consider one cubic Tait vertex with incident colours

\[
uv,
\qquad
vw,
\qquad
wu.
\]

A bicoloured route entering on `uv` and leaving on `vw` produces the Petersen-state transition

\[
F_{uv}=\{s,uv\}
\longrightarrow
F_{vw}=\{s,vw\}.
\]

The two Petersen edges share the pivot `s`. The three Petersen neighbours of `s` are precisely

\[
uv,
\qquad
vw,
\qquad
wu.
\]

Therefore the side root emitted by the transition is the third Tait colour `wu`.

### Theorem 2.1 — local transport identification

Every turn of a bicoloured path or cycle in the complementary Tait multipole is exactly one step of the constant-pivot Petersen/co-root transport with pivot `s`.

Conversely, every constant-pivot transition among the three states

\[
F_{uv},F_{vw},F_{wu}
\]

is one Tait turn at a three-colour vertex.

### Consequence 2.2

A Tait route with `m` turns determines an octahedral crossed-resolution transport word of length `m`, with exactly the same ordered source vertices and emitted third-colour word.

---

## 3. Orientation of the triangle surface

Let

\[
S_T
\]

be the triangle surface of the Tait multipole. Its triangles are dual to source vertices of `T`; crossing an internal source edge moves from one triangle to the adjacent triangle.

Choose an orientation on one triangle. Under the colour-preserving edge gluing, the induced orientation on the adjacent triangle must be the opposite one.

### Theorem 3.1 — orientation character on the dual graph

The orientation double cover of `S_T` restricted to the dual graph `T` is the bipartite double cover. For every closed dual walk `gamma`,

\[
\boxed{
 w_1(S_T)(\gamma)
 =|\gamma|\pmod2.}
\]

### Proof

Every traversal of one dual edge crosses one triangle gluing and reverses the chosen local triangle orientation. After `m` crossings the orientation returns exactly when `m` is even. ∎

### Corollary 3.2

`S_T` is orientable if and only if the internal dual graph is bipartite. A Möbius generator is represented by an odd closed dual walk.

---

## 4. DDD crossed-route orientation

For the DDD atom with fixed disjoint pair

\[
s,
\qquad d,
\]

choose the crossed route `X` and one of its two blocks. The DDD orientation theorem defines the block-orientation character

\[
\nu_X=\kappa.
\]

For an octahedral overlap word of length `m`,

\[
\boxed{
\kappa(\pi_\gamma)=m\pmod2.}
\]

This follows because every local transport is a transposition and, inside the stabiliser `D_8`, permutation sign is `(-1)^\kappa`.

---

## 5. Exact comparison

Let `gamma` be any closed physical bicoloured route in the Tait multipole. Regard it simultaneously as:

1. a closed dual walk in the triangle surface;
2. the constant-pivot Petersen transport word of Theorem 2.1.

The number of dual-edge crossings equals the number of Tait turns and hence the length of the Petersen transport word.

### Theorem 5.1 — orientation comparison theorem

\[
\boxed{
 w_1(S_T)(\gamma)
 =\kappa(\pi_\gamma)
 =\nu_X(\gamma).}
\]

### Proof

Both sides are the common path-length parity `|gamma| mod 2`, by Theorems 3.1 and the DDD internal-twist theorem. The local transport identification ensures that the two lengths count the same physical turns, not merely abstract walks of isomorphic graphs. ∎

### Corollary 5.2 — equality of orientation covers

The following two double covers of the physical Tait transport system are canonically identical:

1. the orientation double cover of the triangle surface;
2. the cover obtained by choosing and transporting one block of crossed DDD route `X`.

On this common cover the exceptional DDD cocycle is the coboundary of the chosen oriented block.

---

## 6. Annulus and Möbius consequences

### Flat annulus

Every closed walk preserving the annular transverse orientation has

\[
w_1=0.
\]

Therefore

\[
\kappa=0
\]

on the serial generator. This is exactly the even-return branch of the DDD orientation theorem.

### Flat Möbius

The Möbius generator reverses transverse orientation, so

\[
w_1=1.
\]

Therefore

\[
\boxed{
\kappa=\nu_X=1.}
\]

The canonical crossed-splice Möbius cell carries the nontrivial physical crossed-route orientation class.

### Theorem 6.1 — Möbius bit calibration

The topological orientation bit introduced in the flat-Möbius response is exactly the physical DDD orientation-descent bit. No further finite lookup table is required to compare the two.

---

## 7. Relation to the DDD cohomology generator

The nontrivial DDD cocycle

\[
\alpha(g)=\epsilon_1r_2+\epsilon_2r_1
\]

becomes a coboundary on the crossed-route orientation cover:

\[
\alpha|_{\ker\kappa}=\delta x.
\]

The comparison theorem identifies `ker kappa` with the orientable double cover of `S_T`.

### Corollary 7.1 — Stiefel--Whitney interpretation

The exceptional class

\[
[\alpha]\in H^1(D_8,E_5)
\]

is the affine lift of the first Stiefel--Whitney obstruction to descending an oriented crossed route from the orientation cover to the physical base.

In particular, the earlier triangle/star orientation parity, antipodal-switch indecomposability, and flat-Möbius reversal are concrete manifestations of the same orientation-descent mechanism.

### Trust note

For the second crossed route `Y`, the orientation character is

\[
\nu_Y=\kappa+\chi.
\]

The extra `chi` is the separately known bad-sheet exchange character. The theorem identifies the surface orientation canonically with route `X`; simultaneous handling of both routes still requires the existing sheet-exchange compatibility argument.

---

## 8. Revised finite odd-return frontier

The comparison gap is closed. The remaining odd-return problem is no longer to identify the bit, but to act on it.

For the first odd return in a minimal interval, prove one of:

1. the canonical Möbius/DDD cell is replaced by one of its crossed root resolutions;
2. its support exposes a four-port separator or common-cut carrier;
3. it enters the zero/co-root defect-tree branch;
4. the interval complexity strictly decreases after passing to the orientation cover and descending a compatible replacement.

All required orientation data are explicit.

---

## 9. Trust boundary

### Exact here

- the assignment `d -> F_d={s,d}` from Tait colours to Petersen/DDD atom states;
- identification of every Tait turn with one constant-pivot Petersen transition and its correct emitted root;
- surface orientation character as dual-walk length parity;
- DDD crossed-route orientation character as the same physical turn parity;
- canonical equality of the two orientation double covers;
- calibration of the flat Möbius bit with the nontrivial DDD orientation class;
- Stiefel--Whitney interpretation of the exceptional orientation descent.

### Still open

- composition-safe elimination or replacement of every bounded odd-return cell;
- simultaneous compatibility of the second crossed route with bad-sheet exchange;
- packaging all local decreases into one global well-founded measure;
- horizontal/global induction and the global five-support theorem.