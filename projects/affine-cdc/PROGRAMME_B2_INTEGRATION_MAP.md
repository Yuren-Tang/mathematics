# Programme B2 integration and provenance map

## 1. Exact controls

- authoritative intake: `Yuren-Tang/research-workbench#24`, comment `5019218548`;
- integration base: `curation/affine-cdc-programme-b1-v1@4d7b9c74ea4377a58e219a7c6c3cb569a8229276`;
- immutable source: `proof-development/affine-cdc-rigour-v1@d62974704d6dac77aaa00275a595fedf7f70cfd2`;
- writable branch: `curation/affine-cdc-programme-b2-v1`;
- exact source splice: `9799d8a657cb43ed5d896d53ef16c50fc79c4e1e`.

The source splice has two parents, in order:

1. the exact B1 integration base;
2. the immutable B2 source checkpoint.

Its tree imports only the five B2 proof dossiers and the checkpoint `OBLIGATION_DAG.md`.

## 2. Unit-to-destination map

| Unit | Exact source path | Active destination | Controlling output |
|---|---|---|---|
| B2.1 | `proof-development/AC_PD_B2_1_SINGULAR_QUADRATIC_SCHUR_EQUIVALENCE.md` | `five-support/b2-formulation-and-witness-hierarchy.md`; `five-support/root-flow-lifting.md` | anisotropic mother flow; quadratic full witness; singular/Schur fixed-data equivalence |
| B2.2 | `proof-development/AC_PD_B2_2_COGRAPHIC_CYCLE_CONTINUITY.md` | `five-support/b2-formulation-and-witness-hierarchy.md`; `five-support/equivalent-formulations-and-proof-families.md` | exact inverse-cycle edge-map definition and graph-level equivalence |
| B2.3 | `proof-development/AC_PD_B2_3_ORTHOGONAL_ROOT_MODULE_CORRECTION.md` | `five-support/b2-formulation-and-witness-hierarchy.md`; `SUPERSESSION_MAP.md`; source ledgers | false universal theorem withdrawn; $q-2$ lower bound; deleted permutation module; rank-three exception |
| B2.4 | `proof-development/AC_PD_B2_4_FOURIER_STRESS_DUALITY.md` | `five-support/b2-formulation-and-witness-hierarchy.md`; `five-support/equivalent-formulations-and-proof-families.md` | Fredholm duality; exact Fourier count; primal-witness boundary |
| B2 aggregate | `proof-development/AC_PD_B2_FORMULATION_AND_WITNESS_MAP.md` | `THEOREM_DEPENDENCY_MAP.md`; `MATHEMATICAL_ARCHITECTURE.md`; `FORMAL_STATUS.md` | full witness/fixed-data/dual hierarchy |
| checkpoint ledger | `proof-development/OBLIGATION_DAG.md` | retained unchanged as authorial provenance | B2 state and B3 transition at the immutable source |

## 3. Recovered public-source provenance

The B2 dossiers audit and reconstruct mathematics from the retired public checkpoint

`research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`.

Principal packets:

- `FIVE_CDC_ANISOTROPIC_RANK_FOUR_FLOW_V1.md`;
- `FIVE_CDC_SINGULAR_QUOTIENT_LIFT_V1.md`;
- `FIVE_CDC_QUADRATIC_CYCLE_EQUATION_V1.md`;
- `FIVE_CDC_SCHUR_QUOTIENT_CRITERION_V1.md`;
- `FIVE_CDC_K5_COGRAPHIC_MAP_V1.md`;
- `FIVE_CDC_ROOT_LIFT_FOURIER_STRESS_DUALITY_V1.md`;
- `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`.

The last packet is retained only as historical provenance. Its universal theorem is false and is superseded by B2.3.

## 4. Reconstruction maps

The graph-level full-witness arrows carry explicit inverse data:

- support family ↔ coordinate root flow;
- root flow ↔ anisotropic $H_5$ flow;
- anisotropic flow ↔ quadratic cycle coordinates through $\Phi$;
- support family ↔ cographic edge map through support-pair labels and target-star preimages.

The fixed-data arrows require:

- the quotient Fano flow;
- the singular kernel line or plane;
- the contracted quotient graph;
- the incidence equation or eliminated coordinate;
- the lift torsor.

The dual layers require a primal target and preimage before a lift is reconstructed.

## 5. Excluded material

The intake does not consume:

- any `AC_PD_B3_*` dossier;
- any `AC_PD_B4_*` or later dossier;
- later `OBLIGATION_DAG.md` revisions;
- Programme B2/B3/B4/B5 handoffs as mathematical source;
- any moving-branch commit after `d62974704d6dac77aaa00275a595fedf7f70cfd2`.

## 6. Assurance

The B2 source units are complete authorial proofs for the stated equivalences and correction. Curator integration is not independent audit, Lean verification, manuscript acceptance, peer review, publication, release, arXiv, DOI, or novelty determination.
