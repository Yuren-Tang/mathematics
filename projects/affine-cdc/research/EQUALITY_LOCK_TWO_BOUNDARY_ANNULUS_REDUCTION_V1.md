# Equality Tait response has two boundary components and one annular core

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `ebd2203e94ea13c4d2688c868551159f45c1bbb5`.

**Parents:**

- `EQUALITY_LOCK_IDENTITY_HEXAGON_CORE_V1.md`;
- `EQUALITY_LOCK_PRIVATE_MATCHING_TAIT_DECOMPOSITION_V1.md`;
- `TAIT_MULTIPOLE_TRIANGLE_SURFACE_CURVATURE_V1.md`;
- `FLAT_ANNULUS_TAIT_RESPONSE_REDUCTION_V1.md`;
- `FLAT_MOBIUS_TAIT_ORIENTATION_REDUCTION_V1.md`;
- `NEGATIVE_EULER_TAIT_DIPOLE_REDUCTION_V1.md`;
- `FOUR_PORT_TAIT_DIPOLE_PEELING_V1.md`.

**Status:** exact topological reduction of the connected pure-gauge equality Tait core. Its four boundary semiedges have one colour and its two open bicoloured responses are the same matching. The boundary of the associated triangle surface therefore has exactly two components. Consequently positive Euler characteristic and the flat Möbius branch are impossible; zero Euler characteristic is exactly one annulus. The minimal flat annulus has six source vertices and is the identity hexagon. Every negative-Euler equality core admits response-preserving dipole descent until a bounded four-port matching flip or boundary degeneration is exposed. Thus no unbounded topological species remains in the equality core.

**Not implied:** promotion from fixed Tait response to the complete five-support profile under arbitrary replacement, cover-independent inverse transfer through a peel/Pachner history, elimination of every bounded matching-flip event in the original root-labelled carrier, global proof-DAG closure, canonical acceptance, Lean verification, manuscript integration, or the global five-support theorem.

---

## 1. Connected equality Tait core

Fix one adjacent-channel projection of a pure-gauge equality lock. After suppressing private-matching subdivision vertices, let

\[
T
\]

be its connected properly three-edge-coloured four-port core with colours

\[
\{r,s,t\}.
\]

The four ordered boundary semiedges all have colour `r`, and the exact marked response is

\[
\boxed{
(r,r,r,r;\ M_{rs},M_{rt},M_{st})
=(r^4;M,M,\varnothing).}
\]

Here `M` is one perfect matching of the four ports.

Let

\[
S_T
\]

be the coloured triangle surface of `T`.

---

## 2. Boundary components from open bicoloured matchings

Because every boundary semiedge has colour `r`, every boundary surface vertex is the interval link of either:

- one open `rs` path; or
- one open `rt` path.

Following one boundary component alternates between an `rs` path and an `rt` path. Therefore the boundary-component graph on the four ports has edge multiset

\[
M_{rs}\sqcup M_{rt}.
\]

### Theorem 2.1 — boundary-cycle dictionary

The connected components of

\[
M_{rs}\sqcup M_{rt}
\]

are canonically the boundary components of `S_T`.

This statement does not require flatness.

### Proof

At one boundary semiedge, the two boundary corners are continued through the unique open bicoloured paths containing `r` with the other colours `s` and `t`. Moving along the surface boundary therefore alternates exactly between the endpoint pairings of these two path systems. Conversely every alternating matching cycle traces one surface boundary component. ∎

### Corollary 2.2 — equality gives two boundary components

Since

\[
M_{rs}=M_{rt}=M,
\]

the multigraph

\[
M\sqcup M
\]

is the disjoint union of two doubled matching edges. Hence

\[
\boxed{|\pi_0(\partial S_T)|=2.}
\]

The two blocks of the locked terminal matching are exactly the two surface boundary components.

---

## 3. Surface classification

A connected compact surface with exactly two boundary components has:

### Orientable case

\[
\chi=2-2g-2=-2g\le0.
\]

Equality holds exactly for

\[
g=0,
\]

i.e. the annulus.

### Nonorientable case

With `k>=1` crosscaps,

\[
\chi=2-k-2=-k<0.
\]

### Theorem 3.1 — equality topology dichotomy

Exactly one of:

1. \[
   \chi(S_T)=0
   \]
   and `S_T` is an annulus;
2. \[
   \chi(S_T)<0.
   \]

In particular:

\[
\boxed{
S_T\text{ is never a disk and never a Möbius band}.}
\]

Thus the topological orientation bit of the flat Möbius line cannot occur in a double-equal equality response.

---

## 4. The completely flat equality core

Assume every interior bicoloured link has length six and every boundary link has length three. Then `S_T` is flat and has Euler characteristic zero. By Theorem 3.1 it is an annulus.

Let

\[
b=4
\]

be the number of boundary semiedges and

\[
n=|V(T)|.
\]

The flat-annulus lower bound gives

\[
\boxed{n\ge b+2=6.}
\]

### Theorem 4.1 — identity-hexagon normal form

