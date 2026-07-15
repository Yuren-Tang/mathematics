# AffineCDC theory map v1: the affine incidence pair

**Date:** 2026-07-15  
**Status:** structural synthesis; theorem-level linear algebra. The rank-three
quadratic and all-rank residue formulations still require independent audit and
formalization in this presentation.

This note identifies the smallest honest compatibility object through which the
quotient-sheaf, stress, Lagrangian, support-residue and tensor descriptions
factor. It does not claim that this reduced object alone remembers the final
cycle-double-cover extraction.

## 1. Source datum and compatibility image

Let \(G\) be a finite cubic graph and let

\[
f:E(G)\to\Gamma
\]

be a nowhere-zero binary flow. Put

\[
Q_e=\Gamma/\langle f(e)\rangle.
\]

The full source object is \((G,\Gamma,f)\). It retains the graph and dart
structure needed for CDC extraction.

The compatibility problem factors through the affine incidence pair below.

## 2. Global incidence space

Let

\[
I(G)=\{(v,e):v\in e\}
\]

and define

\[
E_f=\bigoplus_{(v,e)\in I(G)}Q_e.
\]

It has a vertex decomposition

\[
E_f=\bigoplus_vE_v,
\qquad
E_v=\bigoplus_{e\ni v}Q_e,
\]

and an edge decomposition

\[
E_f=\bigoplus_{e=uv}
\left(Q_e^{(u)}\oplus Q_e^{(v)}\right).
\]

## 3. Vertex space, affine coset and edge matching

For each vertex define

\[
\Delta_v:\Gamma\to E_v,
\qquad
\Delta_v(m)=([m]_e)_{e\ni v}.
\]

The three incident flow lines have zero common intersection, so \(\Delta_v\) is
injective. Put

\[
L_v=\operatorname{im}\Delta_v,
\qquad
L_{\mathrm{vert}}=\bigoplus_vL_v.
\]

For an incidence \((v,e)\), let \(\kappa_{v,e}\in Q_e\) be the common class of
the other two incident flow values. Put

\[
\kappa=(\kappa_{v,e})_{(v,e)}.
\]

Then

\[
C_{\mathrm{vert}}
=
\kappa+L_{\mathrm{vert}}
\]

is exactly the space of all choices of one local affine family at every vertex.

For an edge \(e=uv\), let

\[
D_e=\{(x,x):x\in Q_e\}
\]

and put

\[
L_{\mathrm{edge}}=\bigoplus_eD_e.
\]

Membership in \(L_{\mathrm{edge}}\) says that the two endpoint labels agree on
every edge.

The central compatibility object is

\[
\boxed{
\mathfrak I_f
=
(E_f,L_{\mathrm{vert}},L_{\mathrm{edge}},
\kappa+L_{\mathrm{vert}}).
}
\]

## 4. Universal affine-intersection theorem

Let \(E\) be finite-dimensional, let \(L,M\le E\), and let \(C=\kappa+L\).
Then

\[
\boxed{
C\cap M\ne\varnothing
\iff
\phi(\kappa)=0
\quad
\text{for every }\phi\in L^\perp\cap M^\perp.
}
\]

Indeed,

\[
C\cap M\ne\varnothing
\iff
\kappa\in L+M,
\]

and

\[
(L+M)^\perp=L^\perp\cap M^\perp.
\]

If nonempty, \(C\cap M\) is a torsor under \(L\cap M\).

Applied to \(\mathfrak I_f\),

\[
\boxed{
\text{compatible global affine families}
=
C_{\mathrm{vert}}\cap L_{\mathrm{edge}}.
}
\]

## 5. Quotient-sheaf model

Let

\[
\pi_{\mathrm{edge}}:E_f\to E_f/L_{\mathrm{edge}}
\]

be the quotient map and restrict it to \(L_{\mathrm{vert}}\).

Using

\[
L_{\mathrm{vert}}\cong\Gamma^{V(G)}
\]

through the maps \(\Delta_v\), and

\[
E_f/L_{\mathrm{edge}}\cong\bigoplus_eQ_e
\]

