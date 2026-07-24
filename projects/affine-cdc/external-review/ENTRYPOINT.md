# External review entrypoint — AffineCDC five-support frontier

## 1. The problem

The goal is:

> Every finite bridgeless multigraph has a cycle double cover using at most five indexed even subgraphs.

The theorem is not independently accepted.

On a loopless cubic graph, five supports are encoded by roots

$$
R_5=\{ij:1\le i<j\le5\}\subset E_5,
$$

with each edge in two supports and the three incident roots forming a support triangle.

## 2. Current mathematical position

Substantial pieces are independently supported:

- root-flow semantics;
- one-cross reduction;
- finite boundary/route and Morse tables;
- selected seam/genealogy interfaces;
- general multigraph outer shell, conditional on a cubic theorem;
- source-fidelity and OR1 packets in their exact scopes;
- component-channel local arithmetic and explicit positive models.

The former v9 general component-chain theorem is **not** an active proof component. Independent audit

`audit/affine-cdc-component-chain-v1@a4f20f05532c307a3a8f9d98ac4c5162e7b8ad57`

found material false scope: a shortest chain between two distinguished terminal paths can contain a third terminal path internally. The first contraction can split the original distinguished terminal darts, destroying the inherited path.

## 3. Exact failed candidate

- RL source: `02b37476198e9eaa2b4cd8d2a2edd76782bdcd49`;
- PDL reconstruction: `e36ba22f09e3a9fc6358f3b03615f8fde6c00d96`;
- independent audit: `a4f20f05532c307a3a8f9d98ac4c5162e7b8ad57`.

The source and reconstruction remain valuable provenance. Their universal component-chain, co-root/zero totality and end-to-end induction claims are failed candidates.

## 4. What survives independently

Audit `a4f20f05...` independently verified:

- channel parity and the unique inactive triangle;
- all active/inactive and active/active local root-NNI rows;
- the equal-endpoint root branch alternatives;
- all eighty-four final two-terminal matching configurations;
- the co-root `6-7` route-changing model;
- the zero-parent Heawood `H_35` model.

These are exact local theorems/models, not a universal chain theorem.

## 5. New central review problem

The controlling open interface is:

`AC-FRONTIER-COMPONENT-CHAIN-TERMINAL-EXHAUSTION`.

A repair must prove one of:

1. every co-root and zero-parent application has exactly two terminal path components and all other nontrivial channel components are closed;
2. a generalized contraction theorem handles internal terminal paths while preserving the distinguished terminal darts and paths;
3. a different source-faithful singular-parent return closes both fibres.

## 6. Permanent witnesses

Reviewers must read `COUNTEREXAMPLE_AND_SUPERSESSION_LEDGER.md`, especially:

- fixed-boundary versus literal-parent failure;
- inherited-flow discontinuity;
- old SCC/no-sink rank failures;
- `Omega` exterior-switch defect;
- `Xi` same-arc equal-face witness;
- zero-parent omission;
- third-terminal-path component-chain witness.

## 7. Reading order

1. this file;
2. `MATHEMATICAL_SPINE.md`;
3. `COMPONENT_CHAIN_REVIEW_PACKET.md`;
4. `COUNTEREXAMPLE_AND_SUPERSESSION_LEDGER.md`;
5. `FINITE_CERTIFICATE_MANIFEST.md`;
6. `QUESTIONS_FOR_EXTERNAL_REVIEWERS.md`;
7. `REPOSITORY_AND_BRANCH_AUTHORITY_MAP.md`.

## 8. Most valuable external contribution

The priority is a smallest exact proof or counterexample for terminal-component exhaustion or generalized internal-terminal contraction. Broad plausibility, local row verification alone or another positive model does not close the interface.