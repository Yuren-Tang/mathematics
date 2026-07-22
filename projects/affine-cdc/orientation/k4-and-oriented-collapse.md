# The $K_4$ fibre, orientation data loss, and enriched collapse

## 1. The standard $K_4$ flow

Let

$$
W=\{0,x,y,z\}\leq\Gamma=\mathbf F_2^3,
\qquad z=x+y,
$$

and take the vertex set of $K_4$ to be $W$. Define

$$
f(uv)=u+v.
$$

Every edge has a nonzero value. At each vertex the three incident values are the three nonzero elements $x,y,z$ of $W$, whose sum is zero. Thus $f$ is a nowhere-zero rank-three flow.

## 2. A projective-plane lift

Define

$$
g_0(uv)=W\setminus\{0,f(uv)\}.
$$

The two retained elements sum to $f(uv)$, and the three roots at every source vertex are

$$
\{y,z\},\qquad \{z,x\},\qquad \{x,y\},
$$

so $g_0$ is compatible.

For $a\in\{x,y,z\}$, the $a$-direction edges form one perfect matching, and $F_a$ is its Hamiltonian four-cycle complement. Thus $g_0$ has three connected four-cycle face occurrences and no other nonempty faces. Therefore

$$
\chi(S_{g_0})=4-6+3=1.
$$

The surface is closed and connected, hence nonorientable; in fact it is the projective plane.

### Theorem 2.1

Compatibility and exact indexed edge double coverage do not force one prescribed compatible lift to be orientable.

## 3. A sphere lift in the same fibre

Define a vertex field by

$$
k_u=u.
$$

For every edge $uv$,

$$
k_u+k_v=f(uv),
$$

so $k\in H_f^0$ and

$$
\Lambda_f(k)=\mathbf 1_E.
$$

Translating $g_0$ by $k$ gives

$$
g_1(uv)=W\setminus\{u,v\}.
$$

For $a\in W$, the support $F_a$ is the triangle on $W\setminus\{a\}$. There are four triangular face occurrences, so

$$
\chi(S_{g_1})=4-6+4=2.
$$

This is the tetrahedral sphere and is orientable.

The all-edge word is not a cut in $K_4$, because it pairs nontrivially with every triangle. Hence the gauge law gives

$$
\omega(g_0)=[\mathbf 1_E]\ne0,
\qquad
\omega(g_1)=0.
$$

### Theorem 3.1 — exact fixed-fibre conclusion

The same fixed Fano-flow fibre contains both a projective-plane lift and a sphere lift.

Consequently:

1. per-lift automatic orientability is false;
2. gauge motion can change the fixed-lift orientation class;
3. this example is not a counterexample to fixed-fibre existence, because $\Omega_f=0$.

The example is an exact theorem, not a census or computational inference.

## 4. Support-only outer-shell boundary

Programme A's ordinary CDC route retains, after the affine construction:

- indexed even edge supports on the cubic expansion;
- cut parity after projection to the original loopless core;
- exact multiset double-coverage multiplicity;
- a generic undirected circuit decomposition after collapse.

It deliberately does not retain face directions, partner maps, or rotations in the outer shell. The checked theorem `Port.cubic_flow_cdc` likewise drops the rotation witness returned by `exists_indexed_dart_cover` and applies a generic support decomposition.

### Proposition 4.1

The support-only collapse/decomposition witness does not by itself transport an oriented CDC or an orientation class.

The missing data are:

- the directed cyclic order of each retained face occurrence;
- which occurrence uses each direction of an edge;
- the pairing of projected segments through one collapsed vertex cluster.

An arbitrary undirected decomposition may choose circuits unrelated to the original face boundaries. This is a data-loss boundary, not a counterexample to orientation-preserving collapse.

## 5. Enriched oriented collapse

Let $H$ be a finite loopless expanded graph and $G_0$ the loopless graph obtained by collapsing vertex fibres. Assume the Programme A collapse datum:

