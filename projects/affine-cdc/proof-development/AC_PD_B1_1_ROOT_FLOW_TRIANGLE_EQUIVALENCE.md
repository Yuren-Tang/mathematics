# AC-PD-B1.1 — five-support, root-flow, and $K_5$-triangle equivalence

**Proof-development state:** `COMPLETE-DRAFT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Programme:** B — five-support strengthening  
**Depends on:** A0 multiplicity semantics and the loopless finite cubic graph model  
**Immediate consumers:** B1.2 matching/four-flow normalization; B2 equivalent-formulation chain; B3 surface/target semantics  
**External mathematical inputs:** none

## 0. Scope and graph model

Let $G$ be a finite loopless cubic multigraph. Parallel edge objects are allowed and remain distinct. Cubic means that every active vertex is incident with exactly three edge objects. Isolated ambient vertices are irrelevant and may be omitted.

The loopless qualification is load-bearing for the present once-per-edge incidence language and for the phrase “the three incident roots”. A loop-aware five-support statement could instead be written on darts or with half-edge degrees, but that is not the object used by the integrated five-support corpus.

Write

$$
[5]=\{1,2,3,4,5\},
$$

let $\varepsilon_1,\dots,\varepsilon_5$ be the standard basis of $\mathbf F_2^5$, and define

$$
E_5=
\left\{x\in\mathbf F_2^5:
\sum_{i=1}^5x_i=0
\right\}.
$$

The ten roots are

$$
R_5=
\{\varepsilon_i+\varepsilon_j:1\leq i<j\leq5\}.
$$

Equivalently, identify $R_5$ with the two-element subsets of $[5]$, hence with the edge set of $K_5$.

## 1. Indexed five-support even double covers

### Definition 1.1

An **indexed five-support even double cover** of $G$ is a five-tuple

$$
\mathcal F=(F_1,F_2,F_3,F_4,F_5),
\qquad
F_i\subseteq E(G),
$$

such that:

1. for every vertex $v$ and every $i$,
   $$
   |F_i\cap\operatorname{Inc}_G(v)|\equiv0\pmod2;
   $$
2. for every edge object $e$,
   $$
   \bigl|\{i\in[5]:e\in F_i\}\bigr|=2.
   $$

Empty supports and equal support values at different indices are allowed. The index names remain part of the witness. This is the natural pre-decomposition object; no circuit decomposition is included in the definition.

## 2. Root-valued flows

### Definition 2.1

A **root-valued $E_5$-flow** is a map

$$
\lambda:E(G)\longrightarrow R_5
$$

such that for every vertex $v$,

$$
\sum_{e\in\operatorname{Inc}_G(v)}\lambda(e)=0
\qquad\text{in }E_5.
$$

Because the coefficient field has characteristic two and $G$ is loopless, this is the unoriented once-per-edge conservation law.

## 3. From five supports to a root-valued flow

Given $\mathcal F=(F_i)_{i\in[5]}$, define

$$
\lambda_{\mathcal F}(e)
=
\sum_{i:e\in F_i}\varepsilon_i.
$$

### Lemma 3.1 — root condition

For every edge $e$, one has $\lambda_{\mathcal F}(e)\in R_5$.

### Proof

Exactly two distinct support indices contain $e$. Hence $\lambda_{\mathcal F}(e)$ is the sum of exactly two distinct standard basis vectors. $\square$

### Lemma 3.2 — conservation

For every vertex $v$,

$$
\sum_{e\in\operatorname{Inc}_G(v)}
\lambda_{\mathcal F}(e)=0.
$$

### Proof

Take the $i$-th coordinate. It equals

$$
\sum_{e\in\operatorname{Inc}_G(v)}
\mathbf 1_{e\in F_i}
=
|F_i\cap\operatorname{Inc}_G(v)|\pmod2,
$$

which is zero by vertex-evenness. Every coordinate vanishes, so the vector sum is zero. $\square$

Thus $\lambda_{\mathcal F}$ is a root-valued $E_5$-flow.

## 4. From a root-valued flow to five supports

Given $\lambda:E(G)\to R_5$, define

$$
F_i(\lambda)
=
\{e\in E(G):\lambda(e)_i=1\}
\qquad(i\in[5]).
$$

### Lemma 4.1 — exact edge multiplicity

Every edge belongs to exactly two of the supports $F_i(\lambda)$.

### Proof

Every root has Hamming weight two. $\square$

### Lemma 4.2 — vertex evenness

For every vertex $v$ and every $i$,

$$
|F_i(\lambda)\cap\operatorname{Inc}_G(v)|
\equiv0\pmod2.
$$

### Proof

The left-hand parity is the $i$-th coordinate of

$$
\sum_{e\in\operatorname{Inc}_G(v)}\lambda(e),
$$

which is zero by conservation. $\square$

Thus $(F_i(\lambda))_{i\in[5]}$ is an indexed five-support even double cover.

## 5. Mutual inverse property

### Theorem 5.1 — root-flow equivalence

The two constructions

$$
\mathcal F\longmapsto\lambda_{\mathcal F},
\qquad
\lambda\longmapsto(F_i(\lambda))_{i\in[5]}
$$

are mutually inverse. Hence indexed five-support even double covers of $G$ are canonically equivalent to root-valued $E_5$-flows.

### Proof

Starting with $\mathcal F$, an edge $e$ belongs to $F_i(\lambda_{\mathcal F})$ exactly when the $i$-th coordinate of $\lambda_{\mathcal F}(e)$ is one, exactly when $e\in F_i$.

Starting with $\lambda$, the vector reconstructed from its coordinate supports has a one exactly in the coordinates where $\lambda(e)$ has a one, hence is $\lambda(e)$. These equalities hold edgewise and coordinatewise. $\square$

### Corollary 5.2 — equivariance under support renaming

The natural action of $S_5$ by permuting support indices corresponds exactly to the coordinate-permutation action on $E_5$ and $R_5$.

### Proof

Both actions permute the same coordinate indicators in the defining formula for $\lambda_{\mathcal F}$. $\square$

This is the precise sense in which support names are gauge labels rather than unordered support values.

## 6. The local $K_5$ triangle law

Identify a root $\varepsilon_i+\varepsilon_j$ with the edge $\{i,j\}$ of $K_5$.

### Lemma 6.1 — three roots summing to zero form a triangle

Let $r_1,r_2,r_3\in R_5$. Then

$$
r_1+r_2+r_3=0
$$

if and only if there are three distinct indices $i,j,k\in[5]$ such that, after reordering,

$$
r_1=\varepsilon_i+\varepsilon_j,
\qquad
r_2=\varepsilon_j+\varepsilon_k,
\qquad
r_3=\varepsilon_k+\varepsilon_i.
$$

### Proof

Suppose first that the sum is zero. No two roots can be equal: if $r_1=r_2$, then $r_3=0$, contrary to $r_3\in R_5$.

Represent the roots by two-subsets $A,B,C\subseteq[5]$. Vector addition is symmetric difference, so

$$
A\triangle B\triangle C=\varnothing,
\qquad
C=A\triangle B.
$$

Since $|A|=|B|=|C|=2$,

$$
2=|A\triangle B|
=|A|+|B|-2|A\cap B|
=4-2|A\cap B|,
$$

and therefore $|A\cap B|=1$. Write

$$
A=\{i,j\},
\qquad
B=\{j,k\},
$$

with $i,j,k$ distinct. Then

$$
C=A\triangle B=\{i,k\}.
$$

Conversely, the three displayed triangle-edge roots sum to zero because every coordinate occurs twice. $\square$

### Theorem 6.2 — triangle-labelling equivalence

A root-valued $E_5$-flow on a finite loopless cubic multigraph is exactly an edge labelling

$$
\tau:E(G)\longrightarrow E(K_5)
$$

such that the three edge labels incident at every vertex are the three edges of one triangle of $K_5$.

### Proof

The root/edge identification is a bijection $R_5\cong E(K_5)$. At a cubic vertex, flow conservation says that its three root labels sum to zero. Lemma 6.1 is exactly the triangle condition. Conversely every target triangle has root sum zero, giving conservation. $\square$

### Corollary 6.3 — local nondegeneracy

At every cubic vertex:

- the three root values are pairwise distinct;
- exactly three support coordinates occur locally;
- each of those three coordinates occurs on exactly two incident edges;
- the other two coordinates occur on no incident edge.

This is the local five-support incidence law.

## 7. Parallel edges, components, and empty cases

- **Parallel edges.** Distinct source edge objects may receive equal or different $K_5$ labels; they remain separate coordinates of the source flow and separate members of all supports.
- **Disconnected graph.** All constructions and inverse equalities are componentwise. No connectedness hypothesis is used.
- **Empty active graph.** The unique empty root flow corresponds to five empty indexed supports.
- **Repeated supports.** Equality $F_i=F_j$ does not identify indices $i,j$; the root coordinate labelling retains them separately.
- **Loops.** No loop extension is asserted. The present theorem uses the loopless cubic incidence object of the five-support programme.

## 8. What this theorem does and does not prove

This unit closes the first three entries of the integrated object layer:

$$
\text{indexed five-support even cover}
\Longleftrightarrow
R_5\text{-valued }E_5\text{ flow}
\Longleftrightarrow
K_5\text{-triangle labelling}.
$$

It does **not** yet identify this object with:

- a matching plus a four-flow, until the exact complement and terminal/boundary conditions are defined;
- a cographic or cycle-continuous map, until source and target circuit conventions are fixed;
- a quadratic-cycle equation, until the coordinate choice and reconstruction map are explicit;
- a fixed Fano projection, fixed plane, or fixed compatible lift;
- the componentwise surface/halfcube criterion.

Those arrows remain separate B1/B2 obligations rather than consequences of terminology.

## 9. Corpus mapping and correction boundary

This dossier supplies the omitted proof of Theorem 1.1 and the local triangle law in `five-support/root-flow-lifting.md`, and closes entries 1–3 of the global equivalence package in `five-support/equivalent-formulations-and-proof-families.md`.

It also sharpens the graph model to the finite loopless cubic multigraph actually used by the incidence and Fano-flow layers. No claim is made that the later matching, cographic, quadratic, or fixed-lift formulations are already closed merely because the integrated chapter lists them as equivalent.

## 10. Completion assessment

`AC-PD-B1.1` is `COMPLETE-DRAFT`. The next active unit is B1.2: define and prove the exact matching/four-flow equivalence, including the status of the distinguished support, the matching condition, the graph obtained after deletion, and the necessary boundary behavior at the resulting degree-two/degree-three vertices.
