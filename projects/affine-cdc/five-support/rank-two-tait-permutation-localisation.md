# Rank-two persistent intersections and local Tait permutations

## 1. Purpose

Let

$$
w=z\odot z'
$$

be a gauge-invisible common-edge word of two physical cycles with odd ribbon intersection.  Suppose its minimal auxiliary dual-flow rank is two.

Then there is a plane

$$
U^*\le\Gamma^*
$$

and a flow

$$
u:E(G)\to U^*
$$

such that

$$
w_e=u(e)(f(e)).
$$

Let

$$
\langle h\rangle
=
\operatorname{Ann}(U^*)
\le\Gamma.
$$

The pairing identifies

$$
U^*
\cong
(\Gamma/\langle h\rangle)^*.
$$

Thus the rank-two obstruction is controlled by two `\mathbf F_2^2`-valued flows:

$$
\bar f:E(G)\to Q:=\Gamma/\langle h\rangle,
$$

and

$$
u:E(G)\to Q^*.
$$

The norm word is

$$
\boxed{w_e=u(e)(\bar f(e)).}
$$

This chapter proves that away from the zero loci of these two quotient flows, the support of `w` is an even degree-two system.  At a fully nonzero cubic vertex, the two Tait triples define a permutation of three points; the common-edge word is exactly its moved-point set.  Since an intersection of two cubic cycles cannot use all three incident edges, the permutation is never a three-cycle.

Consequently every rank-two support component is a circuit or a path whose endpoints lie at quotient-flow defects.

## 2. The quotient Fano flow

Put

$$
Q=\Gamma/\langle h\rangle
\cong\mathbf F_2^2.
$$

The quotient

$$
\bar f=\pi_h\circ f
$$

is a `Q`-valued flow.  Because `f` is nowhere zero,

$$
\bar f(e)=0
\iff
f(e)=h.
$$

Thus its zero set is the Fano colour class

$$
E_h=f^{-1}(h).
$$

### Lemma 2.1 — colour-zero matching

The set `E_h` is a matching.

#### Proof

Two incident edges of colour `h` would force the third flow value at their cubic vertex to be `h+h=0`, contradicting nowhere-zeroness. ∎

At a vertex not incident with `E_h`, the three values of `\bar f` are the three nonzero points of `Q`.  At a vertex incident with one `h`-edge, the quotient triple is

$$
0,r,r
$$

for one nonzero `r\in Q`.

## 3. The auxiliary four-flow

The dual flow

$$
u:E(G)\to Q^*
$$

has, at every cubic vertex, one of the standard binary four-flow types:

1. `0,0,0`;
2. `0,\xi,\xi` for one nonzero `\xi`;
3. the three distinct nonzero covectors of `Q^*`.

Call a vertex **dual-Tait** in the third case and **dual-defective** in the first two cases.

Similarly call a vertex **quotient-Tait** when its three `\bar f` values are nonzero, and **colour-defective** when it is incident with `E_h`.

## 4. Local Tait permutation

Let `v` be both quotient-Tait and dual-Tait.  Write the incident quotient colours as

$$
q_1,q_2,q_3=Q\setminus\{0\}
$$

and the incident dual values as

$$
\xi_1,\xi_2,\xi_3=Q^*\setminus\{0\}.
$$

Every nonzero covector `\xi` has a unique nonzero kernel point

$$
\kappa(\xi)\in Q\setminus\{0\}.
$$

Hence the local assignment

$$
q_i\longmapsto\kappa(\xi_i)
$$

defines a permutation

$$
\sigma_v\in S_3.
$$

### Theorem 4.1 — moved-point norm law

For each incident edge `i`,

$$
\boxed{
w_i=\xi_i(q_i)=1
\iff
\sigma_v(q_i)\ne q_i.}
$$

Thus the local support of `w` is exactly the moved-point set of `\sigma_v`.

#### Proof

A nonzero covector on the two-dimensional space `Q` vanishes exactly on its one-dimensional kernel, whose unique nonzero point is `\kappa(\xi_i)`.  Therefore

$$
\xi_i(q_i)=0
\iff
q_i=\kappa(\xi_i).
$$

∎