The ordered response

\[
(r^4;M,M,\varnothing)
\]

has a connected flat representative with exactly six source vertices. Equality

\[
n=6
\]

forces the minimal serial annulus and is boundary-order- and colour-isomorphic to the six-vertex identity hexagon.

### Proof

The flat-annulus equality theorem says that a minimal annulus consists of two alternating boundary corollas, one for each boundary-response cycle, joined by one two-vertex transverse colour bridge. For four ports and equal matchings, each corolla is one doubled matching block. The resulting six-vertex graph is exactly the canonical equality identity hexagon. ∎

### Corollary 4.2 — complete bounded profile

Forgetting the fixed Tait colouring, this six-vertex identity hexagon realises every ordered conserved root quadruple and hence all ten support-unordered four-terminal states.

Therefore the minimal flat equality core itself is not profile-locked.

---

## 5. Nonminimal flat annuli

For a flat annular equality core with

\[
n>6,
\]

the annular compression theorem gives a connected response-equivalent six-vertex representative.

Thus at fixed ordered Tait response:

\[
\boxed{
\text{flat equality annulus}
\Longrightarrow
\text{strict compression to the identity hexagon}.}
\]

The remaining issue is only promotion of this fixed-response replacement to a complete root-profile transfer in the ambient source graph.

---

## 6. Negative Euler characteristic

Assume

\[
\chi(S_T)<0.
\]

The core still has four boundary semiedges. A connected dipole-free properly three-edge-coloured multipole with nonempty boundary has at most three ports. Therefore `T` contains a coloured one-dipole.

Cancel one such dipole.

### Type P — response preserving

If at most one complementary bicoloured residue is open, cancellation preserves

\[
(r^4;M,M,\varnothing)
\]

and removes two source vertices. The surface homeomorphism type and Euler characteristic are unchanged.

### Type F — four-port matching flip

If both complementary residues are open, cancellation changes exactly one of the two equal matchings on the same four endpoints. Thus the response leaves the double-equal sector:

\[
(M,M)\longmapsto(M,M'),
\qquad M'\ne M.
\]

This is a bounded route-changing four-port event.

### Type B — boundary degeneration

If two paired incidences are boundary semiedges, the two-vertex neighbourhood is already one bounded two-/four-port carrier or separator branch.

### Theorem 6.1 — negative equality reduction

Repeated Type-P cancellation cannot terminate in a dipole-free four-port core. Hence after finitely many strict two-vertex descents it exposes Type F or Type B.

Equivalently:

\[
\boxed{
\chi(S_T)<0
\Longrightarrow
\begin{cases}
\text{bounded matching flip},\\
\text{bounded boundary degeneration},\\
\text{or category/separator exit}.
\end{cases}}
\]

No negative-genus equality response survives as an unbounded carrier.

---

## 7. Unified connected equality topology theorem

### Theorem 7.1

Every connected equality Tait core with response

\[
(r^4;M,M,\varnothing)
\]

enters exactly one of the following structural branches:

1. **annular compression:** a nonminimal flat annulus compresses at fixed response;
2. **identity hexagon:** the flat minimal core has six vertices and complete root profile;
3. **matching flip:** one dipole changes one of the two equal responses;
4. **boundary degeneration:** one bounded two-/four-port event occurs;
5. **category exit:** a two-, three-, or four-edge separator or bounded graph degeneration is exposed.

The flat Möbius orientation branch and an unbounded negative-Euler prime response are absent.

---

## 8. Interaction with private matching decorations

Before suppression, the physical equality carrier is the Tait core plus one private-root matching.

The existing private-edge theorem eliminates the disconnected two-rail branch and supplies:

- crossed private-edge root NNI;
- aligned private-edge equal-label cancellation;
- a two-edge cut when no private edge joins the rails.

The triple-projection faithfulness and seven-section Pachner theorem show that private subdivisions cannot constitute a common invisible side alphabet.

Hence the only remaining equality burden is not topological classification. It is the cover-independent transfer of one cap-compatible root state through:

\[
\boxed{
\text{private-edge surgeries}
+
\text{Pachner flips}
+
\text{response-preserving dipole peels}.}
\]

---

## 9. Trust boundary

### Exact here

- boundary components as cycles of `M_(rs) sqcup M_(rt)`;
- exactly two boundary components in the double-equal response;
- exclusion of disk and Möbius topology;
- annulus as the unique zero-Euler equality surface;
- six-vertex identity hexagon as the minimal flat annulus;
- complete profile of the identity hexagon;
- strict fixed-response compression of nonminimal flat annuli;
- compulsory dipole in every negative-Euler four-port equality core;
- finite termination at a matching flip or boundary degeneration;
- absence of an unbounded topological equality species.

### Still open

- complete five-support profile transfer under annular compression;
- root-compatible realisation of every abstract Type-F event as a profile escape;
- cover-independent inverse transfer through a mixed Pachner/peel history;
- a monotone defect-relocation/enclosure measure;
- global proof-DAG closure;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication, and the global five-support theorem.
