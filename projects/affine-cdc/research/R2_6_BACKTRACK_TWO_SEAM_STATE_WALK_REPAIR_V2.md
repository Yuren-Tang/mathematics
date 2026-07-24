# R2.6 backtracks are cut by two state-walk seams

## Research Lead repair and retraction v2

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `82dd87096df56bf16c0a4513f2064db12ed01594`

**Controls with:**

- `CELLWISE_ROOT_SEAM_AND_CONSTANT_RUN_TRACK_ERASURE_V1.md`;
- `PETERSEN_PIVOT_RESOLUTION_V1.md`;
- `PIVOT_CHANGE_SIX_PORT_STAR_COMPLETION_V1.md`;
- `CONSTANT_PIVOT_FULL_STATE_CONTEXTUAL_CONSUMPTION_V1.md`;
- `R2_6_CELLWISE_SEAM_RUN_INTERFACE_AUDIT_AND_PDL_HANDOFF_V2.md`.

**Supersedes:**

- the general-open conclusion of `R2_6_IMMEDIATE_BACKTRACK_SOURCE_SCOPE_CORRECTION_V1.md`;
- every use of a graph-side Type-T contraction as a prerequisite for the cellwise R2.6 theorem.

**Retains from the v1 warning:**

- coefficient free reduction `s->t->s` is not by itself a source-graph contraction;
- `PETERSEN_BACKTRACK_TYPE_T_REDUCTION_V1.md`, the Type-T square, and the square envelope do not prove arbitrary physical Type-T subgraph deletion;
- the phrase `two relocations undo each other` is valid only for a literal complete-state involution digon.

**Correction:** the cellwise theorem never needs to contract the whole Type-T corridor. The two seams are placed at the two **state-walk pivot-change cells**, not at the two edges of the reduced Petersen skeleton viewed without their adjoining runs. Each such cell has distinct neighbouring Petersen-edge states and therefore satisfies the nonbacktracking six-port hypotheses. The interval between the seams is one constant-pivot run and rootifies by its unique full-state nonpivot section.

**Restored status:**

`R2.6 CLOSED AT RL AUTHORIAL LEVEL / NO TYPE-T GRAPH CONTRACTION INPUT / PDL RECONSTRUCTION AND INDEPENDENT ASSURANCE REQUIRED`.

No established five-CDC theorem is claimed.

---

## 1. Normalized Petersen-edge state walk

Let

`F_0,F_1,...,F_m`

be the coefficient projection of one normalized nonbranching full-state atom track.

After absorbing identity subdivisions and coefficient-neutral repeated-state intervals into the surrounding constant-run history, every genuine transition satisfies:

1. `F_(r-1) != F_r`;
2. `F_(r-1)` and `F_r` are adjacent vertices of the line graph `L(P)`;
3. hence they share exactly one Petersen root.

Define the transition pivot

`p_r = F_(r-1) intersect F_r`.

Partition the pivot word `p_1,...,p_m` into maximal constant runs.

A genuine pivot change occurs at an index `r` with

`p_r=s`, `p_(r+1)=t`, `s!=t`.

Since both pivots are endpoints of the intermediate atom state,

`F_r={s,t}`.

---

## 2. Run-boundary nonbacktracking lemma

Write the neighbouring states as

`F_(r-1)={s,x}`,  `F_r={s,t}`,  `F_(r+1)={t,y}`.

### Lemma 2.1

At every genuine run boundary,

`x!=t` and `y!=s`.

### Proof

If `x=t`, then `F_(r-1)=F_r={s,t}`, contradicting the normalized distinctness of consecutive genuine states. Likewise `y=s` would give `F_(r+1)=F_r`. Therefore the local four-root sequence

`x -> s -> t -> y`

is nonbacktracking in exactly the sense required by the six-port theorem. ∎

### Consequence 2.2

The side roots

`z=x+t`,  `w=s+y`

are nonzero, distinct and intersecting. The exact relative `(0,2,2)` table gives a root seam in this source cell while fixing both turn corollas and every complete exterior datum.

Thus every boundary between two maximal constant-pivot runs is a legal seam site.

---

## 3. Reduced-skeleton backtrack versus local cell

Suppose the **reduced run skeleton** contains

`s -> t -> s`.

Let the first change `s->t` occur at state `F_r={s,t}` and the second change `t->s` occur at state `F_q={t,s}`.

These are two occurrences of the same Petersen edge in the coefficient projection, but they need not be the same physical source state.

Between them the transition pivots are all equal to `t`. Hence the segment

`F_r,...,F_q`

is one constant-`t` run, possibly containing distinct physical topologies and arbitrary rooted side attachments.

### Lemma 3.1 — the two switch cells are individually genuine

The first switch has local states

`{s,x} -> {s,t} -> {t,y}`

with `x!=t`, `y!=s`.

The second switch has local states

`{t,x'} -> {t,s} -> {s,y'}`

with `x'!=s`, `y'!=t`.

Therefore both are nonbacktracking six-port cells.

### Proof

Apply Lemma 2.1 at each of the two distinct maximal-run boundaries. The fact that the next **run pivot** after `t` is `s` says nothing about the immediate nonshared endpoint `y` of the first next atom state. It only identifies the far boundary of the entire constant-`t` run. ∎

This is the index distinction missed by the v1 scope correction.

---

## 4. Why a zero-length middle run is not a new case

Assume formally that the two run changes were consecutive with no genuine `t` transition between them.

