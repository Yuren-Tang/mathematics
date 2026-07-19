# Five-support covers as singular-quotient anisotropic lifts

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level research checkpoint; not canonical pending review  
**Parent:** `FIVE_CDC_ANISOTROPIC_RANK_FOUR_FLOW_V1.md`

## 1. The invariant quotient

Let `(H,q)` be the four-dimensional minus-type quadratic space over `F₂`; one
may take `(H,q)=(H_5,q_5)`. Choose a nonzero singular vector

\[
0\neq k\in H,
\qquad q(k)=0,
\]

and put

\[
\Gamma:=H/\langle k\rangle.
\]

Then `Γ` is a three-dimensional binary vector space. Define

\[
W_k:=k^\perp/\langle k\rangle\leq\Gamma.
\]

Since `k^\perp` has dimension three, `W_k` is a plane.

The quotient quadratic space

\[
k^\perp/\langle k\rangle
\]

is the anisotropic binary plane. Indeed, a four-dimensional minus-type space has
Witt index one, so a nonzero singular vector spans a maximal totally singular
subspace; the induced two-dimensional quotient has no nonzero singular vector.

## 2. Anisotropic fibres

Let `\bar v∈Γ` be nonzero. Its two lifts to `H` are `v` and `v+k`, and

\[
q(v+k)=q(v)+B(v,k)
\]

because `q(k)=0`.

### Theorem 2.1 — anisotropic fibre theorem

Every nonzero class of `Γ` has at least one anisotropic lift to `H`. More
precisely:

1. if `\bar v∈W_k\setminus\{0\}`, then both lifts are anisotropic;
2. if `\bar v∉W_k`, then exactly one lift is anisotropic.

#### Proof

If `\bar v∈W_k\setminus\{0\}`, choose `v∈k^\perp`. Its image in the anisotropic
plane `k^\perp/\langle k\rangle` is nonzero, hence `q(v)=1`. Also
`B(v,k)=0`, so `q(v+k)=q(v)=1`.

If `\bar v∉W_k`, then `B(v,k)=1`, and therefore

\[
q(v+k)=q(v)+1.
\]

Exactly one of the two lifts has quadratic value one. ∎

Thus the ten anisotropic vectors of `H` project onto the seven nonzero vectors
of `Γ` with multiplicities

\[
2,2,2,1,1,1,1.
\]

The three doubled classes are exactly the nonzero vectors of the canonical plane
`W_k`.

## 3. Edgewise lifting of a Fano flow

Let `G` be a finite cubic loopless multigraph and let

\[
f:E(G)\to\Gamma\setminus\{0\}
\]

be a nowhere-zero rank-three flow.

By Theorem 2.1, every edge value has an anisotropic lift to `H`. On edges with

\[
f(e)\notin W_k
\]

the lift is forced. On edges with

\[
f(e)\in W_k\setminus\{0\}
\]
there are two choices differing by `k`.

Choose any anisotropic edgewise lift

\[
\widetilde f_0:E(G)\to H.
\]

Since `f` is a flow, at every vertex `v` the sum of the three incident lifted
values projects to zero in `Γ`; hence it lies in the kernel line:

\[
\sum_{e\ni v}\widetilde f_0(e)
=\eta_v k,
\qquad
\eta_v\in\mathbf F_2.
\]

Changing the lift on an edge of the plane subgraph

\[
G_{W_k}:=(V(G),\{e:f(e)\in W_k\})
\]

adds `k` at both endpoints. Therefore the problem of turning the edgewise lift
into an actual `H`-flow is the binary incidence equation

\[
\partial_{G_{W_k}}d=\eta,
\]

where `d` is supported on the plane edges.

## 4. Exact lifting obstruction

### Theorem 4.1 — singular-quotient lift criterion

The rank-three flow `f` admits an anisotropic `H`-valued flow lift if and only if
for every connected component `K` of `G_{W_k}` one has

\[
\boxed{
\sum_{v\in V(K)}\eta_v=0.
}
\]

When nonempty, the lift space is a torsor under the binary cycle space

\[
\mathcal C(G_{W_k}).
\]

#### Proof

The image of the binary incidence map of a connected graph is the even-sum
vertex subspace. Apply this independently on each component of `G_{W_k}`. The
kernel is the cycle space. ∎

This is the invariant form of the fixed-plane component-parity obstruction. It
does not depend on a coordinate decomposition `f=(b,x,y)` or on a chosen
forbidden triple.

## 5. Identification with the colour-cut obstruction

Normalize one forced outside lift on every edge not in `W_k`. Summing the vertex
defects over a component `K` cancels all internal lifted edges and leaves the
lifted values on `δ_G(K)`. The projection of this boundary sum vanishes, so it is
either `0` or `k`.

The coefficient of `k` is exactly the common parity with which the four outside
`Γ`-colours occur on `δ_G(K)`. Hence

\[
\boxed{
\sum_{v\in K}\eta_v
=
\Omega_{W_k}(K).
}
\]

Thus the following are identical:

- the forbidden-three-colour component obstruction;
- the Schur-product boundary defect;
- the failure of the prescribed anisotropic edge lifts to satisfy conservation
  in the kernel line;
- the obstruction to lifting a rank-three flow through
  `H\twoheadrightarrow H/\langle k\rangle`.

## 6. Coordinate recovery

Under the coordinate isomorphism

\[
\Phi(b,d,x,y)
=(b,d,b+d+y,b+d+x,b+d+x+y)
\]

of the anisotropic-flow chapter, the forgotten coordinate is `d` and the kernel
vector is

\[
k=\Phi(0,1,0,0)=(0,1,1,1,1),
\]

which is singular of weight four. The quotient flow is `(b,x,y)`.

For `b=0`, nowhere-zeroness gives `(x,y)\neq(0,0)` and both values of `d` are
anisotropic, corresponding to the doubled plane fibres. For `b=1`, the
anisotropic equation uniquely prescribes

\[
d=(1+x)(1+y),
\]

corresponding to the four forced outside fibres. The global requirement that `d`
be a cycle is exactly the lifting criterion above.

## 7. Conceptual consequence

The five-support problem is not merely an arbitrary rank-four flow problem. It
has the precise form

\[
\boxed{
\text{rank-three Fano flow}
\quad\rightsquigarrow\quad
\text{anisotropic lift through a singular line quotient of }O^-(4,2).
}
\]

Ordinary AffineCDC proves that a rank-three flow admits compatible local affine
families automatically. The five-support strengthening asks whether one can
choose the rank-three flow and a singular quotient so that its one-dimensional
anisotropic lifting obstruction vanishes.

The next structural task is to compare this kernel-line obstruction with the
existing rank-four dual-Fano/Pfaffian residue. The two theories now meet at an
explicit extension

\[
0\longrightarrow\langle k\rangle
\longrightarrow H
\longrightarrow\Gamma
\longrightarrow0.
\]
