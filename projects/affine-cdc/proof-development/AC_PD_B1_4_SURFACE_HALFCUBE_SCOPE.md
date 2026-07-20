# AC-PD-B1.4 — cycle-face surfaces, half-cube potentials, and fixed-lift scope

**Proof-development state:** `COMPLETE-DRAFT / SCOPE-CORRECTION`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Recovered controlling packets:** `FIVE_CDC_COLORED_SURFACE_DUAL_HALFCUBE_V1.md`, `FIVE_CDC_HALFCUBE_SCOPE_CORRECTION_V1.md`, and its displayed-table erratum at `research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`  
**Depends on:** B1.1  
**Immediate consumers:** B3 surface/dual/halfcube programme; B4 reconfiguration; B9 target/source composition frontier  
**External mathematical inputs:** none

## 0. Scope correction

There are three distinct statements.

1. A root lift is equivalent to a properly eight-face-coloured cycle-face embedding, hence to a properly eight-vertex-coloured dual triangular cellulation.
2. A homomorphism from the **full dual graph** to the five-coordinate half-cube produces a componentwise five-support compression on that fixed embedding.
3. A homomorphism from the **old-colour quotient** $J_g$ classifies only those compressions constant on all face components carrying the same old support index.

The graph-level existence theorem is bidirectional after the embedding is allowed to vary. For one arbitrary prescribed embedding, a five-support cover need not integrate to a half-cube potential unless its edge-root cocycle has zero dual holonomy. Thus the integrated phrase “for fixed $g$, $g$ yields a five-support cover iff $T_g^{(1)}\to\mathscr A_5$” is valid only when “yields” means **componentwise relabelling of the face components of $g$**.

## 1. Compatible root lifts

Let $G$ be a finite loopless cubic multigraph and let $I$ be an eight-element support-index set. A compatible root lift is an edge labelling

$$
g:E(G)\longrightarrow\binom I2
$$

such that at every cubic vertex there are three distinct indices $a,b,c\in I$ and the three incident labels are

$$
\{a,b\},\qquad\{b,c\},\qquad\{c,a\}.
$$

For $a\in I$, define

$$
F_a=\{e:a\in g(e)\}.
$$

At every vertex the local degree of $F_a$ is zero or two. Hence every nonempty connected component of $F_a$ is a finite circuit: an ordinary polygonal cycle or a parallel-edge digon.

## 2. Construction of the cycle-face surface

Attach one polygonal disc along every connected component of every $F_a$.

### Theorem 2.1 — closed surface construction

The resulting cell complex $S_g$ is a closed two-dimensional surface, possibly nonorientable, whose one-skeleton is $G$ and whose face boundaries are exactly the support-cycle components.

### Proof

Every source edge $e$ has a two-element root label $\{a,b\}$, so it lies on exactly two attached face discs, one of colour $a$ and one of colour $b$. Its interior therefore has a two-sided disc neighbourhood.

At a cubic vertex with local labels $ab,bc,ca$, the three face corners of colours $a,b,c$ occur cyclically and join to a three-edge link. The vertex link is a circle, so the vertex has a disc neighbourhood. There are no boundary edges or boundary vertices. Since the complex is finite and every point has a disc neighbourhood, it is a closed surface. Polygonal two-faces are allowed when $G$ has a parallel digon. $\square$

Each face inherits its support index. Two faces sharing an edge have the two distinct indices in that edge label, so the face colouring is proper.

### Theorem 2.2 — root-lift/surface equivalence

Compatible root lifts of $G$ with index set contained in $I$ are equivalent to cycle-face embeddings of $G$ in a closed surface together with a proper colouring of their face occurrences by $I$.

### Proof

The forward construction is Theorem 2.1. Conversely, label every source edge by the unordered pair of colours of its two incident face occurrences. At a cubic vertex the three face sectors are pairwise adjacent around the vertex; properness makes their colours $a,b,c$ distinct, and the three edge labels are $ab,bc,ca$. Thus the reconstructed labelling is a compatible root lift. The two constructions are inverse up to the natural cell-isomorphism. $\square$

## 3. Dual triangular cellulation

Let $T_g$ be the cellular dual of $S_g$.

- vertices of $T_g$ are individual support-cycle face components;
- dual edges are source edge objects of $G$;
- dual triangular faces are source vertices of $G$.

The proper face colouring gives a proper vertex colouring

$$
\kappa_g:V(T_g)\longrightarrow I.
$$

Thus a root lift is equivalently a closed triangular cellulation with a proper eight-colouring of its vertices. The full dual remembers distinct connected components of one old support; the colour quotient does not.

## 4. The five-coordinate half-cube

Let

