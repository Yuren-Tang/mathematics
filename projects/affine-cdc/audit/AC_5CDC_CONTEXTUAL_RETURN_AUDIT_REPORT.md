# AC-5CDC-AUDIT-RETURN-01 — independent contextual-return audit

**Role:** `AffineCDC — Independent 5-CDC Contextual-Return Auditor`  
**Owned branch:** `audit/affine-cdc-five-cdc-return-v1`  
**Exact branch base:** `1f57422e0e415d8902d56eb294183815c0a0b640`  
**Fixed candidate:** `proof-development/affine-cdc-rigour-v1@1f57422e0e415d8902d56eb294183815c0a0b640`  
**Frozen Research Lead source:** `research/affine-cdc-five-cdc-v1@71a10f9ba86c1d2b8b7885e78fa9baa303c77818`  
**Audit guide:** `2679f098e6c596083d671a67d2630d5c58c6280f`, used only as a falsification checklist.

## 1. Final classification

\[
\boxed{\text{MATERIAL RETURN/WELL-FOUNDEDNESS GAP — NO 5-CDC ACCEPTANCE}}
\]

No counterexample to the 5-CDC statement was found.  The return is a proof-gap
classification: the candidate has not established the parent-level terminal
reachability needed before defining `d_N`.

| Unit | Classification | Controlling reason |
|---|---|---|
| G — R2.6 cellwise erasure | `ACCEPT WITH EXPLICIT REPAIR` | The unmarked seam, run and periodic arguments check out.  A mark on the active central diagonal is not fixed boundary data and needs explicit active-diagonal transport. |
| H — witnessed recursion / child fidelity | `BLOCKED-PROOF` | The `Q_N/P_N` order and inherited child are sound, but generic child separator/category exits are asserted to lift to parent exits without the required four-terminal partition proof. |
| I — genealogy / legal consumer alphabet | `ACCEPT` | Ordered-dart lineage, raw central-mark consumption, suspended ancestor marks, call-local marks, and switch--pop endpoint normalization are mutually consistent for the chosen proof execution. |
| J — target boundary / resolved relation / rank | `BLOCKED-PROOF` | The active-obligation segmentation, macro totality, no-reset invariant and re-splicing needed to exclude terminal-free SCCs are not proved.  Hence terminal reachability and `d_N` do not follow. |

## 2. Audit method

The audit did not use RL/PDL completion labels, ordinary CDC Lean, Curator status,
or an unreproduced finite certificate as proof authority.  It:

1. reconstructed the Petersen-root algebra by hand;
2. independently enumerated all 120 ordered nonbacktracking pivot cells;
3. traced ordered darts, active diagonals, raw and suspended marks through the
   frozen local source movies;
4. separated child graph-category facts from child-to-parent terminal fidelity;
5. tested the resolved-call SCC proof against the smallest finite abstract
   relations satisfying its stated hypotheses.

Companion deliverables:

- `AC_5CDC_AUDIT_RETURN_SEAM_INTERFACE_LEDGER.md`;
- `AC_5CDC_AUDIT_RETURN_RECURRENCE_RANK.md`;
- `AC_5CDC_AUDIT_RETURN_SMALLEST_COUNTEREXAMPLE_LEDGER.md`;
- `AC_5CDC_AUDIT_RETURN_PIVOT_ENUM.py`.

## 3. Unit G — cellwise seam and periodic cylinder

### Independently accepted

For a genuine nonbacktracking path `x-s-t-y`, one global support permutation
puts `s=12`, `t=34`.  Then `x` is `35` or `45`, and `y` is `15` or `25`.
The side roots `z=x+t` and `w=s+y` are the complementary choices in those two
pairs.  They are distinct and meet exactly in support `5`.  The audit enumerator
confirms all `120/120` ordered cases.

The four-port word `(z,z,w,w)` has one zero pairing and two root pairings, both
with central root `z+w`.  The root pairings differ by one legal relative NNI on
the same four ordered exterior darts.  Identity subdivision separates
consecutive seam collars without adding a mathematical source move.  The
nonpivot section of a constant-pivot run matches the two opposite resolutions
at a pivot-change seam.  Closed no-change runs, normalized open tracks,
one-unresolved-endpoint scope, and the periodic-cylinder crosscut are valid.

