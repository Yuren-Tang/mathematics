# AC-PD-B2 — formulation and witness hierarchy

**Proof-development state:** `READY-FOR-CURATOR / MATHEMATICAL-CORRECTION`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Constituent units:** B2.1–B2.4  
**External mathematical inputs:** none  
**Assurance:** complete authorial proofs for the stated equivalences and correction; not independent audit and not formal verification

## 0. Purpose

Programme B2 classifies the singular, quadratic, Schur, cographic, orthogonal, stress, and Fourier descriptions by the amount of witness data they retain. It also withdraws a false universal $2r$-dimensional orthogonal-root theorem and replaces it with a sharp dimension bound and the correct deleted permutation module.

The central rule is:

> two formulations belong in one equivalence box only when their fixed data and reconstruction maps are explicit.

A quotient residue, boundary word, dual annihilator, or Fourier spectrum may decide a fixed solvability problem without itself being a graph-level five-support witness.

## 1. Complete graph-level witness equivalences

For a finite loopless cubic multigraph $G$, the following are equivalent.

1. An indexed five-support even double cover.
2. An $R_5$-valued flow in
   $$
   H_5=\left\{z\in\mathbf F_2^5:\sum_i z_i=0\right\}.
   $$
3. A $K_5$-triangle edge labelling.
4. An anisotropic flow in the minus-type four-space $(H_5,q_5)$, where
   $$
   q_5(z)=\sum_{i<j}z_iz_j.
   $$
5. A quadruple of cycle words
   $$
   b,d,x,y\in\mathcal C(G)
   $$
   satisfying
   $$
   b*d=(\mathbf1+x)*(\mathbf1+y).
   $$
6. A cycle-continuous edge map
   $$
   M(G)\longrightarrow M^*(K_5),
   $$
   meaning an arbitrary ground-set map whose inverse image sends every target binary cycle, equivalently every cut of $K_5$, to a source binary cycle.

The reconstruction maps are explicit:

- supports are the five coordinate words;
- anisotropic values are exactly the weight-two roots;
- the coordinate isomorphism is
  $$
  \Phi(b,d,x,y)
  =(b,d,b+d+y,b+d+x,b+d+x+y);
  $$
- the cographic edge map records the unordered pair of support indices containing each source edge.

Thus the full witness box is

$$
\boxed{
\text{five supports}
\Longleftrightarrow
R_5\text{-flow}
\Longleftrightarrow
K_5\text{ triangles}
\Longleftrightarrow
O^-(4,2)\text{ anisotropic flow}
\Longleftrightarrow
\text{quadratic cycle solution}
\Longleftrightarrow
M(G)\to M^*(K_5)\text{ cycle-continuous}.}
$$

No injectivity, strong-map, quotient, or matroid-embedding property is included in the last formulation.

## 2. Fixed singular-quotient solvability equivalences

Let $(H,q)$ be a four-dimensional minus-type quadratic space, let $0\ne k\in H$ be singular, and put

$$
\Gamma=H/\langle k\rangle,
\qquad
W_k=k^\perp/\langle k\rangle.
$$

Fix a nowhere-zero Fano flow $f:E(G)\to\Gamma\setminus\{0\}$. Then the following are equivalent.

1. $f$ admits an anisotropic $H$-flow lift.
2. The component sums of the kernel-line lift defects vanish on every component of the plane subgraph $G_{W_k}$.
3. The corresponding fixed-plane forbidden-three-colour obstruction vanishes.
4. In coordinates $f=(b,x,y)$, there exists a cycle word $d$ satisfying
   $$
   b*d=(\mathbf1+x)*(\mathbf1+y).
   $$
5. After contracting the $b=0$ components, the Schur word satisfies
   $$
   x*y\in\mathcal C(Q_b).
   $$

When nonempty, the anisotropic lift set is a torsor under

$$
\mathcal C(G_{W_k}),
$$

and the coordinate $d$-solution set is the same torsor written in one chart.

These are complete **fixed-data** equivalences only when the quotient flow, singular kernel line or plane, contracted quotient, and lift torsor are retained. The Schur boundary word alone is an obstruction projection, not a five-support witness.

## 3. One obstruction in four resolutions

For one fixed singular quotient, the following componentwise bits are identical.

1. The sum of vertex lift defects in the kernel line.
2. The forbidden-three-colour local-family obstruction.
3. The parity of one, hence every, outside colour on the plane-component cut.
4. The quotient boundary of the Schur product $x*y$.

Accordingly, singular, fixed-plane, and Schur arguments are not separate barriers. They are invariant, local, and eliminated-coordinate resolutions of one incidence obstruction.

## 4. Stress duality

For the quotient differential

$$
\delta_f:\Gamma^{V(G)}\to\bigoplus_eQ_e,
$$

its transpose is the equilibrium-stress divergence operator

$$
(\delta_f^*\psi)_v=\sum_{e\ni v}\psi_e.
$$

For any selected vertex or fibre evaluation map, the orthogonal complement of its attainable image is exactly the space of relative stresses whose divergence is supported on the selected interface.

### Exact linear statement

A prescribed target vector is attainable if and only if every relative stress annihilates its displacement from the base lift. This is a complete Fredholm alternative. When attainable, a primal preimage reconstructs the translated lift.

### Witness boundary

The stress space by itself records linear dependencies. It does not specify the base flow, base lift, target vector, or primal preimage and is therefore not a graph-level five-support witness.

