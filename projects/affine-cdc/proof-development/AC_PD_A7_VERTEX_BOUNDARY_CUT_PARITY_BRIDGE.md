# AC-PD-A7 — exact vertex-parity, boundary-parity, and cut-parity bridge

**Proof-development state:** `COMPLETE-DRAFT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Depends on:** `AC-PD-A0`, `AC-PD-A6`  
**Immediate consumer:** `AC-PD-A8`  
**External mathematical inputs:** none

## 0. Purpose

The affine extraction in A6 returns supports satisfying the companion graph API's loopless once-per-edge vertex-even predicate. The outer theorem and collapse argument use intrinsic cut-evenness. This unit proves their exact equivalence on the loopless graph and records the precise failure with loops.

Let `G` be a multigraph and let `F\subseteq E(G)` be a finite support.

## 1. Two local degree conventions

### Intrinsic half-edge degree

Let

\[
\deg_F^{\mathrm{half}}(v)
\]

count endpoint occurrences at `v` among selected edges. A nonloop edge contributes one; a loop contributes two.

The intrinsic mod-two boundary is

\[
\partial_GF
:=
\{v:\deg_F^{\mathrm{half}}(v)\equiv1\pmod2\}.
\]

### Once-per-edge incidence count

Let

\[
\operatorname{Inc}_G(v)
:=
\{e\in E(G):e\text{ is incident with }v\}
\]

be a set of edge objects. Define

\[
\deg_F^{\mathrm{set}}(v)
:=
|F\cap\operatorname{Inc}_G(v)|.
\]

A loop appears once in this set, regardless of its two endpoint occurrences.

The current companion predicate is

\[
\operatorname{VertexEven}^{\mathrm{set}}_G(F)
\iff
\forall v,\quad
\deg_F^{\mathrm{set}}(v)\equiv0\pmod2.
\]

## 2. Exact loopless equality

### Lemma 2.1 — degree equality on loopless graphs

If `G` is loopless, then for every vertex `v`,

\[
\boxed{
\deg_F^{\mathrm{set}}(v)
=
\deg_F^{\mathrm{half}}(v).
}
\]

#### Proof

Every selected edge incident with `v` is a nonloop and has exactly one endpoint occurrence at `v`. Thus the edge objects counted by the incidence set are in bijection with the endpoint occurrences counted by the intrinsic degree. Parallel edges remain separate objects on both sides. ∎

### Corollary 2.2 — vertex-even equals boundary-even

If `G` is loopless, then

\[
\operatorname{VertexEven}^{\mathrm{set}}_G(F)
\iff
\partial_GF=\varnothing.
\]

#### Proof

Apply Lemma 2.1 at every vertex. ∎

## 3. Boundary parity equals cut parity

Recall that `F` is cut-even when

\[
\forall S\subseteq V(G),\quad
|F\cap\delta_G(S)|\equiv0\pmod2.
\]

A0 proved the intrinsic identity

\[
|F\cap\delta_G(S)|
\equiv
\sum_{v\in S}\deg_F^{\mathrm{half}}(v)
\pmod2,
\]

and hence

\[
\operatorname{CutEven}_G(F)
\iff
\partial_GF=\varnothing.
\]

Combining this with Corollary 2.2 gives the exact bridge.

### Theorem 3.1 — loopless parity equivalence

For every finite support of a loopless multigraph,

\[
\boxed{
\operatorname{VertexEven}^{\mathrm{set}}_G(F)
\iff
\partial_GF=\varnothing
\iff
\operatorname{CutEven}_G(F).
}
\]

No finiteness of the ambient vertex carrier and no connectedness hypothesis is required; only the support must be finite.

## 4. Application to the affine supports

Let `(F_s)_{s\in\mathbf F_2^3}` be the graph-level family from A6 on the finite loopless cubic graph.

### Corollary 4.1 — each affine support is cut-even

For every `s\in\mathbf F_2^3`,

\[
\operatorname{CutEven}_G(F_s).
\]

#### Proof

A6 proves the once-per-edge vertex-even condition. Apply Theorem 3.1. ∎

### Corollary 4.2 — intrinsic even double cover

The indexed family `(F_s)` is an intrinsic even double cover in A0's sense:

1. every member is cut-even;
2. every active edge has coverage multiplicity exactly two.

#### Proof

The first assertion is Corollary 4.1. The second is A6 Theorem 4.1. ∎

Flattening to a multiset preserves both facts and retains repeated and empty occurrences.

## 5. Why looplessness is necessary for this adapter

### Proposition 5.1 — singleton-loop counterexample

Let `G` consist of one loop `\ell` at a vertex `v`, and let `F=\{\ell\}`. Then:

- `F` is intrinsically boundary-even;
- `F` is cut-even;
- `F` is not once-per-edge vertex-even.

#### Proof

The loop contributes two endpoint occurrences at `v`, so its intrinsic degree is even. It crosses no cut. But it is one edge object in `\operatorname{Inc}_G(v)`, so the set-incidence count is one. ∎

Thus the current companion predicate is not a general multigraph parity definition. The full theorem handles loops by A1, not by extending this adapter.

## 6. Edge and degenerate cases

### Empty support

The empty support satisfies all three parity predicates.

### Empty graph and isolated vertices

All conditions are vacuous. Isolated vertices contribute zero to both local degree conventions.

### Parallel edges

Each edge object is counted separately. The two-edge digon support has set degree two and half-edge degree two at each endpoint, hence is cut-even.

### Disconnected graphs

All local parity conditions are componentwise; cut-evenness follows globally from the same boundary identity.

## 7. Formal assurance boundary

The companion graph-level extraction proves the set-incidence `IsEven` predicate because the active graph is loopless. A0 and this dossier supply the paper-side proof that this predicate is exactly intrinsic cut parity on that domain. No Lean theorem is changed, and no claim is made that the current once-per-edge API correctly represents loops.

## 8. Exported interface

A8 may cite:

1. every A6 support is intrinsically cut-even;
2. the indexed and multiset affine families are intrinsic even double covers of the loopless cubic graph;
3. the equivalence requires looplessness and finite support, not connectedness;
4. loop cases remain exclusively under A1's deletion/reinsertion interface.

## 9. Completion assessment

`AC-PD-A7` is `COMPLETE-DRAFT`. No contradiction or new-mathematics gap arose. The next dependency-respecting unit is `AC-PD-A8`: memberwise projection through the A2 collapse datum, preservation of cut parity, and exact double coverage of the loopless original core, including auxiliary edges, empty images, equal images, and multiset occurrence bookkeeping.
