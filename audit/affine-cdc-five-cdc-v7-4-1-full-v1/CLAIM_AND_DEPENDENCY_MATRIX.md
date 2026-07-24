# AC-5CDC-AUD-V741 — claim and dependency matrix

**Candidate:** `f90a068fbcc81d34850bb53426f4c2efb4cb5388`  
**Legend:** `VERIFIED`, `VERIFIED-CONDITIONAL`, `NO-BLOCKER-FOUND`, `MATERIAL-GAP`, `DOWNSTREAM-BLOCKED`, `PERMANENTLY-FALSE`.

| Node / claim | Controlling source | Independent disposition | Reason |
|---|---|---|---|
| Root arithmetic in `E_5` | R2.1; v7.2/v7.4 inverse tables | **VERIFIED** | Direct two-subset enumeration gives only weights `0,2,4`; pair counts `10/30/15`; no fourth parent value. |
| Conserved boundary-state census | `AC_PD_5CDC_R2_1_BOUNDARY_ROUTE_CERTIFICATE.md` | **VERIFIED** | Fresh enumeration gives `640` ordered words and the stated ten state counts.  This is only a finite boundary classification. |
| One valid smaller cross | `AC_PD_5CDC_R1_ONE_CROSS_STRUCTURAL_REDUCTION.md` | **VERIFIED** | The exterior-component and bridge-split arguments prove that one cross closure is connected, loopless, bridgeless, cubic and of order `N-2`; theta is the no-simple-edge base. |
| Current-flow singular Morse termination | `AC_PD_5CDC_R2_2_SINGULAR_MORSE_DESCENT.md` | **NO-BLOCKER-FOUND** | The displayed positive additive potentials and no-local-minimum eliminations prove termination of the forward current-flow surgery.  The file correctly does not claim inverse return. |
| Target-synchronised prefix to first cancellation | `AC_PD_5CDC_V7_2_FIRST_CANCELLATION_AND_SINGLE_POP.md` | **NO-BLOCKER-FOUND** | Accepted internal steps are root NNIs on the cross plus valid parallel target NNIs; route/category failures are terminalised; the positive potential makes the prefix finite. |
| Actual-target lower-order call | same | **VERIFIED-CONDITIONAL** | In the genuine branch the target cap closure is connected, loopless, bridgeless, cubic and of order `N-2`.  Strong induction may be applied there. |
| Single arbitrary-flow inverse pop | same | **VERIFIED** | Intersecting, equality, good-disjoint and missing-index rows exhaust the algebra; fresh borrowing enumeration gives `180=120+60`; the missing-index source movie leaves at most one standard atom. |
| Local one-atom critical overlaps | `AC_PD_5CDC_R2_3_FIRST_FAILURE_AND_LOCAL_CONFLUENCE.md`; v7.2 state-walk | **VERIFIED** | The local alphabet has no persistent branching and at most one atom after the bounded two-co-root overlap normalization. |
| Constant-pivot runs and six-port seams | `AC_PD_5CDC_V7_2_STATE_WALK_CELLWISE_RECONSTRUCTION.md` | **VERIFIED IN STATED SCOPE** | Fresh enumeration gives all `120` nonbacktracking seam cells; the file proves run/seam gluing for a supplied finite comparison. |
| Arbitrary one-atom state reaches complete root endpoint or exact terminal | asserted in v7.3/v7.4/v7.4.1 integration | **MATERIAL-GAP** | The v7.2 state-walk theorem expressly leaves construction of the finite continuation comparison, prescribed-parent endpoint realization and a well-founded scheduler open.  No v7.4.1 theorem supplies them. |
| General rooted-carrier component chain | old `FC-COMPONENT-CHAIN-ROOT-NNI` | **PERMANENTLY-FALSE** | #81 Heawood carrier has a third terminal path; fresh enumeration gives 36 category-safe outputs and zero inherited length-one chains. |
| Exact-two-terminal-path component chain | `AC_PD_V7_4_1_APPLICATION_SCOPED_COMPONENT_CHAIN.md` | **VERIFIED** | Under the explicit decomposition, internal quotient nodes are exactly inactive singletons or closed cycles; one fixed connector list contracts literally and the final matching changes. |
| Co-root terminal-exhaustion constructor | #82 census; v7.4.1 co-root reclosure | **VERIFIED IN APPLICATION SCOPE** | Cutting exactly two nonadjacent marked edges of one channel cycle creates exactly four terminals and two arcs; all other channel components remain closed. |
| Zero-parent terminal-exhaustion constructor | #82 census; v7.4.1 zero reclosure | **VERIFIED IN APPLICATION SCOPE** | Deleting the active cell exposes exactly four selected-channel branch darts; the central edge is nonchannel; exactly two paths remain. |
| #78 arbitrary equal-face / `Xi` totality | frozen negative audit | **PERMANENTLY-FALSE** | `9-14:23` preserves the marked route.  v7.4.1 does not use it as a provider. |
| Co-root prescribed-parent application escape | `FC-PURE-NNI-CO-ROOT-APPLICATION-ESCAPE` | **VERIFIED-CONDITIONAL** | Once a complete root-valued prescribed-parent state is genuinely available, the scoped constructor, component chain and final separation/opposite-route classification close the fibre.  Universal entry into that state is blocked upstream. |
| Zero-parent application escape | `FC-PURE-NNI-ZERO-PARENT-APPLICATION-ESCAPE` | **VERIFIED-CONDITIONAL** | Once the complete state is available, the exact constructor, crossed matching, sheet alignment, component switch and literal parent NNI close the fibre.  Universal entry is blocked upstream. |
| No-rank-reset inside one parent obligation | v7.4.1 inverse/prefix reclosure | **VERIFIED-CONDITIONAL** | The pair `(L,C)` is well-founded after an application chain is opened: one list is fixed and `C` decreases; a new list is opened only after literal parent success lowers `L`. |
| Complete stored-prefix return | v7.4.1 inverse/prefix reclosure | **DOWNSTREAM-BLOCKED** | It requires every one-atom output to reach the complete root endpoint at which the parent table is evaluated. |
| Exact terminal consumers | v7.2 terminal census; current-descendant ledgers | **NO-BLOCKER-FOUND** | Cut completions are strictly smaller; bounded bases are explicit; no component-chain move introduces a new terminal type.  This does not repair the nonterminal one-atom gap. |
| Ordinary cubic induction | v7.4.1 inverse/prefix reclosure and proof DAG | **DOWNSTREAM-BLOCKED** | The return step is incomplete.  Two uses of `P_{N-2}`—the initial cross input and the actual cancellation target—are both strictly lower, but the same-order inverse return is not proved. |
| Cubic five-support theorem | v7.4.1 proof DAG | **DOWNSTREAM-BLOCKED** | Depends on the incomplete ordinary induction. |
| General-graph outer shell | `AC_PD_5CDC_GENERAL_GRAPH_OUTER_SHELL.md` | **VERIFIED-CONDITIONAL** | Port-cycle expansion is cubic and bridgeless; memberwise collapse preserves cut parity and exact multiplicity; loops may be inserted in two fixed supports.  It requires the cubic theorem as input. |
| Every finite bridgeless multigraph has a five-CDC | candidate conclusion | **DOWNSTREAM-BLOCKED** | The conditional outer shell cannot bridge the missing cubic return theorem. |

## Exact dependency cut

The first unavailable edge in the claimed active DAG is

```text
one standard co-root atom
    -/-> complete root-valued prescribed-parent state or exact terminal.
```

All nodes strictly downstream of that edge are conditional only.  The v7.4.1 application-scoped component-chain repair is mathematically useful and passes its own scope audit, but it begins after the missing edge and therefore cannot close it.
