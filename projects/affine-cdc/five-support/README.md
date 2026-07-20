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
6. [`common-cut-circuit-localisation.md`](common-cut-circuit-localisation.md) — scalar-component incidence, odd witness circuits, and singleton/transition/quartic localisation.
7. [`quartic-witness-designs.md`](quartic-witness-designs.md) — unbounded abstract quartic cores and symplectic cross-intersection.
8. [`route-locked-quotient-phase.md`](route-locked-quotient-phase.md) — quotient Tait flow, binary phase, affine sheet plane, Kempe differences, and endpoint signatures.
9. [`quartic-transition-skeletons.md`](quartic-transition-skeletons.md) — connected pairwise marked ribbon skeletons.
10. [`quartic-terminal-nucleus.md`](quartic-terminal-nucleus.md) — canonical `O^-(4,2)` nucleus, curvature carrier, symmetry correction, and split-or-peel recursion.
11. [`quartic-terminal-defect-geometry.md`](quartic-terminal-defect-geometry.md) — bounded equality/one-factor/root-triangle coefficient gadgets.
12. [`quartic-nucleus-transport.md`](quartic-nucleus-transport.md) — successive-nucleus transport and marked shell.
13. [`scalar-interval-transfer.md`](scalar-interval-transfer.md), [`scalar-interval-caps-and-cells.md`](scalar-interval-caps-and-cells.md), and [`periodic-kempe-ladders.md`](periodic-kempe-ladders.md) — finite elementary interval and ladder normal forms.
14. [`g-component-transition-quotient.md`](g-component-transition-quotient.md) — physical quotient `\Gamma_g`, transition systems, exact cut lifting, and terminal parity.
15. [`route-capped-line-graph-carrier.md`](route-capped-line-graph-carrier.md) — the canonical route-capped `4`-regular carrier.
16. [`relative-touch-homology.md`](relative-touch-homology.md) and [`touch-shadows-and-cap-residue.md`](touch-shadows-and-cap-residue.md) — relative formulation, shadow correction, cap closure, and the bounded two-transition residue.
17. [`cap-residue-isotropic-completion.md`](cap-residue-isotropic-completion.md), [`minimal-cap-cocycle-decomposition.md`](minimal-cap-cocycle-decomposition.md), and [`cocircuit-cutrank-mechanism.md`](cocircuit-cutrank-mechanism.md) — local degenerations, coupled/separated completion, and split-or-prime cut-rank.
18. [`natural-transversal-physical-projection.md`](natural-transversal-physical-projection.md) and [`natural-transversal-cycle-cut-exact-sequence.md`](natural-transversal-cycle-cut-exact-sequence.md) — canonical projection to `\widehat Q` and the exact cycle--cut sequence.
19. [`physical-cycle-cut-response-form.md`](physical-cycle-cut-response-form.md) — the Lagrangian physical response code.
20. [`ribbon-intersection-response.md`](ribbon-intersection-response.md) — response as mod-two ribbon intersection; radical, Euler genus, orientability, and Petrial law.
21. [`gauge-radicalisation-duality.md`](gauge-radicalisation-duality.md) — exact admissible radicalisation and persistent odd-intersection duality.
22. [`persistent-intersection-hyperbolic-flow.md`](persistent-intersection-hyperbolic-flow.md) — Schur-dual words as hyperbolic-flow norm supports and the dual-rank hierarchy.
23. [`rank-one-persistent-interval-localisation.md`](rank-one-persistent-interval-localisation.md) — rank-one reduction to one odd scalar circuit or interval.
24. [`rank-two-tait-permutation-localisation.md`](rank-two-tait-permutation-localisation.md) — rank-two reduction to one odd closed or defect-to-defect carrier.
25. [`cube-multicycle-cocircuit-certificate.md`](cube-multicycle-cocircuit-certificate.md) — exact negative certificate against a single projected circuit.
26. [`cap-residue-symmetry-correction.md`](cap-residue-symmetry-correction.md) — separation of sheet `S_4`, terminal-route coordinates, and DDD support-label `D_8`.
27. [`frontier-localisation.md`](frontier-localisation.md) — exact remaining rank-three/composition frontier.
28. [`equivalent-formulations-and-proof-families.md`](equivalent-formulations-and-proof-families.md) and [`finite-laboratories-and-certificates.md`](finite-laboratories-and-certificates.md) — alternate proof families and finite evidence.

## Scope

The programme strengthens, but does not replace, the complete paper-level Cycle Double Cover spine. No global five-support theorem is claimed. The controlling fixed-lift criterion remains

$$
T_g^{(1)}\longrightarrow\mathscr A_5,
$$

not merely the factorable quotient through `J_g`.

The nonflat endpoint now has a physical topological and code-theoretic normal form.

1. Every common-cut witness compresses to a two-transition cap residue.
2. Minimal completion is coupled or separated; cut-rank separates disconnected, split, and prime carriers.
3. The natural transversal gives
   $$
   0\to\operatorname{Cut}(\widehat Q)
   \to\operatorname{Cocycle}(M_\tau)
   \to\operatorname{Cycle}(\widehat Q)\to0.
   $$
4. The resulting response form is the ribbon-surface mod-two intersection pairing. Its radical is boundary homology and its rank is Euler genus.
5. Admissible gauge/Petrial motion radicalises a response cycle exactly when one explicit linear equation is solvable. Failure gives physical cycles `z,z'` with odd intersection and
   $$
   z\odot z'\in\mathcal B_f^\perp
   =\mathcal C(G)*\mathcal F_f.
   $$
6. This common-edge word is the norm support of a dual-valued hyperbolic flow. Dual ranks one and two are localised respectively to scalar intervals/circuits and defect-to-defect paths/circuits.

The first genuinely unlocalised branch is now **dual rank three**, together with composition of the already localised rank-one and rank-two carriers. The likely final comparison target is the physical DDD support-label class, but no identification is claimed.

The flat-potential, defect-forest, four-pole, and horizontal bad-flow transfer problems remain open downstream.

## Reliability

The chapters distinguish theorem-level arguments, exact finite results, corrections, counterexamples, and open boundaries. Inclusion here does not create Lean, independent-review, peer review, publication, release, arXiv, or DOI status. See [`../FORMAL_STATUS.md`](../FORMAL_STATUS.md).
