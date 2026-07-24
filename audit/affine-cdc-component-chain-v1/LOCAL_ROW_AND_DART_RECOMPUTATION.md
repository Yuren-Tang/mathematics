# AC-AUDIT-CHAIN-01 — local row and dart recomputation

**Frozen source:** `02b37476198e9eaa2b4cd8d2a2edd76782bdcd49`  
**Audit convention:** roots are two-subsets of `[5]`; addition is symmetric difference  
**Canonical channel:** `h=35`; `H_35` consists of roots meeting `{3,5}` once  
**Unique inactive triangle:** `I_35=124`

No Research Lead table or supplied hash was used as input.  Stable edge
identities and endpoint darts were retained throughout.

---

## 1. Complete channel-degree table

For a triangle `T`, the three incident roots are its three two-subsets.

| triangle | `H_35` degree | status |
|---|---:|---|
| `123` | 2 | active |
| `124` | 0 | inactive |
| `125` | 2 | active |
| `134` | 2 | active |
| `135` | 2 | active |
| `145` | 2 | active |
| `234` | 2 | active |
| `235` | 2 | active |
| `245` | 2 | active |
| `345` | 2 | active |

This independently proves the `0/2` parity and uniqueness of the inactive
triangle for the canonical channel.  Support permutation gives the general
statement.

The non-`H_35` roots are exactly

```text
12, 14, 24, 35.
```

---

## 2. All active/inactive rows

Let the central edge be the displayed common non-channel root.  The
root-valued opposite pairing is shown by its two pairs of physical exterior
roots.  The unshown other pairing has a four-support co-root value.

| central | source | root pairing | new central | target |
|---|---|---|---:|---|
| `12` | `123 + 124` | `13-14 \| 23-24` | `34` | `134 + 234` |
| `12` | `125 + 124` | `15-14 \| 25-24` | `45` | `145 + 245` |
| `14` | `134 + 124` | `13-12 \| 34-24` | `23` | `123 + 234` |
| `14` | `145 + 124` | `15-12 \| 45-24` | `25` | `125 + 245` |
| `24` | `234 + 124` | `23-12 \| 34-14` | `13` | `123 + 134` |
| `24` | `245 + 124` | `25-12 \| 45-14` | `15` | `125 + 145` |

Every target triangle is active.  In each row the old active passage is
replaced by a three-edge passage through both vertices.  The two unused roots
at the old inactive vertex remain non-channel roots.

### 2.1 Exact inactive-singleton continuation check

At an inactive `124` vertex the two noncentral exterior roots are two of
`12,14,24`.  If the next quotient connector is one of those edges, the NNI may
move its endpoint from the old inactive vertex to the old active vertex, but:

- the stable edge identity is unchanged;
- its root is unchanged;
- its root remains outside `H_35`;
- its moved endpoint lies on the newly enlarged channel component;
- its other endpoint and all ancestry fields are unchanged.

The checker enumerated:

```text
6 active/inactive rows
x 2 choices of next inactive exterior connector
x 2 labelled target-side assignments
= 24 ordered continuation configurations.
```

No inherited-connector loss and no channel-membership transition occurred.

This verifies the high-priority “both quotient edges incident with the same
inactive singleton” case.

---

## 3. All distinct active/active rows

For a non-channel connector with distinct active endpoint triangles, there are
exactly six unordered source rows.

| central | source | root pairing | new central | target |
|---|---|---|---:|---|
| `12` | `123 + 125` | `13-15 \| 23-25` | `35` | `135 + 235` |
| `14` | `134 + 145` | `13-15 \| 34-45` | `35` | `135 + 345` |
| `24` | `234 + 245` | `23-25 \| 34-45` | `35` | `235 + 345` |
| `35` | `135 + 235` | `13-23 \| 15-25` | `12` | `123 + 125` |
| `35` | `135 + 345` | `13-34 \| 15-45` | `14` | `134 + 145` |
| `35` | `235 + 345` | `23-34 \| 25-45` | `24` | `234 + 245` |

The other exterior pairing has a four-support co-root central value.  The
displayed new central root is non-`H_35` in every row.

At each active endpoint, the central connector is the unique non-channel
incidence.  Therefore, when an internal quotient node is a closed channel
cycle, a later quotient connector cannot be incident at the same entry vertex:
that vertex has no second non-channel edge.  The cycle's exit connector is at
an untouched stable vertex.  This proves the source's entry/exit assertion in
the closed-cycle case.

