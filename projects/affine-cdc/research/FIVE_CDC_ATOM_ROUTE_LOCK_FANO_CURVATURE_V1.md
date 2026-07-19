# Atom route-lock, Fano compression, and quadratic touch curvature

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level finite reduction of blocked one-edge co-root atoms; exact quotient and local-to-global curvature formalism; strict graph replacement remains open  
**Parents:** `FIVE_CDC_DDD_ATOM_RESOLUTION_TRIALITY_V1.md`, `FIVE_CDC_DEFECT_MINIMAL_FOREST_PETERSEN_TRANSPORT_V1.md`, `FIVE_CDC_BBD_GLOBAL_AFFINE_HOLONOMY_K6_DEFECT_STRIP_V1.md`

## 1. Purpose

A nondegenerate one-edge co-root atom has three local resolutions:

\[
\{\infty i,X,Y\},
\]

where `infinity i` is the present co-root realisation and `X,Y` are the two root-valued crossed resolutions.  The preceding packet did not determine whether one of the two crossed resolutions can be realised by a genuine Kempe switch in the complementary four-pole.

This packet proves the exact obstruction law.  If neither crossed resolution is realised, every full support-pair challenge is forced to use the original atom pairing.  The forced orbit is a six-state `K_{2,4}`.  At either of its two `C`-states, the four locked challenges compress the complementary root flow to a nowhere-zero `F_2^3`-flow with equal terminal value.

The four scalar circuit partitions then possess a precise local-to-global obstruction: a quadratic bit carried by edges of the terminal colour.  When the global curvature class vanishes, all four circuit partitions admit one common affine side potential.

The exact residual ladder is therefore:

\[
\boxed{
\text{K4 rank drop}
\quad\text{or}\quad
\text{nonzero quadratic touch curvature}
\quad\text{or}\quad
\text{flat eight-state potential geometry}.
}
\]

No five-cycle double cover theorem or strict replacement theorem is claimed.

## 2. Universal route-lock theorem

Let the four boundary semiedges be ordered so that the present atom incidence pairs

\[
12\mid34.
\]

Let their root labels be

\[
\ell_1,\ell_2,\ell_3,\ell_4\in R_5,
\qquad
\ell_1+\ell_2+\ell_3+\ell_4=0.
\]

Put

\[
d=\ell_1+\ell_2=\ell_3+\ell_4.
\]

The atom is root-valued exactly when `d` is a root.  The bad cases are

\[
d=0
\quad\text{or}\quad
 d=q_i=\mathbf 1+e_i.
\]

Let `a in R_5` be a full challenge, meaning that the symmetric difference of the two corresponding supports has all four terminals.  Equivalently,

\[
\langle a,\ell_t\rangle=1
\qquad(t=1,2,3,4).
\]

Switching one terminal path component toggles `a` on the two terminals of its route.

### Theorem 2.1 — unique bad route

For every bad boundary state and every full challenge `a`:

\[
\boxed{
\begin{array}{c|c}
\text{route}&\text{new internal sum}\
\hline
12\mid34&d,\
13\mid24&d+a,\
14\mid23&d+a.
\end{array}}
\]

Moreover `d+a` is always a root.  Consequently:

\[
\boxed{
\text{exactly one route remains bad, namely the original atom pairing.}
}
\]

#### Proof

A route parallel to `12|34` toggles either both or neither terminal at each atom endpoint, so `d` is unchanged.  Either crossed route toggles exactly one terminal at each endpoint, so the new sum is `d+a`.

If `d=0`, then `d+a=a` is a root.  If `d=q_i`, the full-challenge equations give

\[
\langle a,q_i\rangle
=
\langle a,\ell_1\rangle+
\langle a,\ell_2\rangle
=0.
\]

A root has even intersection with `q_i` exactly when it avoids `i`.  Hence `a subset [5]\setminus\{i\}`, and `q_i+a` is the complementary root in that `K_4`.  ∎

Thus a blocked atom forces the universal policy

\[
\boxed{
\operatorname{route}(a)=12\mid34
\quad\text{for every full challenge }a.
}
\]

Exact enumeration of all `640` ordered root boundary states gives `280` bad states and `840` bad-state/full-challenge pairs.  Every one has the route word

