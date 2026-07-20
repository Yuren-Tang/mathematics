# Root-valued flows and the five-support lifting problem

## 1. The five-support object

Let $G$ be a finite loopless cubic multigraph. An indexed five-support even double cover is a five-tuple

$$
(F_1,\ldots,F_5)
$$

of vertex-even edge supports such that every source edge belongs to exactly two indexed supports. Empty supports and equal support values at different indices are allowed.

Put

$$
H_5=E_5=\left\{x\in\mathbf F_2^5:\sum_i x_i=0\right\},
\qquad
R_5=\{\varepsilon_i+\varepsilon_j:i<j\}.
$$

### Theorem 1.1 — root, triangle, and anisotropic equivalence

The following are canonically equivalent:

1. indexed five-support even double covers;
2. root-valued flows $E(G)\to R_5$;
3. $K_5$-triangle edge labellings;
4. anisotropic flows in the minus-type quadratic space $(H_5,q_5)$, where
   $$
   q_5(x)=\sum_{i<j}x_ix_j.
   $$

The anisotropic vectors of $H_5$ are exactly its ten weight-two roots.

## 2. Relation to the rank-three AffineCDC theorem

A nowhere-zero Fano flow

$$
f:E(G)\to\mathbf F_2^3\setminus\{0\}
$$

has a compatible eight-index affine root lift by Programme A. The eight-support complete-root model is the exceptional plus-type six-space $O^+(6,2)$.

The five-support strengthening asks whether the graph has an anisotropic root flow in $O^-(4,2)$. It is not a request to delete three supports from one prescribed eight-support lift. At graph level the Fano flow, compatible lift, embedding, and support identification may all vary.

The eight-to-five problem is a specific exceptional reduction

$$
O^+(6,2)\rightsquigarrow O^-(4,2),
$$

not the first step of a universal $O^+(2r,2)$ hierarchy.

## 3. Exact matching/four-flow formulation

A fixed support-coordinate inverse image is an even support. A fixed root-label inverse image is a matching.

An exact matching/four-flow datum consists of:

1. even supports $B,D$;
2. a matching $M=B\cap D$;
3. a nowhere-zero $\mathbf F_2^2$-flow on $G-M$.

### Theorem 3.1

$G$ has an indexed five-support even double cover if and only if it has exact data $(B,D,M,w)$.

Equivalently, replace $D$ by even $M$-endpoint parity in every component of $G-B$:

$$
|M\cap\delta_G(K)|\equiv0\pmod2.
$$

Bare matching plus four-flow is insufficient.

## 4. Complete quadratic witness

Define the linear isomorphism

$$
\Phi(b,d,x,y)
=(b,d,b+d+y,b+d+x,b+d+x+y)
$$

from $\mathbf F_2^4$ to $H_5$. Direct expansion gives

$$
q_5(\Phi(b,d,x,y))=bd+x+y+xy.
$$

### Theorem 4.1 — quadratic cycle equation

$G$ has five indexed even supports if and only if there are cycle words

$$
b,d,x,y\in\mathcal C(G)
$$

such that

$$
\boxed{b*d=(\mathbf1+x)*(\mathbf1+y).}
$$

The five supports are the five coordinate words of $\Phi(b,d,x,y)$. This is a complete graph-level witness, not merely an obstruction equation.

## 5. Exact cographic formulation

A cycle-continuous edge map in this corpus is a function

$$
\phi:E(G)\to E(K_5)
$$

such that the inverse image of every cut of $K_5$, equivalently every binary cycle of $M^*(K_5)$, is a binary cycle of $G$.

### Theorem 5.1

Five indexed even supports are equivalent to such a cycle-continuous edge map.

- the target label of a source edge is the pair of support indices containing it;
- the support $F_i$ is the inverse image of the target star $\delta_{K_5}(i)$.

No strong-map, quotient, embedding, injectivity, or surjectivity property is implied.

