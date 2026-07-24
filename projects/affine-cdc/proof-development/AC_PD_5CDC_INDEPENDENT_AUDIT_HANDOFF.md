# AC-PD-5CDC — independent audit handoff

**Prepared by:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Mathematical candidate to audit:** `Yuren-Tang/mathematics:proof-development/affine-cdc-rigour-v1@1f57422e0e415d8902d56eb294183815c0a0b640`  
**Frozen RL source:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1@71a10f9ba86c1d2b8b7885e78fa9baa303c77818`  
**This handoff:** post-snapshot audit guide only; it does not change the frozen mathematical candidate.

---

## 1. Required independence

The auditor must not infer correctness from:

- RL or PDL completion classifications;
- the number of supporting dossiers;
- agreement between RL and PDL prose;
- the prior Programme A/B curation or Lean corpus, except where the frozen proof
  explicitly imports an already accepted theorem;
- computational certificates without independent reproduction;
- the fact that a boundary-equivalent diagram is aesthetically natural.

Every load-bearing theorem below should be independently reconstructed or
attacked by a counterexample.

---

## 2. Headline candidate

The frozen snapshot claims:

\[
\boxed{\text{Every finite bridgeless multigraph has a five-cycle double cover.}}
\]

The shortest claimed proof is:

\[
R0\to R1\to R2.1\to R2.2\to R2.3\to R2.4\to R2.6\to R2.7
\to Q_N/P_N\to\text{outer shell}.
\]

`R2.5` and the old global `C6/C8` route are not required by the shortest proof.

---

## 3. Audit units and attack questions

### A. `R0` — five supports / root flow

Files/authority:

- controlling Programme B1 equivalence;
- final DAG.

Reconstruct:

- five vertex-even supports with exact multiplicity two imply an `R_5` root on
  every cubic edge;
- every cubic vertex receives one support triangle;
- converse coordinatewise evenness;
- no hidden assumption that the five supports are distinct or nonempty.

### B. `R1` — one-cross structural reduction

File:

- `AC_PD_5CDC_R1_ONE_CROSS_STRUCTURAL_REDUCTION.md`.

Attack:

- connected/disconnected exterior cases;
- loops in the two cross closures;
- old bridges versus newly created bridges;
- parallel edges;
- proof that at least one cross is simultaneously connected, loopless and
  bridgeless;
- theta as the exact no-simple-edge base.

### C. `R2.1` — finite boundary/route certificate

File:

- `AC_PD_5CDC_R2_1_BOUNDARY_ROUTE_CERTIFICATE.md`.

Reproduce independently:

- `640` conserved ordered root boundaries;
- ten state triples and counts;
- `J_i`, `K_i` and `J_j cap K_i={B_j}`;
- all sixteen route-row types;
- fixed-route graph `P_3 sqcup C_4 sqcup P_3`;
- uniqueness of the non-`K_i` route in equality and DDD rows.

Do not infer physical route existence from the finite target table alone.

### D. `R2.2` — current-flow Morse descent

File:

- `AC_PD_5CDC_R2_2_SINGULAR_MORSE_DESCENT.md`.

Recompute:

- all equality flip changes and the `9/12/9` split;
- secondary `Phi` on the twelve neutral faces;
- DDD weight table;
- strict decrease under every selected root NNI;
- strict decrease under every equal-face cancellation;
- no omitted positive-vertex terminal or forbidden source move.

### E. `R2.3` — first failure / critical overlaps

File:

- `AC_PD_5CDC_R2_3_FIRST_FAILURE_AND_LOCAL_CONFLUENCE.md`.

Attack:

- exactly one zero/co-root first failure;
- all four-root pairing patterns;
- quadruple equality;
- missing-index doubled-disjoint row;
- two-co-root transient tree normalization;
- source category safety;
- no hidden second persistent atom.

### F. `R2.4` — full-state physical track

File:

- `AC_PD_5CDC_R2_4_FULL_STATE_FORCED_BACKBONE.md`.

Attack:

- atom/Petersen-edge dictionary with ordered resolution sheets;
- every nonexit critical overlap really gives a Petersen pivot turn;
- unique nonpivot section of an arbitrary constant-pivot run;
- six-port star/forced-route alternative;
- no independent route bit at consecutive cells;
- source-faithful immediate-backtrack bigon filling;
- retention of all side roots, cap block, route and dart data.

### G. `R2.6` — cellwise track erasure

File:

- `AC_PD_5CDC_R2_6_CELLWISE_TRACK_ERASURE.md`.

Mandatory independent checks:

1. Reproduce all `120` ordered nonbacktracking four-pivot cases.
2. Verify the human normal form `s=12,t=34` and the exact side-root word
   `(z,z,w,w)`.
3. Verify there is one zero and two root middle pairings and that the two root
   topologies differ by one legal relative NNI.
4. Check consecutive pivot changes and identity subdivision: collars must have
   disjoint interiors without inserting a non-source state.
5. Check the constant-run section at both seam endpoints, including crossed
   resolution order.
6. Check literal equality of source dart slots, roots, side data, support
   transport, cap block, route and suspended marks at every glue seam.
7. Check the no-pivot-change closed run separately.
8. Check open tracks with switch--pop collars.
9. Check one-unresolved-endpoint scope: it must remain unresolved.
10. Check the periodic cylinder, connected legal root `1`-skeleton and proper
    crosscut.

Primary falsification target:

> Find one decorated change cell or seam/run endpoint for which coefficient
> compatibility holds but the complete physical source boundary does not glue.

### H. `R2.7-HW1` — witnessed recursion / child fidelity

Files:

- `...MUTUAL_INDUCTION_HISTORY_WITNESS.md`;
- `...CHILD_CONTEXT_FIDELITY.md`.

Attack:

- exact old arbitrary-flow call;
- noncircular proof order `Q_N` then `P_N`;
- every cancellation child starts from inherited flow;
- disconnected child really implies a cyclic two-edge cut;
- connected child is a literal lower `Q` instance;
- child route/bounded/separator exits remain valid parent exits.

### I. `R2.7-HW2/HW3` — genealogy and consumer alphabet

Files:

- `...FULL_LABELLED_GENEALOGY_GLUING.md`;
- `...FIXED_ORDER_CONSUMER_COMPATIBILITY.md`.

Attack:

- edge identity versus ordered dart lineage;
- active-diagonal lineage maps;
- central-mark consumption versus suspended replacement mark;
- literal endpoint equality at concatenation seams;
- proof that every nonterminal support switch can be omitted from the chosen
  history or moved to a root/switch--pop collar;
- proof that no raw support-switch atom cell enters a closed singular core.

### J. `R2.7` — target boundary and resolved-call rank

File:

- `AC_PD_5CDC_R2_7_RESOLVED_CALL_CONTEXTUAL_TRANSFER.md`.

This is the highest-priority audit unit.

Check:

1. Every discrepancy state retains one literal ordinary target-parent boundary.
2. Every cellwise replacement fixes that boundary, not merely the coefficient
   endpoint orbit.
3. At zero singular complexity the comparison ends on the selected parent
   topology `p(T)`, not an arbitrary root topology in the same ordinary
   component.
4. The finite resolved relation is genuinely saturated under every replacement
   used in the no-sink proof.
5. Every resolved-call cycle expands to a finite, well-bracketed source witness.
6. Innermost compression preserves the target-parent segmentation of the cycle.
7. Applying the fixed-order theorem obligation by obligation really converts the
   recurrence to strict `d_top` descent.
8. Directed distance `d_N` is taken only after terminal reachability has been
   proved.
9. The `(N,d_N)` induction does not invoke same-level `P_N` or an unranked parent
   reset.
10. Original-prefix consumption is immediate and never reintroduced by inner
    normalization.

Primary falsification target:

> Construct a boundary-equivalent root replacement of a singular recurrence
> which fails to realize the selected parent topology, leaving only an arbitrary
> root NNI loop.  Such an example would invalidate the no-sink step.

### K. Cap/route consumer

File:

- `AC_PD_5CDC_R2_TO_R1_CAP_ROUTE_CONSUMER_AUDIT.md`.

Check:

- one selected cross suffices;
- initial separating rescue occurs on the original four-pole;
- descendant route change is only a terminal for contextual return;
- same-matching direct terminal uses zero-to-theta resolution;
- every direct terminal after surgery is returned before an original profile
  conclusion;
- one global `S_5` permutation aligns all five terminal traces;
- no all-three-reconnection or complete-profile theorem is silently restored.

### L. General-graph outer shell

File:

- `AC_PD_5CDC_GENERAL_GRAPH_OUTER_SHELL.md`.

Check:

- port-cycle expansion at degree two and parallel edges;
- looplessness and bridgelessness of every expanded edge;
- componentwise common five-index set;
- vertex-even/cut-even equivalence upstairs;
- exact cut correspondence under collapse;
- exact edge multiplicity under projection;
- loops added to two supports preserve evenness;
- standard `5-CDC` definition permits five even subgraphs rather than five
  connected circuits.

---

## 4. Forbidden audit shortcuts

Do not accept the proof by restoring any of these superseded claims:

- arbitrary lower-order terminal flow;
- automatic inverse weld;
- generic two-edge marked-flow selection;
- child-prefix versus parent-prefix descent;
- permanent central-mark count;
- support-switch cells as Ptolemy cells;
- global canonical `C6/C8` section;
- proper Petersen subcycle as whole annulus;
- descendant/original profile identification;
- same-matching bridge as final discharge;
- all-three reconnection solubility.

---

## 5. Required audit output

For every unit `A--L`, return one of:

- `ACCEPT`;
- `ACCEPT WITH EXPLICIT REPAIR`;
- `BLOCKED-PROOF`;
- `COUNTEREXAMPLE`;
- `OUT OF SCOPE / DEPENDENCY NOT ASSURED`.

For every non-`ACCEPT` item provide:

- exact file and theorem/line target;
- smallest concrete configuration;
- whether the defect is coefficient-only, source-topological, contextual,
  well-foundedness, definition, or attribution;
- whether repair changes downstream statements.

Final classifications:

1. `FULL CANDIDATE ACCEPTED FOR CURATOR INTAKE`;
2. `ACCEPTED AFTER LISTED LOCAL REPAIRS`;
3. `MATERIAL GAP — NO 5-CDC ACCEPTANCE`;
4. `COUNTEREXAMPLE TO CANDIDATE`.

No audit result may imply Lean, manuscript, release or publication status unless
separately authorised.
