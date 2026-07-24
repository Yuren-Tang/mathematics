# Fixed-channel component chains are contracted by ordinary root NNIs

## Research Lead channel-surgery theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-03`  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `d7009b74ff5d98a1ac6f68d1ab4b77b6602cfb70`

**Purpose.** Supply the missing source-level mechanism behind both:

1. zero-parent escape in the equality `(0,2,2)` fibre; and
2. the same-arc equal-neighbour defect found by independent audit `AC-AUDIT-XI-01` in the co-root fixed-channel theorem.

The mechanism does not select an arbitrary equal face.  It constructs a physical shortest chain between the two distinguished channel paths and contracts that chain one root NNI at a time.  The rank is the length of this witnessed channel-component chain.  It is not a distance in a finite state graph and no conclusion is inferred from finiteness alone.

---

## 1. Root-flow parity for one fixed channel

Fix a support pair

\[
h=ab
\]

and one complete root-valued cubic state.  Put

\[
H_h=F_a\triangle F_b.
\]

An edge belongs to `H_h` exactly when its root meets `h` in one support index.
At every cubic vertex the number of incident `H_h` edges is even, hence is zero or two.

### Lemma 1.1 — the unique inactive triangle

A vertex has `H_h`-degree zero exactly when its support triangle is

\[
I_h=[5]\setminus h.
\]

Every other support triangle has `H_h`-degree two.

### Proof

If a triangle contains neither endpoint of `h`, all three of its roots are disjoint from `h`.  Since there are exactly three remaining supports, this triangle is `I_h`.

If a triangle contains both endpoints of `h`, its root `h` is unselected and its other two roots meet `h` once.  If it contains exactly one endpoint of `h`, two of its roots meet `h` once.  Thus every non-`I_h` triangle has degree two. ∎

Call a degree-two vertex **channel-active** and an `I_h` vertex **channel-inactive**.

---

## 2. Root NNI absorbs one inactive vertex

Let a non-`H_h` edge `e=uv` join a channel-active vertex `u` to a channel-inactive vertex `v`.

Write

\[
I_h=\{i,j,k\},
\qquad
e=ij,
\]

and suppose the active triangle is

\[
\Delta_u=\{i,j,a\}
\]

for one `a in h`; the other endpoint has triangle `ijk`.

The unique root-valued opposite NNI is

\[
ija+ijk
\longrightarrow
ika+jka,
\]

with new central root

\[
ak.
\]

The new central root meets `h` once.  Both target triangles are channel-active.

### Lemma 2.1 — inactive-vertex absorption

Under this NNI, the old `H_h` passage through `u`

\[
ia\;--\;ja
\]

is replaced by the longer passage

\[
ia\;--\;ak\;--\;ja
\]

through both source vertices.  The two other roots `ik,jk` of the inactive vertex remain non-`H_h` frontier roots.

Consequently one channel-inactive vertex is absorbed into the selected channel component, and every stable outside dart remains available for continuation.

### Canonical `H_35` rows

For `h=35`, `I_h=124`.  The six possible absorption rows are

\[
\begin{array}{c|c}
123+124&134+234\\
125+124&145+245\\
134+124&123+234\\
145+124&125+245\\
234+124&123+134\\
245+124&125+145.
\end{array}
\]

The common root on each line is respectively `12,12,14,14,24,24`; the new central root is `34,45,23,25,13,15`.  Every row is an ordinary root-valued NNI.

---

## 3. Root NNI joins two active channel components

Let a non-`H_h` edge `e=uv` have both endpoints channel-active.  Each endpoint has one local `H_h` passage through its two exterior darts.

There are two cases.

1. **Distinct endpoint triangles.**  They share central root `e`.  The unique opposite root-valued NNI cross-connects the four selected exterior darts.  Its new central root is again outside `H_h`, because it is the symmetric difference of two `H_h` roots.
2. **Equal endpoint triangles.**  The root-valued equal-face branch swap is the alternative cross-connection.  The zero pairing is not used.

### Lemma 3.1 — component contraction

If the two local passages belong to distinct `H_h` components, the root alternative has the following exact topological effect.

- path plus closed cycle becomes one path with the same terminal endpoints;
- two closed cycles become one closed cycle;
- two terminal paths become two terminal paths with the other terminal matching.

No coefficient-only inference is involved: this is the literal transition system of the selected physical `H_h` edges at the two NNI vertices.

