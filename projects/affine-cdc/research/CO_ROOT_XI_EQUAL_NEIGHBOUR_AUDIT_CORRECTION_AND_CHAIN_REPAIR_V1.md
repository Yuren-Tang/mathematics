# The audited `Xi` equal-neighbour lemma is withdrawn and replaced by marked-arc component chains

## Research Lead scope correction and repair v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-03`  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `e24123ef583d3ee08efe9cf3608283593b5aec71`  
**Independent audit consumed:** `Yuren-Tang/mathematics:audit/affine-cdc-xi-co-root-v1@53be22a0f65b85068b11e5f781579618967db9dd`

---

## 1. Accepted audit correction

The independent audit correctly refutes the universal statement:

> every equal bad face admits either a marked-route exit or a one-sided `H_14` component switch after zero or one root branch swap.

The matching-only proof omitted the locations of the two marked edges on the two outside arcs.  If both marked edges lie on the same outside arc, both root placements may remain one common component with the same marked route.

Therefore the following are withdrawn as controlling totality statements:

- Theorem 5.1 of `DDD_LOCK_H14_SWITCH_INVARIANT_DESCENT_THEOREM_V1.md` in its arbitrary-equal-face form;
- the equal-neighbour totality step of `PURE_NNI_ALL_INDEX_AMBIENT_ESCAPE_MASTER_THEOREM_V3.md`;
- the corresponding PDL matching-only reconstruction at `fee97446...`;
- the claim that `Xi` alone supplies a strict macro at every nonterminal lock.

The audit defect is material and was not visible when the issue-#75 return was filed.

---

## 2. Retained exact mathematics

The audit independently verified and this correction retains:

1. uniqueness of the transported fixed-channel frame;
2. vertexwise invariance of `Xi` over the whole physical component and its exterior;
3. all six distinct-neighbour root NNI rows with `Delta Xi=-2`;
4. the bad-free `124` / roots `12,24` route contradiction;
5. ordinary root-NNI and support-switch cap/dart/parent/prefix contracts;
6. the separation between the co-root and zero-parent fibres.

Thus `Xi` remains a valid strict arithmetic certificate whenever a productive row is source-legally available.  It is no longer the universal source-selection theorem.

---

## 3. Exact audit witness

In the frozen Heawood flow, take

\[
h=14,
\qquad p=1-6:12,
\qquad q=2-3:34.
\]

The equal bad face `9-14:23` has endpoint types `123,123`.  Both marked edges lie on one outside arc.  Its root branch swap preserves the common marked component and route.  Hence the old one-sided collar cannot start.

This witness is retained as a permanent counterexample to the arbitrary-equal-face lemma.

---

## 4. The missing datum and the replacement selection rule

Cut the two marked `H_14` edges `p,q`.  Their common channel cycle becomes two distinguished marked arcs.

The missing source datum is not the outside perfect matching alone.  It is the complete physical distribution

\[
(\text{arc containing }p^+,p^-;
 \text{arc containing }q^+,q^-)
\]

together with every intervening channel component and inactive vertex.

The replacement theorem is `FIXED_CHANNEL_COMPONENT_CHAIN_ROOT_NNI_THEOREM_V1.md`:

1. form the connected quotient whose nodes are `H_14` components and the unique inactive type `235` vertices;
2. choose a shortest physical chain between the two marked arcs;
3. absorb every inactive vertex by one ordinary root NNI;
4. merge every intervening closed `H_14` cycle by one ordinary root NNI or equal branch swap;
5. use the final physical connector, whose endpoints lie on different marked arcs, to change the marked terminal matching.

The chain length decreases at every nonterminal move.  No arbitrary same-arc equal face is selected.

---

## 5. Direct repair of the audit witness

For the exact audit graph, stable edge `6-7:23` joins the two marked arcs.  Its endpoint triangles are

\[
123,\qquad234.
\]

Perform the ordinary root NNI

\[
123+234\longrightarrow124+134
\]

with central root

\[
23\longmapsto14.
\]

Keep stable darts `1-6:12` and `7-12:34`; reattach

\[
5-6:5-6\longmapsto5-7,
\]

\[
7-8:7-8\longmapsto6-8.
\]

Cutting the marked edges after this NNI gives route

\[
(1,3)\mid(2,6)
\]

instead of

\[
(1,2)\mid(3,6).
\]

Thus the fixed-route lock exits immediately.  The resulting graph is connected, simple, cubic, bridgeless, of girth five and cyclic edge-connectivity five.  The stable-state digest is

`72e67089476af09b33daf91316b9b71b687f98291457e4514c8a384bba626ec0`.

This does not invalidate the audit witness; it demonstrates the corrected global selection rule.  The unproductive face `9-14` is ignored, and a connector between different marked arcs is selected instead.

---

## 6. Repaired co-root theorem

### Theorem `FC-PURE-NNI-CO-ROOT-COMPONENT-CHAIN-ESCAPE`

Every complete category-safe fixed-order co-root prescribed-parent lock admits a finite source-faithful same-order history of ordinary root NNIs and, only after a separating channel appears, one legal support-component switch and the literal parent NNI, ending in one of:

1. a root flow on the literal prescribed parent;
2. a cap-compatible route/profile state;
3. a named cyclic `2/3/4`-cut or bounded terminal.

### Proof

Fix one physical rescue channel and cut its two marked edges.  A nonterminal category-safe state has connected cut carrier; otherwise the two marked edges expose a bridge/two-cut or bounded shore.

Apply the marked-arc corollary of the component-chain theorem.  Every intermediate root NNI contracts the witnessed physical chain.  The final connector changes the marked endpoint matching.  After reinserting the marked edges, this is either a separating channel or a route/profile exit.  Apply the existing Phase-B consumer in the separating case. ∎

This proof uses neither the false equal-face lemma nor `Xi` totality.  The retained `Xi` rows remain optional strict shortcuts.

---

## 7. Revised status of prior files

### Controlling for arithmetic only

- `DDD_LOCK_H14_SWITCH_INVARIANT_DESCENT_THEOREM_V1.md`, Sections 1--4, the conditional coefficient movies, and the bad-free route calculation;
- PDL `AC_PD_5CDC_V7_3_FIXED_CHANNEL_XI_RECONSTRUCTION.md` only for independently verified frame/invariance/table portions.

### Rejected as universal source selection

- the arbitrary equal-neighbour route-or-split implication;
- deterministic `Xi` totality based on selecting any bad equal face;
- the old `N`-strict-macro bound as an unconditional theorem.

### New controlling totality provider

- `FIXED_CHANNEL_COMPONENT_CHAIN_ROOT_NNI_THEOREM_V1.md`;
- this correction.

---

## 8. Quantitative replacement

The old conditional bound counted at most `N` strict `Xi` macros.  The repaired construction instead has the exact witnessed bound

\[
\Lambda_h,
\]

the current shortest component-chain length between marked arcs, followed by at most one separating switch and one parent NNI.

Every nonterminal chain move lowers `Lambda_h` by one.  This is a physical channel-complex rank; it is not an SCC distance and does not rely on finite-state recurrence.

---

## 9. Assurance boundary

The repaired co-root theorem is at Research Lead authorial level only.  The audit disproved the previous proof, not this later chain construction.  PDL must reconstruct and an independent reviewer must attack:

- inactive-type absorption;
- stable continuation of the quotient path;
- final marked-matching change;
- every cap/route/category output;
- literal parent and stored-prefix integration.

No prior independent-verification status is restored automatically.