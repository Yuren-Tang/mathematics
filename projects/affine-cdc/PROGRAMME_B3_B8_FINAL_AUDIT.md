# Programme B3–B8 final curation audit

## 1. Exact controls

- authoritative packet: `Yuren-Tang/research-workbench#24`, comment `5019639996`;
- integration base: `curation/affine-cdc-programme-b2-v1@08b662ecc31848456b9904f4d5b85c3801d090a1`;
- candidate branch: `curation/affine-cdc-programme-b3-b8-v1`;
- exact source splice: `4dadc7add4743d7da63e28d93806c8d76529c07b`.

The exact final candidate SHA is recorded in the authoritative issue #24 return.

## 2. Exact unit checkpoints

| Unit | Checkpoint | Retained state |
|---|---|---|
| B3 | `d806168bb579dbc13f267f44f631e07de909b706` | `READY-FOR-CURATOR / PROVENANCE-REPAIRED` |
| B4 | `345074690b7a8658c1208ae84f10d709f8b74bcf` | `READY-FOR-CURATOR / FRONTIER-EXPLICIT` |
| B5 | `274970ef9c56cafdbfceeed3c0cc08238d3dfd40` | `READY-FOR-CURATOR / FRONTIER-LOCALIZED` |
| B6 | `404f7511f16d1225e066a91842a57e2084943c72` | `READY-FOR-CURATOR / MATHEMATICAL-CORRECTION / AC-RL-GAPS-EXPLICIT` |
| B7 | `164f7655f9ec7c0e0a73d49303cf66230fb26487` | `READY-FOR-CURATOR / AC-RL-GAPS-EXPLICIT / GLOBAL-COMPOSITION-OPEN` |
| B8 | `989cb002598fd91786029be201c2747c697bb476` | `READY-FOR-CURATOR / ASSURANCE-NORMALIZED` |

The source splice has the B2 base as first parent and all six checkpoints as additional ordered parents.

## 3. Source-tree audit

The splice tree imports exactly:

- four B3 dossiers;
- four B4 dossiers;
- four B5 dossiers;
- five B6 dossiers;
- three B7 dossiers;
- one B8 assurance ledger;
- the B8 checkpoint `OBLIGATION_DAG.md`.

Total: twenty-one unit dossiers plus one DAG path.

No `PROGRAMME_B*_CURATOR_HANDOFF.md` file was copied into the candidate. Handoffs remain routing/control sources only.

## 4. Source-blob audit

Relative to the exact source splice, the Curator delta modifies nineteen canonical corpus/control paths and no file under `projects/affine-cdc/proof-development/`.

Therefore all twenty-one dossiers and the B8 DAG retain exact source blob identity.

## 5. Candidate-delta audit

Before this audit file, the exact B2 base-to-candidate comparison was:

- `37` commits ahead;
- `0` behind;
- `41` changed paths;
- `22` exact source paths;
- `19` Curator corpus/control paths.

The source-splice-to-candidate comparison was:

- one Curator commit ahead;
- zero behind;
- exactly nineteen canonical paths;
- no proof-development path.

This final audit adds one canonical control path only.

## 6. B3 audit

The active corpus now:

- keeps `T_g^{(1)}` and `J_g` distinct;
- preserves exact common-link, capacity, and eight-vertex theorems;
- classifies unused-root/core/ideal-pivot results as factorable;
- keeps flower numerical data on the certificate axis;
- corrects the all-parallel matching representative to `\{01,23,45\}` while retaining orbit sizes `28,168,224`.

No valid recovered target packet is falsely superseded.

## 7. B4 audit

The active corpus now records:

- exact vertical torsor and disconnected reduced gauge code;
- gauge/Petrial correspondence;
- connected-cycle adjacency;
- disconnected switch decomposition as a path;
- support pivots as special connected switches with one explicit new lift;
- recomputation of the new fibre;
- internal composite linear image versus connected-neighbour subset;
- external composite reslicing versus connected adjacency;
- `7737` composite endpoints versus `2801` one-step neighbours.

No universal flow connectedness or good-state escape theorem is claimed.

## 8. B5 audit

The active interface chapter preserves theorem-level:

- cubic local support law;
- cyclic three-cut gluing;
- ten four-pole states and `640` ordered assignments;
- exact profile-intersection gluing;
- cap forcing;
- Kempe pairing alignment;
- routing weights;
- uniform-routing elimination.

It retains mismatch kernels, policy tables, Type T/H classification, monodromy, and small census as finite results. Cap forcing is not upgraded to full-cap containment, and abstract transitions are not path-realizability theorems.

