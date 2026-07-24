# AC-5CDC-AUDIT-SHELL-01 — cap/route trace matrix

**Candidate:** `proof-development/affine-cdc-rigour-v1@1f57422e0e415d8902d56eb294183815c0a0b640`  
**Audit branch:** `audit/affine-cdc-five-cdc-shell-v1`

This matrix follows one specified root flow on one selected valid cross closure.  “Inherited” means that labels and complete ordered context are retained through the declared move history; mere existence of some flow on the same terminal graph is not inherited return.

| Stage | Exact input | Candidate output | Quantifier/source check | Result |
|---|---|---|---|---|
| R1 selected cross | Connected loopless bridgeless cubic `G`, simple edge `uv` | One of the two cross closures is connected, loopless, bridgeless, cubic, order `N-2` | Existence of one selected cross is enough; no all-three premise is used | `ACCEPT` |
| Initial cross flow | One **specified** root flow `lambda` on selected closure `G_j` | Ordered boundary state in `J_j={A,B_j,C_j}` | Boundary labels are inherited from `lambda` | `ACCEPT` |
| Finite intersection | `sigma in J_j` and original cap profile `K_i` | `J_j cap K_i={B_j}` | Independently recomputed from all `640` conserved ordered root quadruples | `ACCEPT` |
| Immediate `B_j` | Inherited boundary state `B_j` | Root-valued cap insertion | Distinct intersecting block roots force the cap central root; no recolouring | `ACCEPT` |
| Equality separating rescue | Inherited state `A`; a separating challenge routed by `M_j` or `M_k` in the original four-pole | Immediate state in `K_i` | Route table has targets `(B_i,B_j,B_k)`; rescue occurs before descendant surgery | `ACCEPT` |
| DDD separating rescue | Inherited state `C_j`; a separating crossed challenge with nonoriginal route | Immediate state in `K_i` | Exact route row has two `K_i` targets and one non-`K_i` target | `ACCEPT` |
| Fixed route | No separating rescue | Equality path `A-B_i-C_i` or DDD path `C_j-D_i-C_k`, physical route `M_i` | Unique non-`K_i` route is literally the original cap matching | `ACCEPT` |
| Pre-route-change surgery | Root NNI/equal-face history before first route change | Same ordered four terminal slots and same boundary word | Candidate retains complete ordered boundary; no original-profile conclusion is made yet | `ACCEPT` as exported interface |
| Descendant route change | First complementary challenge realised with `M_j` or `M_k` on descendant `P_t` | A current descendant state `tau in K_i` | Correctly treated only as a terminal for `R2.7`; not asserted to lie in `Sigma(P_0)` | `ACCEPT` conditional on R2.7 |
| Cross direct terminal, inherited equality | Zero-source cross matching with inherited boundary `(p,p,p,p)` | Candidate assigns an arbitrary root triangle to the cap-attached theta | Inherited two matching edges are `p,p` and force central value `0`; arbitrary triangle changes labels without a declared history | `BLOCKED-PROOF` (`K-01`) |
| Cross direct terminal, inherited DDD | Zero-source cross matching with inherited paired roots that may be disjoint | Candidate assigns an arbitrary root triangle | Existing central sum may be a co-root; no source-faithful transport to the chosen triangle is supplied | `BLOCKED-PROOF` (`K-01`) |
| Same-matching direct terminal | Two inherited loops joined by a zero bridge | Candidate chooses distinct intersecting loop roots `p,q`, then uses the correct `(0,2,2)` crossed resolution | The `(0,2,2)` NNI is valid only after the new intersecting pair has been chosen; the change from inherited loop labels is an unproved recolouring | `BLOCKED-PROOF` (`K-01`) |
| Connected cancellation child | Specified post-cancellation root flow and restricted complete context | Literal lower-order `Q_{N-2}` instance | Graph category, order drop, outer darts, cap block, route and supports are recorded | `ACCEPT` as child-interface statement |
| Disconnected cancellation | Cancellation output has two components | Cyclic two-edge-cut exit | The cut endpoints on a cyclic shore are distinct; completion/gluing is the standard lower-order two-shore disposition | `ACCEPT` conditional on lower-order theorem |
| Child terminal return | Child `Q` call reaches terminal | Decorated history returned and lifted through stored cancellation | This is exactly what `HW1` requires, but direct-terminal rows above fail to supply it | `BLOCKED-PROOF` globally |
| Common boundary state | Four-pole and cap have equal multisets of five traces | One global `pi in S_5` aligns all traces | A multiplicity-respecting bijection of equal traces aligns every terminal root simultaneously | `ACCEPT` |
| Generic accepted exit | Route/profile, bounded, separator, category, theta or two-cut flag | Branch is declared terminated | Only some flags have visible consumers; no exact exhaustive exit-to-root-flow theorem is supplied before `P_N` | `BLOCKED-PROOF` (`K-02`) |
| `Q_N` | Every specified inherited selected-cross flow | Exit or finite decorated history from that flow to cap-compatible terminal | Direct terminal supplies only some terminal flow, not necessarily a history from the specified flow | `BLOCKED-PROOF` |
| `P_N` | Lower `P_{N-2}` gives a specified cross flow; same-level `Q_N` is invoked | Root flow on order-`N` graph | Phase order is noncircular, but the required `Q_N` premise is not established and exits are not exhaustively consumed | `BLOCKED-PROOF` |

## Independent finite boundary recomputation

Using the ten weight-two vectors of `F_2^5`, I enumerated all ordered quadruples `(r_1,r_2,r_3,r_4)` satisfying `r_1+r_2+r_3+r_4=0`.  The result is exactly `640`.  The routing-weight state counts are:

| State | Weight triple | Count |
|---|---:|---:|
| `A` | `(0,0,0)` | `10` |
| `B_0,B_1,B_2` | permutations of `(0,1,1)` | `60` each |
| `C_0,C_1,C_2` | permutations of `(0,2,2)` | `30` each |
| `D_0,D_1,D_2` | permutations of `(2,1,1)` | `120` each |

The independently generated complementary-challenge targets collapse to the same sixteen support-unordered rows stated in R2.1.  In particular, for cap index `i`, equality and DDD blocked rows have exactly one target outside `K_i`, and that target is under route `M_i`.

## Matrix conclusion

The finite cap algebra, one-cross quantifiers, descendant-return discipline, and global support permutation survive audit.  The terminal-flow/source-history interface does not.  The smallest obstruction is already present at the zero-source direct matching; no deep R2 recurrence is needed to expose it.