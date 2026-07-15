# Affine Lagrangian intersection and AffineCDC

**Date:** 2026-07-15  
**Status:** theorem-level structural draft; terminology provisional; not yet independently audited or Lean-formalized in this presentation.

This note gives a global quadratic-space formulation of AffineCDC. The local Fano packages assemble into two Lagrangians:

- a vertex Lagrangian whose characteristic torsor is the space of all local affine families;
- an edge-diagonal Lagrangian expressing equality of the two endpoint labels.

Compatibility is their affine intersection.

---

## 1. An abstract intersection theorem

Let \((E,q)\) be a finite-dimensional nondegenerate quadratic space over \(\mathbf F_2\), and let

\[
B(x,y)=q(x+y)+q(x)+q(y)
\]

be its polar symplectic form.

Let \(L\le E\) be a Lagrangian subspace. Since \(B|_L=0\), the restriction \(q|_L\) is linear. Define the characteristic torsor of \(L\) by

\[
\operatorname{Char}_q(L)
=
\left\{
\kappa\in E:
B(z,\kappa)=q(z)
\text{ for every }z\in L
\right\}.
\]

The restriction map

\[
E\longrightarrow L^*,
\qquad
\kappa\longmapsto B(-,\kappa)|_L
\]

is surjective and has kernel \(L^\perp=L\). Hence \(\operatorname{Char}_q(L)\) is a nonempty affine torsor under \(L\).

Let \(M\le E\) be another Lagrangian.

### Theorem 1.1 — exact intersection criterion

\[
\boxed{
\operatorname{Char}_q(L)\cap M\ne\varnothing
\iff
q|_{L\cap M}=0.
}
\]

If the intersection is nonempty, it is an affine torsor under \(L\cap M\).

### Proof

Suppose \(m\in\operatorname{Char}_q(L)\cap M\). For \(z\in L\cap M\),

\[
q(z)=B(z,m)=0,
\]

because \(z,m\in M\) and \(M\) is isotropic.

Conversely, choose \(\kappa\in\operatorname{Char}_q(L)\) and suppose \(q|_{L\cap M}=0\). Then for every \(z\in L\cap M\),

\[
B(z,\kappa)=q(z)=0.
\]

Thus

\[
\kappa\in(L\cap M)^\perp.
\]

For Lagrangians,

\[
(L\cap M)^\perp=L+M.
\]

Hence \(\kappa=\ell+m\) for some \(\ell\in L\) and \(m\in M\). Since \(\operatorname{Char}_q(L)=\kappa+L\),

\[
m=\kappa+\ell\in\operatorname{Char}_q(L)\cap M.
\]

Finally, the difference of two intersection points lies in both \(L\) and \(M\), while adding an element of \(L\cap M\) preserves the intersection. Therefore the intersection is a torsor under \(L\cap M\).

### Corollary 1.2

If \(M\) is **totally singular**, meaning

\[
q|_M=0,
\]

then

\[
\boxed{
\operatorname{Char}_q(L)\cap M\ne\varnothing.
}
\]

This is the form used by AffineCDC.

---

## 2. The global incidence quadratic space

Let \(G\) be a finite cubic graph with a nowhere-zero flow

\[
f:E(G)\to\Gamma,
\qquad
\Gamma=\mathbf F_2^3.
\]

For every edge \(e\), put

\[
Q_e=\Gamma/\langle f(e)\rangle.
\]

The binary plane \(Q_e\) carries the canonical anisotropic quadratic form

\[
q_e(x)=\mathbf 1_{x\ne0}.
\]

Let

\[
I(G)=\{(v,e):v\in e\}
\]

be the incidence set, and define

\[
\mathbb E_f
=
\bigoplus_{(v,e)\in I(G)}Q_e,
\qquad
q_f
=
\sum_{(v,e)\in I(G)}q_e.
\]

Its polar form is the direct sum of the nondegenerate polar forms on the edge quotients. Thus \((\mathbb E_f,q_f)\) is a nondegenerate quadratic space.

Every edge quotient appears twice, once at each endpoint.

---

## 3. The vertex Lagrangian

At a vertex \(v\), the three incident flow values are the three nonzero elements of a plane

\[
W_v\le\Gamma.
\]

Put

\[
\mathbb E_v
=
\bigoplus_{e\ni v}Q_e.
\]

The local diagonal map is

\[
\Delta_v:\Gamma\to\mathbb E_v,
\qquad
\Delta_v(x)=([x]_e)_{e\ni v}.
\]

Its image

\[
L_v=\operatorname{im}\Delta_v
\]

is the local Fano Lagrangian. The local affine-family space is its characteristic torsor

\[
\operatorname{Char}_{q_v}(L_v)
=
\kappa_v+L_v.
\]

Taking direct sums gives

\[
L_{\mathrm{vert}}
=
\bigoplus_vL_v
\le\mathbb E_f
\]

and

\[
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
=
\bigoplus_v\operatorname{Char}_{q_v}(L_v).
\]

Thus:

\[
\boxed{
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
=
\text{all choices of one local affine family at every vertex}.
}
\]

