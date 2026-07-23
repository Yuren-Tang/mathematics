# The $q=5$ oriented five-support specialization

## 1. Integral and binary five-support targets

Let $I=[5]$. The integral target is

$$
A_4=\left\{x\in\mathbf Z^5:\sum_{i=1}^5x_i=0\right\}
$$

with roots

$$
\Phi(A_4)=\{\pm(\varepsilon_i-\varepsilon_j):i\ne j\}.
$$

The binary target is

$$
H_5=\left\{z\in\mathbf F_2^5:\sum_i z_i=0\right\},
\qquad
R_5=\{\varepsilon_i+\varepsilon_j:i<j\}.
$$

Because $5$ is odd, $H_5$ is already nondegenerate under the standard dot product and has dimension four. With

$$
q_5(z)=\sum_{i<j}z_iz_j,
$$

its ten anisotropic vectors are exactly $R_5$, giving the standard $O^-(4,2)$ model.

## 2. Exact oriented specialization

### Theorem 2.1

For a finite loopless multigraph with reference orientations, the following are canonically equivalent:

1. directed indexed Eulerian five-support systems;
2. $A_4$ root flows;
3. edge labellings by the directed edges of the complete digraph on $[5]$, where
   $$
   \varepsilon_i-\varepsilon_j
   $$
   is the arc $j\to i$.

A full oriented five-support CDC is obtained only after choosing directed circuit decompositions of the five coordinate supports.

At a cubic source vertex, multiply each incident root by its incidence sign at that vertex. The three resulting roots sum to zero. Three nonzero type-$A$ roots with zero sum form a directed target triangle

$$
\varepsilon_a-\varepsilon_b,
\qquad
\varepsilon_b-\varepsilon_c,
\qquad
\varepsilon_c-\varepsilon_a
$$

on three distinct support indices. Thus the integral local object is an oriented $K_5$ triangle.

## 3. Reduction to the existing $R_5/K_5$ witness

Modulo $2$,

$$
\pm(\varepsilon_i-\varepsilon_j)
\longmapsto
\varepsilon_i+\varepsilon_j.
$$

Therefore every $A_4$ root flow gives:

1. an $R_5$-valued flow;
2. a $K_5$ edge labelling whose three local labels form a triangle;
3. five indexed vertex-even supports with exact edge multiplicity two;
4. an anisotropic flow in $O^-(4,2)$.

Conversely, an $R_5$ flow determines the unordered five-support witness but not its integral signs. Its lift to an $A_4$ root flow is exactly the sign-and-balance problem of the generic dossier.

Hence the safe hierarchy is

$$
\boxed{
A_4\text{ root flow}
\Longrightarrow
R_5\text{ flow}
\Longleftrightarrow
K_5\text{ triangle labels}
\Longleftrightarrow
O^-(4,2)\text{ anisotropic flow}.}
$$

The reverse arrow to $A_4$ requires a sign lift and is not automatic from the binary equivalence box.

## 4. Full witness and cycle occurrence boundary

The five binary coordinate supports are Eulerian. They do not include a circuit partition. For a prescribed full five-support circuit witness, the exact integral-lift criterion is the occurrence-graph cut condition from

`MOD2_REDUCTION_AND_FIXED_WITNESS_OBSTRUCTION.md`.

For a cubic graph, every nonempty connected component of one support is $2$-regular and hence is already a circuit occurrence. In that setting the prescribed occurrence graph is naturally available after components and repeated indices are retained. The remaining question is whether those occurrences can be oriented so that each source edge is used oppositely.

Repeated equal support values at different indices remain distinct. Empty indices remain part of the five-coordinate witness and simply contribute no circuit occurrence.

## 5. Quadratic and Schur coordinates

The frozen Programme B2 coordinate isomorphism writes a binary five-support witness as cycle words

$$
b,d,x,y\in\mathcal C(G)
$$

satisfying

$$
\boxed{b*d=(\mathbf1+x)*(\mathbf1+y).}
$$

The resulting five supports are

$$
\Phi(b,d,x,y)
=(b,d,b+d+y,b+d+x,b+d+x+y).
$$

This is a complete reconstruction of the **unordered binary** witness. It does not record:

- a sign on $\varepsilon_i-\varepsilon_j$;
- a direction on a circuit occurrence;
- an integral Kirchhoff lift;
- a prescribed surface orientation.

Likewise, fixed singular-quotient and Schur criteria decide whether a prescribed binary quotient lifts to an anisotropic $O^-(4,2)$ flow. They lie before the additional integral sign-lift problem. Relative stresses and Fourier counts are dual or counting certificates and require a primal binary witness before any orientation question can even be posed.

## 6. Cographic formulation

A binary five-support witness is equivalently a cycle-continuous edge map

$$
\phi:E(G)\to E(K_5),
$$

where the inverse image of each target star is a source cycle word. This map remembers the unordered target edge $\{i,j\}$.

An $A_4$ root flow refines it to a directed target-edge labelling

$$
\widetilde\phi:E(G)\to A(K_5)
$$

