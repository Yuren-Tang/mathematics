# The Heawood zero-parent state has a literal root-only `H_35` escape

## Research Lead source certificate v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-03`  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `212d789a5967813e7277fb3e269060926c99cb0e`

**Verdict.** The source movie prescribed in `research-workbench#77` is correct.  One remote root-valued equal-face branch swap changes the physical `H_35` decomposition; one legal closed `H_35` switch changes exactly one `13` branch and one `23` branch; one final root NNI realizes the literal zero parent with central root `35`.  All intermediate states are complete root-valued labelled graphs of the same order.  No `2--0` cancellation, zero insertion, co-root atom, lower-order call, track erasure, or finite-state inference occurs.

---

## 1. Stable labelled input

Let `V={1,...,14}`.  Stable edge identities, initial incidences and roots are

| stable edge | root | stable edge | root | stable edge | root |
|---|---:|---|---:|---|---:|
| `1-2` | `23` | `1-6` | `12` | `1-14` | `13` |
| `2-3` | `34` | `2-11` | `24` | `3-4` | `13` |
| `3-8` | `14` | `4-5` | `12` | `4-13` | `23` |
| `5-6` | `13` | `5-10` | `23` | `6-7` | `23` |
| `7-8` | `24` | `7-12` | `34` | `8-9` | `12` |
| `9-10` | `13` | `9-14` | `23` | `10-11` | `12` |
| `11-12` | `14` | `12-13` | `13` | `13-14` | `12` |

Every vertex equation is root-valued.  The initial triangle row is

\[
\begin{array}{c|cccccccccccccc}
v&1&2&3&4&5&6&7&8&9&10&11&12&13&14\\
\hline
\Delta_v&123&234&134&123&123&123&234&124&123&123&124&134&123&123.
\end{array}
\]

The active edge is stable edge `4-5:12`.  Its ordered branches are

\[
A=3-4=13,\qquad B=5-6=13,\qquad
C=4-13=23,\qquad D=5-10=23.
\]

Thus

\[
(A,B,C,D)=(13,13,23,23),
\]

the current crossed topology is `AC|BD`, the other root crossed topology is `AD|BC`, and the prescribed parent is

\[
AB\mid CD
\]

with forced central value zero.

### Retained cap block

Fix cap vertices `7,12`, cap edge `7-12:34`, and ordered cap darts

\[
6-7=23,\quad 7-8=24,\quad 11-12=14,\quad 12-13=13.
\]

Their two physical sums are

\[
23+24=34,
\qquad
14+13=34.
\]

The remote NNI below moves only the far endpoint of stable dart `12-13`; its endpoint at cap vertex `12`, its root, stable identity and cap order remain fixed.  The support switch and active parent NNI are disjoint from the cap vertices.  Hence the cap coordinate survives literally.

---

## 2. Remote equal-face root branch swap

Stable edge `13-14` has root `12`.  At both endpoints the other roots are `13,23`, so the local pair is

\[
123+123.
\]

Perform the root-valued branch-swap NNI which retains

- stable central edge `13-14:12`;
- stable dart `4-13:23` at vertex `13`;
- stable dart `9-14:23` at vertex `14`;

and reattaches exactly

\[
12-13:13\;\longmapsto\;12-14:13,
\]

\[
1-14:13\;\longmapsto\;1-13:13.
\]

The outside endpoints `12` and `1`, both central darts, every active dart and every cap dart identity are fixed.  Both local triangles remain `123`; hence every root equation remains valid.

Call the resulting state `S_1`.

---

## 3. Exact physical `H_35` split

An edge belongs to

\[
H_{35}=F_3\triangle F_5
\]

exactly when its root meets `35` once.

In `S_1`, the selected subgraph has exactly two nontrivial connected components.

The first component is

\[
\boxed{
Z_0=1-2-3-4-13-1
}
\]

with stable edge set

\[
\boxed{
\{1-2,2-3,3-4,4-13,1-14\}.
}
\]

Here stable edge `1-14` has current incidence `1-13`.  This component contains active branches

\[
A=3-4:13,
\qquad
C=4-13:23.
\]

The second component is

\[
\boxed{
Z_1=5-6-7-12-14-9-10-5
}
\]

with stable edge set

\[
\boxed{
\{5-6,6-7,7-12,12-13,9-14,9-10,5-10\}.
}
\]

Here stable edge `12-13` has current incidence `12-14`.  This component contains

\[
B=5-6:13,
\qquad
D=5-10:23.
\]

Thus the remote NNI has changed the physical channel geometry, not merely the coefficient row: the current active passages `AC` and `BD` now close separately.

