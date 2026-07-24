# AC-PD-5CDC v7.2 — first-cancellation synchronization and arbitrary-flow single pop

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Frozen research input:** `research/affine-cdc-five-cdc-v1@094ca09f6d3982b785a3f3428d9ec079dbba0855`  
**Classification:** `COMPLETE-DRAFT THROUGH THE SINGLE POP / PURE-NNI RETURN SEPARATE`.

This dossier independently reconstructs the part of the v7.2 route from one
specified root flow on the valid cross closure through the first cancellation
and the unique inverse pop.  It uses ordinary lower-order existence only on the
actual smaller target cap closure.  It does not use a witnessed `Q_n`, a child
history, a mixed-order call graph, `M_N`, `d_N`, a bubble, or a terminal frame.

---

## 1. Parallel cap context

Let `P_0` be the ordered four-pole obtained by deleting the endpoints of one
simple edge of the order-`N` target graph.  Let `C_i` be the original cap and
`E_j`, `j != i`, one valid cross reconnection.  Write

\[
\widehat G_0=P_0\cup C_i,
\qquad
G_{j,0}=P_0\cup E_j.
\]

Fix one specified root-valued `E_5` flow `lambda_0` on `G_{j,0}`.  The target
closure `widehat G_0` is a graph topology only; no target flow is assumed.

The independently reconstructed ten-state table gives

\[
\Sigma(E_j)=J_j=\{A,B_j,C_j\},
\qquad
J_j\cap K_i=\{B_j\}.
\]

Thus:

1. `B_j` glues the original cap immediately;
2. a separating equality or DDD channel gives the ordinary horizontal rescue;
3. otherwise the current root flow lies in one fixed-route equality or DDD lock,
   and every nonescaping challenge is routed by the original cap matching `M_i`.

Only Case 3 remains below.

---

## 2. Target-synchronized monotone prefix

At stage `r` retain the same ordered exterior semiedges and the parallel pair

\[
G_{j,r}=P_r\cup E_j,
\qquad
\widehat G_r=P_r\cup C_i.
\]

The cross graph carries the current root flow `lambda_r`; the target graph need
not carry a flow.  If an equal adjacent root-triangle pair is already present,
stop.  Otherwise the audited equality/DDD Morse theorem supplies a strictly
potential-lowering root `2--2` NNI on `G_{j,r}`.

Apply the same uncoloured local topology replacement to `widehat G_r`.

### Cross side

The selected move is root-valued, hence the new cross graph is connected,
loopless and bridgeless unless a named bounded/category exit is exposed.  In the
internal branch it carries the transported specified root flow.

### Target side

The target test is topological.  Deleting the two NNI vertices leaves four
ordered branch incidences.  If the new target central edge is a bridge, the
exterior partition is the new pairing; placing the old two vertices on the
opposite shore exhibits a two-edge cut in the current target.  Endpoint
coincidences give the named loop/parallel/triangle/low-port bounded branches.
Thus exactly one of:

1. the parallel target NNI is connected, loopless, bridgeless and cubic;
2. the current target has a cyclic two-cut;
3. the current target has a bounded acyclic/parallel/low-port degeneration.

Cases 2--3 are current-target terminals and are not continued as source moves.

### Route test

Before the first route change the ordered four-root boundary word is unchanged.
The exact route rows show that every route away from `M_i` from the two blocked
outer components lands in `K_i`.  Such a descendant state is a root flow on the
current target cap closure and is a terminal input for the later pure-NNI
return.

An accepted internal step therefore consists exactly of:

\[
\boxed{
\text{route-preserving root NNI on the cross flow}
+
\text{valid parallel target NNI}.}
\]

Every accepted equality step strictly lowers `(E,Phi)` and every accepted DDD
step strictly lowers `Omega`.  These are nonnegative integers at fixed order.
The no-local-minimum theorem says that if no equal adjacent pair is present,
another lowering root NNI exists.  Hence the accepted prefix is finite and ends
at a route/category terminal or at the first equal-face pair.

### Pure-prefix theorem

Immediately before the first cancellation the accumulated source word contains
only internal root-valued `2--2` NNIs.  It contains no cancellation, support
switch, order change, zero/co-root edge, child call, genealogy frame, or second
independent discrepancy.  Every parallel target along it is connected,
loopless, bridgeless and cubic.

---

## 3. First-cancellation target disposition

Cancel the first equal-face pair in the cross flow and write

\[
G_j^-=P^-\cup E_j,
\qquad
\widehat G^-=P^-\cup C_i.
\]

Both graphs have two fewer vertices than their parents.  The cancellation fixes
all four ordered outer semiedges, the cap index/block, the route record and all
exterior attachments.

### 3.1 Disconnected inherited cross output

Every component of the exterior after deleting the cancelled vertices contains
at least two local cancellation incidences.  If the root-valued cross output is
disconnected, there are two components with two incidences each.

- If one component contains zero or four outer terminal endpoints, its parent
  shore is attached through exactly two old edges: a two-cut.
- If it contains exactly two outer terminal endpoints, the corresponding parent
  target shore has four boundary edges.  It is a cyclic four-cut unless the
  shore is the explicit acyclic two-vertex cap.

Thus no disconnected child call is made: the current target is already a
2-cut, cyclic 4-cut, or bounded low-port terminal.

### 3.2 Connected cross output but invalid parallel target

Apply the three-reconnection category theorem at the cancelled target edge.
Either `widehat G^-` is connected, loopless and bridgeless, or the current
parent target already has a cyclic cut of size at most four or one explicit
loop/parallel/triangle/theta/acyclic/low-port degeneration.

### 3.3 Route change

