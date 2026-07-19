# AC-PD-A3 — binary eight-flow external boundary and equal-order transport

**Proof-development state:** `COMPLETE-DRAFT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Depends on:** `AC-PD-A0`, `AC-PD-A1`, `AC-PD-A2`  
**Immediate consumers:** `AC-PD-A4`, `AC-PD-A10`  
**External mathematical input:** Seymour's nowhere-zero six-flow theorem only

## 0. Result and dependency boundary

Let `G` be a finite loopless multigraph with no singleton cut. Then `G` has a nowhere-zero flow with values in

\[
\Gamma_3:=\mathbf F_2^3.
\]

Equivalently, there is a map

\[
f:E(G)\longrightarrow \Gamma_3\setminus\{0\}
\]

such that at every vertex

\[
\sum_{e\ni v}f(e)=0.
\]

No orientation appears in the final formula because `-x=x` in `\Gamma_3` and the graph is loopless.

The sole non-elementary input is Seymour's theorem that every finite graph without an isthmus has a nowhere-zero integral six-flow. The remaining steps are proved here:

1. disconnected and isolated-vertex reduction;
2. literal inclusion of a six-flow in the class of eight-flows;
3. reduction of an integral eight-flow modulo eight;
4. an internal proof that the number of nowhere-zero flows over a finite abelian group depends only on the order of the group;
5. transfer from `\mathbf Z/8\mathbf Z` to `\mathbf F_2^3`;
6. orientation forgetting in characteristic two.

Thus Tutte's equal-order theorem is retained as historical provenance but is not an opaque logical premise.

## 1. Oriented group flows

Let `G=(V,E)` be a finite loopless multigraph. Parallel edge objects are distinct. Fix an arbitrary orientation of every edge. For an abelian group `A`, define the boundary homomorphism

\[
\partial_A:A^E\longrightarrow A^V
\]

by

\[
(\partial_Ax)(v)
=
\sum_{e\text{ entering }v}x_e
-
\sum_{e\text{ leaving }v}x_e.
\]

An **`A`-flow** is an element of `\ker\partial_A`. It is **nowhere-zero** when `x_e\ne0` for every edge.

### Proposition 1.1 — orientation independence

Existence and number of nowhere-zero `A`-flows do not depend on the chosen orientation.

#### Proof

Reversing one edge and replacing its coordinate `x_e` by `-x_e` is a bijection between the two flow kernels and preserves nonzeroness. Compose these bijections for all reversed edges. ∎

### Proposition 1.2 — isolated vertices are inert

Deleting or adjoining isolated vertices changes neither the flow kernel nor the nowhere-zero flow set.

#### Proof

An isolated vertex contributes one identically zero coordinate to the target `A^V` and no edge coordinate to the source. ∎

Hence a finite-active-edge graph with an arbitrary isolated ambient carrier may first be replaced by its finite active vertex subgraph.

## 2. Componentwise assembly

Let `G_1,\dots,G_r` be the edge-bearing connected components of `G`.

### Proposition 2.1 — flow product decomposition

Restriction gives a canonical bijection

\[
\operatorname{Flow}_A(G)
\cong
\prod_{j=1}^r\operatorname{Flow}_A(G_j),
\]

and this restricts to a bijection on nowhere-zero flows.

#### Proof

Every edge and every nontrivial boundary equation belongs to one component. Thus the boundary map is the direct product of the component boundary maps. Nonzeroness is coordinatewise. ∎

### Corollary 2.2 — componentwise bridgelessness

If `G` has no singleton cut, every edge-bearing component has no isthmus. Conversely, if each edge-bearing component has no isthmus, then `G` has no singleton cut.

This is A0's bridge/singleton-cut equivalence applied componentwise.

## 3. External theorem: Seymour six-flow

### External Theorem 3.1 — Seymour, 1981

Every finite graph with no isthmus has a nowhere-zero integral six-flow: after choosing an orientation, there is

\[
z:E(G)\longrightarrow\mathbf Z
\]

such that

\[
\partial_{\mathbf Z}z=0,
\qquad
z_e\in\{\pm1,\pm2,\pm3,\pm4,\pm5\}
\]

for every edge.

**Primary source.** P. D. Seymour, “Nowhere-zero 6-flows”, *Journal of Combinatorial Theory, Series B* **30** (1981), 130–135, DOI `10.1016/0095-8956(81)90058-7`. The article abstract states exactly that every graph with no isthmus admits such a circulation with values `±1,...,±5`.

**Accessible independent proof.** M. DeVos, E. Rollová, R. Šámal, “A new proof of Seymour's 6-flow theorem”, *Journal of Combinatorial Theory, Series B* **122** (2017), 187–195; arXiv `1512.06214`.

If one reads Seymour's statement as connected, Proposition 2.1 applies it independently to the edge-bearing components. The empty graph has the unique empty flow.

## 4. Six-flow to integral eight-flow

### Proposition 4.1 — literal range inclusion

Every nowhere-zero integral six-flow is a nowhere-zero integral eight-flow.

#### Proof

An integral `k`-flow has values `z_e` satisfying

\[
0<|z_e|<k.
\]

The six-flow inequalities `0<|z_e|<6` imply `0<|z_e|<8` without changing orientation, values, or conservation equations. ∎

This step is an inclusion of value ranges, not an invocation of a second flow theorem.

## 5. Integral eight-flow to a `\mathbf Z/8\mathbf Z`-flow

Let

\[
\rho:\mathbf Z\longrightarrow\mathbf Z/8\mathbf Z
\]

be reduction modulo eight.

### Proposition 5.1 — modular reduction

If `z` is a nowhere-zero integral eight-flow, then

\[
\bar z_e:=\rho(z_e)
\]

is a nowhere-zero `\mathbf Z/8\mathbf Z`-flow.

#### Proof

Since `\rho` is a homomorphism,

\[
\partial_{\mathbf Z/8\mathbf Z}\bar z
=
\rho(\partial_{\mathbf Z}z)
=0.
\]

Moreover `0<|z_e|<8`, so no `z_e` is divisible by eight. Hence `\bar z_e\ne0`. ∎

## 6. Flow-kernel count over an arbitrary finite abelian group

The next theorem internally proves the equal-order transport needed here.

For `B\subseteq E`, let `G[B]` be the spanning subgraph with vertex set `V` and edge set `B`. Let

\[
c(B)
\]

be the number of connected components of `G[B]`, including isolated vertices. Put

\[
\beta(B):=|B|-|V|+c(B).
\]

This is the cycle rank of the spanning subgraph.

### Theorem 6.1 — flow-kernel cardinality

For every finite abelian group `A` and every `B\subseteq E`,

\[
\boxed{
|\ker(\partial_A:A^B\to A^V)|
=
|A|^{\beta(B)}.
}
\]

#### Proof

Choose a spanning forest `T\subseteq B`, one spanning tree in every nontrivial component and no edge in an isolated component. Then

\[
|T|=|V|-c(B),
\qquad
|B\setminus T|=\beta(B).
\]

We show that restriction to the chord set is a bijection

\[
\ker\partial_A
\longrightarrow
A^{B\setminus T}.
\]

Assign arbitrary values to the chord edges `B\setminus T`. In each tree component, solve the conservation equations from leaves inward. At a leaf, the value on the unique remaining tree edge is forced uniquely by the already assigned incident values. Delete that leaf and continue. After all non-root vertices are removed, the root equation holds automatically because the sum of all vertex boundaries in a component is zero: every oriented edge contributes once with each sign. Thus every chord assignment extends uniquely to a flow.

Conversely, a flow is determined by its chord values by the same leaf elimination. Hence the flow group is in bijection with `A^{B\setminus T}` and has cardinality `|A|^{\beta(B)}`. Parallel edges cause no change; they are distinct coordinates and may be tree edges or chords. ∎

### Remark 6.2 — loops

The present theorem is applied only to the loopless core. If loops were allowed in the standard oriented boundary convention, each loop would contribute a free `A`-coordinate and the same formula would remain valid when loops count as cycle-rank edges. This does not license the companion once-per-edge incidence convention across loops.

## 7. Inclusion–exclusion and equal-order transport

Let

\[
N_G(A)
\]

be the number of nowhere-zero `A`-flows on `G`.

### Theorem 7.1 — explicit flow-count formula

For every finite abelian group `A`,

\[
\boxed{
N_G(A)
=
\sum_{B\subseteq E}
(-1)^{|E|-|B|}
|A|^{|B|-|V|+c(B)}.
}
\]

#### Proof

For each edge `e`, let `Z_e` be the set of flows whose `e`-coordinate is zero. Inclusion–exclusion gives

\[
N_G(A)
=
\sum_{S\subseteq E}(-1)^{|S|}
\left|\bigcap_{e\in S}Z_e\right|.
\]

A flow in the intersection is exactly a flow supported on `B=E\setminus S`. By Theorem 6.1 its number is

\[
|A|^{|B|-|V|+c(B)}.
\]

Substitute `|S|=|E|-|B|`. ∎

### Corollary 7.2 — dependence only on group order

If finite abelian groups `A` and `A'` have equal order, then

