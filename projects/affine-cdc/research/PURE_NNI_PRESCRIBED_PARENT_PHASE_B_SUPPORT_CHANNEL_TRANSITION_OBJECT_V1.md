# Prescribed-parent support-channel transition object

## Research Lead Phase B result v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-01`  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `61d6d7da706e858e10274d37e8d91dd51d4aaf33`  
**Parents:**

- `PURE_NNI_PRESCRIBED_PARENT_STATE_INTERFACE_NORMAL_FORM_V1.md`;
- `PURE_NNI_PRESCRIBED_PARENT_PHASE_A_MINIMAL_AMBIENT_EMBEDDING_V1.md`;
- `INVERSE_DIPOLE_KEMPE_RESCUE_V1.md`;
- `ONE_CROSS_SINGULAR_FIXED_ROUTE_REDUCTION_V1.md`;
- `TEN_STATE_BOUNDARY_GRAPH_RIGIDITY_V1.md`;
- the root/zero/co-root NNI table and exact terminal ledger.

**Phase-B conclusion:** every prescribed-parent `(4,2,2)` state has an exact finite horizontal transition object. All nonlocked states admit a source-faithful fixed-order prescribed-parent realization after at most one crossed-root NNI, one legal closed support-component switch, and one parent NNI. The unique residual node is the already known oriented DDD full-channel lock. It is not removed by track erasure, periodic crosscuts, or finiteness. A fourteen-vertex prime complete state realizes this residual node.

No rank or universal escape theorem is claimed.

---

## 1. Normal form

By an `S_5` support permutation and an ordered relabelling of the four active darts, put

\[
(A,B,C,D)=(12,34,13,24).
\]

Let the prescribed parent matching be

\[
M_0=AB\mid CD.
\]

The two root-valued crossed matchings are

\[
M_1=AC\mid BD,
\qquad
M_2=AD\mid BC,
\]

with central roots

\[
r_1=23,\qquad r_2=14.
\]

The parent central value is

\[
A+B=C+D=Q_5.
\]

At the support-unordered ten-state level this boundary is exactly

\[
D_0=(2,1,1),
\]

whose bad route is `M_0` and whose two root routes are `M_1,M_2`.

---

## 2. Relevant support channels

The prescribed pair `A=12`, `B=34` is disjoint. The four roots intersecting both are

\[
\mathcal X(A,B)=\{13,14,23,24\}.
\]

For `h in mathcal X(A,B)`, both marked edges `A,B` lie in

\[
H_h=F_i\triangle F_j
\qquad(h=ij).
\]

A legal switch of one connected component `Z` of `H_h` translates every root on `Z` by `h`.

### Lemma 2.1 — separating-channel parent repair

If `A` and `B` lie in different components of `H_h`, switch the component containing exactly one of them. Then

\[
(A+h)+B=Q_5+h
\]

or

\[
A+(B+h)=Q_5+h.
\]

Because `h subset {1,2,3,4}`, the value `Q_5+h` is the complementary two-subset and hence a root.

The switch is a root-flow involution on the complete current closed graph. It preserves graph order, all unselected darts, and the labelled prescribed topology. After the switch, the ordinary NNI to `M_0` is root-valued and realizes the parent.

This is exactly the DDD horizontal rescue theorem read with the prescribed-parent obligation retained.

---

## 3. Why the other crossed sheet is part of the local macro

A channel may connect `A,B` in the current crossed closure but separate them after the root NNI between `M_1` and `M_2`.

The move

\[
M_1\longleftrightarrow M_2
\]

is always a legal root NNI for the fixed word because its two central values are `23` and `14`.

### Theorem 3.1 — crossed-sheet conjugated rescue

Suppose that on at least one of the two crossed root topologies there is an `h in mathcal X(A,B)` for which `A,B` lie in different `H_h` components. Then the prescribed parent is realized by the finite source movie

\[
\boxed{
\text{zero or one crossed-root NNI}
\longrightarrow
\text{one closed }H_h\text{-component switch}
\longrightarrow
\text{one root NNI to }M_0.}
\]

Every intermediate state is a root-valued connected cubic graph of the same order unless an exact route/category terminal occurs. The movie preserves the complete exterior dart identity and discharges the live parent obligation literally.

### Important exclusion

