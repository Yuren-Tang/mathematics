# Pure-NNI prescribed-parent state/interface normal form

## Research Lead Phase 0 dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-01`  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `094ca09f6d3982b785a3f3428d9ec079dbba0855`  
**PDL obstruction consumed:** `proof-development/affine-cdc-rigour-v1@698bcf752b637ba0ac31d4d0e8b348ed6eaf79aa`

**Purpose:** fix the exact complete state and interface manipulated by issue `research-workbench#74`. This is not a history of AffineCDC and does not assert a repair. It prevents four distinct statements from being conflated:

1. existential root solubility of a graph;
2. witnessed transport of one supplied flow;
3. erasure of a supplied singular track;
4. realization of one prescribed ordinary parent topology.

No rank is defined here.

---

## 1. Exact proposition and quantifiers

Fix an integer `N` and a stored pure-`2--2` source prefix

\[
C_0\longrightarrow C_1\longrightarrow\cdots\longrightarrow C_\ell,
\]

where every `C_j` is a labelled connected loopless bridgeless cubic cap-context graph of order `N`, with common ordered exterior cap block and complete dart ancestry.

At the first cancellation below `C_\ell`, let

\[
H
\]

be the actual connected loopless bridgeless child **target cap closure** of order `N-2`. Ordinary lower-order existence supplies an arbitrary root flow

\[
\nu:E(H)\to R_5.
\]

The word **arbitrary** means that no path from the inherited child cross flow to `nu` is supplied or required.

Apply the exact inverse-cancellation table once. The result is one order-`N` complete state `S_0` whose current source topology may differ from `C_\ell`, while the prescribed predecessor target remains

\[
\operatorname{par}(S_0)=C_\ell.
\]

### Proposition `PP_N(C_\ell,S_0)`

For every such supplied `nu` and every resulting nonterminal single-pop state `S_0`, construct a finite source-faithful same-order history in the declared fixed-order alphabet which ends in exactly one of:

1. **prescribed-parent success:** a root flow on the labelled topology `C_\ell`, with the stored dart identity needed to cross the next prefix edge;
2. **strict prefix progress:** the prescribed parent has been realized and the source-prefix index changes from `ell` to `ell-1` by crossing that actual stored source NNI;
3. **named terminal:** one exact route/profile, cyclic `2/3/4`-cut, bounded low-port, theta, loop, bridge, parallel, or outer-shell consumer, carrying the identity map back to the stored prefix.

An unresolved recurrent complete-state component is not a conclusion of `PP_N`; it is a blocker or counterexample to the proposed repair.

### Existential versus witnessed statements

- `P_{N-2}(H)` supplies only existence of `nu` on `H`.
- The single inverse pop is witnessed locally from the actual values of `nu` on two stored lineages.
- Every subsequent same-order move must be witnessed on the current order-`N` source state.
- A proof that `C_\ell` has some unrelated root flow is insufficient unless the proof constructs it from the allowed current interface or enters a named terminal whose consumer legitimately chooses a new lower-order flow.

---

## 2. Minimal complete state tuple

A fixed-order prescribed-parent state is

\[
\boxed{
S=(N,G,\delta,\lambda,\chi,P,\mathfrak B,\kappa,\mathscr H,\mathfrak a,\tau,\alpha).
}
\]

### 2.1 `N` — literal graph order

`N=|V(G)|`. It is fixed throughout the pure-NNI phase.

### 2.2 `G` — labelled current source topology

`G` records:

- labelled cubic vertices;
- every edge and semiedge;
- the active two-vertex NNI neighbourhood when present;
- the complete incidence relation.

Graph isomorphism without the labels below is not state equality.

### 2.3 `delta` — ordered dart and exterior-slot data

`delta` records:

- both darts of every internal edge;
- ordered exterior darts of each local four-/six-port interface;
- the identity of cap darts and prefix-surviving darts;
- local vertex slots used by a prescribed NNI or support switch.

### 2.4 `lambda` — current coefficient assignment

`lambda` assigns to every current edge one of:

- a root in `R_5`;
- one permitted zero;
- one permitted co-root `Q_i`.

Every state is root-valued except for at most one normalized atom. Transient two-defect critical pairs are macro interiors, not state vertices.

### 2.5 `chi` — crossed-resolution sheet

When an atom is present, `chi` records its two crossed root resolutions and the currently selected side. In a root state it records the crossed topology from which the active parent obligation is being attempted, when relevant.

### 2.6 `P` — prescribed-parent obligation

`P` is a labelled cubic topology on the same vertex/dart set as `G`, together with the exact ordinary parent NNI pairing to be realized.

`P` is an obligation, not a claim that its central coefficient is a root. It survives auxiliary moves until discharged, replaced by an explicitly later prefix obligation, or terminated by a named consumer.

