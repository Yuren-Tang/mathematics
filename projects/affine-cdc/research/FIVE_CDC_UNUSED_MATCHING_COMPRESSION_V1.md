# Compression from an unused matching of root labels

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level research checkpoint; not canonical pending review  
**Parent:** `FIVE_CDC_SOURCE_DEPENDENT_HALFCUBE_COMPRESSION_V1.md`

## 1. Setup

Let

\[
g:E(G)\longrightarrow E(K_8)
\]

be an AffineCDC root flow, and let `J_g⊆K_8` be its used-label graph. The
source-dependent half-cube theorem says that `g` compresses to five supports
whenever

\[
J_g\longrightarrow\mathscr A_5
\]

admits a graph homomorphism, where `\mathscr A_5` is the distance-two graph on
`F_2^5`.

## 2. Three unused independent roots

### Theorem 2.1 — unused-matching compression

Suppose the complement

\[
K_8-E(J_g)
\]

contains a matching of size three. Equivalently, there are three pairwise
vertex-disjoint root labels

\[
u_1v_1,\qquad u_2v_2,\qquad u_3v_3
\]

that never occur as values of `g`. Then `g` compresses to a five-support double
cover.

#### Proof

Choose a five-clique

\[
c_1,\ldots,c_5
\]

in `\mathscr A_5`; for example, take five distinct unit vectors in the odd
parity component. Assign

\[
a(u_i)=a(v_i)=c_i
\qquad(i=1,2,3)
\]

and assign the two remaining vertices of `K_8` to `c_4` and `c_5`.

The only pairs of source vertices receiving the same image are the three matched
pairs `u_iv_i`, and those pairs are nonedges of `J_g` by hypothesis. Every edge
of `J_g` therefore joins two distinct vertices of the chosen five-clique, hence
maps to an edge of `\mathscr A_5`. Thus

\[
a:J_g\to\mathscr A_5
\]

is a graph homomorphism. Apply the source-dependent compression theorem. ∎

At the support level, the construction identifies each unused pair of original
indices and replaces the corresponding two supports by their symmetric
difference. The other two indices remain separate.

## 3. A numerical consequence

### Corollary 3.1

If the root flow uses at most fourteen distinct `K_8` edge labels, then it
compresses to five supports.

#### Proof

The complement of `J_g` has at least

\[
28-14=14
\]

edges. A graph on eight vertices with matching number at most two has at most
thirteen edges. Indeed, the extremal matching bound gives

\[
\max\left\{\binom52,\binom22+2(8-2)\right\}
=
\max\{10,13\}
=13.
\]

Hence the complement contains a matching of size three, and Theorem 2.1 applies.
∎

An elementary proof of the thirteen-edge bound may be substituted: take a
maximal two-edge matching. Its four endpoints form a vertex cover of the graph;
optimizing the possible edges subject to the absence of a third disjoint edge
gives the same bound.

## 4. Small cubic graphs

A cubic graph on `n` vertices has `3n/2` edges, so a root flow uses at most
`3n/2` distinct root labels. Consequently:

### Corollary 4.1

Every AffineCDC root flow on a cubic graph with at most eight vertices compresses
to five supports.

This conclusion is about every root lift, not merely existence of some favourable
lift. It is not intended as a new small-order result about `5-CDC`; its value is
that it locates where a genuinely nontrivial root-label compression obstruction
can first occur.

For a ten-vertex cubic graph there are fifteen edges. Thus the unused-matching
criterion can fail only if essentially all fifteen edge occurrences carry
distinct root labels or if the complement's missing-label graph has unusually
small matching number.

## 5. Strategic meaning

Coordinate omission requires three unused **vertices** of `K_8`. The present
criterion requires only three unused pairwise-disjoint **edges**. It is therefore
substantially weaker and survives examples in which all eight original support
indices are active.

The remaining difficult case is very dense root-label usage:

\[
\nu(K_8-E(J_g))\leq2,
\]

where `\nu` denotes matching number. In that regime all unused root labels are
controlled by at most four coordinate vertices, and `J_g` contains a large dense
core. This is the first natural place to seek minimal half-cube compression
obstructions.

## 6. Next questions

1. Classify the edge-minimal subgraphs `J⊆K_8` that do not map to
   `\mathscr A_5`.
2. Determine whether every such obstruction contains `K_6` or the dense graph
   `K_8-C_5`.
3. Test whether the local triangle structure of cubic root flows forbids those
   dense obstruction graphs or permits them with controlled multiplicity.
4. Use Hamming-gauge moves to create an unused three-matching in the root-label
   complement.