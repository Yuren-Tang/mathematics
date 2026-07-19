# The physical `g`-component transition quotient

## 1. Purpose

The route-locked nonflat analysis is expressed through four scalar circuit partitions on the common set of `g`-edges.  Previous localisation chapters compressed individual scalar intervals, but a graph-level composition theorem needs an auxiliary object whose separators lift back to the original four-pole.

This chapter constructs that object.

Delete all `g`-edges and contract each remaining connected component.  The `g`-edges become the edges of an even-degree four-pole multigraph.  Every scalar sheet induces a perfect-matching transition system at each contracted vertex, and its scalar components containing `g`-edges become exactly the transition circuits of this quotient.

Most importantly, every edge cut of the quotient lifts verbatim to an actual `g`-edge cut of the original four-pole.  Thus the common-cut and quartic design theory now sits on a physical transition graph rather than on a bare incidence matrix.

## 2. Route-locked setup

Let

$$
c:E(Q)\longrightarrow V\setminus\{0\},
\qquad
V\cong\mathbf F_2^3,
$$

be a full-rank route-locked flow on a cubic four-pole `Q`, with all four terminal semiedges coloured by one nonzero vector `g`.

Put

$$
E_g
=
\{e:c(e)=g\}.
$$

This includes the four terminal semiedges when boundary flags are being counted.  Internally, `E_g` is a matching on cubic vertices.

Choose

$$
V=\langle g\rangle\oplus U,
\qquad
U\cong\mathbf F_2^2,
$$

and write

$$
c(e)=\sigma(e)g+\bar c(e).
$$

For every nonzero `\delta\in U^*`, the quotient Kempe system is

$$
K_\delta
=
\{e:\delta(\bar c(e))=1\}.
$$

Each `K_\delta` is a disjoint union of graph cycles and contains no `g`-edge.

## 3. Kempe closure equals non-`g` connectivity

Let

$$
Q^\circ
=
Q-E_g
$$

be the graph obtained by deleting internal `g`-edges and removing the four terminal `g`-semiedges while retaining their incident vertices.

A **Kempe closure** of a set of non-`g` edges is obtained by repeatedly adjoining every component of every `K_\delta` that meets the current set.

### Theorem 3.1 — Kempe-component equivalence

The Kempe closures in `Q^\circ` are exactly the ordinary connected components of `Q^\circ`.

#### Proof

Every `K_\delta` lies in `Q^\circ`, so a Kempe closure cannot leave an ordinary connected component.

Conversely, consider one vertex of `Q^\circ`.

- At an ordinary quotient vertex, the three incident quotient colours are the three nonzero elements of `U`.  Fix one incident edge of colour `q`.  The two nonzero functionals satisfying `\delta(q)=1` pair that edge, respectively, with each of the other two incident edges in their two Kempe systems.  Hence Kempe closure through one edge reaches all three incident edges.
- At an endpoint of a deleted `g`-edge, the two remaining incident edges have the same nonzero quotient colour `q`.  Each of the two Kempe systems containing `q` uses both edges, so closure passes through the vertex.

Therefore Kempe closure propagates across every adjacency of `Q^\circ`.  It equals ordinary connectivity.  ∎

### Corollary 3.2

The previously unbounded side attachments of one scalar interval all lie in a single `Q^\circ` component.  Their simultaneous three-Kempe closure is not a new object; it is that component.

## 4. The `g`-component quotient

Let

$$
\mathcal C_g
=
\pi_0(Q^\circ).
$$

Define a four-pole multigraph

$$
\Gamma_g
$$

as follows.

- Its vertices are the components `R\in\mathcal C_g`.
- Every internal edge `e\in E_g` becomes an edge joining the components containing its two endpoints.
- If both endpoints lie in one component, `e` becomes a loop.
- Each terminal `g`-semiedge becomes a terminal flag incident with the component containing its endpoint.

There are no non-`g` edges between distinct quotient vertices by construction.

### Theorem 4.1 — even-degree quotient

Every vertex of `\Gamma_g` has even total incidence degree, counting loops twice and terminal flags once.

#### Proof

Fix one scalar sheet `H_\phi` and one component `R\in\mathcal C_g`.  Every incidence of a `g`-edge at `R` belongs to `H_\phi`.  At its endpoint in `R`, exactly one non-`g` edge of `H_\phi` continues into `R`.

Thus the restriction

$$
H_\phi\cap R
$$

