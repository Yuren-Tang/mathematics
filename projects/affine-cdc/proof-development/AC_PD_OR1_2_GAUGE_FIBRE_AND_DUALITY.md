# AC-PD-OR1.2 — gauge law, fixed-fibre quotient, and orientation duality

**Proof-development state:** `COMPLETE-DRAFT / FIXED-FIBRE-CLASSIFICATION`  
**Depends on:** OR1.1; integrated Programme-A solution torsor; integrated Programme-B gauge/partial-Petrial theorem  
**Scope:** one fixed finite loopless cubic multigraph and one fixed nowhere-zero `F_2^3`-flow

## 0. What is being proved

The issue-#49 return proposed a gauge transformation law and a fixed-fibre quotient. This dossier proves them from the accepted ingredients rather than treating the audit return as theorem authority.

The two load-bearing inputs are:

1. the labelled compatible-lift fibre above a fixed flow `f` is a torsor under `H_f^0`;
2. the integrated B4 theorem identifies an admissible gauge word with the corresponding partial Petrial of the cycle-face surface.

## 1. The vertical solution torsor

Fix

\[
f:E(G)\longrightarrow\Gamma\setminus\{0\},
\qquad \Gamma=\mathbf F_2^3.
\]

Define

\[
H_f^0=
\left\{
k:V(G)\to\Gamma:
 k_u+k_v\in\langle f(e)\rangle
 \text{ for every }e=uv
\right\}.
\]

Because `f(e)` is nonzero and `F_2` has two scalars, every `k in H_f^0` determines a unique bit `lambda_e(k)` by

\[
k_u+k_v=\lambda_e(k)f(e).
\]

This gives a linear map

\[
\Lambda_f:H_f^0\longrightarrow C^1(G),
\qquad
k\longmapsto\lambda(k),
\]

and the gauge code

\[
\mathcal B_f:=\operatorname{im}\Lambda_f.
\]

The integrated fibre theorem gives a free transitive action

\[
(g,k)\longmapsto g^k
\]

of `H_f^0` on labelled compatible root lifts above `f`. On an edge-bearing disconnected graph,

\[
\ker\Lambda_f=\Gamma^{\pi_0(G)},
\qquad
\mathcal B_f\cong H_f^0/\Gamma^{\pi_0(G)}.
\]

The kernel consists of componentwise constant translations. They preserve the unlabelled surface but relabel every support index on a component by the same affine translation.

## 2. Partial Petrial law

The integrated B4 theorem states

\[
S_{g^k}=S_g^{\tau(\operatorname{supp}\Lambda_f(k))},
\]

where the right side is the partial Petrial obtained by exchanging the two face sides of exactly the selected edge bands.

Choose vertex-disc orientations for `S_g` and transport the local triangle orientations by the translations `k_v`. A partial Petrial on one edge toggles exactly one edge-band twist bit and changes no other bit. Therefore:

### Theorem 2.1 — chain-level gauge law

For transported vertex-disc orientations,

\[
\boxed{
w(g^k)=w(g)+\Lambda_f(k).
}
\]

If a fresh independent choice of vertex-disc orientations is made on `S_{g^k}`, then for some `x in C^0(G)` one has

\[
w_{\mathrm{fresh}}(g^k)
=w(g)+\Lambda_f(k)+\delta x.
\]

Consequently the convention-independent law is

\[
\boxed{
\omega(g^k)
=\omega(g)+[\Lambda_f(k)]
\quad\text{in }C^1(G)/\operatorname{Cut}(G).
}
\]

### Proof

By the B4 correspondence, `lambda_e(k)=1` is precisely the operation that exchanges the two long face sides of the band at `e`. Relative to transported endpoint-disc orientations this converts an untwisted band into a twisted band and conversely, hence adds the coordinate vector of `e` to `w`. Summing over the support of `lambda` gives the first formula. Any other disc-orientation choice differs by vertex reversals and hence by one coboundary, giving the remaining statements. `square`

This proves the proposed law from the actual partial-Petrial theorem; no unproved naturality assertion from the audit return is needed.

## 3. Fixed-fibre obstruction

Let

\[
q:C^1(G)\longrightarrow C^1(G)/\operatorname{Cut}(G)
\]

be the quotient map and define

\[
\Lambda_{\mathrm{or}}:=q\circ\Lambda_f.
\]

For a base lift `g`, define

\[
\mathcal O_g
:=
\{k\in H_f^0:S_{g^k}\text{ is orientable}\}.
\]

By OR1.1 and Theorem 2.1,

\[
k\in\mathcal O_g
\iff
\Lambda_{\mathrm{or}}(k)=\omega(g).
\]

### Theorem 3.1 — labelled fixed-fibre classification

The orientable labelled lifts in the fixed `f`-fibre form either the empty set or one affine torsor:

\[
\boxed{
\mathcal O_g=\varnothing
\quad\text{or}\quad
k_0+\ker\Lambda_{\mathrm{or}}.
}
\]

Equivalently, an orientable lift exists exactly when

\[
\boxed{
w(g)\in\operatorname{Cut}(G)+\mathcal B_f.
}
\]

