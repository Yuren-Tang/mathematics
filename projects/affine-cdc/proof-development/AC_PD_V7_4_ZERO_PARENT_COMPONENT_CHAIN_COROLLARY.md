# AC-PD v7.4 — zero-parent `H_35` terminal-path escape

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Classification:** `COMPLETE-DRAFT FOR THE ZERO-PARENT (0,2,2) FIBRE / NEW AUDIT REQUIRED`.

This dossier reconstructs the complete zero-parent source movie.  It uses the
component-chain theorem to change the **outside** terminal matching before any
support switch or literal parent NNI is attempted.

---

## 1. Canonical zero-parent state

Let the four ordered active branches be normalized to

\[
(A,B,C,D)=(13,13,23,23).
\]

The two crossed active topologies are

\[
AC|BD,\qquad AD|BC,
\]

both with central root

\[
13+23=12.
\]

The literal stored parent is

\[
AB|CD
\]

with central value zero.

Fix the physical rescue channel

\[
h=35.
\]

The roots `13,23` belong to `H_35`, while the active crossed central root `12`
does not.  The unique inactive triangle is

\[
I_{35}=124.
\]

---

## 2. Complementary carrier and category test

Remove the interiors of the two active vertices while retaining the four
ordered stable branch semiedges `A,B,C,D`.  Let `R` be the complementary rooted
carrier.

### Lemma 2.1 — connected nonterminal carrier

If `R` is disconnected, every component has at least one terminal incidence,
otherwise the original graph was disconnected.  Since there are four terminals,
one component has at most two.

- one terminal gives a bridge/single attachment;
- two terminals give an exact two-edge cut;
- a bounded component gives its named low-port consumer.

Hence every category-safe nonterminal zero-parent state has connected `R`.

All stable active branch darts, the active central edge identity, cap block and
stored-prefix map remain boundary coordinates while the chain moves occur in
`R`.

---

## 3. Outside `H_35` matching

The selected subgraph `H_35\cap R` has four terminal incidences.  Its physical
matching is one of:

\[
AB|CD,\qquad AC|BD,\qquad AD|BC.
\]

### Immediate crossed matching

If the outside matching is `AC|BD` or `AD|BC`, choose the active crossed root
sheet with the same matching, using zero or one root-valued branch-swap NNI on
the active edge.

The full `H_35` system then consists of two closed components.  Each contains:

- exactly one of the two `13` active branches;
- exactly one of the two `23` active branches.

This is the productive separating configuration.

### Residual lock

The only nonabsorbed matching is

\[
AB|CD.
\]

Then `H_35\cap R` has two distinguished terminal paths

\[
P_{13}:A--B,\qquad P_{23}:C--D,
\]

plus closed cycles.

---

## 4. Component-chain contraction

Form the physical quotient with nodes:

- the two terminal paths;
- every closed `H_35` cycle;
- every inactive `124` vertex.

Choose one shortest simple path once and retain its stable nonchannel connector
edges.  Apply `FC-COMPONENT-CHAIN-ROOT-NNI`.

- an active/inactive row absorbs one `124` vertex;
- an active/active root NNI or equal branch swap absorbs one intervening cycle;
- every pre-final move deletes the first named connector from the inherited
  list;
- every category or route failure is an exact terminal.

At the final connector the outside matching changes from `AB|CD` to exactly one
of

\[
AC|BD,\qquad AD|BC.
\]

The final equal-endpoint case is safe because its two passages are the two
**distinct** terminal paths.  It is not an arbitrary same-component equal face.

---

## 5. Crossed-sheet alignment

Choose the active crossed topology with the same newly exposed outside
matching.  This requires zero or one root branch-swap on the active central edge
`12`.

After alignment, the complete `H_35` system has two closed components, each
containing one `13` branch and one `23` branch.  The branch-swap is category-
tested before continuation; a cut/bounded or cap-compatible output is consumed
immediately.

No target progress is inferred merely from switching crossed sheets.  Progress
was already supplied by the physical outside matching change.

---

## 6. One legal closed switch

