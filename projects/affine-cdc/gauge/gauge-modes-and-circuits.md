# Gauge modes, harmonic cut quotients, and circuits

**Status.** The equivalence, parity theorem, sharpness example, and classifications
through weight six are theorem-level graph arguments. The historical small-graph
census is supporting evidence and is not used in the proofs. These results have
not yet been Lean-formalized.

Let $G$ be a finite connected loopless multigraph and let

$$
f:E(G)\longrightarrow\Gamma
$$

be a nowhere-zero binary flow. The gauge-moduli code is

$$
\mathcal B_f
:=
\left\{
\lambda\in\mathbf F_2^E:
\exists k:V(G)\to\Gamma,
\ k_u+k_v=\lambda_ef(e)
\text{ for every }e=uv
\right\}.
$$

Equivalently,

$$
\mathcal B_f=\ker T_f
$$

for the tensor operator. This chapter gives its intrinsic graph-theoretic
meaning.

## 1. Supports are cuts

Let $0\neq\lambda\in\mathcal B_f$, choose a potential $k$, and put

$$
S:=\operatorname{supp}\lambda.
$$

If $e=uv\notin S$, then $k_u=k_v$. Hence $k$ is constant on each connected
component of $G-S$. Since some edge of $S$ has endpoints with different
potentials, $G-S$ is disconnected.

Therefore

$$
\boxed{
\operatorname{supp}\lambda
\text{ is an edge cut for every nonzero }\lambda\in\mathcal B_f.
}
$$

In particular,

$$
d(\mathcal B_f)\geq\lambda'(G),
$$

where $d$ is the minimum nonzero codeword weight and $\lambda'(G)$ is edge
connectivity.

## 2. The contracted quotient

Contract every connected component of $G-S$ to one vertex and call the resulting
connected loopless multigraph $Q_S$. If a component $X$ carries the constant
potential $p_X$, then for every quotient edge $e=XY$,

$$
f(e)=p_X+p_Y.
$$

Thus the restricted labels form an exact $\Gamma$-valued tension on $Q_S$.
They are also a flow: summing the original flow equations over all vertices of
one component cancels internal edges and leaves

$$
\sum_{e\in\partial X}f(e)=0.
$$

Hence

$$
\boxed{
f|_S
\in
\operatorname{Flow}(Q_S;\Gamma)
\cap
\operatorname{Tension}(Q_S;\Gamma),
}
$$

and it is nowhere zero.

Such a labelled quotient will be called a **harmonic cut quotient**, or a
nowhere-zero flow–tension bicycle.

## 3. Exact characterization

Conversely, suppose a partition of $V(G)$ into connected parts produces a
connected quotient $Q$, and suppose the quotient vertices have labels
$p_X\in\Gamma$ satisfying

$$
f(e)=p_X+p_Y\neq0
$$

for every crossing edge $e=XY$. Give every original vertex in part $X$ the
potential $p_X$. Then

$$
k_u+k_v=
\begin{cases}
0,&e\text{ lies inside a part},\\
f(e),&e\text{ crosses the partition}.
\end{cases}
$$

Thus the indicator of the crossing set belongs to $\mathcal B_f$.

### Theorem 3.1 — harmonic quotient theorem

For a nonempty edge set $S$,

$$
\boxed{
\mathbf1_S\in\mathcal B_f
\iff
Q_S\text{ carries }f|_S
\text{ as a nowhere-zero exact flow–tension bicycle}.
}
$$

The gauge code, tensor kernel, and harmonic cut quotients are three presentations
of the same homogeneous rigidity problem.

## 4. Harmonic coordinates and bicycle dimension

Choose coordinates on $\Gamma$. Each coordinate of the quotient potential is a
binary vertex function whose coboundary is also a binary flow. Hence it is
harmonic for the mod-$2$ graph Laplacian.

Equivalently, every coordinate edge word belongs to the binary bicycle space

$$
\mathsf{Bic}(Q_S)
:=
\mathcal C(Q_S)\cap\mathcal C(Q_S)^\perp.
$$

