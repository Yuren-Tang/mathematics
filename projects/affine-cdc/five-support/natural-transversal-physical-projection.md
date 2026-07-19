# Natural-transversal projection to the physical capped cubic graph

## 1. Purpose

The bounded nonflat cap residue lives in the transition matroid of the canonical route-capped flag-line graph

$$
F=\mathcal L(\widehat Q).
$$

The isotropic analysis produces either one cocircuit coupling the two cap vertices or two disjoint one-cap cocircuits.  A priori, however, a cocircuit of `M_\tau(F)` is still an object on transition triples rather than an edge object in the original cubic four-pole.

The line-graph origin of `F` supplies a canonical physical projection.  At every line vertex `v_e`, there is one local transition pairing the two half-edges at each endpoint flag of `e`.  Taking this local transition at every `v_e` gives a distinguished transversal.  Its circuit partition consists exactly of the vertex triangles of `\widehat Q`, and its touch-graph is canonically `\widehat Q` itself.

Consequently every full transition-matroid cocycle has a canonical projection to an ordinary binary cycle of `\widehat Q`.  The two cap coordinates of that cycle record whether the cocycle completion uses the local transition at each cap vertex.  After deleting the caps, the projection becomes an internal cycle, a two-terminal join, or a four-terminal routing subgraph.

This is the first choice-free projection of the coupled/separated cocircuit mechanism back to the physical capped cubic graph.

## 2. The natural local transversal

Let `G` be a cubic multigraph and

$$
F=\mathcal L(G)
$$

its flag-line graph.  For an edge `e=uv` of `G`, the four line half-edges at `v_e` occur in two endpoint pairs, one pair at the `u`-flag and one pair at the `v`-flag.

Define

$$
\ell_e
$$

to be the **local transition** which pairs within these two endpoint pairs.  Put

$$
T_{\mathrm{loc}}
=
\{\ell_e:e\in E(G)\}.
$$

This is one transition from every vertex triple of `F`, hence a transversal of the transition matroid.

Let

$$
P_{\mathrm{loc}}
$$

be the circuit partition of `F` determined by `T_{\mathrm{loc}}`.

### Theorem 2.1 — vertex-triangle partition

The circuits of `P_{\mathrm{loc}}` are canonically indexed by the vertices of `G`.  For a vertex `x` of `G`, the three edge-flags incident with `x` form one line-graph triangle

$$
\Delta_x,
$$

and

$$
P_{\mathrm{loc}}
=
\{\Delta_x:x\in V(G)\}.
$$

The statement remains valid for loops and parallel edges when flags are retained: the corresponding circuit may be a degenerate triangle in the multigraph sense.

#### Proof

At a line vertex `v_e`, the local transition never joins the two endpoint sides of `e`.  A line edge created at a cubic vertex `x` is therefore followed, at its next line vertex, by the other line edge created at the same vertex `x`.  Hence the three line edges determined by the three flags at `x` concatenate among themselves and form one circuit `\Delta_x`.

Every line half-edge was created at a unique cubic vertex of `G`, so these vertex circuits are disjoint and exhaust all line edges of `F`. ∎

## 3. The natural touch-graph is the original graph

The touch-graph of a circuit partition has one vertex for each partition circuit and one edge for each vertex of the `4`-regular graph.

### Theorem 3.1 — canonical touch-graph identification

There is a canonical labelled graph isomorphism

$$
\boxed{
\operatorname{Tch}(P_{\mathrm{loc}})
\cong
G.
}
$$

Under this isomorphism:

- the touch vertex corresponding to `\Delta_x` is identified with `x\in V(G)`;
- the touch edge corresponding to the line vertex `v_e`, where `e=uv`, is identified with the original edge `e` joining `u` and `v`;
- loops and parallel edges are preserved with their flag incidences.

#### Proof

At `v_e`, the two pairs of the local transition lie on the two vertex circuits determined by the two end-flags of `e`.  Thus the touch edge labelled by `v_e` joins `\Delta_u` and `\Delta_v`, with both ends at `\Delta_u` when `e` is a loop.  This is exactly the incidence of `e` in `G`. ∎

Apply this to

$$
G=\widehat Q.
$$

The resulting transversal and partition will still be denoted by

$$
T_{\mathrm{loc}},
\qquad
P_{\mathrm{loc}}.
$$

## 4. Cographic restriction

For a circuit partition `P` of a `4`-regular graph, the standard touch-graph theorem identifies the transition-matroid restriction to the chosen transversal with the cographic matroid of the touch-graph:

$$
M_\tau(F)|\tau(P)
\cong
M^*(\operatorname{Tch}(P)).
$$