Since each \(L_v\) is Lagrangian, \(L_{\mathrm{vert}}\) is Lagrangian.

---

## 4. The edge-diagonal Lagrangian

For an edge \(e=uv\), its two incidence copies form

\[
Q_e^{(u)}\oplus Q_e^{(v)}.
\]

Define the edge diagonal

\[
D_e
=
\{(x,x):x\in Q_e\}.
\]

It is Lagrangian for the polar form, and it is totally singular because

\[
q_e(x)+q_e(x)=0.
\]

Put

\[
L_{\mathrm{edge}}
=
\bigoplus_{e\in E(G)}D_e.
\]

Then \(L_{\mathrm{edge}}\) is a totally singular Lagrangian in \((\mathbb E_f,q_f)\).

Membership in \(L_{\mathrm{edge}}\) says exactly that the two quotient labels assigned to an edge by its endpoints agree.

Therefore:

\[
\boxed{
\text{compatible global affine families}
=
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
\cap
L_{\mathrm{edge}}.
}
\]

---

## 5. Compatibility as affine Lagrangian intersection

Apply Corollary 1.2 with

\[
L=L_{\mathrm{vert}},
\qquad
M=L_{\mathrm{edge}}.
\]

Because \(L_{\mathrm{edge}}\) is totally singular,

\[
q_f|_{L_{\mathrm{vert}}\cap L_{\mathrm{edge}}}=0.
\]

Hence

\[
\boxed{
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
\cap
L_{\mathrm{edge}}
\ne\varnothing.
}
\]

Thus there exists a choice of local affine families whose labels agree across every edge. This is the Fano compatibility theorem.

The entire existence proof is the abstract fact that a characteristic torsor of one Lagrangian meets every totally singular Lagrangian.

---

## 6. The solution torsor

The abstract theorem also gives the moduli space without additional work:

\[
\boxed{
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
\cap
L_{\mathrm{edge}}
\text{ is a torsor under }
L_{\mathrm{vert}}\cap L_{\mathrm{edge}}.
}
\]

An element \(z\in L_{\mathrm{vert}}\) has a unique presentation

\[
z_{v,e}=[k_v]_e
\]

for vertex vectors \(k_v\in\Gamma\). The edge-diagonal condition is

\[
[k_u]_e=[k_v]_e,
\]

equivalently

\[
k_u+k_v\in\langle f(e)\rangle.
\]

Thus

\[
\boxed{
L_{\mathrm{vert}}\cap L_{\mathrm{edge}}
\cong
H^0(G;\mathscr Q_f).
}
\]

Consequently the compatible affine-family space is a torsor under the global section space, exactly as the original affine equation predicts.

---

## 7. Global Fano duality becomes literal intersection

Use the polar form on \(Q_e\) to identify

\[
Q_e\cong\operatorname{Ann}(f(e)).
\]

Then an element of \(L_v\) is exactly a legal dual configuration at \(v\), and the edge-diagonal condition says that the two endpoint covectors on an edge are the same. Hence the same intersection is also the equilibrium-stress space:

\[
\boxed{
L_{\mathrm{vert}}\cap L_{\mathrm{edge}}
\cong
\operatorname{Stress}(f).
}
\]

Therefore

\[
H^0(G;\mathscr Q_f)
\cong
\operatorname{Stress}(f)
\]

is not merely an accidental isomorphism. The two spaces are two descriptions of the same Lagrangian intersection inside \(\mathbb E_f\).

After quotienting constants and alternating stresses, this becomes the reduced duality

\[
\mathcal B_f\cong\operatorname{EssStress}(f)\cong\mathcal K_f^*.
\]

---

## 8. Relation to the quadratic-handshaking proof

The exact criterion says that the only possible obstruction to the affine intersection is

\[
q_f|_{L_{\mathrm{vert}}\cap L_{\mathrm{edge}}}.
\]

But an element of \(L_{\mathrm{edge}}\) has the same quotient vector at the two ends of every edge. Therefore

\[
q_f(z)
=
2\sum_eq_e(z_e)
=
0.
\]

This is exactly the earlier quadratic-handshaking calculation.

Thus the two proofs are the same statement at different resolutions:

\[
\boxed{
\begin{array}{c}
q_f|_{L_{\mathrm{vert}}\cap L_{\mathrm{edge}}}=0\\[2mm]
\Updownarrow\\[2mm]
\sum_vq_v(z_v)=2\sum_eq_e(z_e)=0\\[2mm]
\Updownarrow\\[2mm]
\varepsilon\partial s=0.
\end{array}
}
\]

The Lagrangian-intersection formulation is strongest because it simultaneously gives existence, the full solution torsor, and the global Fano duality.

---

## 9. Structural boundary

The abstract theorem is not specific to graphs or to Fano geometry. What is special to AffineCDC is the local input:

1. each edge quotient has a canonical quadratic refinement;
2. the local homogeneous family space is Lagrangian;
3. the local affine-family space is its characteristic torsor;
4. edge matching is represented by a totally singular diagonal.

Whenever another local system has the same four properties, global compatibility follows by the same intersection theorem.
