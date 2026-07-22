# Six-leaf pivot topology has only zero/DDD singular minima

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `0a206df85fd8a07945e5b92bc68379b92bfb572c`  

**Parents:**

- `projects/affine-cdc/research/PIVOT_CHANGE_SIX_PORT_STAR_COMPLETION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_PIVOT_RESOLUTION_V1.md`;
- `projects/affine-cdc/research/TIGHT_THREE_CLASS_FORCED_PAIR_COCIRCUIT_V1.md`;
- the defect-minimal forest and zero/DDD local grammar.

**Status:** complete finite classification of every unrooted binary cubic topology on the six labelled boundary roots of one pivot-change cell. There are `105` labelled six-leaf trees. Their internal split labels have defect energy `0,1,2,3` with counts `20,45,36,4`. Under nearest-neighbour interchange, every positive-energy topology has an immediate lower-energy neighbour except fifteen energy-one local minima. Those fifteen split into five three-cycles. Each three-cycle has one zero-defect topology and two co-root-defect topologies carrying the same co-root direction; its two root internal labels are one disjoint root pair, equivalently one Petersen-edge/DDD state. Thus the local topology landscape has no singular minimum beyond the already known equality/DDD triality.  

**Not implied:** that a nearest-neighbour interchange is automatically a physical Kempe move or a cover-preserving source replacement, that every topology descent preserves bridgelessness, completion of the spine--attachment theorem, global induction, canonical acceptance, Lean verification, manuscript integration, or the global five-support theorem.

---

## 1. Standard pivot boundary

By `S_5` symmetry use the standard six-port pivot-change boundary

\[
(s,x,z\mid w,t,y)
=
(12,35,45\mid25,34,15).
\]

The total boundary sum is zero.

Let `T` be an unrooted binary cubic tree with these six labelled leaves. Such a tree has:

- six leaf edges;
- four internal cubic vertices;
- three internal edges.

Every internal edge `e` determines a bipartition

\[
A_e\mid A_e^c
\]

of the six leaves. Conservation forces its `E_5` label to be

\[
\lambda_T(e)=\sum_{p\in A_e}r_p.
\]

The total boundary sum is zero, so either shore gives the same label.

### Definition 1.1 — topology defect energy

Put

\[
\boxed{
E(T)
=
\#\{e\text{ internal}:\lambda_T(e)\notin R_5\}.
}
\]

The only possible internal weights are `0,2,4`; therefore an internal edge is:

- root-valued when its weight is `2`;
- a zero defect when its weight is `0`;
- a co-root defect when its weight is `4`.

The tree is a root-valued six-port completion exactly when

\[
E(T)=0.
\]

---

## 2. Complete topology census

The number of unrooted binary trees with six labelled leaves is

\[
(2\cdot6-5)!!=7!!=105.
\]

Exact enumeration gives:

\[
\boxed{
\begin{array}{c|cccc}
E(T)&0&1&2&3\\
\hline
\#T&20&45&36&4.
\end{array}}
\]

The complete internal weight-pattern table is

\[
\boxed{
\begin{array}{c|c}
\text{sorted internal weights}&\#T\\
\hline
(2,2,2)&20\\
(0,2,2)&9\\
(2,2,4)&36\\
(2,4,4)&36\\
(4,4,4)&4.
\end{array}}
\]

Thus:

- all twenty energy-zero trees are root-valued completions;
- every energy-one tree has exactly one zero or one co-root internal edge;
- no other defect weight occurs.

---

## 3. NNI graph

Two six-leaf trees are adjacent when they differ by one nearest-neighbour interchange on an internal edge.

Let

\[
\mathcal N_6
\]

be the resulting graph on the `105` labelled topologies.

### Theorem 3.1 — basic NNI census

\[
\boxed{
|V(\mathcal N_6)|=105,
\qquad
|E(\mathcal N_6)|=315.
}
\]

Every vertex has degree six.

The induced graph on the twenty root-valued trees has:

\[
\boxed{
20\text{ vertices},
\qquad30\text{ edges},
\qquad\deg=3,
}
\]

and is connected.

Hence the root-valued topology sector is itself one connected finite reconfiguration space.

---

## 4. Strict descent table

For a topology `T`, let

\[
d_-(T)
=
\#\{T'\sim T:E(T')<E(T)\}.
\]

The exact distribution is

\[
\boxed{
\begin{array}{c|c|c}
E(T)&d_-(T)&\#T\\
\hline
0&0&20\\
1&2&30\\
1&0&15\\
2&2&32\\
2&4&4\\
3&4&4.
\end{array}}
\]

Consequently:

### Theorem 4.1 — all non-singular topologies descend

Every positive-energy topology has an adjacent topology of lower energy except exactly fifteen energy-one local minima.

There is no energy-two or energy-three local minimum.

Thus the complete local obstruction to topology-energy descent is a finite fifteen-state set.

---

## 5. The fifteen singular minima

At each of the fifteen local minima:

1. two internal edges are roots;
2. those two roots are disjoint;
3. the third internal edge is either zero or their co-root sum.

Let the two root labels be

\[
a,b\in R_5,
\qquad a\cap b=\varnothing.
\]

