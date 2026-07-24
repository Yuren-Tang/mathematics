# AC-SCOPE-TERMINALS-01 — zero-parent terminal census

**Role:** `AffineCDC — Terminal-Exhaustion Scope Auditor` (`AC-TE-AUD`)  
**Fibre:** normalized complete zero-parent `(0,2,2)` state  
**Classification:** `EXACTLY-TWO-TERMINAL-PATHS VERIFIED IN APPLICATION SCOPE`

## 1. Frozen source boundary

This census uses exactly the five frozen authorities listed in issue #82.  It does not trust the RL/PDL universal component-chain conclusion.  It uses the independently retained fixed-channel degree table, inactive/cycle contraction rows, ordered final matching calculation, stable-dart contracts and exact terminal-consumer ledger only after independently proving the genuine zero-parent carrier has no third terminal path.

## 2. Exact complete zero-parent state

Let `G` be the current complete labelled cubic source graph in a complete fixed-order zero-parent state.  Let the active crossed cell consist of adjacent vertices `u,v` and stable central edge `e=uv`.

Normalize the ordered stable branches to

```text
(A,B,C,D) = (13,13,23,23),
```

with literal prescribed parent `AB|CD`, current root crossed topology `AC|BD` or `AD|BC`, and current central root

```text
lambda(e)=12.
```

Select the literal physical channel

```text
h=35,  H_35=F_3 triangle F_5.
```

Then:

- each branch root `13` or `23` lies in `H_35`;
- the active central root `12` does not lie in `H_35`;
- the unique inactive triangle is `124`;
- each active vertex has exactly its two branch incidences in `H_35` and its central incidence outside `H_35`.

The complete state retains the closed graph `G`, every stable edge and dart, both crossed sheets, the literal zero parent, physically glued cap block, route/profile, graph-category, support-component, support-transport, missing-index and stored-prefix fields.  No terminal semiedge is present before the active-cell deletion.

## 3. Complementary physical carrier

Delete the interiors of the two active vertices `u,v` and the central edge between them.  For each of the four branch stable edges, retain the outside endpoint dart and replace the removed inside incidence by one ordered terminal semiedge.  Call the resulting complementary rooted carrier `R`.

The terminal incidences are exactly

```text
A, B, C, D,
```

with their frozen ordering inherited from the prescribed parent and active-dart labels.  Each retains:

- its stable branch-edge identity;
- its outside endpoint and endpoint dart;
- root label (`13`,`13`,`23`,`23`);
- membership in literal `H_35`;
- active-cell boundary identity;
- stored-prefix ancestry.

The deleted central edge produces no channel terminal: its root `12` lies outside `H_35`, and both of its endpoints are deleted.

## 4. Exhaustive extra-terminal ledger

| Complete-state datum | Additional `H_35` terminal after active-cell deletion? | Reason |
|---|---|---|
| four ordered active branches | yes, exactly `A,B,C,D` | These are the four channel incidences cut by deleting `u,v`. |
| active central edge | no | Root `12` is outside `H_35`; both endpoints are deleted. |
| physically glued cap block | no | Cap vertices, cap edge and cap darts remain ordinary physical incidences of `G`; none is cut unless it is one of the four named branches, in which case it is already counted by its stable identity. |
| exterior attachments | no | Every exterior edge remains in the complementary graph or is one of the four named branch edges. |
| route/profile field | no | It records a boundary matching/consumer state; it is not a physical half-edge. |
| alternate crossed sheet | no | It is a stored local topology on the same four branch darts, not a second carrier boundary. |
| support-component field | no | It records the current closed-channel decomposition of `G`. |
| prior support switch | no | Any earlier legal switch changes roots on a closed component and the current state is then recomputed as a new complete closed graph. |
| future support switch | no at census time | The zero-parent construction permits a switch only after a crossed outside matching has produced closed components. |
| prescribed parent | no | `AB|CD` is a live target topology, not presently spliced into `R`. |
| stored prefix | no | It is an ancestry map on stable darts. |
| pre-existing cut semiedge | impossible in scope | The application begins with a complete cubic source graph, not an unclosed four-pole. |

Therefore active-cell deletion creates all and only four `H_35` terminal incidences.

## 5. Retained channel degree

Before deletion, every vertex of the complete root-valued graph has `H_35` degree `0` or `2`.

Count each retained branch semiedge as one channel incidence at its outside endpoint.

- Every retained vertex not incident with a branch edge is unchanged and has degree `0` or `2`.
- At the outside endpoint of `A,B,C,D`, the former full branch-edge incidence is replaced by the terminal semiedge with the same root and stable dart; the channel degree is unchanged.
- The deleted active vertices are not vertices of `R`.

Thus every retained physical vertex has `H_35` degree `0` or `2` when terminal semiedges are included.  The only free channel ends are the four ordered terminal ends `A,B,C,D`.

## 6. Exact path/cycle census

In the complete graph `G`, `H_35(G)` is a disjoint union of closed cycles.  The active central edge is not selected, so each active vertex lies on `H_35` through its two branch edges.

Consider the channel cycles meeting `u` or `v`.

### Case 1 — distinct channel cycles

If `u` and `v` lie on different `H_35` cycles, deleting each active vertex cuts its cycle once and leaves one terminal path joining the two branch semiedges formerly incident with that vertex.  Hence there are exactly two terminal paths in total.

### Case 2 — one common channel cycle

If `u` and `v` lie on one `H_35` cycle, they are nonadjacent along that channel cycle in a continuing category-safe state.  An `H_35` edge directly joining `u,v` in addition to the nonchannel central edge would be a parallel-edge degeneration and would be consumed before this census.  Deleting the two nonadjacent vertices splits the common cycle into exactly two terminal paths.

