# Programme B2 — formulation and witness hierarchy

## 1. Scope

Let $G$ be a finite loopless cubic multigraph. Programme B2 classifies the anisotropic, singular, quadratic, Schur, cographic, stress, and Fourier descriptions of five-support data by the amount of witness information they retain.

The controlling rule is:

> Two formulations belong in one equivalence box only when their fixed data and reconstruction maps are explicit.

The global five-support theorem remains open. This chapter identifies equivalent witnesses and exact fixed-data criteria; it does not prove that every bridgeless cubic graph possesses such a witness.

## 2. The five-support mother space

Put

$$
H_5=\left\{z\in\mathbf F_2^5:\sum_{i=1}^5z_i=0\right\}
$$

and

$$
q_5(z)=\sum_{1\le i<j\le5}z_iz_j.
$$

The polar form is the standard dot product restricted to $H_5$. The space is nondegenerate, four-dimensional, and of minus type. Its anisotropic vectors are exactly the ten weight-two roots

$$
R_5=\{\varepsilon_i+\varepsilon_j:i<j\}.
$$

Thus an anisotropic $H_5$-flow is exactly an $R_5$-valued flow.

## 3. Complete graph-level witness equivalences

The following are canonically equivalent.

1. An indexed five-support even double cover $(F_i)_{i\in[5]}$.
2. An $R_5$-valued flow.
3. A $K_5$-triangle edge labelling.
4. An anisotropic flow in $(H_5,q_5)\cong O^-(4,2)$.
5. Cycle words $b,d,x,y\in\mathcal C(G)$ satisfying
   $$
   \boxed{b*d=(\mathbf1+x)*(\mathbf1+y).}
   $$
6. A cycle-continuous edge map
   $$
   \phi:E(G)\longrightarrow E(K_5)
   $$
   whose inverse image sends every cut of $K_5$, equivalently every binary cycle of $M^*(K_5)$, to a binary cycle of $G$.

The explicit coordinate isomorphism is

$$
\Phi(b,d,x,y)=(b,d,b+d+y,b+d+x,b+d+x+y).
$$

The five support words are the five coordinates of $\Phi(b,d,x,y)$. The quadratic equation says edgewise that the resulting word has weight two.

For the cographic formulation, the target edge $\{i,j\}$ records the two support indices containing the source edge. The support $F_i$ is the inverse image of the star $\delta_{K_5}(i)$. No injectivity, surjectivity, strong-map, weak-map, matroid quotient, or embedding property is implied by “cycle-continuous edge map”.

## 4. Fixed singular-quotient data

Let $(H,q)$ be a four-dimensional minus-type quadratic space, choose a nonzero singular vector $k$, and put

$$
\Gamma=H/\langle k\rangle,
\qquad
W_k=k^\perp/\langle k\rangle.
$$

Fix a nowhere-zero Fano flow $f:E(G)\to\Gamma\setminus\{0\}$. Every class in $W_k\setminus\{0\}$ has two anisotropic lifts differing by $k$; every class outside $W_k$ has one anisotropic lift. Choosing preliminary lifts produces a vertex defect word $\eta$. Changing a lift on a $W_k$-edge adds $k$ at both endpoints.

Therefore the following are equivalent for the fixed quotient data.

1. $f$ admits an anisotropic $H$-flow lift.
2. The kernel-line defect has even sum on every component of the $W_k$-valued subgraph.
3. The B1 fixed-plane component obstruction vanishes.
4. In coordinates $f=(b,x,y)$ there exists a cycle word $d$ satisfying the quadratic equation.
5. After contracting the $b=0$ components,
   $$
   x*y\in\mathcal C(Q_b).
   $$

When nonempty, the lift set is a torsor under the cycle space of the plane subgraph. These are complete fixed-data equivalences only while the quotient flow, singular line or plane, quotient graph, and lift torsor remain named.

A Schur boundary word by itself does not reconstruct a five-support witness.

## 5. One obstruction in four resolutions

For one fixed singular quotient, the following componentwise bits coincide:

1. the sum of kernel-line vertex defects;
2. the forbidden-three-colour affine obstruction;
3. the parity of one, hence all, outside colours on the component cut;
4. the quotient boundary of $x*y$.

The singular, fixed-plane, colour-cut, and Schur descriptions are therefore resolutions of one obstruction, not four independent barriers.

## 6. Exact stress duality

For the quotient differential

$$
\delta_f:\Gamma^{V(G)}\to\bigoplus_{e\in E(G)}Q_e,
$$

its transpose is the equilibrium-stress divergence operator

$$
(\delta_f^*\psi)_v=\sum_{e\ni v}\psi_e.
$$

For a selected fibre evaluation map $\rho_F$ with image code $\mathcal C_F$, the dual code $\mathcal C_F^\perp$ consists exactly of the corresponding relative stresses.

A prescribed target fibre vector $t$ occurs in the fixed lift orbit if and only if

$$
t-q_F(g)\in\mathcal C_F,
$$

if and only if every relative stress annihilates its displacement. This is an exact Fredholm alternative. When the criterion holds, one still needs a primal preimage under $\rho_F$ to reconstruct the translated lift. Relative stresses are dual dependencies, not source witnesses.

## 7. Exact Fourier count

