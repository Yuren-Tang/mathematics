# Noncrossing side signatures and the bounded return-window theorem

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `317ebf08571651dba372f1b81bd5ff260e86f2ef`  
**Parents:**

- `projects/affine-cdc/research/MINIMAL_LAMINAR_INTERVAL_SURGERY_V1.md`;
- `projects/affine-cdc/research/SIDE_SIGNATURE_CONTROL_TARGET_V1.md`;
- `projects/affine-cdc/research/PETERSEN_PIVOT_RESOLUTION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_BACKTRACK_TYPE_T_REDUCTION_V1.md`.

**Status:** exact graph-combinatorial localisation theorem: every noncrossing four-port side signature is either globally bounded or contains a same-component return window with at most six side outputs. Graph-side replacement of that bounded window remains open.  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, source-graph contraction, or the global five-support theorem.

---

## 1. Linear interval model

Let `G` be a finite connected graph with no singleton edge cut. Let `R` be a connected interval region whose edge boundary is partitioned as

\[
\delta(R)=P\sqcup S,
\]

where:

- `P` is the set of route-port edges, with
  \[
  |P|\le p;
  \]
- `S=(s_1,\ldots,s_n)` is the linearly ordered list of side-attachment edges along one oriented transport spine or one linearised side boundary.

Delete the vertices of `R` and consider the connected components of the outside graph. Two side positions `i,j` receive the same label when the outside endpoints of `s_i,s_j` lie in the same outside component.

Thus the side signature determines a set partition

\[
\mathcal P_S
\]

of the ordered set `[n]`.

A block is **port-bearing** when its outside component is also incident with at least one edge of `P`.

---

## 2. Noncrossing branch

### Definition 2.1 — crossing

Two distinct blocks `A,B` cross when there exist

\[
a<b<c<d
\]

with

\[
a,c\in A,
\qquad
b,d\in B.
\]

The partition is **noncrossing** when no such quadruple exists.

This is the linear-order form of the surviving branch after the earlier crossing-signature alternative has returned to route/profile escape or a known lift defect.

---

## 3. Singleton blocks are port-controlled

### Lemma 3.1 — singleton injection

Every singleton block of `P_S` is port-bearing. Consequently the number of singleton blocks is at most `p`.

### Proof

Let an outside component `C` occur at exactly one side position. If `C` were incident with no route-port edge, then its complete edge boundary in `G` would consist of that single side edge. That edge would be a singleton edge cut, contrary to the hypothesis on `G`.

Hence `C` is incident with a route port. Distinct outside components are incident with disjoint sets of port edges, so choosing one port from each singleton component gives an injection into `P`. Therefore there are at most `p` singleton blocks. ∎

### Four-port consequence

For a minimal laminar four-port interval,

\[
\boxed{
\#\{\text{singleton side blocks}\}\le4.
}
\]

Thus every side attachment except at most four belongs to an outside component that returns to the interval at least once.

---

## 4. Interval-block lemma for noncrossing partitions

Remove all singleton positions from the side order and retain the induced order on the remaining positions. Every remaining block has size at least two, and the induced partition remains noncrossing.

### Lemma 4.1 — adjacent equal block in reduced order

A finite noncrossing partition of a linearly ordered set, all of whose blocks have size at least two, contains two consecutive positions belonging to the same block.

### Proof

Choose a block `B` whose span

\[
[\min B,\max B]
\]

is minimal by inclusion.

Suppose a position `x` strictly inside this span belonged to a different block `C`. Since `C` has at least two elements, choose another element `y in C`.

If `y` lies outside the span of `B`, then the two occurrences of `B` at its endpoints and the two occurrences `x,y` of `C` alternate, producing a crossing. Hence every element of `C` lies strictly inside the span of `B`.

But then the span of `C` is strictly contained in the span of `B`, contradicting minimality. Therefore every position between `min B` and `max B` belongs to `B`. In particular two consecutive positions belong to `B`. ∎

---

## 5. Bounded return-window theorem

### Theorem 5.1 — bounded same-component return

Assume the side partition `P_S` is noncrossing. Then exactly one of the following holds.

1. **Globally bounded signature:** every block is a singleton, and
   \[
   n\le p.
   \]
