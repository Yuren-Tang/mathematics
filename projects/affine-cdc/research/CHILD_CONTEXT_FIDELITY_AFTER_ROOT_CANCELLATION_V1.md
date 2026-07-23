# Child-context fidelity after one internal root cancellation

## Research Lead witnessed-induction interface v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**PDL interface:** `AC-PD-5CDC-HW1-CF`.

**Parents:**

- `ROOT_SURGERY_AUTOMATIC_CATEGORY_SAFETY_V1.md`;
- `ARBITRARY_EDGE_THREE_RECONNECTION_CATEGORY_V1.md`;
- `GLOBAL_SMALL_CUT_COMPLETION_AND_GLUING_V1.md`;
- `ROUTE_CHANGE_TERMINAL_CONTEXTUAL_TRANSFER_V1.md`;
- `NESTED_CANCELLATION_BUBBLE_COMPRESSION_V1.md`;
- the exact parallel-closure semantics of `GLOBAL_CAP_LIFT_INTERFACE_COMPATIBILITY_V1.md`.

**Status:** exact construction and category fidelity of the lower-order witnessed child. An internal equal-face cancellation in a witnessed one-cross context either produces a genuine lower-order context satisfying the structural hypotheses of the witnessed proposition `Q_(N-2)`, or already exposes a parent-level small-cut/bounded/route terminal. The child retains the same ordered outer four-pole boundary, cap index, selected reconnection matching, inherited root flow and fixed-route datum. A successful child return lifts through the stored cancellation interface by witnessed bubble compression.

Separator exits arising later inside the child are returned with an explicit ancestor incidence map. The assertion that every such tagged descendant separator is an accepted exit for every ancestor frame is the separate `HW2` genealogy/gluing audit and is not silently claimed here.

---

## 1. Parent parallel-closure context

Fix an ordered cubic four-pole

\[
P
\]

with ordered outer semiedges

\[
t_1,t_2,t_3,t_4.
\]

Let

\[
C_i
\]

be the distinguished two-vertex cap of matching `M_i`, and let

\[
E_j
\]

be one selected zero-vertex reconnection matching.

The parent target and inherited cross closure are

\[
\widehat G=P\cup C_i,
\qquad
G_j=P\cup E_j.
\]

Assume:

1. `widehat G` is connected, loopless, bridgeless and cubic;
2. `G_j` is connected, loopless, bridgeless and cubic;
3. `G_j` carries one specified root-valued flow `lambda`;
4. the cap block, terminal ordering and physical fixed route are recorded;
5. every current-flow surgery is internal relative to the four ordered outer semiedges.

Let

\[
N=|V(\widehat G)|.
\]

---

## 2. Internal equal-face cancellation

Suppose two adjacent internal vertices

\[
u,v\in V(P)
\]

carry the same root triangle under `lambda` and are cancelled along their common root edge.

The two pairs of equal-labelled exterior incidences are reconnected. Let

\[
P^-
\]

be the resulting ordered four-pole. Define the parallel descendant closures

\[
G_j^-=P^-\cup E_j,
\qquad
\widehat G^-=P^-\cup C_i.
\]

The inherited flow on `G_j^-` is denoted

\[
\mu.
\]

### Lemma 2.1 — boundary fidelity

The cancellation preserves literally:

- the four ordered outer semiedge objects;
- their root labels;
- the cap index `i`;
- the selected reconnection index `j`;
- the distinguished cap block;
- every exterior rooted attachment.

Moreover

\[
|V(G_j^-)|=|V(G_j)|-2,
\qquad
|V(\widehat G^-)|=N-2.
\]

### Proof

The selected cancellation is internal to the four-pole in the relative current-flow descent. It deletes only `u,v` and reconnects their four internal/exterior incidences. No ordered outer semiedge is deleted, paired to another terminal, or relabelled. The external gadgets `E_j,C_i` are untouched. Exactly two source vertices are removed from both parallel closures. ∎

---

## 3. Inherited cross closure

By the equal-face cancellation theorem, `mu` is root-valued on `G_j^-`.

### Lemma 3.1 — root category

`G_j^-` is loopless and every connected component is bridgeless and carries the restricted nowhere-zero root flow.