$$
E_5=
\left\{x\in\mathbf F_2^5:\sum_{i=1}^5x_i=0\right\},
$$

and let

$$
R_5=\{x\in E_5:|\operatorname{supp}x|=2\}.
$$

Define the even half-cube graph $\mathscr A_5$ by

$$
V(\mathscr A_5)=E_5,
\qquad
xy\in E(\mathscr A_5)
\iff
x+y\in R_5.
$$

It is the Cayley graph of $E_5$ with root set $R_5$.

## 5. A dual potential produces five supports

Let

$$
\varphi:V(T_g)\longrightarrow E_5
$$

be a graph homomorphism $T_g^{(1)}\to\mathscr A_5$. If a source edge $e$ is dual to an edge $xy$ of $T_g$, put

$$
\lambda_\varphi(e)=\varphi(x)+\varphi(y)\in R_5.
$$

### Theorem 5.1 — componentwise half-cube compression

The map $\lambda_\varphi$ is a root-valued $E_5$-flow and hence determines an indexed five-support even double cover of $G$.

### Proof

Every dual edge maps to a target edge, so every $\lambda_\varphi(e)$ is a root. A source vertex is dual to a triangle $xyz$. Around that triangle,

$$
\begin{aligned}
&\lambda(xy)+\lambda(yz)+\lambda(zx)\\
&=(\varphi(x)+\varphi(y))
 +(\varphi(y)+\varphi(z))
 +(\varphi(z)+\varphi(x))\\
&=0.
\end{aligned}
$$

The three summands are nonzero roots. B1.1 therefore identifies them with a $K_5$ triangle and proves the local five-support parity law. $\square$

The word $\varphi(C)$ may be chosen separately for every old support-cycle component $C$, even when several components have the same old colour $\kappa_g(C)$.

## 6. Exact meaning of fixed-embedding equivalence

### Definition 6.1

A **componentwise five-support compression of the fixed root lift $g$** is an assignment

$$
p:V(T_g)\longrightarrow E_5
$$

such that for every dual edge $xy$ the difference $p(x)+p(y)$ is a root. The resulting root on the corresponding source edge defines the new five-support cover.

### Theorem 6.2

For fixed $g$, componentwise five-support compressions in the sense of Definition 6.1 are exactly graph homomorphisms

$$
T_g^{(1)}\longrightarrow\mathscr A_5.
$$

### Proof

The defining edge condition is exactly adjacency in the Cayley graph $\mathscr A_5$. $\square$

This is the correct fixed-embedding “if and only if”. It is a definition-level equivalence plus Theorem 5.1's proof that the resulting edge roots satisfy the source vertex equations.

## 7. Holonomy criterion for carrying an external cover on the same embedding

Let

$$
\lambda:E(T_g)\longrightarrow E_5
$$

be any root-valued edge labelling; in particular it may come from a five-support cover of $G$ constructed independently of $g$.

### Theorem 7.1 — dual potential criterion

There exists a map $p:V(T_g)\to E_5$ with

$$
p(x)+p(y)=\lambda(xy)
$$

on every dual edge if and only if

$$
\sum_{e\in C}\lambda(e)=0
$$

for every cycle $C$ of the dual graph $T_g^{(1)}$.

When a solution exists, the solution set is a torsor under one constant translation on each connected component of $T_g^{(1)}$.

### Proof

Necessity follows by telescoping around a cycle. Conversely, choose one root vertex in each connected component and assign it an arbitrary potential. For any other vertex, define its potential by summing $\lambda$ along a path from the root. The cycle-sum hypothesis makes this independent of path. Edge equations follow immediately. Two solutions have zero difference across every edge and are therefore componentwise constant. $\square$

### Corollary 7.2 — local conservation is not enough on a fixed surface

A five-support root flow automatically has zero sum around each triangular face of $T_g$, because those faces correspond to source vertices. This does not by itself force zero sum around noncontractible or other independent cycles of the dual graph. The residual obstruction is dual holonomy.

Therefore an arbitrary five-support cover of $G$ need not be represented by a potential on one prescribed $T_g$. The graph-level theorem must allow the cycle-face embedding to be built from the cover itself.

## 8. Graph-level topological equivalence

### Theorem 8.1 — graph-level surface/halfcube criterion

For a finite loopless cubic multigraph $G$, the following are equivalent.

1. $G$ has an indexed five-support even double cover.
2. $G$ has a cycle-face embedding $S$ whose dual triangular graph $T_S^{(1)}$ admits a homomorphism to $\mathscr A_5$.

### Proof

$(2)\Rightarrow(1)$ is Theorem 5.1.

For $(1)\Rightarrow(2)$, apply B1.1 to regard the five supports as a root lift on a five-element index set. Attach discs along the connected components of the five supports, obtaining its own cycle-face surface by Theorem 2.1.

