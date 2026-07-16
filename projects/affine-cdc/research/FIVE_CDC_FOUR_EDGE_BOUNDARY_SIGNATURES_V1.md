# Four-edge boundary signatures for five-support cycle double covers

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level finite interface classification; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_K4_RESERVE_LINE_THREE_CUT_REDUCTION_V1.md`, `FIVE_CDC_HORIZONTAL_RENEWAL_NEIGHBOURHOOD_V1.md`, `gauge/gauge-modes-and-circuits.md`

## 1. Purpose

The `K_4` reserve-line theorem removes every cyclic three-edge interface from a vertex-minimal counterexample. The next harmonic quotient types visible in the renewal census have components with boundary size four:

- the weight-four quotient `4K_2`;
- the weight-six quotient `2K_3`;
- the weight-eight quotient `2C_4`.

This packet classifies the complete local state space carried by four boundary edges in an indexed five-support cycle double cover.

The key contrast is:

\[
\boxed{
\text{three boundary edges have one support signature; four boundary edges have four.}
}
\]

This is the first genuinely nontrivial gluing interface. It gives a finite four-state language in which the remaining pure point-renewal mechanism may be expressed.

## 2. Five-support covers of a four-pole

Let `P` be a graph fragment with four labelled boundary semiedges

\[
1,2,3,4.
\]

An indexed five-support boundary cover consists of five edge sets

\[
F_1,\ldots,F_5
\]

such that:

1. every internal vertex has even degree in each `F_i`;
2. every internal edge belongs to exactly two supports;
3. every boundary semiedge belongs to exactly two supports.

For one support `F_i`, the boundary trace

\[
\partial F_i\subseteq\{1,2,3,4\}
\]

has even cardinality. Hence it is:

- empty;
- one of the six pairs;
- the full four-set.

The ordered five-tuple

\[
(\partial F_1,\ldots,\partial F_5)
\]

is the labelled boundary signature.

Support-index permutation does not change the indexed cover up to renaming. Terminal permutation gives the unlabelled four-pole type.

## 3. Pair-multigraph encoding

Let `t` be the number of supports whose boundary trace is the full four-set.

After removing these `t` full traces, every boundary terminal still needs degree

\[
2-t
\]

in the remaining pair traces. Regard each pair trace as an edge of a loopless multigraph `M` on the four boundary terminals. Then `M` is `(2-t)`-regular.

Since `t\le2`, there are three cases.

### Case `t=2`

The pair multigraph is zero-regular: it has no edges. The remaining three supports are empty.

### Case `t=1`

The pair multigraph is one-regular: it is a perfect matching. The remaining two supports are empty.

### Case `t=0`

The pair multigraph is two-regular with four edges. A loopless two-regular multigraph on four vertices is either:

- two disjoint doubled edges;
- one simple four-cycle.

This gives the complete classification.

## 4. The four boundary types

### Theorem 4.1 — four-edge signature classification

Up to permutation of the five support indices and permutation of the four boundary terminals, exactly four signatures occur.

### Type A — double full trace

\[
\boxed{
\varnothing,
\varnothing,
\varnothing,
1234,
1234.
}
\]

Two supports cross all four boundary edges; three supports do not meet the boundary.

### Type B — full trace plus a matching

\[
\boxed{
\varnothing,
\varnothing,
12,
34,
1234.
}
\]

One support crosses all four edges; two supports use complementary pairs; two are absent.

### Type C — doubled matching

\[
\boxed{
\varnothing,
12,
12,
34,
34.
}
\]

Two supports use one boundary pair twice, two use its complementary pair twice, and one is absent.

### Type D — four-cycle pair pattern

\[
\boxed{
\varnothing,
12,
13,
24,
34.
}
\]

The four pair traces form a simple `C_4` on the boundary terminals; one support is absent.

#### Proof

The pair-multigraph analysis in Section 3 gives the four possibilities and no others. Their numbers of full traces and the connectedness/multiplicity type of the pair multigraph distinguish them under all support and terminal permutations. ∎

## 5. Exact finite counts

Before quotienting by symmetries, the boundary equations have:

\[
\boxed{640}
\]

ordered five-support solutions.

After forgetting support-index order, there are

\[
\boxed{10}
\]

multisets of even boundary traces.

After also quotienting by all `S_4` terminal relabellings, these ten multisets form exactly the four orbits A--D.

These counts are reproduced by the dependency-free private verifier.

## 6. Four-edge gluing criterion

Let a cubic graph `G` be separated by a four-edge cut into two four-poles `P` and `Q`, with corresponding boundary semiedges labelled `1,2,3,4`.

Let

\[
\Sigma(P)
\]

be the set of labelled five-support boundary signatures realizable on `P`, and define `\Sigma(Q)` similarly.

### Theorem 6.1 — exact signature-intersection gluing

The graph `G` has an indexed five-support cycle double cover if and only if there are boundary covers of `P` and `Q` whose labelled signatures agree after one permutation of the five support indices.

Equivalently,

\[
\boxed{
G\text{ has a five-support CDC}
\iff
\Sigma(P)\cap\Sigma(Q)\ne\varnothing,
}
\]

where signatures are recorded with the common boundary-edge labelling and support-index order is quotiented out.

#### Proof

A global cover restricts to each shore. Every support crosses the cut evenly, and the same support contains the same cut edges on both restrictions, so the two labelled signatures agree.

Conversely, suppose the shore signatures agree after relabelling the five supports on one side. Glue the corresponding boundary semiedges into the four cut edges. Each support has even degree at every shore vertex; each internal edge remains double-covered; and every cut edge is present in the same two support indices on both sides, hence exactly twice in the glued graph. ∎

### Corollary 6.2

Unlike a cyclic three-edge cut, a four-edge cut is not automatically reducible from existence alone. The obstruction is precisely the possible disjointness of the two finite signature sets

\[
\Sigma(P),\Sigma(Q)
\subseteq
\{	ext{labelled forms of A,B,C,D}\}.
\]

Thus the first nontrivial decomposition problem is a finite boundary-state compatibility problem.

## 7. Standard two-vertex cap

Choose a boundary pairing

\[
12\mid34.
\]

Cap the four-pole by adding two cubic vertices `x,y`, joining `1,2` to `x`, joining `3,4` to `y`, and adding the internal edge `xy`.

The cubic boundary-pair lemma at `x` and `y` gives:

### Proposition 7.1

The standard two-vertex cap realizes exactly boundary Types B and D.

#### Mechanism

The two supports using the cap edge `xy` connect one terminal at `x` to one at `y`.

The support using pair `12` at `x` and the support using pair `34` at `y` either:

- are the same global support, producing one full trace and hence Type B;
- are distinct, producing four pair traces forming a boundary `C_4`, hence Type D.

Types A and C require different closure data.

This shows that even the simplest cubic completion samples only half of the four-state interface space.

## 8. Why this is the next mechanism after three-cut reduction

The low-weight harmonic quotient classification now aligns with boundary size.

### `K_4` quotient

Each quotient component has boundary degree three. Three-edge boundary signatures are unique, so the interface glues automatically. This is the reducible reserve-line theorem.

### `4K_2` quotient

The two quotient components each have boundary degree four. The gauge mode is a single four-pole interface between two shores.

### `2K_3` quotient

The three quotient components each have boundary degree four: two cut edges join each pair of components. The gauge mode couples three four-pole boundary states.

### `2C_4` quotient

The four quotient components again each have boundary degree four, arranged cyclically with doubled quotient edges.

Therefore, after eliminating `K_4` lines, the surviving canonical low-weight gauge modes all live in the four-state boundary-signature world.

## 9. Connection to pure point renewal

In a cyclically four-edge-connected minimal counterexample, every marked core in the reduced renewal model is private:

\[
B_f\cap\mathbf F_2^{R_C}=0.
\]

The exact universal modules show that low-weight four-boundary gauge modes destroy one private `K_6` and create another.

The four-edge signature theorem suggests the following interpretation:

> a horizontal or vertical move changes the finite boundary signature realized by one or more four-pole components; pure point renewal is the statewise persistence of a boundary-signature mismatch.

This is a mechanism hypothesis, not yet a theorem. The theorem-level content is that only four unlabelled signature types are available and that gluing is exactly signature intersection.

## 10. A finite interface programme

For a four-pole `P`, define its **five-support signature set**

\[
\Sigma(P).
\]

The next structural tasks are:

1. determine which subsets of the four signature types can occur for bridgeless cubic four-poles;
2. determine how gauge partial Petrials act on `\Sigma(P)`;
3. determine how connected-cycle Fano-flow switches change `\Sigma(P)`;
4. identify whether the universal three- and six-dimensional renewal modules arise from a small finite transition system on triples or networks of four-pole signatures;
5. prove that persistent disjoint signature sets force a bounded four-pole decomposition.

The desired replacement for the previous points-plus-lines arrangement is:

\[
\boxed{
\text{pure point renewal}
\longrightarrow
\text{finite four-boundary signature dynamics}.
}
\]

## 11. Trust boundary

The four-type classification, exact gluing criterion, and standard-cap proposition are elementary finite theorems. The ordered/multiset/orbit counts are exhaustively verified.

The connection between renewal modules and four-pole signature mismatch is a programme-level mechanism inference and remains to be proved.

No statement here proves that every cyclic four-edge cut is reducible, that every four-pole realizes a prescribed signature, that every pure point module is generated by four-pole mismatch, or that every bridgeless cubic graph has a five-cycle double cover.
