# A directed projectivity edge cannot be replaced locally by the complementary hexagon arc

## Research Lead scope-correction theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `9a94d17f223c507fb03ea30ddd8450c7c6b2059b`.

**Parents:**

- `DIRECTED_HEXAGON_FLAG_SIMPLE_TRANSITIVITY_V1.md`;
- `RELATIVE_PROJECTIVITY_DIRECTED_REWRITING_BOUNDARY_V1.md`;
- `PIVOT_CHANGE_SIX_PORT_STAR_COMPLETION_V1.md`;
- `PETERSEN_PIVOT_RESOLUTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`.

**Correction:** `RELATIVE_PROJECTIVITY_DIRECTED_REWRITING_BOUNDARY_V1.md` isolated a directed hexagon-lift property (`DHL`) as a sufficient bypass and left a canonical local form as an open target. The present theorem proves that the strict local form—one actual token edge replaced by the complementary five-edge hexagon arc while fixing the exterior source incidences—is impossible. The abstract rewrite changes the number and labels of emitted side-root incidences. Only a larger physical strip in which those extra incidences already exist can realize the hexagon relation.

**Status:** exact source-arity obstruction with a complete four-case Wolfram certificate. It strengthens the trust boundary and leaves the current actual-`C6/C8` recurrence proof controlling.

---

## 1. Side outputs of a pivot path

Let

\[
p_{i-1}\longrightarrow p_i\longrightarrow p_{i+1}
\]

be one reduced turn in the Petersen pivot path. The adjacent DDD states are

\[
\{p_{i-1},p_i\},
\qquad
\{p_i,p_{i+1}\}.
\]

The pivot-resolution theorem gives the emitted side root

\[
\boxed{r_i=p_{i-1}+p_{i+1}.}
\]

For a nonbacktracking Petersen turn the two distance-two roots intersect, so `r_i` is a root. If

\[
p_{i-1}=p_{i+1},
\]

then `r_i=0`; this is exactly an immediate pivot backtrack.

Hence an open pivot path

\[
p_0,p_1,\ldots,p_m
\]

with fixed predecessor and successor data carries one exterior side incidence for every internal pivot. The side word is not determined merely by the endpoints.

---

## 2. One directed edge and its local source boundary

Consider one directed token edge

\[
s\longrightarrow t
\]

inside an actual reduced contextual path, with predecessor `x` and successor `y`:

\[
x\longrightarrow s\longrightarrow t\longrightarrow y.
\]

The minimal source cell is the six-port pivot-change cell of `PIVOT_CHANGE_SIX_PORT_STAR_COMPLETION_V1.md`. Its two emitted side roots are

\[
\boxed{z=x+t,}
\qquad
\boxed{w=s+y.}
\]

Thus, after the two resolved endpoint turns are retained, the directed edge contributes exactly two exterior side-root incidences.

---

## 3. Complementary hexagon arc

By `S_5 times C_2` simple transitivity it suffices to use the canonical directed lifted-hexagon flag

\[
13^0\to24^1\to35^0\to14^1\to23^0\to45^1\to13^0.
\]

Orient the distinguished edge as

\[
\boxed{s=13\longrightarrow t=24.}
\]

The complementary directed five-edge arc from `s` to `t` is

\[
\boxed{
13\longrightarrow45\longrightarrow23\longrightarrow14
\longrightarrow35\longrightarrow24.
}
\]

Write

\[
a=45,
\quad b=23,
\quad c=14,
\quad d=35.
\]

Replacing the single edge in the same endpoint context would change

\[
x,s,t,y
\]

to

\[
x,s,a,b,c,d,t,y.
\]

The replacement therefore emits six side roots:

\[
\boxed{
 x+a,
\ s+b,
\ a+c,
\ b+d,
\ c+t,
\ d+y.
}
\]

This is already an arity change from two side incidences to six.

---

## 4. Complete endpoint-context classification

The Petersen neighbours of `s=13` other than `t=24` are

\[
\boxed{x\in\{25,45\}.}
\]

The Petersen neighbours of `t=24` other than `s=13` are

\[
\boxed{y\in\{15,35\}.}
\]

There are four endpoint contexts.

### Case 1 — the unique reduced context

Take

\[
\boxed{x=25,\qquad y=15.}
\]

Neither endpoint immediately backtracks along the complementary arc. The original side word is

\[
\boxed{(x+t,s+y)=(45,35).}
\]

The replacement side word is

\[
\boxed{
(x+a,s+b,a+c,b+d,c+t,d+y)
=(24,12,15,25,12,13).
}
\]

All six values are roots, but:

1. the arity is six rather than two;
2. the side-root multiset is different;
3. four new exterior source incidences are required.

### Case 2

For

\[
x=25,\qquad y=35=d,
\]

the last replacement side value is

\[
d+y=0.
\]

The replacement has an immediate right backtrack.

### Case 3

For

\[
x=45=a,\qquad y=15,
\]

the first replacement side value is

\[
x+a=0.
\]

The replacement has an immediate left backtrack.

### Case 4

For

\[
x=45=a,\qquad y=35=d,
\]

both endpoint side values are zero. The replacement backtracks at both ends.

### Theorem 4.1 — unique reduced embedding and boundary mismatch

Up to support permutation and sheet reversal, the complementary five-edge hexagon arc has exactly one reduced embedding into a four-pivot endpoint context. In that embedding its side word is

