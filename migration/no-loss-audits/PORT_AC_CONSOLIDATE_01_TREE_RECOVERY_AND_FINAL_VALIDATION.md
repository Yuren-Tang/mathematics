# PORT-AC-CONSOLIDATE-01 tree, recovery, and final validation

## 1. Exact control

- START: `Yuren-Tang/research-workbench#87` comment `5075948677`;
- writer: `MATH-CUR::chatgpt:6a57882c-55cc-83ed-a9f8-4ce0ed7c4d8d`;
- lease generation: `20260725T005438Z-19153`;
- branch: `curation/affine-cdc-global-rebaseline-v2`;
- exact start tip: `24f777d45693ff7e031dc93137a4aec5b879a7b3`;
- canonical comparison: `main@960c92b7ff231c78b387894149779083060a75eb`;
- receiver: local `PORT-DIR`.

The final branch SHA is recorded in the issue return because a commit cannot contain itself.

## 2. Pre-final ancestry observation

Immediately before this file:

- branch tip: `38617f3059e4215959b3547f4da003ca6194cdcf`;
- ahead of exact start: `20` commits;
- behind exact start: `0`;
- merge base: exactly `24f777d45693ff7e031dc93137a4aec5b879a7b3`;
- changed paths: `18`;
- all changed paths are additions.

This final audit adds one path and one commit. Expected final delta: `21 commits / 19 added paths / 0 deleted or moved paths`.

## 3. Active tree manifest

### Registry schema

1. `registry/schema/mathematical-unit.schema.json`
2. `registry/schema/typed-relation.schema.json`

### Natural units and relations

3. `registry/units/graph-theory/cycle-covers/PORT_AC_CONSOLIDATE_01_UNITS.json`
4. `registry/relations/PORT_AC_CONSOLIDATE_01_RELATIONS.json`
5. `registry/discovery/PORT_AC_CONSOLIDATE_01_DISCOVERY_ADDENDUM.md`

### Project views

6. `registry/views/programme.affine-cdc.json`
7. `registry/views/frontier.five-cdc.json`

### Source manifest and source-to-unit map

8. `sources/manifests/PORT_AC_CONSOLIDATE_01_SOURCE_MANIFEST.json`
9. `migration/source-to-unit-map/PORT_AC_CONSOLIDATE_01_MAP.json`
10. `migration/source-to-unit-map/batches/PORT_AC_01_AC_RL_31EC4A49.json`
11. `migration/source-to-unit-map/batches/PORT_AC_02_AC_PDL_F90A068F.json`
12. `migration/source-to-unit-map/batches/PORT_AC_03_FULL_AUDIT_1E7EE9D1.json`
13. `migration/source-to-unit-map/batches/PORT_AC_04_TERMINAL_AUDIT_C954F222.json`
14. `migration/source-to-unit-map/batches/PORT_AC_05_CHAIN_NEGATIVE_A4F20F05.json`
15. `migration/source-to-unit-map/batches/PORT_AC_06_XI_NEGATIVE_53BE22A0.json`

### Validation and no-loss audits

16. `migration/validate_port_ac_consolidate_01.py`
17. `migration/no-loss-audits/PORT_AC_CONSOLIDATE_01_PASS_A_VALIDATION.md`
18. `migration/no-loss-audits/PORT_AC_CONSOLIDATE_01_EPISTEMIC_PRESERVATION.md`
19. this file.

## 4. Source recovery pointers

| Source | Exact recovery ref | Classification file |
|---|---|---|
| RL | `research/affine-cdc-five-cdc-v1@31ec4a49caf2dbddf2f5e1e2dd3d8a866f3847c8` | `PORT_AC_01_AC_RL_31EC4A49.json` |
| PDL | `proof-development/affine-cdc-rigour-v1@f90a068fbcc81d34850bb53426f4c2efb4cb5388` | `PORT_AC_02_AC_PDL_F90A068F.json` |
| full audit | `audit/affine-cdc-five-cdc-v7-4-1-full-v1@1e7ee9d14608bfdd3524d588d96bfc3470654686` | `PORT_AC_03_FULL_AUDIT_1E7EE9D1.json` |
| terminal audit | `audit/affine-cdc-terminal-exhaustion-v1@c954f2220c082bc3b47821657b7a1164876aeaab` | `PORT_AC_04_TERMINAL_AUDIT_C954F222.json` |
| chain negative | `audit/affine-cdc-component-chain-v1@a4f20f05532c307a3a8f9d98ac4c5162e7b8ad57` | `PORT_AC_05_CHAIN_NEGATIVE_A4F20F05.json` |
| Xi negative | `audit/affine-cdc-xi-co-root-v1@53be22a0f65b85068b11e5f781579618967db9dd` | `PORT_AC_06_XI_NEGATIVE_53BE22A0.json` |

The complete pre-migration corpus remains recoverable at `curation/affine-cdc-global-rebaseline-v2@24f777d45693ff7e031dc93137a4aec5b879a7b3`.

## 5. Registry validation result

Equivalent validation of the committed payloads passed with:

```text
sources=6
substantive_items=80
canonical_units=33
logical_relations=21
discovery_relations=6
unclassified=0
status=PASS
```

The deterministic branch-native validator checks:

- JSON loading;
- exact six-source refs and SHA format;
- packet and item counts;
- unique stable unit IDs;
- every mapped unit reference exists;
- every relation endpoint exists;
- logical/discovery relation types remain disjoint;
- both project views reference existing units;
- five-CDC view remains `OPEN / NO ACCEPTED PROOF`;
- no-delete, no-wholesale-merge, no-main-movement, and captured/unreviewed defaults.

## 6. No-loss and non-upgrade result

- six source packets classified: `6/6`;
- substantive items classified: `80/80`;
- unclassified: `0`;
- negative, failed, withdrawn, heuristic, computation/experiment, explicit model, authorial candidate, open question, and conditional theorem material retained;
- no experiment represented as proof;
- no author-complete packet represented as an independent pass;
- no scoped counterexample generalized to the five-CDC conjecture;
- no conditional suffix used to bridge the open one-atom endpoint interface.

## 7. AC and five-CDC view reconstruction

- `programme.affine-cdc` reconstructs independently established-in-scope units, open frontier, failed/refuted claims, permanent negatives, historical discovery, and legacy compatibility entrypoints.
- `frontier.five-cdc` reconstructs the exact first missing edge, conditional downstream chain, failed v7.4.1 proof, external-review questions, and three permanent negative boundaries.

Neither view owns or duplicates mathematical truth.

## 8. Mutation and isolation audit

No pre-existing `projects/**` file was deleted, moved, or modified by this intake. No RL, PDL, audit, Lean, manuscript, release, tag, DOI, arXiv, publication, workflow, or other repository/branch surface was written.

No wholesale merge, rebase, squash, force-push, branch deletion, or history rewrite occurred. `mathematics:main` was rechecked as identical to `960c92b7ff231c78b387894149779083060a75eb` before this final file.

## 9. Final readiness

`READY FOR INDEPENDENT SOURCE-FIDELITY / EPISTEMIC-NON-UPGRADE AUDIT`.

This readiness is a curation/integration status only. Five-CDC remains open, and canonical movement remains a later Portfolio Owner control point.