---

## 4. All equal active endpoint root branch swaps

For an active triangle `T`, let `r` be the central non-channel root and let
`x,y` be its two channel roots.  The three physical pairings of the four
ordered exterior darts are:

```text
current root placement: (x_u,y_u) | (x_v,y_v)
other root placement:   (x_u,y_v) | (y_u,x_v)
zero placement:         (x_u,x_v) | (y_u,y_v).
```

The first two have central root `r=x+y`; the last has central value zero.
The root branch swap is therefore the mixed pairing, never the equal-root
pairing.

| equal endpoint type | central root | channel roots | root branch swap |
|---|---:|---|---|
| `123 + 123` | `12` | `13,23` | `13_u-23_v \| 23_u-13_v` |
| `125 + 125` | `12` | `15,25` | `15_u-25_v \| 25_u-15_v` |
| `134 + 134` | `14` | `13,34` | `13_u-34_v \| 34_u-13_v` |
| `145 + 145` | `14` | `15,45` | `15_u-45_v \| 45_u-15_v` |
| `234 + 234` | `24` | `23,34` | `23_u-34_v \| 34_u-23_v` |
| `245 + 245` | `24` | `25,45` | `25_u-45_v \| 45_u-25_v` |
| `135 + 135` | `35` | `13,15` | `13_u-15_v \| 15_u-13_v` |
| `235 + 235` | `35` | `23,25` | `23_u-25_v \| 25_u-23_v` |
| `345 + 345` | `35` | `34,45` | `34_u-45_v \| 45_u-34_v` |

This is a root-placement statement on ordered darts, not an unlabelled
matching calculation.

---

## 5. Final terminal-path connector rows

Take two distinct channel terminal paths with ordered endpoints

```text
P: A,B
Q: C,D.
```

At the connector vertices, orient the local channel passages as
`A--B` and `C--D`.  In every distinct row of Section 3 and every equal row of
Section 4, the root-valued alternative cross-connects one dart from `P` to one
dart from `Q`.  Hence the old matching

```text
AB | CD
```

is replaced by exactly one of

```text
AC | BD,
AD | BC.
```

It cannot remain `AB|CD`.

The checker enumerated all ordered endpoint types:

```text
6 unordered distinct rows -> 12 ordered source rows
9 equal rows              ->  9 ordered source rows
total                     -> 21 ordered triangle rows

21 rows x 4 ordered terminal orientations = 84 configurations.
```

Results:

| target terminal matching | count |
|---|---:|
| `AC | BD` | 42 |
| `AD | BC` | 42 |
| `AB | CD` preserved | 0 |

If the labelled assignment of the two target triangles to the two central
vertices is also distinguished, the enumeration has `168` movies, again with
zero matching-preserving output.

Repeated external endpoints, loops or parallel edges are not silently
continued: they are graph-category outcomes.  The matching claim above is for
category-safe configurations with four physical terminal darts.

---

## 6. Physical component effects

The local transition system gives:

| incident channel components | root alternative |
|---|---|
| path + closed cycle | one path, same two path terminals |
| closed cycle + closed cycle | one closed cycle |
| terminal path + terminal path | two terminal paths, opposite terminal matching |

The first two rows contract a quotient node.  The third row does **not** merge
two path nodes into one inherited node; it changes their four-terminal
matching.  This distinction is the load-bearing reason the universal theorem
fails when an internal quotient node is itself a terminal path.

A root NNI does not split an incident **closed** channel component: deleting
the two local channel passages opens the two incident components into paths,
and the cross-pairing joins them into the topology shown above.  The
multi-terminal defect is not a hidden split of a closed cycle; it is use of the
third transition row where the proof assumes the first.

---

## 7. Independent Heawood recomputations

### 7.1 Permanent #78 same-arc negative movie

Fixed channel: `H_14`  
Marked edges: `1-6:12`, `2-3:34`  
Equal face: `9-14:23`, endpoint types `123,123`

Root branch swap:

```text
9-10@9  -> vertex 14
1-14@14 -> vertex 9
central 9-14:23 retained.
```

Before and after, cutting the marked edges gives the same ordered matching

```text
(1,2) | (3,6).
```

