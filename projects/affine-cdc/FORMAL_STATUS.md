# Formalization and reliability boundary

This file separates mathematical content, source provenance, exact computation, independent review, formal verification, and publication status. Natural reconstruction and current-best inclusion do not confer stronger assurance.

## 1. Natural Cycle Double Cover target

The natural public theorem is:

> Every multigraph with finite active edge set and no bridges has a cycle double cover.

Loops are allowed. A circuit is a nonempty inclusion-minimal cut-even edge set, so a singleton loop is a circuit.

The companion Lean repository still contains an earlier loopless ambient-finite `Statement.lean` checkpoint. That declaration is defined but not proved. The approved natural statement has not yet been implemented as the final Lean theorem.

## 2. Machine-checked anchor

At the current audited companion-repository checkpoint, Lean verifies:

- local affine-family classification;
- quotient, gauge, dual-configuration, invariance, and branching machinery;
- rank-three affine compatibility in the original branching/cross-bit presentation;
- dart-level indexed support construction with exact double coverage;
- a cycle double cover for a finite loopless cubic graph already carrying the required nowhere-zero `F_2^3` flow.

Lean does not yet prove the unconditional outer-shell theorem or the natural statement with loops and active-edge finiteness.

## 3. Paper-level complete CDC mathematics

The active corpus contains theorem-level arguments for:

- invariant characteristic-torsor/Lagrangian compatibility;
- graph-level even-cover extraction;
- vertex-even/cut-even bridge and pure collapse transport;
- finite circuit decomposition;
- loop deletion and reinsertion;
- cubic expansion and binary-flow input;
- assembly of the full finite-active-edge CDC theorem.

These arguments are not automatically Lean-checked by corpus inclusion. The exact primary Tutte theorem/page source for the equal-order group-flow input remains a publication source gate; the Seymour six-flow citation is separately verified.

## 4. Formal correspondence still required

The canonical invariant local object is

$$
\kappa_v+L_v=\operatorname{Char}_{q_v}(L_v).
$$

The existing Lean API uses the original branching presentation. Their equivalence is mathematically documented but is not yet a checked bridge. The graph-level multiset even-cover object and outer collapse shell also remain to be implemented formally.

## 5. Five-support mathematical status

The active `five-support/` corpus synthesizes the exact public checkpoint

`dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`.

### Theorem-level public mathematics

Written general arguments include:

- root-valued `E_5` flow and equivalent global formulations;
- universal compatible eight-support root lift;
- fixed-plane component parity and singular/Schur/stress/Fourier/colour-cut forms;
- root-lift, cycle-face surface, and full-dual correspondence;
- componentwise criterion `T_g -> A_5`;
- factorable half-cube classification in corrected scope;
- dominating-clique capacity for ranks two through five;
- gauge/Petrial correspondence and marked-core affine occurrence loci;
- connected-cycle switch laws and internal/external dichotomy;
- three-cut gluing and ten-state four-edge interface;
- cap forcing, pairing alignment, routing coordinates, and Type T/Type H reduction;
- affine holonomy, root-fibre section theory, Tait resolution, and Type H Tait escape;
- BBD root rigidity, `H^1(S_5,E_5)=0`, canonical defect flow, `K_6` completion, induced defect forest, and Petersen transport;
- DDD atom triality, unique bad route, rank-two Tait escape;
- full-rank curvature/common-cut duality and flat-potential equivalence.

“Theorem-level” means that a mathematical statement and argument are written. It does not mean independently audited, formalized, peer reviewed, or accepted for publication.

### Exact finite mathematics

Exact computation supports named finite results including:

- the fixed-flow cube obstruction;
- thirty-vertex renewal and switch censuses;
- complete Petersen Fano-flow/fibre/surface/switch classification;
- flower `J_5` mixed-core and one-step neighbourhood;
- small four-pole profile census;
- routing, monodromy, atom, root-fibre, cohomology, reserve-code, and renewal tables;
- explicit no-two-cut and nonflat witnesses.

These are exact results about finite objects, not universal graph theorems.

### Open mathematics

Not proved:

- the global five-support statement;
- universal existence of a good Fano flow or compatible lift;
- common-cut localization in the full-rank nonflat atom sector;
- a composition-safe interface for the flat potential;
- zero-network/co-root-forest pruning;
- Type T decomposition and elimination of all residual Type H families;
- full-cap-profile or arbitrary four-pole realizability;
- horizontal escape/decomposition for every bad-flow component;
- completeness of the target obstruction library.

## 6. Five-support formal status

No theorem in the reconstructed five-support corpus is represented as Lean-formalized unless separately identified in the companion repository. The reconstruction did not modify Lean.

There is no checked Lean theorem asserting the global five-support statement, the componentwise surface criterion, the four-pole routing reductions, or the holonomy/defect/atom/localization results.

## 7. Independent-review status

The accepted outer-shell MP2 packet retains its recorded review history. The full seventy-eight-packet five-support checkpoint has not received one independent line-by-line audit as a whole.

`AC-CORPUS-01` performed substantive Curator synthesis and self-audit for consistency, dependency, scope, source coverage, recovery, and supersession. Self-audit is not independent mathematical review.

A future independent audit should prioritize:

1. the componentwise surface criterion and scope correction;
2. four-pole routing closure and physical realizability;
3. BBD root rigidity and cohomology assembly;
4. variational defect-forest inequalities;
5. route-lock, curvature, and flat-potential proofs;
6. every transfer step used in a future localization/composition theorem.

## 8. Source and retirement status

- canonical CDC mathematics lives in `core/` and `reduction/`;
- current five-support mathematics lives in `five-support/`;
- the seventy-eight discovery-order packets are retired from the current tip after exact successor mapping;
- their bodies, commits, priority, counterexamples, corrections, and finite evidence remain recoverable from `dad218dd...`;
- private notebook/recovery branches remain mapped evidence and are not copied wholesale;
- the recovered combined verifier remains `CODE-PARTIAL` where explicitly recorded.

See:

- [`CHAPTER_PROVENANCE.md`](CHAPTER_PROVENANCE.md);
- [`MIGRATION_LEDGER.md`](MIGRATION_LEDGER.md);
- [`RETIRED_SOURCE_CLASSIFICATION.md`](RETIRED_SOURCE_CLASSIFICATION.md);
- [`SOURCE_RECOVERY_AUDIT.md`](SOURCE_RECOVERY_AUDIT.md).

Retirement from the current tree is a representation decision, not an assurance upgrade or deletion of public history.

## 9. Publication and release status

This work did not:

- write or revise a manuscript;
- authorize arXiv submission;
- establish novelty relative to the literature;
- create a release or tag;
- modify a DOI or Zenodo record;
- implement a timestamp or priority-attestation workflow.

## 10. Reliability rules

1. Natural reformulation does not inherit Lean status without a checked bridge.
2. Exact finite computation does not prove a universal theorem.
3. Bad lift, bad fixed-flow fibre, and bad graph have different quantifiers.
4. `J_g -> A_5` is factorable compression; the complete fixed-lift object is `T_g`.
5. `K_6`-free does not imply a half-cube map.
6. Connected-cycle and arbitrary binary-cycle switches are different adjacency notions.
7. Route-lock does not imply a graph two-cut or flatness.
8. Local algebraic resolution is not graph replacement until boundary semantics and gluing are proved.
9. Superseded packets may retain valid narrower theorems and exact evidence.
10. Current-best inclusion, Director acceptance, independent audit, Lean verification, peer review, and publication are separate axes.