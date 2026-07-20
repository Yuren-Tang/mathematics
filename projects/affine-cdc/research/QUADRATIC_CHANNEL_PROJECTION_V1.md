# Quadratic channel projection and repair-channel cohomology

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Canonical base:** `Yuren-Tang/mathematics:main@960c92b7ff231c78b387894149779083060a75eb`  
**Status:** branch-native exploratory mathematics; algebraic core at theorem level, physical composition frontier still open  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, release, DOI, arXiv submission, or the global five-support theorem.

This dossier consolidates the post-atom mechanism discovered after the route-locked DDD and defect-forest analysis. Its purpose is to preserve the exact mathematical core before corpus integration and proof-development decomposition. It also records one correction to an earlier issue-only checkpoint: the leaf/internal quadratic classification belongs canonically to the **fundamental-bond potential**, not always to a unique physical ambient value. Some leaf potentials have a root/co-root double fibre, which is precisely part of the DDD ambiguity.

---

## 1. Ambient quadratic space

Let

\[
E_5=\left\{x\in\mathbf F_2^5:\sum_{i=1}^5x_i=0\right\}.
\]

For an even-weight vector put

\[
q(x)=\frac{|x|}{2}\pmod 2.
\]

Thus

- `q(x)=1` exactly for the ten weight-two roots `R_5`;
- `q(x)=0` for `0` and the five weight-four co-roots.

Let

\[
b(x,y)=q(x+y)+q(x)+q(y)
\]

be the associated alternating bilinear form. In the `K_5` edge model, roots are edges and `b(r,s)=1` exactly when the corresponding edges meet.

Fix a root

\[
r=ab\in R_5.
\]

The six roots meeting `r` are

\[
S_r=\{ak,bk:k\in[5]\setminus\{a,b\}\}.
\]

They are the edge set of the complete bipartite graph

\[
K_r=K_{\{a,b\},\,[5]\setminus\{a,b\}}\cong K_{2,3}.
\]

These six roots are the canonical repair channels for a zero defect adjacent to two `r`-edges.

---

## 2. The quadratic channel projection

For `x in E_5` define its unsafe-channel word

\[
U_r(x)\in C^1(K_r;\mathbf F_2)
\]

by

\[
U_r(x)(s)=1_{\{x+s\notin R_5\}},\qquad s\in S_r.
\]

Equivalently,

\[
U_r(x)(s)=1+q(x+s)=q(x)+b(x,s).
\]

Identify `E_5` with the four-dimensional cut-potential space of `K_r`: for `p in E_5`,

\[
(\delta p)(ij)=p_i+p_j.
\]

Because the all-one vector is not in `E_5`, the map

\[
\delta:E_5\longrightarrow B^1(K_r;\mathbf F_2)
\]

is an isomorphism. Define the quadratic map

\[
\Psi_r(x)=x+q(x)r.
\]

### Theorem 2.1 — exact channel formula

For every `x in E_5`,

\[
\boxed{U_r(x)=\delta\Psi_r(x).}
\]

### Proof

For a channel `s in S_r`, `b(r,s)=1`, hence

\[
\delta\Psi_r(x)(s)
=b(x,s)+q(x)b(r,s)
=b(x,s)+q(x)
=U_r(x)(s).
\]

### Consequence 2.2 — every single-edge obstacle is a cut

The full six-channel obstruction caused by one physical edge value is always a cut of `K_{2,3}`. There is no arbitrary six-bit local obstacle alphabet.

---

## 3. Image, missing profiles, and singular fibres

The map `Psi_r:E_5 -> E_5` has twelve image points.

### Theorem 3.1 — image

\[
\boxed{
\operatorname{Im}\Psi_r
=E_5\setminus(R_5\cap r^\perp).
}
\]

The four missing potentials are

- `r` itself;
- the three roots disjoint from `r`.

After applying `delta`, the missing unsafe profiles are

