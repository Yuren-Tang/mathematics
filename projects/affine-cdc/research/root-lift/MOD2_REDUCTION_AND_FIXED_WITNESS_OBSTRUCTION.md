# Mod-$2$ reduction and the prescribed-witness sign obstruction

## 1. Integral and binary targets

Let $I$ be an index set of cardinality $q\ge3$. The integral target is

$$
A_I=\left\{x\in\mathbf Z^I:\sum_i x_i=0\right\},
$$

with roots $\pm(\varepsilon_i-\varepsilon_j)$. Reduction modulo $2$ lands in

$$
E_I=\left\{x\in\mathbf F_2^I:\sum_i x_i=0\right\}.
$$

For every distinct $i,j$,

$$
\boxed{
\varepsilon_i-\varepsilon_j
\equiv
\varepsilon_i+\varepsilon_j
\pmod2.}
$$

Thus the sign and order of the two endpoints disappear, while the unordered pair $\{i,j\}$ remains.

## 2. Binary root-flow theorem

Let $G$ be a finite loopless multigraph with reference orientations and let

$$
\varphi:E(G)\to\{\pm(\varepsilon_i-\varepsilon_j):i\ne j\}
$$

be an integral root flow. Its reduction

$$
\bar\varphi:E(G)\to
R_I:=\{\varepsilon_i+\varepsilon_j:i<j\}\subset E_I
$$

satisfies the binary Kirchhoff law.

For each $i$, put

$$
F_i=\{e:\bar\varphi_i(e)=1\}.
$$

Then every $F_i$ is vertex-even and every edge belongs to exactly two distinct indexed supports. Conversely, any such indexed even double-support system gives the $R_I$-valued binary flow

$$
e\longmapsto\varepsilon_{i(e)}+\varepsilon_{j(e)}.
$$

### Theorem 2.1

The following are canonically equivalent:

1. indexed vertex-even supports $(F_i)_{i\in I}$ with exact two-index edge multiplicity;
2. an $R_I$-valued binary flow;
3. an edge labelling by $E(K_I)$ whose inverse image of the star at $i$ is $F_i$.

If $G$ is cubic, the three labels incident with a vertex are the three edges of a triangle of $K_I$: in every coordinate, zero or two of the three local labels contain that coordinate.

This theorem retains unordered support incidence only. It contains no circuit partition and no orientation sign.

## 3. Deleted permutation module

The standard dot product on $E_I$ has radical

$$
\operatorname{rad}(E_I)=
\begin{cases}
0,&q\text{ odd},\\
\langle\mathbf1_I\rangle,&q\text{ even}.
\end{cases}
$$

Hence:

- for odd $q$, $E_I$ itself is the nondegenerate deleted permutation module of dimension $q-1$;
- for even $q$, the nondegenerate target is the fully deleted quotient
  $$
  \overline E_I=E_I/\langle\mathbf1_I\rangle
  $$
  of dimension $q-2$.

The quotient is necessary for nondegenerate orthogonal geometry, but not for the basic indexed-support equivalence. Keeping the raw $E_I$ labels is safer when reconstruction of the pair $\{i,j\}$ is required.

### Small even boundary

At $q=4$, complementary pairs have the same class:

$$
[\varepsilon_i+\varepsilon_j]
=
[\varepsilon_k+\varepsilon_l]
\quad
\text{when }\{k,l\}=I\setminus\{i,j\}.
$$

Thus $\overline E_I$ alone loses the six labelled $K_4$ roots by identifying opposite target edges. For even $q\ge6$, the weight-two root classes remain distinct. In particular, the $q=8$ quotient retains all $28$ unordered roots.

## 4. Why mod-$2$ does not orient

Reduction modulo $2$ forgets

- which of $i,j$ has coefficient $+1$;
- the direction of either support use relative to the reference edge;
- the circuit decomposition of each support;
- occurrence names and cyclic orders.

Therefore an unordered $R_I$-flow is not an oriented CDC and is not a chosen decomposition. Its integral lift problem is a simultaneous sign-and-balance problem.

For a prescribed support tuple $(F_i)$, an integral lift is equivalent to choosing, for every edge in supports $i,j$, one of the two roots

$$
\pm(\varepsilon_i-\varepsilon_j)
$$

so that the integral Kirchhoff equation holds at every vertex. Coordinatewise, this asks for orientations of all $F_i$ such that the two support uses of each edge are opposite.

## 5. Prescribed full circuit witness

Let

$$
\mathcal W=(\mathcal W_i)_{i\in I}
$$

be a prescribed **unoriented** full indexed circuit witness: every $\mathcal W_i$ is a finite multiset of circuit occurrences, and every source edge belongs to exactly two occurrences with distinct indices.

Form the **occurrence adjacency multigraph** $H_{\mathcal W}$:

- one vertex for every circuit occurrence, not merely for every support index;
- one edge $\widehat e$ for every source edge object $e$;
- $\widehat e$ joins the two circuit occurrences containing $e$.

Parallel edges are retained. Under the distinct-index, edge-simple circuit convention, $H_{\mathcal W}$ is loopless.

Choose an arbitrary preliminary orientation of every circuit occurrence. Define

$$
t_{\mathcal W}(e)=
\begin{cases}
0,&\text{the two preliminary circuit orientations traverse }e\text{ oppositely},\\
1,&\text{they traverse }e\text{ in the same direction}.
\end{cases}
$$

