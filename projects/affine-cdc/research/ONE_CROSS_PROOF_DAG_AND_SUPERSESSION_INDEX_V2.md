# One-cross five-support proof DAG and supersession index

## Research Lead control index v2

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `550bbb43189bb72af1c000ccd41fdc5a3707d8c6`.

**Supersedes for controlling use:** `ONE_CROSS_PROOF_DAG_AND_SUPERSESSION_INDEX_V1.md`.

**Purpose:** provide PDL, Curator, Director, and future auditors one unambiguous current proof surface after the finite-condensation and relative-colored-weld compression.

**Assurance boundary:** organisational authority only. Inclusion here adds no independent mathematical verification.

---

## 1. Headline theorem

The preferred cubic theorem is:

> **Simple-edge reducibility.** Every simple edge of a connected loopless bridgeless cubic multigraph has a smaller connected loopless bridgeless cross reduction, and every root-valued `E_5` flow on that reduction extends to the original graph.

Controlling statement:

- `SIMPLE_EDGE_FIVE_SUPPORT_REDUCIBILITY_V1.md`.

Together with the theta base, this gives the cubic theorem by induction.

Current controlling global summary:

- `FIVE_SUPPORT_GLOBAL_ONE_CROSS_CLOSURE_V6.md`.

---

## 2. Four-package proof surface

### Package A — intrinsic root language

#### A1 — root-flow equivalence

Five indexed even supports covering every edge twice are equivalent to an `R_5`-valued flow.

- `five-support/root-flow-lifting.md`.

#### A2 — triangle law and root triality

At each cubic vertex the roots form a `K_5` triangle. A four-root interface has root/root/singular triality.

- `ROOT_FLOW_TRIANGLE_COMPLEX_PACHNER_V1.md`;
- the exact four-root pairing-sum classification.

#### A3 — bridge-zero

A bridge in a group-valued flow has value zero. Root-valued outputs are therefore automatically bridgeless componentwise.

- `ROOT_SURGERY_AUTOMATIC_CATEGORY_SAFETY_V1.md`.

---

### Package B — structural simple-edge reduction

#### B1 — simple edge or theta

A connected loopless cubic multigraph without a simple edge is theta.

#### B2 — one valid cross closure

At every simple edge, at least one of the two cross closures is connected, loopless, bridgeless, cubic, and smaller by two vertices.

- `ONE_CROSS_RECONNECTION_EXISTENCE_V1.md`.

Controlling graph ingredients:

- exterior components have at least two terminals;
- bridge cuts are laminar;
- the two cross terminal bipartitions cross;
- simultaneous cross loops force a bridge;
- a loop in one cross closure is incompatible with an old-bridge partition in the other.

No low-cut gluing theorem is a prerequisite.

---

### Package C — relative colored edge extension

#### C1 — selected-cross trichotomy

For the selected cross flow:

1. intersecting roots restore the cap;
2. equal roots give equality state `A`;
3. disjoint roots give DDD state `C_j`.

#### C2 — six route rows

Under cap blocking:

- `A,B_i,C_i` form the equality outer path with route `M_i`;
- `C_j,D_i,C_k` form the DDD outer path with route `M_i`.

A separating component repairs the cap; otherwise the carrier is an oriented full-channel lock.

- `ONE_CROSS_SINGULAR_FIXED_ROUTE_REDUCTION_V1.md`.

Finite certificate only:

- `TEN_STATE_BOUNDARY_GRAPH_RIGIDITY_V1.md`;
- earlier complete route tables.

The complete blocked-profile theorem is not controlling.

#### C3 — singular Morse termination

Equality and DDD are two singular orbits of one positive additive triangle-Morse theorem.

- `SINGULAR_CARRIER_DISCRETE_MORSE_UNIFICATION_V1.md`.

Finite certificate parents:

- `EQUALITY_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`.

#### C4 — terminal normalisation

- route terminal: `ROUTE_CHANGE_TERMINAL_CONTEXTUAL_TRANSFER_V1.md`;
- direct matching/theta terminal: `DIRECT_PAIRING_BRIDGE_TO_THETA_ZERO_RESOLUTION_V1.md`.

#### C5 — first-failure localisation

The first failed inverse move creates exactly one zero/co-root edge and preserves the full exterior cap context.

- `PACHNER_HISTORY_FIRST_FAILURE_ONE_EDGE_ATOM_V1.md`.

#### C6 — complete one-token grammar

Zero is removed immediately in the same-order flip layer. A co-root token moves without branching through labelled critical overlaps.

- `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`;
- `FIRST_FAILURE_NORMALIZATION_AUTOMATIC_CATEGORY_SAFETY_V1.md`.

#### C7 — constant-pivot and forced-backbone full state

- `CONSTANT_PIVOT_FULL_STATE_CONTEXTUAL_CONSUMPTION_V1.md`;
- `PTOLEMY_TRACK_FORCED_BACKBONE_SINK_ELIMINATION_V1.md`;
- `SIX_OUTPUT_FULL_STATE_CYCLE_CORRECTION_V1.md`;
- all applicable scope corrections.

#### C8 — orientation-hardened odd exclusion

Every pivot-closed physical subtrack stabilizes the cap-distinguished block and therefore has even length. The first lap already excludes odd double traversal.

- `ORIENTED_ODD_PETERSEN_SUBTRACK_EXCLUSION_V1.md`.

Supporting sources:

- `ORIENTED_CHANNEL_LOCK_BOUNDARY_CALIBRATION_V1.md`;
- `FORCED_DDD_BACKBONE_BINARY_TRANSPORT_V1.md`;
- `PETERSEN_RESOLUTION_PARITY_V1.md`.

#### C9 — even source movies

- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `PETERSEN_C6_AUTOMATIC_CATEGORY_SAFETY_V1.md`;
- `PETERSEN_C8_TWO_C6_HISTORY_FILLING_REDUCTION_V1.md`.

#### C10 — finite-condensation contextual return

For one fixed history and target order, the complete contextual graph is finite. Prefix level is SCC-constant. No nonterminal sink SCC survives. The condensation DAG supplies same-order rank; only target-order induction remains.

- `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V3.md`.

This supersedes v1 and v2. Do not reconstruct a second explicit induction on history length.

#### C11 — cap restoration

- `ONE_CROSS_CAP_RESTORATION_THEOREM_V1.md`.

---

### Package D — induction and outer shell

#### D1 — simple-edge reducibility

- `SIMPLE_EDGE_FIVE_SUPPORT_REDUCIBILITY_V1.md`.

#### D2 — cubic induction

Theta base plus repeated simple-edge reduction.

- `FIVE_SUPPORT_GLOBAL_ONE_CROSS_CLOSURE_V6.md`.

#### D3 — general graph shell

Componentwise cubic assembly, port-cycle expansion/collapse, and loop reinsertion preserve exactly five indexed supports.

- `GENERAL_BRIDGELESS_FIVE_CDC_OUTER_SHELL_V1.md`.

---

## 3. Mechanism interpretations and no-go boundaries

These files guide architecture but are not substitutes for the controlling lemmas.

### M1 — direct defect-minimal shortcut boundary

- `SINGLE_DEFECT_DIRECT_AUGMENTATION_BOUNDARY_V1.md`.

Controlling warning:

> a defect-removing root NNI changes source topology; returning a root flow through the inverse NNI is exactly contextual transfer.

A real bypass requires fixed-topology simulation or extendable-orbit selection.

### M2 — relative colored-weld interpretation

- `COLOURED_PACHNER_RELATIVE_WELD_INTERPRETATION_V1.md`.

Interpretation:

- root flow = proper five-coloring of the triangle pseudocomplex;
- root NNI = colored `2--2` flip;
- equal-face cancellation = colored weld;
- first failure = improper inverse weld;
- forced Petersen token = relative projectivity;
- v3 confluence = a special relative five-colored weld theorem.

Known colored Pachner connectivity assumes both endpoints already colored and is not a proof of R2.

### M3 — naked boundary-counting reconnaissance

- `BOUNDARY_COUNTING_ORBIT_SELECTION_RECONNAISSANCE_V1.md`.

No naked ten-state linear or elementary quadratic identity is controlling. Any future counting shortcut must use a reproducible enriched labelled/route tensor.

---

## 4. Superseded global surfaces

Do not use as controlling proof summaries:

- `FIVE_SUPPORT_GLOBAL_MINIMAL_COUNTEREXAMPLE_CLOSURE_V1.md`;
- `FIVE_SUPPORT_GLOBAL_MINIMAL_COUNTEREXAMPLE_REPAIRED_V2.md`;
- every intermediate one-cross global summary through v5.

Use:

- `FIVE_SUPPORT_GLOBAL_ONE_CROSS_CLOSURE_V6.md`.

---

## 5. Superseded contextual masters

Do not use as controlling:

- `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V1.md`;
- `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V2.md`.

Use:

- `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V3.md`.

V2 remains a valid alternate proof-order formulation conditional on the same hypotheses; v3 is preferred because it replaces history-length induction by condensation rank.

---

## 6. Demoted side theorem families

The following may remain correct and useful but are not prerequisites of the current one-cross proof:

1. two-/three-/four-cut gluing programmes;
2. all-three reconnection category theorem;
3. complete ten-state blocked-profile classification;
4. Type T/Type H four-cut mismatch elimination;
5. cyclically five-edge-connected reduction;
6. full-defect-tree descent;
7. affine `A_3`, selector-plane, flat-code, Stokes, and `D_8` cohomology programmes;
8. abstract root-tube filling and any tube-to-history implication;
9. naked support-unordered boundary-count identities.

PDL must not reconstruct them merely because they occur earlier in discovery chronology.

---

## 7. Current load-bearing attack surface

The compressed cubic proof has two headline propositions.

### R1 — structural reducibility

At every simple edge, one valid smaller cross closure exists.

### R2 — relative colored edge extension

Every root flow on that selected cross closure extends to the original graph.

Within R2 the most attack-sensitive arrows are:

1. physical validity of all six route rows;
2. no-local-minimum finite certificates for both singular Morse tables;
3. complete one-token critical-overlap exhaustiveness;
4. retention of all side/support/cap data through constant-pivot sections;
5. orientation stabilization of every pivot-closed physical subtrack;
6. source-level `C6` movie and `C8` seam compatibility;
7. finiteness of the complete contextual graph;
8. prefix monotonicity and sink-SCC elimination;
9. componentwise lower-order recursion after cancellation.

Failure of R1 or any indispensable R2 arrow destroys the compressed candidate.

---

## 8. Current research bypass targets

AC-RL may continue to seek:

### Target F'

A general relative five-colored weld theorem that proves R2 without Petersen-specific analysis.

### Target O+

An enriched labelled/route tensor or orbit-selection theorem guaranteeing one extendable cross flow.

Neither target is presently established or controlling.

---

## 9. Current classification

\[
\boxed{
\text{COMPLETE MINIMAL AUTHORIAL CANDIDATE}
}
\]

with:

\[
\boxed{
\text{FINITE-CONDENSATION CONTEXTUAL RETURN}
+
\text{RELATIVE COLOURED-WELD INTERPRETATION}
}
\]

and assurance boundary:

\[
\boxed{
\text{NOT PDL-RECONSTRUCTED}
/
\text{NOT INDEPENDENTLY ACCEPTED}.
}
