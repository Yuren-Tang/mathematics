# Complete Cycle Double Cover theorem

This directory is the controlling Programme A surface for the complete Cycle Double Cover theorem.

## Natural theorem

> Every multigraph with finite active edge set and no singleton cut has a finite circuit double cover.

Loops, parallel edge objects, disconnected components, isolated vertices, and an arbitrary ambient vertex carrier are allowed. Every active edge object occurs in exactly two indexed circuit occurrences.

## Exact sources and assurance

- immutable authorial A0–A10 source: `proof-development/affine-cdc-rigour-v1@8bee16780b549f51e1f29343671a059961ec4172`;
- original Curator candidate: `curation/affine-cdc-programme-a-v1@68715fb29bb4b6555e2bc3e089603c5390d01566`;
- Independent Audit A: `audit/affine-cdc-complete-cdc-spine-v1@2fac31f4e76c819dd42a179a2772501c50ee93ad`;
- Audit A result: `VERIFIED SUBJECT TO NAMED EXTERNAL THEOREMS / NON-BLOCKING EXPLICITNESS REPAIRS`;
- immutable repair checkpoint: `proof-development/affine-cdc-rigour-v1@06bce656dcf5bfd6491ec08f51a702ea56d2470d`.

The three returned explicitness items are closed as

`EXPOSITORY-REPAIR / NO-THEOREM-CHANGE / NO-NEW-MATHEMATICS`.

## Controlling reading order

1. [`foundations-expansion-and-flow.md`](foundations-expansion-and-flow.md) — A0–A3 foundations, loop normalization, expansion, and binary-flow boundary.
2. [`audit-a-explicitness-repairs.md`](audit-a-explicitness-repairs.md) — controlling replacements for the exact Seymour convention, the full A4 reverse reconstruction, and the status of the old Tutte route.
3. [`affine-compatibility-and-extraction.md`](affine-compatibility-and-extraction.md) — A4–A7 affine compatibility and indexed even-support extraction, read together with the complete reverse proof in the repair chapter.
4. [`collapse-decomposition-and-assembly.md`](collapse-decomposition-and-assembly.md) — A8–A10 collapse, decomposition, loop reinsertion, and final assembly.

The repair chapter is not an additional theorem premise. It is the controlling integrated projection of the PDL overlay for the named compressed passages.

## Logical external input

The sole non-elementary external logical input is Seymour’s nowhere-zero six-flow theorem, used for finite connected loopless multigraphs with parallel edge objects allowed and then assembled componentwise.

The transport

$$
\mathbf Z/8\mathbf Z\longrightarrow\mathbf F_2^3
$$

is proved internally from the flow-kernel cardinality formula and inclusion–exclusion. Tutte’s equal-order theorem is historical provenance only.

## Historical companion

`reduction/outer-shell-and-binary-flow.md` remains useful historical and mechanism-level material, but §§4.1–4.2 are not controlling. Read the prominent status file

[`../reduction/OUTER_SHELL_HISTORICAL_ROUTE_NOTICE.md`](../reduction/OUTER_SHELL_HISTORICAL_ROUTE_NOTICE.md).

## Provenance controls

- [`../PROGRAMME_A_INTEGRATION_MAP.md`](../PROGRAMME_A_INTEGRATION_MAP.md);
- [`../AC_UNIFIED_INTEGRATION_MAP.md`](../AC_UNIFIED_INTEGRATION_MAP.md);
- [`../AC_UNIFIED_ASSURANCE_BOUNDARY.md`](../AC_UNIFIED_ASSURANCE_BOUNDARY.md);
- exact source dossiers under [`../proof-development/`](../proof-development/).

## Assurance boundary

Programme A’s original theorem spine has passed Independent Audit A. The repaired passages are closed and Curator-integrated, but this alignment does not claim a second independent re-audit of the repaired prose, end-to-end Lean verification, manuscript approval, peer review, publication, release, arXiv, DOI, novelty, or timestamp action.