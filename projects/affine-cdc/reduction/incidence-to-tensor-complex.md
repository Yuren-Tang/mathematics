# From affine incidence geometry to the tensor complex

**Status.** The exact sequences and chain maps below are theorem-level linear
algebra. Their matrix identities have been checked on the canonical rank-three
$K_4$ and rank-four $K_{3,3}$ examples. This presentation has not yet been
Lean-formalized.

This chapter gives the precise relation between the affine incidence-pair
complex, the quotient sheaf, and the flow tensor complex. It supersedes the
earlier provisional description of the tensor complex as merely a “reduced
compression.”

## 1. Graphical data and the tensor operators

Let $G=(V,E)$ be a finite connected graph and let

$$
f:E\longrightarrow\Gamma
$$

be a nowhere-zero binary flow whose values span $\Gamma$. Let

$$
\mathcal C:=\mathcal C(G)\leq\mathbf F_2^E
$$

be the binary cycle space and put

$$
Q_G:=\mathbf F_2^E/\mathcal C^\perp
\cong\mathcal C^*.
$$

For an edge $e$, let $\bar e\in Q_G$ be the restricted coordinate functional.
The flow induces a surjection

$$
F_f:Q_G\longrightarrow\Gamma,
\qquad
F_f(\bar e)=f(e).
$$

Define

$$
T_f:\mathbf F_2^E\longrightarrow\Gamma\otimes Q_G,
\qquad
T_f(\lambda)=\sum_{e\in E}\lambda_ef(e)\otimes\bar e,
$$

and

$$
W_f:\Gamma\otimes Q_G\longrightarrow\Lambda^2\Gamma,
\qquad
W_f(a\otimes q)=a\wedge F_f(q).
$$

Since

$$
W_fT_f(e)=f(e)\wedge f(e)=0,
$$

one obtains the flow tensor complex

$$
\boxed{
\mathcal T_f:
\mathbf F_2^E
\xrightarrow{T_f}
\Gamma\otimes Q_G
\xrightarrow{W_f}
\Lambda^2\Gamma.
}
$$

Write

$$
\mathcal B_f:=\ker T_f,
\qquad
\mathcal K_f:=\ker W_f/\operatorname{im}T_f.
$$

The first is the gauge-moduli code and the second is the middle tensor homology.

## 2. Degree-zero comparison with the quotient sheaf

For the quotient-sheaf complex, put

$$
C_f^0:=\Gamma^V,
\qquad
C_f^1:=\bigoplus_{e\in E}Q_e,
$$

where

$$
Q_e:=\Gamma/\langle f(e)\rangle,
$$

and

$$
(\delta_fm)_e=[m_u+m_v]
\qquad(e=uv).
$$

Let

$$
H_f^0:=\ker\delta_f,
\qquad
H_f^1:=\operatorname{coker}\delta_f.
$$

For $m\in H_f^0$, there is a unique bit $\lambda_e(m)$ satisfying

$$
m_u+m_v=\lambda_e(m)f(e).
$$

This defines

$$
s_f:H_f^0\longrightarrow\mathbf F_2^E.
$$

### Theorem 2.1

There is a canonical short exact sequence

$$
\boxed{
0\longrightarrow
\Gamma
\longrightarrow
H_f^0
\xrightarrow{s_f}
\ker T_f
\longrightarrow0,
}
$$

where $\Gamma$ is embedded as the constant sections. Consequently,

$$
\boxed{
H_f^0/\Gamma\cong\mathcal B_f.
}
$$

### Proof

The kernel of $s_f$ consists of sections constant across every edge, hence of
global constants because $G$ is connected.

Regard

$$
\Gamma\otimes Q_G
\cong
\operatorname{Hom}(\mathcal C,\Gamma).
$$

For $c=(c_e)\in\mathcal C$,

$$
T_f(\lambda)(c)
=
\sum_ec_e\lambda_ef(e).
$$

Thus $T_f(\lambda)=0$ exactly when the $\Gamma$-valued edge function
$g_e=\lambda_ef(e)$ has zero sum on every cycle. On a connected graph this is
equivalent to $g$ being a tension,