It remains to map its five face colours into the **even** half-cube. Choose any odd word $t\in\mathbf F_2^5$ and assign to the face colour $i$ the even word

$$
q_i=t+\varepsilon_i.
$$

For $i\ne j$,

$$
q_i+q_j=\varepsilon_i+\varepsilon_j\in R_5,
$$

so the five words form a $K_5$ in $\mathscr A_5$. Colour every face component of support $i$ by $q_i$. Adjacent dual vertices therefore map to adjacent half-cube vertices. $\square$

### Parity correction

One may equivalently use the odd component of the full half-cube and label by singleton words $\varepsilon_i$. If $\mathscr A_5$ is defined specifically as the **even** component, singleton words are not its vertices; an odd translation as above is required. The integrated and recovered prose should be normalized accordingly.

## 9. The global-colour quotient

Let $J_g$ be the graph on the old colours actually used by $\kappa_g$, with an edge $ab$ whenever some dual edge joins an $a$-coloured vertex to a $b$-coloured vertex. Then

$$
T_g^{(1)}\xrightarrow{\kappa_g}J_g
$$

is the colour-adjacency quotient.

### Theorem 9.1 — exact factorization criterion

For a homomorphism $\varphi:T_g^{(1)}\to\mathscr A_5$, the following are equivalent.

1. $\varphi$ is constant on every fibre of the old-colour map $\kappa_g$.
2. There is a graph homomorphism
   $$
   \psi:J_g\to\mathscr A_5
   $$
   such that
   $$
   \varphi=\psi\circ\kappa_g.
   $$

### Proof

$(2)\Rightarrow(1)$ is immediate. If $(1)$ holds, define $\psi(a)$ to be the common $\varphi$-value of the $a$-coloured dual vertices. If $ab$ is an edge of $J_g$, choose a witnessing dual edge $xy$ with colours $a,b$. Since $\varphi$ is a graph homomorphism, $\psi(a)=\varphi(x)$ and $\psi(b)=\varphi(y)$ are adjacent. Hence $\psi$ is a graph homomorphism and gives the required factorization. $\square$

### Corollary 9.2 — strict scope

A map $J_g\to\mathscr A_5$ gives a componentwise compression, but it classifies only the **global-index-factorable** subclass. A general map $T_g^{(1)}\to\mathscr A_5$ may assign different values to disconnected face components with the same old support colour.

The recovered stacked-triangulation certificate shows that this inclusion is genuinely strict. Its exact witness table is governed by the erratum packet; this finite strictness example is not re-derived here.

## 10. Relation to B1.3

B1.3 studies a globally factorable five-point subset inside the point-index torsor of one fixed Fano flow. Its data are constant at the level of global old point indices.

B1.4 allows independent values on individual support-cycle components of one fixed root lift. Therefore:

$$
\text{B1.3 global five-coordinate slice}
\Longrightarrow
J_g\to\mathscr A_5
\Longrightarrow
T_g^{(1)}\to\mathscr A_5,
$$

for the corresponding lift, but neither converse is automatic at the same fixed $(f,g)$.

At graph level, both successful routes imply a five-support cover; that cover may then be re-encoded by some factorable Fano-flow presentation via B1.3, not necessarily the original one.

## 11. Components and cell conventions

- If $G$ is disconnected, the surface and dual are disjoint unions; potentials and translations are componentwise.
- Parallel source edges give distinct dual edges and may give polygonal two-faces.
- Proper colouring is a colouring of face **occurrences/components**, not merely of abstract support values.
- No loop extension is asserted.
- The dual one-skeleton may be a multigraph; graph homomorphism conditions are imposed edgewise.

## 12. Corpus correction recommendation

Before Programme B curation:

1. rewrite the fixed-$g$ boxed criterion in `five-support/surfaces-and-halfcube.md` as Definition 6.1/Theorem 6.2, or explicitly say “componentwise compression of the same embedding”;
2. do not claim that an arbitrary cover integrates on an arbitrary fixed dual without the holonomy criterion;
3. replace singleton labels in the even half-cube by an odd translate of the five singleton words, or state that the odd component is being used;
4. retain $J_g$ only as the global-index-factorable quotient;
5. preserve the strictness example under its corrected witness table.

## 13. Completion assessment

`AC-PD-B1.4` is `COMPLETE-DRAFT / SCOPE-CORRECTION`. The next B1 task is to consolidate B1.1–B1.4 into one exact equivalence-and-implication diagram, update the persistent DAG, and emit a coherent Programme B1 checkpoint for Curator intake while keeping B2–B9 active/open according to dependency order.
