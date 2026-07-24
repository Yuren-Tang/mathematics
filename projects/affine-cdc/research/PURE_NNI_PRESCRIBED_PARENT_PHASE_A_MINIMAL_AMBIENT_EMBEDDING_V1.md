# Prescribed-parent witness has a minimal complete prime ambient embedding

## Research Lead Phase A result v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-01`  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `5fe36ece724f0a05fbf02572ef6eadae476a6d7c`  
**Interface:** `PURE_NNI_PRESCRIBED_PARENT_STATE_INTERFACE_NORMAL_FORM_V1.md`

**Phase-A verdict:** the four-root witness is not forced into a route, `2/3/4`-cut, or bounded terminal. It has a complete connected loopless bridgeless fixed-cap ambient realization in which both the current source graph and the prescribed-parent topology have cyclic edge-connectivity five. The smallest such prime realization has twelve vertices.

This is not a counterexample to five-CDC or to existential root solubility. It is a complete nonterminal witness to the prescribed-parent interface.

---

## 1. Labelled current source graph

Let

\[
V=\{0,1,\ldots,11\}.
\]

Define the labelled cubic graph `G` by

\[
\begin{aligned}
E(G)=\{&03,06,0\,11,
16,18,1\,10,
29,2\,10,2\,11,\\
&37,3\,10,
45,48,4\,11,
56,57,79,89\}.
\end{aligned}
\]

Every displayed pair denotes one edge with its two labelled darts.

The active edge is

\[
e=0\,11.
\]

Its four ordered exterior darts are

\[
A=03,\qquad B=11\,4,\qquad C=06,\qquad D=11\,2.
\]

The current local pairing is

\[
AC\mid BD.
\]

---

## 2. Complete root flow

Assign roots as follows:

\[
\begin{array}{c|c@{\qquad}c|c@{\qquad}c|c}
03&12&06&13&0\,11&23\\
16&12&18&13&1\,10&23\\
29&14&2\,10&12&2\,11&24\\
37&23&3\,10&13&45&13\\
48&14&4\,11&34&56&23\\
57&12&79&13&89&34
\end{array}
\]

At every vertex the three incident roots form one `K_5` triangle. Explicitly:

\[
\begin{array}{c|c}
0&(12,13,23)\\
1&(12,13,23)\\
2&(14,12,24)\\
3&(12,23,13)\\
4&(13,14,34)\\
5&(13,23,12)\\
6&(13,12,23)\\
7&(23,12,13)\\
8&(13,14,34)\\
9&(14,13,34)\\
10&(23,12,13)\\
11&(23,24,34).
\end{array}
\]

Thus

\[
\lambda:E(G)\to R_5
\]

is a root-valued `E_5` flow.

At the active edge the ordered word is exactly

\[
(A,B,C,D)=(12,34,13,24),
\]

and the current central root is

\[
A+C=B+D=23.
\]

The crossed sheet is therefore `R_23`.

---

## 3. Prescribed parent topology

The prescribed parent pairing is

\[
AB\mid CD.
\]

Let `P` be obtained from `G` by the labelled `2--2` reattachment

\[
06,\ 11\,4
\quad\longmapsto\quad
11\,6,\ 04,
\]

with every edge identity and every other dart fixed. Hence

\[
E(P)=igl(E(G)\setminus\{06,4\,11\}\bigr)\cup\{04,6\,11\}.
\]

For the supplied boundary word the forced parent central value is

\[
A+B=C+D=12+34=Q_5.
\]

Therefore the supplied flow cannot be reinserted on `P` without changing the boundary word.

---

## 4. Graph-category certificate

### Theorem 4.1 — current graph is prime for the v7.2 ledger

`G` is:

- connected;
- simple and loopless;
- cubic;
- bridgeless;
- girth five;
- without a cyclic edge cut of size at most four.

The minimum cyclic cut size is five. There are nine complementary shore pairs attaining size five.

### Theorem 4.2 — prescribed parent is also prime

`P` is:

- connected;
- simple and loopless;
- cubic;
- bridgeless;
- girth five;
- without a cyclic edge cut of size at most four.

Its minimum cyclic cut size is five, attained by eight complementary shore pairs.

### Finite certificate

For either graph enumerate every proper subset `X subset V` containing vertex `0`. Retain `X` only when both induced shores contain a cycle. Direct incidence counting gives

\[
|\delta_G(X)|\ge5,
\qquad
|\delta_P(X)|\ge5.
\]

This is a finite `2^11-1` labelled subset check for each graph. It uses no flow or isomorphism inference.

Consequently no current or prescribed topology terminal from the `2/3/4`-cut, loop, bridge, parallel, theta, triangle, or low-port ledger is present.

---

## 5. Cap block and route/profile field

Choose cap vertices

\[
1,\ 10
\]

with cap edge

\[
1\,10=23.
\]

Order the four cap-side darts as

\[
t_1=16,\quad t_2=18,\quad t_3=10\,2,\quad t_4=10\,3.
\]

Their roots are

\[
(12,13,12,13).
\]

Let

\[
M_0=t_1t_2\mid t_3t_4
\]

be the physical cap matching. Its two central values are both `23`, so the cap is root-valued. The equal-root matching is

\[
M_1=t_1t_3\mid t_2t_4,
\]

and the other crossed root matching is `M_2`. In ten-state notation the displayed boundary is one labelled `B_1` state lying in the cap-compatible component `K_0`.

