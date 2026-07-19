# Cap-forcing kernels for cyclic four-edge cuts

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level finite minimal-counterexample reduction; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_FOUR_EDGE_BOUNDARY_SIGNATURES_V1.md`, `FIVE_CDC_K4_RESERVE_LINE_THREE_CUT_REDUCTION_V1.md`

## 1. Purpose

Four boundary edges carry four unlabelled five-support signature types. With the four terminals labelled, the states arising from the standard two-vertex cubic cap form a six-state subsystem.

This packet applies vertex minimality to all three cap pairings of one shore of a cyclic four-edge cut. The result is a small finite obstruction kernel:

\[
\boxed{
\text{each shore must realize at least two cap states with distinct matching indices.}
}
\]

If the original graph remains uncovered, the two shore profiles are disjoint. After taking minimal witnesses and quotienting by symmetry, exactly six profile-pair kernels remain.

This is the first concrete finite-state reduction of the irreducible four-pole problem.

## 2. Labelled B and D states

The four boundary terminals admit exactly three perfect matchings. Write them as

\[
M_0,M_1,M_2.
\]

Refine the boundary Types B and D by their matching index.

### State `B_i`

One support uses all four terminals, and the two pair-supports form the perfect matching `M_i`.

### State `D_i`

Four pair-supports form the simple four-cycle whose missing complementary matching is `M_i`.

Thus the standard-cap state space is the six vertices

\[
\mathcal P
=
\{B_0,B_1,B_2,D_0,D_1,D_2\}.
\]

It is useful to picture `\mathcal P` as a triangular prism: the matching index is the triangular coordinate and the letter `B/D` is the two-level coordinate.

Types A and C remain valid four-pole signatures but are not induced by the standard two-vertex cap.

## 3. Which states a cap can induce

Fix a cap pairing `M_i`. The two terminals of each block attach to one new cubic vertex, and the two new vertices are joined by the cap edge.

The boundary-signature classification shows:

### Lemma 3.1 — cap exclusion rule

A cap using pairing `M_i` induces exactly one of the states

\[
\boxed{
\mathcal K_i
:=
\{B_j,D_j:j\ne i\}.
}
\]

In particular it never induces `B_i` or `D_i`.

#### Proof

The cap realizes only Types B and D. In either type, the matching index is one of the two perfect matchings that cross between the two cap blocks. The matching `M_i` itself consists of the two within-block pairs and is therefore excluded. Conversely the finite local cap patterns realize both letters for each of the two crossing matching indices. ∎

## 4. Every cap completion is bridgeless

Let `P` be one shore of a cyclic four-edge cut in a connected bridgeless cubic loopless multigraph. For any perfect matching `M_i` of its four boundary semiedges, form the standard two-vertex cap completion `P^{M_i}`.

### Lemma 4.1

Every `P^{M_i}` is a connected bridgeless cubic loopless multigraph.

#### Proof

Cubicity, connectedness, and looplessness are immediate; parallel edges are allowed.

For the cap edge, choose one terminal from each cap block and a path between their endpoints inside the connected shore. Together with the two terminal edges and the cap edge this gives a cycle.

For a terminal edge, the corresponding original cut edge lies on a cycle of the bridgeless ambient graph. The segment of that cycle inside the shore joins its endpoint to another boundary endpoint. Close this segment either through one cap vertex or through both cap vertices and the cap edge, according to the second endpoint's cap block.

For an internal shore edge, choose a cycle containing it in the ambient graph. A shore segment of that cycle containing the edge has two boundary endpoints whenever the cycle leaves the shore; close those endpoints through the cap. Hence every completion edge lies on a cycle. ∎

If the opposite shore is cyclic, it has at least four vertices: a cubic shore with four boundary edges and two vertices has only one internal edge and contains no cycle. Therefore adding two cap vertices still produces a graph strictly smaller than the original graph.

## 5. Minimality forces cap profiles

For a four-pole `P`, let

\[
\Sigma(P)
\]

be its set of labelled five-support boundary signatures realizable by boundary covers.

Let its standard-cap profile be

\[
\Pi(P)
:=
\Sigma(P)\cap\mathcal P.
\]

### Theorem 5.1 — cap-forcing theorem

Let `G` be a vertex-minimal bridgeless cubic graph without a five-support cycle double cover, and let `P` be either shore of a cyclic four-edge cut. Then

\[
\boxed{
\Pi(P)\cap\mathcal K_i\ne\varnothing
\qquad(i=0,1,2).
}
\]

Equivalently, the matching-index projection

\[
\operatorname{ind}\Pi(P)
:=
\{i:B_i\in\Pi(P)\text{ or }D_i\in\Pi(P)\}
\]

has cardinality at least two.

#### Proof

For each `i`, the cap completion `P^{M_i}` is bridgeless cubic and strictly smaller than `G`. By vertex minimality it has a five-support cycle double cover. Restrict this cover to the original four-pole. Lemma 3.1 says its boundary signature belongs to `\mathcal K_i`. Therefore `\Pi(P)` meets every `\mathcal K_i`.

A subset of `\mathcal P` meets all three `\mathcal K_i` exactly when it contains states with at least two distinct matching indices. If all states had one index `j`, the cap set `\mathcal K_j` would be missed. Conversely two distinct indices ensure that for every `i` at least one available index differs from `i`. ∎

### Corollary 5.2 — minimal shore witnesses

Every cap-forced shore profile contains a two-state subprofile

\[
\{X_i,Y_j\},
\qquad
X,Y\in\{B,D\},
\qquad
 i\ne j.
\]

There are exactly twelve such inclusion-minimal profiles.

## 6. Counterexample cuts require disjoint profiles

Let `P,Q` be the two shores of the cyclic four-edge cut, with the common boundary-edge labelling.

The exact gluing theorem gives

\[
G\text{ has a five-support CDC}
\iff
\Sigma(P)\cap\Sigma(Q)\ne\varnothing.
\]

Hence in a minimal counterexample:

\[
\boxed{
\Sigma(P)\cap\Sigma(Q)=\varnothing.
}
\]

In particular their cap profiles `\Pi(P),\Pi(Q)` are disjoint, while each has matching-index projection of size at least two.

Thus an irreducible cyclic four-cut is represented by two disjoint subsets of the triangular-prism state space, each projecting to at least two prism columns.

## 7. Six minimal obstruction kernels

Choose one minimal two-state witness from each shore profile. There are thirty disjoint witness pairs before symmetry.

Quotient simultaneously by:

- the `S_3` permutation of matching indices;
- interchange of the two shores.

### Theorem 7.1 — six cap-forcing kernels

Exactly six orbits remain. Representatives are:

\[
\begin{array}{c|c}
\text{shore }P&\text{shore }Q\\
\hline
\{B_0,B_1\}&\{B_2,D_0\}\\
\{B_0,B_1\}&\{D_0,D_1\}\\
\{B_0,B_1\}&\{D_0,D_2\}\\
\{B_0,D_1\}&\{B_1,D_0\}\\
\{B_0,D_1\}&\{B_1,D_2\}\\
\{B_0,D_1\}&\{D_0,D_2\}.
\end{array}
\]

Every cyclic four-edge cut in a vertex-minimal counterexample contains, after relabelling and possibly exchanging shores, one of these six minimal disjoint profile kernels.

#### Proof status

The cap-forcing characterization is elementary. The orbit count is a finite exhaustive classification over the twelve minimal profiles, reproduced by the private verifier. ∎

Additional signatures in `\Sigma(P)` or `\Sigma(Q)` may enlarge the profiles, but disjointness forbids adding a signature already realized on the opposite shore. The six kernels are minimal witnesses, not a classification of all enlarged disjoint profile pairs.

## 8. Mechanism significance

The three-cut and four-cut situations now differ sharply.

### Three-edge cut

There is only one local support pattern. Both shores necessarily match, so gluing is automatic.

### Four-edge cut

There are four unlabelled types and ten labelled states. Minimality forces each shore to realize at least two prism states, but the two shore sets can remain disjoint. The incompatibility is finite and has six minimal kernels.

Thus the first irreducible decomposition obstruction is not an arbitrary graph phenomenon. It is a six-case boundary-state mismatch.

## 9. Connection to harmonic quotients

The low-weight gauge modes remaining after `K_4` three-cut reduction have four-boundary quotient components.

- `4K_2` gives two four-poles joined by four quotient edges.
- `2K_3` gives three four-poles, each incident with two edges to each of the other two.
- `2C_4` gives four four-poles arranged cyclically with doubled interfaces.

The cap-forcing theorem suggests that their renewal dynamics should be expressible using triangular-prism profiles and the six mismatch kernels.

In particular, the universal three-cube driven by a minimum `2K_3` circuit may encode coupled changes of three four-pole profiles. The universal six-cube may be a larger network built from the same six-state local prism.

This interpretation remains conjectural; the finite boundary and cap theorems are exact.

## 10. Refined programme

The remaining irreducible mechanism has three nested finite levels.

### Level 1 — shore signature set

\[
\Sigma(P)
\subseteq
\{A,B_i,C_i,D_i:i=0,1,2\}.
\]

### Level 2 — cap-forced prism profile

\[
\Pi(P)
\subseteq
\{B_i,D_i:i=0,1,2\},
\qquad
|\operatorname{ind}\Pi(P)|\ge2.
\]

### Level 3 — cut mismatch kernel

Two cyclic-cut shores in a minimal counterexample have disjoint profiles containing one of six minimal witness pairs.

The next tasks are therefore:

1. determine which of the six kernels can actually be realized by bridgeless cubic four-poles;
2. show that some kernels force additional A or C states and hence destroy disjointness;
3. compute the action of gauge partial Petrials on the triangular-prism profile;
4. map the universal renewal modules to networks of these kernels;
5. prove that persistent kernel dynamics either acquires a common signature or decomposes into a smaller bounded four-pole system.

The mechanism target is now:

\[
\boxed{
\text{pure point renewal}
\longrightarrow
\text{six finite four-pole mismatch kernels}
\longrightarrow
\text{escape or bounded decomposition}.
}
\]

## 11. Trust boundary

The cap exclusion rule, bridgeless-cap lemma, minimality forcing theorem, and signature-disjointness condition are elementary graph-theoretic results.

The six-kernel orbit classification is exact finite computation.

The proposed identification of universal renewal modules with coupled prism-profile dynamics is a programme-level inference, not yet a theorem.

No statement here proves that all six kernels are realizable, eliminates every cyclic four-edge cut, proves horizontal escape from pure point renewal, or proves the five-cycle double cover conjecture.
