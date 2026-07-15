# Migration ledger

This ledger records the transition from the historical flat directory of theorem
dossiers to the canonical mathematical corpus. It is organized by source file,
not by discovery date. A source is removed from the active tree only after its
substantive mathematical content has a named destination below. Git history
preserves every deleted source verbatim.

Status terms:

- **merged** — all substantive content is integrated into one canonical chapter;
- **split** — distinct mathematical components were moved to different chapters;
- **superseded** — a later theorem corrects or strictly strengthens the source;
- **example absorbed** — an example is retained inside the theorem it tests;
- **programme deferred** — the source body is absent or the claim remains
  programmatic.

## 1. Compatibility core

| Historical source | Canonical destination | Action and mathematical decision |
|---|---|---|
| `affine-incidence-pair-complex.md` | [`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md) | **Merged.** The pair complex, its $H^0/H^1$, affine class, quotient-sheaf cancellation, and dual stress complex now form one rank-independent chapter. |
| `theory-map-v1-affine-incidence-pair.md` | [`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md), [`reduction/incidence-to-tensor-complex.md`](reduction/incidence-to-tensor-complex.md) | **Split and superseded.** Its compatibility image is retained; its provisional description of the tensor complex as a compression is replaced by the later chain-level zigzag. |
| `fano-quadratic-lagrangian-package.md` | [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md) | **Merged.** The canonical quadratic plane, local Lagrangian, characteristic torsor, legal dual configurations, cross-bit, and support parity are one local theorem package. |
| `affine-lagrangian-intersection.md` | [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md) | **Merged.** The abstract characteristic-torsor intersection theorem and its global application are now the central positive proof. |
| `fano-quadratic-transgression.md` | [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md), [`rank-hierarchy/transgression-and-dual-fano-residue.md`](rank-hierarchy/transgression-and-dual-fano-residue.md) | **Split.** The rank-three quadratic identity and support-boundary proof are equivalent views of the core theorem; the odd-valence plane-supported extension is preserved explicitly. |

## 2. Rank hierarchy

| Historical source | Canonical destination | Action and mathematical decision |
|---|---|---|
| `rank-three-coincidence-principle.md` | [`rank-hierarchy/transgression-and-dual-fano-residue.md`](rank-hierarchy/transgression-and-dual-fano-residue.md) | **Merged.** Support degree, local half-dimension, quotient-sheaf index, and quadraticity now appear as one rank-three coincidence theorem. |
| `higher-degree-fano-transgression.md` | [`rank-hierarchy/transgression-and-dual-fano-residue.md`](rank-hierarchy/transgression-and-dual-fano-residue.md) | **Merged.** The all-rank degree-lowering identity and outside-plane parity are the positive first half of the rank hierarchy. |
| `dual-fano-residue-theorem.md` | [`rank-hierarchy/transgression-and-dual-fano-residue.md`](rank-hierarchy/transgression-and-dual-fano-residue.md) | **Merged as controlling theorem.** The hidden annihilator-plane residue is the complete all-rank compatibility criterion. |
| `rank-four-cubic-directional-residue.md` | [`rank-hierarchy/rank-four-first-obstruction.md`](rank-hierarchy/rank-four-first-obstruction.md) | **Merged as specialization.** The alternating-form quotient, cross-bit, Pfaffian, cubic residue, and global formula are the rank-four equation of the all-rank residue. |
| `rank-four-k33-residue-example.md` | [`rank-hierarchy/rank-four-first-obstruction.md`](rank-hierarchy/rank-four-first-obstruction.md) | **Example absorbed.** The explicit flow matrix, essential stress, local residue table, and incompatibility computation are retained in full. |
| `rank-four-six-vertex-dichotomy.md` | [`rank-hierarchy/rank-four-first-obstruction.md`](rank-hierarchy/rank-four-first-obstruction.md) | **Merged.** The triangular-prism solution and the $K_{3,3}$ obstruction are presented together as the minimal sharpness theorem. |
| `symplectic-vertex-plane-parity.md` | [`rank-hierarchy/rank-four-first-obstruction.md`](rank-hierarchy/rank-four-first-obstruction.md) | **Merged as interpretation.** Global symplectic parity and the essential local anomaly now follow the rank-four residue theorem. |

## 3. Incidence-to-tensor reduction

| Historical source | Canonical destination | Action and mathematical decision |
|---|---|---|
| `incidence-tensor-comparison.md` | [`reduction/incidence-to-tensor-complex.md`](reduction/incidence-to-tensor-complex.md) | **Merged and corrected.** The cohomological exact sequences are retained. The statement that no chain-level quotient was known is removed because it was superseded by the later bridge. |
| `chain-level-incidence-tensor-bridge.md` | [`reduction/incidence-to-tensor-complex.md`](reduction/incidence-to-tensor-complex.md) | **Merged as controlling refinement.** The universal tension resolution, lifted incidence complex, extended quotient sheaf, and canonical zigzag now govern the relation. |

## 4. Tensor and code theory

