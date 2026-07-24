# The naked Petersen `C6` alternating star carriers are root-NNI connected

## Research Lead finite source certificate v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`;
- `PIVOT_CHANGE_SIX_PORT_STAR_COMPLETION_V1.md`;
- `TURN_COROLLA_POINTWISE_MATCHING_CHANGE_OBSTRUCTION_V1.md`.

**Status:** exact positive theorem for the undecorated minimal six-output carrier. The two checkerboard completions carrying canonical stars on the even matching `(01)(23)(45)` and the odd matching `(12)(34)(50)` are joined by an explicit sequence of twenty-three root-valued cubic NNIs. Every intermediate state is connected, loopless, cubic, has the same six ordered boundary semiedges, and carries a root on every edge.

The path necessarily deforms the pivot rails and turn incidences: eight moves are auxiliary, twelve use a turn spoke as active edge, and three use a pivot-rail edge as active edge. Therefore the theorem does not yet lift over arbitrary fixed resolved constant-pivot carriers. It supplies the finite naked path whose decorated source-faithful lift is now the exact R2.6 target.

---

## 1. Representative identity hexagon

Use the Petersen six-cycle of pivots

\[
\boxed{
(p_0,p_1,p_2,p_3,p_4,p_5)
=(34,12,35,14,23,15).
}
\]

Its side roots are

\[
z_i=p_{i-1}+p_{i+1},
\]

hence

\[
\boxed{
(z_0,z_1,z_2,z_3,z_4,z_5)
=(25,45,24,25,45,24).
}
\]

All indices are modulo six.

---

## 2. The naked rail carrier

Introduce six turn vertices

\[
R_0,\ldots,R_5.
\]

The even turn vertices form one root triangle rail:

\[
R_0R_2:12,
\qquad
R_2R_4:14,
\qquad
R_4R_0:15.
\]

The odd turn vertices form the other:

\[
R_1R_3:35,
\qquad
R_3R_5:23,
\qquad
R_5R_1:34.
\]

At `R_i`, the two rail roots and the third root `z_i` form the required turn triangle.

Let

\[
B_0,\ldots,B_5
\]

be six ordered boundary semiedges with values `z_i`.

For each star gadget use a centre `C_k` and a side-cherry vertex `S_k`.

---

## 3. Even checkerboard state

The even matching is

\[
M_{\rm ev}=\{01,23,45\}.
\]

For a matched pair `ij`, connect:

- `R_i` to the centre by root `z_i`;
- `R_j` to the centre by root `z_j`;
- the centre to the side cherry by root `z_i+z_j`;
- the side cherry to `B_i,B_j` by roots `z_i,z_j`.

Use:

\[
(C_0,S_0)\text{ on }01,
\quad
(C_1,S_1)\text{ on }23,
\quad
(C_2,S_2)\text{ on }45.
\]

Call the resulting complete root-valued six-pole

\[
\mathcal E.
\]

Every internal vertex is one root triangle.

---

## 4. Odd checkerboard state

The odd matching is

\[
M_{\rm odd}=\{12,34,50\}.
\]

Use the same twelve internal vertex slots, reassigned as follows:

\[
(C_1,S_0)\text{ on }12,
\quad
(C_2,S_1)\text{ on }34,
\quad
(C_0,S_2)\text{ on }50.
\]

The rail edges and the six ordered boundary semiedges remain exactly the same.

Call this root-valued six-pole

\[
\mathcal O.
\]

---

## 5. NNI notation

A row

\[
U{-}V:c\to c',
\qquad
X(\alpha)\leftrightarrow Y(\beta)
\]

means:

1. the active edge is `UV`, with old root `c`;
2. the branch `UX` of root `alpha` is exchanged with the branch `VY` of root `beta`;
3. all other incidences and edge labels are fixed;
4. the new central value is `c'`.

The row determines one ordinary cubic NNI uniquely.

Boundary vertices `B_i` are never active vertices and their ordered identities and root values remain fixed.

---

## 6. The twenty-three-move certificate

