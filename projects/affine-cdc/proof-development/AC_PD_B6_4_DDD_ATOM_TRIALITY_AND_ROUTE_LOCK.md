# AC-PD-B6.4 — DDD atom triality and unique route-lock

**Proof-development state:** `COMPLETE-DRAFT / ORIGIN-SCOPE-SEPARATED`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Validated sources:** `FIVE_CDC_DDD_ATOM_RESOLUTION_TRIALITY_V1.md` and `FIVE_CDC_ATOM_ROUTE_LOCK_CURVATURE_V1.md`  
**Depends on:** B2.1 root/co-root geometry; B5 four-terminal routing  
**Immediate consumers:** B7 route-lock rank and curvature analysis  
**External mathematical inputs:** none

## 0. Scope separation

The local atom theorems below are unconditional once a nondegenerate co-root atom is supplied. They do not depend on the invalid nontrivial defect-minimal-forest conclusion corrected in B6.3.

What remains conditional is the assertion that such an atom necessarily occurs as a leaf-to-leaf component of one canonical BBD residual forest.

## 1. Co-root atom

Fix $i\in[5]$ and put

$$
q_i=\mathbf1+\varepsilon_i.
$$

Let

$$
Q=[5]\setminus\{i\}.
$$

Choose two distinct perfect matchings $M_0,M_1$ of $K_Q$. Form a two-vertex four-pole whose internal edge has label $q_i$ and whose two terminal roots at the two endpoints are the two edges of $M_0$ and $M_1$ respectively.

Each terminal pair sums to $q_i$, so cubic conservation holds. The atom is nondegenerate exactly when $M_0\ne M_1$.

## 2. DDD state bijection

Let $M_*$ be the third perfect matching of $K_Q$, say

$$
M_*=\{X,Y\}.
$$

Then

$$
F_*(A)=\{\infty i,X,Y\}
$$

is a perfect matching of $K_6$.

### Theorem 2.1 — atom/state bijection

The map

$$
A(i;M_0,M_1)\longmapsto F_*(A)
$$

is an $S_5$-equivariant bijection between the fifteen unordered nondegenerate co-root atoms and the fifteen one-factors of $K_6$.

### Proof

For each $i$, an unordered pair of distinct matchings among the three matchings of $K_Q$ is uniquely determined by the omitted matching. There are $5\cdot3=15$ choices. The inverse recovers $i$ and $M_*$ from the unique co-root edge $\infty i$ in the one-factor. $\square$

The stabilizer is the one-factor stabilizer

$$
\operatorname{Stab}_{S_5}(A)\cong D_8.
$$

## 3. Resolution triality

Relabel $Q=\{a,b,c,d\}$ so that

$$
M_0=\{ab,cd\},
\qquad
M_1=\{ac,bd\},
\qquad
M_*=\{ad,bc\}.
$$

The four terminal roots form the four-cycle complementary to $M_*$. They admit three terminal pairings.

### Theorem 3.1 — three resolutions

The three pairings force the three internal labels

$$
\boxed{q_i,\qquad ad,\qquad bc.}
$$

Equivalently, the possible internal labels are exactly the three edges of the DDD one-factor

$$
F_*(A)=\{\infty i,ad,bc\}.
$$

### Proof

For the original pairing, both endpoint sums are the complement vector $q_i$. For the two crossed pairings,

$$
ab+bd=ac+cd=ad,
$$

and

$$
ab+ac=cd+bd=bc.
$$

$\square$

Thus the original route gives the co-root realization; the two crossed routes give the two root-valued local resolutions.

Changing the terminal pairing is not automatically a valid replacement in the ambient graph. A composition/gluing theorem is still required.

## 4. Ordered route-lock state

Let the terminal roots be

$$
\ell=(\ell_1,\ell_2,\ell_3,\ell_4)\in R_5^4,
\qquad
\sum_j\ell_j=0,
$$

and fix the current pairing

$$
P_0=12\mid34.
$$

Put

$$
d=\ell_1+\ell_2=\ell_3+\ell_4.
$$

The state is bad when $d$ is zero or a co-root. A root $a$ is a full challenge when every $\ell_j+a$ is again a root.

