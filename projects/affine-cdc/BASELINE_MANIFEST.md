# AffineCDC rolling-baseline manifest

This manifest records the temporary integration candidate created by `AC-BASELINE-01`. It is a provenance and synchronization document, not an authorization to move the default branch.

## 1. Exact refs

### Previous canonical default

`Yuren-Tang/mathematics:main@749e0579581fcc838685138b3582f4de306b8e72`

### Accepted outer-shell MP2 source

`Yuren-Tang/mathematics:promotion/affine-cdc-outer-shell-v1@0927011177cabac20f06a57fa5e57476d6f13dee`

### Five-support public frontier checkpoint

`Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`

### Temporary integration branch

`Yuren-Tang/mathematics:integration/affine-cdc-best-baseline-dad218dd-v1`

### History-preserving merge commit

`081b17e23c4c64dc29d9266378c6196903d01b80`

### Navigation state before this manifest

`0b0a12848b1534edb46a571e5a447e665508305e`

### Final candidate tip

The final candidate tip is the branch head containing this manifest. Its exact immutable SHA is recorded in the authoritative `[RETURN AC-BASELINE-01/CURATOR]` comment in `Yuren-Tang/research-workbench` issue #24.

A Git commit cannot contain its own SHA without a circular definition. The branch name plus the external exact return therefore forms the final-tip record; this file records all non-self-referential parents and predecessor tips.

## 2. Merge parents and ancestry

The ordinary non-squash merge was created through PR #3 with exact parents:

1. first parent: `0927011177cabac20f06a57fa5e57476d6f13dee`;
2. second parent: `dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`.

Required ancestry properties:

- all three MP2 commits remain ancestors of the candidate;
- all eighty-two public five-support source commits remain ancestors of the candidate;
- no cherry-pick reconstruction, squash, rebase, or history rewrite was used;
- the two source lines have exact common base `749e0579581fcc838685138b3582f4de306b8e72`;
- the merge had no content conflict.

The final return supplies the post-navigation comparison checks for both parents and the old default base.

## 3. Source content included

### MP2 delta

Exactly three non-research AffineCDC paths:

1. `projects/affine-cdc/reduction/outer-shell-and-binary-flow.md` — added;
2. `projects/affine-cdc/FORMAL_STATUS.md` — modified;
3. `projects/affine-cdc/PUBLICATION_PROGRAM.md` — modified.

These files retain the exact MP2 source content and status labels.

### Five-support checkpoint

The checkpoint contributes seventy-eight public programme files under:

`projects/affine-cdc/research/`

They are retained as exact source files with their original commits, internal status declarations, corrections, counterexamples, finite certificates, and open obligations. The Curator did not rewrite the eighty-two-commit history into a monograph.

### Curator navigation delta

Exactly four new corpus-level files:

1. [`CURRENT_BEST.md`](CURRENT_BEST.md);
2. [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md);
3. [`SUPERSESSION_MAP.md`](SUPERSESSION_MAP.md);
4. [`BASELINE_MANIFEST.md`](BASELINE_MANIFEST.md).

No source mathematical file was edited during navigation staging.

## 4. Commit and file accounting

Relative to `main@749e057...`, the candidate contains:

- `3` MP2 source commits;
- `82` five-support source commits;
- `1` ordinary merge commit;
- `4` Curator navigation commits;
- expected total: `90` commits ahead, `0` behind.

The expected path delta is:

- `3` MP2 paths;
- `78` public five-support research paths;
- `4` navigation paths;
- expected total: `85` changed paths relative to the old default base.

The authoritative return records the actual final comparison and stops if these counts or paths differ.

## 5. Source-to-destination map

| Source | Destination in candidate | Transfer |
|---|---|---|
| MP2 outer-shell source `092701117...` | same three canonical AffineCDC paths | Exact history and file content preserved through first merge parent. |
| Five-support checkpoint `dad218dd...` | same `projects/affine-cdc/research/` paths | Exact eighty-two-commit source history preserved through second merge parent. |
| Private notebook/recovery evidence | no wholesale destination | Mapped as evidence only; public claims rely on public packets or explicit finite-certificate boundaries. |
| Curator synthesis | four root-level AffineCDC navigation files | New mapping/status prose only; no theorem or source edit. |

Detailed current-use relations are in [`SUPERSESSION_MAP.md`](SUPERSESSION_MAP.md).

## 6. Private evidence mapped but omitted

The private computation/recovery line remains:

`Yuren-Tang/research-workbench:research/affine-cdc-five-cdc-notebook-v1`

It is not copied into this public candidate. Its roles are limited to:

- exact computation provenance;
- recovery evidence;
- cross-checking public finite certificates.

The incomplete rescued combined verifier remains `CODE-PARTIAL`. No hidden notebook state or hidden reasoning is treated as a public theorem source.

## 7. Status non-upgrades

This integration makes no upgrade on any assurance axis.

- **Mathematical completeness:** MP2 retains its Director-accepted paper-level status; five-support claims retain their individual universal, finite, counterexample, partial, conjectural, false, superseded, or open classifications.
- **Independent review:** no line-by-line independent audit of the full eighty-two-commit checkpoint is created by this integration.
- **Formal status:** no outer-shell or five-support result acquires Lean status.
- **Source status:** exact public sources and historical sources remain distinct.
- **Peer review/publication:** no peer-review, novelty, manuscript, arXiv, release, or DOI status changes.
- **Global theorem:** no global five-cycle-double-cover theorem is manufactured.

The controlling trust boundary is stated in [`CURRENT_BEST.md`](CURRENT_BEST.md) and [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md).

## 8. Historical and supersession preservation

The candidate preserves:

- old `main@749e057...` as an exact ancestor/common base;
- M1, M2, adaptive-ordering, binary-eight-flow, MP1, and MP2 source relations;
- every public five-support source commit;
- materially corrected and false overstrong formulations as historical sources;
- exact controlling-successor links in [`SUPERSESSION_MAP.md`](SUPERSESSION_MAP.md).

No branch is deleted or renamed by this workstream.

## 9. Live research synchronization design

No live-research synchronization is performed now.

Only after a later owner decision moves `main` to an accepted integration tip may synchronization occur:

1. verify the new exact `main`;
2. if `research/affine-cdc-five-cdc-v1` still equals `dad218dd...`, fast-forward it to the new baseline;
3. if it has advanced, merge the new `main` into the live research branch without rebase or history rewrite;
4. continue research from the synchronized branch;
5. set the next exact baseline intake trigger;
6. do not delete source branches in the same operation.

This design is recorded only; it is not authorized for execution by `AC-BASELINE-01`.

## 10. Priority-attestation coverage

Current coverage consists of public Git/GitHub commit ancestry, exact source SHAs, issue-based branch ownership, and the history-preserving merge record.

A separate timestamp or priority-attestation workflow is:

`NOT IMPLEMENTED / NOT AUTHORIZED IN AC-BASELINE-01`.

No automated timestamp workflow, release, tag, DOI mutation, or external priority claim is created here. The private notebook is mapped but does not enlarge public attestation coverage.

## 11. Review and movement gates

The candidate now waits for staged review:

1. `AffineCDC — Research Lead`: fidelity review of `CURRENT_BEST.md` and `FRONTIER_STATUS.md`, and report of any live drift;
2. `AffineCDC — Director`: theorem/counterexample/status review;
3. `Research Portfolio — Director`: ancestry, no-loss, lifecycle, and owner-facing integration review;
4. later owner decision: only then may a separate movement packet be prepared.

Completion of this branch does **not** authorize movement of `main`.