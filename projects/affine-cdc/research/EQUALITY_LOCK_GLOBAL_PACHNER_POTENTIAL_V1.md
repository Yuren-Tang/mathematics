# Full equality carriers admit a globally monotone Pachner descent

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent surface:** branch head containing `EQUALITY_LOCK_TWO_BOUNDARY_ANNULUS_REDUCTION_V1.md`.  

**Parents:**

- `ROOT_FLOW_TRIANGLE_COMPLEX_PACHNER_V1.md`;
- `EQUALITY_LOCK_TRIPLE_TAIT_PROJECTION_FAITHFULNESS_V1.md`;
- `EQUALITY_LOCK_SEVEN_SECTION_PACHNER_DESCENT_V1.md`;
- `EQUALITY_LOCK_PRIVATE_MATCHING_TAIT_DECOMPOSITION_V1.md`;
- `EQUALITY_LOCK_TWO_BOUNDARY_ANNULUS_REDUCTION_V1.md`;
- the category-safe root NNI and equal-face cancellation lemmas.

**Status:** exact correction and strengthening. The seven-section dossier correctly identifies the local Pachner alphabet and proves a clean-core descent, but its statement that all six displayed branch-to-branch involutions are visibility-neutral is false: two of them lower the three-projection visibility by two. After correcting the complete thirty-pair table, one obtains a projection-independent lexicographic potential on all ten support-triangle types. Every nonempty root-labelled cubic four-pole whose four boundary semiedges all carry the equality root has either an equal-face cancellation or a strictly potential-lowering root Pachner flip. This includes all private-matching subdivision vertices. Hence adaptive changes of equality projection cannot cycle at the current-flow level.

**Not implied:** preservation of the complete five-support boundary profile under every flip, cover-independent inverse transfer of an arbitrary root cover through the resulting history, elimination of the final bounded direct-pairing atom, global proof-DAG closure, canonical acceptance, Lean verification, manuscript integration, release, publication, or the global five-support theorem.

---

## 1. Normalisation and all ten triangle states

Fix the active equality root

\[
r=12.
\]

The ten local root-flow states are the ten support triangles

\[
\binom{[5]}3.
\]

At a cubic source vertex of type `ijk`, the three incident root labels are

\[
ij,ik,jk.
\]

A source edge joins two triangle types exactly when they share its root label. Equal adjacent triangle types admit the label-preserving two-face cancellation. Distinct adjacent triangle types lie in one four-support tetrahedron and admit exactly one nontrivial root-valued `2--2` Pachner flip.

The four boundary semiedges of the equality carrier all have label

\[
12.
\]

No other root label may occur on the boundary of the selected four-pole.

---

## 2. Primary three-projection visibility

Let

\[
\nu(T)
\]

be the number of the three adjacent-channel equality Tait projections in which the support triangle `T` is a genuine branch vertex. Triple faithfulness gives

\[
\boxed{
\nu(T)=
\begin{cases}
3,&12\subset T,\\
0,&T=345,\\
2,&\text{otherwise}.
\end{cases}}
\]

Thus

\[
\nu(123)=\nu(124)=\nu(125)=3,
\]

\[
\nu(134)=\nu(135)=\nu(145)
=\nu(234)=\nu(235)=\nu(245)=2,
\]

and

\[
\nu(345)=0.
\]

For a root-labelled source region `R`, define

\[
\boxed{
E(R)=\sum_{v\in V(R)}\nu(\Delta_v).}
\]

For the thirty unordered adjacent distinct triangle pairs, exact evaluation of the tetrahedral flip gives

\[
\boxed{
9\text{ directions lower }E,
\quad12\text{ preserve }E,
\quad9\text{ raise }E.}
\]

### Correction 2.1 — seven-section energy statement

The branch-to-branch flips

\[
\boxed{
\{123,124\}\longleftrightarrow\{134,234\},}
\]

and

\[
\boxed{
\{123,125\}\longleftrightarrow\{135,235\}}
\]

are not visibility-neutral. In the displayed directions their old pair has weight `6` and their new pair has weight `4`, so each lowers `E` by two.

Therefore the claims in `EQUALITY_LOCK_SEVEN_SECTION_PACHNER_DESCENT_V1.md` that all six displayed branch-to-branch involutions preserve `E`, and that only the three private-collapse pairs lower `E`, are quarantined. Its local adjacency list and clean-core nonstationarity conclusion remain usable after this corrected energy accounting.

