# Oriented channel locks from the fixed-route outer sector

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `c5a4f912b48bd9491bc594ebe7645d67ba563fbb`  
**Parents:**

- `projects/affine-cdc/research/THREE_RECONNECTION_FIXED_ROUTE_OUTER_SECTOR_V1.md`;
- `projects/affine-cdc/research/INVERSE_DIPOLE_KEMPE_RESCUE_V1.md`;
- `projects/affine-cdc/research/DDD_ROUTE_ORIENTATION_COVER_V1.md`;
- `projects/affine-cdc/research/QUADRATIC_CHANNEL_PROJECTION_V1.md`.

**Status:** exact calibration between the ten-state fixed-route boundary sector and the source-side equality/DDD full-channel locks. A blocked two-vertex cap does not merely force the two marked reconnection edges to lie on one component of every rescue channel. It fixes the cyclic endpoint order of that component: every relevant channel cuts open to the original cap matching. In the DDD branch, the two cap shores distinguish one block of this crossed matching, so the exceptional `D_8` cocycle restricts to a coboundary. Therefore the residual inverse-lift obstruction is holonomy-free; what remains is edgewise root-admissible composition of one oriented channel lock.  
**Not implied:** existence of a root-valued replacement for every oriented lock, contraction of every constant-pivot or equality strip, enclosure preservation under repeated dipole descent, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Cap and reconnection matchings

Let a two-vertex cubic cap have four ordered external terminals

\[
1,2,3,4.
\]

Let

\[
M_i=12\mid34
\]

be the matching whose two blocks are the two cap vertices. The other two terminal matchings are denoted

\[
M_j=13\mid24,
\qquad
M_k=14\mid23.
\]

Deleting the two cap vertices and reconnecting their four external incidences colourwise produces one of the two cross reconnections. Fix

\[
E_j=M_j
\]

and denote its two new edges by

\[
e=13,
\qquad
f=24.
\]

Let `P` be the complementary four-pole. The reduced closed graph is

\[
G_j=P\cup E_j.
\]

Suppose a root-valued flow `lambda` on `G_j` gives

\[
p=\lambda(e),
\qquad
q=\lambda(f).
\]

Cutting `e,f` recovers the boundary state of `P`.

---

## 2. Cutting two edges of one even subgraph

Let `H` be an even subgraph of `G_j` containing both `e` and `f`. Delete the interiors of `e,f` and regard the four exposed ends as the ordered terminals of `P`.

### Lemma 2.1 — component/routing dictionary

Exactly one of the following occurs.

1. **Different components.**  
   If `e,f` lie in distinct components of `H`, deleting them opens two paths whose endpoints are the two blocks of `M_j`. Thus the route on `P` is
   \[
   \boxed{M_j.}
   \]

2. **One component, cap order.**  
   If `e,f` lie on one cycle and their cyclic endpoint order cuts the cycle into paths `1--2` and `3--4`, the route is
   \[
   \boxed{M_i.}
   \]

3. **One component, opposite cross order.**  
   If the same cycle cuts into paths `1--4` and `2--3`, the route is
   \[
   \boxed{M_k.}
   \]

No fourth route is possible.

### Proof

Every component of a closed even subgraph is an Eulerian component; the component containing a specified edge is a cycle after suppressing repeated degree-two portions. Cutting one edge of one component produces one path joining its two exposed ends. Hence two different components give the direct reconnection matching `M_j`. Cutting two edges of one component gives the two complementary arcs of that cycle, which realise exactly one of the other two perfect matchings. The ordered cyclic endpoint order distinguishes `M_i` from `M_k`. ∎

### Consequence 2.2 — rescue versus oriented lock

For a repair channel `H_s` containing `e,f`:

- route `M_j` is equivalent to component separation and permits the one-component Kempe rescue;
- routes `M_i,M_k` are the two possible same-component locks;
- specifying route `M_i` records the missing orientation/cyclic-order datum of the lock.

Thus a bare full-channel lock is strictly weaker than an oriented full-channel lock.

---

## 3. Equality state and the six channels

Assume

\[
p=q=t=uv.
\]

After cutting `e,f`, the boundary state is `A`: supports `u,v` have full trace and the other three supports have empty trace.

For every

\[
w\in[5]\setminus\{u,v\},
\]

