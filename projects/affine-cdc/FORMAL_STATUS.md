# Formalization and reliability boundary

This file separates mathematical content, source provenance, exact computation, independent review, formal verification, and publication status. A theorem does not inherit a stronger status merely because it has been rewritten in a natural invariant language or integrated into the primary corpus.

## 1. Natural Cycle Double Cover target

The natural public theorem is:

> Every multigraph with finite active edge set and no bridges has a cycle double cover.

Loops are allowed. A circuit is a nonempty inclusion-minimal cut-even edge set, so a singleton loop is a circuit.

The companion Lean repository still contains an earlier self-contained `Statement.lean` checkpoint whose public declaration is loopless and quantifies over finite ambient vertex and edge types. That declaration is defined but not yet proved. The approved natural mathematical target has not yet been implemented as the final Lean statement.

## 2. Machine-checked anchor

At the current audited companion-repository checkpoint, Lean verifies:

- local affine-family classification;
- quotient, gauge, dual-configuration, invariance, and branching machinery;
- rank-three affine compatibility in the original branching/cross-bit presentation;
- dart-level indexed support construction with exact double coverage;
- a cycle double cover for a finite loopless cubic graph already carrying the required nowhere-zero $\mathbf F_2^3$ flow.

The last item is a cubic-flow corollary. Lean does not yet prove either the current unconditional loopless `CDCStatement` or the approved full theorem with loops and active-edge finiteness.

## 3. Paper-level complete CDC mathematics not yet machine-checked

The canonical corpus contains theorem-level arguments for:

- the invariant characteristic-torsor/Lagrangian compatibility proof;
- graph-level even-cover extraction;
- finite-support circuit decomposition;
- vertex-even/cut-even bridge;
- pure cut-even collapse transport;
- loop deletion and singleton-loop reinsertion;
- port-cycle cubic expansion;
- adaptive binary ordering and flow-preserving expansion;
- the isolated classical `BinaryEightFlow` boundary;
- assembly of the full finite-active-edge CDC theorem.

These are paper-level mathematical arguments. They are not automatically Lean-checked by their inclusion in the corpus.

The external six-flow citation to Seymour is verified. The exact primary Tutte theorem/page source for the equal-order group-flow existence input remains a publication source gate. Existence and counting theorems must remain distinct.

## 4. Formal correspondence still required

The canonical invariant local object is

$$
\kappa_v+L_v
=
\operatorname{Char}_{q_v}(L_v).
$$

The existing Lean local-family API uses the original branching presentation. Their mathematical equivalence is documented, but the bridge is not yet a checked Lean term.

Similarly, the current Lean indexed support construction has not yet been factored formally through the named graph-level multiset even-cover predicate and the outer collapse shell.

## 5. Five-support mathematical status

The reconstructed `five-support/` corpus integrates theorem-level public arguments, exact finite classifications, counterexamples, and open programmes from checkpoint

`dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`.

### Theorem-level public mathematics

The following are written with general mathematical arguments in the public source surface and synthesized in the corpus:

- root-valued $E_5$ flow and equivalent five-support formulations;
- universal compatible eight-support root lift above a cubic Fano flow;
- fixed-plane component-parity/singular-quotient criterion;
- Schur, stress, Fourier, and colour-cut equivalents;
- root-lift/cycle-face-surface/dual-triangulation correspondence;
- complete componentwise criterion $T_g^{(1)}\to\mathscr A_5$;
- exact factorable half-cube classification in its narrowed scope;
- dominating-clique capacity for ranks two through five;
- gauge/Petrial correspondence and marked-core affine occurrence loci;
- exact internal switch correction image and internal/external dichotomy;
- three-edge-cut gluing and ten-state four-edge interface;
- cap forcing, pairing alignment, routing coordinates, and uniform-routing elimination;
- affine holonomy, root-fibre section theory, Tait-resolution equivalence, and Type H Tait escape;
- BBD root rigidity, $H^1(S_5,E_5)=0$, and canonical defect flow;
- $K_6$ completion, defect strips, variational defect forest, and Petersen transport;
- DDD atom triality, unique bad route, rank-two Tait escape;
- full-rank curvature/common-cut duality and flat-potential equivalence.

