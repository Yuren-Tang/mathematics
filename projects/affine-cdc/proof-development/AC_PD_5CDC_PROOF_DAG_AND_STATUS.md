# AC-PD-5CDC — final proof DAG and assurance status

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**PDL branch:** `proof-development/affine-cdc-rigour-v1`  
**Frozen Research Lead authority consumed:** `research/affine-cdc-five-cdc-v1@71a10f9ba86c1d2b8b7885e78fa9baa303c77818`  
**Classification:** `COMPLETE-DRAFT / FULL HUMAN PROOF CLOSED AT PDL LEVEL / READY FOR INDEPENDENT AUDIT AND DIR-CURATOR SNAPSHOT INTAKE`.

There is no remaining declared mathematical proof gap in the PDL reconstruction.
This is not independent assurance, canonical acceptance, Lean verification,
manuscript acceptance, release or publication.

---

## 1. Headline theorem spine

\[
\begin{array}{c}
\text{five indexed even supports}\
\Updownarrow\\
R_5\text{-valued }E_5\text{ flow on a loopless cubic graph}\
\Downarrow\ R1\\
\text{one valid smaller cross closure at every simple edge}\
\Downarrow\ R2.1-R2.3\\
\text{finite boundary route + current-flow descent + one-token grammar}\
\Downarrow\ R2.4\\
\text{one full-labelled nonbranching physical co-root track}\
\Downarrow\ R2.6\\
\text{cellwise root seams + constant-run sections erase every normalized track}\
\Downarrow\ R2.7\\
\text{witnessed resolved-call contextual return}\
\Downarrow\\
Q_N\text{ witnessed edge extension}\
\Downarrow\\
P_N\text{ cubic root solubility by theta base and vertex induction}\
\Downarrow\\
\text{port-cycle expansion/collapse outer shell}\
\Downarrow\\
\boxed{\text{every finite bridgeless multigraph has a }5\text{-CDC}.}
\end{array}
\]

---

## 2. Closed proof units

| Unit | PDL file | Exact state |
|---|---|---|
| `R0` | controlling Programme B1 equivalence | five indexed even supports, root-valued `E_5` flows, `K_5` triangle labels and anisotropic `O^-(4,2)` flow formulation agree |
| `R1` | `AC_PD_5CDC_R1_ONE_CROSS_STRUCTURAL_REDUCTION.md` | every simple edge has a connected loopless bridgeless cubic cross closure with exactly two fewer vertices; theta is the no-simple-edge base |
| `R2.1` | `AC_PD_5CDC_R2_1_BOUNDARY_ROUTE_CERTIFICATE.md` | 640 conserved boundaries; ten states; exact `J_i,K_i`; sixteen route rows; `P_3 sqcup C_4 sqcup P_3`; one selected cross forces immediate cap, separating rescue or one original-cap fixed route |
| `R2.2` | `AC_PD_5CDC_R2_2_SINGULAR_MORSE_DESCENT.md` | positive equality and DDD current-flow potentials; finite root-NNI/equal-face descent; no hidden local minimum |
| `R2.3` | `AC_PD_5CDC_R2_3_FIRST_FAILURE_AND_LOCAL_CONFLUENCE.md` | exactly one zero/co-root first failure; immediate zero normalization; bounded critical overlaps; no atom proliferation |
| `R2.4` | `AC_PD_5CDC_R2_4_FULL_STATE_FORCED_BACKBONE.md` | standard atom/Petersen edge dictionary; unique full-labelled physical pivot walk; constant-run root sections; source-faithful backtrack removal; retained side/cap/route data |
| `R2.5` | `AC_PD_5CDC_R2_5_ORIENTED_ODD_EXCLUSION.md` | physical cap-block orientation excludes odd pivot-closed `C_5,C_9` and double laps |
| `R2.6` | `AC_PD_5CDC_R2_6_CELLWISE_TRACK_ERASURE.md` | every genuine pivot-change cell has a local root seam; all residual constant-pivot intervals rootify; literal gluing gives closed/open/periodic track erasure |
| `R2.7-HW1` | `AC_PD_5CDC_R2_7_MUTUAL_INDUCTION_HISTORY_WITNESS.md`; `...CHILD_CONTEXT_FIDELITY.md` | simultaneous `Q_N/P_N` recursion returns explicit child histories; disconnected cancellation is a cyclic two-cut exit |
| `R2.7-HW2` | `AC_PD_5CDC_R2_7_FULL_LABELLED_GENEALOGY_GLUING.md` | ordered-dart genealogy; suspended ancestor marks; identity gluing of nested replacements |
| `R2.7-HW3` | `AC_PD_5CDC_R2_7_FIXED_ORDER_CONSUMER_COMPATIBILITY.md` | support switches occur only as root histories or switch--pop endpoint collars; closed singular cores contain only the proved Ptolemy alphabet |
| `R2.7` | `AC_PD_5CDC_R2_7_RESOLVED_CALL_CONTEXTUAL_TRANSFER.md` | target-boundary-preserving fixed-order normalization; finite resolved-call relation; no terminal-free sink; rank `(N,d_N)`; original-prefix inverse transfer |
| R2-to-R1 | `AC_PD_5CDC_R2_TO_R1_CAP_ROUTE_CONSUMER_AUDIT.md` | descendant route states return before original-profile claims; same-matching direct terminal rootifies to theta; one global `S_5` permutation gives labelled cap gluing; `Q_N/P_N` cubic induction closes |
| outer shell | `AC_PD_5CDC_GENERAL_GRAPH_OUTER_SHELL.md` | finite port-cycle cubic expansion; memberwise cut-even collapse; loops added to two fixed supports; exactly five members retained |

---

## 3. Shortest controlling dependency route

