# AffineCDC theorem dependency map

This map separates the complete Cycle Double Cover theorem from the open five-support strengthening.

## 1. Complete theorem DAG

```text
A0  finite-active multigraph, cut, intrinsic parity, circuit, and occurrence semantics
├── A1  loop deletion and exact two-occurrence reinsertion
└── A2  loopless port-cycle cubic expansion and collapse data
    └── A3  Seymour six-flow boundary and internal order-eight group-flow transport
        └── A4  affine pair complex, quotient equation, and stress obstruction
            └── A5  rank-three quadratic-Lagrangian compatibility
                └── A6  graph/dart indexed even-support extraction
A0 + A6 ── A7  loopless vertex/boundary/cut parity equivalence
A2 + A6 + A7 ── A8  cut-even collapse and exact occurrence transport
A0 + A8 ── A9  terminating finite circuit decomposition
A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 ── A10 final theorem
```

The preferred integrated chapters are:

- [`complete-cdc/foundations-expansion-and-flow.md`](complete-cdc/foundations-expansion-and-flow.md): A0–A3;
- [`complete-cdc/affine-compatibility-and-extraction.md`](complete-cdc/affine-compatibility-and-extraction.md): A4–A7;
- [`complete-cdc/collapse-decomposition-and-assembly.md`](complete-cdc/collapse-decomposition-and-assembly.md): A8–A10.

The exact unit checkpoints and source destinations are in [`PROGRAMME_A_INTEGRATION_MAP.md`](PROGRAMME_A_INTEGRATION_MAP.md).

## 2. Foundational outputs

A0 exports:

- finite-active multigraph and active-vertex reduction;
- singleton cut/bridge equivalence;
- intrinsic half-edge boundary parity;
- cut-even/boundary-even equivalence;
- circuit characterization;
- indexed and multiset occurrence semantics;
- componentwise and degenerate cases.

A1 exports exact equivalence between a graph and its loopless core at the level of cuts, core circuits, CDC existence, and forced singleton-loop occurrences.

## 3. Expansion and flow outputs

A2 exports:

- finite loopless cubic expansion `H`;
- collapse map `π` and injective original-edge lift `λ`;
- internal/external edge partition;
- degree-two parallel fibres;
- component correspondence and exact size formulae;
- no-singleton-cut preservation;
- cut pullback `δ_H(π⁻¹(S)) = λ(δ_G(S))`.

A3 consumes Seymour’s six-flow theorem and proves:

- literal six-to-eight range inclusion;
- modular reduction to `Z/8Z`;
- flow-kernel cardinality by spanning forests;
- nowhere-zero flow count by inclusion–exclusion;
- equal-order transfer to `F₂³`;
- exact loopless characteristic-two orientation adapter.

Only Seymour is an external non-elementary logical input.

## 4. Affine compatibility outputs

A4 constructs:

- edge quotient planes `Q_e`;
- incidence space `E_f`;
- local torsor `κ+L_vert`;
- edge diagonal `L_edge`;
- pair complex `P_f`;
- obstruction class `[κ]`;
- quotient equation `δ_fm=c_f`;
- equilibrium-stress criterion.

A5 proves:

- canonical anisotropic quadratic forms on rank-three quotients;
- local Fano Lagrangians;
- local families as characteristic torsors;
- total singularity of the edge diagonal;
- characteristic-torsor intersection;
- automatic global compatibility.

The pair complex captures compatibility but does not replace retained graph/dart data.

## 5. Support extraction and parity outputs

A6 uses the compatible edge lines and retained graph/dart pairing to produce an `F₂³`-indexed family `(F_s)` with:

- local once-per-edge vertex parity;
- exact edge occurrence multiplicity two;
- retained empty and repeated support occurrences.

A7 proves on loopless graphs:

`once-per-edge vertex-even ⇔ intrinsic boundary-even ⇔ cut-even`.

The adapter is intentionally not extended to loops.

## 6. Collapse and decomposition outputs

A8 projects each support through `λ` and proves:

- memberwise cut-evenness downstairs;
- exact original-edge occurrence transport;
- harmless empty and repeated images;
- no assertion that circuits project to circuits.

A9 proves:

- every finite cut-even support contains a circuit;
- strict-cardinality terminating decomposition;
- exact edgewise `0/1` count within one support;
- global occurrence preservation after concatenating indexed decompositions.

## 7. Final theorem

A10 assembles:

```text
finite-active no-singleton-cut multigraph
→ loopless core
→ cubic expansion
→ F₂³ flow
→ compatible affine family
→ indexed intrinsic even cover upstairs
→ indexed intrinsic even cover downstairs
→ circuit double cover of the core
→ circuit double cover after loop reinsertion
```

The output is a finite indexed family, equivalently a finite multiset, of circuits covering every active edge object exactly twice.

## 8. Assurance dependencies

The proof states are authorial:

- A0–A9: `COMPLETE-DRAFT`;
- A10 aggregate: `READY-FOR-CURATOR` at the immutable source checkpoint;
- integrated candidate: Curator-integrated authorial paper-proof.

Independent audit, Lean verification, manuscript acceptance, peer review, release, arXiv, DOI, and publication are separate axes. See [`PROGRAMME_A_ASSURANCE_BOUNDARY.md`](PROGRAMME_A_ASSURANCE_BOUNDARY.md).

## 9. Five-support dependency tree

The global five-support theorem remains open. Its current active corpus begins with root-flow equivalences, then passes through surfaces, gauge/reconfiguration, four-pole routing, holonomy/defects, and localization/composition.

Programme B1 and later proof-development checkpoints are not consumed by Programme A. The active five-support dependency details remain in [`five-support/README.md`](five-support/README.md) and [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md).