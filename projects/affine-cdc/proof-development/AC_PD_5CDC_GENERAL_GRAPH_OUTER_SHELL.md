# AC-PD-5CDC — support-count-preserving general-graph outer shell

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Programme:** finite bridgeless `5`-cycle-double-cover endpoint  
**Frozen Research Lead input:** `research/affine-cdc-five-cdc-v1@71a10f9ba86c1d2b8b7885e78fa9baa303c77818`  
**Classification:** `COMPLETE-DRAFT / GENERAL FINITE BRIDGELESS OUTER SHELL CLOSED`.

This dossier proves that the reconstructed cubic five-support theorem implies
the standard finite bridgeless `5`-cycle-double-cover statement without
increasing the number of cover members.

---

## 1. Convention

A **circuit** is a connected `2`-regular subgraph.  A **cycle**, in the standard
cycle-double-cover / `k`-cycle-double-cover convention, is an even subgraph and
may be a disjoint union of circuits.  A `5-CDC` is a family of at most five even
subgraphs in which every edge occurs exactly twice.

Therefore an indexed five-support cover

\[
(F_1,F_2,F_3,F_4,F_5)
\]

with every `F_i` even and every edge in exactly two members is literally a
`5-CDC`.  Empty or repeated members are harmless.  Decomposing each member into
connected circuits is neither required nor desirable, since it can increase
the number of members.

---

## 2. Cubic input

Assume the PDL-reconstructed cubic theorem:

> Every finite connected loopless bridgeless cubic multigraph has five indexed
> vertex-even supports, with every edge in exactly two supports.

Apply this componentwise using the same index set `{1,2,3,4,5}`.  Taking the
union of support `i` over all components preserves vertex evenness and exact
edge multiplicity.  Thus the theorem already holds for every finite, possibly
disconnected, loopless bridgeless cubic multigraph.

---

## 3. Remove loops

Let `G` be a finite bridgeless multigraph.  Delete all loops and call the result
`G_0`.

- Loops cross no edge cut.
- Every nonloop singleton cut of `G_0` would be the same singleton cut in `G`.
- Hence `G_0` is loopless and bridgeless on every edge-bearing component.
- No active vertex has degree one.

Isolated vertices are irrelevant.

---

## 4. Port-cycle expansion

For every active vertex `v` of degree `d>=2`, choose a cyclic order of its
incident nonloop edge occurrences.  Replace each incidence by one port vertex.

- The original edge `e=uv` becomes one external edge `lambda(e)` between its two
  port vertices.
- For `d>=3`, join the `d` ports over `v` in one internal cycle.
- For `d=2`, join the two ports by two distinct parallel internal edges.

Call the expanded multigraph `H`.

### Lemma 4.1 — cubic and loopless

Every port vertex has one external edge and two internal cycle edges, hence
degree three.  Original nonloop edges join different original endpoint fibres,
and all auxiliary edges join distinct port vertices in one fibre.  Thus `H` is
loopless and cubic; parallel edges are allowed.

### Lemma 4.2 — bridgelessness

Every internal fibre edge lies on its fibre cycle, including the two-edge cycle
used at degree two.

Let `lambda(e)` be an external edge.  Since `e` is not a bridge of `G_0`, it lies
on an ordinary closed trail, and hence on a circuit after deleting repetitions.
Lift the circuit's original edges to external edges of `H`.  At every visited
original vertex, join the entering and leaving ports by one path in the fibre
cycle.  This gives a closed trail in `H` containing `lambda(e)`.  Therefore the
external edge is not a bridge.

Thus every edge-bearing component of `H` is finite, loopless, bridgeless and
cubic.

---

## 5. Apply the cubic theorem

Apply the cubic theorem componentwise to `H`.  Obtain exactly five indexed
supports

\[
F'_1,\ldots,F'_5\subseteq E(H)
\]

such that:

- each `F'_i` is vertex-even;
- every edge of `H` occurs in exactly two `F'_i`.

Because `H` is loopless, the standard cut-sum identity gives:

\[
F'_i\text{ vertex-even}
\iff
|F'_i\cap\delta_H(X)|\equiv0\pmod2
\quad\text{for every }X\subseteq V(H).
\]

Thus every upstairs support is cut-even.

---

## 6. Memberwise collapse projection

Let

\[
\pi:V(H)\to V(G_0)
\]

send every port to its original vertex.  For each index define

\[
F_i^0=\{e\in E(G_0):\lambda(e)\in F'_i\}.
\]

### Theorem 6.1 — cut parity descends

For every vertex set `S subseteq V(G_0)`, an original edge `e` crosses
`delta_(G_0)(S)` exactly when `lambda(e)` crosses

\[
\delta_H(\pi^{-1}S).
\]

No internal fibre edge crosses this latter cut.  Hence there is a bijection

\[
F_i^0\cap\delta_{G_0}(S)
\longleftrightarrow
F'_i\cap\delta_H(\pi^{-1}S).
\]

The right side has even cardinality, so `F_i^0` is cut-even.

### Theorem 6.2 — exact multiplicity descends

For every nonloop original edge:

\[
e\in F_i^0
\iff
\lambda(e)\in F'_i.
\]

The lifted edge belongs to exactly two upstairs supports, so `e` belongs to the
same two indexed downstairs supports.

Therefore

\[
(F_1^0,\ldots,F_5^0)
\]

is a five-member cut-even double cover of the loopless core `G_0`.

---

## 7. Reinsert loops

Let `L` be the set of loops deleted from `G`.  Choose two fixed indices, say
`1,2`, and put

\[
F_1=F_1^0\cup L,
\qquad
F_2=F_2^0\cup L,
\qquad
F_i=F_i^0\quad(i=3,4,5).
\]

A loop crosses no cut, so every `F_i` remains cut-even.  Each loop lies in
exactly supports `1` and `2`; each nonloop edge retains its previous two-support
membership.

Thus the five-index family is preserved exactly.

---

## 8. Full outer-shell theorem

### Theorem 8.1

If every finite connected loopless bridgeless cubic multigraph has an indexed
five-support double cover, then every finite bridgeless multigraph has a
`5`-cycle double cover.

### Proof

Delete loops, port-cycle-expand the loopless core, apply the cubic theorem
componentwise, project each of the same five supports through collapse, and add
all loops to two fixed members.  Sections 3--7 prove evenness and exact double
coverage at every stage. ∎

---

## 9. Dependency consequence

Combining this theorem with:

- `AC_PD_5CDC_R1_ONE_CROSS_STRUCTURAL_REDUCTION.md`;
- `AC_PD_5CDC_R2_TO_R1_CAP_ROUTE_CONSUMER_AUDIT.md`;
- the theta base and simultaneous `Q_N/P_N` induction;

produces the complete PDL proof-draft endpoint:

\[
\boxed{\text{Every finite bridgeless multigraph has a 5-cycle double cover.}}
\]

---

## 10. Trust boundary

### Closed here

- standard even-subgraph interpretation of `5-CDC`;
- loop deletion;
- explicit finite port-cycle cubic expansion;
- proof that the expansion is loopless, cubic and bridgeless;
- componentwise use of one common five-index set;
- vertex-even to cut-even conversion;
- memberwise support projection;
- exact multiplicity preservation;
- loop reinsertion into two fixed supports;
- support-count-preserving deduction of the general theorem.

### Still required before project acceptance

- updated global proof DAG and fixed PDL snapshot;
- independent adversarial audit of the full proof;
- Curator integration and AC-DIR disposition;
- any Lean or manuscript programme separately authorised downstream.

This file is a proof-development result, not an independent audit, canonical
acceptance, publication or release claim.
