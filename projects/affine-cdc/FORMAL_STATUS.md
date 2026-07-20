# Formalization and reliability boundary

This file separates current mathematical inclusion, authorial proof completion, independent audit, machine verification, manuscript projection, peer review, publication, release, arXiv, and DOI status.

## 1. Natural complete theorem

Programme A proves at authorial paper-proof level:

> Every multigraph with finite active edge set and no singleton cut has a finite circuit double cover.

A circuit is a nonempty inclusion-minimal finite cut-even support. Loops, parallel edge objects, disconnected components, isolated vertices, and an arbitrary ambient vertex carrier are allowed.

For nonloop active edges, no singleton cut is equivalent to no bridge.

## 2. Programme A status

Exact source:

`proof-development/affine-cdc-rigour-v1@8bee16780b549f51e1f29343671a059961ec4172`.

Integrated scope:

- A0–A9: `COMPLETE-DRAFT` authorial proof units;
- A10: `READY-FOR-CURATOR` aggregate authorial proof;
- curation candidate: Curator-integrated authorial paper-proof.

These statuses do not mean independently audited or machine-checked.

The controlling integrated proof is under [`complete-cdc/`](complete-cdc/). Exact unit provenance is in [`PROGRAMME_A_INTEGRATION_MAP.md`](PROGRAMME_A_INTEGRATION_MAP.md).

## 3. Logical external input

The sole external non-elementary logical theorem is Seymour’s nowhere-zero six-flow theorem:

P. D. Seymour, “Nowhere-zero 6-flows”, Journal of Combinatorial Theory, Series B 30 (1981), 130–135, DOI `10.1016/0095-8956(81)90058-7`.

Programme A proves internally:

- flow-kernel cardinality over arbitrary finite abelian groups;
- the nowhere-zero flow count by inclusion–exclusion;
- dependence of that count only on group order;
- transport from `Z/8Z` to `F₂³`.

Tutte’s equal-order theorem is historical provenance, not an unresolved logical premise. Exact Tutte primary-page refinement may remain useful bibliographically but is not a proof-completeness gate.

## 4. Machine-checked anchor

The companion checkpoint

`Yuren-Tang/affine-cdc:main@ebd7098a7a8b824e8c0a511d3c71f61705672aa8`

machine-checks substantial internal slices, including:

- local affine-family classification;
- quotient, gauge, branching, and dual-configuration machinery;
- rank-three compatibility in the original branching/cross-bit presentation;
- dart gluing and indexed dart supports;
- exact two-point edge coverage;
- a cubic-flow graph-level CDC result.

It does not yet prove the integrated natural theorem end to end.

Unformalized or unassembled interfaces include:

- finite-active multigraph semantics with loops and arbitrary ambient vertex carrier;
- exact loop deletion/reinsertion witness normalization;
- the port-cycle expansion/collapse dossier used by Programme A;
- Programme A’s internal equal-order flow-count proof;
- the invariant pair-complex and characteristic-torsor global presentation;
- the explicit even-cover-first graph/dart extraction and collapse factorization;
- final circuit decomposition and outer theorem assembly.

No Lean repository was changed by this intake.

## 5. Independent-review status

Programme A has not yet passed dedicated independent Audit A.

The priority audit targets are:

1. alternate-path lifting for external edges in the port-cycle expansion;
2. spanning-forest flow-kernel count and inclusion–exclusion;
3. local affine-family completeness and quotient formula;
4. Fano cross-pairing and characteristic-torsor intersection;
5. graph/dart descent and indexed occurrence counting;
6. loopless set-incidence to intrinsic cut-parity conversion;
7. pulled-back-cut collapse and repeated projected occurrences;
8. terminating circuit decomposition and loop/core reinsertion.

These are assurance targets, not known defects.

## 6. Complete-theorem source status

The active current-best proof surface is:

- `complete-cdc/README.md`;
- `complete-cdc/foundations-expansion-and-flow.md`;
- `complete-cdc/affine-compatibility-and-extraction.md`;
- `complete-cdc/collapse-decomposition-and-assembly.md`.

The A0–A10 dossiers and `OBLIGATION_DAG.md` remain under `proof-development/` as exact authorial provenance, audit detail, and repair inputs.

The specialized `core/` and `reduction/` chapters remain current mechanism-level companions. They do not supersede the end-to-end Programme A dependency closure.

## 7. Programme B separation

The five-support theorem remains open. This intake consumes no B1 or later PDL checkpoint.

The next B1 checkpoint is

`778b09ac8260192e022f512f24cdef1d04871f37`.

No B1 theorem or correction acquires current-best status through Programme A.

## 8. Five-support current status

The active `five-support/` corpus contains theorem-level public arguments, exact finite computations, counterexamples, corrections, and open programmes from its previously integrated source line.

The global five-support theorem, universal good-flow existence, full-rank localization/composition, full-cap realizability, horizontal escape/decomposition, and target-library completeness remain open.

No five-support statement is represented as Lean-formalized unless separately identified in the companion repository.

## 9. Manuscript and publication status

This intake did not:

- edit or approve Paper A;
- establish novelty relative to literature;
- authorize arXiv or journal submission;
- create a release or tag;
- modify a DOI or Zenodo record;
- implement a timestamp or priority-attestation workflow.

A later manuscript revision must consume an AC-DIR-dispositioned mathematical candidate and may not silently repair theorem content.

## 10. Reliability rules

1. Curator integration does not equal independent audit.
2. Natural reformulation does not inherit Lean status without checked bridges.
3. Exact finite computation does not prove a universal theorem.
4. Intrinsic half-edge parity and once-per-edge incidence parity agree only on loopless graphs.
5. The pair complex does not by itself retain graph/dart/indexed-support semantics.
6. Collapse preserves cut-even supports and occurrence multiplicity, not circuit minimality.
7. Equal support values at distinct indices remain distinct occurrences.
8. Current-best inclusion, Director acceptance, independent audit, Lean verification, manuscript approval, peer review, publication, release, and DOI status are separate axes.

See [`PROGRAMME_A_ASSURANCE_BOUNDARY.md`](PROGRAMME_A_ASSURANCE_BOUNDARY.md) for the intake-specific boundary.