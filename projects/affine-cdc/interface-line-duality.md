# Interface line duality and the universal sewing space

**Date:** 2026-07-14  
**Status:** theorem-level structural draft for interfaces satisfying the cap-extension property; not yet Lean-formalized.

Let a connected graph be split along an edge interface

$$
S=\{e_i=a_ib_i:1\le i\le k\},
$$

with nonzero flow values

$$
h_i=f(e_i)\in\Gamma.
$$

Cap the two sides by boundary vertices $x_A$ and $x_B$, joining $x_A$ to every $a_i$ and $x_B$ to every $b_i$, with the cap edges carrying the same values $h_i$.

Assume the interface has the **cap-extension property**: every homogeneous or affine solution on the sewn graph restricts uniquely to compatible capped solutions on both sides. This property was established for the AffineCDC 2-edge and 3-edge interfaces.

Define the common boundary line space

$$
\boxed{
L_S:=\bigcap_{i=1}^k\langle h_i\rangle\le\Gamma.
}
$$

Because every $\langle h_i\rangle$ is a one-dimensional binary subspace, $L_S$ is either zero or a line.

## 1. Matching condition for capped gauges

Let $k_A$ and $k_B$ be homogeneous capped gauge solutions. Write

$$
u=k_A(x_A),
\qquad
v=k_B(x_B).
$$

After deleting the cap vertices and sewing corresponding boundary edges, the two gauges match globally exactly when

$$
u+v\in\langle h_i\rangle
\qquad
\text{for every }i.
$$

Therefore the sewing condition is

$$
\boxed{
u+v\in L_S.}
$$

Equivalently, the obstruction is the quotient class

$$
[u+v]\in\Gamma/L_S.
$$

## 2. Universal kernel exact sequence

Define

$$
q_S:
K_A\oplus K_B\to\Gamma/L_S,
\qquad
q_S(k_A,k_B)=[k_A(x_A)+k_B(x_B)],
$$

where $K_A,K_B$ are the homogeneous capped solution spaces.

The map is surjective: global constant gauges on either side allow the cap value to be shifted by an arbitrary element of $\Gamma$.

The kernel is exactly the homogeneous solution space $K_G$ of the sewn graph.

Hence

$$
\boxed{
0\longrightarrow
K_G
\longrightarrow
K_A\oplus K_B
\xrightarrow{q_S}
\Gamma/L_S
\longrightarrow0.
}
$$

For connected graphs, constants give a copy of $\Gamma$ inside each $K$, and the reduced moduli code is

$$
\mathcal B=K/\Gamma.
$$

Taking dimensions yields

$$
\boxed{
b_G=b_A+b_B+\dim L_S.
}
$$

Thus every interface contributes precisely the dimension of the common boundary-line intersection.

## 3. The theta-interface moduli space

Let $\Theta_S$ be the graph with two vertices joined by the $k$ interface edges, labelled by $h_i$.

A normalized homogeneous gauge on $\Theta_S$ is determined by the potential difference

$$
d\in\Gamma
$$

between its two vertices.

For the $i$-th edge, one must have

$$
d=\lambda_i h_i
$$

for some bit $\lambda_i$.

Therefore a nonzero interface gauge exists exactly when

$$
d\in\bigcap_i\langle h_i\rangle=L_S.
$$

The map $d\mapsto(\lambda_i)_i$ is injective, and every element of $L_S$ produces such a gauge word. Hence

$$
\boxed{
\mathcal B_{\Theta_S,h}\cong L_S.
}
$$

Combining this with the kernel sequence gives

$$
\boxed{
0\longrightarrow
\mathcal B_{\Theta_S,h}
\longrightarrow
\mathcal B_G
\longrightarrow
\mathcal B_A\oplus\mathcal B_B
\longrightarrow0.
}
$$

This identifies the pure sewing modes with the gauge modes of the labelled theta interface.

## 4. Local duality

The interface therefore carries a canonical short exact sequence

$$
\boxed{
0\longrightarrow
\mathcal B_{\Theta_S,h}
\cong L_S
\longrightarrow
\Gamma
\longrightarrow
\Gamma/L_S
\longrightarrow0.
}
$$

The two ends have complementary meanings:

- $L_S$ is the space of legal changes in the sewing;
- $\Gamma/L_S$ is the space of matching obstructions.

This is the elementary local duality behind the cut-gluing formulas.

## 5. Two-edge cut

For a 2-edge cut, flow conservation gives

$$
h_1=h_2=h.
$$

Therefore

$$
L_S=\langle h\rangle,
\qquad
\dim L_S=1.
$$

Hence

$$
\boxed{
b_G=b_A+b_B+1.}
$$

The unique nonzero vector of $L_S$ is the simultaneous switch of both cut edges.

## 6. Three-edge cut

For a nowhere-zero 3-edge interface,

$$
h_1+h_2+h_3=0.
$$

The three values are distinct. Therefore their one-dimensional spans have trivial common intersection:

$$
L_S=0.
$$

Hence

$$
\boxed{
b_G=b_A+b_B.}
$$

There is no pure sewing mode, and the matching obstruction space is the whole coefficient space $\Gamma$.

## 7. General interface consequence

Since binary lines intersect nontrivially only when they are equal,

$$
\boxed{
L_S\ne0
\iff
h_1=h_2=\cdots=h_k.
}
$$

Therefore an interface contributes a pure sewing bit exactly when all its edge labels are equal.

If at least two boundary labels are distinct, then

$$
L_S=0
$$

and the interface itself is gauge-rigid.

This statement is independent of the number of interface edges; the cut size matters only through the flow equations that constrain which label patterns are possible.

## 8. Affine solution fibers

The same argument applies to affine solution torsors.

For any compatible pair of capped affine solutions, the possible sewings form a torsor under $L_S$.

Therefore every compatible pair has exactly

$$
|L_S|=2^{\dim L_S}
$$

sewings.

In particular:

- a 2-edge interface has two sewings;
- a 3-edge interface has one sewing.

This recovers the polynomial factors

$$
\Pi_G=2^{\dim L_S}\Pi_A\Pi_B
$$

for the 2-edge and 3-edge interfaces.

## 9. Relation to the sheaf interface

In the quotient-sheaf description, the matching map lands in the local interface obstruction space

$$
\Gamma/L_S.
$$

In the theta-graph description, the interface moduli are

$$
L_S.
$$

Thus the sheaf and theta pictures are the quotient and kernel halves of the same exact sequence

$$
0\to L_S\to\Gamma\to\Gamma/L_S\to0.
$$

This explains why the earlier sheaf Mayer--Vietoris sequence and the later theta-interface sewing code carry apparently different interface spaces: they are complementary pieces of one local coefficient sequence.

## 10. Scope

The algebraic sewing theorem above requires the cap-extension property in order to identify global solutions with capped solution pairs.

For the AffineCDC rank-three theory:

- the 2-edge case follows from single-edge constraint redundancy;
- the 3-edge case follows from the local Fano boundary-extension lemma.

For larger interfaces, the line-duality statement still describes matching of already-capped gauges, while global-to-capped extension may require additional hypotheses or new local exactness results.
