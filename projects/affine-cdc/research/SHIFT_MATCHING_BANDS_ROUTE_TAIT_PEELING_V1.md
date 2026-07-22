# Shift-matching bands as route-Tait multipoles

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `e948e19fcfe13ed76b7ebd91936d8e57109ca621`  
**Parents:**

- `projects/affine-cdc/research/KEMPE_BLOCKER_TAIT_SIDE_NETWORK_V1.md`;
- `projects/affine-cdc/research/FOUR_PORT_TAIT_DIPOLE_PEELING_V1.md`;
- `projects/affine-cdc/research/LOW_PORT_TAIT_CORE_GLUING_V1.md`;
- `projects/affine-cdc/research/MINIMAL_RIGID_CYCLE_KEMPE_INTERVAL_EMISSION_V1.md`.

**Status:** exact reclassification and graph-inductive peeling theorem for the isolated private-shift matching sector. The vertices whose blocked side edge is the private root `s=ab` form maximal cubic multipoles with one matching colour and two alternating Kempe-rail colours. These route-Tait bands admit the same one-dipole descent as the complementary Tait side network. Inverse expansion again has only root/equality/DDD outcomes. Failure of bridgelessness under cancellation exposes a cyclic three-cut, and loop degeneration exposes a bounded three-cut neighbourhood. Thus the matching sector is not a separate unbounded composition mechanism.  
**Not implied:** that every residual finite equality/DDD cell is eliminated in the locked profile, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Private root shift and local vertex types

Fix a private root shift

\[
s=ab\in R_5,
\qquad
W=[5]\setminus\{a,b\}.
\]

The safe Kempe subgraph is

\[
H_s=F_a\triangle F_b.
\]

At a cubic source vertex the local root triangle has one of the three established types.

- **Type A:** the complementary triangle on `W`; no incident edge belongs to `H_s`.
- **Type B:**
  \[
  au,av,uv
  \]
  or the `b`-shore analogue; two safe edges and one complementary Tait side edge.
- **Type C:**
  \[
  au,bu,ab
  \]
  for one `u\in W`; two safe edges and one side edge labelled exactly `s=ab`.

Every `s`-edge has Type-C vertices at both ends and is an isolated edge of the blocked graph.

---

## 2. Maximal Type-C bands

Let

\[
X_s
\]

be the set of Type-C vertices.

Construct a multipole `B` as one connected component of the following incidence system:

1. include every `s`-edge with both endpoints in `X_s`;
2. include every safe edge of `H_s` whose two endpoints lie in `X_s`;
3. when a safe edge joins a Type-C vertex to a vertex outside `X_s`, cut it at the Type-C end and retain it as a boundary semiedge.

Every internal vertex of `B` has:

- one `s`-edge;
- two safe incidences.

Thus `B` is a connected cubic multipole. Its boundary consists only of safe semiedges.

We call `B` a **shift-matching band**.

---

## 3. Alternating rail colouring

The subgraph of `B` formed by safe edges has degree at most two. Its components are paths and cycles.

### Lemma 3.1 — closed Type-C runs are even

Every safe-edge cycle contained entirely in Type-C vertices has even length.

### Proof

At a Type-C vertex with local triangle

\[
au,bu,ab,
\]

one safe edge contains support `a` and the other contains support `b`. Therefore traversing the vertex changes shore from `a` to `b` or from `b` to `a`.

Along one safe edge its root label is fixed, so the shore on arrival equals the shore on departure. Hence every successive Type-C vertex flips the shore. A closed run returns to its initial shore only after an even number of flips. ∎

### Theorem 3.2 — route-Tait colouring

Every shift-matching band admits a proper abstract three-edge colouring.

- colour all `s`-edges green;
- on every safe path, alternate red and blue;
- on every safe cycle, alternate red and blue, possible by Lemma 3.1.

Then every internal vertex is incident with exactly one red, one blue, and one green edge.

### Trust note

Red and blue are route colours, not fixed root labels. Their root values may vary along the band. The colouring is used for the graph reducer; root values enter only in the inverse-expansion table.