\[
(24,12,15,25,12,13),
\]

whereas the original edge side word is

\[
(45,35).
\]

Therefore no boundary-preserving local source movie can replace the one edge by the complementary five-edge path.

---

## 5. Source-arity obstruction

### Theorem 5.1 — failure of strict local `DHL`

There is no equivariant local theorem of the following form:

> replace an arbitrary full-context occurrence of one directed projectivity edge by the complementary five-edge arc of its lifted Petersen hexagon while fixing every exterior source incidence and side-root attachment.

### Proof

By simple transitivity, any such theorem transports to the canonical flag. Theorem 4.1 shows that the unique reduced endpoint embedding changes two exterior side incidences into six and changes their root labels. A local source surgery fixing the exterior incidence set cannot create four new semiedges or replace the prescribed side word. The other endpoint contexts contain immediate zero/backtrack turns and reduce before giving a five-edge replacement. ∎

### Corollary 5.2

The `DHL` condition of `RELATIVE_PROJECTIVITY_DIRECTED_REWRITING_BOUNDARY_V1.md`, when interpreted as a strict single-edge fixed-boundary source replacement, is false and is superseded by the present correction.

---

## 6. What can still realize a hexagon relation

The obstruction does not contradict the actual `C6` source movie.

In an actual physical `C6` track:

1. all six pivot turns already occur;
2. all six side-root incidences already exist in the annular source neighbourhood;
3. consecutive cells share their resolved turn corollas;
4. the relative `(0,2,2)` NNI acts inside that fixed larger boundary;
5. the canonical star contains a genuine equal-face dipole.

Thus the source movie does not create the complementary five-edge path from one edge. It consumes a strip in which the complete hexagon and its side attachments are already present.

Likewise an actual `C8` theorem works because two physically present `C6` factors and their seam data already exist.

---

## 7. Full-channel locks do not supply the missing incidences

An oriented full-channel lock asserts that several even-subgraph repair channels:

- contain the two marked reconnection edges in one component;
- cut open in the same ordered cap route;
- carry no residual orientation holonomy.

These are global path systems in the existing source graph. They are not additional Pachner-history vertices or side-root semiedges. The existence of all repair channels therefore does not manufacture the four extra side incidences required by the complementary projectivity arc.

Consequently:

\[
\boxed{
\text{Kempe-channel completeness}
\not\Rightarrow
\text{projectivity path lifting}.
}
\]

---

## 8. Corrected architectural consequence

The collapsible projectivity core remains an exact description of the abstract recurrence relations. It cannot by itself replace physical recurrence extraction.

The controlling route remains:

1. take an actual recurrent full-context token path;
2. remove actual constant runs and actual immediate backtracks;
3. extract an actual shortest repeated-pivot subtrack;
4. exclude odd physical subtracks by the cap orientation;
5. obtain an actual `C6` or `C8` with all side attachments present;
6. apply the source-level relative movie and strict cancellation;
7. conclude no bad sink SCC in the finite contextual graph.

The projectivity complex is therefore:

- a conceptual presentation;
- a finite certificate that `C8` is not abstractly primitive;
- a symmetry reduction for actual complete hexagons;
- not a local rewriting engine on arbitrary contextual edges.

---

## 9. Revised research frontier

The proposed local canonical `DHL` target is closed negatively.

A remaining global question could ask for a source-realizable cellular disk whose entire boundary strip and all side attachments are already present. But such a theorem is not presently weaker than the controlling finite-condensation recurrence argument; it repackages the same global coherence burden.

Therefore AC-RL should not prioritize arbitrary projectivity-diagram lifting unless a new source construction supplies the missing incidence data independently.

The higher-leverage frontier returns to the concrete attack surface:

1. PDL reconstruction of the actual full-state forced backbone;
2. full verification of cap-block orientation on every physical subtrack;
3. source-level `C6` movie and `C8` seam compatibility;
4. inverse-cancellation quadruple-equality lower-order recursion;
5. finiteness and transition completeness of the contextual graph.

---

## 10. Wolfram certificate

A direct exact enumeration gives:

\[
\begin{array}{c|c|c|c}
x&y&\text{replacement endpoint status}&\text{replacement side word}\\
\hline
25&15&\text{reduced}&(24,12,15,25,12,13)\\
25&35&\text{right backtrack}&(24,12,15,25,12,0)\\
45&15&\text{left backtrack}&(0,12,15,25,12,13)\\
45&35&\text{both backtracks}&(0,12,15,25,12,0).
\end{array}
\]

The original side words in the four cases are respectively

\[
(45,35),
(45,15),
(25,35),
(25,15).
\]

No case has the same boundary arity or side-root multiset.

---

## 11. Trust boundary

### Exact here

- side-output formula along a pivot turn;
- complete canonical endpoint-context classification;
- uniqueness of the reduced complementary-arc embedding;
- exact original and replacement side words;
- boundary-arity obstruction;
- refutation of strict local fixed-boundary `DHL`;
- distinction between Kempe-channel completeness and Pachner-history path lifting;
- compatibility of the correction with the existing actual `C6/C8` source movies.

### Not implied

- any defect in the controlling actual-`C6/C8` recurrence proof;
- failure of a genuinely global diagram theorem with pre-existing side incidences;
- PDL reconstruction or independent acceptance;
- Lean verification, manuscript integration, release, arXiv, DOI, peer review, publication;
- or the established truth of the five-cycle double-cover conjecture.