through endpoint difference, the restricted map becomes

\[
\delta_f:\Gamma^{V(G)}\to\bigoplus_eQ_e,
\qquad
(\delta_fm)_e=[m_u+m_v].
\]

The image of \(\kappa\) becomes \(c_f\). Hence

\[
\delta_fm=c_f
\]

is the coordinate form of

\[
C_{\mathrm{vert}}\cap L_{\mathrm{edge}}\ne\varnothing.
\]

Moreover,

\[
H^0(G;\mathscr Q_f)
=
L_{\mathrm{vert}}\cap L_{\mathrm{edge}}.
\]

The affine obstruction is the class of \(\kappa\) modulo
\(L_{\mathrm{vert}}+L_{\mathrm{edge}}\).

## 6. Dual pair and stresses

The dual incidence space is

\[
E_f^*
=
\bigoplus_{(v,e)}Q_e^*
\cong
\bigoplus_{(v,e)}\operatorname{Ann}(f(e)).
\]

A tuple at \(v\) lies in \(L_v^\perp\) exactly when its three covectors sum to
zero. Therefore

\[
L_{\mathrm{vert}}^\perp
=
\bigoplus_v\operatorname{DualConfig}(W_v).
\]

A dual tuple lies in \(L_{\mathrm{edge}}^\perp\) exactly when the two endpoint
covectors on every edge agree. Consequently

\[
\boxed{
L_{\mathrm{vert}}^\perp
\cap
L_{\mathrm{edge}}^\perp
=
\operatorname{Stress}(f).
}
\]

The universal affine-intersection theorem becomes the dual solvability
criterion:

\[
C_{\mathrm{vert}}\cap L_{\mathrm{edge}}\ne\varnothing
\iff
\psi(\kappa)=0
\quad
\text{for every equilibrium stress }\psi.
\]

Thus quotient sheaf and stress are the primal and dual presentations of the
same incidence pair.

## 7. Rank-three quadratic enhancement

Assume \(\Gamma=\mathbf F_2^3\). Each \(Q_e\) is a binary plane and carries the
canonical quadratic form

\[
q_e(x)=\mathbf1_{x\ne0}.
\]

Its polar form identifies

\[
Q_e\cong Q_e^*\cong\operatorname{Ann}(f(e)).
\]

Taking direct sums identifies \(E_f\cong E_f^*\), under which

\[
L_{\mathrm{vert}}\longleftrightarrow L_{\mathrm{vert}}^\perp,
\qquad
L_{\mathrm{edge}}\longleftrightarrow L_{\mathrm{edge}}^\perp.
\]

Both primal spaces are Lagrangian. Moreover,

\[
C_{\mathrm{vert}}
=
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
\]

and \(L_{\mathrm{edge}}\) is totally singular. Compatibility becomes

\[
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
\cap
L_{\mathrm{edge}}
\ne\varnothing.
\]

The global Fano self-duality is literal:

\[
L_{\mathrm{vert}}\cap L_{\mathrm{edge}}
\cong
L_{\mathrm{vert}}^\perp\cap L_{\mathrm{edge}}^\perp.
\]

The left side is the global-section space; the right side is the stress space.

## 8. Support, cross-bit and residue

Let

\[
\psi\in
L_{\mathrm{vert}}^\perp\cap L_{\mathrm{edge}}^\perp.
\]

At a vertex define

\[
\beta_v(\psi)=\psi_v(\kappa_v)
\]

and

\[
\sigma_v(\psi)=
\sum_{e\ni v}\mathbf1_{\psi_e\ne0}.
\]

Put

\[
\rho_v(\psi)=\sigma_v(\psi)+\beta_v(\psi).
\]

Every nonzero edge covector is counted at both endpoints, so

\[
\sum_v\sigma_v(\psi)=0.
\]

Also

\[
\psi(\kappa)=\sum_v\beta_v(\psi).
\]

Thus in every rank

\[
\boxed{
\psi(\kappa)=\sum_v\rho_v(\psi).
}
\]

Locally, \(\rho_v=1\) means that the three incident covectors are the three
nonzero points of a plane contained in \(\operatorname{Ann}(W_v)\).

