# Flow--tension duality and the finite-state boundary of the five-CDC programme

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level linear duality and exact finite local classification; global finite-index completeness remains open  
**Parents:** `FIVE_CDC_INTERIOR_AFFINE_HOLONOMY_NORM_V1.md`, `FIVE_CDC_ROOT_ADMISSIBLE_LINEARIZATION_V1.md`, `FIVE_CDC_ROUTING_WEIGHT_HOLONOMY_V1.md`

## 1. Purpose

The current framework contains several finite local universes:

- ten support-unordered four-terminal states;
- three terminal matchings / routing directions;
- four rainbow support-permutation types;
- ten roots in `R_5`;
- edgewise root-admissibility forbidden-set sizes `0,1,1,6`.

Finite local data do not by themselves imply that the whole unbounded graph class can be checked by a finite census. This packet separates the exact finite layers from the still-unproved finite-index/completeness layer, and proves that the global root-admissible linearization problem is governed by an affine flow--tension duality.

The principal conclusions are:

1. the monodromy kernel dimensions are `2,1,1,0` for types `2^2 1, 4 1, 3 2, 5`;
2. for the singleton types `4 1` and `3 2`, every locally admissible edge has one forced bit or one free bit, so global feasibility is exactly partial binary-cycle extension;
3. failure of singleton extension is exactly an ordinary cut-parity certificate;
4. for type `2^2 1`, every local admissible set is either all of `F_2^2` or one affine line; global failure is exactly a three-direction `F_2^2`-tension certificate;
5. the three nonzero tension directions are the same `AG(2,2)` directions that index the three terminal matchings;
6. type `5` has no kernel freedom and is determined by the unique ambient conjugator plus edgewise root checks;
7. a finite exhaustive proof for the full programme would require a finite-index or bounded-representative theorem under gluing, or a bound on minimal counterexamples. Neither is currently proved.

No five-cycle double cover theorem is claimed.

## 2. General affine flow feasibility

Let `P` be a finite graph or four-pole with absolute cycle space

\[
Z_1(P;F_2).
\]

Let `K` be a finite-dimensional vector space over `F_2`. For every edge `e`, let the nonempty allowed set be an affine subspace

\[
A_e=a_e+L_e\subseteq K,
\]

where `L_e\le K`.

We seek

\[
c\in Z_1(P;F_2)\otimes K
\]

such that

\[
c(e)\in A_e
\qquad(e\in E(P)).
\]

Choose the representative chain `a=(a_e)_e` and put

\[
L=\bigoplus_e L_e\le K^{E(P)}.
\]

Then the problem is to find `l\in L` such that

\[
\partial(a+l)=0.
\]

## 3. Affine flow--tension duality

Write `K^*` for the dual vector space. A vertex potential

\[
q:V(P)\to K^*
\]

induces the tension

\[
\tau_q(uv)=q(u)+q(v)\in K^*.
\]

### Theorem 3.1 -- exact feasibility criterion

There exists a `K`-valued cycle `c` with `c(e)\in A_e` for every edge if and only if

\[
\sum_{e\in E(P)}\tau_q(e)(a_e)=0
\]

for every vertex potential `q` satisfying

\[
\tau_q(e)\in L_e^\perp
\qquad(e\in E(P)).
\]

Equivalently, infeasibility is certified by one potential `q` such that

\[
\tau_q(e)\in L_e^\perp
\quad\text{for all }e,
\]

and

\[
\boxed{
\sum_e\tau_q(e)(a_e)=1.
}
\]

#### Proof

The equation `\partial(a+l)=0` with `l\in L` is solvable exactly when `\partial a` belongs to `\partial L`. By finite-dimensional linear duality over `F_2`, this holds exactly when every covector `q` annihilating `\partial L` also annihilates `\partial a`.

Under the adjoint incidence map, `q` becomes the tension `\tau_q`. The condition that `q` annihilate `\partial L` is exactly the edgewise condition `\tau_q(e)\in L_e^\perp`; and

\[
\langle q,\partial a\rangle
=
\langle \tau_q,a\rangle
=
\sum_e\tau_q(e)(a_e).
\]

This gives the criterion. ∎

Thus every failure of global root-admissible linearization is a tension obstruction, not an unspecified nonlinear phenomenon.

## 4. Singleton monodromy types: ordinary cut certificates

For support-permutation types `4 1` and `3 2`, let

\[
Q_\pi=1+\pi.
\]

The exact `E_5` calculation gives

