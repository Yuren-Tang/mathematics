# AffineCDC current mathematical state

## 1. Complete result line

Programme A supplies a complete authorial paper-proof of:

> Every multigraph with finite active edge set and no singleton cut has a finite circuit double cover.

Equivalently, no nonloop active edge is a bridge. The theorem allows loops, parallel edge objects, disconnected components, isolated vertices, and an arbitrary ambient vertex carrier.

The exact proof chain is:

1. intrinsic multigraph, cut, circuit, and indexed-occurrence semantics;
2. exact loop deletion;
3. finite loopless cubic port-cycle expansion;
4. nowhere-zero `F₂³` flow;
5. affine pair complex and rank-three characteristic-torsor compatibility;
6. graph/dart indexed even-support extraction;
7. loopless vertex-to-cut parity bridge;
8. cut-even collapse with exact occurrence transport;
9. one terminating circuit decomposition downstairs;
10. exact two-occurrence loop reinsertion.

The controlling proof chapters are under [`complete-cdc/`](complete-cdc/).

## 2. Logical source boundary

Seymour’s nowhere-zero six-flow theorem is the sole external non-elementary logical input.

Programme A proves equal-order finite-abelian-group transport internally by:

- spanning-forest flow-kernel counting;
- inclusion–exclusion for nowhere-zero flows;
- transport from `Z/8Z` to `F₂³` by equality of group order.

Tutte’s theorem is historical provenance and no longer an unresolved logical source gate.

## 3. Load-bearing clarifications

1. Circuit characterization and finite circuit decomposition are distinct interfaces.
2. Intrinsic half-edge boundary parity is loop-aware; once-per-edge vertex parity is loopless only.
3. The pair complex captures compatibility but not graph/dart/indexed-support semantics.
4. Collapse transports cut-even supports and occurrence multiplicity, not circuits.
5. Equal support values at distinct indices remain separate occurrences.
6. The natural hypotheses do not include connectedness, simplicity, looplessness, ambient-vertex finiteness, or absence of isolated vertices.

## 4. Programme A source state

- canonical base: `main@960c92b7ff231c78b387894149779083060a75eb`;
- immutable source: `proof-development/affine-cdc-rigour-v1@8bee16780b549f51e1f29343671a059961ec4172`;
- integrated scope: A0–A10 and Programme A obligation/provenance ledger;
- excluded scope: B1 checkpoint `778b09ac8260192e022f512f24cdef1d04871f37` and every later PDL commit.

The exact dossiers remain in `proof-development/` as authorial provenance. See [`PROGRAMME_A_INTEGRATION_MAP.md`](PROGRAMME_A_INTEGRATION_MAP.md).

## 5. Five-support strengthening

The open strengthening asks for five indexed even supports, equivalently a root-valued flow into the ten roots of `E₅`.

The complete fixed-lift object is the full cycle-face dual triangulation; the global support-colour quotient gives only the factorable subroute.

The global five-support theorem remains open. Programme A makes no claim about Programme B mathematics.

## 6. Five-support durable blocks and frontier

The active corpus records mature root-flow, surface, gauge, reconfiguration, four-pole, holonomy, defect, and atom results. Controlling negative boundaries remain:

- a fixed Fano flow may fail to admit five supports;
- the colour quotient is not the complete fixed-lift object;
- `K₆`-free does not imply a half-cube map;
- a bad fixed-flow fibre does not imply a bad graph;
- arbitrary binary-cycle switches are not single horizontal adjacencies;
- route-lock implies neither a graph two-cut nor automatic flatness;
- finite census does not prove universal closure.

The sharp endpoint remains localization and composition of full-rank route-locked defects. See [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md).

## 7. Assurance state

Programme A is:

`CURATOR-INTEGRATED / AUTHORIAL PAPER-PROOF COMPLETE`.

It is not yet independently audited and is not end-to-end Lean verified. No manuscript, peer-review, publication, release, arXiv, DOI, or timestamp status is created.

See [`PROGRAMME_A_ASSURANCE_BOUNDARY.md`](PROGRAMME_A_ASSURANCE_BOUNDARY.md) and [`FORMAL_STATUS.md`](FORMAL_STATUS.md).

## 8. Reading order

- complete theorem: [`complete-cdc/README.md`](complete-cdc/README.md);
- architecture: [`MATHEMATICAL_ARCHITECTURE.md`](MATHEMATICAL_ARCHITECTURE.md);
- theorem graph: [`THEOREM_DEPENDENCY_MAP.md`](THEOREM_DEPENDENCY_MAP.md);
- exact Programme A map: [`PROGRAMME_A_INTEGRATION_MAP.md`](PROGRAMME_A_INTEGRATION_MAP.md);
- active surface: [`ACTIVE_MATHEMATICAL_SURFACE.md`](ACTIVE_MATHEMATICAL_SURFACE.md);
- five-support corpus: [`five-support/README.md`](five-support/README.md);
- exact frontier: [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md).