If the graph-category test at the root NNI returns a loop, parallel edge, bridge, exact cyclic `2/3/4`-cut or bounded degeneration, that named output is consumed instead of continuing.

---

## 4. The channel-component quotient

Let `R` be a connected rooted cubic carrier, possibly with selected terminal semiedges.  Form an auxiliary multigraph

\[
\mathcal Q_h(R)
\]

as follows.

### Nodes

- one node for each nontrivial connected component of `H_h cap R`;
- one singleton node for every channel-inactive vertex.

### Edges

Every physical edge of `R` outside `H_h` joins the nodes containing its two endpoints.  Loops and parallel quotient edges are retained as witnessed physical edges.

### Lemma 4.1 — quotient connectivity

If `R` is connected, then `mathcal Q_h(R)` is connected.

### Proof

Project any physical path in `R`.  An `H_h` edge stays inside one channel-component node.  Every other edge becomes a quotient edge.  A channel-inactive vertex is represented by its own node, so no part of the path disappears. ∎

---

## 5. Shortest physical component chain

Let `P_0,P_1` be two distinguished terminal path components of `H_h cap R`.  Choose a shortest simple path

\[
\mathfrak c=(X_0=P_0,X_1,\ldots,X_ell=P_1)
\]

in `mathcal Q_h(R)`, retaining for every quotient edge its exact stable physical source edge.

The nonnegative integer

\[
\boxed{\Lambda_h(\mathfrak c)=\ell}
\]

is the **physical component-chain rank**.

### Theorem 5.1 — chain contraction

Assume no route/profile or graph-category output has yet occurred.  If `ell>1`, there is one ordinary root NNI which returns a complete root state and replaces `mathfrak c` by a witnessed path of length `ell-1`.

### Proof

Consider the first physical quotient edge.

#### Case A — `X_1` is channel-inactive

Apply Lemma 2.1 at the physical edge from `X_0` to this inactive vertex.  The vertex is absorbed into the distinguished channel path.  The next stable non-`H_h` edge of the quotient path remains attached to the enlarged component.  Contracting `X_0X_1` gives the inherited path

\[
X_0',X_2,\ldots,X_ell
\]

of length `ell-1`.

#### Case B — `X_1` is a closed `H_h` component

Apply Lemma 3.1 at the witnessed physical edge between `X_0` and `X_1`.  The root alternative merges the closed cycle into the distinguished path.  All later quotient-path edges lie at untouched stable vertices of `X_1` or later components and remain available.  Again the first quotient edge is contracted.

Every move is root-valued.  A failed category test is a named terminal rather than a continuation. ∎

### Final edge

When `ell=1`, the witnessed physical non-`H_h` edge joins the two distinguished terminal paths directly.  Lemma 3.1 changes their terminal matching.  This is genuine target progress, not a decrease inferred from finiteness.

### Quantitative bound

The construction uses at most

\[
|V(R)|+c_h(R)-1
\]

ordinary root NNIs before the terminal matching changes, where `c_h(R)` is the number of nontrivial `H_h` components.  The sharper bound is the initial witnessed quotient distance.

---

## 6. Source fidelity

Every chain move is an ordinary labelled root NNI or equal-face root branch swap.  The established complete-state move contract retains or updates literally:

- every stable exterior dart and its ancestor identity;
- the live prescribed-parent topology;
- the selected physical support channel `h`;
- cap vertices, cap darts and ordered cap identity;
- current route/profile and channel-component partitions;
- missing-index and trace-assignment coordinates;
- stored-prefix identity.

After every move, route, cap and graph category are recomputed.  A cap-compatible state, separating channel, invalid category or named bounded object is consumed immediately.

The theorem uses no support switch during the chain.  Therefore there is no orbit-minimum issue, exterior switch-energy issue, zero-overlap issue or missing-index migration ambiguity.

---

## 7. Co-root marked-arc corollary

Let `p,q` be the two disjoint marked roots in one fixed physical rescue system `H_h`, and suppose they lie on the same channel component with the prescribed locked route.

Cut the interiors of the two marked edges.  The marked channel component becomes two distinguished terminal paths `P_0,P_1`; every other nontrivial `H_h` component is a closed cycle.

If the graph with the two marked edge interiors removed is disconnected, the two marked edges expose an exact bridge/two-cut or bounded shore, already in the terminal ledger.  Otherwise apply Theorem 5.1.

