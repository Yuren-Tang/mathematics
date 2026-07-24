# AC-AUDIT-XI-01 — source-movie and scope ledger

**Audit role:** temporary independent mathematical reviewer  
**Frozen candidate:** `fee97446ee8b99f07740f394e99ef4a2ecc3e40e`  
**Audit branch:** `audit/affine-cdc-xi-co-root-v1`  
**Theorem scope:** co-root/DDD `(4,2,2)` sector only

---

## 1. Canonical frame

Let `p,q` be the ordered disjoint marked roots, let `m` be the unused support,
and let `h_*` meet `p` and `q` once each.  Write

`p={p_0,p_1}`, `q={q_0,q_1}`, `h_*={p_0,q_0}`.

A support bijection satisfying

`eta(p)=12`, `eta(q)=34`, `eta(m)=5`, `eta(h_*)=14`

is unique.  Indeed:

- `p_0` lies in both `p` and `h_*`, so it must map to
  `12 intersect 14 = {1}`;
- `p_1` must map to `2`;
- `q_0` lies in both `q` and `h_*`, so it must map to
  `34 intersect 14 = {4}`;
- `q_1` must map to `3`;
- `m` must map to `5`.

This verifies frame uniqueness and distinguishes the literal physical support
pair `h_*` from its current canonical label `14`.

### Common-marked switch

In canonical coordinates a common marked `H_14` switch gives

`12 -> 24`, `34 -> 13`.

With `eta' = tau_14 o eta`, the new roots return to `12,34`, the unused support
remains `5`, and the same physical pair `h_*` remains labelled `14`.

The three component cases are exact:

1. neither marked occurrence: retain `eta`;
2. both marked occurrences: use `eta'=tau_14 o eta`;
3. exactly one marked occurrence: this is a separating rescue component and is
   consumed before it is treated as a nonexit invariant switch.

---

## 2. Whole-component `Xi` invariance

At a vertex of an `H_14` component, exactly two incident roots are translated by
`14`.  On support triangles this is `tau_14=(1 4)`.

For an unmarked switched component `Z`:

- vertices in `Z` change `T -> tau_14(T)`;
- vertices outside `Z` are unchanged;
- every vertex weight is unchanged because `xi o tau_14 = xi`.

For a common-marked switched component:

- physical switching applies `tau_14` on `Z`;
- frame transport applies a second `tau_14` on every vertex;
- vertices in `Z` are acted on twice;
- vertices outside `Z`, including exterior and cap vertices, are acted on once;
- all weights remain unchanged.

Therefore the complete closed-graph sum

`Xi(S)=sum_v xi(eta(Delta_v))`

is invariant in both nonexit switch cases.  No exterior cancellation, orbit
minimum, or quarantined `Omega` statement is used.

---

## 3. Source contracts for strict distinct-neighbour NNIs

For a bad type `123,234` select its internal `23` incidence.  For `125,245`
select its internal `25` incidence.  The DDD boundary roots are only `12,34`, so
these are internal carrier edges.

The independently recomputed six root NNIs are listed in
`FINITE_TABLE_RECOMPUTATION.md`.  Each move:

- is root-valued;
- preserves graph order;
- preserves every exterior dart of the two-vertex cell;
- leaves the literal parent obligation live unless it is the parent NNI itself;
- preserves labelled cap objects;
- updates the witnessed prefix map by the actual local source movie;
- requires recomputation of channel partitions, route/profile and exact graph
  category before continuation.

Conditional on the output remaining a complete prime oriented lock, `Xi`
falls by exactly two.

---

## 4. The intended equal-neighbour movie

For an equal bad face of type `T`, the coefficient-level movie is:

1. zero or one root-valued branch-swap between the two root placements;
2. switch a closed `H_14` component containing exactly one local passage;
3. perform the strict mixed-pair NNI
   `T+tau_14(T) -> 124+134` or `124+145`.

If Step 2 is source-legal, every state is root-valued and the total change is
`Delta Xi=-2`.

The load-bearing source assertion is therefore not the coefficient table.  It
is the proposed route-or-split implication:

> for the two root placements of an equal face, either the branch-swap changes
> the oriented marked `H_14` route, or one placement has the two local passages
> in distinct closed components.

That implication is false as stated.

---

## 5. Exact Heawood counterexample to the route-or-split implication

Use the exact Heawood root flow recorded in the frozen source.  The graph edges
and roots are:

```text
12:23   16:12   1-14:13
23:34   2-11:24 34:13   38:14
45:12   4-13:23 56:13   5-10:23
67:23   78:24   7-12:34
89:12   9-10:13 9-14:23
10-11:12 11-12:14 12-13:13 13-14:12
```

Take the marked edges

- `A=1-6` with root `12`;
- `B=2-3` with root `34`;
- fixed rescue support `h=14`.

The `H_14` component is the Hamilton cycle

```text
1-6-5-4-3-2-11-10-9-8-7-12-13-14-1.
```

The edge `9-14` has root `23`.  Both endpoints have triangle type `123`:

- vertex `9`: roots `12,13,23`;
- vertex `14`: roots `12,13,23`.

Thus `9-14` is exactly an equal bad face selected at central root `23`, and both
local passages lie on the marked `H_14` component.

