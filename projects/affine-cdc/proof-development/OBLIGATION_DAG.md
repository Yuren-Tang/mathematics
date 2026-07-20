# AffineCDC proof-development obligation DAG

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Standing issue:** `Yuren-Tang/research-workbench#37`  
**Owned branch:** `proof-development/affine-cdc-rigour-v1`  
**Exact initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Programme state:** persistent; Programme A and B1–B4 are `READY-FOR-CURATOR`; Programme B continues

## 1. Control and assurance boundary

This branch develops rigorous mathematical proof units. It does not move `main`, alter Research Lead or Curator branches, mutate Lean or manuscript repositories, create releases or tags, or change publication/DOI surfaces.

Status words are authorial proof-development states:

`QUEUED`, `ACTIVE`, `ARGUMENT`, `BLOCKED-FRONTIER`, `BLOCKED-SOURCE`, `COMPLETE-DRAFT`, `READY-FOR-CURATOR`, `INTEGRATED`, `REPAIR`, `SUPERSEDED`.

`COMPLETE-DRAFT` and `READY-FOR-CURATOR` do not mean independently audited or machine-checked.

## 2. Complete-CDC programme

Programme A is complete and ready for Curator intake at immutable checkpoint

`8bee16780b549f51e1f29343671a059961ec4172`.

Its A0–A10 chain proves the finite-active-edge no-singleton-cut multigraph CDC theorem with exact loop, parallel-edge, disconnected, collapse, parity, multiplicity, source, and assurance boundaries.

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

### B1 — exact object and quantifier layer

Immutable intake checkpoint: `778b09ac8260192e022f512f24cdef1d04871f37`.

| Unit | State | Output |
|---|---|---|
| `B1.1` | `COMPLETE-DRAFT` | five supports ↔ root flow ↔ $K_5$ triangle law |
| `B1.2` | `COMPLETE-DRAFT / CORPUS-CORRECTION` | exact $(B,D,M)$ matching/four-flow theorem and component $T$-join condition |
| `B1.3` | `COMPLETE-DRAFT` | fixed-flow/fixed-plane colour-cut, distinguished-support, and plane-profile criterion |
| `B1.4` | `COMPLETE-DRAFT / SCOPE-CORRECTION` | root-lift/surface equivalence, full-dual half-cube potential, holonomy, and quotient scope |
| `B1` | `READY-FOR-CURATOR` | consolidated graph/fixed-flow/fixed-lift map |

### B2 — formulation and witness hierarchy

Immutable intake checkpoint: `d62974704d6dac77aaa00275a595fedf7f70cfd2`.

| Unit | State | Output |
|---|---|---|
| `B2.1` | `COMPLETE-DRAFT` | anisotropic $O^-(4,2)$ mother flow; singular lift; quadratic equation; Schur criterion |
| `B2.2` | `COMPLETE-DRAFT / TERMINOLOGY-BOUNDARY` | cographic cycle-continuous edge-map equivalence |
| `B2.3` | `COMPLETE-DRAFT / MATHEMATICAL-CORRECTION` | false universal $2r$ hierarchy refuted; $q-2$ bound; deleted permutation module |
| `B2.4` | `COMPLETE-DRAFT / WITNESS-SCOPE` | relative-stress Fredholm duality and exact Fourier count |
| `B2` | `READY-FOR-CURATOR / MATHEMATICAL-CORRECTION` | full witness versus fixed-data/dual hierarchy |

### B3 — target, dual, and quotient layer

Immutable intake checkpoint: `d806168bb579dbc13f267f44f631e07de909b706`.

