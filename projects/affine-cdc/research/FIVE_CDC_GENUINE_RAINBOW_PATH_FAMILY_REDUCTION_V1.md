# Genuine rainbow path families and the final zero-norm reduction

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level reduction of genuine three-switch loops; finite edge-membership signature verified exactly; composition/decomposition consequence remains open  
**Parents:** `FIVE_CDC_RAINBOW_SWITCH_FLOW_TAIT_RESOLUTION_V1.md`, `FIVE_CDC_TYPE_H_TAIT_ESCAPE_V1.md`, `FIVE_CDC_TYPE_H_LOCAL_TO_GLOBAL_HOLONOMY_STACK_V1.md`

## 1. Purpose

The preceding local-to-global packet allowed the rank-one switch-flow support to contain a terminal path together with closed components.  That is correct for an arbitrary rank-one quotient flow, but it is too broad for a genuine rainbow loop.

A genuine rainbow loop is the composite of three switches on three individual terminal-path components.  Let these paths be

\[
P_0,\qquad P_1,\qquad P_2,
\]

in routing-colour order.  The first and third switches have the same support coefficient `u`; the middle switch has coefficient `v`.  Therefore

\[
\boxed{
 t_\gamma
 =
 (P_0\triangle P_2)\otimes u
 +
 P_1\otimes v.
}
\]

This path formula sharpens all zero-norm lifting obstructions.

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
6. the family of all path-component choices admits a finite edge-membership obstruction signature on the cube `F_2^3`, but edgewise enumeration alone does not yield decomposition: the connectivity of the six terminal paths must be used.

No five-cycle double cover theorem is claimed.

## 2. The genuine three-path formula

Let `x` be the initial indexed root cover and `x^gamma` the cover after the three physical path switches, before support names are quotiented.  For the canonical rainbow word the switch coefficients are

\[
w_0=u,\qquad w_1=v,\qquad w_2=u,
\]

with `u,v` independent in the switch plane

\[
W=\langle u,v\rangle\cong F_2^2.
\]

Since switching a path component adds its incidence chain tensored with the support-pair coefficient,

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

This is the only edgewise information needed below.

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

it follows that every edge value of `t_gamma` is either `0` or `kappa`.

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

In the basis `u,v`, the values `0,kappa` are exactly the vectors whose two coordinates are equal.  The `u`-coordinate of `t_gamma` is `1_{P_0 triangle P_2}`, while the `v`-coordinate is `1_{P_1}`.  Equality of the two coordinates on every edge gives the identity. ∎

### Corollary 3.2 — no genuine odd-component branch

The nonzero support of a rank-one genuine loop is the single path component `P_1`.  It contains no closed component.

Thus the odd closed components allowed by an arbitrary rank-one quotient flow are absent from the genuine rainbow family.

## 4. Spanning-path dichotomy

The middle switch `P_1` is a terminal path component of a relative even subgraph.  At an internal vertex it has degree either zero or two.

### Proposition 4.1 — nonspanning means empty vertex relation

If `P_1` omits an internal vertex `w`, then all three edges incident with `w` have switch-flow value zero.  Hence the root-fibre vertex relation at `w` is empty for types `2^2 1` and `3 2`.

#### Proof

By Theorem 3.1, `t_gamma` is nonzero precisely on `P_1`.  A vertex outside the path has no incident path edge.  Apply the previously proved all-zero-vertex obstruction. ∎

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

If `P_1` is spanning, it contains every internal vertex exactly once.  Its complement is a perfect matching of the internal vertices together with the two zero-valued terminal semiedges.  The matching-complement degree-two system has only the one terminal path `P_1`, with `n` internal vertices.  By Lemma 4.2, `n` is even.  The exact even-component lifting theorem therefore supplies a root lift. ∎

### Corollary 4.4 — rank-one Tait escape

Inside a minimal Type H kernel, every zero-norm rank-one lifted loop must have a nonspanning middle path.  A spanning middle path would give a Tait resolution and hence strict boundary-profile escape.

Thus the genuine rank-one residual mechanism is not oddness.  It is:

\[
\boxed{
\text{every relevant middle Kempe path misses an internal vertex}.
}
\]

This is a path-coverage obstruction suitable for decomposition arguments.

## 5. Full-rank monodromy is an XOR path-cover problem

Let `pi` have type `4 1` or `5`.  The exact root-fibre theorem says that a zero-norm root lift exists if and only if `t_gamma` has no zero edge.

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
   E(P)=P_1\cup(P_0\triangle P_2).
   }
   \]
4. the loop has a Tait resolution.

#### Proof

The equivalence of root linearization, no zero edge, and Tait resolution is the full-rank part of the preceding switch-flow theorem.  The equivalence with the displayed path cover follows directly from the edgewise formula. ∎

### Corollary 5.2 — full-rank residual certificate

Inside a minimal Type H kernel, every zero-norm full-rank lift has an edge

\[
e\notin P_1\cup(P_0\triangle P_2).
\]

Thus the residual obstruction is a concrete uncovered edge of a two-chain path cover.

## 6. The complete genuine zero-norm ladder

The previous local-to-global stack now sharpens to:

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

The component-holonomy oddness branch was an artefact of allowing an arbitrary rank-one switch flow.  It is removed from the genuine three-path family.

## 7. Finite path-choice signature

For each of the three challenge subgraphs, let

\[
P_j^0,\ P_j^1
\]

