# Collapse, circuit decomposition, and final theorem assembly

## 1. Setup

Let `G₀` be the finite-active loopless core and let `(H,π,λ)` be its port-cycle cubic expansion.

- `π:V(H) → V(G₀)` collapses every active fibre to its original vertex;
- `λ:E(G₀) → E(H)` injects original edge objects as the external edges;
- internal edges lie entirely inside fibres;
- for every vertex set `S`, `δ_H(π⁻¹(S)) = λ(δ_{G₀}(S))`.

The previous chapter supplies a finite indexed intrinsic even double cover `(F'_i)_{i∈I}` of `H`. In the AffineCDC construction, `I=F₂³`.

## 2. Memberwise collapse of supports

For a support `F'⊆E(H)`, define its projection by

`proj(F') = {e∈E(G₀) : λ(e)∈F'}`.

Only external-edge membership is retained. Internal fibre edges disappear.

### Lemma 2.1 — exact cut-intersection bijection

For every vertex set `S⊆V(G₀)`, the injection `λ` restricts to a bijection

`proj(F') ∩ δ_{G₀}(S)  →  F' ∩ δ_H(π⁻¹(S))`.

Every lifted original crossing edge appears on the right, and no internal edge can cross a union of complete fibres.

### Theorem 2.2 — cut-even collapse

If `F'` is cut-even in `H`, then `proj(F')` is cut-even in `G₀`.

For each cut, Lemma 2.1 gives equal finite cardinalities. The upstairs cardinality is even, so the downstairs cardinality is even.

The theorem uses only cut parity. It does not require or preserve circuit minimality.

## 3. Exact occurrence transport

For each index `i`, let `F_i = proj(F'_i)`.

### Theorem 3.1 — exact original-edge multiplicity

For every original edge `e`,

`{i : e∈F_i} = {i : λ(e)∈F'_i}`.

Therefore the projected family covers every original edge exactly twice.

Auxiliary internal edges have no downstairs counterpart and require no transported coverage equation.

### Corollary 3.2 — even double cover after collapse

The projected indexed family `(F_i)` is an intrinsic even double cover of `G₀`.

Empty projected supports are allowed; a support may consist only of internal edges upstairs. Distinct upstairs supports may project to equal downstairs supports. Both occurrences remain because exact coverage counts indices, not distinct support values.

Passing to a multiset retains one occurrence for every index and preserves the multiplicity equation.

## 4. Why circuit structure is postponed

An upstairs circuit may:

- lie completely inside one fibre and project to the empty support;
- project to a nonminimal cut-even support;
- split into several downstairs circuits;
- share its projected support with another upstairs circuit.

Therefore the valid collapse theorem is

`cut-even support + occurrence multiplicity → cut-even support + occurrence multiplicity`,

not a map from upstairs circuits to downstairs circuits.

The canonical proof decomposes only once, after collapse.

## 5. Binary structure of cut-even supports

For finite supports `A` and `B`, symmetric difference satisfies

`∂(A △ B) = ∂A △ ∂B`.

Thus cut-even supports form a vector space over `F₂`. If `B⊆A` and both are cut-even, then `A\B = A △ B` is cut-even.

The foundations chapter proves that every nonempty finite cut-even support contains a circuit.

## 6. Terminating circuit decomposition

### Theorem 6.1 — finite decomposition

Every finite cut-even support `F` is a disjoint union of finitely many circuits.

Proof by induction on `|F|`:

- if `F` is empty, use the empty family;
- otherwise choose a circuit `C⊆F`;
- the remainder `F\C` is cut-even by symmetric-difference closure;
- its cardinality is strictly smaller;
- apply induction and add `C`.

The resulting circuits are pairwise edge-disjoint and their union is exactly `F`. Hence each edge of `F` occurs in exactly one circuit occurrence of this memberwise decomposition.

The theorem allows loops, parallel digons, disconnected supports, and disconnected ambient graphs. In the complete spine it is applied to the loopless core after collapse.

## 7. Memberwise decomposition of an indexed cover

Let `(F_i)_{i∈I}` be a finite indexed family of finite cut-even supports. Decompose every occurrence separately:

`F_i = disjoint union of C_{i,j}`.

Use the total index set of pairs `(i,j)`.

### Theorem 7.1 — global multiplicity preservation

For every edge `e`, the number of circuit occurrences `C_{i,j}` containing `e` equals the number of parent indices `i` for which `e∈F_i`.

Partition the circuit occurrences by the parent index. Within one parent decomposition, the local count is exactly the indicator of `e∈F_i`; summing over parent indices gives the equality.

### Corollary 7.2 — even double cover refines to circuit double cover

