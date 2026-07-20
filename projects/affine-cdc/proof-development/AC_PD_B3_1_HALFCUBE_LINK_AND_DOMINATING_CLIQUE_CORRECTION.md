# AC-PD-B3.1 — quadratic common-link formula and validated dominating-clique capacity

**Proof-development state:** `COMPLETE-DRAFT / PROVENANCE-REPAIR`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Validated controlling packets:** `FIVE_CDC_HALFCUBE_CLIQUE_LINK_CAPACITY_V1.md` and `FIVE_CDC_DOMINATING_CLIQUE_EXACT_CAPACITY_V1.md` at `research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`  
**Depends on:** B1.4 half-cube target semantics; elementary quadratic and graph-homomorphism theory  
**Immediate consumers:** B3 finite target classification; B5 interface targets; B9 factorable-target route  
**External mathematical inputs:** none

## 0. Provenance repair

An earlier version of this dossier incorrectly attributed two false statements to recovered packets named `FIVE_CDC_HALFCUBE_COMMON_LINK_REDUCTION_V1.md` and `FIVE_CDC_TARGET_DOMINATING_CLIQUE_CAPACITY_V1.md`. Those names are not the controlling source packets. The actual packets are the two files named above, and their half-cube link table and exact join theorem are mathematically correct.

This repaired unit therefore has two purposes:

1. prove a general quadratic formula that explains the explicit half-cube link table;
2. independently verify the recovered dominating-clique classification rather than supersede it.

## 1. Quadratic Cayley target

Let $(E,q)$ be a finite-dimensional nondegenerate quadratic space over $\mathbf F_2$, with polar form

$$
B(x,y)=q(x+y)+q(x)+q(y).
$$

Let $\mathscr A(E,q)$ be the loopless graph on $E$ with

$$
x\sim y
\quad\Longleftrightarrow\quad
q(x+y)=1.
$$

For a nonempty clique $C\subseteq E$, fix $\alpha\in C$ and put

$$
S_C=\{c+\alpha:c\in C\setminus\{\alpha\}\},
\qquad
D_C=\operatorname{span}S_C.
$$

## 2. Exact common-link formula

### Theorem 2.1

A vertex $y=\alpha+z$ is adjacent to every member of $C$ if and only if

$$
\boxed{
q(z)=1,
\qquad
B(z,d)=1\quad(d\in S_C).}
$$

### Proof

Adjacency to $\alpha$ is $q(z)=1$. For $c\ne\alpha$, let $d=c+\alpha$. Since $C$ is a clique, $q(d)=1$. Therefore

$$
q(y+c)=q(z+d)=q(z)+q(d)+B(z,d)=B(z,d),
$$

once $q(z)=1$. Thus adjacency to $c$ is exactly $B(z,d)=1$. $\square$

### Corollary 2.2

The linear equations $B(z,d)=1$ are consistent exactly when the assignment $d\mapsto1$ on $S_C$ respects every linear dependence. If $z_0$ is one solution, then

$$
\Gamma(C)
=
\alpha+
\{z\in z_0+D_C^\perp:q(z)=1\}.
$$

Thus a common link is a quadratic slice of an affine linear coset. The recovered half-cube packets do not replace this slice by a bare annihilator; instead they compute the slice explicitly in the five-coordinate target.

## 3. Half-cube clique links

Let $\mathscr A_5$ be the even half-cube. Translation and coordinate permutation act transitively on cliques of each size $1\le r\le5$. Evaluating Theorem 2.1 on the canonical cliques

$$
Q_r\subseteq\{0,12,13,14,15\}
$$

gives

$$
\begin{array}{c|c|c}
r&\operatorname{Lk}(Q_r)&\chi\\
\hline
1&J(5,2)=L(K_5)&5\\
2&K_3\square K_2&3\\
3&K_2\sqcup K_1&2\\
4&K_1&1\\
5&\varnothing&0.
\end{array}
$$

These are exactly the link types and chromatic numbers stated and proved in `FIVE_CDC_HALFCUBE_CLIQUE_LINK_CAPACITY_V1.md`.

## 4. Exact dominating-clique reduction

Let $J,H$ be finite simple loopless graphs and suppose

$$
J=K_r\vee R.
$$

### Theorem 4.1

There is a homomorphism $J\to H$ if and only if there are an $r$-clique $Q\subseteq H$ and a homomorphism

$$
R\longrightarrow H[\Gamma_H(Q)].
$$

### Proof

A homomorphism is injective on the source clique and maps it to an $r$-clique $Q$. Every remainder vertex is adjacent to all clique vertices, so its image lies in the common link. Conversely, combine a clique bijection with a homomorphism into the common link. $\square$

Applying the half-cube link table yields the recovered exact theorem.

### Theorem 4.2 — validated half-cube capacity

For every finite loopless graph $R$ and every $2\le r\le5$,

$$
\boxed{
K_r\vee R\longrightarrow\mathscr A_5
\quad\Longleftrightarrow\quad
\chi(R)\le5-r.}
$$

### Proof

The forward implication follows because the relevant common link has chromatic number $5-r$. Conversely, that link contains a clique $K_{5-r}$; a $(5-r)$-colouring gives $R\to K_{5-r}$ and hence a map into the link. $\square$

For $r=1$, the exact statement is instead

$$
K_1\vee R\to\mathscr A_5
\quad\Longleftrightarrow\quad
R\to L(K_5),
$$

so chromatic number alone does not classify the five-chromatic boundary.

## 5. General cardinality warning

A general homomorphism need not be injective on $R$, so Theorem 4.1 does not imply a vertex-count bound

$$
|V(J)|\le r+|\Gamma_H(Q)|.
$$

That inequality is valid only for injective maps on the remainder. This is a general warning, not a correction to the recovered half-cube capacity packets, which use chromatic homomorphism capacity rather than remainder cardinality.

## 6. Validated downstream consequences

The following recovered results survive this audit.

1. $K_6\not\to\mathscr A_5$, because $\omega(\mathscr A_5)=5$.
2. $K_3\vee C_{2m+1}\not\to\mathscr A_5$, because the triangle link is bipartite.
3. $K_2\vee R\not\to\mathscr A_5$ exactly when $\chi(R)\ge4$.
4. The flower-snark core $K_3\vee C_5$ has a short valid common-link obstruction.
5. The rank-one target remains the finer homomorphism problem $R\to L(K_5)$.

All conclusions remain target-graph statements. A quotient calculation for $J_g$ does not automatically classify the full dual $T_g^{(1)}$; B1.4's scope boundary remains controlling.

## 7. Completion assessment

`AC-PD-B3.1` is `COMPLETE-DRAFT / PROVENANCE-REPAIR`. It validates the controlling recovered link and capacity packets and supplies a more general quadratic derivation. No source packet is marked false by this unit.