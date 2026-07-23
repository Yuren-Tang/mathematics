# The $q=8$ affine/Fano specialization

## 1. Three targets attached to eight indices

Let the index set be the affine space

$$
I=\Gamma=\mathbf F_2^3.
$$

There are three distinct target levels.

### Integral level

$$
A_7=\left\{x\in\mathbf Z^{\Gamma}:\sum_{a\in\Gamma}x_a=0\right\},
$$

with roots $\pm(\varepsilon_a-\varepsilon_b)$.

### Raw binary level

$$
E_8=\left\{z\in\mathbf F_2^{\Gamma}:\sum_a z_a=0\right\},
$$

with unordered roots $\varepsilon_a+\varepsilon_b$.

### Orthogonal quotient

Because $8$ is even, $\mathbf1_\Gamma$ spans the radical of the dot product on $E_8$. The fully deleted module is

$$
\overline E_8=E_8/\langle\mathbf1_\Gamma\rangle,
$$

of dimension six. The quadratic form

$$
q([z])=\frac{\operatorname{wt}(z)}2\pmod2
$$

is well-defined and has plus type. Its $28$ root classes

$$
[\varepsilon_a+\varepsilon_b]
$$

are anisotropic and remain pairwise distinct. Thus the binary eight-support target is the exceptional $O^+(6,2)$ root model.

The integral target has rank seven. Passing to $\overline E_8$ removes a binary radical and forgets the sign; it is not an integral model of $A_7$.

## 2. The affine quotient to a Fano flow

Define

$$
\pi_\Gamma:A_7\longrightarrow\Gamma,
\qquad
\pi_\Gamma\left(\sum_a n_a\varepsilon_a\right)
=\sum_a (n_a\bmod2)a.
$$

For a root,

$$
\boxed{
\pi_\Gamma(\varepsilon_a-\varepsilon_b)=a+b\ne0.}
$$

Therefore every $A_7$ root flow projects to a nowhere-zero $\Gamma$-flow.

On the binary level, the map

$$
E_8\longrightarrow\Gamma,
\qquad
z\longmapsto\sum_a z_a a
$$

annihilates $\mathbf1_\Gamma$, because the sum of all eight points of $\mathbf F_2^3$ is zero. It therefore factors through $\overline E_8$.

For each nonzero $h\in\Gamma$, the four unordered pairs $\{a,a+h\}$ are the four affine lines of direction $h$. Hence a compatible unordered lift above a Fano flow chooses, on every source edge of value $h$, one of these affine pairs.

## 3. Generic $A_7$ statement

The generic theorem gives

$$
\boxed{
A_7\text{ root flows}
\longleftrightarrow
\text{directed indexed Eulerian eight-support systems}.}
$$

A full oriented eight-support CDC is obtained after directed circuit decomposition. Reducing modulo $2$ gives an unordered eight-support root flow in $E_8$, hence in the $O^+(6,2)$ quotient, and then the Fano-flow quotient $a+b$.

Thus the safe implication chain is

$$
A_7\text{ root flow}
\Longrightarrow
E_8\text{ unordered root flow}
\Longrightarrow
O^+(6,2)\text{ root flow}
\Longrightarrow
\Gamma\text{-flow}.
$$

None of the reverse arrows is automatic without retained lift data.

## 4. Fixed compatible affine-pair lift

Fix a nowhere-zero Fano flow

$$
f:E(G)\to\Gamma\setminus\{0\}
$$

and a compatible labelled affine-pair lift

$$
g(e)=\{a_e,b_e\},
\qquad
a_e+b_e=f(e).
$$

The unordered pair data define the eight vertex-even supports

$$
F_a=\{e:a\in g(e)\}.
$$

### Theorem 4.1 — fixed-pair integral sign lift

The following are equivalent, independently of surface terminology:

1. the fixed unordered pair labelling $g$ lifts to an $A_7$ root flow by choosing one of
   $$
   \pm(\varepsilon_{a_e}-\varepsilon_{b_e})
   $$
   on every edge;
2. all eight supports can be oriented as directed Eulerian supports so that the two uses of every edge are opposite;
3. after fixing the support-component circuit occurrences in the cubic case, their occurrence-graph twist class vanishes.

The proof is the generic forward/reverse construction and the fixed-witness cut criterion.

In the cubic compatible setting, every nonempty connected support component is a circuit occurrence. Thus the affine construction supplies a particularly natural full unoriented witness to which the sign criterion applies.

## 5. Comparison with the frozen OR1 class

The frozen OR1 candidate retains partner maps and rotations and constructs a cycle-face surface $S_g$. It records the fixed-lift class

$$
\omega(g)\in C^1(G)/\operatorname{Cut}(G).
$$

Within that frozen theorem package,

$$
\omega(g)=0
$$

is equivalent to orienting the retained support-component faces so that the two sides of every edge are opposite. Therefore, for the fixed compatible pair lift,

