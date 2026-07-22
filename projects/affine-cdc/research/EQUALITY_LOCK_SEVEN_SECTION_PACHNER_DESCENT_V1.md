# Seven equality branch sections admit Pachner descent

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `b9667146b28e0d8a23ac1301aa678d916f832c02`.

**Parents:**

- `EQUALITY_LOCK_PRIVATE_MATCHING_TAIT_DECOMPOSITION_V1.md`;
- `EQUALITY_LOCK_TRIPLE_TAIT_PROJECTION_FAITHFULNESS_V1.md`;
- `ROOT_FLOW_TRIANGLE_COMPLEX_PACHNER_V1.md`;
- the category-safe NNI and equal-face cancellation lemmas.

**Status:** exact finite and graph-level descent theorem for a clean connected equality branch core in one adjacent-channel Tait projection. The seven branch sections have fifteen nontrivial adjacency pairs. Three pairs flip to private-matching subdivisions and strictly lower the total visibility in the three faithful projections. The other twelve pairs form six tetrahedral/DDD involutions; orienting the six zero-energy involutions away from the distinguished section `123` strictly lowers a secondary count. A connected four-port clean branch core with only `r`-coloured boundary cannot avoid all three progress moves. Therefore no clean equality branch core is locally irreducible.

**Not implied:** that one fixed projection remains connected after every decreasing flip, simultaneous preservation of all three ordered Tait responses, cover-independent transfer through an arbitrary flip sequence, elimination of the connected private-matching-decorated equality carrier, global proof-DAG closure, canonical acceptance, Lean verification, manuscript integration, or the global five-support theorem.

---

## 1. Normalised seven sections

Normalise

\[
r=12,
\qquad
s=13,
\qquad
t=23,
\qquad
d=45.
\]

Write a branch section in Tait-colour order `(r,s,t)`. The seven sections are

\[
\boxed{
\begin{array}{c|ccc}
123&12&23&13\\
124&12&14&24\\
125&12&15&25\\
134&34&14&13\\
135&35&15&13\\
234&34&23&24\\
235&35&23&25
\end{array}}
\]

They are exactly the seven support triangles not containing the private root `45`.

The three omitted triangles are

\[
145,
\qquad
245,
\qquad
345,
\]

and are the three private-matching subdivision types.

Two branch vertices can be joined by a Tait-colour edge exactly when their entries in that colour column are equal.

---

## 2. Equal sections

If two adjacent branch vertices carry the same section, all three root labels at their incident colour positions agree.

### Theorem 2.1 — forward root cancellation

An edge joining two identical branch sections admits equal-face dipole cancellation:

1. remove the two vertices and their common root edge;
2. reconnect the other two colour pairs;
3. each reconnected pair has equal root labels;
4. the inherited flow remains root-valued;
5. two source vertices are removed.

Category failure exposes the established small-cut or bounded-degeneration branch.

---

## 3. The three private-collapse flips

There are exactly three unordered nonidentical adjacency pairs whose tetrahedral root NNI leaves the seven-section branch set:

\[
\boxed{
\begin{aligned}
\{124,125\}&\longleftrightarrow\{145,245\},\\
\{134,135\}&\longleftrightarrow\{145,345\},\\
\{234,235\}&\longleftrightarrow\{245,345\}.
\end{aligned}}
\]

Their old and new central roots are respectively

\[
12\leftrightarrow45,
\qquad
13\leftrightarrow45,
\qquad
23\leftrightarrow45.
\]

### Theorem 3.1 — private-collapse Pachner move

In each line the forward arrow is the unique root-valued `2--2` Pachner flip. It replaces two branch vertices by two private-matching subdivision vertices and creates one private `45` edge.

The third local pairing has the four-support co-root missing `3`, `2`, or `1` respectively; hence each line is one root/root/co-root DDD triality.

---

## 4. Six branch-to-branch Pachner involutions

All remaining nontrivial branch adjacencies form exactly six flip involutions:

### Four-support sector `1234`

