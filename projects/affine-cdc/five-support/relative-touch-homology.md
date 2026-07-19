# Curvature witnesses as fourfold relative touch cycles

## 1. Purpose

The route-capped line-graph carrier places all four scalar sheets inside one standard transition matroid.  It also clarifies an important boundary.

A common-cut witness is not yet known to be a circuit of the transition matroid.  In each scalar touch-graph, it is a **relative cycle**: its boundary vanishes at closed scalar-circuit vertices, but may remain at the two terminal scalar circuits and at complementary partition circuits.

The four common-cut equations are the fiber product of these four relative cycle spaces.  The curvature functional is the total evaluation of the relative boundary on the four `P^{34}` terminal vertices.

This gives the exact bridge still missing before Bouchet--Traldi connectivity theory can be used: either close the relative boundary by bounded cap/complement data, or turn the failure of closure into a separator in the physical `g`-component quotient.

## 2. Route-capped circuit partitions

Let

$$
F=\mathcal L(\widehat Q)
$$

be the route-capped flag-line graph, and let

$$
P_\phi=P(\widehat H_\phi)
$$

be the circuit partition associated with the closed scalar even subgraph.

The distinguished scalar circuits of `P_\phi` are:

- one circuit `C^{12}_\phi` obtained by closing `P^{12}_\phi` with `z_{12}`;
- one circuit `C^{34}_\phi` obtained by closing `P^{34}_\phi` with `z_{34}`;
- one circuit `\widetilde C` for every closed scalar component
  $$
  C\in\mathcal Z_\phi.
  $$

All other circuits of `P_\phi` are called complementary circuits.

Let

$$
\operatorname{Tch}(P_\phi)
$$

be the touch-graph.  Its edges are labelled by edges of `\widehat Q`.

## 3. The `g`-touch subgraph and its boundary

Restrict the touch-graph to the edges labelled by internal `g`-edges:

$$
\Theta_\phi
=
\operatorname{Tch}(P_\phi)[E_g^{\mathrm{int}}].
$$

Every such edge is selected by `\widehat H_\phi`, so it has:

- one endpoint at the distinguished scalar circuit containing it;
- one endpoint at a complementary circuit.

Define the interior and boundary vertex sets

$$
I_\phi
=
\{\widetilde C:C\in\mathcal Z_\phi\},
$$

and

$$
B_\phi
=
V(\Theta_\phi)\setminus I_\phi.
$$

Thus `B_\phi` contains:

- the two terminal scalar circuits `C^{12}_\phi,C^{34}_\phi` when incident with an internal `g`-edge;
- every complementary circuit incident with an internal `g`-edge.

## 4. Relative boundary map

Let

$$
C_1(\Theta_\phi)
=
\mathbf F_2^{E_g^{\mathrm{int}}}.
$$

Forget the boundary coordinates in the ordinary graph boundary map and retain only the interior coordinates:

$$
\partial^{\mathrm{rel}}_\phi:
\mathbf F_2^{E_g^{\mathrm{int}}}
\longrightarrow
\mathbf F_2^{I_\phi}.
$$

For one closed scalar component `C`, the corresponding coordinate is

$$
(\partial^{\mathrm{rel}}_\phi x)_C
=
|x\cap C|\pmod2.
$$

### Theorem 4.1 — common cuts are relative touch cycles

For `x\subseteq E_g^{\mathrm{int}}`, the following are equivalent.

1. `x` is a cut vector in the scalar sheet `H_\phi`.
2. `x` meets every closed scalar component evenly.
3. 
   $$
   \partial^{\mathrm{rel}}_\phi x=0.
   $$
4. `x` is a relative `1`-cycle of the graph pair
   $$
   (\Theta_\phi,B_\phi).
   $$

#### Proof

The first two conditions are the scalar sheet-cut criterion.  By the one-sided touch-incidence theorem, the matrix of `\partial^{\mathrm{rel}}_\phi` is exactly the closed-component incidence block for sheet `\phi`.  The last condition is the definition of a relative graph cycle: its ordinary boundary is allowed to lie in `B_\phi` but must vanish on `I_\phi`.  ∎

Hence the common relative cycle space is

$$
\boxed{
\mathcal Z_{\mathrm{com}}
=
\bigcap_{\phi\in U^*}
\ker\partial^{\mathrm{rel}}_\phi.
}
$$

This is exactly the kernel of the four-partite closed-component matrix.

## 5. Terminal relative boundary

For `x\in\mathcal Z_{\mathrm{com}}`, define

$$
\beta_\phi(x)
=
\left(
|x\cap P^{12}_\phi|,
|x\cap P^{34}_\phi|
\right)
\in\mathbf F_2^2.
$$

These are the coordinates of the ordinary touch boundary of `x` at the two distinguished terminal circuit vertices.

Complementary touch vertices may also carry boundary; `\beta_\phi` records only the terminal part.

### Theorem 5.1 — curvature as relative-boundary evaluation

Under the standard side convention,

$$
\boxed{
\Omega(x)
=
\sum_{\phi\in U^*}
\beta_{\phi,34}(x).
}
$$

Equivalently, curvature evaluates the fourfold relative boundary on the sum of the four `P^{34}` terminal vertices.

#### Proof

The standard curvature representative has coordinate

$$
\omega_e
=
\sum_\phi1_{e\in P^{34}_\phi}.
$$