$$
\boxed{
\text{$A_7$ integral sign lift of $g$}
\iff
\text{oppositely oriented retained faces}
\iff
\omega(g)=0,}
$$

where the last equivalence inherits the exact assurance status

`AUTHORIAL / CURATOR-INTEGRATED / NOT YET INDEPENDENTLY VERIFIED`.

The generic occurrence class and $\omega(g)$ are not identified as literal cohomology classes; they are two resolutions of this same fixed-face event after the complete cellular data are supplied.

## 6. Compatible-lift torsor

The rank-three affine construction supplies a nonempty compatible-lift torsor above a fixed Fano flow. Its vertical motion is described in the frozen candidate by

$$
H_f^0
$$

and the gauge-word map

$$
\Lambda_f:H_f^0\to C^1(G),
\qquad
\mathcal B_f=\operatorname{im}\Lambda_f.
$$

The chain-level law is

$$
w(g^k)=w(g)+\Lambda_f(k)
$$

for transported local orientations. Consequently, the family question becomes the linear quotient

$$
\Omega_f
\in
C^1(G)/(\operatorname{Cut}(G)+\mathcal B_f).
$$

Within the frozen OR1 package,

$$
\boxed{
\Omega_f=0
\iff
\text{some compatible affine-pair lift above $f$ admits an $A_7$ sign lift}.}
$$

This is a genuine simplification: the search over the compatible affine torsor is reduced to one finite binary linear obstruction and its dual orientation-stress test.

It is not a proof that the obstruction vanishes.

## 7. What the Fano structure contributes

Beyond the generic $A_7$ statement, the affine/Fano structure contributes:

1. a canonical eight-point index set with a translation action;
2. the quotient map from unordered roots $\{a,b\}$ to the nonzero direction $a+b$;
3. exactly four affine-pair lifts above each nonzero Fano value;
4. automatic nonemptiness of the compatible unordered lift fibre in the inherited rank-three theory;
5. an explicit torsor of compatible lifts;
6. an explicit linear image $\mathcal B_f$ describing accessible partial-Petrial changes;
7. the quotient obstruction $\Omega_f$ and a dual stress space.

These objects organize the integral sign-lift problem; they do not eliminate it.

## 8. What the exceptional orthogonal model does not contribute

The exceptional isomorphism with $O^+(6,2)$ does not:

- retain the sign of $\varepsilon_a-\varepsilon_b$;
- choose an orientation of a support component;
- select a circuit decomposition;
- provide a canonical section $\overline E_8\to A_7$;
- force $\omega(g)=0$ for every compatible lift;
- force $\Omega_f=0$ for every fixed Fano flow.

The dimension coincidence

$$
8-2=6=2\cdot3
$$

explains why the fully deleted module has the same dimension as a rank-three orthogonal space. It does not start a universal $O^+(2r,2)$ tower for $2^r$ support points; the inherited Programme B2 lower bound rules out that extrapolation from $r\ge4$.

## 9. Exact $K_4$ warning inherited from the frozen candidate

For the standard Fano flow on $K_4$, the frozen candidate exhibits two compatible lifts in the same fibre:

- one with projective-plane cycle-face surface and nonzero $\omega$;
- one with tetrahedral-sphere surface and zero $\omega$.

Thus even in the smallest exact example:

1. compatible affine lifting does not imply per-lift integral sign lifting;
2. gauge motion can change the sign-lift obstruction;
3. that particular fibre has $\Omega_f=0$ and is not a fixed-fibre counterexample.

This example rules out the strongest proposed simplification but does not decide universal fixed-fibre vanishing.

## 10. Open boundary

The following remain open in the inherited orientation programme:

- whether $\Omega_f=0$ for every nowhere-zero Fano flow on every finite bridgeless cubic multigraph;
- if not, whether every such graph admits at least one Fano flow with $\Omega_f=0$.

For the present root-lift programme, the corresponding exact statement is:

> Does every relevant fixed Fano-flow fibre contain a compatible unordered affine-pair lift whose signs form an $A_7$ root flow?

No universal vanishing, graph-level oriented CDC, or canonical integral section is claimed here.

## 11. Classification

| Statement | Classification |
|---|---|
| $A_7$ root flow gives directed eight supports | specialization theorem |
| mod-$2$ target is the fully deleted $O^+(6,2)$ module | specialization theorem |
| affine pair $\{a,b\}$ projects to Fano value $a+b$ | specialization theorem |
| fixed compatible pair lift has an $A_7$ sign lift iff its retained occurrences orient oppositely | fixed-witness criterion |
| this event is represented by $\omega(g)=0$ | frozen OR1 comparison; not independently verified here |
| some lift in the fixed fibre succeeds iff $\Omega_f=0$ | frozen OR1 fixed-fibre comparison |
| Fano torsor makes the search linear | proved structural simplification within the frozen package |
| Fano or $O^+(6,2)$ structure forces vanishing | false as a per-lift claim; open at fixed-fibre/global level |
| orthogonal quotient canonically recovers integral signs | false |
