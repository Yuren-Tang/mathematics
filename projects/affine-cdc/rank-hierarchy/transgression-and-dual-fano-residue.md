# The rank hierarchy: transgression and the dual-Fano residue

**Status.** The general identities and proofs in this chapter are theorem-level
finite-dimensional arguments. The residue formulas have also been checked by
exact enumeration in ranks three through six, but the enumeration is supporting
evidence rather than part of the proof. This presentation has not yet been
Lean-formalized.

This chapter explains both why rank three is exceptional and what replaces its
quadratic compatibility mechanism in higher rank.

## 1. The support polynomial

Let $U$ be a $d$-dimensional vector space over $\mathbf F_2$. Define its nonzero
indicator

$$
\nu_U(u):=\mathbf1_{u\neq0}.
$$

In linear coordinates $u=(x_1,\dots,x_d)$,

$$
\boxed{
\nu_U(x)
=1+\prod_{i=1}^d(1+x_i)
=\sum_{\varnothing\neq S\subseteq\{1,\dots,d\}}
\prod_{i\in S}x_i.
}
$$

Hence

$$
\deg\nu_U=d.
$$

This degree is intrinsic because invertible linear coordinate changes preserve
algebraic degree. Its top additive polarization is the binary volume form on
$U$.

Let now

$$
\Gamma=\mathbf F_2^r
$$

and, for $0\neq h\in\Gamma$, put

$$
Q_h:=\Gamma/\langle h\rangle.
$$

Then

$$
\dim Q_h=r-1,
\qquad
\deg\nu_{Q_h}=r-1.
$$

Thus edge support is linear in rank two, quadratic in rank three, cubic in rank
four, and of degree $r-1$ in general.

## 2. Rank three as the unique balanced quadratic point

At a cubic vertex with incident values $h_1,h_2,h_3$, define

$$
E_v:=Q_{h_1}\oplus Q_{h_2}\oplus Q_{h_3}
$$

and

$$
\Delta_v:\Gamma\longrightarrow E_v,
\qquad
x\longmapsto([x]_{h_1},[x]_{h_2},[x]_{h_3}).
$$

The map is injective, so

$$
\dim\operatorname{im}\Delta_v=r,
\qquad
\dim E_v=3(r-1).
$$

The image can be half-dimensional only if

$$
2r=3(r-1),
$$

which has the unique solution

$$
r=3.
$$

The same equation appears globally. For a connected cubic graph,

$$
|E|=\frac32|V|,
$$

and the quotient-sheaf cochain dimensions are

$$
\dim C_f^0=r|V|,
\qquad
\dim C_f^1=(r-1)|E|
=\frac32(r-1)|V|.
$$

Therefore

$$
\chi_f
:=\dim C_f^0-\dim C_f^1
=\frac{3-r}{2}|V|.
$$

The quotient-sheaf complex is balanced exactly when $r=3$.

### Theorem 2.1 — rank-three coincidence principle

For cubic binary flow geometry, the following conditions hold simultaneously
exactly at rank three:

1. the edge-quotient support function is quadratic;
2. the local homogeneous family space is half-dimensional;
3. the quotient-sheaf complex has index zero;
4. the local family space can be Lagrangian in the incidence space;
5. the global compatibility problem can be expressed as an intersection of two
   Lagrangians in one nondegenerate quadratic space.

Thus the rank-three quadratic-Lagrangian theorem is not an accidental elegant
rephrasing. It is the unique balanced quadratic member of the rank hierarchy.

## 3. All-rank Fano transgression

Let $W\leq\Gamma$ be a plane and put

$$
D:=W\setminus\{0\}.
$$

For $h\in D$, let

$$
\nu_h:Q_h\longrightarrow\mathbf F_2
$$

be the nonzero indicator. Let

$$
\nu_{\Gamma/W}:\Gamma/W\longrightarrow\mathbf F_2
$$

be the nonzero indicator on the quotient by the whole plane.

### Theorem 3.1 — degree-lowering Fano transgression

For every $x\in\Gamma$,

$$
\boxed{
\sum_{h\in D}\nu_h([x]_h)
=
\nu_{\Gamma/W}([x]_W).
}
$$

### Proof

If $x=0$, all terms vanish. If $x\in W\setminus\{0\}$, it spans exactly one of
the three lines $\langle h\rangle$, so one quotient class is zero and the other
two are nonzero; the sum is zero. If $x\notin W$, all three quotient classes
are nonzero; the sum is one. These are exactly the values of the right-hand
side. $\square$

