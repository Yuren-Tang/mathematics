# Singular root-triality confluence and cover-independent terminal transport

## Research Lead master theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `4099ce53b4e4f0f40a83a249b5db88e5bdf07f4b`.

**Primary consumer:** `FIVE_CDC_MECHANISM_AND_PROOF_ARCHITECTURE_V1.md`.

**Purpose:** isolate the abstract well-founded argument behind cover-independent contextual return. Equality potentials, DDD potentials, Ptolemy histories, Petersen token walks, and the relative `C6` movie are not five independent global mechanisms. They verify separate hypotheses of one singular-confluence theorem.

**Status:** exact abstract theorem with an authorial interface map to the present five-CDC candidate. The abstract implication proved here is elementary finite-state and well-founded reasoning. The substantive mathematical burden remains the verification that the concrete root-surgery system satisfies every hypothesis with complete labelled source semantics.

---

## 1. Contexts and the two well-founded coordinates

A **root context** consists of:

1. an ordered finite cubic source multipole;
2. all exterior incidence labels;
3. its complete root boundary word;
4. the distinguished cap matching and its orientation when present;
5. any route data that must survive inverse transfer.

Its **target order** is the number

\[
N(C)
\]

of vertices in the corresponding closed cap context.

A finite forward root-surgery history is

\[
H:
C_0\longrightarrow C_1\longrightarrow\cdots\longrightarrow C_m.
\]

Every step is one of:

- a root-valued `2--2` triality/Pachner move, preserving target order;
- an equal-face `2--0` cancellation, lowering target order by two after closing the same exterior context.

For inverse transport we use the lexicographic order

\[
\boxed{
\bigl(N(C_0),m\bigr).
}
\]

Successful reversal of one regular move lowers the second coordinate. A genuine cancellation lowers the first coordinate.

---

## 2. Terminal root states

A **terminal root state** on `C_m` is a root-valued flow together with the complete labelled boundary and route data required by `C_0`.

The terminal need not be the flow used to construct the forward history.

This arbitrariness is the reason ordinary reversal of the forward proof is insufficient.

A terminal is **cap-compatible** when its boundary state belongs to the target cap profile. Route-changing terminals and direct-pairing terminals are permitted only after they have been converted into such cap-compatible root states.

---

## 3. Regular inverse transfer and first failure

Starting with a cap-compatible terminal root state on `C_m`, reverse the history while every forced central value remains a root.

If the complete inverse history succeeds, terminal transport is proved.

Otherwise let

\[
C_j\longrightarrow C_{j+1}
\]

be the first forward step whose inverse fails.

### Hypothesis F — one-edge first-failure localisation

Restoring the old local topology at the first failed inverse step produces:

1. the correct flow equation at every vertex;
2. unchanged root values on every old exterior edge;
3. exactly one non-root central edge;
4. central value
   \[
   0
   \quad\text{or}\quad
   Q_i,
   \]
   where `Q_i` is a co-root;
5. the complete ordered four-root boundary and route orientation of the failed local move.

No second defect is present at first failure.

The resulting marked object is called a **one-token state**.

---

## 4. Same-order token transitions

A one-token state may be changed by bounded source-level normalisations that preserve target order and the complete exterior context.

### Hypothesis L — complete local token grammar

Every same-order token move is one of:

1. immediate zero-to-root triality resolution;
2. transport of one co-root token through a disjoint critical move;
3. one of finitely many labelled critical-overlap normalisations;
4. canonical resolution of a constant-pivot run;
5. production of a cap-compatible route or theta terminal;
6. production of an equal-face cancellation.

The token never branches into two independent defects.

All root and co-root labels used during persistent transport are nonzero, so the concrete source moves remain in the required connected bridgeless category. Zero is resolved before persistent transport.

---

## 5. Finite enriched token graph

For one fixed prefix

\[
C_0\to\cdots\to C_j
\]

and one fixed exterior context, let

\[
\mathcal T_j
\]

be the directed graph of all complete labelled one-token states reachable by the same-order moves of Hypothesis L.

A vertex records at least:

- token type and position;
- local source topology;
- all roots on the critical neighbourhood;
- the ordered exterior incidences;
- cap-route orientation;
- constant-pivot support transport;
- the current history position.

### Hypothesis S — finite full-state reachability

The graph `mathcal T_j` is finite.

No quotient is allowed to identify two states merely because they have the same coefficient token or the same collapsed pivot skeleton. States with different support holonomy, route data, or source incidence are distinct.

---

## 6. Reduction of a terminal-free recurrent class

Suppose a reachable strongly connected component of `mathcal T_j` has no exit to:

- rootification;
- a cap-compatible terminal;
- strict cancellation.

### Hypothesis P — forced-backbone reduction

Every such terminal-free recurrent component contains a nonbranching co-root token track. After:

1. resolving constant-pivot runs by their unique full-state root sections;
2. deleting immediate inverse backtracks without discarding support transport;
3. retaining every fixed rooted side attachment;