\[
(\mathrm{bad},\mathrm{good},\mathrm{good}).
\]

## 3. The six-state co-root route-lock orbit

Assume `d=q_i`.  Put

\[
Q=[5]\setminus\{i\}.
\]

At each atom endpoint the two boundary roots are disjoint edges of `K_Q`, hence form a perfect matching of `K_Q`.

A safe switch acts only on terminals `1,2`; therefore the right ordered perfect matching is fixed.  The left ordered perfect matching may be any of the six ordered matchings of `K_Q`.

### Theorem 3.1 — exact `K_{2,4}` orbit

For fixed `i` and fixed right ordered matching, the safe-switch orbit has six ordered states and transition graph

\[
\boxed{K_{2,4}.}
\]

The bipartition is:

- two `C`-states, where the left and right unordered matchings coincide;
- four `D`-states, where they differ.

At a `D`-state the two full challenges are the two edges of the omitted third matching; they lead to the two `C`-states.  At a `C`-state the four full challenges are the four edges outside the common matching; they lead to the four `D`-states.

Globally, the `180` ordered co-root bad states split into exactly `30` such six-state components.

For the canonical state

\[
(23,45,24,35),
\]

with atom pairing `12|34`, the two full challenges are `25` and `34`.  Their blocked route leads to the two `C`-states.  The DDD rainbow routes are crossed routes and would rootify the atom immediately; DDD is therefore a resolution symmetry, not the blocked endpoint.

## 4. Fano compression at a locked `C`-state

Use the canonical locked `C`-state

\[
(35,24,24,35).
\]

Here

\[
q_1=2345,
\qquad
p=24,
\qquad
q=35,
\qquad
p+q=q_1.
\]

The four full challenges are

\[
23,25,34,45.
\]

Let

\[
V=E_5/\langle q_1\rangle.
\]

Then `dim V=3`.  The two terminal roots `p,q` have the same image

\[
g=[p]=[q]\ne0.
\]

Every root has nonzero image, because the kernel contains only `0,q_1`.  Hence the complementary root flow descends to a nowhere-zero flow

\[
c:E(Q)\longrightarrow V\setminus\{0\}
\]

whose four terminal values are all `g`.

For a challenge root `a subset Q`, define

\[
\lambda_a([r])=|a\cap r|\pmod2.
\]

This is well defined because `lambda_a(q_1)=0`.  The four full challenges give exactly the affine plane

\[
\boxed{
\Lambda_g
=
\{\lambda\in V^*: \lambda(g)=1\}.
}
\]

For every `lambda in Lambda_g`, the scalar flow

\[
H_\lambda=\{e:\lambda(c(e))=1\}
\]

has four terminal semiedges and, under route-lock, pairs them as

\[
12\mid34.
\]

Thus the atom obstruction is converted into four locked scalar circuit partitions indexed by `AG(2,2)`.

## 5. Exact rank-drop theorem

Suppose the edge colours of `c` fail to span all of `V`.  Since `g` occurs at the terminals, any annihilating functional `mu` satisfies `mu(g)=0`.

The three nonzero functionals on `V` vanishing at `g` are represented upstairs by

\[
p,
\qquad q,
\qquad q_1.
\]

### Theorem 5.1 — rank drop is exactly the `K_4` sector

\[
\boxed{
\dim\langle c(E)\rangle<3
\iff
\text{every root label of the complementary four-pole avoids support }1.
}
\]

In that case the labels are precisely roots of the induced `K_4` on supports `2,3,4,5`, and the quotient span has dimension two.

#### Proof

If the annihilator were represented by the terminal root `p`, then every incident label at a terminal carrying `p` would have even intersection with `p`.  But a zero-sum triple of nonzero roots containing `p` is a triangle of `K_5`; the other two triangle edges each meet `p` once.  Contradiction.  The same argument excludes `q`.

The only remaining annihilator is `q_1`.  A root has even intersection with `q_1` exactly when it avoids support `1`.  Conversely the six roots of that `K_4` map to the three nonzero elements of a two-dimensional quotient subspace.  ∎

This sector is the precise `K_4`-complement/DDD rank-drop branch.  It must not be conflated with a graph separator.

