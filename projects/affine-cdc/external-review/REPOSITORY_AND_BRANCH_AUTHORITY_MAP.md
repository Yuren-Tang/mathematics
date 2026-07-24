# Repository and branch authority map for external reviewers

## 1. Start here

Current mixed-assurance corpus candidate:

`Yuren-Tang/mathematics:curation/affine-cdc-global-rebaseline-v2`

Exact base:

`curation/affine-cdc-programme-a-b1-b8-source-fidelity-v1@f4d6f801fac69746ca0b2ce9351735a43c79b482`.

This branch organizes status and provenance. It does not claim to be an independently accepted proof of the five-support theorem.

## 2. Exact theorem and candidate sources

| Role | Exact ref | Use |
|---|---|---|
| source-fidelity base | `f4d6f801...` | stable Programme A/B1--B8 corpus |
| source-fidelity audit | `ea8ec33d...` | independent assurance of B2/B8 repair |
| OR1 candidate | `e6af564...` | orientation-obstruction theorem packet |
| OR1 audit | `6c20cead...` | independent verification subject to D1--D6 |
| old PDL full draft | `1f57422...` | historical failed candidate and source of audited local units |
| old core audit | `00b4b376...` | accepts R0/R1/R2.1/R2.2; blocks R2.3/R2.4 |
| old return audit | `492eea3e...` | accepts/repairs finite seams and genealogy; blocks old rank |
| old shell audit | `a94c4021...` | accepts outer shell; blocks cap assembly |
| v9 RL source | `02b37476...` | active authorial component-chain candidate |
| `Xi` audit | `53be22a0...` | verified subtheorems and same-arc counterexample |
| PDL v7.4 start | `fee97446...` | #80 reconstruction workspace boundary |

Full SHAs appear in `../CROSS_REPOSITORY_AUTHORITY_MAP.md`.

## 3. Active workbench issues

- #62 — global rebaseline control and Curator return;
- #80 — PDL component-chain reconstruction;
- #81 — focused independent component-chain review.

Historical audit controls:

- #68 — old structural/core audit;
- #69 — old contextual-return audit;
- #70 — old cap/shell audit;
- #71 — synthesis audit not launched;
- #78 — `Xi` co-root audit and exact counterexample.

Issue chronology is not required for mathematical reading. Use it only to confirm role, scope and exact return refs.

## 4. Lean authority

`Yuren-Tang/affine-cdc:main@ebd7098a7a8b824e8c0a511d3c71f61705672aa8`

is a partial machine-checked anchor. It does not check the v9 component chain, universal five-support theorem, full OR1 orientation packet or the global mixed-assurance spine.

## 5. Manuscript and publication authority

Paper/manuscript branches, releases, tags, arXiv and DOI records are projections or archival records. They are not inputs to the current theorem-status decision unless an exact mathematical checkpoint is separately identified.

## 6. Branch discipline

- Do not review moving RL/PDL tips by default.
- Do not combine assertions from different snapshots unless the integration map names the interface.
- Do not treat an audit result as applying outside its exact candidate and units.
- Do not merge the candidate into `main` as part of review.
- Record the exact source and audit SHA for every verdict.

## 7. Suggested external-review branch

A future external reviewer should branch from the final SHA of `curation/affine-cdc-global-rebaseline-v2` and add reports only under a dedicated audit/review directory. The Curator corpus itself should remain immutable review input.