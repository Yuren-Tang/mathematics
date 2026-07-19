# AC-PD-A4 — affine incidence pair complex and exact obstruction interface

**Proof-development state:** `COMPLETE-DRAFT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Depends on:** `AC-PD-A2`, `AC-PD-A3`  
**Immediate consumer:** `AC-PD-A5`  
**External mathematical inputs:** none  
**Formal anchor inspected:** `Yuren-Tang/affine-cdc@ebd7098a7a8b824e8c0a511d3c71f61705672aa8`

## 0. Purpose and retained-data warning

Let `G` be a finite loopless cubic multigraph, not necessarily connected, let `Γ` be a finite-dimensional vector space over `𝔽₂`, and let

\[
f:E(G)\longrightarrow \Gamma\setminus\{0\}
\]

be a nowhere-zero flow. This unit constructs the canonical affine compatibility object

\[
(\mathcal P_f,\kappa)
\]

and proves that all of the following are equivalent:

1. the local affine families admit a globally edge-compatible choice;
2. an affine intersection is nonempty;
3. the distinguished class `[κ]` vanishes in the cokernel of the pair complex;
4. the quotient-sheaf cochain `c_f` is a coboundary;
5. every equilibrium stress annihilates `κ`.

The pair complex is the complete centre of the **compatibility problem**. It is not the whole AffineCDC source object: it does not retain named vertices, edge objects, darts, the combinatorial interpretation of local lines, or the indexed-support extraction. The source data `(G,Γ,f)` must remain attached through A6.

## 1. Local Fano planes

At a vertex `v`, write the three incident edge objects as `e_1,e_2,e_3` and their flow values as

\[
h_i=f(e_i).
\]

Conservation gives

\[
h_1+h_2+h_3=0.
\]

### Lemma 1.1 — the three values are distinct

The values `h_1,h_2,h_3` are pairwise distinct nonzero vectors.

#### Proof

They are nonzero by hypothesis. If, for example, `h_1=h_2`, then characteristic two gives

\[
h_3=h_1+h_2=0,
\]

contradiction. The other cases are identical. ∎

### Lemma 1.2 — local plane

The span

\[
W_v:=\langle h_1,h_2\rangle
\]

is two-dimensional and

\[
W_v\setminus\{0\}=\{h_1,h_2,h_3\}.
\]

#### Proof

The distinct nonzero vectors `h_1,h_2` are linearly independent over `𝔽₂`. Their plane has the four elements

\[
0,h_1,h_2,h_1+h_2,
\]

and `h_1+h_2=h_3`. ∎

No ordering of the three directions is retained in the constructions below.

## 2. Edge quotients and incidence space

For an edge `e`, put

\[
Q_e:=\Gamma/\langle f(e)\rangle.
\]

Since `f(e)\ne0`,

\[
\dim Q_e=\dim\Gamma-1.
\]

Let the incidence or dart set be

\[
I(G):=\{(v,e):e\text{ is incident with }v\}.
\]

Because `G` is loopless, every edge has exactly two darts, one at each endpoint. Parallel edges remain distinct because darts remember the edge object.

Define

\[
E_f:=\bigoplus_{(v,e)\in I(G)}Q_e.
\]

There are two canonical decompositions:

\[
E_f=\bigoplus_{v\in V(G)}E_v,
\qquad
E_v:=\bigoplus_{e\ni v}Q_e,
\]

and

\[
E_f=\bigoplus_{e=uv}
\bigl(Q_e^{(u)}\oplus Q_e^{(v)}\bigr).
\]

Isolated vertices do not occur in the cubic active graph; if an ambient carrier contains them, their local summand is zero.

## 3. Vertex translation subspaces

For every vertex `v`, define

\[
\Delta_v:\Gamma\longrightarrow E_v,
\qquad
\Delta_v(m)=([m]_e)_{e\ni v}.
\]

### Proposition 3.1 — injectivity of `Δ_v`

The map `Δ_v` is injective.

#### Proof

If `Δ_v(m)=0`, then

\[
m\in\langle h_1\rangle
\cap\langle h_2\rangle
\cap\langle h_3\rangle.
\]

Any two distinct one-dimensional subspaces intersect only in zero, so `m=0`. ∎

Put

\[
L_v:=\operatorname{im}\Delta_v,
\qquad
L_{\mathrm{vert}}:=\bigoplus_vL_v.
\]

Thus `Δ_v` identifies `Γ` with `L_v`, and the product map identifies

\[
\Gamma^{V(G)}\cong L_{\mathrm{vert}}.
\]

## 4. The distinguished local translate

Fix an incidence `(v,e)`. Let

\[
h=f(e)
\]

and let `h',h''` be the other two nonzero directions in `W_v`. Since

