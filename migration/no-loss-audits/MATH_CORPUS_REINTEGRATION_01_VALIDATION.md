# MATH-CORPUS-REINTEGRATE-01 validation

## Exact control

- role: `Mathematics — Corpus Reintegration Curator` (`MATH-CUR-REINT`);
- exact parent: `main@5a2fb189fec6f93e26c43a344ac7ab69ac1a074b`;
- sole workspace: `curation/corpus-reintegration-v1`;
- final branch SHA: recorded in the durable issue return because a commit cannot contain its own SHA.

## 1. Ancestry and mutation isolation

Pre-validation compare against the exact parent returned:

```text
status: ahead
merge base: 5a2fb189fec6f93e26c43a344ac7ab69ac1a074b
ahead: 18
behind: 0
changed paths before this record: 18
```

This record adds one commit and one path. Expected final delta is `19 commits / 19 changed paths`.

No branch other than `curation/corpus-reintegration-v1` was created or written by this role. No force update, rebase, squash, history rewrite, PR, merge, `main` movement, release, tag, DOI, arXiv, submission, publication action or external contact occurred.

## 2. Complete changed-file inventory

1. `projects/affine-cdc/ACTIVE_MATHEMATICAL_SURFACE.md`
2. `projects/affine-cdc/CORPUS_AUTHORITY.md`
3. `projects/affine-cdc/COUNTEREXAMPLE_AND_SUPERSESSION_LEDGER.md`
4. `projects/affine-cdc/CURRENT_BEST.md`
5. `projects/affine-cdc/FORMAL_STATUS.md`
6. `projects/affine-cdc/MATHEMATICAL_ARCHITECTURE.md`
7. `projects/affine-cdc/PUBLICATION_PROGRAM.md`
8. `projects/affine-cdc/README.md`
9. `projects/affine-cdc/THEOREM_DEPENDENCY_MAP.md`
10. `projects/affine-cdc/complete-cdc/PAPER_A_STRUCTURAL_MANUSCRIPT.md`
11. `projects/affine-cdc/external-review/ENTRYPOINT.md`
12. `projects/affine-cdc/external-review/FIVE_CDC_SPECIALIST_HANDOFF.md`
13. `projects/affine-cdc/external-review/REPOSITORY_AND_BRANCH_AUTHORITY_MAP.md`
14. `projects/affine-cdc/five-support/COMPONENT_CHAIN_LOCAL_THEORY.md`
15. `projects/affine-cdc/five-support/FIVE_SUPPORT_AND_5CDC.md`
16. `projects/affine-cdc/rank-hierarchy/PAPER_B_DEFERRED_STATUS.md`
17. `projects/affine-cdc/research/root-lift/ROOT_LIFT_AND_ORIENTATION_THEORY.md`
18. `registry/views/corpus.affine-cdc.reintegration-v1.json`
19. this file.

No canonical theorem source, audit bundle, unit registry, typed-relation file, source manifest, source-to-unit map, batch classification, recovery manifest, validator or Lean/manuscript repository was modified.

## 3. Freshness binding

The human corpus is explicitly bound to:

- parent `5a2fb189fec6f93e26c43a344ac7ab69ac1a074b`;
- units blob `a04ab3c878e500ad3b6fd9f6d0f84127fe26c82f`;
- relations blob `6d79b6e165ded818b9c1ce8c70734b654db15b8c`;
- programme-view blob `c14b2d5f0eec301a1bbc39ec7bfeb086150b63f0`;
- source-map blob `cf856729980e298233580169f65220091fcd88b4`.

The binding is duplicated only as metadata in `CORPUS_AUTHORITY.md` and `registry/views/corpus.affine-cdc.reintegration-v1.json`; theorem wording remains owned by normalized unit IDs.

Result: `PASS`.

## 4. Existing recovery/no-loss validation non-regression

The deterministic validator `migration/validate_port_ac_consolidate_01.py` reads:

- the six-source manifest;
- the source-to-unit map and six batch files;
- the unit registry;
- typed relations;
- `programme.affine-cdc` and `frontier.five-cdc` views;
- immutable source objects named by exact commit/path/blob/anchor.

The final compare inventory contains none of these inputs. Their blobs and frozen source commits are identical to the previously passing snapshot. Therefore the deterministic result is preserved by exact input identity:

```text
sources=6
substantive_items=80
canonical_units=34
unclassified=0
status=PASS
```

This is an input-identity non-regression proof, not a claim that a fresh shell invocation was made through the GitHub connector. The prior recovery report, source pointers and validation evidence remain unchanged and applicable.

Result: `PASS — exact validator-input identity`.

## 5. Six-question reader test

