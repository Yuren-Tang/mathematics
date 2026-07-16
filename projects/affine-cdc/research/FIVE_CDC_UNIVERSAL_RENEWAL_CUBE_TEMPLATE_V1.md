# The universal eight-state renewal-cube template

**Programme:** `AffineCDC — Research Lead`  
**Status:** exact finite computational evidence with theorem-level affine interpretation; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_RENEWAL_SKELETON_AND_RESERVE_CODE_CENSUS_V1.md`, `FIVE_CDC_ESSENTIAL_RENEWAL_QUOTIENT_V1.md`, `FIVE_CDC_GAUGE_PARTIAL_PETRIAL_CORRESPONDENCE_V1.md`

## 1. Purpose

The residual-neighbour census contains exactly five wholly bad fibres with three-dimensional reduced gauge code. Each fibre is an eight-state point-renewal system: every state contains exactly one private dual `K_6`.

This packet asks whether the five fibres represent five different obstruction mechanisms or repeated realizations of one mechanism.

The exact answer at the weighted-dual level is:

\[
\boxed{
\text{all five fibres realize one universal affine eight-state template.}
}
\]

The statement concerns weighted dual one-skeletons: vertices are support-cycle faces, and the multiplicity of a dual edge is the number of source edges shared by the two faces. It does not identify the complete rotation systems or assert equivalence of the underlying Fano flows.

## 2. Weighted dual type

For a root lift `g`, let

\[
D_g
\]

be the weighted graph whose vertices are the support-cycle components and whose edge multiplicity between two vertices is the number of source edges incident with the corresponding two faces.

The simple support of `D_g` is the graph used in the componentwise half-cube test

\[
T_g^{(1)}\longrightarrow\mathscr A_5.
\]

The weights retain more of the cycle-face embedding than the simple graph, while still forgetting the cyclic rotation data at dual vertices.

Two gauge states have the same **weighted dual type** when their weighted graphs `D_g` are isomorphic.

## 3. Exact eight-type theorem

### Computational Theorem 3.1

Across the five three-dimensional residual fibres:

1. there are forty gauge states in total;
2. their weighted dual graphs fall into exactly eight isomorphism classes;
3. every one of the five fibres contains each of the eight classes exactly once.

Thus, for each fibre `f`, the state-to-type map

\[
\Theta_f:\mathbf F_2^3\longrightarrow\{\mathsf T_0,\ldots,\mathsf T_7\}
\]

is a bijection.

Choose the class labels so that the first fibre has

\[
\Theta_0(q)=\mathsf T_q.
\]

For every other fibre there is an affine automorphism

\[
\alpha_f\in\operatorname{AGL}(3,2)
\]

such that

\[
\boxed{
\Theta_f(q)=\Theta_0(\alpha_f(q)).
}
\]

Hence the five weighted-dual renewal systems are affinely equivalent.

### Proof status

This is an exact finite computation. Weighted graph isomorphism is checked by a dependency-free backtracking verifier, and the resulting state permutations are checked directly against the affine law

\[
\alpha(x+y)+\alpha(0)
=
\alpha(x)+\alpha(y).
\]

No heuristic graph hash is used.

## 4. Topological-size profile

Every universal cube has the same number-of-faces profile:

\[
\begin{array}{c|c}
\text{number of support-cycle faces}&\text{cube states}\\
\hline
10&3\\
11&3\\
12&2
\end{array}
\]

Since the source graph has

\[
|V|=30,
\qquad
|E|=45,
\]

the corresponding surface Euler characteristics are

\[
\chi=F-15,
\]

namely

\[
-5,-4,-3.
\]

Thus the partial-Petrial cube moves among three adjacent Euler-characteristic levels. The profile is a `3+3+2` partition of the affine cube.

Relative to one reference affine labelling, the three level sets are

\[
\begin{aligned}
F=10&:\{0,1,2\},\\
F=11&:\{3,5,6\},\\
F=12&:\{4,7\}.
\end{aligned}
\]

The first two are affine two-flats with one point removed; the last is an affine line. Under another fibre these sets are transported by the corresponding affine state relabelling.

The displayed coordinates are template coordinates, not intrinsic Fano colour names.

## 5. Reserve profile

Each state has one private marked `K_6`. Let `R_q` be the reserve outside its six face zones.

Every universal cube has

\[
\begin{array}{c|c}
|R_q|&\text{cube states}\\
\hline
1&5\\
3&3.
\end{array}
\]

In template coordinates, the three reserve-three states are

\[
\{3,4,7\}.
\]

They are the three points of the affine two-flat

\[
\{0,3,4,7\}
\]

other than zero. Equivalently, the reserve-three states form an affine triangle: a two-flat with one point deleted.

The same affine pattern occurs in every fibre after state relabelling.

The weighted reserve graphs have the following forms:

- the five reserve-one states have one dual edge among the vertices outside the `K_6`, together with isolated outside vertices;
- among the three reserve-three states, two have a triangle as outside induced graph and one has a four-vertex path, together with isolated outside vertices.

Consequently the eight weighted dual types split as:

\[
\begin{array}{c|c|c}
\text{face count}&\text{reserve graph}&\text{types}\\
\hline
10&K_2\text{ plus isolates}&3\\
11&K_2\text{ plus isolates}&2\\
11&K_3\text{ plus isolates}&1\\
12&K_3\text{ plus isolates}&1\\
12&P_4\text{ plus isolates}&1
\end{array}
\]

The reserve graph and face count do not alone distinguish all eight types; the attachments between the outside vertices and the six clique faces carry the remaining information.

## 6. Gauge-code profile

Every universal cube has the same nonzero gauge-word weight multiset:

\[
\boxed{
6,12,14,18,24,24,26.
}
\]

The unique minimum-weight word has harmonic cut quotient

\[
2K_3.
\]

Every marked clique reserve has size one or three, so

\[
|R_q|<6=d(B_f).
\]

The reserve-shortened-code theorem therefore forces every marked clique to be private.

The universal cube can consequently be read as follows:

1. the `2K_3` circuit and its linear combinations generate an eight-state Petrial orbit;
2. every old almost-global clique is destroyed by every nonzero move;
3. every new state carries a different almost-global clique;
4. the resulting weighted dual type is determined by the affine cube state.

## 7. Renewal representation

The universal template gives an injective representation

\[
\Theta:\mathbf F_2^3\hookrightarrow\mathcal D,
\]

where `\mathcal D` denotes weighted-dual isomorphism types.

Since `\Theta` is bijective onto eight types, the gauge torsor is not merely a parameter space for repeated copies of one bad graph. Every affine state has its own weighted dual type.

At the same time, the five separate residual fibres induce the same representation up to `\operatorname{AGL}(3,2)`. Thus the obstruction dynamics is more stable than the individual switched-flow presentation.

This is the first exact evidence for a reusable **renewal atom**:

\[
\boxed{
\text{different horizontal flow states}
\quad\rightsquigarrow\quad
\text{the same affine Petrial obstruction module}.
}
\]

## 8. Mechanism significance

The result changes the interpretation of the five highest-dimensional residual examples.

They are not evidence for uncontrolled diversity. Instead they suggest that a small number of affine renewal modules may govern the persistent region of the flow-reconfiguration graph.

The current module has:

- state space `\mathbf F_2^3`;
- one private `K_6` per state;
- eight pairwise nonisomorphic weighted dual types;
- minimum harmonic circuit `2K_3`;
- reserve sizes one and three in an affine `5+3` pattern;
- surface face counts in an affine `3+3+2` pattern.

This is a considerably sharper object than the original statement that five fibres of size eight remain bad.

## 9. Existing mechanism and surviving obstruction

### What is now explained

- **Why every old clique dies:** every reserve is smaller than the gauge-code distance.
- **Why the fibre nevertheless remains bad:** the state-to-core map is a bijection.
- **Why the five examples look alike:** their weighted-dual renewal representations are affinely equivalent.
- **Why affine geometry persists:** gauge composition is addition in `\mathbf F_2^3`, and the topological type partition is transported by affine automorphisms.

### What remains unexplained

- why the `2K_3` circuit forces exactly these eight weighted dual types;
- why the face-count and reserve partitions have the displayed affine shapes;
- whether the full rotation systems, not merely weighted dual graphs, also form one universal template;
- how one connected-cycle switch transforms or destroys this renewal module;
- whether every occurrence of this module forces a graph decomposition or admits a bounded horizontal escape.

## 10. Next theorem target

The next structural target is an explicit transition theorem for the universal cube.

One seeks three topological or code-theoretic binary invariants

\[
I_1(D_g),\ I_2(D_g),\ I_3(D_g)
\]

that recover the affine state

\[
q=(I_1,I_2,I_3)
\]

without referring to the arbitrary gauge basis.

A successful intrinsic coordinate system would turn the finite template into a theorem-level local model. It would also make it possible to compute how a horizontal connected-cycle switch acts on the renewal cube and to prove one of:

\[
\boxed{
\text{the cube is broken and an uncovered state appears}
}
\]

or

\[
\boxed{
\text{the cube persists and supplies a canonical decomposition interface}.
}
\]

## 11. Trust boundary

The eight weighted-dual classes, their one-per-fibre occurrence, the affine equivalence of the five state labellings, and the face/reserve profiles are exact finite computational results.

The interpretation as a universal renewal atom is a programme-level inference from those exact facts.

No statement here proves equivalence of the five Fano flows, equality of full surface rotation systems, horizontal escapability of the cube, or the five-cycle double cover conjecture.
