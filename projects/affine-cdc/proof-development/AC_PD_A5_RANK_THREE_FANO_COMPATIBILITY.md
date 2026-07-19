# AC-PD-A5 — rank-three Fano compatibility by quadratic Lagrangian intersection

**Proof-development state:** `COMPLETE-DRAFT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Depends on:** `AC-PD-A4`  
**Immediate consumer:** `AC-PD-A6`  
**External mathematical inputs:** none

## 0. Main theorem

Let `G` be a finite loopless cubic multigraph, not necessarily connected, and let

\[
f:E(G)\longrightarrow \Gamma\setminus\{0\},
\qquad
\Gamma=\mathbf F_2^3,
\]

be a nowhere-zero flow. Let

\[
(\mathcal P_f,\kappa)
\]

be the affine incidence pair constructed in A4. Then

\[
\boxed{
(\kappa+L_{\mathrm{vert}})
\cap L_{\mathrm{edge}}
e\varnothing.
}
\]

Equivalently,

\[
[\kappa]=0\in H^1(\mathcal P_f),
\qquad
[c_f]=0\in\operatorname{coker}\delta_f.
\]

The compatible-family space is a torsor under

\[
L_{\mathrm{vert}}\cap L_{\mathrm{edge}}
\cong H_f^0.
\]

The proof is invariant and basis-free at the theorem level: each edge quotient is a canonical anisotropic quadratic plane; each local affine family is a characteristic torsor of a Fano Lagrangian; the global edge diagonal is a totally singular Lagrangian; an abstract quadratic-Lagrangian theorem forces intersection.

## 1. Canonical quadratic structure on a binary plane

Let `U` be a two-dimensional vector space over `𝔽₂`. Define

\[
q_U(u)=
\begin{cases}
0,&u=0,\\
1,&u\ne0.
\end{cases}
\]

Define its polarization

\[
B_U(u,v):=q_U(u+v)+q_U(u)+q_U(v).
\]

### Proposition 1.1 — canonical anisotropic plane

The map `q_U` is a quadratic form, and `B_U` is the unique nonzero alternating bilinear form on `U`. It is nondegenerate. Moreover `q_U` has no nonzero singular vector.

#### Proof

If `u,v` are linearly dependent, then one of them is zero or `u=v`; direct substitution gives `B_U(u,v)=0`. If they are independent, the three vectors `u,v,u+v` are all nonzero, so

\[
B_U(u,v)=1+1+1=1
\]

in `𝔽₂`. Thus relative to any basis `(u,v)`, the Gram matrix is

\[
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

which is bilinear, alternating, and nondegenerate. Since the space of alternating forms on a binary plane is one-dimensional, this is the unique nonzero one. Finally, the definition gives `q_U(x)=1` for every nonzero `x`. ∎

## 2. Edge quotient planes in rank three

The one-dimensional space

\[
\Lambda^3\Gamma^*
\]

over `𝔽₂` has a unique nonzero element; denote it by

\[
\omega.
\]

For `0\ne h\in Γ`, put

\[
Q_h:=\Gamma/\langle h\rangle.
\]

This is a binary plane. Its canonical quadratic form is

\[
q_h([x])=
\begin{cases}
0,&x\in\langle h\rangle,\\
1,&x\notin\langle h\rangle.
\end{cases}
\]

### Proposition 2.1 — polar determinant formula

The polar form of `q_h` is

\[
\boxed{
B_h([x],[y])=\omega(h,x,y).
}
\]

#### Proof

The right-hand side is unchanged if `x` or `y` is altered by a multiple of `h`, so it descends to `Q_h`. It is alternating and nonzero: choose `x,y` whose images form a basis of `Q_h`; then `(h,x,y)` is a basis of `Γ`, so `ω(h,x,y)=1`. By Proposition 1.1 there is only one nonzero alternating form on `Q_h`, namely the polarization of its canonical anisotropic quadratic form. ∎

In particular each `(Q_h,q_h)` is a nondegenerate quadratic plane.

## 3. Local Fano incidence space

Let `W\le Γ` be a plane and let

\[
D:=W\setminus\{0\}=\{h_1,h_2,h_3\},
\qquad
h_1+h_2+h_3=0.
\]

Define

\[
E_W:=\bigoplus_{h\in D}Q_h,
\qquad
q_W:=\sum_{h\in D}q_h,
\qquad
B_W:=\sum_{h\in D}B_h.
\]

Then `E_W` has dimension six and `B_W` is nondegenerate as a direct sum of three nondegenerate planes.

Define

\[
\Delta_W:\Gamma\longrightarrow E_W,
\qquad
\Delta_W(x)=([x]_h)_{h\in D},
\]

and put

\[
L_W:=\operatorname{im}\Delta_W.
\]

### Theorem 3.1 — local Fano Lagrangian

The map `Δ_W` is injective and `L_W` is Lagrangian in `(E_W,B_W)`.

#### Proof

If `Δ_W(x)=0`, then `x` lies in all three distinct lines `\langle h\rangle`, whose common intersection is zero. Hence `Δ_W` is injective and

\[
\dim L_W=3=\tfrac12\dim E_W.
\]

For `x,y\in Γ`, Proposition 2.1 gives

\[
\begin{aligned}
B_W(\Delta_Wx,\Delta_Wy)
&=\sum_{h\in D}\omega(h,x,y)\\
&=\omega\left(\sum_{h\in D}h,x,y\right)\\
&=0.
\end{aligned}
\]

Thus `L_W` is isotropic of half dimension, hence Lagrangian. ∎

## 4. Quadratic transgression on the Fano diagonal

Let

\[
\ell_W:\Gamma\longrightarrow\mathbf F_2
\]

be the unique nonzero linear functional with kernel `W`.

### Theorem 4.1 — Fano transgression

For every `x\in Γ`,

\[
\boxed{
q_W(\Delta_Wx)=\ell_W(x).
}
\]

#### Proof

By definition,

\[
q_W(\Delta_Wx)
=
\sum_{h\in D}\mathbf 1_{x\notin\langle h\rangle}.
\]

If `x=0`, all three terms vanish. If `x\in W\setminus\{0\}`, it lies in exactly one of the three nonzero lines of `W`; one term vanishes and two equal one, giving zero in `𝔽₂`. If `x\notin W`, it lies in none of the three lines, so all three terms equal one and the sum is one. This is precisely the functional with kernel `W`. ∎

Thus the restriction of the six-dimensional quadratic form to the Lagrangian `L_W` is linear rather than zero.

## 5. Characteristic torsors

Let `(E,q)` be a finite-dimensional nondegenerate quadratic space over `𝔽₂`, with polar form `B`, and let `L\le E` be Lagrangian. Since `B|_L=0`, the restriction `q|_L` is linear. Define

\[
\operatorname{Char}_q(L)
:=
\{a\in E:B(z,a)=q(z)\text{ for every }z\in L\}.
\]

### Proposition 5.1 — existence and torsor structure

The set `Char_q(L)` is nonempty and is an affine torsor under `L`.

#### Proof

Consider the restriction map

\[
\rho:E\longrightarrow L^*,
\qquad
\rho(a)=B(-,a)|_L.
\]

Nondegeneracy of `B` identifies `E` with `E^*`. Every functional on `L` extends to `E`, so `ρ` is surjective. Its kernel is

\[
L^\perp=L
\]

because `L` is Lagrangian. The fibre over the linear functional `q|_L` is therefore nonempty and is one affine coset of `L`. ∎

## 6. The local affine family is the characteristic torsor

For each `h\in D`, let `κ_h\in Q_h` be the common class of the other two nonzero elements of `W`, and put

\[
\kappa_W:=(\kappa_h)_{h\in D}\in E_W.
\]

### Lemma 6.1 — local cross-pairing identity

For every `x\in Γ`,

\[
\boxed{
B_W(\Delta_Wx,\kappa_W)=\ell_W(x).
}
\]

#### Proof

Both sides are linear in `x`. Choose independent `a,b\in W`, put `c=a+b`, and choose `t\notin W` with `ω(a,b,t)=1`. Use the representatives

\[
\kappa_a=[b]_a,
\qquad
\kappa_b=[a]_b,
\qquad
\kappa_c=[a]_c.
\]

Write

\[
x=\alpha a+\beta b+\gamma t.
\]

By Proposition 2.1 and alternation,

\[
\begin{aligned}
B_W(\Delta_Wx,\kappa_W)
&=\omega(a,x,b)+\omega(b,x,a)+\omega(c,x,a)\\
&=\gamma+\gamma+\gamma\\
&=\gamma.
\end{aligned}
\]

The coordinate `γ` is exactly `\ell_W(x)`. The computation is independent of the displayed representative choices because each `κ_h` is a quotient class. ∎

### Theorem 6.2 — characteristic description of local families

One has

\[
\boxed{
\kappa_W\in\operatorname{Char}_{q_W}(L_W),
\qquad
\operatorname{Char}_{q_W}(L_W)=\kappa_W+L_W.
}
\]

Under A4's local classification, this is exactly the set of local affine even families at a vertex with flow plane `W`.

#### Proof

For `z=Δ_Wx`, Lemma 6.1 and Theorem 4.1 give

\[
B_W(z,\kappa_W)=\ell_W(x)=q_W(z).
\]

Thus `κ_W` is characteristic. Proposition 5.1 says the characteristic set is the affine coset `κ_W+L_W`. A4 identifies the same coordinate coset with the complete local-family space. ∎

### Corollary 6.3 — anisotropic affine Lagrangian

The quadratic form is constant on `κ_W+L_W`, and its value is one.

#### Proof

For `z\in L_W`, characteristicity gives

\[
q_W(\kappa_W+z)
=q_W(\kappa_W)+q_W(z)+B_W(\kappa_W,z)
=q_W(\kappa_W).
\]

Every component of `κ_W` is nonzero, so

\[
q_W(\kappa_W)=1+1+1=1.
\]

∎

## 7. Abstract quadratic-Lagrangian intersection

### Lemma 7.1 — orthogonal of an intersection

For subspaces `L,M` of a finite-dimensional nondegenerate bilinear space,

\[
(L\cap M)^\perp=L^\perp+M^\perp.
\]

If `L,M` are Lagrangian, then

\[
(L\cap M)^\perp=L+M.
\]

#### Proof

The inclusion `L^⊥+M^⊥\subseteq(L\cap M)^⊥` is immediate. For equality, compare dimensions:

\[
\dim(L^\perp+M^\perp)
=
\dim L^\perp+\dim M^\perp-\dim(L^\perp\cap M^\perp),
\]

and use nondegeneracy together with

\[
L^\perp\cap M^\perp=(L+M)^\perp.
\]

Both sides have dimension `\dim E-\dim(L\cap M)`. For Lagrangians, `L^⊥=L` and `M^⊥=M`. ∎

### Theorem 7.2 — characteristic-torsor intersection theorem

Let `(E,q)` be a finite-dimensional nondegenerate quadratic space over `𝔽₂`, and let `L,M\le E` be Lagrangians. Then

\[
\boxed{
\operatorname{Char}_q(L)\cap M\ne\varnothing
\iff
q|_{L\cap M}=0.
}
\]

When nonempty, the intersection is a torsor under `L\cap M`.

#### Proof

Suppose `m\in\operatorname{Char}_q(L)\cap M`. For `z\in L\cap M`,

\[
q(z)=B(z,m)=0
\]

because `z,m\in M` and `M` is isotropic.

Conversely, choose `κ\in\operatorname{Char}_q(L)` and assume `q` vanishes on `L\cap M`. Then for every `z\in L\cap M`,

\[
B(z,\kappa)=q(z)=0,
\]

so by Lemma 7.1,

\[
\kappa\in(L\cap M)^\perp=L+M.
\]

Write `κ=ℓ+m` with `ℓ\in L`, `m\in M`. Since `Char_q(L)=κ+L`,

\[
m=\kappa+\ell\in\operatorname{Char}_q(L)\cap M.
\]

Differences of two intersection points lie in `L\cap M`, and translation by that intersection preserves both sets; hence the intersection is a torsor under `L\cap M`. ∎

### Corollary 7.3 — totally singular target

If `M` is a totally singular Lagrangian, meaning `q|_M=0`, then

\[
\operatorname{Char}_q(L)\cap M\ne\varnothing.
\]

## 8. Global quadratic incidence space

Return to the finite cubic flow graph `(G,f)`. On every incidence quotient use the canonical form `q_e=q_{f(e)}` and define

\[
q_f:=\sum_{(v,e)\in I(G)}q_e,
\qquad
B_f:=\sum_{(v,e)\in I(G)}B_e
\]

on `E_f`.

### Proposition 8.1 — nondegeneracy

The quadratic space `(E_f,q_f)` is nondegenerate.

#### Proof

Its polar form is the direct sum of the nondegenerate polar forms on the incidence quotient planes. ∎

### Proposition 8.2 — vertex Lagrangian and characteristic torsor

The subspace

\[
L_{\mathrm{vert}}=\bigoplus_vL_v
\]

is Lagrangian, and

\[
\boxed{
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
=
\kappa+L_{\mathrm{vert}}.
}
\]

#### Proof

At each vertex, Theorems 3.1 and 6.2 give a local Lagrangian and its characteristic torsor. Direct sums preserve nondegeneracy, Lagrangian dimension, and characteristic equations componentwise. ∎

### Proposition 8.3 — edge diagonal is totally singular Lagrangian

For an edge `e=uv`, the diagonal

\[
D_e:=\{(x,x):x\in Q_e\}
\le Q_e^{(u)}\oplus Q_e^{(v)}
\]

is a totally singular Lagrangian for the quadratic form `q_e\oplus q_e`. Consequently

\[
L_{\mathrm{edge}}:=\bigoplus_eD_e
\]

is a totally singular Lagrangian in `(E_f,q_f)`.

#### Proof

For diagonal vectors `(x,x)` and `(y,y)`,

\[
(B_e\oplus B_e)((x,x),(y,y))
=B_e(x,y)+B_e(x,y)=0.
\]

Thus `D_e` is isotropic. Its dimension is `\dim Q_e=2`, exactly half the dimension of `Q_e\oplus Q_e`, so it is Lagrangian. Moreover

\[
(q_e\oplus q_e)(x,x)=q_e(x)+q_e(x)=0,
\]

so it is totally singular. Direct sums preserve both properties. ∎

## 9. Rank-three automatic compatibility

### Theorem 9.1 — global Fano compatibility

One has

\[
\boxed{
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
\cap L_{\mathrm{edge}}
e\varnothing.
}
\]

Equivalently, the AffineCDC local families admit a globally compatible choice.

#### Proof

By Propositions 8.2 and 8.3, `L_vert` and `L_edge` are Lagrangians and `L_edge` is totally singular. Apply Corollary 7.3. A4 identifies the resulting intersection point with a globally edge-compatible choice of local affine families. ∎

### Corollary 9.2 — obstruction vanishing and full moduli

The obstruction classes vanish:

\[
[\kappa]=0\in H^1(\mathcal P_f),
\qquad
[c_f]=0\in\operatorname{coker}\delta_f.
\]

The compatible-family space is a torsor under

\[
L_{\mathrm{vert}}\cap L_{\mathrm{edge}}
\cong H_f^0.
\]

#### Proof

Use A4's equivalence between compatibility, obstruction vanishing, and the solution torsor. ∎

## 10. Lower-resolution forms of the same proof

The invariant theorem contains two familiar coarser presentations.

### Proposition 10.1 — quadratic handshaking

For every `z\in L_{\mathrm{vert}}\cap L_{\mathrm{edge}}`,

\[
q_f(z)=0.
\]

#### Proof

The same quotient vector occurs at the two endpoint incidences of each edge, so

\[
q_f(z)=\sum_eq_e(z_e)=2\sum_eq_e(z_e)=0.
\]

This is exactly the restriction condition in Theorem 7.2. ∎

### Proposition 10.2 — stress cancellation

Under the polar self-duality of the quotient planes, every equilibrium stress `ψ` satisfies

\[
\psi(\kappa)=0.
\]

#### Proof

The local characteristic identity reads

\[
\psi_v(\kappa_v)=q_v(\psi_v).
\]

Summing over vertices and using edge matching of the stress gives

\[
\psi(\kappa)
=
\sum_vq_v(\psi_v)
=
2\sum_eq_e(\psi_e)
=0.
\]

This is A4's Fredholm criterion. ∎

Recording only whether each quotient component is nonzero turns `q_v` into the local support parity or cross-bit and the global sum into boundary cancellation. These are projections of the same quadratic identity, not independent proofs with stronger hypotheses.

## 11. Components and degenerate cases

### Disconnected graph

Every quadratic incidence object is a direct sum over edge-bearing components. The theorem applies either globally or independently componentwise. No connectedness hypothesis is present.

### Empty graph

For the empty active graph, `E_f=0`; both Lagrangians and `κ` are zero. Their intersection contains the unique zero vector.

### Parallel edges

Each parallel edge contributes its own pair of quotient-plane incidence summands and its own diagonal. No step identifies edge objects sharing endpoints.

### Loops

The representation is loopless by A1–A3. A loop would have one edge object but two oriented endpoint occurrences, whereas the current graph/dart API and edge-diagonal decomposition are formulated for two distinct endpoint darts. No loop extension is asserted here.

### Rank boundary

The proof uses that every `Q_e` is a two-dimensional anisotropic quadratic plane and that the three local flow directions are exactly the nonzero points of a plane in `Γ`. It is a rank-three theorem. It does not imply automatic compatibility in rank four or above.

## 12. Formal and output boundary

The companion Lean repository machine-checks rank-three compatibility in the original branching/cross-bit presentation. A4 verifies the exact local-family coordinate correspondence. The invariant characteristic-torsor and quadratic-Lagrangian assembly in this dossier is a complete paper proof but is not thereby a checked Lean theorem in this form.

The theorem outputs a compatible collection of local affine families. It does not by itself reconstruct the dart permutation or graph-level indexed supports. A6 must retain the original graph, flow, and local combinatorial data and prove the support extraction and exact edge multiplicity two.

## 13. Exported interface

A6 may cite:

1. every rank-three edge quotient has a canonical nondegenerate anisotropic quadratic form;
2. every local translation space is Lagrangian;
3. every local affine-family coset is exactly its characteristic torsor;
4. the global vertex space is Lagrangian;
5. the global edge diagonal is a totally singular Lagrangian;
6. the characteristic torsor intersects the edge diagonal;
7. therefore compatible local affine families exist on every finite cubic loopless `F₂³`-flow graph, without connectedness;
8. the full compatible-family moduli is the torsor under `L_vert∩L_edge`;
9. graph/dart data remain required for support extraction.

## 14. Completion assessment

`AC-PD-A5` is `COMPLETE-DRAFT`. No contradiction, external source gap, or genuine frontier question arose. The next dependency-respecting unit is `AC-PD-A6`: exact graph-level indexed even-support extraction, including the retained dart construction, vertex parity, exact edge multiplicity two, empty and repeated supports, and flattening to a multiset witness.