### 2.7 `mathfrak B` — cap block

`mathfrak B` records:

- the two original cap vertices when present;
- their ordered terminal incidences;
- the distinguished cap matching index;
- every dart identity required for cap gluing.

### 2.8 `kappa` — physical route/profile state

`kappa` records:

- the current ten-state boundary/profile class when defined;
- the physical matching used by each active complementary support-pair challenge;
- whether the cap-compatible sector `K_i`, fixed route `M_i`, or an exact route escape has been reached.

A coefficient transition without `kappa` is not a complete transition.

### 2.9 `mathscr H` — support-component attachment data

For every support pair `h=ij` read by an allowed switch, let

\[
H_h=F_i\triangle F_j.
\]

`mathscr H` records only the component data needed by the current finite interface:

- which active boundary darts lie in the same component of `H_h`;
- the physical terminal matching of that component relative to the active four-pole;
- whether it meets the cap block;
- the ordered outside attachment paths required to perform the switch source-faithfully.

The full historical route of an unrelated support component is not stored.

### 2.10 `mathfrak a` — atom position and orientation

If present,

\[
\mathfrak a=(e,Q_i,\{r_0,r_1\},\text{active side},\text{orientation}),
\]

with exact edge/dart position and the neighbouring cell in which continuation is attempted.

### 2.11 `tau` — graph-category and terminal flags

`tau` is exactly one of:

- `prime`: connected, loopless, bridgeless, cubic, no currently returned terminal;
- a named cyclic `2`-, `3`-, or `4`-cut with its shores;
- one named bounded loop/parallel/triangle/theta/acyclic low-port object;
- route/profile terminal;
- outer-shell loop/bridge/singleton-cut terminal.

A generic `separator` or `category-safe` flag is not permitted.

### 2.12 `alpha` — identity to the stored pure-NNI prefix

`alpha` maps every surviving current dart and cap incidence to its ancestor in `C_ell` and records the active prefix index. It is the data needed to splice a successful parent realization into the literal source prefix.

### Historical data which are not coordinates

The following are witnesses attached to transitions, not state coordinates:

- the lower child history before `nu` was chosen;
- genealogy words of completed bubbles;
- the path by which the same state was first reached;
- an uncoloured arborescence path not yet lifted root-valuedly;
- a van Kampen diagram chosen for a previous comparison;
- the number of times a state has occurred;
- any undefined distance or rank.

---

## 3. Prescribed-parent status field

For every state define

\[
\operatorname{obl}(S)\in
\{\text{live},\text{realized},\text{advanced},\text{terminal},\text{failed}\}.
\]

- `live`: `P` remains the exact next topology to realize.
- `realized`: `G=P` and `lambda` is root-valued.
- `advanced`: the stored source NNI has been crossed and `alpha` points to the next prefix obligation.
- `terminal`: `tau` has one named consumer.
- `failed`: a finite closed nonterminal transition component has been proved, or an algebraic impossibility remains with no boundary-changing move.

Merely changing `G` while retaining the same impossible parent boundary leaves `obl=live`.

---

## 4. Fixed-order move/macro contracts

### 4.1 Ordinary root NNI

**Reads:** `(G,delta,lambda,P,mathfrak B,kappa,tau,alpha)` and one labelled two-vertex neighbourhood.

**Precondition:** the new central value is a root and the output is in the prime category, or an exact category alternative is returned.

**Preserves:** `N`, exterior darts, cap identity, every coefficient outside the local cell, and `P` unless this is the prescribed parent edge.

**Writes:** local topology, local dart incidences, central root, support-component data touched by the move, and possibly `kappa`.

**Parent effect:**

- if the move is the prescribed parent NNI, `obl` becomes `realized`;
- otherwise `P` remains literally live and `alpha` is updated by the witnessed auxiliary source movie.

**Reversibility:** reversible when the inverse central value is root and no category/route exit intervenes.

**Terminal:** exact route, cut, or bounded output only.

### 4.2 Zero alternative

**Reads:** one failed parent/auxiliary NNI with forced old central value zero.

**Preserves:** `N`, exterior word, cap block, and live prescribed parent.

**Writes:** the other crossed root topology and sheet.

**Parent effect:** does not realize a fixed parent whose central value is still zero.

**Reversibility:** the local crossed-root involution is reversible.

### 4.3 One-atom continuation

**Reads:** `mathfrak a`, the adjacent root NNI/full-channel cell, complete darts, route and support attachments.

**Preserves:** `N`, cap identity, `P`, and all exterior data outside the bounded overlap.

**Writes:** atom position, missing index, crossed sheet, local topology, and affected `mathscr H`; after normalization at most one atom remains.

**Parent effect:** remains live unless the continuation returns a root state on `P`, advances the prefix, or enters a named terminal.

