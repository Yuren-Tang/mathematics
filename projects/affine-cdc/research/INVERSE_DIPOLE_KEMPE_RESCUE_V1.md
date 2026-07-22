# Kempe rescue for inverse-dipole equality and DDD failures

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** current branch head containing `TYPE_H_PHYSICAL_COMMUTATION_ELIMINATION_V1.md`  
**Parents:**

- `projects/affine-cdc/research/FOUR_PORT_TAIT_DIPOLE_PEELING_V1.md`;
- `projects/affine-cdc/research/SHIFT_MATCHING_BANDS_ROUTE_TAIT_PEELING_V1.md`;
- `projects/affine-cdc/research/TYPE_H_PHYSICAL_COMMUTATION_ELIMINATION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_IDENTITY_HEXAGON_TRANSVERSE_TRANSVERSAL_PARITY_V1.md`;
- `projects/affine-cdc/research/DDD_ROUTE_ORIENTATION_COVER_V1.md`.

**Status:** exact horizontal rescue theorem for the only two non-root cases in inverse dipole expansion. Equality and disjoint-root failures disappear after one ordinary Kempe component switch whenever the two reconnected edges are separated by one relevant support-pair Kempe system. Hence a surviving failed expansion is precisely a finite route lock: a six-channel `K_{2,3}` lock in the equality case or a four-channel `K_{2,2}`/DDD lock in the disjoint case. No additional local lift-failure state remains.  
**Not implied:** elimination of every full-channel lock, automatic existence of a separating component, a complete global induction theorem, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Inverse dipole setup

Let a two-vertex dipole cancellation produce a smaller cubic graph `G'`. The two colourwise reconnected edges are

\[
e,\qquad f.
\]

Let

