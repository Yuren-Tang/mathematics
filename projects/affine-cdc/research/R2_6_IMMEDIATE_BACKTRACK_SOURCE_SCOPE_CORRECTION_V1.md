# R2.6 immediate-backtrack source scope correction

## Research Lead correction and quarantine v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `536f931b190255f199c2e21269f6cbca9e618d11`

**Corrects:**

- `CELLWISE_ROOT_SEAM_AND_CONSTANT_RUN_TRACK_ERASURE_V1.md` insofar as it treats every immediate pivot backtrack as already source-faithfully deletable or as two ordinary nonbacktracking seam sites;
- Theorem 4.1 and Theorem 6.1 of `MARKED_CLOSED_TRACK_DIRECT_ROOT_SEAM_V1.md` insofar as they import an unspecified `source-faithful Type-T backtrack normalization`;
- Step 3.3 and the downstream conclusions of `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md` insofar as coefficient-side `abba` reduction is promoted to complete source-history erasure;
- `PTOLEMY_TRACK_FORCED_BACKBONE_SINK_ELIMINATION_V1.md` insofar as a Petersen-projected immediate backtrack is asserted to be a cancellable history digon without proving equality of the two physical source moves;
- `V7_R2_5_CORE_CLASSIFICATION_SCOPE_CORRECTION_V1.md` insofar as it declared arbitrary immediate backtracks consumed;
- v7/v7.1 and the v5 proof DAG insofar as general fixed-order one-atom termination imports the uncorrected cellwise theorem.

**Status after correction:**

\[
\boxed{
\text{R2.6 BACKTRACK-REDUCED TRACK ERASURE CLOSED AT RL AUTHORIAL LEVEL}}
\]

\[
\boxed{
\text{GENERAL R2.6 HAS ONE OPEN LOCAL-COMPOSITION INTERFACE:}
\quad
\text{NONLITERAL TYPE-T BACKTRACK BIGON}.}
\]

Consequently:

\[
\boxed{
\text{R2.7-v7.1 IS CONDITIONAL ON THE BACKTRACK-BIGON THEOREM}.}
\]

This correction does not produce a counterexample to the theorem. It removes an unsupported source-level implication.

---

## 1. Three different notions previously conflated

Let the Petersen pivot skeleton contain

\[
s\longrightarrow t\longrightarrow s,
\qquad s\perp t.
\]

The following statements are distinct.

### 1.1 Coefficient backtrack

The two switch states are the same Petersen edge

\[
F=\{s,t\}
\]

with opposite orientations, and the forced shore-resolution word is

\[
\boxed{t,s,s,t}.
\]

This is exact.

### 1.2 Literal history involution digon

Two consecutive contextual transitions are the same labelled local `2--2` source move followed immediately by its inverse, with identical complete endpoint state.

This is source-faithfully deletable by root involutivity.

### 1.3 Embedded Type-T corridor

Two coefficient transitions use the same Petersen edge in opposite directions but occur at different physical source locations, possibly separated by an arbitrarily long constant-pivot run with side-root attachments.

This need not be a literal involution digon. Its source-history deletion is not implied by the coefficient word.

The previous cellwise dossiers moved from 1.1 to 1.2 without excluding 1.3.

---

## 2. What the existing backtrack sources actually prove

### `PETERSEN_BACKTRACK_TYPE_T_REDUCTION_V1.md`

This file proves:

- the exact `abba` word;
- formal free reduction of the Petersen path;
- coefficient-side Type-T/Type-H normal form.

It explicitly states that formal cancellation does **not** assert source-subgraph contraction and lists as open:

- source-graph contraction of an `abba` unit;
- preservation of side-root semantics;
- four-pole transfer.

### `FOUR_ROOT_INTERFACE_TYPE_T_SQUARE_V1.md`

This file proves:

- the disjoint doubled-root boundary `a,b,b,a`;
- an explicit root-valued canonical square completion;
- fixed-boundary support-response congruence.

It explicitly leaves open:

- enclosure of a physical Type-T backtrack with all side attachments as a genuine four-port region;
- universal state-set inclusion;
- integration with the return-cell table.

### `TYPE_T_KERNEL_SQUARE_ENVELOPE_V1.md`

This file identifies the finite square-envelope states but again leaves open physical enclosure and source replacement.

### `FORCED_DDD_BACKBONE_BINARY_TRANSPORT_V1.md`

This file says explicitly that graph-safe localisation/removal of an embedded Type-T unit remains open.

Therefore none of these files is the unspecified `source-faithful Type-T backtrack normalization` imported by the later seam dossiers.

---

## 3. Why two ordinary pivot-change seams do not apply

The ordinary local pivot-change seam uses four consecutive pivots

\[
x\to s\to t\to y
\]

with

\[
x\ne t,
\qquad
s\ne y.
\]

Its side roots are

\[
z=x+t,
\qquad
w=s+y,
\]

and the proof needs `z,w` to be distinct intersecting roots.

For an immediate backtrack `s\to t\to s`:

- at the first switch the next pivot satisfies `y=s`, so `w=s+s=0`;
- at the second switch the preceding pivot satisfies `x=t`, so `z=t+t=0`.

Thus neither occurrence lies in the nonbacktracking `(0,2,2)` local theorem.

