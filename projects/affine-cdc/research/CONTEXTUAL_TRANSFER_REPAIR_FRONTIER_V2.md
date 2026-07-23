# Contextual-transfer repair frontier after local cancellation normalisation

## Research Lead controlling frontier v2

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Supersedes as frontier description:**

- the broad repair queue in `CANCELLATION_EXIT_REENTRY_WELL_FOUNDEDNESS_GAP_V1.md`;
- `MARKED_WELD_RELATIVE_CONTEXTUAL_RETURN_TARGET_V1.md` as the preferred repair route;
- the completion reading of `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V4.md`.

**Status:** the cancellation re-entry gap has been reduced to one precise unbounded endpoint state. All zero-valued inverse failures now have direct root-valued alternative source insertions. The doubled-disjoint row either has the same root-valued alternative insertion or enters one standard missing-index co-root transport state. Internal closed co-root tracks erase by root annuli, and open tracks whose endpoint sides are already root-normalized erase by root strips. The only unresolved interface is a missing-index co-root track which reaches the original unresolved oriented full-channel boundary and may continue through another forward episode.

R2.7 remains `BLOCKED-FRONTIER`; no global closure is restored by this file.

---

## 1. Complete local inverse table

For one inverse `2--2` flip:

\[
\begin{array}{c|c}
\text{forced old diagonal}&\text{disposition}\\
\hline
\text{root}&\text{direct inverse flip}\\
0&\text{the other crossed root NNI}\\
\text{co-root}&\text{one oriented root alternative / co-root discrepancy cell}.
\end{array}
\]

For one inverse equal-face cancellation with returned reconnecting roots `a,b`:

\[
\begin{array}{c|c}
\text{relation of }a,b&\text{disposition}\\
\hline
\text{distinct intersecting}&\text{original root insertion}\\
a=b&\text{root-valued alternative insertion after one adjacent borrow}\\
a\perp b,\ \text{good borrow}&\text{root-valued alternative insertion}\\
a\perp b,\ \text{missing-index borrow}&\text{one }(Q_i,Q_j,ij)\text{ transport state}.
\end{array}
\]

Thus no inverse cancellation requires a recursive equality call or an automatic lower-order exit.

---

## 2. Direct source theorems now available

### Quadruple equality

`QUADRUPLE_EQUALITY_THREE_VERTEX_BORROWING_ROOTIFICATION_V1.md` gives the two-NNI five-leaf table.

`ROOT_VALUED_ALTERNATIVE_INVERSE_CANCELLATION_INSERTION_V1.md` strengthens it: the final root topology contains an equal-face pair whose cancellation is exactly the current smaller source graph. Hence the repair is one direct root-valued alternative inverse insertion.

### Good doubled-disjoint

`DOUBLED_DISJOINT_THREE_VERTEX_BORROWING_DICHOTOMY_V1.md` gives the `120/60` support dichotomy.

In the `120` good cases, `ROOT_VALUED_ALTERNATIVE_INVERSE_CANCELLATION_INSERTION_V1.md` again identifies one direct root-valued alternative insertion.

### Missing-index doubled-disjoint

The remaining `60` cases produce exactly

\[
(Q_i,Q_j,ij),
\]

one degree-two co-root transport state. After full-defect-tree normalization there is at most one co-root token and no new alphabet.

---

## 3. Global co-root track results

### Constant-pivot runs

Every maximal constant-pivot run has its unique side-preserving nonpivot root section.

### Backtracks

Every immediate pivot backtrack is the Type-T word `abba` and deletes formally/source-faithfully after normalization.

### Closed tracks

`PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md` reduces every internal closed component to:

- no pivot change: root section;
- odd `C5/C9`: orientation contradiction;
- even `C6/C8`: root-annulus replacement.

Therefore an interior closed singular component is impossible in a minimal lifted comparison.

### Open tracks with normalized endpoints

`PETERSEN_OPEN_TRACK_ROOT_STRIP_REPLACEMENT_V1.md` proves the local/open-chain theorem:

- consecutive side roots on every nonbacktracking four-pivot path are distinct intersecting (`120/120` finite certificate);
- every cell has the relative `(z,z,w,w)` canonical star;
- canonical cells glue linearly;
- if both short endpoint sides are root-normalized or accepted exits, the complete open track has a root strip replacement.

Read it through `OPEN_TRACK_ROOT_STRIP_ENDPOINT_SCOPE_CORRECTION_V1.md`.

---

## 4. The sole unresolved endpoint

Let a missing-index co-root track reach the original target context `C_0` while the original cap remains blocked and the physical route remains the fixed route.

At that endpoint:

- horizontal rescue may still give immediate cap lift;
- route change gives profile escape;
- bounded or separator structure gives an accepted exit;
- otherwise the endpoint is again one oriented full-channel lock and launches another finite equality/DDD forward descent.

If repeated continuation returns to the same complete outer endpoint state, the trajectory forms a periodic full-state track on a history cylinder. The existing closed-track root annulus removes its internal monodromy, but no strict macro rank or cap-profile consequence has yet been proved from that removal.

### Target 4.1 — periodic outer-endpoint discharge

Prove that a periodic outer-endpoint episode gives one of:

1. a cap-compatible root state on the original context;
2. a route/profile change;
3. a bounded/separator exit;
4. a strictly smaller source/context measure which does not rely on arbitrary-flow inverse weld;
5. a source replacement which prevents return to the same complete endpoint state.

This is the only remaining unbounded R2.7 theorem.

---

## 5. Quarantined shortcuts

The following must not be used:

- cancellation automatically gives a completed order-`N-2` contextual exit;
- every non-two-cut marked pair admits a `B`-flow;
- arbitrary terminal and inherited root flows are always Kempe equivalent;
- the six canonical `C6` charts form one simultaneous source graph;
- every open co-root track has root-valued short endpoint sides;
- closed-track erasure by itself supplies strict progress at an unresolved outer endpoint.

---

## 6. Status of master v4

`ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V4.md` contains valuable architecture but is not controlling.

It must be revised because:

1. the inverse-cancellation disjoint row has the good/missing-index dichotomy;
2. zero repairs are direct alternative root-valued insertions;
3. open strips require normalized endpoint sides;
4. the periodic outer endpoint remains unconsumed.

No v5 completion theorem should be issued until Target 4.1 is closed.

---

## 7. PDL interface

PDL should retain and reconstruct independently:

1. R1 and R2.1--R2.6 already under reconstruction;
2. quadruple-equality alternative insertion;
3. doubled-disjoint `120/60` dichotomy;
4. missing-index transport identification;
5. closed-track root-annulus erasure;
6. normalized-endpoint open-strip theorem.

PDL must stop R2.7 at Target 4.1 and must not certify contextual transfer, cap restoration, or global closure before this endpoint is resolved.

---

## 8. Assurance boundary

### Closed at authorial level

- all local inverse coefficient rows;
- zero-row direct root-valued source replacements;
- isolation of one missing-index co-root token;
- constant-pivot/backtrack normalization;
- internal closed-track erasure;
- normalized-endpoint open-track erasure.

### Still open

- periodic outer-endpoint discharge;
- complete contextual inverse transfer;
- one-cross cap restoration;
- simple-edge extension and global five-support closure;
- PDL completion, independent audit, Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.
