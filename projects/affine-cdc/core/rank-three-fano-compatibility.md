# Rank-three Fano geometry and automatic compatibility

**Status.** The finite-dimensional quadratic and symplectic arguments below are
complete paper proofs. Their identification with the original local-family API
and the indexed-support construction is anchored in the companion Lean
repository. The quadratic presentation and the graph-level even-cover
factorization have not yet been independently formalized in this form.

This chapter assumes the rank-independent incidence geometry of
[`affine-incidence-and-obstruction.md`](affine-incidence-and-obstruction.md).

## 1. The canonical quadratic plane

Let $U$ be a two-dimensional vector space over $\mathbf F_2$. Define

$$
q_U(u):=
\begin{cases}
0,&u=0,\\
1,&u\neq0.
\end{cases}
$$

Its polarization is

$$
B_U(u,v):=q_U(u+v)+q_U(u)+q_U(v).
$$

If $u,v$ are dependent, then $B_U(u,v)=0$. If they are independent, then
$u,v,u+v$ are the three nonzero vectors of $U$, and $B_U(u,v)=1$. Hence $B_U$
is the unique nonzero alternating form on $U$, and $q_U$ is its canonical
anisotropic quadratic refinement.

Now let

$$
\Gamma=\mathbf F_2^3
$$

and choose the unique nonzero volume form

$$
\omega\in\Lambda^3\Gamma^*.
$$

For $0\neq h\in\Gamma$, the quotient

$$
Q_h:=\Gamma/\langle h\rangle
$$

is a binary plane. Its canonical quadratic form is

$$
q_h([x])=\mathbf1_{x\notin\langle h\rangle},
$$

and its polar form is

$$
\boxed{
B_h([x],[y])=\omega(h,x,y).
}
$$

This identity is well defined because changing a representative by a multiple
of $h$ does not change the determinant.

## 2. The local Fano Lagrangian

Let $W\leq\Gamma$ be a plane and let

$$
D:=W\setminus\{0\}.
$$

Thus $D=\{h_1,h_2,h_3\}$ with

$$
h_1+h_2+h_3=0.
$$

Define

$$
E_W:=\bigoplus_{h\in D}Q_h,
\qquad
q_W:=\sum_{h\in D}q_h,
\qquad
B_W:=\sum_{h\in D}B_h.
$$

The space $E_W$ has dimension six and $B_W$ is nondegenerate. Define

$$
\Delta_W:\Gamma\longrightarrow E_W,
\qquad
\Delta_W(x)=([x]_h)_{h\in D},
$$

and put

$$
L_W:=\operatorname{im}\Delta_W.
$$

### Theorem 2.1 — local Fano Lagrangian

The map $\Delta_W$ is injective and $L_W$ is Lagrangian in $(E_W,B_W)$.

### Proof

The three distinct lines $\langle h\rangle$ have trivial common intersection,
so $\Delta_W$ is injective and $\dim L_W=3$. For $x,y\in\Gamma$,

$$
\begin{aligned}
B_W(\Delta_Wx,\Delta_Wy)
&=\sum_{h\in D}\omega(h,x,y)\\
&=\omega\left(\sum_{h\in D}h,x,y\right)\\
&=0.
\end{aligned}
$$

Thus $L_W$ is isotropic and has half the dimension of $E_W$, hence is
Lagrangian. $\square$

## 3. Quadratic transgression

Let

$$
\ell_W:\Gamma\longrightarrow\mathbf F_2
$$

be the unique nonzero linear functional with kernel $W$.

### Theorem 3.1 — Fano quadratic transgression

For every $x\in\Gamma$,

$$
\boxed{
q_W(\Delta_Wx)=\ell_W(x).
}
$$

### Proof

By definition,

$$
q_W(\Delta_Wx)
=
\sum_{h\in D}\mathbf1_{x\notin\langle h\rangle}.
$$

If $x=0$, the sum is zero. If $x\in W\setminus\{0\}$, exactly one quotient
class vanishes and the other two are nonzero, so the sum is zero in
$\mathbf F_2$. If $x\notin W$, all three quotient classes are nonzero, so the
sum is one. This is exactly $\ell_W(x)$. $\square$

The same identity follows from polarization: the quadratic part cancels because

$$
\sum_{h\in D}\iota_h\omega
=
\iota_{\sum h}\omega
=0.
$$

Thus the sum of three canonical quotient quadratics becomes linear on the Fano
diagonal.

## 4. The characteristic torsor

Let $(E,q)$ be a nondegenerate quadratic space over $\mathbf F_2$, with polar
form $B$, and let $L\leq E$ be Lagrangian. Since $B|_L=0$, the restriction
$q|_L$ is linear. Define

$$
\operatorname{Char}_q(L)
:=
\{\kappa\in E:B(z,\kappa)=q(z)\text{ for every }z\in L\}.
$$

The restriction map

$$
E\longrightarrow L^*,
\qquad
\kappa\longmapsto B(-,\kappa)|_L
$$

is surjective with kernel $L^\perp=L$. Therefore

