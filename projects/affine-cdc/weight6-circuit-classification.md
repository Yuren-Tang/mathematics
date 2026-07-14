# Classification of weight-six gauge circuits

**Date:** 2026-07-14  
**Status:** theorem-level draft; not yet Lean-formalized.

Let $G$ be a finite connected loopless multigraph with a nowhere-zero binary
flow $f:E(G)\to\Gamma$, where $\dim\Gamma\le3$. Let
$\lambda\in\mathcal B_f$ be a gauge circuit of weight six, and put
$S=\operatorname{supp}\lambda$.

Contract the connected components of $G-S$. The quotient $Q_S$ has six edges,
is connected and loopless, and carries the restricted labels as a nowhere-zero
flow and exact tension. The all-edge word is a circuit of its gauge code.

## Theorem

Up to isomorphism and a linear change of coordinates in $\Gamma$, exactly
three quotient types occur:

1. $6K_2$: two vertices joined by six parallel edges, all with one label $h$;
2. $2K_3$: a triangle with every edge doubled, the three doubled pairs labelled
   $x$, $y$, and $x+y$;
3. $K_4$: four vertices forming a simple complete graph, with vertex
   potentials $0,x,y,x+y$; each of the three nonzero labels occurs on one
   perfect matching.

Conversely, the all-edge word is a gauge circuit in each of these three
labelled quotients.

Thus

$$
\boxed{
\text{weight-six gauge circuits}
=
6K_2,\ 2K_3,\ \text{or }K_4
\text{ flow--tension quotients}.
}
$$

## 1. There is no degree-two quotient vertex

Suppose a quotient vertex $v$ has incident edges $e_1,e_2$. The flow equation
forces their labels to be equal.

The word supported on $\{e_1,e_2\}$ is an exact tension: assign potential $h$
to $v$ and $0$ to every other component. It is therefore a nonzero proper
gauge word, contradicting circuit minimality.

Hence

$$
\delta(Q_S)\ge3.
$$

Since $Q_S$ has six edges,

$$
\sum_v\deg(v)=12,
$$

so $Q_S$ has at most four vertices.

## 2. Two quotient vertices

All six edges are parallel. Exactness forces every edge label to equal the
single potential difference $h\ne0$. Six copies of $h$ satisfy the flow
equation.

Any gauge potential difference between the two vertices must be either $0$ or
$h$. Therefore the gauge code consists only of the zero word and the all-edge
word, which is a circuit.

This gives $6K_2$.

## 3. Three quotient vertices

Write the edge multiplicities between the three vertex pairs as $a,b,c$, with

$$
a+b+c=6.
$$

### A missing vertex pair

If one multiplicity is zero, the quotient is a path of two parallel bundles.
At either endpoint, the flow equation forces the incident bundle multiplicity
to be even. Thus the two positive multiplicities are $2$ and $4$.

Either bundle then gives a proper gauge word of weight two or four, contrary to
minimality.

### All three vertex pairs present

Translate one vertex potential to $0$, and write the other two as independent
vectors $x,y$. The three pair labels are

$$
x,\qquad y,\qquad x+y.
$$

At the first vertex, the flow equation is

$$
(a\bmod2)x+(b\bmod2)y=0.
$$

Independence forces $a$ and $b$ even. The other vertex equations force $c$
even. Since all are positive and sum to six,

$$
a=b=c=2.
$$

Thus the quotient is $2K_3$.

To check minimality, normalize a possible gauge potential to zero at the first
vertex. At the other two vertices it must be respectively either $0$ or
$x$, and either $0$ or $y$. The edge between them rules out the two mixed
choices. Hence only the zero and full gauge words occur.

## 4. Four quotient vertices

Minimum degree at least three and total degree twelve force the quotient to be
cubic.

If it had two parallel edges at a vertex, their equal labels would cancel in
the flow equation and force the third incident edge label to be zero. Three
parallel edges would disconnect the remaining vertices. Therefore the quotient
is simple, hence it is $K_4$.

Let the four vertex potentials be $p_0,p_1,p_2,p_3$. They are pairwise
distinct. At any vertex, the flow equation reduces to

$$
p_0+p_1+p_2+p_3=0.
$$

After translation, the potentials are

$$
0,\qquad x,\qquad y,\qquad x+y
$$

for independent $x,y$. The opposite edges of $K_4$ therefore carry equal
labels, and the three perfect matchings receive $x$, $y$, and $x+y$.

For minimality, normalize a competing gauge potential at the vertex labelled
$0$. Each of the other three values is either $0$ or its original potential.
Because every pair of vertices is adjacent, mixed choices are impossible.
Again only the zero and full words occur.

## 5. Partition form in the original graph

A weight-six circuit therefore determines one of three connected-part
partitions of $G-S$:

- two parts with six equal-labelled crossing edges;
- three parts with two edges between every pair, labelled by one Fano line
  $x,y,x+y$;
- four parts whose quotient is $K_4$, with the quotient potentials forming an
  affine plane.

This is a directly checkable graph-theoretic description of all weight-six
dependencies.

## 6. Low-weight table

Combining the parity theorem and the earlier classifications:

| Weight | Gauge circuits |
|---:|---|
| $1$ | none |
| $2$ | equal-labelled $2K_2$ quotient |
| $3$ | none |
| $4$ | equal-labelled $4K_2$ quotient |
| $5$ | none |
| $6$ | $6K_2$, $2K_3$, or affine-plane $K_4$ quotient |

The next unresolved circuit layer is weight eight.
