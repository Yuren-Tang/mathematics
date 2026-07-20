# AffineCDC

AffineCDC studies affine incidence geometry above nowhere-zero binary flows, its complete Cycle Double Cover consequence, and the stronger open problem of compressing compatible covers to five indexed supports.

## 1. Unified current candidate

Branch:

`curation/affine-cdc-programme-a-b1-b8-unified-v1`.

Fixed inputs:

- accepted B1–B8 candidate `0100895d57aab7d21153c580fa9bdc45fafc832e`;
- Programme A repair checkpoint `06bce656dcf5bfd6491ec08f51a702ea56d2470d`;
- exact repair splice `a35da6ba6e4908c70f970f3cadf5fcf4b582dae4`.

This candidate aligns Programme A and B1–B8 without consuming B9 or AC-RL working-ahead material.

## 2. Complete Cycle Double Cover theorem

Programme A proves:

> Every multigraph with finite active edge set and no singleton cut has a finite circuit double cover.

The original Programme A candidate `68715fb29bb4b6555e2bc3e089603c5390d01566` passed Independent Audit A at `2fac31f4e76c819dd42a179a2772501c50ee93ad`.

Audit result:

`VERIFIED SUBJECT TO NAMED EXTERNAL THEOREMS / NON-BLOCKING EXPLICITNESS REPAIRS`.

The three explicitness/source repairs are now closed and integrated without theorem change:

1. exact Seymour multigraph convention;
2. complete A4 reverse local-family proof;
3. old Tutte route historical and non-controlling.

Read `complete-cdc/README.md` and `complete-cdc/audit-a-explicitness-repairs.md`.

## 3. Five-support programme

For finite loopless cubic multigraphs, five-support existence has exact root, triangle, matching/four-flow, Fano-plane, surface, anisotropic, quadratic, and cographic formulations. Singular/Schur criteria retain fixed data; stress/Fourier are dual/counting layers.

The global five-support theorem remains open.

Preferred reading:

1. `five-support/b1-object-quantifier-and-scope.md`;
2. `five-support/b2-formulation-and-witness-hierarchy.md`;
3. `five-support/surfaces-and-halfcube.md`;
4. `five-support/gauge-and-reconfiguration.md`;
5. `five-support/cuts-four-poles-and-routing.md`;
6. `five-support/holonomy-defects-and-atoms.md`;
7. `five-support/frontier-localisation.md`;
8. `five-support/finite-laboratories-and-certificates.md`.

## 4. Controlling B distinctions

- $T_g^{(1)}\to\mathscr A_5$ is componentwise same-embedding compression;
- $J_g\to\mathscr A_5$ is only old-colour-factorable compression;
- connected switch support gives one horizontal edge; disconnected support gives a path;
- `7737` composite endpoints and `2801` one-step neighbours remain distinct;
- cap forcing is not full-cap containment;
- finite routing transitions require source path-pair realization;
- BBD common origin is conditional on `AC-RL-BBD-GROUPOID-CLOSURE`;
- the nontrivial defect forest is removed pending `AC-RL-BBD-VARIATION-SLICE`.

The four further localization gaps are:

- `AC-RL-TYPE-T-SERIALISATION`;
- `AC-RL-FLAT-POTENTIAL-INTERFACE`;
- `AC-RL-COMMON-CUT-LOCALISATION`;
- `AC-RL-TYPE-H-COMMON-WITNESS`.

## 5. Finite assurance

Finite results retain the classes `F-PROVED`, `F-CERT-PUBLIC`, `F-CERT-PRIVATE`, `F-CENSUS`, `CODE-PARTIAL`, and `AFFECTED`. B8 is assurance normalization, not independent review or public-code certification.

## 6. Project controls

- `ACTIVE_MATHEMATICAL_SURFACE.md`;
- `CURRENT_BEST.md`;
- `MATHEMATICAL_ARCHITECTURE.md`;
- `THEOREM_DEPENDENCY_MAP.md`;
- `FORMAL_STATUS.md`;
- `AC_UNIFIED_INTEGRATION_MAP.md`;
- `AC_UNIFIED_ASSURANCE_BOUNDARY.md`;
- `CHAPTER_PROVENANCE.md`;
- `SUPERSESSION_MAP.md`;
- `FRONTIER_STATUS.md`.

## 7. Assurance

Programme A’s original spine has passed Independent Audit A; the closed repaired prose is integrated but not separately re-audited. B1–B8 have not yet received dedicated Audit B. No end-to-end Lean, manuscript, peer-review, publication, release, arXiv, DOI, novelty, timestamp, or canonical `main` status is created.