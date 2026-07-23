# A call-free child return episode lifts to one fixed parent-order root/token history

## Research Lead innermost-episode theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `WELD_ACTIVE_DIAGONAL_SIX_LEAF_LIFT_V1.md`;
- `WELD_SUPPORT_SWITCH_SOURCE_POP_V1.md`;
- `WELD_RELATION_FIRST_EXIT_V1.md`;
- `WELD_MARK_EQUAL_FACE_OVERLAP_V1.md`;
- first-failure one-edge localisation and critical-overlap normalization;
- the finite full-labelled one-token transport grammar.

**Status:** exact base theorem for variable-order episode compression. Let a parent equal-face cancellation create a lower-order child. Suppose the finite child return history contains no further genuine `2--0` cancellation. Then the complete child episode, including inverse return through the parent weld, admits a predecessor-order realisation using only root-valued moves and at most one normalized zero/co-root atom. If the weld relation remains in `B`, the lift is fully root-valued. At the first `B -> A/C` exit, one ordinary atom is created after the failing child step has been crossed; the remaining finite child prefix lifts by the established one-token overlap grammar. No lower-order state remains in the lifted history.

This is the innermost induction step needed to eliminate order-changing bubbles from a finite repeated-state episode.

---

## 1. One call-free child history

Let a parent-order equal-face cancellation have output two ordered reconnecting edges

\[
e_p,e_q
\]

with current roots

\[
p,q\in R_5,
\qquad
(p,q)\in B.
\]

The lower-order child return history is a finite sequence

\[
H_0\longrightarrow H_1\longrightarrow\cdots\longrightarrow H_m
\]

whose steps are restricted to:

1. root-valued `2--2` Pachner flips;
2. support-pair component switches;
3. identity/subdivision moves and bounded local normalizations which do not change order;
4. route/profile or bounded/separator exits.

There is no genuine `2--0` cancellation inside the episode.

The four ordered weld incidences are transported through the history by the established incidence/envelope rules.

At `H_0`, inverse insertion is the original parent expansion. At `H_m`, the child terminal provides the current roots on the transported output pair.

---

## 2. Stepwise lift while `B` is preserved

Assume the transported pair is in `B` before and after one child step.

### Disjoint or exterior `2--2` step

The parent inverse insertion support and the child flip support commute strictly, or the marked incidence is a fixed exterior branch. Inflate the child step by the unchanged equal-face pair. This gives one predecessor-order root-valued square/relative flip.

### Active-diagonal `2--2` step

If one reconnecting edge is the active child diagonal, pointwise edge lineage fails. Apply `WELD_ACTIVE_DIAGONAL_SIX_LEAF_LIFT_V1.md`.

The before/after parent expansions have one common ordered six-port boundary and are connected by at most six predecessor-order root NNIs.

### Support-pair component switch

Apply `WELD_SUPPORT_SWITCH_SOURCE_POP_V1.md`. If the switched output pair remains in `B`, the lower component switch lifts to a genuine expanded root-valued component switch. Component merger or splitting at the inserted pair causes no ambiguity.

### Lemma 2.1 — root lift of a `B`-preserving prefix

Every finite initial child segment along which the weld pair remains in `B` has a fully root-valued predecessor-order lift preserving:

- all ordered exterior incidences;
- cap and route data;
- all nonweld side-root outputs;
- the current mobile weld envelope/sheet.

### Proof

Concatenate the applicable local lift for each child step. Consecutive lifts agree on the complete expanded endpoint state, so the histories glue. ∎

---

## 3. First exit

Suppose the pair first leaves `B` at the child transition

\[
H_{j-1}\longrightarrow H_j.
\]

The prefix through `H_(j-1)` lifts root-valuedly by Lemma 2.1.

There are two source mechanisms.

### Active child diagonal

The six-leaf theorem gives a bounded predecessor-order path whose endpoint has exactly one missing-index co-root edge.

### One-sided support switch

The support-switch pop theorem gives a predecessor-order expansion whose only non-root edge is the central value

\[
p'+q'=0
\quad\text{or}\quad
Q_i.
\]

In both cases:

- the child transition has already been completed;
- every other edge is a root;
- the parent source topology has been restored/expanded;
- the residual atom lies after Step `j`, with the strict child prefix
  \[
  H_0\to\cdots\to H_j
  \]
  already consumed from the opposite direction.

### Theorem 3.1 — one parent-order first-exit atom

The first failure of a call-free child return creates exactly one ordinary parent-order zero/co-root atom and no new defect alphabet.

---

## 4. Lifting the remaining finite prefix with one atom

After the first exit, retain the complete parent-order state:

- one zero/co-root atom;
- both crossed resolutions when the atom is a co-root;
- ordered exterior and weld incidences;
- all cap/route/side data.

Traverse the remaining finite child prefix one step at a time.

### Root `2--2` overlap

Use the first-failure critical-overlap table:

- disjoint steps commute;
- exterior contact fixes the atom boundary;
- a good overlap relocates one atom;
- the unique bad overlap creates only a transient two-co-root tree and immediately normalizes back to at most one atom.

When the child step uses the former active weld diagonal, use the same six-port envelope as the root lift; the one-token local table is supported on that bounded six-leaf region.

### Support-switch overlap

Use the full-labelled current-flow/defect-exchange table. A prescribed component switch either:

- rootifies the active outer relation;
- transports the unique atom;
- exchanges it with the weld boundary;
- gives an accepted route/profile/bounded/separator exit.

It never creates two persistent atoms.

### Lemma 4.1 — finite one-token prefix lift

Every remaining finite call-free child prefix has a predecessor-order lift with at most one normalized atom at every stage, or reaches an accepted exit.

### Proof

Induct on the finite number of remaining child steps. The complete local transition alphabet above is exhaustive and closes after each step back to zero or one atom. ∎

No termination theorem is needed for this lemma: the prefix length is fixed and finite.

---

## 5. Complete innermost episode lift

### Theorem 5.1 — call-free child episode compression

A finite child solve/return episode containing no nested genuine cancellation can be replaced, relative to its complete parent boundary, by one finite predecessor-order history with:

1. only root-valued states if the weld relation remains in `B`;
2. at most one normalized zero/co-root atom if a first `B -> A/C` exit occurs;
3. the same final complete parent root/atom state as the original child pop;
4. no lower-order history vertex;
5. no hidden mark duplication or arbitrary flow reselection.

The replacement uses only:

- strict relative commutation;
- the six-leaf active-diagonal lift;
- root support-switch lifting;
- the one-token critical-overlap/current-flow grammar.

---

## 6. Central-mark exclusion in a repeated complete state

A call-free episode has no inner `2--0` move. For the outer cancellation which opened it, all four output incidences are external marks and survive throughout the call-free history.

More generally, in a finite complete-state recurrence, a cancellation which consumes a central active mark strictly lowers the mark count by `WELD_CENTRAL_MARK_CANCELLATION_POP_V1.md` and no later inverse move automatically restores that mark.

Therefore a repeated complete state with the same ordered active marks cannot contain a net central-mark-consuming call.

This fact will separate strict mark progress from recurrence compression in the next theorem.

---

## 7. Consequence for source-level continuation fidelity

The old variable-order gap asked whether

\[
\text{cancel}
\to
\text{call-free lower history}
\to
\text{return}
\]

could be regarded as one fixed-order parent episode.

The answer is now yes:

\[
\boxed{
\text{call-free lower episode}
\Longrightarrow
\text{finite parent root/one-token history}.
}
\]

This is stronger than coefficient mark transport and weaker than arbitrary marked-weld return. It is exactly the innermost bubble needed for induction on the number of nested calls.

---

## 8. Assurance boundary

### Exact here

- root lift of every `B`-preserving call-free child step;
- bounded source lift at an active diagonal;
- support-switch source lift/pop;
- one parent-order atom at first exit;
- finite transport of that atom through the remaining call-free prefix;
- elimination of every lower-order vertex from an innermost episode;
- incompatibility of central-mark consumption with recurrence of the same complete marked state.

### Not yet claimed

- compression of an episode containing nested cancellations;
- corrected stack completion;
- unconditional R2.7 or cap restoration;
- PDL reconstruction or independent audit;
- Lean verification, manuscript integration, curation, release or publication.