### Proof

The first assertion is the standard fibre theorem for a linear map: a nonempty inverse image of one point is a coset of the kernel. The second follows because the image of `Lambda_or` is

\[
(\mathcal B_f+\operatorname{Cut}(G))/\operatorname{Cut}(G).
\]

`square`

## 4. Base-independent quotient

Changing the base lift from `g` to `g^{k_1}` changes `w(g)` by an element of `B_f` modulo cuts. Therefore the class

\[
\boxed{
\Omega_f
:=[w(g)]_f
\in
C^1(G)/(\operatorname{Cut}(G)+\mathcal B_f)
}
\]

is independent of the chosen base compatible lift.

### Corollary 4.1

The fixed Fano-flow fibre contains an orientable lift if and only if

\[
\Omega_f=0.
\]

Thus:

- `omega(g) in C^1/Cut` is the obstruction of one fixed lift;
- `Omega_f in C^1/(Cut+B_f)` is the obstruction of the entire fixed-flow fibre.

These objects must not be conflated.

## 5. Unlabelled surface classification

Two fields with the same gauge word differ by a componentwise constant translation and hence give the same unlabelled partial-Petrial surface with an affine relabelling of face indices. The set of orientable gauge words is

\[
\mathcal P_g
:=
\{\lambda\in\mathcal B_f:w(g)+\lambda\in\operatorname{Cut}(G)\}.
\]

### Corollary 5.1

One has

\[
\boxed{
\mathcal P_g=\varnothing
\quad\text{or}\quad
\lambda_0+igl(\mathcal B_f\cap\operatorname{Cut}(G)\bigr).
}
\]

Hence labelled orientable lifts are a torsor under

\[
\Lambda_f^{-1}(\operatorname{Cut}(G)),
\]

while unlabelled orientable surfaces in the vertical orbit are a coset under

\[
\mathcal B_f\cap\operatorname{Cut}(G).
\]

## 6. Dual orientation criterion

Use the standard edge dot product on `C^1(G)`. Since all spaces are finite dimensional,

\[
(\operatorname{Cut}(G)+\mathcal B_f)^\perp
=
\operatorname{Cut}(G)^\perp\cap\mathcal B_f^\perp.
\]

Put

\[
Z_1(G):=\operatorname{Cut}(G)^\perp
\]

and define the orientation-stress space

\[
\boxed{
\operatorname{Stress}_{\mathrm{or}}(f)
:=Z_1(G)\cap\mathcal B_f^\perp.
}
\]

### Theorem 6.1 — dual holonomy/stress criterion

The fixed `f`-fibre contains an orientable lift if and only if

\[
\boxed{
\langle w(g),z\rangle=0
\quad
\text{for every }z\in\operatorname{Stress}_{\mathrm{or}}(f).
}
\]

If the condition fails, any `z` with nonzero pairing is simultaneously:

1. a source-cycle twist holonomy;
2. a linear functional annihilating every accessible gauge/Petrial word;
3. a certificate that `Omega_f` is nonzero.

### Proof

By finite-dimensional annihilator duality,

\[
w(g)\in\operatorname{Cut}(G)+\mathcal B_f
\]

if and only if it is annihilated by the orthogonal complement of that sum. Apply Theorem 3.1. `square`

## 7. Code-theoretic form

The integrated gauge chapter proves, componentwise,

\[
\mathcal B_f
=
\bigl(\mathcal C(G)*\mathcal F_f\bigr)^\perp,
\]

where `C(G)` is the binary cycle space, `F_f` is the span of the coordinate words of the fixed flow, and `*` denotes coordinatewise product. Therefore

\[
\mathcal B_f^\perp
=
\mathcal C(G)*\mathcal F_f
\]

and

\[
\boxed{
\operatorname{Stress}_{\mathrm{or}}(f)
=
\mathcal C(G)
\cap
\bigl(\mathcal C(G)*\mathcal F_f\bigr).
}
\]

This is an exact alternate presentation, not a claim that every element has already been localized or classified.

## 8. Separation from the compatibility stress

Programme A identifies the compatible-solution moduli `H_f^0` with the dual of the original affine compatibility obstruction space. That self-duality proves existence of compatible lifts.

The orientation-stress space above is different:

- it lives in the source edge-word space;
- it annihilates the **image** of accessible Petrial words;
- it tests whether one already compatible lift can be made orientable.

Thus automatic compatibility does not imply automatic orientability. Any identification between the two stress presentations requires an additional explicit map and cannot be inferred from the Fano self-duality slogan.

## 9. Exact closure and open boundary

Closed in this unit:

1. the chain-level gauge law;
2. the quotient law for `omega`;
3. the base-independent fixed-fibre obstruction `Omega_f`;
4. the empty-or-torsor classification;
5. the exact dual criterion.

Not closed:

1. `Omega_f=0` for every fixed Fano flow;
2. existence of some Fano flow with `Omega_f=0` on every bridgeless cubic graph;
3. any monotone horizontal reconfiguration theorem for `Omega_f`.

These are genuine graph-level existence questions, not missing linear algebra.
