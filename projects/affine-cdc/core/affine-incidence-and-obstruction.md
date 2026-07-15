# Affine incidence geometry and the compatibility obstruction

**Status.** The linear-algebra statements in this chapter are theorem-level and
rank-independent. They reorganize the quotient-sheaf, affine-intersection, and
stress formulations into one canonical object. The identification of the local
affine coset with the original AffineCDC local-family construction is anchored
in the companion Lean repository; the invariant presentation here has not yet
been formalized in this form.

## 1. Source data and the compatibility image

Let $G=(V,E)$ be a finite cubic graph, not necessarily connected, let $\Gamma$
be a finite-dimensional vector space over $\mathbf F_2$, and let

$$
f:E\longrightarrow \Gamma
$$

be a nowhere-zero flow. Thus at every vertex $v$ the three incident values sum
to zero. Since none of them is zero, they are distinct and are the three
nonzero points of a plane

$$
W_v\leq \Gamma.
$$

For every edge $e$, put

$$
Q_e:=\Gamma/\langle f(e)\rangle.
$$

The full source datum $(G,\Gamma,f)$ retains vertices, edges, incidences, darts,
and the local combinatorial meaning needed later for the graph-level multiset
even-double-cover construction. The compatibility question factors through a
smaller affine linear object constructed below.

## 2. The incidence space

Let

$$
I(G):=\{(v,e):v\in e\}
$$

be the incidence set and define

$$
E_f:=\bigoplus_{(v,e)\in I(G)}Q_e.
$$

This space has two useful decompositions:

$$
E_f=\bigoplus_{v\in V}E_v,
\qquad
E_v:=\bigoplus_{e\ni v}Q_e,
$$

and

$$
E_f=\bigoplus_{e=uv}
\left(Q_e^{(u)}\oplus Q_e^{(v)}\right).
$$

The first decomposition records local choices at vertices. The second records
the two endpoint labels that must agree along each edge.

## 3. Vertex families and the canonical affine translate

For a vertex $v$, define

$$
\Delta_v:\Gamma\longrightarrow E_v,
\qquad
\Delta_v(m)=([m]_e)_{e\ni v}.
$$

The map is injective. Indeed, an element in its kernel lies in all three
incident flow lines, and three distinct one-dimensional binary subspaces have
trivial common intersection. Put

$$
L_v:=\operatorname{im}\Delta_v,
\qquad
L_{\mathrm{vert}}:=\bigoplus_{v\in V}L_v.
$$

For an incidence $(v,e)$, let $h=f(e)$ and let $h',h''$ be the other two
incident flow values at $v$. Since $h'+h''=h$, the two vectors $h'$ and $h''$
have the same image in $Q_e$. Define

