# Formalization and reliability boundary

This file separates machine-checked results, the approved mathematical target,
the unchanged Lean checkpoint, paper proofs, exact computations, and open
programmes. A theorem does not inherit a stronger status merely because it has
been rewritten in a more invariant language or placed in a cleaner architecture.

## 1. Approved mathematical target and current Lean checkpoint

The natural public theorem is:

> Every multigraph with finite active edge set and no bridges has a cycle double
> cover.

Loops are allowed. The natural circuit is a nonempty inclusion-minimal cut-even
edge set, so a singleton loop is a circuit. The author has approved Path A for a
future clean migration of the public Lean statement to this semantics and to
active-edge finiteness.

The companion repository
[`Yuren-Tang/affine-cdc`](https://github.com/Yuren-Tang/affine-cdc) still contains
the earlier self-contained Mathlib-only audit file `Statement.lean`. Its current
`CDCStatement` is loopless and quantifies over finite ambient vertex and edge
types. That declaration is **defined but not yet proved**. It remains unchanged
until the separate exact declaration-and-migration packet is approved and a
later local Lean task implements it.

Thus the current Lean checkpoint is not the final natural mathematical statement,
and approval of Path A is not evidence that the migration has already occurred.

## 2. Machine-checked anchor

At the current audited companion-repository checkpoint, Lean verifies:

- the local affine-family classification;
- the quotient, gauge, dual-configuration, invariance, and branching machinery;
- the rank-three affine compatibility conclusion in the original
  branching/cross-bit presentation;
- the dart-level indexed support construction with exact double coverage;
- passage from that construction to a cycle double cover for a finite loopless
  cubic graph already carrying the required nowhere-zero
  $\mathbf F_2^3$-flow.

The last item is a **cubic-flow corollary**, not the final unconditional theorem.
The Lean repository does not yet prove either the current loopless
`CDCStatement` for all finite loopless bridgeless multigraphs or the approved
full theorem with loops and active-edge finiteness.

## 3. Invariant mathematical bridge not yet machine-checked

The canonical mathematical corpus identifies the original local-family object
with the characteristic torsor

$$
\text{original Lean local family}
\longleftrightarrow
\kappa_v+L_v
=
\operatorname{Char}_{q_v}(L_v).
$$

It then proves rank-three compatibility through the quadratic-Lagrangian
intersection theorem.

This identification and the invariant proof are paper-level mathematics until
separately formalized. The existing Lean theorem and the canonical corpus should
therefore be treated as corresponding presentations with a documented
mathematical identification, not as literally the same checked term.

## 4. Cover factorization and outer reduction not yet machine-checked

The canonical graph-theoretic factorization is

$$
\begin{array}{c}
\text{finite bridgeless multigraph}\
\downarrow\;\text{delete loops}\
\text{loopless bridgeless core}\
\downarrow
\text{cubic expansion with rank-three flow}\
\downarrow
\text{compatible affine family}\
\downarrow
\text{graph-level multiset even double cover}\
\downarrow
\text{vertex-even/cut-even bridge on the loopless expansion}\
\downarrow
\text{pure cut-even collapse transport}\
\downarrow
\text{even double cover of the loopless original core}\
\downarrow
\text{one final circuit decomposition}\
\downarrow\;\text{reinsert two singleton circuits per loop}\
\text{cycle double cover of the original multigraph}.
\end{array}
$$

The current Lean proof passes through relevant even supports internally, but the
following have not yet been formalized as the approved architecture:

- a named graph-level even-double-cover predicate and construction theorem;
- finite-support circuit decomposition at its weakest natural hypothesis;
- vertex-even/cut-even bridge lemmas under the current loopless convention;
- pure cut-even graph-collapse transport;
- loop deletion and singleton-loop reinsertion;
- the independent port-cycle expansion and the expansion-first outer shell;
- adaptive prefix avoidance and the flow-preserving adaptive expansion;
- the isolated classical `BinaryEightFlow` interface, including componentwise
  assembly and the loopless characteristic-two adapter;
- the full unconditional theorem.

The chapter
[`reduction/even-cover-and-collapse.md`](reduction/even-cover-and-collapse.md)
records the present mathematical factorization. It is not itself evidence that
these statements are already checked.

## 5. Paper-proof layer

The following canonical chapters contain written theorem-level arguments:

- [`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md);
- [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md);
- [`reduction/outer-shell-and-binary-flow.md`](reduction/outer-shell-and-binary-flow.md);
- [`reduction/even-cover-and-collapse.md`](reduction/even-cover-and-collapse.md);
- [`rank-hierarchy/transgression-and-dual-fano-residue.md`](rank-hierarchy/transgression-and-dual-fano-residue.md);
- [`rank-hierarchy/rank-four-first-obstruction.md`](rank-hierarchy/rank-four-first-obstruction.md);
- [`reduction/incidence-to-tensor-complex.md`](reduction/incidence-to-tensor-complex.md);
- [`tensor/code-flag-complex.md`](tensor/code-flag-complex.md);
- [`tensor/exact-sequences-and-functoriality.md`](tensor/exact-sequences-and-functoriality.md);
- [`tensor/torsion-and-rigidity.md`](tensor/torsion-and-rigidity.md);
- [`gauge/gauge-modes-and-circuits.md`](gauge/gauge-modes-and-circuits.md);
- [`gauge/interface-gluing.md`](gauge/interface-gluing.md).

“Theorem-level” means that a mathematical statement and argument are written. It
does not mean peer review, independent line-by-line audit, or Lean formalization.

The chapter
[`reduction/outer-shell-and-binary-flow.md`](reduction/outer-shell-and-binary-flow.md)
now gives the paper-level outer-shell packet. It proves the finite-active-edge
port-cycle expansion, exact collapse data, preservation of bridgelessness, the
adaptive binary ordering theorem, and both the expansion-first and adaptive
flow-first routes. Its `BinaryEightFlow` node remains a classical external
Seymour--Tutte input. None of the outer shell, adaptive ordering, or the
Seymour--Tutte input is thereby machine-checked.

The verified Seymour source is P. D. Seymour, “Nowhere-zero 6-flows”,
*Journal of Combinatorial Theory, Series B* **30** (1981), 130–135, DOI
`10.1016/0095-8956(81)90058-7`. The exact primary Tutte theorem and page pinpoint
remain an unresolved publication source gate; the existence theorem and the
flow-counting theorem must continue to be cited as distinct statements.

## 6. Exact computational layer

Exact finite calculations support:

- local residue identities in small ranks;
- the canonical rank-four $K_{3,3}$ obstruction;
- the triangular-prism comparison;
- small-graph gauge-circuit censuses;
- selected matrices in the incidence-to-tensor bridge.

These calculations verify examples, expose obstructions, and detect errors. They
do not replace the general proofs.

## 7. Conditional and programmatic layer

The following claims remain conditional or programmatic:

- “mixed Schur–Koszul complex” as established terminology or a novel general
  theory;
- a complete categorical treatment of deletion, contraction, and arbitrary
  graph interfaces;
- decorated higher-rank residues beyond the scalar compatibility criterion;
- integral or polynomial lifts of binary tensor torsion;
- transition-matroid, delta-matroid, embedding, Petrial, and surface-polynomial
  theories whose source bodies are absent from the current tree;
- publication-level novelty claims before a proper literature comparison.

## 8. Reliability rules

1. A clean invariant reformulation does not inherit Lean status from an older
   equivalent-looking implementation without a checked bridge.
2. A finite computation supports an example or identity but does not establish
   an all-rank theorem.
3. A cubic-flow cycle double cover is not the unconditional CDC theorem.
4. The approved full finite bridgeless-multigraph theorem is the natural external
   target; the current loopless ambient-finite Lean declaration is an unchanged
   implementation checkpoint.
5. An approved migration direction is not an implemented declaration.
6. Historical filenames, prompts, and superseded ontologies are not current
   mathematical authority.
7. Director-reviewed paper proofs of adaptive ordering and the outer shell do not
   acquire Lean status; Seymour and Tutte remain external until an explicit
   formal theorem boundary or implementation is accepted.

## 9. Scope of the canonical integration

The canonical corpus integrates every active mathematical Markdown dossier that
was present on `main` at the start of the reorganization. It does not claim to
reconstruct material available only as a filename and hash in the dated
snapshot. That boundary is recorded in
[`topology/README.md`](topology/README.md).

Git history preserves superseded formulations and discovery order. Their former
existence is not evidence that their terminology, theorem hierarchy, or
reliability status remains current.
