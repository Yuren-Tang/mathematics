# Programme B1 — five-support object, quantifiers, and fixed-data scope

## 1. Scope

Throughout this chapter, $G$ is a finite loopless cubic multigraph. Parallel edge objects and disconnected components are allowed. The loopless hypothesis is load-bearing for the once-per-edge incidence language used by the five-support programme.

Programme B1 closes the object and quantifier layer. It does **not** prove the global five-support theorem for every graph. It proves exact equivalences among several ways of expressing the existence of a five-support witness and separates them from statements in which a Fano flow, plane, root lift, or surface has already been fixed.

The exact authorial source is

`proof-development/affine-cdc-rigour-v1@778b09ac8260192e022f512f24cdef1d04871f37`.

## 2. The graph-level five-support object

Put

$$
E_5=\left\{x\in\mathbf F_2^5:\sum_{i=1}^5x_i=0\right\},
\qquad
R_5=\{\varepsilon_i+\varepsilon_j:i<j\}.
$$

An **indexed five-support even double cover** is a five-tuple

$$
(F_1,\ldots,F_5)
$$

of vertex-even edge supports such that every source edge belongs to exactly two indexed supports. Empty supports and equal support values at different indices are allowed; occurrence indices remain part of the witness. Circuit decomposition is not included in this definition.

For every edge $e$, record the two support coordinates containing it:

$$
\lambda(e)=\sum_{i:e\in F_i}\varepsilon_i\in R_5.
$$

Coordinatewise vertex evenness is exactly the flow equation. Conversely, the coordinate inverse images of a root-valued flow recover the five supports.

### Theorem 2.1 — canonical object equivalence

The following data are canonically equivalent:

1. an indexed five-support even double cover of $G$;
2. a root-valued flow
   $$
   \lambda:E(G)\to R_5\subset E_5;
   $$
3. an edge labelling by $E(K_5)$ such that the three labels at every source vertex form the three edges of one triangle of $K_5$.

The constructions are mutually inverse and equivariant under permutation of the five support indices.

## 3. Exact matching/four-flow theorem

Two distinct inverse-image statements must not be confused.

- The inverse image of a fixed **support coordinate** is an even support: at a local target triangle that coordinate occurs zero or two times.
- The inverse image of a fixed **root label** is a matching: a target triangle contains a given target edge at most once.

A matching and a four-flow alone do not retain enough lift data for the converse.

Let $W\cong\mathbf F_2^2$. An exact matching/four-flow datum consists of:

1. even supports $B,D\subseteq E(G)$;
2. a matching
   $$
   M=B\cap D;
   $$
3. a nowhere-zero $W$-flow on $G-M$.

### Theorem 3.1 — exact matching/four-flow equivalence

$G$ has an indexed five-support even double cover if and only if it has exact matching/four-flow data $(B,D,M,w)$.

The second even support $D$ may be eliminated only by retaining an explicit component parity condition. Equivalently, $G$ has a five-support cover if and only if there exist:

1. an even support $B$;
2. a matching $M\subseteq B$;
3. a nowhere-zero $\mathbf F_2^2$-flow on $G-M$;
4. even $M$-endpoint parity in every connected component of $G-B$.

The fourth item is the exact $T$-join or terminal datum. The phrase “matching plus four-flow with appropriate terminal behaviour” is not a complete theorem statement unless this condition is displayed.

## 4. Fixed Fano flow and fixed plane

Fix a nowhere-zero Fano flow

$$
f:E(G)\to\Gamma\setminus\{0\},
\qquad
\Gamma=\mathbf F_2^3,
$$

and fix a plane $W\leq\Gamma$. Choose $a\notin W$ and write uniquely

$$
f=w+ba,
\qquad
B_W=\operatorname{supp}b=\{e:f(e)\notin W\}.
$$

Let

$$
G_W=G-B_W
$$

and, for each outside colour $c\in\Gamma\setminus W$, let

$$
M_c=\{e:f(e)=c\}.
$$

Every $M_c$ is a matching. For each component $K$ of $G_W$, define

$$
n_c(K)=|M_c\cap\delta_G(K)|\pmod 2.
$$

The four bits $n_c(K)$ are equal. Denote their common value by $\chi_W(K)$.

### Theorem 4.1 — fixed-$(f,W)$ criterion

For the fixed pair $(f,W)$, the following are equivalent:

1. there is a global five-coordinate affine slice above $(f,W)$;
2. there is an even support $D$ satisfying
   $$
   B_W\cap D=M_a;
   $$
3. every component of $G_W$ contains an even number of endpoints of $M_a$;
4. $n_a(K)=0$ for every component $K$;
5. $n_c(K)=0$ for every component $K$ and every $c\notin W$;
6. after contracting the components of $G_W$, every outside-colour class is Eulerian;
7. the local affine component obstruction $\Omega_W(K)$ vanishes for every component.

These are resolutions of one fixed-data obstruction, not seven different graph-level theorems.

For fixed $f$, define

$$
\mathfrak O_f(W)=\{K\in\pi_0(G_W):\chi_W(K)=1\}.
$$

Then $f$ admits a globally point-index-factorable five-coordinate lift exactly when

$$
\exists W\leq\Gamma,\quad \dim W=2,\quad \mathfrak O_f(W)=\varnothing.
$$

This may fail for a prescribed $f$. Such failure is not a counterexample for $G$, because another Fano flow may succeed.

### Theorem 4.2 — graph-level existential Fano form