For an allowed set $A\subseteq Q_F$,

$$
|\mathcal C_F\cap A|
=
\frac{|\mathcal C_F|}{|Q_F|}
\sum_{y\in\mathcal C_F^\perp}\widehat{\mathbf1_A}(y).
$$

The nonzero frequencies are relative stresses. The zero frequency is the exact uniform main term; it is not a probabilistic independence assumption.

A positive count proves existence in the fixed affine orbit. An explicit witness still requires a codeword, a primal preimage, the translated lift, and B1 root-flow/support reconstruction. A zero count gives an aggregate Fourier cancellation identity and need not yield one separating stress for a nonlinear product set. Finite weight enumerators and cancellation tables remain exact finite evidence unless a uniform theorem is separately proved.

## 8. Orthogonal source fidelity and mathematical correction

### 8.1 Exact historical packet

The recovered packet

`FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`

at blob `2043ada9d28789ecc5f4f0028e62133f37835bc1` is a valid theorem-level historical source in the following exact scope:

- the eight-coordinate even-weight module $H_8$;
- the Hamming kernel and moment map;
- the six-dimensional plus-type quotient $O^+(6,2)$;
- its twenty-eight anisotropic roots;
- rank-three AffineCDC root lifts;
- five-coordinate $O^-(4,2)$ slices and omitted-triple orthogonality.

It fixes the rank-three/eight-support setting. It contains no arbitrary-rank $\Gamma\oplus\Gamma^*$ construction, no formula $d_h(a)=([a],\operatorname{ev}_a)$, and no universal $O^+(2r,2)$ tower.

### 8.2 Separate unreconstructed extrapolation

The alleged arbitrary-rank tower is classified separately as

`SOURCE-UNRECONSTRUCTED / INFERRED-EXTRAPOLATION OR UNCOMMITTED DRAFT / MATHEMATICALLY REFUTED BY B2.3`.

It is not one of the seventy-eight recovered packets and receives no packet assurance class. The displayed formula is not canonically type-correct: $a\in\Gamma$ canonically gives an element of $\Gamma^{**}$, not of $\Gamma^*$, absent an additional chosen self-duality.

### 8.3 Sharp lower bound

Let $I$ have even cardinality $q$, and suppose roots $r_{ab}$ in a quadratic space satisfy

$$
Q(r_{ab})=1,
\qquad
r_{ab}+r_{bc}+r_{ca}=0.
$$

Fixing a base point gives potentials $p_a$ with $r_{ab}=p_a+p_b$. The Gram matrix of the $q-1$ nonbase potentials is $J+I$, whose rank over $\mathbf F_2$ is $q-2$. Hence

$$
\boxed{\dim V\ge q-2.}
$$

For $q=2^r$, dimension $2r$ is impossible from $r=4$ onward.

### 8.4 Correct universal module and exceptional dimensions

The correct universal additive root module is

$$
\overline E_I=
\left\{z\in\mathbf F_2^I:\sum_i z_i=0\right\}/\langle\mathbf1_I\rangle,
$$

of dimension $q-2$, with

$$
q_I([z])=\frac{\operatorname{wt}(z)}2\pmod2.
$$

The roots $[\varepsilon_a+\varepsilon_b]$ are anisotropic, satisfy every triangle relation, span the module, and attain the lower bound.

- Five supports use the four-dimensional minus space $O^-(4,2)$.
- Eight supports use the six-dimensional plus space $O^+(6,2)$ because $8-2=6=2\cdot3$.
- Rank three is exceptional; the valid packet is not the first member of a universal $O^+(2r,2)$ tower.

The genuine all-rank transgression/residue hierarchy remains valid and distinct. It does not imply a complete-root $2r$ tower.

## 9. Classification table

| Formulation | Scope | Full source witness? | Reconstruction requirement |
|---|---|---:|---|
| five indexed supports | graph level | yes | none |
| $R_5$ flow / $K_5$ triangles | graph level | yes | coordinate supports |
| anisotropic $O^-(4,2)$ flow | graph level | yes | identify anisotropic roots |
| quadratic cycle solution | graph level | yes | apply $\Phi$ |
| cographic cycle-continuous edge map | graph level | yes | target-star preimages |
| singular quotient | fixed flow and kernel line | no, until lifted | solve incidence equation and retain torsor |
| Schur quotient | fixed coordinate quotient | no, until lifted | solve for $d$ |
| component obstruction | fixed quotient | no | incidence or $T$-join solve |
| relative stress space | fixed evaluation map | no | target plus primal preimage |
| Fourier spectrum/count | fixed orbit and allowed set | existence/count only | exhibit codeword and preimage |
| deleted permutation module | universal target model | target data only | choose a root-valued source flow |

## 10. Provenance and later-programme boundary

The controlling source-fidelity repair is

`proof-development/affine-cdc-rigour-v1@9ce8de5ca5b7b41e139be4c94572de7725446046`.

Programme B2 does not consume B3 target corrections, B4 reconfiguration, B5 separator/routing, B6/B7 defect/frontier work, or B9. It does not prove the global five-support theorem. This curation preserves Programme A, B1, and B3–B8 mathematics and creates no independent-review, Lean, manuscript, publication, release, arXiv, DOI, or novelty status.