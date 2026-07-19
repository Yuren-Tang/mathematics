# Five-support strengthening

This directory is the active reconstructed corpus for the AffineCDC five-support programme. It replaces discovery chronology with natural mathematical dependency.

The exact public source checkpoint is

`research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`.

Its seventy-eight `research/FIVE_CDC_*.md` packets are retired from the current tip after successor mapping. They remain recoverable through Git history; see [`../CHAPTER_PROVENANCE.md`](../CHAPTER_PROVENANCE.md), [`../RETIRED_SOURCE_CLASSIFICATION.md`](../RETIRED_SOURCE_CLASSIFICATION.md), and [`../SOURCE_RECOVERY_AUDIT.md`](../SOURCE_RECOVERY_AUDIT.md).

## Reading order

1. [`root-flow-lifting.md`](root-flow-lifting.md) — root-valued `E_5` flows, global equivalences, universal eight-support lifts, and fixed-plane obstruction theory.
2. [`surfaces-and-halfcube.md`](surfaces-and-halfcube.md) — cycle-face surfaces, full dual triangulations, componentwise half-cube criterion, target links, and marked obstruction arrangements.
3. [`gauge-and-reconfiguration.md`](gauge-and-reconfiguration.md) — gauge torsors, partial Petrials, support pivots, connected-cycle flow motion, switch laws, and two-level dynamics.
4. [`cuts-four-poles-and-routing.md`](cuts-four-poles-and-routing.md) — three-cut gluing, ten-state four-edge interface, cap forcing, Kempe pairing, routing weights, and Type T/Type H reduction.
5. [`holonomy-defects-and-atoms.md`](holonomy-defects-and-atoms.md) — affine holonomy, Tait resolution, BBD origin, defect forests, Petersen transport, route-locked atoms, curvature, and flat potentials.
6. [`common-cut-circuit-localisation.md`](common-cut-circuit-localisation.md) — scalar-component incidence, odd witness circuits, the physical-cut counterexample, and singleton/transition/quartic localisation.
7. [`quartic-witness-designs.md`](quartic-witness-designs.md) — unbounded abstract quartic cores and the symplectic cross-intersection formulation.
8. [`route-locked-quotient-phase.md`](route-locked-quotient-phase.md) — quotient Tait flow, binary phase, affine sheet plane, Kempe differences, and aligned/crossed endpoint signatures.
9. [`quartic-transition-skeletons.md`](quartic-transition-skeletons.md) — connected pairwise sheet-incidence graphs, terminal Euler trails, exact cycle rank, and marked ribbon skeletons.
10. [`quartic-terminal-nucleus.md`](quartic-terminal-nucleus.md) — the canonical `O^-(4,2)` terminal nucleus, intrinsic `E_5/K_5`, curvature carrier, block projections, symmetry correction, and split-or-peel recursion.
11. [`quartic-terminal-defect-geometry.md`](quartic-terminal-defect-geometry.md) — projected sheet conservation and bounded equality/one-factor/root-triangle coefficient gadgets.
12. [`quartic-nucleus-transport.md`](quartic-nucleus-transport.md) — canonical `S_4`-equivariant isometry between successive nuclei, diagonal singular gluing, curvature transport, and the marked shell.
13. [`scalar-interval-transfer.md`](scalar-interval-transfer.md) — elementary `g`-to-`g` intervals, telescoping side output, eighteen transfer states, and algebraic backtrack reduction.
14. [`scalar-interval-caps-and-cells.md`](scalar-interval-caps-and-cells.md) — physical backtrack caps and periodic three-turn cells for elementary intervals.
15. [`periodic-kempe-ladders.md`](periodic-kempe-ladders.md) — rigid simultaneous three-Kempe wiring inside periodic elementary intervals.
16. [`g-component-transition-quotient.md`](g-component-transition-quotient.md) — the physical quotient obtained by contracting `Q-E_g`, four transition systems, common cuts, exact cut lifting, and terminal-sensitive parity.
17. [`route-capped-line-graph-carrier.md`](route-capped-line-graph-carrier.md) — the canonical route-capped `4`-regular flag-line graph, four scalar circuit partitions, and unified transition law.
18. [`relative-touch-homology.md`](relative-touch-homology.md) — the initial relative-cycle formulation and its superseding shadow-closure correction.
19. [`touch-shadows-and-cap-residue.md`](touch-shadows-and-cap-residue.md) — distinguished/shadow circuit pairs, automatic complementary-boundary closure, cap completion, and the bounded two-transition residue.
20. [`cap-residue-isotropic-completion.md`](cap-residue-isotropic-completion.md) — even triple law and complete IAS classification of loop, parallel, twin, and pendant local cap degenerations.
21. [`minimal-cap-cocycle-decomposition.md`](minimal-cap-cocycle-decomposition.md) — existence of full completion and the coupled/separated minimal-cocycle dichotomy.
22. [`frontier-localisation.md`](frontier-localisation.md) — exact remaining physical projection/composition frontier.
23. [`equivalent-formulations-and-proof-families.md`](equivalent-formulations-and-proof-families.md) — preferred and independent proof families, exact equivalences, templates, and negative boundaries.
24. [`finite-laboratories-and-certificates.md`](finite-laboratories-and-certificates.md) — exact finite computations, counterexamples, certificates, and evidentiary scope.

## Scope

The five-support programme strengthens, but does not replace, the complete paper-level Cycle Double Cover spine in the parent project. No global five-support theorem is claimed.

The controlling fixed-lift criterion is

$$
T_g^{(1)}\longrightarrow\mathscr A_5,
$$

not merely the global-colour quotient criterion `J_g -> A_5`.

The sharp nonflat frontier now has three coordinated carriers.

1. **Incidence carrier.** Every quartic design has a canonical minus-type terminal nucleus. A split sheet projects to a bounded `K_6` coefficient gadget; an all-concentrated design peels to a smaller design. The natural sheet symmetry is `S_4`; comparison with physical terminal-route and DDD support-label symmetries is open.
2. **Physical cut carrier.** Contracting the connected components of `Q-E_g` gives an even-total-degree four-pole `\Gamma_g` with four physically realised transition systems. Every internal quotient cut lifts exactly to a `g`-coloured cut in `Q`.
3. **Standard isotropic carrier.** Closing the terminals according to `12\mid34` and taking the flag-line graph gives one canonical `4`-regular graph carrying all four scalar partitions. Shadow closure and the two route caps compress every nonflat witness to one transition at each cap vertex.

The bare two-transition residue is not a full cocycle. Apart from loop/parallel/twin/pendant degenerations, an inclusion-minimal completion is either one coupled cap-to-cap cocircuit or two disjoint one-cap cocircuits with disjoint vertex supports.

The central missing theorem is a physical projection theorem: the separated branch must yield independent terminal interfaces or a separator, while the coupled branch must yield an isotropic split, alternate route/root escape, or the graph-level comparison with the DDD class.

The flat-potential, defect-forest, four-pole, and horizontal bad-flow transfer problems remain open.

## Reliability

The chapters distinguish theorem-level arguments, exact finite results, corrections, counterexamples, and open boundaries. Inclusion here does not create Lean, independent-review, peer review, publication, release, arXiv, or DOI status. See [`../FORMAL_STATUS.md`](../FORMAL_STATUS.md).
