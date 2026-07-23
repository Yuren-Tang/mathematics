# One cross root flow already forces the original cap route

## Research Lead finite reduction v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `2d366a9aa3a8850e7d6c4c0fa2ef199b7eab66fb`.

**Parents:**

- `TEN_STATE_BOUNDARY_GRAPH_RIGIDITY_V1.md`;
- `INVERSE_DIPOLE_KEMPE_RESCUE_V1.md`;
- the exact direct-reconnection and cap profiles.

**Purpose:** remove the all-three-reconnection hypothesis from the fixed-route reduction. One selected cross reconnection root flow is enough: either it already glues the original cap or its equality/DDD singular state has the original cap matching as its unique blocked physical route.

**Status:** exact authorial finite reduction. It depends on the complete labelled ten-state challenge rows, but not on the classification of the entire physical profile `Sigma(P)`.

---

## 1. Setup

Let `P` be an ordered cubic four-pole with terminal matchings

\[
M_i,M_j,M_k,
\qquad
\{i,j,k\}=\{0,1,2\}.
\]

Let `cap_i` be the original two-vertex cap and let `E_j` be one cross zero-vertex reconnection.

Their exact profiles are

\[
\Sigma(E_j)=J_j=\{A,B_j,C_j\}
\]

and

\[
\Sigma(cap_i)=K_i=\{B_j,B_k,D_j,D_k\}.
\]

Assume the closed cross graph

\[
P\cup E_j
\]

has one root-valued flow. Restrict it to `P` and denote its support-unordered boundary state by

\[
\sigma\in J_j.
\]

---

## 2. Immediate cap-compatible state

Since

\[
B_j\in K_i,
\]

if

\[
\sigma=B_j,
\]

then `P` and `cap_i` have one common boundary state. A global permutation of the five support indices aligns the complete labelled traces and the original cap glues root-valuedly.

Thus a failed cap restoration from the selected cross flow has only

\[
\boxed{
\sigma=A
\quad\text{or}\quad
\sigma=C_j.
}
\]

These are precisely:

- the equality singular fibre;
- the disjoint-root/DDD singular fibre.

No third singular state occurs.

---

## 3. Blocking assumption

Assume the original cap is globally blocked:

\[
\Sigma(P)\cap K_i=\varnothing.
\]

Every physical Kempe switch starting from the selected labelled trace produces another state in `Sigma(P)`. Therefore none of its actual route targets may lie in `K_i`.

The complete labelled route table can now be used row by row. It is unnecessary to know every other state of `Sigma(P)`.

---

## 4. Equality start

Assume

\[
\sigma=A.
\]

For every complementary support-pair challenge at `A`, the three matching targets are

\[
B_i,
\qquad B_j,
\qquad B_k,
\]

under routes

\[
M_i,
\qquad M_j,
\qquad M_k
\]

respectively.

But

\[
B_j,B_k\in K_i.
\]

Cap blocking therefore forces the actual physical route to be

\[
\boxed{M_i,}
\]

with target `B_i`.

At `B_i`, its two relevant challenge rows have unique non-`K_i` targets

\[
A
\quad\text{and}\quad
C_i
\]

under `M_i`. At `C_i`, the unique non-`K_i` target is `B_i`, again under `M_i`.

### Theorem 4.1 — equality outer orbit

The complete blocked Kempe orbit reachable from the selected equality state is contained in

\[
\boxed{
J_i:\ A-B_i-C_i,
}
\]

and every relevant challenge has physical route `M_i`.

A separating channel component gives the ordinary horizontal equality rescue. If no such component exists, the selected flow enters an oriented six-channel equality lock with route `M_i`.

---

## 5. DDD start

Assume

\[
\sigma=C_j.
\]

For each of the four crossed DDD repair challenges, the exact route row has:

1. one target on the opposite outer path
   \[
   L_i=\{C_j,D_i,C_k\}
   \]
   under route `M_i`;