Switch either one of the two closed components by support pair `35`.  The
switch is a legal root-flow involution and preserves the uncoloured topology,
stable darts, cap vertex identities, literal parent obligation and graph order.

Exactly one active `13` branch and one active `23` branch are translated:

\[
13\mapsto15,\qquad23\mapsto25.
\]

Up to the fixed ordered symmetry, the active word becomes

\[
(15,13,25,23).
\]

Hence

\[
15+13=35,\qquad25+23=35.
\]

---

## 7. Literal parent NNI

Perform the stored `AB|CD` NNI on the active central edge.  Its new central root
is

\[
35.
\]

The four branch stable edges retain their outside endpoints and ancestry; only
the explicitly selected inside darts change endpoint according to the stored
parent topology.  The output is the literal labelled predecessor, not an
isomorphic root closure.

The prefix map is updated by this actual local source movie and is the identity
elsewhere.

---

## 8. Independent Heawood certificate

Use the fourteen-vertex stable edge/root table recorded in the frozen source,
with active edge `4-5:12` and ordered branches

\[
A=3-4:13,\quad B=5-6:13,\quad C=4-13:23,\quad D=5-10:23.
\]

### Remote root branch swap

At stable edge `13-14:12`, both endpoint triangles are `123`.  Retain the
central edge and the two `23` darts; reattach

\[
12-13\to12-14,\qquad1-14\to1-13.
\]

All root equations remain valid.

### Exact `H_35` split

After the branch swap the two closed components are

\[
Z_0=1-2-3-4-13-1
\]

and

\[
Z_1=5-6-7-12-14-9-10-5.
\]

The first contains active branches `A,C`; the second contains `B,D`.  Thus the
outside and active crossed matchings are aligned.

### Switch and parent

Switch `Z_0` by `35`.  The active word becomes

\[
(15,13,25,23).
\]

Then on stable edge `4-5` reattach

\[
5-6@5\to5-6@4,\qquad4-13@4\to4-13@5
\]

and change the central root `12 -> 35`.

The final active triangles are `135,235`, and the topology is the literal
`AB|CD` parent.

### Independent checks

Direct reconstruction from the stable table verifies:

| state | connected | simple | cubic | bridges | girth | cyclic edge-connectivity |
|---|---|---|---|---:|---:|---:|
| initial | yes | yes | yes | 0 | 6 | 6 |
| post-remote NNI | yes | yes | yes | 0 | 5 | 5 |
| post-switch | yes | yes | yes | 0 | 5 | 5 |
| final parent | yes | yes | yes | 0 | 5 | 5 |

Every vertex equation was independently checked after each move.  The retained
cap vertices `7,12`, ordered cap darts and stable edge identities survive
literally.

The published state digests are retained only as reproducibility labels; the
proof uses the displayed incidences and roots.

---

## 9. Universal zero-parent theorem

### Theorem `FC-PURE-NNI-ZERO-PARENT-ESCAPE`

Every complete category-safe fixed-order state in the zero-parent `(0,2,2)`
fibre has a finite source-faithful same-order history ending in exactly one of:

1. a root flow on the literal prescribed-parent topology;
2. a cap-compatible route/profile state;
3. a named cyclic `2/3/4`-cut or bounded terminal.

The history consists of:

1. a witnessed `H_h` component-chain contraction when the outside matching is
   not already crossed;
2. zero or one active crossed root NNI for matching alignment;
3. one legal closed support-component switch;
4. the literal parent NNI.

No `2--0` cancellation, lower-order call, track-erasure progress, SCC distance,
`Q_N`, `M_N`, `d_N`, nested bubble or terminal frame is used.

---

## 10. General support word

For a general zero word `(a,a,b,b)` with distinct intersecting roots, let
`r=a+b`.  A support permutation carries `(a,b,r)` to `(13,23,12)`; the remaining
two supports determine the physical analogue of `H_35`.  Transport the entire
labelled state, apply the canonical theorem, and transport back by the same
single support permutation.  The literal parent and stable dart identities are
carried throughout.