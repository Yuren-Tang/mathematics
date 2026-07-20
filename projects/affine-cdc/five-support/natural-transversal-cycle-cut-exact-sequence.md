# The natural-transversal cycle--cut exact sequence

## 1. Purpose

For the route-capped cubic graph `\widehat Q`, the flag-line carrier

$$
F=\mathcal L(\widehat Q)
$$

has a canonical local-transition transversal.  Restriction to that transversal is the cographic matroid of `\widehat Q`, so every full transition-matroid cocycle projects to a binary cycle of the physical capped graph.

This chapter identifies the kernel of that projection exactly.

At every original cubic vertex `x`, take, at each incident edge `e`, the two cross transitions at the line vertex `v_e`.  Their union is a full transition-matroid cocycle.  Summing these vertex cocycles over a shore `S` cancels the contributions of edges internal to the shore and leaves the two cross transitions precisely on the graph cut `\delta(S)`.

The resulting cut cocycles exhaust the kernel of the natural projection.  Hence there is a canonical short exact sequence

$$
\boxed{
0
\longrightarrow
\operatorname{Cut}(\widehat Q)
\longrightarrow
\operatorname{Cocycle}(M_\tau(F))
\longrightarrow
\operatorname{Cycle}(\widehat Q)
\longrightarrow
0.
}
$$

Thus a full isotropic cocycle on the line-graph carrier is a physical cycle--cut extension, not an unrelated circle-graph object.  In particular, a cap cocircuit with zero natural projection is exactly a physical bond of the capped cubic graph.

## 2. Circuit-partition vertex cocycles

Let `F` be a `4`-regular multigraph and let `P` be a circuit partition.  At a vertex `v` of `F`, the transition chosen by `P` has two pairs.  A circuit `\gamma\in P` is **singly incident** at `v` when exactly one of these two pairs belongs to `\gamma`.

For `\gamma\in P`, define a transition set

$$
K_P(\gamma)
$$

as follows.  At every vertex where `\gamma` is singly incident, include the two transitions other than the transition used by `P`; include nothing at all other vertices.

### Lemma 2.1 — partition-circuit cocycle

For every circuit `\gamma` of `P`,

$$
\boxed{K_P(\gamma)\text{ is a cocycle of }M_\tau(F).}
$$

Within one connected component of `F`, the sum of the sets `K_P(\gamma)` over all circuits `\gamma` of `P` is zero.

#### Proof

Choose an Euler system and an `IAS` representation of the transition matroid.  The standard core vector of a partition circuit `\gamma` is the binary row coefficient recording the vertices at which `\gamma` is singly incident.  The local interlacement calculation has three cases according to which transition of the vertex triple is used by `P`; in every case the resulting row-space word has weight two on the triple, omits the transition of `P`, and is zero when `\gamma` is not singly incident.  This is exactly `K_P(\gamma)`.

At a vertex joining two distinct partition circuits, each of those two circuits contributes the same pair of non-`P` transitions, so their sum is zero.  At a vertex at which one partition circuit is doubly incident, no circuit contributes.  Hence summing over all partition circuits in a component gives zero. ∎

This is the full-matroid lift of the ordinary vertex-cut relation in the touch-graph of `P`.

## 3. Vertex stars of the natural partition

Now let `G` be a cubic multigraph and

$$
F=\mathcal L(G).
$$

Let `P_{\mathrm{loc}}` be the circuit partition using the local transition at every line vertex.  Its circuits are the vertex triangles

$$
\Delta_x
\qquad(x\in V(G)).
$$

For one vertex `x\in V(G)`, put

$$
K_x
=
K_{P_{\mathrm{loc}}}(\Delta_x).
$$

### Theorem 3.1 — physical star cocycle

The cocycle `K_x` has the exact support

$$
\boxed{
K_x
=
\bigcup_{e\ni x}
\{\text{the two cross transitions at }v_e\}.
}
$$

#### Proof

The vertex circuit `\Delta_x` is singly incident at `v_e` exactly when `e` has one end-flag at `x`.  The transition used by `P_{\mathrm{loc}}` is the local transition, so Lemma 2.1 includes the two cross transitions there.  At all other line vertices `\Delta_x` is not incident. ∎

