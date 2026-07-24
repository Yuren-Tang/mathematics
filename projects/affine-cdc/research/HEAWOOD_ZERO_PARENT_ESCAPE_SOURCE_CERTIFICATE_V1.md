# Heawood zero-parent escape — complete source certificate v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-03`  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `212d789a5967813e7277fb3e269060926c99cb0e`  
**PDL input:** `proof-development/affine-cdc-rigour-v1@fee97446ee8b99f07740f394e99ef4a2ecc3e40e`  
**Classification:** `COMPLETE FINITE SOURCE MOVIE / MODEL CASE ONLY / UNIVERSAL ZERO-PARENT THEOREM NOT CLAIMED HERE`.

This dossier independently reconstructs the candidate movie prescribed in
`research-workbench#77`.  Every edge below has a persistent physical identity;
an NNI moves only the named local dart while retaining the opposite outside
dart.  The verification is therefore a labelled source movie, not a
coefficient-only calculation.

---

## 1. Initial labelled Heawood flow

Use vertices `1,...,14` and the twenty-one persistent edge identities

```text
e1_2   e1_6   e1_14  e2_3   e2_11  e3_4   e3_8
e4_5   e4_13  e5_6   e5_10  e6_7   e7_8   e7_12
e8_9   e9_10  e9_14  e10_11 e11_12 e12_13 e13_14.
```

Their initial endpoints and roots are

| edge id | endpoints | root |
|---|---:|---:|
| `e1_2` | `1-2` | `23` |
| `e1_6` | `1-6` | `12` |
| `e1_14` | `1-14` | `13` |
| `e2_3` | `2-3` | `34` |
| `e2_11` | `2-11` | `24` |
| `e3_4` | `3-4` | `13` |
| `e3_8` | `3-8` | `14` |
| `e4_5` | `4-5` | `12` |
| `e4_13` | `4-13` | `23` |
| `e5_6` | `5-6` | `13` |
| `e5_10` | `5-10` | `23` |
| `e6_7` | `6-7` | `23` |
| `e7_8` | `7-8` | `24` |
| `e7_12` | `7-12` | `34` |
| `e8_9` | `8-9` | `12` |
| `e9_10` | `9-10` | `13` |
| `e9_14` | `9-14` | `23` |
| `e10_11` | `10-11` | `12` |
| `e11_12` | `11-12` | `14` |
| `e12_13` | `12-13` | `13` |
| `e13_14` | `13-14` | `12` |

The support triangles at vertices `1,...,14` are

```text
123,234,134,123,123,123,234,124,123,123,124,134,123,123.
```

In particular the active vertices `4,5` and the remote vertices `13,14` are
all of type `123`.  The active edge is the persistent edge `e4_5`, with
central root `12`, and its ordered exterior branches are

```text
A = e3_4  : 3-4  : 13,
B = e5_6  : 5-6  : 13,
C = e4_13 : 4-13 : 23,
D = e5_10 : 5-10 : 23.
```

Thus

\[
(A,B,C,D)=(13,13,23,23),
\]

with current crossed topology `AC|BD` and literal prescribed parent `AB|CD`.
The current central root is `13+23=12`; the parent central value is zero.

---

## 2. Exact dart convention

For each persistent edge identity `e`, retain two persistent darts.  An NNI
reattachment changes the incident vertex of only the named local dart; the
opposite outside dart, the edge identity, root label and ancestry remain fixed.

The complete movie moves exactly four noncentral local darts:

| step | edge id | fixed outside dart | moved local dart |
|---|---|---|---|
| remote branch swap | `e12_13` | at vertex `12` | `13 -> 14` |
| remote branch swap | `e1_14` | at vertex `1` | `14 -> 13` |
| literal parent NNI | `e5_6` | at vertex `6` | `5 -> 4` |
| literal parent NNI | `e4_13` | at vertex `13` | `4 -> 5` |

The central edge identities `e13_14` and `e4_5` retain both endpoints.
The former retains root `12`; the latter changes root only in the final parent
NNI, from `12` to `35`.

