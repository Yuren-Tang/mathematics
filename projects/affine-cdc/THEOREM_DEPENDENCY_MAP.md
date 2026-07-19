# AffineCDC theorem dependency map

This map separates the complete Cycle Double Cover spine from the open five-support strengthening and records the dependencies among the active chapters.

## 1. Complete CDC existence spine

$$
\boxed{
\begin{array}{c}
\text{bridgeless multigraph with finite active edge set}\\
\downarrow\;\text{delete loops}\\
\text{finite loopless bridgeless core}\\
\downarrow\\
\text{cubic expansion with nowhere-zero }\mathbf F_2^3\text{ flow}\\
\downarrow\\
\text{affine incidence datum }(\mathcal P_f,\kappa)\\
\downarrow\\
\text{rank-three Fano compatibility}\\
\downarrow\\
\text{compatible indexed support family}\\
\downarrow\\
\text{graph-level multiset even double cover}\\
\downarrow\\
\text{cut-even collapse transport}\\
\downarrow\\
\text{one finite circuit decomposition}\\
\downarrow\;\text{reinsert singleton loop circuits}\\
\text{cycle double cover.}
\end{array}}
$$

Controlling chapters:

- [`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md);
- [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md);
- [`reduction/even-cover-and-collapse.md`](reduction/even-cover-and-collapse.md);
- [`reduction/outer-shell-and-binary-flow.md`](reduction/outer-shell-and-binary-flow.md).

This spine is paper-level mathematics with the formal boundaries stated in [`FORMAL_STATUS.md`](FORMAL_STATUS.md).

## 2. Five-support object layer

$$
\boxed{
\begin{array}{c}
\text{indexed five-support even cover}\\
\Updownarrow\\
\text{root-valued }E_5\text{ flow}\\
\Updownarrow\\
\text{$K_5$ triangle labelling}\\
\Updownarrow\\
\text{matching + nowhere-zero }\mathbf F_2^2\text{ flow}\\
\Updownarrow\\
\text{quadratic-cycle / cographic formulation.}
\end{array}}
$$

Controlling chapter:
[`five-support/root-flow-lifting.md`](five-support/root-flow-lifting.md).

## 3. Projection/lifting layer

$$
\begin{array}{c}
\text{nowhere-zero Fano flow }f\\
\downarrow\\
\text{universal compatible eight-support root lift }g\\
\downarrow\;\text{choose plane/slice }W\\
\text{singular quotient and component obstruction}\\
\Updownarrow\\
\text{outside-colour cut parity}\\
\Updownarrow\\
\partial(x*y)=0\\
\Updownarrow\\
\text{vanishing against all relative stresses.}
\end{array}
$$

The fixed-plane theorem is complete after `f` and `W` are fixed. The graph-level five-support statement requires varying the flow, lift, and componentwise surface map.

## 4. Surface/target layer

$$
\begin{array}{c}
\text{compatible root lift }g\\
\Updownarrow\\
\text{coloured cycle-face surface }S_g\\
\Updownarrow\\
\text{coloured dual triangulation }T_g\\
\downarrow\\
T_g^{(1)}\longrightarrow\mathscr A_5\ ?
\end{array}
$$

The colour quotient factors this as

$$
T_g^{(1)}\longrightarrow J_g\longrightarrow\mathscr A_5,
$$

but the factorable route through `J_g` is a strict subclass.

Controlling chapter:
[`five-support/surfaces-and-halfcube.md`](five-support/surfaces-and-halfcube.md).

## 5. Vertical gauge and horizontal flow layers

For one fixed Fano flow:

$$
\text{root-lift torsor}
\longrightarrow
\text{reduced gauge code }B_f
\longrightarrow
\text{marked-core occurrence cosets }A_C.
$$

Across Fano flows:

$$
\operatorname{NZFlow}(G;\mathbf F_2^3)
\xrightarrow{\text{connected-cycle switches}}
\text{new flow, new gauge code, new obstruction arrangement}.
$$

Internal switch directions correct one fixed slice; external directions reslice the quotient.

Controlling chapter:
[`five-support/gauge-and-reconfiguration.md`](five-support/gauge-and-reconfiguration.md).

## 6. Source-interface layer

$$
\begin{array}{c}
\text{persistent obstruction or bad fibre}\\
\downarrow\\
\text{reserve code / harmonic quotient}\\
\downarrow\\
\begin{cases}
\text{cyclic three-cut}&\Rightarrow\text{immediate gluing},\\
\text{cyclic four-cut}&\Rightarrow\text{ten-state shore profiles}.
\end{cases}
\end{array}
$$

For a four-cut:

$$
\text{cap forcing + Kempe closure}
\longrightarrow
\text{deterministic routing}
\longrightarrow
P_5\mid P_5
\quad\text{or}\quad
P_4\mid C_3.
$$

Controlling chapter:
[`five-support/cuts-four-poles-and-routing.md`](five-support/cuts-four-poles-and-routing.md).

## 7. Type H holonomy and defect layer

$$
\begin{array}{c}
\text{rainbow routing loop}\\
\downarrow\\
\text{root-fibre section / Tait-resolution problem}\\
\downarrow\\
\begin{cases}
\text{Tait resolution}&\Rightarrow\text{profile escape},\\
\text{no section}&\Rightarrow\text{local or holonomy certificate}
\end{cases}\\
\downarrow\\
\text{BBD root rigidity and canonical }E_5\text{ defect flow}\\
\downarrow\\
\text{induced defect forest, zero networks, co-root strips}\\
\downarrow\\
L(\mathrm{Petersen})\text{ transport and DDD atoms}.
\end{array}
$$

Controlling chapter:
[`five-support/holonomy-defects-and-atoms.md`](five-support/holonomy-defects-and-atoms.md).

## 8. Route-locked endpoint

A blocked co-root atom gives a locked quotient flow with equal terminal colour `g`:

$$
\begin{array}{c}
\text{locked }\mathbf F_2^3\text{ quotient flow}\\
\downarrow\\
\begin{cases}
\operatorname{rank}=2&\Rightarrow\text{Tait escape},\\
\operatorname{rank}=3,\ \Omega=0&\Rightarrow\text{eight-state affine potential},\\
\operatorname{rank}=3,\ \Omega\ne0&\Rightarrow\text{support-minimal common-cut witness}.
\end{cases}
\end{array}
$$

The nonflat witness is a curvature-odd circuit in the four-partite closed-component incidence matroid.

Controlling chapters:

- [`five-support/holonomy-defects-and-atoms.md`](five-support/holonomy-defects-and-atoms.md);
- [`five-support/common-cut-circuit-localisation.md`](five-support/common-cut-circuit-localisation.md).

## 9. Nonflat circuit localisation

The support-minimal witness satisfies the exact trichotomy

$$
\boxed{
\begin{cases}
|\eta|=1&\Rightarrow\text{aligned or crossed enriched atom},\\
|C\cap\eta|=2&\Rightarrow\text{marked scalar transition interval},\\
|\eta|=4k+1&\Rightarrow\text{quartic near-resolution core}.
\end{cases}}
$$

The quartic incidence axioms alone are unbounded: abstract designs exist for every `k\ge1`. Physical route-lock supplies:

- quotient `\mathbf F_2^2` Tait flow plus one binary phase;
- an affine plane of four scalar sheets;
- three quotient Kempe cycle systems;
- aligned/crossed endpoint labels;
- connected pairwise ribbon transition skeletons.

Controlling chapters:

- [`five-support/common-cut-circuit-localisation.md`](five-support/common-cut-circuit-localisation.md);
- [`five-support/quartic-witness-designs.md`](five-support/quartic-witness-designs.md);
- [`five-support/route-locked-quotient-phase.md`](five-support/route-locked-quotient-phase.md);
- [`five-support/quartic-transition-skeletons.md`](five-support/quartic-transition-skeletons.md).

## 10. Quartic terminal nucleus and strict abstract progress

For one quartic design, the four whole-sheet sums

$$
s_i=1_X+e_i
$$

span a canonical minus-type four-space

$$
S\cong O^-(4,2).
$$

Its five singular points and ten anisotropic roots form the intrinsic `E_5/K_5` geometry. The fixed route matching has coordinate stabiliser `D_8`, and the odd curvature quotient is

$$
S/s_\infty^\perp\cong\mathbf F_2.
$$

Terminal-point distribution gives the strict dichotomy

$$
\boxed{
\text{root-exposed split}
\quad\text{or}\quad
\text{canonical nucleus peel }k\mapsto k-1.
}
$$

More precisely:

- distribution `3` is a co-root equality wire;
- distribution `2+1` is one `K_6` perfect-matching vertex;
- distribution `1+1+1` is one perfect-matching vertex followed by one root triangle;
- if every sheet has distribution `3`, the old nucleus peels and the residual blocks form a level-`k-1` quartic design.

Successive nuclei are canonically `D_8`-equivariantly isometric. Their distinguished blocks form the maximal totally singular diagonal graph of that isometry, and every pairwise transition skeleton grows by one fixed two-vertex shell contributing exactly two cycles.

Controlling chapters:

- [`five-support/quartic-terminal-nucleus.md`](five-support/quartic-terminal-nucleus.md);
- [`five-support/quartic-terminal-defect-geometry.md`](five-support/quartic-terminal-defect-geometry.md);
- [`five-support/quartic-nucleus-transport.md`](five-support/quartic-nucleus-transport.md).

## 11. Scalar interval compression

Each four-witness scalar block is divided into four non-`g` intervals. For a fixed sheet, one interval is a walk on a three-colour triangle.

The exact interval chain is:

$$
\begin{array}{c}
\text{arbitrarily long scalar interval}\\
\downarrow\\
(q_-,q_+,\text{turn parity})\\
\downarrow\\
\text{one of eighteen quotient transfer states},
\end{array}
$$

with telescoping side output

$$
\sum\text{side colours}=x_-+x_+.
$$

Its physical normal form is

$$
\boxed{
\text{two-vertex Tait backtrack cap}
\quad\text{or}\quad
\text{periodic chain of three-turn triangle cells with bounded ends}.
}
$$

Thus interval length produces no new flow state. The sole remaining unbounded datum is the ordered side-attachment semantics of the periodic cells and its simultaneous compatibility across all four sheets.

Controlling chapters:

- [`five-support/scalar-interval-transfer.md`](five-support/scalar-interval-transfer.md);
- [`five-support/scalar-interval-caps-and-cells.md`](five-support/scalar-interval-caps-and-cells.md).

## 12. Open closure dependencies

The current frontier requires the following bridges.

1. **Side-semantic composition**  
   A periodic triangle-cell chain must yield repeated enriched state with matching attachments, a smaller cyclic separator, a transition-matroid split, a bounded four-pole transfer, or the physical `D_8` class.

2. **Bounded atom and interval composition**  
   Aligned/crossed singleton atoms, two-edge scalar intervals, and internal Tait caps must become valid replacements or gluing interfaces.

3. **Physical nucleus descent**  
   The strict abstract decrease `k\mapsto k-1` must preserve the four-sheet ribbon/Kempe/terminal semantics, or its failure must expose a bounded DDD interface.

4. **Flat-potential interface**  
   The eight-state potential must yield finite transfer data, a proper split, or a smaller separator.

5. **Forest pruning and four-pole transfer**  
   Local defect factors must reduce zero/co-root trees and expand the ten-state boundary profile.

6. **Horizontal/global theorem**  
   Every persistent bad-flow component must have a good exit or a coherent decomposition certificate.

Target-library completeness may be developed in parallel but does not remove the need for source composition.

Controlling frontier chapter:
[`five-support/frontier-localisation.md`](five-support/frontier-localisation.md).

## 13. Secondary projections

These depend on a five-support solution but do not control its existence.

- orientable good lift `\Rightarrow` nowhere-zero `\mathbf Z_5` flow;
- Fano line-field flattening `\Rightarrow` Tait colouring in the planar setting;
- coefficient holonomy describes transport of affine `\mathbf F_5` structures;
- tensor/Schur and Fourier/stress complexes provide alternate algebraic projections.

## 14. Assurance axes

No arrow in this map automatically transfers:

- Lean status;
- independent audit;
- peer review;
- novelty or publication status;
- release or DOI status.

Those axes are recorded separately in [`FORMAL_STATUS.md`](FORMAL_STATUS.md).