### Defect G-MARK-1

**File/theorem:**
`AC_PD_5CDC_R2_6_CELLWISE_TRACK_ERASURE.md`, Theorem 4.1 and the identity-gluing
use in Theorem 8.1.

**Smallest configuration:** one genuine pivot-change cell, for example

`35 -> 12 -> 34 -> 15`,

with `z=45`, `w=25`, and one surviving ancestor mark on the active central
atom/diagonal.

**Defect type:** source-topological / genealogy interface.

**Defect:** the proof says all listed marks lie on the fixed boundary and are
therefore unchanged.  A suspended central mark may lie on the active diagonal,
not on an exterior boundary dart.  It must be transported to the new diagonal
by the labelled active-NNI lineage and then matched to the adjacent run-strip
endpoint.

**Repair:** add the passive/active mark case split stated in the seam ledger.
The required local lineage already exists in the HW2 source movies.  This repair
does not change the unmarked R2.6 statement or its downstream topology.

**G classification:** `ACCEPT WITH EXPLICIT REPAIR`.

## 4. Unit H — witnessed `Q_N/P_N` recursion and child fidelity

### Independently accepted

The within-level order is noncircular:

- `Q_N` consumes lower `Q_n` and fixed-order local theorems;
- `P_N` consumes lower `P_n` and the already proved same-level `Q_N`.

Equal-face cancellation supplies the inherited child root flow.  The connected
child is cubic, loopless and bridgeless; disconnected output exposes a cyclic
two-edge cut rather than a synchronized multi-component call.  No unrelated
terminal recolouring is needed.

### Defect H-CROSS-1

**File/theorem:**
`AC_PD_5CDC_R2_7_CHILD_CONTEXT_FIDELITY.md`, Theorem 5.1.

**Defect type:** contextual definition/interface.

The file should explicitly construct both the smaller target cap closure and the
smaller inherited selected cross closure from the cancelled four-pole.  Merely
saying that the same cap shore and matching convention remain does not literally
instantiate the quantified input of `Q_{N-2}`.  This is a local repair: name
`P'`, `G'_i=P' union cap_i`, and `G'_j=P' union E_j`, and state that the
cancellation support is disjoint from the fixed outer closure collar.

### Defect H-SEP-1

**File/section:**
`AC_PD_5CDC_R2_7_CHILD_CONTEXT_FIDELITY.md`, Section 4.6 and Theorem 5.1's
accepted child exits.

**Smallest configuration:** one stored equal-face dipole and a child separator
using one or both of the two new reconnection edges.

**Defect type:** source-topological / contextual return.

**Defect:** restoring the dipole may change or remove the child cut.  The text
asserts that the result is the same cut order or an accepted bounded low-port
configuration, but gives no partition census of the four cancellation terminals
and no exact downstream bound.  Thus a child branch may terminate without a
proved parent exit.

**Downstream impact:** a purported finite `Q_{N-2}` witness can end before a
valid parent endpoint exists.  That invalidates the resolved-call macro endpoint
used in J.

**H classification:** `BLOCKED-PROOF`.

## 5. Unit I — labelled genealogy and legal consumer alphabet

The primitive labels are correctly taken to be ordered darts.  Passive marks
are fixed pointwise; an active diagonal uses a one-to-one mobile-envelope map.
Raw central cancellation truly deletes its central darts.  In a successful
paired bubble, a still-live ancestor obligation is instead carried on the
central dart pair of each predecessor-order raw insertion as a suspended
boundary mark.  Call-local marks disappear with the eliminated frame.

The distinction is coherent and does not resurrect an edge in the lower graph.
The frozen six-leaf and five-leaf movies provide literal endpoint tuples for
concatenation.  The locked Morse descent uses only root NNIs and equal-face
cancellations, so support switches may be confined to root/terminal histories or
switch--pop endpoint collars.  No raw singular support-switch atom is consumed
as an interior Ptolemy cell.

