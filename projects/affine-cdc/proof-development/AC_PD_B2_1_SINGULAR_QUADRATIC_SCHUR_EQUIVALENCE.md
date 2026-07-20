# AC-PD-B2.1 — anisotropic, singular-quotient, quadratic, and Schur equivalence

**Proof-development state:** `COMPLETE-DRAFT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Recovered controlling packets:** `FIVE_CDC_ANISOTROPIC_RANK_FOUR_FLOW_V1.md`, `FIVE_CDC_SINGULAR_QUOTIENT_LIFT_V1.md`, `FIVE_CDC_QUADRATIC_CYCLE_EQUATION_V1.md`, and `FIVE_CDC_SCHUR_QUOTIENT_CRITERION_V1.md` at `research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`  
**Depends on:** B1.1–B1.3  
**Immediate consumers:** B2.2 cographic formulation; B2.3 orthogonal rank reduction; B2.4 stress/Fourier duality; B4 flow switches  
**External mathematical inputs:** none

## 0. Classification of the four formulations

The four formulations have different resolutions.

1. An anisotropic $H_5$-flow is a complete graph-level five-support witness.
2. A singular quotient fixes a rank-three Fano flow and asks whether it has an anisotropic lift; the full lift torsor must be retained.
3. The quadratic cycle equation is a coordinate-isomorphic complete graph-level witness.
4. The Schur quotient is a fixed-coordinate solvability criterion obtained after eliminating the lift coordinate; by itself it is an obstruction equation, but together with the fixed flow data it is equivalent to the lift.

No witness is lost when these data and quantifiers are stated exactly.

## 1. The canonical minus-type four-space

Define

$$
H_5=
\left\{s=(s_1,\dots,s_5)\in\mathbf F_2^5:
\sum_{i=1}^5s_i=0
\right\}
$$

and

$$
q_5(s)=\sum_{1\leq i<j\leq5}s_is_j.
$$

For $s\in H_5$, the weight is $0$, $2$, or $4$, and

$$
q_5(s)=\binom{\operatorname{wt}(s)}2\pmod2.
$$

Hence

$$
q_5(s)=1
\quad\Longleftrightarrow\quad
\operatorname{wt}(s)=2.
$$

The polar form is the restriction of the standard dot product:

$$
B_5(s,t)=\sum_{i=1}^5s_it_i.
$$

It is nondegenerate on $H_5$, because the orthogonal complement of $H_5$ in $\mathbf F_2^5$ is spanned by the all-one word, which has odd weight and is not in $H_5$. Thus $(H_5,q_5)$ is a nondegenerate four-dimensional minus-type quadratic space. Its ten anisotropic vectors are exactly the ten weight-two roots $R_5$; its five nonzero singular vectors are the weight-four words.

## 2. Graph-level anisotropic-flow equivalence

Let $G$ be a finite loopless multigraph; cubicity is needed only for the local triangle and matching consequences.

### Theorem 2.1

The following are canonically equivalent.

1. $G$ has an indexed five-support even double cover $(F_i)_{i\in[5]}$.
2. $G$ has an $H_5$-valued flow
   $$
   g:E(G)\to H_5
   $$
   satisfying
   $$
   q_5(g(e))=1
   $$
   for every edge.

### Proof

Given the supports, set

$$
g(e)=
(\mathbf1_{e\in F_1},\dots,\mathbf1_{e\in F_5}).
$$

Coordinatewise evenness gives the flow equations, and exact double coverage gives weight two, hence anisotropy.

Conversely, an anisotropic value in $H_5$ has weight two. Taking the five coordinate supports gives even supports and exact double coverage. The two constructions are inverse. $\square$

For cubic $G$, this is the B1.1 $K_5$-triangle law written as the anisotropic orbit of $O^-(4,2)$.

## 3. Linear coordinates and the complete quadratic equation

Define

$$
\Phi:\mathbf F_2^4\longrightarrow H_5
$$

by

$$
\Phi(b,d,x,y)
=
(b,d,b+d+y,b+d+x,b+d+x+y).
$$

This is a linear isomorphism. Direct expansion gives

$$
q_5(\Phi(b,d,x,y))
=bd+x+y+xy.
$$

For edge words, let $*$ denote coordinatewise multiplication and let $\mathbf1$ denote the all-edge word.

### Theorem 3.1 — quadratic cycle variety

For a finite loopless multigraph $G$, the following are equivalent.

1. $G$ has an indexed five-support even double cover.
2. There exist cycle words
   $$
   b,d,x,y\in\mathcal C(G)
   $$
   satisfying
   $$
   \boxed{
   b*d=(\mathbf1+x)*(\mathbf1+y).}
   $$

No separate nowhere-zero condition is required.

### Proof

An $H_5$-flow is exactly a quadruple of binary cycle words under the linear isomorphism $\Phi$. Its edge value is anisotropic exactly when

$$
b_ed_e+x_e+y_e+x_ey_e=1,
$$

which rearranges to the displayed equation. By Theorem 2.1, edgewise anisotropy is exactly five-support existence. $\square$

The five support words reconstructed from a solution are

$$
\begin{aligned}
F_1&=b,\\
F_2&=d,\\
F_3&=b+d+y,\\
F_4&=b+d+x,\\
F_5&=b+d+x+y.
\end{aligned}
$$

Every one is a cycle word. The quadratic equation says precisely that at each edge the resulting five-bit word has weight two rather than zero or four.

### Corollary 3.2 — odd-subgraph form

Putting

$$
r=\mathbf1+x,
\qquad
s=\mathbf1+y,
$$

gives

$$
b*d=r*s.
$$

On a cubic graph, $r$ and $s$ have odd local degree everywhere, while $b,d$ are even. Thus five-support existence is equivalently equality between the intersection of two even subgraphs and the intersection of two everywhere-odd subgraphs.

## 4. Singular-line quotient

Let $(H,q)$ be any four-dimensional minus-type quadratic space over $\mathbf F_2$, choose a nonzero singular vector $k$, and define

$$
\Gamma=H/\langle k\rangle,
\qquad
W_k=k^\perp/\langle k\rangle.
$$

Then $\dim\Gamma=3$, $\dim W_k=2$, and the induced quadratic plane on $W_k$ is anisotropic.

### Lemma 4.1 — anisotropic fibres

For every nonzero class $\bar v\in\Gamma$:

1. if $\bar v\in W_k\setminus\{0\}$, both lifts $v,v+k$ are anisotropic;
2. if $\bar v\notin W_k$, exactly one lift is anisotropic.

### Proof

One has

$$
q(v+k)=q(v)+B(v,k)
$$

because $q(k)=0$.

If $\bar v\in W_k\setminus\{0\}$, choose $v\in k^\perp$. Its nonzero image in the anisotropic quotient plane has quadratic value one, and $B(v,k)=0$, so both lifts are anisotropic.

If $\bar v\notin W_k$, then $B(v,k)=1$, so the two quadratic values differ by one. Exactly one is anisotropic. $\square$

Thus the anisotropic orbit projects to the seven nonzero Fano vectors with fibre multiplicities

$$
2,2,2,1,1,1,1,
$$

where the doubled classes are $W_k\setminus\{0\}$.

## 5. Fixed-flow anisotropic lifting

Let $G$ be finite, loopless, and cubic, and fix a nowhere-zero flow

$$
f:E(G)\to\Gamma\setminus\{0\}.
$$

Choose one anisotropic lift $\widetilde f_0(e)$ of every edge value. Outside $W_k$ this choice is forced; on plane edges it has two choices differing by $k$.

At each vertex $v$, the lifted sum lies in the kernel line:

$$
\sum_{e\ni v}\widetilde f_0(e)=\eta_vk,
\qquad
\eta_v\in\mathbf F_2.
$$

Let

$$
G_{W_k}=(V(G),\{e:f(e)\in W_k\}).
$$

Changing the lift on a plane edge adds $k$ at both endpoints. Hence a correction word $z$ supported on $G_{W_k}$ solves the lift problem exactly when

$$
\partial_{G_{W_k}}z=\eta.
$$

### Theorem 5.1 — singular-quotient lift criterion

The fixed flow $f$ admits an anisotropic $H$-flow lift if and only if

$$
\sum_{v\in V(K)}\eta_v=0
$$

for every connected component $K$ of $G_{W_k}$.

When nonempty, the anisotropic lift space is a torsor under

$$
\mathcal C(G_{W_k}).
$$

### Proof

For a connected finite graph, the image of the binary incidence map is the even-sum vertex subspace and its kernel is the cycle space. Apply this independently to every component. $\square$

This is a complete fixed-data equivalence: the quotient flow plus one solution determines the whole lift torsor. The quotient flow alone is not a five-support witness.

## 6. Coordinate realization of the singular quotient

In the model $H=H_5$, use $\Phi$ and put

$$
k=\Phi(0,1,0,0)=(0,1,1,1,1).
$$

This is a nonzero singular weight-four vector. The quotient map is

$$
\pi\Phi(b,d,x,y)=(b,x,y).
$$

Its canonical plane $W_k$ is the $b=0$ plane.

For a nonzero quotient value $(b,x,y)$:

- if $b=0$, then $(x,y)\ne(0,0)$ and both values of $d$ satisfy anisotropy;
- if $b=1$, anisotropy uniquely forces
  $$
  d=(1+x)(1+y).
  $$

Thus for a fixed nowhere-zero Fano flow $(b,x,y)$, solving the anisotropic lift problem is exactly solving for one cycle word $d$ in

$$
\boxed{
 b*d=(\mathbf1+x)*(\mathbf1+y).}
$$

On $b=1$ edges, $d$ is prescribed. On $b=0$ edges, $d$ is free edgewise and must be chosen globally to be a cycle word.

### Corollary 6.1 — fixed-coordinate solution torsor

If one solution $d_0$ exists, all solutions are

$$
d_0+\mathcal C(G_{b=0}),
$$

where $G_{b=0}$ is the spanning subgraph of edges with $b=0$.

### Proof

Two solutions agree on all $b=1$ edges. Their difference is a cycle word supported on $b=0$ edges. Conversely adding such a cycle word preserves the equation and the cycle condition. $\square$

## 7. The Schur quotient

Contract every connected component of $G_{b=0}$ and retain the $b=1$ edge objects, allowing loops and parallel edges. Denote the quotient multigraph by $Q_b$.

The restrictions of $x$ and $y$ to the retained edges are binary flows on $Q_b$: summing the original coordinate equations over a contracted component cancels all internal edges. The all-one word on the retained edges is also a flow, because it is the descended support $b$.

Let

$$
(x*y)_e=x_ey_e
$$

on the retained quotient edges.

### Theorem 7.1 — Schur-quotient criterion

For the fixed nowhere-zero Fano flow $(b,x,y)$, the following are equivalent.

1. There exists a cycle word $d$ satisfying the quadratic lift equation.
2. The singular-line anisotropic lift obstruction vanishes.
3. The fixed-plane five-coordinate obstruction vanishes on every component of $G_{b=0}$.
4. The Schur word is a quotient flow:
   $$
   \boxed{x*y\in\mathcal C(Q_b).}
   $$

### Proof

The equivalence of the first three statements follows from Sections 5–6 and B1.3. It remains to identify the boundary.

For a component $K$ of $G_{b=0}$, every cut edge has $b_e=1$. The outside colour $(x,y)=(0,0)$ has indicator

$$
(1+x_e)(1+y_e).
$$

The common outside-colour obstruction is therefore

$$
\Omega(K)
=
\sum_{e\in\delta_G(K)}(1+x_e)(1+y_e).
$$

On this cut, the sums of $1$, $x$, and $y$ are all zero: the first is the cut sum of the binary flow $b$, and the others are cut sums of coordinate flows. Expanding leaves

$$
\Omega(K)
=
\sum_{e\in\delta_G(K)}x_ey_e.
$$

This is exactly the boundary of $x*y$ at the quotient vertex representing $K$. Hence all component obstructions vanish exactly when $x*y$ is a quotient flow. $\square$

### Corollary 7.2 — basis independence

The condition $x*y\in\mathcal C(Q_b)$ depends only on the plane $W_k$, not on the chosen basis of its dual coordinates.

### Proof

The group $\mathrm{GL}(2,2)$ is generated by swapping $x,y$ and replacing $y$ by $x+y$. Swapping leaves the product unchanged. Under the second move,

$$
x*(x+y)=x+x*y.
$$

Since $x$ is already a quotient flow, one product is a flow if and only if the other is. $\square$

## 8. One obstruction in four resolutions

For fixed $(f,k)$ or fixed coordinates $(b,x,y)$, the following quantities are the same componentwise bit:

1. the sum of vertex lift defects $\sum_{v\in K}\eta_v$;
2. the B1.3 forbidden-three-colour obstruction $\Omega_{W_k}(K)$;
3. the parity of one, hence every, outside colour on $\delta_G(K)$;
4. the quotient boundary $\partial_{Q_b}(x*y)$.

In the coordinate model, the four forced anisotropic lifts of the outside quotient colours sum to the kernel vector $k$: only the outside state $(x,y)=(0,0)$ has forced $d=1$. Therefore the common outside parity is exactly the coefficient of $k$ in the boundary lift sum.

These are not four independent barriers.

## 9. Complete graph-level equivalence diagram

Combining B1 and this unit gives

$$
\boxed{
\begin{array}{c}
\text{five indexed even supports}\\
\Updownarrow\\
R_5\text{-valued root flow}\\
\Updownarrow\\
\text{anisotropic }O^-(4,2)\text{-flow}\\
\Updownarrow\\
\exists(b,d,x,y)\in\mathcal C(G)^4:\
 b*d=(\mathbf1+x)*(\mathbf1+y)\\
\Updownarrow\\
\exists\text{ fixed Fano slice with soluble singular lift}\\
\Updownarrow\\
\exists(b,x,y):\ x*y\in\mathcal C(Q_b).
\end{array}}
$$

In the last line, $(b,x,y)$ must be a nowhere-zero rank-three flow and $Q_b$ is part of the datum. Omitting either condition creates a false weakening.

## 10. Boundary and evidence status

- The graph-level anisotropic and quadratic formulations are full witness equivalences.
- The singular quotient and Schur formulations are full **fixed-data solvability equivalences** when the quotient flow, plane/kernel, quotient graph, and lift torsor are retained.
- The boundary word $\partial(x*y)$ alone is only an obstruction projection; it does not reconstruct $d$ without solving the incidence equation.
- No literature novelty claim is made. A dedicated source audit remains a publication task, not a logical proof dependency.
- No formalization claim is made.

## 11. Corpus normalization

The integrated formulation chapter should present one mother object and three projections:

1. mother object: anisotropic minus-type four-flow;
2. singular quotient: fixed Fano flow plus kernel-line lift torsor;
3. coordinate chart: quadratic cycle equation;
4. eliminated coordinate: Schur quotient boundary.

It should not list these as unrelated proof metaphors, nor call the quotient obstruction a complete witness without its fixed data and solution torsor.

## 12. Completion assessment

`AC-PD-B2.1` is `COMPLETE-DRAFT`. The next active unit is B2.2: audit and prove the exact cographic/cycle-continuous map formulation, including which source circuits or cocircuits are preserved, whether the map is an edge map or a matroid morphism, and its equivalence to the $K_5$ triangle/root-flow witness.