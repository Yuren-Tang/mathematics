# Programme B1 integration manifest

## 1. Control

- authoritative intake: `Yuren-Tang/research-workbench#24`, comment `5018524043`;
- integration base: `curation/affine-cdc-programme-a-v1@68715fb29bb4b6555e2bc3e089603c5390d01566`;
- immutable source: `proof-development/affine-cdc-rigour-v1@778b09ac8260192e022f512f24cdef1d04871f37`;
- control handoff: `proof-development/PROGRAMME_B1_CURATOR_HANDOFF.md`, read from the live PDL branch as routing authority only;
- candidate branch: `curation/affine-cdc-programme-b1-v1`.

## 2. History-preserving splice

The immutable source and Programme A candidate share ancestor

`8bee16780b549f51e1f29343671a059961ec4172`.

They were spliced by merge commit

`35c7a2851f070061175194eef10568c0a456cf8e`

with parents, in order:

1. `68715fb29bb4b6555e2bc3e089603c5390d01566`;
2. `778b09ac8260192e022f512f24cdef1d04871f37`.

The merge tree admits only:

- `AC_PD_B1_1_ROOT_FLOW_TRIANGLE_EQUIVALENCE.md`;
- `AC_PD_B1_2_MATCHING_FOUR_FLOW_EQUIVALENCE.md`;
- `AC_PD_B1_3_FIXED_FLOW_PLANE_CRITERION.md`;
- `AC_PD_B1_4_SURFACE_HALFCUBE_SCOPE.md`;
- `AC_PD_B1_EQUIVALENCE_AND_SCOPE_MAP.md`;
- the exact `OBLIGATION_DAG.md` at `778b09ac...`.

The source-side Programme A handoff is not copied into the candidate tree. The later Programme B1 handoff was read as a control document and is not treated as mathematical source.

## 3. Integrated destinations

The preferred active B1 theorem surface is:

- `five-support/b1-object-quantifier-and-scope.md`.

The exact boundary controls are:

- `PROGRAMME_B1_INTEGRATION_MAP.md`;
- `PROGRAMME_B1_QUANTIFIER_BOUNDARIES.md`;
- this manifest.

Synchronized corpus surfaces include:

- `five-support/root-flow-lifting.md`;
- `five-support/equivalent-formulations-and-proof-families.md`;
- `five-support/surfaces-and-halfcube.md`;
- `THEOREM_DEPENDENCY_MAP.md`;
- `MATHEMATICAL_ARCHITECTURE.md`;
- `FORMAL_STATUS.md`;
- `CURRENT_BEST.md`;
- `ACTIVE_MATHEMATICAL_SURFACE.md`;
- `five-support/README.md`.

## 4. Mathematical intake boundary

Consumed:

- B1 root-flow and $K_5$ triangle equivalence;
- exact matching/four-flow theorem;
- fixed-flow/fixed-plane component criterion;
- root-lift/surface equivalence;
- fixed-lift full-dual half-cube criterion;
- prescribed-dual holonomy criterion;
- old-colour quotient factorability boundary;
- even-halfcube parity convention;
- B1 obligation and provenance ledger.

Not consumed:

- B2 singular/quadratic/Schur/cographic/orthogonal/Fourier dossiers;
- B3 target correction dossiers;
- later PDL obligation-ledger modifications;
- later handoffs or moving-tip mathematics;
- any new finite certificate or correction after `778b09ac...`.

## 5. Assurance boundary

Programme B1 is integrated as:

`CURATOR-INTEGRATED / AUTHORIAL B1 PROOF LAYER COMPLETE`.

This is not:

- acceptance or proof of the global five-support theorem;
- independent mathematical audit;
- end-to-end Lean verification;
- manuscript approval or revision;
- peer review or publication;
- release, tag, arXiv, DOI, or timestamp action.

## 6. Repository isolation

This intake does not modify:

- `curation/affine-cdc-programme-a-v1@68715fb...`;
- `main@960c92b...`;
- the live PDL branch;
- any Lean or manuscript repository.

No branch deletion, rename, force-push, rebase, squash, or public-history rewrite is authorized or used.

## 7. Completion test

The intake is complete when:

1. every B1 arrow has an exact proof pointer;
2. all graph/fixed-flow/fixed-lift quantifiers are explicit;
3. all six corrections are installed in the active corpus;
4. B2+ files are absent from the candidate delta;
5. Programme A remains the fixed Audit A candidate;
6. the final candidate SHA is returned to issue #24 for AC-DIR disposition.
