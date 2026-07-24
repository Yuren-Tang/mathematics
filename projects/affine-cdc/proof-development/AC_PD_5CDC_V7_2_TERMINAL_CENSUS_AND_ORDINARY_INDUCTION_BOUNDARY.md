# AC-PD-5CDC v7.2 — exact terminal census and ordinary-induction boundary

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Classification:** `TERMINAL CENSUS COMPLETE / GLOBAL INDUCTION CONDITIONAL ON PURE-NNI TARGET REINSERTION`.

This dossier records every terminal type used by the v7.2 first-cancellation
route, the graph on which the conclusion lives, whether a root flow is already
supplied, and the exact consumer.  It prevents descendant profiles, category
flags or arbitrary theta recolourings from being treated as silent completion.

---

## 1. Terminal-result type

A terminal result is the tuple

\[
\mathcal T=(H,\lambda?,B,\kappa,\mathcal C,\alpha),
\]

where:

- `H` is the exact current target graph or shore completion;
- `lambda?` is either a supplied root flow on `H` or the explicit statement
  that ordinary lower-order existence must supply one;
- `B` is the ordered outer cap boundary, when present;
- `kappa` is the route/profile state, when present;
- `C` is one named terminal class below;
- `alpha` is the identity map from surviving current darts to the surrounding
  pure-NNI prefix.

No terminal is only a word such as `separator` or `theta`.

---

## 2. Immediate cap and route terminals

### 2.1 Selected cross already in `K_i`

The restricted cross flow itself supplies the boundary roots.  One global
support permutation aligns the complete five trace labels with the standard
cap state; gluing `C_i` produces a supplied root flow on the current target.
There is no recolouring of an inherited flow edge by edge.

### 2.2 Horizontal equality/DDD rescue

The support-pair component switch is performed on the specified cross flow and
directly produces intersecting cap insertion roots.  The resulting target flow
is supplied by that explicit switch.

### 2.3 Route change during the synchronized prefix or at cancellation

Before the first route change, internal surgery fixes the ordered outer root
word.  The exact route row puts the current descendant boundary in `K_i`.
Gluing the cap gives a supplied root flow on the current descendant target.
This is not yet an original-profile statement; it is returned only through the
stored pure-NNI prefix, conditional on the fixed-order return theorem.

---

## 3. Target-invalid NNI and first-cancellation category terminals

### 3.1 Cyclic two-cut

Complete each connected cyclic shore by one edge.  Both completions are
connected, loopless, bridgeless, cubic and strictly smaller.  Ordinary strong
induction supplies root flows; one global `S_5` permutation aligns the two
completion-edge roots.  Delete the completion edges and reglue the cut.

A nonempty acyclic two-port shore is impossible by the cubic shore formula
`n=k-2`.

### 3.2 Cyclic three-cut

Complete each cyclic shore by one cubic vertex.  The completions are strictly
smaller valid inputs.  The three boundary roots at each completion vertex form
one root triangle.  One global support permutation aligns the two ordered
triangles.  A noncyclic three-port shore is the explicit one-vertex gadget.

### 3.3 Cyclic four-cut

After two-cut reduction, each cyclic shore is connected.  Complete each shore
by each of the three two-vertex caps.  Every completion is strictly smaller
because the opposite cyclic shore has more than two vertices.  Ordinary strong
induction gives the three cap-forced profile intersections.  The exact finite
profile theorem and the Type T/H physical commutation eliminations give a
common boundary state; one global support permutation aligns it and the shores
glue.

A noncyclic four-port shore is exactly the explicit two-vertex cap.

### 3.4 Disconnected cross output at first cancellation

This is not a multi-component child.  The distribution of the four local
cancellation incidences yields, on the current parent target, either:

- a two-cut;
- a cyclic four-cut;
- the acyclic two-vertex cap.

The corresponding consumer is Sections 3.1 or 3.3.

### 3.5 Connected cross output but invalid smaller target

The three-reconnection category theorem returns on the current parent target:

- a cyclic cut of size at most four; or
- one bounded loop/parallel/triangle/theta/acyclic/low-port neighbourhood.

No invalid target is passed to lower induction.

---

## 4. Bounded graph terminals

### 4.1 Loop

