# AffineCDC proof-development obligation DAG

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Standing issue:** `Yuren-Tang/research-workbench#37`  
**Owned branch:** `proof-development/affine-cdc-rigour-v1`  
**Exact initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Programme state:** persistent; Programme A and B1–B8 are `READY-FOR-CURATOR`; B9 is `BLOCKED-FRONTIER / CORRECTED-ASSEMBLY`

## 1. Completed checkpoints

| Programme | State | Immutable checkpoint | Closed layer |
|---|---|---|---|
| `A` | `READY-FOR-CURATOR` | `8bee16780b549f51e1f29343671a059961ec4172` | complete finite-active-edge CDC theorem spine |
| `B1` | `READY-FOR-CURATOR` | `778b09ac8260192e022f512f24cdef1d04871f37` | root-flow/fixed-plane/fixed-lift equivalences |
| `B2` | `READY-FOR-CURATOR / CORRECTION` | `d62974704d6dac77aaa00275a595fedf7f70cfd2` | witness hierarchy and orthogonal correction |
| `B3` | `READY-FOR-CURATOR / PROVENANCE-REPAIRED` | `d806168bb579dbc13f267f44f631e07de909b706` | target/full-dual/factorable scope |
| `B4` | `READY-FOR-CURATOR / FRONTIER-EXPLICIT` | `345074690b7a8658c1208ae84f10d709f8b74bcf` | vertical/horizontal motion |
| `B5` | `READY-FOR-CURATOR / FRONTIER-LOCALIZED` | `274970ef9c56cafdbfceeed3c0cc08238d3dfd40` | cuts, four-poles, routing |
| `B6` | `READY-FOR-CURATOR / CORRECTION / AC-RL-GAPS` | `404f7511f16d1225e066a91842a57e2084943c72` | individual holonomy, Tait escape, DDD atoms; BBD corrections |
| `B7` | `READY-FOR-CURATOR / AC-RL-GAPS / GLOBAL-OPEN` | `164f7655f9ec7c0e0a73d49303cf66230fb26487` | route-lock rank, curvature, exact localisation gaps |
| `B8` | `READY-FOR-CURATOR / ASSURANCE-NORMALIZED` | `989cb002598fd91786029be201c2747c697bb476` | finite-certificate and code/reproducibility ledger |

## 2. B9 corrected assembly

`AC-PD-B9` is fixed at the current branch checkpoint as

`BLOCKED-FRONTIER / CORRECTED-ASSEMBLY / AC-RL-DEPENDENT`.

It proves the five-support outer reduction:

$$
\text{finite-active bridgeless multigraph case}
\Longleftrightarrow
\text{finite loopless bridgeless cubic case}.
$$

Loops can be inserted into two fixed support occurrences; port-cycle collapse preserves all five indexed supports and exact edge multiplicity.

It does **not** prove the cubic five-support theorem.

## 3. Exact unresolved obligations

1. `AC-RL-BBD-GROUPOID-CLOSURE`;
2. `AC-RL-BBD-VARIATION-SLICE`;
3. `AC-RL-TYPE-T-SERIALISATION`;
4. `AC-RL-FLAT-POTENTIAL-INTERFACE`;
5. `AC-RL-COMMON-CUT-LOCALISATION`;
6. `AC-RL-TYPE-H-COMMON-WITNESS`.

The first two concern the corrected BBD route. The last four are the corrected DDD/four-pole source-localisation route. Finite certificates close none of them.

## 4. Minimal sufficient future packages

Either of the following would close the global strengthening.

- **Escape:** every bridgeless cubic graph has some Fano flow/root lift with full dual mapping to $\mathscr A_5$.
- **Decomposition:** every persistent bad cubic state yields a strictly smaller labelled interface decomposition whose profiles glue.

A mixed escape/decomposition theorem also suffices.

## 5. Persistent-role state

AC-PDL remains active for:

- AC-RL-returned proof packets;
- Curator/audit/Lean/manuscript repair units;
- theorem-DAG maintenance;
- new mature proof checkpoints.

Without such input, B9 remains blocked rather than declared complete or abandoned.