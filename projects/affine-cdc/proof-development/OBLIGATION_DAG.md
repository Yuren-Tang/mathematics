# AffineCDC proof-development obligation DAG

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Standing issue:** `Yuren-Tang/research-workbench#37`  
**Owned branch:** `proof-development/affine-cdc-rigour-v1`  
**Exact initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Programme state:** persistent; Programme A and B1 are `READY-FOR-CURATOR`; Programme B continues

## 1. Control and assurance boundary

This branch develops rigorous mathematical proof units. It does not move `main`, alter Research Lead or Curator branches, mutate Lean or manuscript repositories, create releases or tags, or change publication/DOI surfaces.

Status words are authorial proof-development states:

`QUEUED`, `ACTIVE`, `ARGUMENT`, `BLOCKED-FRONTIER`, `BLOCKED-SOURCE`, `COMPLETE-DRAFT`, `READY-FOR-CURATOR`, `INTEGRATED`, `REPAIR`, `SUPERSEDED`.

`COMPLETE-DRAFT` and `READY-FOR-CURATOR` do not mean independently audited or machine-checked.

## 2. Complete-CDC DAG

```text
A0  foundational graph/cut/circuit/multiplicity semantics
├──> A1  loop deletion and exact loop reinsertion
└──> A2  loopless cubic expansion and collapse data
      └──> A3  binary-flow external boundary
            └──> A4  affine pair complex and obstruction object
                  └──> A5  rank-three Fano compatibility
                        └──> A6  graph-level even-support extraction
A0 ───────────────────────────────┘
A0 + A6 ──> A7  vertex/boundary/cut parity bridge
A2 + A6 + A7 ──> A8  collapse and multiplicity transport
A0 + A8 ──> A9  finite circuit decomposition
A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 ──> A10 final theorem
```

| Code | State | Exact checkpoint | Closed output |
|---|---|---|---|
| `AC-PD-A0` | `COMPLETE-DRAFT` | `0d8c9102fa117e5f58b5d1617f3fae782c164097` | finite-active multigraph, cuts, intrinsic parity, circuits, components, indexed/multiset multiplicity |
| `AC-PD-A1` | `COMPLETE-DRAFT` | `b193d55461040a6b6b7692e4f24e91d88c97a663` | exact loop deletion, preservation, and forced two-singleton reinsertion |
| `AC-PD-A2` | `COMPLETE-DRAFT` | `7c271c41f9d442ddb14034fb40b730fcc61c83a5` | finite loopless cubic port-cycle expansion, components, fibres, cut pullback, collapse |
| `AC-PD-A3` | `COMPLETE-DRAFT` | `6817896a301157db886f7c016866748a9161d15f` | Seymour boundary, literal 6-to-8 step, internal equal-order group-flow transport, characteristic-two adapter |
| `AC-PD-A4` | `COMPLETE-DRAFT` | `93bd8019099f0fa10ee53928681167f81506c407` | local affine torsor, pair complex, quotient equation, stress dual, retained-data boundary |
| `AC-PD-A5` | `COMPLETE-DRAFT` | `6ce41bd87b5700346c572f701c40c8ac6f374e3f` | canonical quotient quadratics, Fano Lagrangians, characteristic torsor, automatic compatibility |
| `AC-PD-A6` | `COMPLETE-DRAFT` | `f953619d6fda7105fef406892530496c7d72178a` | point-indexed graph supports, local evenness, exact double coverage, multiset flattening |
| `AC-PD-A7` | `COMPLETE-DRAFT` | `b0755c3b95939482c6e223c24e4d8327c53f02e8` | exact loopless equivalence of set-incidence parity, intrinsic boundary parity, and cut parity |
| `AC-PD-A8` | `COMPLETE-DRAFT` | `d9718c6204d4f11aa853ee2f6e350d5c08444820` | memberwise cut-even collapse and exact original-edge occurrence transport |
| `AC-PD-A9` | `COMPLETE-DRAFT` | `400404e5413dfc933668aa0ec152010bae5a742c` | terminating finite circuit decomposition and global multiplicity preservation |
| `AC-PD-A10` | `READY-FOR-CURATOR` | `143538ef0fc9518ce877a42fa422d57cb6e3ce8a` | natural finite-active-edge no-singleton-cut CDC theorem assembly and assurance ledger |

### Programme A corrections retained

1. A0 owns circuit semantics and characterization; A9 owns finite decomposition.
2. Intrinsic half-edge boundary parity is the natural loop-aware notion; the companion once-per-edge predicate is loopless only.
3. The pair complex captures compatibility but not graph/dart/indexed-support semantics.
4. Equal-order group-flow transport is proved internally rather than left as a Tutte black box.
5. Collapse preserves cut-even supports and occurrence multiplicity, not circuits.
6. Equal support values at different indices remain different occurrences.
7. The natural hypotheses are finite active edge set plus no singleton cut; connectedness, simplicity, looplessness, and ambient-vertex finiteness are unnecessary.