No dart is created, deleted, identified or recoloured without the displayed
support switch.

---

## 3. Step 1 — remote equal-face root branch swap

At the remote edge `e13_14`, retain

```text
e4_13 : 4-13 : 23,
e9_14 : 9-14 : 23,
e13_14:13-14 : 12.
```

Move the two root-`13` local darts:

```text
e12_13 : 12-13 -> 12-14,
e1_14  : 1-14  -> 1-13.
```

The new remote incidences are therefore

```text
vertex 13: e1_14:13, e4_13:23, e13_14:12,
vertex 14: e12_13:13, e9_14:23, e13_14:12.
```

Both vertices remain type `123`; every other root and every other incidence is
unchanged.  This is the other root-valued equal-face placement, not the zero
placement.

### Exact `H_35` route change

An edge lies in `H_35` exactly when its root contains precisely one of supports
`3,5`.  Before the remote NNI, the complementary four-pole has matching

```text
AD | BC.
```

After the remote NNI it has matching

```text
AC | BD.
```

The local active placement is also `AC|BD`; hence the complete physical
`H_35` system splits into two closed components.

The components are exactly

\[
Z_0=1-2-3-4-13-1
\]

with edge set

```text
{e1_2,e2_3,e3_4,e4_13,e1_14}
= {1-2,2-3,3-4,4-13,1-13},
```

and

\[
Z_1=5-6-7-12-14-9-10-5
\]

with edge set

```text
{e5_6,e6_7,e7_12,e12_13,e9_14,e9_10,e5_10}
= {5-6,6-7,7-12,12-14,9-14,9-10,5-10}.
```

There are no further `H_35` edges.  The active branches satisfy

```text
A,C in Z_0,
B,D in Z_1.
```

Thus `Z_0` is the required mixed separating physical component.

---

## 4. Step 2 — switch the physical component `Z_0`

Switch `Z_0` by the fixed support root `35`.  Every edge of `Z_0` keeps its
physical identity and endpoints and changes root by symmetric difference with
`35`:

```text
23 -> 25,
34 -> 45,
13 -> 15.
```

The switched edge table on `Z_0` is

| edge | old root | new root |
|---|---:|---:|
| `e1_2` | `23` | `25` |
| `e2_3` | `34` | `45` |
| `e3_4` | `13` | `15` |
| `e4_13` | `23` | `25` |
| `e1_14` (`1-13`) | `13` | `15` |

Every vertex on `Z_0` undergoes the support transposition `(3 5)`:

```text
1:123->125,
2:234->245,
3:134->145,
4:123->125,
13:123->125.
```

All other triangles remain unchanged.  Root conservation holds at every
vertex.  The same physical edge set remains `H_35`; the switch is a legal
closed-component involution.

The active word is now literally

\[
(A,B,C,D)=(15,13,25,23),
\]

because

```text
A=e3_4 : 13->15,
B=e5_6 : 13 unchanged,
C=e4_13:23->25,
D=e5_10:23 unchanged.
```

The current central edge `e4_5` remains root `12`, since it is not in `H_35`.
But

\[
15+13=35,
\qquad
25+23=35.
\]

Therefore the literal stored parent `AB|CD` is now root-valued with central
root `35`.

---

## 5. Step 3 — literal prescribed-parent NNI

Perform the stored parent NNI on the persistent central edge `e4_5`:

```text
e5_6  : 5-6  -> 4-6   (outside dart at 6 fixed),
e4_13 : 4-13 -> 5-13  (outside dart at 13 fixed),
e4_5  : root 12 -> 35 (endpoints 4,5 fixed).
```

The final active vertices are

```text
vertex 4: A=15, B=13, central=35, triangle 135;
vertex 5: C=25, D=23, central=35, triangle 235.
```

Hence the final topology is exactly `AB|CD`, not merely an isomorphic crossed
topology.  The live prescribed-parent obligation is discharged and the stored
prefix dart identity can be crossed literally.

---

