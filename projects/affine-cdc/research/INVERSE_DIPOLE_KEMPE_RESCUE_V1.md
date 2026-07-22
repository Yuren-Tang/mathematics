# Kempe rescue for inverse-dipole equality and DDD failures

## Research dossier v1.1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `43d20b46026ab06e604bc121be073c78bf70bad5`  
**Parents:**

- `projects/affine-cdc/research/FOUR_PORT_TAIT_DIPOLE_PEELING_V1.md`;
- `projects/affine-cdc/research/SHIFT_MATCHING_BANDS_ROUTE_TAIT_PEELING_V1.md`;
- `projects/affine-cdc/research/TYPE_H_PHYSICAL_COMMUTATION_ELIMINATION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_IDENTITY_HEXAGON_TRANSVERSE_TRANSVERSAL_PARITY_V1.md`;
- `projects/affine-cdc/research/DDD_ROUTE_ORIENTATION_COVER_V1.md`.

**Status:** exact horizontal rescue theorem for the only two non-root cases in inverse dipole expansion. Equality and disjoint-root failures disappear after one ordinary Kempe component switch whenever the two reconnected edges are separated by one relevant support-pair Kempe system. A surviving failed expansion is therefore exactly a finite route lock: a six-channel `K_{2,3}` lock in the equality case or a four-channel `K_{2,2}`/DDD lock in the disjoint case.  
**Not implied:** elimination of every full-channel lock, automatic existence of a separating component, a complete global induction theorem, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Inverse dipole setup

Let a two-vertex dipole cancellation produce a smaller cubic graph `G'`. Let its two colourwise reconnected edges be `e,f`, and let a root-valued flow on `G'` have values

\[
p=\lambda(e),\qquad q=\lambda(f).
\]

Reinserting the two cancelled vertices forces the restored dipole edge to have value

\[
r=p+q.
\]

The expansion succeeds exactly when `p,q` are distinct intersecting roots. The only failures are:

1. `p=q`, giving `r=0`;
2. `p,q` disjoint, giving one co-root `r=p+q`.

---

## 2. Ordinary Kempe switches

For a root `s=ab`, define

\[
H_s=F_a\mathbin{\triangle}F_b
   =\{g:\lambda(g)+s\in R_5\}.
\]

Every connected component `Z` of `H_s` may be switched:

\[
\lambda_Z=\lambda+s1_Z.
\]

If exactly one of `e,f` lies in `Z`, exactly one of `p,q` is translated by `s`.

---

## 3. Equality rescue

Assume `p=q=t`. Let `s` be any root distinct from and intersecting `t`. Then `t+s` is the third root in the `K_5` triangle containing `s,t`; in particular `t+s` and `t` are distinct intersecting roots. Both marked edges lie in `H_s`.

### Theorem 3.1 — equality rescue

If `e,f` lie in different connected components of `H_s` for one such `s`, switch the component containing exactly one marked edge. The marked values become

\[
(t+s,t),
\]

and the restored dipole value is

\[
(t+s)+t=s\in R_5.
\]

Hence the original dipole expands root-valuedly.

### Equality lock

A failed equality expansion survives every one-switch rescue exactly when, for every root `s` intersecting `t`, the two marked edges belong to the same component of `H_s`.

If `t=uv`, the six such roots are

\[
\{uw,vw:w\in[5]\setminus\{u,v\}\},
\]

the six edges of `K_{2,3}`. Thus residual equality is one exact six-channel lock.

---

## 4. DDD rescue

Assume `p,q` are disjoint. Relabel supports so that

\[
p=12,\qquad q=34.
\]

The four cross roots are

\[
13,14,23,24.
\]

Each intersects both `p` and `q`, so both marked edges lie in every corresponding `H_s`.

### Theorem 4.1 — DDD rescue

If `e,f` lie in different connected components of `H_s` for one cross root `s`, switch the component containing exactly one marked edge. If the `p` edge is switched, the new pair is

\[
(p+s,q).
\]

The root `p+s` meets `q` in exactly one support index, so the pair is root-expandable.

For example,

\[
12+13=23,
\]

and `23` meets `34` at support `3`.

### DDD lock

A disjoint-root expansion survives all one-switch rescues exactly when the marked edges lie in the same component of `H_s` for all four cross roots.

These four roots form the channel square `K_{2,2}`. Switching a common component translates both values and preserves disjointness, so component separation is the exact progress condition.

---

## 5. Complete local trichotomy

### Theorem 5.1 — first failed expansion theorem

Every inverse dipole expansion enters exactly one of:

1. **immediate root lift:** `p,q` are distinct and intersect;
2. **horizontal rescue:** equality or DDD occurs, but one relevant Kempe system separates the marked edges;
3. **exact route lock:** equality gives a six-channel `K_{2,3}` lock, while DDD gives a four-channel `K_{2,2}` lock.

There is no fourth local failure mechanism.

### Corollary 5.2

A zero/equality cell or one-co-root DDD cell is not terminal merely from its coefficient label. It is terminal only if every relevant Kempe system connects the two marked reduced edges.

---

## 6. Interaction with cyclic five-edge connectivity

Physical commutation eliminates all Type-T and Type-H four-pole mismatch kernels. Hence a vertex-minimal counterexample may be assumed cyclically five-edge-connected.

The route-Tait dipole theorems show that a cancellation either gives a smaller bridgeless cubic graph or exposes a cyclic three-cut / bounded separator. The separator branch already glues. Therefore every surviving equality or DDD failure occurs after a genuine smaller bridgeless reduction and satisfies the lock conditions above.

The remaining induction gap is one full-channel lock, not category preservation or finite coefficient classification.

---

## 7. Relation to channel geometry

### Equality

The six-channel equality lock is the source-side zero/identity fibre of the quadratic `K_{2,3}` channel projection and the Type-Z identity-return sector.

### DDD

For disjoint roots `p=uv`, `q=xy`, the four rescue roots

\[
ux,uy,vx,vy
\]

are the crossed-resolution square. The orientation refinement is the already calibrated class

\[
w_1=\kappa=\nu_X.
\]

Thus inverse-lift DDD failure and the earlier DDD route-holonomy frontier are the same physical component problem.

---

## 8. Final local target

To complete bounded inverse-lift transfer it is enough to prove the following.

### Target 8.1 — full-channel lock elimination

Let `e,f` be marked internal edges of a cyclically five-edge-connected root-valued smaller graph. If they lie in the same component of every relevant channel system, prove one of:

1. a nonlaminar attachment yields profile escape;
2. the common connections enclose a smaller two-, three-, or four-pole;
3. a matching-plus-Tait band admits strict dipole descent;
4. the DDD orientation switch produces a crossed root resolution;
5. the equality lock produces a square-envelope escape;
6. a strictly smaller marked-edge instance remains.

All coefficient, state, and orientation data in this target are explicit.

---

## 9. Trust boundary

### Exact here

- equality rescue by one separating Kempe component;
- DDD rescue by one separating cross-channel component;
- exact six-channel and four-channel lock conditions;
- identification of failed inverse expansion with a physical route lock;
- elimination of every nonlocked equality/DDD cell;
- reduction to full-channel lock elimination.

### Still open

- elimination of every equality six-channel lock;
- elimination of every DDD four-channel lock;
- global ordering of repeated graph reductions and horizontal rescues;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