Since

$$
\deg\nu_h=r-1,
\qquad
\deg\nu_{\Gamma/W}=r-2,
$$

Fano summation cancels the top-degree part and lowers support degree by one.
At the level of top polarizations, for a volume form
$\Omega\in\Lambda^r\Gamma^*$ this cancellation is

$$
\sum_{h\in D}\iota_h\Omega
=
\iota_{\sum_{h\in D}h}\Omega
=0.
$$

At rank three this is the quadratic-to-linear transgression used in the
Lagrangian proof. At rank four it is cubic-to-quadratic; the scalar identity
survives, but there is no nondegenerate bilinear polarization carrying the full
edge support datum.

## 4. The affine level-set identity in every rank

For each $h\in D$, let $\kappa_h\in Q_h$ be the common class of the other two
nonzero vectors of $W$, and put

$$
\kappa_W:=(\kappa_h)_{h\in D}.
$$

### Theorem 4.1

For every $m\in\Gamma$,

$$
\boxed{
\sum_{h\in D}
\nu_h(\kappa_h+[m]_h)
=1.
}
$$

### Proof

If $m=0$, all three components are nonzero. If $m\notin W$, none of the three
translated classes can vanish. If $m\in W\setminus\{0\}$, exactly two
translated classes vanish and the third is nonzero. In every case the support
has odd cardinality. $\square$

Thus the local affine family

$$
\kappa_W+\Delta_W(\Gamma)
$$

lies in a constant odd-support level set in every rank. Only at rank three is
that level set the characteristic torsor of a Lagrangian.

## 5. Global outside-plane parity

Let $G$ be cubic and let $k=(k_v)$ be a global section of the quotient sheaf.
For an edge $e=uv$, define

$$
s(k)_e:=\nu_{Q_e}([k_v]_e).
$$

The section condition makes this independent of the endpoint. At a vertex $v$,
Theorem 3.1 gives

$$
(\partial s(k))_v
=
\nu_{\Gamma/W_v}([k_v]_{W_v}).
$$

Applying the augmentation to a boundary yields

$$
\boxed{
\sum_{v\in V}
\nu_{\Gamma/W_v}([k_v]_{W_v})
=0.
}
$$

Hence the number of vertices at which $k_v\notin W_v$ is even in every rank.
At rank three, $\Gamma/W_v$ is one-dimensional, so this one bit is the complete
quotient coordinate. For $r>3$, the scalar support indicator forgets the
direction of the class in $\Gamma/W_v$, and parity alone no longer decides
compatibility.

## 6. Legal dual configurations and the cross-bit

Let $W\leq\Gamma$ be a plane and $D=W\setminus\{0\}$. A legal dual
configuration is a family

$$
\eta=(\eta_h)_{h\in D},
\qquad
\eta_h\in\operatorname{Ann}(h),
\qquad
\sum_{h\in D}\eta_h=0.
$$

For distinct $h,h'\in D$, the value $\eta_h(h')$ is independent of the chosen
ordered pair. Indeed, writing $D=\{h_1,h_2,h_3\}$, using
$h_1+h_2+h_3=0$, the equations $\eta_i(h_i)=0$, and
$\eta_1+\eta_2+\eta_3=0$ identifies all six cross-values. Define their common
value by

