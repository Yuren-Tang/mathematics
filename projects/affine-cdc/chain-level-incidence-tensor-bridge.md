# The chain-level incidence–tensor bridge

**Date:** 2026-07-15  
**Status:** theorem-level structural draft; matrix identities checked on the
canonical rank-three \(K_4\) and rank-four \(K_{3,3}\) examples; not yet
independently audited or Lean-formalized.

This note strengthens the incidence–tensor comparison from a cohomological
identification to a canonical chain-level zigzag.

Let \(G=(V,E)\) be a finite connected graph and let

\[
f:E\to\Gamma
\]

be a nowhere-zero spanning binary flow.

Write

\[
\mathcal C=\mathcal C(G)
\]

for the binary cycle space and

\[
Q_G=\mathbf F_2^E/\mathcal C^\perp\cong\mathcal C^*.
\]

For \(e\in E\), let \(\bar e\in Q_G\) be the restricted coordinate
functional.

---

## 1. The universal tension resolution

Let

\[
D_G:\Gamma^V\to\Gamma^E
\]

be the \(\Gamma\)-valued graph coboundary:

\[
(D_Gm)_e=m_u+m_v,
\qquad e=uv.
\]

Define

\[
P_G:\Gamma^E\to\Gamma\otimes Q_G
\]

by

\[
\boxed{
P_G(g)=\sum_eg_e\otimes\bar e.
}
\]

Under

\[
\Gamma\otimes Q_G
\cong
\operatorname{Hom}(\mathcal C,\Gamma),
\]

the value of \(P_G(g)\) on a cycle \(c=(c_e)\) is

\[
P_G(g)(c)=\sum_ec_eg_e.
\]

Hence

\[
\ker P_G
=
\{\Gamma\text{-valued edge functions with zero sum on every cycle}\}.
\]

For a connected graph this is exactly the tension space

\[
\operatorname{Tens}_\Gamma(G)=\operatorname{im}D_G.
\]

The coordinate functionals \(\bar e\) span \(Q_G\), so \(P_G\) is
surjective. Therefore:

### Theorem 1.1

\[
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
\]

is exact.

---

## 2. The flow-line inclusion

Define

\[
J_f:\mathbf F_2^E\to\Gamma^E
\]

coordinatewise by

\[
\boxed{
(J_f\lambda)_e=\lambda_ef(e).
}
\]

Because every \(f(e)\ne0\), the map \(J_f\) is injective. Its image is the
direct sum of the edge flow lines:

\[
\operatorname{Line}(f)
=
\bigoplus_e\langle f(e)\rangle
\le\Gamma^E.
\]

The tensor operator factors as

\[
\boxed{
T_f=P_GJ_f.
}
\]

---

## 3. The lifted incidence complex

Define

\[
M_f:\Gamma^E\to\Lambda^2\Gamma
\]

by

\[
\boxed{
M_f(g)=\sum_eg_e\wedge f(e).
}
\]

Since

\[
M_f=W_fP_G,
\]

one has

\[
M_fD_G=0
\]

and

\[
M_fJ_f=0.
\]

The first identity follows from the vertex flow equations, and the second from
\(f(e)\wedge f(e)=0\).

Therefore there is a canonical three-term complex

\[
\boxed{
\widehat{\mathcal R}_f:
\Gamma^V\oplus\mathbf F_2^E
\xrightarrow{D_G+J_f}
\Gamma^E
\xrightarrow{M_f}
\Lambda^2\Gamma.
}
\]

This is the **lifted incidence complex**.

---

## 4. The extended quotient-sheaf complex

For every edge put

\[
Q_e=\Gamma/\langle f(e)\rangle.
\]

Since

\[
\Gamma^E/J_f(\mathbf F_2^E)
\cong
\bigoplus_eQ_e,
\]

the map \(M_f\) descends to

\[
\mu_f^1:
\bigoplus_eQ_e
\to
\Lambda^2\Gamma,
\qquad
\mu_f^1((x_e))
=
\sum_ef(e)\wedge\widetilde x_e.
\]

Define the extended quotient-sheaf complex

\[
\boxed{
\widehat{\mathscr Q}_f:
\Gamma^V
\xrightarrow{\delta_f}
\bigoplus_eQ_e
\xrightarrow{\mu_f^1}
\Lambda^2\Gamma.
}
\]

There is a canonical surjective chain map

\[
q_{\mathrm{sheaf}}:
\widehat{\mathcal R}_f
\longrightarrow
\widehat{\mathscr Q}_f
\]

given by projection to \(m\) in degree zero, quotient by the flow lines in
degree one, and the identity in degree two.

Its kernel is

\[
\boxed{
[
\mathbf F_2^E
\xrightarrow{J_f}
J_f(\mathbf F_2^E)
\to0
],
}
\]

which is contractible.

### Theorem 4.1

\[
\boxed{
\widehat{\mathcal R}_f
\overset{\simeq}{\longrightarrow}
\widehat{\mathscr Q}_f
}
\]

is a canonical quasi-isomorphism.

---

## 5. The full tensor complex as a chain-level quotient

The full tensor complex is

