# AC-PD-B1 — root-flow, fixed-plane, and fixed-lift equivalence map

**Proof-development state:** `READY-FOR-CURATOR`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Constituent units:** B1.1–B1.4  
**External mathematical inputs:** none  
**Assurance:** complete authorial proof-development checkpoint; not independent audit and not a formal proof

## 0. Purpose

This checkpoint normalizes the root object, the exact matching/four-flow bridge, the fixed-flow/fixed-plane obstruction, and the fixed-lift surface target into one diagram with explicit quantifiers. It corrects several synthesis compressions that had merged mathematically distinct levels.

The ambient graph throughout is a finite loopless cubic multigraph; parallel edge objects and disconnected components are allowed.

## 1. Graph-level equivalences

The following graph-level existence statements are equivalent.

### Object form

1. $G$ has an indexed five-support even double cover.
2. $G$ has a root-valued flow
   $$
   \lambda:E(G)\to R_5\subset E_5.
   $$
3. $G$ has a $K_5$-edge labelling such that the three labels at every source vertex form one target triangle.

These equivalences are canonical and mutually inverse by B1.1.

### Exact matching/four-flow form

4. There exist even supports $B,D$, a matching
   $$
   M=B\cap D,
   $$
   and a nowhere-zero $\mathbf F_2^2$-flow on $G-M$.
5. Equivalently, there exist an even support $B$, a matching $M\subseteq B$, a nowhere-zero $\mathbf F_2^2$-flow on $G-M$, and even $M$-endpoint parity in every component of $G-B$.

B1.2 proves $(1)\Longleftrightarrow(4)\Longleftrightarrow(5)$.

### Existential Fano-flow/plane form

6. There exist a nowhere-zero flow
   $$
   f:E(G)\to\mathbf F_2^3\setminus\{0\}
   $$
   and a plane $W\leq\mathbf F_2^3$ such that every component $K$ of
   $$
   G_W=(V(G),\{e:f(e)\in W\})
   $$
   has even cut parity for one, hence every, outside colour:
   $$
   |\{e\in\delta_G(K):f(e)=c\}|
   \equiv0\pmod2
   \qquad(c\notin W).
   $$

B1.3 proves $(1)\Longleftrightarrow(6)$.

### Topological/halfcube form

7. There exists a cycle-face embedding $S$ of $G$ whose dual triangular graph admits a homomorphism
   $$
   T_S^{(1)}\to\mathscr A_5,
   $$
   where $\mathscr A_5$ is the even half-cube on five coordinates.

B1.4 proves $(1)\Longleftrightarrow(7)$.

Consequently the complete graph-level root package is

$$
\boxed{
\begin{array}{c}
\text{five indexed even supports}\\
\Updownarrow\\
R_5\text{-valued }E_5\text{ flow}\\
\Updownarrow\\
K_5\text{-triangle labelling}\\
\Updownarrow\\
(B,D,M,\mathbf F_2^2\text{-flow})\\
\Updownarrow\\
\exists(f,W)\text{ with empty plane profile}\\
\Updownarrow\\
\exists S:\ T_S^{(1)}\to\mathscr A_5.
\end{array}}
$$

No arrow in this box fixes a previously chosen $f$, $W$, root lift, or surface unless explicitly stated.

## 2. Fixed-flow equivalences

Now fix a nowhere-zero Fano flow $f$ and a plane $W$.

Write

$$
f=w+ba,
\qquad
B_W=\operatorname{supp}b,
\qquad
M_a=\{e:f(e)=a\},
$$

for any $a\notin W$. For each component $K$ of $G_W=G-B_W$, the four outside-colour cut parities are equal; call the common value $\chi_W(K)$.

The following are equivalent:

1. the fixed pair $(f,W)$ admits a global five-coordinate affine slice;
2. there is an even support $D$ with
   $$
   B_W\cap D=M_a;
   $$
3. every component of $G_W$ contains an even number of $M_a$ endpoints;
4. $\chi_W(K)=0$ for every component $K$;
5. the local affine obstruction $\Omega_W(K)$ vanishes for every component;
6. after contracting the $G_W$ components, each outside-colour class is Eulerian.

For fixed $f$, a globally point-index-factorable five-support lift exists exactly when one of the seven plane profiles is empty:

$$
\exists W,\qquad
\mathfrak O_f(W)=\varnothing.
$$

This criterion may fail for a prescribed flow. Such failure is not a graph-level counterexample, because another flow may succeed.

## 3. Fixed-lift and same-embedding statements

Now fix a compatible eight-index root lift $g$. It determines:

- a properly face-coloured cycle-face surface $S_g$;
- its full dual triangular cellulation $T_g$;
- the old-colour quotient $J_g$.

### Full componentwise route

A componentwise relabelling of the face components of $g$ by five-coordinate even words is exactly a graph homomorphism

$$
T_g^{(1)}\to\mathscr A_5.
$$

It produces a five-support cover by taking the half-cube difference across every dual edge.

### Factorable route

Such a map factors through

$$
T_g^{(1)}\to J_g
$$

if and only if it is constant on all face components carrying the same old support index. Thus

$$
J_g\to\mathscr A_5
$$

classifies only global-index-factorable compression. This is a strict subclass of all same-embedding componentwise compression.

### Carrying an externally chosen cover on the same surface

Let $\lambda$ be the root flow of an independently chosen five-support cover. It is represented by a potential on the fixed $T_g$ exactly when

$$
\sum_{e\in C}\lambda(e)=0
$$

for every cycle $C$ of the dual graph. Local source-vertex conservation verifies only the triangular face boundaries; residual dual holonomy may remain.

Hence no theorem says that an arbitrary cover integrates on an arbitrary fixed lift or fixed surface.

## 4. Exact implication hierarchy at fixed data

For a corresponding fixed flow and lift, the safe hierarchy is

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

The converses need not hold at the same fixed $(f,g)$.

At graph level, however, every successful right-hand route yields a five-support cover, which can be re-encoded by **some** existential factorable Fano-flow presentation. That presentation need not recover the original fixed flow or root lift.

## 5. Corrections required in the integrated corpus

### Correction 1 — matching object

The inverse image of a fixed support coordinate is an even support, not a matching. The inverse image of a fixed root label is a matching. The exact four-flow converse additionally requires the $(B,D)$ or component-parity datum.

### Correction 2 — undefined terminal behaviour

“Matching plus four-flow with appropriate terminal behaviour” must be replaced by B1.2's explicit even-support/$T$-join condition.

### Correction 3 — fixed-$g$ biconditional

For fixed $g$, the biconditional with $T_g^{(1)}\to\mathscr A_5$ is correct only for “componentwise compression of the same embedding”, not for arbitrary five-support existence on $G$.

### Correction 4 — half-cube parity component

If $\mathscr A_5$ is defined as the even component, singleton words $\varepsilon_i$ are not vertices. Five support colours may be embedded by choosing one odd word $t$ and using

$$
t+\varepsilon_i\in E_5.
$$

Alternatively one may explicitly use the isomorphic odd component.

### Correction 5 — full dual versus colour quotient

$J_g$ forgets individual support-cycle components. Its exact finite classification cannot be promoted to the full dual $T_g$.

## 6. Source and evidence boundary

The equivalence proofs in B1.1–B1.4 are elementary and self-contained. Recovered source packets provide provenance and finite negative/strictness certificates.

The following remain evidence or separately scoped theorem families, not premises of this checkpoint:

- the fixed-flow cube certificate;
- the stacked-triangulation strictness certificate;
- the $K_6/K_8-C_5$ factorable quotient classification;
- dominating-clique capacity and deeper target obstructions;
- finite obstruction libraries and gauge-arrangement coverage.

## 7. Dependency transition

B1 closes the exact object and quantifier layer. It does not yet close the claimed equivalence with:

- cographic/cycle-continuous maps;
- quadratic-cycle and Schur equations;
- singular quotient formulations;
- orthogonal rank reduction;
- Fourier/stress duality.

Those are B2 obligations. Any formulation that reconstructs only a quotient or obstruction must be checked for lost lift, component, or holonomy data before it may enter the equivalence box.

## 8. Completion assessment

`AC-PD-B1` is `READY-FOR-CURATOR`. The next active unit is `AC-PD-B2`: normalize the singular, quadratic, Schur, cographic, orthogonal, and Fourier/stress formulations, prove each exact arrow, and separate full equivalence from one-way obstruction projections.
