# AC-PD-A5 — rank-three Fano compatibility by quadratic Lagrangian intersection

**Proof-development state:** `COMPLETE-DRAFT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Depends on:** `AC-PD-A4`  
**Immediate consumer:** `AC-PD-A6`  
**External mathematical inputs:** none

## 0. Main theorem

Let $G$ be a finite loopless cubic multigraph, not necessarily connected, and let

$$
f:E(G)\longrightarrow \Gamma\setminus\{0\},
\qquad
\Gamma=\mathbf F_2^3,
$$

be a nowhere-zero flow. For the affine incidence pair $(\mathcal P_f,\kappa)$ of A4, there exists

$$
x\in
(\kappa+L_{\mathrm{vert}})
\cap L_{\mathrm{edge}}.
$$

Equivalently,

$$
[\kappa]=0\in H^1(\mathcal P_f),
\qquad
[c_f]=0\in\operatorname{coker}\delta_f.
$$

The compatible-family space is a torsor under

$$
L_{\mathrm{vert}}\cap L_{\mathrm{edge}}
\cong H_f^0.
$$

The proof is invariant: every edge quotient is a canonical anisotropic quadratic plane; every local affine-family coset is the characteristic torsor of a Fano Lagrangian; the global edge diagonal is a totally singular Lagrangian; an abstract quadratic-Lagrangian theorem forces an intersection.

## 1. The canonical quadratic binary plane

Let $U$ be a two-dimensional vector space over $\mathbf F_2$. Define

$$
q_U(u)=
\begin{cases}
0,&u=0,\\
1,&u≠0.
\end{cases}
$$

and polarize by

$$
B_U(u,v)=q_U(u+v)+q_U(u)+q_U(v).
$$

### Proposition 1.1

The map $q_U$ is a quadratic form; $B_U$ is the unique nonzero alternating bilinear form on $U$, hence is nondegenerate; and $q_U$ has no nonzero singular vector.

### Proof

If $u,v$ are dependent, direct substitution gives $B_U(u,v)=0$. If they are independent, then $u,v,u+v$ are the three nonzero vectors of $U$, so

$$
B_U(u,v)=1+1+1=1.
$$

Relative to any basis the Gram matrix is

$$
\begin{pmatrix}0&1\\1&0\end{pmatrix},
$$

which is alternating and nondegenerate. The alternating-form space on a binary plane is one-dimensional, so this is its unique nonzero element. The final assertion is immediate from the definition of $q_U$. $\square$

## 2. Edge quotient planes in rank three

The one-dimensional space $\Lambda^3\Gamma^*$ over $\mathbf F_2$ has a unique nonzero element; denote it by $\omega$. For $0≠h\in\Gamma$, put

$$
Q_h=\Gamma/\langle h\rangle.
$$

Its canonical quadratic form is

$$
q_h([x])=
\begin{cases}
0,&x\in\langle h\rangle,\\
1,&x\notin\langle h\rangle.
\end{cases}
$$

### Proposition 2.1 — polar determinant formula

$$
B_h([x],[y])=\omega(h,x,y).
$$

### Proof

Changing $x$ or $y$ by a multiple of $h$ does not change the right-hand side, so it descends to $Q_h$. It is alternating and nonzero: if $[x],[y]$ form a basis of $Q_h$, then $(h,x,y)$ is a basis of $\Gamma$ and $\omega(h,x,y)=1$. Proposition 1.1 identifies it with the polar form of $q_h$. $\square$

Thus every $(Q_h,q_h)$ is a canonical nondegenerate anisotropic quadratic plane.

## 3. The local Fano Lagrangian

Let $W\leq\Gamma$ be a plane and

$$
D=W\setminus\{0\}=\{h_1,h_2,h_3\},
\qquad
h_1+h_2+h_3=0.
$$

Define

$$
E_W=\bigoplus_{h\in D}Q_h,
\qquad
q_W=\sum_{h\in D}q_h,
\qquad
B_W=\sum_{h\in D}B_h,
$$

and

$$
\Delta_W:\Gamma\longrightarrow E_W,
\qquad
\Delta_W(x)=([x]_h)_{h\in D},
\qquad
L_W=\operatorname{im}\Delta_W.
$$

### Theorem 3.1 — local Fano Lagrangian

The map $\Delta_W$ is injective and $L_W$ is Lagrangian in $(E_W,B_W)$.

### Proof

The three distinct lines $\langle h\rangle$ have trivial common intersection, so $\Delta_W$ is injective and $\dim L_W=3$. The space $E_W$ has dimension six and nondegenerate polar form. For $x,y\in\Gamma$,

$$
\begin{aligned}
B_W(\Delta_Wx,\Delta_Wy)
&=\sum_{h\in D}\omega(h,x,y)\\
&=\omega\left(\sum_{h\in D}h,x,y\right)\\
&=0.
\end{aligned}
$$

Thus $L_W$ is isotropic of half dimension and hence Lagrangian. $\square$

## 4. Fano quadratic transgression

Let $\ell_W:\Gamma\to\mathbf F_2$ be the unique nonzero linear functional with kernel $W$.

### Theorem 4.1

For every $x\in\Gamma$,

$$
q_W(\Delta_Wx)=\ell_W(x).
$$

### Proof

By definition,

$$
q_W(\Delta_Wx)=
\sum_{h\in D}\mathbf 1_{x\notin\langle h\rangle}.
$$

If $x=0$, the sum is zero. If $x\in W\setminus\{0\}$, precisely one quotient class vanishes and two are nonzero, so the sum is zero in $\mathbf F_2$. If $x\notin W$, all three quotient classes are nonzero and the sum is one. This is exactly $\ell_W(x)$. $\square$

## 5. Characteristic torsors

Let $(E,q)$ be a finite-dimensional nondegenerate quadratic space over $\mathbf F_2$, with polar form $B$, and let $L\leq E$ be Lagrangian. Since $B|_L=0$, the restriction $q|_L$ is linear. Define

$$
\operatorname{Char}_q(L)
=
\{a\in E:B(z,a)=q(z)\text{ for every }z\in L\}.
$$

### Proposition 5.1

The set $\operatorname{Char}_q(L)$ is nonempty and is an affine torsor under $L$.

### Proof

The restriction map

$$
E\longrightarrow L^*,
\qquad
a\longmapsto B(-,a)|_L
$$

is surjective: nondegeneracy identifies $E$ with $E^*$ and every functional on $L$ extends to $E$. Its kernel is $L^\perp=L$. The fibre over the functional $q|_L$ is therefore a nonempty affine coset of $L$. $\square$

## 6. Local affine families as characteristic vectors

For $h\in D$, let $\kappa_h\in Q_h$ be the common class of the other two nonzero elements of $W$, and put

$$
\kappa_W=(\kappa_h)_{h\in D}\in E_W.
$$

### Lemma 6.1 — local cross-pairing

For every $x\in\Gamma$,

$$
B_W(\Delta_Wx,\kappa_W)=\ell_W(x).
$$

### Proof

Choose independent $a,b\in W$, put $c=a+b$, and choose $t\notin W$ with $\omega(a,b,t)=1$. Use representatives

$$
\kappa_a=[b]_a,
\qquad
\kappa_b=[a]_b,
\qquad
\kappa_c=[a]_c.
$$

Write $x=\alpha a+\beta b+\gamma t$. Proposition 2.1 gives

$$
\begin{aligned}
B_W(\Delta_Wx,\kappa_W)
&=\omega(a,x,b)+\omega(b,x,a)+\omega(c,x,a)\\
&=\gamma+\gamma+\gamma\\
&=\gamma.
\end{aligned}
$$

The coefficient $\gamma$ is $\ell_W(x)$. The result is independent of representative choices because every $\kappa_h$ is a quotient class. $\square$

### Theorem 6.2 — local characteristic torsor

$$
\kappa_W\in\operatorname{Char}_{q_W}(L_W),
\qquad
\operatorname{Char}_{q_W}(L_W)=\kappa_W+L_W.
$$

Under A4's local classification, this is exactly the space of local affine even families at a vertex with flow plane $W$.

### Proof

For $z=\Delta_Wx$, Lemma 6.1 and Theorem 4.1 give

$$
B_W(z,\kappa_W)=\ell_W(x)=q_W(z).
$$

Thus $\kappa_W$ is characteristic. Proposition 5.1 gives the affine coset $\kappa_W+L_W$. A4 identifies the same quotient-label coset with all local affine families. $\square$

### Corollary 6.3

The quadratic form is constant with value one on $\kappa_W+L_W$.

### Proof

For $z\in L_W$, characteristicity gives

$$
q_W(\kappa_W+z)
=q_W(\kappa_W)+q_W(z)+B_W(\kappa_W,z)
=q_W(\kappa_W).
$$

Every component of $\kappa_W$ is nonzero, so $q_W(\kappa_W)=1+1+1=1$. $\square$

## 7. The abstract intersection theorem

### Lemma 7.1

For subspaces $L,M$ of a finite-dimensional nondegenerate bilinear space,

$$
(L\cap M)^\perp=L^\perp+M^\perp.
$$

In particular, if $L$ and $M$ are Lagrangian, then

$$
(L\cap M)^\perp=L+M.
$$

### Proof

The inclusion from right to left is immediate. Equality follows by dimension comparison, using

$$
L^\perp\cap M^\perp=(L+M)^\perp
$$

and nondegeneracy. For Lagrangians, $L^\perp=L$ and $M^\perp=M$. $\square$

### Theorem 7.2 — characteristic-torsor intersection

Let $(E,q)$ be a finite-dimensional nondegenerate quadratic space over $\mathbf F_2$ and let $L,M\leq E$ be Lagrangians. Then

$$
\operatorname{Char}_q(L)\cap M\text{ is nonempty}
\quad\Longleftrightarrow\quad
q|_{L\cap M}=0.
$$

When nonempty, the intersection is a torsor under $L\cap M$.

### Proof

If $m\in\operatorname{Char}_q(L)\cap M$ and $z\in L\cap M$, then

$$
q(z)=B(z,m)=0
$$

because $z,m\in M$ and $M$ is isotropic.

Conversely choose $\kappa\in\operatorname{Char}_q(L)$ and assume $q$ vanishes on $L\cap M$. Then

$$
B(z,\kappa)=q(z)=0
\qquad(z\in L\cap M),
$$

so Lemma 7.1 gives $\kappa\in L+M$. Write $\kappa=\ell+m$ with $\ell\in L$ and $m\in M$. Since $\operatorname{Char}_q(L)=\kappa+L$,

$$
m=\kappa+\ell\in\operatorname{Char}_q(L)\cap M.
$$

Taking differences proves the torsor statement. $\square$

### Corollary 7.3

If $M$ is a totally singular Lagrangian, then $\operatorname{Char}_q(L)\cap M$ is nonempty.

## 8. Global Fano compatibility

On each incidence quotient $Q_e$, use the form $q_e=q_{f(e)}$ and define

$$
q_f=\sum_{(v,e)\in I(G)}q_e,
\qquad
B_f=\sum_{(v,e)\in I(G)}B_e
$$

on $E_f$.

### Proposition 8.1

The quadratic space $(E_f,q_f)$ is nondegenerate.

### Proof

Its polar form is the direct sum of the nondegenerate polar forms on the incidence quotient planes. $\square$

### Proposition 8.2

The space

$$
L_{\mathrm{vert}}=\bigoplus_vL_v
$$

is Lagrangian and

$$
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
=
\kappa+L_{\mathrm{vert}}.
$$

### Proof

Apply Theorems 3.1 and 6.2 at each vertex and take direct sums. $\square$

### Proposition 8.3

For an edge $e=uv$, the diagonal

$$
D_e=\{(x,x):x\in Q_e\}
\leq Q_e^{(u)}\oplus Q_e^{(v)}
$$

is a totally singular Lagrangian for $q_e\oplus q_e$. Consequently

$$
L_{\mathrm{edge}}=\bigoplus_eD_e
$$

is a totally singular Lagrangian in $(E_f,q_f)$.

### Proof

For diagonal vectors,

$$
(B_e\oplus B_e)((x,x),(y,y))
=B_e(x,y)+B_e(x,y)=0,
$$

so $D_e$ is isotropic. It has dimension two, half the dimension of $Q_e\oplus Q_e$, and is therefore Lagrangian. Moreover

$$
(q_e\oplus q_e)(x,x)=q_e(x)+q_e(x)=0.
$$

Direct sums preserve both properties. $\square$

### Theorem 8.4 — rank-three automatic compatibility

There exists

$$
x\in
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
\cap L_{\mathrm{edge}}.
$$

Hence the AffineCDC local families admit a globally compatible choice.

### Proof

Propositions 8.2 and 8.3 give two Lagrangians, of which $L_{\mathrm{edge}}$ is totally singular. Apply Corollary 7.3, then A4's affine-family interpretation. $\square$

### Corollary 8.5 — obstruction and moduli

$$
[\kappa]=0\in H^1(\mathcal P_f),
\qquad
[c_f]=0\in\operatorname{coker}\delta_f,
$$

and the compatible-family space is a torsor under

$$
L_{\mathrm{vert}}\cap L_{\mathrm{edge}}
\cong H_f^0.
$$

## 9. Lower-resolution identities

### Proposition 9.1 — quadratic handshaking

For $z\in L_{\mathrm{vert}}\cap L_{\mathrm{edge}}$, write $z_{u,e}=z_{v,e}=z_e$ at every edge $e=uv$. Then

$$
\begin{aligned}
q_f(z)
&=\sum_{e=uv}
\bigl(q_e(z_{u,e})+q_e(z_{v,e})\bigr)\\
&=\sum_e\bigl(q_e(z_e)+q_e(z_e)\bigr)\\
&=0.
\end{aligned}
$$

This is exactly the restriction condition in Theorem 7.2.

### Proposition 9.2 — stress cancellation

Under the polar self-duality of the quotient planes, every equilibrium stress $\psi$ satisfies

$$
\psi(\kappa)=0.
$$

### Proof

The local characteristic identity gives $\psi_v(\kappa_v)=q_v(\psi_v)$. Edge matching of the stress then yields

$$
\begin{aligned}
\psi(\kappa)
&=\sum_vq_v(\psi_v)\\
&=\sum_{e=uv}
\bigl(q_e(\psi_e)+q_e(\psi_e)\bigr)\\
&=0.
\end{aligned}
$$

This is A4's Fredholm criterion. Recording only whether each quotient component is nonzero produces the earlier support-parity or cross-bit cancellation; it is a projection of the same quadratic identity.

## 10. Components and boundary cases

- **Disconnected graph.** Every object is a direct sum over edge-bearing components; no connectedness hypothesis is used.
- **Empty graph.** All spaces and $\kappa$ are zero, and the unique zero point is compatible.
- **Parallel edges.** Each edge object contributes its own pair of quotient summands and diagonal.
- **Loops.** The representation is loopless by A1–A3; no loop extension of the current dart/diagonal API is asserted.
- **Rank.** The proof is genuinely rank three: each quotient is a binary plane and the three incident directions are the nonzero points of one Fano plane. No higher-rank automatic-compatibility claim follows.

## 11. Formal and output boundary

The companion Lean repository machine-checks rank-three compatibility in the original branching/cross-bit presentation; A4 checks the exact local-family coordinate correspondence. The invariant characteristic-torsor and quadratic-Lagrangian assembly here is a complete paper proof, not thereby a Lean theorem in this form.

The output is a compatible collection of local affine families. It does not reconstruct graph-level indexed supports from a bare pair complex; A6 must retain the original graph, flow, incidence, and dart data.

## 12. Exported interface

A6 may cite:

1. canonical nondegenerate anisotropic quadratic forms on all rank-three edge quotients;
2. local and global vertex Lagrangians;
3. exact identification of the local affine-family coset with the characteristic torsor;
4. total singularity and Lagrangianity of the edge diagonal;
5. existence and full torsor of globally compatible local families;
6. persistence of graph/dart data as a separate downstream requirement.

## 13. Completion assessment

`AC-PD-A5` is `COMPLETE-DRAFT`. No contradiction, source gap, or genuine frontier question arose. The next dependency-respecting unit is A6, graph-level indexed even-support extraction.
