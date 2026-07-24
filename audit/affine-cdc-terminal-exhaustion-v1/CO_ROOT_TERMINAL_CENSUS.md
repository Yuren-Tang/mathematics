# AC-SCOPE-TERMINALS-01 — co-root terminal census

**Role:** `AffineCDC — Terminal-Exhaustion Scope Auditor` (`AC-TE-AUD`)  
**Fibre:** complete co-root/DDD prescribed-parent lock  
**Classification:** `EXACTLY-TWO-TERMINAL-PATHS VERIFIED IN APPLICATION SCOPE`

## 1. Frozen source boundary

This census reads exactly:

- mixed-assurance baseline `curation/affine-cdc-global-rebaseline-v2@24f777d45693ff7e031dc93137a4aec5b879a7b3`;
- RL source `research/affine-cdc-five-cdc-v1@02b37476198e9eaa2b4cd8d2a2edd76782bdcd49`;
- PDL reconstruction `proof-development/affine-cdc-rigour-v1@e36ba22f09e3a9fc6358f3b03615f8fde6c00d96`;
- component-chain audit `audit/affine-cdc-component-chain-v1@a4f20f05532c307a3a8f9d98ac4c5162e7b8ad57`;
- `Xi` audit `audit/affine-cdc-xi-co-root-v1@53be22a0f65b85068b11e5f781579618967db9dd`.

The failed universal conclusion of `FC-COMPONENT-CHAIN-ROOT-NNI` is not used.  Only independently retained fixed-channel parity, inactive/cycle local rows, ordered final matching, stable-dart contracts and named terminal consumers are used after the application census below is established.

## 2. Exact complete application object

The carrier before cutting is the **current complete labelled cubic source graph** `G` in one complete fixed-order co-root prescribed-parent state.  It is not an unclosed cross, an abstract four-pole, or a graph with latent boundary semiedges.

The complete state retains literally:

- the current labelled cubic topology and every stable edge/dart;
- the two distinct marked physical edges `p,q`, whose roots are the two disjoint marked parent roots;
- the live prescribed-parent topology;
- the physically glued cap block, including its vertices, cap edge and ordered cap darts;
- the selected physical rescue support `h` and the literal channel `H_h`;
- route/profile, graph-category and terminal fields;
- support transport and current channel-component partition;
- the stored-prefix ancestry map.

The cap and exterior are subgraphs of `G`.  Route/profile, prescribed-parent and stored-prefix data are fields on this graph; they are not extra physical ports.  This is the complete-state meaning used by the frozen co-root dossiers and by the `Xi` closed-graph invariant, which explicitly sums over exterior and cap vertices.

A continuing co-root lock has the following named hypotheses:

1. `G` is connected and category-safe;
2. `p,q` are distinct marked `H_h` edges with disjoint root labels;
3. `p,q` lie on one physical `H_h` component with the blocked ordered route;
4. no separating rescue channel, cap-compatible route/profile state, cyclic `2/3/4` cut or bounded category has already fired.

Because two roots incident at one root-valued cubic vertex always intersect, the disjoint marked roots cannot be incident at a common vertex.  Thus the two marked physical edges are nonadjacent.

## 3. Physical carrier before and after cutting

### 3.1 Before cutting

For every vertex `v` of `G`, the incident root triangle has `H_h` degree `0` or `2`.  Therefore the physical subgraph `H_h(G)` is a disjoint union of closed channel cycles.  There are no channel endpoints in the complete state.

Let `C_*` be the unique selected channel cycle containing both marked edges `p,q`.

### 3.2 Cutting operation

Construct `R_{p,q}` by deleting only the interiors of `p` and `q`, retaining both endpoint darts of each edge as labelled channel semiedges.  No vertex, cap edge, exterior edge, stored-prefix edge or other physical edge is deleted.

The resulting ordered channel terminal incidences are exactly

```text
p@u_p, p@v_p, q@u_q, q@v_q,
```

with the order fixed by the marked-edge and route data.  These four semiedges retain:

- stable edge identity (`p` or `q`);
- the selected endpoint dart;
- its current endpoint vertex;
- root label and membership in the literal physical channel `H_h`;
- marked-edge ancestry and stored-prefix ancestry.

## 4. Exhaustive extra-terminal ledger

| Complete-state datum | Could it create an additional `H_h` terminal? | Reason |
|---|---|---|
| physically glued cap block | no | Its vertices and edges remain in `G`; no cap incidence is cut.  A cap edge may belong to `H_h`, but it remains an ordinary internal channel edge. |
| exterior attachments | no | They are ordinary stable edges of the complete graph and are not removed. |
| route/profile field | no | It records an ordered physical pairing/consumer state; it does not add or delete an incidence. |
| marked darts | no additional terminal | The four marked endpoint darts are precisely the four semiedges listed above, not four further objects. |
| prescribed-parent topology | no | It is a live target field until the literal parent NNI; it is not spliced into the current carrier. |
| support transport | no | It relabels the same physical channel and incidences. |
| stored prefix | no | It is an ancestry map on surviving stable darts. |
| earlier local NNI history | no | The census is performed on the current complete descendant after all such moves and category tests; the current graph is closed. |
| separating-channel switch | no | It has not occurred in the continuing lock.  If it had, the Phase-B consumer would already terminate the application. |
| any pre-existing cut semiedge | impossible in scope | Such an object would be a rooted carrier, not the complete cubic application state supplied to this corollary. |

Hence the cut operation creates all and only four channel terminal incidences.

## 5. Retained channel degree

Count a retained terminal semiedge as one `H_h` incidence at its retained endpoint.