---

## 4. Closed component switch

Switch the complete closed component `Z_0` by support pair `35`.  Incidences are unchanged.  The exact root translations are

\[
\begin{array}{c|ccccc}
\text{stable edge}&1-2&2-3&3-4&4-13&1-14\\
\hline
\text{before}&23&34&13&23&13\\
\text{after}&25&45&15&25&15.
\end{array}
\]

At every vertex of `Z_0`, exactly two selected incident roots are translated, so the complete flow remains root-valued.

The active word becomes

\[
\boxed{
(A,B,C,D)=(15,13,25,23).
}
\]

The active central edge is still `4-5:12`.  The two parent sums are now

\[
A+B=15+13=35,
\qquad
C+D=25+23=35.
\]

Therefore the literal prescribed-parent topology is root-valued with central root `35`.

---

## 5. Literal parent NNI

Perform the NNI on stable edge `4-5` that groups `A,B` at vertex `4` and `C,D` at vertex `5`.

Retain stable darts `3-4@4`, `5-10@5`, both central darts and all outside endpoints.  Move exactly

\[
5-6@5\longmapsto5-6@4,
\qquad
4-13@4\longmapsto4-13@5.
\]

Equivalently, the current incidences become

\[
5-6:5-6\longmapsto4-6,
\qquad
4-13:4-13\longmapsto5-13.
\]

Change the central root

\[
4-5:12\longmapsto35.
\]

The final active triangles are

\[
135
\quad\text{and}\quad
235,
\]

and the topology is exactly the stored labelled `AB|CD` parent, not merely an isomorphic closure.  The prefix map is updated by the four explicitly moved inside darts and is the identity elsewhere.

---

## 6. Graph-category audit

Let

- `G_0` be the initial graph;
- `G_1` be the graph after the remote NNI;
- `G_2=G_1` be the graph after the support switch;
- `G_3` be the final parent graph.

Exact exhaustive subset enumeration gives

\[
\begin{array}{c|cccccc}
&\text{connected}&\text{simple}&\text{cubic}&\text{bridges}&\text{girth}&\lambda_c\\
\hline
G_0&\text{yes}&\text{yes}&\text{yes}&0&6&6\\
G_1&\text{yes}&\text{yes}&\text{yes}&0&5&5\\
G_2&\text{yes}&\text{yes}&\text{yes}&0&5&5\\
G_3&\text{yes}&\text{yes}&\text{yes}&0&5&5.
\end{array}
\]

With the convention that one fixed vertex belongs to the enumerated shore, the numbers of complementary-shore representatives attaining the displayed cyclic connectivity are respectively

\[
28,\qquad5,\qquad5,\qquad8.
\]

Thus no loop, parallel edge, bridge, cyclic `2/3/4`-cut, theta or bounded low-port terminal occurs.  The only output is literal parent success.

---

## 7. Reproducible serialisation

Serialise a state as the whitespace-free UTF-8 JSON array of rows

```text
[stable_edge_id,min(current_endpoint),max(current_endpoint),sorted_root_digits]
```

sorted lexicographically by stable edge id.  The SHA-256 digests are

| state | digest |
|---|---|
| initial `S_0` | `4bfadd66ae43ed73c0cb339524884d295264b5468794406412770788993c799d` |
| post-remote-NNI `S_1` | `a7f4f8c0ff4e75310517d4d61776d17633022463a0a5b8fe07d81777d127a543` |
| post-switch `S_2` | `c5a50827fd01e692ed56d5e2e8c82f0391018cff2c969c13e15b315edf618d9d` |
| final parent `S_3` | `18526bf3f8736cae7c298305a9d9f3da49bac4be18828a40ac1368f4070843d7` |

A reproducer needs only the initial table, symmetric difference of root labels, the two incidence changes in Section 2, the five root translations in Section 4, the two incidence changes in Section 5, and exhaustive shore enumeration for Section 6.

---

## 8. Exact model-case theorem

### Theorem `HEAWOOD-ZERO-PARENT-H35-ESCAPE`

The displayed complete Heawood zero-parent state admits the source-faithful same-order movie

```text
remote equal-face root branch swap at 13-14
    -> physical H_35 split
    -> switch Z_0=1-2-3-4-13-1
    -> active word (15,13,25,23)
    -> literal AB|CD parent NNI with central root 35.
```

No forbidden move or recursive call occurs.

### Scope

This certificate proves the exact finite model required by issue #77.  Universality does not follow from this one movie or from the false matching-only remote equal-face lemma.  The universal theorem is supplied separately by the fixed-channel component-chain construction.