“Theorem-level” means a mathematical statement and argument are written. It does not mean independently audited, formalized, peer reviewed, or accepted for publication.

### Exact finite computational mathematics

Exact computation supports:

- fixed-flow cube obstruction;
- thirty-vertex renewal and switch censuses;
- complete Petersen Fano-flow/fibre/surface/switch classification;
- flower-$J_5$ mixed-core and one-step neighbourhood classification;
- small four-pole profile census;
- routing and monodromy tables;
- atom counts and explicit no-two-cut/nonflat witnesses;
- root-fibre and cohomology tables;
- selected reserve-code and renewal modules.

These are exact theorems about named finite objects. They do not establish universal graph statements.

### Open five-support mathematics

Not proved:

- the global five-support cycle-double-cover statement;
- universal existence of a good Fano flow or good compatible lift;
- common-cut localization in the full-rank nonflat atom sector;
- a composition-safe finite interface for the flat potential;
- zero-network/co-root-forest pruning;
- Type T decomposition;
- elimination of all residual Type H obstruction families;
- full-cap-profile or arbitrary four-pole realizability theorem;
- horizontal escape/decomposition for every bad-flow component;
- completeness of the target obstruction library.

## 6. Five-support formal status

No theorem in the reconstructed five-support corpus is represented here as Lean-formalized unless separately identified in the companion repository. The reconstruction did not modify Lean.

In particular, there is no checked Lean theorem asserting:

- existence of a five-support cover for every bridgeless cubic graph;
- the componentwise half-cube criterion as a formal graph/surface theorem;
- the four-pole routing reductions;
- the holonomy, defect-forest, atom-curvature, or localization results.

Some underlying affine compatibility, gauge, and support-construction infrastructure is machine-checked in another presentation. That does not transfer formal status to the new five-support statements without explicit bridges.

## 7. Independent-review status

The accepted outer-shell MP2 packet has its recorded Director disposition and review history. The full 78-packet five-support checkpoint has not received one independent line-by-line audit as a whole.

This reconstruction performed a Curator self-audit for consistency, dependency, scope, source coverage, and supersession. Self-audit is not independent mathematical review.

A future independent audit should prioritize:

1. the componentwise surface criterion and scope correction;
2. the four-pole routing closure and physical realizability boundary;
3. BBD root rigidity and cohomology assembly;
4. variational defect-forest inequalities;
5. atom route-lock, curvature, and flat-potential proofs;
6. every transfer step used in a future localization/composition theorem.

## 8. Source status

- canonical CDC sources live in `core/` and `reduction/`;
- reconstructed five-support mathematics lives in `five-support/`;
- exact discovery, priority, finite-evidence, correction, and intermediate sources remain in `research/`;
- private notebook/recovery branches remain mapped evidence and are not copied wholesale;
- snapshot-only older topological sources remain subject to their restoration boundary.

The source-to-corpus map is [`MIGRATION_LEDGER.md`](MIGRATION_LEDGER.md).

## 9. Publication and release status

This reconstruction did not:

- write or revise a manuscript;
- authorize arXiv submission;
- establish novelty relative to the literature;
- create a release or tag;
- modify a DOI or Zenodo record;
- implement a timestamp or priority-attestation workflow.

The public Git history records exact source priority. Publication decisions remain separate.

## 10. Reliability rules

1. Natural reformulation does not inherit Lean status without a checked bridge.
2. Exact finite computation does not prove a universal theorem.
3. A bad lift, bad fixed-flow fibre, and bad graph have different quantifiers.
4. $J_g\to\mathscr A_5$ is factorable compression; the complete fixed-lift object is $T_g$.
5. A $K_6$-free graph need not map to the half-cube.
6. Connected-cycle switches and general binary-cycle switches are not the same adjacency notion.
7. Route-lock does not imply a graph two-cut or flatness.
8. A successful local algebraic resolution is not valid graph replacement until boundary semantics and gluing are proved.
9. Superseded packets may retain valid narrower theorems and exact evidence.
10. Corpus placement, Director acceptance, independent audit, Lean verification, peer review, and publication are separate axes.