# Flat Tait annuli: response compression and the minimal serial normal form

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `d9ab209d27c7da89982afde38cbbe8947790a764`  
**Parents:**

- `projects/affine-cdc/research/TAIT_MULTIPOLE_TRIANGLE_SURFACE_CURVATURE_V1.md`;
- `projects/affine-cdc/research/TAIT_FOUR_PORT_RESPONSE_COMPRESSION_V1.md`;
- `projects/affine-cdc/research/NONCROSSING_SIDE_SIGNATURE_WINDOW_V1.md`;
- `projects/affine-cdc/five-support/periodic-kempe-ladders.md`.

**Status:** exact fixed-response reduction for the completely flat annular Tait branch. Every flat annulus has monochromatic boundary, and the two nontrivial boundary matchings form exactly two alternating cycles, one per annular boundary component. If `b` is the total number of boundary semiedges and `n` the number of source vertices, then `n>=b+2`; the same ordered Tait response has a connected canonical representative with exactly `b+2` vertices. Equality forces a minimal two-corolla serial annulus joined by one two-vertex colour bridge. In a noncrossing four-port environment, an unbounded minimal serial annulus contains a bounded same-component return cell on at most six consecutive boundary ports.  
**Not implied:** full five-support boundary-profile equivalence, preservation of bridgelessness under every response replacement, contraction of the bounded return cell, identification of its finite holonomy class, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Flat annular setup

Let `T` be a connected properly three-edge-coloured cubic multipole with colour set

\[
\{x,y,z\}.
\]

Let

\[
S_T
\]

be its coloured triangle surface. Assume that `S_T` is completely flat and homeomorphic to an annulus. Thus every interior surface-vertex link contains six triangles and every boundary surface-vertex link contains three triangles.

Write

\[
n=|V(T)|,
\qquad
b=|\partial T|.
\]

The two boundary components of `S_T` are denoted

\[
\partial_0S_T,
\qquad
\partial_1S_T.
\]

---

## 2. Monochromatic straight boundaries

Give every triangle of `S_T` the equilateral Euclidean metric. Complete flatness makes the universal cover a Euclidean strip triangulated by the regular triangular tiling.

### Theorem 2.1 — monochromatic annular boundary

There is one colour, say `x`, such that every boundary edge of `S_T`, equivalently every boundary semiedge of `T`, has colour `x`.

### Proof

At every boundary surface vertex, exactly three equilateral triangles meet, so the interior angle is `pi`; the boundary has no corner and develops to a straight line in the triangular tiling. A straight edge line of the properly side-coloured triangular tiling uses one fixed edge direction and hence one fixed side colour.

The two boundary lines of a Euclidean strip are parallel, so they have the same direction and the same colour. Pulling the development back to `S_T` gives the result. ∎

### Corollary 2.2

The `xy` and `xz` bicoloured systems induce perfect matchings

\[
M_y:=M_{xy},
\qquad
M_z:=M_{xz}
\]

on all `b` ordered boundary ports. The `yz` system has no boundary.

---

## 3. Boundary cycles are the response cycles

At a boundary surface vertex, the two incident boundary edges have colour `x`. Its interval link in `T` is either an `xy` path or an `xz` path joining precisely the two `x`-boundary semiedges meeting at that surface vertex.

Moving around one boundary component, these two kinds of surface vertices alternate.

### Theorem 3.1 — two response cycles

The graph on the boundary ports with edge set

\[
M_y\cup M_z
\]

is a disjoint union of exactly two alternating even cycles:

\[
\boxed{
M_y\cup M_z
=C_0\sqcup C_1,}
\]

where `C_j` is the cyclic sequence of `x`-boundary semiedges on `\partial_jS_T`.

### Proof

Every boundary port is incident with one `M_y` edge and one `M_z` edge, so the union is a disjoint union of alternating cycles. The matching edge at a boundary surface vertex joins the two boundary semiedges adjacent at that same surface vertex. Consequently following alternating matching edges is exactly following the corresponding surface boundary component. Since an annulus has two boundary components, exactly two cycles occur. ∎

