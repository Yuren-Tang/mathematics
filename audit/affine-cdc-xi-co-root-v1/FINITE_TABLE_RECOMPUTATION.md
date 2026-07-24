# AC-AUDIT-XI-01 — independent finite-table recomputation

**Audit role:** temporary independent mathematical reviewer  
**Frozen candidate:** `fee97446ee8b99f07740f394e99ef4a2ecc3e40e`  
**Scope:** fixed-channel `Xi` arithmetic for the co-root/DDD `(4,2,2)` sector only  
**Zero-parent `(0,2,2)` sector:** excluded

This report was recomputed from the root system itself.  No RL/PDL table or
provided digest was used as an input.

---

## 1. Root-system conventions

A root is a two-subset of `[5]`.  Addition is symmetric difference.  A support
triangle `ijk` carries the three roots `ij,ik,jk`.

For `h=14`, an edge belongs to `H_14` exactly when its root meets `{1,4}` in
one element.  Switching one `H_14` component adds `14` to every selected root.
At a support triangle this is the support transposition

`tau_14=(1 4)`.

The candidate weight is

| `T` | 123 | 124 | 125 | 134 | 135 | 145 | 234 | 235 | 245 | 345 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `xi(T)` | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 2 | 1 | 0 |

---

## 2. All ten `tau_14` images

| `T` | `tau_14(T)` | `xi(T)` | `xi(tau_14(T))` |
|---|---|---:|---:|
| 123 | 234 | 1 | 1 |
| 124 | 124 | 0 | 0 |
| 125 | 245 | 1 | 1 |
| 134 | 134 | 0 | 0 |
| 135 | 345 | 0 | 0 |
| 145 | 145 | 0 | 0 |
| 234 | 123 | 1 | 1 |
| 235 | 235 | 2 | 2 |
| 245 | 125 | 1 | 1 |
| 345 | 135 | 0 | 0 |

Thus the seven set-orbits are

- `123 <-> 234`;
- `125 <-> 245`;
- `135 <-> 345`;
- fixed: `124,134,145,235`.

The equality

`xi(tau_14(T))=xi(T)`

holds in all ten cases.

---

## 3. Exhaustive distinct-neighbour rows

The triangles containing root `23` are exactly

`123,234,235`.

The triangles containing root `25` are exactly

`125,235,245`.

Hence there are exactly three unordered distinct pairs for each central root.
For each pair, the four exterior roots have two alternative pairings.  Exactly
one pairing has a root central value; the other has a four-support co-root
central value.

| central | source pair | root-valued exterior pairing | new root | target pair | other central value | source `Xi` | target `Xi` | delta |
|---|---|---|---|---|---|---:|---:|---:|
| 23 | `123+234` | `12-24`, `13-34` | 14 | `124+134` | 1234 | 2 | 0 | -2 |
| 23 | `123+235` | `12-25`, `13-35` | 15 | `125+135` | 1235 | 3 | 1 | -2 |
| 23 | `234+235` | `24-25`, `34-35` | 45 | `245+345` | 2345 | 3 | 1 | -2 |
| 25 | `125+235` | `12-23`, `15-35` | 13 | `123+135` | 1235 | 3 | 1 | -2 |
| 25 | `125+245` | `12-24`, `15-45` | 14 | `124+145` | 1245 | 2 | 0 | -2 |
| 25 | `235+245` | `23-24`, `35-45` | 34 | `234+345` | 2345 | 3 | 1 | -2 |

Every target triangle is root-valued.  Every row has exactly one root-valued
opposite NNI and satisfies `Delta Xi=-2`.

---

## 4. Equal-pair coefficient placements

For an equal pair, write the two vertices as `u,v`, the central root as `r`,
and the two exterior roots as `x,y`.  There are exactly three labelled
pairings of the four exterior darts:

1. current root placement: `(x_u,y_u) | (x_v,y_v)`;
2. other root placement: `(x_u,y_v) | (y_u,x_v)`;
3. zero placement: `(x_u,x_v) | (y_u,y_v)`.

The first two have central root `x+y=r`.  The third has central value zero.
The four bad equal rows are:

| equal type | central root | exterior roots | `tau_14(T)` | mixed pair after one one-passage switch | strict final row |
|---|---|---|---|---|---|
| 123 | 23 | 12,13 | 234 | `123+234` | `124+134` |
| 234 | 23 | 24,34 | 123 | `234+123` | `124+134` |
| 125 | 25 | 12,15 | 245 | `125+245` | `124+145` |
| 245 | 25 | 24,45 | 125 | `245+125` | `124+145` |

The coefficient calculation is correct: if a legal closed `H_14` switch can
be applied to exactly one local passage, the switch preserves global `Xi`, the
local pair becomes `T+tau_14(T)`, and the final root NNI lowers `Xi` by two.

The finite table does **not** prove that such a one-passage component always
exists or that the root branch-swap always changes the marked route.  That is a
separate source-geometry assertion audited in
`SOURCE_MOVIE_AND_SCOPE_LEDGER.md`.

---

## 5. Independent serialization digest

For reproducibility I serialized an independently chosen JSON object containing:

- the ten `(T,tau_14(T),xi(T),xi(tau_14(T)))` rows;
- the six strict rows, including both alternative central values;
- the four equal rows and their three labelled pairings.

Sorted keys and compact separators give SHA-256

`d77520804de5ee0febd29b6ae28af3c62f45887d4f70d392e283eb7b3576a617`.

This is an audit digest for this report's schema.  It is intentionally
independent of the RL serialization and does not validate any source-geometry
claim.

---

## 6. Finite-table verdict

- canonical-frame arithmetic: **verified**;
- all ten `tau_14` images: **verified**;
- vertex-weight invariance under `tau_14`: **verified**;
- six distinct-neighbour rows: **verified**;
- four equal-row coefficient movies, conditional on a one-passage component:
  **verified**;
- universal equal-neighbour route-or-split implication: **not a finite-table
  consequence and not verified here**.
