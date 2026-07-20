# AffineCDC proof-development obligation DAG

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Standing issue:** `Yuren-Tang/research-workbench#37`  
**Owned branch:** `proof-development/affine-cdc-rigour-v1`  
**Exact initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Programme state:** persistent; Programme A and B1–B3 are `READY-FOR-CURATOR`; Programme B continues

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

Programme A immutable intake checkpoint: `8bee16780b549f51e1f29343671a059961ec4172`.

## 3. Programme B — five-support proof tree

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

### B1 — exact object and quantifier layer

| Code | State | Exact checkpoint / output |
|---|---|---|
| `AC-PD-B1.1` | `COMPLETE-DRAFT` | `ed0288c2485d4eb826b49b8289a0025e1b2c0d64` — five-support ↔ root flow ↔ $K_5$ triangle law |
| `AC-PD-B1.2` | `COMPLETE-DRAFT / CORPUS-CORRECTION` | `24e923bcfcfc3aa2765c3269018c977bd1351403` — exact $(B,D,M)$ matching/four-flow theorem and component $T$-join condition |
| `AC-PD-B1.3` | `COMPLETE-DRAFT` | `dbd01c86059368619a51f9b5252dfec0a2cf7778` — fixed-flow/fixed-plane colour-cut, distinguished-support, and plane-profile criterion |
| `AC-PD-B1.4` | `COMPLETE-DRAFT / SCOPE-CORRECTION` | `a9695a1045bdb157b8d0d8aa1e318302c28e785d` — root-lift/surface equivalence, full-dual half-cube potential, holonomy, and quotient scope |
| `AC-PD-B1` | `READY-FOR-CURATOR` | `73be22f42298470bd9ebaeb519de7ed686c27e41` — consolidated graph/fixed-flow/fixed-lift map |

Programme B1 immutable intake checkpoint: `778b09ac8260192e022f512f24cdef1d04871f37`.

### B2 — formulation and witness hierarchy

| Code | State | Closed output |
|---|---|---|
| `AC-PD-B2.1` | `COMPLETE-DRAFT` | anisotropic $O^-(4,2)$ mother flow; singular-line lift torsor; quadratic cycle equation; Schur quotient criterion |
| `AC-PD-B2.2` | `COMPLETE-DRAFT / TERMINOLOGY-BOUNDARY` | exact cographic cycle-continuous edge-map equivalence and composition law |
| `AC-PD-B2.3` | `COMPLETE-DRAFT / MATHEMATICAL-CORRECTION` | refutation of false universal $2r$ orthogonal-root claim; sharp $q-2$ lower bound; deleted permutation module; rank-three exception |
| `AC-PD-B2.4` | `COMPLETE-DRAFT / WITNESS-SCOPE` | exact prescribed-value Fredholm duality; relative-stress code; product-avoidance Fourier count; witness reconstruction boundary |
| `AC-PD-B2` | `READY-FOR-CURATOR / MATHEMATICAL-CORRECTION` | formulation/witness hierarchy at `769d4e9ec48c99eab695a0fc49b0a622e7e36ac4` |

Programme B2 immutable intake checkpoint: `d62974704d6dac77aaa00275a595fedf7f70cfd2`.

### B3 — target, dual, and quotient layer

| Code | State | Exact checkpoint / output |
|---|---|---|
| `AC-PD-B3.1` | `COMPLETE-DRAFT / PROVENANCE-REPAIR` | `bcd7398a5d2e7c15948ea2707fec1484a6a78cb5` — general quadratic common-link formula; validation of clique-link and exact capacity packets |
| `AC-PD-B3.2` | `COMPLETE-DRAFT / PROVENANCE-REPAIR` | `5cf1ace96102982db1b9e79d1cc5d15f1fb39f2d` — independent $K_6$/$K_8-C_5$ no-go proofs and validation of exact eight-vertex classification |
| `AC-PD-B3.3` | `COMPLETE-DRAFT / SCOPE-NORMALIZATION` | `9b9263195e0bc578a71ffdb182c3fdb3ece52703` — packet audit; factorable/full-dual separation; matching representative correction; certificate classification |
| `AC-PD-B3` | `READY-FOR-CURATOR / PROVENANCE-REPAIRED` | `e7f4143bc1e12fa8ea20478f79402c5e02f81abe` — consolidated target and scope map |

#### B3 boundaries retained

1. $T_g^{(1)}$ is the complete same-embedding object; $J_g$ is the old-colour-factorable quotient.
2. Clique links and dominating-clique capacity are valid target-graph theorems.
3. For eight-colour quotients, $J\to\mathscr A_5$ iff $J$ contains neither $K_6$ nor $K_8-C_5$.
4. Unused-root containers, two-apex/pentagon cores, and ideal pivots are factorable-route objects.
5. The flower $D_9$ obstruction is full-dual conditional on its explicit finite certificate.
6. Numerical censuses remain certificate data, not independently audited proofs.
7. The all-parallel unused-matching representative is corrected to $\{01,23,45\}$; the three orbit sizes remain $28,168,224$.

### Remaining Programme B units

| Code | State | Exact unit boundary |
|---|---|---|
| `AC-PD-B4` | `ACTIVE` | vertical gauge translations, partial Petrials, support-cycle pivots, horizontal connected-cycle switches, and exact preserved/transported data |
| `AC-PD-B5` | `QUEUED` | three-cut, four-pole, and routing-state reductions |
| `AC-PD-B6` | `QUEUED` | holonomy, BBD/DDD, canonical defects, and atom statements |
| `AC-PD-B7` | `QUEUED` | route-lock, curvature, and common-cut localization consequences |
| `AC-PD-B8` | `QUEUED` | finite laboratories and exact certificates; evidence separated from proof |
| `AC-PD-B9` | `BLOCKED-FRONTIER` | exact smallest missing global composition/localization implication; only this genuine new-mathematics gap returns to AC-RL |

## 4. Repair queue

No repair unit is active. The B3 provenance mistake was repaired before Curator handoff; issue #37 comment `5017021539` was updated in place. Any later defect must record the exact triggering checkpoint, statement, severity, repair, AC-RL need, and Curator-ready test.

## 5. Current active unit

`AC-PD-B4` is active. Its first subunit will normalize the vertical action: the gauge translation group, reduced stabilizers, exact local-face effect, and the equivalence between admissible gauge words and code-filtered partial Petrials. It will then separate support-cycle pivots from horizontal Fano-flow switches and prove which disconnected switches are compositions rather than single reconfiguration edges.