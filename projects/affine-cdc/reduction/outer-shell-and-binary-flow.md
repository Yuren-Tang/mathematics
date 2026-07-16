# Outer shell and binary flow

This chapter supplies the graph-theoretic outer shell connecting the natural
finite-active-edge Cycle Double Cover statement to the cubic rank-three affine
compatibility theorem. It is a mathematical chapter. It does not claim that the
outer shell, Seymour's theorem, Tutte's theorem, adaptive ordering, collapse
transport, or the unconditional endpoint has been formalized in Lean.

Two exact routes are retained:

\[
G\longrightarrow H\longrightarrow (H,f)
\tag{expansion-first}
\]

and

\[
G\longrightarrow (G,f)\longrightarrow
(H,\widetilde f,\pi,\lambda).
\tag{adaptive flow-first}
\]

The adaptive flow-first route is the preferred concise route for Paper A. The
expansion-first route remains an independent flow-free expansion theorem and a
plausible lower-cost formalization route. Both routes hand the same object to
the affine core: a finite loopless cubic bridgeless graph carrying a nowhere-zero
\(\mathbf F_2^3\)-flow and exact collapse data.

## 1. Scope and conventions

A multigraph \(G\) has active vertex and edge sets \(V(G)\) and \(E(G)\)
inside possible larger ambient carriers. Parallel edge objects are allowed. The
outer shell acts on the loopless core.

The active vertex set is

\[
V_+(G):=\{v\in V(G):\operatorname{Inc}_G(v)\ne\varnothing\}.
\]

The natural finiteness hypothesis is

\[
E(G)\text{ is finite}.
\]

The ambient carriers may be infinite; infinitely many isolated vertices are
harmless.

For a loopless graph, \(\delta_G(S)\) is the active edge cut of
\(S\subseteq V(G)\). The bridge hypothesis is the intrinsic form

\[
\forall S\subseteq V(G),\qquad |\delta_G(S)|\ne1.
\tag{1.1}
\]

No connectedness hypothesis is imposed. On every edge-bearing connected
component, (1.1) is equivalent to the absence of a cut-edge.

A nowhere-zero \(\mathbf F_2^3\)-flow in the current AffineCDC convention is a
map

\[
f:E(G)\longrightarrow\mathbf F_2^3\setminus\{0\}
\]

such that

\[
\sum_{e\ni v}f(e)=0
\tag{1.2}
\]

at every active vertex \(v\). This is an unoriented sum over incident edge
objects. It agrees with the ordinary signed group-flow equation in
characteristic two only for loopless graphs: a loop cancels in an oriented
boundary but appears once in the present incidence set.

## 2. Active finiteness and low-degree fibres

### Proposition 2.1 — active vertices are finite

If \(E(G)\) is finite, then \(V_+(G)\) is finite.

#### Proof

Every active vertex is an endpoint of an active edge, and every edge has at most
two endpoints. Thus \(V_+(G)\) lies in the finite union of the endpoint sets of
the active edges. \(\square\)

### Proposition 2.2 — active degrees are finite and not one

Let \(G\) be loopless, let \(E(G)\) be finite, and assume (1.1). Every active
vertex has finite degree at least two.

#### Proof

Every incidence set is contained in the finite active edge set. If an active
vertex \(v\) had unique incident edge \(e\), then
\(\delta_G(\{v\})=\{e\}\), contrary to (1.1). \(\square\)

The exact fibre conventions are therefore:

- degree zero: an isolated vertex, with empty expansion fibre;
- degree one: impossible among active vertices;
- degree two: a two-cycle made of two distinct parallel internal edge objects;
- degree three and above: an ordinary cycle on the incidence ports.

A degree-three fibre is a triangle rather than an identity gadget. This uniform
choice makes the expansion vertices literally the incidence ports and yields
exact size formulae.

## 3. Port-cycle expansion and collapse data

Choose independently for every \(v\in V_+(G)\) a cyclic order on the finite set
\(\operatorname{Inc}_G(v)\). A linear start may be retained for indexing; the
graph itself uses the induced cyclic order.

Define a graph \(H\) as follows.

### Vertices

\[
V(H):=\{(v,e):v\in V_+(G),\ e\in\operatorname{Inc}_G(v)\}.
\]