Combining this with Theorem 3.1 gives the following physical restriction.

### Theorem 4.1 — natural-transversal cographic model

For the route-capped line graph,

$$
\boxed{
M_\tau(\mathcal L(\widehat Q))|T_{\mathrm{loc}}
\cong
M^*(\widehat Q).
}
$$

The ground-set identification sends the local transition `\ell_e` to the original edge `e` of `\widehat Q`.

This is canonical: it uses only the endpoint flags of the original cubic graph and the already fixed route caps.

## 5. Projection of full cocycles

Let

$$
D\subseteq E(M_\tau(F))
$$

be a cocycle of the full transition matroid.  Define its **natural physical projection** by

$$
Z(D)
=
\{e\in E(\widehat Q):\ell_e\in D\}.
$$

Equivalently,

$$
Z(D)
\leftrightarrow
D\cap T_{\mathrm{loc}}.
$$

### Theorem 5.1 — cocycles project to physical cycles

For every full transition-matroid cocycle `D`,

$$
\boxed{
Z(D)\in Z_1(\widehat Q;\mathbf F_2).
}
$$

That is, every vertex of `\widehat Q` has even degree in `Z(D)`.

#### Proof

In a binary representation, restricting a row-space vector to a subset of columns gives a cocycle of the restricted matroid.  Hence

$$
D\cap T_{\mathrm{loc}}
$$

is a cocycle of

$$
M_\tau(F)|T_{\mathrm{loc}}.
$$

By Theorem 4.1 this restricted matroid is `M^*(\widehat Q)`.  The cocycle space of a cographic matroid is the ordinary cycle space of the graph. ∎

The projection may be empty; the theorem does not assert that every nonzero isotropic cocircuit uses a local transition.  What it does assert is that every local-transition coordinate occurring in a completion is globally constrained by the original cubic graph rather than by an arbitrary interlacement presentation.

## 6. The two cap coordinates

Let

$$
p=v_{z_{12}},
\qquad
q=v_{z_{34}}
$$

be the two cap vertices of `F`.  At each cap vertex there are:

- the local transition `\ell_{z_{rs}}`;
- two cross transitions.

The nonflat residue specifies one cross transition

$$
r_{12}
\quad\text{at }p,
\qquad
r_{34}
\quad\text{at }q.
$$

Every cocycle containing the residue meets each cap triple in exactly two elements.  Define

$$
\kappa_{12}(D)
=
1_{\ell_{z_{12}}\in D},
\qquad
\kappa_{34}(D)
=
1_{\ell_{z_{34}}\in D}.
$$

### Lemma 6.1 — cap-pair interpretation

At cap `rs`:

1. `\kappa_{rs}(D)=1` exactly when the cocycle pair consists of the prescribed residue transition and the local transition;
2. `\kappa_{rs}(D)=0` exactly when the cocycle pair consists of the two cross transitions.

Moreover,

$$
z_{rs}\in Z(D)
\iff
\kappa_{rs}(D)=1.
$$

#### Proof

A cocycle meets a vertex triple in zero or two transitions.  Since it contains the prescribed cross transition, the second transition is either the local transition or the other cross transition.  The last equivalence is the definition of `Z(D)`. ∎

Thus every cap cocycle carries a canonical physical cap word

$$
\kappa(D)
=
(\kappa_{12}(D),\kappa_{34}(D))
\in\mathbf F_2^2.
$$

## 7. Removing the caps

Put

$$
Q=\widehat Q-\{z_{12},z_{34}\},
$$

with the four exposed end-flags regarded as terminals `1,2,3,4`.

For a cycle vector `Z(D)` define

$$
Z^\circ(D)
=
Z(D)\setminus\{z_{12},z_{34}\}.
$$

### Theorem 7.1 — exact terminal boundary of the projection

The odd-degree boundary of `Z^\circ(D)` in the uncapped four-pole is

$$
\boxed{
\partial Z^\circ(D)
=
\kappa_{12}(D)(1+2)
+
\kappa_{34}(D)(3+4).
}
$$

Consequently:

1. `\kappa(D)=(0,0)`: `Z^\circ(D)` is an internal even subgraph;
2. `\kappa(D)=(1,0)`: it is a `{1,2}`-join, hence a `1`--`2` path system plus internal cycles;
3. `\kappa(D)=(0,1)`: it is a `{3,4}`-join plus internal cycles;
4. `\kappa(D)=(1,1)`: it is a four-terminal even subgraph whose terminal-path decomposition realizes one of the three pairings
   $$
   12\mid34,
   \qquad
   13\mid24,
   \qquad
   14\mid23,
   $$
   together with internal cycles.

