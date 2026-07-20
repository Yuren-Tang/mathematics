# Programme B1 final curation audit

## 1. Exact controls

- authoritative intake: `Yuren-Tang/research-workbench#24`, comment `5018524043`;
- integration base: `curation/affine-cdc-programme-a-v1@68715fb29bb4b6555e2bc3e089603c5390d01566`;
- immutable B1 source: `proof-development/affine-cdc-rigour-v1@778b09ac8260192e022f512f24cdef1d04871f37`;
- candidate branch: `curation/affine-cdc-programme-b1-v1`;
- exact source splice: `35c7a2851f070061175194eef10568c0a456cf8e`.

The exact final candidate SHA is recorded in the authoritative issue #24 return.

## 2. Splice and ancestry audit

The splice commit has two parents, in order:

1. `68715fb29bb4b6555e2bc3e089603c5390d01566`;
2. `778b09ac8260192e022f512f24cdef1d04871f37`.

Its tree contains exactly:

- B1.1 root-flow/triangle dossier;
- B1.2 matching/four-flow dossier;
- B1.3 fixed-flow/plane dossier;
- B1.4 surface/halfcube dossier;
- B1 aggregate equivalence/scope map;
- the immutable B1 `OBLIGATION_DAG.md`.

The source-side `PROGRAMME_A_CURATOR_HANDOFF.md` was excluded from the splice tree. The later `PROGRAMME_B1_CURATOR_HANDOFF.md` was read as a control/routing document only and was not copied into the candidate.

## 3. Source-blob audit

Relative to the exact splice commit, the Curator delta modifies no file under `projects/affine-cdc/proof-development/`.

Therefore the five B1 dossiers and the B1 checkpoint DAG retain exact source blob identity.

## 4. Six-correction audit

All six corrections required by the intake are visible in the active corpus.

1. **Support coordinate versus root label.** A support-coordinate inverse image is even; a root-label inverse image is a matching.
2. **Four-flow converse.** Bare matching plus four-flow is insufficient; the exact $(B,D)$ or component endpoint-parity/$T$-join datum is required.
3. **Fixed-lift scope.** The fixed-$g$ biconditional concerns componentwise relabelling of the same cycle-face embedding.
4. **Holonomy boundary.** An external cover integrates on a prescribed dual exactly when every dual cycle has zero root-flow sum.
5. **Factorability boundary.** $J_g$ classifies only maps constant on old-colour fibres.
6. **Half-cube parity.** Singleton words lie in the odd component; the even component requires an odd translation.

## 5. Quantifier audit

The candidate distinguishes all required levels.

### Graph-level

Only $G$ is fixed. The flow, plane, matching data, root lift, and cycle-face embedding are existential.

### Fixed $(f,W)$

The global slice, distinguished support, component $T$-join, one/all outside-colour parities, quotient Eulerianity, and local affine obstruction are equivalent.

### Fixed $f$

Factorable success means that some plane profile is empty. Failure of one prescribed flow is not failure of the graph.

### Fixed compatible lift $g$

$T_g^{(1)}\to\mathscr A_5$ classifies componentwise compression of the same embedding.

### Fixed dual plus external root flow

A potential exists exactly when every dual cycle holonomy vanishes. Triangular-face conservation alone is insufficient.

### Old-colour quotient

$J_g\to\mathscr A_5$ is exactly the fibre-constant factorable subclass of full-dual maps.

## 6. B2+ exclusion audit

The live PDL branch is ten commits ahead of the immutable B1 source. Its later delta contains:

- five `AC_PD_B2_*` dossiers;
- two `AC_PD_B3_*` correction dossiers;
- later `OBLIGATION_DAG.md` changes;
- `PROGRAMME_B1_CURATOR_HANDOFF.md`;
- `PROGRAMME_B2_CURATOR_HANDOFF.md`.

None of those later mathematical files or later ledger versions is present in the candidate source intake.

The candidate does not disposition B2 or B3 claims. It only marks their formulation/correction layers as requiring separate exact intake.

## 7. Programme A isolation

- `curation/affine-cdc-programme-a-v1` remains exactly `68715fb29bb4b6555e2bc3e089603c5390d01566`;
- no Programme A `complete-cdc/` chapter was modified by the B1 Curator delta;
- Programme A remains the fixed Audit A candidate;
- no Audit A status was upgraded or otherwise changed.

## 8. Repository isolation

- `main` remains exactly `960c92b7ff231c78b387894149779083060a75eb`;
- the live PDL branch was not modified;
- no branch was deleted or renamed;
- no force-push, rebase, squash, or public-history rewrite occurred;
- no Lean or manuscript repository was changed;
- no publication, release, arXiv, DOI, or timestamp action occurred.

## 9. Assurance audit

Programme B1 is classified as:

`CURATOR-INTEGRATED / AUTHORIAL B1 PROOF LAYER COMPLETE`.

It is not independently audited and not end-to-end Lean verified. Exact finite certificates mentioned in the wider corpus retain their finite-evidence scope.

The global five-support theorem remains open.

## 10. Stop-condition audit

No stop condition was triggered.

- no contradiction among the B1 units was found;
- no unrecorded fixed-data hypothesis was required;
- no ambiguity between even-support and circuit objects remains in the B1 active text;
- no graph-model change was required;
- no B2+ mathematical result was needed to install the six B1 corrections.

## 11. AC-DIR disposition questions

The candidate leaves these exact decisions to AC-DIR:

1. whether to accept this candidate as the next rolling five-support corpus baseline while keeping Programme A separately fixed for Audit A;
2. whether B1 should receive a dedicated independent audit now or be included in a later correction-aware Audit B scope;
3. whether to authorize the next separate B2 intake from its exact immutable checkpoint only after B1 disposition;
4. whether any accepted B1 correction requires an immediate issue #36 scope update before B2/B3 integration;
5. whether later canonical movement, if authorized, should preserve this two-parent provenance splice.

No mathematical ambiguity requires pre-disposition escalation.
