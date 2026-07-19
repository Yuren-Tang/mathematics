# Five-support strengthening

This directory is the active reconstructed corpus for the AffineCDC five-support programme. It replaces discovery chronology with natural mathematical dependency.

The exact public source checkpoint is

`research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`.

Its seventy-eight `research/FIVE_CDC_*.md` packets are retired from the current tip after successor mapping. They remain recoverable through Git history; see [`../CHAPTER_PROVENANCE.md`](../CHAPTER_PROVENANCE.md), [`../RETIRED_SOURCE_CLASSIFICATION.md`](../RETIRED_SOURCE_CLASSIFICATION.md), and [`../SOURCE_RECOVERY_AUDIT.md`](../SOURCE_RECOVERY_AUDIT.md).

## Reading order

1. [`root-flow-lifting.md`](root-flow-lifting.md)  
   Root-valued `E_5` flows, global equivalences, universal eight-support lifts, and fixed-plane obstruction theory.

2. [`surfaces-and-halfcube.md`](surfaces-and-halfcube.md)  
   Cycle-face surfaces, full dual triangulations, componentwise half-cube criterion, target links, and marked obstruction arrangements.

3. [`gauge-and-reconfiguration.md`](gauge-and-reconfiguration.md)  
   Gauge torsors, partial Petrials, support pivots, connected-cycle flow motion, switch laws, and two-level dynamics.

4. [`cuts-four-poles-and-routing.md`](cuts-four-poles-and-routing.md)  
   Three-cut gluing, ten-state four-edge interface, cap forcing, Kempe pairing, routing weights, and Type T/Type H reduction.

5. [`holonomy-defects-and-atoms.md`](holonomy-defects-and-atoms.md)  
   Interior affine holonomy, Tait resolution, BBD common origin, defect forests, Petersen transport, route-locked atoms, curvature, and flat potentials.

6. [`common-cut-circuit-localisation.md`](common-cut-circuit-localisation.md)  
   Scalar-component incidence, odd witness circuits, the physical-cut counterexample, and the singleton/transition/quartic-core localisation theorem.

7. [`quartic-witness-designs.md`](quartic-witness-designs.md)  
   Unbounded abstract quartic cores, an explicit design for every size `4k+1`, and the symplectic cross-intersection formulation.

8. [`route-locked-quotient-phase.md`](route-locked-quotient-phase.md)  
   Quotient Tait flow, binary phase, affine scalar-sheet plane, Kempe cycle differences, and aligned/crossed endpoint switch signatures.

9. [`quartic-transition-skeletons.md`](quartic-transition-skeletons.md)  
   Connected pairwise sheet-incidence graphs, terminal Euler trails, exact cycle rank, and the marked ribbon transition skeleton.

10. [`quartic-terminal-nucleus.md`](quartic-terminal-nucleus.md)  
    The canonical `O^-(4,2)` terminal nucleus, its intrinsic `E_5/K_5` geometry and `D_8` route stabiliser, the curvature carrier, block projections, and the split-or-peel recursion.

11. [`quartic-terminal-defect-geometry.md`](quartic-terminal-defect-geometry.md)  
    Projected sheet conservation and the exact identification of terminal distributions `3`, `2+1`, and `1+1+1` with an equality wire, one `K_6` one-factor vertex, or a one-factor vertex followed by a root triangle.

12. [`quartic-nucleus-transport.md`](quartic-nucleus-transport.md)  
    Canonical isometry between successive nuclei, diagonal singular gluing, curvature transport, and the exact two-vertex marked shell contributed by each concentrated peel.

13. [`scalar-interval-transfer.md`](scalar-interval-transfer.md)  
    Elementary `g`-to-`g` scalar intervals, telescoping side output, eighteen quotient transfer states, and algebraic backtrack reduction.

14. [`scalar-interval-caps-and-cells.md`](scalar-interval-caps-and-cells.md)  
    Physical backtrack caps with exact four-sheet routing and periodic three-turn triangle cells for elementary intervals.

15. [`periodic-kempe-ladders.md`](periodic-kempe-ladders.md)  
    Exact three-Kempe wiring inside periodic elementary intervals and the rigid three-rail ladder normal form.

16. [`g-component-transition-quotient.md`](g-component-transition-quotient.md)  
    The physical Eulerian quotient obtained by contracting `Q-E_g`, its four transition systems, common-cut formulation, exact cut lifting, and terminal-sensitive cut parity.

17. [`route-capped-line-graph-carrier.md`](route-capped-line-graph-carrier.md)  
    The canonical route-capped `4`-regular flag-line graph, four scalar circuit partitions, unified aligned/crossed transition law, and one-sided touch incidence.

18. [`relative-touch-homology.md`](relative-touch-homology.md)  
    The common-cut kernel as a fourfold relative touch-cycle space, curvature as terminal relative-boundary evaluation, and the exact obstruction to direct isotropic connectivity.

19. [`frontier-localisation.md`](frontier-localisation.md)  
    Exact remaining localisation/composition frontier and recommended proof order.

20. [`equivalent-formulations-and-proof-families.md`](equivalent-formulations-and-proof-families.md)  
    Preferred and independent proof families, exact equivalences, sufficient templates, and negative boundaries.

21. [`finite-laboratories-and-certificates.md`](finite-laboratories-and-certificates.md)  
    Exact finite computations, counterexamples, certificates, and their evidentiary scope.

## Scope

The five-support programme strengthens, but does not replace, the complete paper-level Cycle Double Cover spine in the parent project. No global five-support theorem is claimed.

The controlling fixed-lift criterion is

$$
T_g^{(1)}\longrightarrow\mathscr A_5,
$$

not merely the global-colour quotient criterion `J_g -> A_5`.

The sharp nonflat frontier has three coordinated carriers.

1. **Incidence carrier.**  Every quartic design has a canonical minus-type terminal nucleus. A split sheet projects to a bounded `K_6` defect gadget with at most two cubic vertices; an all-concentrated design peels to a smaller quartic design through one canonical `D_8` nucleus layer.
2. **Physical cut carrier.**  Contracting the connected components of `Q-E_g` gives an Eulerian four-pole `\Gamma_g` with four physically realized transition systems. Every internal quotient cut lifts exactly to a `g`-coloured cut in `Q`, with parity determined by the number of original terminal flags on the shore.
3. **Standard `4`-regular carrier.**  Closing the terminals according to `12\mid34` and taking the flag-line graph gives one canonical `4`-regular graph carrying all four scalar circuit partitions. The common-cut witness is presently a fourfold relative touch cycle, not yet a proved transition-matroid circuit.

The elementary non-`g` pieces between consecutive full `g`-incidences have finite flow algebra: eighteen transfer states, bounded backtrack caps, or rigid periodic Kempe ladders. A witness-to-witness arc may nevertheless contain arbitrarily many additional edges of `E_g\setminus\eta`; it is a transition walk in `\Gamma_g`, not one elementary interval.

The central missing theorem is now a **relative-boundary closure/decomposition theorem**: close the complementary touch boundary by bounded data and obtain a transverse dependence, or force a terminal-even separator/transition two-sum in `\Gamma_g`, with the irreducible alternative identified as the physical `D_8` class.

The flat-potential, defect-forest, four-pole, and horizontal bad-flow transfer problems remain open.

## Reliability

The chapters synthesize theorem-level public arguments, exact finite results, independent proof families, corrections, counterexamples, and open boundaries. Inclusion here does not create Lean, independent-review, peer review, publication, release, arXiv, or DOI status. See [`../FORMAL_STATUS.md`](../FORMAL_STATUS.md).