$G$ has an indexed five-support even double cover if and only if there exist a nowhere-zero Fano flow $f$ and a plane $W$ with

$$
\mathfrak O_f(W)=\varnothing.
$$

The existential quantifier on $f$ is essential.

## 5. Compatible root lifts and cycle-face surfaces

Fix a compatible root lift

$$
g:E(G)\to\binom I2
$$

on an eight-element index set $I$. For each old support index $i$, its support is vertex-even, so each nonempty connected component is a circuit. Attach one face disc to every such support-cycle component.

### Theorem 5.1 — root-lift/surface equivalence

Compatible root lifts are equivalent to properly face-coloured cycle-face embeddings $S_g$ of $G$, and dually to closed triangular cellulations $T_g$ with a proper colouring of their vertices by the old support indices.

The vertices of the full dual $T_g$ are individual face components. Distinct components carrying the same old index remain distinct vertices.

## 6. Fixed-lift same-embedding compression

Let $\mathscr A_5$ be the even half-cube:

$$
V(\mathscr A_5)=E_5,
\qquad
xy\in E(\mathscr A_5)\iff x+y\in R_5.
$$

A **componentwise five-support compression of the fixed lift $g$** assigns an even word to every individual support-cycle face component so that adjacent dual vertices differ by a root.

### Theorem 6.1 — exact fixed-lift biconditional

For fixed $g$, componentwise compressions of the same embedding are exactly graph homomorphisms

$$
T_g^{(1)}\to\mathscr A_5.
$$

Taking the half-cube difference across every dual edge produces a root-valued $E_5$-flow on $G$, hence a five-support cover.

This theorem does **not** say that every independently chosen five-support cover of $G$ is represented on the prescribed surface $S_g$.

## 7. Dual holonomy on a prescribed surface

Let

$$
\lambda:E(T_g)\to E_5
$$

be an externally supplied root labelling, for example the root flow of a five-support cover constructed without reference to $g$.

### Theorem 7.1 — integration criterion

There is a potential $p:V(T_g)\to E_5$ satisfying

$$
p(x)+p(y)=\lambda(xy)
$$

on every dual edge if and only if

$$
\sum_{e\in C}\lambda(e)=0
$$

for every cycle $C$ of the dual graph.

Local conservation verifies the triangular dual face boundaries only. It does not imply vanishing on all dual cycles. Residual dual holonomy is the exact obstruction to carrying an external cover on one prescribed embedding.

## 8. Full dual versus old-colour quotient

Let $J_g$ be the graph of old support colours used by $g$, with an edge for every used old root. The old colouring gives a quotient

$$
T_g^{(1)}\to J_g.
$$

### Theorem 8.1 — factorability boundary

A map $T_g^{(1)}\to\mathscr A_5$ factors through $J_g$ if and only if it is constant on all face components carrying the same old support index.

Therefore

$$
J_g\to\mathscr A_5
$$

classifies only the old-colour-factorable subclass of same-embedding componentwise compression. It is not the complete fixed-lift criterion.

Any finite theorem or certificate proved only for $J_g$ retains exactly that quotient scope.

## 9. Even-halfcube parity convention

The singleton words $\varepsilon_i$ have odd weight, so they lie in the odd component of the full half-cube. They are not vertices of $\mathscr A_5$ when $\mathscr A_5$ denotes the even component.

To realize the five support colours inside the even component, choose any odd word $t\in\mathbf F_2^5$ and use

$$
q_i=t+\varepsilon_i\in E_5.
$$

Then

$$
q_i+q_j=\varepsilon_i+\varepsilon_j\in R_5,
$$

so the five $q_i$ form a $K_5$ in $\mathscr A_5$. Equivalently, one may state explicitly that the isomorphic odd component is being used.

## 10. Graph-level surface equivalence

### Theorem 10.1

The following are equivalent:

1. $G$ has an indexed five-support even double cover;
2. there exists a cycle-face embedding $S$ of $G$ whose dual graph admits a homomorphism
   $$
   T_S^{(1)}\to\mathscr A_5.
   $$

For the forward direction, build the cycle-face surface from the five-support cover itself and embed its five face colours by the odd-translation construction above. Thus the embedding is existentially quantified; no prescribed-surface holonomy problem arises.

## 11. Safe implication hierarchy at fixed data

For corresponding fixed flow and fixed lift, the safe hierarchy is

$$
\boxed{
\text{global five-point slice}
\Longrightarrow
J_g\to\mathscr A_5
\Longrightarrow
T_g^{(1)}\to\mathscr A_5
\Longrightarrow
\text{five-support cover}.}
$$

The converses need not hold for the same fixed $(f,g)$. At graph level, any successful right-hand route yields a five-support cover, which can then be re-encoded by **some** existential Fano-flow/plane presentation; it need not recover the original fixed data.

## 12. Boundary with Programme B2 and later work

Programme B1 does not close cographic, quadratic, Schur, singular, orthogonal, or Fourier/stress arrows except where they are explicitly used in the fixed-plane component criterion above. Their full witness equivalence, quotient loss, or obstruction status belongs to Programme B2.

The global five-support theorem remains open. Finite cube, strictness, and target certificates remain exact finite evidence in their stated scope; they are not universal proofs.

## 13. Assurance

This chapter integrates complete authorial B1 proofs. It is not an independent audit and is not Lean-formalized end to end. It creates no manuscript, peer-review, publication, release, arXiv, DOI, or priority-attestation status.
