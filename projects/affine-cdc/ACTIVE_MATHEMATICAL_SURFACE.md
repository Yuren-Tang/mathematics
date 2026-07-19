# AffineCDC active mathematical surface

This file identifies the current-best mathematical surface produced by `AC-CORPUS-01` and later exact Research Lead frontier commits.

## 1. Construction line

The active surface is built on:

- `main@749e0579581fcc838685138b3582f4de306b8e72`;
- public five-support checkpoint `dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`;
- accepted outer-shell source `0927011177cabac20f06a57fa5e57476d6f13dee`;
- reconstruction base `7a166d2eb5642ec967f640323488e49f1c2ad5d4`;
- completed corpus migration `960c92b7ff231c78b387894149779083060a75eb`;
- later commits on `research/affine-cdc-five-cdc-v1`.

Retired discovery packets remain recoverable in Git ancestry; they are not the current reading surface.

## 2. Primary entrypoints

- [`README.md`](README.md);
- [`CURRENT_BEST.md`](CURRENT_BEST.md);
- [`MATHEMATICAL_ARCHITECTURE.md`](MATHEMATICAL_ARCHITECTURE.md);
- [`THEOREM_DEPENDENCY_MAP.md`](THEOREM_DEPENDENCY_MAP.md);
- [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md).

## 3. Complete CDC spine

The paper-level Cycle Double Cover line is contained in:

- [`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md);
- [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md);
- [`reduction/outer-shell-and-binary-flow.md`](reduction/outer-shell-and-binary-flow.md);
- [`reduction/even-cover-and-collapse.md`](reduction/even-cover-and-collapse.md).

The natural theorem allows loops and finite active edge set. The present Lean declaration remains an earlier loopless ambient-finite checkpoint.

## 4. Active five-support chapters

1. [`five-support/root-flow-lifting.md`](five-support/root-flow-lifting.md);
2. [`five-support/surfaces-and-halfcube.md`](five-support/surfaces-and-halfcube.md);
3. [`five-support/gauge-and-reconfiguration.md`](five-support/gauge-and-reconfiguration.md);
4. [`five-support/cuts-four-poles-and-routing.md`](five-support/cuts-four-poles-and-routing.md);
5. [`five-support/holonomy-defects-and-atoms.md`](five-support/holonomy-defects-and-atoms.md);
6. [`five-support/common-cut-circuit-localisation.md`](five-support/common-cut-circuit-localisation.md);
7. [`five-support/quartic-witness-designs.md`](five-support/quartic-witness-designs.md);
8. [`five-support/route-locked-quotient-phase.md`](five-support/route-locked-quotient-phase.md);
9. [`five-support/quartic-transition-skeletons.md`](five-support/quartic-transition-skeletons.md);
10. [`five-support/quartic-terminal-nucleus.md`](five-support/quartic-terminal-nucleus.md);
11. [`five-support/quartic-terminal-defect-geometry.md`](five-support/quartic-terminal-defect-geometry.md);
12. [`five-support/quartic-nucleus-transport.md`](five-support/quartic-nucleus-transport.md);
13. [`five-support/scalar-interval-transfer.md`](five-support/scalar-interval-transfer.md);
14. [`five-support/scalar-interval-caps-and-cells.md`](five-support/scalar-interval-caps-and-cells.md);
15. [`five-support/periodic-kempe-ladders.md`](five-support/periodic-kempe-ladders.md);
16. [`five-support/g-component-transition-quotient.md`](five-support/g-component-transition-quotient.md);
17. [`five-support/route-capped-line-graph-carrier.md`](five-support/route-capped-line-graph-carrier.md);
18. [`five-support/relative-touch-homology.md`](five-support/relative-touch-homology.md);
19. [`five-support/frontier-localisation.md`](five-support/frontier-localisation.md);
20. [`five-support/equivalent-formulations-and-proof-families.md`](five-support/equivalent-formulations-and-proof-families.md);
21. [`five-support/finite-laboratories-and-certificates.md`](five-support/finite-laboratories-and-certificates.md).

The global five-support theorem remains open. The controlling fixed-lift object is `T_g^{(1)}`, not merely the factorable quotient `J_g`.

## 5. Current nonflat architecture

The common-cut witness is localized to a singleton, a marked two-edge transition, or a quartic core.

At the incidence level:

- quartic designs exist for every `4k+1`;
- every design has a canonical `O^-(4,2)` terminal nucleus with intrinsic `E_5/K_5` geometry and route stabiliser `D_8`;
- a split sheet exposes a bounded `K_6` defect gadget;
- an all-concentrated design peels to level `k-1`.

At the physical level there are three carriers.

1. **`g`-component quotient `\Gamma_g`.** Contract the components of `Q-E_g`. Four scalar sheets become four transition systems on an even-total-degree four-pole. Every internal quotient cut lifts exactly to a `g`-coloured cut of `Q`; cut parity retains the number of original terminal flags on the shore.
2. **Route-capped line graph.** Close terminals according to `12\mid34` and take the flag-line graph. This gives one canonical `4`-regular graph carrying four scalar circuit partitions and a uniform aligned/crossed transition law.
3. **Relative touch homology.** The common-cut kernel is the intersection of four relative touch-cycle spaces. Curvature is terminal relative-boundary evaluation. Complementary touch boundary may remain, so the witness is not yet proved to be a transition-matroid circuit.

Elementary non-`g` paths between consecutive full `g`-incidences have eighteen transfer states and bounded cap-or-periodic-ladder normal forms. Consecutive witness edges may contain further edges of `E_g\setminus\eta`; whole witness arcs are transition walks in `\Gamma_g`.

## 6. Exact frontier

The immediate theorem is:

$$
\boxed{
\text{fourfold relative curvature cycle}
\Longrightarrow
\begin{cases}
\text{bounded touch-boundary closure / transverse dependence},\\
\text{terminal-even separator or transition two-sum in }\Gamma_g,\\
\text{physical }D_8\text{ class}.
\end{cases}}
$$

Direct use of isotropic connectivity is not yet justified because the present witness is only relatively closed at the scalar-circuit shore.

## 7. Reliability and provenance

See:

- [`CHAPTER_PROVENANCE.md`](CHAPTER_PROVENANCE.md);
- [`MIGRATION_LEDGER.md`](MIGRATION_LEDGER.md);
- [`SUPERSESSION_MAP.md`](SUPERSESSION_MAP.md);
- [`RETIRED_SOURCE_CLASSIFICATION.md`](RETIRED_SOURCE_CLASSIFICATION.md);
- [`SOURCE_RECOVERY_AUDIT.md`](SOURCE_RECOVERY_AUDIT.md);
- [`FORMAL_STATUS.md`](FORMAL_STATUS.md);
- [`RECONSTRUCTION_MANIFEST.md`](RECONSTRUCTION_MANIFEST.md).

Current-best inclusion does not create independent review, Lean verification, peer review, manuscript approval, release, arXiv, DOI, or publication status.
