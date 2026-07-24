# AC-5CDC-AUDIT-RETURN-01 — complete-state seam/interface ledger

**Candidate:** `proof-development/affine-cdc-rigour-v1@1f57422e0e415d8902d56eb294183815c0a0b640`  
**Frozen source inspected:** `research/affine-cdc-five-cdc-v1@71a10f9ba86c1d2b8b7885e78fa9baa303c77818`  
**Audit guide:** `2679f098e6c596083d671a67d2630d5c58c6280f`, used only as an attack list.

This ledger distinguishes coefficient compatibility, ordinary source topology,
ordered-dart identity, and contextual decorations.  Equality in the first column
never substitutes for the later columns.

## G. R2.6 cellwise track erasure

| Interface | Independent reconstruction | Result |
|---|---|---|
| Ordered four-pivot census | Enumerating `x-s-t-y` in `KG(5,2)` with `x != t`, `s != y` gives `10*3*2*2=120` cases.  The audit script verifies all 120. | `PASS` |
| Human normal form | Put `s=12`, `t=34`.  Then `x in {35,45}`, `y in {15,25}`.  Consequently `z=x+t` is the complementary member of `{35,45}`, and `w=s+y` is the complementary member of `{15,25}`.  Hence `z,w` are distinct roots meeting exactly in support `5`. | `PASS` |
| Middle coefficient word | Once the two turn corollas are fixed, the four middle branches are two occurrences of the left side root and two of the right side root: `(z,z,w,w)`. | `PASS`, conditional only on the stated full-state pivot-cell incidence model |
| Three pairings | Equal-label pairing has central value `0`; both crossed pairings have central value `u=z+w`, a root. | `PASS` |
| Relative root NNI | The two crossed pairings are the two binary four-port trees differing only in their internal pairing.  One relative NNI connects them while fixing the four ordered exterior darts. | `PASS` |
| Consecutive change cells | Duplicating a complete root state by an identity interval is a cellular subdivision, not a new mathematical source state.  Opposite-side collars then have disjoint interiors. | `PASS` |
| Constant-pivot endpoint section | At a transition `{s,x}->{s,y}` with side root `z=x+y`, the compatibility equation selects `(x,y)` and excludes `(s,s)`.  Thus a run with pivot `s` selects its nonpivot sheet.  At a change state `{s,t}`, the left run selects `t` and the right run selects `s`, exactly the two seam sides. | `PASS` |
| Closed run with no pivot change | The selected nonpivot sheet is periodic when the complete initial and terminal state is literally the same.  Nontrivial support transport is retained as rooted path data rather than set to identity. | `PASS` |
| Open track and unresolved-endpoint scope | Root-normalized and switch--pop short sides satisfy the open-strip hypothesis.  With one unresolved outer side, the final incident component is correctly left unresolved. | `PASS` |
| Periodic cylinder | After literal endpoint identification, closed-track erasure yields a connected root-valued cylinder.  A connected finite CW cylinder has connected `1`-skeleton because each `2`-cell attaches to one connected component of the existing `1`-skeleton.  A shortest graph path between boundary vertex sets is a proper embedded crosscut; cutting it gives a rectangle. | `PASS` |
| Passive exterior data | Source slots, exterior roots, side outputs, support transport, cap block and route are fixed by a relative four-port NNI and by the endpoint-relative run sections. | `PASS` |
| Active/suspended central mark | `AC_PD_5CDC_R2_6_CELLWISE_TRACK_ERASURE.md`, Theorem 4.1, says every mark is unchanged because all listed data lie on the fixed boundary.  A surviving ancestor mark may instead occupy the active central atom/diagonal.  It is not a boundary dart and must be transported to the new diagonal by the active-NNI lineage map. | `REPAIR REQUIRED (G-MARK-1)` |

### G-MARK-1 — exact repair

Replace the blanket sentence “all listed data live on the fixed boundary” by a
marked case split:

1. passive boundary marks are fixed pointwise;
2. a mark on the active central dart pair is transported bijectively to the new
   central dart pair by the labelled active-diagonal NNI lineage;
3. the marked endpoint produced on each seam side is proved literally equal to
   the marked endpoint expected by the adjacent nonpivot run section.

The local lineage machinery already reconstructed in
`AC_PD_5CDC_R2_7_FULL_LABELLED_GENEALOGY_GLUING.md` supplies the intended map,
but R2.6 must invoke it explicitly.  This is a local source-fidelity repair; it
does not alter the unmarked seam theorem.