### External edges

For every original edge \(e=uv\), create one edge \(\lambda(e)\) joining
\((u,e)\) to \((v,e)\).

### Internal edges

For every active vertex \(v\), join its ports in the chosen cyclic order. If
\(d_G(v)=2\), the two successor incidences produce two distinct parallel edges
between the two ports.

Define

\[
\pi:V(H)\longrightarrow V(G),\qquad \pi(v,e)=v.
\]

Isolated vertices have empty \(\pi\)-fibres. Surjectivity is neither required
nor natural.

### Theorem 3.1 — exact port-cycle expansion

Let \(G\) be a loopless multigraph with finite active edge set satisfying
(1.1). The construction gives a finite loopless cubic multigraph \(H\), a
vertex map \(\pi\), and an injective edge lift \(\lambda\) such that:

1. \(\lambda(e)\) has endpoints in the fibres over the endpoints of \(e\);
2. every edge of \(H\) joining distinct \(\pi\)-fibres is \(\lambda(e)\) for a
   unique \(e\in E(G)\);
3. every other edge of \(H\) lies inside one fibre;
4. an active fibre is a cycle of length \(d_G(v)\), with length two interpreted
   as two parallel edges;
5. an isolated fibre is empty;
6. the exact sizes are
   \[
   |V(H)|=2|E(G)|,\qquad |E(H)|=3|E(G)|.
   \tag{3.1}
   \]

No connectedness hypothesis or conclusion is present.

#### Proof

Every loopless original edge contributes two incidence ports, so

\[
|V(H)|=\sum_{v\in V_+(G)}d_G(v)=2|E(G)|.
\]

Every port has one external edge and two internal cycle-edge objects, including
the two distinct parallel objects in a degree-two fibre. Hence \(H\) is cubic.
The fibres contribute \(2|E(G)|\) internal edges and the lift contributes
\(|E(G)|\) external edges, proving (3.1).

External edges join ports over distinct original endpoints. Internal edges join
distinct ports; the degree-two case uses parallel edges, not loops. Thus \(H\)
is loopless. The collapse assertions follow directly from the two edge classes,
and \(\lambda\) is injective because original edge objects remain distinct.
\(\square\)

### Theorem 3.2 — preservation of bridgelessness

Under the hypotheses of Theorem 3.1, \(H\) has no singleton cut.

#### Proof

Every internal edge has an alternate route along the complementary arc of its
fibre cycle. In a degree-two fibre the alternate route is the parallel mate.

Let \(e=uv\) be an original edge. Condition (1.1) implies that \(u\) and \(v\)
remain connected in \(G-e\); otherwise the vertices reachable from \(u\) in
\(G-e\) would have cut exactly \(\{e\}\). Lift a \(u\)-to-\(v\) path in
\(G-e\) to external edges of \(H\), and join successive lifted edges inside the
visited fibres by fibre arcs. This gives an alternate path between the endpoints
of \(\lambda(e)\) avoiding \(\lambda(e)\).

Thus every edge of \(H\) has an alternate path between its endpoints. No edge is
a cut-edge in its component, hence no cut has size one. \(\square\)

The construction is componentwise. A disconnected \(G\) generally produces a
disconnected \(H\); connecting distinct components would violate the exact
inter-fibre-edge condition.

## 4. The isolated binary-eight-flow input

The only deep external graph-theoretic input is the following exact interface.

### External Theorem 4.1 — `BinaryEightFlow`

Let \(X\) be a loopless multigraph with finite active edge set and no singleton
cut. Parallel edges are allowed and connectedness is not required. Then there
exists

\[
f:E(X)\longrightarrow\mathbf F_2^3\setminus\{0\}
\]

satisfying the unoriented conservation equation (1.2) at every active vertex.

This is a paper-level external interface, not a machine-checked theorem of the
present project.

### 4.1 Exact classical reduction

For each edge-bearing connected component of \(X\):

1. apply Seymour's theorem in the connected loopless multigraph form to obtain
   an orientation and integer circulation \(\varphi\) with
   \[
   0<|\varphi(e)|<6;
   \]
2. regard the same orientation and function as an integer \(8\)-flow by literal
   range inclusion \(0<|\varphi(e)|<6<8\);