The complete boundary word is preserved by cancellation.  If this is the first
route change, the exact route row is in `K_i`; gluing `C_i` gives a supplied root
flow on `widehat G^-`.

### 3.4 Genuine smaller target

In the remaining branch

\[
\widehat G^-
\]

is connected, loopless, bridgeless, cubic and has order `N-2`.  Ordinary strong
induction applies directly to this target closure and supplies one arbitrary
root flow `nu` on it.  No relation between `nu` and the inherited cross flow is
needed or asserted.

This is the only graph-order descent in v7.2.

---

## 4. Source-level arbitrary-flow inverse pop

Let `a,b` be the roots on the two stored cancellation-output lineages under the
supplied flow on `widehat G^-`.  Split those lineages and restore two labelled
vertex slots.  The complete exterior dart boundary is fixed in every row.

### 4.1 Distinct intersecting roots

If `a != b` and `a cap b != empty`, the central value `a+b` is a root.  The
literal original equal-face insertion is root-valued and recreates the required
predecessor topology.

### 4.2 Equality row

If `a=b`, borrow one adjacent root vertex with other roots `d,e`, so `a=d+e`.
On five ordered leaves

\[
A=B=C=a,\qquad D=d,\qquad E=e,
\]

the alternative topology

\[
T_3=AE\mid C\mid BD
\]

has internal roots `d,e`; its three vertices all carry the root triangle
`{a,d,e}`.  The first two vertices are an equal-face pair.  Cancelling them
reconnects the exact old direct `a` lineage and the exact `e` dart of the
borrowed vertex.  Hence `T_3` is one legal root-valued inverse insertion from
the current smaller graph, not a recolouring through a zero state.

### 4.3 Good doubled-disjoint row

Let `a perpendicular b`, borrow an adjacent `a`-vertex with `a=d+e`, and use

\[
A=b,\quad B=a,\quad C=b,\quad D=d,\quad E=e.
\]

After support normalization `a=12`, `b=34`, every decomposition has
`d=1k`, `e=2k`, `k in {3,4,5}`.  For `k in {3,4}`, `b` intersects `e` and

\[
T_3=AE\mid C\mid BD
\]

is fully root-valued.  Its left and middle vertices have the same triangle
`{b,e,b+e}`.  Cancelling that equal-face pair returns exactly the old direct
`b` lineage and the borrowed vertex `(a,d,e)`.  Thus the repair is a direct
root-valued alternative inverse insertion preserving all five ordered exterior
darts.

### 4.4 Missing-index doubled-disjoint row

The unique remaining normalized case is

\[
a=12,\quad b=34,\quad d=15,\quad e=25.
\]

On

\[
T_4=AE\mid D\mid BC
\]

the two non-root internal edges are

\[
Q_1=34+25,
\qquad
Q_5=12+34,
\]

and the middle root is `15`.  This is the ordered three-vertex source object

\[
(34,25,Q_1)
-
(Q_1,15,Q_5)
-
(Q_5,12,34).
\]

Perform the NNI on the `Q_1` edge which pairs `34` with `Q_5`.  Its new central
value is

\[
34+Q_5=12,
\]

a root.  The result is

\[
(34,Q_5,12)
-
(12,25,15)
\]

with the old right vertex `(Q_5,12,34)` still attached through `Q_5`.
Consequently exactly one co-root edge remains, namely the standard atom

\[
(Q_5,12,34)
-
(Q_5,34,12),
\]

while the other new vertex is the root triangle `(12,25,15)`.  The NNI fixes
all five exterior dart slots and all cap/route/support data.  A category failure
of this NNI is precisely the named two-cut or bounded branch.

Thus the missing-index row has a complete source-level normalization to one
standard co-root atom; there is no hidden second persistent atom.

### 4.5 Local identifications

A borrowed dart coincidence, loop, parallel edge, insufficient ordinary
neighbourhood, or separator is not folded into the generic row.  It is returned
as the exact current-target bounded/two-cut/low-port terminal.

### Single-pop theorem

Every arbitrary root flow on the actual smaller target cap closure produces,
after exactly one inverse cancellation pop, exactly one of:

\[
\boxed{
\begin{array}{c}
\text{a root-valued same-order contextual state},\\
\text{one standard co-root atom on a same-order contextual state},\\
\text{an exact current-target terminal}.
\end{array}}
\]

Only the intersecting row is necessarily the literal predecessor topology.
The equality, good-disjoint and missing-index rows may be neighbouring
five-leaf topologies with the same complete exterior boundary and the required
predecessor topology stored as target.

---

## 5. Independent finite certificates

A fresh Wolfram enumeration over the ten weight-two roots gives:

- `180` ordered doubled-disjoint borrowing data `(a,b,d,e)` with
  `a perpendicular b`, `d+e=a`;
- `120` good cases where the common index of `d,e` lies in `b`;
- `60` missing-index cases;
- the two classes partition all `180` cases.

No extra coefficient row occurs.  The human proof above uses the `S_5` normal
form and the explicit ordered source NNI; the enumeration is only an exhaustive
check.

---

## 6. Exact status boundary

Closed here:

- root-NNI-only strict prefix;
- target synchronization at every accepted root NNI;
- finite arrival at route/category exit or first cancellation;
- all first-cancellation target/cross category branches;
- ordinary lower `P` applied to the actual target closure;
- all arbitrary-flow single-pop rows;
- source-level missing-index two-co-root normalization;
- one-atom and same-order output bound.

Not closed here:

- fixed-order target normalization after the single pop;
- proof that an unresolved one-atom parent obligation reaches its prescribed
  parent topology rather than another root detour;
- final terminal census and ordinary induction synthesis;
- independent audit or any established five-CDC claim.
