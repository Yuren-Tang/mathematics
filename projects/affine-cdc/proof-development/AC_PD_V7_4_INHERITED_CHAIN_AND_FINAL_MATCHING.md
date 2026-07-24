# AC-PD v7.4 — inherited component chain and final matching

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Classification:** `LOAD-BEARING GRAPH-RANK LEMMAS / COMPLETE-DRAFT`.

This dossier isolates the two points at which a quotient argument can silently
become nonphysical:

1. claiming a shorter path after an NNI without retaining the actual later
   connectors;
2. claiming the final local reconnection changes the ordered terminal matching
   without knowing that the two passages are distinct physical components.

Both are proved below with stable edge/dart witnesses.

---

## 1. Witnessed chain object

A witnessed component chain consists of

\[
\mathfrak C=(X_0, c_1, X_1,c_2,\ldots,c_\ell,X_\ell)
\]

where:

- `X_0,X_ell` are the two distinguished `H_h` terminal paths;
- every intermediate `X_i` is either a closed `H_h` cycle or one inactive
  singleton vertex;
- every `c_i` is a named stable physical edge outside `H_h`;
- the ordered endpoint darts of `c_i` identify its incidences in `X_{i-1}` and
  `X_i`;
- all `X_i` are pairwise distinct.

A shortest simple path in the initial connected quotient supplies such an
object.  Shortestness is used only to obtain a simple initial list.  It is not
recomputed after a move.

Define the stage rank by the number of remaining connector witnesses.

---

## 2. Inactive first node

Assume `X_1={v}` is inactive and connectors `c_1,c_2` both meet `v`.
This is the strongest possible collision: the entry and exit quotient edges are
both incident with the source vertex modified by the NNI.

Use the active/inactive row at `c_1`.  The source vertex `v` is replaced by one
of the two target active vertices, while the other target vertex comes from the
old active endpoint.  The new central edge is in `H_h`, so both target vertices
belong to the enlarged component `X_0'`.

The stable edge `c_2`:

- is not the central edge `c_1`;
- is not deleted;
- keeps its root, outside endpoint and outside dart;
- has a root disjoint from `h`, hence remains outside `H_h`;
- has its inside dart reattached to one target active vertex in `X_0'`.

Therefore