## 6. Four scalar circuit partitions and side data

For each `lambda in Lambda_g`, the scalar subgraph `H_lambda` consists of:

- one terminal path component joining `1,2`, assigned side value `0`;
- one terminal path component joining `3,4`, assigned side value `1`;
- zero or more closed cycle components, whose side values may be chosen freely.

At an internal cubic vertex `v`, the three incident nonzero colours are the nonzero vectors of a two-dimensional subspace

\[
L_v\le V.
\]

### Lemma 6.1 — local affine extension

1. If `g notin L_v`, exactly one `lambda in Lambda_g` vanishes on all of `L_v`.  The other three scalar subgraphs pass through `v`.  Their three side values extend uniquely to an affine function
   \[
   f_v:\Lambda_g\to F_2.
   \]

2. If `g in L_v`, one incident edge has colour `g` and every scalar subgraph passes through `v`.  The four side values extend affinely if and only if
   \[
   \boxed{
   \bigoplus_{\lambda\in\Lambda_g} f_v(\lambda)=0.
   }
   \]

The second assertion uses the elementary identity

\[
\operatorname{Aff}(AG(2,2),F_2)
=
\{\text{four-bit words of even parity}\}.
\]

## 7. The quadratic touch-curvature class

Let

\[
E_g=\{e:c(e)=g\}.
\]

The `g`-edges form a matching.  For `e=uv in E_g`, every scalar subgraph contains `e`, so `u,v` lie in the same scalar component for every `lambda`.  The local parity defect is therefore the same at both endpoints.  Define

\[
\omega(e)
=
\bigoplus_{\lambda\in\Lambda_g}
 s_\lambda(e),
\]

where `s_lambda(e)` is the side value of the scalar component containing `e`.

Changing the chosen side value of a closed scalar component `C subset H_lambda` flips `omega(e)` exactly on the `g`-edges of `C`.  Put

\[
B=
\left\langle
1_{C\cap E_g}:
\lambda\in\Lambda_g,
\ C\text{ a closed component of }H_\lambda
\right\rangle
\le F_2^{E_g}.
\]

### Definition 7.1 — AG(2,2) touch curvature

\[
\boxed{
\Omega(c)=[\omega]\in F_2^{E_g}/B.
}
\]

This class is independent of all choices of side values on scalar cycles.

Equivalently, form the four-sheet touch hypergraph whose vertices are scalar components and whose hyperedge corresponding to `e in E_g` contains the four scalar components using `e`.  The terminal-path component values are fixed to `0,1`; `Omega(c)` is the obstruction to assigning values to the remaining component vertices so that every four-hyperedge has even parity.

A nonzero dual certificate is a set `S subset E_g` such that every closed scalar component meets `S` evenly, while the fixed terminal-side data have odd total pairing with `S`.

The local quotient

\[
\operatorname{Fun}(AG(2,2),F_2)
/
\operatorname{Aff}(AG(2,2),F_2)
\cong F_2
\]

is the unique quadratic bit at a `g`-edge.  This is the same one-dimensional representation type as the previously isolated DDD `D_8` affine class.  A canonical equality of the two global classes remains a next theorem, not an assumption.

## 8. Flat branch: the common affine side potential

### Theorem 8.1 — flat-potential equivalence

The following are equivalent.

1. `Omega(c)=0`.
2. Side values can be chosen on all closed scalar components so that every local side function is affine.
3. There exists a vertex potential
   \[
   p:V(Q)\to V
   \]
   with terminal values
   \[
   p(t_1)=p(t_2)=0,
   \qquad
   p(t_3)=p(t_4)=g,
   \]
   and, for every internal edge `e=uv`,
   \[
   \boxed{
   p(u)+p(v)\in\{0,c(e)+g\}.
   }
   \]

#### Proof

The first two statements are the definition of the curvature quotient.

Restriction gives an isomorphism

\[
V\xrightarrow{\sim}
\operatorname{Aff}(\Lambda_g,F_2),
\qquad
x\longmapsto(\lambda\mapsto\lambda(x)).
\]

Indeed both spaces have dimension three, and the four functionals in `Lambda_g` span `V^*`.  Hence every affine local side function has a unique representing vector `p(v)`.