The current shortest proof does **not** require extracting a simple Petersen
cycle and then constructing a global `C6/C8` annulus.

After `R2.4`, use the complete physical track directly:

\[
\boxed{
\text{local seam at every pivot change}
+
\text{constant-run rootification}
\Longrightarrow
\text{complete track erasure}.}
\]

Consequently `R2.5` is a correct independent strengthening and diagnostic
certificate, but it is not load-bearing for the shortest `R2.6 -> R2.7`
consumer route.

The old bounded `C6/C8` source movies remain valid local mathematics and may be
retained for exposition or independent checking; they are no longer required
to construct one global history section.

---

## 4. Exact well-foundedness architecture

### Witnessed recursion

`Q_N` starts from a specified inherited cross flow.  A strict cancellation calls
`Q_{N-2}` on the inherited child, not bare existence `P_{N-2}`.  The child
returns a decorated finite history.

### Variable-order compression

Innermost successful calls are replaced by predecessor-order histories using:

- root-NNI generator lifts;
- immediate `A/C` insertion normalization;
- switch--pop endpoint collars;
- suspended central ancestor marks;
- literal complete-state seam equality.

### Fixed-order theorem

Every discrepancy detour retains the same ordinary target-parent boundary.
Cellwise track replacement lowers unresolved/singular diagram complexity while
fixing that boundary.  At zero singular complexity it is a root-valued
realization of the selected parent topology, so `d_top` strictly decreases.
This is not an assertion that arbitrary root-valued NNI loops are absent.

### Resolved-call rank

At fixed order form the finite resolved parent relation and saturate it under the
proved boundary-equivalent macros.  A terminal-free sink cycle would expand,
compress to fixed order, and become a target-directed recurrence; the fixed-order
theorem forces strict parent-tree descent and rules it out.  Directed distance
to the terminal set is the finite rank `d_N`.

The complete strategy terminates by lexicographic induction on

\[
(N,d_N),
\]

inside the already decreasing original-history prefix.

No child history length, child/parent prefix comparison or permanent mark-count
decrease is used.

---

## 5. Exact cap/route terminal alphabet

Starting from one selected cross state:

1. `B_j`: immediate original-cap root insertion;
2. separating equality/DDD channel: immediate cap rescue;
3. fixed-route equality/DDD lock: finite current-flow history;
4. first route change on a descendant: a `K_i` terminal on that descendant,
   followed by `R2.7` return to the original four-pole;
5. cross direct matching: root theta terminal;
6. same direct matching: one zero bridge, crossed `(0,2,2)` resolution to root
   theta, followed by contextual return;
7. genuine cancellation: inherited lower `Q` call and resolved parent return;
8. disconnected cancellation: cyclic two-cut gluing exit;
9. bounded/separator/category event: declared outer exit.

A support-unordered common state glues only after one global support permutation
aligns all five terminal traces and hence every labelled terminal root.

---

## 6. Superseded controlling claims

The final proof does not use any of the following:

1. cancellation automatically completes an order-`N-2` relative obligation;
2. an arbitrary lower-order root flow can be inserted back cover-independently;
3. generic two-edge root-adjacency selection or marked-weld flow selection;
4. comparison of child history prefix with parent history prefix;
5. central-mark deletion as a permanent global descent coordinate;
6. raw support-switch atom cells as interior Ptolemy cells;
7. finite endpoint order restoration alone as variable-order compression;
8. a shortest Petersen pivot subcycle treated as a complete physical annulus;
9. simultaneous canonical stars or one global `C6` history section;
10. a descendant `K_i` state identified directly with an original-profile state;
11. a same-matching bridge terminal treated as an immediate original-graph exit;
12. flows on all three reconnection closures or complete-profile classification.

The old `AC-PD-5CDC-EQ-RETURN / MWR` and prime two-edge flexibility frontier is
retired from the controlling proof.  Its finite channel algebra and obstruction
interpretations remain mathematically interesting noncontrolling material.

---

## 7. Literature/definition boundary

The standard modern `5-CDC` convention treats a cycle as an even subgraph,
possibly disconnected, and a `k`-cycle double cover as at most `k` such members.
Thus the five indexed supports are already a standard `5-CDC`; no memberwise
circuit decomposition is required.

The targeted precedent search found no established theorem supplying the new
relative contextual-transfer mechanism.  Literature and novelty conclusions
remain subject to the separate Paper A literature/novelty audit and future
5-CDC manuscript work.

---

## 8. Current exact classification

\[
\boxed{
\begin{array}{c}
\text{R0--R1 closed}\
+\ \text{R2.1--R2.7 closed at PDL complete-draft level}\
+\ \text{one-cross cap consumer and cubic induction closed}\
+\ \text{general finite bridgeless outer shell closed}\
\hline
\text{complete human proof draft of the finite 5-CDC theorem}.
\end{array}}
\]

Therefore the branch is:

- `COMPLETE-DRAFT`;
- `READY FOR INDEPENDENT ADVERSARIAL AUDIT`;
- `READY FOR AC-DIR / AC-CORPUS-V2 SNAPSHOT INTAKE`;
- **not** independently accepted;
- **not** canonical/Curator authority;
- **not** Lean-verified;
- **not** manuscript/release/publication authority.

---

## 9. Required next stages

1. Freeze and return the exact PDL snapshot to AC-DIR.
2. Launch an independent full dependency/source-fidelity audit of the complete
   proof, with special focus on:
   - target-boundary preservation in fixed-order track replacement;
   - resolved-call SCC saturation and rank;
   - child cap/route fidelity;
   - direct-terminal zero-to-theta return;
   - support-count-preserving outer shell.
3. Curator integrates only after DIR disposition of the audit.
4. Lean and manuscript programmes require separate authorisation and must not be
   inferred from this proof-development checkpoint.
