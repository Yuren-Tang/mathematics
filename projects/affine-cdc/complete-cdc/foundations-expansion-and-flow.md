# Foundations, cubic expansion, and the binary-flow boundary

## 1. Multigraph and active-edge semantics

A multigraph is a vertex set `V`, a set `E` of active edge objects, and an endpoint multiset for every edge. Repeated endpoints are allowed, so loops are allowed; distinct edge objects with the same endpoint multiset are parallel and remain distinct throughout every construction.

The theorem assumes that `E` is finite. The ambient vertex carrier need not be finite. The active vertex set consists of endpoints of active edges and is finite, with at most `2|E|` members. Consequently every cut, parity calculation, component argument, and recursive decomposition can be reduced to finite active data without deleting isolated ambient vertices from the statement.

For a vertex set `S`, the cut `δ_G(S)` consists of nonloop edge objects with exactly one endpoint in `S`. Loops cross no cut. A singleton cut is a cut containing exactly one edge object.

### Theorem 1.1 — singleton cuts and bridges

For a nonloop edge `e`, the following are equivalent:

1. deleting `e` separates its endpoints;
2. `e` is the unique edge of some cut.

Thus a finite-active multigraph has no singleton cut exactly when it has no nonloop bridge. The cut formulation is primary below because it is insensitive to loops and pulls back exactly through the port-cycle collapse.

## 2. Intrinsic parity and circuits

For a finite support `F ⊆ E(G)`, define the half-edge degree at a vertex by counting endpoint occurrences. A nonloop contributes one at each endpoint; a loop contributes two at its vertex. The intrinsic boundary `∂_G F` is the set of vertices with odd half-edge degree.

A support is cut-even when it meets every cut in even cardinality.

### Lemma 2.1 — cut-parity identity

For every vertex set `S`,

`|F ∩ δ_G(S)|` is congruent modulo two to the sum of the half-edge degrees of `F` over vertices of `S`.

Internal nonloop edges contribute twice, loops contribute twice, exterior edges contribute zero, and crossing edges contribute once.

### Theorem 2.2 — intrinsic parity equivalence

For every finite support,

`F is cut-even` if and only if `∂_G F` is empty.

The forward implication tests singleton vertex sets. The reverse implication applies Lemma 2.1 to every cut.

A circuit is a nonempty finite cut-even support that is inclusion-minimal among nonempty cut-even supports.

### Theorem 2.3 — circuit characterization

For a finite support `C`, the following are equivalent:

1. `C` is a circuit;
2. `C` is a polygonal cycle support;
3. the edge-bearing support graph is connected and every active support vertex has half-edge degree two.

The polygonal cases include:

- one loop;
- two distinct parallel nonloop edges;
- an ordinary simple cycle of length at least three.

The key existence lemma is that every nonempty finite boundary-even support contains one polygonal cycle: follow a maximal vertex-simple path in the support, using positive even degree at its endpoint to close a loop or return to an earlier vertex. Minimality then identifies a circuit with the resulting polygonal cycle.

This chapter fixes circuit semantics and characterization. The theorem that every finite cut-even support decomposes into circuits is postponed until the final chapter.

## 3. Indexed families and occurrence multiplicity

A finite indexed support family is a tuple `(F_i)_{i∈I}`. Its coverage multiplicity at an edge `e` is the number of indices `i` for which `e ∈ F_i`.

Indices are occurrences. If `F_i = F_j` with `i ≠ j`, the two occurrences remain distinct. Empty supports are permitted and contribute no coverage.

An intrinsic even double cover is a finite indexed family of cut-even supports covering every active edge exactly twice. A circuit double cover is a finite indexed family of circuits covering every active edge exactly twice.

Reindexing by a bijection preserves the witness. Concatenation adds multiplicities. Componentwise covers concatenate because cut parity and edge identity are componentwise.

The empty active graph has the empty circuit double cover. A loop-only graph has the explicit cover containing two occurrences of the singleton circuit of every loop.

## 4. Exact loop deletion and reinsertion

Let `L(G)` be the loop set and let `G₀` be the edge-deletion subgraph obtained by removing all loops.

### Theorem 4.1 — exact cut preservation

For every vertex set `S`,

`δ_{G₀}(S) = δ_G(S)`.

Therefore `G` has no singleton cut exactly when `G₀` has no singleton cut, and every nonloop edge has the same bridge status before and after loop deletion.

For a support containing no loops, cut-even and circuit status are identical in `G` and `G₀`.

### Theorem 4.2 — circuit separation across loops

Every circuit of `G` is exactly one of:

- a singleton loop support;
- a circuit of the loopless core `G₀`.

There is no circuit mixing a loop with another edge, because the singleton loop is already a nonempty cut-even proper subset.

### Theorem 4.3 — CDC witness normal form

A circuit double cover of `G₀` extends to one of `G` by adding two singleton occurrences for every deleted loop. Conversely, every circuit double cover of `G` contains exactly two singleton occurrences for each loop, and deleting those forced occurrences gives a circuit double cover of `G₀`.

Hence circuit-double-cover existence is equivalent for `G` and `G₀`.

## 5. Port-cycle cubic expansion

Now let `G` be loopless, finite-active, and without singleton cuts. Every active vertex has degree at least two.

For each active vertex `v`, choose a cyclic permutation of its finite incidence set. Create one port `(v,e)` for every incidence of an original edge `e` at `v`.

