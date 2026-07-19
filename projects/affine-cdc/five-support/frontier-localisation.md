# The current five-support frontier: relative boundary and composition

## 1. Closed layers

The active corpus now closes, within stated scopes:

- five-support/root-flow equivalences;
- fixed-plane lifting obstruction;
- surface/dual/halfcube formulations;
- gauge and horizontal switch laws;
- three-cut gluing and ten-state four-cut interfaces;
- Type T/Type H reduction and Tait escape from the soluble Type H branch;
- BBD/DDD defect geometry, Petersen transport, unique bad route, and rank-two escape;
- full-rank curvature/common-cut duality and flat-potential equivalence;
- odd witness circuits and singleton/transition/quartic localisation;
- unbounded abstract quartic designs;
- quotient Tait-phase and affine sheet/Kempe structure;
- canonical quartic `O^-(4,2)` nucleus, bounded split gadgets, and exact split-or-peel recursion;
- elementary interval transfers, caps, periodic cells, and Kempe ladders;
- physical `g`-component transition quotient;
- canonical route-capped `4`-regular line-graph carrier;
- fourfold relative touch-homology formulation.

The global five-support theorem remains open.

## 2. Global proof routes

For a bridgeless cubic graph `G`, graph-level success may occur by:

1. **escape:** one Fano flow and one compatible lift satisfy
   $$
   T_g^{(1)}\longrightarrow\mathscr A_5;
   $$
2. **decomposition:** every persistent bad region produces a proper interface across which smaller five-support covers glue.

The sharp current bottleneck is source-side decomposition, not a larger finite obstruction census.

## 3. Route-locked nonflat endpoint

A blocked co-root atom gives a full-rank quotient flow with terminal colour `g` and four scalar sheets routed as `12\mid34`.

For `\Omega(c)\ne0`, choose a support-minimal witness

$$
\eta\subseteq E_g.
$$

It is a curvature-odd circuit of the closed-component incidence matrix and has one of:

1. singleton aligned/crossed atom;
2. marked two-edge scalar transition;
3. quartic core `|\eta|=4k+1`.

The witness need not be a cut in the original four-pole.

## 4. Quartic split-or-peel

The four whole-sheet block sums span a canonical minus-type four-space

$$
S\cong O^-(4,2)
$$

with intrinsic `E_5/K_5`, route stabiliser `D_8`, and curvature carrier

$$
S/s_\infty^\perp\cong\mathbf F_2.
$$

Terminal distribution gives bounded coefficient gadgets:

- `3`: equality transport;
- `2+1`: one-factor vertex;
- `1+1+1`: one-factor vertex plus root triangle.

If all sheets are concentrated, the canonical nucleus peels and leaves a quartic design of level `k-1`. Hence

$$
\boxed{
\text{bounded root-exposed split}
\quad\text{or}\quad
k\mapsto k-1.
}
$$

This is strict incidence progress, not yet graph composition.

## 5. Correct physical path scale

A quartic block has four marked witness arcs, but an arc may contain additional edges of `E_g\setminus\eta`. Only a path between consecutive **full** `g`-incidences is an elementary non-`g` interval.

Elementary intervals have finite algebra:

- eighteen quotient transfer states;
- telescoping side-output sum;
- bounded Tait backtrack cap or periodic triangle-cell chain;
- rigid three-Kempe ladder wiring.

Whole witness arcs are transition walks through the physical quotient described next.

## 6. Physical quotient `\Gamma_g`

Delete all `g`-edges and contract each connected component. The result is an even-total-degree four-pole `\Gamma_g` whose edges are the `g`-edges and whose four scalar sheets induce four perfect-matching transition systems.

Scalar components containing `g`-edges are exactly transition circuits/trails. Common-cut localisation therefore lives on `\Gamma_g`.

Every internal quotient cut lifts exactly:

$$
\delta^{\mathrm{int}}_{\Gamma_g}(\mathcal U)
=
\delta^{\mathrm{int}}_Q(X_\mathcal U).
$$

The parity formula is

$$
|\delta^{\mathrm{int}}(\mathcal U)|
\equiv t(\mathcal U)\pmod2,
$$

where `t(\mathcal U)` counts original terminal flags on the shore.

Thus a terminal-even separator found in `\Gamma_g` is already a physical separator in `Q`.

## 7. Canonical `4`-regular carrier

Close the terminals according to `12\mid34` and take the flag-line graph

$$
F=\mathcal L(\widehat Q).
$$

Every scalar even subgraph gives a canonical circuit partition `P_\phi` of this common `4`-regular graph. The four sheets are four transition transversals of one transition matroid.

Scalar components become distinguished circuits. Their incidence with internal `g`-edges is one-sided incidence in the touch-graph. The local transition distributions are exactly:

- non-`g` aligned: `2+2+0`;
- non-`g` crossed: `2+1+1`;
- `g` aligned: all four sheets use one cross transition;
- `g` crossed: two sheets use each cross transition.

## 8. Relative touch cycles

For each sheet, restrict the touch-graph to internal `g`-edges. Let interior vertices be closed scalar circuits and boundary vertices be terminal scalar circuits together with complementary partition circuits.

Then

$$
\eta\in Z_1(\Theta_\phi,B_\phi)
$$

for every sheet, and

$$
\mathcal Z_{\mathrm{com}}
=
\bigcap_\phi Z_1(\Theta_\phi,B_\phi).
$$

Its terminal relative boundary is

$$
\beta_\phi(\eta)
=
\bigl(|\eta\cap P^{12}_\phi|,
      |\eta\cap P^{34}_\phi|\bigr),
$$

and curvature is

$$
\Omega(\eta)
=
\sum_\phi\beta_{\phi,34}(\eta).
$$

The pointed curvature matroid is the coextension of the stacked relative boundary matrix by this terminal functional.

## 9. Exact obstruction to standard split theory

The witness is closed at all closed scalar-circuit vertices, but may have boundary at:

- terminal scalar circuits;
- complementary partition circuits.

Therefore it is a relative touch cycle, not yet an ordinary touch cycle or a proved transverse circuit/cocircuit of `M_\tau(F)`. Direct use of transition-matroid or isotropic connectivity is premature.

The terminal part is already finite and carried by the canonical nucleus. The uncontrolled data are the complementary boundary syndromes

$$
b_\phi
=
\partial_{B,\phi}(\eta)
\big|_{\text{complementary circuits}}.
$$

## 10. Primary theorem target

Prove

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

Equivalent concrete forms:

1. close each complementary syndrome using bounded cap or complementary touch paths;
2. show its support lies in a proper quotient region and expose a two-cut or four-cut;
3. factor the relative cycle through a low-order touch/transition separation;
4. prove that the only nonclosable four-sheet syndrome is the physical DDD orbit.

## 11. Secondary programmes

After relative-boundary closure:

1. compose singleton and marked-pair interfaces;
2. extract a finite flat-potential interface;
3. prune defect forests;
4. complete Type T/Type H four-pole composition;
5. prove horizontal escape/decomposition;
6. enlarge target certificates only where the source theorem requires it.

Planar Fano-line flattening, orientable good lifts, and coefficient holonomy remain valuable projections but are not the current bottleneck.

## 12. Reliability boundary

No active source proves the global five-support theorem. No Lean, independent-review, peer-review, merge, release, arXiv, DOI, or publication status is implied.
