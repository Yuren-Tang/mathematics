# AC-PD-5CDC R2.7 — mutual induction supplies the missing history witness

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Programme:** compressed five-support proof, global-return unit `R2.7`  
**Classification:** `COMPLETE-DRAFT / ARBITRARY-TERMINAL-FLOW USE LOCATED / WITNESS-PRODUCING MUTUAL INDUCTION CLOSED CONDITIONALLY ON CHILD-CONTEXT FIDELITY`.

This dossier addresses `AC-PD-5CDC-HW1` from
`AC_PD_5CDC_R2_7_WITNESSED_INNERMOST_BUBBLE_COMPRESSION.md`.

---

## 1. The exact old arbitrary-flow step

The old one-cross cap-restoration proof uses ordinary vertex-number induction.
After the equality/DDD Morse descent reaches a genuine equal-face
cancellation, it declares a smaller target and invokes the outer induction
hypothesis.  The returned root flow on the descendant is explicitly allowed
to be arbitrary and need not be the inherited cancellation output.

Schematically:

\[
(G,\lambda)
\xrightarrow{2--0}
(H,\mu)
\xrightarrow{\text{ordinary existence induction}}
(H,\nu),
\]

where no history from `mu` to `nu` is supplied.

This is exactly the variable-order episode-compression gap.  Endpoint
normalisation can insert above `nu`, but local generator lifts cannot transport
an unspecified change `mu -> nu`.

The gap is therefore real in the old theorem statement.  It is not repaired by
finite state semantics, topology arborescences, local borrowing or marked-weld
flow selection.

---

## 2. Two simultaneous propositions

Replace the single existence induction by simultaneous strong induction on
closed target order.

### Proposition `P_N` — root solubility

Every connected loopless bridgeless cubic multigraph of order at most `N` has
a root-valued `E_5` flow.

### Proposition `Q_N` — witnessed one-cross cap restoration

Let `G=P union cap_i` be a connected loopless bridgeless cubic graph of order
at most `N`.  Let `G_j=P union E_j` be one valid connected loopless bridgeless
cross closure, and let

\[
\lambda:E(G_j)\to R_5
\]

be **any specified inherited root flow**.

Then either an accepted route, bounded, separator or category branch occurs,
or there exists a finite decorated contextual history starting at `lambda`
and ending at a root flow which glues `cap_i`.  The history records:

- every root-valued `2--2` NNI;
- every support-pair component switch;
- every equal-face cancellation and returned insertion;
- complete ordered incidences and cancellation matching;
- cap block, route sheet, support transport and side data.

Thus `Q_N` is the old extension theorem strengthened by a witness, not by a
new endpoint conclusion.

---

## 3. Proof order at one vertex level

Assume `P_n` and `Q_n` for every `n<N`.

Prove the level-`N` statements in the order:

\[
\boxed{Q_N\ \text{first},\qquad P_N\ \text{second}.}
\]

This order is noncircular.

---

## 4. Proof of `Q_N`

Start from the specified inherited cross flow `lambda`.

### 4.1 Boundary and immediate branches

The selected cross roots are equal, intersecting or disjoint.

- Intersecting gives the original cap immediately.
- A separating equality or DDD channel gives a witnessed support-switch
  history and the cap.
- Route, bounded and separator outcomes are declared exits.

All are explicit current-flow operations.

### 4.2 Locked equality/DDD branch

If every rescue channel is locked, apply the controlling current-flow Morse
rule.

Every nonterminal step is one of:

1. a specified strictly potential-lowering root Pachner NNI;
2. a specified support-pair switch or route event;
3. a specified equal-face cancellation.

The positive integer potentials make the forward segment finite.  No new root
flow is selected during a root NNI or support switch.

### 4.3 Strict cancellation

Suppose the current witnessed history reaches

\[
(G',\lambda')\xrightarrow{2--0}(H',\mu').
\]

The cancellation output `mu'` is already a specified root flow.  The source
category theorem supplies a smaller admissible contextual child, of target
order at most `N-2`, with inherited starting flow `mu'`.

Invoke

\[
\boxed{Q_{N-2}}
\]

on that inherited child state.  The induction output is not an arbitrary root
flow; it is a finite decorated history beginning at `mu'`.

If the child exits through route, bounded, separator or category data, the
parent branch exits.  Otherwise its witnessed history reaches the required
child terminal and includes every nested cancellation pair.

Apply the witnessed variable-order compression theorem from
`AC_PD_5CDC_R2_7_WITNESSED_INNERMOST_BUBBLE_COMPRESSION.md` to lift the child
history through the stored parent cancellation interface.  The result is a
predecessor-order history with at most one atom at each state.  Apply the
fixed-order return consumer to discharge that discrepancy and resume the
stored parent continuation.