The expanded graph `H` has two classes of edge objects.

### External edges

For each original edge `e = uv`, create one external edge `λ(e)` joining `(u,e)` and `(v,e)`. The map `λ:E(G) → E(H)` is injective.

### Internal edges

For each port `(v,e)`, create one internal edge joining it to the successor port in the chosen cyclic order.

If `deg_G(v)=2`, the two ports are joined by two distinct parallel internal edge objects. This convention is forced: one edge would make the ports degree two, while a loop would violate looplessness.

Let `π(v,e)=v` be the collapse map.

### Theorem 5.1 — expansion structure

The graph `H` is finite, loopless, and cubic. Its active fibres are connected port cycles. Every edge joining distinct fibres is a unique lifted original edge, and every auxiliary edge lies inside one fibre.

The exact size formulae are

`|V(H)| = 2|E(G)|` and `|E(H)| = 3|E(G)|`.

The edge-bearing connected components of `H` correspond exactly to those of `G`. Isolated original vertices have empty fibres and are intentionally not in the active expansion.

### Theorem 5.2 — preservation of no singleton cuts

Every internal edge lies on its fibre cycle and has an alternate internal path. For an external edge `λ(e)`, the original edge `e` is not a bridge, so an alternate path between its endpoints in `G-e` lifts to an alternate walk through external edges and connected fibre arcs in `H-λ(e)`.

Thus no edge of `H` is a bridge, and `H` has no singleton cut.

### Theorem 5.3 — exact collapse and cut pullback

Collapsing each active fibre and deleting all internal edges recovers the active original graph, preserving every original edge object and endpoint multiset.

For every vertex set `S ⊆ V(G)`,

`δ_H(π⁻¹(S)) = λ(δ_G(S))`.

No internal edge crosses a union of complete fibres. This exact cut identity is the structural input used later for support projection.

## 6. Binary eight-flow theorem

Let `K` be a finite loopless multigraph without singleton cuts. Choose an orientation only for the group-flow argument.

### External theorem 6.1 — Seymour

Every finite graph with no isthmus has a nowhere-zero integral six-flow.

The source is P. D. Seymour, “Nowhere-zero 6-flows”, Journal of Combinatorial Theory, Series B 30 (1981), 130–135, DOI `10.1016/0095-8956(81)90058-7`.

Seymour is applied componentwise to the edge-bearing components. Isolated vertices are inert.

A nowhere-zero integral six-flow is literally an integral eight-flow because `0 < |z_e| < 6` implies `0 < |z_e| < 8`. Reduction modulo eight then gives a nowhere-zero `Z/8Z` flow.

The remaining transport to `F₂³` is internal.

### Theorem 6.2 — flow-kernel count

For a finite abelian group `A` and a spanning subgraph with edge set `B`, the number of `A`-flows supported on `B` is

`|A|^(|B|-|V|+c(B))`,

where `c(B)` counts connected components including isolated vertices.

Choose one spanning tree in every nontrivial component. Arbitrary values on the chord edges extend uniquely to a flow by solving tree-edge values from leaves inward. The root equation holds automatically because the total boundary in a component is zero.

### Theorem 6.3 — nowhere-zero flow count

Inclusion–exclusion over the coordinates forced to zero gives

`N_G(A) = Σ_{B⊆E} (-1)^(|E|-|B|) |A|^(|B|-|V|+c(B))`.

Therefore the number, and hence existence, of nowhere-zero flows over a finite abelian group depends only on the order of the group.

Since `|Z/8Z| = |F₂³| = 8`, the modular eight-flow implies a nowhere-zero `F₂³` flow.

Tutte’s classical equal-order group-flow theorem remains historical provenance. It is not a logical black box in the integrated proof because Theorems 6.2–6.3 prove the required transport.

### Theorem 6.4 — characteristic-two adapter

On a loopless graph, an oriented `F₂³` flow is canonically the same as an edge labelling whose once-per-edge incidence sum is zero at every vertex. Every minus sign is a plus sign in characteristic two, and every loopless incident edge occurs once.

This adapter is not extended to loops: in the standard oriented boundary a loop cancels between its two endpoint occurrences, whereas a once-per-edge incidence set would count it once. Loops have already been removed by Theorem 4.1.

## 7. Exported interface

The next chapter may use:

1. exact finite-active multigraph, circuit, cut, and multiplicity semantics;
2. equivalence of no singleton cuts and absence of nonloop bridges;
3. exact loop deletion and forced two-occurrence reinsertion;
4. a finite loopless cubic expansion with maps `π` and injective `λ`;
5. exact component, size, edge-partition, collapse, and cut-pullback laws;
6. a nowhere-zero `F₂³` flow on the expanded graph;
7. Seymour 1981 as the sole external non-elementary logical input;
8. the internal equal-order transport and the loopless characteristic-two representation adapter.

## 8. Assurance and provenance

This chapter integrates A0–A3. The detailed authorial proofs and their exact intermediate checkpoint SHAs remain in `proof-development/`. The integration does not add independent audit or Lean status.

The highest-priority later audit targets in this chapter are:

- lifting an alternate path for every external edge through arbitrary port-cycle fibres;
- the spanning-forest kernel count;
- inclusion–exclusion and the exact equal-order transport;
- loop/core witness normalization.