- the full six-edge word `delta r = 1_{E(K_r)}`;
- the three nonzero four-cycles of `K_{2,3}`.

Thus the complete local defect of the quadratic projection consists of one full-curvature word and three cycle/triality words.

### Theorem 3.2 — fibres

There are exactly four non-singleton fibres:

\[
\boxed{\Psi_r^{-1}(0)=\{0,r\},}
\]

and, for each root `d` disjoint from `r`,

\[
\boxed{\Psi_r^{-1}(d+r)=\{d,d+r\}.}
\]

Here `d` is a root and `d+r` is a co-root. All other fibres are singletons.

### Mechanistic interpretation

- `0` and the root `r` are indistinguishable to the six repair channels: this is the zero/equality-wire ambiguity.
- For each of the three directions in `r^perp/<r>`, a crossed root and a co-root are indistinguishable: these are the three DDD root/co-root ambiguities.

The singular fibres therefore have no fifth local orbit beyond the zero class and the three DDD triality classes.

---

## 4. Local and regional curvature law

Suppose `x+y+z=0` at a cubic vertex. Then

\[
\Psi_r(x)+\Psi_r(y)+\Psi_r(z)
=(q(x)+q(y)+q(z))r
=b(x,y)r.
\]

Applying `delta` gives:

### Theorem 4.1 — local Gauss law

\[
\boxed{
U_r(x)+U_r(y)+U_r(z)
=b(x,y)\,\mathbf 1_{E(K_r)}.
}
\]

For a vertex set `X` in a physical graph carrying an `E_5` flow `lambda`, internal edges cancel and one obtains:

### Corollary 4.2 — regional Gauss law

\[
\boxed{
\bigtriangleup_{e\in\delta_G(X)}U_r(\lambda(e))
=\left(\sum_{v\in X}\kappa_r(v)\right)
\mathbf 1_{E(K_r)},
}
\]

where `kappa_r(v)=b(lambda(e_1),lambda(e_2))` for any two incident values at `v`.

Hence a closed region has only two possible total channel boundaries: zero or the full six-channel curvature word.

This is the same quadratic-polarisation mechanism as the hyperbolic norm-carrier identity, now expressed in the repair-channel quotient.

---

## 5. Safe-cycle exclusion and the six-channel leaf fan

Let `lambda:E(G)->E_5` be an `E_5` flow minimal in number of non-root edges within a class closed under cycle toggles. For a root `s`, define

\[
\operatorname{Safe}_s(\lambda)
=\{e:\lambda(e)+s\in R_5\}.
\]

If a binary cycle `D` is contained in `Safe_s(lambda)`, then

\[
\lambda'=\lambda+s1_D
\]

is again a flow, and every traversed edge is root-valued. Therefore:

### Theorem 5.1 — safe-cycle exclusion

If a defect edge `e` is repairable by `s`, then `e` is a bridge of the safe subgraph `Safe_s(lambda)`.

For a zero leaf with local values

\[
(0,r,r),
\]

all six `s in S_r` are repair channels. A safe cycle through the zero edge exits along one of the two `r`-edges and changes the local triple to a root triangle.

For a co-root one-factor leaf

\[
(q,r_1,r_2),\qquad q+r_1+r_2=0,
\]

there are six root coefficients `s` with `q+s` root:

- four ordinary safe-cycle channels;
- the two DDD crossed channels `r_1,r_2`.

Thus both singular leaf orbits carry a six-channel repair fan, but the co-root orbit splits into four cycle channels and two crossed-incidence channels.

---

## 6. The cap property of the six channels

The set `S_r=E(K_{2,3})` contains no three distinct elements summing to zero. In the `K_6` edge model, three nonzero vectors sum to zero only when the corresponding edges form a triangle or a perfect matching; `K_{2,3}` has neither a triangle nor a three-edge matching.

### Theorem 6.1 — monochromatic correction cycles

Let `eta:E(G)->S_r union {0}` satisfy the cubic flow equations. At every cubic vertex its incident values are either

