# AC-PD-A1 — exact loop deletion and singleton-loop reinsertion

**Proof-development state:** `COMPLETE-DRAFT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Depends on:** `AC-PD-A0` at `0d8c9102fa117e5f58b5d1617f3fae782c164097`  
**Immediate consumers:** `AC-PD-A2`, `AC-PD-A10`  
**External mathematical inputs:** none

## 0. Purpose

This unit proves that loops can be removed before the loopless outer-shell argument and restored afterward with exact circuit and multiplicity bookkeeping.

The result is stronger than one-way preservation: deleting loops preserves every cut exactly, reflects the no-singleton-cut condition, classifies all circuits involving loops, and gives an equivalence between CDC witnesses of the original graph and CDC witnesses of its loopless core together with the forced two singleton occurrences for each loop.

## 1. Loopless core

Let `G=(V,E,\partial)` be a multigraph with finite active edge set. Let

\[
L(G):=\{e\in E(G):e\text{ is a loop}\}
\]

and define the loopless core

\[
G_0:=G[E(G)\setminus L(G)].
\]

The vertex carrier is unchanged. Some vertices active only through loops may become isolated in `G_0`.

### Proposition 1.1 — elementary properties

1. `E(G_0)=E(G)\setminus L(G)` is finite.
2. `G_0` is loopless.
3. Every parallel nonloop edge object of `G` remains a distinct edge object of `G_0`.
4. `V_+(G_0)\subseteq V_+(G)`; equality need not hold.
5. If `E(G)` consists only of loops, then `E(G_0)=\varnothing`.

#### Proof

All assertions follow directly from edge deletion and the definitions. ∎

## 2. Exact preservation of cuts and bridges

### Theorem 2.1 — cut identity after loop deletion

For every `S\subseteq V(G)`,

\[
\boxed{
\delta_{G_0}(S)=\delta_G(S).
}
\]

Here the two sets are identified as subsets of the common nonloop edge set `E(G_0)`.

#### Proof

A loop belongs to no cut. Every nonloop edge is retained with the same endpoints. Therefore an edge crosses `S` in `G_0` exactly when it crosses `S` in `G`. ∎

### Corollary 2.2 — no-singleton-cut equivalence

\[
\boxed{
\operatorname{NoSingletonCut}(G)
\iff
\operatorname{NoSingletonCut}(G_0).
}
\]

#### Proof

The families of cuts are identical by Theorem 2.1. ∎

### Corollary 2.3 — nonloop bridge status is unchanged

For every nonloop edge `e\in E(G_0)`,

\[
e\text{ is a bridge of }G
\iff
e\text{ is a bridge of }G_0.
\]

#### Proof

By A0 Proposition 2.4, bridge status is equivalent to appearing as the unique edge of a cut. Apply Theorem 2.1. ∎

Loops themselves are never bridges. Thus the natural phrase “bridgeless multigraph” is exactly equivalent to “loopless core has no bridge”.

## 3. Exact preservation of nonloop support parity

For a support `F\subseteq E(G_0)`, regard the same set of edge objects as a support of `G`.

### Proposition 3.1 — cut-even identity

\[
\boxed{
\operatorname{CutEven}_{G_0}(F)
\iff
\operatorname{CutEven}_{G}(F).
}
\]

#### Proof

For every vertex set `S`, Theorem 2.1 gives

\[
F\cap\delta_{G_0}(S)=F\cap\delta_G(S).
\]

Hence the required cardinality parities are identical. ∎

The same statement follows from intrinsic boundary parity: a support containing no loops has the same endpoint-occurrence degrees in `G_0` and `G`.

## 4. Circuit classification across loop deletion

### Theorem 4.1 — circuits of the loopless core remain circuits

If `C\subseteq E(G_0)`, then

\[
C\text{ is a circuit of }G_0
\iff
C\text{ is a circuit of }G.
\]

#### Proof

Nonemptiness is unchanged. By Proposition 3.1, `C` and every subset of `C` have the same cut-even status in the two graphs. Therefore inclusion-minimal nonempty cut-even status is identical. ∎

### Theorem 4.2 — every circuit of `G` is either a singleton loop or a core circuit

Let `C` be a circuit of `G`. Exactly one of the following holds:

1. `C=\{\ell\}` for one loop `\ell\in L(G)`;
2. `C\subseteq E(G_0)` and `C` is a circuit of `G_0`.

#### Proof

If `C` contains a loop `\ell`, then `\{\ell\}` is a nonempty cut-even support: loops cross no cut. Minimality of `C` forces `C=\{\ell\}`.

If `C` contains no loop, then `C\subseteq E(G_0)` and Theorem 4.1 applies. The alternatives are disjoint. ∎

### Corollary 4.3 — no mixed loop/nonloop circuit

A circuit never contains both a loop and another edge. In particular, loop reinsertion cannot alter or merge a core circuit.

## 5. Reinsertion construction

Let

\[
\mathcal C_0=(C_i)_{i\in I}
\]

be a cycle double cover of `G_0`, where `I` is finite. Since `E(G)` is finite, the loop set `L(G)` is finite.

Define a new finite index set

\[
I^+:=I\sqcup(L(G)\times\{0,1\}).
\]

Define the family `\mathcal C^+=(C^+_j)_{j\in I^+}` in `G` by

\[
C^+_j=
\begin{cases}
C_j,&j\in I,\\
\{\ell\},&j=(\ell,0)\text{ or }(\ell,1).
\end{cases}
\]

### Theorem 5.1 — exact loop reinsertion

`\mathcal C^+` is a cycle double cover of `G`.

#### Proof

Every old occurrence `C_i` is a circuit of `G` by Theorem 4.1. Every new singleton loop support is a circuit by A0 Corollary 4.6.

For a nonloop edge `e`, only old occurrences can contain it, and its multiplicity remains

\[
\mu_{\mathcal C^+}(e)=\mu_{\mathcal C_0}(e)=2.
\]

For a loop `\ell`, exactly the two occurrences indexed by `(\ell,0)` and `(\ell,1)` contain it, so

\[
\mu_{\mathcal C^+}(\ell)=2.
\]

Thus every active edge is covered exactly twice by circuit occurrences. ∎

## 6. Converse and witness normal form

### Theorem 6.1 — every CDC of `G` has exactly two singleton occurrences per loop

Let `\mathcal C=(C_i)_{i\in I}` be a cycle double cover of `G`. For each loop `\ell`, exactly two indices `i\in I` satisfy

\[
C_i=\{\ell\}.
\]

No other circuit occurrence contains `\ell`.

#### Proof

By Theorem 4.2, any circuit containing `\ell` is exactly the singleton support `\{\ell\}`. The CDC multiplicity equation requires exactly two occurrences containing `\ell`. ∎

### Theorem 6.2 — deletion of forced loop occurrences recovers a core CDC

Delete from `\mathcal C` the two singleton occurrences belonging to every loop. The remaining indexed family is a cycle double cover of `G_0`.

#### Proof

By Theorem 4.2, every remaining circuit lies in `E(G_0)` and is a circuit of `G_0`. Removing singleton-loop occurrences changes no nonloop edge multiplicity. Every nonloop edge therefore remains covered exactly twice. ∎

### Corollary 6.3 — CDC existence equivalence

For every finite-active-edge multigraph `G`,

\[
\boxed{
G\text{ has a cycle double cover}
\iff
G_0\text{ has a cycle double cover}.
}
\]

Moreover, up to reindexing, a CDC witness of `G` is exactly a CDC witness of `G_0` plus two forced singleton circuit occurrences for each loop.

## 7. Degenerate cases

### Empty graph

If `E(G)=\varnothing`, then `G=G_0` and the empty family is a CDC.

### Loop-only graph

If every active edge is a loop, then `G_0` has empty active edge set. Starting from its empty CDC, Theorem 5.1 produces precisely two singleton occurrences for each loop.

### Vertices becoming isolated

A vertex incident only with removed loops becomes isolated in `G_0`. This affects no cut, bridge condition, circuit of the core, or cover multiplicity. No surjectivity or active-vertex equality is required.

### Disconnected graphs

Loop deletion is componentwise. A component consisting of one vertex and any number of loops becomes an isolated vertex; every other component retains its nonloop cut structure exactly. The reinsertion family is the disjoint concatenation of the forced singleton-loop occurrences with the core CDC.

### Parallel edges

Nonloop parallel edge objects are untouched. In particular, a two-edge digon circuit in `G_0` remains the same circuit in `G`.

## 8. Exported interface

Downstream units may use the following statements without re-proving them.

1. `G_0` is finite-active-edge and loopless.
2. `\delta_{G_0}(S)=\delta_G(S)` for every vertex subset `S`.
3. `G` has no singleton cut if and only if `G_0` has no singleton cut.
4. Every nonloop edge has the same bridge status before and after loop deletion.
5. A nonloop support has identical cut-even and circuit status in `G` and `G_0`.
6. Every circuit of `G` is either a singleton loop or a circuit of `G_0`.
7. Every core CDC extends by two singleton occurrences per loop.
8. Conversely, every CDC of `G` contains exactly those forced loop occurrences and reduces to a core CDC.

## 9. Corpus mapping

This unit expands the concise loop discussion in `reduction/even-cover-and-collapse.md` and the natural loop-aware theorem boundary in `FORMAL_STATUS.md`. It is consistent with the baseline statement that looplessness is a reduction condition for the present affine/flow machinery rather than a hypothesis of the natural external theorem.

No source boundary is involved and no controlling correction is required.

## 10. Completion assessment

`AC-PD-A1` is `COMPLETE-DRAFT`. The next dependency-respecting unit is `AC-PD-A2`, the exact loopless cubic port-cycle expansion and collapse datum, including degree-two parallel fibres, components, auxiliary edges, size formulae, and preservation of the no-singleton-cut condition.
