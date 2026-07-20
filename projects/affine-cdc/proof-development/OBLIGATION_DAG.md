# AffineCDC proof-development obligation DAG

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Standing issue:** `Yuren-Tang/research-workbench#37`  
**Owned branch:** `proof-development/affine-cdc-rigour-v1`  
**Exact initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Programme state:** persistent; Programme A and B1–B7 are `READY-FOR-CURATOR`; Programme B continues

## 1. Assurance boundary

This branch develops authorial mathematical proof units. It does not move `main`, alter Curator or Research Lead branches, mutate Lean/manuscript repositories, or change release/publication surfaces.

## 2. Programme checkpoints

| Programme | State | Immutable checkpoint | Closed layer |
|---|---|---|---|
| `A` | `READY-FOR-CURATOR` | `8bee16780b549f51e1f29343671a059961ec4172` | complete finite-active-edge CDC theorem spine |
| `B1` | `READY-FOR-CURATOR` | `778b09ac8260192e022f512f24cdef1d04871f37` | root-flow/fixed-plane/fixed-lift equivalences |
| `B2` | `READY-FOR-CURATOR / CORRECTION` | `d62974704d6dac77aaa00275a595fedf7f70cfd2` | witness hierarchy and orthogonal correction |
| `B3` | `READY-FOR-CURATOR / PROVENANCE-REPAIRED` | `d806168bb579dbc13f267f44f631e07de909b706` | target/full-dual/factorable scope |
| `B4` | `READY-FOR-CURATOR / FRONTIER-EXPLICIT` | `345074690b7a8658c1208ae84f10d709f8b74bcf` | vertical/horizontal motion |
| `B5` | `READY-FOR-CURATOR / FRONTIER-LOCALIZED` | `274970ef9c56cafdbfceeed3c0cc08238d3dfd40` | cuts, four-poles, routing |
| `B6` | `READY-FOR-CURATOR / CORRECTION / AC-RL-GAPS` | `404f7511f16d1225e066a91842a57e2084943c72` | individual holonomy, Tait escape, DDD atoms; BBD corrections |

## 3. B7 — route-lock, curvature, and localisation

| Unit | State | Exact checkpoint / output |
|---|---|---|
| `B7.1` | `COMPLETE-DRAFT / LOCALISATION-OPEN` | `81348e2bd1e218ec554ea1faf2ccc0a3f865a2fd` — rank-one impossibility, rank-two Tait escape, flat potential, nonflat common scalar-sheet cut |
| `B7.2` | `COMPLETE-DRAFT / AC-RL-RETURN` | `042b2a4ed564df78f9e54427713ed5a3c7cdedee` — exact Type T, Type H, flat, and nonflat localisation gaps |
| `B7` | `READY-FOR-CURATOR / AC-RL-GAPS-EXPLICIT / GLOBAL-COMPOSITION-OPEN` | `9407f2eaeca70b0d6cb2e6b4900cd6b42853d8f2` — consolidated route-lock/curvature map |

### Retained B7 theorem layer

1. Rank one locked quotient is impossible.
2. Rank two is a Tait colouring and lifts to boundary state `A`, hence escapes.
3. Full rank has the exact dichotomy:
   - flat eight-state affine potential;
   - nonflat common `g`-edge set simultaneously a cut in all four scalar sheets with odd terminal word.
4. The common scalar cut is not yet a graph cut of the four-pole and the flat potential is not yet a bounded interface.

### Exact AC-RL returns

Returned in issue #8 comment `5019455976`:

- `AC-RL-TYPE-T-SERIALISATION`;
- `AC-RL-FLAT-POTENTIAL-INTERFACE`;
- `AC-RL-COMMON-CUT-LOCALISATION`;
- `AC-RL-TYPE-H-COMMON-WITNESS`.

Earlier BBD returns remain active:

- `AC-RL-BBD-GROUPOID-CLOSURE`;
- `AC-RL-BBD-VARIATION-SLICE`.

## 4. Remaining programmes

| Code | State | Boundary |
|---|---|---|
| `AC-PD-B8` | `ACTIVE` | inventory and assurance-normalize finite laboratories, code, hashes, witnesses, counts, and theorem dependencies |
| `AC-PD-B9` | `BLOCKED-FRONTIER` | assemble the corrected global dependency frontier without claiming the five-support theorem |

## 5. Current active unit

`AC-PD-B8` is active. It will build one certificate ledger separating reproducible exact computations, finite tables used as theorem inputs, illustrative censuses, and results affected by B2/B3/B6 corrections.