one obtains a simple Petersen pivot core of type

\[
C_5,
\quad C_6,
\quad C_8,
\quad\text{or}\quad C_9.
\]

The reduction is source-incidence preserving and does not replace the complete physical region by an abstract coefficient cycle.

---

## 7. Odd and even recurrence

### Hypothesis O — odd holonomy exclusion

For the simple odd cores

\[
C_5,
\qquad C_9,
\]

the transported crossed-resolution sheet is reversed. Since the cap fixes an oriented route sheet, such a core cannot return to the same complete labelled token state.

Thus no terminal-free strongly connected component can be supported on an odd core.

### Hypothesis E — even identity-return cancellation

Every even recurrent core has a source-level strict exit.

1. A primitive `C6`, with all constant-run carriers retained as fixed rooted branches, admits a relative root-valued `(0,2,2)` move to a canonical star.
2. The canonical star contains an equal-face dipole.
3. Cancelling that dipole lowers target order by two.
4. Every `C8` is reduced by two seam-compatible `C6` cells, preserving every shared root incidence and exterior attachment, and inherits the same strict exit.

No abstract longitudinal tube filling is used as a substitute for this source movie.

---

## 8. No nonterminal sink theorem

### Theorem 8.1 — no terminal-free sink SCC

Under Hypotheses L, S, P, O, and E, every reachable strongly connected component of `mathcal T_j` has an exit to at least one of:

1. rootification of the token;
2. a cap-compatible root terminal on a strict history prefix;
3. an equal-face cancellation lowering target order.

### Proof

Assume a reachable sink strongly connected component `X` has none of the three exits.

By Hypothesis L, zero cannot persist, so `X` contains only co-root token states. Hypothesis P reduces one recurrent token track in `X` to a simple Petersen core of length `5,6,8`, or `9`, with all complete labelled source data retained.

- Length `5` or `9` contradicts Hypothesis O: the oriented resolution sheet does not return.
- Length `6` or `8` contradicts Hypothesis E: the core has a strict cancellation exit.

Therefore no such `X` exists. ∎

### Corollary 8.2 — an exit is reachable

From every vertex of the finite graph `mathcal T_j`, a directed path reaches rootification, a cap-compatible terminal, or strict cancellation.

Indeed, otherwise the set of reachable vertices contains a sink SCC with no such exit.

---

## 9. Singular contextual confluence

### Theorem 9.1 — cover-independent terminal transport

Assume, for every target order below or equal to `N`, that:

1. regular forward histories are finite;
2. Hypotheses F, L, S, P, O, and E hold;
3. every route or direct-pairing outcome is converted to a cap-compatible root terminal;
4. every cancellation output is handled componentwise in strictly lower target order;
5. every move preserves the complete labelled exterior context required by the original cap.

Then every cap-compatible root state on the terminal object of every finite history

\[
C_0\to\cdots\to C_m,
\qquad N(C_0)\le N,
\]

transports to a cap-compatible root state on `C_0`.

### Proof

Use lexicographic induction on

\[
\bigl(N(C_0),m\bigr).
\]

#### Base cases

If `m=0`, there is nothing to transfer. The minimum target-order contexts are explicit bounded terminals.

#### Regular inverse success

If the final inverse move is root-valued, perform it. The remaining prefix has length `m-1`, so the induction hypothesis applies to

\[
\bigl(N(C_0),m-1\bigr).
\]

#### First failure

By Hypothesis F, the failure produces one labelled zero/co-root token at some strict prefix position `j<m`.

By Corollary 8.2, same-order normalisation reaches one of three exits.

1. **Rootification.**  
   The failed inverse step now succeeds root-valuedly. Continue on a strict history prefix, lowering the second induction coordinate.

2. **Cap-compatible terminal.**  
   The terminal lies on `C_j` with `j<m`. Apply the induction hypothesis to the strict prefix
   \[
   C_0\to\cdots\to C_j.
   \]

3. **Strict cancellation.**  
   The target order drops by two. Apply the outer induction hypothesis to the resulting lower-order cap context, independently of its new history length.

Every branch lowers the lexicographic pair. Hence terminal transport succeeds. ∎

---

## 10. Relation to Newman's lemma

Ordinary Newman's lemma says that a terminating locally confluent rewrite system is globally confluent.

The present theorem is not a direct application because:

1. the terminal root flow is arbitrary and need not descend from the original flow;
2. inverse moves can leave the root orbit and enter singular fibres;
3. the singular object carries route orientation and complete source incidence;
4. confluence is relative to one exterior cap context;
5. some critical cycles resolve only by lowering a second, outer order.

Theorem 9.1 is therefore a **singular relative Newman theorem with an outer induction parameter**.

Its abstract proof is finite-state and well founded. The mathematical content lies in proving the hypotheses for the root-triality system.

---

## 11. Concrete AffineCDC hypothesis map

### Forward termination

