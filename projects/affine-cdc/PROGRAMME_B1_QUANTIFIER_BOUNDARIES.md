# Programme B1 quantifier boundaries

This file is the compact control surface for every B1 statement whose truth depends on what has already been fixed.

## 1. Graph-level existence

For a finite loopless cubic multigraph $G$, the following are equivalent:

1. $G$ has five indexed even supports with exact double coverage;
2. $G$ has an $R_5$-valued $E_5$ flow;
3. $G$ has a $K_5$-triangle edge labelling;
4. $G$ has exact matching/four-flow data $(B,D,M,w)$;
5. $G$ has an even support $B$, matching $M\subseteq B$, nowhere-zero $\mathbf F_2^2$ flow on $G-M$, and even $M$-endpoint parity in every component of $G-B$;
6. there exist a Fano flow $f$ and plane $W$ with empty component-obstruction profile;
7. there exists a cycle-face embedding $S$ whose full dual maps to the even half-cube.

All auxiliary data in items 4–7 are existential. No previously chosen flow, plane, lift, or embedding is retained by the equivalence.

## 2. Fixed support coordinate and fixed root label

For one five-support witness:

- fixing a support coordinate gives an even edge support;
- fixing one root label gives a matching.

These are different inverse images. Neither statement may replace the other.

## 3. Fixed matching/four-flow data

A matching $M$ and nowhere-zero $\mathbf F_2^2$ flow on $G-M$ are not sufficient by themselves.

The converse requires either:

- an additional even support $D$ with $M=B\cap D$, where $B$ is the outside-plane even support; or
- even endpoint parity for $M$ in every component of $G-B$.

This missing datum is exactly the finite $T$-join condition.

## 4. Fixed pair $(f,W)$

Fix a nowhere-zero Fano flow $f$ and plane $W$.

The following are equivalent only for this fixed pair:

- a global five-coordinate slice above $(f,W)$;
- a distinguished even support $D$;
- the component $T$-join condition;
- vanishing of one outside-colour cut parity;
- vanishing of all four outside-colour cut parities;
- Eulerian outside-colour classes after contraction;
- vanishing of the local affine component obstruction.

The statement is not universally quantified over all $f$ or all $W$.

## 5. Fixed flow $f$

For a prescribed $f$, a globally point-index-factorable lift exists if and only if

$$
\exists W\leq\mathbf F_2^3,\qquad \mathfrak O_f(W)=\varnothing.
$$

A fixed flow may fail for every plane. This proves failure of that flow fibre only, not failure of the graph.

## 6. Fixed root lift $g$

Fix a compatible root lift $g$ and its cycle-face surface $S_g$.

The biconditional

$$
T_g^{(1)}\to\mathscr A_5
$$

means exactly that the individual face components of the **same embedding** can be relabelled by five-coordinate even words with root differences across dual edges.

It does not mean that every five-support cover of $G$ is representable on $S_g$.

## 7. Fixed dual plus external cover

Fix the dual graph $T_g$ and an independently chosen root flow $\lambda$.

A potential on this prescribed dual exists if and only if

$$
\sum_{e\in C}\lambda(e)=0
$$

for every dual cycle $C$.

Source-vertex conservation checks only the triangular dual face boundaries. It does not remove residual dual holonomy.

## 8. Old-colour quotient $J_g$

A map

$$
J_g\to\mathscr A_5
$$

is equivalent to a full-dual map that is constant on all face components carrying the same old support index.

Thus $J_g$ classifies only global-index-factorable compression. Any theorem about $J_g$, including finite target classifications, keeps that scope.

## 9. Half-cube parity

When $\mathscr A_5$ denotes the even half-cube, singleton words $\varepsilon_i$ are not vertices. The five colours are embedded by choosing one odd word $t$ and using

$$
t+\varepsilon_i.
$$

Alternatively, the odd component must be named explicitly.

## 10. Fixed-data implication chain

For matching fixed data, only the following implications are automatic:

$$
\text{global five-point slice}
\Longrightarrow
J_g\to\mathscr A_5
\Longrightarrow
T_g^{(1)}\to\mathscr A_5
\Longrightarrow
\text{five-support cover}.
$$

No converse is asserted at the same fixed $(f,g)$.

## 11. Assurance

These are integrated authorial B1 theorem boundaries. They are not independent-audit, Lean, manuscript, publication, release, arXiv, or DOI determinations.