---

## 4. Boundary alternatives

The boundary of a route-Tait band consists of ends of red--blue paths. Hence its total boundary size is even.

Exactly one of the following occurs.

1. **Closed band:** boundary size zero.
2. **Two-port band:** boundary size two.
3. **Higher-port band:** boundary size at least four.

### Theorem 4.1 — the closed branch is globally soluble

If a shift-matching band has no boundary, it is a connected component of the original source graph.

If the source graph is connected, the band is the whole graph. Its route-Tait colouring is a proper three-edge colouring, hence gives a three-support cycle double cover.

Therefore a five-support counterexample cannot contain a closed shift-matching band.

### Theorem 4.2 — two-port branch

A two-port band has equal root values at its two boundary semiedges in every root-valued flow, by boundary conservation. Its complete boundary profile is universal up to support permutation and it enters the established two-cut gluing theorem.

If the corresponding completion is not bridgeless, the failure is itself a bridge/separator branch.

### Theorem 4.3 — higher-port bands contain a route-Tait dipole

Every connected shift-matching band with at least four boundary semiedges contains a coloured one-dipole in the route-Tait colouring.

### Proof

The general dipole-free boundary theorem for properly three-edge-coloured connected multipoles gives total boundary size at most three. Apply it to the route-Tait colouring of `B`. ∎

---

## 5. Graph-inductive cancellation

Let `e=xy` be a route-Tait one-dipole of colour green, red, or blue. Remove `x,y,e` and reconnect the other two colour pairs.

The cancellation depends only on the abstract cubic graph and route colouring. It does not require the current root values on the reconnected half-edges to agree.

This is the correct direction for minimal-counterexample induction:

1. reduce the source graph by two vertices;
2. obtain an arbitrary five-support root flow on the reduced graph;
3. expand that flow across the cancelled dipole.

### Theorem 5.1 — inverse route-Tait expansion

Let the two reconnected reduced-graph edges have root values

\[
p,q\in R_5.
\]

Reinserting the two cubic vertices forces the dipole edge value

\[
r=p+q.
\]

Exactly one of:

1. `p,q` distinct and intersecting: `r` is a root and expansion succeeds;
2. `p=q`: `r=0`, the bounded equality unit;
3. `p,q` disjoint: `r` is a co-root, the bounded DDD atom.

No fourth lift state occurs.

Thus the use of abstract rail colours introduces no new root-lifting alphabet.

---

## 6. Bridgelessness and separator extraction

Assume the original closed cubic source graph `G` is bridgeless, and perform a nondegenerate dipole cancellation to obtain `G'`.

Let the four non-dipole incidences at the two removed vertices be reconnected in two colour pairs.

### Lemma 6.1 — a new reconnection edge cannot be a bridge

If one new reconnection edge were a bridge of `G'`, its removal would separate its two endpoints while the other reconnection edge lies entirely on one shore. Restoring the dipole and placing its two vertices on that shore leaves exactly one original attachment edge crossing to the opposite shore. That original edge would be a bridge of `G`, contradiction.

### Lemma 6.2 — an old bridge exposes a three-cut

Suppose an old edge `h` becomes a bridge of `G'`. Let

\[
G'-h=A\sqcup B.
\]

Neither new reconnection edge crosses between `A,B`. If both reconnection pairs lie on the same shore, then `h` was already a bridge of `G`. Hence one pair lies in `A` and the other in `B`.

Restoring the dipole, place its two vertices with either shore. Then `h` together with the two attachments from the dipole to the opposite shore forms a three-edge cut in `G`.

If both shores contain cycles, this is a cyclic three-cut and the established three-cut gluing theorem applies. If one shore is acyclic, the dipole lies in a bounded reducible appendage.

### Theorem 6.3 — category-safe alternative

A nondegenerate route-Tait dipole cancellation either:

1. produces a smaller bridgeless cubic graph; or
2. exposes a cyclic three-cut / bounded acyclic separator in the original graph.

Thus loss of bridgelessness is a progress certificate, not a new obstruction.

