# Repository and branch authority map for external reviewers

## 1. Current corpus

`Yuren-Tang/mathematics:curation/affine-cdc-global-rebaseline-v2`

Exact base:

`curation/affine-cdc-programme-a-b1-b8-source-fidelity-v1@f4d6f801fac69746ca0b2ce9351735a43c79b482`.

This branch is a mixed-assurance status/provenance corpus, not a proof acceptance.

## 2. Exact authorities

| Role | Exact ref | Current use |
|---|---|---|
| source-fidelity base | `f4d6f801fac69746ca0b2ce9351735a43c79b482` | stable Programme A/B1--B8 base |
| source-fidelity audit | `ea8ec33d49294ac31a53f46aed7a62c7b9b81908` | independent B2/B8 assurance |
| OR1 candidate/audit | `e6af5645107d0f21ac6c262c63a1db5dab8f0fd1` / `6c20cead05bd12b1027c349c4f259b117d8e0861` | verified subject to D1--D6 |
| old PDL full draft | `1f57422e0e415d8902d56eb294183815c0a0b640` | failed candidate and source of audited local units |
| old core audit | `00b4b376190500a005bf3c3a4bfd3f6429864175` | accepts R0/R1/R2.1/R2.2 |
| old return audit | `492eea3ea3d9d4540a706f42524e1b03f06e66bf` | accepts repaired local seams/genealogy; rejects old rank |
| old shell audit | `a94c4021b0bf8160806c4a64601be492196b472a` | accepts conditional outer shell; rejects cap assembly |
| v9 RL source | `02b37476198e9eaa2b4cd8d2a2edd76782bdcd49` | failed general-chain candidate provenance |
| PDL v7.4 reconstruction | `e36ba22f09e3a9fc6358f3b03615f8fde6c00d96` | complete failed reconstruction provenance |
| `Xi` audit | `53be22a0f65b85068b11e5f781579618967db9dd` | verified local arithmetic and same-arc counterexample |
| component-chain audit | `a4f20f05532c307a3a8f9d98ac4c5162e7b8ad57` | material false-scope verdict, local row assurance and third-terminal witness |

## 3. Workbench controls

- #62 — current global rebaseline and Curator return;
- #80 — completed PDL reconstruction, exact return `e36ba22...`;
- #81 — completed independent chain audit, exact return `a4f20f05...`;
- #68--#70 — old fixed-candidate audits;
- #71 — synthesis audit not launched;
- #78 — `Xi` audit.

Issues assign and record work. Mathematical authority comes from the exact referenced source/audit files.

## 4. Lean

`Yuren-Tang/affine-cdc:main@ebd7098a7a8b824e8c0a511d3c71f61705672aa8`

is a partial machine-checked anchor. It does not check the failed general component-chain theorem, a repaired terminal-exhaustion theorem, the global five-support result or the complete OR1 packet.

## 5. Manuscript/publication

Manuscript branches, releases, tags, arXiv and DOI records are projections or archival surfaces. They do not upgrade theorem assurance.

## 6. Review discipline

- freeze every source and audit by exact SHA;
- do not combine moving RL/PDL tips;
- do not generalize local audit acceptance beyond its scope;
- retain both the `Xi` and third-terminal-path witnesses in every repair review;
- do not merge into `main` during review;
- record source, repair and verifying audit separately.

## 7. Next review object

The next mathematical review should target a future exact repair of

`AC-FRONTIER-COMPONENT-CHAIN-TERMINAL-EXHAUSTION`,

not re-audit the unchanged failed theorem. A separate independent integration audit may meanwhile review this rebaseline's assurance/provenance fidelity.