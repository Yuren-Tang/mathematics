# AC-PD-A8 — cut-even collapse and exact multiplicity transport

**Proof-development state:** `COMPLETE-DRAFT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Depends on:** `AC-PD-A2`, `AC-PD-A6`, `AC-PD-A7`  
**Immediate consumer:** `AC-PD-A9`  
**External mathematical inputs:** none

## 0. Main output

Let `G` be the finite-active-edge loopless core and let

\[
(H,\pi,\lambda)
\]

be its A2 port-cycle expansion, where

\[
\pi:V(H)\to V(G),
\qquad
\lambda:E(G)\hookrightarrow E(H)
\]

is the injective lift of original edge objects. Suppose

\[
\mathcal F'=(F'_i)_{i\in I}
\]

is a finite indexed intrinsic even double cover of `H`; in the AffineCDC application, `I=\mathbf F_2^3` and this is supplied by A6–A7.

Define memberwise projection

\[
\operatorname{proj}(F')
:=
\{e\in E(G):\lambda(e)\in F'\}.
\]

Then the projected indexed family

\[
\mathcal F=(\operatorname{proj}(F'_i))_{i\in I}
\]

is an intrinsic even double cover of `G`:

- every projected support is cut-even;
- every original edge is covered exactly twice;
- empty and repeated projected supports remain as indexed occurrences.

No circuit structure is projected or asserted.

## 1. Structural cut identity

A2 proves that for every vertex subset `S\subseteq V(G)`:

1. an original edge `e` crosses `S` exactly when `\lambda(e)` crosses `\pi^{-1}(S)`;
2. no internal fibre edge crosses `\pi^{-1}(S)`.

Consequently

\[
\boxed{
\delta_H(\pi^{-1}(S))
=
\lambda(\delta_G(S)).
}
\]

and `λ` restricts to a bijection

\[
\delta_G(S)\xrightarrow{\sim}\delta_H(\pi^{-1}(S)).
\]

This remains true when `π` is not surjective onto isolated ambient vertices, because isolated vertices are endpoints of no active edge.

## 2. Memberwise projected support

For `F'\subseteq E(H)`, define

