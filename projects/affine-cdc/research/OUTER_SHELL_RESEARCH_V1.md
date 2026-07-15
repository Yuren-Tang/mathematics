# AffineCDC outer-shell research V1

**Workstream:** M1 — Outer Shell  
**Base:** `749e0579581fcc838685138b3582f4de306b8e72`  
**Status:** theorem-level closure reached  
**Scope:** loopless finite-active-edge bridgeless multigraphs; loop deletion and reinsertion remain outside this workstream

## 1. Candidate exact theorems and closure

The required package exists. It need not be constructed simultaneously.

The clean order is

\[
G\longmapsto H\longmapsto f,
\]

where:

1. `H` is the port-cycle cubic expansion of `G`;
2. `H` is finite, loopless, cubic, and bridgeless, and carries canonical collapse data back to `G`;
3. a nowhere-zero \(\mathbf F_2^3\)-flow on `H` is then supplied by the classical six-flow theorem together with Tutte's group-flow equivalence.

Thus the strongest exact outer-shell theorem justified here is the following.

### Theorem 1.1 — finite-active-edge cubic binary-flow shell

Let \(G\) be a loopless multigraph whose active edge set \(E(G)\) is finite. Assume that no cut of \(G\) consists of one edge. Then there exist a finite loopless cubic multigraph \(H\), a vertex map

\[
\pi:V(H)\to V(G),
\]

an injective edge lift

\[
\lambda:E(G)\hookrightarrow E(H),
\]

and a map

\[
f:E(H)\to \mathbf F_2^3
\]

such that:

1. \(H\) is bridgeless;
2. \(f(e)\neq0\) for every \(e\in E(H)\);
3. at every vertex of \(H\), the three incident flow values sum to zero;
4. \(\lambda(e)\) has endpoints lying over the endpoints of \(e\);
5. every edge of \(H\) joining different \(\pi\)-fibres is \(\lambda(e)\) for a unique \(e\in E(G)\);
6. every other edge of \(H\) lies inside one \(\pi\)-fibre;
7. the fibre over an active vertex \(v\) is a cycle of length \(\deg_G(v)\), with a two-cycle interpreted as two parallel edges;
8. the fibre over an isolated vertex is empty.

Moreover one may choose

\[
|V(H)|=2|E(G)|,
\qquad
|E(H)|=3|E(G)|.
\]

No connectedness hypothesis or conclusion is required.

### Corollary 1.2 — exact connection to the affine core

Assume the established affine rank-three theorem in its natural graph-level form:

> every finite loopless cubic graph carrying a nowhere-zero \(\mathbf F_2^3\)-flow has a finite multiset vertex-even double cover.

Then every loopless bridgeless multigraph with finite active edge set has a finite multiset cut-even double cover. The cover is obtained by applying the affine theorem to \((H,f)\), converting vertex-evenness to cut-evenness on the loopless graph \(H\), and projecting supports through \((\pi,\lambda)\).

Finite circuit decomposition may then be performed on the original graph, not on \(H\). This is the weaker and sufficient outer-shell output.

### 1.3 Layer separation

| Layer | Status in this workstream | Exact role |
|---|---|---|
| loop deletion and singleton-loop reinsertion | excluded; already canonical outside M1 | reduces the natural theorem to the loopless core and restores loops after final decomposition |
| degree reduction / cubic expansion | proved here at theorem level | constructs the finite port-cycle graph \(H\) |
| preservation of bridgelessness | proved here at theorem level | permits use of a global nowhere-zero flow theorem on \(H\) |
| nowhere-zero binary flow | reduced exactly to classical theorems | Seymour six-flow plus Tutte group-flow equivalence supplies \(f:E(H)\to\mathbf F_2^3\setminus\{0\}\) |
| collapse / projection data | constructed together with \(H\) | identifies original edges with all inter-fibre edges and transports cut parity |
| isolated vertices | represented by empty fibres | avoids ambient-vertex finiteness and any unnecessary surjectivity requirement |
| cut-even double covers | sufficient transported output | exact double coverage survives projection; circuits are decomposed only downstairs |

## 2. Definitions

### 2.1 Active finiteness

The **active edge set** is the graph edge set \(E(G)\), as distinguished from any ambient edge carrier. The **active vertex set** is