\[
\begin{array}{c|c|c|c}
\#&\text{active edge}&\text{central root}&\text{exchanged branches}\\
\hline
1&C_0S_0&24\to24&R_1(45)\leftrightarrow B_1(45)\\
2&R_5C_2&24\to35&R_3(23)\leftrightarrow R_4(45)\\
3&R_3C_2&23\to23&C_1(25)\leftrightarrow S_2(25)\\
4&R_1R_3&35\to24&S_0(45)\leftrightarrow C_2(23)\\
5&R_3S_2&25\to25&S_0(45)\leftrightarrow B_4(45)\\
6&S_0S_2&45\to45&B_0(25)\leftrightarrow R_3(25)\\
7&C_0S_0&24\to24&B_1(45)\leftrightarrow S_2(45)\\
8&R_1R_3&24\to35&C_2(23)\leftrightarrow B_4(45)\\
9&C_1S_1&45\to45&C_2(25)\leftrightarrow B_3(25)\\
10&S_1C_2&25\to34&B_2(24)\leftrightarrow R_5(35)\\
11&C_1S_1&45\to23&B_3(25)\leftrightarrow C_2(34)\\
12&R_3S_0&25\to34&C_2(23)\leftrightarrow B_1(45)\\
13&S_0C_2&23\to23&C_0(24)\leftrightarrow B_2(24)\\
14&R_3S_0&34\to25&B_1(45)\leftrightarrow C_2(23)\\
15&C_1C_2&34\to34&S_1(23)\leftrightarrow R_3(23)\\
16&R_3C_1&23\to45&S_0(25)\leftrightarrow C_2(34)\\
17&R_1R_5&34\to34&B_4(45)\leftrightarrow R_4(45)\\
18&R_5S_1&35\to24&B_4(45)\leftrightarrow C_2(23)\\
19&R_5C_2&23\to23&S_1(24)\leftrightarrow C_0(24)\\
20&R_2C_1&24\to15&R_4(14)\leftrightarrow S_0(25)\\
21&R_4C_1&14\to14&R_1(45)\leftrightarrow R_3(45)\\
22&R_3C_2&34\to25&R_4(45)\leftrightarrow R_5(23)\\
23&R_2C_1&15\to24&S_0(25)\leftrightarrow R_4(14).
\end{array}
\]

The endpoint after Row 23 is exactly `O` with the assignment of Section 4.

---

## 7. Root verification

### Lemma 7.1 — local validity of every row

For each row:

1. the four exchanged exterior branch values sum to zero;
2. the displayed new central value is the sum of the two branch roots retained at either active endpoint;
3. the displayed new central value has weight two;
4. the two new active vertices carry root triangles.

### Proof

This is direct substitution in the table. For example, Row 2 has retained values `15` and `45` at one endpoint, whose sum is `14` only depending on the precise retained pair; the descriptor table fixes the complementary branch assignment and gives central root `35`. The two vertex equations are equivalent because the total four-branch sum is zero. The same two-bit symmetric-difference check applies row by row.

For audit, the complete state is reconstructed recursively from the previous row and the stated branch exchange; no unlisted edge changes. ∎

### Theorem 7.2 — naked alternating root path

The sequence of twenty-three NNIs gives

\[
\boxed{
\mathcal E
\rightsquigarrow
\mathcal O
}
\]

through connected loopless cubic six-poles carrying root-valued `E_5` flows and the same ordered boundary word

\[
(25,45,24,25,45,24).
\]

### Independent finite certificate

A direct exact graph computation verifies at all twenty-four states:

- twelve internal vertices of degree three;
- six fixed boundary vertices of degree one;
- connectedness and looplessness;
- twenty-one distinct edges;
- Kirchhoff sum zero at every internal vertex;
- weight two on every edge;
- exact endpoint equality with `O`.

The displayed move list is the controlling reproducible certificate.

---

## 8. Move-support census

The twenty-three active edges split as:

\[
\boxed{
8\text{ auxiliary},
\quad
12\text{ turn-spoke},
\quad
3\text{ pivot-rail}.}
\]

The three pivot-rail active moves are Rows 4, 8 and 17.

Thus no pointwise-relative lift fixing all turn corollas can realise this path, consistently with `TURN_COROLLA_POINTWISE_MATCHING_CHANGE_OBSTRUCTION_V1.md`.

---

## 9. Exact decorated-lift target

Let every naked rail edge be replaced by its actual resolved constant-pivot carrier with all emitted side roots and exterior attachments retained.

For each of the twenty-three naked NNIs, prove one of:

1. a root-valued relative full-state lift over the decorated carriers;
2. a route/profile escape;
3. a smaller separator or bounded source cell;
4. one standard first-failure atom feeding the established one-token grammar.

The auxiliary moves are already ordinary bounded local NNIs. The unresolved moves are the twelve turn-spoke and three rail-active rows.

A successful sequential lift would give a legal even-to-odd full-state history and repair the R2.6 section problem without simultaneous stars.

---

## 10. Assurance boundary

### Exact here

- explicit naked even and odd alternating carriers;
- complete root labels;
- twenty-three legal root NNIs;
- preservation of the ordered six-output boundary;
- connectedness, cubicity and looplessness of every intermediate state;
- exact endpoint assignment;
- move-support census.

### Not claimed

- preservation of arbitrary resolved constant-run decorations;
- a pointwise-relative turn-corolla path;
- completed `C6/C8` annulus or open strip;
- R2.7, cap restoration or five-CDC;
- PDL reconstruction, independent audit, Lean, manuscript, curation, release or publication.