Thus $t_{\mathcal W}\in C^1(H_{\mathcal W};\mathbf F_2)$.

Reversing one circuit occurrence toggles exactly the incident edges of $H_{\mathcal W}$. If $x$ records which occurrences are reversed, then

$$
t_{\mathcal W}\longmapsto t_{\mathcal W}+\delta x.
$$

### Theorem 5.1 — exact prescribed-witness sign criterion

The prescribed unoriented full witness admits orientations making the two occurrences of every source edge opposite if and only if

$$
\boxed{
[t_{\mathcal W}]=0
\quad\text{in}\quad
C^1(H_{\mathcal W})/\operatorname{Cut}(H_{\mathcal W}).}
$$

Equivalently:

$$
t_{\mathcal W}\in\operatorname{Cut}(H_{\mathcal W}),
$$

or

$$
\langle t_{\mathcal W},z\rangle=0
\quad
(z\in Z_1(H_{\mathcal W})).
$$

When nonempty, the set of orientation choices is the affine solution set

$$
x_0+\ker\delta,
$$

so one independent global reversal remains on each connected component of $H_{\mathcal W}$.

### Proof

A reversal vector $x$ succeeds exactly when

$$
t_{\mathcal W}+\delta x=0.
$$

This equation is solvable exactly when $t_{\mathcal W}$ is a cut. Cut-cycle orthogonality gives the dual criterion. ∎

## 6. Support words versus full witnesses

If only the unoriented support tuple $(F_i)$ is prescribed, there need not be a prescribed occurrence graph. At vertices of support degree greater than two, different circuit pairings give different $H_{\mathcal W}$ and different cochains $t_{\mathcal W}$.

The exact support-only criterion is therefore either of the following equivalent existential statements:

1. there exists a circuit decomposition of every $F_i$ whose occurrence obstruction vanishes;
2. there exists an integral root-flow lift of the unordered $R_I$-flow.

One must not attach a single canonical occurrence obstruction to support-only data without a canonical decomposition rule. In the cubic two-regular support setting, connected support components are already circuit occurrences, so the ambiguity is greatly reduced; occurrence identities and repeated indices must nevertheless remain explicit.

## 7. Relation to the frozen OR1 class $\omega(g)$

For a compatible cubic affine lift $g$, the frozen OR1 candidate retains canonical support components, partner maps, and rotations and constructs a cellular cycle-face surface $S_g$. It defines

$$
\omega(g)=[w(g)]
\in C^1(G)/\operatorname{Cut}(G)
$$

from vertex-disc orientation changes.

The generic class

$$
[t_{\mathcal W}]
\in
C^1(H_{\mathcal W})/\operatorname{Cut}(H_{\mathcal W})
$$

is **not literally the same object**:

- its $0$-cochain gauge reverses circuit occurrences;
- $\omega(g)$ gauges vertex-disc orientations on the source graph;
- the two quotient spaces generally have different dimensions and different cut subspaces.

When $\mathcal W$ is the retained face witness of $g$, both vanish exactly when those faces can be oriented to traverse every edge oppositely. They are therefore two cellular resolutions of the same orientability event. A literal comparison requires the complete signed-rotation/cellular chain complex; no bare canonical isomorphism between the two displayed quotients is asserted here.

Because OR1 has not yet passed issue #51, this dossier uses only the stated frozen definitions for comparison and does not promote their assurance status.

## 8. Relation to the fixed-fibre class $\Omega_f$

The OR1 fixed-fibre object is

$$
\Omega_f\in
C^1(G)/(\operatorname{Cut}(G)+\mathcal B_f),
$$

where $\mathcal B_f$ is the image of the allowed affine gauge/Petrial motion inside one fixed compatible-lift fibre.

This has a strictly different quantifier from the generic prescribed-witness class:

- $[t_{\mathcal W}]$ tests one fixed full circuit witness;
- $\omega(g)$ tests one fixed retained affine lift and surface;
- $\Omega_f$ asks whether **some** lift in a specified torsor has vanishing fixed-lift obstruction.

Thus $\Omega_f$ is not the universal sign-lift obstruction of an arbitrary unordered root flow. It is obtained only after supplying:

1. a nonempty family of compatible lifts;
2. an action on that family;
3. a linear twist-change map;
4. a quotient by its image.

The generic analogue would be a quotient of a fixed-witness obstruction by the image of an explicitly defined reconfiguration group. Without that family data, the analogy must not be upgraded to identity.

## 9. Exact scope corrections

| Claim | Classification |
|---|---|
| integral root reduction gives unordered roots | proved equivalence |
| unordered roots give indexed even supports | proved equivalence |
| unordered root flow gives a chosen circuit decomposition | false |
| every prescribed full witness has a sign lift | false in general; exact cut criterion |
| prescribed support words have one canonical obstruction | false without canonical decomposition |
| occurrence class equals $\omega(g)$ literally | false / scope-corrected |
| occurrence class and $\omega(g)$ test the same retained-face orientability event | naturally related after full cellular data |
| occurrence class equals $\Omega_f$ | false; different family quantifier |
| even-$q$ orthogonal geometry uses $E_I/\langle\mathbf1\rangle$ | proved target correction |