---

## 3. A global secondary potential

The twelve `E`-neutral adjacent pairs form six flip involutions. Define a triangle weight

\[
\phi(T)=
\begin{cases}
1,&T=124,\\
3,&T=125,\\
0,&\text{otherwise}.
\end{cases}
\]

and put

\[
\boxed{
\Phi(R)=\sum_{v\in V(R)}\phi(\Delta_v)
=N_{124}(R)+3N_{125}(R).}
\]

For the six `E`-neutral involutions, orient the flip from the larger `Phi`-sum to the smaller `Phi`-sum. Explicitly, the lower sides are

\[
\boxed{
\{123,134\}
<
\{124,234\},}
\]

\[
\boxed{
\{123,135\}
<
\{125,235\},}
\]

\[
\boxed{
\{123,234\}
<
\{124,134\},}
\]

\[
\boxed{
\{123,235\}
<
\{125,135\},}
\]

\[
\boxed{
\{124,145\}
<
\{125,245\},}
\]

and

\[
\boxed{
\{124,245\}
<
\{125,145\}.}
\]

Here `<` means that the left pair has smaller `Phi`-sum. The inequalities are respectively

\[
0<1,
\quad0<3,
\quad0<1,
\quad0<3,
\quad1<3,
\quad1<3.
\]

Hence none of the twelve `E`-neutral adjacent pairs remains tied after `Phi` is added.

### Theorem 3.1 — exact `15/15` split

Order root Pachner flips lexicographically by

\[
(E,\Phi).
\]

Among the thirty unordered adjacent distinct triangle pairs:

\[
\boxed{
15\text{ current pairs admit a strictly decreasing flip},}
\]

and

\[
\boxed{
15\text{ are the lower side of their flip}.}
\]

There is no tie.

The finite census is:

- `9` pairs lower `E`;
- of the `12` `E`-neutral pairs, exactly `6` lower `Phi` and `6` raise it;
- the remaining `9` raise `E`.

---

## 4. Complete nondecreasing adjacency table

Assume a distinct adjacent triangle pair does **not** admit a lexicographically decreasing root flip. Group the fifteen possible current pairs by their common root edge.

\[
\boxed{
\begin{array}{c|l}
\text{common root}&\text{allowed nondecreasing adjacent pairs}\\
\hline
12&\varnothing\\
13&123\!-\!134,\ 123\!-\!135\\
14&124\!-\!145\\
15&\varnothing\\
23&123\!-\!234,\ 123\!-\!235\\
24&124\!-\!245\\
25&\varnothing\\
34&134\!-\!234,\ 134\!-\!345,\ 234\!-\!345\\
35&135\!-\!235,\ 135\!-\!345,\ 235\!-\!345\\
45&145\!-\!245,\ 145\!-\!345,\ 245\!-\!345.
\end{array}}
\]

Equal adjacent types are omitted because they admit the two-face cancellation.

### Exact finite certificate

Direct enumeration of all thirty adjacent distinct pairs verifies:

\[
\boxed{
30=15\text{ decreasing}+15\text{ nondecreasing},}
\]

with the displayed root-by-root table. The human proof below uses only this table. An independent Wolfram evaluation produced the same `30/15/15/0-tie` census.

---

## 5. No nonempty four-port local minimum

### Theorem 5.1 — full ten-triangle Pachner descent

Let `R` be a nonempty connected cubic multipole with a root-valued `E_5` flow such that:

1. `R` has exactly four boundary semiedges;
2. every boundary semiedge has root label `12`;
3. every internal source vertex is one of the ten support triangles.

Then `R` contains at least one of:

1. an edge joining two equal support triangles, hence an equal-face cancellation;
2. an adjacent distinct triangle pair whose root Pachner flip strictly lowers
   \[
   (E,\Phi).
   \]

### Proof

Assume neither move exists. Then every internal edge must use one of the nondecreasing distinct pairs in the table of Section 4.

#### Step 1 — no internal `12` edge

The `12` row is empty. Therefore every `12` incidence is a boundary incidence. In particular the only possible boundary vertices are

\[
123,124,125.
\]

#### Step 2 — eliminate all triangles using `15` or `25`

The `15` row is empty. Every occurrence of a triangle containing root `15` would require an internal continuation of its `15` incidence, because the only boundary root is `12`. Hence

\[
125,135,145
\]

cannot occur.

Likewise the `25` row is empty, so

