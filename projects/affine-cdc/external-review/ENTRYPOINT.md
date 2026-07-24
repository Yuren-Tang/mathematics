# External review entrypoint — AffineCDC and the five-support problem

## 1. The problem

A cycle double cover is a multiset of cycles/even subgraphs in which every edge occurs exactly twice. The five-support target asks for at most five indexed members.

The current global goal is:

> **Five-support / 5-CDC goal.** Every finite bridgeless multigraph has a cycle double cover using at most five indexed even subgraphs.

The theorem is **not independently accepted** in this corpus.

## 2. Root-flow language

On a loopless cubic graph, five indexed supports are encoded by roots

$$
R_5=\{ij:1\le i<j\le5\}
$$

inside the even-weight space $E_5\subset\mathbf F_2^5$. An edge labelled $ij$ belongs to supports $i$ and $j$. The three roots at a cubic vertex form the three edges of a triangle on three support indices.

Thus five-support existence on cubic graphs is equivalent to an $R_5$-valued nowhere-zero flow satisfying the root-triangle local law.

## 3. What is already independently supported

- exact root-flow/five-support semantics;
- one-cross structural reduction;
- finite boundary-route and local Morse tables;
- selected seam and genealogy subinterfaces;
- the general multigraph outer shell, conditional on the cubic theorem;
- B2/B8 source-fidelity and packet accounting;
- OR1 fixed-lift/fixed-fibre orientation obstruction subject to six named repairs;
- several exact counterexamples to old proof shortcuts.

See `../GLOBAL_REBASELINE_V2_ASSURANCE_MATRIX.md`.

## 4. Current authorial proof proposal

The active proposal is the v9 fixed-channel component-chain route:

```text
root-flow semantics
→ one-cross reduction and finite local core
→ forward root-NNI history to one cancellation
→ solve the actual smaller target
→ one inverse pop and complete prescribed-parent state
→ fixed-channel component chain for co-root/zero parents
→ literal parent and stored-prefix return
→ ordinary induction
→ independently accepted outer shell.
```

The new load-bearing mechanism is explained in `COMPONENT_CHAIN_REVIEW_PACKET.md`.

## 5. Current assurance state

- component-chain source: RL authorial at `02b37476198e9eaa2b4cd8d2a2edd76782bdcd49`;
- PDL reconstruction: active issue #80;
- focused independent audit: active issue #81;
- current corpus status: mixed assurance, not theorem acceptance.

## 6. Known counterexamples

Do not review the proposal without first reading:

`COUNTEREXAMPLE_AND_SUPERSESSION_LEDGER.md`.

Important failures include:

- literal-parent reinsertion from boundary equivalence;
- horizontal/SCC progress without a physical rank;
- exterior-switch failure of the local `Omega` formula;
- the same-arc equal-face counterexample to `Xi` totality;
- omission of the zero-parent `(0,2,2)` row;
- arbitrary terminal recolouring, generic connectivity and track-erasure shortcuts.

## 7. Recommended reading order

1. this file;
2. `MATHEMATICAL_SPINE.md`;
3. `COMPONENT_CHAIN_REVIEW_PACKET.md`;
4. `COUNTEREXAMPLE_AND_SUPERSESSION_LEDGER.md`;
5. `FINITE_CERTIFICATE_MANIFEST.md`;
6. `QUESTIONS_FOR_EXTERNAL_REVIEWERS.md`;
7. `REPOSITORY_AND_BRANCH_AUTHORITY_MAP.md`.

Only then consult the exact source files listed in those documents.

## 8. What feedback is most valuable

The highest-value response is not a verdict on the whole conjecture. It is a proof or counterexample for one of:

1. inherited physical-chain fidelity after one contraction;
2. the final terminal-matching change;
3. the co-root marked-arc corollary;
4. the zero-parent terminal-path corollary;
5. end-to-end preservation of literal parent/cap/dart/prefix data.

A smallest exact witness is preferable to a broad plausibility judgment.