# Zero-parent Heawood `H_35` source-movie certificate

## Research Lead certificate v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-03`  
**Frozen start:** `research/affine-cdc-five-cdc-v1@212d789a5967813e7277fb3e269060926c99cb0e`  
**PDL input:** `proof-development/affine-cdc-rigour-v1@fee97446ee8b99f07740f394e99ef4a2ecc3e40e`  
**Classification:** `COMPLETE SOURCE CERTIFICATE / MODEL CASE ONLY`.

This file independently verifies the exact movie required by issue
`research-workbench#77`.  The verification is on labelled physical edges and
darts, not only on endpoint notation or coefficient multisets.

The movie is valid.  It gives a root-valued same-order history

```text
remote equal-face branch swap at 13--14
    -> split physical H_35
    -> switch Z_0
    -> literal parent NNI at 4--5.
```

It proves that the PDL Heawood witness is escapable.  It is not by itself the
universal zero-parent theorem.

---

## 1. Fixed labelled Heawood source

Use vertices `1,...,14`.  Each physical edge has a persistent identity `e_uv`;
when an NNI reattaches an edge, the exterior dart and edge identity survive.
The initial root flow is:

| edge identity | endpoints | root |
|---|---:|---:|
| `e1_2` | `1--2` | `23` |
| `e1_6` | `1--6` | `12` |
| `e1_14` | `1--14` | `13` |
| `e2_3` | `2--3` | `34` |
| `e2_11` | `2--11` | `24` |
| `e3_4` | `3--4` | `13` |
| `e3_8` | `3--8` | `14` |
| `e4_5` | `4--5` | `12` |
| `e4_13` | `4--13` | `23` |
| `e5_6` | `5--6` | `13` |
| `e5_10` | `5--10` | `23` |
| `e6_7` | `6--7` | `23` |
| `e7_8` | `7--8` | `24` |
| `e7_12` | `7--12` | `34` |
| `e8_9` | `8--9` | `12` |
| `e9_10` | `9--10` | `13` |
| `e9_14` | `9--14` | `23` |
| `e10_11` | `10--11` | `12` |
| `e11_12` | `11--12` | `14` |
| `e12_13` | `12--13` | `13` |
| `e13_14` | `13--14` | `12` |

Every vertex carries one support triangle.  In particular:

- vertices `4,5,13,14` have type `123`;
- the active central edge is `e4_5:12`;
- the active ordered exterior darts are
  
  \[
  A=e3\_4:13,\qquad B=e5\_6:13,\qquad
  C=e4\_{13}:23,\qquad D=e5\_{10}:23;
  \]
- the current topology is `AC|BD` and the prescribed parent is `AB|CD`;
- the retained cap vertices are `7,12`.

Thus the active word is exactly

\[
(A,B,C,D)=(13,13,23,23)
\]

with current central root `12` and parent central value zero.

---

## 2. Step 1 — remote equal-face branch swap at `e13_14`

The equal face has central edge `e13_14:12`.  Its four exterior edge identities
are

\[
e4\_{13}:23,\quad e12\_{13}:13,
\quad e9\_{14}:23,\quad e1\_{14}:13.
\]

Perform the other root-valued placement while retaining `e13_14` as the
central physical edge:

| edge identity | old endpoints | new endpoints | root |
|---|---:|---:|---:|
| `e12_13` | `12--13` | `12--14` | `13` |
| `e1_14` | `1--14` | `1--13` | `13` |
| `e4_13` | `4--13` | unchanged | `23` |
| `e9_14` | `9--14` | unchanged | `23` |
| `e13_14` | `13--14` | unchanged | `12` |

The dart at vertex `12` of `e12_13` remains the same cap dart, in the same cap
slot and with root `13`; only its opposite endpoint moves from `13` to `14`.
The dart at vertex `1` of `e1_14` likewise survives literally.  Therefore
`delta`, the cap-vertex identities, the cap slots and `alpha` have an explicit
edge-by-edge update.

The two local triangles remain `123`; all other vertex triangles are unchanged.
No zero or co-root coefficient occurs.

### Exact route change

Before this remote branch swap, the physical outside `H_35` matching at the
active four ports is

\[
AD\mid BC.
\]

After the branch swap it is

\[
AC\mid BD,
\]

which agrees with the current active placement.  Consequently the closed
`H_35` system splits into two components rather than one common marked cycle.
If the complete route/profile ledger consumes this matching change earlier, it
is already an accepted route output; on the prime nonterminal branch the movie
continues below.

---

## 3. Step 2 — exact physical `H_35` split

An edge belongs to `H_35` exactly when its root contains exactly one of supports
`3,5`.  Since the displayed flow initially uses no support `5`, these are
precisely the edges whose roots contain `3`.

After Step 1 the complete components are exactly:

\[
Z_0=1-2-3-4-13-1
\]

with physical edge set

