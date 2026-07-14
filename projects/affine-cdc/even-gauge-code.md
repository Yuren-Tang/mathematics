# The Fano gauge code is even

**Date:** 2026-07-14  
**Status:** theorem-level draft; not yet Lean-formalized.

Let $G$ be a finite loopless multigraph and let

$$
f:E(G)\to\Gamma,
\qquad
\dim_{\mathbf F_2}\Gamma\le 3,
$$

be a nowhere-zero binary flow. Let $\mathcal B_f$ be the gauge-moduli code:
$\lambda\in\mathcal B_f$ iff the vector-valued edge function

$$
g_e:=\lambda_e f(e)
$$

is an exact tension.

## Theorem

Every word of $\mathcal B_f$ has even Hamming weight:

$$
\boxed{
\lambda\in\mathcal B_f
\Longrightarrow
\operatorname{wt}(\lambda)\equiv0\pmod2.
}
$$

Equivalently, $\mathcal B_f$ is an even binary code. In particular, every
flow-constraint-matroid circuit has even cardinality.

## 1. Reduction to a nowhere-zero flow--tension bicycle

Fix $\lambda\in\mathcal B_f$ and put $S=\operatorname{supp}\lambda$.
Contract every connected component of $G-S$. On the resulting loopless
multigraph $Q_S$, the restricted labels

$$
g:S\to\Gamma
$$

are simultaneously:

- a nowhere-zero flow;
- an exact tension.

It is therefore enough to prove that every nowhere-zero $\Gamma$-valued
flow--tension bicycle on a finite loopless multigraph has an even number of
edges when $\dim\Gamma\le3$.

## 2. Scalar harmonic tensions

Choose coordinates on $\Gamma\le\mathbf F_2^3$. Write the coordinate edge
functions as

$$
x_e=a_u+a_v,
\qquad
y_e=b_u+b_v,
\qquad z_e=c_u+c_v
$$

for $e=uv$. Since each coordinate is also a flow, the vertex functions
$a,b,c$ satisfy the mod-$2$ harmonic equations

$$
\deg(v)a_v+\sum_{u\sim v}a_u=0,
$$

and similarly for $b,c$, with parallel neighbours counted with multiplicity.

Because every coordinate edge function lies both in the binary cycle space
and in the binary cut space,

$$
\sum_e x_e=0,
\qquad
\sum_e x_ey_e=0,
$$

and similarly for all degree-one and degree-two coordinate monomials.

## 3. The cubic identity

The remaining term is

$$
S_3:=\sum_{uv\in E}(a_u+a_v)(b_u+b_v)(c_u+c_v).
$$

Let

$$
P:=\sum_v\deg(v)a_vb_vc_v.
$$

Expanding $S_3$, the two pure endpoint terms contribute $P$. The six mixed
terms split into three oriented sums:

$$
A=\sum_v b_vc_v\sum_{u\sim v}a_u,
$$

$$
B=\sum_v a_vc_v\sum_{u\sim v}b_u,
$$

$$
C=\sum_v a_vb_v\sum_{u\sim v}c_u.
$$

By harmonicity,

$$
A=B=C=P.
$$

Hence, in characteristic two,

$$
S_3=P+A+B+C=P+P+P+P=0.
$$

Therefore every squarefree coordinate monomial of degree at most three has
zero total over the edge set.

## 4. The nonzero indicator polynomial

For $(x,y,z)\in\mathbf F_2^3$, the indicator of being nonzero is

$$
\mathbf 1_{(x,y,z)\ne0}
=
x+y+z+xy+xz+yz+xyz.
$$

Every label $g_e$ is nonzero, so

$$
|S|
=
\sum_{e\in S}\mathbf 1_{g_e\ne0}.
$$

Each of the seven monomial sums on the right vanishes by the preceding
identities. Thus

$$
|S|\equiv0\pmod2.
$$

This proves the theorem.

## 5. Consequences

### No odd circuits

There are no gauge circuits of weights

$$
1,3,5,7,\ldots
$$

in the rank-three Fano theory.

Thus the previous low-weight classification sharpens to:

- weight $2$: equal-labelled two-edge bonds;
- weight $4$: equal-labelled four-edge bonds;
- the next possible weight is $6$, not $5$.

### Constraint-matroid consequence

The flow constraint matroid is an **even binary matroid**: every circuit has
even size. Equivalently, its cycle code $\mathcal B_f$ is even.

### Coding-theoretic formulation

Since

$$
\mathcal B_f=(\mathcal C(G)*\mathcal F_f)^\perp,
$$

evenness is equivalent to

$$
\mathbf 1_E\in\mathcal C(G)*\mathcal F_f.
$$

The harmonic proof above therefore yields the nontrivial Schur-code identity

$$
\boxed{
\mathbf 1_E\in\mathcal C(G)*\mathcal F_f
}
$$

for every nowhere-zero rank-at-most-three binary flow.

### Census check

The complete small-graph census agrees:

- triangular prism circuits: weight $6$;
- cube circuits: weights $4,6,8,10,12$;
- Wagner circuits: weights $4,6,8,10$;
- Petersen circuits: weights $8,10,12$.

No odd circuit occurs.

## 6. Significance

This is the first general graph-theoretic theorem produced naturally by the
flow-tensor/code-flag framework that is not merely a dimension restatement.
It converts the Fano rank bound into a parity law for every gauge dependency,
and it rules out an infinite family of possible flow--tension quotients at
once.