$$
\operatorname{Char}_q(L)
$$

is a nonempty affine torsor under $L$.

For $h\in D$, let $\kappa_h\in Q_h$ be the common class of the other two
nonzero elements of $W$, and put

$$
\kappa_W:=(\kappa_h)_{h\in D}\in E_W.
$$

### Theorem 4.1 — local affine families are characteristic vectors

One has

$$
\boxed{
\kappa_W\in\operatorname{Char}_{q_W}(L_W),
\qquad
\operatorname{Char}_{q_W}(L_W)=\kappa_W+L_W.
}
$$

Under the local AffineCDC classification, this characteristic torsor is exactly
the space of local affine families at the vertex with flow plane $W$.

### Proof

For $z=\Delta_Wx$,

$$
B_W(z,\kappa_W)=\ell_W(x)=q_W(z).
$$

The first equality is the local cross-pairing identity; it may also be checked
on the four cosets of $W$ in $\Gamma$. Hence $\kappa_W$ is characteristic. The
second assertion follows because the characteristic set is a torsor under
$L_W$. Componentwise its elements are

$$
(\kappa_h+[m]_h)_{h\in D},
\qquad
m\in\Gamma,
$$

which is the intrinsic quotient-label formula for the local family. $\square$

The quadratic form is constant on this torsor. Indeed, for $z\in L_W$,

$$
q_W(\kappa_W+z)
=q_W(\kappa_W)+q_W(z)+B_W(\kappa_W,z)
=q_W(\kappa_W).
$$

Since every component of $\kappa_W$ is nonzero,

$$
q_W(\kappa_W)=1.
$$

Thus the local affine-family space is an anisotropic affine Lagrangian coset.

## 5. Legal dual configurations

Use $B_h$ to identify

$$
Q_h\cong Q_h^*\cong\operatorname{Ann}(h).
$$

A tuple $z=(z_h)\in E_W$ corresponds to covectors

$$
\eta_h(x)=B_h(z_h,[x])=\omega(h,z_h,x).
$$

The legal dual-configuration condition is

$$
\sum_{h\in D}\eta_h=0.
$$

This holds if and only if

$$
B_W(z,\Delta_Wx)=0
\qquad
\text{for every }x\in\Gamma,
$$

that is, if and only if

$$
z\in L_W^\perp=L_W.
$$

Consequently

$$
\boxed{
\operatorname{DualConfig}(W)
\cong L_W
\cong\Gamma.
}
$$

For $z=\Delta_Wa$, the old cross-bit is

$$
\beta_W(z)=\ell_W(a)=q_W(z).
$$

Since $q_W(z)$ is the parity of the number of nonzero components of $z$, the
local branching theorem becomes

$$
\boxed{
\text{cross-bit}
=
q_W|_{L_W}
=
\text{support parity}.
}
$$

This is not an additional coincidence: both observables are the restriction of
the same canonical quadratic form to the local Fano Lagrangian.

## 6. The abstract affine Lagrangian-intersection theorem

### Theorem 6.1

Let $(E,q)$ be a finite-dimensional nondegenerate quadratic space over
$\mathbf F_2$, with polar form $B$, and let $L,M\leq E$ be Lagrangians. Then

$$
\boxed{
\operatorname{Char}_q(L)\cap M\neq\varnothing
\iff
q|_{L\cap M}=0.
}
$$

When nonempty, the intersection is a torsor under $L\cap M$.

### Proof

Suppose $m\in\operatorname{Char}_q(L)\cap M$. For $z\in L\cap M$,

$$
q(z)=B(z,m)=0
$$

because $z,m\in M$ and $M$ is isotropic.

Conversely, choose $\kappa\in\operatorname{Char}_q(L)$ and assume
$q|_{L\cap M}=0$. Then

$$
B(z,\kappa)=q(z)=0
\qquad
(z\in L\cap M),
$$

so

$$
\kappa\in(L\cap M)^\perp=L+M.
$$

Write $\kappa=\ell+m$ with $\ell\in L$ and $m\in M$. Since
$\operatorname{Char}_q(L)=\kappa+L$,

$$
m=\kappa+\ell\in\operatorname{Char}_q(L)\cap M.
$$

The torsor statement follows by taking differences. $\square$

### Corollary 6.2

If $M$ is totally singular, meaning $q|_M=0$, then

$$
\operatorname{Char}_q(L)\cap M\neq\varnothing.
$$

## 7. Global Fano compatibility

Return to a finite cubic graph, not necessarily connected, with a nowhere-zero
flow

$$
f:E(G)\longrightarrow\Gamma=\mathbf F_2^3.
$$

For every incidence $(v,e)$, use the quadratic form $q_e$ on $Q_e$ and define

$$
q_f:=\sum_{(v,e)\in I(G)}q_e
$$

on the incidence space $E_f$. The vertex space is

$$
L_{\mathrm{vert}}=\bigoplus_vL_v,
$$

and its characteristic torsor is

$$
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
=
\kappa+L_{\mathrm{vert}}.
$$

