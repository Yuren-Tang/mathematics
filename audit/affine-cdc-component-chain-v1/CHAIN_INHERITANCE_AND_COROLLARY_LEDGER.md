# AC-AUDIT-CHAIN-01 — chain inheritance and corollary ledger

**Frozen source:** `Yuren-Tang/mathematics@02b37476198e9eaa2b4cd8d2a2edd76782bdcd49`  
**Permanent negative audit:** `audit/affine-cdc-xi-co-root-v1@53be22a0f65b85068b11e5f781579618967db9dd`  
**Disposition:** material false scope in the general chain theorem; review stopped without authoring a repair

---

## 1. What the local contraction proof actually establishes

Let a shortest quotient chain be

```text
X_0=P_0, X_1, ..., X_l=P_1
```

with a stable physical non-channel connector for each quotient edge.

The source-level inheritance is valid in the following two internal-node
types.

### 1.1 `X_1` is an inactive singleton

The first connector is the central edge of one of the six rows in
`LOCAL_ROW_AND_DART_RECOMPUTATION.md`.  The NNI makes both source vertices
channel-active and inserts the new channel central edge into the old passage
through `X_0`.

If the successor connector `X_1X_2` is incident with the same inactive source
vertex, one of its endpoint darts moves to the old active vertex.  Its stable
edge id, root, non-channel status and other endpoint survive.  It therefore
joins the enlarged component to `X_2`.

No extra hypothesis about distinct source vertices is needed in this case.

### 1.2 `X_1` is a closed channel cycle

At an active vertex exactly two incidences are channel edges.  The connector
used to enter the cycle is its unique non-channel incidence.  Hence a second
quotient connector cannot leave the cycle at that same vertex.

The root alternative cross-connects the path passage and the cycle passage.
The result is one terminal path with the same two `P_0` terminal darts.  Every
later connector is incident at an untouched stable vertex of the old cycle or
a later quotient node.  Its root is unchanged and remains non-channel.

No component split occurs in this closed-cycle case.

### 1.3 What is not established

The written theorem does not require every other terminal path to be absent.
If `X_1` is a third terminal path, the local transition is not path plus cycle;
it is terminal path plus terminal path.  Its exact effect is an opposite
four-terminal matching.  There is no enlarged path carrying the old `P_0`
terminal pair.

This is a third connector type omitted from both cases of the proof.

---

## 2. Complete multi-terminal source certificate

### 2.1 Canonical serialized data

Schema:

```text
AC-AUDIT-CHAIN-01-multiterminal-scope-v1
```

Base stable-state digest:

`4bfadd66ae43ed73c0cb339524884d295264b5468794406412770788993c799d`.

Fixed channel:

```text
h=14.
```

Cut stable edges:

```text
["1-14","10-11","13-14"].
```

Ordered terminal pairs:

```text
P_0 = ["1-14@1","10-11@11"]
X_1 = ["10-11@10","13-14@13"]
P_1 = ["1-14@14","13-14@14"].
```

Pre-move channel components:

```text
P_0: [1,2,3,4,5,6,11]
X_1: [7,8,9,10,12,13]
P_1: [14].
```

A shortest physical quotient chain is:

```text
P_0 -- ["3-8", root 14] -- X_1
    -- ["9-14", root 23] -- P_1.
```

### 2.2 Selected root NNI

```text
central stable edge: 3-8
central root: 14 -> 23
source triangles: 134 + 124
target triangles: 234 + 123

retained:
    2-3@3
    8-9@8

moved:
    7-8@8 -> vertex 3
    3-4@3 -> vertex 8.
```

Post-move stable-state digest:

`d0987e1e4f72a8f8b535718b3075a5053f9b10609a67a68bf885f316e070e6f2`.

Post-move channel components:

```text
Y_0: [1,4,5,6,8,9,10]
Y_1: [2,3,7,11,12,13]
P_1: [14].
```

The old `P_0` terminal darts are split between `Y_0` and `Y_1`.

Post-move graph data:

```text
connected: yes
simple: yes
cubic: yes
bridges: 0
girth: 5
cyclic edge-connectivity: 5.
```

### 2.3 Exhaustive one-step certificate

The carrier has `18` non-cut central edges.  For each, the checker enumerated
both labelled root-valued cross-assignments.  All `36` outputs were valid
root-triangle states and category-safe.

```text
inherited P_0 and P_1 length-one chain: 0 / 36
all three terminal pairs preserved but no direct P_0-P_1 connector: 24 / 36
P_0 split: 10 / 36
P_1 split: 2 / 36.
```

No loop, parallel edge, bridge or cyclic `2/3/4` cut occurred in any output.