- At vertices not incident with `p` or `q`, no incidence changes, so the `H_h` degree remains `0` or `2`.
- At an endpoint of `p` or `q`, the deleted edge incidence is replaced by its labelled terminal semiedge; the channel degree therefore remains `2`.
- No marked endpoint is shared, because the marked roots are disjoint.

Thus every retained physical vertex of `R_{p,q}` has channel degree `0` or `2` when terminal semiedges are included.  The only degree-one objects are the free ends of the four terminal semiedges.

## 6. Exact terminal-component census in the connected case

Remove the interiors of two nonadjacent edges from the cycle `C_*`.  The remaining edge set of `C_*` has exactly two connected components: the two complementary cyclic arcs between the four marked endpoint darts.

Call them `P_0,P_1`, ordered by the frozen route orientation.  Each:

- contains exactly two of the four terminal incidences;
- is nontrivial, since `p,q` are nonadjacent;
- retains the stable cyclic ancestry inherited from `C_*`.

There cannot be one terminal path, because the two deleted edge interiors disconnect a cycle at two distinct nonadjacent places.  There cannot be three or more terminal paths, because no third channel edge or vertex was removed and every retained vertex has channel degree `0` or `2`.

Equivalently, in any finite graph whose retained vertices have channel degree `0/2` and whose only free channel ends are four terminal incidences, every path component has exactly two free ends.  The four ends therefore give exactly two path components.  Here the stronger cycle-cut description identifies those two components canonically and supplies their ordered terminal darts; no unspecified connectivity or pairing assumption is used.

Every other nontrivial component of `H_h(G)` was a closed cycle disjoint from `p,q`.  It is unchanged in `R_{p,q}` and remains closed.  Therefore:

```text
H_h(R_{p,q}) = P_0 disjoint-union P_1 disjoint-union (closed cycles),
```

with no third terminal path.

## 7. Connected/disconnected consumer split

The component-chain invocation is made only after testing whether the full physical cut carrier `R_{p,q}` is connected.

Suppose it is disconnected.  Since `G` was connected and only `p,q` were cut, every component of `R_{p,q}` contains at least one of the four terminal incidences.  Hence some component `S` contains at most two.

### One terminal incidence

Then exactly one of `p,q` crosses from `S` to its complement in `G`.  Thus that marked edge is a bridge/single attachment.  The bridge terminal fires before any component-chain invocation.

### Two terminal incidences

The two incidences must come from the two different marked edges; if they were the two ends of one removed edge, restoring that internal edge would not reconnect `S` to the rest of `G`.  Therefore

```text
delta_G(S) = {p,q},
```

an exact two-edge cut.

- if `S` contains a cycle, the exact cyclic two-cut consumer applies on strictly smaller completions;
- if `S` is acyclic, the cubic low-port shore formula places it in the named bounded one-/two-port category.

Thus every disconnected cut carrier is consumed by the bridge/two-cut/bounded ledger before the chain theorem is called.  No disconnected continuing case is left unnamed.

## 8. Stable ancestry needed downstream

The ordered terminal darts are the retained endpoint darts of the two marked stable edges.  They remain boundary data during the remote chain moves.  The independently retained local rows establish, for the only possible internal node types now remaining:

- an inactive singleton is absorbed while every later stable connector survives;
- a closed cycle is merged without changing the two terminal darts of the distinguished path;
- the final connector changes the ordered four-terminal matching;
- every category failure is returned to a named consumer.

Once the present census excludes internal terminal paths, these are exactly the local cases required by the narrowly application-scoped contraction.  No new general chain theorem is asserted here.

## 9. Relation to the #81 Heawood witness

The permanent witness with digest

`d24c63ab56320803b9c795ac08389674b6f67edf89dc5c4ef9a729c5436a3e61`

cuts three `H_14` edges:

```text
1-14:13, 10-11:12, 13-14:12,
```

and therefore has six terminal incidences and three terminal paths.

It violates the genuine co-root application hypotheses in two independent ways:

1. the application cuts exactly the two marked channel edges and has no pre-existing semiedge; the witness inserts a third cut edge;
2. the three displayed cut roots contain no pair of distinct disjoint marked roots of the co-root parent (`13` intersects `12`, while the other two roots are equal).

The witness is therefore controlling against the broad rooted-carrier theorem but is not an application carrier.  It cannot be embedded by reclassifying the third cut as a cap, exterior or stored-prefix port, because those objects are physically closed in the complete state.

## 10. Claim-by-claim disposition

| Required claim | Disposition |
|---|---|
| physical carrier before/after cut defined | verified |
| every created channel half-edge listed | exactly four, the two endpoint darts of each marked edge |
| cap/route/marked/exterior/prefix extra-terminal search | no extra terminal |
| retained interior degree `0/2` | verified, counting retained semiedges at their incident vertices |
| connected nonterminal carrier has exactly four terminals | verified |
| exactly two ordered terminal paths | verified by cutting one closed cycle at two nonadjacent marked edges |
| all other nontrivial components closed | verified |
| disconnected carrier has prior named consumer | bridge / exact two-cut / bounded low-port shore verified |
| #81 witness relation | excluded by three-cut/six-terminal and marked-root hypotheses |

## 11. Fibre verdict

`EXACTLY-TWO-TERMINAL-PATHS VERIFIED IN APPLICATION SCOPE`.

This verdict authorizes only a narrowly co-root application-scoped use of the independently retained contraction rows.  It does not restore arbitrary-equal-face `Xi` totality, the failed general rooted-carrier theorem, the complete induction, five-support, or five-CDC.