# AffineCDC

AffineCDC studies affine incidence geometry above nowhere-zero binary flows, its complete Cycle Double Cover consequence, the orientation obstruction of retained cycle-face surfaces, and the stronger open problem of compressing compatible covers to five indexed supports.

## 1. Current orientation candidate

Branch:

`curation/affine-cdc-orientation-obstruction-v1`.

Exact base:

`curation/affine-cdc-programme-a-b1-b8-unified-v1@ec765cd03271abd3588ec36faec3d53d0f8aa03b`.

Exact OR1 authorial source:

`proof-development/affine-cdc-rigour-v1@9dc0b3a5c906e51f8f1816e00b85f7aa2a744b1b`.

This candidate adds a separate orientation-refinement layer without changing the complete ordinary CDC theorem or the five-support programme.

Read:

1. `orientation/surface-and-fixed-lift-obstruction.md`;
2. `orientation/fixed-fibre-gauge-and-duality.md`;
3. `orientation/k4-and-oriented-collapse.md`;
4. `AC_OR1_DEPENDENCY_AND_FRONTIER_MAP.md`;
5. `AC_OR1_PROVENANCE_AND_ASSURANCE.md`.

## 2. Complete Cycle Double Cover theorem

Programme A proves:

> Every multigraph with finite active edge set and no singleton cut has a finite circuit double cover.

The original Programme A candidate `68715fb29bb4b6555e2bc3e089603c5390d01566` passed Independent Audit A at `2fac31f4e76c819dd42a179a2772501c50ee93ad`.

Audit result:

`VERIFIED SUBJECT TO NAMED EXTERNAL THEOREMS / NON-BLOCKING EXPLICITNESS REPAIRS`.

The three explicitness/source repairs are integrated without theorem change:

1. exact Seymour multigraph convention;
2. complete A4 reverse local-family proof;
3. old Tutte route historical and non-controlling.

Read `complete-cdc/README.md` and `complete-cdc/audit-a-explicitness-repairs.md`.

## 3. Orientation-obstruction layer

For one compatible labelled lift $g$ above a fixed rank-three flow $f$:

- retained partner/rotation data reconstruct the indexed cycle-face surface $S_g$;
- $\omega(g)=[w(g)]\in C^1(G)/\operatorname{Cut}(G)$ is the obstruction of that lift;
- gauge motion satisfies
  $$
  w(g^k)=w(g)+\Lambda_f(k);
  $$
- $\Omega_f\in C^1(G)/(\operatorname{Cut}(G)+\mathcal B_f)$ is the base-independent obstruction of the fixed-flow fibre;
- orientable labelled lifts are empty or one torsor under $\ker\Lambda_{\mathrm{or}}$;
- orientable unlabelled Petrial words are empty or one coset under $\mathcal B_f\cap\operatorname{Cut}(G)$;
- the dual criterion uses $\operatorname{Stress}_{\mathrm{or}}(f)=Z_1(G)\cap\mathcal B_f^\perp$.

The $K_4$ fibre contains both a projective-plane lift and a tetrahedral-sphere lift. Thus per-lift automatic orientability is false, while that fixed fibre still has $\Omega_f=0$.

The support-only Programme A outer shell discards orientation data. An enriched directed-face projection followed by direction-preserving trail decomposition transports an oriented CDC through collapse. Deleted loops are reinserted as two oppositely directed singleton-loop occurrences.

Open:

- `AC-RL-OR-FIXED-FIBRE-VANISHING`;
- `AC-RL-OR-GRAPH-EXISTENCE`.

## 4. Five-support programme

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

## 5. Controlling B distinctions

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

These six five-support obligations are separate from the two orientation obligations.

## 6. Finite assurance

Finite results retain the classes `F-PROVED`, `F-CERT-PUBLIC`, `F-CERT-PRIVATE`, `F-CENSUS`, `CODE-PARTIAL`, and `AFFECTED`. B8 is assurance normalization, not independent review or public-code certification.

## 7. Project controls

- `ACTIVE_MATHEMATICAL_SURFACE.md`;
- `CURRENT_BEST.md`;
- `MATHEMATICAL_ARCHITECTURE.md`;
- `THEOREM_DEPENDENCY_MAP.md`;
- `FORMAL_STATUS.md`;
- `AC_OR1_INTEGRATION_MAP.md`;
- `AC_OR1_DEPENDENCY_AND_FRONTIER_MAP.md`;
- `AC_OR1_PROVENANCE_AND_ASSURANCE.md`;
- `AC_UNIFIED_INTEGRATION_MAP.md`;
- `AC_UNIFIED_ASSURANCE_BOUNDARY.md`;
- `CHAPTER_PROVENANCE.md`;
- `SUPERSESSION_MAP.md`;
- `FRONTIER_STATUS.md`.

## 8. Assurance

Programme A's original spine passed Independent Audit A; its repaired prose is integrated but not separately re-audited. B1--B8 have not yet received dedicated Audit B. OR1 is an authorial, Curator-integrated fixed-fibre classification ready for an independent fixed-corpus audit; Lean checks only its retained reconstruction ingredients. No end-to-end Lean, manuscript, peer-review, publication, release, arXiv, DOI, novelty, timestamp, or canonical `main` status is created.
