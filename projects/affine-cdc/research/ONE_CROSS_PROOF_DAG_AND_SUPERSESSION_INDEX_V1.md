# One-cross five-support proof DAG and supersession index

## Research Lead control index v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `6a2bf83515d3ac8b3d38cf94735c15c38dcfbedb`.

**Purpose:** give PDL, Curator, Director, and independent auditors one unambiguous current proof surface. This index distinguishes controlling propositions, concrete supporting lemmas, finite certificates, alternate side theorems, and superseded discovery routes.

**Assurance boundary:** organisational authority only. Inclusion in this index does not add independent mathematical verification.

---

## 1. Headline theorem

The preferred cubic theorem is:

> **Simple-edge reducibility.** Every simple edge of a connected loopless bridgeless cubic multigraph has a smaller connected loopless bridgeless cross reduction, and every root-valued `E_5` flow on that reduction extends to the original graph.

The controlling statement is:

- `SIMPLE_EDGE_FIVE_SUPPORT_REDUCIBILITY_V1.md`.

Together with the explicit theta base, it gives the cubic theorem by induction.

The controlling global summary is:

- `FIVE_SUPPORT_GLOBAL_ONE_CROSS_CLOSURE_V5.md`.

---

## 2. Minimal proof DAG

### A. Intrinsic language

#### A1 — root-flow equivalence

Five indexed even supports covering every edge twice are equivalent to an `R_5`-valued flow.

Controlling source:

- `five-support/root-flow-lifting.md`.

#### A2 — local triangle law and root triality

At a cubic vertex the roots form a `K_5` triangle. Four rooted branches have three binary resolutions, with root/root/singular triality.

Controlling sources:

- `ROOT_FLOW_TRIANGLE_COMPLEX_PACHNER_V1.md`;
- the four-root pairing-sum classification consumed throughout the branch.

#### A3 — bridge-zero law

A bridge in a group-valued flow has value zero. Therefore a connected graph carrying a root-valued flow is automatically bridgeless.

Controlling source:

- `ROOT_SURGERY_AUTOMATIC_CATEGORY_SAFETY_V1.md`.

---

### B. Structural simple-edge reduction

#### B1 — simple edge or theta

Every connected loopless cubic multigraph with more than two vertices has a simple edge; otherwise it is the two-vertex theta multigraph.

#### B2 — one valid cross closure

At a simple edge, one of the two cross reconnections is connected, loopless, bridgeless, cubic, and smaller by two vertices.

Controlling source for B1--B2:

- `ONE_CROSS_RECONNECTION_EXISTENCE_V1.md`.

Supporting graph facts:

- exterior components carry at least two terminals;
- bridge cuts are laminar;
- the two cross terminal bipartitions cross;
- simultaneous cross loops force a bridge;
- a loop in one cross closure excludes an old-bridge partition in the other.

No low-cut gluing theorem is a prerequisite.

---

### C. One-cross boundary reduction

#### C1 — selected cross trichotomy

The selected cross-edge roots are:

1. intersecting: immediate cap lift;
2. equal: equality state `A`;
3. disjoint: DDD state `C_j`.

#### C2 — six route rows

Under original-cap blocking:

- `A,B_i,C_i` form the equality outer path with route `M_i`;
- `C_j,D_i,C_k` form the DDD outer path with route `M_i`.

A separating Kempe component gives immediate repair; otherwise the singular carrier is an oriented full-channel lock.

Controlling source:

- `ONE_CROSS_SINGULAR_FIXED_ROUTE_REDUCTION_V1.md`.

Finite certificate source:

- `TEN_STATE_BOUNDARY_GRAPH_RIGIDITY_V1.md`;
- the complete ten-state route table in the earlier cap-library dossiers.

Only the six displayed rows are controlling. The complete blocked-profile classification is now an optional strengthening.

---

### D. Singular carrier termination

#### D1 — two positive Morse tables

Equality and DDD are two singular boundary orbits of one theorem schema. Every nonempty carrier admits a root `2--2` move or equal-face `2--0` cancellation lowering a positive additive triangle weight.

Controlling source:

- `SINGULAR_CARRIER_DISCRETE_MORSE_UNIFICATION_V1.md`.

Finite certificate sources:

- `EQUALITY_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`.

These are certificate subsections, not separate global architectures.

---

### E. Terminal normalisation

#### E1 — route terminal

A first route change on a descendant produces a cap-compatible terminal, not an immediate original-profile state.

- `ROUTE_CHANGE_TERMINAL_CONTEXTUAL_TRANSFER_V1.md`.

#### E2 — direct matching terminal

Every zero-vertex matching is converted to the root-soluble theta terminal. The same-matching bridge case uses one zero-to-root crossed resolution.

- `DIRECT_PAIRING_BRIDGE_TO_THETA_ZERO_RESOLUTION_V1.md`.

---

### F. Singular contextual confluence

#### F1 — first failure

Inverse transfer first fails at exactly one zero/co-root edge.

- `PACHNER_HISTORY_FIRST_FAILURE_ONE_EDGE_ATOM_V1.md`.

#### F2 — critical-overlap token grammar

The co-root token moves without branching through complete labelled critical overlaps; zero is immediately removed.

- `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`;
- `FIRST_FAILURE_NORMALIZATION_AUTOMATIC_CATEGORY_SAFETY_V1.md`.

#### F3 — constant-pivot full-state section

- `CONSTANT_PIVOT_FULL_STATE_CONTEXTUAL_CONSUMPTION_V1.md`.