\[
\boxed{
\begin{aligned}
\{123,124\}&\longleftrightarrow\{134,234\},\\
\{123,134\}&\longleftrightarrow\{124,234\},\\
\{123,234\}&\longleftrightarrow\{124,134\}.
\end{aligned}}
\]

### Four-support sector `1235`

\[
\boxed{
\begin{aligned}
\{123,125\}&\longleftrightarrow\{135,235\},\\
\{123,135\}&\longleftrightarrow\{125,235\},\\
\{123,235\}&\longleftrightarrow\{125,135\}.
\end{aligned}}
\]

Every arrow is the unique root-valued tetrahedral NNI. In each tetrahedron the third pairing is the co-root on all four support indices.

Thus the six equations are precisely six DDD triality involutions, not a new equality-specific move.

---

## 5. Three-projection visibility energy

For a support triangle `T`, let

\[
\nu(T)
\]

be the number of the three equality Tait projections in which `T` is a branch vertex.

The triple-faithfulness theorem gives

\[
\boxed{
\nu(T)=
\begin{cases}
3,&12\subset T,\\
2,&|T\cap\{1,2\}|=1,\\
0,&T=345.
\end{cases}}
\]

For a root-labelled source region `R`, define

\[
\boxed{
E(R)=\sum_{v\in V(R)}\nu(\Delta_v).}
\]

### Theorem 5.1 — energy change of a tetrahedral flip

Across all thirty unordered adjacent distinct triangle pairs of the five-coloured triangle complex, a root Pachner flip changes `E` by

\[
-2,
\qquad
0,
\qquad
+2.
\]

The exact directed count is

\[
\boxed{9\text{ decreasing},\quad12\text{ neutral},\quad9\text{ increasing}.}
\]

For the seven branch sections:

1. each private-collapse flip of Section 3 decreases `E` by two;
2. each branch-to-branch involution of Section 4 preserves `E`.

### Proof

The section weights are:

\[
\nu(123)=\nu(124)=\nu(125)=3,
\]

\[
\nu(134)=\nu(135)=\nu(145)=
\nu(234)=\nu(235)=\nu(245)=2,
\]

\[
\nu(345)=0.
\]

Substitution in the fifteen tetrahedral pairing equations gives the result. The `9/12/9` count is the complete finite table over the five four-support tetrahedra. ∎

---

## 6. Secondary neutral energy

Fix the present projection with private root `45` and define

\[
N_{123}(R)
=|\{v:\Delta_v=123\}|.
\]

Orient every neutral involution of Section 4 from the side containing `123` to the side not containing `123`.

### Theorem 6.1

Every oriented neutral flip satisfies

