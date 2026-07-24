# AC-AUDIT-CHAIN-01 — focused independent audit report

**Classification:** `BLOCKED — MATERIAL GAP OR FALSE SCOPE`  
**Frozen Research Lead source:** `Yuren-Tang/mathematics@02b37476198e9eaa2b4cd8d2a2edd76782bdcd49`  
**Owned audit branch:** `audit/affine-cdc-component-chain-v1`  
**Permanent negative boundary retained:** `audit/affine-cdc-xi-co-root-v1@53be22a0f65b85068b11e5f781579618967db9dd`  
**Controlling source theorem:** `projects/affine-cdc/research/FIXED_CHANNEL_COMPONENT_CHAIN_ROOT_NNI_THEOREM_V1.md`

---

## 1. Executive disposition

The fixed-channel component-chain mechanism is **not a universal theorem in the
scope stated in Theorem 5.1**.

The local contraction movies are sound in the two cases actually analysed by
the source:

1. an internal quotient node is one channel-inactive vertex; or
2. an internal quotient node is a closed `H_h` cycle.

The statement, however, assumes only that `P_0,P_1` are two distinguished
terminal path components.  It does not assume that they are the only terminal
path components.  A shortest quotient path may therefore have a third terminal
path as an internal node.  Such a node is neither Case A nor Case B.  Moreover,
the root NNI at either adjacent connector changes the terminal matching of the
two incident paths; it does not contract them to one inherited path with the
same distinguished terminal pair.

This is not a prose-only omission.  Section 3 gives a complete labelled
category-safe Heawood carrier for which:

- the shortest witnessed quotient chain has length `2`;
- its internal node is a third terminal path;
- every one of the `36` labelled root-valued NNIs available in the carrier is
  category-safe;
- none produces an inherited length-`1` chain between the two original
  distinguished terminal pairs.

Thus the source has promoted an application-specific theorem — exactly two
terminal paths, all other nontrivial channel components closed — to a broader
universal statement.  The inherited-chain conclusion is false in that broader
scope.

The co-root and zero-parent applications themselves do impose the omitted
two-terminal-path geometry.  The counterexample therefore does **not** refute
either corollary directly.  In accordance with the stop rule in issue #81,
review stopped at the material general-theorem defect; no replacement theorem
or Research Lead repair was invented.

---

## 2. Exact allocation of the defect

| Layer | Audit disposition |
|---|---|
| General chain theorem | **Material false scope.** Theorem 5.1 permits an internal terminal-path node, but its proof and conclusion require internal nodes to be inactive singletons or closed cycles. |
| Co-root corollary | The #78 counterexample remains valid against the old arbitrary-equal-face lemma. The new `6-7` movie and the two-marked-arc local matching calculation were independently verified. No new co-root counterexample was found before the mandatory stop, but universal end-to-end acceptance is not granted. |
| Zero-parent corollary | The exact Heawood `H_35` movie, category data, crossed-sheet alignment, component switch and literal parent NNI were independently reproduced. The universal corollary was not promoted after the general theorem failed in stated scope. |
| End-to-end integration | **Blocked.** The controlling totality theorem is misstated, and a corrected application-specific theorem has not been independently reconstructed in this audit. |

The result is therefore not `VERIFIED SUBJECT TO BOUNDED EXPLICITNESS
REPAIRS`: the missing terminal-component hypothesis changes the mathematical
domain and is refuted by a labelled source carrier, rather than merely requiring
more exposition.

---

## 3. Complete labelled counterexample to universal chain contraction

### 3.1 Root-valued Heawood state

Use the exact fourteen-vertex root state independently reconstructed from the
frozen source:

| stable edge | root | stable edge | root | stable edge | root |
|---|---:|---|---:|---|---:|
| `1-2` | `23` | `1-6` | `12` | `1-14` | `13` |
| `2-3` | `34` | `2-11` | `24` | `3-4` | `13` |
| `3-8` | `14` | `4-5` | `12` | `4-13` | `23` |
| `5-6` | `13` | `5-10` | `23` | `6-7` | `23` |
| `7-8` | `24` | `7-12` | `34` | `8-9` | `12` |
| `9-10` | `13` | `9-14` | `23` | `10-11` | `12` |
| `11-12` | `14` | `12-13` | `13` | `13-14` | `12` |

Every vertex carries one of the ten support triangles and satisfies the root
equation.  The stable-state digest under the source JSON convention is

`4bfadd66ae43ed73c0cb339524884d295264b5468794406412770788993c799d`.

Fix `h=14`.  Cut the interiors of the three selected channel edges

```text
1-14:13,  10-11:12,  13-14:12.
```

Keep all six resulting terminal darts with their stable identities.

### 3.2 Three ordered terminal paths

The cut `H_14` system has exactly three terminal path components:

| node | vertices | ordered terminal darts |
|---|---|---|
| `P_0` | `{1,2,3,4,5,6,11}` | `1-14@1`, `10-11@11` |
| `X_1` | `{7,8,9,10,12,13}` | `10-11@10`, `13-14@13` |
| `P_1` | `{14}` | `1-14@14`, `13-14@14` |

The physical non-`H_14` quotient edges include

```text
P_0 -- 3-8:14 -- X_1 -- 9-14:23 -- P_1,
```

and there is no quotient edge from `P_0` directly to `P_1`.  Hence this is a
shortest simple quotient path of length `2`, exactly within the written
hypotheses of Theorem 5.1.  Its internal node `X_1` is a terminal path, not a
closed cycle.

### 3.3 The prescribed first-connector NNI

At stable connector `3-8:14`, the endpoint triangles are `134` and `124`.
The unique root-valued opposite row is

```text
134 + 124  ->  234 + 123,     central root 14 -> 23.
```

One exact labelled realization is:

```text
retain  2-3@3:34  and  8-9@8:12;
move    7-8@8:24  to vertex 3;
move    3-4@3:13  to vertex 8.
```

All stable edge identities, the other endpoint of every moved dart, and all
terminal-dart identities are retained.

After the move, the cut `H_14` components are:

| component | vertices | terminal darts |
|---|---|---|
| `Y_0` | `{1,4,5,6,8,9,10}` | `1-14@1`, `10-11@10` |
| `Y_1` | `{2,3,7,11,12,13}` | `10-11@11`, `13-14@13` |
| `P_1` | `{14}` | `1-14@14`, `13-14@14` |

The two original `P_0` terminal darts, `1-14@1` and `10-11@11`, now lie in
different channel components.  Consequently there is no inherited node
`P_0'`, and the claimed path

```text
P_0', P_1
```

does not exist.

The resulting complete graph is connected, simple, cubic, bridgeless, has
girth `5`, and has cyclic edge-connectivity `5`.  No route/category terminal
excuses the failed inheritance.  Its stable-state digest is

`d0987e1e4f72a8f8b535718b3075a5053f9b10609a67a68bf885f316e070e6f2`.

### 3.4 Exhaustion of all one-NNI alternatives

The checker retained physical darts, stable edge ancestry, root labels and the
six ordered terminal darts.  It enumerated every non-cut central edge and every
labelled root-valued alternative:

```text
18 non-cut central edges
36 labelled root-valued NNI movies
36 connected, simple, cubic, bridgeless outputs
36 outputs of girth 5 and cyclic edge-connectivity 5
0 inherited length-1 chains between the original P_0 and P_1 terminal pairs.
```

Outcome partition:

```text
24 movies keep all three original terminal pairs internally connected,
   but still have no P_0--P_1 quotient edge;
10 movies split P_0 and X_1;
 2 movies split P_1 and X_1.
```

Thus this finite certificate refutes not only the source's chosen first-edge
proof step, but the one-NNI inherited-chain conclusion on this labelled
carrier.

Canonical counterexample-certificate digest:

`d24c63ab56320803b9c795ac08389674b6f67edf89dc5c4ef9a729c5436a3e61`.

The full certificate schema is recorded in
`CHAIN_INHERITANCE_AND_COROLLARY_LEDGER.md`.

---

## 4. Independently verified bounded mathematics

The audit did not use Research Lead tables or digests as premises.  The
following were recomputed from roots as two-subsets of `[5]` with symmetric
difference addition:

1. for every fixed channel, channel degree is `0` or `2`, and the unique
   inactive triangle is `[5]\setminus h`;
2. all six canonical `H_35` active/inactive rows, including exact dart
   reattachments and preservation of a second connector at the inactive
   singleton;
3. all six distinct active/active non-channel rows;
4. all nine active equal-endpoint root branch swaps, with the zero pairing
   separated explicitly;
5. all `84` ordered final-terminal configurations (`168` when target-side
   assignment is also distinguished): every root alternative changes the
   terminal matching;
6. the permanent #78 same-arc Heawood counterexample;
7. the new co-root `6-7` route-changing movie;
8. the complete zero-parent Heawood `H_35` movie and graph-category data.

The independent local-row digest is

`75ed977851a944f2cd80577e629a2f6936da5dfce49ad9d5a9e0e82c8b2494d4`.

The aggregate Heawood/corollary recomputation digest is

`2353b22b111c9dd47319b2c14637c08d93ae2f4eac10605a00f29c5f46842fe8`.

Finite success is used only to check the displayed source movies.  It is not
used as a substitute for a universal proof.

---

## 5. Terminal-consumer check

The frozen proof-development terminal ledger at
`proof-development/affine-cdc-rigour-v1@fee97446...` contains consumers for:

