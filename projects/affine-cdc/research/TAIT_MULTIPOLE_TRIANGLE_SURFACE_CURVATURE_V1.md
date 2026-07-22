# Tait multipole triangle surfaces and the curvature decomposition

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `246e565deade601c9f9d660cafde1e175230c68d`  
**Parents:**

- `projects/affine-cdc/research/KEMPE_BLOCKER_TAIT_SIDE_NETWORK_V1.md`;
- `projects/affine-cdc/research/MINIMAL_LAMINAR_INTERVAL_SURGERY_V1.md`;
- `projects/affine-cdc/research/NONCROSSING_SIDE_SIGNATURE_WINDOW_V1.md`;
- `projects/affine-cdc/five-support/periodic-kempe-ladders.md`;
- `projects/affine-cdc/five-support/ribbon-intersection-response.md`.

**Status:** exact topological and combinatorial curvature theorem for every connected properly three-edge-coloured side multipole. A disk side network always exposes a bicoloured source carrier with edge boundary at most four. A zero-curvature side network with no positive-curvature link is a flat annulus or flat Möbius band; these are respectively the topological translation and orientation-reversing serial branches.  
**Not implied:** that every physical minimal laminar interval has disk or zero-Euler Tait surface, identification of the flat Möbius class with the physical `D_8` cocycle, composition-safe contraction of every flat annulus, elimination of negative-Euler surfaces, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Properly coloured cubic multipoles

Let `T` be a finite connected cubic multipole with:

- ordinary internal edges;
- boundary semiedges;
- a proper edge colouring by
  \[
  \{1,2,3\},
  \]
  so that every cubic source vertex is incident with exactly one edge or semiedge of each colour.

Write

\[
n=|V(T)|,
\qquad
b=|\partial T|,
\qquad
e=|E_{\mathrm{int}}(T)|.
\]

The cubic degree equation is

\[
\boxed{3n=2e+b.}
\]

For a pair of colours `i,j`, let

\[
T_{ij}
\]

be the submultipole consisting of the `i`- and `j`-coloured edges and semiedges. Every source vertex has degree two in `T_{ij}`. Hence every connected component of `T_{ij}` is exactly one of:

1. a closed alternating bicoloured cycle;
2. an alternating bicoloured path whose two ends are boundary semiedges.

Let

\[
\mathcal C(T)
\]

be the set of all closed bicoloured components over the three colour pairs, and let

\[
\mathcal P(T)
\]

be the set of all open bicoloured path components.

For a component `L`, write

\[
|L|
\]

for the number of source vertices of `T` traversed by `L`.

---

## 2. The coloured triangle surface

For every source vertex `v` of `T`, take one abstract triangle

\[
\Delta_v
\]

whose three sides are labelled `1,2,3`.

For every ordinary edge of colour `i` joining source vertices `u,v`, glue the `i`-side of `\Delta_u` to the `i`-side of `\Delta_v`, matching the endpoint colours. Leave the side corresponding to a boundary semiedge unglued.

Denote the resulting triangular cellulation by

\[
S_T.
\]

### Theorem 2.1 — surface and link dictionary

`S_T` is a connected compact triangular surface with nonempty boundary. Its vertices are canonically the bicoloured components of `T`:

1. a closed component
   \[
   C\in\mathcal C(T)
   \]
   is the circular link of one interior surface vertex;
2. an open component
   \[
   P\in\mathcal P(T)
   \]
   is the interval link of one boundary surface vertex.

The number of triangles incident with the corresponding surface vertex is exactly `|C|` or `|P|`.

### Proof

A corner of a triangle labelled by the omitted colour `k` is continued across exactly the sides of the other two colours `i,j`. Following the corner link is therefore exactly following the component of `T_{ij}` through the corresponding source vertex.

Every such component is a cycle or a path. Hence every vertex link in the glued complex is a circle or an interval, so the complex is a surface with boundary. Connectedness follows from connectedness of `T`. The number of incident triangles is the number of source vertices in the bicoloured component. ∎

### Corollary 2.2 — boundary-link count

\[
\boxed{|\mathcal P(T)|=b.}
\]

### Proof

Every boundary semiedge of colour `i` is an endpoint in the two bicoloured systems containing `i`. Thus the total number of open-path endpoints is `2b`. Every open path has exactly two endpoints. ∎

### Corollary 2.3 — total link length

\[
\boxed{
\sum_{C\in\mathcal C(T)}|C|
+
\sum_{P\in\mathcal P(T)}|P|
=3n.}
\]

### Proof

Every source vertex lies in exactly one component of each of the three bicoloured systems. ∎

---

## 3. Euler characteristic

The triangle surface has

\[
F=n
\]

faces. Its surface edges consist of one edge for every ordinary source edge and one unglued boundary edge for every semiedge, so

\[
E=e+b
=\frac{3n+b}{2}.
\]

Its surface vertices are the bicoloured components:

\[
V=|\mathcal C(T)|+|\mathcal P(T)|
=|\mathcal C(T)|+b.
\]

