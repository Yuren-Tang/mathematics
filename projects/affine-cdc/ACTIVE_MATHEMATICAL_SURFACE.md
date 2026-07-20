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
- [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md);
- [`five-support/README.md`](five-support/README.md).

## 3. Complete CDC spine

The paper-level Cycle Double Cover line is contained in:

- [`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md);
- [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md);
- [`reduction/outer-shell-and-binary-flow.md`](reduction/outer-shell-and-binary-flow.md);
- [`reduction/even-cover-and-collapse.md`](reduction/even-cover-and-collapse.md).

The natural theorem allows loops and finite active edge set. The present Lean declaration remains an earlier loopless ambient-finite checkpoint.

## 4. Active five-support extension

The ordered active surface is listed in [`five-support/README.md`](five-support/README.md). The latest route-locked chain closes:

- common-cut circuit localisation and the singleton/transition/quartic trichotomy;
- unbounded quartic designs, canonical terminal nucleus, bounded split gadgets, and strict peel recursion;
- quotient Tait phase, Kempe differences, marked transition skeletons, elementary intervals, and periodic ladders;
- the physical `g`-component quotient `\Gamma_g`;
- the route-capped `4`-regular flag-line carrier;
- touch-shadow closure and the bounded two-transition cap residue;
- IAS local degenerations, minimal coupled/separated completion, cocircuit cut-rank, and the symmetry correction;
- the natural-transversal physical projection;
- the exact physical cycle--cut sequence and its symmetric Lagrangian response form.

The global five-support theorem remains open. The controlling fixed-lift object is `T_g^{(1)}`, not merely the factorable quotient `J_g`.

## 5. Correct nonflat architecture

At incidence level, quartic designs have natural sheet symmetry

$$
AGL(2,2)\cong S_4.
$$

This is distinct from both the terminal-route coordinate group and the support-label `D_8` stabiliser of a DDD one-factor. Their comparison is open.

At physical level the relevant objects are now:

1. **Cut carrier `\Gamma_g`.** Internal quotient cuts lift exactly to `g`-coloured cuts of the original four-pole.
2. **Isotropic carrier `F=\mathcal L(\widehat Q)`.** Every nonflat witness compresses to one cross transition at each route-cap vertex.
3. **Minimal cap completion.** Apart from local loop/parallel/twin/pendant cases, the residue completes either to one coupled cocircuit or two disjoint one-cap cocircuits.
4. **Physical natural transversal.** Its circuit partition consists of the vertex triangles of `\widehat Q`, and its touch-graph is canonically `\widehat Q`.
5. **Cycle--cut response.** Full cocycles fit into
   $$
   0\to\operatorname{Cut}(\widehat Q)
   \to\operatorname{Cocycle}(M_\tau(F))
   \to\operatorname{Cycle}(\widehat Q)\to0.
   $$
   The extension is governed, up to cross-label diagonal gauge, by a symmetric response form `\mathcal B_{\widehat Q}` on the physical cycle space.

## 6. Exact frontier

Write a cap cocycle in local/cross coordinates as

$$
(z,a,z+a).
$$

Then

$$
z\in\operatorname{Cycle}(\widehat Q),
\qquad
 a\bmod\operatorname{Cut}(\widehat Q)
 =\mathcal B_{\widehat Q}(z,-).
$$

The zero-cycle branch is closed structurally:

$$
\boxed{z=0\Longrightarrow\text{a physical bond of }\widehat Q.}
$$

For the coupled residue this bond contains both cap edges and yields a terminal-even separator; for a separated one-cap residue it yields a one-ended physical bond.

The only potentially irreducible branch is therefore

$$
\boxed{
\text{coupled prime cap cocircuit}
+
z\ne0
+
\text{locked terminal response}.
}
$$

The next theorem must use the common Fano flow, four affine scalar sheets, Kempe systems, endpoint selectors, and `\Gamma_g` to turn every such response word into:

- a physical separator or transition two-sum;
- a crossed route and root escape;
- a bounded replacement or horizontal switch;
- or a genuine comparison with the DDD support-label class.

The cube certificate shows that cocircuit minimality alone does not force `z` to be one connected physical circuit.

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
