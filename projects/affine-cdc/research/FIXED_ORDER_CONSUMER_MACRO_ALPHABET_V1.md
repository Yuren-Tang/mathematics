# The fixed-order consumer sees only normalized macro endpoints

## Research Lead consumer-alphabet theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**PDL interface:** `AC-PD-5CDC-HW3`.

**Parents:**

- `NESTED_CANCELLATION_BUBBLE_COMPRESSION_V1.md`;
- `INNERMOST_CANCELLATION_BUBBLE_RAW_INSERTION_LIFT_V1.md`;
- `WELD_INSERTION_SUPPORT_SWITCH_LIFT_V1.md` v2;
- the central/adjacent one-atom NNI movies;
- the endpoint equality/DDD normalization theorems;
- `THETA_ROOT_FLOW_SUPPORT_SWITCH_CONNECTIVITY_V1.md`;
- the fixed-order closed/open/Petersen track consumer.

**Status:** exact scheduling and interface theorem. Lifted support-switch corrections, bounded one-atom movies and endpoint alternative insertions need not be added as recurrent cell types to the Ptolemy/Petersen no-sink theorem. They occur inside finite witnessed macros whose complete histories are retained for genealogy, but whose internal states are not rescheduled by the outer fixed-order consumer. The consumer receives only the normalized predecessor-order endpoint: a root state, one standard co-root atom with its two crossed resolutions, or an accepted exit. Consequently the recurrent consumer alphabet remains the already proved root-NNI/first-failure/Petersen-track alphabet.

---

## 1. Three scheduling layers

The witnessed contextual proof has three distinct kinds of evolution.

### Layer A — forward current-flow search

Equality/DDD Morse descent selects explicit root NNIs, root support switches, route events and strict cancellations. Between cancellations its positive integer potential strictly decreases. This layer is finite before any recursive call.

### Layer B — witnessed cancellation-return macro

A strict cancellation opens a child frame. The lower witnessed history, raw insertion lifts, support-switch corrections, bounded central/adjacent movies and endpoint borrowing are concatenated and compressed by the witnessed bubble theorem.

The complete Layer-B output is one predecessor-order endpoint:

\[
\boxed{
\text{root state}
\quad\text{or}\quad
\text{one normalized co-root state}
\quad\text{or}\quad
\text{accepted exit}.}
\]

### Layer C — fixed-order discrepancy consumer

Only if Layer B returns one normalized co-root state does the closed/open/Petersen track consumer begin. Its task is to rootify that endpoint discrepancy or leave through a route/bounded/category terminal.

These layers are executed sequentially. Internal Layer-B states are witness data, not new Layer-C scheduling vertices.

---

## 2. Finite macro opacity

A **finite witnessed macro** consists of:

1. a declared finite list of labelled source states and moves;
2. one fixed input complete state;
3. one normalized output complete state or accepted exit;
4. the complete ancestor-incidence, cap, route and side-attachment witness.

Macro opacity means only that the outer scheduler treats the macro as one transition from its input to its output. It does not delete or forget the internal history.

### Theorem 2.1 — opacity is sound

Replacing a finite witnessed subhistory by one scheduler edge preserves:

- its exact endpoint state;
- every ancestor genealogy record;
- every accepted exit;
- global finiteness and well-foundedness.

### Proof

The internal move list is finite and already constructed. The outer scheduler makes no choice inside it and resumes only after its normalized endpoint is reached. Expanding the macro edge recovers the original decorated history verbatim. ∎

No potentially infinite process is hidden inside a macro:

- current-flow segments terminate by their Morse potential;
- child histories are finite by witnessed strong induction;
- bubble compression terminates by frame count;
- local NNI/support-switch movies have explicit finite length;
- theta recolouring needs at most three switches.

---

## 3. Root NNIs

A successful root-valued parent NNI is already an ordinary root edge of the fixed-order scheduler.

A finite path of root NNIs inside one active-diagonal or borrowing movie belongs to Layer B. It may be retained as one witnessed macro or expanded; either interpretation uses only the established root-NNI cell type.

Thus root-NNI paths require no enlargement of the consumer alphabet.

---

## 4. Lifted support-switch corrections

### Root-valued support switches

A root support switch selected by the current-flow descent belongs to Layer A and is finite under the current-flow potential.

A root support switch inside a child return or theta terminal belongs to Layer B and is part of its finite witnessed macro.

An initial horizontal separating switch which directly restores the cap is an accepted rootification terminal.

### One-atom raw support-switch lifts

