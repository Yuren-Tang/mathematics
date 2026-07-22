# The Möbius-to-disk orientation switch in the DDD branch

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `aa9fcdb66a92d3857124859d64f4bda427804cab`  
**Parents:**

- `projects/affine-cdc/research/FLAT_MOBIUS_TAIT_ORIENTATION_REDUCTION_V1.md`;
- `projects/affine-cdc/research/TAIT_SURFACE_DDD_ORIENTATION_COMPARISON_V1.md`;
- `projects/affine-cdc/research/TAIT_FOUR_PORT_RESPONSE_COMPRESSION_V1.md`;
- `projects/affine-cdc/research/DDD_ROUTE_ORIENTATION_COVER_V1.md`.

**Status:** exact fixed-response graph switch which changes the canonical Möbius orientation class to the disk class. The crossed and parallel two-vertex splices have identical ordered boundary root colours and identical three Tait endpoint matchings; they differ only by the first Stiefel--Whitney/DDD orientation bit. The parallel splice subsequently contracts to the boundary corolla, removing the two bridge vertices. Thus every canonical odd-return cell has an explicit orientation-first, vertex-second descent at the fixed response level.  
**Not implied:** that every ambient locked profile admits the switch, elimination of the unique bad route when the switch is blocked, preservation of bridgelessness without a separator branch, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. One ordered response cycle

Let all ordered boundary ports have root colour `x`, and let

\[
M_y,
\qquad
M_z
\]

be two perfect matchings whose union is one alternating cycle

\[
C_B=M_y\cup M_z.
\]

Choose one `y`-edge

\[
a_1a_2\in M_y
\]

and one `z`-edge

\[
b_1b_2\in M_z.
\]

Deleting these two edges cuts `C_B` into two paths on the four exposed endpoints.

Add two new vertices `u,v` and one edge

\[
u\mathbin{-_x}v.
\]

There are two colour-preserving ways to reconnect the four `y/z` incidences while keeping the endpoint pairs `a_1a_2` in the `xy` system and `b_1b_2` in the `xz` system.

---

## 2. Parallel and crossed splices

### Parallel splice

Use

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

Denote the resulting multipole by

\[
P(M_y,M_z).
\]

### Crossed splice

Use

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

Denote the resulting multipole by

\[
X(M_y,M_z).
\]

Both have `b+2` source vertices.

---

## 3. Boundary response is unchanged

### Theorem 3.1 — response equality

\[
\boxed{
\mathfrak R(P(M_y,M_z))
=
\mathfrak R(X(M_y,M_z))
=
(x^b,M_y,M_z).}
\]

### Proof

In both splices, the deleted `y`-edge `a_1a_2` is replaced in the `xy` subgraph by a `yxy` path with the same endpoints. The assignment of the `z` half-edges at `u,v` is invisible to the `xy` system.

Similarly the deleted `z`-edge `b_1b_2` is replaced in the `xz` subgraph by a `zxz` path with the same endpoints, independently of the `y` assignment. The ordered boundary colours remain all `x`. ∎

Thus ordinary Tait route data cannot distinguish the two splices.

---

## 4. The complementary residue detects the switch

The `yz` subgraph sees both assignments.

### Theorem 4.1 — smoothing dichotomy

1. In the parallel splice, the two paths of `C_B-\{a_1a_2,b_1b_2\}` close separately. Hence the `yz` subgraph has two closed components.
2. In the crossed splice, the two paths join into one closed component. Hence the `yz` subgraph has one closed component.

### Proof

After deleting one `y`-edge and one `z`-edge from one cycle, the four endpoints inherit one pairing from the two remaining path components. The parallel reconnection uses that pairing and closes the two paths separately; the crossed reconnection uses the other pairing and joins them into one cycle. ∎

---

## 5. Surface topology

Both splices have

\[
n=b+2
\]

triangles and one boundary component.

For the parallel splice, the number of closed bicoloured residues is two. Therefore

\[
\chi
=2+\frac{b-(b+2)}2
=1.
\]