2. two targets in the forbidden cap cycle `K_i` under `M_j,M_k`.

Hence cap blocking forces the actual route to be

\[
\boxed{M_i.}
\]

The target is `D_i`. The rows at `D_i` then have unique non-`K_i` targets `C_j,C_k` under `M_i`, and the rows at `C_k` return to `D_i` under `M_i`.

### Theorem 5.1 — DDD outer orbit

The complete blocked Kempe orbit reachable from the selected DDD state is contained in

\[
\boxed{
L_i:\ C_j-D_i-C_k,
}
\]

and every relevant challenge has physical route `M_i`.

A separating crossed-channel component gives the ordinary horizontal DDD rescue. If no such component exists, the selected flow enters an oriented four-channel DDD lock with route `M_i`.

---

## 6. One-cross fixed-route theorem

### Theorem 6.1

Let `P` be an ordered four-pole and `cap_i` its original cap. Suppose one cross closure

\[
P\cup E_j
\]

has a root-valued flow.

Then exactly one of:

1. the selected boundary state is `B_j in K_i`, and the original cap glues immediately;
2. a separating equality or DDD Kempe component repairs the cap insertion;
3. the selected flow enters one fixed-route singular lock, with every relevant physical challenge routed by the original cap matching
   \[
   \boxed{M_i.}
   \]

The equality lock is supported on `J_i`; the DDD lock is supported on `L_i`.

### Proof

The selected state lies in `J_j={A,B_j,C_j}`. The `B_j` case is cap-compatible. The other two cases are Sections 4--5. ∎

---

## 7. What has been removed

Theorem 6.1 does not require:

- root flows on the other cross reconnection;
- a root flow on the direct reconnection;
- intersections with all three profiles `J_r`;
- classification of the complete profile as `J_i` or `J_i union L_i`;
- cyclic two-, three-, or four-cut reduction;
- Type T or Type H elimination.

The only finite input is the labelled route row at the selected state and along its forced outer orbit.

---

## 8. Interface with singular confluence

The output of Theorem 6.1 is exactly the input needed by the repaired singular normalisation theorem:

- one equality boundary `r,r,r,r`, or one DDD boundary `p,p,q,q`;
- one selected current root flow on a smaller cross closure;
- one cap-oriented physical route `M_i`;
- horizontal rescue already exhausted;
- global cap blocking, so every route change is a cap-compatible terminal.

Equality and DDD forward potentials then supply finite histories, and `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V1.md` returns every cap-compatible terminal through those histories.

---

## 9. Strong inductive consequence

Assume every connected loopless bridgeless cubic graph of lower vertex order has a root-valued flow.

If one cross closure of `P` is a lower-order connected loopless bridgeless cubic graph, Theorem 6.1 and singular contextual confluence imply that

\[
P\cup cap_i
\]

also has a root-valued flow.

Thus one smaller cross closure is enough to restore the deleted edge.

---

## 10. PDL obligations

PDL should verify:

1. `J_j cap K_i={B_j}` for cross `j ne i`;
2. the complete labelled rows at `A,B_i,C_i`;
3. the complete labelled rows at `C_j,D_i,C_k`;
4. uniqueness of the non-`K_i` route target in each row;
5. the distinction between a separating component rescue and a full-channel lock;
6. preservation of the cap orientation `M_i` into the singular confluence package.

This finite package is strictly smaller than reconstructing every Kempe-closed subset of the ten-state space.

---

## 11. Trust boundary

### Exact authorial claim

- one cross flow either glues the cap or enters a fixed-route equality/DDD lock;
- the all-three-reconnection profile theorem is not required for this reduction;
- only the selected Kempe orbit, not the complete profile, is needed.

### Not claimed

- independent route-table verification;
- elimination of the resulting lock without the singular confluence package;
- canonical acceptance, Lean verification, manuscript integration, release, peer review, or publication.
