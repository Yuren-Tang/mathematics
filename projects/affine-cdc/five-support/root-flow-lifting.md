# Root-valued flows and the five-support lifting problem

## 1. The five-support object

Let $G$ be a finite loopless cubic multigraph. An indexed five-support even double cover is a five-tuple

$$
(F_1,\ldots,F_5)
$$

of vertex-even edge supports such that every source edge belongs to exactly two indexed supports. Empty supports and equal support values at different indices are allowed. This is the natural pre-decomposition object; circuit decomposition is not part of the definition.

Put

$$
E_5=\left\{x\in\mathbf F_2^5:\sum_i x_i=0\right\},
\qquad
R_5=\{\varepsilon_i+\varepsilon_j:i<j\}.
$$

For an edge contained in supports $F_i,F_j$, assign the root $\varepsilon_i+\varepsilon_j$. Coordinatewise support parity is exactly the $E_5$ flow equation. Conversely, the coordinate inverse images of a root-valued flow recover the indexed supports.

### Theorem 1.1 — root-flow and triangle equivalence

The following are canonically equivalent:

1. indexed five-support even double covers;
2. root-valued flows
   $$
   \lambda:E(G)\to R_5\subset E_5;
   $$
3. edge labellings by $E(K_5)$ for which the three labels at every cubic vertex form one triangle of $K_5$.

The constructions are mutually inverse and equivariant under permutations of the five support indices.

## 2. Relation to the rank-three AffineCDC theorem

A nowhere-zero Fano flow

$$
f:E(G)\to\Gamma\setminus\{0\},
\qquad
\Gamma\cong\mathbf F_2^3,
$$

has a compatible eight-index affine root lift by the rank-three theorem. The five-support strengthening asks whether $G$ also has a root-valued $E_5$ flow.

This is not a request to delete three arbitrary supports from one prescribed eight-support witness. At graph level one may change the Fano flow, compatible lift, cycle-face embedding, and support identification.

## 3. Exact matching/four-flow formulation

A fixed support coordinate and a fixed root label have different inverse images.

- A fixed **support-coordinate** inverse image is an even support: locally the coordinate occurs zero or two times.
- A fixed **root-label** inverse image is a matching: a target triangle contains a given target edge at most once.

The previous compressed statement that a distinguished support coordinate itself gives a matching was false.

Let $W\cong\mathbf F_2^2$. An exact matching/four-flow datum consists of:

1. even supports $B,D$;
2. a matching
   $$
   M=B\cap D;
   $$
3. a nowhere-zero $W$-flow on $G-M$.

### Theorem 3.1 — exact matching/four-flow equivalence

$G$ has an indexed five-support even double cover if and only if it has exact data $(B,D,M,w)$ as above.

The support $D$ can be removed from the data only by replacing it with the exact finite $T$-join condition.

### Corollary 3.2 — component form

$G$ has an indexed five-support even double cover if and only if there exist:

1. an even support $B$;
2. a matching $M\subseteq B$;
3. a nowhere-zero $\mathbf F_2^2$-flow on $G-M$;
4. even $M$-endpoint parity in every component of $G-B$.

Equivalently,

$$
|M\cap\delta_G(K)|\equiv0\pmod2
$$

for every component $K$ of $G-B$.

Bare matching plus four-flow is insufficient: it forgets the root-fibre or boundary datum required for reconstruction.

## 4. Fixed Fano flow and fixed plane

Now fix both a nowhere-zero Fano flow $f$ and a plane $W\leq\Gamma$. Choose $a\notin W$ and write

$$
f=w+ba,
\qquad
B_W=\operatorname{supp}b=\{e:f(e)\notin W\}.
$$

Let

$$
G_W=G-B_W.
$$

For each outside colour $c\in\Gamma\setminus W$, put

$$
M_c=\{e:f(e)=c\}.
$$

Each $M_c$ is a matching. If $K$ is a component of $G_W$, define

