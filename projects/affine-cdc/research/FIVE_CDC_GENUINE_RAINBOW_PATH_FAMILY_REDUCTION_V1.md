# Genuine rainbow path families and the final zero-norm reduction

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level reduction of each genuine three-switch loop; exact finite obstruction signature for the physical lift family; a cube-coordinate model is retained only conditionally  
**Parents:** `FIVE_CDC_RAINBOW_SWITCH_FLOW_TAIT_RESOLUTION_V1.md`, `FIVE_CDC_TYPE_H_TAIT_ESCAPE_V1.md`, `FIVE_CDC_TYPE_H_LOCAL_TO_GLOBAL_HOLONOMY_STACK_V1.md`

## 1. Purpose

The preceding local-to-global packet allowed the rank-one switch-flow support to contain a terminal path together with closed components. That is correct for an arbitrary rank-one quotient flow, but it is too broad for a genuine rainbow loop.

A genuine rainbow loop is the composite of three switches on three individual terminal-path components. Let these paths be

\[
P_0,\qquad P_1,\qquad P_2,
\]

in routing-colour order. The first and third switches have the same transported support coefficient `u`; the middle switch has coefficient `v`. Therefore

\[
\boxed{
 t_\gamma
 =
 (P_0\triangle P_2)\otimes u
 +
 P_1\otimes v.
}
\]

This path formula sharpens every zero-norm lifting obstruction for one physical lifted loop.

The principal conclusions are:

1. for rank-one monodromy types `2^2 1` and `3 2`, zero norm forces
   \[
   P_1=P_0\triangle P_2;
   \]
2. consequently the nonzero switch-flow support is exactly the single middle terminal path `P_1`;
3. a rank-one zero-norm lift either has an all-zero vertex, or `P_1` is a spanning terminal path and a Tait resolution exists;
4. the previously possible odd closed component cannot occur in a genuine three-path loop;
5. for full-rank types `4 1` and `5`, a Tait resolution exists exactly when
   \[
   E(P)=P_1\cup(P_0\triangle P_2);
   \]
6. the complete physical lift family is therefore labelled only by ambient translations, uncovered-edge sets, and missed-vertex sets;
7. a `27`-state cube model exists as an exact abstract local model if the path-component choices can be coherently trivialised, but that global trivialisation has not yet been proved.

No five-cycle double cover theorem is claimed.

## 2. The genuine three-path formula

Let `x` be the initial indexed root cover and `x^gamma` the cover after the three physical path switches, before support names are quotiented. For the canonical rainbow word the transported switch coefficients are

\[
w_0=u,\qquad w_1=v,\qquad w_2=u,
\]

with `u,v` independent in the switch plane

\[
W=\langle u,v\rangle\cong F_2^2.
\]

Since switching a path component adds its incidence chain tensored with the transported support-pair coefficient,

\[
x^\gamma
=
 x+P_0\otimes u+P_1\otimes v+P_2\otimes u.
\]

Hence the switch flow is

\[
\boxed{
 t_\gamma=x+x^\gamma
 =(P_0\triangle P_2)\otimes u+P_1\otimes v.
}
\]

Put

\[
A:=P_0\triangle P_2,
\qquad
B:=P_1.
\]

Then edgewise the four switch-flow values are

\[
\begin{array}{c|c|c}
1_A&1_B&t_\gamma\\
\hline
0&0&0\\
1&0&u\\
0&1&v\\
1&1&\kappa:=u+v.
\end{array}
\]

This is the only edgewise information needed for the single-loop theorems.

## 3. Rank-one monodromy collapses to one terminal path

Let the support permutation `pi` have type `2^2 1` or `3 2`, and assume the ambient norm defect vanishes.

The exact root-image theorem gives

\[
W\cap\operatorname{im}(1+\pi)
=
\{0,\kappa\}.
\]

Since a zero-norm switch flow is of the form

\[
t_\gamma=(1+\pi)r,
\]

