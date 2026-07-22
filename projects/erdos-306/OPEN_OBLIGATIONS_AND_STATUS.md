# Open obligations and status

## 1. Mathematical completeness

No missing load-bearing mathematical implication was found in the four exact input sources after applying the PDL and Review B corrections.

No `BLOCKED-FRONTIER` is created.

No codex-only theorem is indispensable: every conceptual implication used by the corpus is present in the released proof, the PDL human proof, or the stated external PNT/RS boundary.

## 2. Exact remaining obligations

### `E306-PDL-RS-PUBLISHER-SCAN`

**Class:** `SOURCE-GATED / BLOCKED-SOURCE / NON-BLOCKING-DOWNSTREAM`.

Compare, symbol by symbol, the released Lean statements

- `rosser_schoenfeld_cor3`;
- `rosser_schoenfeld_thm5`

with the publisher scan at the cited pages and equations.

This is not a new proof obligation. It is external source certification.

### `E306-PDL-C4-RELEASE-REFACTOR-CORRESPONDENCE`

**Class:** `ACTIVE / NON-BLOCKING`.

Maintain an exact map from:

- v0.0.3 declarations;
- frozen refactor principle/handoff modules;
- current paper terminology.

This becomes load-bearing only if a future manuscript or release claims that the purified architecture itself has been formalized.

### `E306-DOC-RELEASE-STATUS-COMMENTS`

**Class:** `DOCUMENTATION-STATUS DEFECT / SEPARATE AUTHORITY`.

Correct stale comments such as:

- old claims that G5/G7 remain open;
- old descriptions of analytic inputs;
- comments suggesting a third nonstandard axiom.

The kernel theorem and audit remain controlling. This curation branch does not modify Lean.

## 3. Manuscript-consumer obligations

The next manuscript worker must:

1. start from exact REV3 `94615a5...`;
2. consume this corpus and PDL `cecd3c...`;
3. replace the concrete terminal architecture by the symbolic one;
4. preserve exact boundary hypotheses and fibre factors;
5. state release/PNT status separation;
6. update `PROOF_LEDGER.md` only after the text changes;
7. return a new exact manuscript checkpoint for assurance.

These are projection obligations, not unresolved mathematical lemmas.

## 4. Editorial and publication gates

Outside this corpus:

- bibliography/source audit;
- author metadata;
- acknowledgements and AI disclosure;
- arXiv categories, comments, licence, and source package;
- substantive Owner review;
- explicit submission authorization.

## 5. Current classification

`READY-FOR-MANUSCRIPT-CONSUMER / MATHEMATICAL-SPINE-COMPLETE / RS-SOURCE-CERTIFICATION-OPEN / RELEASE-REFACTOR-MAP-NONBLOCKING`.

## 6. Return rule for future defects

Return to `E306-PDL` only if a future consumer discovers:

- a missing implication not supplied by the current proof sources;
- incompatible parameter assumptions;
- an indispensable theorem existing only on the frozen refactor;
- a finite residual whose mathematical proposition or hypotheses are absent;
- a mismatch between the public theorem and the construction endpoint.

No such item was found in this intake.