\[
(0,0,0)
\]

or

\[
(0,s,s)
\]

for one `s in S_r`. Consequently, `eta` is a disjoint union of monochromatic cycles.

A genuine change from one repair channel to another must therefore leave the six-channel alphabet. The additional value is necessarily in the complementary root/co-root sector already represented by the DDD and defect mechanisms.

---

## 7. Minimal cut covers and the four-certificate bound

For each ambient value `x`, its unsafe set is the cut

\[
U_r(x)=\delta\Psi_r(x).
\]

Consider an inclusion-minimal family of cuts

\[
C_1,\ldots,C_m
\]

covering all edges of a connected graph `K`. Choose a private edge `e_i` belonging only to `C_i`. Writing `C_i=delta p_i`, define

\[
\Phi:V(K)\to\mathbf F_2^m,
\qquad
\Phi(v)=(p_1(v),\ldots,p_m(v)).
\]

Across `e_i`, the images differ by the `i`th basis vector. The private edges cannot contain a cycle, since summing around it would give a nonempty sum of distinct basis vectors equal to zero.

### Theorem 7.1 — cut-cover bound

\[
\boxed{m\le |V(K)|-1.}
\]

For `K=K_{2,3}` this gives

\[
\boxed{m\le4.}
\]

Thus every complete six-channel blockage has a certificate involving at most four physical edge values at coefficient level.

---

## 8. Maximal blockers and spanning trees

Suppose four cuts form an inclusion-minimal cover of `E(K_r)`. Their four private edges form a spanning tree `T` of `K_r`. Moreover, each cut is the fundamental bond of its private tree edge.

### Theorem 8.1 — maximal blocker classification

There is a bijection

\[
\boxed{
\{\text{minimal four-cut covers of }E(K_r)\}
\longleftrightarrow
\{\text{spanning trees of }K_r\},
}
\]

where a spanning tree is sent to its four fundamental bonds.

Under `Aut(K_{2,3})`, spanning trees have exactly two orbits:

1. a path `P_5`;
2. a subdivided claw with degree sequence `(3,2,1,1,1)`.

For a tree edge `e`, let `p_e in E_5` be the even representative of the vertex side of its fundamental bond. Then:

### Theorem 8.2 — quadratic type of the bond potential

\[
\boxed{
q(p_e)=
\begin{cases}
0,& e\text{ is a leaf edge of }T,\\
1,& e\text{ is an internal edge of }T.
\end{cases}}
\]

Indeed, deleting a leaf edge gives component sizes `1+4`, whose even side has size four; deleting an internal edge gives sizes `2+3`, whose even side has size two.

### Correction and trust boundary

The theorem concerns the cut **potential** `p_e`. A physical ambient value `x` satisfying `Psi_r(x)=p_e` need not be unique. In particular, some leaf potentials are among the root/co-root double fibres of Theorem 3.2. Therefore the path pattern

\[
0,1,1,0
\]

for the four bond potentials is an exact coefficient skeleton, but its direct identification with the physical Type-T routing-colour word `abba` remains a conjectural dictionary, not a theorem.

---

## 9. Flat shores from a channel spanning tree

Assume a flat channel profile: for every physical vertex `v`, its six-shore word `chi_v` is a cut of `K_r`. Choose a potential `P_v in E_5` with

\[
\chi_v=\delta P_v.
\]

Fix a spanning-tree basis `T` for the channel cut space and write

\[
P_v=\sum_{e\in E(T)}\theta_e(v)p_e.
\]

Define physical basis shores

\[
Y_e=\{v:\theta_e(v)=1\}.
\]

For a channel edge `s=uv in E(K_r)`, let `P_T(u,v)` be the unique tree path. Then:

### Theorem 9.1 — path reconstruction of the six shores

\[
\boxed{
X_s=\triangle_{e\in P_T(u,v)}Y_e.
}
\]

Thus the six canonical safe shores are generated by four physical cuts with the graphic path matrix of `T`. This is the precise four-cut coordinate system behind the flat branch.

