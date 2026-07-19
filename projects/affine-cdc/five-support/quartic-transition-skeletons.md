# Pairwise transition skeletons of quartic cores

## 1. Purpose

A quartic witness design consists of four near-resolutions of a set

$$
X,
\qquad
|X|=4k+1,
$$

with one omitted point in each sheet and `4k` independent four-element block vectors.

The quotient Tait-phase theorem adds physical relations among the four sheets, but before using quotient colours one can extract one further exact consequence of the basis condition.  Any two near-resolutions determine a connected bipartite transition skeleton with two terminal leaves.  Thus a pair of scalar sheets cannot split into unrelated marked regions.

## 2. The pairwise incidence graph

Fix distinct sheets `i` and `j`.  Let

$$
\mathcal R_i,
\qquad
\mathcal R_j
$$

be their near-resolutions, omitting the distinct points

$$
e_i,
\qquad
e_j.
$$

Define the bipartite multigraph

$$
T_{ij}
$$

as follows.

Its vertices are

$$
\mathcal R_i
\sqcup
\mathcal R_j
\sqcup
\{s_i,s_j\},
$$

where `s_i` lies on the `i` side and `s_j` lies on the `j` side.

Every point `x\in X` gives one edge:

- on the `i` side, use the unique block of `\mathcal R_i` containing `x`, unless `x=e_i`, in which case use `s_i`;
- on the `j` side, use the unique block of `\mathcal R_j` containing `x`, unless `x=e_j`, in which case use `s_j`.

Thus the edges of `T_{ij}` are canonically indexed by the witness points `X`.

Every block vertex has degree four, and the two terminal vertices have degree one.

## 3. Connectedness

### Theorem 3.1 — connected transition skeleton

For every pair of distinct sheets `i,j`, the graph `T_{ij}` is connected.

#### Proof

Suppose first that `C` is a connected component of `T_{ij}` containing neither terminal vertex.  Sum, over `\mathbf F_2`, the incidence vectors of all block vertices in `C`.

Every point-edge belonging to `C` has both of its block endpoints in `C`, so its coordinate occurs twice in the sum.  No point-edge leaves `C`.  Hence the sum is zero.

This is a nonempty linear relation among block incidence vectors from `\mathcal R_i\cup\mathcal R_j`.  Those vectors are a subset of the full `4k`-element basis and are therefore independent.  Thus no terminal-free component exists.

Consequently every component contains at least one of `s_i,s_j`, so there are at most two components.  If there were two, each would contain exactly one terminal vertex.  But all block vertices have even degree four, while that component would contain exactly one odd-degree vertex, its terminal leaf.  This contradicts the handshaking lemma.  Therefore one component contains both terminal vertices and all block vertices.  The graph is connected.  ∎

### Corollary 3.2 — exact size and cycle rank

The graph `T_{ij}` has

$$
|V(T_{ij})|=2k+2,
\qquad
|E(T_{ij})|=4k+1.
$$

Its binary cycle rank is

$$
\boxed{
\beta_1(T_{ij})
=
|E|-|V|+1
=
2k.
}
$$

### Corollary 3.3 — terminal Euler trail

The only odd-degree vertices of `T_{ij}` are `s_i` and `s_j`.  Hence `T_{ij}` admits an Euler trail from `s_i` to `s_j` traversing every witness edge exactly once.

After deleting the two terminal leaves and their incident edges, one obtains a connected bipartite core with:

- `2k` block vertices;
- `4k-1` edges;
- two vertices of degree three;
- all other vertices of degree four;
- the same cycle rank `2k`.

## 4. Physical interpretation

For a physical quartic common-cut core, take two scalar sheets

$$
H_\phi,
\qquad
H_\psi.
$$

Then:

- the block vertices of `T_{\phi\psi}` are the closed scalar components meeting the witness;
- the two terminal vertices represent the terminal component in the two sheets;
- each edge is one witness `g`-edge;
- the four incident witness edges at a block vertex inherit a cyclic order from the corresponding scalar circuit.

Therefore the physical object is not merely a connected bipartite multigraph.  It is a connected **ribbon transition skeleton** with two terminal leaves.

The quotient Tait-phase theorem gives

$$
H_\phi\triangle H_\psi
=
K_{\phi+\psi},
$$

where `K_{\phi+\psi}` is a disjoint union of quotient Kempe cycles.  Those cycles change the continuation at each witness edge according to its aligned/crossed endpoint signature.

Thus each physical pair of sheets carries three simultaneous structures:

1. a connected quartic transition skeleton `T_{\phi\psi}`;
2. a rotation system inherited from scalar circuits;
3. a Kempe cycle system implementing the sheet change.

This is the natural setting for a transition-matroid split or a smaller cyclic separator.

## 5. Updated local target

The pairwise transition skeleton cannot be discarded as a collection of independent blocks.  A future composition theorem should analyse its connected ribbon structure and prove one of:

1. a two-edge scalar interval exposes a series pair or transition-matroid two-sum;
2. a proper subtrail yields a smaller cyclic separator or bounded four-pole transfer;
3. repeated enriched states along an Euler trail give a replaceable segment with matching side semantics;
4. every irreducible ribbon skeleton carries the crossed DDD `D_8` signature.

The cycle rank `2k` shows why an abstract quartic core need not collapse to a path.  Physical progress must use the rotation and Kempe data, not connectedness alone.

## 6. Reliability boundary

Proved here:

- the exact pairwise transition graph construction;
- connectedness for every pair of quartic near-resolutions;
- its exact degree sequence, size, cycle rank, and terminal Euler trail;
- the induced ribbon interpretation for physical scalar circuits.

Not proved here:

- that the ribbon skeleton has a proper transition-matroid split;
- that a Kempe cycle component gives a bounded replacement;
- classification of enriched quartic phase designs;
- singleton or two-edge composition;
- identification with the physical `D_8` class;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, or DOI status is implied.