# Mixed obstruction cores still form affine arrangements

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level fixed-flow structural result; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_FACE_TRANSITION_OBSTRUCTION_ARRANGEMENT_V1.md`, `FIVE_CDC_RENEWAL_SKELETON_AND_RESERVE_CODE_CENSUS_V1.md`, `FIVE_CDC_FLOWER_J5_MIXED_CORE_OBSTRUCTION_V1.md`

## 1. Purpose

The flower-snark witness introduced a mixed two-state fibre:

\[
K_3\vee C_5\text{-type obstruction}
\quad\longleftrightarrow\quad
K_6\text{-type obstruction}.
\]

This raises a structural question. Was the earlier affine-arrangement language special to marked cliques, or does it survive when obstruction species change?

The answer is:

\[
\boxed{
\text{every finite marked face-circuit certificate has an affine occurrence locus.}
}
\]

Consequently every finite library of clique, chromatic-link, or other marked dual certificates gives a finite affine-subspace arrangement over the fixed-flow gauge torsor.

Mixed-core renewal enlarges the certificate library but does not change the geometry of occurrence loci.

## 2. Fixed-flow gauge torsor

Fix a nowhere-zero Fano flow `f` and one compatible root lift `g`. Let

\[
B_f
\]

be the reduced gauge code. Gauge states are written

\[
g^\beta,
\qquad
\beta\in B_f.
\]

Every state determines a cycle-face embedding and a dual triangular cellulation.

A support face is represented by its exact source-edge circuit. This circuit identity is stronger than an abstract dual-vertex name and can be compared across gauge states.

## 3. Marked face-circuit configurations

A **marked face-circuit configuration** is a finite ordered family

\[
\mathcal C=(F_1,\ldots,F_m)
\]

of support face circuits occurring in one gauge state `g^\beta`, together with any finite data determined by those circuits, such as:

- which pairs share source edges;
- the multiplicity of each shared-edge adjacency;
- a selected subgraph of their dual adjacency graph;
- distinguished vertices, cycles, joins, or dominating cliques inside that graph.

Let

\[
Z_{\mathcal C}
\]

be the union of all source edges traversed by the marked face circuits, and let

\[
R_{\mathcal C}=E(G)\setminus Z_{\mathcal C}
\]

be the reserve.

## 4. Exact persistence theorem

### Theorem 4.1 — marked mixed-core occurrence locus

Let `\mathcal C` occur at gauge state `\beta`. The set of gauge states at which the same marked source-edge face circuits persist is

\[
\boxed{
A_{\mathcal C}
=
\beta+\left(B_f\cap\mathbf F_2^{R_{\mathcal C}}\right).
}
\]

In particular `A_{\mathcal C}` is an affine subspace of the gauge torsor.

All dual adjacency and edge-multiplicity data among the marked circuits remain unchanged throughout this locus.

#### Proof

A gauge word preserves one exact marked face circuit if and only if it vanishes on every source edge traversed by that circuit. For the whole family this condition is

\[
\lambda|_{Z_{\mathcal C}}=0.
\]

Equivalently,

\[
\operatorname{supp}\lambda\subseteq R_{\mathcal C}.
\]

Intersecting with the admissible gauge code gives the direction space

\[
B_f\cap\mathbf F_2^{R_{\mathcal C}}.
\]

If the marked circuits persist as the same source-edge circuits, every shared source edge and its multiplicity persists, so their complete weighted dual incidence data are fixed. ∎

### Corollary 4.2 — exact marked certificate persistence

Any obstruction certificate expressed solely through the weighted dual incidence data of `\mathcal C` persists on the same affine locus.

This includes marked realizations of:

- `K_6`;
- `K_r\vee H`;
- `K_3\vee C_{2k+1}`;
- the compatible `D_9` core;
- any finite target-link capacity violation with a specified set of face circuits.

## 5. Unmarked species are finite unions of cosets

Let `\mathscr P` be one finite dual-graph pattern or certificate type. In a fixed finite gauge fibre, there are only finitely many marked realizations

\[
\mathcal C_1,\ldots,\mathcal C_t
\]

of `\mathscr P` across all states.

### Theorem 5.1 — species occurrence arrangement

The set of states in which `\mathscr P` occurs is

\[
\boxed{
\operatorname{Occ}_f(\mathscr P)
=
\bigcup_{j=1}^t A_{\mathcal C_j},
}
\]

where every `A_{\mathcal C_j}` is an affine coset in `B_f`.

Hence every finite obstruction library

\[
\mathscr L=\{\mathscr P_1,\ldots,\mathscr P_s\}
\]

has total certified bad locus

\[
\boxed{
\operatorname{Bad}_f(\mathscr L)
=
\bigcup_{i=1}^s\operatorname{Occ}_f(\mathscr P_i),
}
\]

again a finite affine-subspace arrangement.

#### Proof

The fibre and every dual graph in it are finite. Enumerate all marked realizations and apply Theorem 4.1 to each. ∎

## 6. Application to the flower-snark mixed fibre

The displayed `J_5` witness has

\[
B_f\cong\mathbf F_2.
\]

One state contains a marked compatible `D_9` certificate, equivalently a marked

\[
K_3\vee C_5
\]

subgraph. The other contains a marked `K_6`.

Both certificates are private:

\[
A_{D_9}=\{0\},
\qquad
A_{K_6}=\{1\}
\]

up to choosing the origin of the gauge torsor.

Therefore the mixed obstruction arrangement is simply

\[
\boxed{
\{0\}\cup\{1\}=B_f.
}
\]

The species changes, but the renewal geometry is still a two-point affine cover.

## 7. What remains finite and what may be infinite

### Fixed-flow geometry

For every fixed finite graph and fixed Fano flow:

- the gauge torsor is finite;
- the collection of marked face circuits is finite;
- every finite certificate library produces a finite affine arrangement.

This part is closed.

### Global certificate library

Across arbitrary compatible dual triangulations, there may be infinitely many obstruction species. The exact dominating-clique theorem compresses all ranks two through five, but rank-one and non-dominating obstructions remain open.

Thus the unresolved infinity lies in discovering a complete structural certificate language, not in the geometry of a certificate once it is marked inside a gauge fibre.

## 8. Research consequence

The previous proposed replacement of affine arrangements by a more general obstruction sheaf is unnecessary at the fixed-flow level.

The correct architecture is:

\[
\boxed{
\text{finite or structured certificate library}
\quad+\quad
\text{affine occurrence arrangement over }B_f.
}
\]

The next tasks separate cleanly:

1. **target theory:** enlarge and compress the certificate library;
2. **gauge theory:** analyze whether the resulting affine cosets cover `B_f`;
3. **horizontal theory:** track how the library and arrangement change under connected-cycle flow switches.

## 9. Trust boundary

The marked-configuration persistence theorem follows from the exact face-circuit stabilizer condition. The finite-union statements are elementary consequences of finiteness.

No claim is made that the currently known certificate library is complete, that every non-homomorphism has a small dominating-clique witness, or that an affine arrangement from a complete library must leave an uncovered state.