The sole required cross-file amendment is G-MARK-1: R2.6 must invoke this active
lineage instead of calling every mark fixed boundary data.

**I classification:** `ACCEPT`.

## 6. Unit J — target-parent preservation and no-sink rank

### What is established

The candidate correctly identifies the required distinction between a selected
ordinary parent topology and an arbitrary root-valued topology.  Subject to
G-MARK-1, Theorem 5.1 is credible as a **relative normalization lemma** for an
already constructed comparison with exact outer obligation `T -> p(T)`.
The original-prefix coordinate also decreases immediately and is not restored by
inner normalization.

### Defect J-TOTAL-1 — no proved total macro scheduler

**File/theorem:**
`AC_PD_5CDC_R2_7_RESOLVED_CALL_CONTEXTUAL_TRANSFER.md`, Sections 6--7,
Theorem 6.1.

A reachable singleton nonterminal state with no outgoing macro is a sink SCC but
has no positive directed cycle.  The proof begins by choosing a cycle without
first proving that every reachable nonterminal parent state has an outgoing
chosen macro.

### Defect J-SEG-1 — target-parent segmentation and re-splicing

**File/theorem:** same, Theorem 6.1.

After a resolved cycle is expanded and innermost calls are compressed, the proof
says to apply Theorem 5.1 obligation by obligation.  It does not prove that:

1. the compressed history retains a literal ordered segmentation into active
   obligations;
2. replacing one segment by a history ending on `p(T)` leaves exactly the initial
   complete state required by the next segment;
3. every mark, route, cap and phase coordinate agrees at that new seam.

HW2 proves seams inside an innermost bubble, not this global parent-success
re-splicing.

### Defect J-RESET-1 — strict `d_top` descent is not an invariant of `M_N`

**File/theorem:** same, Theorem 6.1, especially the inference that only parent
successes remain in a terminal-free sink SCC.

Sinkness excludes outgoing exits; it does not prove that direct normalization or
returned-call macros preserve `d_top`, nor that they cannot restore a larger
ordinary topology.  The smallest abstract countermodel has two nonterminal
states `x,y` with

- `d_top(x)=2`, `d_top(y)=1`;
- `x -> y` a parent success;
- `y -> x` a finite returned reset macro.

`{x,y}` is a terminal-free sink SCC under the currently stated invariants.
This is a countermodel to the no-sink inference, not a graph counterexample to
5-CDC.

### Defect J-SAT-1 — saturation is declarative

The sentence defining saturation includes any endpoint pair supplied by a
boundary-equivalent theorem, but does not give an exhaustive transition schema
or prove closure after compression and replacement.  Finiteness of endpoints
does not establish compositional saturation.

### Consequence

Theorem 6.1 has not proved that every reachable state reaches a terminal.
Therefore `d_N(x)=dist_{M_N}(x,X_N)` cannot yet be used as a finite rank, and the
lexicographic `(N,d_N)` induction remains unavailable.

A sufficient repair is the obligation-stratified resolved-relation theorem
stated in `AC_5CDC_AUDIT_RETURN_RECURRENCE_RANK.md`: totality, exact active
obligation, detour preservation, call-compression segmentation, no reset, and
strict parent success must be proved together.

**Defect type:** well-foundedness / contextual composition.

**Downstream impact:** R2.7, `Q_N` termination, contextual inverse transfer, cap
restoration and the claimed five-CDC theorem are not established.

**J classification:** `BLOCKED-PROOF`.

## 7. Required disposition

The candidate must not pass to full-proof synthesis or Curator intake on the
basis of this audit.  A repair round must at least supply:

1. G-MARK-1 marked seam transport;
2. H-CROSS-1 literal child `Q` instance;
3. H-SEP-1 child-separator-to-parent census;
4. one obligation-stratified, source-level no-sink theorem closing
   J-TOTAL-1/J-SEG-1/J-RESET-1/J-SAT-1.

Only a new fixed candidate containing those repairs should be re-audited.  No
Lean, manuscript, release or publication status follows from this return.