Identity subdivision separates source cells but does not change these coefficient equalities. Hence it does not manufacture two legal ordinary seams.

---

## 4. Exact retained local theorem

### Theorem 4.1 — literal involution digon erasure

Suppose two consecutive singular-history transitions are literally one labelled local root/Ptolemy move and its inverse, including:

- the same source dart slots;
- the same local support vertices;
- the same root labels;
- the same atom edge and active position;
- the same crossed-resolution sheet;
- the same side-root occurrences and rooted attachments;
- the same cap block and route;
- the same surviving mark data.

Then root involutivity gives a source-faithful identity digon. Delete the two cells and identify their equal complete endpoint states.

This deletion preserves all exterior data literally.

### Corollary 4.2

Any immediate pivot backtrack whose two history edges are certified to be a literal inverse pair is harmless.

### Nonconverse

The coefficient condition `s\to t\to s` alone does not certify the hypotheses of Theorem 4.1.

---

## 5. Corrected cellwise theorem

### Theorem 5.1 — backtrack-reduced cellwise track erasure

Let one finite normalized nonbranching full-state co-root track satisfy:

1. every coefficient immediate backtrack is either absent or equipped with a literal involution-digon certificate;
2. after deleting those certified digons, every remaining pivot change is nonbacktracking;
3. constant-pivot runs retain complete boundary data;
4. short sides are normalized or accepted as in the endpoint theorem.

Then:

1. delete the certified literal digons;
2. place a local `(0,2,2)` root seam at every remaining pivot change;
3. separate adjacent collars by identity subdivision;
4. replace every residual constant-pivot interval by the identity product of its unique nonpivot complete history;
5. glue on literal complete endpoint states;
6. apply the closed/open/periodic endpoint constructions.

The track has a root cylinder/rectangle replacement in the stated endpoint class.

This retains the complete cellwise theorem on the backtrack-reduced domain.

---

## 6. Exact open theorem

### Target 6.1 — nonliteral Type-T history-bigon replacement

Let a normalized full-state co-root track contain a maximal corridor whose pivot skeleton is

\[
s\longrightarrow t\longrightarrow s,
\]

where the two switch transitions are not certified literal inverses. The middle constant-`t` run may have arbitrary finite length and rooted side attachments.

Construct one of:

1. a root-valued relative history rectangle replacing the entire corridor and fixing its complete boundary;
2. a route/profile escape;
3. a two-, three-, or four-cut or bounded low-port terminal;
4. a strictly shorter full-state Type-T corridor;
5. a proof that the fixed-order scheduler can be chosen so that every coefficient backtrack is literal.

A valid proof must preserve or explicitly consume:

- all source dart incidences;
- every side-root occurrence and rooted attachment;
- support transport;
- both crossed resolutions;
- cap block and route;
- all required marks.

Coefficient free reduction, fixed-boundary support-response congruence, or an abstract square completion alone is insufficient.

---

## 7. Consequence for v7

The first-cancellation ordinary-induction simplification remains valid through:

- the one-cross reduction;
- monotone pure root-NNI prefix;
- parallel-target tests;
- ordinary lower solution of the first child target cap closure;
- arbitrary-flow single pop;
- target-topology scope correction;
- fixed-order zero removal and one-atom nonbranching.

The only unclosed v7 dependency is now:

\[
\boxed{
\text{general fixed-order one-atom return across a nonliteral Type-T backtrack corridor}.}
\]

No variable-order recursion is reintroduced. The gap is same-order and local-compositional.

---

## 8. PDL retarget

Before declaring v7 complete-draft, PDL must either:

1. prove Target 6.1; or
2. prove that the exact v7 scheduler never produces a nonliteral coefficient backtrack; or
3. return one explicit complete-state counterexample to either proposed statement.

PDL should not use:

- formal Petersen free reduction;
- the coefficient `abba` word alone;
- the canonical Type-T square without enclosure;
- the sentence `the two relocations undo each other` without literal source-move equality.

---

## 9. Correct classification

### Retained authorial results

- R1 valid-cross theorem;
- first-cancellation ordinary-induction reduction;
- target-synchronized monotone root-NNI prefix;
- strict smaller child target cap closure;
- arbitrary-flow single pop;
- target-topology normalization scope;
- fixed-order no-cancellation-reopening alphabet;
- one-atom nonbranching;
- constant-run strips;
- nonbacktracking pivot-change seams;
- backtrack-reduced closed/open/periodic track erasure;
- reverse dependency acyclicity apart from the named local interface.

### Open

- nonliteral Type-T history-bigon replacement or scheduler avoidance.

### Current authorial classification

\[
\boxed{
\text{R2.6 BACKTRACK-REDUCED CLOSED}
/
\text{R2.6 GENERAL TYPE-T BIGON OPEN}.}
\]

\[
\boxed{
\text{R2.7-v7.1 CONDITIONAL AUTHORIAL CANDIDATE}
/
\text{PDL RECONSTRUCTION AND INDEPENDENT ASSURANCE REQUIRED}.}
\]

### Not claimed

- accepted cap restoration;
- established five-support/five-CDC theorem;
- Lean verification;
- Curator/canonical movement;
- manuscript, release, arXiv, DOI, peer review, or publication status.