One must not replace the middle step by switching an open path in the complementary four-pole while leaving the cap unattached. Such a path switch is useful for reading the route, but an intermediate four-root word may have no root-valued two-vertex completion. The source movie above uses only a genuine closed component switch.

---

## 4. Exact finite transition object

Let `D_0^1` and `D_0^2` denote complete root states with boundary class `D_0`, current cap topology `M_1` or `M_2`, and live parent `M_0`.

Let `K_0` denote prescribed-parent success, and let `T` denote the disjoint union of all named route, `2/3/4`-cut and bounded terminals.

Let `L_0^lock` denote the complete-state condition:

> on both crossed sheets, for every `h in {13,14,23,24}`, the marked edges `A,B` belong to the same connected component of `H_h`, and no named terminal is present.

The controlling directed object is

```text
                          separating H_h component
                    +---------------------------------> K_0
                    |
D_0^1 <============> D_0^2
       crossed root NNI
                    |
                    +---------------------------------> T
                         exact route/category output

if every one of the eight sheet/channel tests is nonseparating:

D_0^1 <============> D_0^2  ------>  L_0^lock
```

The double arrow is one explicit root NNI and its inverse.

### Edge contracts

#### Crossed-sheet edge

- **source movie:** one labelled root `2--2` NNI;
- **boundary map:** fixed ordered word `(A,B,C,D)`;
- **parent obligation:** retained literally;
- **terminal:** exact NNI category output, if any.

#### Separating-channel edge

- **source movie:** one closed support-component switch;
- **boundary map:** exactly one of `A,B` is translated by `h`;
- **parent obligation:** its forced central value changes from `Q_5` to the root `Q_5+h`;
- **next move:** root NNI to the prescribed parent;
- **terminal:** route/profile escape or exact category output if the switch reads such a row.

#### Locked edge

- **source content:** all relevant components join the two marked edges;
- **boundary map:** switching a common component translates both marked values and preserves disjointness;
- **parent obligation:** remains nonroot;
- **meaning:** the state is the exact four-channel DDD lock of `INVERSE_DIPOLE_KEMPE_RESCUE_V1.md` and the `D_0` middle vertex of the fixed-route outer path
  \[
  L_0=C_1-D_0-C_2.
  \]

No coefficient-only transition is present.

---

## 5. Relation to the ten-state route graph

For prescribed route `M_0`, the cap-compatible states are

\[
K_0=\{B_1,B_2,D_1,D_2\}.
\]

The witness belongs to

\[
L_0=\{C_1,D_0,C_2\}.
\]

The exact labelled challenge rows say:

- a non-`M_0` physical route from `D_0` enters `K_0` and is parent success;
- an `M_0` route remains in `L_0`;
- at `D_0`, the two `M_0` targets are `C_1,C_2`;
- the `M_0` rows at either endpoint return to `D_0`.

Therefore the support-channel object above is precisely the labelled root-level lift of the finite path `C_1-D_0-C_2`, with `K_0` as the successful outside sector.

Finiteness of this path does not force an edge to `K_0`.

---

## 6. Repair of the twelve-vertex Phase-A witness

In the twelve-vertex state of the Phase-A dossier, the complementary four-pole has, for `h=14` and `h=23`, the outside matching

\[
AD\mid BC=M_2.
\]

On the current `M_1` closure each corresponding `H_h` is one Hamilton cycle and no one-switch repair is visible.

Perform the crossed root NNI

\[
M_1\to M_2.
\]

On the `M_2` closure the outside `AD` path and the cap `AD` connection form one closed `H_{14}` component, while the `BC` path forms the other. Switch the `AD` component. Exactly `A` among `A,B` is translated by `14`, so the parent central value becomes

\[
Q_5+14=23.
\]

The final NNI to `M_0` is root-valued.

Thus the smallest prime ambient witness is not locked; it is repaired by Theorem 3.1.

---

## 7. A complete prime full-channel lock

The residual node is nonempty. Let `V={0,...,13}` and define the cubic graph

\[
\begin{aligned}
E(G_{14})=\{&05,06,07,
18,1\,10,1\,11,
24,25,29,\\
&39,3\,11,3\,13,
47,4\,10,
58,
6\,12,6\,13,
7\,11,
8\,12,
9\,12,
10\,13\}.
\end{aligned}
\]

Assign roots