### Theorem 3.1 — Euler formula in Tait coordinates

\[
\boxed{
\chi(S_T)
=|\mathcal C(T)|+\frac{b-n}{2}.}
\]

Equivalently,

\[
\chi(S_T)
=
|\mathcal C(T)|+|\mathcal P(T)|
-
\frac{n+b}{2}.
\]

### Proof

Substitute the displayed values of `V,E,F` in `\chi=V-E+F`. ∎

---

## 4. Exact curvature identity

For an interior vertex of a triangular surface with `d` incident triangles, use the integral curvature

\[
6-d.
\]

For a boundary vertex with `d` incident triangles, use

\[
3-d.
\]

Under the link dictionary these become

\[
6-|C|
\qquad(C\in\mathcal C(T))
\]

and

\[
3-|P|
\qquad(P\in\mathcal P(T)).
\]

### Theorem 4.1 — Tait Gauss--Bonnet identity

\[
\boxed{
6\chi(S_T)
=
\sum_{C\in\mathcal C(T)}(6-|C|)
+
\sum_{P\in\mathcal P(T)}(3-|P|).}
\]

### Proof

Using Corollaries 2.2 and 2.3, the right-hand side is

\[
6|\mathcal C(T)|+3b-3n
=6\left(|\mathcal C(T)|+\frac{b-n}{2}\right),
\]

which is `6\chi(S_T)` by Theorem 3.1. ∎

### Interpretation

The side network has only three local curvature possibilities.

1. **Positive interior curvature:** a closed bicoloured cycle of length at most five.
2. **Positive boundary curvature:** an open bicoloured path through at most two source vertices.
3. **Nonpositive curvature:** closed links have length at least six and open links have length at least three.

Because a closed bicoloured cycle alternates two colours, its length is even. Therefore positive interior curvature actually means

\[
\boxed{|C|\le4.}
\]

---

## 5. Disk networks expose a four-port carrier

Assume

\[
S_T\cong D^2.
\]

Then

\[
\chi(S_T)=1.
\]

### Theorem 5.1 — positive-curvature carrier in a disk

Every disk Tait multipole contains at least one of:

1. an open bicoloured path
   \[
   P\in\mathcal P(T),
   \qquad |P|\le2;
   \]
2. a closed bicoloured cycle
   \[
   C\in\mathcal C(T),
   \qquad |C|\le4.
   \]

### Proof

If every closed link had length at least six and every open link had length at least three, every summand in Theorem 4.1 would be nonpositive. This contradicts

\[
6\chi(S_T)=6.
\]

The evenness of closed bicoloured cycles improves `|C|\le5` to `|C|\le4`. ∎

### Theorem 5.2 — four-port source boundary

Let `L` be the carrier supplied by Theorem 5.1 and let `U=V(L)` be its source-vertex set.

Then

\[
\boxed{|\delta_T(U)|\le4,}
\]

where boundary semiedges of `T` incident with `U` are counted in `\delta_T(U)`.

### Proof

If `L=P` is an open bicoloured path through `t\le2` source vertices, its two path ends are boundary semiedges. Every path vertex has exactly one incident edge of the third colour. Some of those third-colour edges may join two vertices of `U`; all others leave `U`. Hence

\[
|\delta_T(U)|\le t+2\le4.
\]

If `L=C` is a closed bicoloured cycle through `t\le4` source vertices, every cycle vertex has exactly one third-colour edge. Again internal pairings only reduce the boundary, so

\[
|\delta_T(U)|\le t\le4.
\]

∎

### Corollary 5.3 — disk strict-descent interface

At the coefficient and source-incidence level, a disk Tait side network cannot be an unbounded irreducible serial object. It exposes a two-, three-, or four-port carrier with its complete rank-two root boundary.

The remaining operation is composition-safe transfer across that bounded carrier. No arbitrary Tait multipole classification is required in the disk branch.

---

## 6. Zero Euler characteristic

Assume

\[
\chi(S_T)=0.
\]

### Theorem 6.1 — curvature or complete flatness

Exactly one of the following occurs.

1. Some link has positive curvature, hence Theorem 5.1 supplies a bounded carrier of the same two types.
2. Every link has zero curvature:
   \[
   \boxed{|C|=6\quad(C\in\mathcal C(T)),}
   \]
   \[
   \boxed{|P|=3\quad(P\in\mathcal P(T)).}
   \]

### Proof

If no link has positive curvature, every summand in Theorem 4.1 is nonpositive. Their sum is zero, so every summand is zero. ∎

### Theorem 6.2 — flat annulus/Möbius classification

In the second branch of Theorem 6.1, give every triangle the equilateral Euclidean metric and use the prescribed side gluings. Then:

1. every interior surface vertex has total angle `2\pi`;
2. every boundary surface vertex has total angle `\pi`;
3. `S_T` is a compact flat surface with geodesic boundary;
4. since `S_T` is connected, has nonempty boundary, and has Euler characteristic zero, it is exactly one of:
   - an annulus;
   - a Möbius band.

