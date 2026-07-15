# Cut interfaces, pullback–pushout gluing, and sewing modes

**Status.** The cycle-space and cographic statements are theorem-level for every
connected cut decomposition. The solution-space formulas require the
**cap-extension property** defined below. That property is established in the
AffineCDC construction for two-edge and three-edge interfaces; it is not claimed
for arbitrary larger interfaces.

## 1. Capped sides and the boundary pattern space

Let a connected graph $G$ be separated by an edge cut

$$
S=\{e_i=a_ib_i:1\leq i\leq k\}
$$

into connected sides $A$ and $B$. Form capped graphs $A^+$ and $B^+$ by adding
boundary vertices $x_A,x_B$ and replacing each cut edge by cap edges
$x_Aa_i$ and $x_Bb_i$.

Let

$$
P_S
:=
\left\{
x\in\mathbf F_2^S:
\sum_{i\in S}x_i=0
\right\}
$$

be the even boundary-pattern space.

Restriction of a cycle in a capped side to its cap edges lies in $P_S$. Since
each side is connected, every even boundary pattern extends to a cycle on each
side.

## 2. Cycle spaces form a fiber product

A global cycle in $G$ is exactly a pair of capped cycles with the same boundary
pattern. Therefore

$$
\boxed{
\mathcal C(G)
\cong
\mathcal C(A^+)
\times_{P_S}
\mathcal C(B^+).
}
$$

Equivalently:

### Theorem 2.1

There is a short exact sequence

$$
\boxed{
0\longrightarrow
\mathcal C(G)
\longrightarrow
\mathcal C(A^+)\oplus\mathcal C(B^+)
\xrightarrow{r_A+r_B}
P_S
\longrightarrow0.
}
$$

Here $r_A,r_B$ are the boundary restriction maps.

## 3. Cographic quotients form the dual pushout

Dualizing gives