\[
V_+(G):=\{v\in V(G):\operatorname{Inc}_G(v)\neq\varnothing\}.
\]

If \(E(G)\) is finite, then \(V_+(G)\) is finite because every edge has at most two endpoints. The ambient vertex carrier may nevertheless be infinite through isolated vertices.

For \(v\in V_+(G)\), define

\[
d_G(v):=|\operatorname{Inc}_G(v)|.
\]

Looplessness ensures that an edge incident with \(v\) contributes one edge object and has its other endpoint distinct from \(v\).

### 2.2 Bridgelessness

The workstream uses the cut formulation

\[
\forall S\subseteq V(G),\qquad |\delta_G(S)|\neq1.
\]

For an active loopless edge \(e=uv\), this implies that \(u\) and \(v\) are joined in \(G-e\). Otherwise, let \(S\) be the vertices reachable from \(u\) in \(G-e\); then \(e\) is the unique edge crossing \(S\), contrary to the hypothesis. This alternate-path formulation is the one used to prove preservation of bridgelessness. No connectedness of the whole graph is involved.

### 2.3 Nowhere-zero binary flow

For a loopless graph \(X\), a nowhere-zero \(\mathbf F_2^3\)-flow is a function

\[
f:E(X)\to\mathbf F_2^3\setminus\{0\}
\]

such that

\[
\sum_{e\ni x}f(e)=0
\]

at every active vertex \(x\). This matches the companion `Port.NowhereZeroFlow`: orientation disappears because \(-a=a\) in characteristic two.

### 2.4 Collapse datum

A collapse datum from \(H\) to \(G\) consists of:

1. a vertex map \(\pi:V(H)\to V(G)\), not required to be surjective;
2. an injective edge lift \(\lambda:E(G)\hookrightarrow E(H)\) preserving endpoints under \(\pi\);
3. the assertion that the inter-fibre edges of \(H\) are exactly the lifted original edges.

