# AC-5CDC-AUD-V741 — scope, callsite and negative-certificate audit

## 1. Permanent #81 negative certificate

The broad statement

> a connected category-safe rooted carrier with two distinguished terminal paths admits an inherited component-chain contraction to a changed matching

is false unless the two distinguished paths are literally all selected-channel terminal paths.

The frozen Heawood state has the following labelled edges:

```text
1-2:23   1-6:12   1-14:13
2-3:34   2-11:24  3-4:13
3-8:14   4-5:12   4-13:23
5-6:13   5-10:23  6-7:23
7-8:24   7-12:34  8-9:12
9-10:13  9-14:23  10-11:12
11-12:14 12-13:13 13-14:12.
```

With `h=14`, cut `1-14`, `10-11`, `13-14`.  The three path components and shortest chain are

```text
P_0 -- 3-8:14 -- X_1 -- 9-14:23 -- P_1.
```

The NNI at `3-8` uses

```text
134+124 -> 234+123, central 14 -> 23,
```

and separates the two old `P_0` darts.  This gives a direct physical failure of the inherited-prefix conclusion, not merely an omitted proof case.

A fresh stable-dart enumeration independently reproduced the complete one-step outcome census:

| outcome | count |
|---|---:|
| all three old terminal pairs remain internally connected, no direct `P_0--P_1` connector | 24 |
| `P_0` and `X_1` split | 10 |
| `P_1` and `X_1` split | 2 |
| inherited length-one chain for original `P_0,P_1` | 0 |

All 36 outputs are connected, simple, cubic and bridgeless, have girth five and cyclic edge-connectivity five.  Hence no category consumer removes the counterexample.

Frozen canonical digest:

`d24c63ab56320803b9c795ac08389674b6f67edf89dc5c4ef9a729c5436a3e61`.

## 2. Permanent #78 negative certificate

For `h=14`, marked edges `1-6:12`, `2-3:34`, and equal face `9-14:23`, the root branch swap preserves

```text
(1,2)|(3,6).
```

It remains a counterexample to:

- arbitrary-equal-face route-or-split;
- `Xi` as an unconditional source selector;
- any inference that an equal bad face alone is productive.

The v7.4.1 packet preserves this negative boundary.  Its `6-7:23` movie is used only after `6-7` is identified as an actual connector between the two marked arcs.

## 3. Exact application restriction

The active theorem is

`FC-EXACT-TWO-TERMINAL-PATH-COMPONENT-CHAIN`.

Its domain is not inferred from four named ports or two distinguished paths.  It requires the literal decomposition

```text
H_h(R)=P_0 disjoint-union P_1 disjoint-union closed channel cycles,
```

plus complete stable-dart, cap, route, parent and prefix data.

The #82 co-root constructor establishes this by cutting exactly two nonadjacent marked channel edges on one closed channel cycle.  The #82 zero constructor establishes it by deleting exactly one active two-vertex cell whose central edge is nonchannel.  The #81 carrier performs three remote cuts and has six terminals, so it is an instance of neither constructor.

## 4. Independent callsite classification

The six-commit delta from the v7.4 head `e36ba22f09e3a9fc6358f3b03615f8fde6c00d96` to the frozen candidate changes only the updated proof DAG and five new v7.4.1 files.  Every active reference in that delta was classified as follows.

| Occurrence | Classification | Disposition |
|---|---|---|
| `FC-COMPONENT-CHAIN-ROOT-NNI` in the old v7.4 theorem reconstruction | historical/failed candidate | not active authority |
| broad wording in old row/dart and inherited-chain files | retained local source only | used only under the exact-two-path hypothesis |
| old co-root corollary broad call | replaced by co-root application lemma | #82 co-root census precedes the conditional chain |
| old zero-parent broad call | replaced by zero-parent application lemma | #82 zero census precedes the conditional chain |
| old v7.4 inverse/induction integration | historical/failed candidate | superseded by v7.4.1 integration |
| v7.4.1 co-root active call | application-scoped | guarded by exact two-edge cut constructor |
| v7.4.1 zero active call | application-scoped | guarded by exact active-cell deletion constructor |
| updated proof DAG chain nodes | application-scoped | each has one #82 constructor as immediate parent |
| old audit handoff | historical | superseded by the v7.4.1 handoff |

No active occurrence was found in which the false universal theorem is invoked on an internal terminal path or inferred from “two distinguished paths”.

## 5. Rank-reset and migration language

The active v7.4.1 chain fixes one witnessed connector list once.  Each prefinal move deletes its first named connector.  The active prefix protocol permits a new connector rank only after literal parent success lowers the stored-prefix length.

No active instruction was found to:

- choose a new shortest path while the same parent obligation is live;
- recompute quotient distance;
- migrate to a different channel to restart the same chain;
- reset the connector rank before final matching progress is consumed.

Historical files contain broader scheduler and migration mechanisms, but the v7.4.1 authority map marks them noncontrolling.  They cannot be imported to fill the separate one-atom continuation gap without a new proof.

## 6. Forbidden-dependency audit

The active v7.4.1 component-chain cone does not use:

- the failed general rooted-carrier theorem;
- the #81-invalid terminal-exhaustion inference;
- arbitrary-equal-face totality;
- `Xi` or `Omega` as an unconditional provider;
- generic NNI connectivity;
- finite-state/SCC distance;
- `Q_N`, `M_N`, `d_N`, nested bubbles or terminal frames.

This negative result must be distinguished from completeness.  The one-atom totality edge is absent rather than legitimately supplied by one of these forbidden mechanisms.

## 7. Scope verdict

The v7.4.1 application-scope repair passes:

```text
broad theorem: permanently false
conditional exact-two-path theorem: valid in stated domain
co-root constructor: domain supplied
zero constructor: domain supplied
active stale broad call: none found.
```

The full candidate remains blocked elsewhere, at the pre-parent-table one-atom continuation interface.