$$
\kappa_{v,e}:=[h']_e=[h'']_e\in Q_e
$$

and let

$$
\kappa:=(\kappa_{v,e})_{(v,e)}\in E_f.
$$

The local affine-family space at $v$ is

$$
C_v:=\kappa_v+L_v,
$$

and the space of independent local choices at all vertices is

$$
C_{\mathrm{vert}}
:=\bigoplus_v C_v
=\kappa+L_{\mathrm{vert}}.
$$

This equality is the invariant form of the local affine classification. It is
the point at which the abstract incidence geometry is attached to the original
AffineCDC construction.

## 4. Edge matching

For an edge $e=uv$, define the diagonal

$$
D_e:=\{(x,x):x\in Q_e\}
\leq Q_e^{(u)}\oplus Q_e^{(v)}
$$

and put

$$
L_{\mathrm{edge}}:=\bigoplus_{e\in E}D_e.
$$

Membership in $L_{\mathrm{edge}}$ says exactly that the two endpoint labels on
every edge agree. Hence the original compatibility problem is

$$
\boxed{
\text{compatible global affine families}
=
(\kappa+L_{\mathrm{vert}})\cap L_{\mathrm{edge}}.
}
$$

This is the smallest symmetric affine-intersection image of the source problem.

## 5. The affine incidence-pair complex

Let $E$ be any finite-dimensional vector space, let $L,M\leq E$, and let
$C=\kappa+L$. Define the two-term complex

$$
\mathcal P(L,M):
L\oplus M\xrightarrow{d}E,
\qquad
d(l,m)=l+m.
$$

The kernel consists of pairs $(z,z)$ with $z\in L\cap M$, so

$$
H^0(\mathcal P(L,M))\cong L\cap M.
$$

Its cokernel is

$$
H^1(\mathcal P(L,M))\cong E/(L+M).
$$

The inhomogeneous equation

$$
d(l,m)=\kappa
$$

is equivalent to

$$
\kappa+l=m\in M,
$$

and hence to

$$
(\kappa+L)\cap M\neq\varnothing.
$$

Therefore:

### Theorem 5.1 — affine pair obstruction

The affine intersection $(\kappa+L)\cap M$ is nonempty if and only if

$$
[\kappa]=0\in E/(L+M).
$$

When nonempty, it is a torsor under $L\cap M$.

### Proof

Solvability is exactly the assertion $\kappa\in L+M$. If $x$ and $x'$ are two
intersection points, then $x+x'\in L\cap M$. Conversely, translating one
solution by any element of $L\cap M$ gives another solution. $\square$

For AffineCDC, define

$$
\boxed{
\mathcal P_f:
L_{\mathrm{vert}}\oplus L_{\mathrm{edge}}
\xrightarrow{+}
E_f.
}
$$

Then

$$
H^0(\mathcal P_f)
\cong
L_{\mathrm{vert}}\cap L_{\mathrm{edge}}
$$

is the homogeneous solution space, while

$$
H^1(\mathcal P_f)
\cong
E_f/(L_{\mathrm{vert}}+L_{\mathrm{edge}})
$$

is the complete linear obstruction space. The distinguished class

$$
[\kappa]\in H^1(\mathcal P_f)
$$

is the affine compatibility obstruction.

This pair complex, together with $\kappa$, is the canonical compatibility
centre:

$$
\boxed{
(\mathcal P_f,\kappa).
}
$$

## 6. Quotient-sheaf presentation

The symmetric pair complex has a canonical asymmetric quotient presentation.
For general $L,M\leq E$, consider

$$
\mathcal Q(L,M):
L\longrightarrow E/M,
\qquad
l\longmapsto[l].
$$

There is a short exact sequence of complexes

$$
0\longrightarrow
[M\xrightarrow{\mathrm{id}}M]
\longrightarrow
\mathcal P(L,M)
\longrightarrow
\mathcal Q(L,M)
\longrightarrow0.
$$

The first complex is contractible, so the quotient map is a canonical
quasi-isomorphism

$$
\mathcal P(L,M)\simeq\mathcal Q(L,M).
$$

For AffineCDC, the endpoint-sum map identifies

$$
E_f/L_{\mathrm{edge}}
\cong
\bigoplus_{e\in E}Q_e.
$$

The maps $\Delta_v$ identify

$$
L_{\mathrm{vert}}\cong\Gamma^V.
$$

Under these identifications, the quotient differential becomes

$$
\delta_f:\Gamma^V\longrightarrow\bigoplus_{e=uv}Q_e,
\qquad
(\delta_fm)_e=[m_u+m_v].
$$

Thus the quotient-sheaf complex is not a second compatibility object. It is the
canonical quotient presentation of the pair complex:

$$
\Gamma^V\xrightarrow{\delta_f}\bigoplus_eQ_e.
$$

Write

$$
H_f^0:=\ker\delta_f,
\qquad
H_f^1:=\operatorname{coker}\delta_f.
$$

Then

$$
H_f^0\cong H^0(\mathcal P_f),
\qquad
H_f^1\cong H^1(\mathcal P_f).
$$

The image of $\kappa$ in the quotient is the intrinsic cochain $c_f$, and

$$
\delta_fm=c_f
$$

is exactly the coordinate form of the affine intersection problem. In
particular,

$$
[c_f]=0\in H_f^1
\iff
[\kappa]=0\in H^1(\mathcal P_f).
$$

## 7. Dual presentation and equilibrium stresses

Dualizing the general pair complex gives

$$
\mathcal P(L,M)^*:
E^*\xrightarrow{d^*}L^*\oplus M^*,
\qquad
d^*(\phi)=(\phi|_L,\phi|_M).
$$

Its degree-zero kernel is

$$
\ker d^*
=L^\perp\cap M^\perp
=(L+M)^\perp
\cong H^1(\mathcal P(L,M))^*.
$$

Consequently the affine intersection is solvable if and only if

$$
\phi(\kappa)=0
\qquad
\text{for every }\phi\in L^\perp\cap M^\perp.
$$

For AffineCDC, identify

$$
Q_e^*\cong\operatorname{Ann}(f(e))\leq\Gamma^*.
$$

A dual incidence tuple lies in $L_{\mathrm{vert}}^\perp$ exactly when, at each
vertex, its three incident covectors sum to zero. It lies in
$L_{\mathrm{edge}}^\perp$ exactly when the two endpoint covectors on every edge
agree. Therefore

$$
\boxed{
L_{\mathrm{vert}}^\perp
\cap
L_{\mathrm{edge}}^\perp
=
\operatorname{Stress}(f),
}
$$

where $\operatorname{Stress}(f)$ is the equilibrium-stress space.

### Theorem 7.1 — Fredholm form of compatibility

The following are equivalent:

1. the local affine families can be chosen compatibly;
2. $[\kappa]=0$ in $H^1(\mathcal P_f)$;
3. $[c_f]=0$ in $H_f^1$;
4. every equilibrium stress $\psi$ satisfies $\psi(\kappa)=0$.

Thus the incidence pair, quotient sheaf, and stress criterion are respectively
the symmetric, primal quotient, and dual presentations of one affine equation.

## 8. Exact dependency and information boundary

The construction has the following dependency order:

$$
(G,\Gamma,f)
\longmapsto
(E_f,L_{\mathrm{vert}},\kappa+L_{\mathrm{vert}},L_{\mathrm{edge}})
\longmapsto
(\mathcal P_f,\kappa).
$$

From $(\mathcal P_f,\kappa)$ one recovers:

- the homogeneous solution space $H^0$;
- the full obstruction space $H^1$;
- the distinguished affine class;
- the quotient-sheaf presentation;
- the stress space and Fredholm criterion;
- the affine solution torsor when it is nonempty.

The compatibility image does **not** by itself retain:

- the original vertex, edge, and dart sets as combinatorial objects;
- the interpretation of a point of $\kappa+L_{\mathrm{vert}}$ as a local even
  family;
- the dart pairing and indexed-support construction that turns a compatible
  family into an even double cover;
- embedding, rotation-system, or surface data.

Accordingly, the honest output chain is

$$
(G,\Gamma,f)
\longmapsto
(\mathcal P_f,\kappa)
\longmapsto
\text{compatible affine families},
$$

followed by a second construction using the retained source data:

$$
(G,\Gamma,f,\text{compatible family})
\longmapsto
\text{graph-level multiset even double cover}.
$$

Circuit decomposition is a later generic graph-theoretic step, performed once
after collapse in the full theorem. The affine incidence-pair complex is
therefore the complete centre of the **compatibility problem**, but not a
replacement for the full graph-theoretic source object.
