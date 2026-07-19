# Touch shadows, bounded cap closure, and the nonflat cap residue

## 1. Purpose

The route-capped line-graph carrier initially presents a common-cut witness as a relative cycle in each scalar touch-graph.  Boundary is known to vanish at closed scalar-circuit vertices, but it appeared that uncontrolled boundary might remain at complementary partition circuits.

For circuit partitions coming from even subgraphs of cubic graphs, this apparent freedom is absent.

Every circuit of the even subgraph has exactly one complementary **shadow circuit** in the line-graph partition.  Every selected edge on that scalar circuit gives a touch edge joining the distinguished circuit to its shadow.  Hence the selected-edge part of the touch-graph is a disjoint union of dipoles.

Consequently:

1. parity at a distinguished scalar circuit automatically equals parity at its shadow;
2. the common-cut equations already close all closed-component touch boundary;
3. terminal boundary is closed by adding at most the two fixed route-cap edges;
4. every nonflat witness produces four ordinary touch cycles;
5. the mod-two sum of their transition supports cancels on every internal witness edge and leaves one cross transition at each of the two cap vertices.

Thus the fourfold relative-boundary problem collapses to one bounded two-transition **cap residue**.

## 2. Even-subgraph circuit partitions

Let `G` be a finite cubic multigraph and let

$$
H\subseteq E(G)
$$

be an even subgraph.  At every vertex of `G`, the `H`-degree is `0` or `2`.

Let

$$
F=\mathcal L(G)
$$

be the flag-line graph, and let

$$
P(H)
$$

be the canonical circuit partition defined as follows.

- If `e\notin H`, use the local transition at the line vertex `v_e`.
- If `e\in H`, use the cross transition whose first pair joins the two selected `H`-continuations and whose second pair joins the two remaining line half-edges.

For every circuit component `C` of `H`, denote by

$$
D_C
$$

the distinguished circuit of `P(H)` that follows the selected `H`-corners.

## 3. The shadow-circuit theorem

At a vertex `x` of a circuit `C`, let the two incident `C`-edges be `e,f`, and let `d_x` be the third incident edge of `G`.

The distinguished circuit uses the line edge joining `e` and `f` at `x`.  The other two line edges at `x`, joining `d_x` to `e` and `f`, form the local shadow track.

### Theorem 3.1 — exact circuit decomposition

The circuit partition `P(H)` consists exactly of:

1. one distinguished circuit `D_C` for every circuit component `C` of `H`;
2. one shadow circuit `S_C` for every circuit component `C` of `H`;
3. one line-graph triangle `A_x` for every isolated vertex `x` of `H`.

These circuits are pairwise edge-disjoint and exhaust `E(F)`.

#### Proof

Fix one component `C` of `H`.

At each vertex `x\in V(C)`, the line edge joining the two `C`-edges is used by the distinguished track.  At a selected edge `e=xy\in C`, the first pair of the cross transition at `v_e` joins the distinguished corners at `x` and `y`.  These pieces concatenate exactly around `C`, giving `D_C`.

The two remaining line edges at `x` meet at the line vertex `v_{d_x}`.  Because `d_x\notin H`, the local transition at `v_{d_x}` pairs these two half-edges at the same endpoint `x`; it does not cross to the other endpoint of `d_x`.  At a selected edge `e=xy`, the second pair of the cross transition at `v_e` joins the shadow half-edge at `x` to the shadow half-edge at `y`.  Hence the shadow pieces concatenate exactly once around the same component `C`, giving one circuit `S_C`.

If `x` is isolated in `H`, all three incident edges are unselected.  The three local transition pairs at their line vertices concatenate the three line edges of the triangle determined by the three flags at `x`, giving `A_x`.

At a vertex of `H`-degree two, its three line edges split into one distinguished corner and two shadow corners.  At a vertex of `H`-degree zero, all three belong to `A_x`.  Therefore all line edges are used exactly once.  ∎

### Corollary 3.2 — selected touch dipoles

Let `\operatorname{Tch}(P(H))` be the touch-graph.  For every selected edge `e\in C\subseteq H`, the touch edge labelled `e` joins

$$
D_C
\quad\text{to}\quad
S_C.
$$

Hence the touch subgraph on selected edges is the disjoint union

$$
\boxed{
\operatorname{Tch}(P(H))[H]
=
\bigsqcup_{C\in\pi_0(H)}
\text{Dipole}(D_C,S_C;E(C)).
}
$$

