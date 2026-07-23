# Complete fixed-prefix states have no hidden genealogy coordinate

## Research Lead state-semantics theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V5.md` v5.2;
- `TARGET_TOPOLOGY_ARBORESCENCE_FIXED_ORDER_V1.md`;
- the order-restoring inverse-cancellation table;
- full-state forced-backbone and cap-route semantics.

**Status:** exact finiteness and Markov-sufficiency theorem. Once an original inverse step has been normalized back to predecessor order, all future legal moves, singular normalizations and accepted exits are determined by finite current labelled data. Edge ancestry, consumed Kempe words, Ptolemy comparison words and nested cancellation histories are transition witnesses, not state coordinates. Therefore repetition of one complete normalized state is genuine pointwise repetition on a fixed labelled incidence universe and may be closed to a history cylinder.

---

## 1. Fixed labelled predecessor universe

Fix one original-prefix level `ell` and let

\[
N=|V(C_\ell)|.
\]

Use the labelled vertex slots of `C_ell`, together with its finite set of exterior semiedge slots and cap incidences.

An inverse original cancellation temporarily passes through a graph with two fewer vertices, but the order-restoring table immediately returns to predecessor order:

- the original insertion restores the two original slots;
- an alternative insertion uses the same two restored slots and the same borrowed neighbouring slot;
- the missing-index branch also lives on those predecessor-order slots.

Hence every vertex of the fixed-prefix macro-state graph is represented on one common finite labelled vertex/dart universe. No live normalized state contains an absent vertex slot from an unresolved lower-order recursive call.

A topology is a pairing of finitely many labelled darts subject to cubic incidence. There are only finitely many such pairings.

---

## 2. Minimal complete state record

A complete normalized state is the tuple

\[
\boxed{
X=(G,\lambda,\alpha,\mathcal R,\mathcal C,T,p)
}
\]

with the following entries.

### 2.1 Current source topology `G`

`G` is the labelled cubic multigraph topology on the fixed vertex/dart universe, including ordered exterior incidences.

### 2.2 Current coefficient assignment `lambda`

Every ordinary edge carries one root in

\[
R_5=\binom{[5]}2.
\]

At an unresolved normalized endpoint there is exactly one co-root atom in

\[
\{Q_1,\ldots,Q_5\}.
\]

Transient zero or two-co-root states occur only inside one bounded local macro and are not state vertices.

### 2.3 Atom record `alpha`

`alpha` is either empty or records:

- the atom edge/dart position;
- the co-root value;
- the two crossed root resolutions;
- the current pivot/resolution-sheet bit.

All choices are finite.

### 2.4 Rooted support and route record `mathcal R`

The five indexed even supports are not independent genealogy data:

\[
F_i=\{e:i\in\lambda(e)\}.
\]

They are determined by `lambda` on the current finite graph.

For operational convenience `mathcal R` may cache finite derived data:

- connected components of `F_i triangle F_j`;
- current terminal pairings of relevant support-pair systems;
- emitted side-root labels on the finite incident edges;
- constant-pivot support transport;
- route orientation and the distinguished crossed-resolution sheet.

Every cached item is a subset, partition, matching or permutation of a finite current set and is uniquely checkable from current labelled data plus the one finite orientation bit. No path word is required.

### 2.5 Cap record `mathcal C`

This records:

- the ordered cap shore;
- the cap matching;
- the distinguished cap block;
- bounded/direct/theta and separator flags.

All live on the fixed finite exterior incidence set.

### 2.6 Target topology `T` and parent pointer `p`

`T=C_ell` is fixed. The target topology arborescence assigns each current ordinary topology one finite parent pointer. The pointer is determined by `G` and the fixed arborescence; it need not be stored separately.

---

## 3. Finiteness

### Theorem 3.1 — finite complete state set

At fixed `N,ell`, the set of complete normalized states is finite.

### Proof

- There are finitely many labelled cubic dart pairings `G`.
- There are at most `10^{|E(G)|}` root assignments, multiplied by finitely many one-co-root atom choices.
- Atom positions and resolutions are finite.
- Support components, terminal matchings, side words and route data are structures on finite current sets.
- Cap data and category flags are finite.
- The target and arborescence are fixed.

The finite union over all topologies is finite. ∎

---

## 4. Markov sufficiency

### Theorem 4.1 — future transitions depend only on the current state

For two occurrences with identical tuple `X`, the set of available canonical next macros and accepted exits is identical.

