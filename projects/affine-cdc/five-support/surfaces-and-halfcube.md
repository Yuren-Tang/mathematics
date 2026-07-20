# Cycle-face surfaces, dual triangulations, and the half-cube target

## 1. From a compatible root lift to a surface

Let $G$ be a finite loopless cubic multigraph and let

$$
g:E(G)\to\binom I2
$$

be a compatible root lift on an eight-element support-index set $I$. At every cubic vertex the three incident root labels are

$$
\{a,b\},\qquad\{b,c\},\qquad\{c,a\}
$$

for distinct $a,b,c\in I$.

For each index $a$, define

$$
F_a=\{e:a\in g(e)\}.
$$

Every $F_a$ is vertex-even. Each nonempty connected component is therefore a circuit of the loopless cubic graph. Attach one polygonal disc along every such support-cycle component.

### Theorem 1.1 — root-lift/surface equivalence

The resulting cell complex $S_g$ is a closed cycle-face surface with one properly coloured face occurrence for every support-cycle component. Conversely, every properly face-coloured cycle-face embedding recovers a compatible root lift by labelling each source edge with the pair of colours of its two incident face occurrences.

Thus compatible root lifts are equivalent to:

1. properly face-coloured cycle-face embeddings $S_g$ of $G$;
2. closed triangular dual cellulations $T_g$ with a proper colouring of their vertices by the old support indices.

The vertices of $T_g$ are individual face components. Distinct components carrying the same old support index remain distinct vertices.

## 2. The even half-cube

Put

$$
E_5=\left\{x\in\mathbf F_2^5:\sum_i x_i=0\right\},
\qquad
R_5=\{\varepsilon_i+\varepsilon_j:i<j\}.
$$

The even half-cube $\mathscr A_5$ is the Cayley graph

$$
V(\mathscr A_5)=E_5,
\qquad
xy\in E(\mathscr A_5)\iff x+y\in R_5.
$$

A graph homomorphism

$$
\varphi:T_g^{(1)}\to\mathscr A_5
$$

assigns an even word to every individual support-cycle face component. Across a source edge, the two incident face words differ by a root. Reading this difference on the source edge produces a root-valued $E_5$ flow and hence an indexed five-support even double cover.

## 3. Exact fixed-lift criterion

A **componentwise five-support compression of the fixed root lift $g$** is an assignment

$$
p:V(T_g)\to E_5
$$

such that $p(x)+p(y)\in R_5$ on every dual edge $xy$.

### Theorem 3.1 — same-embedding componentwise criterion

For fixed $g$, componentwise compressions of the face components of the same embedding are exactly graph homomorphisms

$$
T_g^{(1)}\to\mathscr A_5.
$$

The resulting root difference on every dual edge satisfies the source cubic flow equations and therefore gives a five-support cover.

This is the corrected meaning of the fixed-$g$ biconditional. It is not a statement that every independently chosen five-support cover of $G$ must be representable on the prescribed surface $S_g$.

## 4. Prescribed-surface holonomy

Let

$$
\lambda:E(T_g)\to E_5
$$

be an externally supplied root-valued labelling, for example the root flow of a five-support cover constructed independently of $g$.

### Theorem 4.1 — dual potential criterion

There exists a potential $p:V(T_g)\to E_5$ satisfying

$$
p(x)+p(y)=\lambda(xy)
$$

on every dual edge if and only if

$$
\sum_{e\in C}\lambda(e)=0
$$

for every cycle $C$ of $T_g^{(1)}$.

When a solution exists, the solution set is a torsor under one constant translation on each connected component of the dual graph.

Local source-vertex conservation verifies zero sum around the triangular dual faces. It does not imply zero sum around every independent dual cycle. Residual dual holonomy is the exact obstruction to carrying an external cover on one prescribed surface.

## 5. Graph-level surface criterion and parity convention

### Theorem 5.1 — graph-level equivalence

For a finite loopless cubic multigraph $G$, the following are equivalent:

1. $G$ has an indexed five-support even double cover;
2. there exists a cycle-face embedding $S$ of $G$ whose dual graph admits a homomorphism
   $$
   T_S^{(1)}\to\mathscr A_5.
   $$

For the forward direction, build the cycle-face surface from the five-support cover itself. The embedding is existentially quantified, so no prescribed-surface holonomy obstruction remains.

### Even-component parity correction

The singleton words $\varepsilon_i$ have odd weight and are not vertices of the even component $\mathscr A_5$. Choose one odd word $t\in\mathbf F_2^5$ and map support colour $i$ to

$$
q_i=t+\varepsilon_i\in E_5.
$$

Then

$$
q_i+q_j=\varepsilon_i+\varepsilon_j\in R_5,
$$

so the five words form a $K_5$ in the even half-cube. Equivalently, one may explicitly use the isomorphic odd component.

## 6. The old-colour quotient and its exact scope

Let $J_g$ be the graph whose vertices are the old support indices used by $g$, with an edge $ab$ whenever a source edge has old root label $\{a,b\}$. The proper old colouring gives a quotient

