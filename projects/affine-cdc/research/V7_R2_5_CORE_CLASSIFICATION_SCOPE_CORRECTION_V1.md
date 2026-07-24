# V7 R2.5 core-classification scope correction

## Research Lead dependency reduction v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `8f5d91ee49ea84df9b144b0047da63033f6903eb`

**Corrects:**

- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V7_FIRST_CANCELLATION_RETURN.md` insofar as its fixed-order consumer list made the R2.5 odd-core exclusion appear controlling;
- `ONE_CROSS_PROOF_DAG_AND_SUPERSESSION_INDEX_V5.md` insofar as it placed R2.5 before cellwise R2.6 on the critical path;
- any PDL assignment requiring `C5/C9` exclusion or `C6/C8` classification before reconstructing v7.

**Status:** exact dependency reduction. The repaired cellwise seam/run theorem erases an arbitrary finite normalized nonbranching full-state co-root track directly. It does not first reduce the track to a shortest simple Petersen cycle and does not distinguish odd from even cycle lengths. Therefore the oriented R2.5 odd-core theorem and every `C6/C8` classification are optional stronger mathematics, not dependencies of v7.

No theorem status is promoted.

---

## 1. Minimal fixed-order input actually needed

After local first-failure and critical-overlap normalization, v7 needs only the following track interface.

1. Every persistent singular state contains exactly one standard co-root atom.
2. The singular locus is nonbranching.
3. The atom has two crossed root resolutions, represented by one Petersen edge
   \[
   F=\{s,t\}.
   \]
4. Consecutive atom states share one pivot root and therefore define a finite pivot walk.
5. Every state retains complete source topology, ordered dart incidences, side roots, support transport, cap block, route, crossed resolutions, and required marks.
6. Raw support switches are not internal singular cells.

This is the `full-state normalized pivot-track` interface.

It may be obtained from the local first-failure grammar and the initial sections of the full-state R2.4 reconstruction. No simple-core extraction is required.

---

## 2. Direct cellwise consumption

Given the full-state pivot track:

1. partition it into maximal constant-pivot runs and genuine pivot-change cells;
2. place a local root seam in every pivot-change cell;
3. separate adjacent collars by identity subdivision;
4. replace each constant-pivot interval by the identity product of its unique nonpivot root history;
5. glue on literal complete endpoint states;
6. use the normalized endpoint and periodic crosscut theorems.

This works for:

- arbitrary pivot-walk length;
- repeated vertices and edges in the Petersen projection;
- odd or even projected cycles;
- closed or open tracks;
- immediate backtracks, using the established local backtrack normalization or the verified two-seam interpretation.

No simple-cycle length appears.

---

## 3. R2.5 is bypassed

`AC_PD_5CDC_R2_5_ORIENTED_ODD_EXCLUSION.md` proves the valid stronger statement that an oriented fixed-route physical track cannot contain an odd pivot-closed segment.

V7 does not need this theorem because:

- it never asks whether a recurrent core is `C5`, `C6`, `C8`, or `C9`;
- it cuts every pivot-change occurrence locally before forming a global core;
- after cutting, only constant-pivot intervals remain;
- each such interval rootifies independently.

Thus R2.5 may remain in the corpus as structural/interpretive mathematics, but it is removed from the cap-restoration dependency DAG.

---

## 4. R2.4 is narrowed

The controlling portion of R2.4 is only:

- one atom equals one ordered crossed-resolution pair;
- local transport gives a nonbranching pivot walk;
- constant-pivot and pivot-change cells retain complete full-state data;
- every local star/rootification/category branch has exact source semantics.

The following R2.4 downstream steps are not required by v7:

- shortest recurrent-core extraction;
- simple Petersen-cycle classification;
- reduction to the four lengths `5,6,8,9`;
- preparation for an odd/even annulus split.

PDL may reconstruct a narrow `R2.4-track-interface` theorem instead of reproducing the entire historical core-classification route before v7.

---

## 5. Corrected critical path

The fixed-order v7 consumer now has the dependency order:

1. first-failure one-atom uniqueness and critical overlaps;
2. complete nonbranching pivot-track interface;
3. local pivot-change seam theorem;
4. constant-pivot full-state root section;
5. seam/run identity gluing;
6. endpoint and periodic crosscut consumption.

R2.5 odd-core exclusion and global even-core annuli are absent.

---

## 6. PDL obligations

PDL should verify:

1. one-token nonbranching under the pure-NNI fixed-order alphabet;
2. complete pivot/side-root/cap/route state at every track cell;
3. exact local seam for every nonbacktracking pivot change;
4. exact immediate-backtrack disposition;
5. unique two-sided constant-run history;
6. literal seam/run gluing;
7. closed/open/periodic consumption without cycle classification.

It should not delay v7 on:

- the physical parity character;
- odd double-cover exclusion;
- `C5/C9` elimination;
- `C6/C8` annulus construction.

---

## 7. Classification

### Removed from v7 dependencies

- R2.5 oriented odd-core exclusion;
- simple Petersen-cycle length classification;
- global even-core annulus theorems.

### Retained

- narrow full-state pivot-track interface;
- local seams and constant-run strips;
- cellwise closed/open/periodic erasure.

### Still required

- PDL reconstruction of the narrowed interface and cellwise theorem;
- independent audit.

### Not claimed

- accepted cap restoration;
- established five-support/five-CDC theorem;
- Lean, Curator, manuscript, release, or publication status.
