# AC-PD-5CDC R2.7 — cancellation child-context fidelity

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Programme:** compressed five-support proof, global-return unit `R2.7`  
**Classification:** `COMPLETE-DRAFT / HW1-CF CLOSED / DISCONNECTED CHILD IS A TWO-CUT EXIT`.

This dossier closes the child-context fidelity interface left by
`AC_PD_5CDC_R2_7_MUTUAL_INDUCTION_HISTORY_WITNESS.md`.

---

## 1. Relative equal-face cancellation

Let a connected loopless bridgeless cubic source or cap-closed contextual graph
carry a root-valued `E_5` flow.  Suppose adjacent vertices `u,v` carry the same
root triangle

\[
\{a,b,r\},
\qquad r=a+b,
\]

and are joined by the edge of value `r`.

Write the four noncentral incidences as

\[
a_u,b_u,a_v,b_v,
\]

where the two `a` incidences carry root `a` and the two `b` incidences carry
root `b`.

Equal-face cancellation removes `u,v,r` and reconnects

\[
a_u\sim a_v,
\qquad
b_u\sim b_v.
\]

The ordered exterior semiedges of the ambient four-pole, when present, are
retained as labelled incidences throughout this relative replacement.

The output:

- is cubic;
- has two fewer source vertices;
- inherits a root-valued flow;
- contains no loop;
- is componentwise bridgeless.

The last three facts follow from the equal-face root equations and the
bridge-zero cut-sum lemma.

---

## 2. Exterior after deleting the dipole

Let

\[
H=G-\{u,v\}
\]

with the four retained noncentral incidences treated as terminals.

Because `G` is connected and bridgeless, every component of `H` contains at
least two of the four terminals: a component containing exactly one terminal
would be attached to the rest of `G` by one bridge.

Hence exactly one of the following holds.

1. `H` is connected.
2. `H` has two components `X,Y`, each containing exactly two terminals.

There is no third case.

---

## 3. Disconnected cancellation forces a two-edge cut

### Lemma 3.1

If the equal-face cancellation output is disconnected, then the original
pre-cancellation graph has a two-edge cut.

### Proof

If `H` is connected, adding the two reconnection edges cannot disconnect it.
Thus `H=X\sqcup Y` with two terminals on each side.

For the cancellation output to remain disconnected, neither new reconnection
edge may join `X` to `Y`.  Therefore, after possibly exchanging `a,b` and
`X,Y`,

\[
a_u,a_v\in X,
\qquad
b_u,b_v\in Y.
\]

In the original graph, the only edges from `X` to its complement are exactly
the two old dipole incidences corresponding to `a_u,a_v`.  Removing those two
edges isolates `X`.  Hence they form a two-edge cut.  The same is true on the
`Y` side. ∎

### Corollary 3.2

In a branch in which cyclic two-edge cuts have already been discharged, every
nonexit root-valued equal-face cancellation has connected output.

If the two-edge cut is encountered before that reduction, it is an accepted
small-cut branch: complete both shores by one edge, apply the lower-order
root-flow theorem separately, align the two completion roots by one global
`S_5` permutation on one shore, and glue.

Thus disconnected cancellation is progress, not a recursive child whose two
components require synchronized contextual return.

---

## 4. Preservation of the contextual instance

Assume henceforth that the cancellation does not exit through the two-cut
branch.

### 4.1 Ordered boundary

The relative cancellation changes only the bounded dipole neighbourhood.  All
ordered outer cap incidences are retained as the same labelled semiedge slots.
The child therefore has the same ordered cap shore and the same distinguished
matching convention.

### 4.2 Inherited flow

Every surviving old edge keeps its root.  The two new reconnection edges carry
`a` and `b`.  Hence the child starts with a specified inherited root flow; no
new flow is selected.

### 4.3 Graph category

The child is:

- connected by Corollary 3.2;
- loopless by the loop/flow equation argument;
- bridgeless because every edge has nonzero root value;
- cubic by construction.

It is therefore an admissible smaller input of the same source category.

### 4.4 Strict order

Exactly the two dipole vertices are removed:

\[
|V(H')|=|V(G)|-2.
\]

Thus every child call is strictly lower in the simultaneous `P/Q` induction.

### 4.5 Cap block and route

The cap block is a partition of the retained ordered outer incidences and is
unchanged by an internal relative surgery.

The current physical route/support record restricts to the child by:

- retaining every old support incidence outside the dipole;
- replacing the two equal-face traversals through the dipole by the two
  inherited reconnection edges of the same roots;
- retaining the distinguished route sheet and orientation bit.

This restriction is determined by the current labelled root assignment and
ordered incidences.  It introduces no independent genealogy choice.

If the selected cancellation itself exposes a route/profile change, that is an
accepted parent terminal and no child return is required.

### 4.6 Child exits

A route/profile, bounded, separator or category exit in the child is also a
valid parent exit:

- route and profile conclusions concern the unchanged ordered outer cap shore;
- a bounded terminal remains bounded after restoring the stored finite dipole
  neighbourhood;
- a child cut together with the two stored dipole vertices gives either the
  same cut order or one of the already accepted bounded low-port
  configurations;
- the explicit two-cut case was separated in Section 3.

No child-only terminal is silently reclassified as a successful parent pop.

---

## 5. The child proposition

Let `Q_N` be the witnessed relative cap-restoration proposition from
`AC_PD_5CDC_R2_7_MUTUAL_INDUCTION_HISTORY_WITNESS.md`.

### Theorem 5.1 — child-context fidelity

Every strict equal-face cancellation selected by the equality/DDD current-flow
descent has exactly one of:

1. a cyclic two-edge-cut gluing exit;
2. an accepted route/bounded/separator terminal;
3. one connected loopless bridgeless cubic child of order two less, carrying:
   - the inherited root flow;
   - the same ordered outer cap shore;
   - the restricted cap block, route sheet and support data.

In Case 3 the child is a literal instance of `Q_{N-2}`.  Its returned decorated
history can therefore be consumed by witnessed bubble compression.

### Consequence

The old sentence

> cancellation gives componentwise bridgeless lower-order contexts

must be sharpened in the controlling proof to:

> disconnected output is an immediate two-cut gluing exit; otherwise there is
> one connected inherited lower-order contextual child.

This removes the only component-distribution ambiguity in `HW1-CF`.

---

## 6. Status of `HW1`

Combining:

- witnessed innermost-bubble compression;
- the simultaneous `P_N/Q_N` induction;
- Theorem 5.1 above;

gives the following.

### Corollary 6.1 — history-witness interface

Every recursive cancellation call in the controlling one-cross route can be
made on a specified inherited smaller contextual state and returns either an
accepted exit or an explicit finite decorated move history.  No arbitrary
terminal recolouring is required.

Thus:

\[
\boxed{\texttt{AC-PD-5CDC-HW1 CLOSED}.}
\]

---

## 7. Remaining assurance interfaces

The variable-order compression route now has two remaining interfaces.

### `HW2` — full-labelled genealogy gluing

Verify across every local lift and innermost replacement that ancestor ordered
incidences, cap block, route sheet and side attachments agree literally at
concatenation seams, including central-mark-consuming cancellations.

### `HW3` — fixed-order consumer alphabet

Verify that the fixed-order closed/open/periodic track theorems consume the
flattened cells actually produced by bubble compression:

- root NNIs;
- support-switch correction cells;
- bounded one-atom active-diagonal movies;
- alternative-insertion endpoint macros.

No proof of R2.7 is declared until both are closed together with the retained
R2.4--R2.6 source theorems.

---

## 8. Trust boundary

### Closed here

- exact two-component exterior classification;
- disconnected cancellation implies a two-edge cut;
- two-cut gluing disposition;
- connected nonexit child category;
- inherited flow and strict order;
- ordered cap/route restriction;
- validity of child exits at parent level;
- `HW1-CF` and hence `HW1`.

### Not closed here

- `HW2` and `HW3`;
- independent reconstruction of every fixed-order track theorem;
- unconditional R2.7 and cap restoration;
- the global five-support theorem;
- independent audit, Lean verification, curation, manuscript integration,
  release, arXiv, DOI, peer review or publication.