is a graph in which every ordinary internal vertex has degree zero or two, while every `g`-incidence contributes one boundary vertex of degree one after the `g`-edge is deleted.  The number of odd-degree vertices is even.  Therefore the number of `g`-incidences at `R` is even.  ∎

Hence `\Gamma_g` is an Eulerian four-pole multigraph equipped with four terminal flags.

## 5. Scalar sheets as transition systems

Fix a quotient vertex `R\in\mathcal C_g` and a sheet `H_\phi`.  The restriction `H_\phi\cap R` is a disjoint union of:

- paths whose endpoints are `g`-incidences at `R`;
- closed cycles containing no `g`-incidence.

The path components pair all incident half-edges and terminal flags of `\Gamma_g` at `R`.

### Definition 5.1 — scalar transition matching

Let

$$
T_\phi(R)
$$

be the perfect matching on the `g`-incidences at `R` in which two incidences are paired exactly when one path component of `H_\phi\cap R` joins their endpoints.

The family

$$
T_\phi
=
\{T_\phi(R):R\in\mathcal C_g\}
$$

is a transition system on the even-degree four-pole `\Gamma_g`.

### Theorem 5.2 — exact transition-circuit model

After contracting every non-`g` component, the scalar components of `H_\phi` that contain at least one `g`-edge are exactly the circuits and terminal trails obtained by following `g`-edges of `\Gamma_g` through the transition system `T_\phi`.

The two terminal trails route the boundary as

$$
12\mid34.
$$

#### Proof

Traversing a scalar component alternates between:

1. one `g`-edge or terminal flag;
2. one path component of `H_\phi\cap R` inside a non-`g` component.

Contraction replaces the second item by the corresponding transition pair in `T_\phi(R)`.  This is precisely the definition of a circuit partition generated by a transition system.  Conversely, every transition step lifts to its defining scalar path in `R`, so no component is lost.

The terminal routing is the route-lock hypothesis.  ∎

Closed scalar cycles lying entirely inside one `R` contain no `g`-edge and disappear from the quotient.  They affect gauge side conventions but not the common-cut witness on `E_g`.

## 6. Four physical transition systems

The four sheets give four transition systems

$$
T_\phi
\qquad(\phi\in U^*).
$$

For two sheets `\phi,\psi`, their difference is the Kempe cycle system

$$
H_\phi\triangle H_\psi
=
K_{\phi+\psi}.
$$

Inside one component `R`, the Kempe cycles realize the change from `T_\phi(R)` to `T_\psi(R)`.  In particular, the union of the two perfect matchings

$$
T_\phi(R)\cup T_\psi(R)
$$

is a disjoint union of alternating even cycles, with doubled transition pairs allowed.

### Corollary 6.1 — physical realizability of the transition data

The four transition systems on `\Gamma_g` are not arbitrary perfect matchings.  Every pairwise change is physically realized inside the corresponding non-`g` component by a union of quotient Kempe cycles.

This is the contracted form of the affine-sheet/Kempe-cycle theorem.

## 7. Common cuts on the transition quotient

Let `S\subseteq E_g` be a set of internal `g`-edges.  For one sheet, `S` is a cut vector in every scalar component exactly when it meets every closed scalar circuit evenly.

By Theorem 5.2, the closed scalar circuits containing `g`-edges are exactly the closed transition circuits of `(\Gamma_g,T_\phi)`.

### Theorem 7.1 — transition-quotient common-cut criterion

For `S\subseteq E_g`, the following are equivalent.

1. `S` is a cut vector in all four scalar sheets.
2. For every `\phi\in U^*`, `S` meets every closed transition circuit of `(\Gamma_g,T_\phi)` evenly.
3. The characteristic vector of `S` lies in the common kernel of the four transition-circuit incidence matrices of `\Gamma_g`.

The odd terminal side bit is the same one-dimensional curvature functional as before.

#### Proof

Closed scalar components without `g`-edges are disjoint from `S` and contribute zero automatically.  Every remaining closed scalar component corresponds bijectively to a closed transition circuit and has the same set of `g`-edges.  Apply the scalar sheet-cut criterion.  ∎

### Corollary 7.2

The support-minimal nonflat witness `\eta` is a curvature-odd circuit of a physically realized four-transition-system matroid on `\Gamma_g`.

The previous closed-component incidence matrix is therefore the circuit-incidence representation of this transition quotient, after rows disjoint from `E_g` are omitted.

## 8. Exact lifting of quotient cuts

