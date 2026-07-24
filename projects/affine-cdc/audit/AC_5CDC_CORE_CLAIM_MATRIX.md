# AC-5CDC-AUDIT-CORE-01 — claim-by-claim matrix

**Candidate:** `1f57422e0e415d8902d56eb294183815c0a0b640`  
**Audit branch:** `audit/affine-cdc-five-cdc-core-v1`

## A. R0 — five supports / root flow

| ID | Claim | Audit result | Basis |
|---|---|---|---|
| A1 | Exact multiplicity two gives one value in `R_5` on every edge | `ACCEPT` | Weight-two coordinate vector is immediate and reversible. |
| A2 | Vertex-evenness is equivalent to `E_5` conservation | `ACCEPT` | Coordinatewise parity equals the Kirchhoff equation. |
| A3 | Three incident cubic roots form one `K_5` triangle | `ACCEPT` | Three weight-two vectors sum to zero iff their two-subsets form a triangle. |
| A4 | Converse recovery of the five supports | `ACCEPT` | Coordinate supports recover the original indexed tuple edgewise. |
| A5 | Empty and repeated supports are allowed | `ACCEPT` | No proof step assumes nonempty or pairwise distinct support edge sets. |
| A6 | Parallel source edges and index multiplicity are retained | `ACCEPT` | The construction is on edge objects and named coordinates. |

**Unit A:** `ACCEPT`.

## B. R1 — one-cross structural reduction

| ID | Claim | Audit result | Basis |
|---|---|---|---|
| B1 | Every exterior component has at least two terminals | `ACCEPT` | One terminal would make its original edge a bridge. |
| B2 | Exterior has one component or two two-terminal components | `ACCEPT` | Four terminals and B1. |
| B3 | A non-partition cross joins a disconnected exterior | `ACCEPT` | Both new matching edges cross the two components. |
| B4 | New nonloop edges are nonbridges | `ACCEPT` | Each lies on a cycle through the other new edge or an exterior path. |
| B5 | Old edges remain nonbridges in the selected disconnected closure | `ACCEPT` | Terminal-shore argument; a terminal-free shore would contradict original bridgelessness. |
| B6 | At most one connected-exterior cross has an old bridge | `ACCEPT` | Bridge cuts are compatible; the two cross terminal partitions are crossing. |
| B7 | The two crosses cannot both contain loops | `ACCEPT` | Three terminals at one cubic exterior vertex force the fourth terminal edge to be a bridge. |
| B8 | If one cross has a loop, the opposite cross has no old bridge | `ACCEPT` | Coincident incidences cannot lie on opposite shores of the required bridge cut. |
| B9 | At least one cross is connected, loopless, bridgeless, cubic, and two vertices smaller | `ACCEPT` | B1–B8. |
| B10 | Theta is the exact no-simple-edge base | `ACCEPT` | Degree three and edge multiplicity at least two force one neighbour and three parallel edges. |

**Unit B:** `ACCEPT`.

## C. R2.1 — boundary / route certificate

| ID | Claim | Audit result | Independent output |
|---|---|---|---|
| C1 | Conserved ordered boundaries | `ACCEPT` | `640`. |
| C2 | Ten routing-weight states | `ACCEPT` | Exactly `A,B_i,C_i,D_i`. |
| C3 | State counts | `ACCEPT` | `10`; `60` each `B_i`; `30` each `C_i`; `120` each `D_i`. |
| C4 | Direct profiles `J_i` | `ACCEPT` | `J_i={A,B_i,C_i}`. |
| C5 | Cap profiles `K_i` | `ACCEPT` | `K_i={B_j,B_k,D_j,D_k}`. |
| C6 | `J_j intersect K_i={B_j}` for `j!=i` | `ACCEPT` | Direct set calculation. |
| C7 | Sixteen route rows | `ACCEPT` | `1680` labelled challenges collapse to `16` rows. |
| C8 | Fixed-route graph | `ACCEPT` | `P_3 sqcup C_4 sqcup P_3`. |
| C9 | Unique non-`K_i` route in equality/DDD locked rows | `ACCEPT` | Exact inspection of all relevant route triples. |
| C10 | Finite table does not prove physical route existence | `ACCEPT` | Candidate preserves this distinction. |

**Unit C:** `ACCEPT`.

## D. R2.2 — Morse descent

