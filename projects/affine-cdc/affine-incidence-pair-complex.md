# The affine incidence-pair complex

**Date:** 2026-07-15  
**Status:** theorem-level structural draft; not yet independently audited or
Lean-formalized in this presentation.

This note upgrades the affine incidence pair from a tuple of subspaces to the
canonical two-term complex that simultaneously carries global sections,
obstructions, stresses and the affine compatibility equation.

Let \(E\) be a finite-dimensional vector space over \(\mathbf F_2\), let
\(L,M\le E\), and let \(C=\kappa+L\) be an affine coset. In AffineCDC these are

\[
E=E_f,
\qquad
L=L_{\mathrm{vert}},
\qquad
M=L_{\mathrm{edge}}.
\]

---

## 1. The pair complex

Define the two-term complex

\[
\boxed{
\mathcal P(L,M):
L\oplus M
\xrightarrow{d}
E,
\qquad
d(l,m)=l+m.
}
\]

Its cohomology is

\[
\boxed{
H^0(\mathcal P(L,M))
\cong
L\cap M
}
\]

through

\[
z\longmapsto(z,z),
\]

and

\[
\boxed{
H^1(\mathcal P(L,M))
\cong
E/(L+M).
}
\]

The affine equation

\[
d(l,m)=\kappa
\]

is equivalent to

\[
\kappa+l\in M,
\]

hence to

\[
(\kappa+L)\cap M\ne\varnothing.
\]

If solvable, its solution space is a torsor under

\[
H^0(\mathcal P(L,M))\cong L\cap M.
\]

Its obstruction is exactly

\[
[\kappa]\in H^1(\mathcal P(L,M))=E/(L+M).
\]

Thus the affine intersection problem is an ordinary inhomogeneous equation in
a canonical two-term complex.

---

## 2. Quotient presentation and canonical quasi-isomorphism

Consider the quotient complex

\[
\mathcal Q(L,M):
L\longrightarrow E/M,
\qquad
l\longmapsto[l].
\]

There is a canonical short exact sequence of complexes

\[
\boxed{
0\longrightarrow
[M\xrightarrow{\mathrm{id}}M]
\longrightarrow
\mathcal P(L,M)
\longrightarrow
\mathcal Q(L,M)
\longrightarrow0.
}
\]

The first map is

\[
m\longmapsto(0,m)
\]

in degree zero and the inclusion \(M\hookrightarrow E\) in degree one. The
quotient identifies degree zero with \(L\) and degree one with \(E/M\).

The complex

\[
[M\xrightarrow{\mathrm{id}}M]
\]

is contractible. Therefore

\[
\boxed{
\mathcal P(L,M)
\simeq
\mathcal Q(L,M)
}
\]

by a canonical quasi-isomorphism.

Exchanging \(L\) and \(M\) gives a second quotient presentation

\[
M\longrightarrow E/L.
\]

The pair complex is the symmetric source from which both asymmetric quotient
presentations arise by cancelling a contractible summand.

---

## 3. Application to the quotient sheaf

For AffineCDC put

\[
E=E_f,
\qquad
L=L_{\mathrm{vert}},
\qquad
M=L_{\mathrm{edge}}.
\]

Then

\[
\boxed{
\mathcal P_f:
L_{\mathrm{vert}}\oplus L_{\mathrm{edge}}
\xrightarrow{+}
E_f
}
\]

is the affine incidence-pair complex.

Under

\[
L_{\mathrm{vert}}\cong\Gamma^{V(G)}
\]

and

\[
E_f/L_{\mathrm{edge}}
\cong
\bigoplus_e\Gamma/\langle f(e)\rangle,
\]

the quotient complex

\[
L_{\mathrm{vert}}
\longrightarrow
E_f/L_{\mathrm{edge}}
\]

is exactly the quotient-sheaf cochain complex

\[
\Gamma^{V(G)}
\xrightarrow{\delta_f}
\bigoplus_e\Gamma/\langle f(e)\rangle.
\]

Consequently

\[
\boxed{
H^0(\mathcal P_f)
\cong
H^0(G;\mathscr Q_f)
}
\]

and

