# AC-PD-B3.1 — half-cube common links and dominating-clique correction

**Proof-development state:** `COMPLETE-DRAFT / MATHEMATICAL-CORRECTION`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Affected recovered packets:** `FIVE_CDC_HALFCUBE_COMMON_LINK_REDUCTION_V1.md` and `FIVE_CDC_TARGET_DOMINATING_CLIQUE_CAPACITY_V1.md` at `research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`  
**Depends on:** B1.4 half-cube target semantics; elementary quadratic and graph-homomorphism theory  
**Immediate consumers:** B3 finite target no-go/classification packets; B5 interface targets; B9 target-capacity route  
**External mathematical inputs:** none

## 0. Correction summary

Two recovered target-capacity statements are false as written.

1. The common neighbourhood of a clique in a quadratic Cayley graph is **not** generally a translate of the annihilator of the difference span. Even a one-vertex clique is an immediate counterexample: its common neighbourhood is the anisotropic sphere around that vertex, not the whole space.
2. A graph homomorphism need not be injective outside a dominating clique. Therefore the existence of a homomorphism does **not** imply
   $$
   |V(J)|\leq |C|+|\Gamma_H(\phi(C))|.
   $$
   Arbitrarily many outside twins may collapse to one common neighbour.

This dossier gives the exact replacements.

## 1. Quadratic Cayley target

Let $(E,q)$ be a finite-dimensional nondegenerate quadratic space over $\mathbf F_2$, with polar form

$$
B(x,y)=q(x+y)+q(x)+q(y).
$$

Define the loopless graph

$$
\mathscr A(E,q)
$$

on vertex set $E$ by

$$
x\sim y
\quad\Longleftrightarrow\quad
q(x+y)=1.
$$

The five-coordinate half-cube is the case $E=E_5$ with its minus-type quadratic form.

For a vertex set $C$, write

$$
\Gamma(C)=\bigcap_{c\in C}N(c)
$$

for its open common neighbourhood.

## 2. Exact clique-difference equations

Let $C\subseteq E$ be a nonempty clique and fix $\alpha\in C$. Put

$$
S_C=\{c+\alpha:c\in C\setminus\{\alpha\}\},
\qquad
D_C=\operatorname{span}S_C.
$$

Every $d\in S_C$ is anisotropic because $c$ is adjacent to $\alpha$.

### Theorem 2.1 — exact common-link formula

A vertex $y=\alpha+z$ lies in $\Gamma(C)$ if and only if

$$
\boxed{
q(z)=1,
\qquad
B(z,d)=1\quad\text{for every }d\in S_C.}
$$

### Proof

Adjacency to $\alpha$ is exactly $q(z)=1$. For $c\ne\alpha$, put $d=c+\alpha$. Since $C$ is a clique, $q(d)=1$. Then

$$
q(y+c)=q(z+d)=q(z)+q(d)+B(z,d)=B(z,d).
$$

Thus adjacency to $c$ is exactly $B(z,d)=1$. $\square$

The common link is therefore a quadratic slice of an affine linear system, not merely an affine subspace.

## 3. Linear consistency and the residual quadratic slice

The equations

$$
B(z,d)=1
\qquad(d\in S_C)
$$

are consistent exactly when the assignment $d\mapsto1$ on the generating set $S_C$ respects every linear dependence.

### Proposition 3.1

The following are equivalent.

1. The linear equations $B(z,d)=1$ for $d\in S_C$ have a solution.
2. For every finite subset $T\subseteq S_C$ with
   $$
   \sum_{d\in T}d=0,
   $$
   one has $|T|$ even.
3. The rule $d\mapsto1$ extends to a linear functional
   $$
   \ell_C:D_C\to\mathbf F_2.
   $$

If these conditions hold and $z_0$ is one solution, the full linear solution set is

$$
L_C=z_0+D_C^\perp.
$$

### Proof

This is the standard consistency criterion for assigning values to a spanning family. If $z_0$ solves the equations, every other solution differs by a vector annihilating $D_C$, and every such difference preserves the equations. $\square$

### Corollary 3.2 — corrected common-link reduction

If the linear system is inconsistent, then $\Gamma(C)=\varnothing$. If it is consistent, then

$$
\boxed{
\Gamma(C)=
\alpha+
\{z\in z_0+D_C^\perp:q(z)=1\}.}
$$

Thus common-link size and structure depend on the restriction of $q$ to the affine coset $z_0+D_C^\perp$, not only on $\dim D_C$.

## 4. Immediate counterexamples to the false annihilator formula

### Singleton clique

For $C=\{\alpha\}$, one has $D_C=0$. The false formula gives

$$
\alpha+D_C^\perp=E,
$$

whereas the true common neighbourhood is

$$
N(\alpha)=\alpha+\{z:q(z)=1\}.
$$

Unless every nonzero vector is anisotropic and zero is somehow removed, these sets are different; in the half-cube they are dramatically different.

### Two-vertex clique

If $C=\{\alpha,c\}$ and $d=c+\alpha$, then

$$
\Gamma(C)=
\alpha+\{z:q(z)=1,\ B(z,d)=1\}.
$$

The false annihilator condition $B(z,d)=0$ has the opposite linear parity.

Therefore the recovered formula cannot be repaired by a minor convention change.

## 5. Exact dominating-clique homomorphism theorem

Let $J,H$ be finite simple loopless graphs and let $C\subseteq V(J)$ be a clique such that every vertex of $J-C$ is adjacent to every vertex of $C$. Call $C$ a dominating clique in this strong sense.

### Theorem 5.1 — exact reduction