### Corollary 3.2 — simultaneous noncrossing order

If the boundary ports of one component `C_j` are placed on a line or circle so that both `M_y` and `M_z` are noncrossing, their order is the cycle order of `C_j` up to reversal.

### Proof

The union `M_y union M_z=C_j` is a cycle, hence a 2-connected outerplanar graph. Its outer cyclic order is unique up to reversal. ∎

---

## 4. The parity lower bound

Every source vertex of `T` is incident with at most one boundary semiedge, so

\[
n\ge b.
\]

The cubic degree equation

\[
3n=2e+b
\]

implies

\[
n\equiv b\pmod2.
\]

### Theorem 4.1 — connected annular lower bound

\[
\boxed{n\ge b+2.}
\]

### Proof

If `n=b`, every source vertex is incident with one `x`-boundary semiedge. Hence there is no internal `x`-edge, and the internal graph is exactly the union of the `y`- and `z`-matchings `M_y union M_z`. By Theorem 3.1 this graph has two connected components, contradicting connectedness of `T`.

Since `n` and `b` have the same parity, the next possibility is `n>=b+2`. ∎

---

## 5. Canonical connected response representative

Start with one boundary vertex for every ordered boundary port. Attach its prescribed `x`-semiedge. On the vertices belonging to the two response cycles `C_0,C_1`, insert the `y`- and `z`-edges prescribed by `M_y,M_z`. This gives two disconnected alternating corollas.

Choose one `y`-edge

\[
a_1a_2
\]

of `C_0` and one `z`-edge

\[
b_1b_2
\]

of `C_1`. Delete these two edges. Add two new vertices `u,v` and the edges

\[
u\mathbin{-_x}v,
\]

\[
a_1\mathbin{-_y}u,
\qquad
v\mathbin{-_y}a_2,
\]

\[
b_1\mathbin{-_z}u,
\qquad
v\mathbin{-_z}b_2.
\]

Call the resulting connected multipole

\[
A(M_y,M_z).
\]

### Theorem 5.1 — annular response compression

`A(M_y,M_z)` is connected, properly three-edge-coloured, has the same ordered boundary Tait response as `T`, and satisfies

\[
\boxed{|V(A(M_y,M_z))|=b+2.}
\]

### Proof

Every boundary vertex retains one edge of each of the three colours. Each of `u,v` is incident with one `x`, one `y`, and one `z` edge. The new `x`-edge joins the two corolla pieces through the spliced `y`- and `z` routes, so the multipole is connected.

In the `xy` system, the deleted `y`-edge `a_1a_2` is replaced by the path

\[
a_1-u-v-a_2
\]

with colour word `yxy`, so the endpoint pairing `M_y` is unchanged. The `z`-splice lies outside the `xy` system. Similarly, in the `xz` system, `b_1b_2` is replaced by a `zxz` path and `M_z` is unchanged. Boundary colours are unchanged. ∎

### Corollary 5.2 — strict fixed-response descent

If

\[
n>b+2,
\]

then the flat annular Tait multipole has a connected response-equivalent replacement with strictly fewer source vertices.

Thus no nonminimal-width flat annulus survives at the fixed root-boundary and three-Kempe-response level.

---

## 6. Equality and the minimal serial annulus

Assume

\[
n=b+2.
\]

Then exactly two source vertices have no boundary semiedge. Equivalently, there are exactly two internal `x` half-edges and hence exactly one internal `x`-edge.

### Theorem 6.1 — equality normal form

Every equality case is response-equivalent, by a boundary-order-preserving colour isomorphism, to the canonical annulus `A(M_y,M_z)`.

More concretely:

1. deleting the unique internal `x`-edge leaves two `y/z` alternating boundary corollas;
2. the two endpoints of the `x`-edge splice one `y`-edge of one corolla and one `z`-edge of the other;
3. no additional internal layer or branching remains.

### Proof

