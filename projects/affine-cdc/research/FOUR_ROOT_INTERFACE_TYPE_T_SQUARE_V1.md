# Four-root interfaces and the Type-T square normal form

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `f2f5cc7749ed17898e2244110414aafd9eedbae4`  
**Parents:**

- `projects/affine-cdc/research/PETERSEN_BACKTRACK_TYPE_T_REDUCTION_V1.md`;
- `projects/affine-cdc/research/LOW_PORT_TAIT_CORE_GLUING_V1.md`;
- `projects/affine-cdc/research/TAIT_FOUR_PORT_RESPONSE_COMPRESSION_V1.md`;
- `projects/affine-cdc/five-support/cuts-four-poles-and-routing.md`;
- `projects/affine-cdc/five-support/holonomy-defects-and-atoms.md`.

**Status:** exact four-root boundary classification, exact route-sum table, and explicit minimal root-valued completion of the unique nontrivial interface with no two-vertex root resolution. The exceptional route-sum orbit is exactly the Petersen-backtrack Type-T `abba` word with disjoint roots. Its canonical four-cycle completion has the serial support response forced by the boundary word.  
**Not implied:** universal state-set inclusion for arbitrary smaller-graph covers, deletion of external side attachments, a composition-safe graph reduction in every ambient category, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Conserved four-root boundaries

Identify the ten roots of `E5` with the edges of `K5`.

Let

\[
(r_1,r_2,r_3,r_4)\in R_5^4
\]

be an ordered four-port boundary satisfying root-flow conservation

\[
\boxed{r_1+r_2+r_3+r_4=0.}
\]

For the three terminal pairings

\[
M_{12|34},\qquad M_{13|24},\qquad M_{14|23},
\]

define their forced two-vertex internal sums

\[
d_{12|34}=r_1+r_2=r_3+r_4,
\]

\[
d_{13|24}=r_1+r_3=r_2+r_4,
\]

\[
d_{14|23}=r_1+r_4=r_2+r_3.
\]

A two-vertex cubic four-pole with the indicated pairing is root-valued exactly when the corresponding `d_M` is a root.

---

## 2. Complete boundary multiset classification

### Theorem 2.1 — four-root boundary types

Every conserved four-root boundary has exactly one of the following multiset types.

1. **Quadruple root**
   \[
   a,a,a,a.
   \]

2. **Two doubled roots**
   \[
   a,a,b,b,
   \qquad a\ne b.
   \]

3. **Four distinct roots forming a four-cycle in `K5`.**

No other multiset type occurs.

### Proof

Reduce the four-root multiset modulo two. The roots occurring an odd number of times form a simple even subgraph of `K5` with at most four edges.

- If this odd-support graph is empty, every multiplicity is even, giving either four equal roots or two doubled roots.
- If it is nonempty, it has four distinct edges. A simple even graph with four edges is a four-cycle.

This exhausts the possibilities. ∎

---

## 3. Complete route-sum table

### Theorem 3.1 — route-sum weights

Up to reordering the three pairings, the weights of

\[
(d_{12|34},d_{13|24},d_{14|23})
\]

are exactly:

\[
\boxed{
\begin{array}{c|c}
\text{boundary type}&\text{route-sum weights}\\
\hline
a,a,a,a&(0,0,0)\\
a,a,b,b,\ a\cap b\ne\varnothing&(0,2,2)\\
a,a,b,b,\ a\cap b=\varnothing&(0,4,4)\\
C_4\text{ of four distinct roots}&(2,2,4).
\end{array}}
\]

### Proof

For two doubled roots, the pairing which groups equal roots has sum zero. Both crossed pairings have sum `a+b`.

- If `a,b` meet in one support index, `a+b` is the third root of a `K5` triangle and has weight two.
- If `a,b` are disjoint, `a+b` is a co-root and has weight four.

For four distinct roots forming a cycle, the pairing of opposite cycle edges gives the common co-root supported on the four cycle vertices. The other two pairings pair adjacent cycle edges and give the two diagonals, both roots.

