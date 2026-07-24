# AC-PD v7.4 — fixed-channel component-chain theorem reconstruction

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Workstream:** `AC-PD-5CDC-V7.4-01`  
**Frozen RL source:** `research/affine-cdc-five-cdc-v1@02b37476198e9eaa2b4cd8d2a2edd76782bdcd49`  
**Permanent negative boundary:** `audit/affine-cdc-xi-co-root-v1@53be22a0f65b85068b11e5f781579618967db9dd`  
**Classification:** `COMPLETE-DRAFT OF THE SOURCE-LEVEL COMPONENT-CHAIN THEOREM / SUBJECT TO NEW INDEPENDENT AUDIT`.

The theorem below replaces, and does not repair, the false arbitrary-equal-face
route-or-split lemma.  It does not use `Xi` as a totality provider.  The selected
move is determined by one physical chain between two distinguished channel
paths, not by an arbitrary equal face.

---

## 1. Fixed-channel parity

Fix one support pair

\[
h=ab\in R_5
\]

and one complete root-valued cubic source state.  Put

\[
H_h=F_a\triangle F_b.
\]

A root edge belongs to `H_h` exactly when its root meets `h` in one support
index.

Let a cubic source vertex have support triangle

\[
T=\{i,j,k\}.
\]

Its three incident roots are `ij,ik,jk`.  The number meeting `h` once is even:

- if `T` is disjoint from `h`, it is zero;
- if `T` contains exactly one support of `h`, exactly two incident roots meet
  `h` once;
- if `T` contains both supports of `h`, the edge `h` is inactive and the other
  two roots meet `h` once.

Hence every source vertex has `H_h` degree `0` or `2`.

### Theorem 1.1 — unique inactive triangle

The unique zero-degree triangle is

\[
I_h=[5]\setminus h.
\]

Every other support triangle is channel-active.  Therefore each nontrivial
component of `H_h` is a physical path or cycle; no active component branches.

This is vertexwise root arithmetic, not a statement about an abstract support
quotient.

---

## 2. Rooted carrier and physical quotient

Let `R` be a connected labelled cubic carrier, possibly with selected terminal
semiedges.  Every physical edge retains:

- its stable edge identity;
- its two ordered endpoint darts;
- its current root value;
- its ancestry in the stored prefix.

Define the physical quotient

\[
\mathcal Q_h(R)
\]

as a witnessed multigraph.

### Nodes

1. one node for each nontrivial connected component of `H_h\cap R`;
2. one singleton node for each channel-inactive vertex of type `I_h`.

### Edges

Every stable physical edge outside `H_h` becomes one quotient edge joining the
nodes containing its endpoint darts.  Its stable edge identity is stored as the
edge witness.  Parallel quotient edges and quotient loops are retained.

A quotient loop is not used in a simple chain.  If the physical graph itself
has a loop, bridge, forbidden parallel degeneration or bounded low-port shore,
the existing exact category consumer fires before continuation.

### Lemma 2.1 — connectedness

If the physical carrier `R` is connected, then `Q_h(R)` is connected.

Project any physical path in `R`: an `H_h` edge stays in one active-component
node, and every non-`H_h` edge becomes its witnessed quotient edge.  Inactive
vertices remain singleton nodes, so no segment disappears.

---

## 3. One fixed inherited chain

Let `P_0,P_1` be two distinguished terminal-path components of `H_h\cap R`.
Choose one shortest simple quotient path once:

\[
\mathfrak c_0=(X_0=P_0,X_1,\ldots,X_\ell=P_1).
\]

For every `i=1,...,ell`, store the exact stable non-`H_h` physical connector

\[
c_i
\]

between `X_{i-1}` and `X_i`, including its endpoint darts.

The controlling rank is not a recomputed quotient distance.  At stage `r`, it
is the number of still-unconsumed connectors in the inherited list:

\[
\Lambda_r=\ell-r.
\]

