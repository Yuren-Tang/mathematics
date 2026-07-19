# Route-locked quotient flow as a Tait-phase model

## 1. Purpose

The abstract quartic witness theorem shows that common-cut incidence alone cannot bound the residual nonflat core.  The next input must use the fact that all four scalar sheets arise from one nowhere-zero full-rank

$$
c:E(Q)\longrightarrow V\setminus\{0\},
\qquad
V\cong\mathbf F_2^3,
$$

with all four terminal values equal to one colour `g`.

This chapter gives an exact physical compression of that datum.  After quotienting by `\langle g\rangle`, the flow is a degenerate Tait flow whose zero edges are exactly the `g`-edges.  One additional binary phase recovers the full `\mathbf F_2^3` flow.  The four scalar sheets form an affine plane whose three nonzero differences are quotient Kempe cycle systems.

This structure is absent from an arbitrary quartic witness design and is therefore the first available mechanism for excluding or composing the abstract unbounded ladders.

## 2. Splitting along the terminal colour

Let `Q` be a finite cubic four-pole, with all terminal semiedges assigned the same nonzero colour

$$
g\in V.
$$

Let

$$
E_g=\{e:c(e)=g\}.
$$

Choose a linear complement

$$
V=\langle g\rangle\oplus U,
\qquad
U\cong\mathbf F_2^2.
$$

Write

$$
\pi:V\to U
$$

for the quotient projection and let

$$
\alpha:V\to\mathbf F_2
$$

be the coordinate functional with

$$
\alpha(g)=1,
\qquad
\alpha|_U=0.
$$

Define

$$
\bar c=\pi\circ c,
\qquad
\sigma=\alpha\circ c.
$$

Thus every edge colour has the unique form

$$
c(e)=\sigma(e)g+\bar c(e).
$$

## 3. Exact quotient-phase equivalence

### Theorem 3.1 — Tait-phase representation

The nowhere-zero `V`-flow `c` is equivalent to the following pair of data:

1. a `U`-valued flow
   $$
   \bar c:E(Q)\to U
   $$
   whose zero set is exactly `E_g`;
2. a binary relative flow
   $$
   \sigma:E(Q)\to\mathbf F_2
   $$
   satisfying
   $$
   \sigma(e)=1
   \qquad(e\in E_g).
   $$

The reconstruction is

$$
\boxed{c(e)=\sigma(e)g+\bar c(e).}
$$

#### Proof

Both `\pi` and `\alpha` are linear, so composing the Kirchhoff equations for `c` with them gives the flow equations for `\bar c` and `\sigma`.

One has `\bar c(e)=0` exactly when `c(e)\in\langle g\rangle`.  Since `c(e)` is nonzero, this is equivalent to `c(e)=g`; in that case `\sigma(e)=1`.

Conversely, suppose `\bar c` and `\sigma` satisfy the stated conditions.  Their direct-sum combination is a `V`-flow.  If `\bar c(e)\ne0`, then `\sigma(e)g+\bar c(e)` is nonzero.  If `\bar c(e)=0`, then `e\in E_g` and `\sigma(e)=1`, so the reconstructed value is `g`.  Hence the reconstructed flow is nowhere zero and has exactly the prescribed `g`-edges.  ∎

The choice of complement changes the phase coordinate, but the quotient flow in

$$
V/\langle g\rangle
$$

and all statements invariant under affine phase change are canonical.

## 4. Local quotient law

### Theorem 4.1 — Tait vertices and defect vertices

At every cubic vertex exactly one of the following holds.

1. **Ordinary quotient vertex.**  No incident edge lies in `E_g`.  The three quotient values are the three distinct nonzero elements of `U`.
2. **Defect vertex.**  Exactly one incident edge lies in `E_g`.  The other two quotient values are equal to one nonzero element
   $$
   q_v\in U\setminus\{0\},
   $$
   and their phase bits are opposite.

