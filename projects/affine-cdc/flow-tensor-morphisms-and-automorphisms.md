# Morphisms and automorphisms of flow tensor data

**Date:** 2026-07-14  
**Status:** theorem-level foundational draft; not yet Lean-formalized.

Let $E$ be finite and write $U_E=\mathbf F_2^E$ with basis $(e)_{e\in E}$.

## 1. The diagonal coalgebra

Define

$$
\Delta_E(e)=e\otimes e,
\qquad
\varepsilon_E(e)=1.
$$

### Proposition

A linear map

$$
\phi:U_E\to U_{E'}
$$

satisfies

$$
\Delta_{E'}\phi=(\phi\otimes\phi)\Delta_E
$$

iff every basis vector is sent either to $0$ or to a single basis vector.

If also

$$
\varepsilon_{E'}\phi=\varepsilon_E,
$$

then every basis vector is sent to a basis vector. Hence counital coalgebra maps are exactly set maps $s:E\to E'$.

### Proof

Write

$$
\phi(e)=\sum_j a_jj.
$$

Then

$$
\Delta\phi(e)=\sum_j a_j(j\otimes j),
$$

whereas

$$
(\phi\otimes\phi)\Delta(e)=\sum_{j,k}a_ja_k(j\otimes k).
$$

All off-diagonal coefficients vanish, so at most one $a_j$ is nonzero. Counitality forces that coefficient to be $1$.

Thus the distinguished edge basis is equivalently a diagonal coalgebra structure; it is not arbitrary coordinate clutter.

## 2. Strict morphisms

A based quotient datum is

$$
\mathfrak D=\left(U_E\xrightarrow{\pi}Q\xrightarrow{F}\Gamma\right),
$$

with $\pi,F$ surjective.

A strict morphism

$$
(\phi,\alpha,\beta):\mathfrak D\to\mathfrak D'
$$

consists of a counital diagonal-coalgebra map $\phi$ and linear maps $\alpha,\beta$ such that

$$
\alpha\pi=\pi'\phi,
\qquad
\beta F=F'\alpha.
$$

Since $\pi$ and $F$ are surjective, $\alpha$ and $\beta$ are uniquely determined by $\phi$ whenever they exist. Thus a strict morphism is fundamentally a set map on coordinates satisfying two descent conditions.

## 3. Functoriality

The tensor operators satisfy

$$
(\beta\otimes\alpha)T_{\pi,F}=T_{\pi',F'}\phi.
$$

The wedge maps satisfy

$$
(\Lambda^2\beta)W_F=W_{F'}(\beta\otimes\alpha).
$$

Hence every strict morphism induces a chain map of flow tensor complexes.

## 4. Code-flag formulation

Let

$$
D\subseteq C\subseteq\mathbf F_2^E
$$

and

$$
D'\subseteq C'\subseteq\mathbf F_2^{E'}
$$

be the dual code flags.

A set map $s:E\to E'$ induces pullback

$$
s^*:\mathbf F_2^{E'}\to\mathbf F_2^E,
\qquad
(s^*x)(e)=x(s(e)).
$$

The map descends through the outer quotient exactly when

$$
s^*(C')\subseteq C,
$$

and through the coefficient quotient exactly when

$$
s^*(D')\subseteq D.
$$

Therefore strict morphisms are equivalently set maps whose pullbacks preserve both levels of the code flag.

## 5. Automorphism group

An automorphism must induce a permutation $\sigma\in\operatorname{Sym}(E)$. The descent conditions become

$$
\sigma C=C,
\qquad
\sigma D=D.
$$

Therefore

$$
\boxed{\operatorname{Aut}(\mathfrak D)\cong\{\sigma\in\operatorname{Sym}(E):\sigma C=C,\ \sigma D=D\}.}
$$

No hidden linear automorphisms remain: the induced maps on $Q$ and $\Gamma$ are forced by the coordinate permutation. This passes the automorphism test for nested code flags as the strict objects.

## 6. Graphical realization

For a flow-labelled graph,

$$
C=\mathcal C(G),
\qquad
D=\mathcal F_f.
$$

Hence

$$
\operatorname{Aut}(\mathfrak T(G,f))=
\{\sigma\in\operatorname{Sym}(E):\sigma\mathcal C(G)=\mathcal C(G),\ \sigma\mathcal F_f=\mathcal F_f\}.
$$

Graph automorphisms preserving the flow up to coefficient automorphism form a subgroup. The full group may be larger because preserving the cycle code means preserving the represented cycle/cographic matroid, and such an automorphism need not arise from a vertex automorphism of one graph realization.

Thus the graph is a realization of the strict object rather than something recoverable uniquely from it.

## 7. What the bare object forgets

The code flag remembers tensor homology, Schur multiplication, the constraint matroid, balanced torsion, and coefficient morphisms. It need not remember vertices, a specific quotient graph after deleting a support, embedding or surface data, or the AffineCDC affine class. These belong to graphical or affine enhancements.

## 8. Partial maps

Dropping counitality permits basis vectors to map to $0$. Such coalgebra maps correspond to partial functions $E\rightharpoonup E'$. They are candidates for deletion-like operations, but graph deletion and contraction alter cycle spaces in different variance and generally require spans or correspondences.

## 9. Minimal object

The free coordinate space $U_E$ may be replaced, but only by equivalent data: a finite set $E$, its diagonal coalgebra, or a distinguished spanning family $(q_e)_{e\in E}$ in $Q$.

A minimal strict object can therefore be written as either

$$
(E,\ Q\xrightarrow{F}\Gamma,\ (q_e)_{e\in E})
$$

or equivalently

$$
D\subseteq C\subseteq\mathbf F_2^E.
$$

The code-flag language makes symmetries transparent; the quotient language makes the tensor construction transparent.

## 10. Next categorical questions

1. Should the first strict category use all set maps, only injections, or only bijections?
2. Which partial maps model deletion?
3. Which spans model contraction and cut gluing?
4. Can affine and Hodge enhancements be organized as fibrations over the strict code-flag category?
5. Which invariants are functorial rather than merely isomorphism-invariant?
