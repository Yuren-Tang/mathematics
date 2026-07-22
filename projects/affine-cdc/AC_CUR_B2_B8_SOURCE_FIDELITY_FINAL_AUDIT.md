# AC-CUR-B2-B8-SOURCE-FIDELITY-01 final curation audit

## 1. Exact controls

- PORT-DIR reactivation: `Yuren-Tang/research-workbench#24`, comment `5038617415`;
- controlling AC-DIR supplement: issue #24 comment `5029523835`;
- MATH-CUR acknowledgement: issue #24 comment `5042466358`;
- immutable base: `curation/affine-cdc-programme-a-b1-b8-unified-v1@ec765cd03271abd3588ec36faec3d53d0f8aa03b`;
- authorial source: `proof-development/affine-cdc-rigour-v1@9ce8de5ca5b7b41e139be4c94572de7725446046`;
- writable branch: `curation/affine-cdc-programme-a-b1-b8-source-fidelity-v1`;
- exact source splice: `344bf612d5d4231d954cb57fad15d93aa55d27d5`;
- substantive Curator commit before this audit: `7f59295aacaa97f5c3dbeff8e6e6889e45aa545a`.

The exact final candidate SHA is recorded in the authoritative issue #24 return because a commit cannot contain its own SHA.

## 2. Source-splice audit

The splice has two parents, in order:

1. exact fixed base `ec765cd03271abd3588ec36faec3d53d0f8aa03b`;
2. exact PDL repair checkpoint `9ce8de5ca5b7b41e139be4c94572de7725446046`.

Its tree imports exactly four substantive source paths:

| Path | Exact blob |
|---|---|
| `proof-development/AC_PD_B2_3_ORTHOGONAL_ROOT_MODULE_CORRECTION.md` | `a15cb4aeea52b2c44691e2e7184ea67b1094cc94` |
| `proof-development/AC_PD_B2_3_SOURCE_FIDELITY_REPAIR.md` | `3931acfe5de3672e3a099c83c32bc9556f40c9b0` |
| `proof-development/AC_PD_B2_FORMULATION_AND_WITNESS_MAP.md` | `50673832956a4b43867010a4b24973693025f778` |
| `proof-development/AC_PD_B8_SOURCE_FIDELITY_ADDENDUM.md` | `714f4bfc860ef796f8285b0b396b51bf41bf6d5b` |

The candidate retains those exact blob identities. The PDL `OBLIGATION_DAG.md`, B2/B8 handoffs, B9, and later moving branch state were not imported.

## 3. Comparison audit before final-audit file

Fixed base to substantive candidate:

- status: `ahead`;
- ahead: `12` commits;
- behind: `0`;
- merge base: exactly `ec765cd03271abd3588ec36faec3d53d0f8aa03b`;
- changed paths: `37`;
- exact source paths: `4`;
- Curator paths: `33`.

Source splice to substantive candidate:

- ahead: `1` Curator commit;
- behind: `0`;
- changed paths: exactly `33` Curator paths;
- no `proof-development/` changes.

This final audit adds one Curator control path only.

## 4. Complete changed-file inventory

### Exact source paths — 4

1. `projects/affine-cdc/proof-development/AC_PD_B2_3_ORTHOGONAL_ROOT_MODULE_CORRECTION.md`
2. `projects/affine-cdc/proof-development/AC_PD_B2_3_SOURCE_FIDELITY_REPAIR.md`
3. `projects/affine-cdc/proof-development/AC_PD_B2_FORMULATION_AND_WITNESS_MAP.md`
4. `projects/affine-cdc/proof-development/AC_PD_B8_SOURCE_FIDELITY_ADDENDUM.md`

### Curator paths — 33