---

## 7. Loop and multiple-edge degenerations

Parallel edges are allowed in the cubic multigraph category and cause no difficulty.

Suppose a colourwise reconnection would identify two half-edges at the same outside vertex and create a loop. Then the outside vertex is joined to both dipole vertices by the same route colour. Together with the dipole edge, these three vertices form a bounded triangular neighbourhood.

The three remaining incidences of this neighbourhood form an edge cut of size three. Hence the degeneration enters:

- cyclic three-cut gluing, when both shores contain cycles; or
- a bounded cap/appendage reduction.

If both paired incidences are boundary semiedges, the two-vertex neighbourhood is already the bounded two-port degeneration from the ordinary Tait dipole theorem.

No loop is introduced without simultaneously exposing a bounded three-port or two-port interface.

---

## 8. Peeling theorem for the matching sector

### Theorem 8.1 — route-Tait matching-band reduction

Every maximal shift-matching band in a connected bridgeless cubic source graph enters one of:

1. **global three-colour solution:** the band is closed and equals the whole graph;
2. **two-cut gluing:** the band has two boundary semiedges;
3. **strict graph descent:** a route-Tait dipole cancellation produces a smaller bridgeless cubic graph;
4. **three-cut / bounded degeneration:** cancellation exposes a separator;
5. **bounded equality atom:** inverse expansion reaches `p=q`;
6. **bounded DDD atom:** inverse expansion reaches disjoint `p,q`;
7. **root lift:** inverse expansion succeeds and the reduction continues.

Repeated strict descents terminate because every successful cancellation removes two vertices.

### Corollary 8.2 — no isolated matching frontier

The isolated `s`-edge matching sector is not an additional unbounded branch beyond the Tait side network.

Both sectors are governed by the same structural scheme:

\[
\boxed{
\text{coloured dipole descent}
\longrightarrow
\text{root lift / equality / DDD / small cut}.}
\]

---

## 9. Consequence for the minimal laminar interval

The private-shift side decomposition originally separated:

1. complementary-root Tait multipoles;
2. isolated `s`-matching edges.

The first sector is eliminated by the universal four-port Tait peeling theorem. The second sector groups into route-Tait bands and is eliminated by Theorem 8.1.

Therefore an unbounded minimal laminar interval cannot survive by accumulating either kind of side component.

After maximal peeling, the remaining composition data consist only of:

- two-/three-/four-cut interfaces;
- one root dipole/cap;
- one Type-T square cell;
- one zero/equality unit;
- one co-root/DDD unit;
- or a profile-changing route.

The side-network size itself is no longer an unbounded parameter.

---

## 10. Revised descent measure

For a minimal interval `R`, let

\[
N_T(R)
\]

be the number of vertices in complementary Tait components and

\[
N_M(R)
\]

be the number of vertices in shift-matching bands.

Every nonseparating successful dipole cancellation strictly lowers

\[
\boxed{N_T(R)+N_M(R)}
\]

by two. Every failed cancellation leaves the unbounded sector and enters a bounded atom or small-cut branch.

Thus `N_T+N_M` is a valid first strict coordinate for the complete matching-plus-Tait side network.

---

## 11. Trust boundary

### Exact here

- definition of maximal Type-C shift-matching bands;
- evenness of closed Type-C safe runs;
- proper route-Tait colouring;
- closed/two-port/higher-port alternatives;
- dipole existence for every higher-port band;
- graph-inductive inverse expansion with root/equality/DDD table;
- bridgelessness-or-three-cut alternative;
- bounded loop and double-boundary degenerations;
- elimination of the isolated matching sector as an independent unbounded mechanism;
- strict first coordinate `N_T+N_M`.

### Still open

- elimination of the residual finite zero/DDD/Type-T cells in every locked ten-state profile;
- enclosure bookkeeping when several peeled bands share a four-port interval;
- a single global theorem ordering graph reduction, separator decomposition, and horizontal profile escape;
- canonical acceptance and Lean verification;
- the global five-support theorem.
