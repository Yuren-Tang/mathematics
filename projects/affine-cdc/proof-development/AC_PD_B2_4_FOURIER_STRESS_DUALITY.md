# AC-PD-B2.4 — exact stress and Fourier duality with witness scope

**Proof-development state:** `COMPLETE-DRAFT / WITNESS-SCOPE`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Recovered controlling packet:** `FIVE_CDC_ROOT_LIFT_FOURIER_STRESS_DUALITY_V1.md` at `research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`  
**Depends on:** A4 affine pair complex; B1.4 fixed-lift scope; B2.1 fixed-data lift torsors  
**Immediate consumers:** B4 gauge motion; B6 holonomy and defect duals; B8 finite certificates; B9 frontier  
**External mathematical inputs:** none

## 0. Classification

This unit separates three statements that should not be conflated.

1. **Linear prescribed-value problem.** A target vector lies in a linear evaluation image if and only if every relative stress annihilates it. This is an exact Fredholm alternative.
2. **Nonlinear product-avoidance problem.** An allowed product set meets the evaluation code if and only if an exact Fourier sum is positive. The nonzero frequencies are relative stresses, but no single stress generally decides the intersection.
3. **Full witness.** A successful codeword in the intersection, together with a preimage translation field and the fixed base lift, reconstructs the root lift. The stress space or Fourier spectrum alone does not.

Thus stress/Fourier language is a dual solvability and counting presentation of a fixed affine-lift problem, not a new graph-level five-support witness independent of the fixed flow and base lift.

## 1. The fixed affine lift torsor

Let $G$ be a finite loopless graph, let $\Gamma$ be a finite-dimensional vector space over $\mathbf F_2$, and fix a nowhere-zero flow

$$
f:E(G)\longrightarrow\Gamma\setminus\{0\}.
$$

For $e=uv$, put

$$
Q_e=\Gamma/\langle f(e)\rangle.
$$

The quotient differential is

$$
\delta_f:\Gamma^{V(G)}\longrightarrow\bigoplus_{e\in E(G)}Q_e,
\qquad
(\delta_fk)_e=[k_u+k_v]_e.
$$

Let

$$
H_f^0=\ker\delta_f.
$$

Fix one compatible root lift $g$ above $f$. Translation by $k\in H_f^0$ changes the local point parameter at every vertex while preserving the common quotient label across each edge. Thus the compatible lift orbit based at $g$ is an affine torsor under $H_f^0$ modulo any stabilizer already absorbed in the chosen root-fibre coordinate model.

The statements below concern this fixed orbit. Existence of the base lift in rank three follows from Programme A; higher-rank or constrained base-lift existence is separate.

## 2. The transpose and equilibrium stresses

The dual of $Q_e$ is canonically

$$
Q_e^*\cong\operatorname{Ann}(f(e))\leq\Gamma^*.
$$

Under this identification,

$$
\delta_f^*:
\bigoplus_e\operatorname{Ann}(f(e))
\longrightarrow(\Gamma^*)^{V(G)}
$$

is

$$
(\delta_f^*\psi)_v
=
\sum_{e\ni v}\psi_e.
$$

### Proposition 2.1

The formula above is the transpose of $\delta_f$.

### Proof

For $k\in\Gamma^{V(G)}$ and $\psi=(\psi_e)$,

$$
\begin{aligned}
\langle\psi,\delta_fk\rangle
&=\sum_{e=uv}\psi_e([k_u+k_v]_e)\\
&=\sum_v\left(\sum_{e\ni v}\psi_e\right)(k_v).
\end{aligned}
$$

Each $\psi_e$ vanishes on $f(e)$, so it is well defined on the quotient. $\square$

The kernel of $\delta_f^*$ is the equilibrium-stress space already appearing in A4. Relative stresses below allow a prescribed divergence on a selected region.

## 3. Vertex controllability

For $U\subseteq V(G)$, let

$$
r_U:H_f^0\longrightarrow\Gamma^U
$$

be restriction. For $\alpha\in(\Gamma^*)^U$, let $\widetilde\alpha$ be its zero extension to all vertices and define

$$
\operatorname{RelOb}_f(U)
=
\{\alpha:\widetilde\alpha\in\operatorname{im}\delta_f^*\}.
$$

### Theorem 3.1 — vertex Fredholm alternative

$$
\boxed{
(\operatorname{im}r_U)^\perp
=
\operatorname{RelOb}_f(U).}
$$

Consequently:

1. $r_U$ is surjective if and only if $\operatorname{RelOb}_f(U)=0$;
2. $a\in\Gamma^U$ extends to some $k\in H_f^0$ if and only if
   $$
   \alpha(a)=0
   $$
   for every $\alpha\in\operatorname{RelOb}_f(U)$;
3. the controllability defect is exact:
   $$
   \operatorname{codim}\operatorname{im}r_U
   =
   \dim\operatorname{RelOb}_f(U).
   $$

### Proof