\[
N_G(A)=N_G(A').
\]

In particular, `G` has a nowhere-zero `A`-flow if and only if it has a nowhere-zero `A'`-flow.

#### Proof

The formula in Theorem 7.1 contains `A` only through `|A|`. Existence is equivalent to the positive integer count being nonzero. ∎

### Historical provenance

The equal-order existence theorem is classically due to Tutte; a precise modern statement appears as Theorem 1.1 in B. Litjens, “On dihedral flows in embedded graphs”, *Journal of Graph Theory* **91** (2019), 174–191, at p. 174. Litjens cites W. T. Tutte, “On the imbedding of linear graphs in surfaces”, *Proceedings of the London Mathematical Society* (2) **51** (1949), 474–483, DOI `10.1112/plms/s2-51.6.474`.

The stronger counting statement is represented by the flow polynomial. Tutte's paper “A contribution to the theory of chromatic polynomials”, *Canadian Journal of Mathematics* **6** (1954), 80–91, DOI `10.4153/CJM-1954-010-9`, defines oriented colour-cycles and their count on pp. 81–83 and develops the deletion–contraction polynomial framework thereafter. Modern literature states the arbitrary finite-abelian-group formulation explicitly.

These citations establish provenance. The logical proof used by this dossier is Theorems 6.1 and 7.1 above, so the historical primary-page localization is not an unproved dependency.

## 8. Transfer to `\mathbf F_2^3`

The groups

\[
\mathbf Z/8\mathbf Z
\qquad\text{and}\qquad
\mathbf F_2^3
\]

both have order eight.

### Theorem 8.1 — binary eight-flow

Every finite loopless multigraph with no singleton cut has a nowhere-zero `\mathbf F_2^3`-flow in the oriented sense.

#### Proof

Apply Seymour componentwise to obtain a nowhere-zero integral six-flow. By Proposition 4.1 it is an integral eight-flow. By Proposition 5.1 it reduces to a nowhere-zero `\mathbf Z/8\mathbf Z`-flow. Corollary 7.2 transfers existence to `\mathbf F_2^3`. ∎

This proves exactly the external boundary named `BinaryEightFlow` in the current AffineCDC architecture.

## 9. Orientation forgetting in characteristic two

Let `f:E(G)\to\mathbf F_2^3` be an oriented flow. At a vertex `v`, conservation says

\[
\sum_{e\text{ entering }v}f(e)
-
\sum_{e\text{ leaving }v}f(e)=0.
\]

Since `-x=x` in characteristic two, this is equivalent to

\[
\boxed{
\sum_{e\ni v}f(e)=0.
}
\]

Because `G` is loopless, every incident edge object occurs exactly once in this sum.

### Proposition 9.1 — exact adapter

On a loopless multigraph, oriented `\mathbf F_2^3`-flows are canonically identical to maps

\[
f:E(G)\to\mathbf F_2^3
\]

whose once-per-edge incidence sum is zero at each vertex. Nowhere-zero status is unchanged.

#### Proof

The equations above are termwise identical after replacing every minus sign by plus. Orientation choices disappear without changing edge coordinates. ∎

### Boundary warning

For a loop in the standard oriented boundary map, the two endpoint occurrences cancel. In a once-per-edge incidence set, a loop would appear once. Therefore looplessness is an exact hypothesis of this representation adapter, not of ordinary group-flow theory itself. A1 supplies the loopless core before A3 is invoked.

## 10. Degenerate and representation cases

### Empty graph

The empty edge assignment is a nowhere-zero flow vacuously. The inclusion–exclusion formula gives `N_G(A)=1`.

### Isolated vertices

They impose only zero equations and may be discarded before applying Seymour or counting flows.

### Disconnected graph

Seymour is applied componentwise if necessary, and the component flows concatenate. The counting formula also factors, consistently with Proposition 2.1.

### Parallel edges

They are distinct flow coordinates. Neither Seymour's statement, the spanning-forest proof, nor the characteristic-two adapter identifies them.

### Loops

They were deleted in A1. No loop-dependent convention enters the `BinaryEightFlow` interface.

## 11. Exported interface

Downstream units may cite:

1. every finite loopless no-singleton-cut multigraph has a nowhere-zero `\mathbf F_2^3`-flow;
2. the result is componentwise and unaffected by isolated vertices;
3. the final flow may be represented without orientation as a once-per-edge incidence sum because the coefficient group has exponent two and the graph is loopless;
4. Seymour's six-flow theorem is the sole external mathematical existence premise;
5. six-to-eight is literal range inclusion;
6. reduction modulo eight produces a nowhere-zero `\mathbf Z/8\mathbf Z`-flow;
7. equal-order finite-abelian-group flow existence and counting follow from the internal formula in Theorem 7.1;
8. existence and counting provenance are recorded separately.

## 12. Corpus correction and assurance assessment

The baseline correctly isolated `BinaryEightFlow` and warned that Seymour must be applied componentwise, `6 -> 8` is only range inclusion, the orientation-forgetting adapter is loopless, and Tutte existence must not be conflated with counting.

This dossier strengthens the baseline boundary by proving the equal-order group transfer internally. Consequently, the previously recorded uncertainty about an exact primary Tutte page is no longer a logical blocker. It remains a bibliographic refinement only.

`AC-PD-A3` is `COMPLETE-DRAFT`. The next dependency-respecting unit is `AC-PD-A4`: the affine incidence space, local affine torsor, edge diagonal, pair complex, obstruction class, quotient-sheaf presentation, stress dual, and exact retention boundary back to graph/dart data.
