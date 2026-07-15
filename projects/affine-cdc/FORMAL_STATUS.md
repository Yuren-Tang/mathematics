# Formalization and reliability boundary

This file separates machine-checked results, protected public statements, paper
proofs, exact computations, and open programmes. It is part of the mathematical
content: a theorem does not inherit a stronger status merely because it has
been rewritten in a more invariant language or placed in a cleaner architecture.

## 1. Protected public statement layer

The companion repository
[`Yuren-Tang/affine-cdc`](https://github.com/Yuren-Tang/affine-cdc) contains a
self-contained Mathlib-only audit file `Statement.lean`. Its protected endpoint
is the project's finite loopless multigraph formulation of the unconditional
Cycle Double Cover conjecture.

That public audit statement is **defined but not yet proved** in the companion
repository. The mathematical reorganization in this repository does not alter
its hypotheses, conclusion, loop convention, finiteness convention, or graph
model.

Any future change to the protected public statement is a separate author-level
decision. Internal mathematical generalization does not silently rewrite the
claim being audited.

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
The Lean repository does not yet contain a theorem inhabiting the protected
`CDCStatement` for every finite loopless bridgeless multigraph.

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
\text{compatible affine family}
\longrightarrow
\text{even double cover}
\longrightarrow
\text{cut-even transport through collapse}
\longrightarrow
\text{even double cover of the original graph}
\longrightarrow
\text{cycle double cover}.
$$

The current Lean proof passes through the relevant even supports internally, but
the following have not yet been formalized as the approved architecture:

- a named graph-level even-double-cover predicate and construction theorem;
- finite-support circuit decomposition at its weakest natural hypothesis;
- vertex-even/cut-even bridge lemmas under the protected loop convention;
- pure cut-even graph-collapse transport;
- the independent cubic expansion and flow shell;
- the final unconditional theorem.

The chapter
[`reduction/even-cover-and-collapse.md`](reduction/even-cover-and-collapse.md)
records the present mathematical factorization. It is not itself evidence that
these statements are already checked.

## 5. Paper-proof layer

The following canonical chapters contain written theorem-level arguments:

- [`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md);
- [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md);
- [`reduction/even-cover-and-collapse.md`](reduction/even-cover-and-collapse.md);
- [`rank-hierarchy/transgression-and-dual-fano-residue.md`](rank-hierarchy/transgression-and-dual-fano-residue.md);
- [`rank-hierarchy/rank-four-first-obstruction.md`](rank-hierarchy/rank-four-first-obstruction.md);
- [`reduction/incidence-to-tensor-complex.md`](reduction/incidence-to-tensor-complex.md);
- [`tensor/code-flag-complex.md`](tensor/code-flag-complex.md);
- [`tensor/exact-sequences-and-functoriality.md`](tensor/exact-sequences-and-functoriality.md);
- [`tensor/torsion-and-rigidity.md`](tensor/torsion-and-rigidity.md);
- [`gauge/gauge-modes-and-circuits.md`](gauge/gauge-modes-and-circuits.md);
- [`gauge/interface-gluing.md`](gauge/interface-gluing.md).

“Theorem-level” means that a mathematical statement and argument are written.
It does not mean peer review, independent line-by-line audit, or Lean
formalization.

The outer expansion/flow theorem packet required for the unconditional CDC shell
is not yet a closed canonical chapter in this repository. Its absence is a
mathematical and formalization gap, not merely an editorial gap.

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
4. The protected public statement is the claim the project must ultimately
   prove; internal architecture may be generalized without changing that audit
   surface.
5. Historical filenames, prompts, and superseded ontologies are not current
   mathematical authority.

## 9. Scope of the canonical integration

The canonical corpus integrates every active mathematical Markdown dossier that
was present on `main` at the start of the reorganization. It does not claim to
reconstruct material available only as a filename and hash in the dated
snapshot. That boundary is recorded in
[`topology/README.md`](topology/README.md).

Git history preserves superseded formulations and discovery order. Their former
existence is not evidence that their terminology, theorem hierarchy, or
reliability status remains current.