where the dipole has one parallel touch edge for every edge of `C`.

In particular, no selected touch edge is incident with an uncontrolled complementary circuit.

## 4. Ordinary touch cycles are componentwise even sets

For `x\subseteq H`, regard `x` as a `1`-chain in the selected touch subgraph.

### Corollary 4.1 — exact touch-cycle criterion

The following are equivalent.

1. `x` is an ordinary cycle of `\operatorname{Tch}(P(H))[H]`.
2. For every circuit component `C` of `H`,
   $$
   |x\cap C|\equiv0\pmod2.
   $$
3. The touch boundary of `x` vanishes at both `D_C` and `S_C` for every `C`.

#### Proof

In the dipole for `C`, both vertices have degree `|x\cap C|` in the selected chain.  ∎

Thus distinguished and shadow boundary are identical.  There is no separate complementary-boundary syndrome.

## 5. Route-capped scalar sheets

Return to the route-locked four-pole `Q`.  Close terminal pairs `12` and `34` with cap edges

$$
z_{12},z_{34}
$$

of colour `g`, obtaining the cubic graph `\widehat Q`.

For one scalar sheet `H_\phi`, let

$$
\widehat H_\phi
$$

be its closure.  Its circuit components are:

- the closed scalar components `C\in\mathcal Z_\phi`;
- the circuit
  $$
  C^{12}_\phi=P^{12}_\phi\cup\{z_{12}\};
  $$
- the circuit
  $$
  C^{34}_\phi=P^{34}_\phi\cup\{z_{34}\}.
  $$

For `x\subseteq E_g^{\mathrm{int}}`, define terminal parities

$$
\beta_{\phi,12}(x)
=
|x\cap P^{12}_\phi|,
$$

and

$$
\beta_{\phi,34}(x)
=
|x\cap P^{34}_\phi|
$$

in `\mathbf F_2`.

Define the cap-completed chain

$$
\boxed{
\widehat x_\phi
=
x
+
\beta_{\phi,12}(x)z_{12}
+
\beta_{\phi,34}(x)z_{34}.
}
$$

### Theorem 5.1 — bounded touch closure

If `x` is a cut vector in the scalar sheet `H_\phi`, then `\widehat x_\phi` is an ordinary touch cycle in

$$
\operatorname{Tch}(P(\widehat H_\phi))[\widehat H_\phi].
$$

Conversely, the restriction to internal `g`-edges of any cap-completed touch cycle satisfies the scalar sheet-cut equations.

#### Proof

The scalar cut criterion says that `x` meets every closed scalar component evenly.  The cap coefficient on `z_{12}` makes the total intersection with `C^{12}_\phi` even, and similarly for `C^{34}_\phi`.  Corollary 4.1 then gives an ordinary touch cycle.  The converse is immediate by restriction to closed components.  ∎

### Corollary 5.2 — four ordinary touch cycles

For every common-cut witness `\eta`, the four chains

$$
\widehat\eta_\phi
=
\eta
+
\beta_{\phi,12}(\eta)z_{12}
+
\beta_{\phi,34}(\eta)z_{34}
$$

are ordinary touch cycles, one in each scalar partition touch-graph.

Under the cographic identification

$$
M_\tau(F)|\tau(P_\phi)
\cong
M^*(\operatorname{Tch}(P_\phi)),
$$

each cap-completed transition support is a cocycle vector of the corresponding transverse restriction.  It need not be a cocircuit.

## 6. Terminal parity identities

For every sheet,

$$
\beta_{\phi,12}(x)
+
\beta_{\phi,34}(x)
=
|x|\pmod2,
$$

because all closed-component intersections are even.

Summing over the four sheets gives

$$
\sum_\phi\beta_{\phi,12}(x)
=
\sum_\phi\beta_{\phi,34}(x).
$$

For a common-cut witness, the common value is the curvature:

$$
\boxed{
\sum_\phi\beta_{\phi,12}(x)
=
\sum_\phi\beta_{\phi,34}(x)
=
\Omega(x).
}
$$

Thus a nonflat witness uses each cap edge in an odd number of the four cap completions.

## 7. Transition-support cancellation on internal `g`-edges

Let

$$
F=\mathcal L(\widehat Q).
$$

For a sheet `\phi` and an edge `e\in\widehat H_\phi`, write

$$
\tau_\phi(e)
$$

for the chosen transition of the scalar partition at the line vertex `v_e`.