3. apply Tutte's equal-order existence theorem to
   \[
   (\mathbf Z/2\mathbf Z)^3=\mathbf F_2^3,
   \qquad |\mathbf F_2^3|=8;
   \]
4. forget orientation: since \(-a=a\), signed conservation becomes (1.2) on a
   loopless graph.

Component flows assemble because conservation is vertex-local. Isolated
vertices and the empty active graph are vacuous.

### 4.2 Source boundary

The classical six-flow source is P. D. Seymour, “Nowhere-zero 6-flows”,
*Journal of Combinatorial Theory, Series B* **30** (1981), 130–135. An
accessible proof source with explicit loopless-multigraph conventions is
M. DeVos, E. Rollová, and R. Šámal, “A new proof of Seymour's 6-flow theorem”,
arXiv:1512.06214.

The equal-order group-flow existence theorem is W. T. Tutte, “A contribution to
the theory of chromatic polynomials”, *Canadian Journal of Mathematics* **6**
(1954), 80–91.

Two statements remain distinct:

- existence of an integer \(k\)-flow is equivalent to existence of a nowhere-zero
  flow over any finite abelian group of order \(k\);
- the number of nowhere-zero group flows depends only on the order of the group.

Only existence is used. The counting theorem does not equate bounded integer
flows with group flows.

### 4.3 Loop and parallel-edge conventions

In an oriented boundary, a loop contributes \(f(e)-f(e)=0\). In the current
`incidenceSet` convention it occurs once and contributes \(f(e)\). Thus a
one-vertex one-loop graph admits a standard nonzero group flow but no present
`NowhereZeroFlow`. The interface must remain loopless until an oriented
loop-aware API is introduced.

Parallel edges cause no mismatch: they are distinct edge objects and are counted
separately at both endpoints.

## 5. Expansion-first outer shell

### Theorem 5.1 — flow-independent affine outer shell

Let \(G\) be a loopless multigraph with finite active edge set and no singleton
cut. Then there exist a finite loopless cubic bridgeless multigraph \(H\),
collapse data \((\pi,\lambda)\), and a nowhere-zero
\(\mathbf F_2^3\)-flow on \(H\), with

\[
|V(H)|=2|E(G)|,\qquad |E(H)|=3|E(G)|.
\]

#### Proof

Choose arbitrary cyclic orders, apply Theorems 3.1 and 3.2, and then apply
External Theorem 4.1 to \(H\). \(\square\)

The valid dependency is

\[
G\longrightarrow H\longrightarrow(H,f).
\]

The expansion does not use a flow.

## 6. Fixed-order extension criterion and sharpness

Let a degree-\(d\) vertex have prescribed nonzero values

\[
a_1,\dots,a_d\in\Gamma,
\qquad \sum_{i=1}^d a_i=0,
\]

listed in a chosen cyclic order, where \(\Gamma\) is elementary abelian of
exponent two. Put \(s_0=0\) and \(s_i=a_1+\cdots+a_i\). Let \(c_i\) be the
internal edge from port \(i\) to port \(i+1\), with \(c_d\) closing the cycle.

### Proposition 6.1 — local extension criterion

Every extension has the form

\[
\widetilde f(c_i)=t+s_i\qquad(1\le i\le d)
\tag{6.1}
\]

for one \(t\in\Gamma\), where \(s_d=0\). A nowhere-zero extension exists if
and only if

\[
\{s_0,s_1,\dots,s_{d-1}\}\ne\Gamma.
\tag{6.2}
\]

#### Proof

Conservation at port \(i\) is

\[
\widetilde f(c_{i-1})+a_i+\widetilde f(c_i)=0,
\]

with \(c_0=c_d\). Starting with \(\widetilde f(c_d)=t\), recursion gives
(6.1); the closing equation holds because \(s_d=0\). Nonvanishing is exactly
the condition that \(t\) avoid
\(\{s_1,\dots,s_d\}=\{s_0,\dots,s_{d-1}\}\). \(\square\)

For \(\Gamma=\mathbf F_2^3\), every fixed order of degree at most seven extends.
Degree eight is sharp: successive differences along a cyclic Gray tour through
all eight points form a zero-sum list of nonzero values whose proper prefixes
exhaust \(\mathbf F_2^3\). Thus a preselected flow can fail over a preselected
cyclic order. This does not obstruct an order chosen from the flow.