Canonical certificate digest:

`d24c63ab56320803b9c795ac08389674b6f67edf89dc5c4ef9a729c5436a3e61`.

This is a complete labelled source certificate against the universal
one-NNI inherited-chain conclusion.

---

## 3. High-priority attack ledger

| Attack requested by issue #81 | Independent result |
|---|---|
| Next witnessed connector after active/inactive NNI | Preserved in all 24 ordered configurations, including both quotient edges incident with the inactive singleton. |
| Two quotient edges simultaneously incident with inactive singleton | Sound: the successor dart may move, but its root, stable id, non-channel status and attachment to the enlarged component survive. |
| Active cycle entry/exit reconnected incorrectly | No defect for a closed cycle: one active vertex has only one non-channel incidence, so entry and exit are at distinct vertices. |
| Later connector changes from non-`H_h` to `H_h` | Impossible in the stated local moves because later connector roots are unchanged; independently checked in the finite rows. |
| Quotient contraction splits a component | No split in inactive or path-plus-closed-cycle cases. A material failure occurs instead when the internal node is a terminal path: the NNI changes the terminal matching and destroys the inherited distinguished pair. |
| Equal endpoint branch swap uses wrong pairing | Verified: mixed pairing is root-valued; equal-root pairing has central value zero and is excluded. |
| Final connector changes every ordered terminal matching | Verified in all 84 ordered configurations; 42 reach each crossed matching, 0 preserve the old matching. |
| Category failures have existing consumers | Verified against the frozen terminal ledger for `K_i`, separating channel, cyclic `2/3/4` cuts and bounded categories. No consumer fires in the counterexample. |

---

## 4. Co-root corollary ledger

### 4.1 Permanent #78 negative result

The old statement

```text
an arbitrary equal bad face is route-changing
or exposes a one-passage switch component
```

remains false.

Exact retained witness:

```text
h=14
marked edges 1-6:12 and 2-3:34
equal face 9-14:23 with endpoint types 123,123
branch swap:
    9-10@9  -> vertex 14
    1-14@14 -> vertex 9.
```

Both marked edges lie on the same outside arc.  Before and after the root
branch swap, the marked route is

```text
(1,2) | (3,6).
```

The graph remains category-safe.  Neither the arbitrary-equal-face lemma nor
`Xi` totality is restored.

### 4.2 Two distinguished marked arcs

In a category-safe common-component lock, the selected `H_h` component is a
cycle containing the two distinct marked channel edges.  Cutting the interiors
of those two edges canonically produces two path components.  Their four
terminal darts are the two sides of the marked edges, with stable identities
and cyclic ancestry retained.

Every other nontrivial `H_h` component is a closed cycle.  Thus the co-root
application has the narrower terminal geometry missing from the general
statement.

If the whole cut carrier is disconnected, a component has at most two of the
four cut semiedges:

- one port on a cyclic shore gives a bridge;
- two ports on a cyclic shore give a two-edge cut;
- an acyclic one- or two-port shore is an existing bounded low-port category.

These quantifiers match the frozen terminal consumers.

### 4.3 Independent `6-7` repair movie

Stable connector:

```text
6-7:23
endpoint triangles 123,234
root row 123+234 -> 124+134
central root 23 -> 14.
```

Exact moved darts:

```text
5-6@6 -> vertex 7
7-8@7 -> vertex 6.
```

The ordered marked route changes:

```text
(1,2) | (3,6)  ->  (1,3) | (2,6).
```

The output graph is connected, simple, cubic, bridgeless, girth `5`, cyclic
edge-connectivity `5`; digest:

`72e67089476af09b33daf91316b9b71b687f98291457e4514c8a384bba626ec0`.

This is a valid correction of that exact witness by selecting a connector
between the two marked arcs.  It does not erase the old `9-14` counterexample.

### 4.4 Final marked matching classification

Starting from the two cut marked arcs, the final connector changes their
four-endpoint matching to one of the other two perfect matchings.  Reinserting
the two marked edges gives exactly:

1. two closed channel components, one containing each marked edge — a
   separating channel; or
2. one closed component with the opposite cyclic marked order — the opposite
   marked route.

This local topological classification is verified on ordered endpoints.

The source identifies the second outcome with a cap-compatible route under the
fixed-route blocking hypothesis and sends the first to the existing Phase-B
consumer.  Those consumers exist in the frozen PDL ledger.  Because the audit
stopped at the material general-theorem defect, the complete co-root
parent/prefix reinsertion chain is **not independently promoted** here.

---

## 5. Zero-parent corollary ledger

### 5.1 Inverse-parent value trichotomy