1. `projects/affine-cdc/ACTIVE_MATHEMATICAL_SURFACE.md`
2. `projects/affine-cdc/AC_CUR_B2_B8_SOURCE_FIDELITY_ASSURANCE_LEDGER.md`
3. `projects/affine-cdc/AC_CUR_B2_B8_SOURCE_FIDELITY_INTEGRATION_MANIFEST.md`
4. `projects/affine-cdc/AC_CUR_B2_B8_SOURCE_FIDELITY_INTEGRATION_MAP.md`
5. `projects/affine-cdc/AC_CUR_B2_B8_SOURCE_FIDELITY_MIGRATION_AUDIT.md`
6. `projects/affine-cdc/AC_UNIFIED_ASSURANCE_BOUNDARY.md`
7. `projects/affine-cdc/AC_UNIFIED_FINAL_AUDIT.md`
8. `projects/affine-cdc/AC_UNIFIED_INTEGRATION_MANIFEST.md`
9. `projects/affine-cdc/AC_UNIFIED_INTEGRATION_MAP.md`
10. `projects/affine-cdc/CHAPTER_PROVENANCE.md`
11. `projects/affine-cdc/CURRENT_BEST.md`
12. `projects/affine-cdc/FORMAL_STATUS.md`
13. `projects/affine-cdc/MATHEMATICAL_ARCHITECTURE.md`
14. `projects/affine-cdc/MIGRATION_LEDGER.md`
15. `projects/affine-cdc/PROGRAMME_B2_FINAL_AUDIT.md`
16. `projects/affine-cdc/PROGRAMME_B2_INTEGRATION_MANIFEST.md`
17. `projects/affine-cdc/PROGRAMME_B2_INTEGRATION_MAP.md`
18. `projects/affine-cdc/PROGRAMME_B3_B8_ASSURANCE_LEDGER.md`
19. `projects/affine-cdc/PROGRAMME_B3_B8_FINAL_AUDIT.md`
20. `projects/affine-cdc/PROGRAMME_B3_B8_INTEGRATION_MANIFEST.md`
21. `projects/affine-cdc/PROGRAMME_B3_B8_INTEGRATION_MAP.md`
22. `projects/affine-cdc/PROGRAMME_B3_B8_STATUS_AND_GAPS.md`
23. `projects/affine-cdc/README.md`
24. `projects/affine-cdc/RECONSTRUCTION_MANIFEST.md`
25. `projects/affine-cdc/RETIRED_SOURCE_CLASSIFICATION.md`
26. `projects/affine-cdc/SOURCE_RECOVERY_AUDIT.md`
27. `projects/affine-cdc/SUPERSESSION_MAP.md`
28. `projects/affine-cdc/THEOREM_DEPENDENCY_MAP.md`
29. `projects/affine-cdc/five-support/README.md`
30. `projects/affine-cdc/five-support/b2-formulation-and-witness-hierarchy.md`
31. `projects/affine-cdc/five-support/equivalent-formulations-and-proof-families.md`
32. `projects/affine-cdc/five-support/finite-laboratories-and-certificates.md`
33. `projects/affine-cdc/five-support/root-flow-lifting.md`

## 5. Source/proposition separation audit

The recovered packet

`FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`

at blob `2043ada9d28789ecc5f4f0028e62133f37835bc1` is restored as theorem-level historical source in exact fixed-dimensional scope:

- $H_8$;
- Hamming kernel and moment map;
- six-dimensional $O^+(6,2)$;
- twenty-eight anisotropic roots;
- rank-three compatible root lifts;
- five-coordinate $O^-(4,2)$ slices;
- omitted-triple orthogonality.

It contains no arbitrary-rank $\Gamma\oplus\Gamma^*$ model, no $d_h(a)=([a],\operatorname{ev}_a)$ formula, and no universal $O^+(2r,2)$ tower.

No earlier exact committed source was recovered for that arbitrary-rank proposition. Its exact class is

`SOURCE-UNRECONSTRUCTED / INFERRED-EXTRAPOLATION OR UNCOMMITTED DRAFT / MATHEMATICALLY REFUTED BY B2.3`.

It is a separate non-packet record. The first recoverable committed text displaying it as an earlier theorem is the original PDL B2.3 correction layer; this does not turn it into a historical packet theorem.

The genuine all-rank transgression/residue hierarchy remains valid and distinct.

## 6. Mathematical replacement audit

The following remain unchanged and active:

1. triangle relations force point potentials $r_{ab}=p_a+p_b$;
2. the Gram matrix has rank $q-2$;
3. $\dim V\ge q-2$;
4. dimension $2r$ is impossible for $q=2^r$, $r\ge4$;
5. the deleted permutation module has dimension $q-2$ and attains the bound;
6. rank three is exceptional because $8-2=6=2\cdot3$;
7. five supports use the exact $O^-(4,2)$ root model.

The source-fidelity repair changes attribution and migration only, not this mathematics.

## 7. Seventy-eight-packet accounting audit

The packet-by-packet placement is:

- 39 controlling theorem/mechanism packets;
- 10 independent proof/representation packets;
- 18 finite theorem/witness/certificate packets;
- 10 correction/negative-boundary packets;
- 1 programme-synthesis packet.

Thus

$$
39+10+18+10+1=78.
$$

The named orthogonal packet belongs among the thirty-nine theorem/mechanism packets. There is no packet-wide false-theorem class. The unreconstructed extrapolation is outside the packet population and receives no packet assurance class.

## 8. B8 assurance audit

The fixed-dimensional packet’s valid results retain their actual `F-PROVED`, `F-CERT-PUBLIC`, `F-CERT-PRIVATE`, or other exact classes. No finite result is invalidated merely because it appears in the named packet.

Only computations or deductions that actually presuppose the nonexistent arbitrary-rank tower are `AFFECTED` for that inference. All unrelated B8 classifications remain unchanged. `CODE-PARTIAL` remains non-load-bearing.

## 9. Preserved-mathematics audit

The candidate preserves:

- Programme A theorem, Audit A result, and explicitness repairs;
- B1 object and quantifier boundaries;
- B2 full witness hierarchy, fixed-data criteria, stress/Fourier boundaries, and mathematical correction;
- B3 target/full-dual/factorable mathematics;
- B4 vertical/horizontal and connected/composite motion mathematics;
- B5 interface theorem/certificate boundary;
- B6 positive theorems, groupoid correction, and variation-domain correction;
- B7 rank/curvature theorems and four localization gaps;
- B8 assurance classes outside the corrected attribution;
- all six exact AC-RL frontier obligations;
- B9 blocked/excluded status;
- the open status of the global five-support theorem.

## 10. B9 and later-work exclusion

`projects/affine-cdc/proof-development/AC_PD_B9_CORRECTED_GLOBAL_FRONTIER_ASSEMBLY.md` is absent from the candidate tree. No B9 handoff, later PDL DAG, later moving PDL source, or AC-RL working-ahead mathematics is consumed.

## 11. Repository isolation

Verified unchanged:

- `main@960c92b7ff231c78b387894149779083060a75eb`;
- fixed unified branch `ec765cd03271abd3588ec36faec3d53d0f8aa03b`;
- Audit B branch `110f014c551d4ce0f109ca5559d234ddb124d8f1`;
- PDL source branch `9ce8de5ca5b7b41e139be4c94572de7725446046`.

Only `curation/affine-cdc-programme-a-b1-b8-source-fidelity-v1` was written. No force-push, rebase, squash, branch deletion/rename, public-history rewrite, public issue #2 mutation, Lean/manuscript write, release, publication, arXiv, DOI, or tag action occurred.

## 12. Stop-condition audit

No stop condition was triggered.

- the exact packet body and its valid role are known;
- the absence of an earlier source is honestly classifiable;
- the mathematical correction is self-contained;
- the packet partition is exact;
- B8 assurance can be synchronized without changing unrelated results;
- no new frontier mathematics or later branch state is required;
- no prohibited surface must be mutated.

## 13. Assurance classification and receiver

The candidate is

`CURATOR-INTEGRATED / B2-B8 SOURCE-FIDELITY CORRECTED / MATHEMATICS PRESERVED / INDEPENDENT RE-AUDIT REQUIRED`.

It is not the required independent source-fidelity re-audit and creates no canonical, Lean, manuscript, publication, release, arXiv, DOI, novelty, timestamp, or tag status.

Receiver: `AffineCDC — Director` (`AC-DIR`) through `Yuren-Tang/research-workbench` issue #24.