| Historical source | Canonical destination | Action and mathematical decision |
|---|---|---|
| `flow-tensor-datum.md` | [`reduction/incidence-to-tensor-complex.md`](reduction/incidence-to-tensor-complex.md), [`tensor/code-flag-complex.md`](tensor/code-flag-complex.md), [`tensor/torsion-and-rigidity.md`](tensor/torsion-and-rigidity.md), [`gauge/gauge-modes-and-circuits.md`](gauge/gauge-modes-and-circuits.md) | **Split and ontology corrected.** Every theorem is retained, but the historical claim that the tensor datum is the master compatibility object is rejected. |
| `flow-tensor-theory-foundations-v0.md` | [`tensor/code-flag-complex.md`](tensor/code-flag-complex.md), [`tensor/exact-sequences-and-functoriality.md`](tensor/exact-sequences-and-functoriality.md), [`tensor/torsion-and-rigidity.md`](tensor/torsion-and-rigidity.md) | **Split.** Definitions, index, enhancements, exact sequences, and validation tests are assigned to their actual theorem blocks. |
| `code-flag-schur-koszul.md` | [`tensor/code-flag-complex.md`](tensor/code-flag-complex.md) | **Merged.** Based quotient data, nested code flags, Schur multiplication, syzygies, constraint matroid, matroid quotient, and recognition caveat now form one abstract chapter. |
| `divided-square-exact-sequence.md` | [`tensor/exact-sequences-and-functoriality.md`](tensor/exact-sequences-and-functoriality.md), [`tensor/torsion-and-rigidity.md`](tensor/torsion-and-rigidity.md) | **Split.** The canonical exact sequence and Veronese quotient are structural; their determinant-line consequence belongs to torsion. |
| `coefficient-quotient-exact-sequence.md` | [`tensor/exact-sequences-and-functoriality.md`](tensor/exact-sequences-and-functoriality.md) | **Merged.** The relative wedge complex, long exact sequence, and rank-drop formulas remain together. |
| `flow-tensor-morphisms-and-automorphisms.md` | [`tensor/code-flag-complex.md`](tensor/code-flag-complex.md) | **Merged.** Diagonal coalgebra maps, strict morphisms, code-flag automorphisms, forgotten structure, and categorical limits are one section. |
| `fano-torsion.md` | [`tensor/torsion-and-rigidity.md`](tensor/torsion-and-rigidity.md) | **Merged.** The top wedge, rigidity criterion, basis-packing expansion, Hodge relation, and cut behaviour form one invariant theorem. |

## 5. Gauge, circuits, and interfaces

| Historical source | Canonical destination | Action and mathematical decision |
|---|---|---|
| `harmonic-cut-quotients.md` | [`gauge/gauge-modes-and-circuits.md`](gauge/gauge-modes-and-circuits.md) | **Merged as controlling geometric theorem.** Gauge words, tensor dependencies, and flow–tension quotients are proved equivalent. |
| `even-gauge-code.md` | [`gauge/gauge-modes-and-circuits.md`](gauge/gauge-modes-and-circuits.md) | **Merged.** Third-order bicycle orthogonality, evenness in rank at most three, and the rank-four $K_6$ sharpness example are retained. |
| `weight6-circuit-classification.md` | [`gauge/gauge-modes-and-circuits.md`](gauge/gauge-modes-and-circuits.md) | **Merged.** The complete proof and low-weight table through weight six are retained; weight eight remains open. |
| `interface-correspondence.md` | [`gauge/interface-gluing.md`](gauge/interface-gluing.md) | **Merged.** Cycle-space fiber products, cographic pushouts, mixed variance, theta interfaces, and two-/three-edge laws are one gluing theorem. |
| `interface-line-duality.md` | [`gauge/interface-gluing.md`](gauge/interface-gluing.md) | **Merged as refinement.** The common line $L_S$, matching quotient $\Gamma/L_S$, universal exact sequences, affine fibers, and cap-extension scope are integrated. |

## 6. Working syntheses and navigation

| Historical source | Canonical destination | Action and mathematical decision |
|---|---|---|
| `current-synthesis.md` | all canonical chapters; especially [`MATHEMATICAL_ARCHITECTURE.md`](MATHEMATICAL_ARCHITECTURE.md) and [`FORMAL_STATUS.md`](FORMAL_STATUS.md) | **Superseded.** Its mathematics is distributed to theorem chapters; discovery-stage sections and repeated proofs are not retained as parallel exposition. |
| `NOTE_MAP_AND_STATUS.md` | this ledger and [`FORMAL_STATUS.md`](FORMAL_STATUS.md) | **Superseded.** The old ledger classified dossiers; the new ledger records completed migration and current reliability. |
| historical project `README.md` | [`README.md`](README.md) | **Rewritten.** The entry point now links only to canonical chapters. |
| first version of `MATHEMATICAL_ARCHITECTURE.md` | [`MATHEMATICAL_ARCHITECTURE.md`](MATHEMATICAL_ARCHITECTURE.md) | **Rewritten.** It is reduced to a dependency map and no longer duplicates full proofs. |
| first version of `PUBLICATION_PROGRAM.md` | [`PUBLICATION_PROGRAM.md`](PUBLICATION_PROGRAM.md) | **Rewritten.** Paper blocks cite canonical chapters rather than historical dossiers. |

## 7. Snapshot-only topological sources

The source bodies named in the 2026-07-14 manifest are absent from the active
tree. Their status is recorded in
[`topology/README.md`](topology/README.md).

The older quotient-sheaf, tensor, determinant, cut, higher-rank, and $K_{3,3}$
themes have active replacements. The detailed embedding, Petrial, transition,
delta-matroid, surface-census, and state-polynomial content remains
**programme deferred** until the source bodies are restored and read.

## 8. Completeness criterion for this migration

The migration is complete with respect to the active Markdown mathematics that
was present on `main` when the work began if all of the following hold:

1. every source above has a canonical destination;
2. every unique theorem, proof mechanism, example, counterexample, exact
   sequence, and explicit limitation has been preserved;
3. superseded conclusions are absent from the canonical chapters;
4. only `$...$` and `$$...$$` are used as TeX delimiters;
5. internal links resolve within the new hierarchy;
6. the snapshot-only boundary is not represented as reconstructed mathematics;
7. Git history, rather than duplicate active files, preserves the historical
   formulations.

The final audit checks these conditions before the branch can replace `main`.