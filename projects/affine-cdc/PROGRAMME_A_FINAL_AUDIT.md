# Programme A final curation audit

## 1. Exact refs

- canonical base: `main@960c92b7ff231c78b387894149779083060a75eb`;
- immutable mathematical source: `8bee16780b549f51e1f29343671a059961ec4172`;
- control handoff: `proof-development/PROGRAMME_A_CURATOR_HANDOFF.md`, read from the live PDL branch as a routing document only;
- candidate branch: `curation/affine-cdc-programme-a-v1`.

The exact final candidate SHA is recorded in the authoritative issue #24 return.

## 2. Source-boundary audit

The immutable source is seventeen commits ahead of the canonical base and zero behind. Its mathematical file range is exactly:

- A0–A10;
- the checkpoint `OBLIGATION_DAG.md`.

The candidate fast-forwarded through that exact source history and then added Curator-only corpus and control commits.

Relative to the immutable source, no file under `projects/affine-cdc/proof-development/` is modified by the Curator delta. Therefore the A0–A10 dossiers and checkpoint DAG retain exact blob identity.

## 3. Later-delta exclusion

The live proof-development branch is seventeen commits ahead of `8bee1678...` and contains later B1, B2, B3, handoff, and updated-ledger material.

None of those later mathematical files is present in the Curator delta. In particular, the candidate does not consume:

- `AC_PD_B1_*`;
- `AC_PD_B2_*`;
- `AC_PD_B3_*`;
- later `OBLIGATION_DAG.md` modifications;
- Programme B handoffs.

The Programme A handoff was read only to verify authority, success conditions, exclusions, and stop conditions. It is not treated as mathematical source and is not copied into the candidate.

## 4. Theorem-scope audit

The active theorem is preserved exactly:

> Every multigraph with finite active edge set and no singleton cut has a finite circuit double cover.

The candidate explicitly preserves:

- loops and parallel edge objects;
- disconnected components and isolated vertices;
- arbitrary ambient vertex carrier;
- intrinsic cut-even circuit semantics;
- indexed/multiset occurrence multiplicity;
- equivalence of no singleton cut with absence of nonloop bridges.

No hidden connectedness, simplicity, looplessness, or ambient finiteness hypothesis is introduced.

## 5. Dependency audit

Every A0–A10 arrow has both:

- an exact source checkpoint pointer in `PROGRAMME_A_INTEGRATION_MAP.md`;
- an active integrated destination in `complete-cdc/`.

The active chapter partition is:

- A0–A3: foundations, expansion, and binary flow;
- A4–A7: affine compatibility and graph-level extraction;
- A8–A10: collapse, decomposition, and final assembly.

## 6. Correction audit

All seven material Programme A corrections are visible in the active corpus:

1. circuit semantics/characterization versus later decomposition;
2. intrinsic loop-aware parity versus loopless once-per-edge parity;
3. internal equal-order flow transport and Tutte provenance-only status;
4. compatibility pair complex versus retained graph/dart data;
5. cut-even collapse versus invalid circuit projection;
6. indexed occurrence multiplicity under repeated support values;
7. weakest natural theorem hypotheses.

## 7. Source audit

Seymour 1981 is the sole external non-elementary logical input.

The candidate records:

- literal six-to-eight range inclusion;
- modular reduction to `Z/8Z`;
- internal spanning-forest flow-kernel count;
- inclusion–exclusion nowhere-zero count;
- equal-order transport to `F₂³`.

No indispensable logical source locator remains unresolved.

## 8. Assurance audit

The candidate classifies Programme A as:

`CURATOR-INTEGRATED / AUTHORIAL PAPER-PROOF COMPLETE`.

It does not claim:

- independent Audit A completion;
- end-to-end Lean verification;
- manuscript acceptance or revision;
- peer review or publication;
- release, arXiv, DOI, or timestamp status.

## 9. Architecture and proof-family preservation

The integrated three-chapter proof is the preferred current exposition.

The exact A0–A10 dossiers and checkpoint DAG remain in `proof-development/` for:

- exact theorem numbering;
- local proof details;
- independent audit;
- AC-PDL repair;
- later Lean and manuscript projection.

The pair-complex, quotient, stress, quadratic-Lagrangian, cross-bit, support-parity, dart-rotation, and formal macro-Port views remain correctly classified as equivalent or additional structures rather than stronger theorems.

## 10. Stop-condition audit

No stop condition was triggered.

- no contradiction among A0–A10 was found;
- no hidden final-theorem hypothesis was found;
- Seymour’s theorem is not weaker than the use made of it;
- no formal/paper correspondence issue changes the mathematical claim;
- no destructive supersession of valuable proof-family material was required;
- no later live mathematical commit was needed.

## 11. Repository-isolation audit

- `main` remains exactly `960c92b7ff231c78b387894149779083060a75eb`;
- the live PDL branch was not modified;
- no branch was deleted or renamed;
- no force-push, rebase, squash, or history rewrite occurred;
- no Lean, manuscript, release, arXiv, DOI, or publication surface was changed.

## 12. AC-DIR disposition questions

The candidate leaves the following decisions to AC-DIR:

1. whether to accept this candidate as the next fixed complete-CDC corpus baseline;
2. whether to authorize a separate history-preserving fast-forward of `main`;
3. whether to retarget Audit A immediately to the accepted candidate;
4. how to disposition defects returned by Audit A between AC-PDL repair and genuine AC-RL mathematics;
5. when to authorize later Lean and Paper A projections from the same accepted baseline.

No mathematical ambiguity requiring pre-disposition escalation remains.