Therefore

$$
\langle\omega,x\rangle
=
\sum_\phi|x\cap P^{34}_\phi|
=
\sum_\phi\beta_{\phi,34}(x).
$$

Changing the side of a closed scalar circuit adds its interior vertex cocycle.  Every common relative cycle pairs trivially with that cocycle, so the evaluation is gauge-independent.  ∎

### Corollary 5.2 — quartic terminal boundary

For a quartic witness `\eta` of size `4k+1`, every sheet has exactly one terminal witness edge.  Hence

$$
\beta_{\phi,12}(\eta)
+
\beta_{\phi,34}(\eta)
=1
$$

for every `\phi`, and curvature is the parity of the sheets whose unique terminal edge lies on `P^{34}_\phi`.

## 6. Route-cap coordinates

If the two cap edges are admitted as additional relative chains, then:

- `z_{12}` has no interior boundary and toggles the terminal coordinate `C^{12}_\phi`;
- `z_{34}` has no interior boundary and toggles `C^{34}_\phi`.

Thus the route caps provide canonical basis elements for closing the **terminal** part of a relative boundary in each touch-graph.

They do not automatically close boundary at complementary circuit vertices.  Moreover, the required choice between `z_{12}` and `z_{34}` may depend on the sheet.  This is precisely where the odd four-sheet curvature word enters.

## 7. Relation to the pointed curvature matroid

Let

$$
A
=
\bigoplus_\phi\partial^{\mathrm{rel}}_\phi
$$

be the stacked relative boundary matrix, and let

$$
\omega:
\mathcal Z_{\mathrm{com}}
\longrightarrow\mathbf F_2
$$

be the terminal evaluation of Theorem 5.1.

The single-element coextension represented by columns

$$
(A_{\bullet e},\omega_e)
\qquad(e\in E_g^{\mathrm{int}})
$$

and

$$
(0,1)
$$

is exactly the pointed curvature matroid.  A support-minimal nonflat witness is a circuit through the distinguished point.

The route-capped interpretation gives this coextension a canonical relative-homology meaning:

- `A` is the fourfold relative boundary;
- `\omega` is terminal relative-boundary evaluation;
- the distinguished point records the nonzero curvature fiber.

## 8. Why transition-matroid connectivity does not yet apply directly

For a full circuit partition `P_\phi`, standard transition-matroid theory identifies the transverse matroid on its chosen transitions with the cocycle matroid of `\operatorname{Tch}(P_\phi)`.  Equivalently, vertex cocycles of the touch-graph span the relevant kernel.

A vector `x\in\mathcal Z_{\mathrm{com}}` is orthogonal only to the cocycles of the **closed scalar-circuit vertices** in each sheet.  It may have nonzero boundary at:

- terminal scalar circuits;
- complementary partition circuits.

Therefore `x` is a relative cycle, not necessarily an ordinary touch-graph cycle, and the pointed curvature circuit is not yet proved to be a transverse circuit or cocircuit of `M_\tau(F)`.

This is the exact reason that isotropic connectivity and split decomposition cannot simply be quoted at the present frontier.

## 9. The boundary-closure problem

For each sheet, let

$$
\partial_{B,\phi}(x)
\in
\mathbf F_2^{B_\phi}
$$

be the remaining ordinary touch boundary of a common relative cycle.

The next theorem should prove one of:

1. **bounded closure:** add a bounded set of cap edges and complementary touch paths so that `x` becomes an ordinary touch cycle, hence a transverse dependence;
2. **proper boundary region:** the support of `\partial_{B,\phi}(x)` lies in a proper region whose edge boundary gives a separator in `\Gamma_g`;
3. **transition two-sum:** the relative cycle factors through a low-order separation of the touch-graph or transition matroid;
4. **irreducible boundary:** all four relative boundaries form one rigid orbit, canonically identified with the physical `D_8` class.

The terminal part is already finite and carried by the canonical `O^-(4,2)` nucleus.  The only uncontrolled part is boundary on complementary circuits.

## 10. Exact sequence viewpoint

For each sheet there is the relative graph sequence

$$
Z_1(\Theta_\phi)
\subseteq
Z_1(\Theta_\phi,B_\phi)
\xrightarrow{\ \partial_B\ }
\mathbf F_2^{B_\phi},
$$

where:

- `Z_1(\Theta_\phi)` is the ordinary touch-cycle space;
- `Z_1(\Theta_\phi,B_\phi)` is the scalar common-cut space for that sheet;
- `\partial_B` records the terminal and complementary boundary syndrome.

The global nonflat problem is the fiber product of four such sequences together with one odd terminal functional.

This separates the problem into:

1. a closed transition-matroid layer;
2. a finite terminal curvature layer;
3. a complementary-boundary composition layer.

## 11. Reliability boundary

Proved here:

- exact realization of each scalar common-cut space as a relative touch-cycle space;
- fourfold fiber-product description of the common-cut kernel;
- terminal boundary maps and curvature evaluation;
- route-cap interpretation of terminal boundary coordinates;
- relative-homology interpretation of the pointed curvature coextension;
- precise obstruction to direct use of transition/isotropic connectivity.

Not proved here:

- bounded closure of complementary touch boundary;
- transverse-circuit or cocircuit identification;
- a touch-graph split or isotropic separation;
- physical `D_8` comparison;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, or DOI status is implied.