every edge value of `t_gamma` is either `0` or `kappa`.

### Theorem 3.1 — rank-one path identity

\[
\boxed{
P_1=P_0\triangle P_2.
}
\]

Consequently

\[
\boxed{
 t_\gamma=\kappa\,1_{P_1}.
}
\]

#### Proof

In the basis `u,v`, the values `0,kappa` are exactly the vectors whose two coordinates are equal. The `u`-coordinate of `t_gamma` is `1_{P_0\triangle P_2}`, while the `v`-coordinate is `1_{P_1}`. Equality of the two coordinates on every edge gives the identity. ∎

### Corollary 3.2 — no genuine odd-component branch

The nonzero support of a rank-one genuine loop is the single path component `P_1`. It contains no closed component.

Thus the odd closed components allowed by an arbitrary rank-one quotient flow are absent from the genuine rainbow loop.

## 4. Spanning-path dichotomy

The middle switch `P_1` is a terminal path component of a relative even subgraph. At an internal vertex it has degree either zero or two.

### Proposition 4.1 — nonspanning means empty vertex relation

If `P_1` omits an internal vertex `w`, then all three edges incident with `w` have switch-flow value zero. Hence the root-fibre vertex relation at `w` is empty for types `2^2 1` and `3 2`.

#### Proof

By Theorem 3.1, `t_gamma` is nonzero precisely on `P_1`. A vertex outside the path has no incident path edge. Apply the previously proved all-zero-vertex obstruction. ∎

### Lemma 4.2 — a cubic four-pole has even order

If `P` has `n` internal cubic vertices, `m` internal edges, and four terminal semiedges, then

\[
3n=2m+4.
\]

Therefore `n` is even.

### Theorem 4.3 — genuine rank-one zero-norm dichotomy

For a genuine lifted rainbow loop of support type `2^2 1` or `3 2` with zero ambient norm, exactly one of the following occurs:

1. `P_1` is not spanning, and an all-zero internal vertex gives an empty local root relation;
2. `P_1` is a spanning terminal path, and a root lift exists; equivalently the loop has a Tait resolution.

#### Proof

If `P_1` is not spanning, apply Proposition 4.1.

If `P_1` is spanning, it contains every internal vertex exactly once. Its complement is a perfect matching of the internal vertices together with the two zero-valued terminal semiedges. The matching-complement degree-two system has only the one terminal path `P_1`, with `n` internal vertices. By Lemma 4.2, `n` is even. The exact even-component lifting theorem therefore supplies a root lift. ∎

### Corollary 4.4 — rank-one Tait escape

Inside a minimal Type H kernel, every zero-norm rank-one lifted loop must have a nonspanning middle path. A spanning middle path would give a Tait resolution and hence strict boundary-profile escape.

Thus the genuine rank-one residual mechanism is not oddness. It is:

\[
\boxed{
\text{the selected middle Kempe path misses an internal vertex}.
}
\]

## 5. Full-rank monodromy is an XOR path-cover problem

Let `pi` have type `4 1` or `5`. The exact root-fibre theorem says that a zero-norm root lift exists if and only if `t_gamma` has no zero edge.

By the edge table in Section 2,

\[
t_\gamma(e)=0
\quad\Longleftrightarrow\quad
 e\notin P_1
 \text{ and }
 e\notin P_0\triangle P_2.
\]

### Theorem 5.1 — full-rank path-cover criterion

For a genuine zero-norm rainbow loop of support type `4 1` or `5`, the following are equivalent:

1. the loop is root-admissibly linearizable;
2. the switch flow has no zero edge;
3. the two path chains cover every edge:
   \[
   \boxed{
   E(P)=P_1\cup(P_0\triangle P_2);
   }
   \]
4. the loop has a Tait resolution.

#### Proof

The equivalence of root linearization, no zero edge, and Tait resolution is the full-rank part of the preceding switch-flow theorem. The equivalence with the displayed path cover follows directly from the edgewise formula. ∎