The active edge `0\,11` is disjoint from the cap vertices. The prescribed reattachment fixes all four cap darts and the cap edge. Thus the complete state carries:

\[
\mathfrak B=(1,10;t_1,t_2,t_3,t_4;M_0),
\qquad
\kappa=B_1\in K_0.
\]

This supplied cap flow lives on the current topology `G`; it does not erase the live obligation to realize the different labelled topology `P`.

---

## 6. Support-component attachment data

For `h=ij`, write

\[
H_h=F_i\triangle F_j.
\]

Every nonempty component below is a cycle. The table gives its length, the active darts it contains, and whether it meets the cap vertices `1,10`.

\[
\begin{array}{c|c|c|c}
h&\text{cycle lengths}&\text{active darts}&\text{cap incidence}\\
\hline
12&12&C,D&1,10\\
13&12&A,B&1,10\\
14&12&A,B,C,D&1,10\\
15&11&A,C&1,10\\
23&12&A,B,C,D&1,10\\
24&12&A,B&1,10\\
25&9&A,D&1,10\\
34&12&C,D&1,10\\
35&5,6&B,C\text{ on the }5\text{-cycle}&\text{the }6\text{-cycle meets }1,10\\
45&5&B,D&\varnothing.
\end{array}
\]

The two diagonal challenge networks are identical Hamilton cycles:

\[
H_{14}=H_{23}
=0-3-10-2-11-4-5-7-9-8-1-6-0.
\]

At the active vertices each locally pairs

\[
A-C,\qquad B-D,
\]

but globally the two local paths belong to the same component. Therefore there is no legal switch of only the `A,C` path or only the `B,D` path.

Switching the complete `H_{14}` or `H_{23}` cycle changes all four active roots and leaves

\[
\operatorname{wt}(A+B)=4.
\]

The same holds for every single support-component switch in the displayed complete state:

- if both `A,B` or neither are switched, `A+B` is unchanged;
- if exactly one is switched, the switch root contains support index `5`, so one co-root is changed to another co-root.

Thus no one-component switch immediately realizes the prescribed parent.

---

## 7. Atom, category and prefix fields

The prescribed-parent attempt has atom template

\[
\mathfrak a=(0\,11,Q_5,\{23,14\},R_{23}).
\]

The graph-category field is

\[
\tau=\texttt{prime}.
\]

Let the stored pure-NNI prefix have one active target edge and let

\[
\alpha
\]

be the literal identity on all edge/dart names except for the prescribed reattachment

\[
06,4\,11\leftrightarrow 6\,11,04.
\]

Hence the complete state tuple is fully specified and has live prescribed-parent obligation.

---

## 8. Minimality

### Theorem 8.1 — order twelve is minimal

No complete prime prescribed-parent witness exists at order below twelve.

### Order four

Four distinct outside darts cannot have four distinct outside endpoints. Every realization is one of the bounded endpoint-coincidence graphs.

### Order six

The two connected simple cubic graphs are `K_{3,3}` and the triangular prism.

- The prism has the cyclic three-cut separating its two triangles.
- In `K_{3,3}`, a nondegenerate prescribed reattachment at the witness edge gives the triangular prism, hence the prescribed target has that cyclic three-cut.

### Order eight

A cubic graph on eight vertices has girth at most four by the elementary cubic Moore bound.

- a triangle has a three-edge boundary;
- a shortest four-cycle has at most four outgoing edges.

If the complementary shore is cyclic, this is a cyclic `3`- or `4`-cut. If it is acyclic or disconnected, the cubic shore formula gives the bounded/low-port ledger. Thus no prime current-and-parent pair exists.

### Order ten

A prime graph must have girth at least five. Equality in the cubic girth-five Moore bound at ten vertices forces the Petersen graph.

Normalize one active edge as `01` with branch endpoints

\[
0:\ 4,5,\qquad 1:\ 2,6.
\]

The two nontrivial labelled reattachments have, respectively, cyclic four-cut shores

\[
\{0,2,3,4\}\mid\{1,5,6,7,8,9\}
\]

and

\[
\{0,4,6,9\}\mid\{1,2,3,5,7,8\}.
\]

The edge stabilizer and branch reversal cover every active edge and both crossed choices. Hence every Petersen witness has a prescribed-parent cyclic four-cut terminal.

The twelve-vertex pair `(G,P)` above is prime, proving minimality. ∎

---

## 9. Phase-A conclusion

### Exact output

There exists a smallest complete nonterminal ambient embedding of the PDL witness. It is the twelve-vertex state specified in Sections 1--7.

Consequently no ambient-exclusion theorem can repair v7.2 solely by claiming that every `(4,2,2)` prescribed-parent failure is already a route, small-cut, or bounded terminal.

Phase B is mandatory.

---

## 10. Assurance boundary

### Exact authorial result

- complete labelled graph and flow;
- complete cap/route field;
- complete diagonal support-component data;
- prime current and prescribed topologies;
- minimality through order ten;
- genuine nonterminal prescribed-parent obligation.

### Not yet decided

- reachability of the prescribed parent by a longer fixed-order source movie;
- a complete transition SCC;
- a strict rank;
- local repair versus architecture change.

### Not claimed

- a graph counterexample to five-CDC;
- failure of existential root solubility of `P`;
- Lean, Curator, manuscript, release, or publication status.