$$
\boxed{
0\longrightarrow
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
Q_X:=\mathcal C(X)^*.
$$

Thus

$$
\boxed{
Q_G
\cong
Q_{A^+}\oplus_{P_S^*}Q_{B^+}.
}
$$

If the capped flows carry the original boundary labels, their coefficient maps
assemble by

$$
F_G([q_A,q_B])=F_A(q_A)+F_B(q_B).
$$

The diagonal image of $P_S^*$ is killed because the two sides carry equal
boundary labels and their contributions cancel in characteristic two.

## 4. Mixed variance

The edge-coordinate space behaves in the opposite variance. One global cut
edge becomes two cap edges. Global edge data therefore form an equal-boundary
subspace of

$$
\mathbf F_2^{E(A^+)}\oplus\mathbf F_2^{E(B^+)}.
$$

Hence:

- edge coordinates are assembled by a pullback or equalizer;
- cycle spaces are assembled by a fiber product;
- cographic quotients are assembled by a pushout or coequalizer.

The tensor operator

$$
T_f:\mathbf F_2^E\longrightarrow\Gamma\otimes Q_G
$$

therefore crosses a mixed-variance square. Graph gluing is not naturally one
ordinary covariant chain map. Its canonical object is a linear correspondence
or bicartesian diagram of based quotient data.

## 5. The labelled theta interface

Let $h_i=f(e_i)$ be the nonzero boundary labels. Define $\Theta_S$ to be the
multigraph with two vertices joined by the $k$ interface edges labelled by the
$h_i$.

Its cycle space is

$$
\mathcal C(\Theta_S)=P_S.
$$

Thus the boundary map

$$
P_S^*\longrightarrow\Gamma
$$

appearing in the cographic pushout is itself the coefficient map of a small
flow-labelled graph. The interface is not an auxiliary bookkeeping space; it is
a canonical graphical object.

## 6. The common boundary-line space

Define

$$
\boxed{
L_S:=\bigcap_{i=1}^k\langle h_i\rangle\leq\Gamma.
}
$$

Since each $\langle h_i\rangle$ is a binary line, $L_S$ is either zero or a
line, and

$$
\boxed{
L_S\neq0
\iff
h_1=h_2=\cdots=h_k.
}
$$

A normalized gauge on the theta interface is determined by the potential
difference $d$ between its two vertices. The edge condition requires

$$
d\in\langle h_i\rangle
$$

for every $i$. Therefore:

### Theorem 6.1 — theta-interface gauge space

$$
\boxed{
\mathcal B_{\Theta_S,h}\cong L_S.
}
$$

The interface has a pure gauge mode exactly when all boundary labels are equal.

## 7. Cap matching and local kernel–quotient duality

Let $K_A,K_B$ be the homogeneous solution spaces on the capped sides. For
$k_A\in K_A$ and $k_B\in K_B$, write

$$
u:=k_A(x_A),
\qquad
v:=k_B(x_B).
$$

After deleting the cap vertices and sewing corresponding edges, the gauges
match exactly when

$$
u+v\in\langle h_i\rangle
$$

for every $i$, or equivalently

$$
\boxed{u+v\in L_S.}
$$

Thus the matching obstruction is

$$
[u+v]\in\Gamma/L_S.
$$

The interface carries the canonical coefficient sequence

$$
\boxed{
0\longrightarrow
L_S
\longrightarrow
\Gamma
\longrightarrow
\Gamma/L_S
\longrightarrow0.
}
$$

Its two ends have complementary meanings:

- $L_S$ is the space of legal changes of sewing;
- $\Gamma/L_S$ is the space of matching obstructions.

This explains why the theta-gauge and quotient-sheaf interface descriptions use
apparently different spaces: they are the kernel and quotient halves of one
local exact sequence.

## 8. The cap-extension property

An interface has the **cap-extension property** when homogeneous and affine
solutions on the sewn graph correspond exactly to compatible pairs of capped
solutions, with no additional interior obstruction introduced by capping.

Assume this property. Define

$$
q_S:K_A\oplus K_B\longrightarrow\Gamma/L_S,
\qquad
q_S(k_A,k_B)=[k_A(x_A)+k_B(x_B)].
$$

Global constants make $q_S$ surjective, and its kernel is the homogeneous
solution space $K_G$ of the sewn graph.

### Theorem 8.1 — universal matching sequence

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

For connected graphs, constants give a copy of $\Gamma$ inside each $K$. Put

$$
\mathcal B_X:=K_X/\Gamma,
\qquad
b_X:=\dim\mathcal B_X.
$$

Taking dimensions gives

$$
\boxed{
b_G=b_A+b_B+\dim L_S.
}
$$

More precisely, restriction to the capped sides gives

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

The kernel consists exactly of pure sewing changes.

## 9. Affine solution fibers

The same argument applies to affine solution torsors. For every compatible pair
of capped affine solutions, the possible sewings form a torsor under $L_S$.
Hence the number of sewings is

$$
\boxed{|L_S|=2^{\dim L_S}.}
$$

If $\Pi_X$ denotes a compatible-state polynomial or state sum in which each
affine sewing contributes once, then, provided the archived state-space
definition is restored and the cap-extension hypotheses hold,

$$
\Pi_G
=
2^{\dim L_S}\Pi_A\Pi_B.
$$

This conditional formula preserves the active algebraic consequence without
pretending that the absent topological definition has been reconstructed in the
current repository.

## 10. Two-edge interfaces

For a two-edge cut, flow conservation gives

$$
h_1=h_2=h\neq0.
$$

Therefore

$$
L_S=\langle h\rangle,
\qquad
\dim L_S=1.
$$

The theta interface consists of two equal-labelled parallel edges and has the
unique nonzero gauge word $(1,1)$. Hence

$$
\boxed{
b_G=b_A+b_B+1.}
$$

Every compatible pair of capped affine solutions has two sewings. In the
conditional state-sum notation,

$$
\Pi_G=2\Pi_A\Pi_B.
$$

For a balanced rank-three tensor complex, the extra gauge bit forces
non-rigidity:

$$
\boxed{\tau_G=0.}
$$

The same interface is the unique weight-two gauge circuit described by the
harmonic quotient theorem.

## 11. Three-edge interfaces

For a nowhere-zero three-edge interface,

$$
h_1+h_2+h_3=0.
$$

The three labels are distinct and span a plane, so

$$
L_S=0.
$$

Therefore

$$
\boxed{
\mathcal B_G
\cong
\mathcal B_A\oplus\mathcal B_B,
}
$$

and

$$
\boxed{b_G=b_A+b_B.}
$$

There is a unique affine sewing. In the conditional state-sum notation,

$$
\Pi_G=\Pi_A\Pi_B.
$$

For rank-three balanced tensor complexes,

$$
\boxed{
\tau_G=\tau_A\tau_B.
}
$$

The absence of a three-edge sewing bit is the same local fact as the absence of
a weight-three gauge circuit: three distinct plane labels admit no common
nonzero potential difference.

## 12. What is established for AffineCDC

The cap-extension property is established for the interfaces used in the
original AffineCDC decomposition theory:

- for two-edge cuts, by redundancy of the single-edge constraint after capping;
- for three-edge cuts, by the local Fano boundary-extension lemma.

For larger interfaces, the line space $L_S$ still describes how already-capped
gauges match. The assertion that every global solution extends to capped
solutions may require additional local exactness hypotheses. Therefore the
formula

$$
b_G=b_A+b_B+\dim L_S
$$

is unconditional only in contexts where cap extension has been proved.

## 13. Categorical interpretation

Coefficient quotients act covariantly and give ordinary chain maps. Graph cuts
instead combine

$$
\boxed{
\text{edge pullback}
\quad+
\text{cycle-space fiber product}
\quad+
\text{cographic pushout}.
}
$$

The two-edge and three-edge sewing theorems are the first Mayer–Vietoris-type
laws in this correspondence geometry. Developing deletion, contraction, and
larger interfaces in one stable category remains an open programme.