#### Proof

`Z(D)` has even degree at every vertex of `\widehat Q`.  Deleting one selected cap edge toggles the degree parity at precisely its two end-flags.  Deleting both selected caps adds the two corresponding boundary pairs.  The standard decomposition of a binary subgraph with prescribed even-cardinality boundary gives terminal paths plus cycles. ∎

This theorem does not determine which of the three pairings occurs in the `(1,1)` case.  A crossed pairing would contradict route-lock and rootify the atom; the locked pairing remains compatible with the obstruction.

## 8. Coupled and separated completions

Let `C` be an inclusion-minimal full cocycle completion of the two-transition residue.

### Coupled case

If `C` is one cocircuit containing both cap residues, then

$$
Z(C)
$$

is one canonical physical cycle vector carrying the cap word `\kappa(C)`.  The coupled prime branch may therefore be studied through the four physical alternatives in Theorem 7.1.

### Separated case

Suppose

$$
C=D_{12}\sqcup D_{34},
$$

where `D_{12}` and `D_{34}` are disjoint cocircuits with disjoint isotropic vertex supports and carry the two cap residues separately.

### Corollary 8.1 — edge-disjoint physical projections

The physical cycle vectors

$$
Z(D_{12}),
\qquad
Z(D_{34})
$$

are edge-disjoint in `\widehat Q`.

Moreover:

- `Z(D_{12})` cannot contain `z_{34}`;
- `Z(D_{34})` cannot contain `z_{12}`;
- if `z_{12}\in Z(D_{12})`, deleting it gives a `{1,2}`-join;
- if `z_{34}\in Z(D_{34})`, deleting it gives a `{3,4}`-join;
- if the relevant cap is absent, the corresponding projection is an internal even subgraph, possibly empty.

#### Proof

Disjoint vertex supports in the isotropic matroid mean that the two cocircuits meet disjoint transition triples.  Transition triples of `F` are indexed by edges of `\widehat Q`; hence their intersections with the natural transversal use disjoint original edges.

The cocircuit carrying the `12` residue does not meet the cap vertex `q`, and similarly for the other cocircuit.  The terminal-boundary statements follow from Theorem 7.1. ∎

Thus the separated matroid branch already has a choice-free physical form: two edge-disjoint one-ended cycle/join certificates.

## 9. Mechanism consequence

The nonflat obstruction now passes through the exact chain

$$
\boxed{
\begin{array}{c}
\text{common-cut witness}\
\Downarrow\
\text{two-transition cap residue}\
\Downarrow\
\text{coupled cocircuit or two separated cocircuits}\
\Downarrow\
\text{physical cycle/join projection in }\widehat Q.
\end{array}
}
$$

The next composition theorem should use the cap word and the projected physical subgraph.

1. A separated cocircuit with a selected cap gives a one-pair terminal join and should yield a serial interface, a bounded replacement, or a horizontal switch.
2. A coupled cocircuit with cap word `(1,1)` gives a four-terminal routing subgraph.  A crossed route escapes the blocked atom immediately; the locked route is the only residual two-ended case.
3. Cap words `(0,0)`, `(1,0)`, or `(0,1)` produce internal-cycle or one-pair certificates.  Their relation to the cocircuit cut-rank carrier must determine whether they give a split, a flow switch, or a bounded prime obstruction.
4. The prime coupled locked-route case is the only remaining candidate for comparison with the physical DDD support-label class.

This is stronger than an arbitrary circle-graph split projection: the carrier is the line graph of the actual capped cubic four-pole, and the projection is canonical.

## 10. Reliability boundary

Proved here:

- the canonical local-transition transversal;
- its vertex-triangle circuit partition;
- the canonical identification of its touch-graph with `\widehat Q`;
- the cographic restriction `M_\tau(F)|T_{\mathrm{loc}}\cong M^*(\widehat Q)`;
- projection of every full isotropic cocycle to a physical cycle vector;
- exact cap-word and terminal-boundary classification;
- edge-disjoint physical projections in the separated branch.

Not proved here:

- nonemptiness of the natural projection of every nonzero cocircuit;
- that a projected internal cycle gives a valid horizontal escape;
- that a one-pair join gives a composition-safe replacement;
- that a `(1,1)` projection necessarily uses a crossed route;
- projection of cut-rank-one interlacement splits to graph cuts of `Q` or `\Gamma_g`;
- identification of the prime locked-route cocircuit with the DDD support-label cocycle;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, DOI, or merge status is implied.