Thus in every connected nonterminal application carrier there are exactly two terminal path components pairing `A,B,C,D` in one of the three ordered perfect matchings:

```text
AB|CD,  AC|BD,  AD|BC.
```

This is not an inference from the existence of four named ends alone.  It follows from deleting exactly the two active vertices from a closed `2`-regular physical channel with a nonchannel central edge.  The two paths carry the literal ordered terminal darts.

Every `H_35` cycle disjoint from `u,v` is unchanged and remains closed.  Hence

```text
H_35(R) = two ordered terminal paths disjoint-union closed cycles.
```

There is no third terminal path.

### Residual lock used by the chain

If the outside matching is `AC|BD` or `AD|BC`, the zero-parent consumer proceeds immediately by crossed-sheet alignment, one closed-component switch and the literal parent NNI; no component chain is needed.

The component-chain invocation occurs only in the residual full lock

```text
AB|CD,
```

where the two path components are literally

```text
P_13 : A--B,
P_23 : C--D,
```

and every other nontrivial channel component is closed.  Therefore every internal quotient node is one independently verified inactive `124` singleton or one closed `H_35` cycle.

## 7. Disconnected complement and named consumers

Test connectivity of the full physical complement `R` before invoking the component chain.

If `R` is disconnected, every component has at least one of `A,B,C,D`: a component with no branch incidence was already disconnected from the active cell and hence from `G`.  Some component `S` therefore has at most two terminal incidences.

### One terminal incidence

Then exactly one branch edge crosses from `S` to the active cell in `G`.  It is a bridge/single attachment.  The bridge terminal fires before the component-chain invocation.

### Two terminal incidences

Then

```text
delta_G(S)
```

is exactly the two corresponding branch stable edges.  This is an exact two-edge cut.

- a cyclic shore is consumed by the exact cyclic two-cut completion;
- an acyclic one-/two-port shore is one of the named bounded categories.

Endpoint coincidences producing a loop, parallel edge, triangle, theta or another bounded local topology are separately named in the same terminal ledger and likewise precede continuation.

Therefore there is no disconnected nonterminal complement left for the chain theorem.

## 8. Ordered terminal darts and ancestry

The ordered terminal darts are the outside endpoint darts of `A,B,C,D`; their stable identities do not depend on the current crossed sheet.  The component-chain moves occur in `R` while the deleted active cell, literal parent and branch order remain boundary data.

The independently retained local audit establishes that, once third terminal paths are absent:

- inactive-singleton absorption preserves the next stable connector even when both connectors meet that singleton;
- path-plus-closed-cycle contraction preserves the distinguished path's terminal darts;
- a later connector remains nonchannel and source-labelled;
- the final connector between the two distinct terminal paths changes the ordered matching;
- any category failure is consumed immediately.

After the matching changes, the active crossed sheet is aligned on the same four stable branch darts; one closed `H_35` component is switched; the literal stored `AB|CD` NNI updates only the displayed inside darts and lowers the stored prefix.  No existential recolouring or graph isomorphism substitutes for literal ancestry.

## 9. Relation to the #81 Heawood witness

The permanent #81 witness fixes `h=14` and cuts three channel edges, producing six terminal incidences and three terminal paths.  It cannot arise from genuine zero-parent active-cell deletion.

A genuine zero-parent deletion has the following invariant local certificate:

1. two adjacent deleted active vertices;
2. one central edge outside the selected channel;
3. exactly four selected branch incidences, two at each deleted vertex;
4. branch word support-equivalent to `(13,13,23,23)`;
5. no pre-existing terminal semiedge in the complete graph.

The #81 cut set

```text
1-14:13, 10-11:12, 13-14:12
```

has only three cut edges, six retained endpoint darts, and is not the four-branch boundary of one active two-vertex cell.  In the displayed Heawood topology, trying to take vertex `14` as one deleted vertex forces its two `H_14` branch edges `1-14` and `13-14`, while any second deleted vertex producing `10-11` also cuts another `H_14` branch (`9-10` if vertex `10`, or `2-11` if vertex `11`).  Hence the exact three-edge set is not an active-cell boundary even before imposing the normalized root word.

A support permutation cannot repair this incidence-count and cell-boundary failure.  Nor can the remote third cut be assigned to the cap, route, support-switch or stored-prefix fields, since those are closed physical data or metadata in a complete state.

Thus the #81 certificate remains a counterexample to the broad rooted-carrier theorem but has no genuine zero-parent complete-state embedding.

## 10. Claim-by-claim disposition

| Required claim | Disposition |
|---|---|
| complementary physical carrier defined | verified |
| ordered branches `A,B,C,D` traced | verified with stable darts and roots `(13,13,23,23)` |
| all deletion-created channel terminals listed | exactly four |
| cap/route/exterior/support-switch/prefix extra-terminal search | no extra terminal |
| retained interior `H_35` degree `0/2` | verified |
| connected nonterminal carrier has exactly four terminals | verified |
| exactly two ordered terminal paths | verified from closed-cycle deletion at two active vertices |
| all other nontrivial components closed | verified |
| disconnected complement census | bridge / exact two-cut / bounded consumer verified |
| #81 genuine-state embedding | impossible; exact structural violations identified |

## 11. Fibre verdict

`EXACTLY-TWO-TERMINAL-PATHS VERIFIED IN APPLICATION SCOPE`.

This verdict is limited to the normalized genuine zero-parent complete-state carrier and its support-permutation transports.  It does not promote the failed general component-chain theorem, the full inverse table, ordinary induction, five-support, or five-CDC.