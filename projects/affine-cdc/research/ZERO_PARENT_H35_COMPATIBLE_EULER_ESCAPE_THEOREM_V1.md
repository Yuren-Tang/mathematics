# Zero-parent escape by a fixed `H_35` rank and compatible Euler circuit

## Research Lead universal theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-03`  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `f1087dab4cbb25edec0b83e747b0ba50aac62aef`  
**PDL obstruction consumed:** `proof-development/affine-cdc-rigour-v1@fee97446ee8b99f07740f394e99ef4a2ecc3e40e`  
**Classification:** `COMPLETE AUTHORIAL CANDIDATE FOR FC-PURE-NNI-ZERO-PARENT-ESCAPE / PDL RECONSTRUCTION AND INDEPENDENT AUDIT REQUIRED`.

This theorem closes the exact `(0,2,2)` prescribed-parent row isolated by
AC-PDL v7.3.  It uses one fixed physical rescue channel, one complete-graph
support-transposition-invariant integer rank, nine strict ordinary root NNIs,
and one root-only compatible-Euler macro at the rank plateau.

No equal-face `2--0` cancellation is performed.  No zero or co-root transition
is traversed.  No lower-order call, other crossed-parent substitution, track
erasure, finiteness/SCC distance, `Q_N`, `M_N`, `d_N`, nested bubble, terminal
frame or old `Omega` orbit argument is used.

The co-root `Xi` theorem is retained unchanged and is not used inside the proof
below.

---

## 1. Exact zero-parent normal form

Let `a,b` be distinct intersecting roots.  Write

\[
r=a+b.
\]

After a support permutation and the retained ordering of the four active darts,
normalise

\[
a=13,
\qquad
b=23,
\qquad
r=12,
\]

and

\[
(A,B,C,D)=(13,13,23,23).
\]

The literal prescribed parent is

\[
P=AB\mid CD,
\]

whose forced central value is zero.  The two root-valued crossed sheets are

\[
R_0=AC\mid BD,
\qquad
R_1=AD\mid BC,
\]

both with central root `12`.

Retain the complete fixed-order state

\[
S=(N,G,\delta,\lambda,\chi,P,\mathfrak B,
\kappa,\mathscr H,\tau,\alpha)
\]

from `PURE_NNI_PRESCRIBED_PARENT_STATE_INTERFACE_NORMAL_FORM_V1.md`:
labelled graph, persistent edge and dart identities, root assignment, current
crossed sheet, literal parent, cap block, route/profile data, support-component
attachments, exact category flag and identity to the stored source prefix.

Choose support `5` from the two supports unused by `a,b` and fix the physical
rescue channel

\[
\boxed{h_*=35.}
\]

The other unused support `4` remains part of the canonical frame.  The choice of
`5` is made once for this execution.

---

## 2. The physical `H_35` system

For a root-labelled edge `e`, put

\[
e\in H_{35}
\quad\Longleftrightarrow\quad
|\lambda(e)\cap\{3,5\}|=1.
\]

At every root triangle, the number of `H_35` incidences is zero or two, so
`H_35` is a disjoint union of physical cycles in the complete closed graph.

The active roots `13` and `23` both belong to `H_35`, while the active central
root `12` does not.  Thus each crossed active vertex contributes one physical
`H_35` passage.  A component containing exactly one of the two active passages
contains one `13` branch and one `23` branch.  Switching that component by
`35` gives

\[
13\mapsto15,
\qquad
23\mapsto25,
\]

on exactly one passage, and therefore makes the literal parent root-valued:

\[
15+13=35,
\qquad
25+23=35.
\]

After such a separating switch, one ordinary NNI realises `P` with central root
`35`.

A component containing neither active passage is unmarked.  A component
containing both passages is the common locked component.  There is no fourth
active-incidence pattern, because an `H_35` component entering one active vertex
must leave through the other branch of the same mixed passage.

---

## 3. A complete-graph `tau_35`-invariant rank

Let `tau_35=(3\ 5)` be the support transposition.  Define the triangle weight

\[
\begin{array}{c|cccccccccc}
T&123&124&125&134&135&145&234&235&245&345\\
\hline
\zeta(T)&1&2&1&1&0&1&1&0&1&0.
\end{array}
\]

