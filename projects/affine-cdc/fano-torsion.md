# Fano torsion: a basis-free rigidity invariant

**Date:** 2026-07-14  
**Status:** theorem-level draft; not yet Lean-formalized.

Let $G$ be a finite connected cubic graph and let

$$
f:E(G)\to \Gamma=\mathbf F_2^3
$$

be a spanning nowhere-zero flow.

Write $\mathcal C(G)\le \mathbf F_2^E$ for the binary cycle space and set

$$
Q_G:=\mathbf F_2^E/\mathcal C(G)^\perp
\cong \mathcal C(G)^*.
$$

For an edge $e$, let $\bar e\in Q_G$ be the class of its coordinate vector.
The flow induces a surjection

$$
F^*:Q_G\to\Gamma,
\qquad
F^*(\bar e)=f(e).
$$

Define

$$
W_f:\Gamma\otimes Q_G\to\Lambda^2\Gamma,
\qquad
W_f(a\otimes q)=a\wedge F^*(q).
$$

For every edge,

$$
t_e:=f(e)\otimes\bar e
$$

lies in $\ker W_f$, since

$$
W_f(t_e)=f(e)\wedge f(e)=0.
$$

## 1. Dimension balance

If $n=|V(G)|$ and $m=|E(G)|=3n/2$, then

$$
\dim Q_G=\dim\mathcal C(G)=\frac n2+1.
$$

Because $W_f$ is surjective,

$$
\dim\ker W_f
=
3\left(\frac n2+1\right)-3
=
\frac{3n}{2}
=
m.
$$

Thus the $m$ edge tensors $t_e$ live in an $m$-dimensional space.

## 2. The canonical top wedge

Define

$$
\boxed{
\Theta_f
:=
\bigwedge_{e\in E(G)} t_e
\in
\det(\ker W_f)
=
\Lambda^m(\ker W_f).
}
$$

This is basis-free.

There is also no ordering ambiguity: over $\mathbf F_2$, changing the order of
the edges introduces no sign.

The determinant line is one-dimensional. Hence define the binary **Fano
torsion**

$$
\tau_f=
\begin{cases}
1,&\Theta_f\ne0,\\
0,&\Theta_f=0.
\end{cases}
$$

## 3. Rigidity criterion

Let

$$
T_f:\mathbf F_2^E\to\Gamma\otimes Q_G,
\qquad
T_f(\lambda)=\sum_e\lambda_e t_e.
$$

The homogeneous gauge-moduli code is

$$
\mathcal B_f=\ker T_f.
$$

Since $\operatorname{im}T_f\subseteq\ker W_f$ and both the domain and
$\ker W_f$ have dimension $m$,

$$
\boxed{
\Theta_f\ne0
\iff
T_f:\mathbf F_2^E\overset{\sim}{\longrightarrow}\ker W_f
\iff
\mathcal B_f=0.
}
$$

Therefore

$$
\boxed{
\tau_f=1
\iff
f\text{ is gauge-rigid}.
}
$$

Equivalently, $\tau_f=1$ iff the flow constraint matroid represented by the
columns $f(e)\otimes\bar e$ is free.

## 4. Relation to the basis-packing parity

Choose a cycle-space basis beginning with the three coordinate flows and write

$$
Q_G\cong\Gamma\oplus K.
$$

Under the induced identification

$$
\ker W_f
\cong
\operatorname{Sym}^2\Gamma
\oplus
(\Gamma\otimes K),
$$

the edge tensor becomes

$$
t_e
=
\bigl(f(e)\otimes f(e),\,f(e)\otimes k_e\bigr).
$$

Expanding $\Theta_f$ in this splitting yields the previously derived Fano
basis-packing count $N_f(K)$:

$$
\boxed{
\tau_f=N_f(K)\pmod2.
}
$$

Thus the adapted-basis formula is not the definition of the invariant. It is a
coordinate expansion of the canonical top wedge $\Theta_f$.

## 5. Naturality

The construction is invariant under:

- graph isomorphisms;
- relabelling of edges;
- linear automorphisms of $\Gamma$ carrying one flow to another.

Over $\mathbf F_2$, every invertible $3\times3$ matrix has determinant $1$, so
no orientation character appears.

## 6. Low-cut multiplicativity

Suppose a rank-three flow is assembled along a nontrivial 3-edge cut from
capped flows $f_A$ and $f_B$. The exact gluing theorem gives

$$
b_G=b_A+b_B,
$$

where $b=\dim\mathcal B$.

Consequently,

$$
\boxed{
\tau_G=\tau_A\tau_B.
}
$$

Thus a 3-edge sum is gauge-rigid exactly when both capped factors are
gauge-rigid.

For a 2-edge sum,

$$
b_G=b_A+b_B+1.
$$

Hence

$$
\boxed{
\tau_G=0.
}
$$

The extra sewing bit forces every genuine 2-edge sum to be non-rigid.

Therefore Fano torsion is multiplicative across 3-edge decomposition and
vanishes across 2-edge decomposition. The nontrivial classification is
concentrated in cyclically 4-edge-connected flow cores.

## 7. Interpretation

$\Theta_f$ is the determinant-line form of the rank-three tensor complex

$$
\mathbf F_2^E
\xrightarrow{T_f}
\Gamma\otimes Q_G
\xrightarrow{W_f}
\Lambda^2\Gamma.
$$

It is a characteristic-two analogue of torsion for this finite complex:

- nonzero torsion means exactness and rigidity;
- zero torsion means nontrivial degree-zero and middle homology;
- the Fano Hodge theorem identifies those two homology spaces dually.

This gives a basis-free replacement for the reduced determinant and for the
choice-dependent basis-packing formula.