$$
n_c(K)=|M_c\cap\delta_G(K)|\pmod2.
$$

The four outside-colour parities are equal; denote their common value by $\chi_W(K)$.

### Theorem 4.1 — fixed-$(f,W)$ criterion

For the fixed pair $(f,W)$, the following are equivalent:

1. a global five-coordinate affine slice above $(f,W)$;
2. an even support $D$ with
   $$
   B_W\cap D=M_a;
   $$
3. even $M_a$-endpoint parity in every component of $G_W$;
4. $n_a(K)=0$ for every component;
5. $n_c(K)=0$ for every outside colour and every component;
6. Eulerian outside-colour classes after contracting the components of $G_W$;
7. vanishing of the local affine component obstruction.

These are equivalent presentations of one fixed-data obstruction.

## 5. Fixed flow and graph-level quantifiers

For fixed $f$, define

$$
\mathfrak O_f(W)=\{K\in\pi_0(G_W):\chi_W(K)=1\}.
$$

### Theorem 5.1 — fixed-flow factorable criterion

The prescribed Fano flow $f$ admits a globally point-index-factorable five-coordinate lift if and only if

$$
\exists W\leq\Gamma,
\qquad
\dim W=2,
\qquad
\mathfrak O_f(W)=\varnothing.
$$

This may fail for one fixed flow. A finite fixed-flow obstruction is not a graph-level counterexample because another Fano flow may succeed.

### Theorem 5.2 — graph-level existential form

$G$ has an indexed five-support even double cover if and only if there exist a nowhere-zero Fano flow $f$ and a plane $W$ such that

$$
\mathfrak O_f(W)=\varnothing.
$$

The existential quantifier on $f$ is load-bearing.

## 6. Relation to the full fixed-lift surface object

The fixed-flow criterion above concerns one global five-point subset of the point-index torsor. It is therefore a **global-index-factorable** route.

A fixed compatible root lift $g$ has a finer object: its individual support-cycle face components form the vertices of the full dual triangulation $T_g$. A map

$$
T_g^{(1)}\to\mathscr A_5
$$

may relabel different components carrying the same old support index independently. This is strictly more general than one global point-index slice for the same fixed data.

At graph level, any successful fixed-lift route gives a five-support cover, which can then be re-encoded by some existential Fano-flow/plane presentation. That presentation need not be the original fixed flow or lift.

See [`b1-object-quantifier-and-scope.md`](b1-object-quantifier-and-scope.md) and [`surfaces-and-halfcube.md`](surfaces-and-halfcube.md).

## 7. Strong sufficient templates

Several useful routes sit inside the exact criteria.

- If all values of $f$ lie in one plane $W$, then the profile is empty. This is the nowhere-zero $\mathbf F_2^2$ or Tait sector.
- If the contracted outside-colour classes are Eulerian, the fixed-plane criterion holds.
- Unused root-label patterns and affine-plane residue tests can give factorable compression.

These are sufficient templates. They are not a replacement for the full fixed-lift surface criterion.

## 8. Boundary with Programme B2

Programme B1 closes:

- five supports $\leftrightarrow$ root flow $\leftrightarrow$ $K_5$ triangles;
- exact matching/four-flow data;
- fixed-flow/fixed-plane component parity;
- the graph-level existential Fano-flow/plane form.

It does **not** yet promote all cographic, quadratic, Schur, singular, orthogonal, or Fourier/stress presentations into one unconditional equivalence package. Programme B2 must classify each of those arrows as a full witness equivalence, fixed-data equivalence, quotient with lost lift data, dual obstruction, or evidence.

## 9. Reliability boundary

The B1 statements above are complete authorial proofs at the immutable checkpoint

`778b09ac8260192e022f512f24cdef1d04871f37`.

They are not independently audited or end-to-end Lean verified. Exact finite fixed-flow certificates remain finite evidence in their stated scope. The global five-support theorem remains open. No manuscript, publication, release, arXiv, DOI, or priority status is created by curation.