## 9. B6 correction audit

Unconditional active results retain individual-loop holonomy, root fibres, genuine path-family formulas, Tait escape, DDD atom triality, unique bad route, and local conditional defect geometry.

The following are no longer active unconditionally:

1. physical BBD group/common-origin chain;
2. nontrivial fixed-terminal defect-minimal forest.

They are controlled by:

- `AC-RL-BBD-GROUPOID-CLOSURE`;
- `AC-RL-BBD-VARIATION-SLICE`.

The old assertions were removed from the controlling holonomy, frontier, architecture, dependency, current-state, formal-status, provenance, and supersession surfaces.

## 10. B7 audit

The candidate integrates:

- rank-one impossibility;
- rank-two Tait/root-triangle escape;
- full-rank flat/nonflat curvature dichotomy;
- exact affine-potential edge law;
- common scalar-sheet cut with odd terminal parity.

It does not claim source-graph localization, boundedness, connectedness, composition-safe factorization, physical `D_8` identification, or bounded transfer semantics.

Exact open returns:

- `AC-RL-TYPE-T-SERIALISATION`;
- `AC-RL-FLAT-POTENTIAL-INTERFACE`;
- `AC-RL-COMMON-CUT-LOCALISATION`;
- `AC-RL-TYPE-H-COMMON-WITNESS`.

Together with the two B6 gaps, six exact AC-RL obligations control the frontier.

## 11. B8 assurance audit

The active finite layer uses:

- `F-PROVED`;
- `F-CERT-PUBLIC`;
- `F-CERT-PRIVATE`;
- `F-CENSUS`;
- `CODE-PARTIAL`;
- `AFFECTED`.

Correction propagation is explicit for BBD monodromy, defect/Petersen tables, orthogonal tables, switch populations, and the matching display.

B8 is not independent mathematical review, formal verification, or reproducibility upgrade.

## 12. B9+ exclusion audit

The live PDL branch is seven commits ahead of B8 checkpoint `989cb002...`. Its later delta contains:

- `AC_PD_B9_CORRECTED_GLOBAL_FRONTIER_ASSEMBLY.md`;
- Programme A Audit A repair material;
- later `OBLIGATION_DAG.md`;
- B8/B9 and Programme A repair handoffs.

None of these paths is consumed by the candidate. No B9 theorem, correction, or moving-branch DAG state is dispositioned here.

## 13. Repository isolation

Verified unchanged:

- `main@960c92b7ff231c78b387894149779083060a75eb`;
- Programme A branch `68715fb29bb4b6555e2bc3e089603c5390d01566`;
- Programme B1 branch `4d7b9c74ea4377a58e219a7c6c3cb569a8229276`;
- Programme B2 branch `08b662ecc31848456b9904f4d5b85c3801d090a1`.

The live PDL branch was not modified. No force-push, rebase, squash, branch deletion, public-history rewrite, Lean/manuscript mutation, release, publication, arXiv, or DOI action occurred.

## 14. Stop-condition audit

No packet stop condition was triggered.

- no contradiction among exact B3–B8 units was found after applying B6 corrections;
- no later B9 commit was required;
- no unrecorded source or self-duality choice was introduced;
- finite evidence was not needed as an unstated universal theorem premise;
- the six genuine mathematical gaps were retained rather than guessed through;
- the later workspace consistency review did not supersede the controlling intake packet.

## 15. Assurance state

The integrated candidate is classified as:

`CURATOR-INTEGRATED / B3–B5 AUTHORIAL THEOREM LAYERS / B6 MATHEMATICAL CORRECTION INSTALLED / B7 GLOBAL COMPOSITION OPEN / B8 ASSURANCE NORMALIZED`.

The global five-support theorem remains open. No independent-review, end-to-end Lean, manuscript, peer-review, publication, release, arXiv, DOI, novelty, or timestamp status is created.

## 16. AC-DIR disposition questions

1. accept or revise this candidate as the next rolling five-support corpus baseline;
2. decide whether Audit B should be retargeted to the correction-aware candidate;
3. route the six exact AC-RL gaps and determine their priority/order;
4. decide whether B9 intake should wait for one of those gaps or be consumed only as a corrected frontier map;
5. determine whether Programme A audit-repair material receives a separate intake, preserving the fixed Audit A candidate until explicit disposition;
6. authorize any future canonical movement separately, preserving the multi-checkpoint source splice if accepted.

No mathematical ambiguity requires pre-disposition escalation.