A functional $\alpha$ annihilates $\operatorname{im}r_U$ exactly when its zero extension annihilates $\ker\delta_f$. Finite-dimensional duality gives

$$
(\ker\delta_f)^\perp
=
\operatorname{im}\delta_f^*.
$$

This proves the identity and all consequences. $\square$

Here a relative obstruction is represented by an edge-covector field whose divergence is zero outside $U$ and equals the selected source field on $U$.

## 4. Root-fibre evaluation codes

Fix $F\subseteq E(G)$. For every $e=uv\in F$, choose one endpoint $s(e)$. Define

$$
\rho_F:H_f^0\longrightarrow Q_F:=\bigoplus_{e\in F}Q_e,
\qquad
(\rho_Fk)_e=[k_{s(e)}]_e.
$$

This is independent of the endpoint choice because $k\in\ker\delta_f$ implies

$$
[k_u]_e=[k_v]_e.
$$

Put

$$
\mathcal C_F=\operatorname{im}\rho_F.
$$

For $y=(y_e)\in Q_F^*$, define $\sigma_F(y)\in(\Gamma^*)^{V(G)}$ by placing $y_e$ at $s(e)$ and summing at vertices.

### Theorem 4.1 — edge-fibre Fredholm alternative

$$
\boxed{
y\in\mathcal C_F^\perp
\quad\Longleftrightarrow\quad
\sigma_F(y)\in\operatorname{im}\delta_f^*.}
$$

### Proof

Let $R_F:\Gamma^{V(G)}\to Q_F$ be the one-sided evaluation map. Then $\rho_F=R_F|_{\ker\delta_f}$. Hence

$$
\begin{aligned}
y\perp\operatorname{im}\rho_F
&\Longleftrightarrow
R_F^*y\in(\ker\delta_f)^\perp\\
&\Longleftrightarrow
R_F^*y\in\operatorname{im}\delta_f^*.
\end{aligned}
$$

Under the quotient-dual identification, $R_F^*y=\sigma_F(y)$. $\square$

Changing $s(e)$ on one edge changes $\sigma_F(y)$ by the divergence of the edge field supported on that edge with value $y_e$. Therefore membership in $\operatorname{im}\delta_f^*$ and the dual code $\mathcal C_F^\perp$ are endpoint-choice independent.

## 5. Prescribed fibre values

Let $q_F(g)=(q_e(g))_{e\in F}\in Q_F$ be the fibre coordinates of the base lift. Under translation by $k$,

$$
q_F(g^k)=q_F(g)+\rho_F(k).
$$

### Theorem 5.1 — exact prescribed-value criterion

A target fibre vector $t\in Q_F$ occurs in the fixed lift orbit if and only if

$$
t-q_F(g)\in\mathcal C_F,
$$

if and only if

$$
\langle y,t-q_F(g)\rangle=0
$$

for every $y\in\mathcal C_F^\perp$.

### Proof

The first equivalence is the orbit formula. The second is the standard identity

$$
(\mathcal C_F^\perp)^\perp=\mathcal C_F
$$

in finite-dimensional binary duality. $\square$

When the criterion holds, a preimage $k$ under $\rho_F$ reconstructs the translated root lift. The set of such $k$ is a torsor under $\ker\rho_F$.

This is the point at which a single incompatible target can receive an exact linear stress certificate.

## 6. Allowed product sets

Let $A_e\subseteq Q_e$ be an allowed set of final fibre values and define the translated product set

$$
A=\prod_{e\in F}(A_e-q_e(g))\subseteq Q_F.
$$

### Proposition 6.1

The fixed lift orbit contains an assignment satisfying all edge restrictions if and only if

$$
\boxed{
\mathcal C_F\cap A\ne\varnothing.}
$$

### Proof

A translated lift has fibre increment $c\in\mathcal C_F$. It is allowed exactly when $c_e+q_e(g)\in A_e$ on every edge, which is $c\in A$. $\square$

Unlike Theorem 5.1, this is generally a nonlinear union of prescribed-value problems. There need not be one linear functional separating all of $A$ from $\mathcal C_F$.

## 7. Exact Fourier count

For $y\in Q_F^*$, let

$$
\chi_y(q)=(-1)^{\langle y,q\rangle}
$$

and use the unnormalized Fourier transform

$$
\widehat\phi(y)
=
\sum_{q\in Q_F}\phi(q)\chi_y(q).
$$

### Theorem 7.1 — Fourier/stress formula

For every $A\subseteq Q_F$,

$$
\boxed{
|\mathcal C_F\cap A|
=
\frac{|\mathcal C_F|}{|Q_F|}
\sum_{y\in\mathcal C_F^\perp}
\widehat{\mathbf1_A}(y).}
$$

If $A=\prod_{e\in F}A_e'$, then

