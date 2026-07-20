# Rank-one persistent intersections localise to scalar intervals

## 1. Purpose

A gauge-rigid odd-intersection pair consists of physical cycles

$$
z,z'\in\mathcal C(G),
\qquad
\mathcal B(z,z')=1,
$$

whose common-edge word

$$
w=z\odot z'
$$

lies in the dual gauge code. In dual-flow rank one,

$$
\boxed{
w=c*(\alpha\circ f)}
$$

for one binary cycle `c` and one nonzero covector `\alpha\in\Gamma^*`.

Put

$$
H_\alpha=\{e:\alpha(f(e))=1\}.
$$

The scalar support `H_\alpha` is an even subgraph. This chapter proves that the rank-one norm support is a union of complete scalar circuits and marked intervals, and that at least one such component carries the odd ribbon-intersection bit.

Thus dual rank one reduces to

$$
\boxed{
\text{one odd enriched scalar circuit}
\quad\text{or}\quad
\text{one odd enriched scalar transition interval}.
}
$$

## 2. Two degree-two systems

Let

$$
H=H_\alpha.
$$

Both `H` and `c` have degree zero or two at every vertex, and

$$
w=c\cap H.
$$

Hence every vertex has degree at most two in `w`; every connected component of `w` is a path or a circuit.

### Lemma 2.1 — local continuation law

At a vertex used by both `c` and `H`, exactly one of the following occurs.

1. **Same pair.** `c` and `H` use the same two incident edges. Both belong to `w`, so the common support continues through the vertex.
2. **Different pair.** The two degree-two subsets of the cubic star share exactly one edge. That edge belongs to `w` and terminates a path component there.

The vertices of the second type are called switch vertices of `(c,H)`.

#### Proof

Two two-element subsets of a three-element set are either equal or meet in exactly one element. ∎

## 3. Decomposition on one scalar circuit

Let `C` be one circuit component of `H`. The switch vertices on `C` occur in even number: while traversing `C`, membership of its next edge in `c` toggles exactly at a switch, and the initial state must be recovered.

### Theorem 3.1 — scalar interval decomposition

Exactly one of the following holds.

1. `c\cap C=\varnothing`;
2. `c\cap C=C`;
3. the switch set has cardinality `2s>0`, and after a cyclic indexing
   $$
   v_1,v_2,\ldots,v_{2s},
   $$
   one has
   $$
   \boxed{
   c\cap C
   =
   C[v_1,v_2]
   \sqcup
   C[v_3,v_4]
   \sqcup\cdots\sqcup
   C[v_{2s-1},v_{2s}],
   }
   $$
   where the displayed arcs are the occupied arcs between consecutive switch vertices.

#### Proof

Between consecutive switch vertices, `c` either follows both edges of `C` at every internal vertex or follows neither. The state toggles at each switch and therefore alternates around `C`. With no switches the state is constant, giving the empty or full cases. ∎

Thus every connected component of a rank-one support is either a complete scalar circuit or a marked interval in one scalar circuit.

## 4. Localising the surface-intersection bit

Return to the response cycles `z,z'` with

$$
w=z\odot z'.
$$

On a cubic graph, two nonzero cycle germs meeting a vertex must share an edge. Therefore all possible intersections of ribbon representatives of `z,z'` can be confined to small regular neighbourhoods of the connected components of `w`.

Choose pairwise disjoint regular neighbourhoods `N(K)` of the components `K` of `w`, including small sectors at path endpoints. Perturb the two cycles into general position inside these neighbourhoods and make them disjoint outside.

Let

$$
\epsilon(K)\in\mathbf F_2
$$

be the intersection contribution inside `N(K)`.

### Theorem 4.1 — componentwise intersection sum

$$
\boxed{
\mathcal B(z,z')
=
\sum_{K\in\pi_0(w)}\epsilon(K).
}
$$

#### Proof

The chosen neighbourhoods are disjoint and contain every shared vertex and edge sector. The representatives have no intersections in the complement, and mod-two intersection is additive over disjoint regions. ∎

### Corollary 4.2 — one odd scalar carrier

If

$$
\mathcal B(z,z')=1,
$$

then some connected component `K` of `w` satisfies

$$
\boxed{\epsilon(K)=1.}
$$

In dual rank one, this `K` is either a complete scalar circuit of `H_\alpha` or one marked interval in such a circuit.

## 5. Enriched endpoint data

For a path component `K`, each endpoint is simultaneously:

- a switch vertex between the binary cycle `c` and the scalar circuit;
- a vertex where one of `z,z'` leaves the shared-edge support;
- a local transition state in the natural line-graph carrier;
- a port into the rest of the physical graph.

The bit `\epsilon(K)` depends only on the two endpoint transition states, the signed edge bands along `K`, and the relative traversal of the two response cycles. Hence an odd interval is a finite-boundary enriched interface even when its interior is long.

For a complete scalar circuit, `\epsilon(K)=1` records a closed one-sided or symplectically linked carrier on that scalar component.

## 6. Rank-one frontier consequence

The rank-one persistent obstruction now satisfies

$$
\boxed{
\begin{array}{c}
\mathcal B(z,z')=1,\\
z\odot z'=c*H_\alpha
\end{array}
\Longrightarrow
\begin{cases}
\text{odd complete scalar circuit},\\
\text{odd marked scalar interval}.
\end{cases}}
$$

This is a genuine localisation theorem: the arbitrary global support of the two response cycles has disappeared, and one scalar component with at most two boundary ports carries the obstruction.

The next composition step should combine this result with the existing interval machinery:

1. bounded Tait backtrack caps;
2. periodic triangle-cell chains;
3. transition walks in `\Gamma_g` when further distinguished-colour edges intervene;
4. connected-cycle horizontal switches on closed scalar carriers.

The remaining difficulty is side semantics and root-admissibility, not localisation of the rank-one support.

## 7. Reliability boundary

Proved here:

- path/circuit structure of a rank-one norm support;
- exact alternating-interval decomposition on every scalar circuit;
- componentwise decomposition of the ribbon intersection bit;
- existence of one odd scalar circuit or odd marked interval.

Open:

- composition of every odd interval;
- an admissible horizontal switch for every odd closed scalar carrier;
- reduction of dual rank two or three;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, DOI, or merge status is implied.
