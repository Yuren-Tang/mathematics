# AffineCDC proof-development obligation DAG

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Standing issue:** `Yuren-Tang/research-workbench#37`  
**Owned branch:** `proof-development/affine-cdc-rigour-v1`  
**Exact initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Programme state:** persistent; this ledger remains live after the initial theorem spine

## 1. Control and assurance boundary

This branch develops rigorous mathematical proof units. It does not move `main`, alter Research Lead or Curator branches, mutate Lean or manuscript repositories, create releases or tags, or change publication/DOI surfaces.

Status words are authorial proof-development states:

`QUEUED`, `ACTIVE`, `ARGUMENT`, `BLOCKED-FRONTIER`, `BLOCKED-SOURCE`, `COMPLETE-DRAFT`, `READY-FOR-CURATOR`, `INTEGRATED`, `REPAIR`, `SUPERSEDED`.

`COMPLETE-DRAFT` and `READY-FOR-CURATOR` do not mean independently audited or machine-checked.

## 2. Normalized complete-CDC DAG

```text
A0  foundational graph/cut/circuit/multiplicity semantics
├──> A1  loop deletion and exact loop reinsertion
└──> A2  loopless cubic expansion and collapse data
      └──> A3  binary-flow external boundary
            └──> A4  affine pair complex and obstruction object
                  └──> A5  rank-three Fano compatibility
                        └──> A6  graph-level even double-cover extraction
A0 ───────────────────────────────┘
A0 + A6 ──> A7  intrinsic vertex-boundary/cut-even bridge
A2 + A6 + A7 ──> A8  collapse preservation and multiplicity bookkeeping
A0 + A8 ──> A9  finite circuit decomposition
A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 ──> A10 final theorem assembly
```

The displayed chain is a proof-development order, not a claim that every mathematical construction is logically impossible to state earlier. It records the order in which downstream chapters may rely on closed interfaces.

### Unit table

| Code | State | Exact unit boundary | Completion test | Immediate consumers |
|---|---|---|---|---|
| `AC-PD-A0` | `COMPLETE-DRAFT` | multigraph model; finite active edge set; active vertices; cuts; intrinsic boundary parity; cut-even supports; circuits; components; indexed families and multiset multiplicity; empty and loop-only cases | closed at `0d8c9102fa117e5f58b5d1617f3fae782c164097` | A1, A2, A7, A9, A10 |
| `AC-PD-A1` | `COMPLETE-DRAFT` | delete all loops; preserve nonloop cuts and no-singleton-cut condition; reinsert exactly two singleton-loop circuit occurrences | closed at `b193d55461040a6b6b7692e4f24e91d88c97a663` | A2, A10 |
| `AC-PD-A2` | `COMPLETE-DRAFT` | loopless port-cycle cubic expansion; degree-two parallel fibre; disconnected components; fibres, auxiliary edges, lift and collapse map | closed at `7c271c41f9d442ddb14034fb40b730fcc61c83a5` | A3, A4, A8 |
| `AC-PD-A3` | `COMPLETE-DRAFT` | componentwise `BinaryEightFlow`; Seymour six-flow input; literal 6-to-8 range inclusion; equal-order finite-abelian-group transport; orientation forgetting in characteristic two | closed at `6817896a301157db886f7c016866748a9161d15f` | A4, A10 |
| `AC-PD-A4` | `COMPLETE-DRAFT` | incidence space, local affine torsor, edge diagonal, pair complex, quotient equation, stress dual, retained source-data boundary | closed at `93bd8019099f0fa10ee53928681167f81506c407` | A5 |
| `AC-PD-A5` | `ACTIVE` | canonical quadratic planes; local Fano Lagrangian/characteristic torsor; abstract Lagrangian intersection; global compatibility | every local identity and global implication proved without hidden rank, connectedness, or representation cases | A6 |
| `AC-PD-A6` | `QUEUED` | retain graph/dart data; construct finite indexed supports; prove support parity and exact edge multiplicity two; flatten to multiset | graph-level witness and all index/multiplicity maps explicit | A7, A8 |
| `AC-PD-A7` | `QUEUED` | distinguish intrinsic boundary parity from the companion once-per-edge incidence API; prove the exact bridge used on the loopless cubic graph | required directions and hypotheses proved; any stronger scope corrected | A8 |
| `AC-PD-A8` | `QUEUED` | project supports along injective original-edge lift; prove cut transport and exact double coverage after collapse | auxiliary edges, equal projected supports, empty images and repeated occurrences handled | A9 |
| `AC-PD-A9` | `QUEUED` | decompose each finite cut-even support into finitely many circuits; concatenate indexed decompositions | termination, empty support, multiplicity preservation and component cases proved | A10 |
| `AC-PD-A10` | `QUEUED` | assemble the natural finite-active-edge bridgeless multigraph theorem under the weakest proved hypotheses | every arrow cites an exact completed unit; empty graph, isolated vertices, disconnected graph, parallel edges and loops handled | Curator / later Lean and manuscript projections |

### Boundary corrections recorded at normalization

A0 owns **circuit semantics and characterization**. A9 owns **finite decomposition into circuits**. The baseline prose sometimes mentions decomposition near the definitions; no downstream proof may treat that mention as a closed A0 result.

The intrinsic graph-theoretic parity object is the mod-two boundary of a support, equivalently half-edge degree parity with loops counted twice. The companion formal API's current once-per-edge incidence convention is a distinct loopless representation. A7 will state its exact bridge; it must not be silently extended across loops.

The pair complex is the complete compatibility image but does not retain graph/dart/indexed-support semantics. A6 must consume the retained source object `(G, Γ, f)` together with a compatible point, not a bare abstract pair complex.

## 3. Five-support proof tree

The global five-support theorem remains open. Proof development begins here only after the complete-CDC foundational chain is stable, except for an urgent returned defect.

| Code | State | Family |
|---|---|---|
| `AC-PD-B1` | `QUEUED` | root-flow and fixed-plane/fixed-lift equivalences |
| `AC-PD-B2` | `QUEUED` | singular, quadratic, Schur, cographic, orthogonal and Fourier formulations |
| `AC-PD-B3` | `QUEUED` | dual triangulation, quotient and halfcube structures |
| `AC-PD-B4` | `QUEUED` | vertical and horizontal reconfiguration |
| `AC-PD-B5` | `QUEUED` | three-cuts, four-poles and routing states |
| `AC-PD-B6` | `QUEUED` | holonomy, BBD/DDD and canonical defects |
| `AC-PD-B7` | `QUEUED` | route-lock, curvature and common-cut localization |
| `AC-PD-B8` | `QUEUED` | finite laboratories and exact certificates |
| `AC-PD-B9` | `BLOCKED-FRONTIER` | global five-support assembly; exact smallest missing bridge to be maintained |

## 4. Repair queue

No repair unit is active at this checkpoint. Every later entry must record its trigger, affected integrated checkpoint, exact claim or proof step, severity, required mathematical action, whether it returns to `AC-RL`, and its Curator-ready test.

## 5. Current active unit

`AC-PD-A5` is active. It must prove that in rank three every quotient plane `Q_e` carries its canonical anisotropic quadratic form, that the vertex translation space is Lagrangian and its affine local-family coset is the characteristic torsor, and that the edge diagonal is a totally singular Lagrangian. The abstract characteristic-torsor intersection theorem should then give global compatibility componentwise. The existing branching/cross-bit Lean theorem remains a formal anchor, but the invariant quadratic presentation is not thereby machine-checked.
