# AC-PD-5CDC R2.7 — full-labelled genealogy and seam gluing

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Programme:** compressed five-support proof, global-return unit `R2.7`  
**Classification:** `COMPLETE-DRAFT / HW2 CLOSED / SUCCESSFUL BUBBLES CARRY SUSPENDED CENTRAL MARKS`.

This dossier closes the full-labelled genealogy interface for witnessed and
nested bubble compression.

---

## 1. Primitive labels

The primitive source labels are ordered **dart incidences**, not indivisible
edge names.

A marked edge consists of an ordered pair of endpoint darts.  A two-edge weld
boundary consists of four ordered darts grouped into two pairs.  The complete
context also records:

- the labelled outer semiedges;
- cap shore and distinguished cap block;
- current root assignment;
- derived support components and side roots;
- route sheet and orientation bit;
- bounded/separator flags.

At every state, an ordinary edge is the pairing of two current darts.  This
makes split, reconnection and active-diagonal transport literal operations on a
finite labelled dart universe.

---

## 2. Generator genealogy

### 2.1 Support-pair switch

A support switch changes only coefficients on a fixed even edge set.  It does
not change the dart pairing.  Every marked dart and every outer incidence is
therefore fixed pointwise.

### 2.2 Root `2--2` NNI

The four exterior darts are fixed.  If a marked edge is not the active central
edge, its darts persist unchanged.  If it is active, its lineage is transported
to the new diagonal: the old two central darts are replaced by the unique new
central dart pair in the displayed relative NNI movie.  This is a one-to-one
lineage map, not a duplication.

All active-diagonal source movies used in bubble lifting have the same labelled
outer darts at both ends.  Consecutive moves therefore compose their lineage
maps literally.

### 2.3 External equal-face cancellation

For an equal-face pair with external classes `p_L,p_R,q_L,q_R`, cancellation
pairs

\[
p_L\sim p_R,
\qquad
q_L\sim q_R.
\]

Every marked external dart continues uniquely onto the corresponding output
edge.  Reverse insertion splits the output edge and restores the two ordered
endpoint darts.  No external mark branches.

---

## 3. The central-mark distinction

If a marked edge is the central edge of an **unpaired raw cancellation**, its
two darts are deleted and there is no descendant edge in the lower graph.  This
is the mark-consuming Class IV event of the local overlap theorem.

It must not be described as pointwise lower-order genealogy.

There are two global dispositions.

### 3.1 Child exits

If the lower frame exits through route, bounded, separator or category data,
the parent branch terminates.  No pop and no restoration of the consumed mark
is required.

### 3.2 Successful paired bubble

Suppose the cancellation is paired with a successful returned insertion and
the complete push/child/pop interval is replaced by the predecessor-order raw
insertion strip.

At every child state, raw insertion restores the two parent vertex slots and
one central dart pair.  Mark this central pair as a **suspended boundary mark**.
It is not asserted to exist in the lower graph.  It is boundary data of the
fixed-order replacement strip.

- a child support switch changes its central coefficient by the parity formula
  but leaves the suspended darts fixed;
- a child root NNI disjoint from the interface fixes them;
- an active-diagonal lift transports them through the explicit five-/six-/three
  move lineage map;
- the equality/good-disjoint borrowing movie transports the mark through the
  labelled five-leaf path to the central edge of the root-valued alternative
  insertion;
- the missing-index movie transports it to the unique normalized co-root edge
  and its two crossed resolutions.

Thus a successful bubble has a marked fixed-order replacement even when the
raw lower execution temporarily deleted the ancestor edge.

This does not contradict mark consumption in the lower graph: the statement is
existence of a boundary-equivalent marked replacement history, not pointwise
ancestry through the deleted child state.

---

## 4. Exact seam equality

For a witnessed child generator step, the local lift begins at

\[
I(H_i,\lambda_i;e_i,f_i)
\]

and ends exactly at