### Corollary 5.2 — full-rank residual certificate

Inside a minimal Type H kernel, every zero-norm full-rank lift has an edge

\[
e\notin P_1\cup(P_0\triangle P_2).
\]

Thus the residual obstruction is a concrete uncovered edge of a two-chain path cover.

## 6. The complete genuine zero-norm ladder

For one genuine lifted loop the preceding local-to-global stack sharpens to:

\[
\boxed{
\begin{array}{c|c|c}
\text{support type}&\text{success condition}&\text{residual certificate}\\
\hline
5,4 1&E=P_1\cup(P_0\triangle P_2)&\text{an uncovered edge}\\
3 2,2^2 1&P_1=P_0\triangle P_2\text{ and }P_1\text{ spanning}&\text{a nonspanning middle path}.
\end{array}
}
\]

If the success condition holds, a Tait resolution exists and the Type H Tait-escape theorem destroys the minimal triangle profile.

The component-holonomy oddness branch was an artefact of allowing an arbitrary rank-one switch flow. It is removed from each genuine three-path loop.

## 7. The unconditional physical lift-family signature

Let `Lambda` be the finite set of physical lifted rainbow loops over one triangle shore, including terminal-path-component and repeated-trace-role choices. For every

\[
\lambda\in\Lambda
\]

record:

- its support permutation `pi_lambda`;
- its ambient norm defect
  \[
  d_\lambda=N_{\pi_\lambda}z_\lambda;
  \]
- its selected terminal paths
  \[
  P_0^\lambda,P_1^\lambda,P_2^\lambda.
  \]

Define the **physical obstruction signature**

\[
\mathfrak S(\lambda)
=
\begin{cases}
(\mathrm A,d_\lambda),
&d_\lambda\ne0;\\[1mm]
(\mathrm F,U_\lambda),
&d_\lambda=0,\ \pi_\lambda\text{ full rank};\\[1mm]
(\mathrm R,X_\lambda),
&d_\lambda=0,\ \pi_\lambda\text{ rank one},
\end{cases}
\]

where

\[
U_\lambda
:=
E(P)\setminus
\bigl(P_1^\lambda\cup(P_0^\lambda\triangle P_2^\lambda)\bigr)
\]

and

\[
X_\lambda
:=
V_{\mathrm{int}}(P)\setminus V(P_1^\lambda).
\]

### Theorem 7.1 — exact family obstruction criterion

For every physical lifted loop `lambda` in a minimal Type H kernel, at least one of the following holds:

\[
\boxed{
 d_\lambda\ne0,
 \qquad
 U_\lambda\ne\varnothing,
 \qquad
 X_\lambda\ne\varnothing.
}
\]

Conversely, if one physical lift has

\[
d_\lambda=0
\]

and the corresponding set `U_lambda` or `X_lambda` is empty, then that lift has a Tait resolution and the triangle profile escapes.

#### Proof

Apply the ambient norm theorem first. If the norm vanishes, apply Theorem 5.1 in the full-rank case and Theorem 4.3 in the rank-one case. Then apply the Type H Tait-escape theorem. ∎

This is the correct unconditional family-level object. The remaining target is to prove that a family in which every leaf carries one of these obstructions has a common geometric witness.

## 8. Conditional cube trivialisation and the abstract `27`-state alphabet

It is tempting to choose, for each of the three challenge stages, two fixed terminal paths

\[
P_j^0,P_j^1
\]

and identify every physical lift with

\[
\epsilon=(\epsilon_0,\epsilon_1,\epsilon_2)\in F_2^3.
\]

This requires a coherent trivialisation of the path-component choices through the lifted reconfiguration groupoid. Such a trivialisation is not currently proved: a later challenge subgraph may depend on earlier switches and support transport.

Conditional on such a trivialisation, put

\[
A_\epsilon=P_0^{\epsilon_0}\triangle P_2^{\epsilon_2},
\qquad
B_\epsilon=P_1^{\epsilon_1}.
\]

