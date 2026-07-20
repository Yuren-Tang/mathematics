# Complete Cycle Double Cover theorem

This directory is the current rigorous Programme A surface for the complete Cycle Double Cover theorem.

It integrates the immutable proof-development checkpoint

`proof-development/affine-cdc-rigour-v1@8bee16780b549f51e1f29343671a059961ec4172`

into the natural current-best corpus. Only A0–A10 are consumed. Programme B1 and every later proof-development commit are outside this intake.

## Natural theorem

> Every multigraph with finite active edge set and no singleton cut has a finite circuit double cover.

Here:

- loops and parallel edge objects are allowed;
- the ambient vertex carrier may be infinite;
- isolated vertices and disconnected components are allowed;
- a circuit is a nonempty inclusion-minimal finite cut-even support;
- every active edge object occurs in exactly two circuit occurrences.

For finite-active multigraphs, “no singleton cut” is equivalent to “no nonloop bridge”. The cut formulation is used because it interacts directly with intrinsic parity and collapse.

## Reading order

1. [`foundations-expansion-and-flow.md`](foundations-expansion-and-flow.md)  
   Multigraph and multiplicity semantics, intrinsic parity, circuit characterization, loop deletion, port-cycle cubic expansion, and the binary eight-flow boundary.

2. [`affine-compatibility-and-extraction.md`](affine-compatibility-and-extraction.md)  
   The affine pair complex, rank-three quadratic-Lagrangian compatibility, graph/dart retained data, indexed even-support extraction, and the loopless parity adapter.

3. [`collapse-decomposition-and-assembly.md`](collapse-decomposition-and-assembly.md)  
   Cut-even collapse, exact occurrence transport, terminating circuit decomposition, loop reinsertion, and final theorem assembly.

## Proof-development provenance

The exact authorial dossiers remain under [`../proof-development/`](../proof-development/):

- `AC_PD_A0_FOUNDATIONAL_SEMANTICS.md` through `AC_PD_A10_COMPLETE_CDC_ASSEMBLY.md`;
- `OBLIGATION_DAG.md`.

The canonical source-to-chapter and checkpoint map is [`../PROGRAMME_A_INTEGRATION_MAP.md`](../PROGRAMME_A_INTEGRATION_MAP.md).

## Logical external input

The sole external non-elementary logical input is Seymour’s nowhere-zero six-flow theorem.

The equal-order finite-abelian-group transport needed to pass from a nowhere-zero `Z/8Z` flow to a nowhere-zero `F₂³` flow is proved internally by a spanning-forest kernel count and inclusion–exclusion. Tutte’s equal-order theorem is retained as historical provenance, not as an unresolved logical premise.

## Assurance boundary

This corpus is a Curator integration of an authorial proof-development checkpoint. It is not:

- independent mathematical audit;
- end-to-end Lean verification;
- manuscript acceptance or revision;
- peer review or publication approval;
- release, arXiv, DOI, or timestamp action.

See [`../PROGRAMME_A_ASSURANCE_BOUNDARY.md`](../PROGRAMME_A_ASSURANCE_BOUNDARY.md) and [`../FORMAL_STATUS.md`](../FORMAL_STATUS.md).