## 3. Programme B — five-support proof tree

The global five-support theorem remains open. Programme B proves and normalizes all mature subchains while maintaining the smallest exact frontier gap.

```text
B1  root-flow / fixed-plane / fixed-lift equivalences
├──> B2  singular, quadratic, Schur, cographic, orthogonal, Fourier forms
├──> B3  dual triangulation, quotient, and halfcube structures
└──> B4  vertical and horizontal reconfiguration
B2 + B3 + B4 ──> B5  three-cuts, four-poles, and routing states
B5 ──> B6  holonomy, BBD/DDD, defects, and atoms
B6 ──> B7  route-lock, curvature, and common-cut localization
B1–B7 + B8 finite certificates ──> B9 global five-support assembly
```

| Code | State | Exact unit / checkpoint |
|---|---|---|
| `AC-PD-B1.1` | `COMPLETE-DRAFT` | `ed0288c2485d4eb826b49b8289a0025e1b2c0d64` — five-support ↔ root flow ↔ $K_5$ triangle law |
| `AC-PD-B1.2` | `COMPLETE-DRAFT / CORPUS-CORRECTION` | `24e923bcfcfc3aa2765c3269018c977bd1351403` — exact $(B,D,M)$ matching/four-flow theorem and component $T$-join condition |
| `AC-PD-B1.3` | `COMPLETE-DRAFT` | `dbd01c86059368619a51f9b5252dfec0a2cf7778` — fixed-flow/fixed-plane colour-cut, distinguished-support, and plane-profile criterion |
| `AC-PD-B1.4` | `COMPLETE-DRAFT / SCOPE-CORRECTION` | `a9695a1045bdb157b8d0d8aa1e318302c28e785d` — root-lift/surface equivalence, full-dual half-cube potential, holonomy, and factorable quotient scope |
| `AC-PD-B1` | `READY-FOR-CURATOR` | `73be22f42298470bd9ebaeb519de7ed686c27e41` — consolidated graph/fixed-flow/fixed-lift equivalence and implication map |
| `AC-PD-B2` | `ACTIVE` | normalize and prove singular, quadratic, Schur, cographic, orthogonal, and Fourier/stress formulations; classify every arrow as equivalence, quotient, obstruction, or evidence |
| `AC-PD-B3` | `QUEUED` | prove dual-triangulation, quotient, halfcube target, link, and marked-core constructions beyond the B1 structural interface |
| `AC-PD-B4` | `QUEUED` | prove vertical/horizontal reconfiguration moves, preserved invariants, and exact reachability claims |
| `AC-PD-B5` | `QUEUED` | formalize three-cut, four-pole, and routing-state reductions |
| `AC-PD-B6` | `QUEUED` | prove holonomy, BBD/DDD, canonical defects, and atom statements |
| `AC-PD-B7` | `QUEUED` | prove route-lock, curvature, and common-cut localization consequences |
| `AC-PD-B8` | `QUEUED` | normalize finite laboratories and exact certificates; separate evidence from proof |
| `AC-PD-B9` | `BLOCKED-FRONTIER` | maintain the exact smallest missing global composition/localization implication; return only this genuine new-mathematics gap to AC-RL |

### Programme B1 corrections retained

1. A fixed support-coordinate inverse image is even; a fixed root-label inverse image is a matching.
2. Bare matching plus four-flow is insufficient; exact $(B,D)$ or component-parity/$T$-join data are required.
3. The fixed-flow plane-profile criterion is complete only with its fixed/existential quantifiers stated.
4. A full-dual map $T_g^{(1)}\to\mathscr A_5$ classifies componentwise compression of the same embedding; it does not represent every external cover on an arbitrary fixed surface without zero dual holonomy.
5. $J_g\to\mathscr A_5$ is only the old-colour-factorable subclass.
6. If $\mathscr A_5$ denotes the even half-cube, singleton words require an odd translation before use as its five-clique.

## 4. Repair queue

No repair unit is active. Any later Curator, audit, Lean, manuscript, or Research Lead defect must be entered with:

- exact triggering checkpoint;
- exact false, incomplete, or ambiguous statement;
- mathematical severity;
- required repair;
- whether new mathematics is needed from AC-RL;
- Curator-ready completion test.

## 5. Current active unit

`AC-PD-B2` is active. The first task is to build one exact arrow ledger across `five-support/equivalent-formulations-and-proof-families.md`, `singular-quotient-lifting.md`, `orthogonal-rank-reduction.md`, `fourier-and-stress-duals.md`, and the controlling recovered packets. Each formulation must be classified as a full witness equivalence, a fixed-data equivalence, a quotient with lost lift data, a dual obstruction criterion, or finite evidence. The first proof unit will close the earliest unambiguous arrow and isolate any false or overbroad equivalence before proceeding.