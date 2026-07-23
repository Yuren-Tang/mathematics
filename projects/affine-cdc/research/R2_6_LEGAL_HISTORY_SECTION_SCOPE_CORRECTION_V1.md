# Scope correction: local `C6` star movies do not yet supply a legal global root history section

## Research Lead reverse-audit correction v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Audited surfaces:**

- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `PETERSEN_EVEN_TRACK_ROOT_ANNULUS_REPLACEMENT_V1.md`;
- `PETERSEN_OPEN_TRACK_ROOT_STRIP_REPLACEMENT_V1.md`;
- `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md`;
- `PERIODIC_OUTER_ENDPOINT_ROOT_SEAM_DISCHARGE_V1.md`;
- `R2_6_EVEN_TRACK_SOURCE_REPLACEMENT_PDL_HANDOFF_V1.md`;
- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V6.md` and v6.1 addendum;
- `RESOLVED_CALL_MACRO_ATTRACTOR_RANK_V1.md`.

**Historical corrections retained:**

- `PTOLEMY_ROOT_TUBE_HISTORY_LIFT_SCOPE_CORRECTION_V1.md`;
- `PRE_CANCELLATION_C6_MOVIE_AND_MIXED_SCC_SCOPE_CORRECTION_V1.md`;
- PDL `AC_PD_5CDC_R2_5A_PRE_CANCELLATION_SCOPE_CORRECTION.md`.

**Classification:**

\[
\boxed{
\text{R2.6 LEGAL-HISTORY REALISATION OPEN}
/
\text{R2.7 CONDITIONAL ON R2.6}
/
\text{NO ESTABLISHED FIVE-CDC PROOF}.}
\]

The local root calculations are exact. What is not yet proved is the existence of a complete root-valued history complex whose vertices are full cubic source states and whose edges are legal source moves. Equality of the rooted turn corollas on neighbouring local charts does not by itself provide the required complete shared history states. In particular, all six canonical stars cannot be placed simultaneously in one cubic source graph. The later root-annulus theorem names a common canonical section complex but does not explicitly construct its complete source-state vertices and legal longitudinal history edges in a way that resolves this obstruction.

Until a legal alternating/asynchronous section or a complete finite lifted-annulus certificate is supplied, closed even-track erasure, the global open strip, periodic endpoint discharge, the resolved-call no-SCC theorem and contextual transfer remain conditional at this interface.

---

## 1. Exact local mathematics retained

For one identity-hexagon pivot cell with fixed turn corollas, the unresolved four-branch word is

\[
(z,z,w,w)
\]

with `z,w` distinct intersecting roots.

The three relative topologies are exactly:

1. one equality/zero path;
2. one root cross path;
3. one root canonical star.

The two root topologies are joined by one unique root-preserving relative NNI fixing:

- both turn corollas;
- all six ordered boundary incidences;
- every exterior source edge and root label.

The canonical star contains one equal-face dipole.

For a simple Petersen `C6`, the side word is one repeated root triangle and neighbouring canonical charts induce the same labelled turn corolla. The `C8=C6 triangle C6` side-root and seam formulas are also exact.

These results are retained unconditionally.

---

## 2. The complete-state obstruction

Write the canonical star in Cell `i` with turn corollas

\[
R_i,\ R_{i+1}
\]

and centre `O_i`. The unique outgoing spoke of `R_i` leads to `O_i`.

The adjacent Cell `i-1` uses the same rooted corolla `R_i`, but its canonical spoke leads to `O_{i-1}`.

If both charts are interpreted as subgraphs of one simultaneous source state, the same cubic incidence at `R_i` must lead to two different centres. Keeping both violates cubic degree; identifying them cyclically forces excessive degree at a common centre.

Therefore

\[
\boxed{
\{S_0^\star,\ldots,S_5^\star\}
\text{ with static overlap labels}
\not\Rightarrow
\text{one cubic source state}.}
\]

This was already correctly isolated by the earlier pre-cancellation and PDL scope corrections.

---

## 3. Why the later gluing sentence is insufficient

`PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md` proves that each local NNI treats the shared turn corolla as a fixed rooted exterior branch. It then states that adjacent movies may be glued after cell subdivision and scheduled sequentially.

For a global history lift, one must additionally exhibit at every shared history vertex:

- one complete cubic source topology;
- one root label on every source edge;
- literal equality of the complete endpoint state produced from both incident cells;
- one legal history edge to the next complete state.

Fixing the common corolla does not determine the two local interiors on its opposite history sides, and static compatibility does not provide a complete source state containing the required intermediate data.

The dossiers do not list the complete intermediate states or a legal longitudinal sequence separating neighbouring star interiors in history time.

Thus the implication

\[
\text{cellwise relative NNIs with fixed corollas}
\Longrightarrow
\text{global root history section}
\]

remains an additional theorem.

---

## 4. Consequence for the root annulus

`PETERSEN_EVEN_TRACK_ROOT_ANNULUS_REPLACEMENT_V1.md` proposes

\[
\partial_-N(\gamma)
\rightsquigarrow
\mathcal T_{C_6}^\star
\leftsquigarrow
\partial_+N(\gamma).
\]

This is valid only if `T_C6^star` is a genuine root-valued history cycle:

- every vertex a complete source state;
- every edge a legal root NNI/identity move;
- every cyclic seam source-faithful.

The static section complex of local charts does not establish these properties. The middle product cylinder cannot be formed merely from local chart incidence compatibility.

### Correction 4.1

The `C6` root-annulus replacement is conditional on a legal-history-section realisation theorem.

The `C8` annulus is likewise conditional, because its two-`C6` seam construction consumes the missing `C6` history cylinder.

---

## 5. Consequence for open and periodic tracks

A linear chain avoids cyclic holonomy but still requires complete shared source states at adjacent cells. The existing open-strip theorem proves the local four-pivot intersection table and relative cell movies, but its global linear gluing is conditional on a legal root history strip construction.

The switch--pop collar short-side theorem remains exact; it supplies a valid endpoint once the interior strip exists.

The periodic root crosscut theorem is also exact **conditional on** a genuine connected root history cylinder. It cannot manufacture the missing cylinder.

Thus:

- local open-cell theorem: retained;
- root-normalized endpoint model: retained;
- global open strip: conditional;
- periodic crosscut in an existing root cylinder: retained conditionally;
- periodic endpoint discharge: conditional on the missing cylinder/strip realisation.

---

## 6. Consequence for resolved-call recursion

The resolved-call no-SCC proof excludes a nonterminal parent cycle by compressing child calls and then invoking an exhaustive fixed-order disposition:

1. pure root arborescence;
2. closed-track erasure;
3. open-strip erasure;
4. periodic endpoint discharge;
5. accepted exits.

Items 2--4 consume the missing R2.6 legal-history theorem. A local equal-face cancellation available in one canonical cell does not by itself replace them: the completed lower-order call may return to the same parent SCC, and the resolved-call rank is defined only after nonexit SCCs have been excluded.

Therefore the rank `d_N` and the v6/v6.1 contextual-transfer theorem are conditional on R2.6.

No circular appeal to `d_N` may be used to prove the missing R2.6 section.

---

## 7. Exact live repair targets

Any one of the following would repair the interface.

### Target A — explicit alternating/asynchronous history section

Construct a finite sequence of complete root-valued source states around the `C6` annulus such that:

- each local restriction is cross or canonical star;
- neighbouring star interiors are separated in history time;
- every transition is a legal root NNI/identity move;
- all exterior/cap/route data are fixed;
- the sequence closes.

An alternating three-cell schedule is a candidate, not an established theorem.

### Target B — complete lifted-annulus certificate

Enumerate the finite full-labelled lifted `C6` annuli modulo support and dihedral symmetry. For every admissible annulus, exhibit a root-valued replacement and verify every source vertex, source edge, history move and boundary map.

The certificate must include the map to complete source states, not only local six-port root tables.

### Target C — different strict fixed-order recurrence measure

Prove that the local star/cancellation macro, together with its resolved child return, strictly lowers a parent fixed-order recurrence complexity. This must be independent of the unresolved attractor rank and must survive cancellation re-entry.

---

## 8. Current proof-DAG correction

### Retained complete drafts / exact inputs

- R1 structural reduction;
- R2.1 boundary-route certificate;
- R2.2 current-flow termination;
- R2.3 first failure and local overlap grammar;
- R2.4 full-state forced backbone;
- R2.5 odd `C5/C9` exclusion;
- witnessed child-history, genealogy and innermost-call interfaces;
- local `C6/C8` coefficient and six-port tables;
- downstream terminal and outer-shell consumers.

### Open frontier

\[
\boxed{
\text{R2.6 legal root history section / strip / annulus}.}
\]

### Conditional downstream

- R2.7 global contextual return;
- one-cross cap restoration;
- simple-edge reducibility;
- cubic five-support theorem;
- general finite bridgeless five-CDC outer shell.

---

## 9. Assurance boundary

### Exact here

- localisation of the remaining authorial gap;
- preservation of all local root tables;
- proof that static six-star compatibility is not a simultaneous source state;
- identification of the missing complete-history data;
- dependency impact on annulus, strip, periodic, resolved-call and global theorems;
- three precise repair routes.

### Not claimed

- nonexistence of a legal asynchronous filling;
- falsity of R2.7 or five-CDC;
- a graph counterexample;
- PDL completion or independent audit;
- Lean, manuscript, curation, release or publication status.