**Reversibility:** not assumed globally; each local source movie is explicit.

**Terminal:** exact route/cut/bounded row of the critical-overlap theorem.

### 4.4 Source-faithful support-component switch

**Reads:** a named component `K` of `H_h=F_i triangle F_j`, its complete attachment data in `mathscr H`, and the route/profile row.

**Preserves:** `N`, uncoloured topology `G`, all darts, cap-vertex identity, and the prescribed topology `P` as a labelled obligation.

**Writes:**

\[
\lambda(e)\mapsto\lambda(e)+h
\quad(e\in K),
\]

along with the boundary root word, support-component partitions, crossed sheet if affected, and `kappa`.

**Parent effect:** may change the boundary coefficients and thereby make the prescribed parent central value a root. This is the principal currently legal mechanism capable of breaking the `(4,2,2)` witness without changing graph order.

**Reversibility:** involutive on the same physical component.

**Terminal:** if the physical route changes to the cap-compatible sector or exposes an exact cut/bounded row, use that named consumer.

### 4.5 Seam/run replacement

**Reads:** one supplied finite nonbranching full-state track with normalized endpoints.

**Preserves:** all four labelled boundary sides, including any fixed four-root short-side word; exterior darts; cap; route; prescribed parent field.

**Writes:** only the internal history rectangle/cylinder, replacing singular cells by root seams and constant-run identity strips.

**Parent effect:** none unless a separate theorem identifies a new short side with a root state on `P`. Track erasure alone does not do so.

**Reversibility:** boundary-equivalence macro; no directed progress is inferred.

### 4.6 Periodic root crosscut

**Reads:** two repeated equal complete endpoint collars and a root-valued history cylinder.

**Preserves:** the endpoint boundary data and the live prescribed parent.

**Writes:** a root rectangle whose short side is one legal root history crosscut.

**Parent effect:** no prescribed-parent realization is implied. For a fixed impossible boundary word the crosscut can remain entirely in crossed root topologies.

**Reversibility:** not used as a rank edge.

### 4.7 Route/profile escape

**Reads:** exact `kappa`, supplied boundary roots and cap block.

**Writes:** `tau=route-terminal` and an actual root flow on the exact current descendant target after cap gluing.

**Parent effect:** the local obligation stops only through the named terminal consumer and its stored `alpha`; it is not silently identified with the original topology.

### 4.8 Cut/bounded exit

**Reads:** exact current graph, shores or bounded neighbourhood, boundary word and `alpha`.

**Writes:** one terminal tuple with the named `2/3/4`-cut or bounded consumer.

**Parent effect:** terminal.

### 4.9 Identity subdivision and literal gluing

**Reads:** two literally equal complete endpoint states.

**Preserves:** every coordinate.

**Writes:** only history-cell incidence.

**Parent effect:** none.

---

## 5. Proof-interface diagram

```text
lower P_(N-2) supplies arbitrary nu on actual child target H
                         |
                         v
               one exact inverse pop
                         |
                         v
       S0 = root / one-atom / named terminal
              |             |             |
              |             |             +--> exact consumer
              |             v
              |      fixed-order atom continuation
              |             |
              +-------------+
                         |
                         v
         complete state with live prescribed parent P
               /            |             \
              /             |              \
   boundary-changing    fixed-boundary     exact route/cut/
   source switch        seam/run/crosscut  bounded exit
          |                    |                  |
          v                    v                  v
 parent root / route      supplied track      terminal
 success / new state      erased only
          |                    |
          v                    v
 cross stored source NNI   UNRESOLVED if P remains non-root
          |
          v
 strict prefix progress
```

### Frozen v7.2 stopping point

The frozen source proves the single pop, local root/zero/co-root rows, supplied-track erasure, and terminal consumers. It stops at the arrow

\[
\text{fixed-order discrepancy}
\not\Rightarrow
\text{root state on prescribed }P.
\]

---

## 6. Invariant and non-invariant ledger

### 6.1 Genuine invariants of every nonterminal fixed-order move

- graph order `N`;
- identity of the cap vertices and stored prefix;
- the named prescribed-parent obligation until it is discharged;
- root-flow conservation at every ordinary vertex;
- at most one normalized persistent atom;
- complete exterior dart ancestry outside the active move.

### 6.2 Conditional invariants

- the four-root boundary word is preserved by an internal root NNI, seam/run replacement, periodic crosscut and identity gluing, but not by a support-component switch meeting its darts;
- the physical route is preserved only by moves certified route-preserving;
- graph-category primeness is preserved only on the prime branch of the exact category theorem;
- crossed sheet is preserved by selected run strips but may change under an atom or support macro;
- support-component partitions are preserved only by moves disjoint from the relevant support networks.

### 6.3 Non-invariants which may break the witness

