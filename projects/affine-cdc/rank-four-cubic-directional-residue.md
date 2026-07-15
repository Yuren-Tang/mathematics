# The rank-four cubic directional residue

**Date:** 2026-07-15  
**Status:** theorem-level structural draft; finite-field identities checked exhaustively, not yet independently audited or Lean-formalized.

This note isolates the first obstruction that survives beyond the rank-three
quadratic-Lagrangian theorem.

Let

\[
\Gamma=\mathbf F_2^4
\]

and let \(W\le\Gamma\) be a plane. Write

\[
D=W\setminus\{0\}.
\]

A legal dual configuration is a triple

\[
\eta=(\eta_h)_{h\in D},
\qquad
\eta_h\in\operatorname{Ann}(h),
\qquad
\sum_{h\in D}\eta_h=0.
\]

---

## 1. Legal configurations as alternating two-forms

Define

\[
A_W:\Lambda^2\Gamma^*\longrightarrow\operatorname{DualConfig}(W),
\qquad
A_W(\alpha)_h(x)=\alpha(h,x).
\]

### Theorem 1.1

There is a canonical short exact sequence

\[
\boxed{
0\longrightarrow
\Lambda^2(\Gamma/W)^*
\longrightarrow
\Lambda^2\Gamma^*
\overset{A_W}{\longrightarrow}
\operatorname{DualConfig}(W)
\longrightarrow0.
}
\]

### Proof

The image is legal because \(\alpha(h,h)=0\) and

\[
\sum_{h\in D}\alpha(h,-)
=
\alpha\!\left(\sum_{h\in D}h,-\right)
=0.
\]

The kernel consists precisely of alternating forms satisfying

\[
\alpha(W,\Gamma)=0,
\]

which are the forms descending from \(\Gamma/W\).

For surjectivity, the summation map

\[
\bigoplus_{h\in D}\operatorname{Ann}(h)\to\Gamma^*
\]

is onto: the annihilators of two distinct directions already span
\(\Gamma^*\). Hence

\[
\dim\operatorname{DualConfig}(W)
=3(4-1)-4=5.
\]

The quotient on the left also has dimension

\[
\binom42-\binom22=5.
\]

Thus the induced injection is an isomorphism.

More generally, in rank \(r\), legal configurations are

\[
\Lambda^2\Gamma^*/\Lambda^2(\Gamma/W)^*,
\]

of dimension \(2r-3\). Rank three is the special case in which the kernel
vanishes.

---

## 2. The linear cross-bit

Let \(h_1,h_2,h_3\) be the three nonzero elements of \(W\), with

\[
h_1+h_2+h_3=0.
\]

For \(\eta=A_W(\alpha)\), define

\[
\beta_W(\eta)=\alpha(h_1,h_2).
\]

This is independent of the representative \(\alpha\), because forms descending
from \(\Gamma/W\) vanish whenever one argument lies in \(W\). It is also
independent of the chosen ordered pair of distinct Fano directions.

If \(\kappa_h\in\Gamma/\langle h\rangle\) is the common class of the other two
Fano directions, then

\[
\boxed{
\sum_{h\in D}\eta_h(\kappa_h)=\beta_W(\eta).
}
\]

Indeed, taking cyclic representatives gives

\[
\alpha(h_1,h_2)+\alpha(h_2,h_3)+\alpha(h_3,h_1)
=
\alpha(h_1,h_2).
\]

Thus \(\beta_W\) remains the local affine-obstruction pairing in rank four.

---

## 3. The Pfaffian quadratic form

Choose the unique nonzero volume form

\[
\Omega\in\Lambda^4\Gamma^*.
\]

It determines the divided-square or Pfaffian quadratic form

\[
\operatorname{Pf}:\Lambda^2\Gamma^*\to\mathbf F_2.
\]

In a basis \(e_1,e_2,e_3,e_4\), writing

\[
\alpha=
 a\,e_{12}+b\,e_{13}+c\,e_{14}
 +d\,e_{23}+e\,e_{24}+f\,e_{34},
\]

one has

\[
\operatorname{Pf}(\alpha)=af+be+cd.
\]

Its polar form is the wedge pairing:

\[
B_{\operatorname{Pf}}(\alpha,\gamma)
=
\frac{\alpha\wedge\gamma}{\Omega}.
\]

Let

\[
K_W=\Lambda^2(\Gamma/W)^*.
\]

This is a line. Let \(\tau_W\) be its unique nonzero element. Then

\[
\operatorname{Pf}(\tau_W)=0
\]

and

\[
B_{\operatorname{Pf}}(\alpha,\tau_W)=\beta_W(A_W(\alpha)).
\]

Consequently,

\[
\operatorname{Pf}(\alpha+\tau_W)
=
\operatorname{Pf}(\alpha)+\beta_W(A_W(\alpha)).
\]

---

## 4. The cubic directional residue

### Definition

For a legal configuration \(\eta=A_W(\alpha)\), define

\[
\boxed{
\rho_W(\eta)
=
(1+\beta_W(\eta))\operatorname{Pf}(\alpha).
}
\]

This is independent of the representative \(\alpha\). Indeed, replacing
\(\alpha\) by \(\alpha+\tau_W\) changes the Pfaffian by \(\beta_W(\eta)\), and