#### F4 — forced Petersen backbone

Use only the retained forced-backbone scope, with full-state correction.

- `PTOLEMY_TRACK_FORCED_BACKBONE_SINK_ELIMINATION_V1.md`;
- `FORCED_BACKBONE_EVEN_CYCLE_SINK_SCOPE_CORRECTION_V1.md`;
- `SIX_OUTPUT_FULL_STATE_CYCLE_CORRECTION_V1.md`.

#### F5 — orientation-hardened odd exclusion

Every pivot-closed physical subtrack has even length; odd double-lap recurrence is excluded at the first lap.

- `ORIENTED_ODD_PETERSEN_SUBTRACK_EXCLUSION_V1.md`.

Supporting orientation sources:

- `ORIENTED_CHANNEL_LOCK_BOUNDARY_CALIBRATION_V1.md`;
- `FORCED_DDD_BACKBONE_BINARY_TRANSPORT_V1.md`;
- `PETERSEN_RESOLUTION_PARITY_V1.md`.

#### F6 — even source movies

- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `PETERSEN_C6_AUTOMATIC_CATEGORY_SAFETY_V1.md`;
- `PETERSEN_C8_TWO_C6_HISTORY_FILLING_REDUCTION_V1.md`.

#### F7 — master theorem

No nonterminal sink SCC exists; terminal transfer follows by induction on target order and history length.

- `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V2.md`.

---

### G. Edge extension and induction

#### G1 — one-cross cap restoration

- `ONE_CROSS_CAP_RESTORATION_THEOREM_V1.md`.

#### G2 — simple-edge reducibility

- `SIMPLE_EDGE_FIVE_SUPPORT_REDUCIBILITY_V1.md`.

#### G3 — cubic induction

Theta base plus repeated simple-edge reduction.

- `FIVE_SUPPORT_GLOBAL_ONE_CROSS_CLOSURE_V5.md`.

---

### H. General-graph outer shell

Componentwise cubic assembly, port-cycle expansion/collapse, and loop reinsertion preserve exactly five indexed supports.

- `GENERAL_BRIDGELESS_FIVE_CDC_OUTER_SHELL_V1.md`.

---

## 3. Controlling main-line propositions

The shortest proof has only four packages.

### Package A — root language

A1--A3.

### Package B — structural reducibility

B1--B2.

### Package C — edge extension

C1--C2, D1, E1--E2, F1--F7, G1.

### Package D — induction and outer shell

G2--G3, H.

---

## 4. Demoted but valid side results

The following are not controlling prerequisites:

- cyclic two-cut gluing;
- cyclic three-cut gluing;
- cyclic four-cut gluing;
- all-three reconnection category theorem;
- complete blocked-profile classification `J_i` or `J_i union L_i`;
- Type T physical commutation elimination;
- Type H BBD/DDD physical commutation elimination;
- cyclically five-edge-connected reduction;
- secondary-defect three-edge localisation and endpoint equalisation;
- general defect-tree rootification;
- affine `A_3` translation, Type-X, flat-code, octahedral Stokes, and `D_8` cohomology programmes.

They remain:

- independent structural theorems;
- alternate certificates;
- possible audit cross-checks;
- potential fallback routes if the one-cross spine fails.

They must not silently re-enter the PDL DAG.

---

## 5. Quarantined or superseded implications

Do not use:

1. local Ptolemy coherence as automatic global history coherence;
2. an even Petersen coefficient core as an automatic four-pole;
3. abstract longitudinal tube roots as a pointwise history lift;
4. a route change on a descendant as an immediate original-profile intersection;
5. a same-matching bridge terminal as an original category discharge;
6. collapsed pivot skeleton as a complete full-state invariant;
7. one-lap odd parity alone as exclusion of double-lap recurrence;
8. any claim that all three reconnection closures or low-cut reduction are required.

Use the corresponding controlling corrections listed in Sections 2 and 6.

---

## 6. Proper PDL reconstruction sequence

PDL should reconstruct in this order:

1. Package A from first principles;
2. B1--B2 independently, including repeated terminal endpoints;
3. C1--C2 from the six labelled route rows;
4. the two finite Morse certificates;
5. terminal normalisation;
6. first-failure and full-labelled token grammar;
7. orientation-hardened cycle reduction;
8. `C6/C8` source movies;
9. the abstract confluence induction;
10. one-cross cap restoration;
11. simple-edge induction;
12. the outer shell.

A failure at any step must be returned to AC-RL as a concrete mathematical defect. PDL should not repair it by importing a demoted side theorem unless the new dependence is made explicit.

---

## 7. Audit attack surface

The most load-bearing attack points are:

1. one-cross bridge-cut/loop argument;
2. physical uniqueness of the six blocked route rows;
3. equality and DDD no-local-minimum finite tables;
4. first-failure exhaustiveness;
5. critical-overlap nonbranching with complete source incidences;
6. cap-block orientation preservation on every descendant;
7. exclusion of odd pivot-closed subtracks, including double laps;
8. seam compatibility of the `C8` decomposition;
9. lexicographic noncircularity;
10. memberwise support projection in the outer shell.

---

## 8. Current exact authority

At this index commit, the controlling authorial endpoint is:

- `SIMPLE_EDGE_FIVE_SUPPORT_REDUCIBILITY_V1.md` for the cubic mechanism;
- `FIVE_SUPPORT_GLOBAL_ONE_CROSS_CLOSURE_V5.md` for the global summary;
- the present index for dependencies and supersession.

No claim of established theorem status follows from this designation.