| Unit | State | Exact checkpoint / output |
|---|---|---|
| `B3.1` | `COMPLETE-DRAFT / PROVENANCE-REPAIR` | `bcd7398a5d2e7c15948ea2707fec1484a6a78cb5` — common-link formula and validated capacity packets |
| `B3.2` | `COMPLETE-DRAFT / PROVENANCE-REPAIR` | `5cf1ace96102982db1b9e79d1cc5d15f1fb39f2d` — $K_6$/$K_8-C_5$ no-go and exact eight-vertex classification |
| `B3.3` | `COMPLETE-DRAFT / SCOPE-NORMALIZATION` | `9b9263195e0bc578a71ffdb182c3fdb3ece52703` — target packet audit and factorable/full-dual separation |
| `B3` | `READY-FOR-CURATOR / PROVENANCE-REPAIRED` | `e7f4143bc1e12fa8ea20478f79402c5e02f81abe` — consolidated target/scope map |

Controlling B3 boundaries:

1. $T_g^{(1)}$ is the complete same-embedding object; $J_g$ is the old-colour-factorable quotient.
2. The exact half-cube link, capacity, and eight-vertex packets are valid.
3. Unused-root containers, two-apex/pentagon cores, and ideal pivots are factorable-route objects.
4. Flower/census numerical data remain on the certificate axis.
5. The all-parallel matching representative is corrected to $\{01,23,45\}$; orbit sizes remain $28,168,224$.

### B4 — vertical and horizontal motion

| Unit | State | Exact checkpoint / output |
|---|---|---|
| `B4.1` | `COMPLETE-DRAFT` | `bbfe3bee38cb54c6a9878baa79c5608660492285` — vertical root-lift torsor, componentwise reduced kernel, harmonic quotient, partial Petrial |
| `B4.2` | `COMPLETE-DRAFT / SCOPE-NORMALIZATION` | `21dbd865f0101ad029fa76612229581cdb3735c9` — support pivots, connected-switch adjacency, disconnected commuting decomposition |
| `B4.3` | `COMPLETE-DRAFT / SCOPE-CORRECTION` | `8f854d5744abf77c7d74acaa214685ec215eb4a9` — used-root transport, gauge constraint replacement, internal/external defect transport, connected-neighbour boundary |
| `B4` | `READY-FOR-CURATOR / FRONTIER-EXPLICIT` | `37ad2b11b6b0d55b69eb0a14799e3049790c2c46` — consolidated motion and transport map |

Controlling B4 boundaries:

1. The labelled root-lift fibre is a torsor under $H_f^0$; the reduced code is $H_f^0/\Gamma^{\pi_0(G)}$.
2. Gauge words are exactly code-filtered partial Petrials at fixed Fano flow.
3. Support-cycle pivots preserve the uncoloured embedding and lift one connected-cycle flow switch.
4. General connected switches require a new affine lift solve; disconnected cycle words are commuting paths, not one adjacency.
5. The linear admissible-switch image ranges over composite same-direction endpoints. Connected-neighbour images need not be linear.
6. Internal switches correct a fixed quotient; external switches reslice the quotient.
7. No global escape, component-hitting, or monotone-potential theorem is claimed.

### Remaining units

| Code | State | Exact unit boundary |
|---|---|---|
| `AC-PD-B5` | `ACTIVE` | three-edge cuts, four-poles, boundary signatures, cap forcing, Kempe closure, routing states, and exact gluing |
| `AC-PD-B6` | `QUEUED` | holonomy, BBD/DDD, canonical defects, and atom statements |
| `AC-PD-B7` | `QUEUED` | route-lock, curvature, and common-cut localization consequences |
| `AC-PD-B8` | `QUEUED` | finite laboratories and exact certificates; evidence separated from proof |
| `AC-PD-B9` | `BLOCKED-FRONTIER` | exact smallest missing global composition/localization implication; only genuine new-mathematics gaps return to AC-RL |

## 4. Repair queue

No repair unit is active. The B3 provenance mistake was repaired before handoff and its issue record was corrected in place. Later defects must record triggering checkpoint, exact claim, severity, repair, AC-RL requirement, and Curator-ready test.

## 5. Current active unit

`AC-PD-B5` is active. The first subunit will normalize three-edge-cut and four-pole boundary data, prove the exact parity constraints on terminal root values and support incidences, and identify the minimal gluing datum required to combine local five-support witnesses across a separator.