\[
\dim\ker Q_\pi=1.
\]

Let `k_\pi` generate the kernel. For a zero-norm interior defect `z`, choose a linear section of `Q_\pi` and obtain one cycle-valued solution `y_0`. Every ambient solution is

\[
\boxed{
y=y_0+c\otimes k_\pi,
\qquad
c\in Z_1(P;F_2).
}
\]

For each edge, root admissibility gives a set of allowed bits

\[
B_e\subseteq F_2.
\]

### Computational Theorem 4.1 -- local bit sets

For both types `4 1` and `3 2`, every locally admissible pair `(x(e),z(e))` has

\[
B_e\in\bigl\{\{0\},\{1\},F_2\bigr\}.
\]

For each current root `x`, among the seven locally admissible defect values:

- three give `B_e=F_2`;
- four give a singleton `B_e`.

The eighth ambient defect value is the previously classified forbidden value and gives `B_e=\varnothing`.

Exact dependency-free Wolfram enumeration verifies the statement. The distinction between forced `0` and forced `1` depends on the chosen section, but the forced/free partition does not.

Let `F` be the set of free edges and `J=E(P)\setminus F` the forced edges. Let `p_e` be the unique forced bit on `J`.

### Theorem 4.2 -- cut-extension criterion

The partial assignment `p` extends to a binary cycle

\[
c\in Z_1(P;F_2)
\]

if and only if, for every connected component `C` of the spanning subgraph `(V(P),F)`,

\[
\boxed{
\sum_{e\in\delta(C)}p_e=0.
}
\]

Equivalently, after contracting every free-edge component, the forced-one edges form an Eulerian subgraph.

#### Proof

A completion exists exactly when one can choose a chain `r` supported on `F` such that `\partial(p+r)=0`. On a connected component `C` of the free-edge graph, the incidence map of `F[C]` has image equal to the even-parity vertex vectors. Therefore the prescribed imbalance `\partial p` can be corrected inside `C` exactly when its total parity on `C` is zero. This total parity equals the number modulo two of forced-one edges crossing `\delta(C)`. ∎

### Corollary 4.3 -- exact minimal obstruction form

If singleton-type root-admissible linearization fails, there is a cut

\[
\delta(C)
\]

containing no free edge and an odd number of forced-one edges.

Thus the conjectured implication

\[
\text{avoidance failure}\Longrightarrow\text{cut certificate}
\]

is exact for types `4 1` and `3 2`.

## 5. Double-transposition type: affine lines and coloured tensions

For type `2^2 1`,

\[
K:=\ker Q_\pi\cong F_2^2.
\]

Every ambient solution differs from a chosen solution by a `K`-valued cycle.

### Computational Theorem 5.1 -- exact local allowed sets

For every current root and every ambient defect value, the root-admissible kernel-coordinate set is either

\[
K
\]

or one affine line in `K`.

All six affine lines occur. No empty set, singleton, or three-point set occurs.

Across the forty `(x,z)` cases there are:

- ten full-plane cases;
- thirty affine-line cases.

Exact dependency-free Wolfram enumeration verifies the statement.

Hence every constrained edge has

\[
A_e=a_e+L_e,
\qquad
\dim L_e=1,
\]

while a free edge has `L_e=K`.

Applying Theorem 3.1 gives the following exact obstruction.

### Corollary 5.2 -- three-direction tension certificate

Double-transposition root-admissible linearization fails if and only if there exists

\[
q:V(P)\to K^*\cong F_2^2
\]

such that:

1. `q(u)=q(v)` on every free edge `uv`;
2. on every affine-line constrained edge `e=uv`, the difference
   \[
   q(u)+q(v)
   \]
   is either zero or the unique nonzero functional annihilating the line direction `L_e`;
3. the affine parity is odd:
   \[
   \sum_e(q(u)+q(v))(a_e)=1.
   \]

The three nonzero elements of `K^*` are the three tension colours.

## 6. Return of `AG(2,2)` at the global dual level

The three nonzero elements of

\[
K^*\cong F_2^2
\]

are exactly the three directions of `AG(2,2)`.

Therefore the same three-direction geometry appears at three levels:

1. the three perfect matchings of four terminals;
2. the three routing conservation coordinates;
3. the three possible nonzero tension differences in a double-transposition infeasibility certificate.

This is a structural identification, not a numerical analogy:

\[
\boxed{
\text{terminal matching colour}
=
\text{routing conserved direction}
=
\text{global dual tension colour}.
}
\]