Thus the cancellation branch returns with an explicit witness.

### 4.4 Termination of `Q_N`

- the current-flow potential strictly decreases between cancellations;
- every recursive child has target order at most `N-2`;
- every child history is finite by the strong induction hypothesis;
- witnessed bubble compression removes the variable-order pair without
  choosing a new unrelated flow;
- the fixed-order discrepancy rank terminates the returned parent segment.

Hence `Q_N` produces a finite history or an accepted exit.

---

## 5. Proof of `P_N`

Let `G` have order `N`.

- If `G` has no simple edge, it is theta and has the explicit root triangle.
- Otherwise choose a simple edge and the valid smaller cross closure `G/e`
  supplied by `R1`.
- By `P_{N-2}`, choose one root flow `lambda` on `G/e`.
- Apply the already proved level-`N` proposition `Q_N` to the **specified**
  flow `lambda`.
- The terminal history supplies a root flow on `G`.

Thus `P_N` follows from `P_{N-2}` and `Q_N`.

There is no use of `P_N` inside the proof of `Q_N`.

---

## 6. Formal well-founded shape

The simultaneous induction can be expressed as strong induction on `N` with a
within-level phase bit:

\[
(N,0)=Q_N,
\qquad
(N,1)=P_N,
\]

ordered so that:

- `(n,*) < (N,0)` whenever `n<N`;
- `(N,0) < (N,1)`.

Then:

- `Q_N` consumes only lower-order `Q_n` plus fixed-order local theorems;
- `P_N` consumes lower-order `P_n` and same-level `Q_N`.

This is a well-founded lexicographic induction and contains no circular
existence call.

---

## 7. Why the strengthening is conservative

The endpoint assertion of `Q_N` is exactly the extension assertion already
needed by the cubic proof.  The additional object is only a finite witness
record.

The strengthening adds no requirement that:

- arbitrary root flows on one graph be Kempe equivalent;
- every child terminal lie in one prescribed Kempe component;
- the original cancellation reinsert pointwise;
- graph order never change;
- every scheduling choice terminate.

It requires only that the proof use the concrete moves it already selects and
that recursive calls begin from the inherited child flow rather than discard
it.

---

## 8. Child-context fidelity obligation

The mutual induction closes `HW1` only if every strict cancellation descendant
is genuinely an instance of `Q_n`.

For each cancellation branch verify:

1. the descendant ordered four-pole and its target cap are defined;
2. the inherited cancellation output is a root flow on the selected valid
   cross/route closure of that descendant context;
3. the descendant is connected, loopless and bridgeless, or decomposes into
   accepted componentwise instances;
4. the target order drops by at least two;
5. cap block and physical route data restrict functorially;
6. a child route/category exit is also a valid parent exit.

Call this remaining source-interface check

\[
\boxed{\texttt{AC-PD-5CDC-HW1-CF — child-context fidelity}.}
\]

The old cap-restoration text states componentwise bridgeless lower-order
contexts, but it must be expanded to the six items above before `HW1` receives
full unconditional assurance.

---

## 9. Consequences for the old proof text

### Supersede

The sentence

> any genuine equal-face cancellation lowers target order and enters the outer
> induction hypothesis

must not be read as a call to bare root-flow existence.

### Replace by

> cancel to the inherited smaller contextual state, invoke the witnessed
> relative proposition `Q_{N-2}`, lift its returned history through the stored
> interface, and resume the parent continuation.

### Retain

The top-level use of ordinary root-flow existence is harmless:
`P_{N-2}` supplies the initial root flow on the selected simple-edge cross
closure, after which `Q_N` begins from that specified flow.

---

## 10. Trust boundary

### Closed here

- exact identification of the old arbitrary-flow call;
- simultaneous propositions `P_N,Q_N`;
- noncircular within-level proof order;
- replacement of cancellation existence calls by witnessed relative calls;
- supply of an explicit history witness to bubble compression;
- well-founded phase-bit formulation;
- preservation of the original global endpoint claim.

### Still open

- `HW1-CF` child-context fidelity at every equality/DDD cancellation;
- `HW2` complete ancestor genealogy/cap gluing;
- `HW3` compatibility with the exact fixed-order consumer alphabet;
- reconstruction of R2.4--R2.6 source inputs used by the fixed-order consumer;
- unconditional R2.7, cap restoration and global five-support closure;
- independent audit, Lean verification, curation, manuscript integration,
  release, arXiv, DOI, peer review or publication.

### Current classification

\[
\boxed{
\text{HISTORY-WITNESS ARCHITECTURE CLOSED}
\;/\;
\text{FULL HW1 AWAITS CHILD-CONTEXT FIDELITY}.
}
