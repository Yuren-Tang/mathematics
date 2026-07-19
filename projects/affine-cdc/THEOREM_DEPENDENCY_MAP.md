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

## 2. Five-support object and fixed-lift architecture

$$
\text{five indexed even supports}
\Longleftrightarrow
\text{root-valued }E_5\text{ flow}
\Longleftrightarrow
\text{$K_5$ triangles / matching--four-flow / quadratic-cycle data}.
$$

Above one Fano flow:

$$
\text{compatible eight-support lift}
\Longleftrightarrow
\text{cycle-face surface / coloured dual}
\to
T_g^{(1)}\longrightarrow\mathscr A_5\ ?
$$

The factorable route through `J_g` is a strict subclass.

Controlling chapters:

- [`five-support/root-flow-lifting.md`](five-support/root-flow-lifting.md);
- [`five-support/surfaces-and-halfcube.md`](five-support/surfaces-and-halfcube.md).

## 3. Gauge, routing, and defect reduction

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

## 4. Route-locked dichotomy

For the equal-terminal-colour quotient flow:

$$
\begin{cases}
\operatorname{rank}=2&\Rightarrow\text{Tait escape},\\
\operatorname{rank}=3,\ \Omega=0&\Rightarrow\text{eight-state flat potential},\\
\operatorname{rank}=3,\ \Omega\ne0&\Rightarrow\text{support-minimal common-cut witness}.
\end{cases}
$$

The nonflat witness is a curvature-odd circuit of the closed-component incidence matrix.

## 5. Nonflat localisation

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

## 6. Quartic incidence and strict abstract progress

Abstract designs exist for every `k`, but every design has a canonical terminal nucleus

$$
S\cong O^-(4,2),
\qquad
S/s_\infty^\perp\cong\mathbf F_2.
$$

Terminal distribution gives bounded equality/one-factor/root-triangle coefficient gadgets, or an all-concentrated peel

$$
\boxed{k\longmapsto k-1.}
$$

The natural symmetry is the sheet group `AGL(2,2)\cong S_4`. It is not canonically identified with either the terminal-route stabiliser or the support-label `D_8` of a DDD one-factor.

Controlling chapters:

- [`five-support/quartic-witness-designs.md`](five-support/quartic-witness-designs.md);
- [`five-support/quartic-terminal-nucleus.md`](five-support/quartic-terminal-nucleus.md);
- [`five-support/quartic-terminal-defect-geometry.md`](five-support/quartic-terminal-defect-geometry.md);
- [`five-support/quartic-nucleus-transport.md`](five-support/quartic-nucleus-transport.md).

## 7. Quotient phase and elementary transition paths

After quotient by `\langle g\rangle`, the flow is a degenerate `\mathbf F_2^2` Tait flow plus one binary phase. The four scalar sheets form an affine plane and differ by three quotient Kempe systems.

Between consecutive **full** `g` incidences, an elementary non-`g` path has finite transfer state, telescoping output, and a cap-or-periodic-ladder normal form. A witness arc may contain additional edges of `E_g\setminus\eta`; whole arcs are transition walks rather than one elementary interval.

Controlling chapters:

- [`five-support/route-locked-quotient-phase.md`](five-support/route-locked-quotient-phase.md);
- [`five-support/scalar-interval-transfer.md`](five-support/scalar-interval-transfer.md);
- [`five-support/scalar-interval-caps-and-cells.md`](five-support/scalar-interval-caps-and-cells.md);
- [`five-support/periodic-kempe-ladders.md`](five-support/periodic-kempe-ladders.md).

## 8. Physical cut carrier

Contract the connected components of `Q-E_g` to obtain an even-total-degree four-pole `\Gamma_g`. Scalar sheets become transition systems, and every internal quotient cut lifts exactly:

$$
\delta^{\mathrm{int}}_{\Gamma_g}(\mathcal U)
=
\delta^{\mathrm{int}}_Q(X_\mathcal U),
$$

with terminal-sensitive parity

$$
|\delta^{\mathrm{int}}(\mathcal U)|\equiv t(\mathcal U)\pmod2.
$$