\[
F:=\operatorname{proj}(F')
=\lambda^{-1}(F').
\]

### Lemma 2.1 — finiteness

If `F'` is finite, then `F` is finite.

#### Proof

The injection `λ` maps `F` into the finite set `F'`. ∎

In the present application all active edge sets are finite, so this is automatic but still records the weakest support hypothesis.

### Lemma 2.2 — cut-intersection bijection

For every `S\subseteq V(G)`, the map `λ` restricts to a bijection

\[
F\cap\delta_G(S)
\xrightarrow{\sim}
F'\cap\delta_H(\pi^{-1}(S)).
\]

#### Proof

If `e\in F\cap\delta_G(S)`, then `λ(e)\in F'`, and the structural cut identity places `λ(e)` in `\delta_H(\pi^{-1}(S))`.

Conversely, let `a\in F'\cap\delta_H(\pi^{-1}(S))`. No internal edge lies in this pulled-back cut, so the structural identity gives a unique `e\in\delta_G(S)` with `a=λ(e)`. Since `a\in F'`, the definition of projection gives `e\in F`. Injectivity of `λ` gives uniqueness. ∎

### Theorem 2.3 — cut-even projection

If `F'` is cut-even in `H`, then `\operatorname{proj}(F')` is cut-even in `G`.

#### Proof

For every `S\subseteq V(G)`, Lemma 2.2 gives equal finite cardinalities

\[
|\operatorname{proj}(F')\cap\delta_G(S)|
=
|F'\cap\delta_H(\pi^{-1}(S))|.
\]

The right-hand side is even because `F'` is cut-even. ∎

Only cut parity is used. An upstairs support may have arbitrary internal fibre edges, and all of them disappear under projection without affecting the proof.

## 3. Indexed-family projection

Let `I` be finite and define

\[
F_i:=\operatorname{proj}(F'_i)
\qquad(i\in I).
\]

### Proposition 3.1 — memberwise parity

If every `F'_i` is cut-even in `H`, then every `F_i` is cut-even in `G`.

#### Proof

Apply Theorem 2.3 to each index. ∎

### Theorem 3.2 — exact original-edge coverage

If every edge of `H` lies in exactly two indexed supports `F'_i`, then every original edge of `G` lies in exactly two projected supports `F_i`.

#### Proof

For every `e\in E(G)` and every index `i`,

\[
e\in F_i
\iff
\lambda(e)\in F'_i.
\]

Therefore the index sets are equal:

\[
\{i\in I:e\in F_i\}
=
\{i\in I:\lambda(e)\in F'_i\}.
\]

The latter has cardinality two by the upstairs exact-coverage hypothesis. ∎

The coverage of internal auxiliary edges is not transported and need not be: they are not edges of `G`.

### Corollary 3.3 — intrinsic even double cover after collapse

If `(F'_i)_{i\in I}` is an intrinsic even double cover of `H`, then `(F_i)_{i\in I}` is an intrinsic even double cover of `G`.

## 4. Multiset bookkeeping

Passing from the indexed family to the image multiset

\[
[\,F_i:i\in I\,]
\]

retains one occurrence for every index.

### Proposition 4.1 — repeated images

If `F'_i\ne F'_j` but `F_i=F_j`, both projected occurrences remain. Exact edge coverage counts indices, so identifying equal support values would be invalid in general.

### Proposition 4.2 — empty images

A projected support may be empty, for example when `F'_i` consists entirely of internal fibre edges. Empty occurrences contribute zero to every edge multiplicity and are cut-even. They may be retained without harm.

### Proposition 4.3 — multiset exact coverage

For every original edge `e`, filtering the projected multiset by the predicate `e\in(-)` gives cardinality two.

#### Proof

The multiset filter counts exactly the indices in Theorem 3.2, including separate occurrences with equal support values. ∎

## 5. Why circuits are not projected

An upstairs circuit can behave under projection in several ways:

- it may project to the empty support if it lies entirely inside one fibre;
- different upstairs circuits may have the same projected support;
- one upstairs circuit may enter and leave fibres in a pattern whose projected edge set is cut-even but not inclusion-minimal;
- the projected support may split into several downstairs circuits.

Thus no map

\[
\text{upstairs circuits}
\longrightarrow
\text{downstairs circuits}
\]

is asserted. The preserved invariant is precisely cut parity plus indexed edge multiplicity. A9 decomposes each projected finite cut-even support once, downstairs.

## 6. Components and degenerate cases

### Disconnected graph

The expansion and collapse preserve edge-bearing components. The proof works globally and, equivalently, componentwise.

### Empty graph

Both original and expanded active graphs are empty. Every projected member is empty and the edge multiplicity requirement is vacuous.

### Isolated vertices

They may have empty `π`-fibres. Since they lie on no active cut edge, the cut-intersection bijection remains exact.

### Parallel edges

The injective lift `λ` distinguishes original parallel edge objects, so exact coverage is transferred objectwise.

### Degree-two fibres

Their two parallel internal edges are auxiliary and vanish under projection. Because neither crosses a union of complete fibres, they do not enter the cut parity calculation.

## 7. AffineCDC specialization

Apply the theorem with:

- `I=\mathbf F_2^3`;
- the finite loopless cubic expansion `H` from A2;
- a nowhere-zero rank-three flow from A3;
- the compatible family from A5;
- the graph-level vertex-even family from A6;
- its intrinsic cut-even interpretation from A7.

The result is a finite indexed, hence multiset, cut-even double cover of the loopless original core `G`.

## 8. Exported interface

A9 may cite:

1. a finite indexed family of finite cut-even supports of the loopless original core;
2. exact edge coverage multiplicity two;
3. the associated multiset retains empty and repeated occurrences;
4. auxiliary fibre edges have been discarded safely;
5. no circuit decomposition or circuit projection has been used.

## 9. Completion assessment

`AC-PD-A8` is `COMPLETE-DRAFT`. No contradiction or new-mathematics gap arose. The next dependency-respecting unit is `AC-PD-A9`: finite decomposition of each cut-even support into edge-disjoint circuits, termination, empty support, concatenation across indexed occurrences, and preservation of exact global edge multiplicity.