Hence:

- rank three: no residue is possible;
- rank four: the first hidden dual-Fano residue appears;
- higher rank: residue vertices carry annihilator-plane data.

Support and residue are observables on the dual incidence pair, not primitive
objects.

## 9. Gauge code and tensor complex

The homogeneous intersection

\[
H_f=L_{\mathrm{vert}}\cap L_{\mathrm{edge}}
\]

contains constant sections \(\Gamma\). For \(k=(k_v)\in H_f\), each edge has a
unique coefficient \(\lambda_e\in\mathbf F_2\) such that

\[
k_u+k_v=\lambda_ef(e).
\]

This induces

\[
\boxed{
H_f/\Gamma\cong\mathcal B_f,
}
\]

the gauge-moduli code.

The tensor operator

\[
T_f:\mathbf F_2^E\to\Gamma\otimes Q_G,
\qquad
T_f(\lambda)=\sum_e\lambda_ef(e)\otimes\bar e
\]

is a reduced edge-coordinate presentation with

\[
\ker T_f=\mathcal B_f.
\]

Dually, quotienting stresses by global alternating stresses gives

\[
\operatorname{EssStress}(f)\cong\mathcal K_f^*.
\]

The tensor complex is therefore a reduced linear compression of the primal-dual
incidence pair after removing constants and canonical alternating stresses.

## 10. Model map

| Model | Construction from \(\mathfrak I_f\) |
|---|---|
| local homogeneous families | \(L_{\mathrm{vert}}\) |
| local affine families | \(\kappa+L_{\mathrm{vert}}\) |
| edge compatibility | \(L_{\mathrm{edge}}\) |
| compatible families | \((\kappa+L_{\mathrm{vert}})\cap L_{\mathrm{edge}}\) |
| quotient sheaf | \(L_{\mathrm{vert}}\to E_f/L_{\mathrm{edge}}\) |
| affine obstruction | class of \(\kappa\) modulo \(L_{\mathrm{vert}}+L_{\mathrm{edge}}\) |
| legal dual configurations | \(L_{\mathrm{vert}}^\perp\) |
| equilibrium stresses | \(L_{\mathrm{vert}}^\perp\cap L_{\mathrm{edge}}^\perp\) |
| Fano self-duality | quadratic identification of primal and dual pairs |
| characteristic torsor | quadratic description of \(\kappa+L_{\mathrm{vert}}\) |
| support / cross-bit / residue | observables on the dual intersection |
| gauge code | \((L_{\mathrm{vert}}\cap L_{\mathrm{edge}})/\Gamma\) in edge coordinates |
| tensor complex | reduced presentation of the primal-dual pair |

## 11. What the compatibility image forgets

The incidence pair does not by itself retain all information used for CDC
extraction. The final step still needs:

- the original graph and dart structure;
- the local even-family interpretation;
- the conversion from matched local labels to global cycles.

The honest architecture is therefore

\[
(G,\Gamma,f)
\longmapsto
\mathfrak I_f
\longmapsto
\text{compatible affine families},
\]

followed by

\[
(G,\Gamma,f,\text{compatible family})
\longmapsto
\text{cycle double cover}.
\]

It would be misleading to call the reduced incidence pair the complete source
object.

## 12. Theory Map v1

### Source geometry
\[
(G,\Gamma,f).
\]

### Compatibility core
\[
\mathfrak I_f
=
(E_f,L_{\mathrm{vert}},L_{\mathrm{edge}},
\kappa+L_{\mathrm{vert}}).
\]

### Primal and dual models
- quotient sheaf and affine equation;
- legal dual configurations and stresses.

### Rank-three enhancement
- canonical quadratic forms;
- Lagrangian intersection;
- characteristic torsor;
- Fano self-duality.

### Scalar observables
- support parity;
- cross-bit;
- dual-Fano residue;
- rank-four Pfaffian residue.

### Reduced compression
- gauge code;
- constraint matroid;
- tensor/Koszul complex.

### Output
- compatible indexed dart family;
- cycle double cover.