$$
g_e=m_u+m_v,
$$

for a potential $m$, unique modulo constants. Such an $m$ belongs to $H_f^0$
and maps to $\lambda$. $\square$

## 3. The full obstruction space as a tensor cokernel

Define

$$
\Xi_f:C_f^1\longrightarrow\operatorname{coker}T_f
$$

as follows. For $x=(x_e)_e$, choose lifts $\widetilde x_e\in\Gamma$ and put

$$
\Xi_f(x)
:=
\left[
\sum_e\widetilde x_e\otimes\bar e
\right].
$$

Changing a lift by $\lambda_ef(e)$ changes the tensor by $T_f(\lambda)$, so the
class is independent of lifts. If $x=\delta_fm$, choose the lifts
$\widetilde x_e=m_u+m_v$. Then the associated homomorphism on a cycle $c$ is

$$
\sum_{e=uv}c_e(m_u+m_v)
=
\sum_vm_v\sum_{e\ni v}c_e
=0.
$$

Hence $\Xi_f$ vanishes on coboundaries and descends to

$$
\overline\Xi_f:H_f^1\longrightarrow\operatorname{coker}T_f.
$$

### Theorem 3.1

$$
\boxed{
\overline\Xi_f:
H_f^1
\xrightarrow{\sim}
\operatorname{coker}T_f
}
$$

is a canonical isomorphism.

### Proof

The classes $\bar e$ span $Q_G$, so tensors $a\otimes\bar e$ span
$\Gamma\otimes Q_G$ and are images of edge cochains; hence the map is
surjective.

If $\Xi_f(x)=0$, choose lifts $\widetilde x_e$. There is a word $\lambda$ such
that

$$
\sum_e(\widetilde x_e+\lambda_ef(e))\otimes\bar e=0.
$$

The edge function

$$
g_e:=\widetilde x_e+\lambda_ef(e)
$$

annihilates every cycle, hence is a tension $g_e=m_u+m_v$. Since $g_e$ and
$\widetilde x_e$ represent the same class in $Q_e$, one has
$x=\delta_fm$. $\square$

Thus the entire quotient-sheaf obstruction space, not only its distinguished
affine class, has the canonical tensor presentation

$$
H_f^1\cong\operatorname{coker}T_f.
$$

## 4. The wedge moment

Because $W_fT_f=0$, the wedge map descends to

$$
\overline W_f:\operatorname{coker}T_f\longrightarrow\Lambda^2\Gamma.
$$

Transporting it through $\overline\Xi_f$ gives

$$
\mu_f:H_f^1\longrightarrow\Lambda^2\Gamma.
$$

If $[x]\in H_f^1$ is represented by $x=(x_e)$ and
$\widetilde x_e\in\Gamma$ are lifts, then

$$
\boxed{
\mu_f([x])
=
\sum_ef(e)\wedge\widetilde x_e.
}
$$

This is independent of lifts because $f(e)\wedge f(e)=0$. It is independent of
the cochain representative because a vertex coboundary contributes

$$
\sum_{e=uv}f(e)\wedge(m_u+m_v)
=
\sum_vm_v\wedge\sum_{e\ni v}f(e)
=0.
$$

Since $F_f:Q_G\to\Gamma$ is surjective, $W_f$ and $\mu_f$ are surjective.

### Theorem 4.1

There is a canonical short exact sequence

$$
\boxed{
0\longrightarrow
\mathcal K_f
\longrightarrow
H_f^1
\xrightarrow{\mu_f}
\Lambda^2\Gamma
\longrightarrow0.
}
$$

Hence

$$
\boxed{
\mathcal K_f=\ker\mu_f\subseteq H_f^1.
}
$$

The tensor middle homology is the zero-wedge-moment part of the full incidence
obstruction space.

## 5. The affine class already has zero moment

Let $[c_f]\in H_f^1$ be the intrinsic affine compatibility class. The
wedge-handshake identity gives

$$
\mu_f([c_f])=0.
$$

Therefore

$$
[c_f]\in\mathcal K_f.
$$

Its image under the canonical identification with tensor middle homology is the
tensor obstruction class $\kappa_f$. No arbitrary projection or choice is
involved. In particular,

