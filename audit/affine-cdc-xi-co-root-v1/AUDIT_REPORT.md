# AC-AUDIT-XI-01 — focused independent audit report

**Classification:** `BLOCKED — MATERIAL GAP OR FALSE SCOPE`  
**Reason for classification:** material gap in the equal-neighbour source theorem; the stated co-root scope itself is correctly limited  
**Frozen PDL candidate:** `fee97446ee8b99f07740f394e99ef4a2ecc3e40e`  
**Frozen RL checkpoint:** `212d789a5967813e7277fb3e269060926c99cb0e`  
**Audit branch:** `audit/affine-cdc-xi-co-root-v1`

---

## 1. Audit boundary

This audit covers only the fixed-channel `Xi` repair for the co-root/DDD
prescribed-parent `(4,2,2)` sector.

The zero-parent `(0,2,2)` row is explicitly excluded.  No zero-parent theorem,
new scheduler, lower-order selection principle, or modification of the PDL/RL
candidate was attempted.

The quarantined `Omega` orbit-minimum proof was not used.

---

## 2. Independently verified portions

### 2.1 Canonical frame

Verified:

- uniqueness of the support bijection from `(p,q,m,h_*)` to `(12,34,5,14)`;
- distinction between the literal physical support pair `h_*` and its current
  canonical label;
- common-marked transport `eta'=tau_14 o eta`;
- correct treatment of components containing neither, both, or exactly one
  marked occurrence.

### 2.2 Whole-component invariant

Verified:

- all ten `tau_14` images;
- all ten identities `xi(tau_14(T))=xi(T)`;
- vertex-by-vertex invariance of the complete closed-graph sum, including cap
  and exterior vertices, in both unmarked and common-marked switch cases;
- prior consumption of a separating one-marked component.

This is a genuine repair of the old exterior-energy defect.

### 2.3 Strict distinct-neighbour rows

Verified independently and exhaustively:

- exactly three distinct pairs sharing `23`;
- exactly three distinct pairs sharing `25`;
- one unique root-valued opposite pairing in each row;
- root-valued target triangles in every row;
- `Delta Xi=-2` in all six rows.

### 2.4 Bad-free route contradiction

Verified:

- in the absence of `123,234,125,245`, an `H_14` path starting at boundary root
  `12` is forced through type `124` and roots `12,24` only;
- it cannot reach a boundary `34` occurrence;
- this contradicts the selected oriented full-channel `12`-to-`34` route.

The proof therefore finds a bad vertex on the marked `H_14` component.

### 2.5 Literal source interfaces and scope

Verified at the move-contract level:

- ordinary root NNIs retain labelled exterior darts, cap identity, live parent
  and stored-prefix ancestry, subject to exact category testing;
- closed support-component switches preserve topology/darts and update complete
  support/route fields source-faithfully;
- nonlocked co-root states remain covered by the prior separating-channel and
  exact terminal object;
- the candidate correctly excludes the zero-parent row from the claimed
  conclusion.

---

## 3. Load-bearing defect

The universal equal-neighbour route-or-split theorem is false as stated.

The proof reduces the outside `H_14` geometry to one perfect matching on four
local ports and claims:

> if the outside matching is the third matching, the root branch-swap changes
> the oriented marked route.

This forgets where the two marked edges lie on the two outside paths.  When
both marked edges lie on the same outside path, the two root placements can
both remain one component and induce the same marked route.

### Exact source witness

In the frozen Heawood root flow:

- marked edges: `1-6:12` and `2-3:34`;
- fixed channel: `H_14`;
- equal bad face: `9-14:23`;
- both endpoints have type `123`;
- the `H_14` component is Hamiltonian.

The root branch-swap reattaches

```text
9-10 -> 14-10,
1-14 -> 1-9.
```

Independent checks show:

1. before and after the swap, `H_14` is one component;
2. cutting the marked edges gives the same route `(1,2)|(3,6)` before and after;
3. the cyclic marked-endpoint order is unchanged;
4. all four rescue systems `H_13,H_14,H_23,H_24` remain common-component locks
   with the same marked route;
5. the new graph is connected, simple, cubic, bridgeless, girth five, and has no
   cyclic cut of size at most four;
6. the cell is disjoint from the active parent cell and retained cap vertices.

Thus neither root placement supplies a one-passage component, no route/category
consumer fires, and the prescribed equal-neighbour macro cannot reach its
one-sided switch or strict final NNI.

Full details and a reproducibility digest are in
`SOURCE_MOVIE_AND_SCOPE_LEDGER.md`.

---

## 4. Effect of the defect

The defect directly refutes:

- RL `DDD_LOCK_H14_SWITCH_INVARIANT_DESCENT_THEOREM_V1.md`, Theorem 5.1 in its
  universal “from one equal bad face” form;
- PDL `AC_PD_5CDC_V7_3_FIXED_CHANNEL_XI_RECONSTRUCTION.md`, Section 5.1's
  matching-only route-or-split justification.

It consequently blocks:

- totality of the deterministic fixed-channel descent;
- the conclusion that every nonabsorbing iteration lowers `Xi` by two;
- the claimed finite escape from every locked co-root state;
- the co-root all-index closed-SCC exclusion;
- literal co-root prescribed-parent reinsertion as a completed theorem.

The defect does **not** refute:

- frame uniqueness;
- `tau_14`/`xi` invariance;
- complete-component switch invariance;
- the six strict distinct-neighbour rows;
- the bad-free trapping contradiction;
- the possibility of a repaired co-root theorem using an additional global
  selection lemma or a new same-arc equal-face macro.

The bound of at most `N` strict macros is correct only conditionally on a proof
that a strict macro exists at every nonabsorbed lock state.

---

## 5. Smallest repair surface

The missing state datum is the distribution of the two marked edges over the
two outside arcs of an equal face.

A repaired co-root theorem must prove one of:

1. existence of a distinct bad incidence;
2. existence of an equal bad face with marked edges on different outside arcs;
3. a root-only escape for the same-arc equal-face configuration;
4. an exact route/cut/bounded terminal forced by that configuration.

The current three-perfect-matching argument does not establish any of these.
Choosing the whole common marked component, repeating the root branch-swap, or
appealing to finiteness does not decrease `Xi` in the explicit witness.

This is a co-root research/proof-development repair.  It is logically separate
from the open zero-parent frontier.

---

## 6. Final audit disposition

The fixed-channel arithmetic and switch invariant are sound, but the module is
not independently verified as an escape theorem because one of its two
load-bearing local alternatives is false.

Final classification:

`BLOCKED — MATERIAL GAP OR FALSE SCOPE`

More precisely:

- **material gap:** yes, in the equal-neighbour source movie;
- **false co-root/zero scope:** no; the candidate correctly excludes zero parent;
- **candidate mutation:** none;
- **research/proof-development/corpus mutation:** none;
- **main/Curator/Lean/manuscript/release/tag/DOI/publication mutation:** none.

The audit branch contains exactly the three reports required by issue #78.
