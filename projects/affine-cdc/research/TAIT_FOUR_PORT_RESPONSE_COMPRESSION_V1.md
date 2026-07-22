# Four-port Tait response compression

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `05cd84b3dfc0e01edbea88165cf77e154794702b`  
**Parents:**

- `projects/affine-cdc/research/TAIT_MULTIPOLE_TRIANGLE_SURFACE_CURVATURE_V1.md`;
- `projects/affine-cdc/research/KEMPE_BLOCKER_TAIT_SIDE_NETWORK_V1.md`;
- `projects/affine-cdc/research/MINIMAL_LAMINAR_INTERVAL_SURGERY_V1.md`;
- `projects/affine-cdc/five-support/cuts-four-poles-and-routing.md`.

**Status:** exact finite boundary-response classification and explicit compression theorem for connected properly three-edge-coloured multipoles with at most four ordered boundary semiedges. Every such fixed Tait response has a canonical representative with at most six internal vertices. The positive-curvature carrier of the Tait-surface theorem is therefore either strictly compressible at the fixed root/route response level or already belongs to a six-vertex finite atom list.  
**Not implied:** that replacing the source region preserves bridgelessness in every ambient context, that a cover obtained from graph minimality has the prescribed boundary root labels, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Boundary response of a Tait multipole

Let `T` be a connected cubic multipole properly edge-coloured by the three nonzero elements

\[
x,y,z
\]

of one binary plane, with

\[
x+y+z=0.
\]

Let

\[
B=(b_1,\ldots,b_k)
\]

be its ordered boundary semiedges, each carrying one of the colours `x,y,z`.

For each colour pair, the corresponding bicoloured submultipole is a union of closed cycles and boundary-to-boundary paths. Hence it induces a perfect matching on the boundary semiedges whose colours lie in that pair.

Write

\[
M_{xy}(T),
\qquad
M_{xz}(T),
\qquad
M_{yz}(T)
\]

for these endpoint pairings.

### Definition 1.1 — ordered Tait response

The **ordered Tait response** is

\[
\boxed{
\mathfrak R(T)
=
\bigl(
\operatorname{col}_B,
M_{xy}(T),
M_{xz}(T),
M_{yz}(T)
\bigr),}
\]

where `col_B` records the colour on each ordered boundary semiedge.

Two fixed coloured multipoles are response-equivalent when their ordered Tait responses agree.

### Theorem 1.2 — route-interface completeness

Response-equivalent multipoles have identical fixed rank-two boundary behaviour:

1. the root label on every boundary semiedge is the same;
2. every one of the three quotient Kempe systems induces the same pairing of the ordered boundary ports;
3. gluing either multipole to the same externally root-labelled context gives the same three scalar transition matchings outside the replaced region.

### Proof

The boundary root values are exactly `col_B`. For a scalar system selecting two of the three nonzero plane values, its components through the multipole are precisely the corresponding bicoloured paths. Their complete effect on the external context is their endpoint matching. Closed internal bicoloured cycles have no boundary effect. ∎

### Trust note

The theorem concerns a fixed root-coloured response. It is not equality of the complete set of all five-support boundary states admitted by the underlying uncoloured multipoles.

---

## 2. Boundary colour conservation

Summing the `F_2^2` flow equations over all internal vertices gives

\[
\boxed{
\sum_{b\in B}\operatorname{col}(b)=0.}
\]

Equivalently, the three boundary colour multiplicities have the same parity.

For `1\le k\le4`, the nonempty possibilities are therefore:

1. `k=2`: two copies of one colour;
2. `k=3`: one copy of each colour;
3. `k=4`: either four copies of one colour or two copies each of two colours.

There is no one-port response.

---

## 3. Two ports

Assume the two boundary colours are both `x`.

Every `xy` path and every `xz` path must pair the two ports. There is no boundary in the `yz` system.

### Canonical representative 3.1 — coloured dipole

Take two cubic vertices, put one `x`-boundary semiedge at each, and join the vertices by one `y`-edge and one `z`-edge.

The two parallel internal edges make the multipole connected and give exactly the forced response.

### Theorem 3.2

Every connected two-port Tait multipole is response-equivalent to this two-vertex dipole.

---

## 4. Three ports

Boundary conservation forces the colours to be

\[
x,y,z
\]

once each.

For each colour pair, the two ports carrying those colours must be paired.