If $r_S$ is the dimension of the span of the labels on $S$, then

$$
\boxed{
r_S
\leq
\dim\mathsf{Bic}(Q_S).
}
$$

For a connected quotient, the right side is the nullity of its binary Laplacian
minus one. This turns gauge-mode classification into the study of connected
multigraphs with sufficiently large bicycle space and a compatible nowhere-zero
harmonic colouring.

No quotient vertex can have degree one, because the flow equation there would
consist of one nonzero label. Therefore every harmonic cut quotient has minimum
degree at least two.

## 5. Circuits

The tensor columns $f(e)\otimes\bar e$ represent the flow constraint matroid.
Its cycle code is $\mathcal B_f$. Hence the inclusion-minimal nonempty gauge
supports are exactly its circuits.

Under Theorem 3.1, a gauge circuit is exactly a support-minimal harmonic cut
quotient. Circuit elimination follows from the matroid structure and requires no
separate graph proof.

For a circuit quotient, no vertex can have degree two. If a quotient vertex had
incident edges $e_1,e_2$, flow conservation would force their labels to be equal.
The two-edge set would itself be an exact tension support, contradicting
minimality. Hence every circuit quotient satisfies

$$
\boxed{\delta(Q_S)\geq3.}
$$

## 6. Weights one through four

### Weight one

A one-edge connected loopless quotient has degree-one vertices, so no weight-one
gauge word exists.

### Weight two

A connected two-edge quotient with minimum degree at least two consists of two
vertices joined by two parallel edges. Exactness forces the two labels to equal
the same nonzero potential difference. Therefore

$$
\boxed{
\operatorname{wt}(\lambda)=2
\iff
\operatorname{supp}\lambda
\text{ is an equal-labelled two-edge cut}.
}
$$

### Weight three

A connected loopless three-edge quotient of minimum degree at least two is either
three parallel edges or a triangle. In the first case exactness forces all labels
to equal one nonzero vector $h$, but the flow sum is $3h=h\neq0$. In the second
case degree-two flow conservation again forces all labels to equal $h$, while an
exact tension around the triangle must sum to zero. Thus no weight-three word
exists.

### Weight four circuits

A weight-four circuit quotient has minimum degree at least three and total degree
eight, hence exactly two vertices. It is four parallel edges. Exactness forces all
four labels to equal the same nonzero potential difference. Conversely, the
all-edge word is minimal. Thus

$$
\boxed{
\text{weight-four gauge circuits}
=
\text{equal-labelled }4K_2\text{ quotients}.
}
$$

## 7. Third-order orthogonality of graph bicycles

For any finite loopless multigraph $Q$ and any

$$
x,y,z\in\mathsf{Bic}(Q),
$$

one has

$$
\sum_ex_e=0,
$$

$$
\sum_ex_ey_e=0,
$$

and

$$
\boxed{
\sum_ex_ey_ez_e=0.
}
$$

The first identity is even degree in a cycle. The second is cycle–cut
orthogonality. For the third, write

$$
x_{uv}=a_u+a_v,
\qquad
y_{uv}=b_u+b_v,
\qquad
z_{uv}=c_u+c_v,
$$

where $a,b,c$ are harmonic vertex functions. Let

$$
P:=\sum_v\deg(v)a_vb_vc_v.
$$

Expanding

$$
\sum_{uv}(a_u+a_v)(b_u+b_v)(c_u+c_v)
$$

gives two pure endpoint terms contributing $P$ and three pairs of mixed terms.
Harmonicity converts each mixed pair to another copy of $P$. The total is

$$
P+P+P+P=0.
$$

This is a cubic discrete integration-by-parts identity.

## 8. Evenness in rank at most three

Assume $\dim\Gamma\leq3$. Pad with zero coordinates and write a nowhere-zero
flow–tension bicycle label as $(x_e,y_e,z_e)$. The nonzero indicator is

$$
\mathbf1_{(x,y,z)\neq0}
=
x+y+z+xy+xz+yz+xyz.
$$

Every monomial sum on the right vanishes by first-, second-, or third-order
bicycle orthogonality. Therefore the number of edges is even.