\[
h'+h''=h,
\]

their quotient classes agree in `Q_e`.

### Definition 4.1 — local characteristic offset

Define

\[
\kappa_{v,e}:=[h']_e=[h'']_e\in Q_e.
\]

This is independent of the choice between the two other directions. Set

\[
\kappa_v:=(\kappa_{v,e})_{e\ni v}\in E_v,
\qquad
\kappa:=(\kappa_v)_v\in E_f.
\]

### Proposition 4.2 — exact local-family formula

For `m\in Γ`, the local family with deleted point `m` has quotient coordinate

\[
\Phi_v(m)_e=[m]_e+\kappa_{v,e}.
\]

Consequently the set of all local even families at `v` is exactly

\[
C_v:=\kappa_v+L_v.
\]

#### Proof

A direction-`h` affine line is a coset of `\langle h\rangle`, hence is encoded by one element of `Q_e`. The line assigned by the deleted-point construction is the translate by `[m]_e` of the distinguished line represented by the class of either other local direction, namely `κ_{v,e}`. Thus its coordinate is `[m]_e+κ_{v,e}`.

It remains to show that this parametrizes **all** local even families and does so uniquely. The local classification proof proceeds as follows.

For a line family `P`, let `P` cover a point `s` in direction `h` when `[s]_h=P(h)`. For the displayed family one computes

\[
[s]_h=[m]_h+\kappa_h
\iff
s+m\in W_v\setminus\{0,h\}.
\]

Hence each point is covered either in no direction or in exactly two of the three directions, so the family is even. If `Φ_v(m)=Φ_v(m')`, then for every local direction `h`, the difference `m+m'` lies in `\langle h\rangle`; the intersection of the three direction lines is zero, so `m=m'`.

Conversely, take any even family `P`. Choose a point on one of its three lines. Evenness forces the incidence pattern at that point and at its translate by the chosen direction to be one of two complementary two-direction patterns. In the first case a deleted point obtained by adding the third direction gives `P`; in the second, adding the second direction does. Checking the three quotient coordinates gives `P=Φ_v(m)`.

This is precisely the coordinate-free theorem represented in the companion Lean files by `localFamily`, `isEven_localFamily`, `localFamily_injective`, `exists_localFamily_eq`, and `localEquiv`. ∎

### Corollary 4.3 — local torsor structure

Translation by `a\in Γ` sends

\[
\Phi_v(m)\longmapsto\Phi_v(m+a).
\]

Thus `C_v` is an affine torsor under `L_v\cong Γ`, and the product of independent local choices is

\[
C_{\mathrm{vert}}
:=\prod_v C_v
=
\kappa+L_{\mathrm{vert}}.
\]

## 5. Edge matching subspace

For an edge `e=uv`, define the diagonal

\[
D_e:=\{(x,x):x\in Q_e\}
\le Q_e^{(u)}\oplus Q_e^{(v)}.
\]

Put

\[
L_{\mathrm{edge}}:=\bigoplus_{e\in E(G)}D_e.
\]

### Proposition 5.1 — edge compatibility

An incidence label tuple `x\in E_f` is edge-compatible exactly when

\[
x\in L_{\mathrm{edge}}.
\]

#### Proof

For each edge, compatibility means that the line selected at its two endpoint darts is the same element of `Q_e`. This is exactly membership of the corresponding pair in `D_e`, independently for every edge. ∎

### Theorem 5.2 — affine intersection formulation

The globally compatible local affine families are exactly

\[
\boxed{
(\kappa+L_{\mathrm{vert}})
\cap L_{\mathrm{edge}}.
}
\]

No connectedness assumption is used.

## 6. The general affine pair complex

Let `E` be a finite-dimensional vector space over `𝔽₂`, let `L,M\le E`, and fix `κ\in E`. Define the two-term complex

\[
\mathcal P(L,M):
L\oplus M\xrightarrow{d}E,
\qquad
d(\ell,m)=\ell+m.
\]

### Proposition 6.1 — homogeneous cohomology

There are canonical identifications

\[
H^0(\mathcal P(L,M))\cong L\cap M,
\]

and

\[
H^1(\mathcal P(L,M))\cong E/(L+M).
\]

#### Proof

The kernel consists of pairs satisfying `ℓ+m=0`. In characteristic two this means `ℓ=m`, so the kernel is the diagonal copy of `L∩M`. The image is `L+M`; quotienting `E` by the image gives the cokernel. ∎

### Theorem 6.2 — affine pair obstruction

The following are equivalent:

1. `(κ+L)\cap M\ne\varnothing`;
2. `κ\in L+M`;
3. `[κ]=0` in `E/(L+M)`.

When nonempty, the affine intersection is a torsor under `L\cap M`.

#### Proof

A point of the intersection has the form

\[
κ+\ell=m
\]

with `ℓ\in L`, `m\in M`, equivalently `κ=ℓ+m\in L+M`. This proves the equivalences.

If `x,x'` are two solutions, then `x+x'\in L\cap M`. Conversely, adding any element of `L\cap M` to a solution remains in both affine sets. The action is free and transitive. ∎

For AffineCDC define

\[
\boxed{
\mathcal P_f:
L_{\mathrm{vert}}\oplus L_{\mathrm{edge}}
\xrightarrow{+}E_f.
}
\]

The distinguished class

\[
[\kappa]\in H^1(\mathcal P_f)
\]

is the complete affine compatibility obstruction, and, when it vanishes, the compatible-family space is a torsor under

\[
H^0(\mathcal P_f)
\cong
L_{\mathrm{vert}}\cap L_{\mathrm{edge}}.
\]

## 7. Quotient-sheaf presentation

For general `L,M\le E`, define

\[
\mathcal Q(L,M):
L\longrightarrow E/M,
\qquad
\ell\longmapsto[\ell].
\]

### Proposition 7.1 — canonical quotient of the pair complex

There is a short exact sequence of two-term complexes

\[
0\longrightarrow
[M\xrightarrow{\mathrm{id}}M]
\longrightarrow
\mathcal P(L,M)
\longrightarrow
\mathcal Q(L,M)
\longrightarrow0.
\]

The first complex is contractible. Hence the quotient map is a quasi-isomorphism and induces the same `H^0` and `H^1`.

#### Proof

Embed `M` in degree zero as `m\mapsto(0,m)` and in degree one as the inclusion `M\hookrightarrow E`. The quotient in degree zero is canonically `L`; in degree one it is `E/M`; the induced differential is `ℓ\mapsto[ℓ]`. Exactness is immediate, and the identity differential gives an explicit contracting homotopy for the first complex. ∎

For an edge `e=uv`, define

\[
\sigma_e:Q_e^{(u)}\oplus Q_e^{(v)}\to Q_e,
\qquad
\sigma_e(x,y)=x+y.
\]

### Lemma 7.2 — quotient by the diagonal

The map `σ_e` is surjective and

\[
\ker\sigma_e=D_e.
\]

Therefore

\[
(Q_e^{(u)}\oplus Q_e^{(v)})/D_e\cong Q_e.
\]

#### Proof

Surjectivity follows from `σ_e(x,0)=x`. In characteristic two, `x+y=0` exactly when `x=y`, which is the diagonal condition. ∎

Taking the direct sum over all edges gives

\[
E_f/L_{\mathrm{edge}}
\cong
\bigoplus_{e\in E(G)}Q_e.
\]

Using `Γ^{V(G)}\cong L_{\mathrm{vert}}`, the quotient differential becomes

\[
\delta_f:\Gamma^{V(G)}
\longrightarrow
\bigoplus_{e=uv}Q_e,
\qquad
(\delta_fm)_e=[m_u+m_v]_e.
\]

Let

\[
c_f:=(\kappa_{u,e}+\kappa_{v,e})_{e=uv}
\in\bigoplus_eQ_e.
\]

### Theorem 7.3 — quotient equation

A vertex parameter tuple `m=(m_v)` gives a compatible affine family if and only if

\[
\boxed{
\delta_fm=c_f.
}
\]

Hence

\[
[c_f]=0\in\operatorname{coker}\delta_f
\iff
[\kappa]=0\in H^1(\mathcal P_f).
\]

#### Proof

At edge `e=uv`, compatibility is

\[
\kappa_{u,e}+[m_u]_e
=
\kappa_{v,e}+[m_v]_e.
\]

Rearranging in characteristic two gives

\[
[m_u+m_v]_e
=
\kappa_{u,e}+\kappa_{v,e}.
\]

These edgewise equations are exactly `δ_fm=c_f`. The cokernel equivalence is the quasi-isomorphism above. ∎

## 8. Dual stress presentation

Let `Q_e^*` denote the linear dual. Pullback along the quotient map `Γ\to Q_e` identifies

\[
Q_e^*\cong\operatorname{Ann}(f(e))
:=\{\alpha\in\Gamma^*: \alpha(f(e))=0\}.
\]

### Lemma 8.1 — annihilator identification

The pullback map is injective and its image is exactly `Ann(f(e))`.

#### Proof

A functional on `Q_e` pulls back to a functional on `Γ` vanishing on the quotient kernel `\langle f(e)\rangle`. Conversely, every functional vanishing on that kernel factors uniquely through the quotient. ∎

An element of `E_f^*` is a tuple of incidence covectors `η_{v,e}\in Q_e^*`.

### Lemma 8.2 — orthogonal of the vertex subspace

A tuple `η` lies in `L_{\mathrm{vert}}^\perp` if and only if at every vertex

\[
\sum_{e\ni v}\eta_{v,e}=0
\quad\text{in }\Gamma^*.
\]

#### Proof

Evaluation on `Δ_v(m)` is

\[
\sum_{e\ni v}\eta_{v,e}([m]_e)
=
\left(\sum_{e\ni v}\eta_{v,e}\right)(m).
\]

This vanishes for every `m\in Γ` exactly when the covector sum is zero. ∎

### Lemma 8.3 — orthogonal of the edge diagonal

A tuple `η` lies in `L_{\mathrm{edge}}^\perp` if and only if for every edge `e=uv`,

\[
\eta_{u,e}=\eta_{v,e}.
\]

#### Proof

Orthogonality to `(x,x)\in D_e` means

\[
\eta_{u,e}(x)+\eta_{v,e}(x)=0
\]

for every `x\in Q_e`, hence equality of the two functionals. ∎

Therefore an element of

\[
L_{\mathrm{vert}}^\perp
\cap
L_{\mathrm{edge}}^\perp
\]

is equivalently an edge labelling

\[
\psi_e\in\operatorname{Ann}(f(e))
\]

whose incident labels sum to zero at every vertex. Call this the equilibrium-stress space `Stress(f)`.

### Theorem 8.4 — Fredholm compatibility criterion

The following are equivalent:

1. compatible local affine families exist;
2. `[κ]=0` in `H^1(\mathcal P_f)`;
3. `[c_f]=0` in `\operatorname{coker}\delta_f`;
4. every equilibrium stress `ψ` satisfies
   \[
   \psi(\kappa)=0.
   \]

#### Proof

The first three equivalences were proved in Theorems 6.2 and 7.3. In finite dimension,

\[
\kappa\in L_{\mathrm{vert}}+L_{\mathrm{edge}}
\]

if and only if every functional annihilating that sum also annihilates `κ`. The annihilator of the sum is

\[
(L_{\mathrm{vert}}+L_{\mathrm{edge}})^\perp
=
L_{\mathrm{vert}}^\perp
\cap
L_{\mathrm{edge}}^\perp
=
\operatorname{Stress}(f).
\]

This gives the fourth equivalence. ∎

## 9. Components and empty cases

### Proposition 9.1 — componentwise direct sum

If `G` is the disjoint union of its edge-bearing components `G_j`, then

\[
E_f=\bigoplus_jE_{f_j},
\quad
L_{\mathrm{vert}}=\bigoplus_jL_{\mathrm{vert},j},
\quad
L_{\mathrm{edge}}=\bigoplus_jL_{\mathrm{edge},j},
\quad
\kappa=\bigoplus_j\kappa_j.
\]

Consequently compatibility holds globally if and only if it holds on every component; the solution torsor is the product of component solution torsors.

#### Proof

Incidences, vertex summands, and edge summands do not cross components. Affine intersection and the pair differential therefore split as direct sums. ∎

### Proposition 9.2 — empty graph

For the empty active graph,

\[
E_f=L_{\mathrm{vert}}=L_{\mathrm{edge}}=0,
\qquad
\kappa=0.
\]

There is one compatible empty family, and the obstruction vanishes.

## 10. Information retained and information forgotten

From `(\mathcal P_f,κ)` one recovers:

- the homogeneous solution space;
- the full obstruction space;
- the distinguished obstruction class;
- the affine solution torsor when nonempty;
- the quotient-sheaf equation;
- the equilibrium-stress dual criterion.

It does **not**, by itself, recover:

- the original named vertex and edge objects;
- the two darts belonging to each edge;
- which quotient summands arose at which incidence;
- the interpretation of a point of `κ+L_vert` as three local affine lines;
- the dart pairing and indexed-support construction;
- rotation, embedding, or surface data.

Accordingly the honest dependency is

\[
(G,\Gamma,f)
\longmapsto
(\mathcal P_f,\kappa)
\longmapsto
\text{compatible affine families},
\]

followed by a separate retained-data construction

\[
(G,\Gamma,f,\text{compatible family})
\longmapsto
\text{indexed graph supports}.
\]

A6 must use this retained source datum; it may not pretend that a bare isomorphism class of pair complexes contains the graph-level cover.

## 11. Formal correspondence boundary

The inspected companion Lean checkpoint defines:

- `LineSpace h = Γ ⧸ span{h}`;
- `lineMk h` as the quotient map;
- `LineFamily`, point coverage, and evenness;
- `κ h` as the common class of either other plane direction;
- `localFamily hP m = lineMk h m + κ h`;
- the bijection `localEquiv : Γ ≃ LocalEvenFamily W`;
- translation equivariance.

Thus the local formula and torsor in Sections 3–4 are not an unsupported paper abstraction. What is **not** machine-checked in this invariant form is the assembled global pair-complex, quadratic reformulation, graph-level multiset extraction, or outer-shell theorem. This dossier does not upgrade those formal-status axes.

## 12. Exported interface

A5 may cite:

1. every cubic flow vertex determines a canonical Fano plane;
2. the edge quotients `Q_e` and incidence space `E_f` are well defined;
3. the local even-family space is exactly `κ_v+L_v` with `L_v≅Γ`;
4. global compatibility is the affine intersection `(κ+L_vert)∩L_edge`;
5. the pair obstruction is `[κ]\in E_f/(L_vert+L_edge)`;
6. the quotient equation is `δ_fm=c_f`;
7. the dual obstruction is evaluation against all equilibrium stresses;
8. the solution set, when nonempty, is a torsor under `L_vert∩L_edge`;
9. all constructions split componentwise;
10. graph/dart/support semantics remain retained external data for A6.

## 13. Completion assessment

`AC-PD-A4` is `COMPLETE-DRAFT`. No contradiction, source gap, or new-mathematics obligation arose. The next dependency-respecting unit is `AC-PD-A5`: canonical quadratic forms on the rank-three edge quotients, local Fano Lagrangians and characteristic torsors, the abstract quadratic-Lagrangian intersection theorem, total singularity of the edge diagonal, and automatic global compatibility.