## 7. Adaptive prefix avoidance

### Theorem 7.1 — finite binary rank at least two

Let \(\Gamma\) be a finite elementary abelian \(2\)-group with
\(|\Gamma|\ge4\). Let \(A\) be a finite zero-sum multiset of nonzero elements.
Its occurrences admit an ordering \(a_1,\dots,a_d\) and there is a nonzero
\(q\in\Gamma\) such that

\[
q\notin\{s_0,s_1,\dots,s_{d-1}\},
\qquad s_i=a_1+\cdots+a_i.
\tag{7.1}
\]

For the empty multiset, choose any nonzero \(q\).

#### Proof

Let \(n_a\) be the multiplicity of \(a\ne0\), and let

\[
P:=\{a\ne0:n_a\equiv1\pmod2\}.
\]

Pairs cancel in characteristic two, so

\[
\sum_{a\in P}a=0.
\tag{7.2}
\]

Write \(n_a=\mathbf1_P(a)+2m_a\).

Suppose first that \(P\ne\varnothing\). Order its distinct elements arbitrarily
as \(b_1,\dots,b_k\). Their proper-prefix sequence has \(k\) entries including
zero, while \(1\le k\le|\Gamma|-1\). It therefore omits an element \(q\), and
\(q\ne0\).

At state zero insert every adjacent pair \(a,a\) with \(a\ne q\), with the
required multiplicity. Traverse \(b_1\), insert every \(q,q\) pair at state
\(b_1\), and continue with \(b_2,\dots,b_k\). Every inserted pair is a closed
two-step excursion. An \(a,a\) excursion from zero visits only \(0,a\ne q\).
A \(q,q\) excursion from \(b_1\) visits only \(b_1,b_1+q\); neither is \(q\),
since \(b_1\ne q\) and \(b_1\ne0\). The base prefixes and all excursions avoid
\(q\).

Now suppose \(P=\varnothing\). If \(A\) is empty, the stated choice works.
Otherwise choose a colour \(b\) occurring in \(A\), reserve one pair \(b,b\),
and choose \(q\notin\{0,b\}\), possible because \(|\Gamma|\ge4\). At state
zero insert every remaining pair \(a,a\) with \(a\ne q\). Traverse the first
reserved \(b\), insert all \(q,q\) pairs at state \(b\), and traverse the second
reserved \(b\) back to zero. The same excursion check avoids \(q\).

Thus (7.1) holds. \(\square\)

### Proposition 7.2 — sharp rank boundary

Rank one is false: in \(\mathbf F_2\), the multiset \([1,1]\) has proper
prefixes \(0,1\) in every ordering. Rank two is the first valid rank.

## 8. Flow-preserving adaptive expansion

### Theorem 8.1 — adaptive port-cycle extension

Let \(G\) be a finite-active-edge loopless multigraph carrying a nowhere-zero
\(\Gamma\)-flow, where \(\Gamma\) is a finite elementary abelian \(2\)-group of
rank at least two. One can choose the cyclic order at every active vertex so that
the resulting port-cycle expansion \(H\) carries a nowhere-zero
\(\Gamma\)-flow \(\widetilde f\) with

\[
\widetilde f(\lambda(e))=f(e)
\]

for every original edge \(e\). If \(G\) has no singleton cut, then \(H\) is
bridgeless and has the exact sizes and collapse data of Theorem 3.1.

#### Proof

At an active vertex \(v\), the incident flow values form a finite zero-sum
multiset of nonzero elements. Apply Theorem 7.1 to order the incidences and
choose an omitted nonzero \(q_v\). The linear ordering supplies a cyclic order
and a chosen start port.

Write the ordered values as \(a_{v,1},\dots,a_{v,d(v)}\), with prefix sums
\(s_{v,i}\). On the internal edge \(c_{v,i}\), define

\[
\widetilde f(c_{v,i})=q_v+s_{v,i}
\qquad(1\le i\le d(v)),
\]

where \(s_{v,d(v)}=0\). The set
\(\{s_{v,1},\dots,s_{v,d(v)}\}\) equals the proper-prefix set in (7.1), so every
internal value is nonzero. Proposition 6.1 gives conservation at every port. On
external edges retain \(f(e)\).

