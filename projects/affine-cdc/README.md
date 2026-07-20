# AffineCDC

AffineCDC studies affine incidence geometry attached to nowhere-zero binary flows, its complete Cycle Double Cover consequence, and the stronger open problem of compressing compatible covers to five indexed supports.

The active current-best surface is listed in [`ACTIVE_MATHEMATICAL_SURFACE.md`](ACTIVE_MATHEMATICAL_SURFACE.md).

## 1. Complete Cycle Double Cover theorem

Programme A integrates a complete authorial paper-proof of:

> Every multigraph with finite active edge set and no singleton cut has a finite circuit double cover.

Equivalently, no nonloop active edge is a bridge. Loops, parallel edge objects, disconnected components, isolated vertices, and an arbitrary ambient vertex carrier are allowed.

The proof chain is:

```text
finite-active multigraph with no singleton cut
→ exact loop deletion
→ finite loopless cubic port-cycle expansion
→ nowhere-zero F₂³ flow
→ affine pair complex and rank-three compatibility
→ graph-level indexed even supports
→ intrinsic cut-even collapse
→ one finite circuit decomposition
→ exact loop reinsertion
→ circuit double cover
```

Read the controlling Programme A proof in this order:

1. [`complete-cdc/foundations-expansion-and-flow.md`](complete-cdc/foundations-expansion-and-flow.md);
2. [`complete-cdc/affine-compatibility-and-extraction.md`](complete-cdc/affine-compatibility-and-extraction.md);
3. [`complete-cdc/collapse-decomposition-and-assembly.md`](complete-cdc/collapse-decomposition-and-assembly.md).

The exact A0–A10 authorial dossiers and obligation DAG remain under [`proof-development/`](proof-development/) as provenance and repair surfaces. See [`PROGRAMME_A_INTEGRATION_MAP.md`](PROGRAMME_A_INTEGRATION_MAP.md).

The sole external non-elementary logical input is Seymour’s nowhere-zero six-flow theorem. Equal-order finite-group flow transport is proved internally; Tutte’s theorem is historical provenance rather than an unresolved logical premise.

## 2. Five-support strengthening

An indexed five-support cover is equivalently a root-valued flow

`E(G) → R₅ ⊂ E₅`.

Above a Fano flow, rank-three compatibility always gives a compatible eight-support root lift. The complete fixed-lift target asks for a homomorphism from the full cycle-face dual triangulation to the five-coordinate half-cube. The older quotient criterion through the global support-colour graph is only the factorable subroute.

The global five-support theorem remains open.

Read:

1. [`five-support/root-flow-lifting.md`](five-support/root-flow-lifting.md);
2. [`five-support/surfaces-and-halfcube.md`](five-support/surfaces-and-halfcube.md);
3. [`five-support/gauge-and-reconfiguration.md`](five-support/gauge-and-reconfiguration.md);
4. [`five-support/cuts-four-poles-and-routing.md`](five-support/cuts-four-poles-and-routing.md);
5. [`five-support/holonomy-defects-and-atoms.md`](five-support/holonomy-defects-and-atoms.md);
6. [`five-support/frontier-localisation.md`](five-support/frontier-localisation.md);
7. [`five-support/equivalent-formulations-and-proof-families.md`](five-support/equivalent-formulations-and-proof-families.md);
8. [`five-support/finite-laboratories-and-certificates.md`](five-support/finite-laboratories-and-certificates.md).

Programme B1 and later proof-development checkpoints are not consumed by the present Programme A intake.

## 3. Current five-support frontier

The sharp endpoint is graph-level localization and composition of full-rank route-locked defects.

- nonzero curvature gives a support-minimal common-cut witness with odd terminal parity;
- zero curvature gives an eight-state affine potential;
- neither output has yet been converted universally into a bounded replacement, smaller separator, transition split, or gluing theorem.

See [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md).

## 4. Provenance and control

- [`MATHEMATICAL_ARCHITECTURE.md`](MATHEMATICAL_ARCHITECTURE.md) — natural project architecture;
- [`THEOREM_DEPENDENCY_MAP.md`](THEOREM_DEPENDENCY_MAP.md) — theorem and obligation graph;
- [`CURRENT_BEST.md`](CURRENT_BEST.md) — compact mathematical state;
- [`PROGRAMME_A_INTEGRATION_MAP.md`](PROGRAMME_A_INTEGRATION_MAP.md) — exact A0–A10 checkpoint and destination map;
- [`PROGRAMME_A_ASSURANCE_BOUNDARY.md`](PROGRAMME_A_ASSURANCE_BOUNDARY.md) — proof, audit, Lean, and publication boundaries;
- [`PROGRAMME_A_INTEGRATION_MANIFEST.md`](PROGRAMME_A_INTEGRATION_MANIFEST.md) — exact intake and isolation manifest;
- [`CHAPTER_PROVENANCE.md`](CHAPTER_PROVENANCE.md) — five-support chapter provenance;
- [`MIGRATION_LEDGER.md`](MIGRATION_LEDGER.md) — retired five-support source migration;
- [`SUPERSESSION_MAP.md`](SUPERSESSION_MAP.md) — controlling corrections;
- [`FORMAL_STATUS.md`](FORMAL_STATUS.md) — global assurance boundary.

## 5. Assurance

Programme A is Curator-integrated authorial mathematics. It has not yet passed its dedicated independent audit and is not end-to-end Lean verified.

Current-best inclusion does not create manuscript, peer-review, publication, release, arXiv, DOI, or timestamp status.