The possible local weights are consequently the possible numbers of moved points of a permutation of three elements:

$$
0,
\qquad
2,
\qquad
3.
$$

They correspond respectively to the identity, a transposition, and a three-cycle.

## 5. Exclusion of the three-cycle state

The norm support is also

$$
w=z\odot z'
$$

for two binary cycles on a cubic graph.  At one cubic vertex such an intersection has weight `0`, `1`, or `2`, but never `3`.

### Corollary 5.1 — involutive local Tait law

At every vertex which is quotient-Tait and dual-Tait,

$$
\boxed{
\sigma_v\text{ is the identity or a transposition.}
}
$$

Equivalently,

$$
\boxed{
\deg_w(v)\in\{0,2\}.}
$$

The two three-cycle assignments between the quotient Tait triple and the dual Tait triple are forbidden.

This was also checked by exact enumeration of all sixteen `Q^*`-flow triples for one fixed quotient Tait triple; the general proof is the permutation argument above.

## 6. Defect localisation of the boundary

Let

$$
D_h
$$

be the set of colour-defective vertices, i.e. the endpoints of the matching `E_h`, and let

$$
D_u
$$

be the set of dual-defective vertices.

### Theorem 6.1 — rank-two boundary localisation

The odd-degree boundary of the norm support satisfies

$$
\boxed{
\partial w
\subseteq
D_h\cup D_u.
}
$$

#### Proof

Outside `D_h\cup D_u`, both local flow triples are Tait triples.  Corollary 5.1 gives degree zero or two in `w`. ∎

Therefore every connected component of `w` is either:

- a circuit;
- a path whose two endpoints lie in `D_h\cup D_u`.

No path can terminate in the fully Tait region.

## 7. Local endpoint types

At a colour-defective vertex, the quotient triple has form

$$
0,r,r,
$$

so the `h`-coloured edge never belongs to `w`.  Any path endpoint uses one of the other two edges.

At a dual-defective vertex with triple

$$
0,\xi,\xi,
$$

the zero-dual edge never belongs to `w`.  Again, any endpoint lies on one of the repeated nonzero branches.

Thus every path component has two enriched endpoint labels recording:

- colour defect or dual defect;
- the repeated quotient or dual colour;
- the local transition pair of the two response cycles;
- the adjacent zero edge when present.

This is finite boundary data.

## 8. Componentwise odd-intersection localisation

As in dual rank one, the ribbon intersection of `z,z'` decomposes over connected components `K` of their common-edge support:

$$
\mathcal B(z,z')
=
\sum_K\epsilon(K).
$$

Hence an odd total intersection yields one component with

$$
\epsilon(K)=1.
$$

### Corollary 8.1 — one odd rank-two carrier

Every dual-rank-two persistent pair contains either:

1. one odd closed norm circuit; or
2. one odd defect-to-defect norm path with endpoints in `D_h\cup D_u`.

The arbitrary global response support is again reduced to one connected carrier with at most two boundary ports.

## 9. Relation to existing AffineCDC mechanisms

The two defect sets already have familiar meanings.

- `D_h` is controlled by one fixed Fano colour matching and the quotient Tait-phase geometry.
- `D_u` is the zero locus of an auxiliary four-flow; its nonzero support is a degree-two system and its zero regions are the standard entry point for Tait resolution, zero networks, and component holonomy.

Thus rank two does not require an unrestricted new matroid census.  The next theorem should combine the odd carrier with:

1. the two matchings/zero networks at its endpoints;
2. the quotient Kempe systems on the interior;
3. the existing ten-state four-pole interface;
4. a possible Tait escape when the auxiliary four-flow is nowhere zero on the relevant region.

## 10. Reliability boundary

Proved here:

- quotient/dual four-flow formulation of dual rank two;
- the moved-point description by a local `S_3` permutation;
- exclusion of the two three-cycle local states;
- localisation of path endpoints to colour or dual-flow defects;
- existence of one odd closed or defect-to-defect carrier.

Open:

- composition of every odd defect-to-defect carrier;
- elimination of all rank-two closed carriers;
- reduction of full dual rank three;
- identification of the final DDD class;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, DOI, or merge status is implied.