Let

$$
\mathcal U\subseteq V(\Gamma_g)=\mathcal C_g
$$

be a set of quotient vertices, and let

$$
X_\mathcal U
=
\bigcup_{R\in\mathcal U}V(R)
\subseteq V(Q).
$$

### Theorem 8.1 — physical cut lifting

The internal edge cut of `\mathcal U` in the quotient is exactly the edge cut of `X_\mathcal U` in the original four-pole:

$$
\boxed{
\delta_{\Gamma_g}(\mathcal U)
=
\delta_Q(X_\mathcal U).
}
$$

Every edge in this cut has colour `g`.

#### Proof

No non-`g` edge joins distinct components of `Q^\circ`.  Hence an edge of `Q` crosses between `X_\mathcal U` and its complement exactly when it is a `g`-edge whose endpoints lie in quotient components on opposite sides.  These are precisely the quotient edges in `\delta_{\Gamma_g}(\mathcal U)`.  ∎

### Corollary 8.2 — separator transfer

Any two-edge, four-edge, or smaller cyclic separator found in `\Gamma_g` is an actual same-size `g`-coloured separator in `Q`.  No scalar-to-physical cut conversion is required.

This is the principal advantage of the transition quotient over the bare common-cut incidence hypergraph.

## 9. Component boundary parity

### Theorem 9.1 — even `g`-cut parity

For every vertex set `\mathcal U\subseteq V(\Gamma_g)`,

$$
|\delta_{\Gamma_g}(\mathcal U)|
\equiv0\pmod2.
$$

Equivalently, every lifted `g`-coloured cut in `Q` has even size.

#### Proof

The quotient graph has even degree at every vertex.  In any graph,

$$
|\delta(\mathcal U)|
\equiv
\sum_{v\in\mathcal U}\deg(v)
\pmod2.
$$

The right side is zero.  ∎

Thus the first nontrivial physical interfaces exposed by the quotient are naturally two-cuts and four-cuts, exactly the serial and ten-state interfaces already present in the programme.

## 10. Quartic cores on the transition quotient

For a quartic witness `\eta`, each scalar near-resolution records the closed transition circuits of `(\Gamma_g,T_\phi)` that meet `\eta`, together with one terminal trail containing the omitted witness edge.

The quartic terminal nucleus, split-or-peel recursion, pairwise transition skeletons, and bounded terminal-defect gadgets depend only on these four transition circuit partitions.  Therefore they descend unchanged to the physical quotient `\Gamma_g`.

### Corollary 10.1 — physical location of the quartic algebra

The complete quartic incidence theory lives canonically on one Eulerian four-pole multigraph `\Gamma_g` carrying four physically realized transition systems.

The remaining lifting problem has two parts:

1. find a cut or transition decomposition in `\Gamma_g`;
2. lift any required five-support transfer through the contracted non-`g` components.

The first part is now genuine graph theory, and every edge separator obtained there lifts exactly to `Q`.

## 11. Updated proof target

The sharp transition-quotient theorem should prove one of:

1. a root-exposed terminal-defect gadget forces a two-cut, four-cut, or transition-system split in `\Gamma_g`;
2. a concentrated nucleus shell is a transition-matroid two-sum and peels to the residual quotient instance;
3. a periodic Kempe ladder closes inside a proper quotient region, exposing an even `g`-edge separator;
4. crossing Kempe closures create an alternate transition and break route-lock;
5. the only transition-indecomposable remainder is the physical `D_8` class.

This target no longer asks a scalar common cut to become a cut in `Q`.  It asks the four physical transition systems to force an ordinary cut in `\Gamma_g`, where cut lifting is automatic.

## 12. Reliability boundary

Proved here:

- Kempe closure equals connectivity after deleting the `g`-edges;
- construction of the Eulerian `g`-component four-pole `\Gamma_g`;
- perfect-matching transition systems induced by all four scalar sheets;
- exact correspondence between scalar `g`-components and transition circuits;
- transition-quotient formulation of common cuts and quartic witnesses;
- exact lifting of every quotient edge cut to the original four-pole;
- even parity of all quotient cuts.

Not proved here:

- that the quartic split-or-peel operation already yields a quotient vertex or edge separation;
- a transition-matroid two-sum theorem for the concentrated nucleus;
- five-support transfer through an arbitrary contracted non-`g` component;
- classification of transition-indecomposable four-system quotients;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, or DOI status is implied.