The only linear relations among the `K_x` are the component relations

$$
\sum_{x\in V(H)}K_x=0
$$

for connected components `H` of `G`.

## 4. Cut cocycles

For a vertex set `S\subseteq V(G)`, define

$$
K(S)
=
\sum_{x\in S}K_x.
$$

### Theorem 4.1 — cross-pair cut formula

For every edge `e=uv` of `G`:

- if either both or neither of `u,v` lie in `S`, then `K(S)` is zero on the transition triple at `v_e`;
- if exactly one of `u,v` lies in `S`, then `K(S)` contains both cross transitions and omits the local transition at `v_e`.

Equivalently,

$$
\boxed{
K(S)
=
\bigcup_{e\in\delta_G(S)}
\{\text{both cross transitions at }v_e\}.
}
$$

#### Proof

An edge with two ends in `S` occurs in two vertex-star cocycles and cancels.  An edge with no end in `S` occurs in none.  A cut edge occurs in exactly one `K_x` and retains its two cross transitions. ∎

Hence the map

$$
\kappa_G:
\operatorname{Cut}(G)
\longrightarrow
\operatorname{Cocycle}(M_\tau(\mathcal L(G)))
$$

which sends the cut vector `\delta(S)` to `K(S)` is a well-defined injective linear map.  Its image consists of cocycles with no local-transition coordinates.

## 5. The natural projection

Let

$$
T_{\mathrm{loc}}
$$

be the local-transition transversal.  For a full cocycle `D`, define

$$
\pi_{\mathrm{loc}}(D)
=
D\cap T_{\mathrm{loc}},
$$

identified with an edge set of `G`.

The natural-touch theorem gives

$$
M_\tau(\mathcal L(G))|T_{\mathrm{loc}}
\cong
M^*(G).
$$

Therefore

$$
\pi_{\mathrm{loc}}(D)
\in
\operatorname{Cycle}(G).
$$

### Theorem 5.1 — cycle--cut exact sequence

Let `G` have `c(G)` connected components.  Then

$$
\boxed{
0
\longrightarrow
\operatorname{Cut}(G)
\xrightarrow{\ \kappa_G\ }
\operatorname{Cocycle}(M_\tau(\mathcal L(G)))
\xrightarrow{\ \pi_{\mathrm{loc}}\ }
\operatorname{Cycle}(G)
\longrightarrow
0
}
$$

is exact.

#### Proof

The map `\pi_{\mathrm{loc}}` is the restriction of the row space to the columns in `T_{\mathrm{loc}}`.  It is surjective onto the cocycle space of the restricted matroid.  Since that restriction is `M^*(G)`, its cocycle space is `\operatorname{Cycle}(G)`.

Every `K(S)` contains only cross transitions, so

$$
\operatorname{im}\kappa_G
\subseteq
\ker\pi_{\mathrm{loc}}.
$$

Let

$$
m=|E(G)|,
\qquad
n=|V(G)|,
\qquad
c=c(G).
$$

The full transition matroid of the `4`-regular graph `\mathcal L(G)` has rank `m`, so its cocycle space has dimension `m`.  The cycle space of `G` has dimension

$$
m-n+c.
$$

Hence

$$
\dim\ker\pi_{\mathrm{loc}}
=
n-c.
$$

The cut space of `G` also has dimension `n-c`, and `\kappa_G` is injective.  Therefore its image equals the kernel. ∎

### Corollary 5.2 — unique kernel interpretation

A full transition-matroid cocycle has zero natural projection if and only if it is of the form

$$
K(S)
$$

for a graph shore `S`, unique up to replacing `S` by its complement inside each connected component.

Thus every zero-projection cocycle is literally a graph cut with each cut edge replaced by its pair of cross transitions.

## 6. Cocircuits with zero projection

Suppose now that `D` is a cocircuit of the full transition matroid and

$$
\pi_{\mathrm{loc}}(D)=0.
$$

By Corollary 5.2,

$$
D=K(S)
$$

for some nonempty cut `\delta_G(S)`.

### Theorem 6.1 — zero-projection cocircuits are physical bonds

The graph cut

$$
\delta_G(S)
$$