\[
I(H_{i+1},\lambda_{i+1};e_{i+1},f_{i+1}).
\]

The complete endpoint tuple contains:

- the same labelled topology and dart pairing;
- the same root assignment;
- the same ordinary and suspended mark darts;
- the same cap shore/block;
- the same route sheet and support/side data.

Hence the terminal tuple of one local lift is literally the initial tuple of
the next.  No support permutation, source automorphism or genealogy
isomorphism is inserted at a seam.

### Theorem 4.1 — local-lift concatenation

All root-NNI and support-switch lifts concatenate as paths in one common
complete labelled predecessor-order state space.

---

## 5. Cap, route and support data

The indexed supports are derived from the current root assignment:

\[
F_i=\{e:i\in\lambda(e)\}.
\]

A local lift need not leave the current route unchanged.  Instead it reproduces
exactly the route/support change of the child generator and adds the raw
insertion data.  At each state:

- the outer semiedge order is fixed;
- the cap block remains a partition of those fixed semiedges;
- side roots are read from the current labelled incident edges;
- the route sheet/orientation is transported by the declared local movie;
- any route/profile change is exposed immediately as an accepted exit.

Therefore no hidden route genealogy is needed beyond the current complete
state and the finite local lineage map.

---

## 6. Innermost replacement gluing

Let an innermost successful frame occupy one interval of a larger labelled
execution.

The raw-insertion compression:

1. begins at the exact complete parent state immediately before the push;
2. ends at the exact complete returned parent state immediately after the pop,
   including any transported or normalized atom;
3. fixes every outer dart not internal to the replaced interval;
4. carries every passive ancestor mark pointwise;
5. carries a central consumed ancestor mark as a suspended boundary mark;
6. reproduces the current cap/route/support tuple at both ends.

Thus the interval can be excised and its replacement glued by the identity on
its two complete boundary collars.

### Theorem 6.1 — full-labelled innermost gluing

Every successful innermost bubble replacement preserves all data required by
its surrounding execution.  It removes one paired frame without creating,
duplicating or losing a live boundary obligation.

---

## 7. Nested induction

Choose innermost paired frames successively.

- Passive ancestor marks remain ordinary labelled darts.
- A central ancestor mark is suspended through the compressed strip.
- Child-only marks disappear with the removed child interval.
- The endpoint complete state determines which marks remain active in the
  parent continuation.

Since every replacement is identity-glued on complete collars, later
compressions see exactly the same surrounding labelled data as before.
Induction on the finite number of paired frames therefore preserves full
ancestry/cap/route coherence.

### Corollary 7.1

The fixed-order flattened history supplied by witnessed nested bubble
compression is a history in the complete labelled contextual state space, not
merely an unlabelled topology path.

Hence:

\[
\boxed{\texttt{AC-PD-5CDC-HW2 CLOSED}.}
\]

---

## 8. Remaining interface

Only `HW3` remains on the variable-order compression surface:

> Does the controlling fixed-order closed/open/periodic singular-track theory
> accept every cell produced by the flattened history, especially lifted
> support-switch even corrections and bounded one-atom active-diagonal movies?

The present theorem does not enlarge the fixed-order consumer alphabet by
assertion.

---

## 9. Trust boundary

### Closed here

- ordered-dart genealogy for every generator;
- pointwise external cancellation/insertion genealogy;
- distinction between raw central mark consumption and successful-bubble
  suspended marks;
- one-to-one active-diagonal transport;
- literal complete-state seam equality;
- cap/route/support transport;
- full-labelled innermost replacement gluing;
- nested genealogy induction;
- `HW2`.

### Not closed here

- `HW3` fixed-order consumer compatibility;
- independent reconstruction of the fixed-order singular-track theorems;
- R2.7, cap restoration or universal five-support closure;
- independent audit, Lean verification, curation, manuscript integration,
  release, arXiv, DOI, peer review or publication.