with a source-reference sign. The local Kirchhoff equation says that the incidence-adjusted target arcs form directed cycles. Forgetting target-arc direction gives the cographic map.

No orientation of $K_5$ chosen once and for all supplies this refinement: both directions of each target edge are needed, and their selection is constrained globally by the source flow equations.

## 7. Stress formulations

The existing five-support stress spaces test binary affine-orbit membership or fixed quotient compatibility. They are not orientation stresses unless an additional sign-lift differential has been defined.

For a prescribed full circuit witness, the sign obstruction has its own exact dual space:

$$
Z_1(H_{\mathcal W})
$$

on the circuit-occurrence adjacency graph. A nonzero pairing with the twist word certifies failure of that prescribed orientation lift.

It is therefore unsafe to identify:

- Programme B compatibility stress;
- Programme B2 relative stress;
- OR1 fixed-fibre orientation stress;
- the generic prescribed-occurrence cycle test.

They have different domains, gauge images, and quantifiers.

## 8. Relation to nowhere-zero five-flows

Choose a global bijection

$$
c:I\longrightarrow\mathbf F_5.
$$

It defines a homomorphism

$$
\pi_c:A_4\longrightarrow\mathbf F_5,
\qquad
\pi_c\left(\sum_i n_i\varepsilon_i\right)=\sum_i n_i c(i).
$$

For every root,

$$
\pi_c(\varepsilon_i-\varepsilon_j)=c(i)-c(j)\ne0.
$$

### Theorem 8.1 — coefficient projection

Every $A_4$ root flow projects under $\pi_c$ to a nowhere-zero $\mathbf F_5$-flow.

This implication uses one **globally fixed** coefficient assignment to the five support indices.

### Converse boundary

A nowhere-zero $\mathbf F_5$-flow records only one scalar difference on each edge. To lift it to an $A_4$ root flow one must choose, for every edge, an ordered pair $(i,j)$ with

$$
c(i)-c(j)=\psi(e)
$$

and make all five coordinate Kirchhoff equations hold. The scalar equation is only the image of those equations. Thus a fixed scalar five-flow does not canonically reconstruct a five-support witness or an integral root lift.

This dossier does not assert that a prescribed $\mathbf F_5$-flow always or never has such a lift. That is a separate fixed-data lifting problem.

## 9. Three coefficient structures that must be separated

### 9.1 Endpoint coefficient choice

For one already labelled root $\varepsilon_i-\varepsilon_j$, choosing $c(i),c(j)$ merely evaluates it as a nonzero scalar difference. This is edgewise and loses most root data.

### 9.2 Global affine coefficient structure

A single bijection $c:I\to\mathbf F_5$ identifies the five support indices with the affine line over $\mathbf F_5$. It makes $\pi_c$ a globally defined flow homomorphism. Changing $c$ by an affine transformation changes the scalar flow by a global nonzero scale and translation cancels on differences.

### 9.3 Locally transported structures and holonomy

If coefficient charts are chosen separately at source vertices, their transition maps lie in the affine group of $\mathbf F_5$. Edge compatibility and cycle holonomy must be solved before the local charts define one global support-index coefficient structure. Triviality of this chart holonomy is distinct from:

- existence of the unordered five-support witness;
- sign-lift orientability of its circuit occurrences;
- OR1 surface twist holonomy.

A local affine-$\mathbf F_5$ interpretation must therefore not be advertised as a global nowhere-zero five-flow correspondence without an explicit transport theorem.

## 10. Exact formulation hierarchy

| Formulation | Retains full unordered five-support witness? | Retains integral orientation signs? |
|---|---:|---:|
| $A_4$ root flow | yes | yes, at support-word level |
| directed $K_5$ triangle labels | yes | yes, at support-word level |
| full oriented five-support CDC | yes | yes, plus chosen circuit occurrences |
| $R_5$ flow / $K_5$ triangle labels | yes | no |
| anisotropic $O^-(4,2)$ flow | yes | no |
| quadratic cycle solution | yes after $\Phi$ | no |
| cographic cycle-continuous map | yes by target-star inverse images | no |
| fixed singular/Schur criterion | only after solving the lift | no |
| relative stress/Fourier data | dual/counting layer | no |
| nowhere-zero $\mathbf F_5$-flow | scalar projection only | no root reconstruction |

## 11. Classification

- `A_4 root flow ↔ directed Eulerian five-support system`: **specialization theorem**.
- `A_4 root flow → oriented five-support CDC`: **proved only after circuit decomposition**.
- `A_4 mod 2 = R_5/K_5/O^-(4,2) witness`: **proved specialization theorem**.
- `quadratic, Schur, cographic, and stress data already contain signs`: **false / scope-corrected**.
- `A_4 root flow → nowhere-zero F_5 flow after global coefficient choice`: **proved specialization theorem**.
- `nowhere-zero F_5 flow ↔ oriented five-support witness`: **not proved; proposed equivalence too strong without a global lift theorem**.
- `local affine coefficient charts automatically globalize`: **false without holonomy control**.