The `tau_35` orbits are

\[
123\leftrightarrow125,
\qquad
134\leftrightarrow145,
\qquad
234\leftrightarrow245,
\]

with `124,135,235,345` fixed.  Hence

\[
\boxed{\zeta(\tau_{35}T)=\zeta(T)}
\]

for all ten triangle types.

For a complete root state put

\[
\boxed{
Z_{35}(S)=\sum_{v\in V(G)}\zeta(\Delta_v).}
\]

The sum includes every cap and exterior vertex.  Therefore

\[
0\le Z_{35}(S)\le2N.
\]

### 3.1 Whole-component invariance

If an unmarked physical `H_35` component is switched, every triangle on that
component is acted on by `tau_35` and every exterior triangle is fixed, so
`Z_35` is unchanged.

If the common component containing both active passages is switched and the
zero frame is transported back by `tau_35`, vertices on the component are acted
on twice and exterior vertices once in canonical coordinates.  The displayed
invariance again gives

\[
Z_{35}(S')=Z_{35}(S).
\]

A component containing exactly one active passage is not treated as a
nonabsorbing rank edge: it is the literal parent-repair output of Section 2.

The deterministic proof below does not need a common-component switch, but this
whole-graph invariance supplies the requested equality analogue of the fixed
channel `Xi` interface.

---

## 4. Six productive triangle types and nine strict rows

Call

\[
\mathcal P=\{123,125,134,145,234,245\}
\]

the productive `H_35` types.  At a productive vertex select its unique
non-`H_35` root as follows:

\[
\begin{array}{c|cccccc}
T&123&125&134&145&234&245\\
\hline
c(T)&12&12&14&14&24&24.
\end{array}
\]

For each productive type, the edge carrying `c(T)` is not one of the four
active `13/23` boundary branches.  If its neighbour has a distinct triangle,
the unique root-valued opposite NNI is one of the following nine rows:

\[
\begin{array}{c|c|c|c|c}
\text{central}&\text{source pair}&\text{target pair}
&Z_{\rm source}&Z_{\rm target}\\
\hline
12&123+124&134+234&3&2\\
12&123+125&135+235&2&0\\
12&124+125&145+245&3&2\\
14&124+134&123+234&3&2\\
14&124+145&125+245&3&2\\
14&134+145&135+345&2&0\\
24&124+234&123+134&3&2\\
24&124+245&125+145&3&2\\
24&234+245&235+345&2&0.
\end{array}
\]

Thus every displayed ordinary root NNI satisfies

\[
\boxed{\Delta Z_{35}\in\{-1,-2\}.}
\]

It changes only the named two-vertex cell, fixes the active central edge and the
literal parent obligation, and preserves all exterior edge/dart identities.
After the move, route, support-component and category fields are recomputed.
One exact route/cut/bounded output is absorbed; otherwise another complete
zero-parent state remains with smaller `Z_35`.

The table is exhaustive because a fixed root belongs to exactly three support
triangles.

---

## 5. The selected-row plateau

Repeatedly perform a row of Section 4 whenever one is present and category-safe.
There are at most `2N` such moves before an exact terminal or a state in which:

> for every productive vertex, its selected non-`H_35` edge joins a vertex of
> the same productive triangle type.

Call this the **selected-row plateau**.

### 5.1 Type `124` is absent

The type `124` has no `H_35` incidence.  Its three roots are `12,14,24`.
At the plateau, an edge from `124` to any distinct triangle would be one of the
nine strict rows:

- at `12`, the neighbour would be `123` or `125`;
- at `14`, the neighbour would be `134` or `145`;
- at `24`, the neighbour would be `234` or `245`.

Hence every edge incident with a `124` vertex joins another `124` vertex.  The
`124` vertices form closed connected components.  Since the complete graph is
connected and contains the two active `123` vertices,

\[
\boxed{N_{124}=0.}
\]

### 5.2 A perfect matching of nonchannel edges

Every remaining triangle type has exactly two `H_35` roots and one
non-`H_35` root.  Therefore the non-`H_35` edges form a perfect matching

\[
\boxed{M_{35}}
\]

of all vertices of `G`.

Its edges have exactly the following forms.

1. **Productive nodes.**  An endpoint in `mathcal P` uses its selected root.
   By the plateau condition the other endpoint has the same productive type.
2. **Zero nodes.**  The remaining types are
   
   \[
   \mathcal Z=\{135,235,345\}.
   \]
   
   Their unique nonchannel root is `35`, so a matching edge joins two members
   of `mathcal Z`, equal or distinct.

There is no productive--zero matching edge because their nonchannel roots are
different.

The active central edge is one productive matching edge of type `123+123` and
root `12`.

---

## 6. Every matching node has exactly two root transitions

Contract every persistent edge of `M_35`.  The physical `H_35` edges become the
edges of a connected four-regular labelled multigraph

\[
\boxed{\mathcal Q.}
\]

A vertex of `mathcal Q` remembers:

- the persistent central matching-edge identity;
- its two original cubic endpoints;
- the four ordered incident `H_35` darts;
- all cap/prefix ancestry carried by those darts.

The current two cubic vertices pair the four channel darts in one
**bitransition**.  The three local pairings consist of exactly two root-valued
bitransitions and one forbidden nonroot bitransition.

### 6.1 Equal productive or zero nodes

For an equal triangle pair, the current placement and the root branch-swap
placement are both root-valued and retain the same central root.  The third
placement pairs equal exterior roots and has central value zero.

### 6.2 Distinct zero nodes

The only distinct zero nodes are

\[
\begin{array}{c|c|c}
\text{current}&\text{other root transition}&\text{forbidden transition}\\
\hline
135+235\ (35)&123+125\ (12)&Q_4\\
135+345\ (35)&134+145\ (14)&Q_2\\
235+345\ (35)&234+245\ (24)&Q_1.
\end{array}
\]

Thus they also have exactly two root-valued bitransitions and one co-root
bitransition which is never traversed.

### 6.3 Persistent quotient

Changing a node from one root transition to the other is one ordinary root NNI
on its persistent central edge.  It changes only the pairing of the four
incident `H_35` darts.  The central edge remains outside `H_35`, every channel
edge identity and label is unchanged, and the underlying four-regular
multigraph `mathcal Q` is fixed.

Different matching nodes are vertex-disjoint before contraction.  Hence any
chosen root transition at every node is realised by zero or one source NNI per
node, in any sequential order, with the complete category test after each
move.

The transition at the active node has:

- two permitted bitransitions: the crossed root sheets `R_0,R_1`;
- one forbidden bitransition: the literal zero parent `AB|CD`.

---

## 7. Compatible Euler lemma for one forbidden bitransition

### Lemma 7.1 — special transition theorem

Let `Q` be a finite connected four-regular multigraph.  At every vertex choose
one forbidden bitransition; the other two bitransitions are permitted.  Fix a
vertex `v_0` and split it into two degree-two vertices according to its
forbidden bitransition.  Call the resulting even graph `Q^0`.

Exactly one of:

1. `Q^0` is disconnected;
2. there is a permitted bitransition at every vertex different from `v_0` and
   one permitted bitransition at `v_0` for which the resulting circuit
   partition of `Q` has exactly two circuits, each containing one passage at
   `v_0`.

### Proof

Assume `Q^0` is connected.  At every four-valent vertex choose arbitrarily one
of its two permitted bitransitions; at the two new degree-two vertices the
transition is forced.  These choices give a circuit decomposition of `Q^0`.
Choose one with the minimum number of circuits.

If at least two circuits remain, connectedness implies that two distinct
circuits meet at a four-valent vertex.  The chosen permitted bitransition uses
one passage from each circuit.  Replacing it by the other permitted
bitransition cross-joins the two cut circuits and merges them into one.  It
remains permitted, contradicting minimality.  Hence the compatible circuit
decomposition is one Euler circuit.

The Euler circuit passes once through each of the two split degree-two vertices.
Cut it at those two forced transitions.  The result is two trails, and each
trail has one endpoint in each forbidden block of `v_0`.  Their endpoint
pairing is therefore one of the two permitted bitransitions at `v_0`.  Restore
`v_0` with that permitted bitransition.  Each trail closes separately, giving
exactly two circuits, one through each active passage.  ∎

### Source significance

The proof uses the forbidden bitransitions only to define an auxiliary split
multigraph.  No forbidden zero or co-root state is ever inserted into the
physical source graph.  Only the final permitted transition choices are
realised, each by one root NNI.

---

## 8. The disconnected split is an exact terminal

Apply Lemma 7.1 to `mathcal Q`, with the active matching edge as `v_0` and the
literal parent pairing `AB|CD` as its forbidden bitransition.

Suppose `mathcal Q^0` is disconnected.  Since `mathcal Q` is connected and all
cuts in a four-regular graph are even, the two forbidden blocks lie in two
components.  Uncontracting the remote matching edges shows that the
complementary four-pole of the active two-vertex cell has two components:

\[
R_{AB}\quad\text{containing ports }A,B,
\qquad
R_{CD}\quad\text{containing ports }C,D.
\]

In either crossed current sheet, put both active vertices on the `R_AB` shore.
Exactly the two attachment edges `C,D` cross to `R_CD`.  Hence the current graph
has a two-edge cut.

If both shores contain cycles, this is the named cyclic two-cut consumer.  If
one shore is acyclic or one of the port identities coincides, the exact bounded
low-port/loop/parallel/triangle/theta ledger applies.  Thus disconnectedness of
`mathcal Q^0` is an allowed exact terminal, not an unresolved transition
failure.

No parent zero edge is constructed in this branch.

---

## 9. The connected split gives a root-only parent movie

Assume `mathcal Q^0` is connected.  Lemma 7.1 supplies a permitted transition at
every matching node such that the final physical `H_35` circuit partition has
exactly two components through the active node, one for each active passage.

Realise those transitions source-faithfully:

1. for every remote matching edge whose current transition differs from the
   selected one, perform its unique ordinary root NNI;
2. perform zero or one crossed root NNI at the active edge to choose the selected
   active transition;
3. after every NNI recompute cap, route, support-component and category fields,
   and absorb any named output.

At most `N/2` root NNIs occur.  The quotient edge identities guarantee that
later node moves still read the same four persistent channel darts even when an
earlier move reattached the opposite endpoint of one of them.

In the nonterminal branch the physical `H_35` system is now split.  Each active
component contains exactly one mixed passage.  Switch either such component by
`35`.  If the route/profile or category consumer fires, return it.  Otherwise
the active word is, up to the current crossed ordering,

\[
(15,13,25,23)
\]

or the symmetric alternative, and

\[
A+B=C+D=35.
\]

Perform the literal stored parent NNI with central root `35`.  This is an actual
root flow on the exact labelled topology `P`, with the persistent active edge,
external edge identities, cap block and prefix map retained.

Thus the compatible-Euler macro is entirely root-valued:

\[
\boxed{
\text{finitely many matching-node root NNIs}
\longrightarrow
H_{35}\text{ active split}
\longrightarrow
\text{one }H_{35}\text{ component switch}
\longrightarrow
\text{literal parent NNI}.}
\]

---

## 10. Universal finite descent

### Theorem 10.1 — `FC-PURE-NNI-ZERO-PARENT-ESCAPE`

Every complete category-safe fixed-order state with ordered active word

\[
(13,13,23,23),
\]

current crossed central root `12`, and literal prescribed parent of central
value zero has a finite source-faithful same-order history ending in exactly one
of:

1. a root flow on the literal prescribed-parent topology;
2. a cap-compatible route/profile output;
3. a named cyclic `2/3/4`-cut or bounded terminal.

The history uses only ordinary root NNIs, one legal closed support-component
switch in the successful channel branch, and exact consumers.  It uses no
`2--0` cancellation and no lower-order call.

### Proof

Fix the physical channel `H_35` and rank `Z_35`.

- While a productive selected edge has a distinct neighbour, perform the
  corresponding strict row of Section 4.  Every nonterminal step decreases the
  nonnegative integer `Z_35` by at least one, so this phase is finite.
- At the plateau, Sections 5--6 produce the persistent four-regular transition
  graph `mathcal Q` with exactly one forbidden nonroot bitransition per node.
- Split the active node along its forbidden literal-parent transition.
- If the split graph is disconnected, Section 8 gives the exact two-cut or
  bounded terminal.
- If it is connected, Section 9 gives a finite root-only transition assignment,
  a physical active `H_35` split, one separating component switch and the
  literal parent NNI.

All intermediate source moves retain graph order and the live labelled parent
field.  Every category or route failure is returned on the exact current state.
This exhausts the complete state.  ∎

### Quantitative bound

There are at most `2N` strict rank NNIs, at most `N/2` quotient-transition
NNIs, one component switch and one parent NNI.  The bound is not used as a
finite-state or SCC-distance argument; it follows from the displayed rank and
the explicit one-pass transition assignment.

---

## 11. Dart, cap and category contract

Every ordinary NNI in the proof:

- retains the persistent central edge identity;
- moves only named local darts while fixing their opposite outside darts;
- preserves every root label outside its two-vertex cell;
- retains the literal parent field and updates `alpha` by the witnessed source
  move;
- leaves cap vertices and cap dart identities fixed, although the opposite end
  of a cap-incident edge may be reattached;
- triggers a fresh route/profile, support-component and graph-category test.

The final support switch changes roots, not topology or dart identities.  The
final NNI is the literal stored predecessor NNI, not an isomorphic substitute.

A loop, parallel incidence, bridge, endpoint coincidence, cyclic cut, bounded
theta/direct object or cap-compatible route is consumed by its existing named
ledger.  No generic unlabelled `separator` is used.

---

## 12. Finite table certificate

The companion script

```text
projects/affine-cdc/research/finite/zero_parent_h35_rank_table_v1.py
```

independently enumerates:

- all ten `tau_35` triangle orbits and weight invariance;
- `H_35` degree and the unique nonchannel root of every triangle;
- the six productive types and all nine strict rows;
- their delta multiset
  
  ```text
  {-2,-2,-2,-1,-1,-1,-1,-1,-1};
  ```
- `124` as the unique `H_35`-degree-zero type;
- `135,235,345` as the zero-weight channel types;
- all three distinct-zero matching-node root transitions.

The canonical JSON certificate has SHA-256 digest

```text
aa6446dd5a01f8d4048807ff81b5f596c148f5b92224f529220277cf862e6eff
```

under sorted-key, separator-free JSON serialisation.

The compatible-Euler lemma is a human graph theorem, not an extrapolation from
bounded computation.

---

## 13. Relation to the Heawood source movie

`HEAWOOD_ZERO_PARENT_ESCAPE_SOURCE_CERTIFICATE_V1.md` verifies the requested
model movie

\[
\text{remote branch swap}
\to H_{35}\text{ split}
\to Z_0\text{ switch}
\to(15,13,25,23)
\to\text{parent root }35.
\]

The present theorem explains why that movie is not accidental.  Its remote
branch swap is one permitted transition change in the quotient `mathcal Q`; the
resulting two physical circuits are the active split supplied abstractly by
Lemma 7.1.

The universal proof does not require the Heawood graph or a preselected remote
edge.

---

## 14. Exact effect on the inverse-parent table

At Research Lead authorial level, the fixed-order inverse root-NNI table is now:

\[
\begin{array}{c|c}
\text{forced parent value}&\text{same-order disposition}\\
\hline
\text{root}&\text{literal parent NNI}\\
\text{co-root}&\text{retained v7.3 fixed-channel }\Xi\text{ theorem}\\
0&\text{Theorem 10.1 above}.
\end{array}
\]

Consequently the exact zero node

```text
FC-PURE-NNI-ZERO-PARENT-ESCAPE
```

is closed at RL authorial level, and the complete pure-NNI prescribed-parent
return can be resubmitted to PDL for independent reconstruction.

PDL must independently reconstruct:

1. the `H_35` rank and all nine strict rows;
2. exclusion of `124` and the perfect-matching plateau;
3. the persistent matching contraction and two-root/one-forbidden transition
   census;
4. the compatible-Euler lemma with complete edge/dart identities;
5. the disconnected-split two-cut/bounded lift;
6. the connected-split root-NNI movie and final component switch;
7. cap/route/category handling at every intermediate node;
8. reinsertion into the full fixed-order prefix and ordinary-induction DAG.

This authorial result does not establish an independently assured cubic
five-support theorem or universal five-CDC theorem.  It changes no canonical,
Lean, manuscript, Curator, release, tag, arXiv, DOI, peer-review, publication or
public-theorem status.
