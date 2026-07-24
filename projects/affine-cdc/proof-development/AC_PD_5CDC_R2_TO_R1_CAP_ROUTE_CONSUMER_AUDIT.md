# AC-PD-5CDC — R2 to R1 cap/route consumer audit

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Programme:** compressed five-support proof, simple-edge extension interface  
**Frozen Research Lead input:** `research/affine-cdc-five-cdc-v1@71a10f9ba86c1d2b8b7885e78fa9baa303c77818`  
**Classification:** `COMPLETE-DRAFT / ONE-CROSS CAP CONSUMER CLOSED / CUBIC INDUCTION REASSEMBLY READY`.

This dossier audits the literal hypotheses and terminal semantics connecting the
reconstructed contextual-transfer theorem `R2.7` to the structural one-cross
reduction `R1`.

It corrects three dangerous shortcuts:

1. a `K_i` state on a surgery descendant is not automatically a member of the
   original four-pole profile;
2. a same-matching zero-vertex terminal is not discharged merely by observing a
   bridge;
3. a support-unordered common state must be converted to labelled boundary
   equality by one global support permutation before gluing.

---

## 1. One selected structural cross

Let `G` be a finite connected loopless bridgeless cubic multigraph and let
`e=uv` be a simple edge.  Remove `u,v`, retaining the four ordered outer
incidences.  Their original partition by the deleted vertices is

\[
M_i=X_i\mid Y_i.
\]

The deleted neighbourhood is the two-vertex cap `cap_i`.  Let `E_j`, `j\ne i`,
be one cross zero-vertex reconnection supplied by `R1` such that

\[
G_j=P\cup E_j
\]

is connected, loopless, bridgeless, cubic and has exactly two fewer vertices.

The proof uses only this one selected cross.  No flow on the other cross or on
the direct reconnection is required.

By lower-order root solubility choose a specified root flow on `G_j`.  Cutting
the two reconnection edges gives a boundary state

\[
\sigma\in J_j=\{A,B_j,C_j\}.
\]

The cap profile is

\[
K_i=\{B_j,B_k,D_j,D_k\}.
\]

The finite certificate gives

\[
J_j\cap K_i=\{B_j\}.
\]

---

## 2. Immediate intersecting-root branch

If `sigma=B_j`, the two selected cross roots are distinct and intersect.  Their
sum is a root, so restoring the two deleted cap vertices gives a root-valued
central edge.

The support-unordered state belongs to both the four-pole and cap profiles.
Section 8 proves the required labelled gluing.  This branch closes immediately.

Thus only:

\[
\sigma=A
\quad\text{or}\quad
\sigma=C_j
\]

enters singular analysis.

---

## 3. Separating rescue versus fixed route

Assume for contradiction that the original cap is blocked:

\[
\Sigma(P)\cap K_i=\varnothing.
\]

### Equality start

At `A`, the three route targets are

\[
(B_i,B_j,B_k)
\]

under `(M_i,M_j,M_k)`.  Since `B_j,B_k\in K_i`, every realised non-cap route
would contradict blocking.  Therefore:

- a separating equality channel switches exactly one marked reconnection root
  and gives an immediate `B_j`/`B_k` cap lift; or
- every relevant channel is locked and all nonterminal challenges remain on
  
  \[
  A-B_i-C_i
  \]
  
  with physical route `M_i`.

### DDD start

At `C_j`, every crossed repair row has one non-`K_i` target under `M_i` and two
`K_i` targets under `M_j,M_k`.  Therefore:

- a separating crossed channel gives an immediate cap repair; or
- every relevant channel is locked and all nonterminal challenges remain on
  
  \[
  C_j-D_i-C_k
  \]
  
  with physical route `M_i`.

The complete labelled row audit is exactly
`AC_PD_5CDC_R2_1_BOUNDARY_ROUTE_CERTIFICATE.md`.  The route `M_i` is the literal
original cap matching, not an orbit chosen after the fact.

---

## 4. Current-flow descent

Inside either fixed-route lock, the positive equality or DDD potential chooses
a finite current-flow history whose nonterminal source steps are:

1. a strictly potential-lowering root NNI;
2. a genuine equal-face cancellation;
3. a route/profile terminal.

Initial separating support switches have already been removed.  Any later
support switch is terminal/rootifying and is represented by the normalized
switch--pop collar of the fixed-order consumer.

Every root NNI remains connected and bridgeless.  A genuine equal-face
cancellation either:

- exposes a cyclic two-edge-cut gluing exit; or
- produces one connected inherited lower-order contextual child handled by
  `Q_{N-2}` and `R2.7`.

No arbitrary descendant root flow is selected.

---

## 5. Route-changing terminal

Before the first route-changing event, internal root surgery preserves the four
ordered terminal roots and hence the same ten-state class in `J_i` or `L_i`.
The descendant four-pole need not have the same complete profile as the original
one.

If one complementary challenge is first realised with route `M_j` or `M_k`,
the exact route row gives a root boundary state

\[
\tau\in K_i
\]

on the **current descendant** `P_t`.

The correct implication is:

\[
\tau\in\Sigma(P_t)\cap K_i
\Longrightarrow
\text{cap-compatible terminal for contextual return}.
\]

It is not yet the statement

\[
\tau\in\Sigma(P_0).
\]

Apply `AC_PD_5CDC_R2_7_RESOLVED_CALL_CONTEXTUAL_TRANSFER.md` to the complete
finite history.  The terminal returns to:

- a root state in `K_i` on the original four-pole; or
- another established route/profile, bounded, cyclic two-cut or separator exit.

Only after this return may the original cap be glued.

---

## 6. Direct-pairing terminal

If all source vertices disappear, the remaining ordered four-pole is one of the
three direct matchings.

### Cross matching

Closing by `cap_i` gives the theta multigraph.  Assign a root triangle, for
example

\[
12,13,23.
\]

### Same matching

Closing by `cap_i` gives two loops joined by one bridge.  Observing the bridge is
not by itself a solution.  Give the two loops distinct intersecting roots `p,q`
and the bridge value zero.  Around the zero bridge the branch word is

\[
(p,p,q,q),
\]

whose pairing sums are `(0,2,2)`.  Either crossed resolution turns the graph
into theta with root values

\[
p,q,p+q.
\]

Thus every direct matching supplies a root-valued cap-attached theta terminal
after at most one zero-to-root NNI.

If the terminal occurs after nontrivial surgery, it is returned through `R2.7`;
it is not identified directly with an original-profile state.

---

## 7. Cancellation terminal

A genuine equal-face cancellation is not a completed terminal at parent order.
Use the witnessed simultaneous induction:

- the inherited child is a literal lower-order `Q` instance;
- child history, cap block, route and darts are recorded;
- nested bubbles compress source-faithfully;
- the exact inverse table returns a root/alternative/one-atom parent state;
- fixed-order track normalization completes the parent obligation.

The resolved-call rank and original-prefix induction are those of `R2.7`.

---

## 8. Labelled gluing from a common boundary state

The ten boundary states are support-unordered multisets of the five even traces

\[
S_1,\ldots,S_5\subseteq\{1,2,3,4\}.
\]

Suppose the original four-pole and `cap_i` realise the same support-unordered
state.  Then their trace multisets agree, so there is one permutation

\[
\pi\in S_5
\]

which sends the five cap traces to the five four-pole traces coordinatewise.
Apply `pi` globally to every support index of the cap flow.

At each terminal incidence, its root is exactly the two support indices whose
traces contain that incidence.  Coordinatewise trace equality therefore aligns
every terminal root edge by edge.  Glue corresponding semiedges.

### Theorem 8.1 — labelled cap gluing

A common support-unordered state in

\[
\Sigma(P)\cap K_i
\]

produces a root-valued flow on

\[
P\cup cap_i
\]

after one global support permutation on the cap side.

No terminal permutation and no edgewise independent support relabelling is
used.

---

## 9. Witnessed one-cross extension

Let `Q_N` be the witnessed extension proposition for a specified inherited flow
on one valid selected cross closure.

### Theorem 9.1 — simple-edge extension

For every order-`N` connected loopless bridgeless cubic graph, every specified
root flow on the valid selected cross closure at a simple edge has one of:

1. immediate labelled cap gluing;
2. a finite witnessed contextual history returning a cap-compatible original
   state and hence labelled gluing;
3. a cyclic two-cut, route/profile, bounded theta or separator terminal already
   consumed by the established outer branch.

### Proof

Sections 2--7 exhaust the selected boundary trichotomy and all terminals of the
finite equality/DDD current-flow history.  `R2.7` returns every descendant
cap-compatible terminal to the original context.  Section 8 performs the final
labelled gluing. ∎

This closes `Q_N` at PDL complete-draft level.

---

## 10. Cubic induction

Let `P_N` state that every connected loopless bridgeless cubic graph of order at
most `N` has a root flow.

- If no simple edge exists, the graph is theta and is explicit.
- Otherwise `R1` supplies a valid selected cross closure with two fewer vertices.
- `P_{N-2}` supplies one specified root flow on that closure.
- The already proved same-level `Q_N` extends it across the deleted cap.

The proof order

\[
Q_N\quad\text{then}\quad P_N
\]

is noncircular.  Hence every finite connected loopless bridgeless cubic
multigraph has a root-valued `E_5` flow, equivalently five indexed even supports
covering every edge exactly twice.

---

## 11. Exact supersessions at the consumer interface

Supersede these old readings:

1. “route change on `P_t` immediately proves `Sigma(P_0) cap K_i != empty`”;
2. “same-matching direct terminal is discharged merely because its cap closure
   has a bridge”;
3. “a support-unordered common state glues without proving one global labelled
   alignment”;
4. “strict cancellation directly enters ordinary lower-order existence
   induction”;
5. “all three reconnection closures or the complete profile classification are
   needed”.

Retain:

- one selected valid cross closure;
- `J_j cap K_i={B_j}`;
- the exact unique non-`K_i` route rows;
- finite equality/DDD current-flow descent;
- contextual return of descendant terminals;
- theta base and vertex-order induction.

---

## 12. Trust boundary

### Closed at PDL complete-draft level

- exact selected-cross boundary trichotomy;
- labelled immediate cap branch;
- separating-rescue/fixed-route dichotomy;
- preservation of the literal original cap route;
- descendant route-change scope and contextual return;
- corrected same-matching direct terminal;
- cancellation child consumption;
- one-global-permutation labelled gluing;
- witnessed simple-edge extension `Q_N`;
- noncircular cubic induction `P_N`.

### Still downstream

- support-count-preserving general-graph outer-shell audit;
- updated global proof DAG and fixed snapshot;
- independent adversarial audit;
- Curator integration and AC-DIR disposition.

No Lean, manuscript, release, arXiv, DOI, peer-review or publication status is
asserted here.
