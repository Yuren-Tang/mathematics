# Symplectic vertex-plane parity

**Date:** 2026-07-15  
**Status:** short theorem-level corollary; not yet Lean-formalized.

Let \(G\) be a finite cubic graph and let

\[
f:E(G)\to\Gamma,
\qquad
\Gamma=\mathbf F_2^4,
\]

be a nowhere-zero flow. At every vertex \(v\), the three incident flow values
are the three nonzero points of a plane

\[
W_v\le\Gamma.
\]

Fix a nondegenerate alternating form

\[
\alpha\in\Lambda^2\Gamma^*.
\]

A plane \(W_v\) is \(\alpha\)-Lagrangian exactly when

\[
\alpha|_{W_v}=0.
\]

---

## Theorem

\[
\boxed{
\#\{v\in V(G):W_v\text{ is }\alpha\text{-Lagrangian}\}
\equiv0\pmod2.
}
\]

### Proof

At a vertex \(v\), choose two distinct incident flow values \(h_{v,1},h_{v,2}\)
and put

\[
q_v=h_{v,1}\wedge h_{v,2}\in\Lambda^2\Gamma.
\]

This is independent of the chosen pair because the third value is their sum.
The wedge--handshake identity gives

\[
\sum_vq_v=0.
\]

Applying \(\alpha\) yields

\[
\sum_v\alpha(h_{v,1},h_{v,2})=0.
\]

Since \(W_v\) is two-dimensional, the restriction of \(\alpha\) to \(W_v\) is
either zero or the unique nonzero alternating form. Hence

\[
\alpha(h_{v,1},h_{v,2})
=
\begin{cases}
0,&W_v\text{ is }\alpha\text{-Lagrangian},\\
1,&W_v\text{ is not }\alpha\text{-Lagrangian}.
\end{cases}
\]

Therefore the number of non-Lagrangian vertex planes is even.

A finite cubic graph has an even number of vertices, because

\[
3|V|=2|E|.
\]

Subtracting the even number of non-Lagrangian vertices from the even total
shows that the number of Lagrangian vertex planes is even.

---

## Relation to the cubic directional residue

For the global alternating stress

\[
\psi_e(x)=\alpha(f(e),x),
\]

all edge covectors are nonzero because \(\alpha\) is symplectic. At a vertex,
the rank-four cubic residue is therefore

\[
\rho_v(\psi)=1
\iff
W_v\text{ is }\alpha\text{-Lagrangian}.
\]

The theorem is thus the statement

\[
\sum_v\rho_v(\psi)=0
\]

for every stress arising from one global symplectic form.

An essential stress may instead be represented by local alternating forms
\(\alpha_v\) whose edge contractions agree but which do not arise from one
global \(\alpha\). Its affine obstruction is the parity

\[
\sum_v\mathbf1_{W_v\text{ is }\alpha_v\text{-Lagrangian}}.
\]

Hence rank-four incompatibility is a **symplectic parity anomaly**: a locally
compatible field of symplectic forms can have an odd number of Lagrangian
vertex planes even though every global symplectic form obeys the even-parity
law.

The canonical rank-four \(K_{3,3}\) example is the smallest such anomaly.