is an inclusion-minimal nonempty cut, hence a bond of `G`.

Conversely, if `K(S)` is not a cocircuit, then the cut contains a proper nonempty cut whose cross-pair cocycle is a proper cocycle subset.

#### Proof

If `\delta(T)` were a nonempty proper cut contained in `\delta(S)`, then

$$
K(T)
\subsetneq
K(S)=D
$$

would be a nonzero cocycle properly contained in the cocircuit `D`, impossible.  Thus `\delta(S)` is cut-minimal. ∎

The theorem is one-way as stated: a graph bond need not automatically produce a cocircuit of the full transition matroid without checking that no cocycle with non-cut local coordinates lies properly inside its cross-pair support.  What is exact is that every zero-projection full cocircuit exposes a physical bond.

## 7. Application to the two-cap residue

Return to

$$
G=\widehat Q
$$

with cap edges `z_{12},z_{34}`.

A zero-projection cap cocircuit contains both cross transitions at every active cap triple.  Therefore the corresponding cap edge lies in its physical bond.

### Corollary 7.1 — coupled zero-projection separator

Let `D` be one cocircuit containing both residue transitions and suppose

$$
\pi_{\mathrm{loc}}(D)=0.
$$

Then

$$
D=K(S)
$$

for a physical bond `\delta_{\widehat Q}(S)` containing both cap edges

$$
z_{12},z_{34}.
$$

After removing the caps, the bond gives a genuine internal edge separator of the original four-pole.  Each shore contains one terminal flag from `{1,2}` and one from `{3,4}`, hence exactly two terminal flags.  Its internal boundary therefore has even cardinality.

This is already a terminal-even physical decomposition interface.

### Corollary 7.2 — separated zero-projection separators

Let

$$
C=D_{12}\sqcup D_{34}
$$

be a separated minimal cap completion.

1. If `\pi_{\mathrm{loc}}(D_{12})=0`, then `D_{12}` exposes a physical bond containing `z_{12}` and not `z_{34}`.
2. If `\pi_{\mathrm{loc}}(D_{34})=0`, then `D_{34}` exposes a physical bond containing `z_{34}` and not `z_{12}`.

For a one-cap bond, one terminal pair is split and the other is unsplit.  A shore therefore contains an odd number of terminal flags, and the internal boundary has odd cardinality.  This is a physical one-ended separator, to be routed through the existing three-cut or bounded-interface machinery according to its size and cyclicity.

## 8. Mechanism update

The coupled/separated cap-cocircuit frontier now has an exact first physical split.

### Zero natural projection

$$
\boxed{
\pi_{\mathrm{loc}}(D)=0
\Longrightarrow
\text{physical bond in }\widehat Q.
}
$$

This branch is no longer an isotropic-prime candidate.

### Nonzero natural projection

If

$$
\pi_{\mathrm{loc}}(D)=Z\ne0,
$$

then `Z` is a physical cycle vector.  The cocircuit is a nontrivial extension of this cycle by a cut-space word.  The remaining theorem must exploit simultaneously:

- the cycle support `Z`;
- the cocircuit local set and cut-rank;
- the cap word;
- the cut-space ambiguity in the exact sequence;
- the fixed route-lock and flow labels.

The irreducible candidate has therefore narrowed further:

$$
\boxed{
\text{prime coupled cap cocircuit}
+
\text{nonzero physical cycle projection}
+
\text{locked terminal route}.
}
$$

Only this branch remains a plausible carrier of the physical DDD support-label class.

## 9. Reliability boundary

Proved here:

- partition-circuit cocycles for the natural partition;
- explicit vertex-star cocycles on the line graph;
- the cross-pair formula for graph cuts;
- the canonical cycle--cut short exact sequence;
- exact classification of zero natural projection;
- physical-bond consequence for zero-projection cocircuits;
- terminal parity of coupled and separated zero-projection cap bonds.

Not proved here:

- a canonical splitting of the cycle--cut exact sequence;
- composition-safe reduction for every exposed bond regardless of size;
- classification of nonzero-projection cocircuits;
- compatibility of the physical cycle projection with `\Gamma_g` transition systems;
- identification of the residual prime coupled branch with DDD;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, DOI, or merge status is implied.