For the crossed splice, that number is one. Therefore

\[
\chi
=1+\frac{b-(b+2)}2
=0.
\]

### Theorem 5.1 — disk/Möbius pair

\[
\boxed{
S_{P(M_y,M_z)}\cong D^2,
\qquad
S_{X(M_y,M_z)}\cong\text{Möbius band}.}
\]

### Proof

Both surfaces are connected and have one boundary component. Euler characteristic one gives a disk. Euler characteristic zero with one boundary component gives a Möbius band. ∎

### Corollary 5.2 — orientation toggle

The replacement

\[
X(M_y,M_z)
\longmapsto
P(M_y,M_z)
\]

preserves the full ordered Tait response and changes only

\[
\boxed{
 w_1:\ 1\longmapsto0.}
\]

By the Tait-surface/DDD comparison theorem, this is equivalently

\[
\boxed{
\kappa:\ 1\longmapsto0}
\]

for the crossed-route orientation character.

---

## 6. Vertex descent after orienting

Let

\[
D(M_y,M_z)
\]

be the boundary corolla with one vertex per port and internal `y,z` edges given by `M_y,M_z`. Since their union is one cycle, this multipole is connected and has `b` vertices.

### Theorem 6.1 — disk contraction

\[
\boxed{
\mathfrak R(D(M_y,M_z))
=
\mathfrak R(P(M_y,M_z)).}
\]

Hence after the orientation switch, the two bridge vertices may be removed at fixed response:

\[
P(M_y,M_z)
\longmapsto
D(M_y,M_z),
\]

and

\[
|V|:(b+2)\longmapsto b.
\]

### Corollary 6.2 — lexicographic descent

For the complexity coordinate

\[
(\omega,|V|)
\]

with the nonorientable value ordered above the orientable value, the canonical odd-return cell admits

\[
\boxed{
(1,b+2)
\longmapsto
(0,b+2)
\longmapsto
(0,b).}
\]

The first step removes the DDD orientation obstruction; the second removes two source vertices.

---

## 7. Physical interpretation

The crossed splice is the canonical flat Möbius/odd-DDD cell. Choosing one globally oriented crossed route trivialises the DDD cocycle on the orientation cover.

The parallel splice is the descended orientable realization with the same unordered route response.

### Theorem 7.1 — explicit evenisation of an odd return

At the fixed boundary root and three-Kempe-response level, every canonical odd DDD return has an explicit response-preserving replacement whose orientation character is even.

There is no need to search over an arbitrary family of Möbius gadgets.

### Blocking alternatives

If the ambient physical four-pole does not permit the switch, the failure cannot be a new orientation value. It must be witnessed by the already classified finite data:

1. the unique bad unordered route;
2. a zero/equality relation failure;
3. a co-root/DDD crossed-resolution atom;
4. a separator or profile-changing attachment.

This last statement is the composition target; the fixed-response graph switch itself is exact.

---

## 8. Relation to partial Petrials

On the triangle surface, exchanging the parallel and crossed reconnection inserts or removes one half-twist in the two-triangle bridge band. It is the local partial-Petrial operation on the orientation line.

Under the comparison

\[
w_1=\kappa,
\]

this partial Petrial is exactly the operation changing the crossed-route orientation descent class by the generator of `C_2`.

---

## 9. Trust boundary

### Exact here

- construction of the parallel and crossed splices;
- equality of their ordered boundary colours and all three Tait endpoint matchings;
- one-versus-two complementary closed-residue count;
- disk versus Möbius topology;
- exact change `w_1=kappa:1 -> 0`;
- subsequent two-vertex response compression to the boundary corolla;
- lexicographic orientation/vertex descent at the fixed-response level.

### Still open

- proof that every locked ambient complete profile admits the orientation switch or exposes one of the listed finite blockers;
- preservation of bridgelessness without a separator branch;
- simultaneous compatibility with the second crossed route and bad-sheet exchange;
- global packaging of this local descent with all other atoms;
- horizontal induction and the global five-support theorem.