| ID | Claim | Audit result | Independent output / proof |
|---|---|---|---|
| D1 | Thirty root-triangle sides and fifteen flip involutions | `ACCEPT` | Direct enumeration of adjacent three-subsets. |
| D2 | Equality primary split | `ACCEPT` | `9/12/9`. |
| D3 | Secondary equality potential on neutral faces | `ACCEPT` | `6` decreasing, `6` increasing, no tie. |
| D4 | Positive scalar equality weight | `ACCEPT` | `15` decreasing, `15` increasing, no tie. |
| D5 | Equality nondecreasing table | `ACCEPT` | Independently reproduced exactly. |
| D6 | No nonempty equality local minimum | `ACCEPT` | Candidate elimination is complete and boundary-aware. |
| D7 | DDD weight census | `ACCEPT` | `15` decreasing, `15` increasing, no tie. |
| D8 | DDD nondecreasing table | `ACCEPT` | Independently reproduced exactly. |
| D9 | No nonempty DDD local minimum | `ACCEPT` | Candidate elimination is complete. |
| D10 | Selected root NNIs are legal same-order moves | `ACCEPT` | Root flow stays nonzero; connectedness and bridge-zero exclude category failure. |
| D11 | Equal-face cancellation strictly decreases potential | `ACCEPT` | Deletes two positive-weight vertices and is treated as a recursive/terminal exit. |

**Unit D:** `ACCEPT`.

## E. R2.3 — first failure / critical overlaps

| ID | Claim | Audit result | Basis / defect |
|---|---|---|---|
| E1 | First failed inverse step has one new non-root edge only | `ACCEPT` | All prior edges retain roots; only the restored central edge is new. |
| E2 | Failure value is zero or one co-root | `ACCEPT` | Sum of two roots has weight `0,2,4`. |
| E3 | Inverse-flip zero has a root alternative | `ACCEPT` | Boundary `a,a,b,b` with `a+b` a root. |
| E4 | Quadruple equality occurs only in inverse cancellation | `ACCEPT` | Current root-valued inverse-flip topology excludes all-equal boundary. |
| E5 | Standard co-root atom has two root crossed resolutions | `ACCEPT` | Distinct endpoint matchings of the complementary four-set. |
| E6 | Standard atom/root overlap alphabet | `ACCEPT` | Avoid/contain missing-index dichotomy is exact. |
| E7 | Unique transient two-co-root overlap normalizes to at most one token | `ACCEPT` | One of the two displayed NNIs is root according to cherry-root incidence. |
| E8 | Persistent nonzero token moves are category-safe | `ACCEPT` | A bridge in a connected group flow has value zero. |
| E9 | Raw doubled-disjoint inverse-cancellation row enters the standard alphabet | `BLOCKED-PROOF` | The word `(12,34|12,34)` has central values `Q_5,0,Q_5`; no source-level borrow/normalization lemma is supplied. |
| E10 | No hidden second persistent atom from every first-failure source | `BLOCKED-PROOF` | Depends on E9; the asserted state alphabet has not been proved exhaustive. |

**Unit E:** `BLOCKED-PROOF`.

Exact target: `AC_PD_5CDC_R2_3_FIRST_FAILURE_AND_LOCAL_CONFLUENCE.md`, between the one-edge atom theorem and the standard-atom critical-overlap theorem. Downstream assumption appears in R2.4 and R2.6 state definitions.

## F. R2.4 — full-state forced backbone

| ID | Claim | Audit result | Basis / defect |
|---|---|---|---|
| F1 | Standard atom/Petersen-edge dictionary | `ACCEPT` | Exact nondegenerate triality. |
| F2 | Ordered physical resolution sheets are retained | `BLOCKED-PROOF` | The roots are identified, but the ordered source/dart maps are not written. |
| F3 | Nonexit standard overlap gives one Petersen pivot turn | `ACCEPT` at coefficient level / `BLOCKED-PROOF` at source level | Shared endpoint algebra is exact; physical source composition is not established. |
| F4 | Constant-pivot run has unique nonpivot coefficient section | `ACCEPT` | All `60` ordered transitions verify the local equation. |
| F5 | Constant-pivot run has a complete source-faithful strip | `BLOCKED-PROOF` | No explicit simultaneous source-cell construction or boundary map. |
| F6 | Six-port table has four root stars and two forbidden `s--t` matchings | `ACCEPT` | Verified in all `120` nonbacktracking four-pivot cases. |
| F7 | Six-port table implies star / route-exit / forced-pair trichotomy | `BLOCKED-PROOF` | “Composition-compatible” is not connected to exterior source components by a proved theorem. |
| F8 | One initial sheet determines the entire forced route | `BLOCKED-PROOF` | No ordered-sheet transition map or monodromy calculation. |
| F9 | Immediate backtrack has coefficient word `abba` | `ACCEPT` | Direct from the forced nonpivot choices. |
| F10 | Every immediate backtrack has a labelled source bigon filling | `BLOCKED-PROOF` | No exact move sequence or exact dependency for the invoked involution/square/pentagon lift. |
| F11 | Side roots, cap block, route, support, darts, and marks are preserved | `BLOCKED-PROOF` | Preservation is asserted without literal source boundary identifications. |
| F12 | Full persistent state is one nonbranching physical Petersen walk | `BLOCKED-PROOF` | Depends on E9 and F2–F11. |

**Unit F:** `BLOCKED-PROOF`.

## Final classification

`MATERIAL CORE GAP — NO 5-CDC ACCEPTANCE`.