The missing composition theorem must turn these four possibly crossing physical cuts into a serial replacement, a bounded four-pole, a smaller separator, or an augmenting cycle.

---

## 10. Channel cohomology and DDD triality

The channel graph has

\[
H^1(K_{2,3};\mathbf F_2)\cong\mathbf F_2^2.
\]

Its three nonzero cycles are the three four-cycles

\[
C_{cd},\quad C_{ce},\quad C_{de},
\]

with

\[
C_{cd}+C_{ce}+C_{de}=0.
\]

For a six-bit profile `chi`, define

\[
\varepsilon(\chi)
=(\langle\chi,C_{cd}\rangle,
  \langle\chi,C_{ce}\rangle,
  \langle\chi,C_{de}\rangle).
\]

Then

\[
\varepsilon(\chi)\in\{000,011,101,110\},
\]

and `epsilon(chi)=000` exactly when `chi` is a cut. The three nonzero words have one distinguished zero coordinate and are the canonical triality code expected for one bad route and two crossed routes.

### Status boundary

The algebraic identification

\[
H^1(K_{2,3};\mathbf F_2)^\times
\cong\{011,101,110\}
\]

is exact. Its lifting to an actual physical DDD incidence component requires the still-open relative-witness composition theorem.

---

## 11. Oriented route identifications and an index-two obstruction

Each of the three algebraic resolution classes

\[
\{ak,bk\},\qquad k\notin\{a,b\},
\]

has two orientations. Likewise each of the three perfect matchings on four terminals has two blocks. The full group of bijections preserving the three pair blocks is

\[
W=C_2^3\rtimes S_3,
\qquad |W|=48.
\]

Identify the six oriented terminal blocks with the six edges of `K_4`; the three matchings are the three pairs of opposite edges. The terminal relabelling group `S_4` acts faithfully on these six edges and embeds in `W`.

After orienting the three opposite-edge pairs, define

\[
\epsilon(\sigma;\epsilon_1,\epsilon_2,\epsilon_3)
=\epsilon_1+\epsilon_2+\epsilon_3.
\]

### Theorem 11.1 — oriented route exact sequence

\[
\boxed{
1\longrightarrow S_4
\longrightarrow C_2^3\rtimes S_3
\xrightarrow{\epsilon}C_2
\longrightarrow1.
}
\]

The even subgroup is exactly the image of terminal relabellings.

The eight transversals choosing one edge from each opposite pair split into four triangles and four stars. Even elements preserve the two classes; odd elements exchange them. In the `E_4` root model,

\[
\sum_{e\in\triangle}e=0,
\qquad
\sum_{e\in K_{1,3}}e=(1,1,1,1).
\]

Thus the unique local cokernel bit is represented by the weight-four co-root of `E_4`.

### Conditional global consequence

If a physical transition skeleton carries local oriented route identifications in `W`, their parity defines a `C_2`-valued one-cochain. Changing orientation conventions at states adds a coboundary, so the residual class lies in

\[
H^1(A;\mathbf F_2).
\]

Consequently a path skeleton has no residual parity class, while a triangle skeleton has at most one. This explains, conditionally on the lifting construction, why Type T should be holonomy-free and Type H should retain exactly one exceptional `C_2` class.

The existence and functorial compatibility of these local `W`-identifications on actual four-pole witnesses is not yet proved.

---

## 12. Binary fibre and minimum-defect forest

Fix all unsafe-channel words `U_r(lambda(e))`. On singleton fibres the edge value is determined. On each double fibre choose a baseline `bar lambda(e)` and write

\[
\lambda(e)=\bar\lambda(e)+\eta(e)r,
\qquad\eta(e)\in\mathbf F_2.
\]

At a vertex, conservation reduces to

\[
\sum_{e\ni v}\eta(e)=\rho(v),
\]

provided the baseline residual lies in `<r>`; otherwise the local relation is empty.