For one cap-completed chain define its transition-support vector

$$
\chi_\phi(x)
=
\sum_{e\in\widehat x_\phi}
[\tau_\phi(e)]
$$

in the free binary vector space on all transitions of `F`.

### Lemma 7.1 — four-sheet cancellation at a `g`-edge

For every internal edge `e\in E_g`,

$$
\boxed{
\sum_{\phi\in U^*}
[\tau_\phi(e)]
=0.
}
$$

#### Proof

If `e` is aligned, all four sheets use the same cross transition, which occurs four times.  If `e` is crossed, two sheets use each of the two cross transitions.  In both cases the binary sum is zero.  ∎

## 8. The cap-residue theorem

Define the fourfold transition residue

$$
\rho(x)
=
\sum_{\phi\in U^*}\chi_\phi(x).
$$

By Lemma 7.1, all contributions from internal edges of `x` cancel.  Therefore

$$
\rho(x)
=
\rho_{12}(x)+\rho_{34}(x),
$$

where

$$
\rho_{rs}(x)
=
\sum_\phi
\beta_{\phi,rs}(x)
[\tau_\phi(z_{rs})].
$$

At one cap edge, only the two cross transitions can occur.

### Theorem 8.1 — nonflat cap residue

If `\Omega(x)=1`, then for each `rs\in\{12,34\}` the vector `\rho_{rs}(x)` is exactly one of the two cross-transition basis elements at `v_{z_{rs}}`.

Consequently

$$
\boxed{
\rho(x)
=
[r_{12}]+[r_{34}],
}
$$

where `r_{12}` and `r_{34}` are uniquely determined cross transitions at the two cap vertices.

#### Proof

The total coefficient of the two cross transitions at `v_{z_{rs}}` is

$$
\sum_\phi\beta_{\phi,rs}(x)
=
\Omega(x)
=1.
$$

A binary vector supported on two basis elements and of odd total weight has weight one.  The two cap vertices are distinct, so the total residue has exactly two elements.  ∎

### Corollary 8.2 — bounded nonflat carrier

Every nonflat common-cut witness, regardless of its size, determines a canonical two-transition residue supported entirely on the two fixed route-cap vertices.

All unbounded internal witness support cancels in the four-sheet transition sum.

## 9. Relation to the terminal nucleus and `D_8`

For a quartic witness, each sheet uses exactly one of the two cap edges in its completion.  The four cap-choice bits are the odd terminal side word carried by the canonical nucleus

$$
S/s_\infty^\perp.
$$

Theorem 8.1 refines this one-dimensional coefficient class to a concrete line-graph object:

$$
\boxed{
\text{odd curvature class}
\longmapsto
\text{one cross transition at each route-cap vertex}.
}
$$

The route stabiliser `D_8` preserves the two cap vertices and their cross-transition pairs.  Hence the cap residue is a bounded `D_8`-equivariant carrier of curvature.

The remaining task is to compare its `D_8` orbit with the physical DDD cocycle and to determine whether the two-transition residue is a transition-matroid separation, a transverse cocircuit after bounded extension, or the irreducible DDD class.

## 10. Updated frontier

The complementary touch-boundary problem is closed.  The primary transition-matroid problem is now:

1. classify the four possible two-transition cap residues under route-preserving symmetries;
2. determine which residues extend to a transverse cocircuit or low-order separation of `M_\tau(F)`;
3. project such a separation to a terminal-even cut or transition two-sum in `\Gamma_g`;
4. identify the unique nonseparating residue, if any, with the physical `D_8` class.

The large witness `\eta` remains relevant through the four cap-completed cocycle vectors, but its total four-sheet residue is bounded.

## 11. Reliability boundary

Proved here:

- exact distinguished/shadow decomposition of the line-graph partition of a cubic even subgraph;
- selected touch subgraph as a disjoint union of dipoles;
- automatic equality of distinguished and shadow boundary;
- bounded closure of every scalar common cut by the two fixed route caps;
- four ordinary touch cycles for every common-cut witness;
- cancellation of all internal witness transitions across the four sheets;
- the canonical two-transition cap residue for every nonflat witness.

Not proved here:

- that a cap-completed cocycle vector is a cocircuit;
- that the two-transition residue is itself a circuit or cocircuit of the full transition matroid;
- a low-order split or separator forced by the residue;
- identification with the physical DDD cocycle;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, DOI, or merge status is implied.
