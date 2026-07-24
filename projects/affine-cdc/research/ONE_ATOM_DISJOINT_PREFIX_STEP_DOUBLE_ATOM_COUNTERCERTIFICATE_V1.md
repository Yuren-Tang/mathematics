# Disjoint literal-prefix step can create a second persistent atom

## AC-RL-ONE-ATOM-01 / complete labelled countercertificate v1

**Disposition:** the disjoint-support case of
`ONE-ATOM-NEXT-SOURCE-STEP-MACRO` is false as stated.  The focused endpoint
totality theorem is therefore not proved by the v1 packet.

This certificate does **not** refute `ONE-ATOM-COMPLETE-ENDPOINT-TOTALITY`
itself.  It refutes the claimed scheduler transition which was used to prove
that theorem.

---

## 1. Base labelled Heawood root state

Use the fourteen-vertex cubic graph with stable labelled edges

```text
1-2:23   1-6:12   1-14:13
2-3:34   2-11:24  3-4:13
3-8:14   4-5:12   4-13:23
5-6:13   5-10:23  6-7:23
7-8:24   7-12:34  8-9:12
9-10:13  9-14:23  10-11:12
11-12:14 12-13:13 13-14:12.
```

Every edge value is a root and every vertex sum is zero.  The uncoloured graph
is connected, simple, cubic and bridgeless, with girth `6` and cyclic
edge-connectivity `6`.

Fix the literal stored source NNI `f` on central stable edge `5-6`.  In the base
root flow its two sides are both root-valued.  The current side has

```text
at 6: 1-6:12, 6-7:23, central 5-6:13
at 5: 4-5:12, 5-10:23, central 5-6:13.
```

The literal predecessor pairing pairs

```text
1-6:12 with 5-10:23,
6-7:23 with 4-5:12,
```

so its central value is again `13`.  Its stable-dart movie is

```text
6-7@6  -> vertex 5,
5-10@5 -> vertex 6,
central stable edge 5-6 retained.
```

Thus `f` is an actual root-valued source-prefix NNI, not a topology invented
after the returned flow is known.

---

## 2. Produce one standard atom without changing the source word

Switch the physical cycle

```text
Z = 1-2-11-10-5-4-13-14-1
```

by root `25`.  The changed labels are

```text
1-2 : 23 -> 35
2-11: 24 -> 45
10-11:12 -> 15
5-10: 23 -> 35
4-5 : 12 -> 15
4-13: 23 -> 35
13-14:12 -> 15
1-14:13 -> 1235 = Q_4.
```

All other labels remain unchanged.  Conservation is preserved because each
cycle vertex has two switched incidences.

Exactly one edge is now non-root:

```text
atom a = 1-14:Q_4.
```

At its endpoints the branch pairs are

```text
vertex 1 : 35,12,
vertex 14: 15,23.
```

The two crossed central values are

```text
35+23=25,
35+15=13,
```

both roots.  Hence `1-14` is a standard co-root atom with its two crossed root
restrictions.  The complete uncoloured topology has not changed, so it remains
connected, simple, cubic, bridgeless, girth `6`, cyclic edge-connectivity `6`.

The atom support `{1,14}` is disjoint from the head source-step support `{5,6}`.

---

## 3. The literal disjoint source step creates atom number two

In the switched post-pop state, the current `5-6` cell is still root-valued:

```text
at 6: 12+23=13,
at 5: 15+35=13.
```

Apply the **same literal predecessor pairing** stored in Section 1.  Its two
forced central sums are now

```text
12+35 = 1235 = Q_4,
23+15 = 1235 = Q_4.
```

Therefore the predecessor side of `f` is not a root NNI for the returned state.
It is a second standard co-root atom on the retained central edge `5-6`.

The exact stable-dart movie is

```text
6-7@6  -> vertex 5,
5-10@5 -> vertex 6,
central stable edge 5-6:13 -> Q_4.
```

The old atom `1-14:Q_4` is disjoint and untouched.  The output therefore has
exactly two persistent non-root edges:

```text
1-14:Q_4,
5-6 :Q_4.
```

There is no adjacent three-vertex bad-overlap tree to normalize: the two atoms
have disjoint vertex supports.

---

## 4. No category terminal removes the example

After the literal NNI, the uncoloured graph is obtained by

```text
remove 6-7 and 5-10,
add    5-7 and 6-10,
retain central edge 5-6.
```

It is independently checked to be:

```text
connected: yes
simple: yes
cubic: yes
bridges: 0
girth: 5
cyclic edge-connectivity: 5.
```

Thus no loop, parallel-edge, bridge, cyclic `2/3/4`-cut or acyclic low-port
consumer fires.  Route/cap metadata can be placed outside these disjoint local
supports and is not forced to change by the coefficient calculation.

Canonical standard-library certificate:

`finite/one_atom_disjoint_double_atom_countercertificate_v1.py`.

Canonical digest:

`dd4afccb8578e3ab8e48c33bddaad39e763f18dac398fe8e2d83e80ceeb57aea`.

---

## 5. Exact failed inference

The v1 macro asserted

```text
one atom A, next source NNI f, supp(A) disjoint supp(f)
    -> strict commuting square
    -> one atom A' on the predecessor side of f.
```

Disjointness proves only equality of the two **uncoloured operation orders**.
It does not prove that the literal predecessor side of `f` is root-valued under
the returned edge labels.  In this certificate it is co-root-valued, so
crossing `f` creates a second independent atom.

The retained local critical-overlap theorem does not apply: it assumes a root
Pachner move adjacent to or disjoint from the existing atom.  Here the attempted
inverse source move is precisely not root-valued for the returned state.

Consequently the transition

```text
(L,mu) -> (L-1,mu')
```

is unavailable in the disjoint case, and the v1 lexicographic scheduler is not
total.

---

## 6. Correct residual frontier

The smallest missing implication is now:

> Given one standard co-root atom and a disjoint next literal source NNI whose
> predecessor central value is zero or co-root under the returned labels, produce
> a finite source-faithful same-order history to one complete crossed root
> endpoint or exact terminal **without allowing two persistent atoms**.

Equivalently, one needs a genuine two-discrepancy avoidance theorem, or a proof
that the exact post-pop ancestry forbids the displayed disjoint configuration.
Neither statement is present in the frozen v7.2/v7.4.1 sources or in the v1
one-atom packet.

This obstruction uses no component-chain issue, no SCC argument and no
supplied-comparison objection.  It lies strictly inside the proposed
prefix-directed scheduler.