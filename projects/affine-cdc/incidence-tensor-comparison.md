# The incidence–tensor comparison theorem

**Date:** 2026-07-15  
**Status:** theorem-level linear-algebra draft; not yet independently audited or
Lean-formalized in this presentation.

This note replaces the provisional statement that the flow tensor complex is
merely a “reduced compression” of the affine incidence pair by precise canonical
comparison maps.

Let \(G=(V,E)\) be a finite connected graph and let

\[
f:E\to\Gamma
\]

be a nowhere-zero binary flow whose values span the finite-dimensional
\(\mathbf F_2\)-space \(\Gamma\).

Write

\[
\mathcal C=\mathcal C(G)\le \mathbf F_2^E
\]

for the cycle space and

\[
Q_G=\mathbf F_2^E/\mathcal C^\perp\cong\mathcal C^*.
\]

For \(e\in E\), let \(\bar e\in Q_G\) be the coordinate functional restricted
to \(\mathcal C\).

For each edge put

\[
Q_e=\Gamma/\langle f(e)\rangle.
\]

The quotient-sheaf cochain complex is

\[
C_f^0=\Gamma^V,
\qquad
C_f^1=\bigoplus_{e=uv}Q_e,
\]

with

\[
(\delta_fm)_e=[m_u+m_v].
\]

Write

\[
H_f^0=\ker\delta_f,
\qquad
H_f^1=\operatorname{coker}\delta_f.
\]

The tensor complex is

\[
\mathbf F_2^E
\xrightarrow{T_f}
\Gamma\otimes Q_G
\xrightarrow{W_f}
\Lambda^2\Gamma,
\]

where

\[
T_f(\lambda)=\sum_e\lambda_ef(e)\otimes\bar e
\]

and

\[
W_f(a\otimes q)=a\wedge F_f(q),
\qquad
F_f(\bar e)=f(e).
\]

Put

\[
\mathcal K_f=\ker W_f/\operatorname{im}T_f.
\]

---

## 1. The degree-zero comparison

For \(m=(m_v)\in H_f^0\), the section condition says that for every edge
\(e=uv\),

\[
m_u+m_v\in\langle f(e)\rangle.
\]

Since \(f(e)\ne0\), there is a unique scalar

\[
\lambda_e(m)\in\mathbf F_2
\]

such that

\[
m_u+m_v=\lambda_e(m)f(e).
\]

This defines a linear map

\[
s_f:H_f^0\to\mathbf F_2^E,
\qquad
s_f(m)=(\lambda_e(m))_e.
\]

### Theorem 1.1

There is a canonical short exact sequence

\[
\boxed{
0\longrightarrow
\Gamma
\longrightarrow
H_f^0
\overset{s_f}{\longrightarrow}
\ker T_f
\longrightarrow0,
}
\]

where \(\Gamma\to H_f^0\) sends \(a\) to the constant section \(m_v=a\).

Consequently,

\[
\boxed{
H_f^0/\Gamma\cong\ker T_f.
}
\]

### Proof

The kernel of \(s_f\) consists of sections satisfying \(m_u=m_v\) on every
edge. Since \(G\) is connected, these are exactly the constant sections.

Regard

\[
\Gamma\otimes Q_G
\cong
\operatorname{Hom}(\mathcal C,\Gamma).
\]

For \(c=(c_e)\in\mathcal C\),

\[
T_f(\lambda)(c)
=
\sum_ec_e\lambda_ef(e).
\]

Thus \(T_f(\lambda)=0\) exactly when the \(\Gamma\)-valued edge function
\(g_e=\lambda_ef(e)\) has zero sum on every cycle. Over a connected graph this
is equivalent to \(g\) being a \(\Gamma\)-valued tension,

\[
g_e=m_u+m_v,
\]

for some vertex potential \(m\), unique modulo a constant. Such an \(m\) is a
global section and satisfies \(s_f(m)=\lambda\).

---

## 2. A canonical presentation of \(H_f^1\)

Define

\[
\Xi_f:C_f^1\to\operatorname{coker}T_f
\]

as follows. For \(x=(x_e)_e\), choose arbitrary lifts
\(\widetilde x_e\in\Gamma\) and put

\[
\boxed{
\Xi_f(x)
=
\left[
\sum_e\widetilde x_e\otimes\bar e
\right]
\in
(\Gamma\otimes Q_G)/\operatorname{im}T_f.
}
\]

### Lemma 2.1 — lift independence

Replacing \(\widetilde x_e\) by
\(\widetilde x_e+\lambda_ef(e)\) changes the tensor by

