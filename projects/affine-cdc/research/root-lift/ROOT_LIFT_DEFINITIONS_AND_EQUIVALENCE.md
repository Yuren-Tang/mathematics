# Indexed oriented supports and the corrected $A_{q-1}$ root-flow equivalence

## 1. Scope and assurance

This dossier is the bounded `AC-ROOT-LIFT-01` reconstruction of the generic integral correspondence. It is proved here independently of the OR1 analogy. The frozen OR1 material is used only later for comparison and remains

`AUTHORIAL / CURATOR-INTEGRATED / NOT YET INDEPENDENTLY VERIFIED`.

Throughout the main theorem:

- $G$ is a finite loopless multigraph, possibly disconnected;
- parallel edge objects are distinct;
- $I$ is a finite index set of cardinality $q\ge 3$;
- every edge has a fixed reference orientation;
- empty indices and repeated support values at different indices are allowed.

A loop extension is stated separately in §10.

Put

$$
A_I=\left\{x\in\mathbf Z^I:\sum_{i\in I}x_i=0\right\},
\qquad
\Phi_I=\{\pm(\varepsilon_i-\varepsilon_j):i\ne j\}.
$$

Thus $A_I$ is the type-$A_{q-1}$ root lattice and $\Phi_I$ is its root set.

For a vertex $v$ and a reference-oriented edge $e$, let

$$
\partial_{v,e}=
\begin{cases}
+1,&e\text{ enters }v,\\
-1,&e\text{ leaves }v,\\
0,&e\text{ is not incident with }v.
\end{cases}
$$

## 2. Four different witness levels

The following objects must not be conflated.

### 2.1 Directed indexed support system

A **directed indexed $q$-support system** is a family $(D_i)_{i\in I}$ such that:

1. $D_i$ is a set of directed uses of edge objects of $G$;
2. each edge object $e$ occurs in exactly two distinct indices $i(e)\ne j(e)$;
3. the two directed uses of $e$ are opposite;
4. for every $i$ and every vertex, the number of $D_i$-edges entering equals the number leaving.

The fourth condition says that every $D_i$ is a directed Eulerian subgraph. An empty $D_i$ is retained as an indexed empty support.

### 2.2 Full indexed oriented $q$-CDC

A **full indexed oriented $q$-CDC** is a family

$$
\mathcal C=(\mathcal C_i)_{i\in I}
$$

where each $\mathcal C_i$ is a finite multiset of directed circuit occurrences, with the following properties:

1. every directed edge use in $\mathcal C_i$ belongs to index $i$;
2. each source edge object occurs in exactly two circuit occurrences carrying distinct indices;
3. those two occurrences traverse the source edge in opposite directions.

A circuit is an edge-simple directed closed trail; repeated circuit values remain distinct multiset occurrences. The full witness therefore retains the circuit partition, cyclic order, index, and occurrence multiplicity.

### 2.3 Support word

The **support word** of a full witness forgets the circuit partition and cyclic order and retains only the directed indexed supports $(D_i)$. Distinct full witnesses may have the same support word.

### 2.4 Unoriented support data

Forgetting directions gives indexed edge supports $(F_i)_{i\in I}$ with every edge in exactly two distinct supports. This forgets both the sign of each root and every circuit decomposition.

## 3. Integral root flow

An **$A_{q-1}$ root flow** on the reference-oriented graph is a map

$$
\varphi:E(G)\longrightarrow\Phi_I
$$

satisfying the Kirchhoff law

$$
\sum_{e\in E(G)}\partial_{v,e}\,\varphi(e)=0
\quad\text{in }A_I
\qquad(v\in V(G)).
$$

It is nowhere-zero automatically because every value is a root.

Changing the reference orientation of one edge replaces both its incidence column and its value by their negatives. Hence the underlying flow datum is independent of reference orientations up to the standard sign action.

## 4. Forward construction

Let $(D_i)_{i\in I}$ be a directed indexed $q$-support system. For an edge $e$, let $i\ne j$ be its two support indices. Define

$$
s_i(e)=
\begin{cases}
+1,&D_i\text{ traverses }e\text{ along the reference orientation},\\
-1,&D_i\text{ traverses }e\text{ against it}.
\end{cases}
$$

Opposite traversal gives $s_j(e)=-s_i(e)$. Set

$$
\boxed{\varphi(e)=s_i(e)(\varepsilon_i-\varepsilon_j).}
$$

This is independent of the order in which the two indices are named.

### Theorem 4.1 — forward root-flow theorem

The map $\varphi$ is an $A_{q-1}$ root flow.

### Proof

For a fixed coordinate $i$, the $i$-coordinate of $\varphi(e)$ is exactly the signed direction of the $D_i$-use of $e$, and is zero when $e\notin D_i$. Therefore

$$
\sum_e\partial_{v,e}\varphi_i(e)=0
$$

is precisely the equality of the number of $D_i$-edges entering and leaving $v$. This holds for every $i$, so the vector Kirchhoff equation holds. ∎

A full indexed oriented $q$-CDC first forgets to its support word and then gives the same root flow.

## 5. Reverse construction

Let $\varphi:E(G)\to\Phi_I$ be an $A_{q-1}$ root flow. Every root has a unique ordered presentation