### Proof

Apply `ROOT_SURGERY_AUTOMATIC_CATEGORY_SAFETY_V1.md`, Theorem 4.2. ∎

There are now two structural branches.

---

## 4. Disconnected cross output gives a parent small-cut exit

Assume `G_j^-` is disconnected.

Before reconnection, delete `u,v` from `G_j`. The outside graph has exactly two connected components

\[
A,B,
\]

each incident with exactly two of the four local cancellation incidences. The equal-label reconnection pairs stay within `A` and within `B`; otherwise the output would be connected.

The two edges of the fixed outer reconnection `E_j` also lie wholly inside `A` or `B`, because they are edges of the deleted outside graph. Therefore the set of outer terminals whose endpoints lie in `A` is a union of blocks of the matching `M_j`. Its cardinality is

\[
0,\ 2,\ \text{or }4.
\]

### Case 4.1 — zero or four outer terminals

Choose the outside component containing no outer terminal endpoints. In the parent target `widehat G`, its vertex shore is attached to the rest only by the two old edges leading to `u,v`.

Hence `widehat G` has a two-edge cut.

### Case 4.2 — exactly two outer terminals

Let `S` be the vertices of `P` belonging to `A`. In the target cap closure `widehat G`, the shore boundary consists of:

1. the two old attachment edges from `A` to `u,v`;
2. the two terminal-to-cap edges incident with the two outer terminals of `A`.

Thus

\[
|\delta_{\widehat G}(S)|=4.
\]

If both shores contain cycles, this is a cyclic four-cut. If one shore is acyclic, the cubic shore degree formula identifies the explicit bounded low-port gadget.

### Theorem 4.1 — split-output disposition

If the inherited cross cancellation output is disconnected, no recursive child is formed. The parent target already lies in an accepted two-cut, cyclic four-cut, or bounded acyclic branch.

### Important point

One must not select one root-solved output component and call it the child context. The outer cap may reconnect the two output shores. The correct conclusion is the parent small-cut/bounded branch above.

---

## 5. Connected cross output and target category

Assume now that `G_j^-` is connected. By Lemma 3.1 it is a valid connected loopless bridgeless cross closure carrying the specified inherited root flow `mu`.

It remains to classify the parallel target closure `widehat G^-`.

Apply `ARBITRARY_EDGE_THREE_RECONNECTION_CATEGORY_V1.md` to the parent target graph `widehat G` and the edge `uv`. The equal-face cancellation matching is one of the three perfect matchings of the four exposed incidences. Its corresponding direct reconnection closure is exactly `widehat G^-`.

### Theorem 5.1 — target-category alternative

Exactly one of:

1. `widehat G^-` is connected, loopless, bridgeless and cubic of order `N-2`;
2. the parent target `widehat G` has a cyclic cut of size at most four;
3. the parent target has a bounded loop, parallel-edge, triangle, theta, acyclic or low-port degeneration.

### Proof

The simultaneous three-reconnection category theorem says that either all three reconnection closures at `uv` are connected loopless bridgeless graphs of order `N-2`, or the original graph `widehat G` is already in one of the displayed cut/bounded branches. ∎

Therefore a recursive child is formed only in Alternative 1.

---

## 6. Route and cap-block fidelity

The internal cancellation preserves the complete ordered four-root boundary word by Lemma 2.1. It may nevertheless alter the physical terminal linkage of a complementary support-pair system.

### First route-change branch

If the cancellation is the first event at which the physical route changes away from the fixed matching, apply `ROUTE_CHANGE_TERMINAL_CONTEXTUAL_TRANSFER_V1.md`:

- the boundary state still lies in the same outer fixed-route sector;
- either alternative matching sends it into the cap profile `K_i`;
- the descendant is a cap-compatible terminal for contextual return.

No lower-order child call is made in this branch.

### Fixed-route branch

If no route change occurs, the descendant retains:

- the same route matching;
- the same distinguished cap block;
- the same ordered terminal labels and support traces;
- the inherited current route sheet induced by `mu`.

### Theorem 6.1 — route fidelity alternative

Every category-safe connected cancellation descendant is either:

