# Every nonempty five-leaf root-topology sector is one cycle `C5` or `C6`

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `6489818dc5781f2822c857822126490dbee5a950`.

**Parents:**

- `FIVE_LEAF_PACHNER_PENTAGON_ROOT_INTERVAL_V1.md`;
- `ROOT_FLOW_TRIANGLE_COMPLEX_PACHNER_V1.md`;
- `SIX_LEAF_NNI_ROOT_EXCHANGE_V1.md`;
- the `K_5` root model and Eulerian boundary law.

**Status:** exact complete classification of the root-valued NNI sector for every ordered conserved five-root boundary. Among the fifteen labelled unrooted cubic five-leaf topologies, the root-valued induced subgraph is always exactly one of `empty`, `C5`, or `C6`. The boundary-root multiset gives a human classification: a five-cycle in the support `K5` produces the `C5` sector; a support triangle plus one doubled root produces `C6` unless the doubled root is the complementary edge disjoint from the triangle, in which case the sector is empty. Exact counts are `600` empty words, `1440` `C5` words, and `4200` `C6` words.

**Not implied:** automatic physical identification of the `C5` topology circuit with the oriented Petersen/DDD five-cycle carrier, elimination of a full one-atom lap around either cycle, global contextual-transfer synthesis, final proof-DAG closure, canonical acceptance, Lean verification, manuscript integration, release, publication, or the global five-support theorem.

---

## 1. Five boundary roots as an Eulerian support multigraph

Let

\[
(r_1,r_2,r_3,r_4,r_5)\in R_5^5
\]

be an ordered boundary word with

\[
\boxed{r_1+r_2+r_3+r_4+r_5=0.}
\]

Identify each root with one edge of the support graph `K_5`. Let `M` be the resulting five-edge multigraph on the five support vertices; repeated roots are repeated edges.

The vector sum is zero exactly when every support coordinate occurs an even number of times. Therefore:

### Lemma 1.1 — Eulerian boundary law

The support multigraph `M` is Eulerian: every support vertex has even degree.

Conversely every ordered list of five edges forming an Eulerian multigraph gives a conserved five-root boundary word.

---

## 2. Complete five-edge Eulerian classification

A loopless finite Eulerian multigraph decomposes into edge-disjoint cycles. A two-cycle is a doubled parallel edge. Since `M` has exactly five edges and no loops, the cycle-length partition is exactly one of:

\[
\boxed{5}
\]

or

\[
\boxed{3+2.}
\]

### Theorem 2.1 — boundary multiset dichotomy

Every conserved five-root boundary word has exactly one of the following support forms.

1. **Five-cycle form.**  
   The five roots are distinct and are the five edges of one simple support cycle `C_5`.

2. **Triangle plus doubled root.**  
   Three distinct roots form one support triangle and a fourth root occurs twice.

The doubled root may itself be one triangle edge, may meet the triangle in one support vertex, or may be the unique complementary edge disjoint from the triangle.

No other multiset occurs.

---

## 3. Five-leaf topologies as two-matchings

Label the five external branches by `1,2,3,4,5`. An unrooted cubic five-leaf topology consists of:

- two disjoint cherries, each a two-element subset of the leaves;
- one remaining singleton leaf.

Thus a topology is one two-edge matching in the complete graph on the five boundary positions.

Define the **root-adjacency graph** `H_r` on the five boundary positions by

\[
uv\in E(H_r)
\quad\Longleftrightarrow\quad
r_u+r_v\in R_5.
\]

For roots this means that `r_u,r_v` are distinct and meet in one support index.

### Lemma 3.1 — topology/matching dictionary

A five-leaf topology is root-valued exactly when its two cherries form a size-two matching in `H_r`.

### Proof

Each cherry sum is the root on the corresponding internal edge. If both cherry sums are roots, conservation forces the central vertex to carry three roots summing to zero. Conversely every root-valued tree has root-valued cherry sums. ∎

Two root-valued five-leaf topologies are joined by one root NNI exactly when their two-matchings share one edge. Therefore the root-topology graph is the graph of size-two matchings of `H_r`, with adjacency by one common matching edge.

---

## 4. Five-cycle boundary gives a root `C5`

Assume the support multigraph `M` is a simple five-cycle. Two boundary roots meet exactly when their support-cycle edges are consecutive. Hence

\[
\boxed{H_r\cong C_5.}
\]

The size-two matchings of a five-cycle are obtained by choosing two nonadjacent cycle edges. There are exactly five.

Two such matchings share one edge exactly when their omitted support-cycle vertices are consecutive. Their exchange graph is again a five-cycle.

### Theorem 4.1 — five-cycle sector

For a five-cycle boundary multiset, the complete root-valued five-leaf topology graph is

\[
\boxed{C_5.}
\]

It has five root-valued topologies and five root-preserving NNI edges.

---

## 5. Triangle plus doubled root

Let the three simple-cycle roots form a support triangle on vertices

\[
\{a,b,c\}
\]

with edges

\[
ab,ac,bc.
\]

Let the doubled root be

\[
g.
\]

There are five boundary positions: one for each triangle edge and two positions carrying `g`.

The two `g` positions are not adjacent in `H_r`, because equal roots sum to zero.

Exactly three geometric subcases occur.

### Case 5.1 — `g` is the complementary disjoint edge

Let

\[
\{d,e\}=[5]\setminus\{a,b,c\}
\]

and assume

\[
g=de.
\]

Then `g` is disjoint from every triangle edge. The graph `H_r` is one triangle on the three simple roots plus two isolated vertices.