be its two terminal path components.  A physical path choice is

\[
\epsilon=(\epsilon_0,\epsilon_1,\epsilon_2)\in F_2^3.
\]

Put

\[
A_\epsilon=P_0^{\epsilon_0}\triangle P_2^{\epsilon_2},
\qquad
B_\epsilon=P_1^{\epsilon_1}.
\]

For an edge `e`, record

\[
\sigma(e)=(s_0,s_1,s_2)\in\{\bot,0,1\}^3,
\]

where `s_j=i` means `e in P_j^i`, and `s_j=bot` means `e` lies in neither terminal path of system `j`.  The two paths in one system are edge-disjoint, so these are the only possibilities.

Define the zero-choice set

\[
\mathcal Z_e
=
\left\{
\epsilon\in F_2^3:
 e\notin A_\epsilon\cup B_\epsilon
\right\}.
\]

Equivalently,

\[
\epsilon\in\mathcal Z_e
\]

when

\[
[\,s_0=\epsilon_0\,]
=
[\,s_2=\epsilon_2\,]
\]

and

\[
s_1\ne\epsilon_1,
\]

where `bot` is unequal to both binary choices.

### Computational Theorem 7.1 — exact local family alphabet

Among the `27` edge-membership states `sigma in {bot,0,1}^3`, the cardinalities of `Z_e` are distributed as

\[
\boxed{
1\text{ state of size }8,
\quad
10\text{ states of size }4,
\quad
16\text{ states of size }2.
}
\]

The unique size-eight state is

\[
(\bot,\bot,\bot),
\]

an edge lying in none of the six terminal paths.

Exact dependency-free Wolfram enumeration verifies the table.

### Theorem 7.2 — full-rank family obstruction signature

Let `Lambda_fr` be the set of physical path choices whose lifted loop has full-rank support type and zero ambient norm.  Then every such lift is obstructed by a zero edge if and only if

\[
\boxed{
\Lambda_{\mathrm{fr}}
\subseteq
\bigcup_{e\in E(P)}\mathcal Z_e.
}
\]

#### Proof

For a choice `epsilon`, Theorem 5.1 fails exactly when some edge lies outside `A_epsilon union B_epsilon`, which is exactly `epsilon in Z_e`. ∎

This is the desired finite **family obstruction signature**.  It is not yet a decomposition theorem.

## 8. Why edgewise enumeration is not the mechanism

The local alphabet is finite, but arbitrary collections of the `27` edge types produce many distinct covers of the choice cube.  Enumerating those covers without the path constraints gives a large case list and no decreasing graph parameter.

The missing information is global:

- each colour `P_j^i` is one connected terminal path;
- the two paths of one challenge system are disjoint;
- their terminal pairings are prescribed by the routing policy;
- all six paths arise from three fixed relative even subgraphs;
- their overlaps are constrained at cubic vertices.

Therefore the next theorem must use **path connectivity**, not just the finite edge alphabet.

The target is:

\[
\boxed{
\begin{array}{c}
\text{all relevant path choices obstructed}
\\ \Downarrow\\
\text{common uncovered strip, common missed vertex region,}
\\
\text{or serial/dot-product separation}.
\end{array}
}
\]

## 9. Updated Type H mechanism

The genuine Type H branch is now:

\[
\boxed{
\begin{array}{c}
\text{lifted rainbow family}
\\ \downarrow\\
\text{ambient norm }N_\pi z
\\ \downarrow\\
\begin{cases}
N_\pi z\ne0
&\Rightarrow\text{pure interior translation};\\
N_\pi z=0
&\Rightarrow\text{three-path quotient flow}.
\end{cases}
\\ \downarrow\\
\begin{cases}
\text{full rank: }E=P_1\cup(P_0\triangle P_2),\\
\text{rank one: }P_1=P_0\triangle P_2\text{ and }P_1\text{ spanning}.
\end{cases}
\\ \downarrow\\
\begin{cases}
\text{success}&\Rightarrow\text{Tait resolution and profile escape};\\
\text{failure}&\Rightarrow\text{uncovered edge or missed-vertex path certificate}.
\end{cases}
\end{array}
}
\]

The root-fibre holonomy layer has therefore collapsed, for genuine loops, to terminal-path coverage.

## 10. Trust boundary

The following are theorem-level:

- the three-path switch-flow formula;
- the rank-one path identity;
- removal of closed odd components from genuine rank-one loops;
- the spanning-path dichotomy;
- the full-rank XOR path-cover criterion;
- the family obstruction-set formulation.

The `27`-state cardinality table is exact finite computation.

The following remain open:

- proving that all obstructed choices force a common path strip or smaller separator;
- integrating nonzero norm translations with the same path family;
- translating the path certificates into an explicit dot-product or bounded-fragment replacement;
- proving the analogous composition theorem for the Type T path automaton;
- eliminating the complete cyclic four-cut obstruction.

## 11. Next exact tasks

1. Construct the overlap graph of the six terminal paths `P_j^i`.
2. Prove that a cube-cover by the sets `Z_e`, subject to path connectivity, has a connected witness region meeting the boundary in at most four points.
3. Test whether the witness region is exactly a dot-product factor, serial four-pole, or reconfiguration-contractible fragment.
4. Add nonzero norm data as cycle labels on the same overlap graph.
5. Compare the resulting composition law only with the relevant snark factorisation and cycle-cut literature; do not expand to the full Berge--Fulkerson programme.