2. **Bounded return window:** there exist two side positions
   \[
   i<j
   \]
   belonging to the same outside component such that every position strictly between them is a singleton block. Consequently
   \[
   \boxed{j-i+1\le p+2.}
   \]

### Proof

If every block is a singleton, Lemma 3.1 gives `n<=p`.

Otherwise remove the singleton positions. By Lemma 4.1, two consecutive positions in the reduced order belong to one common nonsingleton block. Returning to the original order, every side position between them was removed and therefore belongs to a singleton block. Lemma 3.1 gives at most `p` such positions. Including the two endpoints yields a window of size at most `p+2`. ∎

### Corollary 5.2 — four-port six-output ceiling

For a noncrossing side signature of a four-port interval,

\[
\boxed{
|S|\le4
\quad\text{or}\quad
\text{there is a same-component return window containing at most six side outputs.}
}
\]

The two endpoint outputs enter one outside component. Every interior output, if present, enters a distinct port-bearing outside component.

---

## 6. Co-root strip form

In a co-root transport strip, every degree-two transport turn emits exactly one side root. Therefore the ordered side-output positions are the transport turns themselves.

### Corollary 6.1 — bounded enriched strip cell

A noncrossing four-port co-root strip either has at most four turns in total or contains a same-component return segment with at most six transport turns and at most seven Petersen endpoint states.

Thus the earlier warning

\[
\text{repeated coefficient state}
\not\Rightarrow
\text{replaceable segment}
\]

remains correct, but unbounded side semantics cannot survive merely by producing a long noncrossing output word. A bounded graph-side return cell always appears before any finite-state pumping argument is needed.

---

## 7. Interaction with the pivot normal form

The Petersen pivot decomposition separates a strip into:

1. rank-two constant-pivot runs;
2. DDD pivot-change states;
3. Type-T backtracks and a reduced Petersen skeleton.

The bounded return-window theorem is orthogonal to that coefficient decomposition. It controls how the emitted side edges are identified in the outside graph.

Hence every support-minimal noncrossing interval now contains one of two bounded objects:

- a complete side signature of size at most four;
- or a return window of at most six outputs, whose endpoints lie in one outside component and whose interior singleton components are all attached to the four route ports.

This is the first unconditional reduction of the unbounded side-output word to a bounded physical incidence pattern.

---

## 8. Revised composition target

It is no longer necessary to solve arbitrary side signatures in one step. It suffices to prove the following bounded-window transfer lemma.

### Target 8.1 — six-output return-cell transfer

For a same-component return window with at most six side outputs, prove one of:

1. **serial replacement:** the window may be contracted or replaced while preserving the four route ports and root boundary;
2. **separator:** the returning outside component and the transport segment determine a smaller cyclic separator or four-pole;
3. **route escape:** one of the at most four port-bearing singleton components creates an interlacing/profile-changing switch;
4. **bounded defect atom:** root-fibre failure or incompatible DDD resolution localises inside the window;
5. **bounded holonomy core:** the window carries one even flat displacement or one odd DDD resolution class requiring a single finite calibration.

Failure of these alternatives would be a finite bounded counterexample to the proposed side-signature control lemma, not an unbounded new transducer language.

---

## 9. Relation to the six-channel ceiling

The return window contains at most six ordered side outputs. This numerically matches the earlier six repair channels and the `K_(2,3)` blocker geometry.

No coordinate identification is asserted here. To use that theorem one must still prove that the six side-output incidences map functorially to the six channel coordinates and that the four maximal certificates agree with the four-port boundary functions.

The present result supplies the missing bounded source object on which that comparison can be made.

---

## 10. Trust boundary

### Exact here

- singleton outside components must be port-bearing in a graph with no singleton cut;
- at most `p` singleton side blocks occur in a `p`-port interval;
- the interval-block lemma for noncrossing partitions;
- the bounded same-component return theorem;
- the four-port ceiling of six side outputs;
- the corresponding six-turn bound for a linear co-root strip.

### Still open

- verification of the noncrossing outside-component partition in every physical pair-preserving interval with repeated visits;
- root-admissible contraction of a bounded return window;
- extraction of a composition-safe cyclic separator;
- identification with the six-channel `K_(2,3)` coordinate system;
- affine calibration of bounded even and odd cores;
- Type-T/Type-H strict descent, horizontal induction, and the global five-support theorem.
