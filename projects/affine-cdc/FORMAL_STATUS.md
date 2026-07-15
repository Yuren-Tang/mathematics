# Formalization and reliability boundary

This file separates machine-checked results, paper proofs, exact computations,
and open programmes. It is part of the mathematical content: a theorem should
not inherit a stronger status merely because it has been rewritten in a more
invariant language.

## 1. Companion Lean repository

The companion repository
[`Yuren-Tang/affine-cdc`](https://github.com/Yuren-Tang/affine-cdc) is the
machine-checked anchor for the original AffineCDC construction. According to the
current project record, it contains the verified local classification, global
compatibility theorem, and cycle-double-cover extraction in the original
formal API.

The following bridge still requires explicit formalization:

$$
\text{original Lean local family}
\longleftrightarrow
\kappa_v+L_v
=
\operatorname{Char}_{q_v}(L_v).
$$

Until that bridge and the invariant proofs are formalized, the Lean theorem and
the canonical mathematical corpus should be treated as corresponding
presentations with a documented mathematical identification, not as literally
the same checked term.

## 2. Paper-proof layer

The following canonical chapters contain written theorem-level arguments:

- [`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md);
- [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md);
- [`rank-hierarchy/transgression-and-dual-fano-residue.md`](rank-hierarchy/transgression-and-dual-fano-residue.md);
- [`rank-hierarchy/rank-four-first-obstruction.md`](rank-hierarchy/rank-four-first-obstruction.md);
- [`reduction/incidence-to-tensor-complex.md`](reduction/incidence-to-tensor-complex.md);
- [`tensor/code-flag-complex.md`](tensor/code-flag-complex.md);
- [`tensor/exact-sequences-and-functoriality.md`](tensor/exact-sequences-and-functoriality.md);
- [`tensor/torsion-and-rigidity.md`](tensor/torsion-and-rigidity.md);
- [`gauge/gauge-modes-and-circuits.md`](gauge/gauge-modes-and-circuits.md);
- [`gauge/interface-gluing.md`](gauge/interface-gluing.md).

These arguments are concrete and mostly basis-free, but they have not all
received independent line-by-line review or Lean formalization. “Theorem-level”
means that a proof is written, not that peer review has occurred.

## 3. Exact computational layer

Exact finite calculations support:

- the local residue identities in small ranks;
- the canonical rank-four $K_{3,3}$ obstruction;
- the triangular-prism comparison;
- small-graph gauge-circuit censuses;
- selected matrices in the incidence-to-tensor bridge.

These calculations verify examples and detect errors. They do not replace the
general proofs.

## 4. Conditional and programmatic layer

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

## 5. Scope of the present integration

The canonical corpus integrates every active mathematical Markdown dossier that
was present on `main` at the start of the reorganization. It does not claim to
reconstruct material available only as a filename and hash in the dated
snapshot. That boundary is recorded in
[`topology/README.md`](topology/README.md).

Git history preserves superseded formulations and discovery order. Their former
existence is not evidence that their terminology or ontology remains current.