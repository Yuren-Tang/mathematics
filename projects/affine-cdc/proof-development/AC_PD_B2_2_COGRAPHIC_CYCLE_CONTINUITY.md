# AC-PD-B2.2 — exact cographic cycle-continuity equivalence

**Proof-development state:** `COMPLETE-DRAFT / TERMINOLOGY-BOUNDARY`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Recovered controlling packet:** `FIVE_CDC_K5_COGRAPHIC_MAP_V1.md` at `research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`  
**Depends on:** B1.1 and B2.1  
**Immediate consumers:** B3 target/category structure; B5 cut interfaces; B9 composition route  
**External mathematical inputs:** none

## 0. Terminology boundary

Let $M,N$ be binary matroids with ground sets $E(M),E(N)$. In this dossier a **cycle-continuous edge map** is an arbitrary function

$$
\phi:E(M)\longrightarrow E(N)
$$

such that the inverse image of every binary cycle of $N$ is a binary cycle of $M$.

No injectivity, surjectivity, linear ground-set extension, strong-map property, weak-map property, matroid quotient, or matroid embedding is implied. The phrase “cycle-continuous matroid map” below always means this inverse-cycle condition.

## 1. Edge-pair labelling

Let $G$ be a finite loopless multigraph and let $S$ be a finite support-index set. An indexed $|S|$-support even double cover $(F_s)_{s\in S}$ assigns to every source edge exactly two support indices. Define

$$
\phi_{\mathcal F}:E(G)\longrightarrow E(K_S)=\binom S2
$$

by

$$
\phi_{\mathcal F}(e)=\{s\in S:e\in F_s\}.
$$

Conversely, any edge map

$$
\phi:E(G)\to E(K_S)
$$

defines support words

$$
F_s=\phi^{-1}(\delta_{K_S}(s)),
$$

where $\delta_{K_S}(s)$ is the star at target vertex $s$. Every source edge then belongs to exactly two of the $F_s$, namely the endpoints of its target edge label.

Thus only the evenness of the star preimages remains to be imposed.

## 2. Cut space of the complete graph

For $A\subseteq S$, write

$$
\delta_{K_S}(A)
$$

for the target cut. Over $\mathbf F_2$,

$$
\delta_{K_S}(A)
=
\bigtriangleup_{s\in A}\delta_{K_S}(s),
$$

where $\triangle$ denotes symmetric difference. Hence the vertex stars generate the binary cut space of $K_S$; their only universal dependency is the symmetric difference of all stars, which is empty.

For any edge map $\phi$, inverse image commutes with symmetric difference:

$$
\phi^{-1}(X\triangle Y)
=
\phi^{-1}(X)\triangle\phi^{-1}(Y).
$$

The binary cycle space $\mathcal C(G)$ is closed under symmetric difference.

## 3. Cut-to-cycle theorem

### Theorem 3.1

For a finite loopless multigraph $G$ and finite index set $S$, the following are equivalent.

1. $G$ has an indexed $|S|$-support even double cover.
2. There is an edge map
   $$
   \phi:E(G)\to E(K_S)
   $$
   such that
   $$
   \phi^{-1}(\delta_{K_S}(s))\in\mathcal C(G)
   $$
   for every $s\in S$.
3. There is such an edge map for which
   $$
   \phi^{-1}(C)\in\mathcal C(G)
   $$
   for every cut $C$ of $K_S$.
4. There is a cycle-continuous edge map
   $$
   M(G)\longrightarrow M^*(K_S)
   $$
   with underlying ground-set map $\phi$.

### Proof

$(1)\Rightarrow(2)$ uses the edge-pair map $\phi_{\mathcal F}$; the star preimage at $s$ is exactly $F_s$ and is even.

$(2)\Rightarrow(1)$ uses the star preimages as the supports. Every target edge has exactly two endpoints, so every source edge is covered exactly twice.

The star-generation and inverse-symmetric-difference identities of Section 2 prove $(2)\Longleftrightarrow(3)$.

By definition, the binary cycles of the cographic matroid $M^*(K_S)$ are the binary cuts of $K_S$. Therefore $(3)$ is precisely the inverse-cycle condition in $(4)$. $\square$

For $|S|=5$, this is the exact cographic formulation of five-support existence.

## 4. Root-flow identification

Identify an edge $\{i,j\}$ of $K_S$ with the root

