# Rank four: the first obstruction layer

**Status.** The structural formulas are theorem-level finite-field arguments.
The explicit six-vertex examples are exact computations. Neither presentation
has yet been Lean-formalized.

This chapter specializes the all-rank dual-Fano residue theorem to
$\Gamma=\mathbf F_2^4$ and collects the first positive and negative examples in
one place.

## 1. Legal configurations as alternating two-forms

Let $W\leq\Gamma$ be a plane and put

$$
D:=W\setminus\{0\}.
$$

A legal dual configuration is

$$
\eta=(\eta_h)_{h\in D},
\qquad
\eta_h\in\operatorname{Ann}(h),
\qquad
\sum_{h\in D}\eta_h=0.
$$

Define

$$
A_W:\Lambda^2\Gamma^*\longrightarrow\operatorname{DualConfig}(W),
\qquad
A_W(\alpha)_h(x)=\alpha(h,x).
$$

### Theorem 1.1

There is a canonical short exact sequence

$$
\boxed{
0\longrightarrow
\Lambda^2(\Gamma/W)^*
\longrightarrow
\Lambda^2\Gamma^*
\xrightarrow{A_W}
\operatorname{DualConfig}(W)
\longrightarrow0.
}
$$

### Proof

The image is legal because $\alpha(h,h)=0$ and

$$
\sum_{h\in D}\alpha(h,-)
=
\alpha\left(\sum_{h\in D}h,-\right)
=0.
$$

The kernel consists exactly of alternating forms satisfying

$$
\alpha(W,\Gamma)=0,
$$

which are the forms descending from $\Gamma/W$. The target has dimension

$$
3(4-1)-4=5,
$$

while the quotient on the left has dimension

$$
\binom42-\binom22=5.
$$

Hence the induced injection is an isomorphism. $\square$

In general rank the same argument gives

$$
\operatorname{DualConfig}(W)
\cong
\Lambda^2\Gamma^*/\Lambda^2(\Gamma/W)^*,
$$

of dimension $2r-3$. Rank three is the special case in which the kernel
vanishes.

## 2. The cross-bit

Let $h_1,h_2,h_3$ be the three nonzero points of $W$. For
$\eta=A_W(\alpha)$, define

$$
\beta_W(\eta):=\alpha(h_1,h_2).
$$

Forms descending from $\Gamma/W$ vanish whenever one argument lies in $W$, so
this is independent of the representative $\alpha$. It is also independent of
the chosen ordered pair of distinct Fano directions.

If $\kappa_h\in Q_h$ is the common class of the other two Fano directions, then

$$
\boxed{
\sum_{h\in D}\eta_h(\kappa_h)=\beta_W(\eta).
}
$$

Thus $\beta_W$ remains the local affine-obstruction pairing in rank four.

## 3. The Pfaffian quadratic form

Choose the unique nonzero volume form

$$
\Omega\in\Lambda^4\Gamma^*.
$$

It determines the divided-square, or Pfaffian, quadratic form

$$
\operatorname{Pf}:\Lambda^2\Gamma^*\longrightarrow\mathbf F_2.
$$

In a basis $e_1,e_2,e_3,e_4$, write

$$
\alpha
=
ae_{12}+be_{13}+ce_{14}+de_{23}+ee_{24}+fe_{34}.
$$

Then

$$
\operatorname{Pf}(\alpha)=af+be+cd.
$$

Its polar form is the wedge pairing:

$$
B_{\operatorname{Pf}}(\alpha,\gamma)
=
\frac{\alpha\wedge\gamma}{\Omega}.
$$

Let

$$
K_W:=\Lambda^2(\Gamma/W)^*.
$$

This is a line. Let $\tau_W$ be its unique nonzero element. Then

$$
\operatorname{Pf}(\tau_W)=0
$$

and

$$
B_{\operatorname{Pf}}(\alpha,\tau_W)
=
\beta_W(A_W(\alpha)).
$$

Consequently

$$
\operatorname{Pf}(\alpha+\tau_W)
=
\operatorname{Pf}(\alpha)+\beta_W(A_W(\alpha)).
$$

## 4. The cubic directional residue

For a legal configuration $\eta=A_W(\alpha)$, define

$$
\boxed{
\rho_W(\eta)
:=
(1+\beta_W(\eta))\operatorname{Pf}(\alpha).
}
$$

This is independent of the representative. Replacing $\alpha$ by
$\alpha+\tau_W$ changes the Pfaffian by $\beta_W(\eta)$, and

$$
(1+\beta_W)\beta_W=0.
$$

As a Boolean polynomial on the five-dimensional legal-configuration space,
$\rho_W$ has degree three.