Its universal cover is a Euclidean strip. The deck generator is:

- a translation in the annulus case;
- a glide reflection in the Möbius case.

### Proof

Six equilateral triangles meet at every interior link and three at every boundary link, giving angles `2\pi` and `\pi`. Hence there are no cone points or boundary corners.

The classification of compact connected surfaces with boundary and Euler characteristic zero leaves exactly the annulus and Möbius band. Developing the flat metric gives a Euclidean strip universal cover; the generator preserves or reverses its orientation according as the quotient is annular or Möbius. ∎

### Corollary 6.3 — topological meaning of the serial alternatives

The completely flat branch has only two topological holonomy types.

1. **Annular translation:** the side network is periodic in the strip direction. This is the natural topological carrier for the existing periodic Kempe ladder and flat-translation branch.
2. **Möbius glide:** one traversal reverses the transverse orientation. This is the natural topological carrier for one index-two orientation class of DDD type.

The second statement is an equality of topological orientation type only. Identification with the physical `D_8` support-label cocycle still requires the established comparison map.

---

## 7. Negative Euler characteristic

If

\[
\chi(S_T)<0,
\]

then either a positive-curvature bounded carrier already exists, or every link is nonpositive and at least one is strictly negative.

By surface classification, negative Euler characteristic means that `S_T` has one of:

- at least three boundary components;
- positive orientable genus;
- enough crosscaps to make the nonorientable Euler characteristic negative.

### Exact conclusion

Negative Euler characteristic is not a new coefficient alphabet. It is a topological complexity certificate carried by a rank-two Tait side network.

### Remaining comparison target

Prove that, in a support-minimal pair-preserving four-port interval, this topology yields one of:

1. a split boundary component and hence a source separator/four-pole;
2. an orientation or homology class mapping to the established DDD/response obstruction;
3. a bounded positive-curvature subcarrier after an admissible Kempe/Petrial move;
4. a strict decrease of Euler complexity under cutting or replacement.

No such source-composition theorem is asserted here.

---

## 8. Unified strict-descent architecture

The matching-plus-Tait side network of a minimal laminar interval may now be organised by the triangle surface `S_T`.

### Positive-curvature branch

\[
\boxed{
\text{short bicoloured link}
\Longrightarrow
\text{source boundary at most four}.}
\]

This subsumes the local two-pole, three-pole, bounded cap, and four-pole alternatives.

### Flat orientable branch

\[
\boxed{
\text{flat annulus}
\Longrightarrow
\text{periodic translation/serial ladder}.}
\]

The remaining task is equality of the outside transition state across one neutral period and contraction of that period.

### Flat nonorientable branch

\[
\boxed{
\text{flat Möbius band}
\Longrightarrow
\text{one orientation-reversing }C_2\text{ class}.}
\]

The remaining task is identification with the physical DDD class and bounded localisation.

### Negative-topology branch

\[
\boxed{
\chi(S_T)<0
\Longrightarrow
\text{separator/genus/holonomy descent target}.}
\]

Thus the earlier five side-signature alternatives are not five unrelated mechanisms. They are the source shadows of curvature and topology on one canonical three-coloured triangle surface.

---

## 9. Relation to the six-output window

The noncrossing return-window theorem gives at most six ordered side outputs in one bounded physical return cell.

The curvature theorem strengthens the semantics of the endpoints when the returning component is Tait-coloured:

- an open bicoloured link gives two endpoints paired in one specific quotient Kempe system;
- a closed bicoloured link gives one actual internal Kempe cycle;
- a flat six-link is one local Euclidean translation cell.

Hence the numerical six-output ceiling is not accidental. It is the zero-curvature valence of an interior vertex in the triangular side surface.

This identifies the correct finite calibration object:

\[
\boxed{
\text{at most six side outputs}
+
\text{one specified bicoloured link/flat period}.}
\]

---

## 10. Trust boundary

### Exact here

- construction of the triangular surface `S_T` from every connected properly three-edge-coloured cubic multipole;
- identification of bicoloured cycles and paths with interior and boundary surface-vertex links;
- the counts `|\mathcal P(T)|=b` and total link length `3n`;
- the Euler-characteristic formula;
- the exact integral Gauss--Bonnet identity;
- existence of a bicoloured path of length at most two or a closed bicoloured cycle of length at most four in every disk side network;
- extraction of a source carrier with edge boundary at most four in the disk branch;
- flatness and annulus/Möbius classification when `\chi=0` and no positive-curvature link exists;
- translation versus glide-reflection topological holonomy.

### Still open

- proof that every physical pair-preserving minimal interval reduces to the disk, flat-annulus, flat-Möbius, or source-separable negative-topology branches in a composition-safe way;
- replacement/gluing across the positive-curvature four-port carrier;
- equality of outside transition states across a neutral annular period;
- identification of Möbius orientation with the physical `D_8` cocycle;
- separator or genus descent for `\chi<0`;
- a global well-founded complexity combining side attachments, surface Euler complexity, interval size, and defect count;
- horizontal/global induction and the global five-support theorem.