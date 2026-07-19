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
   Connected pairwise sheet-incidence graphs, terminal Euler trails, exact cycle rank, and the physical ribbon transition skeleton.

10. [`frontier-localisation.md`](frontier-localisation.md)  
    Exact remaining localisation/composition frontier and recommended proof order.

11. [`equivalent-formulations-and-proof-families.md`](equivalent-formulations-and-proof-families.md)  
    Preferred and independent proof families, exact equivalences, sufficient templates, and negative boundaries.

12. [`finite-laboratories-and-certificates.md`](finite-laboratories-and-certificates.md)  
    Exact finite computations, counterexamples, certificates, and their evidentiary scope.

## Scope

The five-support programme strengthens, but does not replace, the complete paper-level Cycle Double Cover spine in the parent project. No global five-support theorem is claimed.

The controlling fixed-lift criterion is

$$
T_g^{(1)}\longrightarrow\mathscr A_5,
$$

not merely the global-colour quotient criterion `J_g -> A_5`.

The sharp nonflat frontier is composition of a singleton enriched atom or a two-edge scalar transition interval, together with classification or decomposition of enriched quartic phase designs. Pure quartic incidence parity cannot bound the residual core: abstract quartic witness designs exist for every `k\ge1`. Physical route-lock adds an affine plane of scalar sheets related by three quotient Kempe cycle systems, nine endpoint quotient labels with aligned/crossed signatures, and a connected quartic pairwise transition skeleton with two terminal leaves. The flat-potential, defect-forest, four-pole, and horizontal bad-flow transfer problems remain open.

## Reliability

The chapters synthesize theorem-level public arguments, exact finite results, independent proof families, corrections, counterexamples, and open boundaries. Inclusion here does not create Lean, independent-review, peer review, publication, release, arXiv, or DOI status. See [`../FORMAL_STATUS.md`](../FORMAL_STATUS.md).