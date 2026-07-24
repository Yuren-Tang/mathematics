# Prescribed-parent Phase A/B controlling correction

## Research Lead correction v2

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-01`  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `7ee2e9df2c79f5ef6ad179cfd148f6a84c2edbd3`  
**Controls with:** `PURE_NNI_PRESCRIBED_PARENT_STATE_INTERFACE_NORMAL_FORM_V1.md`.

**Supersedes for controlling use:**

- the all-sheet primeness/minimality claim in
  `PURE_NNI_PRESCRIBED_PARENT_PHASE_A_MINIMAL_AMBIENT_EMBEDDING_V1.md`;
- the fourteen-vertex prime-lock and nonterminal `240`-state certificate in
  `PURE_NNI_PRESCRIBED_PARENT_PHASE_B_SUPPORT_CHANNEL_TRANSITION_OBJECT_V1.md`;
- the reduction of the horizontal residual to the four initially displayed
  cross channels.

The old files remain historical append-only records.  Their valid local algebra
and source movies are retained only where explicitly restated below.

**Corrected classification:** `PHASE A COMPLETE WITH A MINIMAL ALL-THREE-TOPOLOGY PRIME EMBEDDING / PHASE B COMPLETE HORIZONTAL OBJECT / AMBIENT PURE-NNI ESCAPE STILL OPEN`.

---

## 1. Two certificate corrections

### 1.1 The twelve-vertex graph

The twelve-vertex flow in the Phase-A v1 dossier correctly has:

- a prime current topology;
- a prime prescribed-parent topology;
- the ordered word `(12,34,13,24)`;
- no one-switch parent realization on its current crossed sheet;
- the stated finite repair after changing crossed sheet.

It is not an all-sheet prime state.  For its other crossed pairing
`AD|BC`, the labelled reattachment obtained by swapping `06` with `2-11`
has the two four-cycles

\[
0-2-10-3-0,
\qquad
4-5-6-11-4.
\]

The equivalent labelled realization obtained by swapping `03` with `4-11`
has

\[
0-4-5-6-0,
\qquad
2-10-3-11-2.
\]

Each four-cycle has a cyclic complementary shore, hence gives a cyclic
four-cut.  Therefore this graph cannot certify a terminal-free complete state
when the alternative crossed-sheet category is part of the state interface.
Its explicit repair remains valid, but its all-sheet primeness claim is
withdrawn.

### 1.2 The old fourteen-vertex lock

For the graph `G_14` displayed in Phase-B v1, the current and prescribed-parent
topologies are prime, but both labelled realizations of `AD|BC` have cyclic
four-cuts.

For the `C-D` reattachment one shore is

\[
\{0,2,4,7\},
\]

with four-cycle `0-2-4-7-0`; the complementary shore contains the cycle

\[
3-11-1-10-13-3.
\]

For the `A-B` reattachment one shore is

\[
\{0,6,8,12\},
\]

with four-cycle `0-6-12-8-0`; the complementary shore contains

\[
1-11-7-4-10-1.
\]

Thus the claimed `240`-state horizontal orbit on that graph is not a
nonterminal SCC of the v7.2 complete-state transition system: the crossed-sheet
edge already reaches a named cyclic-four-cut consumer.  Its coefficient orbit
may still contain `240` states, but it is not a valid prime locked certificate.

---

## 2. Complete support-pair trichotomy at a live co-root parent

Let the prescribed parent have marked boundary roots `A,B` with

\[
A+B=Q_m,
\]

where `Q_m=[5]\setminus\{m\}`.  Then `A,B` are disjoint roots partitioning
`Q_m`.  Let `h` range over the ten support pairs.

Exactly one of the following occurs.

### 2.1 Neutral pairs: two choices

If

\[
h=A\quad\text{or}\quad h=B,
\]

neither marked edge is active in `H_h=F_i\triangle F_j`.  A closed component
switch preserves `A+B=Q_m`.  It may change `C,D`, the crossed sheet, and later
component attachments, so it is a genuine transition rather than a deleted
self-loop.

### 2.2 Missing-index migration: four choices

For each `j\ne m`, put

\[
h=mj.
\]

Exactly one of `A,B` contains `j`, and exactly one of `C,D` contains `j`.
Consequently `H_{mj}` has exactly two active local exterior darts.  The unique
physical component meeting those darts may always be switched source-faithfully.
The marked parent sum becomes

\[
\boxed{Q_m+mj=Q_j.}
\]

Thus the operation does not yet rootify the parent; it migrates the missing
support index from `m` to `j`.  At the boundary-trace level it exchanges the
empty trace with the trace carrying `j`.

This transition is present in every complete state and was absent from the
controlling Phase-B v1 diagram.

### 2.3 Rescue/lock pairs: four choices

The remaining four roots contain one support of `A` and one support of `B`.
Both marked edges are active.

- If they lie in different `H_h` components, switch the component containing
  exactly one marked edge.  Then
  \[
  Q_m+h
  \]
  is the complementary root and the prescribed parent NNI succeeds.
- If they lie in one component, switching that component changes both marked
  roots and preserves the co-root parent defect.  The complete attachment and
  route data must be updated and the ten-pair trichotomy repeated.

Hence the exact count is

\[
\boxed{10=2\text{ neutral}+4\text{ migration}+4\text{ rescue/lock}.}
\]

An initial four-channel lock is only a one-step obstruction.  A complete
horizontal lock must remain closed after every neutral switch, every
missing-index migration, every crossed-sheet NNI, and every newly exposed
rescue test.

---

## 3. Corrected minimal Phase-A embedding: the Heawood state

Let `G_H` be the labelled Heawood graph on vertices `1,...,14` with edges

\[
\begin{aligned}
E(G_H)=\{&12,16,1\,14,23,2\,11,34,38,45,4\,13,56,5\,10,67,\\
&78,7\,12,89,9\,10,9\,14,10\,11,11\,12,12\,13,13\,14\}.
\end{aligned}
\]

Use active edge `12` and ordered exterior darts

\[
A=16,
\qquad B=23,
\qquad C=1\,14,
\qquad D=2\,11.
\]

The current topology is `AC|BD`, the other crossed topology is `AD|BC`, and
the prescribed parent is `AB|CD`.

### 3.1 Complete root flow

Assign

\[
\begin{array}{c|c@{\qquad}c|c@{\qquad}c|c}
12&23&16&12&1\,14&13\\
23&34&2\,11&24&34&13\\
38&14&45&12&4\,13&23\\
56&13&5\,10&23&67&23\\
78&24&7\,12&34&89&12\\
9\,10&13&9\,14&23&10\,11&12\\
11\,12&14&12\,13&13&13\,14&12.
\end{array}
\]

Every vertex carries one root triangle.  At the active cell,

\[
(A,B,C,D)=(12,34,13,24),
\qquad
AC=23,
\qquad
AD=14,
\qquad
AB=Q_5.
\]

### 3.2 Complete topology/category certificate

Direct labelled subset enumeration gives:

\[
\begin{array}{c|c|c|c}
\text{topology}&\text{girth}&\text{cyclic edge connectivity}&
\text{number of minimum shore pairs}\\
\hline
AC|BD&6&6&28\\
AD|BC&5&5&5\\
AB|CD&5&5&5.
\end{array}
\]

All three are connected, simple, loopless, bridgeless and cubic.  No route,
cyclic `2/3/4`-cut or bounded category terminal is present.

### 3.3 Cap and route/profile field

Take cap vertices `7,12`, cap edge `7-12=34`, and ordered cap darts

\[
67=23,\quad 78=24,\quad 11\,12=14,\quad 12\,13=13.
\]

The cap matching has common central root `34`.  The three matching weights are
`(2,4,2)`, so this is the cap-compatible `D_1` member of `K_0`.  The cap is
disjoint from the active cell and is fixed by both active reattachments.

### 3.4 Support-component attachment field

On the current sheet the components meeting active darts have lengths

\[
\begin{array}{c|cccccccccc}
h&12&13&14&15&23&24&25&34&35&45\\
\hline
\text{length}&14&14&14&12&14&14&12&14&12&6\\
\text{active darts}&CD&AB&ABCD&AC&ABCD&AB&AD&CD&BC&BD.
\end{array}
\]

On the other crossed sheet the corresponding lengths are

\[
14,14,14,13,14,14,11,14,11,7,
\]

with the same active-dart sets.  In particular the marked edges `A,B` are in
one component for every one of the four initial rescue roots on both crossed
sheets.  This is a genuine all-three-topology prime initial lock.

### 3.5 Minimality

The order `4,6,8,10` exclusions from the earlier Phase-A dossier remain valid.
For order `12`, an exact Wolfram `GraphData` census gives:

- `94` cubic graphs in total;
- exactly two connected girth-at-least-five graphs of cyclic edge connectivity
  at least five: `TriplexGraph` and `TwinplexGraph`;
- `36` active edges across those two graphs;
- no active edge for which both nontrivial labelled `2--2` reattachments are
  prime.

The exact outcome table is

\[
19\text{ edges with }(\mathrm{nonprime},\mathrm{nonprime}),
\qquad
17\text{ with }(\mathrm{prime},\mathrm{nonprime}),
\qquad
0\text{ with }(\mathrm{prime},\mathrm{prime}).
\]

Since cubic order is even, the displayed order-fourteen Heawood state is a
smallest all-three-topology prime ambient realization of the prescribed-parent
witness.

---

## 4. Valid `240`-state horizontal SCC

Close the same complementary four-pole by either crossed topology and generate
states using:

1. every connected closed `H_h`-component switch for all ten roots `h`;
2. the active crossed root NNI whenever root-valued.

Starting from the displayed Heawood flow, exact labelled enumeration gives one
component of

\[
\boxed{240=120+120}
\]

states:

- `120` on `AC|BD`;
- `120` on `AD|BC`;
- `120` distinct ordered `D_0` boundary words;
- parent central weight exactly four in all `240` states;
- matching-weight pattern exactly `(2,2,4)` in all states;
- no prescribed-parent root state;
- no route/cut/bounded category exit, because both crossed topologies and the
  parent topology are prime independently of the flow.

All generators are involutions.  This is therefore a genuine horizontal
strongly connected component, unlike the invalid Phase-B v1 graph.

It proves that support switching, missing-index migration, active-sheet change,
track erasure and finiteness do not by themselves establish prescribed-parent
realization.

---

## 5. The horizontal SCC is not a full counterexample

One source-faithful ambient root NNI breaks the displayed Heawood SCC.

Perform the NNI at edge `3-8`, swapping branch edges `2-3` and `8-9`:

\[
23,89\longmapsto 28,39,
\qquad
\lambda(38):14\longmapsto23.
\]

The output topology is still connected, simple, bridgeless, girth five and
cyclically five-edge-connected.  Then:

1. perform the active crossed NNI `AC|BD -> AD|BC`, changing the active central
   root `23 -> 14`;
2. switch the closed `H_{14}` component with edge set
   \[
   \{16,2\,11,34,45,56,39,9\,10,10\,11\};
   \]
3. the active boundary changes from
   \[
   (12,34,13,24)
   \quad\text{to}\quad
   (24,34,13,12),
   \]
   so the prescribed parent central value is the root `23`;
4. perform the root NNI to `AB|CD`.

Thus the valid horizontal SCC has an explicit ambient pure-NNI escape.  It is
not closed under the complete fixed-order alphabet and is not a graph/source
counterexample to v7.2.

---

## 6. Correct Phase-A/B disposition

### Phase A

Complete: the Heawood state is a smallest connected loopless bridgeless
all-three-topology prime ambient embedding with all source, dart, cap, route,
support-component, sheet and category data.

### Phase B

Complete at the exact horizontal level:

- the ten support pairs have the `2+4+4` transition trichotomy;
- all nonlocked states have the explicit separating-switch parent movie;
- missing-index migration is an indispensable state transition;
- a valid `240`-state all-index horizontal SCC exists;
- the displayed SCC has an explicit ambient root-NNI escape.

### Remaining boundary

No theorem yet proves that every complete horizontal SCC has such an ambient
escape or a named terminal.  No strict rank is defined.

---

## 7. Assurance boundary

### Exact authorial content

- explicit correction of both invalid crossed-sheet prime claims;
- complete support-pair trichotomy and defect migration identity;
- minimal Heawood all-three-topology prime state;
- exact order-twelve graph census;
- valid `240`-state horizontal SCC;
- explicit ambient-NNI escape movie for that SCC.

### Still required

- independent reproduction of the finite graph/flow/SCC censuses;
- a universal ambient pure-NNI escape or a full closed SCC counterexample;
- PDL reconstruction of any eventual repair.

### Not claimed

No v7.2 closure, five-support theorem, five-CDC theorem, Lean theorem, Curator
movement, manuscript, release, tag, arXiv, DOI or publication status is asserted.