\[
125,235,245
\]

cannot occur.

Thus all triangle types involving support index `5`, except possibly `345`, are absent.

#### Step 3 — eliminate the `4`-sector mixed and active triangles

The only nondecreasing `14` pair is

\[
124-145.
\]

But `145` is already absent. Therefore neither `124` nor `134` can satisfy its internal `14` incidence, so both are absent.

The only nondecreasing `24` pair is

\[
124-245.
\]

Both `124` and `245` are absent. Hence `234` cannot satisfy its `24` incidence and is absent.

#### Step 4 — eliminate the last two types

Only `123` and `345` remain.

A `123` vertex needs internal `13` and `23` continuations. The table allows those only through

\[
134,135,234,235,
\]

all of which are absent. Hence `123` is absent.

A `345` vertex needs internal `34`, `35`, and `45` continuations. Equal `345-345` adjacency is excluded by hypothesis, and every distinct allowed neighbour in those rows is one of the already eliminated mixed types. Hence `345` is absent.

No source vertex remains, contradicting that `R` is nonempty and has four boundary semiedges. ∎

---

## 6. One globally monotone surgery measure

Define

\[
\boxed{
\mathcal P(R)=igl(E(R),\Phi(R),|V(R)|\bigr)}
\]

with lexicographic order.

### Theorem 6.1 — every selected local surgery lowers `P`

1. A distinct-triangle root Pachner flip selected by Theorem 5.1 leaves `|V|` unchanged and strictly lowers `(E,Phi)`.
2. An equal-face cancellation removes two vertices. Since `nu,phi` are nonnegative, it either lowers `E`, or preserves `E` and lowers `Phi`, or preserves both and lowers `|V|` by two. Thus it strictly lowers `P` in every triangle type, including the zero-visibility complementary type `345`.

Therefore an adaptive sequence of root flips and equal-face cancellations chosen by Theorem 5.1 cannot cycle, even when the active equality Tait projection changes.

### Corollary 6.2 — finite current-flow reduction

Starting from any connected root-labelled equality four-pole, repeatedly perform the guaranteed local move whenever the modified graph remains in the connected bridgeless cubic category.

Because `P` is well founded, the process terminates after finitely many steps. Before termination, exactly one of:

1. a category-safe move continues with smaller `P`;
2. category failure exposes a two-, three-, or four-edge separator or a bounded loop/parallel/acyclic degeneration;
3. all source vertices of the selected region disappear, leaving a zero-vertex four-port matching, hence one bounded direct-pairing terminal.

There is no infinite alternation between private-edge surgery, a different equality projection, and branch Pachner moves.

---

## 7. Interaction with the annulus theorem

The two-boundary theorem proves independently that a connected double-equal Tait projection has only:

- one annular zero-Euler species;
- a six-vertex identity-hexagon minimum;
- or negative-Euler dipole descent to a matching flip or boundary degeneration.

The present theorem is complementary and stronger at the root-labelled source level:

1. it retains all ten support-triangle sections rather than suppressing private matching subdivisions;
2. it does not require choosing a fixed Tait surface throughout the descent;
3. it supplies one explicit monotone measure when the active projection changes;
4. it rules out adaptive flip cycles before any topological compression is invoked.

Thus the remaining equality burden is no longer topological termination or local-move termination.

---

## 8. Revised equality frontier

### Closed here

- the energy-accounting error in the seven-section packet;
- a secondary potential resolving all twelve primary-neutral pairs;
- the exact `15/15` flip orientation;
- the complete nondecreasing adjacency table;
- absence of a nonempty local minimum among all ten triangle types;
- one globally monotone current-flow measure;
- termination of adaptive projection changes at a separator, degeneration, or bounded direct-pairing terminal.

### Still open

The surviving obligation is transfer rather than descent:

> Given a cap-compatible root state obtained at the bounded terminal or after a route-changing event, transfer it back through the finite Pachner/cancellation history, or show that the first failed inverse transfer is one already classified zero/co-root one-edge atom, DDD triality, small separator, or strictly smaller enclosed equality lock.

Equivalently, one still needs:

- cover-independent inverse transfer through a finite mixed surgery history;
- controlled conversion of an inverse-transfer failure into the established defect-tree / one-edge-atom grammar;
- final consumption of the bounded direct-pairing terminal;
- global well-founded proof-DAG assembly.

No new coefficient, selector, surface, or local-surgery obstruction remains.