$$
\varphi(e)=\varepsilon_{p(e)}-\varepsilon_{n(e)}.
$$

Put $e$ into $D_{p(e)}$ along the reference orientation and into $D_{n(e)}$ against the reference orientation.

### Theorem 5.1 — canonical reverse support theorem

The family $(D_i)_{i\in I}$ is a directed indexed $q$-support system, and the constructions of §§4–5 are mutually inverse.

### Proof

Each root has exactly one $+1$ and one $-1$ coordinate, so every edge occurs at exactly two distinct indices and the two uses are opposite. The $i$-coordinate of the Kirchhoff equation is exactly directed balance of $D_i$ at every vertex. Mutual inversion is immediate edge by edge. ∎

Thus the exact canonical equivalence is

$$
\boxed{
\text{directed indexed Eulerian $q$-support systems}
\ \longleftrightarrow\
\text{$A_{q-1}$ root flows}.}
$$

It is equivariant under permutations of $I$ and under reference-edge reversal.

## 6. Circuit decomposition

### Lemma 6.1 — finite directed Eulerian decomposition

Every finite directed Eulerian multigraph decomposes into a finite multiset of directed circuits, using every directed edge object exactly once.

### Proof

If no edge remains, stop. Otherwise follow outgoing edges from any incident vertex. Balance prevents the walk from getting stuck away from its start, and finiteness forces a repeated vertex. The segment between two consecutive appearances of that vertex contains a directed circuit. Remove its edges; balance is preserved. Induct on the number of remaining edges. ∎

Applying the lemma independently to every nonempty $D_i$ gives a full indexed oriented $q$-CDC.

### Theorem 6.2 — corrected full-witness statement

An $A_{q-1}$ root flow determines a full indexed oriented $q$-CDC **only after a choice of directed circuit decomposition for each coordinate support**. Conversely, every full witness determines a root flow, but the composite back to a full witness need not recover the original circuit occurrences.

Hence

$$
\text{full indexed oriented $q$-CDC}
\longrightarrow
\text{$A_{q-1}$ root flow}
$$

is generally many-to-one.

## 7. Exact nonuniqueness counterexample

Let $G$ have two vertices $u,v$ and four parallel edges $a,b,c,d$. Reference-orient $a,b$ from $u$ to $v$ and $c,d$ from $v$ to $u$. For any $q\ge3$, use only indices $1,2$ and set

$$
\varphi(e)=\varepsilon_1-\varepsilon_2
\qquad(e=a,b,c,d).
$$

This is a root flow: at both vertices two reference edges enter and two leave. The index-$1$ support has two $u\to v$ and two $v\to u$ edges. It has at least the two circuit decompositions

$$
\{(a,c),(b,d)\},
\qquad
\{(a,d),(b,c)\}.
$$

The opposite decompositions occur at index $2$. Both full oriented witnesses induce the same root flow. Therefore a root flow does not canonically recover circuit occurrence pairing or multiplicity ledger beyond the edge-to-index incidence itself.

## 8. Prescribed full witnesses

Suppose a full unoriented indexed circuit witness is already prescribed. A root flow reconstructs that prescribed witness exactly only if:

1. its unordered edge root at every edge is the prescribed pair of indices;
2. its signs orient every prescribed circuit consistently;
3. the two prescribed occurrences at each edge receive opposite directions.

The second and third conditions are a genuine sign-lift problem treated in `MOD2_REDUCTION_AND_FIXED_WITNESS_OBSTRUCTION.md`. Coordinatewise Eulerianity alone proves only the existence of some decomposition, not compatibility with the prescribed one.

## 9. Multiplicity, repeated supports, and empty indices

The root flow retains exactly:

- the two distinct support indices of every edge;
- the direction used at each of those indices;
- the resulting directed support word;
- which indices are empty.

It does not retain:

- how one directed support is partitioned into circuits;
- the cyclic starting point of a circuit occurrence;
- a pre-existing occurrence name;
- a surface rotation or partner map not determined by the support word.

Equal support words at different indices remain different coordinates. Repeated circuit values after decomposition remain distinct multiset occurrences.

## 10. Loop convention

The main equivalence is loopless. It extends to loops only after fixing a two-dart convention:

- every loop has two opposite reference traversal directions;
- a loop labelled by $\pm(\varepsilon_i-\varepsilon_j)$ contributes one singleton directed loop occurrence at $i$ and the opposite singleton occurrence at $j$;
- a loop contributes zero to every vertex Kirchhoff equation, as its two half-edge incidences cancel.

Without this explicit dart convention, a root value on a loop does not by itself specify the two directed singleton occurrences.

## 11. Classification

| Assertion | Classification |
|---|---|
| directed indexed Eulerian $q$-supports $\leftrightarrow$ $A_{q-1}$ root flows | proved equivalence |
| root flow $\Rightarrow$ some full oriented $q$-CDC | proved only after circuit decomposition |
| full oriented witness $\leftrightarrow$ root flow canonically | false / scope-corrected |
| root flow recovers a prescribed circuit partition | false without extra compatibility data |
| reference orientation affects the intrinsic object | false; standard sign change only |
| disconnected graphs and empty indices | covered componentwise |
| loops | covered only under the explicit two-dart convention |