For two root sums in `E_5`, the prospective parent central value is a symmetric
difference of two roots.  Its support size is necessarily:

```text
0, 2, or 4.
```

These are respectively:

```text
zero parent,
root parent,
co-root parent.
```

No other inverse-parent value occurs.  Thus root/co-root/zero exhaust the
algebraic parent-value table.

### 5.2 Active-cell deletion and carrier connectivity

After deleting the two active vertices, the four ordered active branch darts
are the only ports of the complementary carrier.

If it is disconnected, one component has at most two ports.  As in the
co-root case:

- one cyclic port gives a bridge;
- two cyclic ports give a two-edge cut;
- an acyclic low-port component is a bounded category.

The exact cyclic/bounded consumers already exist.  Hence a category-safe
nonterminal four-port carrier is connected at this interface.

### 5.3 Outside matching trichotomy

Four ordered terminal darts `A,B,C,D` have exactly three perfect matchings:

```text
AB | CD
AC | BD
AD | BC.
```

The two crossed matchings are immediate horizontal outcomes.  The residual
full zero-parent lock is exactly `AB|CD`.  This trichotomy is complete and does
not use a finite-state conclusion.

### 5.4 Crossed-sheet alignment and component split

Normalize:

```text
(A,B,C,D)=(13,13,23,23),
current crossed central root=12,
h=35.
```

After a final connector changes the outside matching to `AC|BD` or `AD|BC`,
choose the root-valued active crossed sheet with the same matching.  This uses
zero or one active equal-face root branch swap; the zero pairing is not used.

Closing the outside paths with that active sheet yields exactly two closed
`H_35` components.  Each contains one `13` branch and one `23` branch.  A
switch of either component by `35` changes exactly:

```text
13 -> 15
23 -> 25
```

on that component.  Up to the fixed ordered symmetry, the active word becomes

```text
(15,13,25,23).
```

Then

```text
15+13 = 25+23 = 35,
```

and the ordinary NNI on the active central edge realizes the literal stored
`AB|CD` parent with central root `35`.

### 5.5 Exact Heawood model

The model movie was reproduced:

```text
remote root branch swap at 13-14
    -> H_35 components
       Z_0=1-2-3-4-13-1
       Z_1=5-6-7-12-14-9-10-5
    -> switch Z_0 by 35
    -> active word (15,13,25,23)
    -> literal parent NNI with central root 35.
```

State digests:

```text
S_0 4bfadd66ae43ed73c0cb339524884d295264b5468794406412770788993c799d
S_1 a7f4f8c0ff4e75310517d4d61776d17633022463a0a5b8fe07d81777d127a543
S_2 c5a50827fd01e692ed56d5e2e8c82f0391018cff2c969c13e15b315edf618d9d
S_3 18526bf3f8736cae7c298305a9d9f3da49bac4be18828a40ac1368f4070843d7.
```

Cyclic connectivity is `6,5,5,5`; all states are connected, simple, cubic and
bridgeless.

The model establishes the exact source movie only.  The universal zero-parent
corollary depends on a correctly scoped two-terminal-path chain theorem, which
was not authored by this audit after the stop condition fired.

---

## 6. Cap, parent and ancestry fields

The local checker never identifies edges merely by current endpoint pairs.
Each stable edge has two stable endpoint-dart identities.  An NNI changes the
current vertex of specified darts and, where required, the central root;
unmoved dart identities remain literal.

For the two exact Heawood movies:

- cap vertices and cap edge are retained;
- moved cap-adjacent darts retain the endpoint at the cap vertex and stable
  order;
- the prescribed-parent topology remains a live labelled field until the
  literal final NNI;
- the selected physical support channel is recomputed from root labels;
- stored-prefix ancestry is identity outside the displayed local darts.

The general source theorem asserts a broader complete-state contract, but the
counterexample is already disjoint from any ambiguity in cap or parent
serialization: the failure occurs in the physical channel-component partition
itself.

---

## 7. End-to-end disposition

Completed bounded checks support the component-chain mechanism in the exact
connector types used by the two corollaries:

```text
inactive singleton
closed intervening cycle
final connector between the two distinguished terminal paths.
```

They do not validate the theorem in its stated universal rooted-carrier scope.
The multi-terminal carrier proves that a third terminal path cannot be treated
as a closed cycle and that no one-NNI inherited chain need exist.

Accordingly:

```text
general theorem: BLOCKED — FALSE SCOPE
co-root local corollary data: bounded checks passed; no universal promotion
zero-parent local corollary data: bounded checks passed; no universal promotion
ordinary-induction integration: BLOCKED pending a separately reviewed,
correctly scoped theorem.
```

No mathematical repair is proposed in this audit.