If every edge has parent multiplicity two, then every edge has final circuit multiplicity two.

An empty parent support contributes no circuit occurrence. If two parent indices carry equal supports, they are decomposed as two occurrences; repeated circuit values across different parents remain repeated occurrences.

## 8. Complete theorem assembly

### Theorem 8.1 — finite-active-edge circuit double cover

Let `G` be a multigraph with finite active edge set and no singleton cut. Then `G` has a finite indexed family of circuits covering every active edge object exactly twice.

### Proof

1. **Foundations.** Use intrinsic half-edge boundary parity, cut-even supports, circuit semantics, and indexed occurrence multiplicity.

2. **Delete loops.** Let `G₀` be the loopless core. Cuts are unchanged, so `G₀` has no singleton cut.

3. **Expand.** Construct the finite loopless cubic port-cycle expansion `H` with maps `π` and injective `λ`. The expansion has no singleton cut.

4. **Binary flow.** Seymour’s six-flow theorem, literal six-to-eight range inclusion, modular reduction, and the internal equal-order count give a nowhere-zero `F₂³` flow on `H`.

5. **Affine pair object.** Build the incidence quotient spaces, local affine torsor, pair complex, quotient equation, and stress obstruction while retaining graph/dart data.

6. **Rank-three compatibility.** Canonical quotient quadratics make the vertex space Lagrangian and the edge diagonal totally singular. The characteristic-torsor intersection theorem supplies a compatible family.

7. **Extract supports.** For every point of `F₂³`, collect the graph edges whose common affine line contains that point. Local evenness gives loopless vertex parity; every affine line has two points, so every edge lies in exactly two indexed supports.

8. **Convert parity.** On the loopless graph, once-per-edge vertex parity equals intrinsic boundary parity and cut parity. Thus the extracted family is an intrinsic even double cover of `H`.

9. **Collapse.** Project each support through `λ`. The pulled-back cut identity preserves cut parity, and membership equivalence preserves exact original-edge multiplicity. This gives an intrinsic even double cover of `G₀`.

10. **Decompose downstairs.** Apply Theorem 6.1 to every projected support and concatenate. Theorem 7.1 preserves multiplicity two. Hence `G₀` has a circuit double cover.

11. **Reinsert loops.** Regard every core circuit as a circuit of `G` and add exactly two occurrences of the singleton circuit of each deleted loop. Every nonloop and loop edge is now covered exactly twice.

This completes the proof.

## 9. Boundary cases

### Empty active graph

The empty indexed family is a circuit double cover. Every subsequent construction degenerates consistently.

### Loop-only graph

The loopless core is empty. Reinsertion supplies exactly two singleton circuit occurrences for each loop.

### Infinite ambient vertex carrier

Only endpoints of finitely many active edges enter the construction. Isolated vertices are inert.

### Disconnected graph

Flow existence, affine compatibility, support parity, collapse, decomposition, and cover concatenation are componentwise or direct sums. No connectedness hypothesis is used.

### Parallel edges

Edge-object identity is preserved through ports, flow coordinates, quotient summands, support membership, collapse, and multiplicity accounting. Two parallel edges may form a digon circuit.

## 10. Exact logical source boundary

The sole external non-elementary logical input is Seymour’s nowhere-zero six-flow theorem.

All other steps are proved within Programme A, including:

- singleton cut/bridge equivalence;
- loop reduction and witness normal form;
- cubic expansion and collapse laws;
- equal-order finite-group flow counting and transport;
- affine pair-complex equivalences;
- quadratic Fano compatibility;
- graph/dart support extraction;
- parity conversion;
- cut-even collapse;
- terminating circuit decomposition;
- exact multiplicity preservation.

Tutte’s equal-order flow theorem is historical provenance only.

## 11. Assurance boundary and audit targets

Programme A is complete at authorial paper-proof level and integrated here by the Curator. It has not yet received the dedicated independent Audit A and is not end-to-end Lean verified.

High-value independent-audit targets are:

1. external-edge nonbridge lifting through arbitrary port fibres;
2. the spanning-forest flow-kernel count and inclusion–exclusion;
3. the local affine-family identification;
4. characteristic cross-pairing and Lagrangian intersection;
5. dart-to-edge support descent and occurrence counting;
6. pulled-back-cut collapse identity;
7. repeated-parent multiplicity preservation;
8. final loop/core witness normalization.

These are assurance targets, not identified defects.

## 12. Provenance

This chapter integrates A8–A10 and depends on the previous two integrated chapters. Exact authorial dossiers, intermediate checkpoint SHAs, and the Programme A obligation DAG remain under `proof-development/` and are mapped in `PROGRAMME_A_INTEGRATION_MAP.md`.