# Full-state scope addendum to the two-seam backtrack repair

## Research Lead v2.1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `244e0832c1f6b03c1338e8bdfb97701ad96f6b9f`

**Controls with:**

- `R2_6_BACKTRACK_TWO_SEAM_STATE_WALK_REPAIR_V2.md`;
- `CONSTANT_PIVOT_FULL_STATE_CONTEXTUAL_CONSUMPTION_V1.md`, especially Theorems 2.1 and 4.1;
- `PIVOT_CHANGE_SIX_PORT_STAR_COMPLETION_V1.md`;
- `CELLWISE_ROOT_SEAM_AND_CONSTANT_RUN_TRACK_ERASURE_V1.md`.

**Scope correction:** Section 4 of the v2 repair should not be read as an independent theorem that every pair of coefficient-identical physical states contracts source-faithfully. That stronger statement is unnecessary. The controlling normalization is the established full-state run theorem: physically rootify every maximal constant-pivot run first, preserving all source histories and attachments. Only genuine run-boundary switch cells remain unresolved. A reduced-skeleton backtrack consists of two such distinct switch occurrences joined by the rooted middle run. The two-seam proof applies to those switch cells.

No theorem status is promoted beyond v2.

---

## 1. Full-state preliminary normalization

Given one normalized nonbranching atom track, apply `CONSTANT_PIVOT_FULL_STATE_CONTEXTUAL_CONSUMPTION_V1.md` to every maximal constant-pivot run.

For each run this produces its unique nonpivot root section and preserves:

- every source topology in the run;
- every emitted side-root occurrence;
- every exterior rooted attachment and incidence order;
- complete support transport;
- the ordered cap block and route;
- the endpoint crossed-resolution roots.

No physical run is deleted and no support monodromy is set equal to the identity.

The exact output of its Theorem 4.1 is:

1. all run interiors are root-valued rooted carriers;
2. the only unresolved locations are genuine pivot-change switch cells;
3. adjacent switch cells are joined by those rooted carriers.

This is the controlling meaning of `partition into runs and switch cells`.

---

## 2. Genuine switch-cell indexing

At one remaining switch cell from run pivot `s` to run pivot `t`, the adjacent atom states have the six-port form

`F^-={s,x}`, `F={s,t}`, `F^+={t,y}`,

where the six-port theorem itself requires and records

`x!=t`, `y!=s`.

These inequalities are not inferred from the next vertex of the **reduced run skeleton**. They are properties of the two atom states immediately adjacent to this physical switch cell.

Therefore every unresolved switch cell output by the full-state run theorem is a legal nonbacktracking seam cell.

---

## 3. Immediate reduced-skeleton backtrack

Let the reduced run skeleton contain

`s -> t -> s`.

By definition this means:

1. one genuine switch occurrence from an `s`-run to a `t`-run;
2. one maximal constant-`t` run, already converted to a rooted carrier;
3. a second genuine switch occurrence from that `t`-run to an `s`-run.

Thus there are two distinct switch cells in the full-state decomposition, regardless of whether their coefficient switch states both project to the same Petersen edge `{s,t}`.

Apply the local six-port seam separately at the two cells and the identity-product strip to the rooted middle carrier.

### Theorem 3.1

Every immediate backtrack in the reduced **run skeleton** is consumed by two legal nonbacktracking switch seams plus the physical root section of the middle run.

No assertion about coefficient-identical state contraction is used.

---

## 4. Coefficient-neutral intervals

If a physical history interval projects repeatedly to the same Petersen edge but does not contain two genuine run-boundary switches, it is not a reduced-skeleton backtrack of Theorem 3.1.

It remains inside the full-state constant-run/root-carrier normalization or an identity subdivision according to the one-token grammar. Its source history and side attachments are retained verbatim.

The v2 proof does not delete such an interval merely because its coefficient label repeats.

---

## 5. Corrected assurance statement

The two-seam backtrack repair depends on:

- full-state physical rootification of maximal runs;
- the exact six-port local theorem at each genuine switch;
- literal endpoint gluing.

It does not depend on:

- source contraction of repeated Petersen labels;
- coefficient free reduction;
- a universal Type-T four-port enclosure;
- physical equality of the two switch moves.

---

## 6. Classification

The restored classification remains:

`R2.6 CLOSED AT RL AUTHORIAL LEVEL / R2.7-v7.1 COMPLETE AUTHORIAL CANDIDATE / PDL RECONSTRUCTION AND INDEPENDENT ASSURANCE REQUIRED`.

Not claimed:

- accepted cap restoration;
- established five-support/five-CDC theorem;
- Lean, Curator, manuscript, release or publication status.