\[
(1+\beta_W)\beta_W=0.
\]

As a Boolean polynomial on the five-dimensional legal-configuration space,
\(\rho_W\) has degree three. This is the **rank-four cubic directional
residue**.

### Geometric interpretation

If \(\beta_W(\eta)=1\), then

\[
\rho_W(\eta)=0.
\]

If \(\beta_W(\eta)=0\), the form \(\alpha\) vanishes on \(W\times W\) and
induces a cross-pairing

\[
T_\eta:W\longrightarrow(\Gamma/W)^*,
\qquad
T_\eta(w)(\bar x)=\alpha(w,x).
\]

Then

\[
\rho_W(\eta)=\det T_\eta.
\]

Therefore

\[
\boxed{
\rho_W(\eta)=1
}
\]

exactly when

1. \(W\) is isotropic for the local alternating form; and
2. the induced pairing
   \(W\times\Gamma/W\to\mathbf F_2\) is perfect.

Equivalently, the plane is isotropic but transverse to the radical in the
strongest possible way.

---

## 5. Failure of the rank-three branching identity

Let

\[
\sigma_W(\eta)
=
\sum_{h\in D}\mathbf1_{\eta_h\ne0}
\]

be the parity of the local stress support.

### Theorem 5.1

\[
\boxed{
\sigma_W(\eta)
=
\beta_W(\eta)+\rho_W(\eta).
}
\]

### Proof

If \(\beta_W(\eta)=1\), the restriction of \(\alpha\) to \(W\) is
nondegenerate. Hence no nonzero \(h\in W\) lies in the radical, so all three
components \(\eta_h=\alpha(h,-)\) are nonzero. Thus

\[
\sigma_W=1=\beta_W,
\qquad
\rho_W=0.
\]

Suppose \(\beta_W(\eta)=0\). Then

\[
\eta_h=0
\iff
T_\eta(h)=0.
\]

For a linear map between binary planes, the parity of the number of nonzero
vectors with nonzero image is one exactly when the map has rank two. Hence

\[
\sigma_W(\eta)=\det T_\eta=\rho_W(\eta).
\]

This proves the identity.

In coordinates adapted to \(W=\langle e_1,e_2\rangle\), with the representative
chosen to have \(f=0\), the formula is

\[
\beta_W=a,
\qquad
\rho_W=(1+a)(be+cd).
\]

Thus the first failure of support parity is genuinely cubic.

---

## 6. The global residue formula

Let \(G\) be a finite cubic graph with a nowhere-zero rank-four flow, and let
\(\psi\) be an equilibrium stress. At every vertex \(v\), its three incident
components form a legal configuration

\[
\psi_v\in\operatorname{DualConfig}(W_v).
\]

The affine-obstruction pairing decomposes as

\[
\psi(c_f)
=
\sum_v\beta_{W_v}(\psi_v).
\]

On the other hand, every nonzero edge stress is counted at its two endpoints,
so

\[
\sum_v\sigma_{W_v}(\psi_v)=0.
\]

Using Theorem 5.1 gives the exact rank-four formula

\[
\boxed{
\psi(c_f)
=
\sum_{v\in V(G)}\rho_{W_v}(\psi_v).
}
\]

Therefore:

\[
\boxed{
[c_f]=0
\iff
\sum_v\rho_{W_v}(\psi_v)=0
\text{ for every equilibrium stress }\psi.
}
\]

The rank-four obstruction is precisely the parity of the vertices carrying a
nonzero cubic directional residue.

Although each \(\rho_{W_v}\) is cubic locally, their sum restricts to the
linear functional

\[
\psi\longmapsto\psi(c_f)
\]

on the global equilibrium-stress space. The nonlinear local densities
linearize globally because the support-parity terms cancel by handshaking.

---

## 7. The first essential-obstruction layer

For a connected cubic rank-four flow on \(n\) vertices,

\[
\dim\operatorname{EssStress}(f)
=
\dim\mathcal B_f+\frac{n-4}{2}.
\]

Thus rank four has dimensionally forced essential stress directions. The cubic
residue formula identifies what these directions measure.

In the smallest gauge-rigid six-vertex case,

\[
\dim\operatorname{EssStress}(f)=1.
\]

The unique nonzero essential stress detects incompatibility exactly when its
local cubic residues occur at an odd number of vertices.

This is the expected mechanism in the known rank-four \(K_{3,3}\) example.

---

## 8. Relation to the rank-three theorem

At rank three,

\[
\Lambda^2(\Gamma/W)^*=0.
\]

Hence every legal configuration has a unique alternating-form representative,
and the cubic residue disappears:

\[
\rho_W\equiv0.
\]

The local identity reduces to

\[
\sigma_W=\beta_W,
\]

which is exactly the Fano branching theorem.

Thus the rank-three compatibility theorem and the rank-four obstruction are
consecutive layers of one hierarchy:

\[
\boxed{
\begin{array}{c|c}
\text{rank three}&\text{quadratic support parity closes}\cr
\text{rank four}&\text{a cubic Pfaffian residue survives}.
\end{array}
}
\]

The divided-square/Pfaffian structure is therefore not an unrelated general
extension. It is the first correction term beyond the Fano quadratic
Lagrangian regime.