`WELD_INSERTION_SUPPORT_SWITCH_LIFT_V1.md` may produce a fixed-order path state whose inserted central edge is zero or co-root. Such a state occurs inside Layer B while the lower child switch is being lifted.

The raw insertion theorem guarantees:

- every noncentral edge remains root-valued;
- there is at most one central atom;
- the macro ends at the raw insertion of the returned child flow;
- endpoint normalization is subsequently applied.

Therefore an internal support-switch correction is not exposed as a recurrent Layer-C edge.

### Theorem 4.1 — switch compatibility

The fixed-order consumer need not classify closed tracks containing arbitrary support-switch cells. Every support-switch correction is consumed inside a finite Layer-A or Layer-B macro, or is an immediate terminal. Layer C receives only its normalized endpoint.

---

## 5. Bounded one-atom movies

The complete active-diagonal table consists of explicit NNI paths:

- `B -> B`: five/six root NNIs;
- `B -> C` and its reverse: five NNIs with one terminal atom;
- `A <-> C`: five NNIs with at most one atom;
- adjacent mark: three root NNIs.

These movies are finite Layer-B witnesses. Their internal one-atom states are not independently rescheduled. Concatenation proceeds to the raw returned insertion and then to endpoint normalization.

### Theorem 5.1

Bounded one-atom movies add no recurrent generator to Layer C. Their only externally visible nonroot output is the final normalized atom already belonging to the standard first-failure grammar.

---

## 6. Endpoint alternative insertion

At the end of one returned bubble:

- equality uses the two-step five-leaf alternative insertion;
- good doubled-disjoint uses the same two-step rootification;
- missing-index produces one standard `(Q_i,Q_j,ij)` unit and immediately applies local defect-tree normalization.

Complete this endpoint macro before recording the Layer-B output.

Hence the consumer sees:

1. a root-valued original or alternative insertion topology; or
2. one normalized co-root edge with both crossed root resolutions and complete side data; or
3. an accepted bounded/category exit.

It never receives a raw zero insertion or a transient two-co-root tree.

---

## 7. Exact Layer-C alphabet

After macro normalization, the fixed-order discrepancy consumer uses only:

1. one complete normalized co-root state;
2. target-directed ordinary `2--2` comparisons;
3. one-edge first-failure/critical-overlap normalization;
4. constant-pivot root sections;
5. normalized immediate backtrack deletion;
6. full-labelled Petersen pivot transport;
7. odd-cycle exclusion;
8. `C6/C8` closed-annulus or normalized-endpoint open-strip replacement;
9. route/profile, direct/theta and separator/category exits.

This is exactly the alphabet of the retained fixed-order no-sink/track theorem. No raw support-switch cell, raw cancellation birth/death cell, zero insertion or persistent two-atom state remains.

---

## 8. No loss of genealogy or diagrammatic evidence

Macro opacity is a scheduler convention only. For final contextual gluing, the macro edge carries:

- the full sequence of support-switch edge sets;
- every NNI split system;
- all intermediate root/atom values;
- ordered frame interfaces;
- cap/route/side records.

If an auditor expands every macro, the complete variable-order decorated history is recovered. The Layer-C proof may therefore use endpoint state semantics without erasing the witness required by `HW2`.

---

## 9. `HW3` audit

The PDL checklist is resolved as follows.

| proposed input | consumer treatment |
|---|---|
| root NNI paths | native consumer cells or finite root macro |
| lifted support-switch even corrections | finite Layer-A/B macro; endpoint only exposed |
| bounded one-atom movies | finite Layer-B macro; final normalized atom only |
| endpoint alternative-insertion macros | completed before consumer entry |

### Classification

\[
\boxed{
\texttt{HW3 FIXED-ORDER CONSUMER ALPHABET CLOSED}
}
\]

No enlargement of the closed-track theorem to arbitrary support-switch cylinders is required.

---

## 10. Assurance boundary

### Exact here

- three-layer scheduler separation;
- sound finite macro opacity;
- placement of every support-switch case;
- placement of every bounded one-atom movie;
- endpoint normalization before recurrence;
- exact retained Layer-C alphabet;
- preservation of complete witness/genealogy data.

### Imported authorial mathematics

- finite current-flow potentials;
- witnessed strong induction;
- bubble compression;
- local generator lift tables;
- fixed-order track consumer.

### Not claimed

- completion of separator disposition after ancestor restoration;
- unconditional PDL R2.7 or global cap restoration;
- independent audit, Lean verification, manuscript integration, curation, release or publication.