### Canonical representative 4.1 — one Tait vertex

One cubic vertex incident with the three ordered boundary semiedges realises the unique response.

### Theorem 4.2

Every connected three-port Tait multipole is response-equivalent to one cubic vertex.

---

## 5. Four ports with colour multiplicities `2+2`

Let the ordered ports be

\[
x_1,x_2,y_1,y_2.
\]

The `xz` response necessarily pairs

\[
x_1\longleftrightarrow x_2,
\]

and the `yz` response necessarily pairs

\[
y_1\longleftrightarrow y_2.
\]

The only variable datum is the perfect matching `M_{xy}` on the four ports. There are exactly three possibilities.

### 5.1 Cross responses

Suppose `M_{xy}` pairs each `x`-port with one `y`-port.

Choose the desired two `x-y` pairs. For each pair take one cubic vertex incident with those two boundary semiedges. Join the two vertices by one internal `z`-edge.

This two-vertex gadget realises the chosen cross response. The two possible cross matchings give the two possible assignments of the `y`-ports.

### 5.2 Parallel response

Suppose

\[
M_{xy}
=
(x_1x_2)(y_1y_2).
\]

Take four cubic vertices, one for each boundary port.

- join the two `x`-boundary vertices by one internal `y`-edge;
- join the two `y`-boundary vertices by one internal `x`-edge;
- join the four vertices by a perfect matching of two `z`-edges which makes the internal graph connected.

The resulting internal graph is a four-cycle. Its `xy` response is the parallel matching, while the `xz` and `yz` responses pair the equal-colour ports as required.

### Theorem 5.1 — complete `2+2` compression

Every connected four-port Tait multipole with boundary multiplicities `2+2` is response-equivalent to:

- a two-vertex gadget in either cross-response case;
- a four-vertex gadget in the parallel-response case.

All three possible responses occur.

### Minimality

A two-vertex gadget has one boundary `x` and one boundary `y` at each vertex, so it can realise only a cross matching. Therefore the parallel response requires at least four vertices, and the displayed four-cycle is vertex-minimal.

---

## 6. Four ports of one colour

Assume all four ordered ports have colour `x`.

The `xy` system supplies one perfect matching

\[
M_y:=M_{xy}
\]

on the four ports, and the `xz` system supplies another

\[
M_z:=M_{xz}.
\]

There are three perfect matchings on four labelled points. Hence there are exactly

\[
3\cdot3=9
\]

ordered response pairs `(M_y,M_z)`.

The `yz` system has no boundary and contributes only closed internal cycles.

### 6.1 Distinct matchings

Assume

\[
M_y\ne M_z.
\]

Take four cubic vertices, one for each `x`-boundary port. Join them by:

- the two `y`-edges of the matching `M_y`;
- the two `z`-edges of the matching `M_z`.

The union of two distinct perfect matchings on four points is a connected four-cycle. Thus this is a connected properly coloured four-vertex multipole with exactly the prescribed response.

There are six ordered distinct-matching responses.

### 6.2 Equal matchings

Assume

\[
M_y=M_z=M.
\]

Write

\[
M=(p_1p_2)(p_3p_4).
\]

Take four boundary vertices `v_1,v_2,v_3,v_4`, carrying the `x`-ports `p_1,p_2,p_3,p_4`, and two internal vertices `u,w` with no boundary semiedge.

Use the internal edges

\[
u\mathbin{-_x}w,
\]

\[
v_1\mathbin{-_y}v_2,
\qquad
v_3\mathbin{-_y}u,
\qquad
v_4\mathbin{-_y}w,
\]

\[
v_1\mathbin{-_z}u,
\qquad
v_2\mathbin{-_z}w,
\qquad
v_3\mathbin{-_z}v_4.
\]

Then:

- the `xy` paths pair `p_1p_2` and `p_3p_4`;
- the `xz` paths pair the same two pairs;
- the `yz` subgraph contains one closed bicoloured cycle.

This gives a connected six-vertex representative for every equal-matching response.

There are three such responses.

### Theorem 6.1 — complete monochromatic four-port compression

Every connected monochromatic four-port Tait multipole is response-equivalent to:

- a four-vertex cycle when `M_y\ne M_z`;
- the displayed six-vertex gadget when `M_y=M_z`.

### Minimality of the equal case