Choices at distinct active vertices are independent. In degree two the two
indexed internal edges are precisely the two distinct parallel fibre edges, and
the same equations apply. Isolated vertices have no ports. Rotating the chosen
start changes indexing only, not the existence statement.

The graph-theoretic conclusions follow from Theorems 3.1 and 3.2. \(\square\)

### Corollary 8.2 — adaptive \(\mathbf F_2^3\) outer shell

Let \(G\) be loopless, finite-active-edge, and without singleton cuts. Apply
External Theorem 4.1 downstairs, then Theorem 8.1. This yields

\[
G\longrightarrow(G,f)\longrightarrow
(H,\widetilde f,\pi,\lambda),
\]

where \(H\) is finite, loopless, cubic, and bridgeless, the original flow values
are preserved on lifted edges, and

\[
|V(H)|=2|E(G)|,\qquad |E(H)|=3|E(G)|.
\]

## 9. Comparison of the two routes

| Feature | Expansion-first | Adaptive flow-first |
|---|---|---|
| Spine | \(G\to H\to(H,f)\) | \(G\to(G,f)\to(H,\widetilde f)\) |
| Cyclic orders | arbitrary, flow-independent | chosen from local flow multisets |
| External theorem | applied to cubic \(H\) | applied to original \(G\) |
| Preserves selected downstairs flow | not asserted | yes |
| Uses adaptive theorem | no | yes |
| Degree-eight fixed-order obstruction | irrelevant | removed by changing order |
| Functoriality burden | noncanonical cyclic orders | additional flow, ordering, omitted point, and start choices |
| Paper exposition | longer detour | preferred concise spine |
| Likely Lean cost | lower local combinatorial cost | higher multiset and prefix infrastructure |
| Independent value | flow-free expansion theorem | stronger data-preserving expansion |

Neither route is canonically functorial without packaging choices. Expansion-first
is equivariant only after cyclic orders are transported. Adaptive flow-first
depends additionally on a selected flow and adaptive witnesses.

Paper A should use adaptive flow-first as the primary concise proof and retain
expansion-first as an independent alternative theorem. This chapter does not
choose the Lean route. On current evidence expansion-first is cheaper locally,
while adaptive flow-first provides stronger data and may become preferable if a
clean multiset ordering API is available.

## 10. Cut-even handoff

Assume the rank-three affine theorem supplies, on the finite loopless cubic flow
graph \(H\), a finite multiset

\[
\mathcal F'=[F'_1,\dots,F'_m]
\]

of vertex-even edge supports with exact double coverage. Since \(H\) is
loopless, finite vertex-even supports are cut-even.