$$
\boxed{
[c_f]=0
\iff
\kappa_f=0.
}
$$

Although the tensor complex does not retain every element of $H_f^1$ as middle
homology, it retains the entire affine compatibility class.

## 6. The universal tension resolution

Define the graph coboundary

$$
D_G:\Gamma^V\longrightarrow\Gamma^E,
\qquad
(D_Gm)_e=m_u+m_v,
$$

and define

$$
P_G:\Gamma^E\longrightarrow\Gamma\otimes Q_G,
\qquad
P_G(g)=\sum_eg_e\otimes\bar e.
$$

Under $\Gamma\otimes Q_G\cong\operatorname{Hom}(\mathcal C,\Gamma)$,

$$
P_G(g)(c)=\sum_ec_eg_e.
$$

Thus $\ker P_G$ is exactly the space of $\Gamma$-valued tensions, which is
$\operatorname{im}D_G$. The coordinate classes span $Q_G$, so $P_G$ is
surjective.

### Theorem 6.1 — universal tension resolution

$$
\boxed{
0\longrightarrow
\Gamma
\longrightarrow
\Gamma^V
\xrightarrow{D_G}
\Gamma^E
\xrightarrow{P_G}
\Gamma\otimes Q_G
\longrightarrow0
}
$$

is exact.

This resolution depends only on the connected graph and the coefficient space,
not on the chosen flow.

## 7. Flow lines and the lifted incidence complex

Define the coordinatewise flow-line inclusion

$$
J_f:\mathbf F_2^E\longrightarrow\Gamma^E,
\qquad
(J_f\lambda)_e=\lambda_ef(e).
$$

It is injective because every flow value is nonzero. The tensor operator
factors as

$$
\boxed{T_f=P_GJ_f.}
$$

Define

$$
M_f:\Gamma^E\longrightarrow\Lambda^2\Gamma,
\qquad
M_f(g)=\sum_eg_e\wedge f(e).
$$

Then

$$
M_f=W_fP_G,
\qquad
M_fD_G=0,
\qquad
M_fJ_f=0.
$$

The first vanishing uses the vertex flow equations; the second uses
$f(e)\wedge f(e)=0$.

Therefore there is a canonical lifted incidence complex

$$
\boxed{
\widehat{\mathcal R}_f:
\Gamma^V\oplus\mathbf F_2^E
\xrightarrow{D_G+J_f}
\Gamma^E
\xrightarrow{M_f}
\Lambda^2\Gamma.
}
$$

## 8. The extended quotient-sheaf complex

Quotienting $\Gamma^E$ by the coordinate flow lines gives

$$
\Gamma^E/J_f(\mathbf F_2^E)
\cong
\bigoplus_eQ_e.
$$

The map $M_f$ descends to

$$
\mu_f^1:\bigoplus_eQ_e\longrightarrow\Lambda^2\Gamma,
\qquad
\mu_f^1((x_e))
=
\sum_ef(e)\wedge\widetilde x_e.
$$

Define

$$
\boxed{
\widehat{\mathscr Q}_f:
\Gamma^V
\xrightarrow{\delta_f}
\bigoplus_eQ_e
\xrightarrow{\mu_f^1}
\Lambda^2\Gamma.
}
$$

Projection in degree zero, quotient by the flow lines in degree one, and the
identity in degree two define a surjective chain map

$$
q_{\mathrm{sheaf}}:
\widehat{\mathcal R}_f
\longrightarrow
\widehat{\mathscr Q}_f.
$$

Its kernel is the contractible complex

$$
[\mathbf F_2^E\xrightarrow{J_f}J_f(\mathbf F_2^E)\to0].
$$

### Theorem 8.1

The map $q_{\mathrm{sheaf}}$ is a canonical quasi-isomorphism:

$$
\boxed{
\widehat{\mathcal R}_f
\xrightarrow{\simeq}
\widehat{\mathscr Q}_f.
}
$$

## 9. The tensor complex as a chain-level quotient

Projection to the $\mathbf F_2^E$ summand in degree zero, $P_G$ in degree one,
and the identity in degree two define a surjective chain map

