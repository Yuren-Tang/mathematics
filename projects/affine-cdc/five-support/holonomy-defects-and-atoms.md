# Interior holonomy, defect geometry, and route-locked atoms

## 1. From boundary routing to an interior affine action

The Type H four-pole kernel contains a rainbow triangle in the boundary routing automaton. A traversal returns to the same support-unordered boundary state but permutes the five support indices.

Let $P$ be the four-pole. An indexed five-support chain is an element of

$$
C_1(P)\otimes E_5.
$$

Two chains with the same boundary differ by

$$
M_P:=Z_1(P;\mathbf F_2)\otimes E_5.
$$

For a lifted loop, let $\pi\in S_5$ be its support monodromy and define

$$
z=x^\gamma+\pi x\in M_P.
$$

The complete ambient interior datum is

$$
(\pi,z)\in M_P\rtimes S_5,
$$

acting by

$$
u\longmapsto\pi u+z.
$$

## 2. Norm defects

Let $m=\operatorname{ord}(\pi)$ and

$$
N_\pi=1+\pi+\cdots+\pi^{m-1}.
$$

Repeated traversal gives

$$
A_{\pi,z}^m(u)=u+d,
\qquad
d=N_\pi z.
$$

Changing the affine origin replaces $z$ by $z+(1+\pi)y$ and leaves $d$ unchanged.

### Theorem 2.1 — cyclic affine classification

For the four monodromy types occurring in the rainbow triangle,

$$
2^21,\qquad41,\qquad32,\qquad5,
$$

one has

$$
H^1(\langle\pi\rangle,E_5)=0.
$$

Therefore:

- if $d\ne0$, the lifted loop has period doubling and a nontrivial pure interior translation;
- if $d=0$, the ambient action is translation-conjugate to the pure permutation $\pi$.

The possible fixed coefficient channels have dimensions $2,1,1,0$ respectively.

This is an ambient classification. The conjugating origin need not preserve the edgewise root condition.

## 3. The root-fibre section problem

Assume $d=0$. Root-admissible linearisation is equivalent to finding a root-valued flow $r$ with

$$
(1+\pi)r=t_\gamma,
$$

where $t_\gamma=x+x^\gamma$ is the actual switch flow of the lifted loop.

For every edge define the finite fibre

$$
\mathcal R_e
=
\{r\in R_5:(1+\pi)r=t_\gamma(e)\}.
$$

At every internal cubic vertex define the relation of triples in the incident fibres whose sum is zero.

A root-admissible linearisation is exactly a global section of this finite local system with the prescribed terminal values.

Failure has three local-to-global levels:

1. an empty edge fibre;
2. nonempty edge fibres but an empty cubic vertex relation;
3. nonempty local relations with nontrivial component holonomy.

## 4. The genuine three-switch word

A physical rainbow loop is the composite of three terminal-path switches $P_0,P_1,P_2$. The first and third coefficients agree. For independent $u,v\in E_5$,

$$
\boxed{
t_\gamma
=
(P_0\triangle P_2)\otimes u
+
P_1\otimes v.
}
$$

Thus the switch flow lies in the plane

$$
W=\langle u,v\rangle\cong\mathbf F_2^2.
$$

This formula removes most of the abstract finite-state universe. The actual root-fibre problem is controlled by one low-rank flow and three connected path systems.

## 5. Tait-resolution equivalence

### Full-rank monodromy types $41$ and $5$

The actual root fibres above $W$ are empty exactly at switch-flow value zero. If every edge value is nonzero, the switch flow is a nowhere-zero $\mathbf F_2^2$ flow and hence a Tait colouring. Type $5$ lifts uniquely; type $41$ leaves one binary extension, which always solves after the edge-local test.

### Rank-one monodromy types $32$ and $2^21$

The switch flow takes values in $\{0,\kappa\}$.

- the zero edges form a matching;
- the $\kappa$ edges form a degree-two system consisting of one terminal path and closed cycles;
- an all-zero cubic vertex has an empty local root relation;
- otherwise a root lift exists exactly when every degree-two component has even order.

This parity condition is precisely the triviality of a two-sheeted or affine-correspondence holonomy around each component.

### Theorem 5.1 — root lifting equals Tait resolution

A genuine zero-norm rainbow loop is root-admissibly linearizable if and only if its switch flow admits a Tait resolution.

For the genuine path word the rank-one relation sharpens further:

$$
P_1=P_0\triangle P_2.
$$

Hence the nonzero support is exactly the single middle terminal path; the apparent odd closed-component branch from the unrestricted quotient-flow model disappears.

A rank-one loop either misses an internal vertex, producing an empty local relation, or its middle path is spanning and the Tait resolution exists.

For full-rank types, the success criterion is

$$
E(P)=P_1\cup(P_0\triangle P_2).
$$

The residual certificate is an uncovered edge.

