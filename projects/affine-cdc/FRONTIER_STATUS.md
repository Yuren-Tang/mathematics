# AffineCDC frontier status

This file records the exact theorem boundary on the active corpus. It is not an assurance upgrade.

## 1. Closed route-locked layers

Within their stated scopes, the active line now closes:

- full-rank curvature/common-cut duality and flat-potential equivalence;
- support-minimal odd-circuit localisation;
- singleton/transition/quartic trichotomy;
- unbounded abstract quartic designs and their symplectic form;
- quotient Tait-phase representation and affine sheet/Kempe relations;
- connected pairwise marked transition skeletons;
- canonical `O^-(4,2)` terminal nucleus, intrinsic `E_5/K_5`, route `D_8`, and curvature carrier;
- exact split-or-peel recursion;
- bounded `K_6` defect geometry of split terminal distributions;
- canonical nucleus transport and pairwise marked shell;
- elementary scalar-interval transfer, backtrack caps, periodic cells, and rigid Kempe ladders;
- physical `g`-component transition quotient `\Gamma_g` and exact internal-cut lifting;
- canonical route-capped `4`-regular line-graph carrier;
- fourfold relative touch-homology formulation.

The global five-support theorem remains open.

## 2. Nonflat localisation

For the locked full-rank nonflat flow, choose a support-minimal witness

$$
\eta\subseteq E_g.
$$

It is a curvature-odd circuit of the closed-component incidence matroid and has exactly one form:

1. singleton enriched atom;
2. a closed scalar component meets `\eta` in two edges;
3. quartic core `|\eta|=4k+1`.

A scalar-common cut need not be a cut in the original four-pole. The exact full-rank singleton certificate proves this.

## 3. Quartic incidence progress

Every quartic design contains a canonical nondegenerate minus-type four-space

$$
S=\langle1_X+e_0,\ldots,1_X+e_3\rangle.
$$

Its five singular points and ten roots form intrinsic `E_5/K_5` geometry. The route matching gives `D_8`, and curvature is carried by

$$
S/s_\infty^\perp\cong\mathbf F_2.
$$

Terminal distribution yields:

- `3`: co-root equality transport;
- `2+1`: one `K_6` perfect-matching vertex;
- `1+1+1`: a perfect-matching vertex followed by a root triangle.

Hence every quartic core satisfies

$$
\boxed{
\text{bounded root-exposed split}
\quad\text{or}\quad
\text{canonical nucleus peel }k\mapsto k-1.
}
$$

This is strict incidence progress, not yet physical graph composition.

## 4. Scope correction for scalar intervals

A scalar circuit block may contain additional `g`-edges outside `\eta`. Therefore its four marked witness edges determine four witness arcs, not necessarily four non-`g` intervals.

An elementary scalar interval lies between consecutive full `g`-incidences. Such an interval has:

- one of eighteen quotient transfer states;
- telescoping side-output sum;
- either a bounded backtrack cap or a periodic triangle-cell chain;
- rigid three-Kempe ladder wiring in the periodic case.

A witness arc may concatenate arbitrarily many elementary intervals separated by edges of `E_g\setminus\eta`.

## 5. Physical cut carrier: `\Gamma_g`

Delete all `g`-edges and contract each remaining connected component. The quotient `\Gamma_g` is an even-total-degree four-pole whose edges are the `g`-edges and whose four scalar sheets give four transition systems.

Every internal quotient cut lifts exactly:

$$
\delta^{\mathrm{int}}_{\Gamma_g}(\mathcal U)
=
\delta^{\mathrm{int}}_Q(X_\mathcal U).
$$

The correct parity law is

$$
|\delta^{\mathrm{int}}(\mathcal U)|
\equiv t(\mathcal U)\pmod2,
$$

where `t(\mathcal U)` counts original terminal flags on the shore. Thus terminal-free and two-terminal shores have even internal boundary.

The quartic incidence partitions live canonically on this physical transition quotient.

## 6. Standard `4`-regular carrier

Close the terminals according to the locked route `12\mid34` and take the flag-line graph

$$
F=\mathcal L(\widehat Q).
$$

Every scalar even subgraph gives a canonical circuit partition of this common `4`-regular graph. The four sheets are four transition transversals of one transition matroid.

At every edge of `\widehat Q`, the four transition choices are governed by one uniform local law:

- non-`g` aligned: `2+2+0`;
- non-`g` crossed: `2+1+1`;
- `g` aligned: all four use one cross transition;
- `g` crossed: two use each cross transition.

Scalar component incidence is one-sided incidence in the partition touch-graphs.

## 7. Relative touch-homology frontier

For each sheet, restrict its touch-graph to internal `g`-edges. Interior vertices are closed scalar circuits; boundary vertices are terminal scalar circuits and complementary partition circuits.

The common-cut space is the fourfold relative cycle space

$$
\mathcal Z_{\mathrm{com}}
=
\bigcap_{\phi\in U^*}
Z_1(\Theta_\phi,B_\phi).
$$

Curvature is terminal relative-boundary evaluation:

$$
\Omega(x)=\sum_\phi\beta_{\phi,34}(x).
$$

The pointed curvature circuit is therefore a circuit in a coextension of the stacked relative boundary matrix. It is **not yet** proved to be a transverse circuit or cocircuit of `M_\tau(F)`, because boundary may remain on complementary partition circuits.

This is the exact obstruction to directly applying isotropic connectivity or split decomposition.

## 8. Immediate theorem target

The primary frontier is now:

$$
\boxed{
\text{fourfold relative curvature circuit}
\Longrightarrow
\begin{cases}
\text{bounded closure to an ordinary touch cycle / transverse dependence},\\
\text{terminal-even separator or transition two-sum in }\Gamma_g,\\
\text{physical }D_8\text{ class}.
\end{cases}}
$$

Concretely, for the complementary boundary syndrome

$$
b_\phi=\partial_{B,\phi}(\eta),
$$

prove one of:

1. bounded cap/complement paths close every `b_\phi`;
2. its support lies in a proper region yielding a cut in `\Gamma_g`;
3. the relative cycle factors through a low-order touch/transition separation;
4. all four syndromes form one irreducible orbit equal to the physical DDD class.

The terminal part is already finite and carried by the canonical nucleus. Only complementary boundary remains uncontrolled.

## 9. Secondary open lines

After this primary bridge:

- compose singleton and marked two-edge interfaces;
- extract a finite interface from the flat potential;
- prune defect forests;
- complete Type T/Type H four-pole composition;
- prove horizontal escape/decomposition;
- enlarge target certificates only where required.

## 10. Status

No active source proves the global five-support theorem. No Lean, independent-review, peer-review, merge, release, arXiv, DOI, or publication status is implied.
