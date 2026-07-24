# AC-PD-5CDC v7.2 — full-state state-walk and cellwise track reconstruction

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Frozen research input:** `research/affine-cdc-five-cdc-v1@094ca09f6d3982b785a3f3428d9ec079dbba0855`  
**Classification:** `COMPLETE-DRAFT AS A FIXED-ORDER TRACK THEOREM / DOES NOT BY ITSELF PROVE TARGET SUCCESS`.

This dossier reconstructs the narrow fixed-order input retained by v7.2.  It
does not use shortest Petersen cycles, the R2.5 odd-core theorem, `C6/C8`
annuli, a Type-T source contraction, abstract `abba` deletion, support-switch
interior cells, or graph-order recursion.

---

## 1. Normalized full-state atom track

After one inverse NNI failure or the missing-index single-pop row, local
normalization leaves at most one standard co-root atom at every persistent
singular state.  A complete state records:

- the literal labelled cubic topology and ordered dart slots;
- every root label and the unique atom edge/value;
- the two crossed root resolutions of the atom;
- every emitted side root and rooted exterior attachment;
- support transport;
- the ordered cap block and route orientation;
- every fixed-order mark required by the comparison.

The critical-overlap table is exhaustive:

1. a disjoint root NNI commutes with the atom;
2. a zero atom adjacent to a root NNI leaves one zero atom and a root new edge;
3. a good co-root overlap leaves one co-root atom and a root new edge;
4. a missing-index overlap creates exactly one transient adjacent co-root edge,
   hence one three-vertex defect tree, and one explicit defect-lowering NNI
   returns to at most one atom or a two-cut/bounded exit.

Thus the persistent singular locus is a one-manifold: it neither branches nor
carries two persistent atoms.  Raw support switches and `2--0/0--2` cells are
absent from the v7.2 fixed-order alphabet.

Associate to each co-root atom its two crossed root resolutions

\[
F=\{s,t\}\in E(KG(5,2)).
\]

Consecutive genuine atom states share exactly one root and therefore form a
finite walk in the line graph of the Petersen graph.  Repeated coefficient
states which are only identity subdivisions or coefficient-neutral intervals
are retained in the physical history and absorbed into the surrounding run;
they are not deleted by coefficient equality.

---

## 2. Maximal-run and switch decomposition

For consecutive genuine states

\[
F_{r-1},F_r
\]

let

\[
p_r=F_{r-1}\cap F_r
\]

be the transition pivot.  Partition the pivot word into maximal constant runs.

### Constant-pivot run

Write

\[
F_j=\{s,d_j\}
\]

through one maximal run, and let `z_j` be the emitted side root between
`F_{j-1}` and `F_j`.  Petersen transport gives

\[
d_{j-1}+d_j+z_j=0.
\]

At that turn a simultaneous root restriction preserving `z_j` must choose the
nonshared endpoints `d_{j-1},d_j`.  The pivot choice `s,s` gives `z_j`, not
zero, and a mixed choice contains two disjoint roots.  Hence the nonpivot
history is unique.

Both root-valued long-side restrictions of a regular neighbourhood have the
same source topologies, side word, exterior darts, support transport, cap/route
and mark data.  Uniqueness forces equality at every slice.  Therefore the two
long sides are literally one complete root history `H`, and

\[
H\times[0,1]
\]

is a legal root-valued identity strip fixing the complete rectangular boundary.
No physical run is contracted and no support monodromy is declared trivial.

### Genuine switch cell

At a change from pivot `s` to pivot `t`, the immediate atom states are

\[
F^-=\{s,x\},\qquad F=\{s,t\},\qquad F^+=\{t,y\}.
\]

Normalized distinctness of consecutive genuine states gives

\[
x\ne t,\qquad y\ne s.
\]

These are local state-walk inequalities; they are not read from the next vertex
of the reduced run skeleton.

---

## 3. Six-port seam at every genuine switch

The four-pivot word is

\[
x\to s\to t\to y,
\]

where consecutive pairs are disjoint Petersen roots and the two displayed
nonbacktracking inequalities hold.  Put

\[
z=x+t,\qquad w=s+y.
\]

### Human normal form

By `S_5` symmetry take

\[
s=12,\qquad t=34.
\]

Then

\[
x\in\{35,45\},
\qquad
y\in\{15,25\}.
\]

Consequently `z` is the other of `35,45` and `w` is the other of `15,25`.
Thus `z,w` are distinct roots meeting in the unique fifth support index.  Hence

\[
(z,z,w,w)
\]

has pairing-weight pattern

\[
(0,2,2).
\]

The two root-valued binary topologies are the crossed path and the canonical
star.  They differ by zero or one relative root NNI while both turn corollas

\[
L=(x,t,z),\qquad R=(s,y,w)
\]

remain fixed pointwise.  This gives a transverse root seam inside the actual
complete source cell.

The seam exposes root `t` toward the left `s`-run and root `s` toward the right
`t`-run.  Those are exactly the nonpivot endpoint roots forced by the two
adjacent identity strips.  Therefore seam and run agree literally on source
darts, edge roots, crossed-resolution choice, side roots, support transport,
cap/route and fixed-order marks.