- current source topology `G`;
- local four-root boundary coefficients under a legal support switch;
- support-component connectivity after an NNI;
- route/profile state under a component switch;
- atom position and missing index;
- crossed-resolution sheet.

### 6.4 Merely finite quantities

The following are finite but not known monotone:

- the number of labelled cubic topologies at order `N`;
- the number of root/one-atom assignments;
- uncoloured target-tree distance;
- atom-track length;
- number of support components;
- number of times a complete state repeats;
- size of a finite SCC.

Finiteness alone proves neither terminal reachability nor prescribed-parent success. No `rho_atom` or replacement rank is defined before a strict transition is exhibited.

---

## 7. Algebraic witness template

Fix ordered active boundary darts

\[
(a,b,c,d)
\]

with

\[
(A,B,C,D)=(12,34,13,24).
\]

The three binary pairings have central values

\[
\begin{array}{c|c}
AB\mid CD&Q_5=1234,\\
AC\mid BD&23,\\
AD\mid BC&14.
\end{array}
\]

The prescribed parent is

\[
P=AB\mid CD.
\]

### Fixed-word obstruction

For every state whose ordered boundary word remains exactly `(12,34,13,24)`, a root-valued realization of `P` is algebraically impossible because its central value is always `Q_5`.

Topology connectivity does not alter this equality. A root path between the two crossed states does not alter it either.

### Two current crossed source templates

#### Sheet `R_23`

- local pairing `AC|BD`;
- central root `23`;
- local root triangles `(12,13,23)` and `(34,24,23)`;
- parent atom would be `Q_5`;
- the two diagonal support-pair challenges are `h=23` and `h=14`.

#### Sheet `R_14`

- local pairing `AD|BC`;
- central root `14`;
- local root triangles `(12,24,14)` and `(34,13,14)`;
- parent atom would be `Q_5`;
- the same two diagonal support-pair challenges occur with the roles of the crossed sheets exchanged.

### Unspecified ambient fields

A complete Phase-A state must still choose:

1. `N` and the full labelled connected loopless bridgeless cubic graph `G`;
2. the four outside endpoints of `a,b,c,d` and all remaining darts;
3. a full root flow extending the displayed local triangles;
4. the cap block `mathfrak B` and its location relative to the active NNI;
5. the physical outer route/profile `kappa`;
6. for `H_14` and `H_23`, whether the two local paths lie in distinct components or one common component, and the outside terminal matching;
7. all other support-component attachments read by a legal switch;
8. whether a switch meets the cap and changes route;
9. the atom orientation/sheet if the parent attempt is represented as one co-root state;
10. exact absence or presence of cyclic `2/3/4`-cuts and bounded category outcomes;
11. the identity map `alpha` to the stored prefix topology.

A local four-root word without these fields is not a Phase-A nonterminal embedding.

---

## 8. Exact Phase-A finite problem

### Finite signature

For either crossed sheet, form the **witness completion signature**

\[
\Omega=(\varepsilon,\kappa,\pi_{14},\mu_{14},\pi_{23},\mu_{23},\beta,\tau,\alpha),
\]

where:

- `epsilon in {23,14}` is the current crossed central root;
- `kappa` is the labelled route/profile state;
- `pi_h` is the partition of the four active boundary darts induced by components of `H_h`;
- `mu_h` is the outside terminal matching and cap-incidence flag of the relevant component(s);
- `beta` is the ordered outside-endpoint coincidence pattern;
- `tau` is one exact prime/terminal category;
- `alpha` is the active prefix identity type.

The admissible values are finite: two sheets, three four-port matchings, finitely many set partitions, ten boundary profile classes, finite endpoint-coincidence types, and the named terminal ledger.

### Phase-A decision problem

Enumerate every algebraically and graph-topologically admissible signature `Omega` extending `(12,34,13,24)` and decide:

1. does one legal `H_14` or `H_23` component switch change the ordered boundary so that `AB|CD` has a root central value;
2. otherwise, does the exact route/category data force a named terminal;
3. otherwise, realize `Omega` by the smallest labelled connected loopless bridgeless cubic graph with a full root flow, fixed cap/route data and no named terminal.

The output is exactly one of:

- a theorem that every admissible signature is parent-rootifiable or terminal;
- one smallest complete nonterminal ambient embedding.

This is the sole Phase-A problem. No rank, generic connectivity theorem, or mixed-order recursion is part of it.

---

## 9. Phase-0 trust boundary

### Defined exactly

- proposition and quantifiers;
- minimal complete state tuple;
- move contracts;
- parent-obligation status;
- interface diagram;
- invariant ledger;
- complete witness schema;
- finite Phase-A decision object.

### Not proved here

- ambient exclusion or existence;
- boundary-changing totality;
- a decreasing complete-state measure;
- v7.2 repair;
- cubic five-support or five-CDC theorem.