The quadruple-root case is immediate. ∎

### Exact finite certificate

Direct enumeration of the `640` ordered conserved four-root boundaries gives:

\[
\begin{array}{c|c|c}
\text{multiplicity type}&\text{weight pattern}&\text{ordered count}\\
\hline
(4)&(0,0,0)&10\\
(2,2)&(0,2,2)&180\\
(2,2)&(0,4,4)&90\\
(1,1,1,1)&(2,2,4)&360.
\end{array}
\]

This certificate is supplementary; the theorem has the structural proof above.

---

## 4. Two-vertex root resolutions

### Corollary 4.1

A conserved four-root boundary has a two-vertex root-valued completion exactly in the route-sum branches of weight two.

Therefore:

- an adjacent doubled pair has two crossed root resolutions;
- a four-cycle boundary has two root resolutions and one co-root route;
- a quadruple root has no two-vertex root resolution;
- a disjoint doubled pair has no two-vertex root resolution.

The four-cycle line is exactly the local DDD triality: the co-root route is the unique bad route and the two crossed routes are root-valued.

---

## 5. Four-cycle completions of the two exceptional types

### 5.1 Four equal boundary roots

Let

\[
a=ij
\]

be a root and choose a support index `k` outside `a`. Put

\[
x=ik,
\qquad
y=jk,
\qquad x+y=a.
\]

Take a four-cycle whose four boundary semiedges all have value `a` and whose internal cycle labels alternate

\[
x,y,x,y.
\]

At every cubic vertex the incident values are

\[
a,x,y,
\qquad a+x+y=0.
\]

Hence this is a connected root-valued four-port completion.

A two-vertex completion is impossible because every forced route sum is zero. Since a cubic four-pole with four semiedges has an even number of internal vertices, the four-cycle is vertex-minimal.

### 5.2 Two doubled disjoint roots

Let

\[
a=ij,
\qquad b=k\ell,
\qquad a\cap b=\varnothing.
\]

Choose one cross root

\[
x=ik.
\]

Order the boundary ports as

\[
\boxed{a,b,b,a}
\]

and join their four incident cubic vertices cyclically with internal labels

\[
\boxed{x,\ x+b,\ x,\ x+a.}
\]

All four displayed internal values are roots: `x` meets each of `a,b` once, and adding `a` or `b` replaces the chosen endpoint on the corresponding shore.

At the four vertices the conservation equations are respectively

\[
a+(x+a)+x=0,
\]

\[
b+x+(x+b)=0,
\]

\[
b+(x+b)+x=0,
\]

\[
a+x+(x+a)=0.
\]

Thus the square is a connected root-valued completion of the disjoint doubled boundary.

Again no two-vertex completion exists, because the route-sum weights are `(0,4,4)`. The square is therefore vertex-minimal.

---

## 6. Exact Type-T identification

A Petersen pivot backtrack

\[
s\longrightarrow t\longrightarrow s
\]

uses one Petersen edge

\[
\{s,t\},
\]

so `s,t` are disjoint roots. Its forced shore-resolution word is

\[
\boxed{t,s,s,t.}
\]

Therefore the Type-T `abba` word is exactly the disjoint doubled-root route-sum orbit

\[
\boxed{(0,4,4).}
\]

### Theorem 6.1 — Type-T square normal form

Every Type-T boundary word

\[
a,b,b,a,
\qquad a\cap b=\varnothing,
\]

has the canonical four-cycle root completion of §5.2.

The completion is unique up to:

1. the choice of one of the four cross roots between the two shores of `a` and `b`;
2. the stabiliser action of the disjoint pair `\{a,b\}`;
3. reversal of the square.

No new coefficient or route-sum state occurs.

---

## 7. The support response is forced by the boundary word

Let the ordered ports be

\[
1,2,3,4
\]

with boundary word

\[
a,b,b,a
\]

and serial matching

\[
M_T=14\mid23.
\]

Because `a,b` are disjoint:

- each of the two support indices of `a` occurs on exactly ports `1,4`;
- each of the two support indices of `b` occurs on exactly ports `2,3`;
- the fifth support index occurs on no boundary port.

