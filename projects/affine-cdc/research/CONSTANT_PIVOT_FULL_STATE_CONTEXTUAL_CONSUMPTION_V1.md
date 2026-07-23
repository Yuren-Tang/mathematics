# Constant-pivot full-state runs are consumed by their unique physical root section

## Research dossier v1 — full-state correction consumer

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `f3f38b703b8955e6c116ae1fa45da2697165fd6b`.

**Parents:**

- `CONSTANT_PIVOT_ORIENTED_ROOT_SECTION_V1.md`;
- `CONSTANT_PIVOT_SCOPE_CORRECTION_V1.md`;
- `SIX_OUTPUT_FULL_STATE_CYCLE_CORRECTION_V1.md`;
- `PETERSEN_STAR_REFLECTION_V1.md`;
- `STAR_EXPANDED_PENTAGON_REFLECTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `PETERSEN_C8_TWO_C6_HISTORY_FILLING_REDUCTION_V1.md`.

**Status:** exact contextual use of constant-pivot runs which respects the full-state cycle correction. A maximal constant-pivot DDD run is not deleted as a support-holonomy-neutral word. Instead, the cap-oriented lock chooses its unique nonpivot root section, preserving every actual emitted side root and every exterior incidence. Thus the complete run is physically root-valued and ceases to carry a first-failure atom. A closed constant-pivot star triangle is therefore transfer success, not a trapped atom loop, even though its abstract support transport is a reflection. In a mixed track, resolve every maximal run without changing its side attachments; the only remaining incompatibilities are the opposite endpoint resolutions at genuine pivot changes. Odd reduced pivot cycles remain excluded by resolution parity, while even reduced cycles are consumed by the relative `C6` star movie and the two-`C6` `C8` reduction, with the resolved runs treated as fixed rooted branches. No claim is made that the collapsed pivot skeleton determines full support monodromy.

**Assurance boundary:** this theorem uses the physical side-preserving root section of each constant-pivot run. It does not assert physical realisability of arbitrary abstract support reflections as independent source loops.

---

## 1. Full state versus pivot skeleton

A co-root transport state is one Petersen edge

\[
F_t=\{s_t,d_t\}.
\]

A sequence of states belongs to the line graph `L(P)` of the Petersen graph. Collapsing a maximal constant-pivot run to one pivot vertex forgets internal support transport.

The full-state correction gives explicit examples:

- a three-turn star triangle has one constant pivot but transposition support monodromy;
- inserting one extra constant-pivot state in a Petersen pentagon changes its full monodromy from a four-cycle to a double transposition.

Therefore the implication

\[
\text{same collapsed pivot skeleton}
\Longrightarrow
\text{same full support state}
\]

is false and is not used below.

---

## 2. Unique physical section of one run

Fix one maximal constant-pivot run

\[
F_t=\{s,d_t\},
\qquad t=0,\ldots,m.
\]

At a transition

\[
\{s,x\}\to\{s,y\}
\]

let `z` be the emitted side root. Then

\[
x+y+z=0.
\]

The oriented cap lock has two candidate resolution sheets:

- the pivot sheet `s`;
- the nonpivot sheet `d_t`.

The local root equation uniquely selects the nonpivot sheet:

\[
\boxed{r_t=d_t.}
\]

### Theorem 2.1 — side-preserving run rootification

Every maximal constant-pivot run has one unique simultaneous root section which:

1. resolves every co-root state in the run;
2. preserves every emitted side-root occurrence exactly;
3. preserves every exterior attachment and its incidence order;
4. preserves the ordered terminal matching and chosen cap block;
5. transports `d_0` to `d_m`.

This is an actual physical root section of the run, not a statement about its support permutation quotient.

---

## 3. Closed constant-pivot loops

Assume

\[
F_m=F_0.
\]

Then

\[
d_m=d_0.
\]

The unique nonpivot section closes root-valuedly and preserves the complete side word.

### Theorem 3.1 — star loops are not trapped atom loops

A closed constant-pivot state walk, including the three-turn star triangle, cannot be a persistent first-failure component in a no-exit contextual state.

### Proof

Apply the unique root section of Theorem 2.1. Every co-root atom in the run is replaced by a root resolution while all physical side attachments remain fixed. This gives complete local root transfer through the run. Hence the alleged persistent defect component disappears. ∎

The abstract star reflection may remain a nontrivial permutation of support names in a coefficient description. It does not obstruct the actual selected root section and is not set equal to the identity.

---

## 4. Mixed tracks and endpoint switch states

Partition a persistent co-root track into maximal constant-pivot runs. Resolve every run by Theorem 2.1.

At a genuine pivot change from pivot `s` to pivot `t`, the shared DDD state is

\[
F=\{s,t\}.
\]

The run on the left forces resolution `t`; the run on the right forces resolution `s`. These are the two opposite crossed resolutions of the same atom.

### Theorem 4.1 — full-state reduction to switch cells

After physical rootification of all maximal constant-pivot runs:

1. every side attachment inside every run is retained;
2. every support transport inside every run is retained as part of the rooted branch data;
3. the only unresolved cells are genuine pivot-change switch states;
4. adjacent switch cells are connected by fully root-valued rooted carriers.

Thus the reduced pivot skeleton records only the locations of unresolved switch cells. It is not asserted to encode the complete support monodromy of the rooted carriers between them.

---

## 5. Odd reduced cycles

After deleting immediate pivot backtracks, a recurrent switch track contains a simple Petersen pivot cycle. Suppose its length is odd (`C5` or `C9`).

The resolution-sheet parity theorem computes the sheet exchange from the pivot changes. Constant-pivot runs add no switch of the selected nonpivot sheet: they transport it root-valuedly from one endpoint to the other.

Therefore the return parity remains

\[
\boxed{1\in\mathbf F_2.}
\]

### Theorem 5.1 — odd exclusion survives full-state decorations

No full-state track whose reduced pivot core is `C5` or `C9` can return to the same oriented contextual state, regardless of the lengths or support monodromies of the intervening constant-pivot runs.

### Star-expanded pentagon

Its pivot-run pattern is `(2,1,1,1,1)`. Rootify the unique length-two run physically. The remaining switch core is one Petersen `C5`, whose odd resolution return is impossible. Thus the star-expanded reflection sector is consumed without asserting that its full support reflection is trivial.

---

## 6. Even reduced cycles

Suppose the reduced switch core is `C6` or `C8`.

The physical rootification of each intervening constant-pivot run supplies one fixed rooted branch at every switch. The relative `C6` cell theorem uses only:

- the two fixed turn resolutions at adjacent switch states;
- the actual emitted side roots at the switch;
- the unchanged rooted branches attached outside the local cell.

Hence all resolved constant-pivot carriers may be retained verbatim as exterior rooted branches during the relative `(0,2,2)` NNI movie.

### Theorem 6.1 — even descent survives full-state decorations

A full-state recurrent track with reduced pivot core `C6` reaches the canonical relative star and an equal-face cancellation while preserving every resolved constant-run attachment.

A reduced `C8` decomposes into two seam-compatible `C6` factors; apply the same movie in one factor while fixing all resolved run and seam data.

Therefore every even decorated track enters strict target-order descent.

---

## 7. Complete full-state recurrence disposition

A closed recurrent contextual track is consumed as follows.

1. **No pivot change:** unique constant-pivot root section gives transfer success.
2. **Immediate backtrack:** the two normalized relocations cancel.
3. **Odd reduced pivot cycle:** oriented resolution parity forbids return.
4. **Even reduced pivot cycle:** relative star movie forces equal-face cancellation.

This list is invariant under arbitrary constant-run lengths and retains all physical side attachments.

### Theorem 7.1 — full-state no-return theorem

No nonterminal recurrent first-failure track survives after full state, support transport, side-output data, and constant-pivot decorations are retained.

The proof does not rely on the false assertion that the pivot skeleton determines full support monodromy.

---

## 8. Correction to contextual authority

Read `CONTEXTUAL_TRANSFER_REPAIRED_AUTHORITY_V2.md` and `ORIENTED_FULL_CHANNEL_LOCK_ELIMINATION_REPAIRED_V2.md` with the following explicit preliminary step:

> Before classifying a recurrent Petersen pivot core, resolve every maximal constant-pivot run by its unique side-preserving nonpivot root section. Treat the resulting rooted carriers as fixed exterior data at the pivot-change cells. Do not delete or trivialise their support monodromy.

With this step, the short full-state cycle correction is fully respected:

- star triangles are rootified;
- star-expanded pentagons reduce physically to odd switch cores;
- Petersen hexagons are consumed by strict descent;
- no support-reflection sector is silently identified with identity.

---

## 9. Trust boundary

### Exact here

- physical side-preserving rootification of every constant-pivot run;
- consumption of closed star triangles as root transfer;
- retention of full support transport as rooted branch data;
- reduction of mixed tracks to pivot-change switch cells without quotienting physical semantics;
- odd-cycle exclusion with arbitrary constant-run decorations;
- even-cycle strict descent with arbitrary constant-run decorations;
- full-state recurrence disposition consistent with the correction census.

### Not claimed

- that every abstract support reflection is physically realised as a standalone source loop;
- that support monodromy is gauge-trivial;
- downstream proof development, curation, Lean verification, manuscript integration, release, or publication.