\[
\boxed{
H^1(\mathcal P_f)
\cong
H^1(G;\mathscr Q_f).
}
\]

The canonical local datum \(\kappa\in E_f\) defines the same affine obstruction
class in either presentation.

---

## 4. The dual pair complex

Dualizing gives

\[
\mathcal P(L,M)^*:
E^*
\xrightarrow{d^*}
L^*\oplus M^*,
\]

where

\[
d^*(\phi)=(\phi|_L,\phi|_M).
\]

Its degree-zero kernel is

\[
\ker d^*
=
L^\perp\cap M^\perp
=
(L+M)^\perp
\cong
H^1(\mathcal P(L,M))^*.
\]

Its degree-one cokernel is

\[
\operatorname{coker}d^*
\cong
(L\cap M)^*
\cong
H^0(\mathcal P(L,M))^*.
\]

For AffineCDC,

\[
L_{\mathrm{vert}}^\perp
\cap
L_{\mathrm{edge}}^\perp
=
\operatorname{Stress}(f).
\]

Hence the stress space is the degree-zero cohomology of the dual pair complex.
The Fredholm solvability criterion is simply

\[
[\kappa]=0
\iff
\phi(\kappa)=0
\quad
\text{for every }
\phi\in H^0(\mathcal P_f^*).
\]

---

## 5. Rank-three Lagrangian self-duality

Assume \(E\) carries a nondegenerate alternating form \(B\) and that \(L,M\)
are Lagrangian. Then

\[
(L+M)^\perp=L\cap M.
\]

Therefore \(B\) induces a perfect pairing

\[
\boxed{
(L\cap M)
\times
E/(L+M)
\longrightarrow
\mathbf F_2,
\qquad
(z,[x])\longmapsto B(z,x).
}
\]

Thus

\[
\boxed{
H^0(\mathcal P(L,M))
\cong
H^1(\mathcal P(L,M))^*.
}
\]

In rank-three AffineCDC, the direct sum of the canonical polar forms on the edge
quotients makes both

\[
L_{\mathrm{vert}}
\quad\text{and}\quad
L_{\mathrm{edge}}
\]

Lagrangian. The global Fano cohomological duality is therefore the standard
intersection-quotient duality of a Lagrangian pair.

This identifies the source of the global duality without a dimension count and
without constructing vertexwise inverses separately.

---

## 6. Characteristic torsor and compatibility

Let \(q\) be a quadratic refinement of \(B\). Suppose

\[
\kappa+L
=
\operatorname{Char}_q(L)
\]

and \(M\) is totally singular.

For \(z\in L\cap M\),

\[
B(z,\kappa)=q(z)=0.
\]

Hence \(\kappa\in(L\cap M)^\perp=L+M\), so

\[
[\kappa]=0\in H^1(\mathcal P(L,M)).
\]

Equivalently,

\[
\operatorname{Char}_q(L)\cap M\ne\varnothing.
\]

Thus the affine Lagrangian-intersection theorem is the statement that the
canonical inhomogeneous class of the pair complex vanishes.

---

## 7. Position in the Theory Map

The central compatibility object should now be read as the affine complex

\[
\boxed{
(\mathcal P_f,\kappa):
L_{\mathrm{vert}}\oplus L_{\mathrm{edge}}
\xrightarrow{+}
E_f,
\qquad
\kappa\in E_f.
}
\]

Its projections are:

| Construction | Image of the pair complex |
|---|---|
| global sections | \(H^0(\mathcal P_f)\) |
| affine obstruction | \([\kappa]\in H^1(\mathcal P_f)\) |
| quotient sheaf | cancel the contractible edge-diagonal subcomplex |
| stresses | \(H^0(\mathcal P_f^*)\) |
| Fredholm criterion | dual evaluation on \([\kappa]\) |
| Fano self-duality | Lagrangian intersection-quotient pairing |
| characteristic compatibility | vanishing of the affine \(H^1\)-class |
| tensor complex | canonical comparison with reduced \(H^0\) and zero-moment \(H^1\) |

The pair complex is therefore a more precise centre than either the quotient
sheaf alone or the bare tuple of incidence subspaces.