A triangle has matching number one, so `H_r` has no size-two matching.

### Theorem 5.1 — empty complementary sector

If the doubled root is the edge complementary to the support triangle, then no five-leaf topology is root-valued:

\[
\boxed{\Sigma_5=\varnothing.}
\]

### Case 5.2 — `g` meets the triangle but is not a triangle edge

After relabelling, take

\[
g=ad
\]

with `d` outside the triangle. The root `g` meets exactly the two triangle edges through `a`, namely `ab,ac`, and is disjoint from `bc`.

Thus `H_r` consists of:

- the triangle on `ab,ac,bc`;
- two nonadjacent twin vertices, each joined to `ab,ac`.

A direct matching check gives six size-two matchings. Under one-edge exchange they form one six-cycle.

### Case 5.3 — `g` is one triangle edge

After relabelling, take

\[
g=ab.
\]

There are three boundary positions carrying the same root `ab`, and one each carrying `ac,bc`.

The three equal-root positions are pairwise nonadjacent in `H_r`. Each is adjacent to both `ac` and `bc`, and `ac,bc` are adjacent to each other.

Again there are exactly six size-two matchings, and their one-edge exchange graph is one six-cycle.

### Theorem 5.2 — all noncomplementary doubled sectors are `C6`

If the doubled root is not the complementary edge disjoint from the support triangle, then the complete root-valued topology graph is

\[
\boxed{C_6.}
\]

This includes both:

- a doubled triangle edge;
- a doubled root meeting the triangle in one support vertex.

---

## 6. Complete root-topology cycle theorem

### Theorem 6.1

For every ordered conserved five-root boundary word, the induced graph of root-valued topologies among all fifteen labelled five-leaf cubic trees is exactly one of:

\[
\boxed{
\varnothing,
\qquad C_5,
\qquad C_6.}
\]

More precisely:

\[
\begin{array}{c|c}
\text{support boundary multiset}&\text{root topology sector}\\
\hline
\text{simple support }C_5&C_5\\
\text{triangle + noncomplementary doubled root}&C_6\\
\text{triangle + complementary doubled root}&\varnothing.
\end{array}
\]

Consequently every nonempty root sector is:

- connected;
- 2-regular;
- one simple cycle;
- free of branching or multiple components.

### Corollary 6.2 — complete boundary-preserving reconfiguration

For any fixed conserved five-root boundary word, every two root-valued five-leaf topologies are connected by a sequence of boundary-preserving root NNIs.

The reconfiguration path lies in one cycle of length five or six.

---

## 7. Exact ordered-word census

There are

\[
\boxed{6240}
\]

ordered conserved five-root boundary words.

### Five-cycle words

There are `12` simple five-cycles in `K_5`. Ordering their five distinct edges gives

\[
12\cdot5!=1440
\]

words.

Each has root topology sector `C_5`.

### Empty triangle/complement words

Choose the support triangle in

\[
\binom53=10
\]

ways. Its complementary edge is unique. Ordering the three distinct triangle roots and two identical copies of the complementary edge gives

\[
\frac{5!}{2!}=60
\]

words per triangle. Hence

\[
10\cdot60=600
\]

empty-sector words.

### `C6` triangle/double words

The remaining words have a triangle and a noncomplementary doubled root. Their number is

\[
6240-1440-600=4200.
\]

Each has root topology sector `C_6`.

### Theorem 7.1 — exact census

\[
\boxed{
600\text{ empty}
\quad+\quad
1440\text{ with }C_5
\quad+\quad
4200\text{ with }C_6
=6240.}
\]

An independent exact enumeration of all fifteen topologies and all `6240` words gives the same classification. The Eulerian multigraph proof is controlling.

---

## 8. Consequence for critical-overlap circuits

The five-leaf pentagon theorem showed that one overlapping pair has no disconnected root sector. The present theorem strengthens this globally across all fifteen local topologies.

A returned boundary word interacting repeatedly with overlapping Pachner moves can therefore do only one of:

1. remain in one root reconfiguration cycle `C_5`;
2. remain in one root reconfiguration cycle `C_6`;
3. carry one equality/DDD first-failure atom at the boundary of an empty root sector.

There is no larger local root-transition graph and no branching circuit.

Thus a one-atom contextual-transfer failure can return to its starting topology only by completing one full lap of:

\[
\boxed{C_5\quad\text{or}\quad C_6.}
\]

This reduces the last global scheduling question to disposition of two bounded circuit types.

The expected interfaces are:

- `C_6`: even identity/equality return and the complete-profile identity-hexagon base;
- `C_5`: odd DDD/Petersen return and the established route/resolution parity machinery.

The exact physical identification of these circuits with those already calibrated carriers is the next theorem; it is not assumed here.

---

## 9. Trust boundary

### Exact here

- Eulerian support-multigraph law for five-root boundaries;
- complete `5` versus `3+2` cycle decomposition;
- topology/size-two-matching dictionary;
- root-sector `C_5` for support five-cycle boundaries;
- empty sector for triangle plus complementary doubled edge;
- root-sector `C_6` for every other triangle-plus-double boundary;
- complete `empty/C5/C6` theorem;
- connectedness and cycle structure of every nonempty sector;
- exact `600/1440/4200` census.

### Still open

- exact physical identification of the topology `C_6` with the equality identity-hexagon return carrier;
- exact physical identification of topology `C_5` with the oriented Petersen/DDD odd return carrier;
- elimination of one complete defect-token lap around either cycle;
- complete contextual-transfer synthesis;
- final proof-DAG audit and well-founded packaging;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication;
- the global five-support theorem.