$$
\beta_W(\eta):=\eta_h(h')
\qquad(h\neq h').
$$

This is the local affine-obstruction pairing, or cross-bit.

The legal-configuration space has dimension

$$
3(r-1)-r=2r-3.
$$

The dimension formula follows because the sum map

$$
\bigoplus_{h\in D}\operatorname{Ann}(h)
\longrightarrow\Gamma^*
$$

is surjective: the annihilators of two distinct directions already span
$\Gamma^*$.

A previously established local criterion is

$$
\beta_W(\eta)=0
\iff
\eta_h|_W=0
\text{ for every }h\in D.
$$

Equivalently, when the cross-bit vanishes, all three components lie in

$$
\operatorname{Ann}(W).
$$

## 7. The hidden dual-Fano residue

Define the local support parity

$$
\sigma_W(\eta)
:=
\sum_{h\in D}\mathbf1_{\eta_h\neq0}.
$$

Define

$$
\rho_W(\eta)=1
$$

exactly when

1. $\beta_W(\eta)=0$; and
2. all three covectors $\eta_h$ are nonzero.

Otherwise set $\rho_W(\eta)=0$.

If $\rho_W(\eta)=1$, then the three components are nonzero elements of
$\operatorname{Ann}(W)$ summing to zero. Hence they are distinct and form the
three nonzero points of a plane

$$
P_\eta\leq\operatorname{Ann}(W).
$$

Thus $\rho_W$ detects a hidden dual Fano line inside the annihilator of the
local flow plane.

### Theorem 7.1 — local residue identity

For every legal dual configuration,

$$
\boxed{
\sigma_W(\eta)
=
\beta_W(\eta)+\rho_W(\eta).
}
$$

### Proof

If $\beta_W(\eta)=1$, each component is nonzero because it takes value one on
another Fano direction. Hence $\sigma_W=1$ and $\rho_W=0$.

If $\beta_W(\eta)=0$, all components lie in $\operatorname{Ann}(W)$ and sum to
zero. A triple summing to zero cannot have support size one. Its support parity
is odd exactly when all three components are nonzero, which is exactly the
condition $\rho_W=1$. $\square$

## 8. Counting local residues

Since

$$
\dim\operatorname{Ann}(W)=r-2,
$$

a residue configuration is obtained by choosing a plane

$$
P\leq\operatorname{Ann}(W)
$$

and an ordered identification between the three nonzero points of $W$ and the
three nonzero points of $P$. Each plane permits

$$
|\operatorname{GL}(2,2)|=6
$$

such identifications. Therefore the number of residue configurations is

$$
\boxed{
6{r-2\brack2}_2
=
(2^{r-2}-1)(2^{r-2}-2).
}
$$

For comparison:

| rank $r$ | legal configurations | residue configurations |
|---:|---:|---:|
| $3$ | $8$ | $0$ |
| $4$ | $32$ | $6$ |
| $5$ | $128$ | $42$ |
| $6$ | $512$ | $210$ |

Rank four is the first possible residue layer.

## 9. The global residue theorem

Let $G$ be a finite cubic graph with a nowhere-zero flow

$$
f:E(G)\longrightarrow\Gamma
$$

and let $\psi$ be an equilibrium stress. At a vertex $v$, the incident edge
covectors form a legal configuration

$$
\psi_v\in\operatorname{DualConfig}(W_v).
$$

The canonical local affine datum gives

$$
\psi(\kappa)
=
\sum_v\beta_{W_v}(\psi_v).
$$

Every nonzero edge covector is counted at both endpoints, so

$$
\sum_v\sigma_{W_v}(\psi_v)=0.
$$

Applying the local residue identity yields the exact global formula.

### Theorem 9.1 — dual-Fano residue theorem

For every equilibrium stress $\psi$,

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
\text{every equilibrium stress has an even number of residue vertices}.
}
$$

This is the complete affine compatibility criterion in every rank. It is
complete because equilibrium stresses are the full dual of the obstruction
space, not merely a selected family of tests.

## 10. Consequences by rank

### Rank three

Here

$$
\dim\operatorname{Ann}(W)=1.
$$

A one-dimensional binary space cannot contain a plane, so

$$
\rho_W\equiv0.
$$

The global theorem gives automatic compatibility. This is the dual form of the
quadratic-Lagrangian theorem.

### Rank four

Here

$$
\dim\operatorname{Ann}(W)=2.
$$

The annihilator itself is the unique possible hidden plane. A residue occurs
exactly when the three incident covectors are its three nonzero points. The
indicator has a canonical cubic Pfaffian equation, developed in
[`rank-four-first-obstruction.md`](rank-four-first-obstruction.md).

### Higher rank

For $r>4$, the annihilator may contain many planes. The scalar compatibility
class records only the parity of residue vertices. Each residue also carries a
plane

$$
P_\eta\leq\operatorname{Ann}(W),
$$

which suggests a finer decorated-residue theory. That refinement is a research
programme, not part of the established compatibility criterion.

## 11. Logical summary

The positive and negative statements fit one chain:

$$
\boxed{
\begin{array}{c}
\text{edge support of degree }r-1\\
\downarrow\ \text{Fano summation}\\
\text{outside-plane support of degree }r-2\\
\downarrow\ \text{dual completion}\\
\text{hidden annihilator-plane residue}.
\end{array}
}
$$

At rank three, support is quadratic, the local family is Lagrangian, and no
annihilator plane exists. At rank four, all three protections fail at once: the
support becomes cubic, the local family is no longer half-dimensional, and the
first hidden dual plane becomes possible.