If `e=uv` has colour `c`, then for every `lambda` with `lambda(c)=1`, the edge belongs to `H_lambda`, so the side values at `u,v` agree:

\[
\lambda(p(u)+p(v))=0.
\]

If `c=g`, this holds for all four `lambda`, forcing `p(u)=p(v)`.  If `c ne g`, the active functionals form an affine line.  The only affine functions vanishing on that line are zero and

\[
1+\lambda(c)=\lambda(g+c).
\]

Therefore

\[
p(u)+p(v)\in\{0,c+g\}.
\]

Conversely such a potential is constant on every active scalar component, and its terminal values force the required route-lock.  ∎

The flat branch is thus governed by an eight-state potential template.  Edges between distinct potential fibres have forced colour

\[
c(e)=p(u)+p(v)+g,
\]

and no edge joins antipodal potential values differing by `g`.  Repetition of a potential value alone is not yet a replacement theorem because same-fibre subgraphs may carry unbounded interior semantics.

## 9. Exact trust-boundary witnesses

Two explicit finite witnesses prevent overstatement.

### Witness A — route-lock need not imply a two-edge cut

There is an eight-vertex simple connected four-pole carrying a rank-two locked flow for which the minimum edge cut separating terminal pairs `12|34` has size four.  Its edge colours use only

\[
\{g,u,g+u\}.
\]

Thus the naive implication

\[
\text{route-lock}\Rightarrow\text{graph two-edge cut}
\]

is false.  This witness lies exactly in the `K_4` rank-drop sector of Theorem 5.1.

### Witness B — route-lock need not be flat

There is a ten-vertex simple connected four-pole carrying a full-rank locked flow with a single internal `g`-edge.  The four fixed side values on that edge are

\[
0100,
\]

which has odd parity.  There are no scalar cycle components available to change it.  Hence

\[
\Omega(c)\ne0.
\]

Thus the naive implication

\[
\text{route-lock}\Rightarrow\text{common affine potential}
\]

is also false.

Both witnesses are dependency-free exact verifier fixtures.

## 10. Updated mechanism diagram

For a blocked nondegenerate co-root atom:

\[
\boxed{
\begin{array}{c}
\text{two crossed root resolutions fail}
\\ \downarrow
\\
\text{all full challenges use the atom pairing}
\\ \downarrow
\\
K_{2,4}\text{ safe orbit}
\\ \downarrow
\\
\text{locked }F_2^3\text{-flow }(c,g)
\\ \downarrow
\\
\begin{cases}
\dim\langle c(E)\rangle=2:
&\text{K4/DDD rank-drop sector},\\
\dim\langle c(E)\rangle=3,\ \Omega(c)\ne0:
&\text{quadratic touch obstruction},\\
\dim\langle c(E)\rangle=3,\ \Omega(c)=0:
&\text{eight-state affine potential }p.
\end{cases}
\end{array}}
\]

This is the present composition interface.  It replaces the vague statement “both Petersen endpoint resolutions are blocked” by three exact algebraic-geometric outputs.

## 11. Relation with transition-matroid language

The scalar subgraphs `H_lambda` are circuit partitions with prescribed terminal components.  Their component incidence and the effect of changing closed-component side values are naturally touch-graph/transition-matroid data.  The combined four-sheet object is slightly richer than one ordinary touch graph because the same `g`-edge is incident with one component in each of four partitions.

Relevant established language includes transition systems, touch graphs, interlacement matrices, and isotropic-matroid connectivity.  No existing theorem has yet been identified that directly turns `Omega(c)` or the flat potential into the required five-support replacement theorem.

## 12. Next exact tasks

1. Identify the curvature quotient `Omega(c)` with a relative cycle/cut space of the combined touch object.
2. Prove that a nonzero curvature certificate yields a smaller transition-matroid split, a bounded DDD atom, or the unique physical `D_8` class.
3. Analyse the flat potential quotient on its eight values and formulate the exact finite interface carried by same-potential fibres.
4. Show that, outside the `K_4` rank-drop sector, either the potential template has a proper split or a repeated fibre is replaceable under enriched four-pole semantics.
5. Return to zero-equality leaves only after the co-root curvature/potential dichotomy is integrated into the forest-pruning theorem.
