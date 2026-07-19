# The route-capped line-graph transition carrier

## 1. Purpose

The physical `g`-component quotient is Eulerian but may have vertices of arbitrary even degree.  Standard transition-matroid and isotropic-system theory, however, is naturally formulated for `4`-regular graphs.  An arbitrary splitting of the high-degree quotient vertices would introduce choices that are not yet known to preserve the quartic curvature circuit.

The original cubic four-pole supplies a canonical `4`-regular carrier without any vertex splitting.

Close the four terminals according to the locked route `12\mid34`, and take the flag-line graph of the resulting cubic multigraph.  Every scalar even subgraph then determines a circuit partition of this one common `4`-regular graph.  Its scalar circuits occur as distinguished circuits of that partition, and the closed-component incidence matrices used in common-cut localisation are literal one-sided incidence matrices of the corresponding touch-graphs.

This places the four scalar sheets inside one standard transition matroid.  The remaining theorem is to identify the pointed curvature circuit with a transverse circuit, cocircuit, or connectivity separation of that carrier.

## 2. Route closure

Let `Q` be the route-locked cubic four-pole with terminal semiedges labelled

$$
1,2,3,4
$$

and terminal colour `g`.  All four scalar sheets route the terminals as

$$
12\mid34.
$$

Join terminal semiedges `1,2` to form one edge

$$
z_{12},
$$

and join `3,4` to form

$$
z_{34}.
$$

Denote the resulting closed cubic multigraph by

$$
\widehat Q.
$$

Extend the flow by

$$
c(z_{12})=c(z_{34})=g.
$$

For every `\phi\in U^*`, the scalar relative even subgraph `H_\phi` closes to an even subgraph

$$
\widehat H_\phi\subseteq E(\widehat Q).
$$

Its two terminal paths become two ordinary circuits after the cap edges are inserted.

The closure depends only on the already fixed route matching.  No additional pairing choice is introduced.

## 3. The flag-line graph

For a cubic multigraph `G`, define its **flag-line graph** `\mathcal L(G)` as follows.

- There is one vertex `v_e` for every edge `e` of `G`.
- At every cubic vertex `x` of `G`, its three incident edge-flags determine three line edges, one for every pair of flags.

This definition uses edge-flags rather than only edge names, so loops and parallel edges are handled without ambiguity.  At `v_e`, the two flags of `e` determine two pairs of incident line half-edges, one pair at each end-flag of `e`.

### Lemma 3.1 — four-regularity

The flag-line graph

$$
F=\mathcal L(\widehat Q)
$$

is a `4`-regular multigraph, with loops and parallel edges allowed.

#### Proof

Each flag of an edge `e` lies at a cubic vertex and is paired there with two other flags.  Hence each of the two flags of `e` contributes two line half-edges at `v_e`, for a total of four.  ∎

At every vertex `v_e` of `F`, the four incident half-edges have a distinguished partition into two endpoint pairs.  Therefore the three transitions at `v_e` are naturally:

1. the **local transition**, pairing within the two endpoint pairs;
2. two **cross transitions**, pairing across the two endpoint pairs.

## 4. Even subgraphs as circuit partitions

Let `G` be cubic and let

$$
H\subseteq E(G)
$$

be an even subgraph.  Every vertex of `G` has `H`-degree `0` or `2`.

For one edge `e` of `G`, define a transition `\tau_H(e)` at `v_e\in\mathcal L(G)`.

### Unselected edge

If `e\notin H`, use the local transition at `v_e`.

### Selected edge

If `e\in H`, then at each end-flag of `e` exactly one of the other two incident edges lies in `H`.  Use the cross transition which pairs:

- the line half-edge toward the selected continuation at one end with the line half-edge toward the selected continuation at the other end;
- the two remaining line half-edges with each other.

The transitions `\tau_H(e)` for all `e` determine a circuit partition

$$
P(H)
$$

of `\mathcal L(G)`.

### Theorem 4.1 — canonical even-subgraph encoding

The assignment

$$
H\longmapsto P(H)
$$

has the following properties.