\[
E(R')=E(R),
\qquad
N_{123}(R')=N_{123}(R)-1.
\]

Thus

\[
\boxed{(E,N_{123})}
\]

strictly decreases lexicographically under every private-collapse flip and every oriented neutral flip.

Equal-section cancellation also strictly decreases `E` because it removes two positive-visibility branch vertices.

---

## 7. Clean connected four-port cores cannot be stationary

Call a projected equality core **clean** when every source vertex is one of the seven branch sections; equivalently, it has no private `45` edge or matching-subdivision vertex.

Assume:

1. the clean core is connected;
2. its only boundary semiedges are the four marked semiedges;
3. all four boundary semiedges have Tait colour `r`;
4. every internal vertex has one incidence of each Tait colour `r,s,t`.

### Theorem 7.1 — clean-core Pachner descent

Every nonempty clean connected four-port equality core contains at least one of:

1. an edge joining identical branch sections, hence an equal-face cancellation;
2. one of the three private-collapse pairs, hence an `E`-decreasing root Pachner flip;
3. a branch-to-branch pair on the `123` side of one neutral involution, hence an `N_(123)`-decreasing root Pachner flip.

### Proof

Assume none occurs.

#### Step 1 — no `123` vertex

At a `123` vertex:

- its `s`-edge has root `23` and can meet only `123,234,235`;
- its `t`-edge has root `13` and can meet only `123,134,135`.

An identical neighbour is excluded. Every nonidentical neighbour is on the `123` side of one neutral involution and is also excluded. The `s`- and `t`-incidences cannot be boundary semiedges because every boundary semiedge has colour `r`.

Hence no `123` vertex exists.

#### Step 2 — sector separation

The remaining branch sections split into

\[
\mathcal A_4=\{124,134,234\},
\]

\[
\mathcal A_5=\{125,135,235\}.
\]

The only adjacency between the two sets is one of the private-collapse pairs

\[
124--125,
\qquad
134--135,
\qquad
234--235,
\]

which are excluded. Connectedness therefore places the whole core in one sector.

#### Step 3 — one internal colour cannot continue

Suppose the core lies in `A_4`.

- At a `134` vertex, the `t`-incidence has root `13`. Inside `A_4` no other section has `t`-root `13`; an internal continuation would therefore be identical, excluded. It cannot be boundary because boundary colour is `r`. Hence no `134` vertex exists.
- At a `234` vertex, the `s`-incidence has root `23`. The same argument excludes `234`.
- Only `124` remains. Its `s`- and `t`-incidences can then continue only to identical `124` vertices, again excluded.

Thus `A_4` cannot support a nonempty core.

The argument for `A_5` is identical:

- `135` has unique internal `t`-root `13`;
- `235` has unique internal `s`-root `23`;
- the remaining `125` vertices would require identical continuations.

Contradiction. ∎

### Corollary 7.2

There is no fourth clean local obstruction and no stationary clean equality branch core.

---

## 8. Exact finite certificate

Among ordered nonidentical branch-section adjacencies:

\[
\boxed{30}
\]

occur.

They split as:

\[
\boxed{6}
\]

ordered private-collapse inputs, and

\[
\boxed{24}
\]

ordered branch-to-branch DDD inputs.

Equivalently, unordered adjacencies split as:

\[
3
\]

private-collapse pairs and

\[
12
\]

branch-to-branch pairs arranged in six flip involutions.

For every nonidentical adjacency, the two off-edge root pairs are simultaneously:

- adjacent in exactly the three private-collapse unordered pairs;
- disjoint in the other twelve unordered pairs.

No mixed adjacent/disjoint pattern occurs.

The finite table was verified exactly in Wolfram Language. The human tetrahedral proof and the clean-core argument are controlling.

---

## 9. Relation to private-edge surgery and surface topology

A private-collapse flip may create matching subdivisions, so Theorem 7.1 is not by itself a global flip algorithm on one fixed projection.

The existing private-edge theorem supplies the complementary source surgeries:

- crossed private edge: root NNI removes one private edge and joins two Tait rails;
- aligned private edge: equal-label cancellation removes two source vertices;
- no cross-rail private edge: two-edge separator.

The triple-faithfulness theorem adds that a vertex hidden as a matching subdivision in one projection remains a branch vertex in the other two, except for the complementary triangle `345`, which is itself an ordinary rank-two Tait vertex of the blocked side network.

Thus the remaining connected equality theorem may adaptively alternate:

\[
\boxed{
\text{private-edge surgery}
\quad+
\text{clean-core Pachner descent}
\quad+
\text{Tait-surface curvature reduction}.}
\]

All three operations have finite local alphabets and category-safe small-cut exits.

---

## 10. Trust boundary

### Exact here

- complete seven-section table;
- equal-section root cancellation;
- three private-collapse Pachner flips;
- six branch-to-branch DDD involutions;
- total visibility energy and exact `9/12/9` flip count;
- secondary `N_(123)` orientation of neutral flips;
- exact clean connected four-port descent theorem;
- exact `6+24` ordered adjacency count;
- absence of a fourth local branch-section mechanism.

### Still open

- construction of one globally monotone measure when the active projection changes;
- proof that an adaptive sequence cannot cycle between private-edge and branch Pachner moves;
- simultaneous preservation or controlled change of the three ordered equality responses;
- cover-independent transfer of a cap-lifting state through the complete surgery sequence;
- global proof-DAG closure;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication, and the global five-support theorem.
