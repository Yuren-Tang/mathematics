# Cut gluing as a pullback–pushout correspondence

**Date:** 2026-07-14  
**Status:** theorem-level structural draft for 2-edge and 3-edge cuts; not yet Lean-formalized.

Let a connected graph $G$ be separated by an edge cut

$$
S=\{e_i=a_ib_i:1\le i\le k\}
$$

into connected sides $A$ and $B$.

Cap each side by a new boundary vertex:

- in $A^+$, join the new vertex $x_A$ to every $a_i$;
- in $B^+$, join the new vertex $x_B$ to every $b_i$.

For $k=2$, the new boundary vertex has degree two and may later be suppressed to recover the usual single-cap-edge formulation. For $k=3$, the cap is cubic.

Let

$$
P_S
=
\left\{
x\in\mathbf F_2^S:
\sum_{i\in S}x_i=0
\right\}
$$

be the even boundary-pattern space.

## 1. Cycle spaces form a fiber product

Restriction of a cycle in a capped side to the cap edges gives an element of $P_S$.

Because the two sides are connected, every even boundary pattern extends to a cycle on each capped side. A global cycle of $G$ is exactly a pair of capped cycles with the same boundary pattern.

Therefore

$$
\boxed{
\mathcal C(G)
\cong
\mathcal C(A^+)
\times_{P_S}
\mathcal C(B^+).
}
$$

Equivalently, there is a short exact sequence

$$
\boxed{
0
\longrightarrow
\mathcal C(G)
\longrightarrow
\mathcal C(A^+)\oplus\mathcal C(B^+)
\xrightarrow{r_A+r_B}
P_S
\longrightarrow0.
}
$$

Here $r_A$ and $r_B$ are boundary-pattern restriction maps.

## 2. Cographic quotients form the dual pushout

Dualizing gives

$$
\boxed{
0
\longrightarrow
P_S^*
\xrightarrow{r_A^*\oplus r_B^*}
Q_{A^+}\oplus Q_{B^+}
\longrightarrow
Q_G
\longrightarrow0,
}
$$

where

$$
Q_X=\mathcal C(X)^*.
$$

Thus $Q_G$ is the pushout quotient

$$
\boxed{
Q_G
\cong
Q_{A^+}\oplus_{P_S^*}Q_{B^+}.
}
$$

If $f_A$ and $f_B$ are the capped flows and $f_G$ is the sewn flow, then

$$
F_G^*([q_A,q_B])
=
F_A^*(q_A)+F_B^*(q_B).
$$

This is well-defined because the diagonal image of $P_S^*$ is killed: both sides carry the same boundary flow labels, so their contributions cancel in characteristic two.

## 3. Why graph gluing is not an ordinary chain map

The edge-coordinate space behaves in the opposite variance.

A global cut edge becomes a pair of cap edges, one on each side. Hence global edge data are represented by an equal-boundary subspace of

$$
U_{A^+}\oplus U_{B^+},
\qquad
U_X=\mathbf F_2^{E(X)}.
$$

So:

- edge coordinates are assembled by a pullback/equalizer;
- cycle-dual quotients are assembled by a pushout/coequalizer.

The flow tensor operator

$$
T_f:U_E\to\Gamma\otimes Q_G
$$

therefore sits across a mixed-variance square.

This is why cut gluing does not naturally appear as a short exact sequence of the three-term tensor complexes in one direction. The correct object is a linear correspondence, or equivalently a bicartesian diagram of pointed quotient data.

## 4. The interface theta graph

Let $\Theta_S$ be the multigraph with two vertices joined by the $k$ interface edges, carrying the boundary flow labels

$$
h_i=f(e_i).
$$

Its cycle space is exactly

$$
\mathcal C(\Theta_S)=P_S.
$$

Thus the boundary datum

$$
P_S^*\to\Gamma
$$

appearing in the pushout is itself the flow quotient map of the labelled theta interface.

The interface is therefore not an auxiliary bookkeeping vector space: it is a small flow-labelled graph.