- exact `K_i` / cap-compatible route states;
- separating support components;
- cyclic `2`, `3`, and `4` cuts, each completed on a strictly smaller graph;
- loop, parallel, triangle, theta, direct-matching, and acyclic low-port
  bounded categories;
- single-pop coincidence and separator outcomes with literal exterior darts.

For a four-port cut carrier, a disconnected component has at most two ports.
A one-port cyclic side exposes a bridge; a two-port cyclic side exposes an
exact two-edge cut; an acyclic side is an existing bounded low-port category.
The quantifiers at this graph-theoretic interface match the recorded
consumers.

No consumer applies to the multi-terminal counterexample in Section 3:
all `36` one-NNI outputs remain prime with cyclic connectivity `5`.

---

## 6. Historical antecedent and regression risk

### 6.1 Exact appearance of the new theorem

The file `FIXED_CHANNEL_COMPONENT_CHAIN_ROOT_NNI_THEOREM_V1.md` first appears
in commit

`c106d903dacca72dc7cca03659fb05df7694f04a`
(`AffineCDC RL: prove fixed-channel component-chain escape`),

whose exact parent is

`d7009b74ff5d98a1ac6f68d1ab4b77b6602cfb70`
(the Heawood zero-parent source movie).

The frozen audit source later packages the theorem at
`02b37476198e9eaa2b4cd8d2a2edd76782bdcd49`.

### 6.2 Closest retained or retired antecedents

1. **Two-boundary annulus reduction.**  
   `EQUALITY_LOCK_TWO_BOUNDARY_ANNULUS_REDUCTION_V1.md`
   (`blob 9ef9d87000a4a0f24e908213b27fc9b4758ae93f`) proves a two-boundary
   topological reduction for one equality Tait response.  It is not a
   stable-dart root-NNI quotient-chain theorem and explicitly leaves
   cover-independent inverse transfer open.

2. **Global Pachner potential.**  
   `EQUALITY_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`
   (`blob f65c9bec746982b58dee02d33ba94160afca1cc4`) gives current-flow
   Pachner descent and uses equal-face cancellation.  Its trust boundary
   excludes preservation of the full boundary profile and arbitrary inverse
   transfer.  It is a conceptual surgery antecedent, not the present theorem.

3. **Fixed-channel `Xi` descent.**  
   `DDD_LOCK_H14_SWITCH_INVARIANT_DESCENT_THEOREM_V1.md`
   (`blob e36e603d01770a24a6a8d0df8645663552919e45`) is the closest
   fixed-channel predecessor.  Its arbitrary-equal-face Theorem 5.1 was
   refuted by audit #78 and is permanently withdrawn as a totality theorem.

4. **Quarantined `Omega` orbit transport.**  
   `DDD_LOCK_OMEGA_PLATEAU_ORBIT_TRANSPORT_SCOPE_CORRECTION_V1.md`
   (`blob fc01c8c6b18abc7548651d4b4593c154dd59ad89`) records that an
   exterior component switch cannot be replaced by a two-vertex local energy
   shift.  This was an earlier failure of a local-to-global source inference.

5. **State-walk / seam-run machinery.**  
   The retained state-walk packets track full-state ancestry and prohibit
   erasing attached interface data merely from repeated abstract states.
   They do not contain a component-quotient contraction theorem.

Searches of the frozen source, retained/retired dossiers and accessible commit
history found no earlier theorem under the exact suggested names:

```text
strip contraction
channel quotient
support-chain surgery
state-walk contraction
inactive atom absorption
route-changing connector
marked-weld chain
Pachner component merge
```

`annulus reduction` and the Pachner dossiers above are the nearest conceptual
antecedents; neither supplies the new claimed inference.

### 6.3 Audit history and regression

The new theorem does **not** silently restore the #78 same-arc inference.  It
records physical marked arcs and selects a connector between them; the exact
`6-7` repair works.

It nevertheless repeats the older architectural error in a new form:
application-specific physical data are discarded when the result is promoted
to a universal theorem.  The source now records physical connectors, stable
darts, channel membership and parent fields, but it does not record the
complete set of terminal path components.  The omitted datum permits the
internal terminal-path counterexample in Section 3.

Accordingly:

- the #78 counterexample is properly excluded;
- no known earlier counterexample was falsely declared repaired;
- a **new regression of quantifier scope** is present;
- the proof contains enough physical data for inactive singletons and closed
  cycles, but not enough terminal-component data for its stated generality.

---

## 7. Final assurance boundary

This audit establishes one material obstruction and then stops.

It does **not**:

- restore the false arbitrary-equal-face theorem;
- use `Xi` as a totality provider;
- propose a patched chain theorem;
- mutate Research Lead, Proof Development, main, Curator, Lean, manuscript,
  release, tag, arXiv, DOI or publication surfaces;
- promote a five-support or five-CDC theorem.

Only the three issue-#81 audit reports are added under
`audit/affine-cdc-component-chain-v1/`.
