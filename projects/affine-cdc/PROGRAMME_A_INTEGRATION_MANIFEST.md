# Programme A curation manifest

## 1. Exact workspace

- repository: `Yuren-Tang/mathematics`;
- canonical base: `main@960c92b7ff231c78b387894149779083060a75eb`;
- immutable source: `proof-development/affine-cdc-rigour-v1@8bee16780b549f51e1f29343671a059961ec4172`;
- curation branch: `curation/affine-cdc-programme-a-v1`.

The exact final candidate SHA is recorded in the authoritative return in `Yuren-Tang/research-workbench` issue #24. A commit cannot contain its own SHA without circularity.

## 2. Intake boundary

The source checkpoint is seventeen commits ahead of the base and zero behind. The source delta contains exactly:

- eleven proof-development dossiers A0–A10;
- `proof-development/OBLIGATION_DAG.md`.

The intake does not consume B1 checkpoint `778b09ac8260192e022f512f24cdef1d04871f37` or any later live-branch commit.

## 3. History-preserving integration

The curation branch was created from the exact canonical base and then fast-forwarded, without force, to the immutable source checkpoint. Therefore:

- all Programme A commits remain exact ancestors;
- intermediate unit checkpoint SHAs remain recoverable;
- no cherry-pick reconstruction, squash, rebase, or history rewrite was used;
- the live proof-development branch was not modified;
- `main` was not moved.

## 4. Active mathematics created

The preferred Programme A reading surface is:

1. `complete-cdc/foundations-expansion-and-flow.md`;
2. `complete-cdc/affine-compatibility-and-extraction.md`;
3. `complete-cdc/collapse-decomposition-and-assembly.md`.

The directory entrypoint is `complete-cdc/README.md`.

These chapters integrate the complete theorem by natural dependency rather than proof-development unit chronology.

## 5. Provenance and assurance control

New control files are:

- `PROGRAMME_A_INTEGRATION_MAP.md`;
- `PROGRAMME_A_ASSURANCE_BOUNDARY.md`;
- this manifest.

The exact A0–A10 dossiers and `OBLIGATION_DAG.md` remain in the current tree under `proof-development/` as authorial source, repair, and audit provenance.

## 6. Material current-best changes

The integrated corpus now records:

1. the natural hypothesis as finite active edge set plus no singleton cut;
2. exact equivalence with absence of nonloop bridges;
3. intrinsic half-edge boundary parity as the loop-aware notion;
4. once-per-edge vertex parity as a loopless representation adapter only;
5. exact loop deletion and forced two-occurrence reinsertion;
6. a closed port-cycle expansion and collapse interface;
7. Seymour 1981 as the sole external non-elementary logical input;
8. internal equal-order finite-group flow counting and transport;
9. the pair complex as compatibility centre but not graph/dart support data;
10. the invariant quadratic-Lagrangian compatibility proof;
11. explicit graph-level indexed support extraction and occurrence multiplicity;
12. collapse of cut-even supports rather than circuits;
13. one terminating circuit decomposition after collapse;
14. complete boundary-case assembly.

## 7. Source and citation boundary

Seymour’s theorem is used as an external theorem with exact article and DOI recorded in the corpus.

Tutte’s equal-order flow work remains cited as historical provenance. Programme A’s internal flow-count theorem removes exact Tutte page localization from the logical obligation list.

## 8. Assurance non-upgrades

This intake does not upgrade:

- independent-review status;
- Lean or other formal-verification status;
- manuscript status;
- peer-review or publication status;
- release, arXiv, DOI, or timestamp status.

The source states `READY-FOR-CURATOR`, an authorial proof-development state. The candidate becomes Curator-integrated authorial mathematics, not independently audited mathematics.

## 9. No-loss and isolation audit

The final audit must verify:

- source checkpoint is an ancestor of the candidate;
- candidate is a descendant of the exact canonical base;
- the eleven dossiers and DAG remain present and byte-identical to the immutable source;
- no B1 file or later PDL delta appears;
- `main` remains exactly `960c92b...`;
- the live proof-development branch is not moved by this work;
- no Lean, manuscript, release, DOI, or publication surface changes.

The authoritative return records the exact comparison results.

## 10. Proposed downstream relationship

The candidate is intended for AC-DIR disposition as the next fixed complete-CDC corpus state. If AC-DIR accepts it, the natural next steps are:

1. decide whether to authorize a history-preserving fast-forward of `main` to the candidate;
2. retarget independent Audit A to the exact accepted candidate;
3. route any audit defects back to AC-PDL;
4. later project the same accepted interfaces into Lean and Paper A.

No such default-branch movement or downstream status change is performed by this manifest.