## 6. Cap-block audit

Retain the cap vertices `7,12` and all six incident persistent darts.

At vertex `7` the incident edge identities

```text
e6_7, e7_8, e7_12
```

never change endpoint or root.

At vertex `12` the incident edge identities

```text
e7_12, e11_12, e12_13
```

remain the same.  The cap dart of `e12_13` at vertex `12` is fixed throughout;
only its opposite local dart is reattached from vertex `13` to vertex `14`.
Its root remains `13`.  Thus the remote NNI is disjoint from the cap **as a
labelled cap interface**, even though one moved edge has its fixed outside dart
at cap vertex `12`.

No cap vertex, cap dart, cap order, or distinguished cap incidence is changed.

---

## 7. Route/profile and support-field audit

The only intended route change before absorption is the physical `H_35`
matching change

```text
AD|BC  ->  AC|BD
```

in the complementary four-pole.  It is recomputed from the persistent edge
identities after the remote NNI; it is not inferred from endpoint notation.
This produces the exact split `Z_0|Z_1` above.

Switching `Z_0` retains the physical `H_35` edge set and component partition.
All other support-component partitions are recomputed from the new root labels;
none is used as an unstated transition.  The final parent NNI consumes the live
obligation immediately, so no post-parent lock field is required.

The support channel is the same physical root `35` throughout.  There is no
quotient by support permutations and no hidden frame migration.

---

## 8. Exact graph-category recomputation

A direct labelled subset enumeration was performed independently for each
uncoloured topology.  For cyclic edge connectivity, all nontrivial vertex
shores were enumerated; a cut was accepted only when both induced shores were
connected and each contained a cycle.

| state | connected | simple | bridges | edge connectivity | cyclic edge connectivity | girth |
|---|---:|---:|---:|---:|---:|---:|
| original Heawood | yes | yes | none | `3` | `6` | `6` |
| after remote NNI | yes | yes | none | `3` | `5` | `5` |
| after `Z_0` switch | yes | yes | none | `3` | `5` | `5` |
| final parent NNI | yes | yes | none | `3` | `5` | `5` |

The support switch does not change the uncoloured topology, so the middle two
rows agree.

One minimum cyclic-cut witness after the remote NNI is the shore

```text
{1,2,3,4,13}
```

with cut

```text
{1-6,2-11,3-8,4-5,13-14}.
```

One minimum cyclic-cut witness after the final parent NNI is the shore

```text
{1,2,3,4,6}
```

with cut

```text
{1-13,2-11,3-8,4-5,6-7}.
```

Consequently no state in the movie has a cyclic `2`, `3`, or `4` cut, loop,
parallel edge, bridge, or bounded category degeneration.  The movie remains in
the prime category until literal parent success.

---

## 9. Finite certificate and reproducibility

The companion script

```text
projects/affine-cdc/research/finite/heawood_zero_parent_escape_certificate_v1.py
```

reconstructs the persistent-edge states, validates all fourteen root triangles,
enumerates `H_35` components, verifies the active word, and computes the graph
category table by exhaustive labelled subset search.

Its canonical JSON certificate has SHA-256 digest

```text
db160ee18300ead7aaf28c56cf83be1068c243b1e51aeabfc896f74c1615b14b
```

under sorted-key, separator-free JSON serialization.

---

## 10. Exact result and boundary

The issue-#77 candidate movie is correct:

\[
\boxed{
\text{remote root branch swap at }13-14
\to H_{35}\text{ split}
\to Z_0\text{ switch}
\to (15,13,25,23)
\to \text{literal parent root }35.}
\]

It is a finite, root-valued, same-order, source-faithful movie.  It uses no
`2--0` cancellation, no lower-order call, no second crossed-parent substitution,
no track erasure, no SCC distance, and no retired mixed-order machinery.

This certificate proves only that the PDL Heawood witness is escapable.  It does
not by itself prove `FC-PURE-NNI-ZERO-PARENT-ESCAPE` for every complete
`(0,2,2)` state.
