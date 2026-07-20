# AffineCDC proof-development obligation DAG

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Standing issue:** `Yuren-Tang/research-workbench#37`  
**Owned branch:** `proof-development/affine-cdc-rigour-v1`  
**Exact initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Programme state:** persistent; Programme A and B1–B5 are `READY-FOR-CURATOR`; Programme B continues

## 1. Control and assurance boundary

This branch develops rigorous mathematical proof units. It does not move `main`, alter Research Lead or Curator branches, mutate Lean or manuscript repositories, create releases or tags, or change publication/DOI surfaces.

Status words are authorial proof-development states:

`QUEUED`, `ACTIVE`, `ARGUMENT`, `BLOCKED-FRONTIER`, `BLOCKED-SOURCE`, `COMPLETE-DRAFT`, `READY-FOR-CURATOR`, `INTEGRATED`, `REPAIR`, `SUPERSEDED`.

`COMPLETE-DRAFT` and `READY-FOR-CURATOR` do not mean independently audited or machine-checked.

## 2. Complete-CDC programme

Programme A immutable intake checkpoint: `8bee16780b549f51e1f29343671a059961ec4172`.

## 3. Five-support programme

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

### Completed programme checkpoints

| Programme | State | Immutable intake checkpoint | Closed layer |
|---|---|---|---|
| `B1` | `READY-FOR-CURATOR` | `778b09ac8260192e022f512f24cdef1d04871f37` | exact object and fixed/existential quantifiers |
| `B2` | `READY-FOR-CURATOR / MATHEMATICAL-CORRECTION` | `d62974704d6dac77aaa00275a595fedf7f70cfd2` | full witnesses, quotient lifts, stress/Fourier, orthogonal correction |
| `B3` | `READY-FOR-CURATOR / PROVENANCE-REPAIRED` | `d806168bb579dbc13f267f44f631e07de909b706` | full dual, factorable quotient, target links/capacity, defect cores |
| `B4` | `READY-FOR-CURATOR / FRONTIER-EXPLICIT` | `345074690b7a8658c1208ae84f10d709f8b74bcf` | vertical Petrials, connected switches, support pivots, defect transport |

### B5 — cuts, four-poles, and routing

| Unit | State | Exact checkpoint / output |
|---|---|---|
| `B5.1` | `COMPLETE-DRAFT` | `e6eb80a4e8973d2c64432528623ba91580e791a3` — cubic local law, three-cut gluing, ten-state alphabet, 640 assignments, four-cut gluing, cap states |
| `B5.2` | `COMPLETE-DRAFT / FRONTIER-EXPLICIT` | `a46c544214d3c98203feeb78da7b2e55dc3bf858` — cap forcing, profile disjointness, terminal-path pairing, alignment dichotomy |
| `B5.3` | `COMPLETE-DRAFT / CERTIFICATE-BOUNDARY` | `3c10d3f8f717f7d476dee0b9680b7128a856d51c` — routing weights, fixed-route sectors, two-colour connectivity, uniform-routing elimination |
| `B5` | `READY-FOR-CURATOR / FRONTIER-LOCALIZED` | `79c69f25a0d40f6b234230ce709269926e5d4520` — consolidated separator/routing map |

Controlling B5 boundaries:

1. Covers glue automatically across cyclic three-cuts; a minimal counterexample is cyclically four-edge-connected.
2. Four labelled terminals carry ten support-unordered states $A,B_i,C_i,D_i$.
3. Four-cut gluing is exactly profile intersection.
4. Minimality forces each shore profile to meet every cap set $\mathcal K_i$, but not to contain one full cap set.
5. A nontrivial Kempe boundary transition is available exactly when internal terminal pairing aligns with the cap route.
6. Fixed routing $M_i$ preserves $\omega_i$ and has transition graph $P_3\sqcup C_4\sqcup P_3$.
7. Uniform routing is reducible and cannot be the residual obstruction.
8. Kernel, policy, Type T/H, monodromy, and small-census tables remain certificate data.
9. The live source alternative is sufficient pairing alignment or bounded four-pole decomposition.

### Remaining units

| Code | State | Exact unit boundary |
|---|---|---|
| `AC-PD-B6` | `ACTIVE` | Type T nested/serial routing; Type H interior holonomy; BBD/DDD canonical defects; atom and transport statements |
| `AC-PD-B7` | `QUEUED` | route-lock, curvature, and common-cut localization consequences |
| `AC-PD-B8` | `QUEUED` | finite laboratories and exact certificates; evidence separated from proof |
| `AC-PD-B9` | `BLOCKED-FRONTIER` | exact smallest missing global composition/localization implication; only genuine new-mathematics gaps return to AC-RL |

## 4. Repair queue

No repair unit is active. Later defects must record triggering checkpoint, exact claim, severity, repair, AC-RL requirement, and Curator-ready test.

## 5. Current active unit

`AC-PD-B6` is active. The first subunit will normalize the Type H boundary monodromy into an interior affine local system and determine which parts of the rainbow parity-square, residual quotient, and root-admissible holonomy packets are complete theorems versus finite lifted tables. In parallel it will identify the Type T serial/nested linkage datum that remains after uniform-routing elimination.