If $\beta_W(\eta)=0$, the form $\alpha$ induces a cross-pairing

$$
T_\eta:W\longrightarrow(\Gamma/W)^*,
\qquad
T_\eta(w)(\bar x)=\alpha(w,x).
$$

Then

$$
\rho_W(\eta)=\det T_\eta.
$$

Therefore the following conditions are equivalent:

1. $\rho_W(\eta)=1$;
2. $W$ is isotropic for $\alpha$ and the induced pairing
   $W\times\Gamma/W\to\mathbf F_2$ is perfect;
3. the three incident covectors are the three nonzero points of
   $\operatorname{Ann}(W)$;
4. the all-rank hidden dual-Fano residue occurs.

Thus the Pfaffian cubic is the algebraic equation of the unique possible hidden
annihilator plane in rank four.

## 5. Support parity and the global obstruction

Let

$$
\sigma_W(\eta)
:=
\sum_{h\in D}\mathbf1_{\eta_h\neq0}.
$$

The all-rank residue identity specializes to

$$
\boxed{
\sigma_W(\eta)
=
\beta_W(\eta)+\rho_W(\eta).
}
$$

For a cubic graph with a nowhere-zero rank-four flow and an equilibrium stress
$\psi$, every nonzero edge covector is counted at two endpoints, so

$$
\sum_v\sigma_{W_v}(\psi_v)=0.
$$

The affine pairing is

$$
\psi(\kappa)=\sum_v\beta_{W_v}(\psi_v).
$$

Hence:

### Theorem 5.1 — rank-four residue formula

$$
\boxed{
\psi(\kappa)
=
\sum_{v\in V(G)}\rho_{W_v}(\psi_v).
}
$$

Consequently,

$$
\boxed{
[\kappa]=0
\iff
\sum_v\rho_{W_v}(\psi_v)=0
\text{ for every equilibrium stress }\psi.
}
$$

Although each local residue is cubic, their sum restricts to the linear
functional $\psi\mapsto\psi(\kappa)$ on the global stress space. The nonlinear
local densities linearize because the support terms cancel by handshaking.

## 6. Dimension of the first essential layer

Let $G$ be connected, cubic, and have $n$ vertices. Let

$$
\mathcal B_f:=H_f^0/\Gamma
$$

be the reduced gauge code. In rank four,

$$
\dim H_f^1-\dim H_f^0=\frac n2.
$$

Since

$$
\dim H_f^0=4+\dim\mathcal B_f
$$

and the canonical alternating-stress subspace has dimension

$$
\dim\Lambda^2\Gamma^*=6,
$$

one obtains

$$
\boxed{
\dim\operatorname{EssStress}(f)
=
\dim\mathcal B_f+\frac{n-4}{2}.
}
$$

Thus rank four has dimensionally forced essential stress directions. The
residue character determines whether those directions actually detect the
affine class.

## 7. Symplectic vertex-plane parity

Fix a nondegenerate alternating form

$$
\alpha\in\Lambda^2\Gamma^*.
$$

At every vertex, let $W_v$ be the local flow plane. A binary plane is
$\alpha$-Lagrangian exactly when $\alpha|_{W_v}=0$.

### Theorem 7.1

$$
\boxed{
\#\{v:W_v\text{ is }\alpha\text{-Lagrangian}\}
\equiv0\pmod2.
}
$$

### Proof

Choose two distinct incident flow values $h_{v,1},h_{v,2}$ and put

$$
q_v:=h_{v,1}\wedge h_{v,2}\in\Lambda^2\Gamma.
$$

This is independent of the chosen pair. The wedge-handshake identity gives

$$
\sum_vq_v=0.
$$

Applying $\alpha$ yields

$$
\sum_v\alpha(h_{v,1},h_{v,2})=0.
$$

The summand is zero exactly at the Lagrangian vertex planes. Hence the number
of non-Lagrangian planes is even. A cubic graph has an even number of vertices,
so the number of Lagrangian planes is also even. $\square$

The global alternating stress

$$
\psi_e^\alpha(x)=\alpha(f(e),x)
$$

has residue one exactly at the $\alpha$-Lagrangian vertex planes. The theorem
therefore says that every stress arising from one global symplectic form has
even residue parity. An essential stress may instead be represented by local
forms $\alpha_v$ whose contractions agree on edges but which do not descend
from one global form. Rank-four incompatibility is therefore a symplectic
parity anomaly.

## 8. The canonical rank-four flow on $K_{3,3}$

Let the bipartition be

$$
L_0,L_1,L_2
\qquad\text{and}\qquad
R_0,R_1,R_2,
$$

and let $a,b,c,d$ be a basis of $\Gamma$. Arrange the edge labels as