A source move is accepted as a chain contraction only when it consumes `c_{r+1}`
and leaves the exact stable witnesses `c_{r+2},...,c_ell` as a valid physical
path to `P_1`.

This converts the shortest-path existence statement into a literal witnessed
graph rank.

---

## 4. Active/inactive contraction

Suppose the first connector `c_1=e=uv` joins an active endpoint `u` in `X_0`
to an inactive singleton `v` of type

\[
I_h=\{i,j,k\}.
\]

Write the central root as `ij`.  The active endpoint triangle is

\[
\{i,j,a\},\qquad a\in h.
\]

The four exterior roots are

\[
ia,ja,ik,jk.
\]

The two opposite pairings have central values

\[
ak\in R_5
\]

and the four-support co-root `ijak`; hence the unique root alternative is

\[
ija+ijk\longrightarrow ika+jka.
\]

The old channel passage

\[
ia--ja
\]

is replaced literally by

\[
ia--ak--ja.
\]

Both target vertices are active.  The two remaining stable edges at the old
inactive vertex retain roots `ik,jk`, which are disjoint from `h` and therefore
remain non-`H_h` connectors.

### Lemma 4.1 — exact inherited continuation

Let `c_2` be the next quotient connector.  It is necessarily one of the other
stable non-`H_h` edges incident with the inactive source vertex.  Although both
`c_1` and `c_2` meet the source vertex modified by the NNI:

1. the stable edge `c_2` is not deleted;
2. its outside endpoint and outside dart are fixed;
3. its root is unchanged and remains non-`H_h`;
4. its moved endpoint dart is attached to one of the two new active vertices;
5. both new active vertices lie in the enlarged component `X_0'` through the
   new channel edge `ak`.

Thus