For a support \(F'\subseteq E(H)\), define

\[
\operatorname{proj}(F'):=\{e\in E(G):\lambda(e)\in F'\}.
\]

### Theorem 10.1 — cut-even projection

If \(F'\) is a finite cut-even support in \(H\), then
\(\operatorname{proj}(F')\) is cut-even in \(G\). Projecting \(\mathcal F'\)
memberwise gives a multiset cut-even double cover of \(G\).

#### Proof

For every \(S\subseteq V(G)\), the collapse laws give a bijection

\[
\operatorname{proj}(F')\cap\delta_G(S)
\longleftrightarrow
F'\cap\delta_H(\pi^{-1}S)
\]

through \(e\mapsto\lambda(e)\). Thus the finite sets have equal parity. Exact
coverage follows from

\[
e\in\operatorname{proj}(F')\iff\lambda(e)\in F'.
\]

Repeated and empty projected supports are retained with multiset multiplicity.
\(\square\)

No circuit-by-circuit projection is asserted. An auxiliary fibre circuit may
project to the empty support, and distinct upstairs supports may have the same
projection. These are harmless at the cut-even multiset level.

The canonical handoff is

\[
\boxed{
\text{outer shell + affine even cover}
\Longrightarrow
\text{multiset cut-even double cover of the loopless core}.}
\]

The chapter `even-cover-and-collapse.md` then performs one finite circuit
decomposition downstairs and handles loop deletion and singleton-loop
reinsertion. Decomposing upstairs would add structure that collapse does not
preserve.

## 11. Loops and the full theorem

For a multigraph \(G\) with finite active edge set and no bridges, delete all
loops to obtain \(G_0\). Loops cross no cut, so deletion preserves the cut
condition on nonloop edges. Apply either outer-shell route to \(G_0\), then the
affine rank-three theorem, then Theorem 10.1. Decompose the resulting finite
cut-even supports into circuits once, downstairs. For every deleted loop \(e\),
add two occurrences of the singleton circuit \(\{e\}\).

Thus looplessness is an internal reduction condition forced by the present flow
and incidence interfaces, not a hypothesis of the natural public theorem.

## 12. Finiteness ledger

| Step | Weakest finiteness used |
|---|---|
| active vertices and degrees | \(E(G)\) finite |
| cyclic orders and adaptive multisets | finite active incidence sets |
| expansion and exact sizes | finite active edges, looplessness |
| Seymour/Tutte | finite active graph after discarding isolated ambient vertices |
| affine application | finite expanded active graph |
| vertex-even/cut-even bridge | finite support |
| collapse transport | finite transported support |
| circuit decomposition | finite support |
| ambient carriers | not required |

No step requires connectedness.

## 13. Reliability classification

| Statement | Status |
|---|---|
| active finiteness and degree lemmas | elementary paper proof here |
| port-cycle expansion, sizes, collapse | reviewed M1 paper proof promoted here |
| preservation of bridgelessness | reviewed M1 paper proof promoted here |
| `BinaryEightFlow` | classical external theorem boundary; not Lean-checked here |
| componentwise, \(6\to8\), loopless adapter | reviewed M2 source audit promoted here |
| fixed-order criterion and degree-eight example | reviewed M1 paper proof |
| adaptive prefix avoidance | Director-reviewed paper theorem from accepted adaptive source |
| adaptive flow-preserving expansion | paper corollary; not Lean-formalized |
| affine compatible-family construction | machine-checked only in the existing companion presentation |
| graph-level multiset even-cover factorization | canonical paper architecture; not checked in that form |
| cut-even bridge and collapse | canonical paper proof in `even-cover-and-collapse.md` |
| unconditional endpoint | mathematical composition target; not proved in Lean |

The current public `Statement.lean` remains an earlier loopless,
ambient-finite, unproved declaration. Nothing here changes it.

## 14. Formalization boundary

Mathlib supplies the multigraph substrate but the audited checkpoint contained
no reusable graph-level nowhere-zero-flow package, Seymour theorem, or Tutte
theorem. The public AffineCDC repository contains `Port.NowhereZeroFlow` and the
already-cubic flow corollary, but no theorem producing a flow from
bridgelessness.

A formal outer shell therefore requires an explicit Director choice among an
isolated external `BinaryEightFlow` theorem boundary, a future imported flow
library, or a major independent formalization of oriented flows, Tutte, and
Seymour. The local implementation must also formalize active-edge finiteness,
port-cycle edge objects, degree-two parallel fibres, collapse data, the
graph-level even-cover interface, and cut-even transport. Adaptive flow-first
adds odd-support decomposition, ordering and prefix witnesses, and the extension
adapter.

No Lean work is performed in this promotion packet.

## 15. Canonical theorem spine

After acceptance, the chapter supports the following sequence:

1. `active_vertices_finite`;
2. `active_degree_ge_two`;
3. `exists_port_cycle_expansion`;
4. `port_cycle_expansion_bridgeless`;
5. `binary_eight_flow` — isolated external input;
6. `exists_expansion_first_outer_shell`;
7. `adaptive_prefix_avoidance`;
8. `fixed_binary_flow_admits_adaptive_port_expansion`;
9. `exists_adaptive_flow_first_outer_shell`;
10. `project_cut_even_double_cover`;
11. `outer_shell_to_cut_even_double_cover`.

The outer shell ends at item 11. Final circuit decomposition and loop
reinsertion remain in `even-cover-and-collapse.md`.

## 16. Higher possibility found

Outside the present scope lie: a canonical or automorphism-equivariant adaptive
ordering; optimization of internal values or control of the omitted point; and
analogues for finite abelian groups not of exponent two. None is required for
the outer shell, and none is promoted here.
