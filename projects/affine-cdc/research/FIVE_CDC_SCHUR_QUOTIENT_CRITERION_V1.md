# The Schur-quotient criterion for five-support affine covers

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level research checkpoint; not canonical pending review

## 1. Coordinate slice of a rank-three flow

Let

\[
f:E(G)\to\mathbf F_2^3\setminus\{0\}
\]

be a nowhere-zero flow on a finite cubic loopless multigraph. Fix a nonzero
functional

\[
b\in(\mathbf F_2^3)^*,
\]

and put

\[
W:=\ker b.
\]

Choose a basis `x,y` of `W^*` and use the same letters for the corresponding
binary coordinate flows of `f`. Thus

\[
f(e)=(b_e,x_e,y_e).
\]

The three coordinate words `b,x,y` lie in the binary cycle space of `G`.

Let `G_0` be the spanning subgraph with edge set

\[
E(G_0)=\{e:b_e=0\}.
\]

This is exactly the plane subgraph `G_W` from the fixed-flow five-support
reduction.

## 2. The quotient graph

Contract every connected component of `G_0` to one vertex. Retain every edge
with `b_e=1`; edges whose endpoints lie in the same component become loops. Call
the resulting multigraph

\[
Q_b.
\]

The words `x` and `y` descend to binary flows on `Q_b`. Indeed, summing either
coordinate flow equation over a contracted component cancels all internal
edges and leaves even parity on the quotient incidence boundary.

The quotient is itself Eulerian, because the all-one word on its non-loop edges
is the descended binary flow `b`.

## 3. Obstruction as a Schur-product boundary

For binary edge words, write

\[
(x*y)_e:=x_ey_e.
\]

### Theorem 3.1 — Schur-quotient criterion

For a component `K` of `G_0`, the fixed-plane five-support obstruction is

\[
\boxed{
\Omega_W(K)
=
\sum_{e\in\delta_G(K)}x_ey_e.
}
\]

Consequently, the fixed flow admits a compatible affine family with at most
five nonempty indexed supports of direction `W` if and only if

\[
\boxed{
x*y\in\mathcal C(Q_b),
}
\]

where `\mathcal C(Q_b)` is the binary cycle space of the quotient graph.

#### Proof

The four outside colours have coordinate pairs

\[
(x_e,y_e)\in\mathbf F_2^2.
\]

By the colour-cut formula, the obstruction may be computed as the parity of the
outside colour `(0,0)` on the cut `δ_G(K)`:

\[
\Omega_W(K)
=
\sum_{e\in\delta_G(K)}(1+x_e)(1+y_e).
\]

Because `δ_G(K)` is a cut and `b,x,y` are flows,

\[
\sum_{e\in\delta_G(K)}1
=
\sum_{e\in\delta_G(K)}b_e
=0,
\]

and

\[
\sum_{e\in\delta_G(K)}x_e
=
\sum_{e\in\delta_G(K)}y_e
=0.
\]

Expanding the indicator therefore leaves

\[
\Omega_W(K)
=
\sum_{e\in\delta_G(K)}x_ey_e.
\]

After contraction, this is exactly the vertex boundary of the edge word `x*y`
at the quotient vertex corresponding to `K`. Hence all component obstructions
vanish exactly when `x*y` is a binary flow on `Q_b`. ∎

## 4. Basis independence

The condition does not depend on the chosen basis of `W^*`. For example,
replacing `y` by `x+y` changes the product to

\[
x*(x+y)=x+x*y.
\]

Since `x` is already a flow on `Q_b`, one product is a flow if and only if the
other is. The other generators of `GL(2,2)` are similar.

Thus the criterion belongs intrinsically to the plane `W`, not to its
coordinates.

## 5. Four-colour parity at quotient vertices

At a quotient vertex, let

\[
n_{ij}
\qquad(i,j\in\mathbf F_2)
\]

be the parity of incident quotient edges with coordinate pair `(i,j)`. The flow
conditions for `1,x,y` imply

\[
n_{00}=n_{01}=n_{10}=n_{11}.
\]

The common value is the affine five-support obstruction. Equivalently, every
quotient vertex is of exactly one of two types:

1. **balanced:** all four colour parities are even;
2. **obstructed:** all four colour parities are odd.

The Schur-product equation distinguishes the two types, since

\[
\partial(x*y)=n_{11}.
\]

In particular, the obstructed quotient vertices occur in an even number in
each connected component of `Q_b`, by the handshaking identity for the boundary
of an edge word.

## 6. Relation to the projected zero matching

Choose `a∉W` so that the outside colour `(0,0)` is represented by `a`. In the
decomposition

\[
f=w+b\,a,
\]

this colour class is exactly the zero set

\[
M=\{e:w(e)=0\}.
\]

The matching/four-flow bridge identifies `M` as the intersection of the two
distinguished even supports in a five-support cover. The Schur formula says

\[
\Omega_W(K)
=
|M\cap\delta_G(K)|\pmod2.
\]

Thus the following are the same condition:

- the affine forbidden-three-colour system is soluble;
- every `G_0` component has even incidence with `M`;
- the zero matching is Eulerian after contraction;
- the Schur product `x*y` is a flow on `Q_b`;
- a second even support can be drawn through the matching inside the contracted
  components.

## 7. Conceptual position

The ordinary rank-three compatibility theorem says that the affine obstruction
always vanishes before any restriction on the number of support indices.

The five-support strengthening introduces a new sliced obstruction:

\[
\boxed{
\partial_{Q_b}(x*y).
}
\]

This is not the original `H^1` compatibility class. It is a Schur-product defect
created by restricting the solution to five of the eight affine indices.

The criterion explains why the gauge and tensor branches become relevant again:
`x*y` is the basic quadratic Schur word of two cycle-space coordinates. The next
problem is to control this defect while varying the rank-three flow, rather than
only moving inside the compatible-family torsor.

## 8. Next problem

For every bridgeless cubic graph, can one choose three binary flows

\[
b,x,y\in\mathcal C(G)
\]

such that

1. `(b_e,x_e,y_e)\neq(0,0,0)` on every edge;
2. after contracting the `b=0` subgraph, the descended product `x*y` is a flow?

This is an exact coordinate form of the AffineCDC five-support problem.