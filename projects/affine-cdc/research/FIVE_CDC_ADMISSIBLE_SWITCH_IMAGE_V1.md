# Admissible cycle switches and the exact five-support correction image

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level research checkpoint; not canonical pending review  
**Parent:** `FIVE_CDC_SCHUR_QUOTIENT_CRITERION_V1.md`

## 1. Setup

Let

\[
f:E(G)\to \Gamma=\mathbf F_2^3\setminus\{0\}
\]

be a nowhere-zero flow on a finite cubic loopless multigraph. Fix a plane

\[
W=\ker b\leq \Gamma
\]

and write the five-support defect for this plane as

\[
d_W(f)\in \mathbf F_2^{\pi_0(G_W)},
\qquad
G_W=(V(G),\{e:f(e)\in W\}).
\]

Equivalently, after choosing coordinates `f=(b,x,y)` and contracting the
components of `G_W`,

\[
d_W(f)=\partial_{Q_W}(x*y).
\]

Fix a nonzero switch direction

\[
t\in W\setminus\{0\}.
\]

For a binary cycle `z`, define the colour switch

\[
f^z_t(e):=f(e)+z_e t.
\]

The switched labelling remains a flow. It is nowhere zero exactly when

\[
z_e=0\qquad(e\in A_t),
\]

where

\[
A_t:=f^{-1}(t).
\]

Since equal nonzero flow values cannot occur twice at a cubic vertex, `A_t` is a
matching. Thus the admissible switch space is the linear cycle space

\[
\mathcal C(G-A_t).
\]

## 2. The two quotient graphs

Put

\[
B:=\{e:f(e)\notin W\},
\qquad
H_t:=G_W-A_t.
\]

Contract every connected component of `H_t` in `G-A_t`. Denote the resulting
multigraph by

\[
R_{W,t}.
\]

Its edge set is naturally `B`; loops are retained. Contracting all of `G_W`
instead gives the earlier quotient

\[
Q_W.
\]

Equivalently, `Q_W` is obtained from `R_{W,t}` by identifying the vertices joined
through the deleted matching edges `A_t`. Write

\[
q:V(R_{W,t})\twoheadrightarrow V(Q_W)
\]

for the quotient map and

\[
q_*:\mathbf F_2^{V(R_{W,t})}\to \mathbf F_2^{V(Q_W)}
\]

for fibrewise summation.

Choose a linear functional `alpha` on `Gamma` whose restriction to `W` is the
unique nonzero functional with kernel `\langle t\rangle`, and put

\[
y_e:=\alpha(f(e))
\qquad(e\in B).
\]

The choice of extension of `alpha` outside `W` changes `y` by the all-one flow on
`R_{W,t}`, so the correction image below is unchanged.

Let `R_1` and `R_0` be the spanning subgraphs of `R_{W,t}` with edge sets

\[
E(R_1)=\{e\in B:y_e=1\},
\qquad
E(R_0)=\{e\in B:y_e=0\}.
\]

For a spanning subgraph `J`, write

\[
\mathsf B(J):=\operatorname{im}(\partial_J)
\subseteq \mathbf F_2^{V(R_{W,t})}
\]

for its binary boundary space.

## 3. Lifting admissible switches

### Proposition 3.1

Contraction induces a surjection

\[
\mathcal C(G-A_t)\twoheadrightarrow \mathcal C(R_{W,t}).
\]

#### Proof

An admissible cycle descends to a cycle after every connected `H_t`-component is
contracted. Conversely, let `Z` be a cycle on `R_{W,t}`. At each contracted
component, the endpoints of the selected `B`-edges have even total parity. Since
the component is connected, internal `H_t`-edges can be chosen with precisely
that boundary. Doing this independently in every component lifts `Z` to a cycle
of `G-A_t`. ∎

Thus only the cycle space of `R_{W,t}` matters for one-direction correction.

## 4. Exact image theorem

For `Z\in\mathcal C(R_{W,t})`, switching in direction `t` changes the plane
defect by

\[
q_*\partial_{R_{W,t}}(y*Z).
\]

### Theorem 4.1 — admissible switch image

The set of all defect changes obtainable by admissible `t`-switches is

\[
\boxed{
\operatorname{Im}\Delta_{W,t}
=
q_*\bigl(\mathsf B(R_1)\cap\mathsf B(R_0)\bigr).
}
\]

Consequently a single admissible `t`-switch kills the current five-support defect
if and only if