\[
\lambda:E(G')\to R_5
\]

be a root-valued flow on `G'`, and write

\[
p=\lambda(e),
\qquad
q=\lambda(f).
\]

Reinserting the two cancelled vertices forces the restored dipole edge to have value

\[
r=p+q.
\]

The expansion succeeds exactly when `p,q` are distinct intersecting roots.

The two failures are:

1. **equality:** `p=q`, so `r=0`;
2. **DDD:** `p,q` are disjoint, so `r=p+q` is a co-root.

---

## 2. Ordinary Kempe component switches

For a root

\[
s=ab,
\]

define the safe support-pair Kempe system

\[
H_s=F_a\triangle F_b
=\{g:\lambda(g)+s\in R_5\}.
\]

Every connected component `Z` of `H_s` may be switched:

\[
\lambda_Z=\lambda+s1_Z.
\]

This remains root-valued on every edge.

If exactly one of `e,f` lies in `Z`, then exactly one of `p,q` is translated by `s`.

---

## 3. Equality rescue

Assume

\[
p=q=t.
\]

Let `s` be any root distinct from and intersecting `t`. Then

\[
t+s
\]

is the third root of the `K_5` triangle containing `s,t`. In particular,

\[
t+s\ne t
\]

and the two roots `t+s,t` intersect.

Both reconnected edges belong to `H_s`, because

\[
t+s\in R_5.
\]

### Theorem 3.1 — equality rescue criterion

If `e,f` lie in distinct connected components of `H_s` for some root `s` intersecting `t`, switch the component containing exactly one of them. The new values on the reconnected edges are

\[
(t+s,t),
\]

which are distinct intersecting roots. Therefore the original dipole expands root-valuedly.

### Proof

The Kempe switch changes one marked value from `t` to `t+s` and leaves the other equal to `t`. The forced dipole value becomes

\[
(t+s)+t=s\in R_5.
\]

At both restored cubic vertices the three incident roots are the triangle

\[
t,\ t+s,\ s.
\]

∎

### Equality lock

A failed equality expansion survives all one-switch rescues exactly when:

\[
oxed{
	ext{for every root }s	ext{ intersecting }t,
\ e,f	ext{ lie in the same component of }H_s.}
\]

The six such roots are precisely the six edges of the channel graph

\[
K_{2,3}
\]

between the two endpoints of `t` and the complementary three support indices.

Thus the residual equality obstruction is one exact six-channel route lock.

---

## 4. DDD rescue

Assume `p,q` are disjoint. After support relabelling write

\[
p=12,
\qquad
q=34.
\]

The four cross roots are

\[
13,\ 14,\ 23,\ 24.
\]

Each cross root `s` intersects both `p` and `q`. Hence both marked edges belong to `H_s`.

Moreover, if only the `p` edge is switched, then

\[
p+s
\]

is a root intersecting `q`. For example,

\[
12+13=23,
\]

which intersects `34` at support `3`.

### Theorem 4.1 — DDD rescue criterion

If `e,f` lie in distinct connected components of `H_s` for one cross root

\[
s\in\{13,14,23,24\},
\]

switch the component containing exactly one marked edge. The two new reconnected values are distinct intersecting roots, so the original dipole expands root-valuedly.

### Proof

Assume the `p` edge is switched. Its new value is `p+s`; the other remains `q`. Since `s` joins one endpoint of `p` to one endpoint of `q`, the third root `p+s` contains the other endpoint of `p` and the chosen endpoint of `q`. It therefore meets `q` in exactly one support index.

The restored dipole value is

\[
(p+s)+q,
\]

which is the third root of their triangle. ∎

### DDD lock

A disjoint-root inverse expansion survives all one-switch rescues exactly when:

\[
oxed{
	ext{for all four cross roots }s,
\ e,f	ext{ lie in the same component of }H_s.}
\]

The four cross roots form the channel square

\[
K_{2,2}
\]

inside the six-channel `K_{2,3}` carrier. This is exactly the physical route-lock condition of the one-co-root DDD atom.

If one switches a common component containing both marked edges, both values translate:

\[
(p,q)\longmapsto(p+s,q+s).
\]

The new pair is again disjoint, so common-component switching cannot remove the DDD relation. Separation is the precise progress condition.

---

## 5. Complete local trichotomy

### Theorem 5.1 — first failed expansion theorem

For one inverse dipole expansion from a root-valued smaller graph, exactly one of the following occurs.

1. **Immediate root lift:** `p,q` are distinct and intersect.
2. **Horizontal rescue:** `p=q` or `p,q` are disjoint, but one relevant Kempe system separates the two reconnected edges; one component switch produces an immediate root lift.
3. **Exact route lock:**
   - equality gives a six-channel `K_{2,3}` lock;
   - DDD gives a four-cross-channel `K_{2,2}` lock.

There is no fourth local failure mechanism.

### Corollary 5.2 — bounded atoms are route-lock certificates

The words “zero/equality atom” and “one-co-root DDD atom” should not be treated as terminal local obstructions by themselves.

They are the coefficient shadows of the following source statement:

\[
oxed{
	ext{all relevant Kempe systems connect the two marked reduced edges.}}
\]

If even one system separates them, the atom disappears immediately.

---

## 6. Interaction with cyclic five-edge connectivity

The physical four-cut commutation theorem proves that a vertex-minimal counterexample may be assumed cyclically five-edge-connected.

The route-Tait dipole theorems prove that every cancellation either:

1. gives a smaller bridgeless cubic graph; or
2. exposes a cyclic three-cut or bounded separator.

The second branch is now eliminated by the established cut-gluing theorems. Therefore every surviving equality or DDD failure in a minimal counterexample occurs after a genuine smaller bridgeless reduction and must satisfy the exact route-lock conditions above.

Thus the remaining induction gap is no longer category preservation or finite coefficient classification. It is the elimination of one full-channel lock.

---

## 7. Channel geometry

### Equality

For `t=uv`, the six rescue roots are

\[
S_t=\{uw,vw:w\in[5]\setminus\{u,v\}\}
\cong E(K_{2,3}).
\]

The equality lock says that the two marked edges belong to the same physical component in all six channel systems.

This is the zero/identity fibre of the quadratic six-channel projection and the source-side form of the Type-Z identity-return sector.

### DDD

For disjoint roots `p=uv` and `q=xy`, the four rescue roots are

\[
\{ux,uy,vx,vy\},
\]

the four-cycle channel carrier attached to their one-factor.

The DDD lock says that the two marked edges remain connected in all four crossed-resolution systems. Its orientation refinement is the already calibrated class

\[
w_1=\kappa=\nu_X.
\]

Hence the local inverse-lift frontier and the earlier channel/DDD holonomy frontier are literally the same physical component problem.

---

## 8. Revised final local target

To complete bounded inverse-lift transfer it is enough to prove:

### Target 8.1 — full-channel lock elimination

Let `e,f` be two marked internal edges of a cyclically five-edge-connected root-valued smaller graph.

If they lie in the same connected component of every relevant channel system, prove one of:

1. a channel component has a nonlaminar attachment and yields profile escape;
2. the common connections enclose a smaller two-, three-, or four-pole;
3. a matching-plus-Tait band admits strict dipole descent;
4. the DDD orientation switch produces a crossed root resolution;
5. the equality six-channel lock produces the canonical square envelope;
6. a strictly smaller marked-edge instance remains.

All coefficient, state, and orientation data needed to state this target are now explicit.

---

## 9. Trust boundary

### Exact here

- equality rescue by one separating Kempe component;
- DDD rescue by one separating cross-channel component;
- exact six-channel and four-channel lock conditions;
- identification of failed inverse expansion with a physical route lock;
- elimination of every nonlocked equality/DDD cell;
- reduction of the bounded transfer problem to full-channel lock elimination.

### Still open

- proof that every equality six-channel lock gives square escape, separator, or descent;
- proof that every DDD four-channel lock gives crossed resolution, separator, or descent;
- global ordering of repeated graph reductions and horizontal rescues;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
