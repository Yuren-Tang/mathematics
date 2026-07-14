# Gauge modes as harmonic cut quotients

**Date:** 2026-07-14  
**Status:** theorem-level draft; not yet Lean-formalized.

Let $G$ be a finite connected graph and let

$$
f:E(G)\to\Gamma
$$

be a nowhere-zero flow over a binary vector space $\Gamma$.

Recall that the homogeneous gauge-moduli code consists of the edge words
$\lambda\in\mathbf F_2^E$ for which there is a potential

$$
k:V(G)\to\Gamma
$$

satisfying

$$
k_u+k_v=\lambda_e f(e)
\qquad(e=uv).
$$

Write this code as $\mathcal B_f$.

## 1. Supports are edge cuts

Take a nonzero $\lambda\in\mathcal B_f$ and put

$$
S:=\operatorname{supp}\lambda.
$$

If $e=uv\notin S$, then

$$
k_u=k_v.
$$

Hence $k$ is constant on every connected component of $G-S$.

Because $\lambda\ne0$, some edge of $S$ has endpoints with different
potentials. Therefore $G-S$ is disconnected.

Thus

$$
\boxed{
\operatorname{supp}\lambda
\text{ is an edge cut for every nonzero }
\lambda\in\mathcal B_f.
}
$$

This gives the immediate bound

$$
d(\mathcal B_f)\ge \lambda'(G),
$$

where $d$ is the minimum nonzero codeword weight and $\lambda'(G)$ is the edge
connectivity.

## 2. The contracted quotient

Let $Q_S$ be the connected multigraph obtained by contracting every connected
component of $G-S$ to one vertex.

For a component $X$, let $p_X$ be the common value of $k$ on $X$. Then every
edge $e$ of $Q_S$ joining components $X$ and $Y$ satisfies

$$
\boxed{
f(e)=p_X+p_Y.
}
$$

Thus $f|_S$ is an exact $\Gamma$-valued tension on $Q_S$.

It is also a flow. Indeed, sum the original flow equations over all vertices of
a component $X$. Every internal edge appears twice and cancels, leaving

$$
\sum_{e\in\partial X}f(e)=0.
$$

These are exactly the flow equations at the quotient vertex $X$.

Therefore

$$
\boxed{
f|_S
\in
\operatorname{Flow}(Q_S;\Gamma)
\cap
\operatorname{Tension}(Q_S;\Gamma).
}
$$

Moreover it is nowhere zero.

## 3. Bicycle characterization

Conversely, suppose a partition of $V(G)$ into connected parts gives a
connected quotient multigraph $Q$, and suppose there is a vertex labelling

$$
p:V(Q)\to\Gamma
$$

such that every edge $e=XY$ of the quotient satisfies

$$
f(e)=p_X+p_Y\ne0.
$$

Let $S$ be the set of edges crossing the partition and define $k$ on each part
to be its label $p_X$. Then

$$
k_u+k_v=
\begin{cases}
0,&e\notin S,\\
f(e),&e\in S.
\end{cases}
$$

Hence the indicator word $\mathbf 1_S$ belongs to $\mathcal B_f$.

We obtain the exact characterization:

$$
\boxed{
\lambda\in\mathcal B_f\setminus\{0\}
\iff
Q_{\operatorname{supp}\lambda}
\text{ carries }f|_S
\text{ as a nowhere-zero flow-tension bicycle}.
}
$$

These quotients may be called **harmonic cut quotients**.

## 4. Harmonic vertex labellings

Choose a basis of $\Gamma$. Each coordinate of $p$ is a binary vertex
function, and its edge coboundary is simultaneously a binary flow.

Thus every coordinate is harmonic for the mod-$2$ graph Laplacian:

$$
L_{Q_S}p_i=0.
$$

Equivalently, the coordinate flow space of $f|_S$ lies in the binary bicycle
space

$$
\mathcal C(Q_S)\cap\mathcal C(Q_S)^\perp.
$$

If $r_S$ is the dimension of the span of the labels $f(S)$, then

$$
\boxed{
r_S
\le
\dim\bigl(
\mathcal C(Q_S)\cap\mathcal C(Q_S)^\perp
\bigr).
}
$$

For a connected quotient, the right-hand side is the nullity of its binary
Laplacian minus one.

This converts the classification of gauge modes into a classification of
small connected multigraphs with sufficiently large binary bicycle space and a
compatible nowhere-zero harmonic colouring.

## 5. Boundary degree restriction

No quotient vertex can have degree one.

Indeed, at such a vertex the flow equation would consist of one nonzero edge
label and could not vanish.

Therefore every harmonic cut quotient has minimum degree at least two.

This already sharply constrains low-weight codewords.

## 6. Weight one and two

A weight-one codeword would give a connected quotient with one edge and a
degree-one vertex, so it is impossible.

For weight two, connectedness and minimum degree at least two force the
quotient to consist of two vertices joined by two parallel edges.

Since both edges have the same endpoint-potential difference, their flow
values are equal.

Hence

$$
\boxed{
\operatorname{wt}(\lambda)=2
\iff
\operatorname{supp}\lambda
\text{ is a 2-edge cut whose two edges have equal flow value}.
}
$$

This is precisely the extra sewing bit in the exact two-edge-cut
factorization.

## 7. Weight three is impossible

Suppose a weight-three codeword existed.

Its quotient has three edges, is connected, and has minimum degree at least
two. There are only two possibilities.

### Two quotient vertices

The quotient consists of three parallel edges. All three are tensions with the
same endpoint difference $h\ne0$. The flow equation is

$$
h+h+h=h\ne0,
$$

a contradiction.

### Three quotient vertices

The quotient is a triangle. At each degree-two vertex the two incident
nowhere-zero flow values must be equal. Hence all three edge values are equal
to some $h\ne0$.

But a tension around the triangle must sum to zero, whereas

$$
h+h+h=h\ne0.
$$

Again this is impossible.

Therefore

$$
\boxed{
\mathcal B_f
\text{ has no codeword of weight }3.
}
$$

This explains structurally why a three-edge cut contributes no independent
sewing modulus, in contrast with a two-edge cut.

## 8. Consequences for cyclic cores

For a cyclically $4$-edge-connected cubic core, every nonzero gauge mode has
weight at least four.

More generally, the gauge-rigidity problem may be restated as:

> Does the flow-labelled graph admit a nontrivial connected cut quotient on
> which the induced labels form a nowhere-zero harmonic bicycle?

This is a graph-theoretic reformulation of the tensor independence condition

$$
\ker T_f=0.
$$

The tensor, sheaf and cut-quotient descriptions are therefore three forms of
the same rigidity problem.