$$
q_{\mathrm{tensor}}:
\widehat{\mathcal R}_f
\longrightarrow
\mathcal T_f.
$$

The chain-map equations are

$$
P_G(D_Gm+J_f\lambda)=T_f(\lambda)
$$

and

$$
W_fP_G=M_f.
$$

Its kernel is

$$
[\Gamma^V\xrightarrow{D_G}\operatorname{Tens}_\Gamma(G)\to0],
$$

whose only nonzero cohomology is the constant-potential space $\Gamma$ in
degree zero.

### Theorem 9.1 — chain-level tensor reduction

There is a canonical short exact sequence of complexes

$$
\boxed{
0\longrightarrow
[\Gamma^V\xrightarrow{D_G}\operatorname{Tens}_\Gamma(G)\to0]
\longrightarrow
\widehat{\mathcal R}_f
\longrightarrow
\mathcal T_f
\longrightarrow0.
}
$$

Combining this with Theorem 8.1 gives the canonical zigzag

$$
\boxed{
\widehat{\mathscr Q}_f
\xleftarrow{\ \simeq\ }
\widehat{\mathcal R}_f
\xrightarrow{\ \twoheadrightarrow\ }
\mathcal T_f.
}
$$

The left arrow removes a contractible flow-line lift. The right arrow removes
the universal tension-resolution complex.

## 10. Cohomology of the zigzag

The long exact sequence recovers

$$
0\longrightarrow
\Gamma
\longrightarrow
H_f^0
\longrightarrow
\mathcal B_f
\longrightarrow0
$$

and gives

$$
H^1(\widehat{\mathscr Q}_f)
\cong
H^1(\mathcal T_f)
=
\mathcal K_f.
$$

The ordinary quotient-sheaf obstruction space is restored by

$$
0\longrightarrow
\mathcal K_f
\longrightarrow
H_f^1
\xrightarrow{\mu_f}
\Lambda^2\Gamma
\longrightarrow0.
$$

Thus the strict dependency order is

1. affine incidence-pair complex;
2. quotient-sheaf presentation;
3. extended quotient sheaf with wedge moment;
4. lifted incidence resolution;
5. tensor complex as a quotient.

## 11. Dual comparison

Since

$$
(H_f^1)^*\cong\operatorname{Stress}(f),
$$

dualizing the wedge-moment exact sequence gives

$$
0\longrightarrow
\Lambda^2\Gamma^*
\longrightarrow
\operatorname{Stress}(f)
\longrightarrow
\mathcal K_f^*
\longrightarrow0.
$$

The first map sends an alternating form $\alpha$ to the canonical stress

$$
\psi_e^\alpha(x)=\alpha(f(e),x).
$$

Its image is the alternating-stress subspace

$$
\operatorname{AltStress}(f).
$$

Therefore

$$
\boxed{
\mathcal K_f^*
\cong
\operatorname{Stress}(f)/\operatorname{AltStress}(f)
=:
\operatorname{EssStress}(f).
}
$$

The tensor middle homology is dual to the essential, rather than the full,
stress space.

## 12. What the reduction preserves and forgets

The tensor complex preserves:

- the reduced global-section space $H_f^0/\Gamma$;
- the zero-wedge-moment obstruction space $\mathcal K_f$;
- the distinguished affine class $\kappa_f$;
- the essential-stress quotient;
- the edge-column matroid represented by $f(e)\otimes\bar e$;
- the code-flag and Schur-product data developed downstream.

It removes or forgets:

- constant vertex translations in degree zero;
- the nonzero wedge-moment quotient $\Lambda^2\Gamma$ of the full obstruction
  space;
- a preferred vertex realization of the cycle code;
- the local incidence decomposition by vertices;
- the original local-family and dart interpretation;
- the final CDC extraction;
- embedding and surface enhancements.

The correct statement is therefore:

$$
\boxed{
\text{the tensor complex is a canonical chain-level reduction of an explicit}
\text{ resolution of the affine incidence geometry.}
}
$$

It is a powerful downstream presentation, but it is not the compatibility
source object.