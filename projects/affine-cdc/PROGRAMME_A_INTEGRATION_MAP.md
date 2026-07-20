# Programme A integration and provenance map

## 1. Exact intake

- canonical base: `main@960c92b7ff231c78b387894149779083060a75eb`;
- immutable source: `proof-development/affine-cdc-rigour-v1@8bee16780b549f51e1f29343671a059961ec4172`;
- writable branch: `curation/affine-cdc-programme-a-v1`;
- consumed scope: A0–A10 and the Programme A part of `proof-development/OBLIGATION_DAG.md`;
- excluded scope: B1 and every later proof-development commit.

The source checkpoint is seventeen commits ahead of the canonical base and zero behind. Its file delta consists only of the eleven A0–A10 dossiers and `OBLIGATION_DAG.md`.

## 2. Integration architecture

| Active destination | Integrated source units | Mathematical role |
|---|---|---|
| `complete-cdc/foundations-expansion-and-flow.md` | A0, A1, A2, A3 | Natural multigraph/circuit/multiplicity semantics; loop normalization; port-cycle expansion; Seymour boundary; internal equal-order flow transport. |
| `complete-cdc/affine-compatibility-and-extraction.md` | A4, A5, A6, A7 | Pair complex and equivalent obstructions; quadratic Fano compatibility; retained graph/dart extraction; exact loopless parity bridge. |
| `complete-cdc/collapse-decomposition-and-assembly.md` | A8, A9, A10 | Cut-even collapse; occurrence transport; terminating circuit decomposition; final theorem and boundary cases. |
| `complete-cdc/README.md` | A10, obligation DAG | Natural reading order, theorem headline, logical source boundary, and assurance warning. |

Existing specialized chapters under `core/` and `reduction/` remain useful mechanism-level companions. Programme A supplies the controlling end-to-end proof spine and exact dependency closure.

## 3. Exact unit ledger

| Unit | Authorial state | Exact checkpoint | Active destination |
|---|---|---|---|
| A0 | `COMPLETE-DRAFT` | `0d8c9102fa117e5f58b5d1617f3fae782c164097` | foundations chapter §§1–3 |
| A1 | `COMPLETE-DRAFT` | `b193d55461040a6b6b7692e4f24e91d88c97a663` | foundations chapter §4; assembly chapter §8 step 2 and step 11 |
| A2 | `COMPLETE-DRAFT` | `7c271c41f9d442ddb14034fb40b730fcc61c83a5` | foundations chapter §5; assembly chapter §2 |
| A3 | `COMPLETE-DRAFT` | `6817896a301157db886f7c016866748a9161d15f` | foundations chapter §6; assembly chapter §10 |
| A4 | `COMPLETE-DRAFT` | `93bd8019099f0fa10ee53928681167f81506c407` | affine chapter §§1–4 |
| A5 | `COMPLETE-DRAFT` | `6ce41bd87b5700346c572f701c40c8ac6f374e3f` | affine chapter §§5–7 |
| A6 | `COMPLETE-DRAFT` | `f953619d6fda7105fef406892530496c7d72178a` | affine chapter §§8–9 |
| A7 | `COMPLETE-DRAFT` | `b0755c3b95939482c6e223c24e4d8327c53f02e8` | affine chapter §10 |
| A8 | `COMPLETE-DRAFT` | `d9718c6204d4f11aa853ee2f6e350d5c08444820` | assembly chapter §§1–4 |
| A9 | `COMPLETE-DRAFT` | `400404e5413dfc933668aa0ec152010bae5a742c` | assembly chapter §§5–7 |
| A10 | `READY-FOR-CURATOR` | `143538ef0fc9518ce877a42fa422d57cb6e3ce8a` | assembly chapter §§8–12 and all root control surfaces |

The immutable aggregate checkpoint is `8bee16780b549f51e1f29343671a059961ec4172`.

## 4. Source retention

The exact source files remain present under `projects/affine-cdc/proof-development/`:

- `AC_PD_A0_FOUNDATIONAL_SEMANTICS.md`;
- `AC_PD_A1_LOOP_DELETION_AND_REINSERTION.md`;
- `AC_PD_A2_PORT_CYCLE_EXPANSION.md`;
- `AC_PD_A3_BINARY_EIGHT_FLOW_BOUNDARY.md`;
- `AC_PD_A4_AFFINE_PAIR_COMPLEX.md`;
- `AC_PD_A5_RANK_THREE_FANO_COMPATIBILITY.md`;
- `AC_PD_A6_GRAPH_LEVEL_EVEN_SUPPORT_EXTRACTION.md`;
- `AC_PD_A7_VERTEX_BOUNDARY_CUT_PARITY_BRIDGE.md`;
- `AC_PD_A8_COLLAPSE_EVEN_COVER.md`;
- `AC_PD_A9_FINITE_CIRCUIT_DECOMPOSITION.md`;
- `AC_PD_A10_COMPLETE_CDC_ASSEMBLY.md`;
- `OBLIGATION_DAG.md`.

They are retained because they are the exact authorial proof-development record, contain intermediate theorem numbering and local verification details, and form the recovery surface for later audit, PDL repair, Lean projection, and manuscript work.

They are no longer the preferred reading order for the current corpus. The three integrated chapters are controlling for exposition and dependency architecture.

## 5. Material corrections integrated

1. Circuit semantics and characterization belong to A0; finite decomposition belongs to A9.
2. Intrinsic half-edge boundary parity is the natural loop-aware notion; once-per-edge incidence parity is loopless only.
3. The pair complex is the complete compatibility object but does not retain graph/dart/indexed-support semantics.
4. Equal-order finite-group flow transport is internally proved; Tutte is provenance, not a logical gate.
5. Collapse preserves cut-even supports and indexed occurrence multiplicity, not circuits.
6. Equal support values at distinct indices remain distinct occurrences.
7. The natural theorem assumes only finite active edge set and no singleton cut; connectedness, simplicity, looplessness, finite ambient vertex carrier, and absence of isolated vertices are unnecessary.

## 6. External-source map

### Logical input

P. D. Seymour, “Nowhere-zero 6-flows”, Journal of Combinatorial Theory, Series B 30 (1981), 130–135, DOI `10.1016/0095-8956(81)90058-7`.

It is used only to obtain a componentwise nowhere-zero integral six-flow on the finite loopless no-isthmus expansion.

### Historical provenance

Tutte’s equal-order group-flow theory explains the classical context, but Programme A proves the required counting and transport statement internally. Exact Tutte page localization is therefore a bibliographic refinement, not an unclosed proof obligation.

### Formal anchor

`Yuren-Tang/affine-cdc:main@ebd7098a7a8b824e8c0a511d3c71f61705672aa8`

This checkpoint machine-checks substantial internal slices but not the integrated natural theorem end to end.

## 7. B1 exclusion audit

The next Programme B checkpoint is `778b09ac8260192e022f512f24cdef1d04871f37`, strictly later than `8bee1678...`.

No B1 theorem, correction, source, file, or later live-branch commit is used in the active Programme A chapters or control files. The B1 section visible in the source `OBLIGATION_DAG.md` is retained as immutable branch-context provenance only and is not part of the integrated mathematical dependency graph.

## 8. Downstream use

Subject to AC-DIR disposition, this candidate is the natural fixed input for:

- independent Audit A;
- later PDL repair units triggered by that audit;
- later Lean implementation from the same accepted interfaces;
- later Paper A revision from the same accepted mathematics.

None of those downstream statuses is conferred by this integration.