# The Fano quadratic Lagrangian package

**Date:** 2026-07-15  
**Status:** theorem-level structural draft; not yet independently audited or Lean-formalized in this presentation.

This note packages the local affine classification, local Fano duality,
cross-bit/support parity and the global compatibility cancellation into one
quadratic-symplectic object.

Let

\[
\Gamma=\mathbf F_2^3,
\qquad
W\le\Gamma,
\qquad
\dim W=2.
\]

Write

\[
D=W\setminus\{0\}.
\]

Thus \(D\) is the three-point line of the Fano plane.

---

## 1. The local quadratic space

For each \(h\in D\), define

\[
Q_h=\Gamma/\langle h\rangle.
\]

The binary plane \(Q_h\) has the canonical anisotropic quadratic form

\[
q_h(u)=\mathbf 1_{u\ne0}.
\]

Its polarization

\[
B_h(u,v)=q_h(u+v)+q_h(u)+q_h(v)
\]

is the unique nonzero alternating form on \(Q_h\). If

\[
\omega\in\Lambda^3\Gamma^*
\]

is the unique nonzero volume form, then

\[
B_h([x],[y])=\omega(h,x,y).
\]

Put

\[
E_W=\bigoplus_{h\in D}Q_h,
\qquad
q_W=\sum_{h\in D}q_h,
\qquad
B_W=\sum_{h\in D}B_h.
\]

Then \((E_W,q_W)\) is a six-dimensional nondegenerate quadratic space, with
underlying symplectic form \(B_W\).

---

## 2. The diagonal Lagrangian

Define

\[
\Delta_W:\Gamma\to E_W,
\qquad
\Delta_W(x)=([x]_h)_{h\in D}.
\]

### Theorem 2.1

The image

\[
L_W:=\operatorname{im}\Delta_W
\]

is a Lagrangian subspace of \((E_W,B_W)\).

### Proof

The map is injective because

\[
\bigcap_{h\in D}\langle h\rangle=0.
\]

For \(x,y\in\Gamma\),

\[
\begin{aligned}
B_W(\Delta_Wx,\Delta_Wy)
&=
\sum_{h\in D}\omega(h,x,y)\\
&=
\omega\!\left(\sum_{h\in D}h,x,y\right)\\
&=0,
\end{aligned}
\]

since the three nonzero elements of \(W\) sum to zero. Thus \(L_W\) is
isotropic. Its dimension is three, half the dimension of \(E_W\), so it is
Lagrangian.

---

## 3. The quadratic restriction

Let

\[
\ell_W:\Gamma\to\mathbf F_2
\]

be the unique nonzero linear functional with kernel \(W\).

### Theorem 3.1 — Fano quadratic transgression

\[
\boxed{
q_W(\Delta_Wx)=\ell_W(x).
}
\]

Indeed,

\[
q_W(\Delta_Wx)
=
\sum_{h\in D}\mathbf 1_{x\notin\langle h\rangle}.
\]

This is zero for \(x=0\), zero for \(x\in W\setminus\{0\}\) because exactly two
terms are nonzero, and one for \(x\notin W\) because all three terms are
nonzero.

Thus the quadratic form restricts to a linear functional on the Lagrangian:

\[
q_W|_{L_W}=\ell_W\circ\Delta_W^{-1}.
\]

The linearity also follows abstractly from \(B_W|_{L_W}=0\).

---

## 4. The characteristic torsor

Define

\[
\operatorname{Char}(W)
=
\left\{
\kappa\in E_W:
B_W(z,\kappa)=q_W(z)
\text{ for every }z\in L_W
\right\}.
\]

Because \(q_W|_{L_W}\) is linear and \(B_W\) is nondegenerate,
\(\operatorname{Char}(W)\) is nonempty. Two representatives differ by an
element of

\[
L_W^\perp=L_W.
\]

Hence

\[
\boxed{
\operatorname{Char}(W)
\text{ is an affine torsor under }L_W\cong\Gamma.
}
\]

For \(h\in D\), let

\[
\kappa_h\in Q_h
\]

be the common class of the other two elements of \(D\). This is well defined
because those two elements differ by \(h\). Put

\[
\kappa_W=(\kappa_h)_{h\in D}\in E_W.
\]

### Theorem 4.1

\[
\boxed{
\kappa_W\in\operatorname{Char}(W),
\qquad
\operatorname{Char}(W)=\kappa_W+L_W.
}
\]

For \(z=\Delta_Wx\), the identity

\[
B_W(z,\kappa_W)=\ell_W(x)=q_W(z)
\]

is exactly the local cross-pairing identity. Therefore every element of the
characteristic torsor has the form

\[
\kappa_W+\Delta_Wm,
\qquad m\in\Gamma.
\]

Componentwise this is

\[
(\kappa_h+[m]_h)_{h\in D},
\]

which is precisely the quotient-label formula for the local affine family.

Thus:

