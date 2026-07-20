# Programme B2 final curation audit

## 1. Exact controls

- authoritative intake: `Yuren-Tang/research-workbench#24`, comment `5019218548`;
- integration base: `curation/affine-cdc-programme-b1-v1@4d7b9c74ea4377a58e219a7c6c3cb569a8229276`;
- immutable B2 source: `proof-development/affine-cdc-rigour-v1@d62974704d6dac77aaa00275a595fedf7f70cfd2`;
- candidate branch: `curation/affine-cdc-programme-b2-v1`;
- exact source splice: `9799d8a657cb43ed5d896d53ef16c50fc79c4e1e`.

The exact final candidate SHA is recorded in the authoritative issue #24 return.

## 2. Splice and ancestry audit

The splice commit has two parents, in order:

1. `4d7b9c74ea4377a58e219a7c6c3cb569a8229276`;
2. `d62974704d6dac77aaa00275a595fedf7f70cfd2`.

Its tree imports exactly:

- B2.1 singular/quadratic/Schur dossier;
- B2.2 cographic dossier;
- B2.3 orthogonal correction dossier;
- B2.4 stress/Fourier dossier;
- B2 aggregate witness map;
- the immutable B2 checkpoint `OBLIGATION_DAG.md`.

Source-side routing handoffs were not copied into the candidate.

## 3. Source-blob audit

Relative to the splice commit, the Curator delta modifies no file under `projects/affine-cdc/proof-development/`.

Therefore all five B2 dossiers and the checkpoint DAG retain exact source blob identity.

## 4. Complete-witness audit

The active corpus now contains explicit mutually inverse reconstructions among:

- five indexed even supports;
- $R_5$-valued flows;
- $K_5$-triangle labellings;
- anisotropic $O^-(4,2)$ flows;
- quadratic cycle solutions $(b,d,x,y)$;
- cographic cycle-continuous edge maps.

The coordinate reconstruction is

$$
\Phi(b,d,x,y)
=(b,d,b+d+y,b+d+x,b+d+x+y).
$$

The cographic map is defined by inverse images of target binary cycles. No strong-map, quotient, embedding, injectivity, or surjectivity claim is introduced.

## 5. Fixed-data audit

The candidate preserves the exact fixed-data equivalence among:

- anisotropic singular-line lifting;
- kernel-line component defect;
- fixed-plane colour-cut obstruction;
- existence of the eliminated cycle word $d$;
- the Schur quotient condition $x*y\in\mathcal C(Q_b)$.

The quotient flow, singular line or plane, quotient graph, and lift torsor remain explicit. A boundary word alone is not represented as a five-support witness.

## 6. Stress and Fourier audit

The active corpus records:

- exact prescribed-value Fredholm duality via relative stresses;
- exact Fourier counting of one fixed evaluation code against one allowed set;
- positive count as existence, not an exhibited primal lift;
- primal recovery through one codeword and preimage;
- zero count as aggregate cancellation, not automatically one separating stress;
- finite weight enumerators as finite evidence, not uniform estimates.

## 7. Orthogonal correction audit

`FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md` has been removed from the active theorem and controlling provenance layers.

It is classified as:

`RETIRED / SUPERSEDED / FALSE THEOREM / HISTORICAL PROVENANCE`.

The candidate installs:

1. the type-invalid-formula warning;
2. the sharp dimension lower bound $\dim V\ge q-2$;
3. the deleted permutation module of dimension $q-2$;
4. the exceptional status of the eight-support $O^+(6,2)$ model;
5. the explicit denial of a universal $O^+(2r,2)$ tower.

## 8. Source-ledger audit

The false packet is no longer classified among absorbed controlling theorems.

The seventy-eight retired source packets are now partitioned as:

$$
38+10+18+10+1+1=78,
$$

where the final class is the one superseded false theorem.

`CHAPTER_PROVENANCE.md`, `MIGRATION_LEDGER.md`, `RETIRED_SOURCE_CLASSIFICATION.md`, and `SUPERSESSION_MAP.md` agree on this classification and preserve ordinary Git recovery.

## 9. B3+ exclusion audit

The live PDL branch is twenty-one commits ahead of the immutable B2 source. Its later delta contains B3, B4, B5, later DAG revisions, and later handoffs.

None of those later mathematical files or ledger versions is consumed by the candidate.

The candidate does not disposition:

- target-link and target-capacity corrections;
- vertical or horizontal reconfiguration;
- cuts, four-poles, or routing;
- later defect, atom, or localization work.

## 10. Stop-condition audit

No stop condition was triggered.

- no contradiction among B2.1–B2.4 was found;
- no unrecorded self-duality is used in the corrected active theorem;
- no dimension-specific orthogonal claim outside B2.3 was needed;
- the cycle-continuity convention is explicit and consistent;
- no B3+ commit was needed;
- no active later theorem was found to depend essentially on the false universal hierarchy.

Any future packet citing that hierarchy must be re-audited before integration.

## 11. Repository isolation

- `main` remains exactly `960c92b7ff231c78b387894149779083060a75eb`;
- Programme A remains exactly `68715fb29bb4b6555e2bc3e089603c5390d01566`;
- Programme B1 remains exactly `4d7b9c74ea4377a58e219a7c6c3cb569a8229276`;
- the live PDL branch was not modified;
- no branch was deleted or renamed;
- no force-push, rebase, squash, or public-history rewrite occurred;
- no Lean or manuscript repository was changed;
- no publication, release, arXiv, DOI, novelty, or timestamp action occurred.

## 12. Assurance audit

Programme B2 is classified as:

`CURATOR-INTEGRATED / AUTHORIAL B2 PROOF LAYER COMPLETE / MATHEMATICAL CORRECTION INSTALLED`.

This is not independent audit, end-to-end Lean verification, manuscript acceptance, peer review, publication, release, arXiv, DOI disposition, or novelty determination.

The global five-support theorem remains open.

## 13. AC-DIR disposition questions

The candidate leaves these exact decisions to AC-DIR:

1. whether to accept this candidate as the next rolling five-support corpus baseline;
2. whether the correction-aware Audit B scope should be retargeted immediately to this candidate;
3. whether a dedicated source audit should separately record the false packet and its replacement before manuscript work;
4. whether to authorize the next bounded B3 intake from its exact immutable checkpoint;
5. whether later canonical movement should preserve the two-parent B2 source splice;
6. whether any downstream packet known to cite the false hierarchy should receive an explicit repair/audit unit before intake.

No mathematical ambiguity requires pre-disposition escalation.