\[
\boxed{
\mathcal T_f:
\mathbf F_2^E
\xrightarrow{T_f}
\Gamma\otimes Q_G
\xrightarrow{W_f}
\Lambda^2\Gamma.
}
\]

Define

\[
q_{\mathrm{tensor}}:
\widehat{\mathcal R}_f
\longrightarrow
\mathcal T_f
\]

by projection to \(\lambda\) in degree zero, \(P_G\) in degree one, and the
identity in degree two.

The chain-map identities are

\[
P_G(D_Gm+J_f\lambda)=T_f(\lambda)
\]

and

\[
W_fP_G=M_f.
\]

The map is surjective in every degree. Its kernel is

\[
\boxed{
[
\Gamma^V
\xrightarrow{D_G}
\operatorname{Tens}_\Gamma(G)
\to0
].
}
\]

This kernel complex has only one nonzero cohomology group:

\[
H^0\cong\Gamma,
\]

the constant potentials.

### Theorem 5.1 — chain-level tensor reduction

There is a canonical short exact sequence of complexes

\[
\boxed{
0\longrightarrow
[
\Gamma^V
\xrightarrow{D_G}
\operatorname{Tens}_\Gamma(G)
\to0
]
\longrightarrow
\widehat{\mathcal R}_f
\longrightarrow
\mathcal T_f
\longrightarrow0.
}
\]

Combining with Theorem 4.1 gives the canonical zigzag

\[
\boxed{
\widehat{\mathscr Q}_f
\ \xleftarrow{\ \simeq\ }\
\widehat{\mathcal R}_f
\ \twoheadrightarrow\
\mathcal T_f.
}
\]

The left arrow removes a contractible flow-line lift. The right arrow removes
the constant-potential coefficient complex.

---

## 6. The long exact comparison

The short exact sequence gives

\[
0\to\Gamma
\to H^0(\widehat{\mathscr Q}_f)
\to H^0(\mathcal T_f)
\to0
\]

and

\[
H^1(\widehat{\mathscr Q}_f)
\overset\sim\longrightarrow
H^1(\mathcal T_f).
\]

Since

\[
H^0(\widehat{\mathscr Q}_f)
=
H^0(G;\mathscr Q_f)
\]

and

\[
H^0(\mathcal T_f)=\ker T_f,
\]

this recovers

\[
\boxed{
0\to\Gamma
\to H^0(G;\mathscr Q_f)
\to\ker T_f
\to0.
}
\]

Moreover,

\[
H^1(\widehat{\mathscr Q}_f)
=
\frac{\ker\mu_f^1}{\operatorname{im}\delta_f}
\]

and

\[
H^1(\mathcal T_f)
=
\frac{\ker W_f}{\operatorname{im}T_f}
=
\mathcal K_f.
\]

Therefore

\[
\boxed{
H^1(\widehat{\mathscr Q}_f)
\cong
\mathcal K_f.
}
\]

If the flow values span \(\Gamma\), then \(W_f\) is surjective and both
complexes have zero \(H^2\).

---

## 7. Recovering the full quotient-sheaf obstruction space

The ordinary quotient-sheaf cohomology fits into

\[
\boxed{
0\to
\mathcal K_f
\to
H_f^1
\xrightarrow{\mu_f}
\Lambda^2\Gamma
\to0.
}
\]

Thus the full quotient-sheaf obstruction space is the extension of the tensor
middle homology by the canonical wedge-moment coefficient space.

---

## 8. The affine class

Let

\[
[c_f]\in H_f^1
\]

be the intrinsic affine obstruction. The wedge-handshake identity is exactly

\[
\mu_f([c_f])=0.
\]

Hence the affine class lies in

\[
H^1(\widehat{\mathscr Q}_f)
\cong
\mathcal K_f.
\]

This is the tensor obstruction class. It is transported by the chain-level
zigzag, not produced by an arbitrary projection.

---

## 9. The master diagram

The complete chain-level picture is

\[
\boxed{
\begin{array}{ccccc}
&&\widehat{\mathcal R}_f&&\\
&\swarrow_{\simeq}&&\searrow_{\mathrm{quotient}}&\\
\widehat{\mathscr Q}_f&&&&\mathcal T_f.
\end{array}
}
\]

It is generated by

\[
D_G:\Gamma^V\to\Gamma^E,
\qquad
J_f:\mathbf F_2^E\to\Gamma^E,
\qquad
P_G:\Gamma^E\to\Gamma\otimes Q_G,
\]

with

\[
P_GD_G=0,
\qquad
P_GJ_f=T_f,
\qquad
M_f=W_fP_G.
\]

This is the exact chain-level replacement for the earlier phrase that the
tensor complex is a “reduced compression” of the quotient sheaf.

---

## 10. Architectural consequence

The strict order is now:

1. the affine incidence-pair complex gives the symmetric local compatibility
   problem;
2. cancelling the edge-diagonal contractible piece gives the quotient sheaf;
3. adjoining the wedge moment gives the extended quotient sheaf;
4. resolving the edge quotient by flow-line lifts gives
   \(\widehat{\mathcal R}_f\);
5. quotienting the universal tension resolution gives the full tensor complex.

Thus the tensor complex is a canonical chain-level reduction of an explicit
resolution of the affine incidence geometry.