$$
\boxed{
F=
\begin{pmatrix}
a&b&a+b\\
c&d&c+d\\
a+c&b+d&a+b+c+d
\end{pmatrix}.
}
$$

Every row and column sums to zero, all labels are nonzero, and they span
$\Gamma$. Since the cycle rank of $K_{3,3}$ is four, every spanning rank-four
binary flow is equivalent to this one under $\operatorname{GL}(\Gamma)$.

A direct row reduction gives

$$
H_f^0=\Gamma,
\qquad
\mathcal B_f=0.
$$

Thus the flow is gauge-rigid. The stress space has dimension seven; after
quotienting the six-dimensional alternating-stress subspace,

$$
\dim\operatorname{EssStress}(f)=1.
$$

A representative of its nonzero class is

$$
\boxed{
\Psi=
\begin{pmatrix}
b^*&a^*&a^*+b^*\\
b^*&a^*&a^*+b^*\\
0&0&0
\end{pmatrix}.
}
$$

Each entry annihilates the corresponding flow value, and every row and column
sums to zero. It is not a global alternating stress: the first and second rows
impose contradictory values on one alternating pairing.

The local data are:

| vertex | $\beta_v$ | $\sigma_v$ | $\rho_v$ |
|---|---:|---:|---:|
| $L_0$ | $1$ | $1$ | $0$ |
| $L_1$ | $0$ | $1$ | $1$ |
| $L_2$ | $0$ | $0$ | $0$ |
| $R_0$ | $0$ | $0$ | $0$ |
| $R_1$ | $0$ | $0$ | $0$ |
| $R_2$ | $0$ | $0$ | $0$ |

At $L_1$, the local form may be represented by

$$
\alpha_{L_1}=b^*\wedge c^*+a^*\wedge d^*.
$$

It vanishes on the local flow plane $\langle c,d\rangle$ and pairs that plane
perfectly with its quotient, so its Pfaffian and residue are one. Hence

$$
\sum_v\rho_v=1,
\qquad
\Psi(\kappa)=1.
$$

Therefore

$$
\boxed{[\kappa]\neq0.}
$$

The canonical rank-four flow on $K_{3,3}$ is incompatible.

## 9. The triangular prism

The only other connected simple cubic graph on six vertices is the triangular
prism. Label its top vertices $0,1,2$, bottom vertices $3,4,5$, and vertical
edges $03,14,25$. A canonical spanning rank-four flow is

| edge | flow value |
|---|---|
| $01$ | $a+c+d$ |
| $12$ | $a+d$ |
| $20$ | $a$ |
| $34$ | $b+c+d$ |
| $45$ | $b+d$ |
| $53$ | $b$ |
| $03$ | $c+d$ |
| $14$ | $c$ |
| $25$ | $d$ |

An explicit solution of the affine gluing equation is

$$
\boxed{
\begin{aligned}
m_0&=a+b+c,\\
m_1&=a+b+c+d,\\
m_2&=a+b,\\
m_3&=c,\\
m_4&=c+d,\\
m_5&=0.
\end{aligned}
}
$$

For every edge $e=uv$, the difference $m_u+m_v$ represents the intrinsic edge
obstruction class. Hence

$$
\boxed{[\kappa]=0.}
$$

A row reduction again gives

$$
\mathcal B_f=0,
\qquad
\dim\operatorname{EssStress}(f)=1.
$$

A representative of the essential class assigns $b^*$ to all three top-triangle
edges and zero to the other six edges. Every nonzero local pattern is
$(b^*,b^*,0)$, so no hidden dual Fano line occurs and every local residue is
zero.

## 10. The six-vertex dichotomy

A simple cubic graph on six vertices has a two-regular complement, which is
either $C_6$ or $C_3\sqcup C_3$. Thus the triangular prism and $K_{3,3}$ are the
only connected simple cubic graphs on six vertices. Both have cycle rank four,
so their spanning rank-four flows are unique up to coefficient change.

### Theorem 10.1

For the canonical spanning rank-four flows:

| graph | $\dim\mathcal B_f$ | $\dim\operatorname{EssStress}(f)$ | affine class |
|---|---:|---:|---|
| triangular prism | $0$ | $1$ | $0$ |
| $K_{3,3}$ | $0$ | $1$ | nonzero |

Therefore neither gauge rigidity nor the dimension of the essential-stress
space determines compatibility. The distinction is exactly the residue
character on the unique essential direction.

The pair is the smallest concrete proof that

$$
\text{essential stress}\not\Rightarrow\text{incompatibility},
$$

while

$$
\text{odd dual-Fano residue parity}
\Longleftrightarrow
\text{incompatibility}
$$

holds after testing all essential stress directions.