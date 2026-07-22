# Negative-Euler Tait topology and coloured dipole descent

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `59bb9317aa49b848c100ade6fc4fd655704dca8d`  
**Parents:**

- `projects/affine-cdc/research/TAIT_MULTIPOLE_TRIANGLE_SURFACE_CURVATURE_V1.md`;
- `projects/affine-cdc/research/TAIT_FOUR_PORT_RESPONSE_COMPRESSION_V1.md`;
- `projects/affine-cdc/research/FLAT_ANNULUS_TAIT_RESPONSE_REDUCTION_V1.md`;
- `projects/affine-cdc/research/FLAT_MOBIUS_TAIT_ORIENTATION_REDUCTION_V1.md`.

**Status:** exact coloured-dipole reduction for the remaining negative-Euler Tait branch. An internal one-dipole either cancels with no change to the ordered Tait boundary response, or flips exactly one perfect matching on four boundary endpoints. If no one-dipole exists, every bicoloured subgraph is connected; a nonempty boundary then has only two same-colour ports or three ports of the three distinct colours, and its ordered Tait response is unique. Thus negative topology carries no unbounded boundary-routing alphabet at the fixed Tait-response level.  
**Not implied:** that internal surface homology is invisible to the complete five-support boundary profile, preservation of bridgelessness under every cancellation, composition-safe elimination of every two-/three-port topological core, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Coloured residues

Let `T` be a finite connected properly three-edge-coloured cubic multipole with colours

\[
\{i,j,k\}.
\]

For a colour pair, write

\[
T_{jk}
\]

for the submultipole consisting of the `j`- and `k`-coloured edges and semiedges. Every source vertex has degree two in `T_{jk}`, so every component is a closed cycle or an open boundary-to-boundary path.

The components of `T_{jk}` are the surface vertices of colour `i` in the triangle-surface model.

---

## 2. One-dipoles

Let

\[
e=uv
\]

be an ordinary internal edge of colour `i`.

### Definition 2.1 — colour-i one-dipole

The edge `e` is an **`i`-dipole** when `u` and `v` lie in distinct components of `T_{jk}`.

At `u`, let the other two incidences have colours `j,k`; do the same at `v`. Cancel `e,u,v` and pair the two remaining `j`-incidences and the two remaining `k`-incidences colourwise.

When one incidence is a boundary semiedge and the other is an ordinary edge, the boundary semiedge is transported to the far endpoint. If both paired incidences are boundary semiedges, the two-vertex neighbourhood is already a bounded two-port carrier and is retained as that branch rather than cancelled inside the cubic category.

Denote the ordinary cancellation by

\[
T/e.
\]

### Theorem 2.2 — surface dipole cancellation

Away from the bounded double-boundary degeneration, `T/e` is a properly three-edge-coloured cubic multipole with two fewer source vertices and the same boundary colour multiset. Its triangle surface is homeomorphic to the triangle surface of `T`.

### Proof

The two triangles corresponding to `u,v` share their `i`-side. The dipole hypothesis says that their opposite `i`-coloured surface vertices are distinct. Removing the interiors of the two triangles and identifying the two exposed `j`-sides and the two exposed `k`-sides is the standard cancellation of a triangular two-face disc. It changes the triangulation but not the underlying surface. The graph operation is precisely the dual colourwise reconnection described above. ∎

### Corollary 2.3

For the Euler coordinates,

\[
n\longmapsto n-2
\]

and the number of closed `jk` residues decreases by one, so the exact Euler characteristic remains unchanged.

---

## 3. Effect on the three boundary matchings

The ordered Tait response consists of the boundary colour word and the endpoint matchings

\[
M_{ij},
\qquad
M_{ik},
\qquad
M_{jk}.
\]

### Theorem 3.1 — two matchings are rigid

Cancelling an `i`-dipole leaves

\[
M_{ij}
\qquad\text{and}\qquad
M_{ik}
\]

unchanged.

### Proof

In the `ij` system, the local path through the dipole has colour word

\[
jij.
\]

After cancellation it is replaced by one `j`-edge with the same two endpoints. Thus every `ij` boundary pairing is unchanged. The `ik` argument is identical. ∎

Let `R_u,R_v` be the two distinct `jk` residues containing `u,v`.

### Theorem 3.2 — complementary response dichotomy

Exactly one of the following occurs.

1. **At most one of `R_u,R_v` is open.**  
   Cancellation leaves the boundary matching `M_{jk}` unchanged.

2. **Both `R_u,R_v` are open paths.**  
   Their four boundary endpoints retain the same set but are reconnected according to the other perfect matching determined by colourwise splicing. All other `jk` endpoint pairs are unchanged.

### Proof

If both residues are closed, the reconnection changes only closed internal cycles. If one is closed and one is open, the splice inserts or removes a closed detour from the open path but leaves its two boundary endpoints paired.

If both are open, each contributes one pair of boundary endpoints. Before cancellation the pairs are the endpoints of `R_u` and `R_v`. The colourwise reconnection joins one half of the first path to one half of the second in each of the two colours, producing the crossed pairing on the same four endpoints. ∎

### Corollary 3.3 — response-preserving strict descent

If an `i`-dipole has at most one open complementary residue, then

\[
\boxed{
\mathfrak R(T/e)=\mathfrak R(T),
\qquad
|V(T/e)|=|V(T)|-2.}
\]

This is a strict ordered-Tait-response descent.

### Corollary 3.4 — bounded route-change carrier

If both complementary residues are open, the entire response change is one matching flip on exactly four ordered boundary endpoints.