1. It is canonical.
2. It is injective: one recovers
   $$
   e\in H
   \quad\Longleftrightarrow\quad
   \tau_H(e)\text{ is a cross transition}.
   $$
3. Every circuit `C` of `H` gives one distinguished circuit `\widetilde C` of `P(H)`.
4. The distinguished circuit `\widetilde C` passes through `v_e` exactly when `e\in C`.

#### Proof

At a cubic vertex of `G` with `H`-degree two, the line edge joining the two selected edges is an `H`-corner.  At a selected edge `e`, the chosen cross transition pairs the `H`-corner at one endpoint with the `H`-corner at the other endpoint.  Hence the `H`-corners concatenate exactly around the circuits of `H`.

At an unselected edge the local transition is used, so no distinguished `H`-circuit passes through its line vertex.  The local-versus-cross distinction recovers the selected edge set, proving injectivity.  ∎

The remaining circuits of `P(H)` use the complementary transition tracks.  They are part of the carrier but are not scalar components of `H`.

## 5. The four scalar transversals

Apply Theorem 4.1 to the four closed scalar subgraphs:

$$
P_\phi=P(\widehat H_\phi),
\qquad
\tau_\phi=\tau(P_\phi)
\qquad(\phi\in U^*).
$$

Thus the route-locked flow determines four transition transversals of the one transition matroid

$$
M_\tau(F).
$$

No expansion of a high-degree vertex of `\Gamma_g` is involved.

## 6. Unified aligned/crossed local law

Fix an edge `e=uv` of `\widehat Q`, with

$$
c(e)=x\ne0.
$$

At endpoint `u`, the other two flow colours form one complementary pair

$$
A_u(e)=\{a,a+x\}.
$$

Define `A_v(e)` similarly.

Call `e`:

- **aligned** if `A_u(e)=A_v(e)`;
- **crossed** if `A_u(e)\ne A_v(e)`.

This extends the earlier aligned/crossed classification of `g`-edges to every edge of the route-capped graph.

### Theorem 6.1 — four-sheet transition distribution

At the line vertex `v_e`, the four scalar transversals have the following exact distributions among the three transitions.

#### Non-`g` aligned edge

If `x\ne g` and `e` is aligned, then:

- two sheets use the local transition;
- the other two sheets use the same cross transition.

The distribution is

$$
\boxed{2+2+0.}
$$

#### Non-`g` crossed edge

If `x\ne g` and `e` is crossed, then:

- two sheets use the local transition;
- one sheet uses one cross transition;
- one sheet uses the other cross transition.

The distribution is

$$
\boxed{2+1+1.}
$$

#### `g`-aligned edge

If `x=g` and `e` is aligned, all four sheets use the same cross transition:

$$
\boxed{4+0+0.}
$$

#### `g`-crossed edge

If `x=g` and `e` is crossed, two sheets use each cross transition and no sheet uses the local transition:

$$
\boxed{2+2+0.}
$$

#### Proof

For `x\ne g`, the affine function

$$
\phi\longmapsto\lambda_\phi(x)
$$

is balanced.  Hence exactly two sheets omit `e` and use the local transition, while exactly two select it and use cross transitions.

The difference between the two selecting sheets is the unique nonzero functional `\delta` with `\delta(x)=0`.  At one endpoint, the selected continuation swaps precisely when `\delta` is one on the corresponding complementary pair.  Equal endpoint pairs give equal swap decisions and therefore the same cross transition.  Distinct endpoint pairs give opposite swap decisions and therefore the two different cross transitions.

For `x=g`, all four sheets select `e`.  The cross-transition bit is the sum of the two affine endpoint-selector bits.  It is constant when the endpoint complementary pairs agree and balanced when they differ.  ∎

### Corollary 6.2

The DDD aligned/crossed atom distinction is the `g`-edge sector of a uniform line-graph transition law valid on every edge of the capped four-pole.

The local transition bit on a `g`-edge is affine in the sheet parameter.  Hence nonflat curvature is not a single-vertex transition defect; it remains a global circuit-routing obstruction.