\[
(X_0',X_2,\ldots,X_\ell;\ c_2,\ldots,c_\ell)
\]

is a literal inherited witnessed path of length `ell-1`.  No connector is
reselected and no distance is recomputed.

The unused third non-`H_h` edge at the inactive vertex remains an ordinary
frontier edge of `X_0'`; it does not affect the inherited chain.

---

## 5. Active/active contraction

Suppose `c_1=e=uv` joins two distinct active `H_h` components.  The central root
`e` is outside `H_h`; at each endpoint the other two incident roots are the
local channel passage.

### Distinct endpoint triangles

If the endpoint support triangles are distinct, write them as

\[
\{i,j,k\},\qquad \{i,j,l\},
\]

sharing the non-channel root `ij`.  The unique root-valued opposite pairing is

\[
ik--il,\qquad jk--jl,
\]

with new central root `kl`.  The other opposite pairing has a four-support
co-root central value.  Because the two external roots paired at the new
central edge both belong to `H_h`, their symmetric difference `kl` is outside
`H_h`.

### Equal endpoint triangles

If both endpoints have the same support triangle, the three labelled
four-dart pairings are:

1. the current root placement;
2. the other root branch-swap placement;
3. the equal-root pairing with central value zero.

Only the second placement is used.  It is an ordinary root-valued equal-face
branch swap and never traverses the zero placement.

### Lemma 5.1 — physical component effect

When the two local channel passages belong to distinct components, the selected
root cross-connection has the literal effects:

- terminal path plus closed cycle becomes one terminal path with the same two
  terminal endpoints;
- closed cycle plus closed cycle becomes one closed cycle;
- two terminal paths become two terminal paths with one of the other two
  ordered terminal matchings.

The new central edge remains non-`H_h`; all other channel edges are unchanged.

### Lemma 5.2 — entry and exit cannot share the modified cycle vertex

Assume `X_1` is an active cycle and the inherited path continues through
connector `c_2`.  Every active cubic vertex has exactly two `H_h` incidences and
therefore exactly one non-`H_h` incidence.  The entry connector `c_1` already
uses the unique non-channel incidence at its endpoint in `X_1`.  Hence the
distinct connector `c_2` cannot be incident with the same source vertex.

Consequently `c_2` and every later connector lie at untouched stable vertices
of `X_1` or later components.  After the NNI merges `X_1` into `X_0`, the exact
list

\[
(X_0',X_2,\ldots,X_\ell;\ c_2,\ldots,c_\ell)
\]

remains a witnessed path of length `ell-1`.

The NNI cannot accidentally merge a later component: its new channel
cross-connections use only the two passages in `X_0` and `X_1`, while its new
central edge is outside `H_h`.

---

## 6. Final connector theorem

When one inherited connector remains, its endpoints lie on the two distinct
distinguished terminal paths `P_0,P_1`.  Cut the two local channel passages at
the connector endpoints.  The outside channel subgraph gives four labelled
subpaths ending at the four ordered terminals.

The current local pairing restores the current matching of `P_0` and `P_1`.
The unique root opposite NNI, or the equal-triangle root branch swap, pairs each
half-passage of `P_0` with one half-passage of `P_1`.  Therefore it gives one of
the other two perfect matchings of the four ordered terminals.

### Theorem 6.1 — final matching necessarily changes

The final root move cannot preserve the old terminal matching:

- for distinct endpoint triangles, the old pairing and the unique root opposite
  pairing are different labelled pairings;
- for equal endpoint triangles, the branch swap is by definition the second
  root placement, while the zero placement is excluded;
- the two local passages belong to distinct terminal components, so this is not
  the same-arc configuration refuted by audit `AC-AUDIT-XI-01`.

Thus the final connector supplies genuine ordered-terminal progress.

---

## 7. Source-field contract

Every chain step is one labelled root-valued `2--2` NNI or equal-face root
branch swap.  It preserves or updates literally:

- graph order;
- every stable edge identity;
- every stable exterior dart and its ancestor;
- the selected physical support channel `h`;
- the live prescribed-parent topology;
- cap vertices, cap darts and their order;
- route/profile and channel-component fields after recomputation;
- graph-category and exact terminal flags;
- missing-index and trace-assignment fields;
- the stored-prefix map.

After each move, the exact graph/category, route and cap tests are run.  A loop,
parallel degeneration, bridge, cyclic `2/3/4` cut, cap-compatible route or
bounded object is consumed immediately rather than treated as a continued
chain state.

No support switch occurs inside the chain theorem.  In particular there is no
switch-orbit energy issue, missing-index migration issue or hidden coefficient
move.

---

## 8. Component-chain theorem

### Theorem `FC-COMPONENT-CHAIN-ROOT-NNI`

Let `R` be a connected category-safe labelled rooted cubic carrier and let
`P_0,P_1` be two distinguished terminal-path components of `H_h\cap R`.  Then a
finite source-faithful same-order history using only ordinary root NNIs and
equal-face root branch swaps ends in exactly one of:

1. a named route/profile, cut or bounded terminal;
2. a category-safe state in which the ordered terminal matching of `P_0,P_1`
   has changed.

Choose one initial shortest simple physical quotient path and retain all
connector witnesses.  Every nonterminal pre-final move consumes its first
connector and lowers the inherited-chain rank by one.  The final move changes
the terminal matching.

The theorem uses no cancellation, lower-order call, track erasure, generic NNI
connectivity, finite-state recurrence, SCC distance, `Q_N`, `M_N`, `d_N`,
nested bubble or terminal frame.

---

## 9. Assurance boundary

Closed here at PDL proof-development level:

- fixed-channel degree `0/2` parity;
- unique inactive triangle;
- connected physical quotient;
- all active/inactive and active/active source types in theorem form;
- exact inherited stable-connector chain;
- strict witnessed chain rank;
- final ordered-terminal matching change;
- complete source-field contract.

Not asserted here:

- independent audit acceptance;
- the two inverse-parent corollaries before their separate reconstruction;
- an established cubic five-support or five-CDC theorem.