In particular, `E_g` is a matching on the cubic vertices.

#### Proof

Two incident `g`-edges would force the third flow value to be zero, so at most one incident edge lies in `E_g`.

If no incident edge is in `E_g`, all three quotient values are nonzero and sum to zero in `U\cong\mathbf F_2^2`.  Two equal values would force the third to be zero, so the three are distinct and exhaust `U\setminus\{0\}`.

If one incident edge has value `g`, the other two full colours sum to `g`.  Their quotient values are therefore equal and nonzero.  Applying `\alpha` to the vertex equation shows that their phase bits sum to one.  ∎

Thus `\bar c` is a Tait three-edge-colouring away from the matched defect edges `E_g`; at an endpoint of a defect edge, one quotient colour passes straight through twice.

## 5. The four scalar sheets are an affine plane

Every functional in

$$
\Lambda_g
=
\{\lambda\in V^*:\lambda(g)=1\}
$$

has a unique expression

$$
\lambda_\phi
=
\alpha+\phi\circ\pi,
\qquad
\phi\in U^*.
$$

Let `H_\phi` be its scalar relative even subgraph.  Its edge indicator is

$$
h_\phi(e)
=
\lambda_\phi(c(e))
=
\sigma(e)+\phi(\bar c(e)).
$$

For `\delta\in U^*`, put

$$
K_\delta
=
\{e:\delta(\bar c(e))=1\}.
$$

### Theorem 5.1 — affine-sheet/Kempe-cycle theorem

For all `\phi,\psi\in U^*`,

$$
\boxed{
H_\phi\triangle H_\psi
=
K_{\phi+\psi}.
}
$$

If `\delta\ne0`, then `K_\delta` is the union of exactly two of the three nonzero quotient-colour classes.  It contains no terminal or internal `g`-edge and is a disjoint union of graph cycles.

Consequently the four scalar sheets form the affine plane

$$
\boxed{
H_0,
\quad
H_0\triangle K_{\delta_1},
\quad
H_0\triangle K_{\delta_2},
\quad
H_0\triangle K_{\delta_1+\delta_2}
}
$$

in the relative binary cycle space.

#### Proof

The indicator identity follows immediately from

$$
h_\phi+h_\psi
=(\phi+\psi)(\bar c).
$$

A nonzero functional on `U\cong\mathbf F_2^2` is one on exactly two of the three nonzero vectors, so `K_\delta` is the union of the corresponding two quotient-colour classes.

At an ordinary quotient vertex, those two colours occur once each, giving degree two in `K_\delta`.  At a defect vertex, the repeated colour contributes either both incident non-`g` edges or neither.  Thus every vertex has degree zero or two.  Since all terminal semiedges have quotient value zero, `K_\delta` has no boundary and is a disjoint union of cycles.  ∎

The four scalar circuit partitions are therefore highly correlated.  They are not four independent near-resolutions.

## 6. Endpoint selector lines

Let `v` be an endpoint of a `g`-edge.  The other two incident edges have one common quotient colour

$$
q_v\in U\setminus\{0\}
$$

and opposite phase bits.  In every scalar sheet `H_\phi`, exactly one of these two edges continues the `g`-edge.

Choose an ordering of the two continuation edges.  The selected edge is then encoded by a bit

$$
s_v(\phi)
=
\varepsilon_v+\phi(q_v)
$$

for one fixed `\varepsilon_v\in\mathbf F_2`, after possibly complementing the bit convention.

### Theorem 6.1 — affine selector theorem

The endpoint selector

$$
s_v:U^*\to\mathbf F_2
$$

is a nonconstant affine function.  Hence:

1. each continuation edge is selected in exactly two of the four scalar sheets;
2. the selector defines one of the three affine parallel classes on `U^*\cong AG(2,2)`;
3. this parallel class depends only on the quotient defect colour `q_v`.