$$
T_g^{(1)}\to J_g.
$$

### Theorem 6.1 — factorability criterion

A map $\varphi:T_g^{(1)}\to\mathscr A_5$ factors through $J_g$ if and only if it is constant on all face components carrying the same old support index.

Therefore

$$
J_g\to\mathscr A_5
$$

classifies only global-index-factorable compression. A general map from the full dual may assign different values to disconnected face components with the same old colour.

Every theorem stated only for $J_g$ keeps this quotient scope. It must not be promoted to a classification of the full dual.

## 7. Existing factorable-quotient theory

The integrated corpus contains exact finite and theorem-level results about maps from spanning old-colour graphs $J\subseteq K_8$ into $\mathscr A_5$, including unused-root criteria and dense quotient obstructions.

Programme B1 does not re-audit or enlarge those downstream target classifications. It fixes their domain:

$$
\text{old-colour quotient }J_g,
$$

not the full componentwise dual $T_g^{(1)}$.

Accordingly, any $K_6$, pentagon, unused-matching, or finite quotient statement in this corpus remains a statement about factorable compression unless a separate full-dual proof is given.

## 8. Clique links and target capacity

The target $\mathscr A_5$ has clique number five. If a source graph contains a dominating clique $K_r$, the remaining vertices must map into the common neighbourhood of an $r$-clique.

For $2\le r\le5$, the existing target-capacity theorem identifies the relevant chromatic threshold. For $r=1$, the link is $J(5,2)=L(K_5)$ and the problem is not controlled by chromatic number alone.

These are target-side results. They do not replace the full-dual source quantifier or prove that every obstruction contains a bounded dominating-clique core.

## 9. Beyond clique obstruction

The implication

$$
K_6\nsubseteq X\Longrightarrow X\to\mathscr A_5
$$

is false for arbitrary graphs. Common-neighbour chromatic cores give a deeper obstruction layer, and compatible finite laboratories realize both clique and non-clique target failures.

These examples are exact finite mathematics. They do not constitute a universal obstruction list.

## 10. Marked obstruction cores and gauge occurrence

A marked obstruction core records exact source face circuits and their weighted dual incidence, not only an abstract target-side graph.

For a marked family $\mathcal C$, let $Z_{\mathcal C}$ be the union of source edges traversed by its faces and put

$$
R_{\mathcal C}=E(G)\setminus Z_{\mathcal C}.
$$

If $B_f$ is the reduced gauge code and $\beta$ is one state containing the marked core, the same marked circuits persist on the affine occurrence locus

$$
A_{\mathcal C}
=
\beta+\left(B_f\cap\mathbf F_2^{R_{\mathcal C}}\right).
$$

Thus a finite marked certificate library gives an affine-subspace arrangement in the gauge torsor. B1 does not assert that the present library is complete or that its union always leaves an uncovered state.

## 11. Visible clique geometry and renewal

Existing downstream theory distinguishes:

- rigid marked cores;
- mobile renewal, where destroying one certificate creates another;
- arrangement escape, where the union of marked occurrence loci is proper.

Projective Petersen-type cores, exposed dual cycles, renewal laboratories, and mixed obstruction species remain in their previous theorem/evidence classifications. Programme B1 changes only the full-dual versus quotient scope in which they may be invoked.

## 12. Orientability data

The cycle-face surface retains information beyond the half-cube map. For a signed rotation-system presentation, a gauge/Petrial word changes the edge-twist vector affinely, and the orientable locus is an affine intersection with the cut space.

An orientable five-support cover yields a nowhere-zero $\mathbf Z_5$ flow after orienting support components and assigning coefficients. This is a sufficient bridge, not an equivalence and not a proof of a five-flow conjecture.

## 13. Safe fixed-data hierarchy

For corresponding fixed flow and root lift:

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

The converses need not hold at the same fixed $(f,g)$. At graph level, any successful route yields a cover that can be re-encoded by some existential Fano-flow/plane presentation, not necessarily the original one.

## 14. Natural dependency order

```text
compatible root lift g
↔ properly coloured cycle-face surface S_g
↔ properly coloured full dual T_g
→ same-embedding componentwise half-cube question
→ old-colour-factorable quotient as a strict subroute
→ target links and marked obstruction cores
→ affine occurrence arrangements and source localization
```

The prescribed-surface converse additionally passes through the dual holonomy criterion.

## 15. Reliability boundary

The B1 root-lift/surface correspondence, same-embedding componentwise criterion, prescribed-dual holonomy criterion, graph-level existential surface criterion, factorability boundary, and parity correction are integrated authorial proofs from checkpoint `778b09ac...`.

Downstream target classifications, gauge theorems, and finite laboratories retain their previous assurance status and are not independently re-audited by this intake. The global five-support theorem and completeness of the obstruction library remain open. No Lean, independent-review, manuscript, publication, release, arXiv, or DOI status is created.
