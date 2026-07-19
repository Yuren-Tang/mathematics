# Colour-cut form of the fixed-plane five-support obstruction

**Programme:** `AffineCDC — Research Lead`  
**Parent checkpoint:** `FIVE_CDC_FIXED_FLOW_REDUCTION_V1.md`  
**Status:** theorem-level refinement; not canonical pending review

## 1. Setup

Let

\[
f:E(G)\to\Gamma\setminus\{0\},
\qquad
\Gamma=\mathbf F_2^3,
\]

be a nowhere-zero flow on a finite cubic loopless multigraph. Fix a plane
`W≤Γ`, and let `G_W` be the spanning subgraph whose edges have values in `W`.
Every non-isolated vertex of `G_W` has degree one or three.

The parent checkpoint defines, for each component `K` of `G_W`, a boundary bit
`Ω_W(K)`. A compatible affine family omitting any three-point set of direction
`W` exists exactly when all these bits vanish.

The purpose of this note is to remove all auxiliary quotient coordinates from
that obstruction.

## 2. Four outside colours have one common cut parity

Let `K` be a connected component of `G_W`. No edge of value in `W` crosses the
cut `δ_G(K)`. For each outside colour

\[
c\in\Gamma\setminus W,
\]

put

\[
n_c(K):=|\{e\in\delta_G(K):f(e)=c\}|\pmod2.
\]

### Theorem 2.1 — equal outside-colour parities

The four bits `n_c(K)`, for `c∉W`, are all equal.

#### Proof

Summing the flow equations over all vertices of `K` cancels internal edges and
gives

\[
\sum_{e\in\delta_G(K)}f(e)=0.
\]

The four elements of `Γ\setminus W` form an affine `W`-plane. Their only
nontrivial binary linear relation is the sum of all four elements:

\[
\sum_{c\in\Gamma\setminus W}c=0.
\]

Indeed, they span `Γ`, so the relation space among the four columns is
one-dimensional. Therefore the parity vector

\[
(n_c(K))_{c\notin W}\in\mathbf F_2^4
\]

is either `0000` or `1111`. ∎

Denote this common bit by

\[
\chi_W(K).
\]

Thus an obstructed component is characterized intrinsically by the fact that
**each of the four outside flow colours crosses its boundary an odd number of
times**.

## 3. Identification with the affine boundary obstruction

### Theorem 3.1 — colour-cut formula

For every component `K` of `G_W`,

\[
\boxed{
\Omega_W(K)=\chi_W(K).
}
\]

#### Proof

Choose any `a∉W` and write every flow value uniquely as

\[
f(e)=w_e+b_ea,
\qquad
w_e\in W,
\quad
b_e\in\mathbf F_2.
\]

Both `w` and `b` satisfy the flow equations. At a degree-one vertex of `G_W`,
the other two incident edges lie outside `W`. If their values are

\[
a+w_1,
\qquad
a+w_2,
\]

and the unique `W`-edge has value `h=w_1+w_2`, the boundary bit from the parent
checkpoint is

\[
1+\ell_h(w_1).
\]

In the two-dimensional space `W`, this bit is one exactly when one of `w_1,w_2`
is zero. Equivalently, it is one exactly when one of the two outside incident
edges has flow colour `a`. Since two equal nonzero flow values cannot occur at a
cubic vertex, the bit is precisely the incidence parity of the `a`-coloured
edge set at that leaf.

Summing over the leaves of `K` counts the `a`-coloured edges crossing `δ_G(K)`;
internal `a`-edges contribute twice. Therefore

\[
\Omega_W(K)=n_a(K)=\chi_W(K).
\]

By Theorem 2.1 this is independent of the chosen outside colour `a`. ∎

## 4. Coordinate-free fixed-plane criterion

### Corollary 4.1

A compatible affine family omitting a three-point set of direction `W` exists
if and only if, for every component `K` of `G_W` and every colour `c∉W`,

\[
\boxed{
|\{e\in\delta_G(K):f(e)=c\}|
\equiv0\pmod2.
}
\]

It is enough to check one outside colour per component, because the four
parities are equal.

### Quotient-graph form

Contract each connected component of `G_W` to one vertex and retain the edges
whose flow values lie outside `W`. The resulting multigraph `Q_W` is edge-coloured
by the four elements of `Γ\setminus W`.

The fixed-plane criterion says:

> for every outside colour `c`, the `c`-coloured edge set of `Q_W` is Eulerian.

At each quotient vertex, either all four colour-degrees are even or all four are
odd. The second case is exactly the affine five-support obstruction.

## 5. Immediate sufficient conditions

1. If `G_W` is connected, then the unique component has empty boundary, so the
   fixed-plane criterion holds.

2. If the flow takes values entirely in `W`, then `G_W=G`; this recovers the
   immediate five-support consequence of a nowhere-zero `F₂²`-flow.

3. More generally, the criterion holds whenever every outside colour matching
   induces an even subgraph after the `G_W` components are contracted.

These conditions clarify the relationship with nowhere-zero `4`-flows: the
five-support problem allows outside colours, but only when their four matching
classes are parity-balanced across every `W`-component.

## 6. Cube certificate in colour-cut form

For the cube flow in the parent checkpoint, each of the seven planes has a
component `K` for which the four outside colours cross `δ(K)` once each. For
example:

| `W\setminus{0}` | obstructed `K` | outside colours, each odd |
|---|---|---|
| `{1,2,3}` | `{0,2,3,4,5,6}` | `4,5,6,7` |
| `{1,4,5}` | `{2,3}` | `2,3,6,7` |
| `{1,6,7}` | `{0,4,5,7}` | `2,3,4,5` |
| `{2,4,6}` | `{0,3}` | `1,3,5,7` |
| `{2,5,7}` | `{0,1,2,3,4,7}` | `1,3,4,6` |
| `{3,4,7}` | `{0,4}` | `1,2,5,6` |
| `{3,5,6}` | `{2,6}` | `1,2,4,7` |

Thus the obstruction table is a collection of explicit four-colour cut
certificates, with no local-family enumeration required.

## 7. Correct next invariant

For a fixed flow, define the plane profile

\[
\mathfrak O_f(W)
:=
\{K\in\pi_0(G_W):\chi_W(K)=1\}.
\]

A five-support affine family exists exactly when

\[
\mathfrak O_f(W)=\varnothing
\]

for some plane `W`.

The graph-level strengthening asks whether the flow can always be chosen so that
one of the seven plane profiles is empty. The next mathematical task is to
compute how `\mathfrak O_f(W)` transforms under elementary changes of the flow.