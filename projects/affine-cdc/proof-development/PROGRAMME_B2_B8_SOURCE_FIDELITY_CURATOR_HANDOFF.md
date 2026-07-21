# CURATION-HANDOFF — AffineCDC B2/B8 source fidelity

**Prepared by:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Authority:** research-workbench issue #37 comment `5028845743`  
**Branch:** `proof-development/affine-cdc-rigour-v1`  
**Authorial repair checkpoint:** `58f2a5e1b95257b4f276f5ea45f6268521e92305`  
**DAG registration:** `986d89ed9b0e6f5d403084f66022e7893e7417c9`  
**Fixed audited object:** `curation/affine-cdc-programme-a-b1-b8-unified-v1@ec765cd03271abd3588ec36faec3d53d0f8aa03b` — unchanged  
**Classification:** `READY-FOR-CURATOR / SOURCE-FIDELITY-REPAIRED / NO-THEOREM-CHANGE`

## 1. Exact source result

No exact committed source was recovered for the arbitrary-rank claim described by

\[
V=\Gamma\oplus\Gamma^*,
\qquad
d_h(a)=([a],\operatorname{ev}_a),
\qquad
O^+(2r,2),
\]

as a complete additive anisotropic-root model for all pairs of the `2^r` points of `F_2^r`.

Its classification is:

`SOURCE-UNRECONSTRUCTED / INFERRED-EXTRAPOLATION OR UNCOMMITTED DRAFT / MATHEMATICALLY REFUTED BY B2.3`.

The controlling intake permits this classification when no committed source exists, so the return is `READY-FOR-CURATOR`, not `BLOCKED-SOURCE`.

## 2. Search boundary

The bounded search covered:

1. the historical rank-hierarchy line through `main@960c92b...`, including `rank-hierarchy/transgression-and-dual-fano-residue.md` and commit `79e6a7ae12293c06f853e1b4f0291ea88d99a88e`;
2. the complete five-support source interval from `main@749e0579581fcc838685138b3582f4de306b8e72` to `research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`, containing eighty-two commits and seventy-eight packets;
3. the exact packet blob `2043ada9d28789ecc5f4f0028e62133f37835bc1`, introduced by `a172b2acb13fc0b042ecb099a08b9631ab1db59a`;
4. plausible orthogonal, anisotropic, singular-quotient, root-flow, rank-four, universal-module and rank-hierarchy packets;
5. the original PDL B2/B8 files, accepted B2 checkpoint, fixed candidate and Audit B ledgers;
6. exact and semantic searches for `Γ⊕Γ*`, `d_h(a)`, `ev_a`, `2r`, `O^+(2r,2)`, universal orthogonal roots, complete-graph roots and triangle addition.

The detailed record is `AC_PD_B2_3_SOURCE_FIDELITY_REPAIR.md`.

## 3. Restored exact provenance

`FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md` is valid theorem-level historical source for:

- the eight-coordinate even-weight module `H_8`;
- the Hamming kernel and moment map;
- the six-dimensional plus-type quotient `O^+(6,2)`;
- its twenty-eight anisotropic roots;
- rank-three AffineCDC root lifts;
- five-coordinate `O^-(4,2)` slices and omitted-triple orthogonality.

It contains no arbitrary-rank tower and must not be classified in toto as false or history-only.

The genuine all-rank transgression/residue hierarchy remains valid but explicitly distinguishes higher rank from the unique rank-three quadratic-Lagrangian case.

## 4. Mathematical correction retained

B2.3 still proves:

\[
\boxed{\dim V\ge q-2}
\]

for every additive anisotropic representation of `K_q` satisfying triangle addition, and constructs the deleted permutation module of dimension `q-2` attaining the bound.

For `q=2^r`, dimension `2r` is impossible for `r≥4`. Rank three is exceptional because `8-2=6=2·3`.

## 5. Authorial repair packet

The repair includes:

- corrected `AC_PD_B2_3_ORTHOGONAL_ROOT_MODULE_CORRECTION.md`;
- `AC_PD_B2_3_SOURCE_FIDELITY_REPAIR.md`;
- corrected `AC_PD_B2_FORMULATION_AND_WITNESS_MAP.md`;
- corrected `PROGRAMME_B2_CURATOR_HANDOFF.md`;
- `AC_PD_B8_SOURCE_FIDELITY_ADDENDUM.md`;
- corrected `PROGRAMME_B8_CURATOR_HANDOFF.md`;
- updated `OBLIGATION_DAG.md`.

The original B2 and B8 checkpoints remain recoverable. The new packet supersedes only their erroneous provenance statements.

## 6. Required replacement-candidate propagation

After AC-DIR supplies the exact replacement branch/base, Curator must repair:

- B2 formulation, root-lift and proof-family chapters;
- the B8 source-assurance chapter;
- `CHAPTER_PROVENANCE.md`;
- `MIGRATION_LEDGER.md`;
- `RETIRED_SOURCE_CLASSIFICATION.md`;
- `SUPERSESSION_MAP.md`;
- `SOURCE_RECOVERY_AUDIT.md`;
- B2 integration/final-audit maps;
- dependency, architecture, active-surface, current-best, formal-status, reconstruction and unified-status surfaces.

The source-unreconstructed extrapolation is not one of the seventy-eight packets. The packet partition must be recomputed after restoring the named packet’s valid class.

## 7. Re-audit boundary

The corrected replacement must return for a bounded B2/B8 source-fidelity re-audit checking attribution, packet roles, packet counts, migration/supersession consistency, assurance synchronization and preservation of the `q-2` theorem.

This authorial repair is not itself an independent audit.

## 8. Unchanged scope

Programme A, B1, B3–B7, B9, all six AC-RL frontier obligations and the open status of the global five-support theorem are unchanged.

Only `projects/affine-cdc/proof-development/` on the persistent branch is modified. The fixed candidate, audit, Curator, default, public-warning, Research Lead, Lean, manuscript, release, publication, arXiv, DOI and tag surfaces are unchanged.

This completes the bounded PDL repair and returns it for Curator intake.