\[
\begin{array}{c|c@{\quad}c|c@{\quad}c|c}
05&23&06&13&07&12\\
18&24&1\,10&23&1\,11&34\\
24&23&25&24&29&34\\
39&14&3\,11&24&3\,13&12\\
47&13&4\,10&12&58&34\\
6\,12&12&6\,13&23&7\,11&23\\
8\,12&23&9\,12&13&10\,13&13.
\end{array}
\]

Every vertex carries a root triangle.

Take active vertices `0,5` and ordered boundary

\[
A=07=12,\quad B=58=34,\quad C=06=13,\quad D=52=24.
\]

The current topology is `M_1=AC|BD`; the other crossed topology is `M_2=AD|BC`; the prescribed parent is `M_0=AB|CD`.

Both crossed graphs and the prescribed-parent graph are connected, simple, bridgeless, cubic, girth five, and have cyclic edge-connectivity five.

### Four channel certificate

In the complementary four-pole the relevant paths are:

\[
\begin{array}{c|c}
h&\text{component containing }A,B\\
\hline
13&A-7-11-1-10-4-2-9-3-13-6-12-8-B\\
14&A-7-4-10-13-3-11-1-8-B\\
23&A-7-4-10-13-3-11-1-8-B\\
24&A-7-11-1-10-4-2-9-3-13-6-12-8-B.
\end{array}
\]

For `14` and `23`, the remaining selected ports form the second path `C-6-12-9-2-D`. Thus every relevant channel has physical matching `AB|CD=M_0`: the marked edges are locked together.

No horizontal separating switch exists on either crossed sheet.

### Finite horizontal SCC certificate

Close the same complementary four-pole by `M_1` or `M_2`. Enumerate states generated by:

1. every closed connected support-component switch for each of the ten roots `h`;
2. the active root NNI `M_1<->M_2` whenever root-valued.

Starting from the displayed flow, the connected labelled state component has exactly

\[
240
\]

states:

- `120` on `M_1`;
- `120` on `M_2`.

Every state has support-unordered active boundary class exactly `D_0`. No state has a root value on `M_0`. All generating edges are involutions, so the component is a strongly connected component of the horizontal transition object.

This finite certificate may be reproduced by storing the ordered edge-root assignment, applying every component switch, applying the active crossed NNI, and hashing the complete labelled state. It uses no graph isomorphism quotient.

### Scope

The `240`-state SCC is closed under the complete horizontal alphabet of this dossier. It is not asserted closed under arbitrary root NNIs elsewhere in the ambient graph. Such moves are the Phase-C frontier.

---

## 8. Atom and track moves do not enlarge the horizontal conclusion

Representing the failed parent as one `Q_5` atom gives crossed sheets `M_1,M_2`. The state-walk seam/run theorem can erase a supplied singular comparison between them, but it fixes the active four-root boundary. It therefore remains inside the `D_0` horizontal SCC.

A periodic crosscut likewise gives a root detour between crossed sheets without changing the parent sum `Q_5`.

Hence:

- atom transport is a bookkeeping realization of edges inside the object;
- track erasure proves coherence of supplied histories;
- neither supplies the missing edge from `L_0^lock` to `K_0`.

---

## 9. Complete Phase-B output

Every complete witness state enters exactly one of:

1. **prescribed-parent repair:** Theorem 3.1;
2. **named route/cut/bounded terminal:** the exact terminal ledger;
3. **oriented DDD full-channel lock:** `L_0^lock`.

The first two are complete source movies/consumers. The third is represented by a nonempty finite horizontal SCC and is the sole Phase-C input.

No strict rank has been exhibited on the locked node.

---

## 10. Assurance boundary

### Exact here

- four-channel separating-switch algebra;
- crossed-sheet conjugated rescue;
- source movie and boundary map of every horizontal edge;
- ten-state identification of the residual node;
- repair of the twelve-vertex witness;
- explicit fourteen-vertex prime full-channel lock;
- complete `240`-state horizontal SCC certificate.

### Still open

- whether arbitrary ambient root NNIs force route/cut/bounded escape from every complete full-channel lock;
- whether a pure fixed-order source movie realizes the prescribed parent from the locked node;
- whether the arbitrary-flow first-cancellation proposition must be changed.

### Not claimed

- a full fixed-order SCC under arbitrary root NNIs;
- a counterexample to cap restoration or five-CDC;
- a rank;
- Lean, Curator, manuscript, release or publication status.