\[
\boxed{
\text{local affine-family space}
=
\text{characteristic torsor of the Fano Lagrangian}.
}
\]

Moreover, \(q_W\) is constant on this torsor. Indeed, for \(z\in L_W\),

\[
q_W(\kappa_W+z)
=
q_W(\kappa_W)+q_W(z)+B_W(\kappa_W,z)
=
q_W(\kappa_W).
\]

Since all three components of \(\kappa_W\) are nonzero,

\[
q_W(\kappa_W)=1.
\]

Hence \(\operatorname{Char}(W)\) is an anisotropic affine Lagrangian coset.

---

## 5. Legal dual configurations are the same Lagrangian

Use \(B_h\) to identify

\[
Q_h\cong\operatorname{Ann}(h).
\]

A tuple \(z=(z_h)\in E_W\) corresponds to covectors

\[
\eta_h(x)=B_h(z_h,[x])=\omega(h,z_h,x).
\]

The legal dual-configuration condition is

\[
\sum_{h\in D}\eta_h=0.
\]

This holds exactly when, for every \(x\in\Gamma\),

\[
0
=
\sum_hB_h(z_h,[x])
=
B_W(z,\Delta_Wx).
\]

Therefore

\[
z\in L_W^\perp=L_W.
\]

Consequently:

\[
\boxed{
\operatorname{DualConfig}(W)
\cong
L_W
\cong
\Gamma.
}
\]

Under this identification, a legal configuration is \(z=\Delta_Wa\), and its
cross-bit is

\[
q_W(z)=\ell_W(a).
\]

But

\[
q_W(z)=\sum_{h\in D}q_h(z_h)
\]

is exactly the parity of the number of nonzero components. Hence the old
branching identity becomes the tautology

\[
\boxed{
\text{cross-bit of }z
=
q_W(z)
=
\text{support parity of }z.
}
\]

This replaces the annihilator-uniqueness and zero/nonzero case split by the
restriction of one quadratic form to one Lagrangian.

---

## 6. Global compatibility in one line

Let \(G\) be a finite cubic graph with a nowhere-zero
\(\mathbf F_2^3\)-flow. At every vertex \(v\), form the local package

\[
(E_v,q_v,L_v,\operatorname{Char}(v)).
\]

Let \(\eta\) be an equilibrium stress, viewed on each edge quotient via the
polar forms \(B_e\). At a vertex, the tuple of incident stress vectors is a
legal dual configuration

\[
z_v\in L_v.
\]

Let

\[
\kappa_v\in\operatorname{Char}(v)
\]

be the canonical local affine datum. The global affine obstruction is obtained
by adding the two endpoint components along every edge. Therefore its pairing
with \(\eta\) decomposes vertexwise:

\[
\eta(c_f)
=
\sum_v B_v(z_v,\kappa_v).
\]

By the characteristic property,

\[
B_v(z_v,\kappa_v)=q_v(z_v).
\]

Hence

\[
\begin{aligned}
\eta(c_f)
&=
\sum_vq_v(z_v)\\
&=
\sum_v\sum_{e\ni v}q_e(z_e)\\
&=
2\sum_eq_e(z_e)\\
&=0.
\end{aligned}
\]

Thus every equilibrium stress annihilates \(c_f\). By the finite-dimensional
dual solvability criterion,

\[
\boxed{
c_f\in\operatorname{im}\delta_f.
}
\]

This is the rank-three Fano compatibility theorem.

The complete mathematical core is therefore:

\[
\boxed{
\text{characteristic Fano torsors}
+
\text{Lagrangian stress condition}
+
\text{each edge counted twice}.
}
\]

---

## 7. Relation to the support-boundary proof

For \(z_v\in L_v\), the quantity

\[
q_v(z_v)
\]

is the parity of its nonzero incident components. Recording those components as
an edge-support chain \(s\) gives

\[
q_v(z_v)=(\partial s)_v.
\]

Therefore the support-boundary identity

\[
\varepsilon\partial s=0
\]

is the support projection of the quadratic-Lagrangian proof above.

The quadratic package is stronger: it simultaneously identifies

- local affine families with a characteristic torsor;
- legal dual configurations with a Lagrangian;
- cross-bit with the restricted quadratic form;
- branching with support parity;
- global compatibility with quadratic handshaking.

---

## 8. Consequences for the project architecture

The primitive local object is not an exact balanced flag. It is the package

\[
\boxed{
(E_W,q_W,L_W,\operatorname{Char}(W)).
}
\]

Exact balancedness belongs to the later global interpolation-rigidity theory.
The local quadratic Lagrangian package instead explains the original affine
classification and the exceptional Fano compatibility theorem even when the
global interpolation operator is singular.

For Paper 1, this package is a candidate replacement for the separate
cross-bit, annihilator-uniqueness and branching sections. The existing Lean
proof remains the verified implementation until this compression is
independently audited and formalized.
