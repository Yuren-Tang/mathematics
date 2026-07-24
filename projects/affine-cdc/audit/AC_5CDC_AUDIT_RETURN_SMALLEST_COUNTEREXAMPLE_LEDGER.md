# AC-5CDC-AUDIT-RETURN-01 — smallest-counterexample search ledger

This ledger records both successful falsification searches and the smallest
remaining proof obstructions.  “No counterexample found” means only within the
stated local search; it is not a global correctness claim.

## Search G1 — ordered nonbacktracking pivot cells

**Universe.** Roots are the ten two-subsets of `[5]`; adjacency is disjointness.
Search all ordered paths `x-s-t-y` with `x != t`, `s != y`.

**Count.** `10*3*2*2=120`.

**Tests.** For every case:

- `z=x+t` and `w=s+y` have weight two;
- `z != w`;
- `|z intersect w|=1`;
- `(z,z,w,w)` has central pairing values `0,z+w,z+w`;
- `z+w` is a root.

**Result.** `120/120 PASS`; no coefficient counterexample.

**Reproducer.** `AC_5CDC_AUDIT_RETURN_PIVOT_ENUM.py`.

## Search G2 — smallest decorated seam stress test

Use the normal-form cell

- `x=35`, `s=12`, `t=34`, `y=15`;
- `z=45`, `w=25`, `u=z+w=24`.

The unmarked four-port has exactly one zero pairing and two root pairings joined
by one NNI.  Add one surviving ancestor mark on the active central atom/diagonal.
The coefficient seam still exists, but the mark is not on the fixed exterior
boundary.  The current R2.6 proof does not say whether it is fixed or transported
and does not compare the transported endpoint with the adjacent run section.

**Disposition.** Not a counterexample to the seam theorem after marked lineage is
added; it is the smallest witness to `G-MARK-1`.

## Search H1 — disconnected cancellation

Delete an equal-face dipole and classify components of the four-terminal
exterior.  Every component has at least two terminals, so there are only:

- one connected component; or
- two components with two terminals each.

If the cancellation output is disconnected, both reconnection edges lie within
shores, and the two original incidences on either shore form a two-edge cut.

**Result.** No counterexample; the cyclic two-cut exit is valid.

## Search H2 — child separator restoration

Smallest unresolved configuration:

- one stored equal-face dipole;
- a child separator which uses at least one of the two new reconnection edges;
- the four cancellation terminals distributed across the child shores.

Restoring the dipole replaces a reconnection edge by two incidences and the
central edge.  Depending on the terminal partition, the child cut can disappear
or change order.  The candidate provides no partition census or exact accepted
parent category.

**Disposition.** `H-SEP-1`, a source-interface proof obstruction.  No concrete
5-CDC counterexample is claimed.

## Search I1 — central mark semantics

Three cases were tested against the frozen source movies.

1. Raw central cancellation: both central darts disappear; no child descendant.
2. Successful paired bubble: predecessor-order raw insertion supplies a central
   pair carrying a suspended ancestor boundary mark.
3. Child exit: no parent pop and no restoration required.

**Result.** The three notions are consistent when call-local and ancestor marks
are distinguished.  No genealogy counterexample found.

## Search I2 — support-switch atom in a closed core

The locked Morse history uses only decreasing root NNIs and equal-face
cancellations.  Support switches can be chosen only as initial rescue,
route/bounded terminal, endpoint rootification, or terminal switch--pop collar.
After immediate `A/C` normalization, no raw singular support-switch cell remains
inside a closed Ptolemy component.

**Result.** No consumer-alphabet counterexample found for the chosen execution.

## Search J1 — terminal-free singleton sink

A one-vertex reachable nonterminal relation with no outgoing edge is a sink SCC
and contains no positive directed cycle.  The current no-sink proof begins by
choosing a cycle and has not separately proved outgoing-macro totality.

**Result.** Smallest abstract countermodel to the stated SCC argument.

## Search J2 — distance-restoring two-state cycle

Let `d_top(x)=2`, `d_top(y)=1`.  Include finite witnessed macros

- `x -> y` (parent success);
- `y -> x` (returned normalization/reset).

Then `{x,y}` is a terminal-free sink SCC.  Local success decreases `d_top`, but a
macro not controlled by a no-reset invariant restores it.

**Result.** Smallest abstract countermodel to the claimed implication from local
parent successes plus finite macro expansion to global strict descent.

## Search J3 — arbitrary-root-loop falsification target

No explicit decorated source loop was found that satisfies all intended active
obligation constraints yet ends on a wrong root topology.  The search instead
found that those constraints are not stated as a proved invariant of `M_N`.
Thus the audit returns `BLOCKED-PROOF`, not `COUNTEREXAMPLE`.

## Global search disposition

- No counterexample to the 5-CDC statement was produced.
- No counterexample to the unmarked `(0,2,2)` seam was produced.
- One local marked-interface repair is required.
- One child-exit interface is unproved.
- The resolved-call no-sink/rank argument admits finite abstract countermodels
  under its currently stated hypotheses.
