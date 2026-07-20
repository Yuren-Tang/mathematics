# AffineCDC chapter provenance

This map records how the active five-support chapters were synthesized from the exact public checkpoint

`research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`.

The source packets are recoverable through Git history. A source name below identifies mathematical provenance, not an active reading dependency.

## 1. `five-support/root-flow-lifting.md`

### Controlling sources

- `FIVE_CDC_ROOT_FLOW_TRIANGLE_COMPLEX_V1.md`;
- `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`;
- `FIVE_CDC_ANISOTROPIC_RANK_FOUR_FLOW_V1.md`;
- `FIVE_CDC_COLOUR_CUT_REFINEMENT_V1.md`;
- `FIVE_CDC_MATCHING_FOUR_FLOW_BRIDGE_V1.md`.

Independent singular, quadratic/Schur, cographic, and orthogonal formulations are retained because they support later operations.

## 2. `five-support/surfaces-and-halfcube.md`

Controlling geometry:

- `FIVE_CDC_COLORED_SURFACE_DUAL_HALFCUBE_V1.md`;
- `FIVE_CDC_HALFCUBE_SCOPE_CORRECTION_V1.md`;
- `FIVE_CDC_COLORED_SURFACE_DUAL_HALFCUBE_ERRATUM_V1.md`.

The full dual triangulation `T_g` is controlling. The old-colour graph `J_g` is retained only as the global-index-factorable quotient.

Target and negative-boundary packets include the half-cube subgraph classification, clique-link capacity, source-dependent compression, no-universal-compression warning, and componentwise programme checkpoints.

## 3. `five-support/gauge-and-reconfiguration.md`

Vertical motion derives from the gauge-as-translation, partial-Petrial, marked-obstruction, frozen-cycle, mixed-core, and essential-renewal packets.

Horizontal motion derives from the support-cycle pivot, harmonic-quotient surgery, admissible-switch image, internal/external switch dichotomy, switch-incidence, and fixed-flow graph-level separation packets.

Gauge/Petrial motion at fixed flow and connected-cycle motion between flows remain separate levels.

## 4. `five-support/cuts-four-poles-and-routing.md`

Controlling packets:

- three-cut reserve-line reduction;
- ten-state four-edge boundary signatures;
- cap forcing;
- four-pole Kempe closure;
- pairing alignment;
- small four-pole profile census;
- routing-weight and holonomy dichotomy.

The chapter separates general graph theorems from finite profile counts. The full-cap-profile theorem remains open.

## 5. `five-support/holonomy-defects-and-atoms.md`

The rainbow/local-system layer comes from the choice-parity square, residual quotient coordinates, affine holonomy norm, root-admissible linearisation, Tait resolution, genuine path-family reduction, and Type H escape packets.

The BBD/DDD layer comes from global BBD holonomy, defect-minimal forest/Petersen transport, DDD atom triality, route-lock curvature, rank-two escape, and full-rank curvature duality.

The BBD per-loop alternatives are superseded by the common-origin/canonical-defect-flow synthesis. The DDD one-bit cohomological class remains a separate live exception.

## 6. `five-support/equivalent-formulations-and-proof-families.md`

This chapter preserves the distinct uses of the Fourier/stress duality, affine-subspace sieve, flow-tension finite-state, orientation transgression, Tait/Tutte bridge, and the singular, quadratic, Schur, cographic, surface, interface, and holonomy sources.

The preferred proof, independent role, exact implication, and scope limitation are retained without keeping parallel discovery-order chapters.

## 7. `five-support/finite-laboratories-and-certificates.md`

The finite layer records fixed-flow orbit obstruction, gauge escape, renewal cubes, reserve-code censuses, horizontal neighbourhoods, componentwise dual censuses, Petersen flow classification, flower-snark mixed cores, and finite atom/monodromy tables.

Exact counts and certificates are retained. Raw discovery logs and private notebook chronology are not active theorem dependencies.

## 8. `five-support/frontier-localisation.md`

The frontier synthesis depends especially on the mechanism-closure map, Type T/Type H reduction, BBD/DDD defect packets, mixed-core laboratories, and later exact AC-RL frontier chapters.

The controlling endpoint is localisation and composition of route-locked full-rank defects, not another unrestricted census.

## 9. Later AC-RL route-locked frontier chapters

The chapters from `common-cut-circuit-localisation.md` through the quartic nucleus, physical transition quotient, route-capped line graph, cap residue, cocircuit completion, cut-rank, physical cycle--cut response, ribbon response, gauge duality, and dual-rank localisation were proved on the active Research Lead branch after the corpus migration.

Their internal AffineCDC inputs are:

- the active route-lock curvature theorem and scalar sheets;
- the gauge/Petrial code;
- the Schur duality
  $$
  \mathcal B_f^\perp=\mathcal C(G)*\mathcal F_f;
  $$
- the physical four-pole and transition-system chapters;
- the existing scalar interval, Tait-resolution, zero-network, and defect geometry.

### External general frameworks consulted

The following established theories supply terminology and general background, not the AffineCDC-specific theorem conclusions.

- Brijder and Traldi's isotropic/transition-matroid work: circuit partitions, touch-graphs, transverse cographic restrictions, interlacement connectivity, and split signatures.
- Kleptsyn and Smirnov, *Ribbon graphs and bialgebra of Lagrangian subspaces*, arXiv:1401.6160 / J. Knot Theory Ramifications 26 (2016), 1642006: ribbon-graph `L`-spaces as Lagrangian subspaces and the chord-intersection special case.
- Standard ribbon-graph and delta-matroid theory: signed rotations, partial dual/Petrial operations, and chord/intersection matrices.
- Standard mod-two Poincare--Lefschetz duality for the boundary radical and surface intersection form.

The active chapters give self-contained proofs of the line-graph natural-transversal sequence, physical response form, gauge-radicalisation criterion, hyperbolic norm representation, and rank-one/two localisation. No novelty claim is inferred merely from the use of established general frameworks.

### Computational reliability

Wolfram checks were used only to:

- sanity-check IAS cocircuit formulas on small interlacement graphs;
- verify local `\mathbf F_2^2` flow tables;
- expose and certify the cube multicycle counterexample.

The general theorems are proved independently of those computations. The cube counterexample is retained as an explicit finite certificate.

## 10. Downstream projections

The Tait/Tutte bridge and orientation/coefficient-holonomy sources support optional Four Colour, orientability, and five-flow projections. These remain mathematically valuable but are not controlling inputs to the global five-support proof.

## 11. Recovery rule

For any retired source packet `FILE`, the exact body is recovered by:

```text
git show dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c:projects/affine-cdc/research/FILE
```

See [`SOURCE_RECOVERY_AUDIT.md`](SOURCE_RECOVERY_AUDIT.md) and [`RETIRED_SOURCE_CLASSIFICATION.md`](RETIRED_SOURCE_CLASSIFICATION.md).