In a connected cubic graph, a loop contributes degree two at its vertex; the
unique remaining nonloop incident edge is a bridge unless the graph is the
explicit bounded loop/bridge neighbourhood.  Delete/reinsert the loop in the
outer-shell support formulation or consume the bounded graph directly.

### 4.2 Parallel, triangle and low-port neighbourhoods

These are the finite endpoint coincidences in the NNI/reconnection category
tables.  Each either:

- is already theta/double-parallel and has an explicit root assignment; or
- exposes one of the 2/3/4-cut shores above; or
- is the one- or two-vertex acyclic shore.

No unbounded residual family is hidden under `bounded`.

### 4.3 Direct matching / theta

Closing a cross direct matching by the two-vertex cap is the theta multigraph;
assign roots `12,13,23` if no flow is already supplied.

Closing the same matching gives two loops joined by one zero bridge.  Assign
distinct intersecting roots `p,q` to the loops and zero to the bridge.  The four
branches are `(p,p,q,q)` and either crossed `(0,2,2)` resolution gives theta
with roots `p,q,p+q`.

This is an ordinary existential terminal in v7.2.  If a root flow on the theta
is already supplied, retain it.  If only the uncoloured bounded topology is
returned, choose the displayed root triangle explicitly.  No assertion is made
that this chosen theta flow is connected by a child history to an earlier flow;
v7.2 has no witnessed child proposition.  The chosen flow is simply the input
to the later pure-NNI prefix return.

---

## 5. Single-pop local terminals

A loop, parallel incidence, unavailable distinct borrowed vertex, or separator
arising in the equality/good-disjoint/missing-index five-leaf neighbourhood is
returned at the current order with the exact exterior darts.  It is consumed by
Sections 3--4.  It is not called a generic root/atom row.

---

## 6. Fixed-order return terminals

During pure-NNI normalization, a selected ordinary parent edge has exactly:

1. root success;
2. zero/co-root discrepancy;
3. route/profile escape to `K_i`;
4. a named 2/3/4-cut or bounded category result.

Items 3--4 are consumed above.  The unresolved discrepancy in Item 2 is **not**
a terminal and is the exact blocked interface in
`AC_PD_5CDC_V7_2_PURE_NNI_TARGET_REINSERTION_OBSTRUCTION.md`.

Therefore this census is exhaustive only after a theorem proves that every
nonterminal discrepancy reaches root success or one of Items 3--4.

---

## 7. No hidden same-level induction

Every recursive use of root solubility in the terminal consumers is strictly
smaller:

- first-cancellation genuine target: order `N-2`;
- cyclic two-cut completion: the opposite nonempty shore is removed;
- cyclic three-cut completion: the opposite cyclic shore has at least three
  vertices and is replaced by one;
- cyclic four-cut completion: the opposite cyclic shore has more than two
  vertices and is replaced by a two-vertex cap.

The bounded one-/two-vertex shores and theta are direct bases.  No terminal
consumer invokes root solubility of another order-`N` connected bridgeless cubic
graph.

---

## 8. Conditional ordinary strong induction

Let `P_N` be root solubility for connected loopless bridgeless cubic graphs of
order at most `N`.  Assuming the missing pure-NNI target-reinsertion theorem,
the induction would be:

1. choose a simple edge, or use theta as the no-simple-edge base;
2. R1 gives a valid cross closure of order `N-2`;
3. lower `P` supplies the specified initial cross flow;
4. the synchronized prefix reaches an exact terminal or the first cancellation;
5. exact terminals are consumed by this ledger;
6. a genuine first cancellation invokes lower `P` only on the actual target
   closure of order `N-2`;
7. the single pop gives root/one-atom/current-terminal output;
8. pure-NNI target reinsertion returns through the prefix;
9. hence `P_N`.

Steps 1--7 and every terminal consumer are reconstructed.  Step 8 is open.
Accordingly ordinary induction is a valid **conditional architecture**, not a
closed proof.

---

## 9. Outer-shell status

The independent shell audit accepted the support-count-preserving implication:

\[
\text{cubic five-support theorem}
\Longrightarrow
\text{finite bridgeless 5-CDC}.
\]

Port-cycle expansion, memberwise cut-even projection, componentwise use of the
same five indices, and insertion of all loops into two fixed supports remain
valid.  They are downstream of the blocked cubic theorem and are not reopened
in this epoch.