\[
\sum_e\lambda_ef(e)\otimes\bar e=T_f(\lambda).
\]

### Lemma 2.2 — coboundaries vanish

\[
\Xi_f(\delta_fm)=0.
\]

Choose the lift \(\widetilde x_e=m_u+m_v\). As a homomorphism
\(\mathcal C\to\Gamma\), the tensor

\[
\sum_{e=uv}(m_u+m_v)\otimes\bar e
\]

sends a cycle \(c\) to

\[
\sum_{e=uv}c_e(m_u+m_v)
=
\sum_vm_v\left(\sum_{e\ni v}c_e\right)
=0.
\]

Hence \(\Xi_f\) descends to

\[
\overline\Xi_f:H_f^1\to\operatorname{coker}T_f.
\]

### Theorem 2.3

\[
\boxed{
\overline\Xi_f:
H_f^1
\overset\sim\longrightarrow
\operatorname{coker}T_f
}
\]

is a canonical isomorphism.

### Proof: surjectivity

The coordinate classes \(\bar e\) span \(Q_G\), so \(\Gamma\otimes Q_G\) is
spanned by tensors \(a\otimes\bar e\). Such a tensor is the image of the
cochain having class \([a]\in Q_e\) at edge \(e\) and zero elsewhere.

### Proof: kernel

Suppose \(\Xi_f(x)=0\). Choose lifts \(\widetilde x_e\). Then for some
\(\lambda\in\mathbf F_2^E\),

\[
\sum_e(\widetilde x_e+\lambda_ef(e))\otimes\bar e=0.
\]

Put \(g_e=\widetilde x_e+\lambda_ef(e)\). The tensor equation says that \(g\)
annihilates every cycle, hence is a tension:

\[
g_e=m_u+m_v.
\]

Since \(g_e\) and \(\widetilde x_e\) define the same class in \(Q_e\),

\[
x_e=[m_u+m_v].
\]

Thus \(x=\delta_fm\).

---

## 3. The wedge-moment map

Because \(W_fT_f=0\), the wedge differential descends to

\[
\overline W_f:\operatorname{coker}T_f\to\Lambda^2\Gamma.
\]

Transporting it through \(\overline\Xi_f\) gives

\[
\mu_f:H_f^1\to\Lambda^2\Gamma.
\]

For a class represented by \(x=(x_e)\), choose lifts
\(\widetilde x_e\in\Gamma\). Then

\[
\boxed{
\mu_f([x])
=
\sum_ef(e)\wedge\widetilde x_e.
}
\]

This is independent of lifts because \(f(e)\wedge f(e)=0\), and independent of
the cochain representative because vertex coboundaries contribute

\[
\sum_{e=uv}f(e)\wedge(m_u+m_v)
=
\sum_vm_v\wedge\left(\sum_{e\ni v}f(e)\right)
=0.
\]

Under the comparison isomorphism,

\[
\mu_f=\overline W_f\circ\overline\Xi_f.
\]

Since the flow values span \(\Gamma\), the map \(F_f:Q_G\to\Gamma\) is
surjective, and therefore \(W_f\) and \(\mu_f\) are surjective.

### Theorem 3.1

There is a canonical short exact sequence

\[
\boxed{
0\longrightarrow
\mathcal K_f
\longrightarrow
H_f^1
\overset{\mu_f}{\longrightarrow}
\Lambda^2\Gamma
\longrightarrow0.
}
\]

Thus

\[
\boxed{
\mathcal K_f=\ker\mu_f\subseteq H_f^1.
}
\]

The tensor obstruction space is the canonical zero-moment subspace of the
quotient-sheaf obstruction space.

---

## 4. Exact comparison and its limitation

The two sides are summarized by

\[
\boxed{0\to\Gamma\to H_f^0\to\ker T_f\to0}
\]

and

\[
\boxed{0\to\mathcal K_f\to H_f^1\overset{\mu_f}{\to}\Lambda^2\Gamma\to0}.
\]

Tensor homology is obtained from quotient-sheaf cohomology by removing the
canonical coefficient pieces in opposite directions:

- quotient constant translations \(\Gamma\) out of \(H_f^0\);
- take the kernel of the wedge moment on \(H_f^1\).

This is canonical and requires no spanning tree, cycle basis or coordinate
choice.

It is a comparison of cohomology and tensor homology. It does **not** by itself
construct a literal quotient chain map, deformation retract or
quasi-isomorphism from the two-term quotient-sheaf complex to the three-term
tensor complex.