## 5. Sewing moduli are interface gauge modes

For the two minimal cases used in AffineCDC, restriction from a global gauge mode to the two capped sides gives a surjection

$$
\mathcal B_{f_G}
\longrightarrow
\mathcal B_{f_A}\oplus\mathcal B_{f_B}.
$$

Its kernel consists exactly of pure sewing changes supported on the interface. These are the gauge modes of the labelled theta graph:

$$
\boxed{
0
\longrightarrow
\mathcal B_{\Theta_S,h}
\longrightarrow
\mathcal B_{f_G}
\longrightarrow
\mathcal B_{f_A}\oplus\mathcal B_{f_B}
\longrightarrow0
}
$$

for $k=2,3$.

This recovers both previously derived cut laws from one interface principle.

## 6. The 2-edge interface

For $k=2$, flow conservation gives

$$
h_1=h_2=h\ne0.
$$

The theta graph consists of two parallel edges with equal labels. Its unique nonzero gauge word is

$$
(1,1).
$$

Hence

$$
\dim\mathcal B_{\Theta_2,h}=1
$$

and

$$
\boxed{
b_G=b_A+b_B+1.
}
$$

The nonzero interface mode is exactly the sewing bit that switches both cut edges simultaneously.

Consequently the compatible-surface polynomial acquires the factor

$$
\boxed{
\Pi_G=2\Pi_A\Pi_B.
}
$$

## 7. The 3-edge interface

For $k=3$, the nonzero boundary values satisfy

$$
h_1+h_2+h_3=0.
$$

They are distinct and span a plane.

A gauge potential difference between the two vertices of $\Theta_3$ would have to be simultaneously one of

$$
0,\ h_1,\ h_2,\ h_3
$$

on all three edges. Since the three nonzero labels are distinct, only the zero difference is possible.

Therefore

$$
\mathcal B_{\Theta_3,h}=0
$$

and

$$
\boxed{
\mathcal B_{f_G}
\cong
\mathcal B_{f_A}\oplus\mathcal B_{f_B}.
}
$$

Thus

$$
\boxed{
b_G=b_A+b_B
}
$$

and

$$
\boxed{
\Pi_G=\Pi_A\Pi_B.
}
$$

The absence of a 3-edge sewing bit is exactly the rigidity of the labelled three-edge theta interface.

## 8. Torsion consequence

For spanning rank-three cubic flows, Fano torsion detects gauge rigidity.

The interface principle gives:

### Three-edge gluing

$$
\boxed{
\tau_G=\tau_A\tau_B.
}
$$

The global flow is rigid exactly when both capped flows are rigid.

### Two-edge gluing

The interface has a nonzero gauge mode, so

$$
\boxed{
\tau_G=0.
}
$$

Every genuine two-edge sum is non-rigid.

## 9. Relation to harmonic cut quotients

The interface theta graph is also the smallest harmonic cut quotient.

- $\Theta_2$ with equal labels gives the unique weight-two gauge circuit.
- $\Theta_3$ with three distinct plane labels has no gauge circuit.

Thus the cut-factorization theorem and the low-weight circuit classification are the same local statement viewed in opposite directions:

- decomposition cuts a graph into pieces through an interface;
- a gauge circuit contracts a graph onto a harmonic interface quotient.

## 10. The categorical lesson

Coefficient quotients act covariantly and produce ordinary chain maps and long exact sequences.

Graph cuts act by mixed variance:

$$
\boxed{
\text{edge pullback}
\quad+\quad
\text{cycle-space fiber product}
\quad+\quad
\text{cographic pushout}.
}
$$

Therefore the natural category of flow tensor data should not have only ordinary linear maps. It should allow spans or linear relations that preserve:

1. the distinguished edge basis;
2. the cographic quotient;
3. the coefficient map;
4. the tensor diagonal.

The 2-edge and 3-edge sewing theorems are the first Mayer--Vietoris laws in this correspondence category.
