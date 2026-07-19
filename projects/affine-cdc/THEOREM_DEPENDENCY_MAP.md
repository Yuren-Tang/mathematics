# AffineCDC theorem dependency map

This map separates the complete Cycle Double Cover spine from the open five-support strengthening.

## 1. Complete CDC spine

$$
\text{bridgeless finite-active-edge multigraph}
\to
\text{cubic binary-flow shell}
\to
\text{rank-three affine compatibility}
\to
\text{even double cover}
\to
\text{collapse transport}
\to
\text{cycle double cover}.
$$

Controlling chapters:

- [`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md);
- [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md);
- [`reduction/outer-shell-and-binary-flow.md`](reduction/outer-shell-and-binary-flow.md);
- [`reduction/even-cover-and-collapse.md`](reduction/even-cover-and-collapse.md).

## 2. Five-support object

$$
\text{five indexed even supports}
\Longleftrightarrow
\text{root-valued }E_5\text{ flow}
\Longleftrightarrow
\text{$K_5$ triangles / matching--four-flow / quadratic-cycle / cographic data}.
$$

Controlling chapter:
[`five-support/root-flow-lifting.md`](five-support/root-flow-lifting.md).

## 3. Fixed-lift architecture

$$
\text{Fano flow}
\to
\text{compatible eight-support lift}
\Longleftrightarrow
\text{cycle-face surface / coloured dual triangulation}
\to
T_g^{(1)}\longrightarrow\mathscr A_5\ ?
$$

The fixed-plane singular quotient, Schur boundary, colour-cut, and stress criteria are complete after the flow and plane are fixed. The factorable route through `J_g` is a strict subclass of the componentwise criterion.

Controlling chapters:

- [`five-support/root-flow-lifting.md`](five-support/root-flow-lifting.md);
- [`five-support/surfaces-and-halfcube.md`](five-support/surfaces-and-halfcube.md).

## 4. Gauge, routing, and defect reduction

$$
\text{gauge torsor / horizontal switches}
\to
\text{three-cut and ten-state four-cut interfaces}
\to
P_5\mid P_5\text{ or }P_4\mid C_3
\to
\text{holonomy / Tait resolution / defect forest / Petersen atoms}.
$$

The soluble Type H branch escapes by Tait colouring. A blocked co-root atom gives the route-locked quotient endpoint.

Controlling chapters:

- [`five-support/gauge-and-reconfiguration.md`](five-support/gauge-and-reconfiguration.md);
- [`five-support/cuts-four-poles-and-routing.md`](five-support/cuts-four-poles-and-routing.md);
- [`five-support/holonomy-defects-and-atoms.md`](five-support/holonomy-defects-and-atoms.md).

## 5. Route-locked dichotomy

For the equal-terminal-colour quotient flow:

$$
\begin{cases}
\operatorname{rank}=2&\Rightarrow\text{Tait escape},\\
\operatorname{rank}=3,\ \Omega=0&\Rightarrow\text{eight-state flat potential},\\
\operatorname{rank}=3,\ \Omega\ne0&\Rightarrow\text{support-minimal common-cut witness}.
\end{cases}
$$

The nonflat witness is a curvature-odd circuit of the closed-component incidence matrix.

## 6. Nonflat circuit localisation

$$
\boxed{
\begin{cases}
|\eta|=1&\Rightarrow\text{aligned/crossed enriched atom},\\
|C\cap\eta|=2&\Rightarrow\text{marked scalar transition pair},\\
|\eta|=4k+1&\Rightarrow\text{quartic near-resolution core}.
\end{cases}}
$$

Controlling chapter:
[`five-support/common-cut-circuit-localisation.md`](five-support/common-cut-circuit-localisation.md).

## 7. Quartic incidence and strict abstract progress

Abstract quartic designs exist for every `k`, so incidence parity alone is unbounded.

Every design nevertheless has a canonical terminal nucleus

$$
S\cong O^-(4,2),
$$

with intrinsic `E_5/K_5` geometry, route stabiliser `D_8`, and curvature carrier

$$
S/s_\infty^\perp\cong\mathbf F_2.
$$

Terminal distribution gives:

- `3`: co-root equality transport;
- `2+1`: one `K_6` one-factor vertex;
- `1+1+1`: one-factor vertex plus root triangle.

Hence

$$
\boxed{
\text{bounded root-exposed split}
\quad\text{or}\quad
\text{canonical nucleus peel }k\mapsto k-1.
}
$$

Controlling chapters:

- [`five-support/quartic-witness-designs.md`](five-support/quartic-witness-designs.md);
- [`five-support/quartic-terminal-nucleus.md`](five-support/quartic-terminal-nucleus.md);
- [`five-support/quartic-terminal-defect-geometry.md`](five-support/quartic-terminal-defect-geometry.md);
- [`five-support/quartic-nucleus-transport.md`](five-support/quartic-nucleus-transport.md).

## 8. Quotient-phase and elementary interval layer

After quotient by `\langle g\rangle`, the flow is a degenerate `\mathbf F_2^2` Tait flow plus one binary phase. The four scalar sheets form an affine plane and differ by the three quotient Kempe cycle systems.

Between consecutive **full** `g`-incidences, an elementary non-`g` scalar path has:

- one of eighteen quotient transfer states;
- telescoping side-output sum;
- a bounded backtrack cap or periodic triangle-cell chain;
- rigid three-rail Kempe wiring.

A witness-to-witness arc may contain additional edges of `E_g\setminus\eta`. It is a transition walk, not necessarily one elementary interval.

Controlling chapters:

- [`five-support/route-locked-quotient-phase.md`](five-support/route-locked-quotient-phase.md);
- [`five-support/scalar-interval-transfer.md`](five-support/scalar-interval-transfer.md);
- [`five-support/scalar-interval-caps-and-cells.md`](five-support/scalar-interval-caps-and-cells.md);
- [`five-support/periodic-kempe-ladders.md`](five-support/periodic-kempe-ladders.md).

## 9. Physical cut carrier

Contract the connected components of `Q-E_g` to obtain an even-total-degree four-pole `\Gamma_g`. The four scalar sheets induce four transition systems.

Scalar components containing `g`-edges are exactly transition circuits/trails. Common-cut localisation therefore lives on `\Gamma_g`.

Every internal quotient cut lifts exactly:

$$
\delta^{\mathrm{int}}_{\Gamma_g}(\mathcal U)
=
\delta^{\mathrm{int}}_Q(X_\mathcal U),
$$

with parity

$$
|\delta^{\mathrm{int}}(\mathcal U)|
\equiv t(\mathcal U)\pmod2.
$$

Controlling chapter:
[`five-support/g-component-transition-quotient.md`](five-support/g-component-transition-quotient.md).

## 10. Canonical `4`-regular carrier

Close the terminals according to `12\mid34` and take the flag-line graph

$$
F=\mathcal L(\widehat Q).
$$

Every scalar even subgraph gives a canonical circuit partition of `F`; the four sheets are four transition transversals of one transition matroid.

Scalar components are distinguished partition circuits, and their incidence with `g`-edges is one-sided touch-graph incidence. The aligned/crossed transition law is uniform on all edges.

Controlling chapter:
[`five-support/route-capped-line-graph-carrier.md`](five-support/route-capped-line-graph-carrier.md).

## 11. Relative touch-homology

For each sheet, let `\Theta_\phi` be the touch subgraph on internal `g`-edges. Interior vertices are closed scalar circuits; boundary vertices are terminal and complementary partition circuits.

The common-cut space is

$$
\mathcal Z_{\mathrm{com}}
=
\bigcap_{\phi\in U^*}Z_1(\Theta_\phi,B_\phi),
$$

and curvature is

$$
\Omega(x)=\sum_\phi\beta_{\phi,34}(x).
$$

Thus the pointed curvature matroid is a coextension of the stacked relative boundary matrix. The witness is not yet proved to be a transverse circuit or cocircuit because complementary touch boundary may remain.

Controlling chapter:
[`five-support/relative-touch-homology.md`](five-support/relative-touch-homology.md).

## 12. Exact open bridge

The primary theorem still needed is

$$
\boxed{
\text{fourfold relative curvature circuit}
\Longrightarrow
\begin{cases}
\text{bounded closure to ordinary touch/transverse dependence},\\
\text{terminal-even separator or transition two-sum in }\Gamma_g,\\
\text{physical }D_8\text{ class}.
\end{cases}}
$$

Equivalently, control the complementary boundary syndromes

$$
b_\phi=\partial_{B,\phi}(\eta).
$$

After this bridge come:

1. singleton and marked-pair composition;
2. flat-potential finite interface;
3. defect-forest pruning;
4. four-pole transfer and gluing;
5. horizontal escape/decomposition;
6. target-certificate completion where required.

## 13. Assurance axes

No arrow in this map automatically transfers Lean status, independent audit, peer review, novelty, release, DOI, arXiv, or publication status. See [`FORMAL_STATUS.md`](FORMAL_STATUS.md).