Controlling chapter:
[`five-support/g-component-transition-quotient.md`](five-support/g-component-transition-quotient.md).

## 9. Standard `4`-regular and touch carriers

Close the terminals according to `12\mid34` and take

$$
F=\mathcal L(\widehat Q).
$$

Every scalar even subgraph gives a circuit partition of the same `4`-regular graph.

For each scalar circuit, the line-graph partition contains one distinguished circuit and one shadow circuit. Selected touch edges form a dipole between them. Thus closed-component parity automatically kills complementary touch boundary.

Adding the two route caps closes every scalar common cut to an ordinary touch cycle.

Controlling chapters:

- [`five-support/route-capped-line-graph-carrier.md`](five-support/route-capped-line-graph-carrier.md);
- [`five-support/relative-touch-homology.md`](five-support/relative-touch-homology.md);
- [`five-support/touch-shadows-and-cap-residue.md`](five-support/touch-shadows-and-cap-residue.md).

## 10. Bounded cap residue

Summing the four cap-completed transition-support vectors cancels every internal witness transition and leaves

$$
\boxed{R=\{r_p,r_q\},}
$$

one cross transition at each cap vertex.

Every full IAS cocycle meets a vertex triple in zero or two elements, so `R` is not itself a cocycle. Local loop/parallel/twin/pendant cases are classified exactly.

Controlling chapter:
[`five-support/cap-residue-isotropic-completion.md`](five-support/cap-residue-isotropic-completion.md).

## 11. Minimal full completion

Except for a loop degeneration, a full cocycle containing `R` exists. Choose an inclusion-minimal one `C`. Then

$$
\boxed{
\begin{cases}
C\text{ is one cocircuit containing }r_p,r_q,&\text{coupled},\\
C=D_p\sqcup D_q\text{ with disjoint one-cap cocircuits},&\text{separated}.
\end{cases}}
$$

In the separated case the two isotropic vertex supports are disjoint.

Controlling chapter:
[`five-support/minimal-cap-cocycle-decomposition.md`](five-support/minimal-cap-cocycle-decomposition.md).

## 12. Cocircuit cut-rank mechanism

For an IAS cocircuit `D`, let `L(D)` be the set of active vertex triples. Then

$$
\operatorname{span}D=\operatorname{span}\tau(L(D)),
$$

and

$$
\boxed{
 r(D)=|L(D)|+\rho_G(L(D)),
 \qquad
 n(D)=|L(D)|-\rho_G(L(D)).
}
$$

For a cocircuit,

$$
\boxed{
\lambda_M(D)=|L(D)|+\rho_G(L(D))-1.
}
$$

Hence:

- `\rho=0`: interlacement disconnection;
- `\rho=1`: Cunningham split, when both shores are nontrivial;
- `\rho\ge2`: prime-side carrier.

Only a **coupled prime cocircuit** can remain an irreducible two-ended candidate. In the separated branch, each one-cap cocircuit has its own cut-rank, and low rank already exposes a split.

Controlling chapter:
[`five-support/cocircuit-cutrank-mechanism.md`](five-support/cocircuit-cutrank-mechanism.md).

## 13. Exact open bridge

The primary theorem still needed is

$$
\boxed{
\text{coupled/separated cap cocircuit}
\Longrightarrow
\begin{cases}
\text{terminal-even separator or serial composition in }\Gamma_g,\\
\text{alternate route and root escape},\\
\text{or graph-level comparison with the DDD class.}
\end{cases}}
$$

The recommended order is:

1. project low cut-rank cocircuits through the line graph to `Q` and `\Gamma_g`;
2. eliminate two disjoint prime one-cap carriers in the separated branch;
3. analyse the prime coupled cap cocircuit;
4. only there construct the comparison with the DDD support-label cocycle;
5. then return to the flat potential, defect-forest pruning, four-pole transfer, and horizontal escape/decomposition.

Controlling frontier chapter:
[`five-support/frontier-localisation.md`](five-support/frontier-localisation.md).

## 14. Assurance axes

No arrow in this map automatically transfers Lean status, independent audit, peer review, novelty, release, DOI, arXiv, or publication status. See [`FORMAL_STATUS.md`](FORMAL_STATUS.md).
