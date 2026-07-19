# AffineCDC source-recovery and no-loss audit

This audit verifies that current-tree retirement of the five-support discovery packets does not lose mathematical source, public priority, ancestry, or recoverability.

## 1. Exact source lineage

The public five-support checkpoint is:

`dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`.

The integration base is:

`7a166d2eb5642ec967f640323488e49f1c2ad5d4`.

Direct comparison verifies that the integration base is eight commits ahead of the checkpoint and zero commits behind. The merge base is exactly `dad218dd...`. Therefore every checkpoint commit and blob is an ancestor of the curation branch.

The canonical default ancestor remains:

`main@749e0579581fcc838685138b3582f4de306b8e72`.

The accepted outer-shell source remains:

`0927011177cabac20f06a57fa5e57476d6f13dee`.

## 2. Exact source population

Comparing `main@749e057...` with `dad218dd...` yields exactly:

- `82` source commits;
- `78` added files under `projects/affine-cdc/research/`;
- no source-file deletion or rename inside that checkpoint line.

The complete seventy-eight-file population is enumerated in [`RETIRED_SOURCE_CLASSIFICATION.md`](RETIRED_SOURCE_CLASSIFICATION.md). Its class count is:

$$
39+10+18+10+1=78.
$$

The final audit corrected one preliminary ledger omission:

`FIVE_CDC_SUPPORT_CYCLE_PIVOT_AND_FLOW_RECONFIGURATION_V1.md`.

It is now mapped to `five-support/gauge-and-reconfiguration.md` and included in the retired-source accounting.

## 3. Recovery procedures

### Recover one source body

```text
git show dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c:projects/affine-cdc/research/FILE
```

### Restore one packet into a worktree without rewriting history

```text
git restore --source=dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c -- projects/affine-cdc/research/FILE
```

### Inspect the complete historical source surface

```text
git ls-tree -r --name-only dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c projects/affine-cdc/research
```

### Recover discovery chronology

```text
git log --reverse -- projects/affine-cdc/research
```

### Compare a retired packet with its active successor

Use `git show` at `dad218dd...` for the packet and the final curation SHA for the successor chapter named in [`CHAPTER_PROVENANCE.md`](CHAPTER_PROVENANCE.md).

These are ordinary read or branch-local restore operations. No force-push, rebase, public-history rewrite, branch deletion, release, or DOI action is required.

## 4. No-loss criteria

A source packet is retired only after all of the following hold:

1. its exact commit and path are known;
2. the checkpoint containing it is an ancestor of the candidate;
3. its current mathematical role has a named successor;
4. independent proof value, finite evidence, counterexample, correction, or open boundary is preserved in the active corpus;
5. assurance status is not silently upgraded;
6. the source body remains recoverable with one exact Git command.

All seventy-eight packets satisfy these criteria.

## 5. Current-value preservation

The active corpus retains:

- controlling definitions and theorem statements;
- preferred proofs and proof syntheses;
- independent singular, Schur, stress/Fourier, cographic, surface, interface, and holonomy proof families;
- exact finite counts used by the theory;
- explicit counterexample roles and negative boundaries;
- the BBD/DDD distinction and the current localisation frontier;
- the incomplete-verifier `CODE-PARTIAL` boundary.

What leaves the current tip is duplicate discovery-order exposition, superseded partial synthesis, and packet-local repetition.

## 6. Control-file recovery

`BASELINE_MANIFEST.md` is also retired from the current tip. It records the temporary `AC-BASELINE-01` integration state and is superseded by:

- [`RECONSTRUCTION_MANIFEST.md`](RECONSTRUCTION_MANIFEST.md);
- [`ACTIVE_MATHEMATICAL_SURFACE.md`](ACTIVE_MATHEMATICAL_SURFACE.md);
- this recovery audit.

Its exact historical body remains recoverable from any ancestor containing it, including `7a166d2eb5642ec967f640323488e49f1c2ad5d4`.

## 7. Source branches and default branch

This finalization does not move or delete:

- `main`;
- `research/affine-cdc-five-cdc-v1`;
- the outer-shell source branch;
- the integration branch;
- any historical commit or tag.

Current-tree deletion affects only the dedicated curation branch. Default-branch movement remains an owner-authorized operation.

## 8. Recovery conclusion

The candidate is history-preserving and source-complete. The active tree may therefore omit the seventy-eight packets and obsolete baseline manifest without mathematical or priority loss.

The final authoritative return records the exact candidate SHA and verifies its relationship to `main` and the source checkpoint.