the six full/empty complementary support-pair challenges are

\[
\{u,w\},
\qquad
\{v,w\}.
\]

Their symmetric-difference subgraphs are exactly

\[
H_{uw}=F_u\triangle F_w,
\qquad
H_{vw}=F_v\triangle F_w.
\]

These are precisely the six equality rescue channels meeting `t`.

### Theorem 3.1 — equality boundary/channel identification

At the `A` boundary state, the following data are identical:

1. the six full/empty challenge routes of the ten-state interface;
2. the six `K_{2,3}` repair channels of the equality inverse-lift failure.

If the blocked cap profile is in the fixed-route outer sector for `M_i`, then every one of these six channels:

- contains `e,f` in one component;
- cuts open with route `M_i`, not merely with an unspecified crossed route.

Hence the residual equality failure is an **oriented six-channel lock**.

### Proof

The boundary traces show that `F_u triangle F_w` and `F_v triangle F_w` have all four terminals in their boundary, so they are exactly the full/empty challenges. The inverse-dipole rescue theorem identifies the same six root shifts as the complete repair set. Fixed-route collapse forces route `M_i` for every challenge. Lemma 2.1 then gives same-component lock with cap cyclic order. ∎

---

## 4. DDD state and the four crossed channels

Assume `p,q` are disjoint. Relabel support indices so that

\[
p=12,
\qquad
q=34.
\]

The fifth support index is absent at the four terminals. Cutting `e,f` gives the direct-pairing state `C_j`.

The complementary support pairs whose traces differ at all four terminals are exactly

\[
\{1,3\},
\{1,4\},
\{2,3\},
\{2,4\}.
\]

Their symmetric differences are the four DDD rescue systems

\[
H_{13},H_{14},H_{23},H_{24}.
\]

### Theorem 4.1 — DDD boundary/channel identification

At the `C_j` boundary state, the four full challenges are exactly the four crossed `K_{2,2}` repair channels of the disjoint-root inverse-lift failure.

If the cap `C_i` is blocked and the complete physical profile lies in the fixed-route outer sector, all four channels cut open with the same route

\[
\boxed{M_i.}
\]

Therefore the residual DDD failure is an **oriented four-channel lock**: component connectivity and cyclic endpoint order are both fixed.

### Proof

A support from `{1,2}` and a support from `{3,4}` occur on complementary direct-pairing terminal blocks, so their traces differ at all four terminals. These are exactly the four cross roots identified by the inverse-dipole rescue theorem. Fixed-route collapse supplies route `M_i`; Lemma 2.1 supplies the oriented same-component interpretation. ∎

### Corollary 4.2 — the second outer path is the DDD carrier

For a cap blocked at `M_i`, a realised DDD state from a cross reconnection must lie in the second outer component

\[
L_i=\{C_j,D_i,C_k\}.
\]

Thus the optional outer `P_3` in the ten-state classification is not an unrelated profile enlargement. It is precisely the boundary carrier of the two crossed reconnection classes and their common oriented route `M_i`.

---

## 5. The cap supplies a canonical route orientation

The matching

\[
M_i=12\mid34
\]

is not merely an unordered pair of blocks in the inverse-dipole problem. Its blocks are distinguished by the two deleted cap vertices. Choose the block `12` as the positive block.

For the DDD atom, the two crossed root-resolution matchings are the two unordered routes `X,Y` of the `D_8` orientation-cover theorem. Whichever of `X,Y` is identified with `M_i`, the cap-side labelling chooses one of its two blocks globally.

### Theorem 5.1 — DDD cohomology vanishes on an oriented inverse-dipole lock

Let `D` be the physical transport subgroup generated along one DDD full-channel lock. Because every channel returns the distinguished cap block to itself, one has

\[
D\le D_X=\ker\kappa
\]

if `M_i` is identified with `X`, or

\[
D\le D_Y=\ker(\kappa+\chi)
\]

if it is identified with `Y`.

Consequently the exceptional DDD cocycle restricts to a coboundary:

\[
\boxed{
\alpha|_D=\delta x
}
\]

or

\[
\boxed{
\alpha|_D=\delta y.
}
\]

### Proof

