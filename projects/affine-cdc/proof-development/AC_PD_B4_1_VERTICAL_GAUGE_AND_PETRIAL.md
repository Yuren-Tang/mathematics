# AC-PD-B4.1 — vertical gauge torsor and code-filtered partial Petrials

**Proof-development state:** `COMPLETE-DRAFT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Validated sources:** `FIVE_CDC_GAUGE_AS_PIECEWISE_ROOT_TRANSLATION_V1.md`, `FIVE_CDC_GAUGE_PARTIAL_PETRIAL_CORRESPONDENCE_V1.md`, and `gauge/gauge-modes-and-circuits.md`  
**Depends on:** A4 local affine torsors; B1.4 cycle-face surfaces  
**Immediate consumers:** B4.2 support pivots and horizontal switches; B4.3 obstruction arrangements; B6 holonomy  
**External mathematical inputs:** none

## 0. Scope

Let $G$ be a finite loopless cubic multigraph with no isolated vertices, let

$$
f:E(G)\to\Gamma\setminus\{0\},
\qquad
\Gamma=\mathbf F_2^3,
$$

be a nowhere-zero flow, and fix one compatible eight-index root lift $g$ of $f$.

If an ambient carrier contains isolated vertices, remove them before forming the gauge torsor: translation variables at isolated vertices act trivially on every root and destroy freeness without contributing mathematical data.

## 1. Root fibres

For $0\ne h\in\Gamma$, let

$$
\mathcal R_h
=
\bigl\{\{s,s+h\}:s\in\Gamma\bigr\}.
$$

For $k\in\Gamma$, define

$$
\tau_k\{s,s+h\}
=
\{s+k,s+h+k\}.
$$

### Lemma 1.1 — fibre stabilizer

On $\mathcal R_h$,

$$
\tau_k=\tau_{k'}
\quad\Longleftrightarrow\quad
k+k'\in\langle h\rangle.
$$

### Proof

The two translated unordered pairs agree exactly when their first endpoints differ by either $0$ or $h$. $\square$

Thus the translation action on one root fibre factors faithfully through

$$
Q_h=\Gamma/\langle h\rangle.
$$

## 2. Admissible vertex fields

Define

$$
H_f^0
=
\left\{
 k:V(G)\to\Gamma:
 k_u+k_v\in\langle f(e)\rangle
 \text{ for every }e=uv
\right\}.
$$

For $k\in H_f^0$, there is a unique edge bit $\lambda_e(k)$ with

$$
k_u+k_v=\lambda_e(k)f(e).
$$

This gives a linear map

$$
\Lambda_f:H_f^0\to\mathbf F_2^{E(G)},
\qquad
k\mapsto\lambda(k).
$$

Its image is the gauge code $\mathcal B_f$.

## 3. Root-lift torsor

For $k\in H_f^0$, define

$$
g^k(e)=\tau_{k_u}(g(e))
$$

for either endpoint $u$ of $e$.

### Theorem 3.1 — exact vertical torsor

The formula is endpoint-independent and defines another root lift of the same flow $f$. Conversely every labelled root lift of $f$ is uniquely $g^k$ for one $k\in H_f^0$.

Hence the labelled root-lift space above $f$ is a torsor under $H_f^0$.

### Proof

For $e=uv$ with $h=f(e)$, admissibility gives $k_u+k_v\in\langle h\rangle$, so Lemma 1.1 gives

$$
\tau_{k_u}(g(e))=\tau_{k_v}(g(e)).
$$

At a source vertex, the three incident roots are the edges of one affine triangle on three support indices. Translating all three indices by $k_v$ preserves that triangle law and every projected difference. Thus $g^k$ is a root lift of $f$.

Conversely, compare $g$ and another lift $g'$ at a vertex $v$. Their local affine triangles have the same three projected directions. The local affine classification gives a unique translation $k_v$ carrying one triangle to the other. Along $e=uv$, the two endpoint translations carry the same old root to the same new root, so Lemma 1.1 gives

$$
k_u+k_v\in\langle f(e)\rangle.
$$

Thus $k\in H_f^0$ and $g'=g^k$. Uniqueness follows because a three-point affine triangle has trivial translation stabilizer. $\square$

## 4. Reduced gauge code and disconnected components

Let $\pi_0(G)$ denote the edge-bearing connected components. A field lies in $\ker\Lambda_f$ exactly when it is constant on every component. Therefore

$$
\ker\Lambda_f
\cong
\Gamma^{\pi_0(G)}.
$$

### Corollary 4.1

There is an exact sequence

$$
0\longrightarrow
\Gamma^{\pi_0(G)}
\longrightarrow
H_f^0
\xrightarrow{\Lambda_f}
\mathcal B_f
\longrightarrow0.
$$

Consequently

$$
\boxed{
\mathcal B_f
\cong
H_f^0/\Gamma^{\pi_0(G)}.}
$$

For connected $G$, this reduces to $H_f^0/\Gamma$. The quotient forgets independent global affine relabellings on the connected components; it does not identify any nonconstant vertical motion.

## 5. Piecewise translations and harmonic quotients

Let $0\ne\lambda\in\mathcal B_f$, choose a lift $k$, and put

$$
S=\operatorname{supp}\lambda.
$$

On every edge outside $S$, $k_u=k_v$. Hence $k$ is constant, say $p_X$, on each connected component $X$ of $G-S$. For every crossing edge $e=XY$,

$$
f(e)=p_X+p_Y.
$$

Thus contracting the regions gives a quotient on which $f|_S$ is simultaneously a nowhere-zero exact tension and a flow. Conversely every such labelled connected-region quotient produces a gauge word.

This is the exact harmonic cut-quotient presentation of vertical motion.

## 6. Local face-side swap

Write a root on $e=uv$ as

$$
g(e)=\{s,s+h\},
\qquad h=f(e).
$$

The two incident support-face sides have labels $s$ and $s+h$.

### Theorem 6.1 — edge swap bit

Across $e$:

- if $\lambda_e=0$, the translated sides glue label-to-equal-label;
- if $\lambda_e=1$, they glue after interchanging the two sides.

### Proof

If $\lambda_e=0$, then $k_u=k_v$. If $\lambda_e=1$, then $k_v=k_u+h$, and

$$
s+k_u=s+h+k_v,
\qquad
s+h+k_u=s+k_v.
$$

$\square$

The gauge support records face-side swaps, not the set of source edges whose root labels happen to change numerically.

## 7. Partial Petrial theorem

Let $S_g$ be the cycle-face embedding of $g$. For $P\subseteq E(G)$, let $S_g^{\tau(P)}$ denote the ribbon embedding obtained by interchanging the two face-side identifications across each edge band in $P$.

### Theorem 7.1 — gauge/Petrial correspondence

For every $k\in H_f^0$,

$$
\boxed{
S_{g^k}=S_g^{\tau(\operatorname{supp}\lambda(k))}.}
$$

Equality is on the fixed cubic one-skeleton, up to independent global support-index translations on connected components.

### Proof

Vertex translations preserve each local disc and its three edge incidences. The only change in tracing a face occurs when it crosses an edge. Theorem 6.1 says that exactly the edges with bit one swap their two sides. Those independent swaps are precisely the partial Petrial. $\square$

### Corollary 7.2

The gauge code is exactly the set of partial-Petrial edge sets accessible while the projected Fano flow is fixed:

$$
\mathcal B_f
=
\{P\subseteq E(G):S_g^{\tau(P)}=S_{g'}
\text{ for some root lift }g'\text{ of }f\}.
$$

## 8. Preserved and changed data

A vertical gauge move preserves:

- the source graph and edge objects;
- the projected Fano flow $f$;
- all local root-flow equations;
- exact edge double coverage.

It may change:

- root labels and the old-colour quotient $J_g$;
- support-cycle components;
- the cycle-face surface and its Euler characteristic/orientability;
- the full dual triangulation $T_g$;
- both factorable and full-dual half-cube compressibility.

A constant field on one source component changes only the support-index names there and has zero Petrial bit.

## 9. Boundary with support pivots

A support-cycle pivot is not a vertical gauge move. It recolours one face component while preserving the uncoloured embedding, and it changes the projected Fano flow. A gauge move preserves the flow while changing the embedding by a code-filtered partial Petrial.

Thus:

$$
\begin{array}{c|c|c}
\text{move}&\text{uncoloured embedding}&\text{Fano flow}\\
\hline
\text{gauge/Petrial}&\text{may change}&\text{fixed}\\
\text{support-cycle pivot}&\text{fixed}&\text{changes}.
\end{array}
$$

## 10. Assurance boundary

The torsor, componentwise kernel, harmonic quotient, edge-swap, and Petrial statements are theorem-level. Numerical changes of face counts in specific laboratories remain certificate data. No claim is made that the accessible Petrial code is the full edge power set, or that every obstructed Petrial orbit has an escape.

## 11. Completion assessment

`AC-PD-B4.1` is `COMPLETE-DRAFT`. The next active unit is B4.2: prove the support-cycle pivot and the complete exponent-two horizontal-switch decomposition, distinguishing one connected-cycle reconfiguration edge from a commuting sequence on disconnected cycle components.