# The physical `g`-component transition quotient

## 1. Purpose

The route-locked nonflat analysis is expressed through four scalar circuit partitions on the common set of `g`-edges. A graph-level composition theorem needs an auxiliary object whose separators lift back to the original four-pole.

Delete all `g`-edges and contract each remaining connected component. The `g`-edges become the edges and terminal flags of an even-degree four-pole multigraph. Every scalar sheet induces a perfect-matching transition system at each contracted vertex, and its scalar components containing `g`-edges become exactly the transition circuits of this quotient.

Most importantly, every **internal** edge cut of the quotient lifts verbatim to the corresponding internal `g`-edge cut of the original four-pole. Cut parity must retain the existing terminal flags: an internal cut has the same parity as the number of original terminals on that side.

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
E_g=\{e:c(e)=g\}.
$$

This includes the four terminal semiedges when boundary flags are counted. Internally, `E_g` is a matching on cubic vertices.

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

For every nonzero `\delta\in U^*`, define the quotient Kempe system

$$
K_\delta=\{e:\delta(\bar c(e))=1\}.
$$

Each `K_\delta` is a disjoint union of graph cycles and contains no `g`-edge.

## 3. Kempe closure equals non-`g` connectivity

Let

$$
Q^\circ=Q-E_g
$$

be obtained by deleting internal `g`-edges and removing the terminal `g`-semiedges while retaining their incident vertices.

A **Kempe closure** of a set of non-`g` edges is obtained by repeatedly adjoining every component of every `K_\delta` that meets the current set.

### Theorem 3.1 — Kempe-component equivalence

The Kempe closures in `Q^\circ` are exactly the ordinary connected components of `Q^\circ`.

#### Proof

Every `K_\delta` lies in `Q^\circ`, so Kempe closure cannot leave an ordinary component.

At an ordinary quotient vertex the three incident quotient colours are the three nonzero elements of `U`. For one incident colour `q`, the two nonzero functionals with `\delta(q)=1` pair that edge respectively with each of the other two incident edges. Thus Kempe closure through one edge reaches all three.

At an endpoint of a deleted `g`-edge, the two remaining edges have the same nonzero quotient colour `q`. Each Kempe system containing `q` uses both edges, so closure passes through the vertex.

Therefore Kempe closure propagates across every adjacency of `Q^\circ`. ∎

### Corollary 3.2

All side attachments of one scalar interval lie in one component of `Q^\circ`; their simultaneous three-Kempe closure is precisely that component.

## 4. The `g`-component quotient

Let

$$
\mathcal C_g=\pi_0(Q^\circ).
$$

Define a four-pole multigraph `\Gamma_g` by:

- one vertex for every `R\in\mathcal C_g`;
- one quotient edge for every internal `g`-edge, joining the components containing its endpoints;
- a loop when both endpoints lie in one component;
- one terminal flag for each original terminal `g`-semiedge.

No non-`g` edge joins distinct quotient vertices.

### Theorem 4.1 — even total incidence degree

Every vertex of `\Gamma_g` has even total incidence degree, counting loops twice and terminal flags once.

#### Proof

Fix one scalar sheet `H_\phi` and one component `R`. Every `g`-incidence at `R` belongs to `H_\phi`; after deleting the `g`-edge, exactly one selected non-`g` continuation enters `R` at that endpoint. All other vertices of `H_\phi\cap R` have degree zero or two. Hence the number of degree-one boundary incidences is even. ∎

Thus `\Gamma_g` is an Eulerian four-pole in the sense of even total degree with its four terminal flags included.

## 5. Scalar sheets as transition systems

For one quotient vertex `R` and one sheet `H_\phi`, the restriction `H_\phi\cap R` is a disjoint union of:

- paths whose endpoints are the `g`-incidences at `R`;
- closed cycles containing no `g`-incidence.

The path components pair all incident half-edges and terminal flags.

### Definition 5.1 — scalar transition matching

Let `T_\phi(R)` be the perfect matching on the `g`-incidences at `R` in which two incidences are paired when one path component of `H_\phi\cap R` joins them.

The family

$$
T_\phi=\{T_\phi(R):R\in\mathcal C_g\}
$$

is a transition system on `\Gamma_g`.

### Theorem 5.2 — exact transition-circuit model

After contracting the non-`g` components, the scalar components of `H_\phi` containing `g`-edges are exactly the circuits and terminal trails obtained by following quotient `g`-edges through `T_\phi`.

The two terminal trails route the boundary as

$$
12\mid34.
$$

#### Proof

A scalar component alternates between one `g`-edge or terminal flag and one path inside a non-`g` component. Contraction replaces the latter by its transition pair. Conversely every transition pair lifts to its defining scalar path. ∎

Closed scalar cycles wholly inside one `R` contain no `g`-edge. They affect gauge side choices but not a witness supported on `E_g`.

## 6. Four physically realized transition systems

The four sheets give four transition systems

$$
T_\phi
\qquad(\phi\in U^*).
$$

For two sheets,

$$
H_\phi\triangle H_\psi=K_{\phi+\psi}.
$$

Inside each component `R`, these Kempe cycles realize the change from `T_\phi(R)` to `T_\psi(R)`. Abstractly, the union of the two perfect matchings is a disjoint union of alternating even cycles, with doubled pairs allowed.

### Corollary 6.1

The four transition systems are not arbitrary. Every pairwise change is physically realized inside the corresponding non-`g` component by quotient Kempe cycles.