### Independent finite certificate

A fresh Wolfram enumeration gives exactly `120` ordered nonbacktracking
four-pivot cells.  In all `120`, `z,w` are distinct intersecting roots and the
pairing-weight pattern is `(0,2,2)`.  The normal-form proof above is the
mathematical proof; the enumeration verifies exhaustion.

---

## 4. Consecutive switches and identity subdivision

Two genuine switch cells may share one history vertex.  Replace that time
vertex by two identical copies joined by an identity interval carrying the same
complete state.  This changes no source graph, root/atom, cap, route, support,
side or mark datum and creates no new singular branch.  The two seam collars can
then be chosen with disjoint interiors.

A zero-width coefficient-neutral interval is not treated as a new switch.  It
is an identity subdivision, a retained repeated-state interval inside a full
run, or a literal complete-state involution digon.

---

## 5. Two-seam reduced-skeleton backtrack repair

Suppose the reduced run skeleton contains

\[
s\to t\to s.
\]

This means physically:

1. one genuine switch from an `s`-run to a `t`-run;
2. one maximal constant-`t` carrier already rootified by its unique nonpivot
   history;
3. a second genuine switch from that `t`-run to an `s`-run.

The two switch states may both project to the Petersen edge `{s,t}`, but they
are two distinct source occurrences with their own immediate neighbours.  The
first has

\[
\{s,x\}\to\{s,t\}\to\{t,y\},
\]

and the second

\[
\{t,x'\}\to\{t,s\}\to\{s,y'\},
\]

with the four required inequalities.  Hence both are legal six-port seam cells.

Place one seam at each switch, cut along both, replace the entire physical
middle `t`-run by its identity strip, and glue on literal complete endpoint
states.  This erases the corridor without:

- deleting an abstract `abba` word;
- contracting a Type-T subgraph;
- assuming the two switch moves are inverse;
- forgetting arbitrary side attachments.

---

## 6. Closed and normalized-open assembly

Place a disjoint seam at every genuine maximal-run boundary.  After cutting,
every residual singular component is a constant-pivot interval and is replaced
by its identity strip.

- A closed track with no switch is the closed identity product of its unique
  run history.
- A closed track with switches glues all seam collars and run strips to a
  root-valued cylinder.
- An open track whose two short sides are root-normalized or accepted glues to a
  root-valued rectangle fixing all four complete sides.
- If one endpoint is unresolved, all interior cells are consumed but that
  endpoint remains an explicit obligation; it is not silently called root.

The construction is independent of pivot-walk length, repetitions, parity and
simple-cycle classification.

---

## 7. Periodic track theorem in its exact scope

If the same complete unresolved endpoint state occurs twice in an already
constructed finite fixed-order comparison, identify the two collars.  The
singular arc closes to an internal track.  The closed theorem gives a connected
root-valued history cylinder.  Its legal `1`-skeleton is connected because a
higher cell attached along a connected boundary cannot join two previously
disconnected `1`-skeleton components.  A shortest path between the two boundary
subcomplexes is a simple root-valued crosscut.  Cutting along it gives a
root-valued rectangle and removes the two repeated unresolved endpoint
occurrences.

This theorem is a replacement theorem for a supplied repeated-endpoint
comparison.  It does **not** by itself prove that an arbitrary one-atom state
has a continuation, or that the root crosscut realizes a prescribed ordinary
parent topology.  Those are downstream scheduler obligations.

---

## 8. Supersession boundary

Retained for v7.2:

- one-atom uniqueness and local critical overlaps;
- complete nonbranching state walk;
- unique physical constant-run root history;
- local six-port seam;
- two-seam backtrack corridor;
- literal seam/run gluing;
- closed, normalized-open and supplied-periodic replacements.

Removed from the controlling path:

- the historical ambient six-port claim that one of four star matchings must be
  admitted by the original locked graph;
- the forced-backbone independent route-bit analysis beyond the narrow
  state-walk interface;
- R2.5 odd `C5/C9` exclusion;
- shortest Petersen-core extraction;
- `C6/C8` annuli;
- Type-T source contraction;
- mixed-order recurrence.

The local seam is a comparison-cell theorem with two already present root
restrictions.  It must not be confused with choosing a new six-port matching in
the original source graph.

---

## 9. Exact status boundary

Closed here:

- normalized full-state run/switch decomposition;
- physical run rootification retaining all attachments;
- state-walk versus reduced-skeleton indexing;
- all `120` six-port seam cases;
- two-seam treatment of every genuine reduced-skeleton backtrack;
- complete-state seam/run gluing;
- closed and normalized-open erasure;
- supplied repeated-endpoint crosscut.

Not closed here:

- construction of a finite continuation comparison from every arbitrary
  one-atom target-parent failure;
- proof that the periodic root short side realizes the prescribed parent
  topology rather than merely another root detour;
- a well-founded pure-NNI target scheduler;
- cap restoration, ordinary induction closure, or any established five-CDC
  theorem.