---

## 5. Dual comparison

Since

\[
(H_f^1)^*\cong\operatorname{Stress}(f),
\]

dualizing gives

\[
0\longrightarrow
\Lambda^2\Gamma^*
\overset{\mu_f^*}{\longrightarrow}
\operatorname{Stress}(f)
\longrightarrow
\mathcal K_f^*
\longrightarrow0.
\]

The map sends \(\alpha\in\Lambda^2\Gamma^*\) to

\[
\boxed{
\psi_e^\alpha(x)=\alpha(f(e),x).
}
\]

Its image is the canonical alternating-stress subspace
\(\operatorname{AltStress}(f)\). Therefore

\[
\boxed{
0\longrightarrow
\operatorname{AltStress}(f)
\longrightarrow
\operatorname{Stress}(f)
\longrightarrow
\mathcal K_f^*
\longrightarrow0
}
\]

and

\[
\boxed{
\mathcal K_f^*
\cong
\operatorname{Stress}(f)/\operatorname{AltStress}(f)
=
\operatorname{EssStress}(f).
}
\]

---

## 6. The affine obstruction

Let \([c_f]\in H_f^1\) be the intrinsic affine compatibility class. Under

\[
H_f^1\cong\operatorname{coker}T_f,
\]

it is represented by

\[
\left[
\sum_e\widetilde c_{f,e}\otimes\bar e
\right],
\]

where \(\widetilde c_{f,e}\) is any lift of the edge obstruction class.

The wedge-handshake identity says

\[
\mu_f([c_f])=0.
\]

Hence

\[
[c_f]\in\ker\mu_f=\mathcal K_f.
\]

This element is exactly the tensor obstruction \(\kappa_f\). Thus the passage
from \([c_f]\) to \(\kappa_f\) is not an additional projection or choice: the
affine class already lies in the canonical zero-moment subspace.

Compatibility is equivalently

\[
[c_f]=0\iff\kappa_f=0.
\]

---

## 7. Relation to the affine incidence pair

For

\[
\mathfrak I_f=(E_f,L_{\mathrm{vert}},L_{\mathrm{edge}},
\kappa+L_{\mathrm{vert}}),
\]

one has

\[
H_f^0=L_{\mathrm{vert}}\cap L_{\mathrm{edge}}
\]

and

\[
H_f^1=E_f/(L_{\mathrm{vert}}+L_{\mathrm{edge}}).
\]

Therefore

\[
\boxed{
\frac{L_{\mathrm{vert}}\cap L_{\mathrm{edge}}}{\Gamma}
\cong\ker T_f
}
\]

and

\[
\boxed{
E_f/(L_{\mathrm{vert}}+L_{\mathrm{edge}})
\cong\operatorname{coker}T_f.
}
\]

The tensor middle homology is the kernel of the canonical wedge moment on the
second quotient.

Dually,

\[
\boxed{
\frac{L_{\mathrm{vert}}^\perp\cap L_{\mathrm{edge}}^\perp}
{\operatorname{AltStress}(f)}
\cong\mathcal K_f^*.
}
\]

This supplies the exact maps omitted by the preliminary Theory Map v1.

---

## 8. Corrected interpretation

The strongest accurate statement is:

\[
\boxed{
\begin{array}{c}
\text{the tensor complex is a canonical alternative presentation}\\
\text{of the reduced degree-zero and zero-moment degree-one}\\
\text{defect spaces of the affine incidence pair.}
\end{array}
}
\]

More concretely,

\[
H_f^0/\Gamma\cong H_0(\text{tensor complex}),
\]

\[
\ker(H_f^1\to\Lambda^2\Gamma)
\cong H_1(\text{tensor complex}),
\]

and

\[
H_f^1\cong\operatorname{coker}T_f.
\]

A canonical chain-level quotient or quasi-isomorphism has not been established.

---

## 9. Consequences for the architecture

The exact hierarchy is now:

1. **affine incidence pair** — compatibility geometry;
2. **quotient-sheaf complex** — primal two-term coordinate presentation;
3. **stress intersection** — dual presentation;
4. **tensor complex** — canonical alternative presentation of reduced global
   sections, the full obstruction cokernel and its zero-wedge-moment subspace;
5. **rank-three quadratic enhancement** — identifies primal and dual reduced
   spaces;
6. **support and residue** — observables detecting the affine class against the
   stress quotient.

Thus “the tensor complex is a reduced compression” was directionally correct
but insufficiently precise. The comparison theorem above is the exact
replacement.