Thus this branch is already a four-port transfer state of the kind classified by the four-port Tait-response theorem and the Type-T/Type-H routing geometry.

There is no larger response disturbance.

---

## 4. Dipole-free connected multipoles

Assume `T` has no colour-i one-dipole for any of the three colours.

### Theorem 4.1 — connected residue theorem

Each of

\[
T_{ij},
\qquad
T_{ik},
\qquad
T_{jk}
\]

is connected.

### Proof

Suppose `T_{jk}` had two distinct components. Since the full multipole `T` is connected, some ordinary `i`-edge must join a vertex of one component to a vertex of the other. That edge is an `i`-dipole, contrary to assumption. ∎

A connected two-regular multipole component is either one closed cycle or one open path with exactly two boundary endpoints.

Let

\[
b_i,b_j,b_k
\]

be the numbers of boundary semiedges of the three colours.

### Corollary 4.2 — pair endpoint equations

\[
\boxed{
 b_i+b_j,
 \quad
 b_i+b_k,
 \quad
 b_j+b_k
 \in\{0,2\}.}
\]

The binary flow boundary law also gives

\[
b_i\equiv b_j\equiv b_k\pmod2.
\]

### Theorem 4.3 — complete nonempty boundary classification

If the boundary is nonempty, then, up to permutation of colours, exactly one of the following occurs:

1. two same-colour ports:
   \[
   (b_i,b_j,b_k)=(2,0,0);
   \]
2. one port of each colour:
   \[
   (b_i,b_j,b_k)=(1,1,1).
   \]

### Proof

Adding the three pair endpoint counts gives

\[
2(b_i+b_j+b_k)\le6,
\]

so the total boundary size is at most three. Equal parity of the three counts leaves precisely the displayed nonempty possibilities. ∎

### Corollary 4.4 — no boundary-routing entropy

In the two-port case, both bicoloured systems containing the boundary colour pair the two ports, and the third bicoloured system is closed. The ordered response is unique.

In the three-port case, each bicoloured system pairs the unique two ports carrying its two colours. The ordered response is again unique.

Thus a dipole-free connected multipole with nonempty boundary has no variable terminal matching.

---

## 5. Negative Euler coordinates of the contracted cores

The dipole-free cores may still carry internal topology.

### Two-port core

For boundary type `(2,0,0)`, exactly one bicoloured residue is closed. Hence

\[
\chi(S_T)
=1+\frac{2-n}{2}
=2-\frac n2.
\]

Negative Euler characteristic begins at

\[
n\ge6.
\]

### Three-port core

For boundary type `(1,1,1)`, all three bicoloured residues are open, so

\[
\chi(S_T)
=\frac{3-n}{2}.
\]

Negative Euler characteristic begins at

\[
n\ge5.
\]

### Interpretation

All remaining negative topology is internal to a two- or three-port multipole whose root boundary and all three Tait endpoint pairings are fixed uniquely.

It cannot support an unbounded family of boundary routing states.

---

## 6. Unified negative-Euler reduction

### Theorem 6.1 — dipole/flip/core trichotomy

Every connected properly three-edge-coloured multipole with nonempty boundary satisfies at least one of:

1. **strict response descent:** it has a one-dipole with at most one open complementary residue, and cancellation preserves the full ordered Tait response while removing two source vertices;
2. **bounded matching flip:** it has a one-dipole between two open complementary residues, and cancellation changes exactly one perfect matching on four boundary endpoints;
3. **contracted topology core:** all bicoloured subgraphs are connected, the boundary has type `(2,0,0)` or `(1,1,1)`, and the ordered Tait boundary response is unique.

### Consequence 6.2

At the fixed ordered-Tait-response level, negative Euler topology supplies no fourth and no unbounded boundary-composition mechanism.

The only possible additional invariant is an internal surface homology/orientation class invisible to the three endpoint matchings.

---

## 7. Relation to strict descent

The previous curvature architecture may now be sharpened.

### Positive curvature

A short link gives a four-port carrier, then a response representative with at most six vertices.

### Flat annulus/Möbius

Response compression leaves a minimal serial strip and then a bounded return cell.

### Negative Euler

Coloured dipoles give strict two-vertex descent until either:

- a four-port matching flip appears;
- or all topology is trapped in a two-/three-port contracted core with unique route response.

Hence the source-composition frontier is no longer a general negative-genus multipole. It is the finite comparison question:

\[
\boxed{
\text{does internal surface homology of a two-/three-port core}
\text{ survive in the complete five-support boundary profile?}}
\]

If not, the core compresses to the canonical one-/two-vertex response gadget. If yes, that survival must map to the already established response/DDD holonomy language.

---

## 8. Trust boundary

### Exact here

- graph and surface definition of a coloured one-dipole;
- topology-preserving two-vertex cancellation;
- invariance of the two matchings containing the dipole colour;
- exact preserve/flip dichotomy for the complementary matching;
- four-endpoint ceiling of every matching flip;
- connectedness of all bicoloured residues in a dipole-free connected multipole;
- complete two-/three-port boundary classification;
- uniqueness of the ordered Tait boundary response of every contracted core;
- reduction of negative topology to strict dipole descent, bounded four-port flip, or a low-port pure topology core.

### Still open

- treatment of the bounded double-boundary degeneration inside the exact cubic replacement category;
- preservation of bridgelessness and the ambient minimal-counterexample class under arbitrary dipole cancellation;
- whether internal topology of a contracted two-/three-port core affects the complete five-support boundary profile;
- explicit map from any surviving internal class to the physical DDD/response obstruction;
- global well-founded complexity, horizontal induction, and the five-support theorem.