## 6. Fixed Fano flow and plane

Fix a nowhere-zero Fano flow $f$ and a plane $W$. Let $G_W$ be the subgraph of $W$-valued edges. For each component $K$ of $G_W$, the four outside-colour cut parities are equal; denote the common bit by $\chi_W(K)$.

For fixed $(f,W)$, the following are equivalent:

1. a global five-coordinate affine slice;
2. the distinguished even support;
3. the matching endpoint $T$-join condition;
4. vanishing of one or all outside-colour cut parities;
5. Eulerian outside-colour classes after contraction;
6. vanishing of the local affine component obstruction.

For fixed $f$, factorable success means

$$
\exists W,\qquad \mathfrak O_f(W)=\varnothing.
$$

A prescribed flow may fail without the graph failing.

## 7. Singular-line and Schur resolution

Let $(H,q)$ be a four-dimensional minus-type space, let $k$ be a nonzero singular vector, and fix a quotient Fano flow in

$$
\Gamma=H/\langle k\rangle.
$$

The following are equivalent for the retained fixed data:

1. an anisotropic $H$-flow lift;
2. vanishing component sums of the kernel-line lift defect;
3. the fixed-plane colour-cut condition;
4. existence of the eliminated cycle word $d$;
5. after contracting the $b=0$ components,
   $$
   x*y\in\mathcal C(Q_b).
   $$

When nonempty, the lift set is a torsor under the cycle space of the plane subgraph.

The Schur boundary word alone is not a five-support witness. The quotient flow, kernel or plane, quotient graph, and a primal solution must remain recoverable.

## 8. Stress and Fourier scope

Relative stresses are the dual linear dependencies of a selected fibre-evaluation code. They give an exact Fredholm criterion for a prescribed target.

For an allowed set $A$ in a fixed evaluation space,

$$
|\mathcal C_F\cap A|
=
\frac{|\mathcal C_F|}{|Q_F|}
\sum_{y\in\mathcal C_F^\perp}\widehat{\mathbf1_A}(y).
$$

A positive count proves existence in the fixed orbit, but a full witness still requires a codeword and primal preimage. A zero count gives aggregate spectral cancellation and need not produce one separating stress.

## 9. Correction of the universal root module

The retired packet `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md` claimed a canonical $2r$-dimensional model for the complete graph on $2^r$ support points. The claim is false for every $r\ge4$, and its displayed evaluation formula is type-invalid without a chosen self-duality.

For any even set $I$ of cardinality $q$, additive anisotropic roots satisfying the triangle law require

$$
\boxed{\dim V\ge q-2.}
$$

The correct universal module is

$$
\overline E_I
=
\left\{z\in\mathbf F_2^I:\sum_i z_i=0\right\}/\langle\mathbf1_I\rangle,
$$

with quadratic form $q_I([z])=\operatorname{wt}(z)/2\pmod2$ and roots $[\varepsilon_a+\varepsilon_b]$.

For eight supports, $q-2=6=2\cdot3$, giving the exceptional $O^+(6,2)$ model. There is no universal $O^+(2r,2)$ tower.

## 10. Relation to the full fixed-lift surface object

A fixed compatible root lift $g$ has the full dual triangulation $T_g$. A map

$$
T_g^{(1)}\to\mathscr A_5
$$

classifies componentwise compression of that same embedding. It is more general than one global point-index slice for the same fixed data.

An external root flow integrates on a prescribed dual only when all dual-cycle holonomies vanish. The old-colour quotient $J_g$ classifies only fibre-constant factorable maps.

## 11. Reliability boundary

The exact B1 and B2 authorial dossiers are retained under `proof-development/`. Programme B2 is complete for the stated witness hierarchy and orthogonal correction.

It is not independently audited or end-to-end Lean verified. The global five-support theorem remains open. No manuscript, publication, release, arXiv, DOI, novelty, or priority status is created by curation.
