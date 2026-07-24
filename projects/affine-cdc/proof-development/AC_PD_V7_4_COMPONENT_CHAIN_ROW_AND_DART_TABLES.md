# AC-PD v7.4 — component-chain row and dart tables

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Frozen RL source:** `02b37476198e9eaa2b4cd8d2a2edd76782bdcd49`  
**Classification:** `EXHAUSTIVE FINITE SOURCE TABLE / COMPLETE-DRAFT`.

This dossier records the coefficient and labelled-dart tables used by
`AC_PD_V7_4_COMPONENT_CHAIN_THEOREM_RECONSTRUCTION.md`.  The tables were
recomputed from the ten two-subset roots and ten support triangles; RL/PDL
finite tables were not treated as proof inputs.

---

## 1. General active/inactive row

Fix

\[
h=ab,\qquad I_h=\{i,j,k\}=[5]\setminus h.
\]

Let the witnessed non-channel connector have root `ij`, joining

\[
T=\{i,j,a\}
\]

to the inactive triangle `I_h=ijk`.  Label the exterior darts at the active
endpoint by roots `ia,ja` and those at the inactive endpoint by `ik,jk`.

The three labelled placements are:

1. current placement `ia-ja | ik-jk`, central `ij`;
2. root opposite placement `ia-ik | ja-jk`, central `ak`;
3. co-root opposite placement `ia-jk | ja-ik`, central `ijak`.

Thus the root alternative is unique:

\[
ija+ijk\longrightarrow ika+jka.
\]

The stable connector edge retains its two central darts but changes root
`ij -> ak`.  The four exterior stable edges are not renamed.  Their inside
darts are reattached according to the root placement; all outside endpoints and
outside darts are fixed.

The old channel passage `ia--ja` becomes `ia--ak--ja`.  The exterior roots
`ik,jk` remain non-channel.

---

## 2. Complete canonical `H_35` active/inactive table

For `h=35`, the inactive type is `124`.  There are exactly six active neighbours
through a non-`H_35` root.

| source pair | old central | root target pair | new central | nonroot alternative |
|---|---:|---|---:|---:|
| `123+124` | `12` | `134+234` | `34` | `1234` |
| `125+124` | `12` | `145+245` | `45` | `1245` |
| `134+124` | `14` | `123+234` | `23` | `1234` |
| `145+124` | `14` | `125+245` | `25` | `1245` |
| `234+124` | `24` | `123+134` | `13` | `1234` |
| `245+124` | `24` | `125+145` | `15` | `1245` |

Every new central root meets `35` once; both target triangles are active.  No
zero alternative occurs in these six rows.

### Dart contract for a row

Write the old central darts as `e@u,e@v`.  At the inactive vertex let the two
other stable darts be `f@v,g@v`; at the active vertex let them be `p@u,q@u`.
The unique root placement fixes the four outside endpoints and pairs the inside
darts so that:

- `p,q` remain the two terminal ends of the enlarged channel passage;
- the new central edge is in `H_35`;
- `f,g` remain non-`H_35` frontier connectors;
- if `f` is the next inherited connector, the same stable edge and outside dart
  survive at one of the two target vertices.

This is true symmetrically when `g` is the inherited connector.

---

## 3. General active/active distinct row

Let two distinct active triangles share their non-channel root `ij`:

\[
T=ijk,\qquad U=ijl,\qquad k\ne l.
\]

The four channel roots are

\[
ik,jk,il,jl.
\]

The two opposite placements have central values:

\[
(ik+il)=(jk+jl)=kl\in R_5,
\]

and

\[
(ik+jl)=(jk+il)=ijkl,
\]

a four-support co-root.  Hence the unique root cross-connection is

\[
ik-il\mid jk-jl
\]

with central root `kl`.

Since the paired exterior roots are both in `H_h`, the symmetric difference
`kl` meets `h` zero or two times and is outside `H_h`.  Thus the NNI reconnects
the channel passages without adding a channel branch.

An exhaustive enumeration over all ten choices of `h` and all adjacent active
triangle pairs found no exceptional distinct row.

---

## 4. Equal active endpoints

Let both endpoint triangles be `T={i,j,k}` and let the central non-channel root
be `ij`.  The two exterior roots at both endpoints are `ik,jk`.

The three labelled placements are:

1. current root placement
   `ik_u-jk_u | ik_v-jk_v`;
2. root branch swap
   `ik_u-jk_v | jk_u-ik_v`;
3. zero placement
   `ik_u-ik_v | jk_u-jk_v`.

The component-chain theorem uses placement 2 only.  It preserves the root
central value `ij` and is a labelled ordinary NNI.  Placement 3 is never
traversed.

Unlike the withdrawn arbitrary-equal-face lemma, no inference is made from the
outside four-port matching alone.  The move is selected only when the two local
passages belong to two named distinct quotient components, or at the final
connector to the two named terminal paths.

---

## 5. Physical transition table

| endpoint node types | selected move | channel effect | inherited-chain effect |
|---|---|---|---|
| active path + inactive singleton | unique active/inactive root NNI | insert inactive vertex into path | consume first connector; next stable nonchannel connector survives |
| active path + distinct active cycle endpoint | unique distinct root NNI | path and cycle become one path | consume first connector; exit connector is at another active vertex |
| active path + equal active cycle endpoint | root branch swap | path and cycle become one path | same |
| closed cycle + closed cycle | distinct root NNI or equal branch swap | one closed cycle | used only in a general quotient contraction, not between the two terminal endpoints |
| terminal path + terminal path | distinct root NNI or equal branch swap | two terminal paths with opposite matching | final target progress |

Every physical failure of looplessness, bridgelessness, cubic category, fixed
route or cap profile is returned immediately to its exact existing consumer.

---

## 6. Why future connectors remain valid

### Inactive singleton

The next quotient edge may share the modified inactive source vertex with the
first edge.  Its root is one of `ik,jk`; it is unchanged, remains outside
`H_h`, and its stable outside dart is fixed.  Its inside dart lands on an active
vertex of the enlarged component.

### Active cycle

A channel-active cubic vertex has two channel incidences and exactly one
non-channel incidence.  Therefore the entry connector and a distinct exit
connector cannot meet the same active source vertex.  The exit edge and its
endpoint darts are untouched by the first NNI.

### Later components

The new channel edges in a contraction connect only the first two quotient
nodes.  The new central edge in an active/active contraction is outside `H_h`.
No later component can be merged silently.

---

## 7. Final matching table

Let the current terminal matching be `AB|CD`.  At the final connector the two
local passages lie in different terminal paths.  The root cross-connection gives
exactly one of:

\[
AC|BD,\qquad AD|BC.
\]

For equal endpoint triangles, the root branch swap gives the same two
possibilities according to the ordered local darts.  The zero placement is not
used.  Hence no final row preserves `AB|CD`.

This statement depends on the two passages being different distinguished
components; it does not revive the false same-arc equal-face claim.

---

## 8. Finite-verification boundary

Independently recomputed:

- all ten `H_h` degree tables;
- the unique inactive triangle for every `h`;
- all six canonical `H_35` active/inactive rows;
- all active/active distinct rows for every `h`;
- the equal-endpoint three-placement table;
- uniqueness of the root alternative in every distinct row.

The finite arithmetic verifies the local rows.  Physical chain totality is
proved by the inherited stable-connector argument, not by enumeration.