$$
\widehat{\mathbf1_A}(y)
=
\prod_{e\in F}
\widehat{\mathbf1_{A_e'}}(y_e).
$$

### Proof

Character orthogonality gives the code indicator

$$
\mathbf1_{\mathcal C_F}(q)
=
\frac{|\mathcal C_F|}{|Q_F|}
\sum_{y\in\mathcal C_F^\perp}\chi_y(q).
$$

Multiply by $\mathbf1_A(q)$, sum over $q$, and interchange the finite sums. Product factorization is the tensor-product factorization of the finite Fourier transform. $\square$

The zero frequency contributes

$$
\frac{|\mathcal C_F|}{|Q_F|}|A|.
$$

This is the uniform main term. It is an exact summand, not an assertion that fibre coordinates are probabilistically independent or uniformly distributed beyond the linear orbit.

Every nonzero frequency is a relative stress by Theorem 4.1. Thus the entire deviation from the uniform term is dual stress data.

## 8. One forbidden value in rank three

Assume $\Gamma=\mathbf F_2^3$. Then $|Q_e|=4$. Suppose one value $a_e\in Q_e$ is forbidden on each edge of $F$, so

$$
A_e'=Q_e\setminus\{a_e\}.
$$

For $y_e\in Q_e^*$,

$$
\widehat{\mathbf1_{A_e'}}(y_e)
=
\begin{cases}
3,&y_e=0,\\
-\chi_{y_e}(a_e),&y_e\ne0.
\end{cases}
$$

Hence, writing $z(y)$ for the number of zero coordinates,

$$
|\mathcal C_F\cap A|
=
\frac{|\mathcal C_F|}{4^{|F|}}
\sum_{y\in\mathcal C_F^\perp}
3^{z(y)}(-1)^{|F|-z(y)}\chi_y(a).
$$

The zero-frequency term is

$$
|\mathcal C_F|\left(\frac34\right)^{|F|}.
$$

### Corollary 8.1 — phase-free sufficient condition

If

$$
\sum_{0\ne y\in\mathcal C_F^\perp}
3^{-\operatorname{wt}(y)}<1,
$$

then an avoiding lift exists.

### Proof

Factor $3^{|F|}$ from the Fourier sum. The absolute value of the total nonzero-frequency contribution is at most

$$
3^{|F|}
\sum_{0\ne y}3^{-\operatorname{wt}(y)},
$$

strictly smaller than the positive zero-frequency contribution. $\square$

This condition is sufficient, not necessary. Failure of the inequality does not prove nonexistence.

## 9. What a zero count certifies

If $|\mathcal C_F\cap A|=0$, the exact Fourier sum cancels. This gives a structured identity among the relative stresses and their phases. It does **not** in general supply one nonzero stress $y$ such that every $a\in A$ violates one affine equation.

A single separating stress exists precisely when the nonlinear allowed set lies wholly in a union of forbidden cosets detected by that stress; this is an additional property, not a consequence of the zero count alone.

Therefore finite computations should distinguish:

1. an exact zero count;
2. the complete Fourier cancellation identity;
3. a single compact linear stress certificate, when one exists;
4. a list or ideal of several stress constraints covering the allowed set.

## 10. Full-witness recovery

The dual data do not by themselves produce five supports. To recover a full witness one needs:

1. the fixed flow $f$;
2. a compatible base lift $g$;
3. the selected edge set and fibre coordinate model;
4. a codeword $c\in\mathcal C_F\cap A$;
5. a preimage $k\in H_f^0$ with $\rho_F(k)=c$;
6. the translated lift $g^k$;
7. the B1 root-flow/support reconstruction.

The Fourier formula proves existence when its count is positive, after which a witness may be found by solving or enumerating the primal code intersection. A positive integer count is an existence proof but not an explicit witness until one codeword or preimage is exhibited.

## 11. Relation to gauge circuits

The full gauge space $H_f^0$ and its minimal interface decompositions describe source-side translation motion. The relative stress code $\mathcal C_F^\perp$ describes dependencies among selected fibre evaluations. They are paired through $\rho_F$, but are not the same object:

- a gauge word is primal motion;
- a relative stress is a dual relation;
- the kernel of $\rho_F$ is invisible motion on the selected fibres;
- the cokernel defect is the relative stress dimension.

Classifying either side by support cardinality alone does not determine the nonlinear avoidance count; the phase data in the Fourier sum also matter.

## 12. Scope and assurance

- The Fredholm and Fourier identities are complete finite-dimensional proofs.
- No false universal orthogonal module from B2.3 is used.
- No probabilistic independence, asymptotic estimate, or weight-enumerator bound is assumed.
- Exact finite weight enumerators remain evidence inputs until a uniform theorem is proved.
- The formulation is fixed-flow and fixed-lift; graph-level five-support existence still requires choosing successful data.
- No formalization or literature novelty claim is made.

## 13. Completion assessment

`AC-PD-B2.4` is `COMPLETE-DRAFT / WITNESS-SCOPE`. The remaining B2 work is to consolidate B2.1–B2.4, reclassify the false universal orthogonal hierarchy, and state the exact boundary between full witness equivalences and dual/quotient projections. After that B2 is ready for Curator intake and B3 becomes active.