## H. Witnessed recursion and child fidelity

| Interface | Independent reconstruction | Result |
|---|---|---|
| `Q_N` before `P_N` | `Q_N` uses only lower `Q_n` and fixed-order theorems; `P_N` uses lower `P_n` and same-level completed `Q_N`.  The phase order `(N,Q)<(N,P)` is noncircular. | `PASS` |
| Inherited child flow | Equal-face cancellation reconnects equal-root incidences and therefore supplies a specified child root flow.  No recolouring is needed at launch. | `PASS` |
| Looplessness | A reconnection loop would require two equal-root incidences at one cubic root vertex; then its third incident value would be zero.  Hence the root-valued child has no such loop. | `PASS` |
| Bridgelessness | A bridge in an abelian-group flow has value zero by the shore cut-sum.  Every child edge is root-valued and nonzero. | `PASS` |
| Disconnected output | Deleting the equal-face dipole leaves either one component or two components with two terminals each.  If both reconnection edges stay within shores, the original incidences form a cyclic two-edge cut. | `PASS` |
| Literal lower `Q` instance | The dossier retains the ordered outer cap shore and restricted route/support data, but it does not explicitly name the smaller target cap closure and the smaller selected cross closure as a pair. | `LOCAL REPAIR REQUIRED (H-CROSS-1)` |
| Child route/profile exit | It concerns the unchanged ordered outer shore. | `PASS` |
| Child bounded exit | Restoring one stored two-vertex dipole changes a fixed finite bound by a fixed constant. | `PASS`, provided the downstream bounded threshold is stated monotonically |
| Child separator/category exit | Section 4.6 asserts, without a four-terminal partition proof, that every child cut restores to the same cut order or an already accepted low-port configuration.  A child separator may use one or both new reconnection edges, and restoring the dipole can change the cut. | `BLOCKED (H-SEP-1)` |

### H-CROSS-1 — exact local repair

For every connected cancellation child define explicitly

- `P'` as the cancelled ordered four-pole;
- `G'_i=P' union cap_i` as the target child;
- `G'_j=P' union E_j` as its inherited selected cross closure.

State that the cancellation support is disjoint from the fixed outer closure
collar and prove `G'_j` has order two less and carries the inherited flow.  This
makes the invocation of `Q_{N-2}` literal rather than schematic.

### H-SEP-1 — missing source lemma

A complete proof needs a census of the position of a child separator relative to
the two new reconnection edges.  For each terminal partition it must exhibit the
parent separator or cite an already proved bounded/category theorem with the
exact resulting port and size bound.  The present sentence in Section 4.6 is not
such a census.  Until supplied, a child branch may terminate without a proved
parent exit.

## I. Genealogy and consumer alphabet

| Interface | Independent reconstruction | Result |
|---|---|---|
| Primitive identity | Ordered endpoint darts, not abstract edge names, are the correct primitive labels. | `PASS` |
| Passive NNI lineage | Exterior darts and nonactive marked edges are fixed pointwise. | `PASS` |
| Active-diagonal lineage | The frozen six-leaf source movie gives a one-to-one mobile-envelope transport; no mark duplication is required. | `PASS` |
| External cancellation | External darts reconnect canonically and inverse insertion restores the ordered pairs. | `PASS` |
| Raw central cancellation | The central darts are genuinely deleted and have no lower-graph descendant. | `PASS` |
| Suspended ancestor mark | In a successful paired bubble, predecessor-order raw insertion supplies a central dart pair on which a still-live ancestor obligation can be carried.  This is boundary-relative data, not false child genealogy. | `PASS` |
| Call-local marks | They disappear with the eliminated child frame; the endpoint tuple determines surviving marks. | `PASS` |
| Literal concatenation | Generator lifts have the exact raw-insertion endpoint states, and the labelled six-/five-leaf paths preserve the ordered exterior tuple. | `PASS` |
| Support-switch alphabet | Locked Morse descent itself uses only root NNIs and equal-face cancellations.  Support switches can therefore be confined to initial rescue, route/bounded terminal histories, endpoint rootification, or switch--pop collars. | `PASS` |
| Closed Ptolemy core | After immediate `A/C` normalization and switch--pop pairing, no raw singular support-switch correction remains in a closed component. | `PASS` |

The only cross-reference repair required by I is that R2.6 must actually use the
active-diagonal mark transport when a seam changes a marked central diagonal.