For an edge `e`, record

\[
\sigma(e)=(s_0,s_1,s_2)\in\{\bot,0,1\}^3,
\]

where `s_j=i` means `e in P_j^i`, and `s_j=bot` means `e` lies in neither terminal path of system `j`. Define

\[
\mathcal Z_e
=
\left\{
\epsilon\in F_2^3:
 e\notin A_\epsilon\cup B_\epsilon
\right\}.
\]

### Computational Proposition 8.1 — abstract local alphabet

Among the `27` formal states `sigma in {bot,0,1}^3`, the cardinalities of `Z_e` are distributed as

\[
\boxed{
1\text{ state of size }8,
\quad
10\text{ states of size }4,
\quad
16\text{ states of size }2.
}
\]

The unique size-eight state is `(bot,bot,bot)`.

Exact dependency-free Wolfram enumeration verifies this abstract table.

### Trust boundary for the cube model

The finite table is exact. Its direct use for the physical family is conditional on constructing the coherent path-component trivialisation.

Failure of such a trivialisation is itself potentially meaningful: it defines an `S_2` path-component transport holonomy over the lifted reconfiguration groupoid. This may become another route to orbit growth or decomposition, but no theorem is claimed yet.

## 9. Why edgewise enumeration is not the mechanism

Even in the conditional cube model, arbitrary collections of the `27` edge types produce many covers of the choice cube. Enumerating them without path connectivity gives a large case list and no decreasing graph parameter.

The missing information is global:

- each switched object is one connected terminal path;
- the two terminal paths of one relative even subgraph are disjoint;
- later challenge systems are transported through previous switches;
- all path triples arise in one finite reconfiguration groupoid;
- their overlaps are constrained at cubic vertices.

Therefore the next theorem must use the **path-component groupoid and overlap geometry**, not just the finite edge alphabet.

## 10. Updated Type H mechanism

The genuine Type H branch is now:

\[
\boxed{
\begin{array}{c}
\text{physical lifted-loop family }\Lambda
\\ \downarrow\\
\lambda\mapsto
(d_\lambda,U_\lambda,X_\lambda)
\\ \downarrow\\
\begin{cases}
\exists\lambda\text{ with no obstruction}
&\Rightarrow\text{Tait resolution and profile escape};\\
\forall\lambda\text{ obstructed}
&\Rightarrow\text{common-witness theorem required}.
\end{cases}
\end{array}
}
\]

The sought common witness should be one of:

- a translation submodule shared by the nonzero norm defects;
- a connected edge strip meeting every full-rank uncovered set;
- a vertex region missed by every relevant middle path;
- nontrivial path-component transport holonomy;
- a serial or dot-product factor bounded by a smaller separator.

## 11. Trust boundary

The following are theorem-level:

- the three-path switch-flow formula for each physical lift;
- the rank-one path identity;
- removal of closed odd components from each genuine rank-one loop;
- the spanning-path dichotomy;
- the full-rank XOR path-cover criterion;
- the unconditional physical obstruction signature.

The `27`-state cardinality table is an exact computation for the conditional fixed-cube model.

The following remain open:

- coherently trivialising path-component choices over the whole lifted groupoid;
- or exploiting the obstruction to such a trivialisation;
- proving that all obstructed physical lifts have a common path strip, missed region, translation, or smaller separator;
- translating the common witness into an explicit dot-product or bounded-fragment replacement;
- eliminating the complete cyclic four-cut obstruction.

## 12. Next exact tasks

1. Build the path-component transport groupoid rather than assuming a fixed cube.
2. Determine its `S_2` holonomy and its interaction with the existing `S_5` support holonomy.
3. Attach the exact signature `(d_lambda,U_lambda,X_lambda)` to every groupoid loop.
4. Prove a finite-family Helly/decomposition principle for these signatures using path connectivity.
5. Compare the resulting witness only with dot-product factorisation, cyclic-cut completion, Catlin reduction, and reconfiguration-contractible fragments.