- a vertex map $\pi:V(H)\to V(G_0)$;
- an injective edge lift $\lambda:E(G_0)\to E(H)$ preserving endpoints;
- every non-lifted auxiliary edge lies inside one $\pi$-fibre;
- every edge joining different fibres is a lifted original edge.

Suppose $H$ carries an oriented circuit double cover: a finite multiset of directed circuit occurrences in which every edge occurs once in each direction.

For one directed circuit occurrence, delete all auxiliary edges from its cyclic dart sequence and replace every remaining $\lambda(e)$ by $e$, preserving the induced direction between collapse fibres.

### Lemma 5.1 — projected directed trail

The projection is either empty or a finite directed closed trail in $G_0$ with no repeated edge object.

Between consecutive lifted edges, the deleted auxiliary segment remains inside one collapse fibre, so endpoints match after projection. Closure comes from cyclicity, and injectivity of $\lambda$ prevents repeated projected edge objects.

The projected trail may revisit a collapsed vertex and therefore need not itself be a circuit.

## 6. Directed decomposition

### Lemma 6.1

Every finite nonempty directed closed trail in a multigraph decomposes into a finite multiset of directed circuits, using every directed edge occurrence exactly once and never reversing an edge.

Split at a repeated vertex and induct on the number of edge occurrences.

### Theorem 6.2 — enriched oriented-collapse transport

Under the enriched datum, an oriented circuit double cover of $H$ induces an oriented circuit double cover of $G_0$.

Every original edge $e$ has one lifted edge $\lambda(e)$, which appears upstairs exactly twice, once in each direction. Projection preserves those directions. Directed decomposition only partitions trails and does not reverse edges. Empty projections are discarded, and repeated circuit values retain multiset multiplicity.

### Corollary 6.3

If a compatible affine lift on the cubic expansion has orientable cycle-face surface, then the original loopless collapsed graph has an oriented CDC.

This corollary consumes the retained oriented face occurrences. It is not a consequence of the existing support-only collapse witness alone.

## 7. Loop-dart convention

The complete Programme A route deletes loops before the loopless cubic reduction. Under the natural dart convention, a loop has two opposite half-edge traversal directions.

After constructing an oriented CDC of the loopless core, reinsert every deleted loop by adding two singleton loop-circuit occurrences, one in each dart direction. This preserves the once-each-direction rule and leaves nonloop edges unchanged.

Any external oriented-CDC statement for multigraphs with loops must state this convention. The current Lean public statement is loopless and does not formalize this reinsertion.

## 8. Correct orientation-aware route

The valid implication chain is

$$
\begin{array}{c}
\text{loopless bridgeless core }G_0\\
\downarrow\\
\text{cubic expansion }H\text{ with a rank-three flow }f\\
\downarrow\\
\text{compatible lift fibre above }f\\
\downarrow\quad\Omega_f=0\\
\text{orientable retained cycle-face surface}\\
\downarrow\quad\text{enriched oriented collapse}\\
\text{directed closed trails on }G_0\\
\downarrow\quad\text{direction-preserving decomposition}\\
\text{oriented CDC of }G_0\\
\downarrow\quad\text{opposite singleton-loop reinsertion}\\
\text{oriented CDC of the original multigraph.}
\end{array}
$$

The unresolved implication is orientable-lift existence, not the enriched collapse transport.

## 9. Exact status table

| Statement | Status |
|---|---|
| every compatible lift is orientable | false; refuted by $g_0$ on $K_4$ |
| one fixed fibre may contain both surface types | authorially proved by $g_0,g_1$ |
| every fixed Fano-flow fibre contains an orientable lift | open |
| every bridgeless cubic graph admits some orientable affine lift | open |
| support-only collapse retains orientation witnesses | false as a witness claim; the data are discarded |
| enriched oriented collapse transports an oriented CDC | authorially proved |
| opposite loop-dart reinsertion preserves oriented coverage | authorially proved under the stated convention |

None of these OR1 authorial results is independently audited or end-to-end Lean verified at this candidate.