The tree-routing and rainbow-holonomy branches therefore meet in one flow--tension duality rather than requiring unrelated elimination arguments.

## 7. Complete monodromy-kernel ladder

The four support-permutation types now have the following exact global form:

\[
\begin{array}{c|c|c|c}
\text{type}
&\dim\ker(1+\pi)
&\text{local allowed geometry}
&\text{global obstruction}
\\
\hline
5
&0
&\text{unique conjugator; six forbidden values}
&\text{purely edgewise check}
\\
4 1
&1
&\text{forced/free bits}
&\text{ordinary cut parity}
\\
3 2
&1
&\text{forced/free bits}
&\text{ordinary cut parity}
\\
2^2 1
&2
&\text{full plane / affine line}
&F_2^2\text{-coloured tension}.
\end{array}
\]

The infinite shore size survives only through the graph carrying these tensions. The coefficient and local-constraint universes are completely finite.

## 8. What finiteness does and does not imply

### 8.1 Fixed finite graph

For every fixed graph, every flow, root lift, gauge fibre, reconfiguration graph, and constraint problem is finite and can in principle be exhaustively enumerated. This may be exponentially large and is not a proof for an unbounded graph class.

### 8.2 Fixed four-terminal static interface

The support-unordered boundary alphabet has ten states. A four-pole static cover profile is a subset of this alphabet, so there are at most

\[
2^{10}=1024
\]

static profiles. Equal profiles are indistinguishable under the exact four-cut gluing rule for static five-support cover existence.

Thus the static four-terminal interface has finite semantic index.

However, identifying all realizable profiles, or replacing every large shore by a bounded representative in a proof that also preserves reconfiguration and obstruction data, still requires a completeness theorem.

### 8.3 Full unbounded programme

Finite local alphabets do not by themselves imply a finite exhaustive proof of the five-CDC conjecture. A complete finite treatment would follow from any one of:

1. an explicit bound on the order of a minimal counterexample;
2. a finite-index gluing congruence for the enriched semantics, together with bounded representatives;
3. a decomposition theorem ensuring every large graph contains a bounded-boundary replaceable region;
4. a finite unavoidable set of reducible configurations.

None is presently known in the full framework.

Large cyclically highly connected cores and unbounded cycle-space dimensions remain possible. The new duality replaces several infinite searches by cut/tension theorems, but does not yet bound the size of a hypothetical counterexample.

## 9. Literature interfaces requiring audit

The following interfaces are mathematically relevant and should be audited before publication or claims of novelty.

1. **Group connectivity / flow choosability.** Prescribed edgewise forbidden values for group flows originate in the group-connectivity framework. Our affine-line constraints are not identical to avoiding one group element, but the methods and terminology are adjacent.
2. **Partial-flow extension.** Existing work studies when boundary or cut flow data extend to a whole graph and when failure yields contractions or exceptional configurations.
3. **Nowhere-zero flow reconfiguration.** Recent work studies cycle-supported transitions, reconfiguration connectivity, contractible subgraphs, and cubic reductions. The present root-valued `E_5` reconfiguration and holonomy should be compared carefully.
4. **Finite integer index and protrusion replacement.** This is the established algorithmic language for finite equivalence classes of boundaried graphs under gluing and replacement. It is a useful model for the missing finite-index theorem, though the present goal is structural rather than kernelization.
5. **Flow--tension and matroid duality.** Theorem 3.1 is elementary finite-dimensional duality, but its exact affine-line specialization and its integration with the four-terminal `AG(2,2)` routing geometry require a novelty check.
6. **Cyclic group cohomology and affine actions.** The norm-defect classification uses standard `H^1` of cyclic groups. The novelty, if any, lies in the chosen module and graph-theoretic application, not in the cohomology identity itself.

## 10. Next exact tasks

1. Translate each of the four rigid routing kernels into its induced coloured-tension data.
2. Determine whether every nonzero coloured-tension certificate forces:
   - a smaller cyclic edge cut;
   - a serial four-pole decomposition;
   - or a bounded replaceable fragment.
3. Add the forced/free and affine-line labels to the exact small-four-pole verifier.
4. Compare the new tension certificate with group connectivity and 2025--2026 flow-reconfiguration literature.
5. Formulate the enriched four-boundary equivalence relation needed for a genuine finite-index theorem, and test whether interior norm defects prevent finite index or disappear under gluing.
6. Do not launch larger graph censuses until one explicit certificate-to-decomposition conjecture has been fixed.