### Theorem 8.1 — even gauge code

For every nowhere-zero binary flow with $\dim\Gamma\leq3$,

$$
\boxed{
\lambda\in\mathcal B_f
\Longrightarrow
\operatorname{wt}(\lambda)\equiv0\pmod2.
}
$$

Equivalently, every circuit of the flow constraint matroid has even cardinality.
In code language,

$$
\mathcal B_f
=(\mathcal C(G)*\mathcal F_f)^\perp
$$

and evenness is equivalent to

$$
\boxed{
\mathbf1_E\in\mathcal C(G)*\mathcal F_f.
}
$$

## 9. Sharpness in rank four

The rank bound is exact. Let $G=K_6$, let

$$
\Gamma=\mathbf F_2^4,
$$

and assign the six vertex potentials

$$
0,\quad e_1,\quad e_2,\quad e_3,\quad e_4,\quad
e_1+e_2+e_3+e_4.
$$

They are pairwise distinct and sum to zero. Label every edge $uv$ by

$$
g_{uv}=p_u+p_v.
$$

The labelling is a nowhere-zero exact tension. At each vertex,

$$
\sum_{u\neq v}g_{uv}
=
\sum_up_u
=0,
$$

so it is also a flow. Hence the all-one word belongs to the gauge code, but

$$
|E(K_6)|=15
$$

is odd. Therefore odd gauge words occur in rank four.

## 10. Classification of weight-six circuits

Let $\dim\Gamma\leq3$ and let $S$ support a gauge circuit of weight six. The
quotient $Q_S$ is connected, loopless, has six edges, and has minimum degree at
least three. Since its total degree is twelve, it has at most four vertices.

### Theorem 10.1

Up to graph isomorphism and a linear change of coordinates in $\Gamma$, exactly
three labelled quotient types occur:

1. $6K_2$: two vertices joined by six parallel edges, all labelled by one
   nonzero vector $h$;
2. $2K_3$: a triangle with every edge doubled, the three doubled pairs labelled
   $x$, $y$, and $x+y$;
3. $K_4$: four vertices with potentials $0,x,y,x+y$, so the three perfect
   matchings carry labels $x$, $y$, and $x+y$.

Conversely, the all-edge word is a gauge circuit in each type.

### Proof

If the quotient has two vertices, all six edges are parallel and exactness makes
their labels equal. Only the zero and all-edge gauge words are possible.

If it has three vertices, let the multiplicities between the three pairs be
$a,b,c$. A missing pair produces two even parallel bundles, one of which is a
proper gauge support. Hence all pairs occur. Translate one potential to zero and
write the other two as independent vectors $x,y$. The labels are $x,y,x+y$.
The three flow equations force $a,b,c$ to be positive and even; since they sum
to six, all equal two. Direct potential checking shows minimality.

If the quotient has four vertices, minimum degree three and total degree twelve
make it cubic. Parallel edges would force a zero third label or disconnect the
remaining vertices, so the graph is simple and hence $K_4$. Flow conservation
gives

$$
p_0+p_1+p_2+p_3=0.
$$

After translation, the potentials are $0,x,y,x+y$. Complete adjacency prevents
any nontrivial proper gauge selection, so the all-edge word is a circuit.
$\square$

## 11. Low-weight table

Combining evenness and the classifications:

| weight | gauge circuits |
|---:|---|
| $1$ | none |
| $2$ | equal-labelled $2K_2$ quotient |
| $3$ | none |
| $4$ | equal-labelled $4K_2$ quotient |
| $5$ | none |
| $6$ | $6K_2$, doubled $K_3$, or affine-plane $K_4$ quotient |

The next unresolved circuit layer is weight eight.

## 12. Structural meaning

The same local objects appear in decomposition theory:

- the equal-labelled two-edge quotient is the unique two-edge sewing mode;
- the three-edge theta graph with distinct plane labels has no gauge mode;
- circuit contraction and interface gluing view the same labelled quotient in
  opposite directions.

This correspondence is developed in
[`interface-gluing.md`](interface-gluing.md).