\[
(X_0',c_2,X_2,\ldots,c_\ell,X_\ell)
\]

is an inherited physical chain.  This is not a path discovered after the move;
it is the old connector list with `c_1` removed.

If `ell=2`, `c_2` is already the final connector from the enlarged path to the
other distinguished path.

---

## 3. Active-cycle first node

Assume `X_1` is a closed active channel cycle.  Let `v` be the endpoint in
`X_1` of entry connector `c_1`.

At an active cubic vertex, exactly two incidences are in `H_h`.  The third and
only third incidence is outside `H_h`.  Hence `c_1` uses the unique nonchannel
dart at `v`.

The next distinct connector `c_2` cannot also meet `v`.  Its endpoint in `X_1`
is a different vertex `w`.  The root NNI or equal branch swap at `c_1` modifies
only the two endpoint vertices of `c_1`; it leaves `w`, `c_2`, both darts of
`c_2`, and its root unchanged.

The cross-connection merges the whole cycle `X_1` into `X_0`; therefore the
unchanged endpoint of `c_2` at `w` now lies in `X_0'`.  The inherited chain is
again the old list with `c_1` removed.

### No silent later merge

The only new `H_h` connections join the two local passages in `X_0,X_1`.  The
new active/active central root is outside `H_h`.  Hence no `X_j`, `j>=2`, is
merged or relabelled without its stored connector being consumed.

---

## 4. Parallel and loop quotient edges

Parallel quotient edges carry different stable physical edge identities.  A
simple node path chooses one witness and remains valid.

A quotient loop joins two vertices of one already contracted channel component;
it is never an edge of a shortest simple chain between distinct nodes.  A
physical graph loop, bridge or forbidden parallel degeneration is an exact
category output and is not admitted into the continuing prime carrier.

Thus multigraph structure does not weaken the inherited-path proof.

---

## 5. Inductive contraction theorem

### Theorem 5.1 — literal prefix deletion

Suppose

\[
\mathfrak C_r=(Y_r,c_{r+1},X_{r+1},\ldots,c_\ell,X_\ell)
\]

is the inherited chain after `r` contractions and no terminal has occurred.
The root NNI at `c_{r+1}` produces

\[
\mathfrak C_{r+1}=(Y_{r+1},c_{r+2},X_{r+2},\ldots,c_\ell,X_\ell).
\]

Every remaining `c_i` has the same stable edge identity, root and outside
ancestry as in the initial state.  Its inside endpoint is unchanged unless it
was the exit dart of an absorbed inactive singleton, in which case the exact
NNI dart map places it in `Y_{r+1}`.

Consequently the rank drops from `ell-r` to `ell-r-1` by deletion of one named
connector.  There is no appeal to shortest distance in a recomputed quotient.

---

## 6. Final connector: distinct endpoint types

Let the last connector join two distinct terminal paths.  At the two endpoint
vertices the current channel passages have four labelled halfedges

\[
x_0,x_1\quad\text{and}\quad y_0,y_1.
\]

Outside the local two-vertex cell, the first path joins `x_0,x_1` to two ordered
terminals and the second joins `y_0,y_1` to the other two terminals.

The current local pairing reconnects `x_0-x_1` and `y_0-y_1`.  The unique
root-valued opposite NNI connects

\[
x_0-y_\epsilon,\qquad x_1-y_{1-\epsilon}
\]

for one `epsilon`.  It therefore pairs each terminal of the first old path with
a terminal of the second old path.  The old matching cannot survive.

The other opposite pairing is co-root-valued and is not traversed.

---

## 7. Final connector: equal endpoint types

For equal endpoint triangles, the current root placement is the pair of local
passages belonging separately to the two terminal paths.  The three labelled
placements are:

1. current root placement;
2. root branch swap;
3. zero placement.

The branch swap is the only alternative root placement.  It cross-connects the
two distinct terminal paths exactly as in Section 6.  Because darts and terminal
ends are labelled, it is not identified with the current placement by symmetry.
The zero placement is forbidden and unused.

### Theorem 7.1 — equal final move changes matching

Even when endpoint support triangles are equal, the selected root branch swap
changes the ordered terminal matching.  The audit-#78 same-arc counterexample is
irrelevant here: its two local passages belonged to one common channel
component, whereas the final-chain hypothesis requires two distinct named
terminal components.

---

## 8. Ordered matching census

If the current matching is

\[
AB|CD,
\]

the final connector yields exactly one of

\[
AC|BD,\qquad AD|BC.
\]

If the current matching is one crossed matching, the final connector yields the
other crossed matching or the separated matching.  In every case it leaves the
current matching.

The ordered endpoints and route orientation are retained, so the conclusion is
stronger than an unlabelled statement that the number of components changes.

---

## 9. Category and complete-state boundary

After each NNI, including the final connector, recompute:

- connectedness, looplessness, cubic category and bridgelessness;
- exact cyclic `2/3/4`-cut and bounded flags;
- channel components and terminal matching;
- cap-compatible route/profile;
- prescribed parent status;
- stable dart and prefix maps.

A failed test is returned to its exact consumer.  Only a category-safe root
state proceeds.

---

## 10. Falsification checklist disposition

1. **Inactive singleton has both adjacent quotient edges at the modified
   vertex:** accepted and handled by the stable `c_2` dart map.
2. **Next connector after absorption:** same stable edge, unchanged nonchannel
   root, inherited ancestry.
3. **Active-cycle entry and exit at one modified vertex:** impossible because
   an active vertex has exactly one nonchannel incidence.
4. **Final equal-endpoint swap preserves matching:** impossible for two distinct
   terminal components; the alternative root placement cross-connects them.
5. **Path shortening is only recomputed distance:** rejected; the proof retains
   one initial connector list and deletes its first witness at each step.

No obstruction remains in these five attack points at PDL reconstruction level.