At the final chain edge, the matching of the four marked endpoints changes.  Reinsert the marked edges.

- One resulting matching places `p,q` in different closed `H_h` components, giving the separating-channel parent repair.
- The other gives the opposite marked route, which is cap-compatible under the fixed-route blocking hypothesis.

Thus every nonterminal common-component co-root lock has a finite root-NNI history to a separating channel or route/profile output.

### Audit-witness repair

In the exact Heawood audit witness with `h=14`, marked edges `1-6:12`, `2-3:34`, the edge `6-7:23` joins the two cut marked arcs.  Its endpoint triangles are `123,234`.  The root NNI

\[
123+234\longrightarrow124+134
\]

has central root `23 -> 14` and reattaches

\[
5-6:5-6\longmapsto5-7,
\qquad
7-8:7-8\longmapsto6-8.
\]

The marked route changes exactly from

\[
(1,2)\mid(3,6)
\]

to

\[
(1,3)\mid(2,6).
\]

The resulting graph is connected, simple, cubic, bridgeless, has girth five and cyclic edge-connectivity five.  Its canonical stable-state digest is

`72e67089476af09b33daf91316b9b71b687f98291457e4514c8a384bba626ec0`.

The same-arc equal face `9-14` found by the audit is therefore not selected.  The chain theorem selects a physical connector between the two marked arcs, exactly the datum missing from the false matching-only lemma.

---

## 8. Zero-parent terminal-path corollary

Normalize

\[
(A,B,C,D)=(13,13,23,23),
\qquad h=35.
\]

Remove the two active vertices and retain the four stable branch semiedges.  Call the complementary carrier `R`.

If `R` is disconnected, one component receives at most two of the four branch semiedges.  This gives a bridge, an exact two-edge cut, or a bounded low-port shore, already in the category ledger.  Hence a complete category-safe nonterminal state has connected `R`.

In a full zero-parent `H_35` lock, the physical terminal matching in `R` is

\[
AB\mid CD.
\]

Thus `H_35 cap R` has two distinguished terminal paths

\[
P_a:A--B,
\qquad
P_b:C--D,
\]

plus closed cycles.  Apply Theorem 5.1.  The final NNI changes the terminal matching to one of

\[
AC\mid BD,
\qquad
AD\mid BC.
\]

Choose the equal-face crossed root topology with the same matching, using zero or one active root branch-swap NNI.  The closed `H_35` system then has two components, each containing exactly one `13` branch and one `23` branch.

Switch either component by `35`.  Up to the fixed ordered symmetry, the active word becomes

\[
(15,13,25,23),
\]

so

\[
15+13=25+23=35.
\]

The final ordinary NNI realizes the literal `AB|CD` parent with central root `35`.

---

## 9. Why the independent-audit defect is respected

The audit correctly refuted the statement that an arbitrary remote equal face is automatically route-changing or one-sided.  The present theorem never makes that inference.

It records:

1. the actual two marked arcs or terminal paths;
2. the unique inactive triangle `I_h`;
3. every intermediate channel component;
4. an exact physical connector edge at every step.

A same-arc equal face is simply ignored.  The selected final connector has endpoints on different distinguished channel paths by construction, so its root NNI genuinely changes the terminal matching.

---

## 10. Assurance boundary

### Proved here at Research Lead authorial level

- the unique inactive-triangle classification;
- inactive-vertex absorption by one root NNI;
- active component contraction by one root NNI or equal branch swap;
- the connected physical quotient and strict chain-length rank;
- co-root marked-arc route/separation escape;
- zero-parent terminal-matching escape;
- an explicit repair of the audit witness.

### Not used

- the false arbitrary equal-face route-or-split theorem;
- the quarantined `Omega` orbit minimum;
- `Xi` as a totality provider;
- a `2--0` cancellation;
- a lower-order root-flow call;
- track erasure;
- generic NNI connectivity;
- finite-state or SCC distance;
- `Q_N`, `M_N`, `d_N`, nested bubbles or terminal frames.

### Required downstream

- PDL reconstruction of the quotient/path contraction with full stable-dart maps;
- independent audit of the inactive-vertex and final-terminal-matching cases;
- complete cap/route/category interface audit.

No established universal five-support/five-CDC theorem, Lean theorem, Curator movement, manuscript, release, tag, arXiv, DOI, peer-review or publication status is claimed.