With four internal vertices and four `x`-boundary semiedges, every vertex carries one boundary semiedge. The remaining `y`- and `z`-edges are two perfect matchings on those four vertices. If the two matchings are equal, their union has two connected components, so the multipole is disconnected.

The number of internal vertices has the same parity as the number of boundary semiedges. Hence the next possible size is six, and the displayed gadget is vertex-minimal.

---

## 7. Uniform six-vertex bound

### Theorem 7.1 — four-port response compression

Let `T` be any connected properly three-edge-coloured cubic multipole with

\[
1\le|\partial T|\le4.
\]

Then there is a connected response-equivalent properly coloured cubic multipole `T_min` with

\[
\boxed{|V(T_{\min})|\le6.}
\]

More precisely:

\[
\begin{array}{c|c|c}
\text{boundary type}&\text{response type}&\text{minimal size ceiling}\\
\hline
x,x&\text{unique}&2\\
x,y,z&\text{unique}&1\\
x,x,y,y&\text{cross}&2\\
x,x,y,y&\text{parallel}&4\\
x,x,x,x&M_y\ne M_z&4\\
x,x,x,x&M_y=M_z&6
\end{array}
\]

Every row is realised by the explicit gadget above.

---

## 8. Consequence for positive-curvature carriers

The Tait triangle-surface curvature theorem supplies, in every disk side network, a source vertex set `U` with

\[
|\delta(U)|\le4.
\]

The restriction to `U` has one ordered Tait response. Theorem 7.1 gives a response-equivalent replacement with at most six internal vertices.

### Corollary 8.1 — strict compression or finite atom

At the fixed root-boundary and three-Kempe-response level, every positive-curvature carrier satisfies exactly one of:

1. its current realisation has more vertices than the canonical response representative and is strictly compressible;
2. it already has at most six vertices and belongs to a finite bounded response class.

Thus no unbounded positive-curvature Tait multipole survives.

### Corollary 8.2 — complete finite calibration surface

The remaining positive-curvature transfer problem is finite. It consists of the displayed two-, three-, four-, and six-vertex gadgets together with their ordered placement among the four route ports.

It is not necessary to classify arbitrary disk Tait multipoles.

---

## 9. Composition boundary

### Exact fixed-witness splicing

Suppose an ambient root-labelled source context meets `T` exactly through its ordered boundary semiedges. Replacing `T` by a response-equivalent canonical gadget and retaining the outside labels gives:

- a root-valued flow on the modified graph;
- the same three quotient Kempe transition matchings at the interface;
- the same external scalar routes.

Conversely, the original fixed Tait flow on `T` expands the canonical response back to the original region whenever the outside boundary labels are the prescribed ones.

### Still required for minimal-counterexample induction

A graph-minimality argument needs additional control:

1. the modified graph must remain in the admissible bridgeless cubic category, or failure must expose a small separator;
2. a cover obtained abstractly on the modified graph must be calibrated to the prescribed boundary root response before expansion;
3. ordered route-port placement must agree with the four-pole matching used by the surrounding interval.

These are source-composition conditions, not missing finite Tait response states.

---

## 10. Unified role in strict descent

Combining the curvature and response theorems gives:

\[
\boxed{
\text{disk Tait side network}
\Longrightarrow
\begin{cases}
\text{strict fixed-response compression},\\
\text{one of finitely many }\le6\text{-vertex atoms}.
\end{cases}}
\]

The genuinely unbounded surviving branches are therefore topological rather than local:

- flat annular translation;
- flat Möbius orientation reversal;
- negative-Euler separator/genus/holonomy.

---

## 11. Trust boundary

### Exact here

- definition and completeness of the fixed ordered Tait response;
- boundary-colour conservation for `k\le4`;
- explicit canonical representatives for every two-, three-, and four-port response;
- exact nine-type classification in the monochromatic four-port case;
- the uniform six-vertex representative bound;
- fixed root-boundary and three-Kempe-response splicing;
- reduction of positive-curvature carriers to strict compression or a finite six-vertex atom list.

### Still open

- preservation of bridgelessness under every canonical replacement;
- forcing the required boundary response from an arbitrary cover of a smaller replacement graph;
- equality between the canonical response and the full five-support four-pole signature;
- elimination/calibration of every finite atom in the locked Type-T/Type-H environment;
- flat-annulus contraction, Möbius/DDD identification, negative-Euler descent;
- horizontal/global induction and the global five-support theorem.