The route-orientation theorem identifies block exchange on `X` with `kappa` and block exchange on `Y` with `kappa+chi`. The ordered cap shore forbids block exchange along the physical lock. Hence the physical subgroup lies in the corresponding kernel. The orientation-cover trivialisation theorem gives the displayed coboundary identity. ∎

### Interpretation

The nontrivial class

\[
[\alpha]\in H^1(D_8,E_5)
\]

cannot be the final obstruction in an inverse-dipole full lock. The cap itself supplies the orientation whose absence created that class.

What may still fail is not affine holonomy but **edgewise root admissibility and incidence composition**:

- a pivot may change and demand opposite root resolutions;
- a side-root output may prevent a simultaneous root section;
- an attached component may force a separator or a smaller lock.

Thus the orientation theorem removes the last unexplained `C_2` datum without pretending to construct the missing graph replacement.

---

## 6. Unified residual lock

The equality and DDD branches now have the same source-level form.

1. Four ordered ports are grouped by the original cap matching `M_i`.
2. Every relevant repair channel connects the two marked reconnection edges in one component.
3. Cutting that component always produces the same **oriented** route `M_i`.
4. No nontrivial DDD orientation holonomy remains.
5. Failure can persist only through edgewise root-fibre/local-relation constraints and attached source incidence.

### Theorem 6.1 — final local mechanism

After:

- three-reconnection forcing;
- physical elimination of all Type-T and Type-H mismatch kernels;
- one-component equality/DDD Kempe rescue;
- fixed-route collapse;
- and oriented-route cohomology trivialisation;

the complete bounded inverse-lift frontier consists of one mechanism:

\[
\boxed{
\text{a holonomy-free oriented full-channel lock with separated side incidence.}
}
\]

There is no independent residual:

- Type-T route word;
- Type-H boundary triangle;
- equality-versus-DDD finite alphabet;
- or DDD orientation bit.

---

## 7. Exact next theorem

A minimal instance of the mechanism in Theorem 6.1 must now satisfy the following dichotomy.

### Target 7.1 — oriented-lock descent

Let `R` be a support-minimal oriented full-channel lock. Prove one of:

1. a nonlaminar side attachment changes the route and gives profile escape;
2. a split attachment produces a two-, three-, or four-edge separator;
3. a matching or rank-two Tait side component admits category-safe dipole descent;
4. a constant-pivot run has a root-admissible serial replacement;
5. a pivot change localises a strictly smaller oriented lock;
6. the complete lock is a bounded direct-pairing/square carrier.

The first three alternatives are already supplied at theorem level by the laminar-interval, four-cut, matching-band, and Tait-peeling modules. The unresolved implication is the enclosure/root-admissibility statement in alternatives 4--5.

### Required preservation lemma

The precise remaining local lemma is:

> A failed inverse expansion created by peeling a separated side component inherits the ordered cap route and is enclosed in a strictly smaller laminar interval.

This is the only step needed to turn the current local reductions into a well-founded minimal-lock contradiction.

---

## 8. Consequence for the global frontier

The programme now has two logically distinct remaining obligations.

### Local obligation

Prove Target 7.1, equivalently the required preservation lemma plus the root-admissible constant-pivot base case.

### Packaging obligation

Order:

- graph vertex descent;
- cyclic three-/four-cut gluing;
- horizontal Kempe rescue;
- and minimal-lock descent

in one well-founded induction.

The packaging is not a new obstruction mechanism. It is required to turn the local theorem into the global five-support statement without circular use of minimality.

---

## 9. Trust boundary

### Exact here

- the cycle-cut component/routing dictionary for two marked reconnection edges;
- identification of the six equality challenges with the `K_{2,3}` repair channels;
- identification of the four DDD challenges with the crossed `K_{2,2}` channels;
- upgrade from bare component lock to cap-oriented channel lock;
- identification of `L_i` as the DDD crossed-reconnection outer component;
- canonical block orientation supplied by the deleted cap vertices;
- trivialisation of the exceptional DDD cocycle on the physical oriented-lock subgroup;
- unification of equality and DDD as one holonomy-free local mechanism.

### Still open

- root-admissible serial replacement of every constant-pivot separated interval;
- proof that every pivot-change failure is enclosed in a strictly smaller oriented lock;
- well-founded global induction and horizontal bookkeeping;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