1. an immediate route-change terminal; or
2. a lower-order fixed-route context with exactly the route/cap data required by the witnessed proposition.

---

## 7. The genuine child context

Assume:

- `G_j^-` is connected;
- `widehat G^-` is connected loopless bridgeless;
- no first route change occurred.

Define

\[
\mathfrak C^-=(P^-;C_i,E_j;\mu;\text{cap block, fixed route}).
\]

### Theorem 7.1 — child-instance fidelity

`mathfrak C^-` is literally an instance of the witnessed relative proposition

\[
Q_{N-2}.
\]

It satisfies:

1. an ordered four-pole and target cap are defined;
2. `mu` is a specified inherited root flow on the selected valid cross closure;
3. both target and cross closures are connected, loopless and bridgeless;
4. the target order is exactly `N-2`;
5. cap block, terminal ordering, fixed route and exterior attachments restrict functorially.

No support permutation, arbitrary new flow, terminal relabelling or component choice is used.

---

## 8. Return and exit tags

Invoke the lower-order witnessed proposition on `mathfrak C^-`.

### Successful cap return

If the child history reaches a root state on `widehat G^-`, concatenate its complete witness with the stored cancellation interface. `NESTED_CANCELLATION_BUBBLE_COMPRESSION_V1.md` lifts the child history through the parent insertion and restores a predecessor-order root/one-atom continuation.

Thus a successful child return is a valid parent continuation.

### Route or direct/theta terminal

The child and parent use the same ordered outer terminals, cap index and distinguished block. A child route terminal or explicit direct/theta root completion is therefore retained with its complete decorated history and lifted through the stored interface exactly as above.

It is a valid parent continuation terminal, not a bare profile assertion on a nonisomorphic descendant.

### Separator/category terminal

A child separator exit is stored together with:

- the labelled child shore vertex/dart set;
- its cut semiedges and order;
- the identity ancestor map on every surviving parent dart;
- the stack of stored insertion interfaces surrounding the child.

This is the exact data needed to decide whether the separator persists, becomes a bounded insertion neighbourhood, or is consumed by componentwise gluing after ancestor restoration.

### Theorem 8.1 — exit-tag fidelity

Every child outcome is returned to the parent with sufficient labelled data for continuation or ancestor-level disposition. Successful root, route and direct/theta outcomes lift immediately by the witnessed bubble theorem. Separator outcomes are not discarded or declared parent exits without proof; they are the explicit input of `HW2` ancestor genealogy/gluing.

---

## 9. Six-item `HW1-CF` audit

The PDL checklist is resolved as follows.

| item | disposition |
|---|---|
| 1. descendant four-pole and target cap | closed by Lemma 2.1 |
| 2. inherited root flow on selected closure | closed by Lemma 3.1 |
| 3. connected/loopless/bridgeless or component decomposition | closed by Theorems 4.1 and 5.1 |
| 4. strict target-order drop | closed: exactly two vertices |
| 5. cap block and route restriction | closed by Theorem 6.1 |
| 6. child exits valid for parent | root/route/direct closed; separator returned with exact ancestor tag and delegated only to `HW2` |

### Classification

\[
\boxed{
\texttt{HW1-CF CHILD INSTANCE CLOSED}
\quad/\quad
\texttt{SEPARATOR ANCESTRY REMAINS HW2}.}
\]

---

## 10. Assurance boundary

### Exact here

- parallel descendant four-pole construction;
- inherited cross flow and order decrease;
- direct parent two-/four-cut extraction from disconnected cross output;
- target-category test by the simultaneous three-reconnection theorem;
- route-change versus fixed-route child dichotomy;
- literal lower-order `Q_(N-2)` instance in the valid branch;
- successful-return lifting;
- complete ancestor tagging of separator exits.

### Imported authorial mathematics

- root cancellation category theorem;
- simultaneous three-reconnection category theorem;
- small-cut/bounded shore classification;
- route-change terminal theorem;
- witnessed nested bubble compression.

### Not claimed

- completion of `HW2` separator genealogy/gluing;
- completion of `HW3` fixed-order consumer alphabet;
- unconditional PDL R2.7 or global cap restoration;
- independent audit, Lean verification, manuscript integration, curation, release or publication.