The two vertices without boundary semiedges are the endpoints of the unique internal `x`-edge. Each has one incident `y`-edge and one incident `z`-edge.

The `y` half-edges at these two vertices must splice one `M_y` edge inside a single response cycle; otherwise the `xy` endpoint pairing would join the two cycles, contradicting Theorem 3.1. The same holds for the two `z` half-edges.

If both splices occurred in the same response cycle, the other corolla would remain disconnected from the unique `x`-edge. Therefore one colour splice occurs in `C_0` and the other in `C_1`. This is exactly the construction of `A(M_y,M_z)`, up to exchanging `y,z` and the two boundary components. ∎

### Definition 6.2 — minimal serial annulus

The equality normal form is the **minimal serial annulus** for its ordered response.

Its size may grow only because the two alternating boundary corollas have many ports. There is no hidden interior Tait width.

---

## 7. Bounded return cells in a long minimal annulus

Place a minimal serial annulus inside a support-minimal pair-preserving four-port interval. The surviving side partition is noncrossing. By Corollary 3.2, on each annular boundary component the interval order of its attachments agrees with the alternating corolla order up to reversal; otherwise one of the matching edges crosses and gives route escape.

### Theorem 7.1 — six-port annular return cell

Exactly one of the following holds.

1. The total side signature on the relevant boundary corolla has at most four outputs.
2. There are two consecutive-in-reduced-order boundary ports belonging to the same outside component such that the corolla arc between them contains at most six consecutive boundary ports.

### Proof

Apply the noncrossing four-port return-window theorem to the ordered ports on the boundary corolla. The order comparison above converts its bounded window directly into a consecutive arc of the alternating response cycle. ∎

### Corollary 7.2 — bounded source size of the return arc

The internal annular part of the return cell contains at most six boundary vertices and at most the two bridge vertices if the chosen arc meets the unique colour splice. Hence its Tait source contribution has at most

\[
\boxed{8}
\]

vertices.

If the arc avoids the splice, it has at most six vertices and is a pure alternating corolla segment.

### Corollary 7.3 — no unbounded flat-annulus transfer language

Every flat annular branch satisfies one of:

1. strict fixed-response vertex compression;
2. a globally bounded four-output signature;
3. an at-most-eight-vertex same-component return cell in the minimal serial annulus;
4. a crossing matching and hence route/profile escape.

Thus an unbounded flat annulus does not survive as a new composition language. Its remaining obstruction is finite return-cell calibration.

---

## 8. Relation to periodic Kempe ladders

The two alternating corollas are the boundary rails of the flat strip. The unique `x`-bridge is the minimal transverse connector. In the universal cover, translation along either response cycle generates the periodic serial direction.

The existing two-cell neutral block of the periodic-ladder theorem is the local six-output translation cell appearing when a return window spans two consecutive three-port periods.

The present theorem adds the missing global statement:

- arbitrary annular width is strictly removable at fixed response;
- the equality case has no hidden width and is exactly serial;
- long serial behaviour contains a bounded return cell before any unbounded state comparison is needed.

Equality of the outside transition state across that return cell remains the finite calibration target.

---

## 9. Composition and trust boundary

### Exact here

- monochromaticity of both flat annular boundaries;
- identification of `M_y union M_z` with exactly the two annular boundary cycles;
- simultaneous noncrossing order uniqueness up to reversal;
- parity lower bound `n>=b+2`;
- explicit connected response-equivalent representative of size `b+2`;
- equality classification as the minimal two-corolla serial annulus;
- localisation of every long minimal serial annulus to a return arc of at most six ports and at most eight annular source vertices.

### Still open

- preservation of bridgelessness and the ambient minimal-counterexample category under the `b+2` replacement;
- promotion from fixed Tait response to the complete five-support four-pole profile;
- composition-safe contraction of the at-most-eight-vertex return cell;
- calibration of the outside same-component transition state;
- flat Möbius/physical `D_8` identification;
- negative-Euler separator or genus descent;
- a global well-founded complexity and the five-support theorem.