## 6. Type H Tait escape

A Tait colouring of a four-pole produces three bicoloured even subgraphs and, after adding two empty supports, a boundary state $B_i$.

At this $B_i$ state the empty/full challenge and the partition/partition challenge are the same symmetric-difference subgraph, so they have the same actual route.

The deterministic policy of every BBD Type H triangle requires these two challenges to use different routes. The actual common route can satisfy at most one; the other genuine Kempe switch leaves the triangle profile. For the DDD triangle, any Tait colouring immediately creates a $B_i$ state outside the DDD profile.

### Theorem 6.1 — Tait-escape theorem

In a minimal Type H kernel,

$$
\boxed{
\text{zero norm}
+
\text{root-admissible linearisation}
\Longrightarrow
\text{strict boundary-profile expansion}.
}
$$

Therefore the soluble zero-norm branch is eliminated rather than merely rephrased.

## 7. Global BBD holonomy

The BBD triangle has sixteen support monodromies. Their raw lifts admit four binary coordinates, but these coordinates do not form a common $V_4$ subgroup of $S_5$; the correct finite structure is a left-right bitorsor rectangle.

Let $\mathcal H\le M_P\rtimes S_5$ be the group generated by all physical based BBD loops. Its projection onto $S_5$ is surjective.

Let $T$ be its pure translation kernel. Every $v\in T$ sends the initial root cover $x$ to another root-valued cover. For each edge, the evaluation image $T_e$ is an $S_5$-submodule of the irreducible even module $E_5$. Hence $T_e$ is $0$ or $E_5$. The latter is impossible because an affine $E_5$-coset contains zero and co-roots, not only roots.

### Theorem 7.1 — root rigidity

$$
T=0.
$$

Thus the physical holonomy group is the graph of one $S_5$-cocycle.

Moreover,

$$
H^1(S_5,E_5)=0,
$$

and therefore also $H^1(S_5,M_P)=0$. There is a unique simultaneous ambient origin $y$ such that every BBD affine holonomy becomes purely linear.

Set

$$
r=x+y.
$$

This is one canonical $E_5$-valued flow with the original terminal values.

- if $r$ is root-valued, Type H escapes by a Tait resolution;
- otherwise every defect edge is zero-valued or co-root-valued.

The earlier per-loop norm, missed-vertex, and uncovered-edge diagnostics become subordinate views of this one canonical flow.

## 8. The $K_6$ completion of $E_5$

Adjoin a symbol $\infty$ and put

$$
q_\infty=0,
\qquad
q_i=\mathbf1+e_i.
$$

Map an edge $\{a,b\}$ of $K_6$ to

$$
q_a+q_b\in E_5\setminus\{0\}.
$$

### Theorem 8.1 — $K_6$ edge model

This is a bijection

$$
E(K_6)\cong E_5\setminus\{0\}.
$$

The ten edges inside $K_5$ are roots; the five edges incident with $\infty$ are co-roots.

Three distinct nonzero vectors sum to zero exactly when the corresponding $K_6$ edges form either:

1. a triangle; or
2. a perfect matching.

Thus cubic conservation of the canonical flow has a complete local geometry.

## 9. Zero networks and co-root strips

If an edge has value zero, conservation makes the other two continuation values equal. Zero edges form equality wires with degree-one equality gates and degree-three all-zero branch vertices.

If there are no zero edges, the co-root edges have local degree:

- $0$ at a root triangle;
- $2$ at a triangle through $\infty$;
- $1$ at a $K_6$ one-factor vertex.

### Theorem 9.1 — defect-strip decomposition

The co-root subgraph is a disjoint union of internal paths and cycles. Path endpoints are exactly the one-factor vertices.

This identifies the bounded local interface at which perfect-matching and snark-factorisation methods may enter. It does not itself provide a valid replacement.

## 10. Variational defect forests

Among all $E_5$ flows with the fixed terminal roots, choose one minimizing the number of non-root edges. Toggle any internal cycle by a root or co-root coefficient. Averaging the defect change gives the cycle inequalities

$$
2R(C)\ge5Z(C)+3D(C),
$$

and

$$
R(C)\ge2D(C),
$$

where $R,Z,D$ count root, zero, and co-root edges on the cycle.

### Theorem 10.1 — defect forest

The complete defect support contains no graph cycle.

### Theorem 10.2 — induced-tree property

No root edge joins two vertices of one defect-tree component. Hence a defect tree with $k$ vertices has boundary size

$$
k+2.
$$

The six possible local weight patterns are:

$$
(2,2,2),\ (0,2,2),\ (2,2,4),\ (2,4,4),\ (0,4,4),\ (0,0,0).
$$

They give root triangles, equality leaves, one-factor leaves, co-root transport vertices, mixed branches, and all-zero branches.

## 11. Petersen transport

