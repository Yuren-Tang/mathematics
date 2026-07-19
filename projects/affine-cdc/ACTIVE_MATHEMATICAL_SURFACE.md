# AffineCDC active mathematical surface

This file identifies the current-best mathematical surface produced by `AC-CORPUS-01` and later exact Research Lead frontier commits.

## 1. Construction line

The active surface is built on:

- `main@749e0579581fcc838685138b3582f4de306b8e72`;
- public five-support checkpoint `dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`;
- accepted outer-shell source `0927011177cabac20f06a57fa5e57476d6f13dee`;
- reconstruction base `7a166d2eb5642ec967f640323488e49f1c2ad5d4`;
- completed corpus migration `960c92b7ff231c78b387894149779083060a75eb`;
- later commits on `research/affine-cdc-five-cdc-v1`.

Retired discovery packets remain recoverable in Git ancestry; they are not the current reading surface.

## 2. Primary entrypoints

- [`README.md`](README.md);
- [`CURRENT_BEST.md`](CURRENT_BEST.md);
- [`MATHEMATICAL_ARCHITECTURE.md`](MATHEMATICAL_ARCHITECTURE.md);
- [`THEOREM_DEPENDENCY_MAP.md`](THEOREM_DEPENDENCY_MAP.md);
- [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md).

## 3. Complete CDC spine

The paper-level Cycle Double Cover line is contained in:

- [`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md);
- [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md);
- [`reduction/outer-shell-and-binary-flow.md`](reduction/outer-shell-and-binary-flow.md);
- [`reduction/even-cover-and-collapse.md`](reduction/even-cover-and-collapse.md).

The natural theorem allows loops and finite active edge set. The present Lean declaration remains an earlier loopless ambient-finite checkpoint.

## 4. Active five-support surface

The active five-support reading surface is the ordered chapter list in [`five-support/README.md`](five-support/README.md). Its latest route-locked extension contains:

- common-cut circuit localisation;
- quartic witness designs and the `O^-(4,2)` terminal nucleus;
- quotient Tait phase, marked transition skeletons, and nucleus transport;
- elementary scalar transfer, caps, cells, and Kempe ladders;
- the physical `g`-component quotient `\Gamma_g`;
- the route-capped `4`-regular flag-line carrier;
- relative touch homology, shadow closure, and the two-transition cap residue;
- IAS loop/parallel/twin/pendant classification;
- minimal two-cap cocycle decomposition.

The global five-support theorem remains open. The controlling fixed-lift object is `T_g^{(1)}`, not merely the factorable quotient `J_g`.

## 5. Current nonflat architecture

The common-cut witness is localised to a singleton, a marked two-edge transition, or a quartic core.

At incidence level:

- quartic designs exist for every `4k+1`;
- every design has a canonical `O^-(4,2)` terminal nucleus with intrinsic `E_5/K_5` geometry;
- a split sheet exposes a bounded `K_6` coefficient gadget;
- an all-concentrated design peels to level `k-1`;
- successive nuclei are canonically equivariant under the natural sheet group `AGL(2,2)\cong S_4`.

The sheet group, the physical terminal-route stabiliser, and the support-label `D_8` stabiliser of a DDD one-factor are distinct. Their comparison remains open.

At physical level there are three coordinated carriers.

1. **`g`-component quotient `\Gamma_g`.** Contract the components of `Q-E_g`. Four scalar sheets become four transition systems on an even-total-degree four-pole. Every internal quotient cut lifts exactly to a `g`-coloured cut of `Q`; cut parity retains the number of original terminal flags on the shore.
2. **Route-capped line graph.** Close terminals according to `12\mid34` and take the flag-line graph. This gives one canonical `4`-regular graph carrying four scalar circuit partitions and one transition matroid.
3. **Touch/isotropic carrier.** Every selected scalar circuit has a shadow circuit. Consequently complementary touch boundary closes automatically. Adding the two fixed route caps turns each scalar common cut into an ordinary touch cycle.

Summing the four cap-completed transition supports cancels every internal witness transition and leaves one selected cross transition at each cap vertex.

## 6. Exact frontier

Let

$$
R=\{r_p,r_q\}
$$

be the bounded two-cap residue. It is not itself a full cocycle because every IAS cocycle meets each vertex triple in zero or two elements.

Except for an immediate loop degeneration, a full cocycle containing `R` exists. Choose one inclusion-minimal under support. Exactly one of:

1. **coupled:** one cocircuit contains both `r_p,r_q`;
2. **separated:** the completion is the disjoint union of two cocircuits, one carrying each residue, and their isotropic vertex supports are disjoint.

The immediate local completion cases are already classified as loop, parallel, twin, or pendant interlacement configurations.

The next theorem must project the minimal completion to the physical layer:

$$
\boxed{
\text{coupled/separated cap cocircuit}
\Longrightarrow
\text{separator, serial composition, alternate route, or DDD comparison.}
}
$$

Only the coupled branch can remain a genuinely irreducible two-ended obstruction.

## 7. Reliability and provenance

See:

- [`CHAPTER_PROVENANCE.md`](CHAPTER_PROVENANCE.md);
- [`MIGRATION_LEDGER.md`](MIGRATION_LEDGER.md);
- [`SUPERSESSION_MAP.md`](SUPERSESSION_MAP.md);
- [`RETIRED_SOURCE_CLASSIFICATION.md`](RETIRED_SOURCE_CLASSIFICATION.md);
- [`SOURCE_RECOVERY_AUDIT.md`](SOURCE_RECOVERY_AUDIT.md);
- [`FORMAL_STATUS.md`](FORMAL_STATUS.md);
- [`RECONSTRUCTION_MANIFEST.md`](RECONSTRUCTION_MANIFEST.md).

Current-best inclusion does not create independent review, Lean verification, peer review, manuscript approval, release, arXiv, DOI, or publication status.