### Proof

Inspect every transition type.

#### Target parent move

The parent topology is determined by `G`. Its four exterior branch values are read from `lambda`; the forced diagonal and root/zero/co-root classification are therefore determined.

#### Local first-failure normalization

The zero/co-root atom, adjacent roots and bounded incidence identifications are contained in `(G,lambda,alpha)`. The alternative NNI, borrowing dichotomy, defect-tree normalization and category outcome depend only on this bounded current neighbourhood.

#### Constant-pivot and forced-backbone transport

The pivot state, resolutions, side roots and support components are contained in `alpha` and `mathcal R`. The next labelled transport cell is determined by current data and the fixed deterministic tie-breaking convention.

#### Horizontal support-pair switch

The current support-pair subgraph is `F_i triangle F_j`, determined by `lambda`. Its component partition and whether a component separates marked incidences are current graph facts.

#### Route/profile exit

The current terminal pairing, cap block and profile state are contained in `mathcal R,mathcal C`.

#### Equality/DDD continuation episode

The current carrier topology, root labels, cap route and fixed deterministic Morse/tie-breaking rule determine the selected finite forward move. Its return is normalized by the order-restoring table before another endpoint state is recorded.

#### Category and separator exits

Connectivity, loops, bridges, parallel identifications and finite edge cuts are properties of current `G` and the current local replacement.

Thus no transition test uses the path by which `X` was reached. ∎

---

## 5. What is not a state coordinate

### 5.1 Ptolemy word

A finite sequence of comparisons witnesses a path between two current topologies. The canonical scheduler uses only the current topology and its arborescence parent. The old word is not needed for the next move.

### 5.2 Kempe switch word

The result of prior switches is already encoded in the current root assignment `lambda`. Future support-pair components are recomputed from that assignment.

### 5.3 Edge ancestry

Only current labelled darts and pairings enter local source moves. Whether a present edge descended historically from one or another cancelled edge does not change its current endpoints, root value or support membership.

### 5.4 Cancellation call stack

No lower-order call survives in a normalized fixed-prefix state. Original/alternative insertion restores predecessor order before the state is recorded.

### 5.5 Length of constant-pivot runs

The current source graph and current atom position contain the actual finite run carrier. Prior traversals of it do not create a new state.

### Corollary 5.1 — history words are edge labels, not vertices

Different finite histories may define different parallel transition witnesses between the same two complete states. This does not enlarge the vertex set.

---

## 6. Pointwise recurrence and cylinder closure

Because states use one fixed labelled incidence universe, equality

\[
X_0=X_k
\]

means literal equality of:

- topology and incidence pairing;
- all edge roots;
- atom position/value/resolutions;
- support and route data;
- cap block and orientation;
- target-prefix metadata.

### Theorem 6.1 — repeated states close canonically

The endpoint collars of a history segment from `X_0` to `X_k=X_0` identify pointwise and form a well-defined labelled history cylinder.

### Proof

Use the identity map on labelled vertex and dart slots. Every coefficient, cap and route decoration agrees by state equality, so both source-history side germs also agree. No auxiliary history isomorphism or genealogy matching is needed. ∎

This is the exact closure hypothesis required by the periodic root-cylinder theorem.

---

## 7. Quotient caution

One may later quotient the finite labelled state set by source automorphisms or global `S_5` support permutations, but such a quotient is not used in the controlling recurrence proof.

If a quotient is used computationally, a repeated quotient state does not by itself give pointwise collar equality. One must choose and retain an explicit labelled representative isomorphism. The v5.2 proof avoids this issue by working with labelled states.

---

## 8. Assurance boundary

### Exact here

- one common labelled predecessor-order incidence universe;
- finite complete state tuple;
- derivation of indexed supports from the current root assignment;
- finiteness of route, cap and orientation decorations;
- Markov sufficiency of the tuple for every canonical transition and exit;
- exclusion of Ptolemy, Kempe, ancestry and call-stack words as state coordinates;
- literal collar identification for repeated labelled states.

### Imported authorial mathematics

- order-restoring inverse table;
- deterministic target topology arborescence;
- local first-failure and current-flow selection rules;
- full-state cap-route semantics.

### Not claimed

- PDL reconstruction or independent audit;
- that a smaller quotient state alphabet is sufficient without labelled witnesses;
- global R2 assurance, five-CDC, Lean, manuscript, curation, release or publication status.
