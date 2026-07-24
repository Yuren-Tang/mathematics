# AC-CORPUS-V2 source recovery and no-wholesale audit

## 1. Base integrity

The branch was created exactly from

`curation/affine-cdc-programme-a-b1-b8-source-fidelity-v1@f4d6f801fac69746ca0b2ce9351735a43c79b482`.

The base already contains the complete source-fidelity repair. This rebaseline does not rewrite its four imported PDL source blobs, packet list, B8 classes or Programme A/B1/B3--B8 chapters.

Independent base assurance is at

`audit/affine-cdc-b2-b8-source-fidelity-reaudit-v1@ea8ec33d49294ac31a53f46aed7a62c7b9b81908`.

## 2. Exact selected external inputs

### OR1

- candidate `e6af5645107d0f21ac6c262c63a1db5dab8f0fd1`;
- audit `6c20cead05bd12b1027c349c4f259b117d8e0861`;
- status: verified subject to `OR1-D1`--`OR1-D6`.

Only theorem/status summaries and exact pointers are integrated. The OR1 candidate tree and audit reports are not merged.

### Old full-draft audit epoch

- PDL candidate `1f57422e0e415d8902d56eb294183815c0a0b640`;
- audit map `2679f098e6c596083d671a67d2630d5c58c6280f` as checklist only;
- core audit `00b4b376190500a005bf3c3a4bfd3f6429864175`;
- contextual-return audit `492eea3ea3d9d4540a706f42524e1b03f06e66bf`;
- shell audit `a94c4021b0bf8160806c4a64601be492196b472a`;
- synthesis audit #71 not launched because the candidate was materially blocked.

Accepted units and negative findings are integrated claim by claim. The PDL candidate and audit branches are not merged.

### v9 repair epoch

- exact RL source `02b37476198e9eaa2b4cd8d2a2edd76782bdcd49`;
- PDL start `fee97446ee8b99f07740f394e99ef4a2ecc3e40e`;
- permanent `Xi` audit `53be22a0f65b85068b11e5f781579618967db9dd`;
- issues #80 and #81 are active status switches.

The Curator reads exact v9 theorem and control files and writes a new synthesis. No `projects/affine-cdc/research/**` or `proof-development/**` source file from this epoch is copied into the branch.

## 3. Historical ancestry reconstruction

The RL line from `936eb8c4...` to rollover `5514b8ef...` adds the earlier weld, strip, annulus, Pachner, routing and contextual-return mechanisms. The line from `5514b8ef...` to v9 `02b374...` adds the first-cancellation, state-walk, prescribed-parent, `Omega`, `Xi`, zero-parent and component-chain epochs.

`COMPONENT_CHAIN_ANTECEDENT_MAP.md` records the exact mathematical relation. It does not infer authority from chronological proximity.

## 4. Packet and source-fidelity preservation

The historical packet population remains:

$$
39\text{ theorem/mechanism}
+10\text{ alternate proof}
+18\text{ finite}
+10\text{ correction}
+1\text{ synthesis}
=78.
$$

The valid fixed-dimensional orthogonal packet remains among the thirty-nine theorem/mechanism packets. The source-unreconstructed arbitrary-rank tower remains a non-packet proposition and is outside the count.

No source body is deleted, renamed or assigned a false packet class.

## 5. No-wholesale-import verification

The integration method is:

```text
exact source read
→ theorem/defect extraction
→ assurance assignment
→ provenance and supersession entry
→ new Curator synthesis.
```

It is not:

```text
merge source branch
→ inherit all files and statuses.
```

Excluded wholesale trees:

- RL `research/affine-cdc-five-cdc-v1`;
- PDL `proof-development/affine-cdc-rigour-v1`;
- all audit branches;
- `Yuren-Tang/affine-cdc` Lean tree;
- manuscript/Paper A trees.

## 6. Recovery commands

Representative exact recovery forms:

```text
git show 02b37476198e9eaa2b4cd8d2a2edd76782bdcd49:projects/affine-cdc/research/FIXED_CHANNEL_COMPONENT_CHAIN_ROOT_NNI_THEOREM_V1.md

git show 53be22a0f65b85068b11e5f781579618967db9dd:audit/affine-cdc-xi-co-root-v1/AUDIT_REPORT.md

git show ea8ec33d49294ac31a53f46aed7a62c7b9b81908:audit/affine-cdc-b2-b8-source-fidelity-reaudit-v1/DEFECT_AND_CANONICAL_READINESS_LEDGER.md
```

The exact path may differ for old audit deliverables listed in their issue returns; the branch/SHA remains the controlling locator.

## 7. Status noninheritance

The following implications are invalid:

- descendant commit implies theorem stronger or correct;
- PDL reconstruction implies independent acceptance;
- audit branch presence implies every parent claim accepted;
- finite certificate implies universal theorem;
- Lean partial anchor implies prose theorem formalized;
- manuscript projection implies mathematical authority;
- Curator integration implies canonical promotion.

## 8. Final source-fidelity state

This branch preserves a single recoverable line:

```text
source body and discovery history
→ exact authorial theorem/candidate
→ exact independent audit finding
→ current Curator assurance class
→ current consumer or supersession.
```

No source is erased and no failed proof is allowed to masquerade as an active theorem.