Then their switch states would satisfy

`F_r={s,t}=F_(r+1)`.

This is not an edge of the simple line graph `L(P)` and has no uniquely defined transition pivot. In the normalized full-state track it is one of:

1. an identity history subdivision;
2. a coefficient-neutral repeated-state interval;
3. a literal complete-state involution digon.

Cases 1--2 are absorbed into a neighbouring constant-pivot run; the state `F={s,t}` may be assigned the pivot selected by that run because no intervening emitted root turn forces the other choice. Case 3 deletes by ordinary root/Ptolemy involutivity.

Thus every **genuine** reduced-skeleton backtrack with two distinct run boundaries has a nonempty normalized constant-pivot interval between its seam sites.

---

## 5. Two-seam replacement of an arbitrary physical backtrack corridor

Let the two switch cells occur at arbitrary physical source locations and let the middle constant-`t` run carry arbitrary finite rooted side attachments.

Proceed as follows.

1. Put the exact local root seam in the first switch cell.
2. Put the exact local root seam in the second switch cell.
3. If the collars share a history vertex, insert an identity interval and choose disjoint collar interiors.
4. Cut along both seams.
5. The singular component between them is exactly the constant-`t` interval.
6. Its two root-valued long-side restrictions are literally the same unique nonpivot full-state history.
7. Replace it by the identity product of that history.
8. Glue to both seam collars by equality of complete endpoint states.

### Theorem 5.1 — source-faithful backtrack-corridor erasure

Every reduced-skeleton immediate backtrack `s->t->s`, including a nonliteral physical Type-T corridor with arbitrary constant-run length and side attachments, has a root-valued relative replacement obtained from two local seams and one constant-run identity strip.

The construction does not:

- delete the coefficient word abstractly;
- contract a Type-T source subgraph;
- enclose the corridor as a universal physical four-port;
- use the canonical Type-T square as a source replacement;
- require the two switch moves to be physical inverses.

It uses only source cells already present at the two run boundaries and the actual full-state history between them.

---

## 6. Complete-state endpoint matching

At the first switch, the left constant-`s` run demands root `t` at the central state and the right constant-`t` run demands root `s`.

At the second switch, the left constant-`t` run demands root `s` and the right constant-`s` run demands root `t`.

The two seams expose exactly these nonpivot roots because their turn corollas are fixed pointwise.

The middle identity strip and both seam collars agree literally on:

- source vertex and dart slots;
- every edge root;
- the selected crossed resolution;
- every emitted side root and rooted attachment;
- support transport;
- cap block and route orientation;
- every surviving mark required by the fixed-order state.

Hence no coefficient-only identification occurs.

---

## 7. Correct role of the Type-T files

The Type-T coefficient and square files remain correct within their stated scopes.

They show:

- the forced resolution word is `t,s,s,t`;
- an abstract four-root Type-T boundary has a canonical root square;
- physical Type-T kernel mismatch is eliminated in the separate four-pole setting.

None is needed for Theorem 5.1.

The v1 warning was therefore right that a Type-T graph contraction was unproved, but wrong that this left R2.6 open. Cellwise seam placement bypasses that graph-contraction problem.

---

## 8. Restored cellwise theorem

### Theorem 8.1

Every finite normalized nonbranching full-state co-root track is erased by:

1. seams at all genuine maximal-run boundaries;
2. identity subdivision for adjacent collars;
3. identity-product strips on every residual constant-pivot interval;
4. exact normalized endpoint and periodic-crosscut constructions.

Reduced-skeleton backtracks require no additional local theorem beyond Theorem 5.1.

Thus the conclusions of the original cellwise closed/open/periodic track theorem are restored.

---

## 9. Impact on v7

The v7 fixed-order one-atom consumer may again use the general cellwise R2.6 theorem.

The controlling fixed-order route remains:

- one-token nonbranching track;
- state-walk run decomposition;
- local seam at every run boundary;
- constant-run identity strips;
- no cancellation reopening;
- fixed-order rank `(prefix length,target distance,atom rank)`.

No R2.5 odd-core theorem, simple-cycle classification, global annulus, Type-T graph peeling or variable-order recursion is restored to the critical path.

---

## 10. PDL audit obligations

PDL must independently check:

1. the distinction between atom-state indices and reduced run-skeleton pivots;
2. normalized distinctness of consecutive genuine Petersen-edge states;
3. Lemma 2.1 at every run boundary;
4. absorption of coefficient-neutral repeated states;
5. existence of a nonempty normalized middle run for two distinct backtrack switch occurrences;
6. both six-port local seam tables;
7. literal endpoint equality with the middle constant-run identity strip;
8. arbitrary side-attachment preservation;
9. closed/open/periodic assembly.

PDL must not justify the theorem by abstract `abba` deletion.

---

## 11. Classification

### Restored authorial result

`R2.6 CLOSED AT RL AUTHORIAL LEVEL`.

### v7 status

`R2.7-v7.1 COMPLETE AUTHORIAL CANDIDATE / ORDINARY STRONG INDUCTION ONLY`.

### Still required

- PDL reconstruction;
- independent audit of state-walk normalization, local seam tables, run gluing, v7 finite tables and terminal consumers.

### Not claimed

- independently accepted cap restoration;
- established five-support/five-CDC theorem;
- Lean verification;
- Curator/canonical movement;
- manuscript, release, arXiv, DOI, peer review or publication status.