### 5.1 Three local placements

At vertex `9` the exterior darts are

- `9-8` with root `12`;
- `9-10` with root `13`.

At vertex `14` they are

- `14-13` with root `12`;
- `14-1` with root `13`.

The current root placement pairs

```text
(9-8,9-10) | (14-13,14-1).
```

The other root placement pairs

```text
(9-8,14-1) | (9-10,14-13).
```

The third placement pairs equal roots and has central value zero.

Remove the two local passages from `H_14`.  The outside system has paths

```text
8-7-12-13
```

and

```text
10-11-2-3-4-5-6-1.
```

Hence its matching pairs the two `12` ports and the two `13` ports: it is the
third, zero matching.  Crucially, the second outside path contains **both**
marked edges `B=2-3` and `A=1-6`; the first contains neither.

### 5.2 Root branch-swap

Perform the root NNI by reattaching the stable `13` branches as

```text
9-10 -> 14-10,
1-14 -> 1-9,
```

while retaining central edge `9-14:23` and the two `12` branches.

Both vertices remain type `123`.  The new `H_14` component is again one
Hamilton cycle:

```text
1-6-5-4-3-2-11-10-14-13-12-7-8-9-1.
```

Thus neither root placement has the two local passages in distinct components.

### 5.3 Marked route does not change

Cut the marked edges `1-6` and `2-3`.

Before the branch-swap the induced pairing of marked endpoints is

```text
(1,2) | (3,6).
```

After the branch-swap it is again

```text
(1,2) | (3,6).
```

The cyclic order of the marked endpoints is unchanged as well.  The branch
swap reverses/reconnects a segment on the complementary arc, but both marked
edges lie on the same outside arc.  Therefore the root branch-swap is not an
oriented route exit.

### 5.4 No alternative rescue or category exit

Independent recomputation after the branch-swap gives, for each of

`H_13,H_14,H_23,H_24`:

- the two marked edges remain in one component;
- cutting them gives the same pairing `(1,2)|(3,6)` as before.

The branch-swapped graph is:

- connected;
- simple;
- cubic;
- bridgeless;
- girth `5`;
- free of cyclic edge cuts of size `1,2,3,4`.

The NNI cell is disjoint from the active parent cell and from the retained cap
vertices `7,12`.  Therefore cap identity, active parent obligation, stable
exterior darts and stored-prefix identity do not supply a hidden exit.

A compact audit serialization of this witness has SHA-256

`ff115bd13027ba947f6724e1ba861f9e9682605f955b5e2a0a42399283d5f5b1`.

---

## 6. Consequence for the four equal-neighbour claims

The coefficient movies for `123,234,125,245` are correct **if** one local
passage can be switched alone.  The universal source theorem providing that
component is false.

The Heawood witness directly refutes:

- RL `DDD_LOCK_H14_SWITCH_INVARIANT_DESCENT_THEOREM_V1.md`, Theorem 5.1 as a
  theorem from an arbitrary equal bad face;
- PDL `AC_PD_5CDC_V7_3_FIXED_CHANNEL_XI_RECONSTRUCTION.md`, Section 5.1's claim
  that the third outside matching automatically changes the oriented marked
  route.

It does not refute:

- frame uniqueness;
- whole-component `Xi` invariance;
- the six strict distinct-neighbour rows;
- the bad-free `124/12,24` trapping argument;
- the possibility that a different global selection theorem or an additional
  same-arc macro could repair co-root escape.

---

## 7. Smallest required co-root repair

A valid replacement must add the locations of the two marked edges on the two
outside arcs.  It must prove at least one of:

1. every oriented DDD lock has a distinct bad incidence;
2. every lock has an equal bad face whose marked edges lie on different outside
   arcs, so the existing route-or-split movie is productive;
3. a new root-only macro escapes the same-arc equal-face configuration;
4. the same-arc configuration forces an exact `K_i`, cut or bounded terminal.

The current matching-only lemma proves none of these.  Finiteness, a switch of
the whole common marked component, or repetition of the root branch-swap does
not lower `Xi` in the displayed witness.

---

## 8. Deterministic descent and SCC scope

The scope-hardened fixed-channel idea is sound in principle:

- choose one physical rescue support `h_*`;
- retain it through strict NNIs;
- transport the frame through common-marked `H_{h_*}` switches;
- do not require numerical invariance under unrelated missing-index migrations.

However the deterministic path is not total because an equal bad face can be
nonproductive as above.  Therefore the claimed finite descent and closed-SCC
exclusion do not follow from the present move alphabet.

The bound of at most `N` strict macros is arithmetically correct **conditional
on** existence of a strict macro at every nonabsorbed lock state.

---

## 9. Integration boundary

The candidate correctly limits its theorem claim to co-root/DDD `(4,2,2)`
states and explicitly excludes the zero-parent `(0,2,2)` row.  No zero-parent
mathematics was reviewed or attempted.

Nonlocked co-root states remain covered by the prior separating-channel and
exact terminal object.  Ordinary NNIs and support switches have adequate
literal contracts for cap, darts, parent and prefix data.  The integration
failure is earlier: the locked-sector equal-neighbour escape theorem is not
proved.