- equality potential:
  `EQUALITY_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- DDD potential:
  `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- removal of the generic bounded DDD residual:
  `DDD_BOUNDED_RESIDUAL_ELIMINATION_V1.md`.

These verify only that selected forward histories terminate. They need not appear as two global proof narratives.

### Hypothesis F

- `PACHNER_HISTORY_FIRST_FAILURE_ONE_EDGE_ATOM_V1.md`.

### Hypothesis L

- zero/equality and co-root/DDD triality;
- `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`;
- `FIRST_FAILURE_NORMALIZATION_AUTOMATIC_CATEGORY_SAFETY_V1.md`;
- `ROUTE_CHANGE_TERMINAL_CONTEXTUAL_TRANSFER_V1.md`;
- `DIRECT_PAIRING_BRIDGE_TO_THETA_ZERO_RESOLUTION_V1.md`.

### Hypothesis S and full-state safeguard

- finiteness of the fixed finite source/history state space;
- `CONSTANT_PIVOT_FULL_STATE_CONTEXTUAL_CONSUMPTION_V1.md`;
- `SIX_OUTPUT_FULL_STATE_CYCLE_CORRECTION_V1.md`.

The correction is essential: collapsed pivot data alone are not the state space.

### Hypothesis P

- `PTOLEMY_TRACK_FORCED_BACKBONE_SINK_ELIMINATION_V1.md`, only in its retained forced-backbone scope;
- `FORCED_BACKBONE_EVEN_CYCLE_SINK_SCOPE_CORRECTION_V1.md`;
- the repaired full-state consumer above.

The word `Ptolemy` is not needed in the master theorem statement. It records one construction of the critical-pair history complex.

### Hypothesis O

- `PETERSEN_RESOLUTION_PARITY_V1.md`;
- `CONSTANT_PIVOT_FULL_STATE_CONTEXTUAL_CONSUMPTION_V1.md`.

### Hypothesis E

- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `PETERSEN_C6_AUTOMATIC_CATEGORY_SAFETY_V1.md`;
- `PETERSEN_C8_TWO_C6_HISTORY_FILLING_REDUCTION_V1.md`.

### Outer induction and target order

- `CONTEXTUAL_TRANSFER_TARGET_ORDER_CORRECTION_V1.md`;
- `ROOT_SURGERY_AUTOMATIC_CATEGORY_SAFETY_V1.md`;
- componentwise smaller-graph induction in the repaired global theorem.

---

## 12. Architectural simplification obtained

If PDL verifies the hypothesis map, the main proof no longer needs separate global chapters titled:

- equality global transfer;
- DDD global transfer;
- global Ptolemy coherence;
- Petersen obstruction theory;
- abstract root tube filling.

Instead it needs:

1. two termination lemmas for the singular fibres;
2. one first-failure lemma;
3. one labelled critical-pair/token theorem;
4. one odd/even recurrence theorem;
5. Theorem 9.1 as the common contextual-return engine.

Ptolemy and Petersen remain indispensable local languages for verifying Items 3--4, but they cease to be independent proof architectures.

---

## 13. Possible further compression

Theorem 9.1 still assumes separate verification of the token cycle theorem. Two stronger future routes remain open.

### Direct one-defect augmentation

Prove directly that a cyclically five-edge-connected cubic graph cannot support a defect-minimal `E_5` flow with one zero/co-root edge. This would bypass the history graph entirely.

### Intrinsic singular complex

Construct one compact singular-triality complex in which equality and DDD are boundary strata and the `C6` star is an actual 2-cell. A standard cellular confluence theorem might then prove Hypotheses P, O, and E simultaneously.

Neither compression is currently established.

---

## 14. PDL theorem obligations

PDL should treat Theorem 9.1 as an abstract reusable lemma and reconstruct the concrete proof in the following order:

1. formalise the exact root contexts and target order;
2. prove regular inverse transfer and first-failure localisation;
3. define complete labelled one-token states;
4. prove the critical-overlap transition relation is exhaustive and nonbranching;
5. prove constant-pivot full-state retraction;
6. prove the forced-backbone cycle reduction without coefficient-only quotienting;
7. verify odd parity and the `C6/C8` source movies;
8. instantiate Theorem 9.1;
9. consume it inside the fixed-route cap theorem.

This is a much smaller and more logically transparent DAG than the discovery chronology.

---

## 15. Trust boundary

### Proved abstractly here

- the no-sink-SCC implication from the stated recurrence hypotheses;
- the lexicographic contextual-transport induction;
- the exact role of history length versus target order;
- the singular relative Newman formulation.

### Not proved anew here

- any concrete equality or DDD potential;
- first-failure localisation;
- exhaustive critical-overlap classification;
- full-state forced-backbone reduction;
- odd parity;
- the `C6/C8` source movies;
- the repaired full-channel theorem;
- the global five-CDC candidate.

Those are the concrete hypotheses to be reconstructed and audited.
