# The pre-cancellation `C6` movie is not a complete contextual root exit

## Research Lead scope-correction dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `bb3d0bbae387ae2a9f8c1c957ffbe032b52a603e`.

**Affected surfaces:**

- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md` as a possible consumer, not as a false local theorem;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md` as a possible same-order-root-exit consumer, not as a false relative movie theorem;
- `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V3.md`, especially Corollary 6.2 and the reduction of bad sink SCCs to token-only SCCs;
- Repair D in `CANCELLATION_EXIT_REENTRY_WELL_FOUNDEDNESS_GAP_V1.md`.

**Correction:** the coherent canonical-star construction lives on the cells of an annular history diagram. Before cancellation it does not produce a proved single contextual state on the original source topology, nor a state of strictly lower prefix/condensation rank. The root-valued boundary circles of the annulus are already part of the recurrent history picture. Consequently Repair D is not supplied by the existing `C6/C8` dossiers. Moreover, a nonterminal sink SCC may contain both root states and token states; a first-failure edge from a root state can remain inside the same SCC.

**Status:** exact scope correction. The local `(0,2,2)` table, relative root NNI, overlap compatibility, and internal equal-face dipole are retained.

---

## 1. Three levels which must be distinguished

### Local chart

For one pivot-change cell `B_i`, the root cross path and canonical star are two root-valued six-port completions joined by one relative root NNI.

### Annular history movie

For a closed Petersen `C6` track, six such local charts are attached to six cells of a regular annular neighbourhood `N(gamma)` in a Ptolemy history diagram. Adjacent charts share fixed turn corollas and their local movies are compatible after cell subdivision.

### Contextual state

A contextual state is one source graph or multipole, one complete root/token assignment, one active history position, and all cap/route/source incidence data at one vertex of the history graph.

A compatible family of charts over several history cells is not automatically one contextual state.

---

## 2. The canonical section complex is not one cubic time slice

Write the canonical star in Cell `i` as having:

- turn corollas `R_i,R_(i+1)`;
- side corolla `D_i`;
- central vertex `O_i`.

The spoke from `R_i` to the star centre has root label `z_i`.

The adjacent Cell `i-1` also uses the same rooted turn corolla `R_i`, but its spoke of value `z_i` leads to `O_(i-1)`.

If all six canonical charts were interpreted as simultaneous subgraphs of one cubic source graph and the shared `R_i` were identified physically, the unique `z_i` incidence of the cubic corolla `R_i` would have to be incident both with `O_i` and with `O_(i-1)`.

There are only two possibilities:

1. keep both edges, making `R_i` have too many incidences;
2. identify the two `z_i` edges, forcing `O_i=O_(i-1)`.

Applying the second option cyclically identifies all six centres. The resulting vertex would inherit more than three distinct incident branches and is not cubic.

Thus the overlap identity

\[
R_i^{(i-1)}=R_i^{(i)}
\]

is an identity of a rooted history interface, not an instruction to place both star interiors on the same side of that interface in one graph.

### Theorem 2.1

The full six-chart canonical section complex `T_C6^star` is not, merely from the stated overlap theorem, a single cubic contextual state.

---

## 3. Alternating charts do not yet give a complete state theorem

The even charts

\[
S_0^star,S_2^star,S_4^star
\]

use pairwise distinct turn-corolla pairs, and likewise for the odd charts. Hence an alternating simultaneous schedule is not ruled out by the local incidence count.

However the existing dossiers do not prove that either alternating union:

1. covers one complete source graph at a vertex of `N(gamma)`;
2. agrees with every source edge outside the local middle interiors;
3. has the same source topology as one fixed contextual state;
4. carries the correct active history position and cap-terminal obligation;
5. lies outside the recurrent SCC or has lower rank.

Therefore an alternating-three-star time slice remains a possible new construction, not a consequence already available for the proof.

---

## 4. What the relative `C6` theorem actually proves before cancellation

`PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md` proves:

1. each root-valued annular boundary restriction is cross or star;
2. each cross restriction reaches the star by one relative root NNI;
3. adjacent local movies fix their shared rooted turn branch;
4. the six cellwise movies form a coherent relative history movie;
5. each canonical star contains an equal-face dipole.

The annular boundary circles are already in the root-valued part of the lifted history diagram. Their root states need not be original-context terminals: their next attempted inverse move may first-fail into the interior token track.

Before the dipole cancellation, the theorem does not state:

\[
\boxed{
\text{one complete root-valued original-context state with strict progress}.}
\]

The only stated strict exit is the equal-face cancellation itself.

### Corollary 4.1 — Repair D is not currently established

The existing `C6/C8` source packets do not repair cancellation re-entry by producing a proved same-order root terminal before cancellation.

Repair D remains open only in the stronger form requiring a new full contextual time-slice/rank theorem. It is not a completed consequence of coherent canonicalisation.

---

## 5. Mixed root/token SCCs

In confluence v3, a root-valued state at positive prefix level has a next inverse move. If the move succeeds, prefix decreases. If it first fails, the state has an edge to a normalized token state at the same declared prefix level.

The file concludes that a nonterminal sink SCC must therefore consist entirely of token states. This does not follow: the first-failure edge may enter a token state in the **same SCC**, and token/root alternative moves may return to a root state.

### Theorem 5.1 — corrected SCC alternative

Without an additional rank or a convention which strictly lowers prefix on every first-failure restoration, a nonterminal sink SCC may be mixed:

\[
\boxed{
\text{root states}
+
\text{token states}.}
\]

What can be concluded is only that every nonterminal sink SCC contains at least one persistent singular state after deterministic root-prefix successes are contracted.

The no-sink proof must either:

1. normalize mixed SCCs to a token transition system by a proved quotient preserving exits; or
2. analyze recurrent paths allowing root and token states together.

Corollary 6.2 of confluence v3 is therefore overstated as written.

---

## 6. Relation to prefix semantics

A first failed inverse move restores the old source topology with one non-root central edge. Topologically the history move has been crossed, even though root transfer failed.

One possible repair is to redefine prefix level so that both successful and failed inverse restorations lower the consumed-history index. The remaining discrepancy must then be recorded separately as an alternative-surgery/token word.

This can remove root/token mixing at one prefix level, but it does not by itself solve the discrepancy word or cancellation re-entry. A complete corrected state definition would require:

- consumed original-history prefix;
- outstanding alternative-surgery discrepancy;
- token state and position;
- all full source/cap data.

No such corrected finite-condensation theorem is presently written.

---

## 7. Consequence for the current repair queue

### Repair D

Not available from the existing C6/C8 packets.

### Remaining live repairs

1. history-coherent terminal selection;
2. cancellation macro-return with a strict secondary rank;
3. inverse-weld flow selection;
4. a new alternating-star/full-time-slice theorem with an explicit contextual rank, if one can be constructed.

The first three remain the primary exact frontier.

---

## 8. Retained trust boundary

### Retained exact local results

- canonical star labels;
- uniqueness of the fixed-triangle local section;
- shared turn-corolla compatibility as history-interface data;
- relative `(0,2,2)` root NNI;
- coherent annular cellwise movie;
- internal equal-face dipole and boundary preservation.

### Corrected global use

- the canonical section complex is not one contextual state merely by gluing labels;
- no same-order root terminal/rank is obtained before cancellation by the stated theorem;
- mixed root/token SCCs are not excluded by confluence v3;
- cancellation remains the only claimed strict exit and is subject to the re-entry gap.

### Not claimed

- impossibility of an alternating-star time-slice construction;
- falsity of the local `C6/C8` source movies;
- impossibility of repairing contextual transfer;
- existence of a five-CDC counterexample;
- independent audit, Lean verification, manuscript integration, release, arXiv, DOI, peer review or publication.