## 7. Touch-graph realization of scalar incidence

For one sheet `\phi`, let

$$
\mathcal D_\phi
$$

be the distinguished circuits of `P_\phi` corresponding to the circuit components of `\widehat H_\phi`.

Let

$$
\operatorname{Tch}(P_\phi)
$$

be the touch-graph of the circuit partition: its vertices are the circuits of `P_\phi`, and every vertex `v_e` of `F` gives one touch edge labelled by `e`.

### Theorem 7.1 — one-sided touch incidence

For every edge `e\in\widehat H_\phi`, the touch edge labelled `e` has exactly one endpoint in `\mathcal D_\phi`.  If that endpoint is the distinguished circuit corresponding to `C`, then

$$
e\in C.
$$

Consequently, the matrix

$$
B_\phi(C,e)
=
1_{e\in C}
$$

is the incidence matrix of the `\mathcal D_\phi` shore of the touch-graph, restricted to selected edges.

#### Proof

At a selected edge `e`, the cross transition has one pair on the distinguished `H`-track and one pair on the complementary track.  Therefore the touch edge at `v_e` joins the corresponding distinguished circuit to a complementary circuit.  The distinguished track is the one belonging to the unique component `C` of `\widehat H_\phi` containing `e`.  ∎

### Corollary 7.2 — common-cut matrices inside touch-graphs

Restrict `B_\phi` to:

- internal `g`-edges;
- distinguished circuits arising from closed scalar components before route capping.

The resulting matrix is exactly the sheet block of the closed-component incidence matrix used in common-cut localisation.

Thus the pointed curvature circuit is represented inside four one-sided touch-incidence projections of circuit partitions of one common `4`-regular graph.

## 8. Relation to transition and isotropic matroids

The `4`-regular graph `F` has its standard transition matroid

$$
M_\tau(F),
$$

and the four scalar sheets are four explicit transition transversals

$$
\tau_\phi\subseteq E(M_\tau(F)).
$$

The route-capped carrier therefore gives access to:

- circuit-nullity formulas for the four partitions;
- touch-graph cycle spaces;
- interlacement presentations;
- isotropic-system connectivity and split theory;
- connected sums, separations, and balanced mutations of `4`-regular graphs.

However, the present theorem does **not** yet identify the support-minimal curvature witness with a circuit or cocircuit of `M_\tau(F)`.  The common-cut matrix records only the distinguished scalar-circuit shore of each touch-graph, and the terminal paths require the two route-cap edges.

## 9. Exact next target

The next bridge should prove one of the following.

1. **Transverse-circuit identification.**  The pointed curvature circuit, after adding the appropriate route-cap data, is a transverse circuit or cocircuit of `M_\tau(F)`.
2. **Touch-boundary split.**  A support-minimal witness gives a low-order separation in one of the four touch-graphs, hence a connected sum or balanced-mutation interface in `F`.
3. **Isotropic connectivity dichotomy.**  Failure of such a separation forces a prime isotropic carrier, whose local transition distributions reduce to the physical `D_8` class.
4. **Comparison with `\Gamma_g`.**  A line-graph separation projects to a terminal-even edge cut or transition two-sum in the physical `g`-component quotient, where cut lifting to `Q` is exact.

The carrier construction is canonical; the missing issue is now the exact matroidal status of the curvature circuit.

## 10. Reliability boundary

Proved here:

- canonical route closure according to `12\mid34`;
- construction of the common `4`-regular flag-line graph;
- canonical injection from cubic even subgraphs to line-graph circuit partitions;
- realization of scalar components as distinguished partition circuits;
- exact four-sheet transition distribution on aligned/crossed `g` and non-`g` edges;
- one-sided touch-graph incidence representation of the common-cut matrices.

Not proved here:

- that the curvature witness is a circuit or cocircuit of the transition matroid;
- that isotropic connectivity yields a physical separator in `\Gamma_g`;
- that balanced mutation is composition-safe for five-support covers;
- a line-graph proof of the physical DDD comparison;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, or DOI status is implied.