Let `m` be the unique support index outside `a union b`.

The fifteen minima divide into five fibres, one for each realised disjoint pair:

\[
\boxed{
\begin{array}{c|c}
\{a,b\}&m\\
\hline
\{34,25\}&1\\
\{12,34\}&5\\
\{12,45\}&3\\
\{12,35\}&4\\
\{34,15\}&2.
\end{array}}
\]

Each fibre contains exactly three topologies.

### Theorem 5.1 — zero/DDD triality fibre

For every fibre labelled by the disjoint pair `{a,b}`:

- one topology has internal defect label
  \[
  0;
  \]
- two topologies have internal defect label
  \[
  a+b,
  \]
  the common co-root on the four support indices of `a union b`;
- the three topologies are pairwise NNI-adjacent and form a triangle.

Hence each singular fibre has the exact local alphabet

\[
\boxed{
\text{one equality/zero state}
\quad+\quad
\text{two crossed DDD states}.}
\]

The disjoint root pair `{a,b}` is one Petersen edge, equivalently one one-factor/DDD atom state.

### Interpretation

The three topology minima are not three new defect species. They are the topology-level triality of one already known singular fibre:

\[
\{0,a+b\}
\]

together with the two crossed placements of the co-root state.

---

## 6. No third local minimum mechanism

Combining the descent table and the triality classification:

### Theorem 6.1 — complete topology normal form

Every labelled six-leaf pivot topology enters one of:

1. a root-valued topology;
2. an NNI step of strictly smaller defect energy;
3. one bounded zero/DDD triality fibre.

Equivalently,

\[
\boxed{
\text{six-leaf topology obstruction}
\Longrightarrow
\text{root completion / strict energy descent / zero--DDD atom}.}
\]

There is no independent rank-three or higher local topology minimum.

This conclusion is compatible with the independent reductions by:

- quadratic singular fibres;
- inverse-dipole equality/DDD rescue;
- Petersen pivot transport;
- the six-port star table;
- Type-H BBD/DDD triangle classification.

---

## 7. Relation to the four star routes

The four root-valued three-cherry star completions from the pivot-change star theorem are four of the twenty energy-zero trees.

The larger count `20` shows that the four-star table is not the complete root topology profile; path-shaped and other labelled trees also give root completions.

This is useful strategically:

- a proof need not force one particular star topology;
- any physical source surgery reaching the connected twenty-state root sector suffices;
- every failure to descend topology energy is already a zero/DDD singular fibre.

Thus the correct final composition target may be stated in topology-invariant form rather than in terms of one distinguished star gadget.

---

## 8. Physical calibration target

NNI is a move in the finite topology space. It is not automatically a legal operation on the original source graph.

To consume Theorem 6.1, prove the following physical statement.

### Target 8.1 — admissible NNI or enclosure

Let `T` be the four-vertex source tree of a support-minimal pivot carrier and let `T'` be an NNI neighbour with

\[
E(T')<E(T).
\]

Then one of:

1. the NNI is realised by a root-fibre/Kempe rerouting in the same source graph;
2. an exterior linkage permits a composition-safe replacement by `T'`;
3. failure of the rerouting exposes a two-, three-, or four-edge separator;
4. the move is blocked by an empty fibre, a rank-one scalar cycle, or a rank-two Tait carrier;
5. the topology lies in one of the bounded zero/DDD triality fibres.

The first four outcomes give strict progress through already established modules; the fifth is bounded.

### Why this is the exact remaining distinction

The finite topology problem is now closed. The only open datum is whether a lowering NNI move can be realised through the actual exterior side semantics, or whether those semantics give the expected separator/low-rank certificate.

---

## 9. Exact finite certificate

The enumeration was performed as follows.

1. Generate all labelled unrooted binary six-leaf trees recursively by subdividing one edge and attaching the next leaf; quotient by internal-vertex relabelling.
2. For each of the `105` trees, compute its three internal terminal splits.
3. Xor the six fixed boundary roots across one shore of every split.
4. Count the non-root internal labels.
5. Generate all six NNI neighbours of every tree.
6. Compute the lower-energy degree and the induced graph on the local minima.
7. Group each minimum by its two root internal labels.

The calculation includes all tree shapes and all leaf labellings. No planarity, cyclic order, or symmetry reduction is assumed in the enumeration.

---

## 10. Trust boundary

### Exact here

- the `105` labelled six-leaf topology count;
- the complete energy and weight-pattern distributions;
- the `315`-edge six-regular NNI graph;
- connectivity and cubicity of the twenty-state root sector;
- the complete strict-descent table;
- the fifteen and only fifteen positive-energy local minima;
- their partition into five NNI triangles;
- the one-zero/two-common-co-root structure of every triangle;
- identification of each fibre with one Petersen-edge/DDD state.

### Finite/computational boundary

The census and adjacency statements are exhaustive finite calculations. A shorter orbit-theoretic proof is desirable but not required for the research certificate.

### Still open

- physical realisation of a lowering NNI move;
- separator extraction when exterior semantics block every lowering move;
- composition-safe transfer between source topologies;
- elimination of the bounded zero/DDD topology fibres inside the complete locked profile;
- global well-founded induction;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