For an edge $e=uv$, the diagonal

$$
D_e=\{(x,x):x\in Q_e\}
$$

is Lagrangian and totally singular because

$$
q_e(x)+q_e(x)=0.
$$

Hence

$$
L_{\mathrm{edge}}=\bigoplus_eD_e
$$

is a totally singular Lagrangian.

### Theorem 7.1 — rank-three Fano compatibility

One has

$$
\boxed{
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
\cap
L_{\mathrm{edge}}
\neq\varnothing.
}
$$

Equivalently, the intrinsic affine class vanishes:

$$
[\kappa]=0\in H^1(\mathcal P_f),
\qquad
[c_f]=0\in H_f^1.
$$

### Proof

Apply Corollary 6.2 to the Lagrangians $L_{\mathrm{vert}}$ and
$L_{\mathrm{edge}}$. $\square$

The compatible-family space is a torsor under

$$
L_{\mathrm{vert}}\cap L_{\mathrm{edge}}
\cong H_f^0.
$$

Thus the theorem gives both existence and the full moduli space.

## 8. Global Fano duality

The polar forms identify the primal incidence space with its dual. Under this
identification,

$$
L_{\mathrm{vert}}\longleftrightarrow L_{\mathrm{vert}}^\perp,
\qquad
L_{\mathrm{edge}}\longleftrightarrow L_{\mathrm{edge}}^\perp.
$$

Consequently the same subspace

$$
L_{\mathrm{vert}}\cap L_{\mathrm{edge}}
$$

has two readings:

$$
\boxed{
H_f^0
\cong
\operatorname{Stress}(f)
\cong
(H_f^1)^*.
}
$$

Equivalently, the symplectic form induces a perfect pairing

$$
(L_{\mathrm{vert}}\cap L_{\mathrm{edge}})
\times
E_f/(L_{\mathrm{vert}}+L_{\mathrm{edge}})
\longrightarrow\mathbf F_2.
$$

This is the invariant source of Fano cohomological duality. It is not merely a
dimension count.

## 9. The same proof at lower resolutions

Let $z\in L_{\mathrm{vert}}\cap L_{\mathrm{edge}}$. Since the same quotient
vector occurs at the two ends of every edge,

$$
q_f(z)
=
2\sum_eq_e(z_e)
=0.
$$

This is exactly the restriction criterion

$$
q_f|_{L_{\mathrm{vert}}\cap L_{\mathrm{edge}}}=0.
$$

Under the dual interpretation, for an equilibrium stress $\psi$ one obtains

$$
\psi(\kappa)
=
\sum_v q_v(\psi_v)
=
2\sum_eq_e(\psi_e)
=0.
$$

Recording only whether each edge component is nonzero gives an edge chain $s$.
At each vertex the transgression identity says

$$
(\partial s)_v
=
q_v(\psi_v)
=
\beta_v(\psi),
$$

and global compatibility becomes

$$
\varepsilon\partial s=0.
$$

Thus the following are the same proof viewed at successively coarser
resolutions:

$$
\boxed{
\begin{array}{c}
\text{affine Lagrangian intersection}\\
\Updownarrow\\
\text{quadratic handshaking}\\
\Updownarrow\\
\text{cross-bit/support-boundary cancellation}.
\end{array}
}
$$

The Lagrangian formulation is strongest because it also gives the complete
solution torsor and explains primal-dual self-duality.

## 10. Odd-valence plane-supported extension

The scalar transgression is not intrinsically limited to a simple cubic star.
Suppose all incident nonzero flow values at a vertex lie in one plane
$W=\{0,h_1,h_2,h_3\}$, and let $m_i$ be the multiplicity of $h_i$.
The flow equation implies

$$
m_1\equiv m_2\equiv m_3\pmod2.
$$

Their common parity equals the degree parity. Therefore, for every $x\in\Gamma$,

$$
\boxed{
\sum_{e\ni v}q_{f(e)}([x])
=
(\deg v\bmod2)\,\ell_W(x).
}
$$

For odd valence this is the same outside-plane identity; for even valence the
quadratic contributions cancel locally. This extension concerns the scalar
support mechanism only. A local-family interpretation and an even-cover
construction for such vertices require additional definitions and do not follow
automatically from the cubic theory.

## 11. Output boundary

A point of

$$
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
\cap
L_{\mathrm{edge}}
$$

is a compatible collection of local affine families. The companion Lean
repository proves that, for the original AffineCDC local objects, the retained
dart and support data yield an indexed family of even edge supports with exact
double coverage. Flattening that family gives the natural graph-level multiset
even double cover.

The existing cubic-flow CDC theorem is obtained by immediately decomposing those
supports and is a checked corollary. In the full proof architecture, circuit
decomposition is deferred until after collapse and performed once on the
loopless original core, followed by singleton-loop reinsertion.

The quadratic theorem proves the compatibility input. It does not reconstruct
the dart permutation or support extraction from the reduced quadratic space.
The source graph and local combinatorial API must therefore remain available to
the downstream even-cover construction.