Hence the set of global lifts is either empty or an affine binary `T`-join space. Differences of two lifts are binary cycles. A minimum-defect lift is a minimum-weight `T`-join, and therefore its ambiguous support is a forest: any cycle could be removed without changing the boundary.

This gives a second derivation of the zero/co-root defect forest from the singular fibres of the channel projection.

For a connected component with terminal set `B`, the realizable boundary traces form either the empty set or an affine coset of

\[
\operatorname{Even}(B).
\]

In particular, a four-terminal ambiguous component has at most three bits of unresolved boundary parity, independent of its internal size. The remaining non-parity information is its route pairing, precisely the datum handled by the four-pole interface theory.

---

## 13. Current physical frontier

The finite algebraic layer is now sharply constrained. The next theorem should compare two physical repair witnesses and prove a strict alternative.

### Target 13.1 — relative-witness subtraction

For two repair witnesses in the same four-pole and active root direction `r`, construct their symmetric difference and decompose it into

\[
\boxed{
\text{root-valued relative Kempe subgraph}
+\text{binary }r\text{-fibre}.
}
\]

Desired consequences:

1. if the binary fibre is a boundary, push it to a smaller region or endpoint;
2. if it is a cycle with trivial parity, perform a Kempe/profile-expanding switch;
3. if it is a cycle with nontrivial parity, localise and contract a DDD `C_2` blossom;
4. if a resolution has no physical route, obtain an empty fibre/local relation and enter the defect branch.

### Target 13.2 — collision-or-progress

Let the three algebraic resolution classes be related to the three terminal matchings by physical witnesses. Prove that either

- the relation is the graph of a permutation;
- a root-valued augmentation/profile escape exists;
- a smaller separator or serial fragment exists;
- or a co-root/DDD blossom exists.

Only after this theorem may the index-two exact sequence of Section 11 be used as a complete physical lifting model.

### Target 13.3 — composition

After relation-to-connection is established:

- prove strict serial/nesting descent for the path spanning-tree orbit;
- prove that the branched orbit either escapes or reduces its unique binary holonomy to a composition-safe DDD/defect-forest unit;
- integrate these local reductions into the horizontal/global bad-flow induction.

---

## 14. Exact theorem versus mechanism ledger

### Exact in this dossier

- the formula `U_r=delta Psi_r`;
- image and fibre classification of `Psi_r`;
- local and regional Gauss laws;
- the cap property of `S_r`;
- safe-cycle exclusion under the stated minimality class;
- the cut-cover bound `m<=4`;
- maximal four-cut covers as spanning-tree fundamental bonds;
- the two spanning-tree orbits of `K_{2,3}`;
- the quadratic type of fundamental-bond potentials;
- reconstruction of six flat shores from four tree-basis cuts;
- the `H^1(K_{2,3})` triality code;
- the oriented-route group exact sequence;
- the binary `T`-join reduction after fixing channel profiles.

### Strong mechanism, not yet a complete physical theorem

- identification of the two channel-tree orbits with the complete Type T/Type H boundary automata;
- lifting nonzero channel cohomology to a physical DDD incidence component;
- asserting that every non-permutation resolution-route relation gives strict progress;
- composition-safe contraction of every nontrivial binary holonomy;
- replacement of the existing atom-localisation, forest-pruning, and four-pole-transfer modules by one master theorem;
- global five-support closure.

---

## 15. Governance and consumer route

This dossier is the branch-native durable source for the mechanism discovered in the late epoch-1 issue discussion and continued after rollover to `AC-RL-02` issue #41.

Recommended consumer sequence:

1. `AC-RL` continues Targets 13.1–13.3 on this branch;
2. `MATH-CUR` may consolidate the exact sections into the rolling corpus while preserving the open-arrow ledger;
3. `AC-PDL` should atomise the theorem chain after the physical statement surface stabilises;
4. independent review remains separate;
5. `AC-DIR` alone controls canonical disposition.