## 5. Unique bad route

### Theorem 5.1

For every bad ordered state and full challenge $a$, the three routes produce internal sums

$$
\begin{array}{c|c}
12\mid34&d,\\
13\mid24&d+a,\\
14\mid23&d+a.
\end{array}
$$

Moreover $d+a$ is always a root. Hence the original pairing is the unique route that remains bad.

### Proof

A switch routed within one block adds $a$ to either zero or two roots in that block and leaves its sum unchanged. A crossed route toggles exactly one root in each old block and changes the internal sum by $a$.

If $d=0$, then $d+a=a$ is a root. If $d$ is a co-root, fullness gives

$$
\langle d,a\rangle
=
\langle\ell_1,a\rangle+
\langle\ell_2,a\rangle
=0.
$$

A two-subset cannot be disjoint from the four-point support of $d$, so it lies inside that support. Removing it from the co-root leaves a two-subset, hence a root. $\square$

### Corollary 5.2 — physical dichotomy

For a physical atom:

1. if some full challenge takes a crossed route, the internal label becomes root-valued locally;
2. if the atom survives every full challenge, every full challenge is routed by the original pairing.

The first case is a root-resolution candidate, not yet a global replacement theorem.

## 6. Finite lock fibres

The exact ordered-state classification has:

- 640 total root quadruples of sum zero;
- 280 bad states;
- 180 co-root-defect states.

For fixed co-root defect and fixed ordered right pair, the six possible left pairs form a $K_{2,4}$ lock fibre. Allowing both left and right switches glues these into five 36-state components, one for each co-root defect.

These counts and graph identifications are exact finite classification data.

## 7. Challenge quotient

At a repeated-matching $C$ state in one co-root fibre, let

$$
\mathcal A=\{a_1,a_2,a_3,a_4\}
$$

be the four full challenges and define

$$
\chi:E_5\to\mathbf F_2^4,
\qquad
\chi(x)=(\langle x,a_1\rangle,\ldots,\langle x,a_4\rangle).
$$

Exact finite root-image classification gives

$$
\ker\chi=\langle q\rangle
$$

for the co-root defect $q$, and

$$
\chi(R_5)=E_4\setminus\{0\},
\qquad
E_4=\{u\in\mathbf F_2^4:\sum_j u_j=0\}.
$$

Every terminal root maps to

$$
g=1111.
$$

### Proposition 7.1 — locked quotient

Universal route-lock on the opposite four-pole induces a nowhere-zero flow

$$
c:E(Q)\to E_4\setminus\{0\}\cong\mathbf F_2^3\setminus\{0\}
$$

with all four terminal values equal to $g$, and the four coordinate even subgraphs all route the terminals by the same pairing $12\mid34$.

The finite statements about $\chi$ are certificate inputs; once accepted, the flow and routing conclusion is immediate.

## 8. What route-lock does not imply

Universal route-lock does not force a graph two-edge separator. Exact rank-two examples have minimum pair-separating cut four. The residual object is a low-rank flow with coordinated scalar-sheet routing, not an ordinary cut.

Nor does route-lock itself prove that one crossed atom resolution transfers to the original graph: terminal incidence changes and must be handled by a four-pole composition theorem.

## 9. Transition to curvature

For the locked quotient $c$, the remaining cases are:

1. rank at most two;
2. full rank with zero quadratic transition curvature;
3. full rank with nonzero curvature.

The rank-two Tait escape and the full-rank curvature/common-cut dichotomy belong to B7. B6 exports the precise locked quotient but does not pre-empt those theorems.

## 10. Assurance boundary

The atom/state bijection, resolution triality, and unique-bad-route theorem are elementary theorem-level results. The ordered census, $K_{2,4}$ fibres, challenge quotient, and finite root-image table remain exact finite certificate data. The existence of an atom as a canonical BBD residual component is conditional on the corrected B6.3 gap.

## 11. Completion assessment

`AC-PD-B6.4` is `COMPLETE-DRAFT / ORIGIN-SCOPE-SEPARATED`. It supplies the independent DDD atom interface passed to B7.