### Theorem 7.1 — forced serial support response

For **every** root-valued multipole with this boundary word, each active support subgraph has exactly two boundary ends and therefore connects:

\[
1\longleftrightarrow4
\]

or

\[
2\longleftrightarrow3,
\]

according to whether the support index belongs to `a` or `b`.

Hence the complete support-unordered boundary response is forced:

\[
\boxed{M_T=14\mid23.}
\]

In particular, the canonical square and any larger root-valued Type-T realisation have the same fixed-boundary support response. Closed internal support cycles may differ, but the external support pairing cannot.

### Proof

For one support coordinate, its selected edge set is an even subgraph. If exactly two boundary semiedges carry that support, they must lie in the same path component; all other components are closed cycles. The boundary word identifies the two ends exactly as displayed. ∎

---

## 8. Fixed-boundary response congruence

### Lemma 8.1

Let `P,P'` be root-valued multipoles with the same ordered ports and identical root values on those ports. Suppose that for every support coordinate the induced equivalence relation on the selected boundary ports is the same in `P` and `P'`.

Then gluing either multipole to the same root-valued outside system produces identical support connectivity outside the replaced region. The two global support systems differ only by internal closed cycles and by the internal realisation of the same boundary paths.

### Proof

For each support coordinate, global components are obtained by taking the transitive closure of:

1. the outside connectivity relation on selected ports;
2. the inside connectivity relation on selected ports.

The outside relation is fixed and the inside relations agree by hypothesis. Therefore the global boundary connectivity agrees. Internal components disjoint from the ports are closed and do not affect the outside relation. ∎

### Corollary 8.2 — fixed-state Type-T retract

At one fixed Type-T boundary state `a,b,b,a`, every larger root-valued realisation is response-congruent to the canonical square.

Thus external side attachments do not create a new **support-response** state once they have been enclosed inside a genuine four-port region.

---

## 9. Composition boundary

The theorem closes the fixed-boundary Type-T normal form but not the entire graph-inductive transfer.

For a strict graph reduction replacing a large Type-T region by the square, one still needs one of the following legitimate frameworks.

1. **Horizontal/fixed-state descent:** the proof continues inside the same boundary state, so Corollary 8.2 is sufficient.
2. **Universal inductive replacement:** every boundary state realised by a cover of the reduced graph must lift through the original region. This requires state-set inclusion, not merely equality for the presently marked `abba` state.
3. **Separator decomposition:** the four ports are cut and the two shores are solved and glued with a boundary-state alignment theorem.

This distinction is essential. The present dossier does not promote fixed-state response congruence to universal state-set inclusion.

---

## 10. Revised Type-T frontier

The source-side Type-T problem is now reduced to:

\[
\boxed{
\text{enclose the `abba` backtrack as a genuine four-port region}
}
\]

and then prove one of:

1. fixed-state horizontal replacement by the canonical square;
2. a smaller four-pole/separator;
3. profile escape before enclosure;
4. universal state-set inclusion for the chosen graph-inductive reducer.

The coefficient word and the minimal root-valued serial carrier are no longer open.

---

## 11. Trust boundary

### Exact here

- complete classification of conserved four-root boundary multisets;
- complete `(0,0,0)/(0,2,2)/(0,4,4)/(2,2,4)` route-sum table;
- exact identification of the DDD and Type-T route-sum orbits;
- explicit minimal four-cycle completions for the two exceptional no-root-route types;
- identification of Petersen `abba` with the disjoint doubled-root orbit;
- forced serial support response for every root-valued `abba` multipole;
- fixed-boundary response congruence and the canonical Type-T square retract.

### Still open

- enclosure of every physical Type-T backtrack together with its external side attachments into one genuine four-port region;
- universal state-set inclusion for graph-inductive replacement;
- treatment of covers of the reduced graph whose square boundary state is not the marked `abba` state;
- integration with the bounded return-cell table;
- a global well-founded descent theorem and horizontal induction;
- the global five-support theorem.