$$
\varepsilon_i+\varepsilon_j
$$

in

$$
H_S=
\left\{z\in\mathbf F_2^S:\sum_{s\in S}z_s=0\right\}.
$$

### Proposition 4.1

Under this identification, Theorem 3.1 is exactly the root-valued-flow equivalence:

$$
\text{cut-preimage cycle-continuity}
\Longleftrightarrow
\sum_{e\ni v}\phi(e)=0
\quad\text{in }H_S
$$

at every source vertex $v$.

### Proof

The $s$-coordinate of the local root sum is the parity of incident source edges whose target label lies in the star $\delta_{K_S}(s)$. Thus the local sum vanishes in every coordinate exactly when every star preimage is even at every source vertex. $\square$

For $S=[5]$, the root orbit is the anisotropic orbit of $(H_5,q_5)$ from B2.1.

## 5. Cubic local form

Assume $G$ is cubic. Let the three incident source edges at $v$ have target labels $a,b,c\in E(K_S)$, counted as edge objects with possible repeated values.

### Theorem 5.1 — target triangle law for $S=[5]$

The cut-preimage condition holds locally at $v$ if and only if the three labels are three distinct edges of one triangle of $K_5$.

### Proof

View each target edge as its incidence root in $H_5$. Local cut-preimage evenness is equivalent to

$$
a+b+c=0.
$$

If two labels were equal, they would cancel and force the third root to be zero, impossible. Thus the labels are distinct. B1.1 proves that three roots of $R_5$ sum to zero exactly when the corresponding target edges form a triangle. The converse is immediate because every triangle boundary is zero in characteristic two. $\square$

This is not an additional theorem beyond the root-flow condition; it is its cubic local resolution.

## 6. Composition

### Proposition 6.1

Cycle-continuous edge maps compose.

### Proof

If

$$
E(M)\xrightarrow{\phi}E(N)\xrightarrow{\psi}E(P)
$$

pull cycles back to cycles, then for every cycle $C$ of $P$,

$$
(\psi\circ\phi)^{-1}(C)
=\phi^{-1}(\psi^{-1}(C)),
$$

which is a cycle of $M$. $\square$

Consequently, any cycle-continuous map from $M(G)$ to a binary matroid that itself admits a cycle-continuous map to $M^*(K_5)$ yields a five-support cover of $G$. This is the exact categorical content of intermediate-target strategies such as Petersen-colouring implications; any particular intermediate theorem still requires its own source and hypothesis audit.

## 7. Cographic, not graphic

The target cycle space in this theorem is the cut space of $K_5$, so the natural target is $M^*(K_5)$. Replacing it by the graphic cycle matroid $M(K_5)$ would impose preimages of target graph cycles rather than target cuts and is a different condition.

No planarity dual graph is being chosen. The adjective “cographic” refers to the matroid dual, not to a geometric embedding of $K_5$.

## 8. Relation to the other B2 formulations

The maps carry the following equivalent full witnesses:

$$
\begin{aligned}
&\phi:E(G)\to E(K_5)
\text{ pulling cuts back to cycles}\\
&\Longleftrightarrow
R_5\text{-valued root flow}\\
&\Longleftrightarrow
\text{anisotropic }H_5\text{-flow}\\
&\Longleftrightarrow
\text{quadratic cycle solution }(b,d,x,y).
\end{aligned}
$$

Unlike the singular quotient or Schur boundary, the cographic edge map retains the complete edgewise root label and is therefore a full graph-level witness.

## 9. Scope and literature boundary

- This dossier proves the binary inverse-cycle equivalence and composition law.
- It does not identify the map with every use of “tension-continuous”, “flow-continuous”, “matroid homomorphism”, or “strong map” in the literature. Those terms vary by direction and convention.
- It does not claim novelty of the $M^*(K_5)$ formulation.
- Any publication statement connecting it to Petersen colouring, normal edge-colouring, or classical 5-CDC literature requires a separate source audit.
- No formalization claim is made.

## 10. Completion assessment

`AC-PD-B2.2` is `COMPLETE-DRAFT / TERMINOLOGY-BOUNDARY`. The next active unit is B2.3: normalize the universal orthogonal root-lift and rank-reduction chain, distinguishing full anisotropic-flow equivalence from projection along singular vectors, quotient residues, and dimension-specific automatic compatibility.