\[
\{e1\_2,e2\_3,e3\_4,e4\_{13},e1\_{14}\},
\]

and

\[
Z_1=5-6-7-12-14-9-10-5
\]

with physical edge set

\[
\{e5\_6,e6\_7,e7\_{12},e12\_{13},e9\_{14},e9\_{10},e5\_{10}\}.
\]

Thus:

- `Z_0` contains exactly the active occurrences `A=e3_4:13` and
  `C=e4_13:23`;
- `Z_1` contains exactly `B=e5_6:13` and `D=e5_10:23`.

The retained cap vertices `7,12` lie in `Z_1`; the selected switch component
`Z_0` is cap-disjoint.

---

## 4. Step 3a — switch `Z_0` by `35`

Switching a complete physical `H_35` component replaces each root `r` on that
component by `r+35`.  The five changed edge roots are:

| edge identity | old root | new root |
|---|---:|---:|
| `e1_2` | `23` | `25` |
| `e2_3` | `34` | `45` |
| `e3_4` | `13` | `15` |
| `e4_13` | `23` | `25` |
| `e1_14` | `13` | `15` |

Every vertex remains root-valued.  The affected triangle types are

\[
123\leftrightarrow125,\qquad
234\leftrightarrow245,\qquad
134\leftrightarrow145.
\]

The active word is now literally

\[
(A,B,C,D)=(15,13,25,23),
\]

while the current central physical edge `e4_5` remains root `12`.

Hence

\[
A+B=15+13=35,
\qquad
C+D=25+23=35.
\]

The prescribed parent has become root-valued.

---

## 5. Step 3b — literal parent NNI

Perform the stored parent pairing `AB|CD` on the same active edge/dart set.
Retain `e3_4` at vertex `4` and `e5_10` at vertex `5`, and reattach:

| edge identity | old endpoints | new endpoints | root |
|---|---:|---:|---:|
| `e5_6` | `5--6` | `4--6` | `13` |
| `e4_13` | `4--13` | `5--13` | `25` |
| `e4_5` | `4--5` | unchanged | `12 -> 35` |

The final active triangles are

\[
\Delta_4=135,\qquad \Delta_5=235.
\]

This is the literal labelled parent topology, not merely an isomorphic cubic
graph.  The exterior darts at `3,6,13,10`, all edge identities, the retained cap
block and the prefix map `alpha` are explicit.

---

## 6. Complete graph-category check

A fresh exhaustive labelled subset computation gives:

| topology | connected | simple | bridgeless | cyclic edge-connectivity |
|---|---:|---:|---:|---:|
| initial Heawood | yes | yes | yes | `6` |
| after remote branch swap | yes | yes | yes | `5` |
| after final parent NNI | yes | yes | yes | `5` |

The support switch changes only coefficients and therefore has the same
uncoloured category as the post-remote topology.  No intermediate graph has a
loop, parallel edge, bridge or cyclic `2/3/4` cut.  If any named route or
bounded category test fires in a more general contextual use, the exact named
consumer is taken instead; this certificate verifies the prime branch.

---

## 7. A shorter conjugate movie on the same witness

The remote move is valid, but the same matching alignment can be performed at
the active face itself.

1. Cross the active edge from `AC|BD` to `AD|BC`, reattaching `e5_10` to vertex
   `4` and `e4_13` to vertex `5`; the central root remains `12`.
2. The existing outside `H_35` matching is already `AD|BC`, so the complete
   components become
   
   \[
   1-2-3-4-10-9-14-1
   \]
   
   containing `A,D`, and
   
   \[
   5-6-7-12-13-5
   \]
   
   containing `B,C`.
3. Switch the first component by `35`, obtaining active word
   `(15,13,23,25)`.
4. Perform the literal parent NNI with central root `35`.

This conjugate version is cap-disjoint at every move.  It is included as a
source simplification, not as a replacement for the mandatory remote-movie
certificate.

---

## 8. Reproducible finite certificate

The standard-library script

`projects/affine-cdc/research/certificates/zero_parent_heawood_and_s3_rank_v1.py`

recomputes:

- every vertex triangle before and after each move;
- the two exact `H_35` components;
- the active word and final central root;
- connectedness, simplicity, bridgelessness and cyclic edge-connectivity;
- the finite rank table used by the universal theorem.

Canonical certificate digest:

`d22bce5ea026f5c461575f05ed81ed6e68c71a0c3c459ce6ada93d96f458422e`.

---

## 9. Scope

Closed by this file:

- the exact issue-#77 Heawood source movie;
- its dart ancestry, cap preservation, support switch and category checks;
- an explicit shorter conjugate source movie.

Not claimed by this file alone:

- the universal `FC-PURE-NNI-ZERO-PARENT-ESCAPE` theorem;
- independent PDL reconstruction;
- an accepted cubic five-support or five-CDC theorem;
- Lean, canonical, manuscript, release or publication status.