There is a graph homomorphism

$$
\phi:J\to H
$$

if and only if there exist:

1. a clique $C'\subseteq V(H)$ with $|C'|=|C|$;
2. a bijection $\phi_C:C\to C'$;
3. a graph homomorphism
   $$
   \theta:J-C\to H[\Gamma_H(C')].
   $$

### Proof

Suppose $\phi:J\to H$. Since $H$ has no loops, adjacent vertices cannot have the same image; hence $\phi|_C$ is injective and its image $C'$ is a clique of the same cardinality. Every $v\in J-C$ is adjacent to every member of $C$, so $\phi(v)$ is adjacent to every member of $C'$. Therefore the restriction of $\phi$ maps $J-C$ into the induced common-link graph and is a homomorphism.

Conversely, combine $\phi_C$ and $\theta$. Edges within $C$ map to edges of $C'$, edges within $J-C$ are preserved by $\theta$, and every cross edge maps to an edge because every point of $\Gamma_H(C')$ is adjacent to every point of $C'$. $\square$

This theorem replaces the false cardinality capacity statement.

## 6. Correct consequences

### Corollary 6.1 — chromatic and clique capacity

If $J\to H$ and $C$ is a dominating clique, then for some $|C|$-clique $C'$ of $H$,

$$
J-C\to H[\Gamma_H(C')].
$$

Consequently

$$
\chi(J-C)
\leq
\chi(H[\Gamma_H(C')]),
$$

and

$$
\omega(J-C)
\leq
\omega(H[\Gamma_H(C')]).
$$

These are homomorphism invariants; vertex cardinality is not.

### Corollary 6.2 — complete remainder

If $J-C$ is a clique of size $s$, then $H$ contains a clique of size $|C|+s$.

### Proof

Its image is an $s$-clique in the common link of $C'$, hence is jointly complete with $C'$. $\square$

### Corollary 6.3 — empty common link

If every $|C|$-clique of $H$ has empty common link and $J-C$ is nonempty, then no homomorphism $J\to H$ exists.

### Corollary 6.4 — injective version

If one separately requires $\phi$ to be injective on $J-C$, then

$$
|V(J)|
\leq
|C|+|\Gamma_H(C')|.
$$

Thus the recovered cardinality theorem is valid for embeddings, not arbitrary graph homomorphisms.

## 7. Counterexample to the false cardinality theorem

Let

$$
J=K_{1,n}
$$

with centre $C=\{c\}$, and let $H=K_2$. The centre is a dominating one-clique, and every star admits a homomorphism to $K_2$ by sending all leaves to the other target vertex. Yet the common link of the image of $c$ has one vertex, while

$$
|V(J)|=n+1
$$

is arbitrarily large. Hence no cardinality bound of the recovered form can follow from homomorphism existence.

## 8. Consequences for existing finite target packets

### Direct $K_6$ no-go remains valid

The packet `FIVE_CDC_K6_TARGET_NO_GO_V1.md` proves directly that the half-cube contains no $K_6$, equivalently a standard $K_5$ has empty common link. Since

$$
K_6-K_5=K_1,
$$

Corollary 6.3 recovers the no-homomorphism statement. Its explicit five-colouring of $K_8-C_5$ remains a valid homomorphism witness. This result does not depend on the false vertex-count bound.

### $K_8-C_5$ classification requires certificate audit, not automatic rejection

The exact brute-force classification packet for maps

$$
K_8-C_5\to\mathscr A_5
$$

is a finite certificate claim and does not become false merely because the general capacity theorem is false. It must be checked against its own exhaustive search and corrected witness table.

### Any cardinality-only no-go requires re-audit

A target impossibility derived only from

$$
|V(J)|>|C|+|\Gamma_H(C')|
$$

for a noninjective homomorphism problem is invalid. Such packets must be repaired using Theorem 5.1, chromatic/clique capacity, holonomy, or a direct finite certificate.

## 9. Target-capacity replacement

For the half-cube target, the correct dominating-clique workflow is:

1. enumerate target cliques $C'$ of the required size up to automorphism;
2. compute the exact induced common-link graph using Theorem 2.1;
3. test whether
   $$
   J-C\to\mathscr A_5[\Gamma(C')];
   $$
4. use chromatic, clique, or exact homomorphism obstructions inside the common link;
5. invoke cardinality only for embeddings or otherwise injective subproblems.

The residual common link is a smaller quadratic-affine target and may still be tractable, but its reduction is quadratic, not merely orthogonal-linear.

## 10. Curator correction requirement

Before B3 target material is promoted:

1. mark `FIVE_CDC_HALFCUBE_COMMON_LINK_REDUCTION_V1.md` as `SUPERSEDED / FALSE FORMULA`;
2. mark the homomorphism cardinality theorem in `FIVE_CDC_TARGET_DOMINATING_CLIQUE_CAPACITY_V1.md` as false, retaining only its injective/embedding variant;
3. install Theorems 2.1 and 5.1 as the active replacements;
4. re-audit downstream no-go packets by proof type;
5. preserve direct finite classifications and direct clique no-go arguments when independently valid;
6. prevent any full-dual conclusion from a quotient target calculation without the B1.4 scope bridge.

## 11. Completion assessment

`AC-PD-B3.1` is `COMPLETE-DRAFT / MATHEMATICAL-CORRECTION`. The next active unit is B3.2: audit the direct $K_6$ no-go and the exact $K_8-C_5$ homomorphism classification, reconstruct their corrected witness tables, and classify precisely what they prove about old-colour quotients versus full dual triangulations.