A one-factor endpoint state containing co-root $q_i$ corresponds to an edge of the Petersen graph in its Kneser model. The fifteen endpoint states are exactly the fifteen Petersen edges.

At a degree-two co-root transport vertex, the endpoint state moves to an adjacent Petersen edge. Therefore the transport graph is

$$
L(\mathrm{Petersen}).
$$

Each turn also emits one side-root label, the third Petersen neighbour of the shared endpoint. A strip is therefore an enriched transducer:

$$
\text{walk in }L(\mathrm{Petersen})
+
\text{side-root output word}.
$$

Repeated transport state alone does not justify pumping or deletion, because the emitted side semantics and attached root components may differ.

## 12. Co-root atoms and DDD triality

The smallest nondegenerate co-root component is one co-root edge between two one-factor leaves. Its four terminal roots admit exactly three pairings:

- the original co-root realization;
- two crossed root-valued realizations.

These three internal labels form one perfect matching of $K_6$. Equivalently, the co-root atom is a Petersen edge and the two root resolutions are its endpoints.

The fifteen atoms are $S_5$-equivariantly bijective with the fifteen $K_6$ one-factors; the stabilizer is $D_8$.

This is a local resolution triality. A crossed pairing changes the incidence of terminal semiedges and therefore still requires a composition theorem.

## 13. Unique bad route and the locked quotient

For a bad atom boundary state with current pairing $12\mid34$, let $d$ be the forced internal sum and let $a$ be a full challenge. The three routes produce

$$
\begin{array}{c|c}
12\mid34&d,\\
13\mid24&d+a,\\
14\mid23&d+a.
\end{array}
$$

The crossed value $d+a$ is always a root.

### Theorem 13.1 — unique bad route

The original atom pairing is the unique route that remains bad.

If every full challenge is blocked, the safe-switch orbit is $K_{2,4}$. At a locked $C$-state, quotient by the co-root direction. The complementary root flow becomes a nowhere-zero $\mathbf F_2^3$ flow

$$
c:E(Q)\to V\setminus\{0\}
$$

with all four terminal values equal to one colour $g$. The four full challenges are the affine plane

$$
\Lambda_g=\{\lambda\in V^*: \lambda(g)=1\},
$$

and all four scalar subgraphs route the terminals as $12\mid34$.

## 14. Rank drop, curvature, and flat potential

If the quotient colours span rank two, every root label avoids one support coordinate. This is exactly the $K_4$/DDD sector and admits the rank-two Tait escape. Route-lock does not imply a graph two-edge cut; explicit rank-two witnesses have pair-separating cut four.

Assume full rank three. Let $E_g$ be the matching of edges of terminal colour $g$. Each of the four scalar partitions gives a side bit on the component containing a $g$-edge. The parity of the four bits is the unique non-affine function on $AG(2,2)$.

Changing side values on closed scalar cycles changes this parity vector by their intersections with $E_g$. The quotient class is

$$
\Omega(c)
\in
\mathbf F_2^{E_g}/B.
$$

### Theorem 14.1 — flat-potential equivalence

The following are equivalent:

1. $\Omega(c)=0$;
2. side choices can make every local four-bit word affine;
3. there is a vertex potential $p:V(Q)\to V$ with terminal values $0,0,g,g$ and
   $$
   p(u)+p(v)\in\{0,c(e)+g\}
   $$
   on every internal edge.

If $\Omega(c)\ne0$, duality gives a support

$$
\eta\subseteq E_g
$$

that is simultaneously a cut in all four scalar sheets and has odd terminal parity.

An explicit full-rank locked witness has $\Omega(c)\ne0$. Hence route-lock does not imply automatic flatness.

## 15. The DDD exception

The BBD global holonomy is killed by $S_5$ root rigidity and cohomology. The DDD subgroup is only $D_8$, and

$$
H^1(D_8,E_5)\cong\mathbf F_2.
$$

The nontrivial class is supported on a cycle whose roots lie in the complementary $K_4$. This is a genuine one-bit affine exception and must not be silently absorbed into the BBD simultaneous-origin theorem.

The curvature bit and the DDD cohomology class have the same one-dimensional representation type. Their canonical graph-level identification remains open.

## 16. Reliability boundary

The affine holonomy formulas, cyclic cohomology table, root-fibre section formulation, genuine switch-flow identity, Tait-resolution theorem, Type H Tait escape, BBD root-rigidity theorem, $S_5$ cohomology vanishing, $K_6$ completion, defect-strip theorem, variational forest theorem, Petersen transport, atom triality, unique bad route, rank-two escape, curvature duality, and flat-potential equivalence are theorem-level in the source surface, with stated finite tables where required.

The conversion of zero networks, co-root strips, Type T linkage, nonflat common cuts, flat potentials, or the DDD class into strict graph reduction remains open. No global five-support theorem follows yet.