A reader beginning at `projects/affine-cdc/README.md` can answer without issue or branch archaeology:

1. **What ordinary theorem is established?** `complete-cdc/PAPER_A_STRUCTURAL_MANUSCRIPT.md` and the three proof chapters state the finite-active/no-singleton-cut CDC endpoint and no-nonloop-bridge equivalence.
2. **What are the exact hypotheses and assurance?** `FORMAL_STATUS.md` and unit-level source pointers separate human proof, independent review, authorial result, open problem and Lean boundary.
3. **What depends on what?** `THEOREM_DEPENDENCY_MAP.md` mirrors the typed relations and places the first missing five-support edge correctly.
4. **What failed and what survives?** `COUNTEREXAMPLE_AND_SUPERSESSION_LEDGER.md` and `five-support/COMPONENT_CHAIN_LOCAL_THEORY.md` place each negative beside its valid narrower theorem.
5. **What are the publication statuses?** Paper A is reviewed but unpublished; higher-rank Paper B is `DEFERRED / PAYOFF GATE NOT MET`; no A/B series is active.
6. **What should a five-CDC specialist examine?** `external-review/FIVE_CDC_SPECIALIST_HANDOFF.md` reaches the one-atom endpoint, double-atom and genuine-image questions directly.

Result: `PASS 6/6`.

## 6. One normalized statement per active unit ID

The controlling registry remains unchanged and its deterministic validator establishes 34 unique unit IDs. New human chapters cite those IDs or exact canonical source theorems; they add no competing registry unit and assign no second normalized statement owner. `registry/views/corpus.affine-cdc.reintegration-v1.json` explicitly records this ownership rule.

Result: `PASS`.

## 7. Prose/typed-relation round trip

Every load-bearing current five-support arrow in prose appears in `THEOREM_DEPENDENCY_MAP.md` with its typed relation or exact canonical dependency. In particular:

- v7.4.1 depends on the one-atom endpoint;
- double atom refutes the broad scheduler;
- conditional disjoint commutation is a specialization;
- supplied coherence only qualifies the endpoint;
- the third terminal refutes the broad chain;
- exact-two specializes the broad chain and uses local tables;
- co-root/zero exhaustion qualifies exact-two only in application carriers;
- conditional parent moves depend on the complete endpoint.

Conversely, all typed relations defining the current first frontier and downstream conditional suffix are exposed in the human dependency map. Expository ordering is marked separately from implication.

Result: `PASS`.

## 8. Negative adjacency

The active chapters keep these triples adjacent:

1. false unconditional scheduler / double-atom certificate / conditional disjoint replacement;
2. false broad rooted-carrier chain / third-terminal certificate / exact-two theorem;
3. false equal-face Xi totality / same-arc certificate / strict-row and bad-free replacement;
4. false canonical full-witness recovery / four-parallel-edge certificate / support-word equivalence;
5. false per-lift Fano orientability / mixed `K_4` fibre / family-quotient formulation.

Result: `PASS`.

## 9. Authority and frontier consistency

All compatibility entrypoints named by `programme.affine-cdc` were regenerated. They now agree that:

- ordinary CDC is separate from manuscript status;
- Paper A is the sole current standalone publication-natural unit;
- Paper B mathematics is preserved while publication is deferred;
- the first five-support gap is the one-atom complete endpoint, not terminal exhaustion;
- root-lift assurance is authorial pending review.

No active file retains `AC-FRONTIER-COMPONENT-CHAIN-TERMINAL-EXHAUSTION` as the controlling first frontier. Historical files remain provenance only.

Result: `PASS`.

## 10. External review path

`external-review/ENTRYPOINT.md` immediately points to `external-review/FIVE_CDC_SPECIALIST_HANDOFF.md`. The packet contains the exact problem, equivalences, theorem/negative graph, first missing endpoint, double-atom certificate, genuine-image question, absent invariant/defect bound, established-approach comparison, six specialist questions and exact source ledger.

Result: `PASS`.

## 11. Five-surface separation

The active corpus separately labels:

- ordinary CDC accepted mathematics;
- Paper A reviewed manuscript and exact formal boundary;
- deferred higher-rank Paper B mathematics;
- unresolved five-support/5-CDC research;
- root-lift/orientation theory and inherited assurance.

No theorem, manuscript, formalization or publication status is transferred between these surfaces.

Result: `PASS`.

## 12. Readiness

`READY FOR #101 INDEPENDENT CORPUS AUDIT`.

This readiness concerns corpus architecture, source fidelity and epistemic separation. It does not accept the five-support conjecture, upgrade root-lift assurance, reopen Paper B publication, or authorize any publication or repository integration action.