## 7. Common cuts on the quotient

Let `S\subseteq E_g` contain internal `g`-edges. Closed scalar components with no `g`-edge are disjoint from `S`; all other closed scalar components correspond exactly to closed transition circuits.

### Theorem 7.1 — transition-quotient common-cut criterion

The following are equivalent.

1. `S` is a cut vector in all four scalar sheets.
2. For every `\phi`, `S` meets every closed transition circuit of `(\Gamma_g,T_\phi)` evenly.
3. The characteristic vector of `S` lies in the common kernel of the four transition-circuit incidence matrices.

The odd terminal side bit is the same curvature functional as before.

### Corollary 7.2

The support-minimal nonflat witness `\eta` is a curvature-odd circuit of a physically realized four-transition-system matroid on `\Gamma_g`.

The previous closed-component matrix is the circuit-incidence representation of this transition quotient after rows disjoint from `E_g` are omitted.

## 8. Exact lifting of internal quotient cuts

For `\mathcal U\subseteq V(\Gamma_g)`, put

$$
X_\mathcal U=\bigcup_{R\in\mathcal U}V(R)\subseteq V(Q).
$$

Write `\delta^{\mathrm{int}}` for the cut consisting only of ordinary internal edges; the four pre-existing terminal semiedges are not included.

### Theorem 8.1 — physical cut lifting

$$
\boxed{
\delta^{\mathrm{int}}_{\Gamma_g}(\mathcal U)
=
\delta^{\mathrm{int}}_Q(X_\mathcal U).
}
$$

Every edge in this cut has colour `g`.

#### Proof

No non-`g` edge joins distinct components of `Q^\circ`. An internal edge crosses the vertex partition exactly when it is a `g`-edge whose endpoints lie in quotient components on opposite sides. ∎

### Corollary 8.2 — separator transfer

Every internal two-edge or four-edge separator found in `\Gamma_g` is an actual same-size `g`-coloured separator in `Q`. In particular, a quotient separator avoiding the four terminal flags requires no further scalar-to-physical conversion.

## 9. Correct terminal parity law

For `\mathcal U\subseteq V(\Gamma_g)`, let

$$
t(\mathcal U)
$$

be the number of the four terminal flags incident with vertices of `\mathcal U`.

### Theorem 9.1 — internal-cut parity

$$
\boxed{
|\delta^{\mathrm{int}}_{\Gamma_g}(\mathcal U)|
\equiv
t(\mathcal U)
\pmod2.
}
$$

#### Proof

Summing the even total degrees of vertices in `\mathcal U` gives

$$
0
\equiv
2|E(\mathcal U)|
+|\delta^{\mathrm{int}}(\mathcal U)|
+t(\mathcal U)
\pmod2.
$$

The internal-edge term vanishes modulo two. ∎

### Corollary 9.2

The internal quotient cut is even whenever the chosen shore contains `0`, `2`, or `4` of the original terminals. In particular:

- a terminal-free internal region has even boundary;
- a shore separating the terminals into two pairs has even boundary;
- odd cuts can occur only for a shore containing one or three terminal flags.

Thus the serial two-cut and ten-state four-cut interfaces remain the first natural even separators in the composition regimes relevant here, but evenness is not asserted for arbitrary terminal shores.

## 10. Quartic cores on the transition quotient

For a quartic witness `\eta`, each near-resolution records the closed transition circuits meeting `\eta`, together with one terminal trail containing the omitted witness edge.

The quartic terminal nucleus, split-or-peel recursion, pairwise transition skeletons, and bounded terminal-defect gadgets depend only on these four transition circuit partitions. They therefore live canonically on `\Gamma_g`.

### Corollary 10.1 — physical location of the quartic algebra

The complete quartic incidence theory sits on one Eulerian four-pole multigraph carrying four physically realized transition systems.

The remaining lifting problem separates into:

1. finding an ordinary cut or transition decomposition in `\Gamma_g`;
2. transporting five-support data through the contracted non-`g` components.

Any edge separator obtained in the first step lifts exactly to `Q`.

## 11. Updated proof target

The sharp transition-quotient theorem should prove one of:

1. a root-exposed terminal-defect gadget forces a two-cut, four-cut, or transition split in `\Gamma_g`;
2. a concentrated nucleus shell is a transition-matroid two-sum and peels to the residual quotient instance;
3. a periodic Kempe ladder closes in a proper terminal-even quotient region and exposes an even `g`-separator;
4. crossing Kempe closures create an alternate transition and break route-lock;
5. the only transition-indecomposable remainder is the physical `D_8` class.

The problem is no longer to turn a scalar common cut directly into a cut of `Q`. It is to force an ordinary separator in the physical quotient, where cut lifting is automatic.

## 12. Reliability boundary

Proved here:

- Kempe closure equals connectivity after deleting `g`-edges;
- construction of the even-total-degree `g`-component four-pole `\Gamma_g`;
- perfect-matching transition systems induced by all four scalar sheets;
- exact correspondence between scalar `g`-components and transition circuits;
- transition-quotient formulation of common cuts and quartic witnesses;
- exact lifting of internal quotient cuts to the original four-pole;
- the terminal-sensitive parity formula for those cuts.

Not proved here:

- that the quartic split-or-peel operation already yields a quotient separation;
- a transition-matroid two-sum theorem for the concentrated nucleus;
- five-support transfer through an arbitrary contracted component;
- classification of transition-indecomposable four-system quotients;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, or DOI status is implied.