The output graph is connected, simple, cubic, bridgeless, girth `5`, cyclic
edge-connectivity `5`.  This permanently retains audit #78's negative result.

Independent post-state digest:

`3ab0ea22efc3ed3f45bfb06d5aa83359a896172fef040f110f11ebf1c2934f2d`.

This digest uses the present audit's stable-edge JSON schema; it does not
replace the #78 witness digest or its authority.

### 7.2 Co-root `6-7` connector movie

At stable edge `6-7:23`, endpoint triangles are `123,234`.  Recompute:

```text
123 + 234 -> 124 + 134,
central 23 -> 14,
5-6@6 -> vertex 7,
7-8@7 -> vertex 6.
```

The marked matching changes from

```text
(1,2) | (3,6)
```

to

```text
(1,3) | (2,6).
```

The output is connected, simple, cubic, bridgeless, girth `5`, cyclic
edge-connectivity `5`.

Independent digest:

`72e67089476af09b33daf91316b9b71b687f98291457e4514c8a384bba626ec0`.

### 7.3 Zero-parent Heawood `H_35` movie

The entire source movie was independently reconstructed with exact stable
edges and darts.

| state | operation | digest | girth | cyclic connectivity | minimum-shore representatives |
|---|---|---|---:|---:|---:|
| `S_0` | initial | `4bfadd66ae43ed73c0cb339524884d295264b5468794406412770788993c799d` | 6 | 6 | 28 |
| `S_1` | root branch swap at `13-14` | `a7f4f8c0ff4e75310517d4d61776d17633022463a0a5b8fe07d81777d127a543` | 5 | 5 | 5 |
| `S_2` | switch `Z_0` by `35` | `c5a50827fd01e692ed56d5e2e8c82f0391018cff2c969c13e15b315edf618d9d` | 5 | 5 | 5 |
| `S_3` | literal parent NNI | `18526bf3f8736cae7c298305a9d9f3da49bac4be18828a40ac1368f4070843d7` | 5 | 5 | 8 |

Every state is connected, simple, cubic and bridgeless.

Exact dart operations:

```text
S_0 -> S_1:
    12-13@13 -> vertex 14
    1-14@14  -> vertex 13
    central 13-14:12 retained

S_1 -> S_2:
    switch stable edges
    {1-2,2-3,3-4,4-13,1-14}
    by support pair 35

S_2 -> S_3:
    5-6@5  -> vertex 4
    4-13@4 -> vertex 5
    central 4-5:12 -> 35.
```

After the switch the ordered active word is `(15,13,25,23)`, and the final
central root is literally `35` on the stored `AB|CD` parent topology.

---

## 8. Checker schema and negative-search ledger

A state is represented by:

```text
stable edge id
two stable endpoint-dart ids
current vertex of each dart
root label
terminal/cut status
ordered distinguished terminal-dart pairs
cap and parent fields carried as inert labelled records when disjoint.
```

For each NNI the checker:

1. enumerates the two cross-pairings of four physical exterior darts;
2. accepts only a two-support central value;
3. verifies every target vertex is one of the ten root triangles;
4. recomputes `H_h` membership from roots, never from a cached table;
5. recomputes physical channel components;
6. retains stable ancestry and ordered terminal darts;
7. checks connectedness, loops, parallel edges, bridges, girth and cyclic
   edge-connectivity.

Negative searches completed:

| target failure | result |
|---|---|
| inactive inherited connector loss | none in 24 ordered configurations |
| later non-channel connector becomes `H_h` | none |
| closed-cycle entry/exit share modified vertex | impossible by unique non-channel incidence |
| final matching preservation | none in 84 ordered configurations |
| #78 same-arc old lemma | counterexample reproduced |
| general chain with an internal terminal-path node | counterexample found; 36/36 one-NNI movies fail inherited length one |
| co-root `6-7` proposed movie mismatch | none |
| zero-parent Heawood movie mismatch | none |

Canonical local-row digest:

`75ed977851a944f2cd80577e629a2f6936da5dfce49ad9d5a9e0e82c8b2494d4`.

Aggregate finite-recomputation digest:

`2353b22b111c9dd47319b2c14637c08d93ae2f4eac10605a00f29c5f46842fe8`.

These digests certify this audit's chosen schemas only.  They are not theorem
proofs and were not compared to Research Lead hashes as a source of truth.