When moving from sheet `\phi` to sheet `\phi+\delta`, the continuation at `v` swaps exactly when

$$
\delta(q_v)=1.
$$

#### Proof

The two phase bits at `v` differ by one.  Adding the common value `\phi(q_v)` therefore selects exactly one continuation edge, and the selector is affine with linear part `\phi\mapsto\phi(q_v)`.  Since `q_v\ne0`, that linear part is nonzero and balanced on the four-point affine plane.  The final statement is the difference formula for the selector.  ∎

Thus the local selector word is always affine.  The odd non-affine curvature bit cannot be generated at one endpoint; it records global component routing.

## 7. The nine edge labels and the aligned/crossed signatures

Let `e=vw` be a `g`-edge.  Its two endpoints define

$$
\tau(e)
=
(q_v,q_w)
\in
(U\setminus\{0\})^2.
$$

There are nine quotient labels.  Under `GL(U)\cong S_3`, they split into two orbits:

- **aligned:** `q_v=q_w`;
- **crossed:** `q_v\ne q_w`.

This is exactly the quotient distinction between equal and distinct complementary endpoint pairs.

For a nonzero sheet difference `\delta\in U^*`, record whether the continuation swaps at the two endpoints:

$$
\rho_e(\delta)
=
(\delta(q_v),\delta(q_w)).
$$

### Theorem 7.1 — local three-switch signature

1. If `e` is aligned, the three nonzero `\delta` give
   $$
   (0,0),\ (1,1),\ (1,1)
   $$
   in some order.
2. If `e` is crossed, the three nonzero `\delta` give
   $$
   (0,1),\ (1,0),\ (1,1)
   $$
   in some order.

#### Proof

For aligned endpoints, exactly one nonzero functional annihilates their common quotient colour and the other two evaluate to one.

For distinct nonzero `q_v,q_w`, the three nonzero functionals respectively annihilate `q_v`, annihilate `q_w`, and annihilate `q_v+q_w`; in the last case both endpoint values are one.  ∎

The crossed signature is the quotient shadow of DDD/Petersen resolution triality: the three sheet differences perform left-only, right-only, and double endpoint switches.

## 8. Consequence for quartic localisation

A physical quartic core is therefore not merely four near-resolutions of the witness set.  It carries the following enrichment:

1. one quotient label `\tau(e)\in(U\setminus\{0\})^2` on every witness `g`-edge;
2. a cyclic order of four witness edges on every closed scalar component block;
3. three fixed Kempe cycle systems `K_\delta` relating the four scalar partitions;
4. endpoint swaps prescribed by the affine selector law;
5. intervening non-`g` paths whose quotient colours and phases satisfy the local Tait-phase equations;
6. the requirement that the four terminal paths retain the route `12\mid34`.

Call this package an **enriched quartic phase design**.

The abstract quartic ladders prove that incidence rank alone is unbounded.  The Tait-phase theorem identifies the exact additional physical structure that any realizable ladder must carry.  The next localisation target is now precise:

$$
\boxed{
\text{classify or decompose enriched quartic phase designs,}
}
$$

with strict progress supplied by a singleton resolution, a two-edge transition interval, a smaller cyclic separator, a ten-state four-pole transfer, or the physical DDD `D_8` class.

## 9. Reliability boundary

Proved here:

- the exact quotient-plus-phase representation of a route-locked `\mathbf F_2^3` flow;
- the ordinary/defect local quotient law;
- the affine-plane relation among the four scalar sheets;
- the fact that all sheet differences are quotient Kempe cycle systems;
- the affine endpoint selector theorem;
- the complete aligned/crossed three-switch signatures.

Not proved here:

- that an abstract quartic witness design admits such an enrichment;
- classification or boundedness of enriched quartic phase designs;
- composition across singleton or two-edge interfaces;
- canonical identification with the physical `D_8` cohomology class;
- defect-forest pruning or the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, or DOI status is implied.