\[
\boxed{
d_W(f)\in
q_*\bigl(\mathsf B(R_1)\cap\mathsf B(R_0)\bigr).
}
\]

#### Proof

Let `Z\in\mathcal C(R_{W,t})` and split it into

\[
Z=Z_1+Z_0,
\qquad
Z_i\subseteq E(R_i).
\]

Since `Z` is a cycle,

\[
\partial Z_1=\partial Z_0.
\]

Moreover `y*Z=Z_1`. Therefore

\[
\partial(y*Z)=\partial Z_1
\in
\mathsf B(R_1)\cap\mathsf B(R_0).
\]

Conversely, suppose

\[
p\in\mathsf B(R_1)\cap\mathsf B(R_0).
\]

Choose edge sets `Z_1\subseteq E(R_1)` and `Z_0\subseteq E(R_0)` with

\[
\partial Z_1=p=\partial Z_0.
\]

Then `Z=Z_1+Z_0` is a cycle and

\[
\partial(y*Z)=p.
\]

Finally apply fibrewise summation `q_*`, which is exactly the passage from the
refined quotient `R_{W,t}` to the plane quotient `Q_W`. ∎

## 5. Dimension before the final quotient

Let `c(J)` denote the number of connected components of a spanning subgraph,
including isolated vertices. Since

\[
\mathsf B(J)^\perp
=
\{\text{vertex functions constant on every component of }J\},
\]

one obtains

\[
\boxed{
\dim\bigl(\mathsf B(R_1)\cap\mathsf B(R_0)\bigr)
=
|V(R_{W,t})|-c(R_1)-c(R_0)+c(R_{W,t}).
}
\]

Indeed the component-constant spaces for `R_1` and `R_0` intersect in the
component-constant space for their union `R_{W,t}`.

This gives a direct rank test for the unsummed correction space. The only further
loss comes from fibrewise summation under `q`.

## 6. Dual obstruction

Let

\[
\mathsf K(J):=\mathsf B(J)^\perp
\]

be the space of functions constant on the components of `J`.

### Corollary 6.1

A vertex functional `lambda\in\mathbf F_2^{V(Q_W)}` annihilates every admissible
`t`-switch correction if and only if

\[
\boxed{
q^*\lambda\in \mathsf K(R_1)+\mathsf K(R_0).
}
\]

Equivalently, the pullback of `lambda` is a sum of one function constant on every
`R_1`-component and one function constant on every `R_0`-component.

#### Proof

Use

\[
(\mathsf B(R_1)\cap\mathsf B(R_0))^\perp
=
\mathsf K(R_1)+\mathsf K(R_0)
\]

and the adjunction between fibrewise sum `q_*` and pullback `q^*`. ∎

This is the exact dual of the admissible correction map. It is a two-partition
harmonic obstruction: failure is controlled by the interaction of the component
partitions of the two outside-colour classes.

## 7. A clean sufficient condition

Suppose, componentwise, that

1. `R_{W,t}` is connected over each connected component of `Q_W` rather than
   several `R`-components being merged only by `A_t`; and
2. both spanning colour subgraphs `R_0` and `R_1` are connected on that component.

Then

\[
\mathsf B(R_1)=\mathsf B(R_0)=\mathsf B(R_{W,t}),
\]

and fibrewise summation maps this full even-sum boundary space onto the boundary
space of `Q_W`. Hence every plane defect is correctable by one admissible
`t`-switch.

The connectivity hypothesis is deliberately strong, but it identifies the
correct mechanism: single-switch failure can occur only because the two outside
colour classes induce incompatible component partitions, or because the deleted
`t`-matching merges distinct refined components at the final quotient.

## 8. Strategic consequence

The earlier description of the nowhere-zero condition as a nonlinear
colour-avoidance barrier was too pessimistic. Once the switch direction `t` is
fixed, avoidance of the unique dangerous colour class `A_t` simply replaces
`\mathcal C(G)` by the linear subspace `\mathcal C(G-A_t)`.

Thus the one-switch problem is completely linear:

\[
\boxed{
\mathcal C(G-A_t)
\longrightarrow
\mathbf F_2^{\pi_0(G_W)},
\qquad
z\longmapsto d_W(f^z_t)+d_W(f).
}
\]

Its image, dimension, and annihilator are given above. The next frontier is not
to linearize this map further, but to understand whether the union of the three
direction images for a plane must contain the current defect, and if not, how two
successive switches interact.