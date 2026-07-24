# Controlling R2.6 addendum to contextual-transfer master v6/v6.1

## Research Lead v6.2 — cellwise seams, identity strips, and periodic crosscuts

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Controls together with:**

- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V6.md`;
- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V6_1_ADDENDUM.md`;
- `CELLWISE_ROOT_SEAM_AND_CONSTANT_RUN_TRACK_ERASURE_V1.md`;
- `R2_6_CELLWISE_SEAM_RUN_INTERFACE_AUDIT_AND_PDL_HANDOFF_V2.md`.

**Exact parent head:** `470d3cb369b9d46ea854c0cd2fa8ce85399040c9`.

**Supersedes exactly:**

- v6 Section 7 insofar as it consumed a global `C6/C8` root annulus or the old global open-star strip;
- v6.1 Section 4 insofar as `closed components use the root-annulus theorem` meant the old canonical-star annulus route;
- v6.1 Section 6 item 1, which delegated reconstruction of the old source-level `C6/C8` annulus/open-strip package;
- the first PDL handoff `R2_6_EVEN_TRACK_SOURCE_REPLACEMENT_PDL_HANDOFF_V1.md`.

**Status:**

`R2.6 CLOSED AT RL AUTHORIAL LEVEL / R2.7 COMPLETE AUTHORIAL CANDIDATE (v6+v6.1+v6.2) / PDL RECONSTRUCTION AND INDEPENDENT ASSURANCE REQUIRED`.

No global five-support theorem is declared.

---

## 1. Correct fixed-order singular-track consumer

After witnessed innermost-call elimination and normalized switch--pop treatment, every persistent singular component has the accepted fixed-order alphabet:

- root-NNI/Ptolemy interior cells;
- at most one nonbranching full-state co-root track;
- no raw support-switch interior cell;
- complete cap, route, support, side-output, crossed-resolution, and mark data.

Consume such a track as follows.

1. Put one explicit local root seam in every genuine pivot-change source cell.
2. Separate adjacent seam collars by source-neutral identity subdivision.
3. The remaining pieces are constant-pivot intervals.
4. On each such interval, root admissibility uniquely forces the nonpivot full-state history on both long sides.
5. Replace the interval by the identity product of that common root history.
6. Glue seam collars and identity strips on literal complete endpoint states.
7. Treat switch--pop births/deaths as separate root-short-side endpoint collars.
8. Leave one unresolved original outer endpoint untouched unless it is discharged locally or repeats.

This yields root cylinders for closed tracks and root rectangles for normalized/accepted open tracks.

The construction does not use:

- a simultaneous six-star state;
- a global canonical `C6` history section;
- `C8=C6 triangle C6` annulus gluing;
- equal-face cancellation or target-order descent inside R2.6;
- an anchored-tree theorem applied to a history track.

---

## 2. Why the constant-run replacement is genuinely two-dimensional

The phrase `canonical root section` alone is insufficient. The exact relative-strip argument is:

- the root-triangle equation makes the nonpivot choice unique at every constant-pivot transition;
- therefore each root-valued long-side restriction equals the same nonpivot complete history;
- all other boundary data are already fixed by the regular neighbourhood;
- hence the two long sides are literally equal as full-state histories;
- their product with an interval is the required root-valued identity strip.

At a pivot change `x -> s -> t -> y`, the seam fixes turn corollas

`L=(x,t,z)` and `R=(s,y,w)`.

Thus it exposes root `t` to the left pivot-`s` run and root `s` to the right pivot-`t` run, exactly matching their unique nonpivot endpoint choices.

---

## 3. Periodic unresolved endpoint

After variable-order compression, suppose the same complete unresolved endpoint state repeats at fixed order.

Identify the repeated collars. The intervening episode becomes a finite closed track in a history cylinder. Apply the cellwise theorem to obtain a connected root-valued history cylinder.

Its legal `1`-skeleton is connected. A shortest path between the two boundary subcomplexes is simple and has interior disjoint from both boundaries. A small regular neighbourhood is an embedded root-valued crosscut. Cutting along it gives a root rectangle separating the repeated endpoint copies.

This is the fixed-order periodic disposition used in the resolved-call SCC contradiction.

---

## 4. Impact on the resolved-call rank

The finite parent macro graph `M_N` and

\[
d_N(x)=\operatorname{dist}_{M_N}(x,\mathcal X_N)
\]

remain unchanged.

If a nonterminal sink SCC existed:

1. expand a cycle to one finite witnessed nested episode;
2. eliminate innermost calls;
3. normalize switch--pop events to endpoint collars;
4. apply the arborescence disposition in the root sector;
5. apply the cellwise seam/identity-strip disposition to closed or normalized-open tracks;
6. apply the periodic crosscut to a repeated unresolved endpoint.

No neutral fixed-order recurrence survives. Therefore every selected resolved parent macro lowers `d_N`, and recursive normalization still terminates lexicographically on `(N,d_N)`.

No child-prefix length, mark count, or graph-order descent inside R2.6 enters the rank.

---

## 5. PDL retarget

At the time of this addendum, the latest observed PDL head is

`Yuren-Tang/mathematics:proof-development/affine-cdc-rigour-v1@efd28ee247135eaaea5b47ea29f7d29fb4720167`.

PDL has complete drafts for mutual witnessed induction, child-context fidelity, innermost-bubble compression, full-labelled genealogy, fixed-order consumer compatibility, R2.4, and R2.5.

The remaining R2.6 proof-development target is now the v2 handoff:

`R2_6_CELLWISE_SEAM_RUN_INTERFACE_AUDIT_AND_PDL_HANDOFF_V2.md`.

PDL should not reconstruct the old global annulus or canonical-star gluing as a controlling dependency.

After R2.6 reconstruction, PDL must still supply:

1. final v6/v6.1/v6.2 contextual-transfer synthesis;
2. literal cap/route hypothesis audit;
3. exact terminal-semantics map for every accepted exit.

---

## 6. Assurance boundary

### Retained

- exact inverse `2--2` and cancellation tables;
- active-diagonal and support-switch source lifts;
- witnessed recursive `P_N/Q_N` organization;
- suspended ancestor marks;
- variable-order episode compression;
- finite resolved-call graph and rank `(N,d_N)`;
- original-prefix induction.

### Replaced here

- old global `C6/C8` annulus consumer;
- old global open-star strip consumer;
- old R2.6 PDL handoff.

### Still required

- PDL reconstruction of the cellwise theorem and its interface lemmas;
- final PDL synthesis;
- cap/route and terminal-semantics audit;
- independent audit of the complete dependency DAG.

### Not promoted

- PDL completion;
- independent assurance;
- accepted cap restoration or R1;
- universal five-support/five-CDC theorem;
- Lean, manuscript, curation, release, arXiv, DOI, peer review, or publication status.