For \(F'\subseteq E(H)\), define

\[
\operatorname{proj}(F'):=\{e\in E(G):\lambda(e)\in F'\}.
\]

No connectedness or finiteness of fibres is needed by the pure cut-parity transport theorem. The particular expansion below has connected finite fibres for a separate reason: to prove that \(H\) is bridgeless.

### 2.5 Port-cycle expansion

Choose a cyclic order on the finite incidence set \(\operatorname{Inc}_G(v)\) for every active vertex \(v\). There are no active degree-one vertices under the hypotheses; see Lemma 3.1.

Define the vertices of \(H\) to be the ports

\[
V(H):=\{(v,e):e\in\operatorname{Inc}_G(v)\}.
\]

There are two classes of edges.

- For each original edge \(e=uv\), create one **external edge** \(\lambda(e)\) joining \((u,e)\) to \((v,e)\).
- For each active vertex \(v\), join its ports in the chosen cyclic order. If \(d_G(v)=2\), the two successor edges are distinct parallel internal edges and form a two-cycle.

Put \(\pi(v,e)=v\).

## 3. Elementary expansion theorem

### Lemma 3.1 — active degrees

If \(G\) is loopless and bridgeless, every active vertex has degree at least two.

#### Proof

If \(v\) had exactly one incident edge \(e\), then \(\delta_G(\{v\})=\{e\}\), contradicting bridgelessness. Isolated vertices have degree zero and are not active. \(\square\)

### Theorem 3.2 — port-cycle cubic expansion

Under the hypotheses of Theorem 1.1, the construction of Section 2.5 gives a finite loopless cubic bridgeless multigraph \(H\) and collapse data \((\pi,\lambda)\) satisfying items 1 and 4–8 of Theorem 1.1, together with the exact size formulae

\[
|V(H)|=2|E(G)|,
\qquad
|E(H)|=3|E(G)|.
\]

#### Proof

**Finiteness.** Each original edge contributes two ports because \(G\) is loopless. Hence

\[
|V(H)|=\sum_{v\in V_+(G)}d_G(v)=2|E(G)|.
\]

Each fibre cycle contributes \(d_G(v)\) internal edge objects, including two distinct parallel objects when \(d_G(v)=2\). Thus there are \(2|E(G)|\) internal edges and \(|E(G)|\) external edges.

**Looplessness.** An external edge joins ports lying over two distinct endpoints of a loopless original edge. An internal edge joins two distinct ports. The degree-two case uses parallel edges, not loops.

**Cubicity.** Every port \((v,e)\) is incident with exactly one external edge, namely \(\lambda(e)\), and exactly two internal cycle-edge objects. Hence its incidence set has cardinality three.

**Collapse properties.** The map \(\lambda\) is injective by construction. External edges preserve original endpoints under \(\pi\). Internal edges remain inside a fibre, and there are no other edges. Isolated vertices have no ports, so their fibres are empty.

**Bridgelessness.** An internal edge has an alternate route between its endpoints along the complementary arc of its fibre cycle, including the parallel mate in the degree-two case. Hence no internal edge is a bridge.

Let \(e=uv\) be an original edge. By Section 2.2 there is a \(u\)-to-\(v\) path in \(G-e\). Lift each edge of that path to its external edge in \(H\). At each intermediate original vertex, join the incoming and outgoing ports by an arc of the fibre cycle; at the two ends, join \((u,e)\) and \((v,e)\) to the first and last path ports in the same way. The resulting walk contains a path between the endpoints of \(\lambda(e)\) and avoids \(\lambda(e)\). Thus no external edge is a bridge. Therefore \(H\) is bridgeless. \(\square\)

### Remark 3.3 — no connectedness

The construction is componentwise. If \(G\) has two active connected components, then the exact inter-fibre-edge condition forbids an auxiliary edge between them, so the resulting \(H\) is also disconnected. Connectedness would be an incorrect general hypothesis or conclusion.

## 4. The exact classical flow input

The expansion theorem is elementary. The existence of the required rank-three binary flow is the only deep external graph theorem used by the outer shell.

### External Theorem 4.1 — Seymour's six-flow theorem, exact form used

For every finite bridgeless multigraph \(X\), after choosing an orientation of its edges, there is an integer circulation \(\varphi\) such that

\[
0<|\varphi(e)|<6
\]

for every edge \(e\). Equivalently, \(X\) has a nowhere-zero integer six-flow. If the published statement is taken for connected graphs, apply it independently to each nontrivial connected component.

Reference: P. D. Seymour, *Nowhere-zero 6-flows*, Journal of Combinatorial Theory, Series B **30** (1981), 130–135.

### External Theorem 4.2 — Tutte group-flow equivalence, exact form used

Let \(X\) be a finite graph, let \(k\ge2\), and let \(A\) be any finite abelian group of order \(k\). Then \(X\) has a nowhere-zero integer \(k\)-flow if and only if it has a nowhere-zero \(A\)-flow. Equivalently, existence and number of nowhere-zero group flows depend on the order of the coefficient group, not its isomorphism type.

The form required here is only the existence equivalence at \(k=8\).

Reference: W. T. Tutte, *A contribution to the theory of chromatic polynomials*, Canadian Journal of Mathematics **6** (1954), 80–91.

### Corollary 4.3 — binary eight-flow input

Every finite bridgeless multigraph has a nowhere-zero \(\mathbf F_2^3\)-flow.

#### Proof reduction

By Theorem 4.1, obtain an integer six-flow. The same circulation is an integer eight-flow because \(0<|\varphi(e)|<6<8\). Apply Theorem 4.2 with the abelian group

\[
A=(\mathbf Z/2\mathbf Z)^3=\mathbf F_2^3,
\qquad |A|=8.
\]

In characteristic two, reversing an edge does not change its value, and the signed Kirchhoff equation becomes the unoriented incidence sum used by the affine port. \(\square\)

### Proof of Theorem 1.1

Apply Theorem 3.2 to construct the finite loopless cubic bridgeless expansion \(H\) with collapse data. Apply Corollary 4.3 to \(H\). The resulting group flow is exactly the `Port.NowhereZeroFlow` datum after forgetting orientation. \(\square\)

## 5. Cover transport and why the weaker shell suffices

Let \(\mathcal F'\) be the graph-level multiset vertex-even double cover of \(H\) produced by the affine rank-three machinery.

1. Since \(H\) is loopless, every member of \(\mathcal F'\) is cut-even.
2. Project each support through \(\lambda\).
3. For every \(S\subseteq V(G)\), the collapse datum gives a bijection

   \[
   \operatorname{proj}(F')\cap\delta_G(S)
   \cong
   F'\cap\delta_H(\pi^{-1}S).
   \]

   Hence cut-evenness is preserved.
4. For every original edge \(e\), membership of \(e\) in a projected support is exactly membership of \(\lambda(e)\) upstairs. Exact double coverage is therefore preserved memberwise with multiset multiplicity.

This proves Corollary 1.2.

The shell does **not** need to transport circuits, rotations, dart orbits, or decompositions. An upstairs circuit can project to the empty support, and distinct upstairs supports can have the same projection. These are harmless because the natural compositional object is a multiset of cut-even supports. One final finite circuit decomposition is performed downstairs.

## 6. Must expansion and flow be constructed simultaneously?

No. The expansion-first route of Theorem 1.1 separates them completely:

\[
\text{bridgeless }G
\xrightarrow{\text{elementary port-cycle expansion}}
\text{bridgeless cubic }H
\xrightarrow{\text{binary eight-flow theorem}}
(H,f).
\]

However, the reverse order is not formally interchangeable. A preselected flow on \(G\) need not extend over a preselected cyclic ordering of a high-degree fibre.

### Proposition 6.1 — exact local extension criterion

Let a degree-\(d\) vertex have incident nonzero values

\[
a_1,\dots,a_d\in\mathbf F_2^3,
\qquad
\sum_{i=1}^d a_i=0,
\]

listed in the cyclic order used by the port-cycle gadget. Let \(x_i\) be the value on the internal edge from port \(i\) to port \(i+1\), with indices modulo \(d\). Conservation at port \(i\) is

\[
x_{i-1}+a_i+x_i=0.
\]

Put

\[
s_0=0,
\qquad
s_i=a_1+\cdots+a_i.
\]

Then every extension has the form

\[
x_i=t+s_i
\]

for one \(t\in\mathbf F_2^3\), and a nowhere-zero extension exists if and only if

\[
\{s_0,s_1,\dots,s_{d-1}\}\neq\mathbf F_2^3.
\]

#### Proof

The conservation equations give recursively \(x_i=x_{i-1}+a_i\), hence \(x_i=t+s_i\). The closing equation is consistent exactly because \(s_d=0\). All internal values are nonzero exactly when \(t\) avoids the prefix-sum set. \(\square\)

### Corollary 6.2 — low-degree automatic extension

For \(d\le7\), every preselected local flow extends over every cyclic ordering. There are at most \(d\) distinct elements among \(s_0,\dots,s_{d-1}\), whereas \(|\mathbf F_2^3|=8\).

### Counterexample 6.3 — first fixed-order failure at degree eight

Let two vertices be joined by eight parallel edges. This graph is loopless and bridgeless. Label the edges, in the chosen cyclic order at one endpoint, by the successive differences of the cyclic Gray tour

\[
000,001,011,010,110,111,101,100,000.
\]

Thus the edge values are

\[
001,010,001,100,001,010,001,100.
\]

They are all nonzero and sum to zero, so they define a nowhere-zero \(\mathbf F_2^3\)-flow on the two-vertex graph. The prefix sums visit all eight elements of \(\mathbf F_2^3\). By Proposition 6.1, no choice of internal initial value \(t\) makes the corresponding eight-cycle fibre nowhere-zero.

Therefore the tempting statement

> every preselected \(\mathbf F_2^3\)-flow extends over every port-cycle expansion

is false. The approved dependency should be expansion first, global flow second. A simultaneous construction is needed only by an alternative strategy that insists on preserving a preselected downstairs flow.

## 7. Low-degree and high-degree vertices

### Degree zero

These are isolated vertices. They create no ports and have empty \(\pi\)-fibres. They affect neither cuts nor edge covers. Surjectivity of \(\pi\) is unnecessary and can be impossible under active-edge finiteness with infinitely many isolated ambient vertices.

### Degree one

This case cannot occur among active vertices of a loopless bridgeless graph. The unique incident edge is the singleton cut at the vertex.

### Degree two

The fibre is a two-cycle: two port vertices joined by two distinct parallel internal edges. Each port has one external and two internal incident edge objects, hence degree three. Both internal edges lie in the two-cycle.

### Degree three

The uniform construction uses a triangle fibre. An identity fibre consisting of one cubic vertex would also work, but the triangle convention makes the vertex set uniformly equal to the incidence set and yields the exact size formulae.

### Degree four through seven

The cycle gadget is elementary, preserves bridgelessness, and any already chosen local binary flow extends for every cyclic order. This extension fact is not needed by the recommended proof.

### Degree eight and above

The expansion itself remains valid without change. Only the reverse-order extension claim fails: a fixed flow and fixed cyclic order can exhaust all eight prefix sums. This is why the outer theorem applies the global flow theorem after constructing \(H\).

## 8. Finiteness ledger

| Use | Exact finiteness needed | Reason |
|---|---|---|
| active vertex set | active-edge finiteness | endpoints of finitely many edges form a finite set |
| degrees and cyclic orders | finite incidence support | every active incidence set is finite |
| construction of \(H\) | active-edge finiteness | \(|V(H)|=2|E(G)|\), \(|E(H)|=3|E(G)|\) |
| Seymour/Tutte input | finiteness of constructed \(H\) | classical finite flow theorems |
| affine compatibility source | finiteness of \(H\)'s active graph | finite global indexing and current port interface |
| cut transport | finiteness of each transported support | parity cardinalities are defined; ambient carriers and fibres need not be finite |
| exact double-cover multiset | finite affine index / finite family | supplied by the rank-three core |
| final circuit decomposition | finite support | descending/minimal decomposition terminates |
| ambient vertex carrier of \(G\) | not needed | may contain infinitely many isolated vertices |
| ambient edge carrier | not needed | only \(E(G)\) must be finite |

No step requires connectedness.

## 9. Counterexamples to overstrong formulations

### 9.1 Ambient finiteness does not follow

Take any finite bridgeless active graph and adjoin infinitely many isolated vertices in the ambient carrier. The active edge set remains finite and all graph cuts on edges are unchanged.

### 9.2 A surjective collapse map is not natural

Take an edgeless graph with infinitely many isolated vertices. It satisfies active-edge finiteness and bridgelessness. No finite cubic source graph can map surjectively onto its vertex carrier. Empty fibres are therefore part of the natural theorem.

### 9.3 Connectedness cannot be added

Let \(G\) be the disjoint union of two nonempty bridgeless components. Under the exact collapse condition, every inter-fibre edge is a lifted original edge, and there is no original edge between the two components. Hence no admissible \(H\) can connect their fibres.

### 9.4 Arbitrary connected cubic gadgets need not preserve bridgelessness

Let \(G\) consist of two two-edge cycles sharing one common vertex \(v\). It is bridgeless and \(d_G(v)=4\). Replace \(v\) by two triangles joined by one edge. On each triangle, use two vertices as ports for the two edges of one lobe and the third vertex as an endpoint of the joining edge. After attaching the four external edges, every gadget vertex is cubic, but the edge joining the triangles is a bridge because the two original lobes are otherwise disjoint. Connected cubic fibres alone are insufficient; the port-cycle fibres work because every internal edge has an internal alternate route.

### 9.5 A fixed downstairs flow need not extend over a fixed expansion

Counterexample 6.3 gives the first obstruction at degree eight.

### 9.6 Circuits do not project to circuits

A fibre cycle is an upstairs circuit consisting only of auxiliary edges, but its projection is empty. Therefore a collapse theorem phrased as circuit-by-circuit projection is false and stronger than needed.

### 9.7 Projected supports need not remain distinct or nonempty

Two distinct upstairs supports can differ only on auxiliary edges and hence have the same projection. An upstairs support contained in auxiliary edges projects to the empty support. Multiset even covers permit both phenomena.

## 10. Standard input versus project-specific argument

### Standard elementary graph theory

- finite active edge set implies finite active vertex set;
- an active degree-one vertex yields a bridge;
- in a finite multigraph, an edge is non-bridging exactly when it lies in a circuit;
- cycle gadgets and the handshaking count.

### Deep external theorem input

- Seymour's nowhere-zero six-flow theorem;
- Tutte's equivalence between integer \(k\)-flows and flows over any abelian group of order \(k\).

The project should expose their exact composite as one named interface:

> **BinaryEightFlow.** Every finite bridgeless multigraph carries a nowhere-zero \(\mathbf F_2^3\)-flow.

This theorem supplies only the function \(f\), nonvanishing, and Kirchhoff conservation. It supplies no affine family, dart data, cover, or collapse map.

### Project-specific theorem packaging established here

No literature-novelty claim is made in this workstream. “Project-specific” means derived or sharpened here for the exact canonical interfaces.

- the active-edge/isolated-vertex form of the port-cycle expansion;
- exact collapse data aligned with the canonical cut-transport chapter;
- exact size bounds \(2|E|\) and \(3|E|\);
- the proof that expansion and flow can be separated by ordering them correctly;
- the sharp local fixed-order extension criterion and the degree-eight counterexample;
- identification of cut-even double covers, rather than circuit decompositions, as the sufficient transported output.

## 11. Dependency graph

\[
\begin{array}{c}
E(G)\text{ finite},\ G\text{ loopless and bridgeless}\\
\downarrow\\
V_+(G)\text{ finite and active degrees }\ge2\\
\downarrow\\
\text{choose cyclic orders on incidence sets}\\
\downarrow\\
(H,\pi,\lambda)\text{ port-cycle expansion}\\
\downarrow\\
H\text{ finite, loopless, cubic, bridgeless}\\
\downarrow\quad\text{Seymour six-flow + Tutte group equivalence}\\
(H,f),\quad f:E(H)\to\mathbf F_2^3\setminus\{0\}\\
\downarrow\quad\text{rank-three affine compatibility and support extraction}\\
\text{vertex-even multiset double cover of }H\\
\downarrow\quad\text{loopless vertex-even/cut-even bridge}\\
\text{cut-even multiset double cover of }H\\
\downarrow\quad\text{pure collapse transport}\\
\text{cut-even multiset double cover of }G\\
\downarrow\quad\text{finite circuit decomposition}\\
\text{cycle double cover of }G.
\end{array}
\]

Loop deletion precedes this graph, and singleton-loop reinsertion follows it, in the full canonical theorem.

## 12. Unresolved gaps

The mathematical outer-shell existence theorem is closed at paper level. The following remain unresolved implementation or audit obligations.

1. **Formal availability of the deep flow input.** The current Mathlib/companion environment has not been checked for a theorem matching `BinaryEightFlow`. Formalizing Seymour's theorem from first principles would be a major independent project. An admissible external theorem interface must be decided explicitly by the Director.
2. **Exact multigraph conventions in the cited flow theorems.** The mathematical reduction from simple/connected formulations to finite loopless multigraphs and disconnected graphs is standard, but the canonical chapter should state it rather than leave it implicit.
3. **Mathlib construction engineering.** The incidence-port vertex type, cyclic successor choices, two-cycle parallel-edge objects, and active-edge rather than ambient-finite API require a separate Lean design.
4. **Named graph-level even-cover interface.** The canonical chapters specify it, but the companion formalization still extracts circuits immediately in `Port.cubic_flow_cdc`.
5. **Formal cut-even bridge and collapse transport.** These are paper-level in the canonical corpus and not yet machine-checked.
6. **Public statement migration.** Loop deletion and active-edge finiteness remain outside M1 and await the approved Path A implementation packet.

No mathematical connectedness gap remains. No simultaneous expansion-flow theorem is required by the recommended spine.

## 13. Recommended canonical theorem spine

Promote, after review, the following theorem sequence without changing the public statement in this workstream.

1. `active_degree_ge_two` — loopless bridgeless active vertices have degree at least two.
2. `exists_port_cycle_expansion` — construct \((H,\pi,\lambda)\) with exact sizes, cubicity, looplessness, and collapse laws.
3. `port_cycle_expansion_bridgeless` — every edge of \(H\) lies in a circuit.
4. `binary_eight_flow` — exact external classical input, stated as a standalone theorem interface and proved or imported only under an approved policy.
5. `exists_affine_outer_shell` — combine 2–4 to obtain \((H,f,\pi,\lambda)\).
6. `project_cut_even_double_cover` — apply the already canonical pure cut transport theorem memberwise.
7. `outer_shell_to_cut_even_double_cover` — compose the affine graph-level even-cover theorem with 5–6.

The canonical outer shell should stop at a cut-even double cover of the loopless original core. Circuit decomposition and loop reinsertion remain separate generic stages.

## 14. Checkpoint

**Checkpoint type:** theorem-level closure.

The expansion-flow-collapse package exists under a precise pair of classical flow theorems. The expansion and flow do not have to be simultaneous, provided the expansion is constructed first. A fixed-flow extension formulation is strictly stronger and false from degree eight for fixed cyclic order.