## 5. Fourier duality

For a fibre-evaluation code $\mathcal C_F\leq Q_F$ and an allowed set $A\subseteq Q_F$,

$$
|\mathcal C_F\cap A|
=
\frac{|\mathcal C_F|}{|Q_F|}
\sum_{y\in\mathcal C_F^\perp}
\widehat{\mathbf1_A}(y).
$$

The nonzero frequencies are precisely relative stresses. The zero frequency is the exact uniform main term; it is not an independence assumption.

This formula is an exact existence/counting criterion for a fixed orbit:

$$
\mathcal C_F\cap A\ne\varnothing
\quad\Longleftrightarrow\quad
|\mathcal C_F\cap A|>0.
$$

If the count is zero, the complete spectrum gives a structured cancellation identity. A single separating stress need not exist for a nonlinear product set. A positive count is an existence proof, but a full witness still requires one codeword, one primal preimage, the fixed base lift, and root/support reconstruction.

Thus Fourier duality is a complete dual count, not an independent constructive equivalence.

## 6. Orthogonal correction

### False claim withdrawn

The recovered universal packet asserts that all unordered pairs of the $2^r$ points of $\mathbf F_2^r$ admit an additive anisotropic-root model in a canonical quadratic space of dimension $2r$. The displayed formula is not type-correct, and the theorem is impossible for every $r\geq4$.

### Sharp lower bound

For any even set $I$ of cardinality $q$, suppose roots $r_{ab}$ satisfy

$$
Q(r_{ab})=1,
\qquad
r_{ab}+r_{bc}+r_{ca}=0.
$$

Fixing a base point gives $r_{ab}=p_a+p_b$. The Gram matrix of the $q-1$ vectors $p_a$ is $J+I$, of rank $q-2$. Hence

$$
\boxed{\dim V\geq q-2.}
$$

For $q=2^r$, the proposed dimension $2r$ fails from $r=4$ onward.

### Correct universal module

The deleted permutation module

$$
\overline E_I
=
\left\{z\in\mathbf F_2^I:\sum_i z_i=0\right\}
\big/
\langle\mathbf1_I\rangle
$$

has dimension $q-2$ and quadratic form

$$
q_I([z])=\frac{\operatorname{wt}(z)}2\pmod2.
$$

The roots

$$
[\varepsilon_a+\varepsilon_b]
$$

are anisotropic and satisfy every triangle relation. This attains the lower bound.

### Exceptional dimensions

- Five supports use the four-dimensional minus space $O^-(4,2)$.
- Eight supports use the six-dimensional plus space $O^+(6,2)$ because
  $$
  8-2=6=2\cdot3.
  $$
- The eight-support realization is exceptional; it is not the first case of a universal $O^+(2r,2)$ tower.

The false universal theorem must be superseded in the active corpus. Any higher-rank small-dimensional analogue is a new research question, not an inherited theorem.

## 7. Exact classification table

| Formulation | Scope | Retains full witness? | Reconstruction requirement |
|---|---|---:|---|
| five indexed supports | graph-level | yes | none |
| $R_5$ root flow / $K_5$ triangles | graph-level | yes | coordinate supports |
| anisotropic $O^-(4,2)$ flow | graph-level | yes | identify anisotropic roots with support pairs |
| quadratic equation $(b,d,x,y)$ | graph-level | yes | apply $\Phi$ |
| cographic cycle-continuous edge map | graph-level | yes | target-star preimages |
| singular quotient | fixed flow and kernel line | no, until lifted | solve incidence equation and retain torsor |
| Schur quotient | fixed coordinate quotient | no, until lifted | solve for $d$ |
| component obstruction | fixed quotient | no | incidence/$T$-join solve |
| relative stress space | fixed evaluation map | no | primal target and preimage |
| Fourier spectrum/count | fixed orbit and allowed set | existence/count only | exhibit codeword and preimage |
| deleted permutation root module | universal target model | target data, not source witness | choose root-valued source flow |

## 8. Required corpus changes

Before B2 promotion, the Curator should:

1. make the full-witness versus fixed-data/dual distinction explicit;
2. present anisotropic flow as the mother object, singular quotient and Schur product as projections, and stress/Fourier as dual criteria;
3. use “cycle-continuous edge map” with a definition rather than unqualified “matroid map”;
4. remove or mark false the universal $\Gamma\oplus\Gamma^*$ / $2r$ theorem;
5. insert the $q-2$ lower bound and deleted permutation module;
6. mark rank three/eight supports as exceptional;
7. re-audit any later packet whose proof cites the false hierarchy;
8. preserve finite weight enumerators and cancellation tables as evidence, not universal estimates.

## 9. Remaining frontier

B2 does not prove that every bridgeless cubic graph has an anisotropic $O^-(4,2)$ flow. It supplies exact equivalent witnesses, fixed-data lift criteria, and dual obstruction languages.

The global unresolved step remains a source theorem guaranteeing successful data or eliminating all obstructions. That is downstream B3–B9 work, not hidden inside the formulation equivalences.

## 10. Completion assessment

`AC-PD-B2` is `READY-FOR-CURATOR / MATHEMATICAL-CORRECTION`. Programme B3 becomes active: normalize the dual triangulation, full dual versus quotient targets, half-cube links, marked-core decompositions, and target-capacity theorems, using the corrected orthogonal modules and exact fixed-lift scope.