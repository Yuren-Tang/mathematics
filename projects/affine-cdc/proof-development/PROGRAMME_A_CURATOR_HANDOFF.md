# CURATION-HANDOFF — AffineCDC Programme A

**Project:** AffineCDC  
**Prepared by:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Authority basis:** research-workbench issue #37; persistent proof-development policy; AC-PDL charter; user instruction to transmit mature proof checkpoints to `MATH-CUR`  
**Live source branch:** `Yuren-Tang/mathematics:proof-development/affine-cdc-rigour-v1`  
**Immutable source checkpoint SHA:** `8bee16780b549f51e1f29343671a059961ec4172`  
**Included packet/file range:** `projects/affine-cdc/proof-development/OBLIGATION_DAG.md` and `AC_PD_A0_*.md` through `AC_PD_A10_*.md` at the immutable checkpoint  
**Controlling canonical base:** `Yuren-Tang/mathematics:main@960c92b7ff231c78b387894149779083060a75eb`  
**Packet classification:** `PROOF-DEVELOPMENT / PROGRAMME-A / READY-FOR-CURATOR`  
**Mathematical completeness:** `COMPLETE` at the authorial paper-proof level  
**Independent-review state:** not independently audited  
**Reliability/trust classification:** coherent proof-development checkpoint; exact theorem and assurance boundaries explicit; no claim of audit, peer review, or end-to-end formal verification  
**Live branch may continue beyond checkpoint:** yes; later Programme B work is excluded unless separately handed off  
**Staging authorized:** yes, on a dedicated Curator branch only  
**Merge/default-branch authority:** no unless separately stated by the responsible authority  
**Next disposition receiver:** `Mathematics — Curator` (`MATH-CUR`), then `AffineCDC — Director` for any canonical movement

## 1. Intake objective

Integrate the completed Programme A theorem spine into the natural rolling AffineCDC corpus while preserving:

- exact statement scope and hypotheses;
- the theorem/proof-obligation dependency map;
- the distinction between intrinsic loop-aware parity and the loopless companion incidence representation;
- source, formal, audit, manuscript, release, and publication boundaries;
- the distinction between the compatibility image and retained graph/dart support data;
- the even-cover-first collapse architecture;
- exact occurrence multiplicity under repeated and empty supports.

The intake is mathematical curation and architecture work, not independent audit or default-branch promotion.

## 2. Accepted mathematical statements in the packet

The packet gives complete authorial proofs of the following chain.

1. **Foundational semantics.** Finite-active-edge multigraphs, cuts, intrinsic boundary parity, cut-even supports, circuits, loops, components, and indexed/multiset multiplicity.
2. **Loop reduction.** Exact cut preservation and equivalence of CDC witnesses between a graph and its loopless core, with two forced singleton occurrences per loop.
3. **Cubic expansion.** Finite loopless cubic port-cycle expansion, including degree-two parallel fibres, component correspondence, bridgelessness, collapse recovery, and cut pullback.
4. **Binary flow boundary.** Seymour six-flow input, literal six-to-eight range inclusion, modular reduction, internal equal-order finite-abelian-group flow counting, and the loopless characteristic-two adapter.
5. **Affine obstruction.** Local affine-family torsors, pair complex, quotient equation, equilibrium-stress dual, and retained source-data boundary.
6. **Rank-three compatibility.** Canonical edge-quotient quadratics, local Fano Lagrangians, characteristic torsors, totally singular edge diagonal, and automatic global intersection.
7. **Graph-level extraction.** Eight point-indexed edge supports, local vertex evenness, and exact twofold edge occurrence.
8. **Parity bridge.** Exact equivalence of once-per-edge vertex parity, intrinsic boundary parity, and cut parity on the loopless graph.
9. **Collapse.** Memberwise preservation of cut parity and exact original-edge multiplicity; no circuit projection claim.
10. **Circuit decomposition.** Terminating finite decomposition of each cut-even support and exact preservation of total occurrence multiplicity.
11. **Final theorem.** Every multigraph with finite active edge set and no singleton cut has a cycle double cover, without connectedness, simplicity, looplessness, or finiteness of the ambient vertex carrier.

## 3. Corrections and exclusions

### Corrections to retain

- A0 owns circuit semantics and characterization; A9 owns finite decomposition.
- Intrinsic half-edge parity counts loops twice. The current once-per-edge incidence API is loopless only.
- Tutte's equal-order theorem is provenance rather than an external logical premise; A3 proves the required counting statement internally.
- The pair complex is the complete compatibility image but does not retain graph, dart, or indexed-support semantics.
- Collapse preserves cut-even supports and occurrence multiplicity, not circuits.
- Equal support values at different indices remain distinct occurrences.
- The weakest proved theorem hypotheses are finite active edge set and no singleton cut.

### Exclusions

- no later Programme B or Research Lead branch delta;
- no claim that the global five-support theorem is proved;
- no claim of independent audit;
- no claim of end-to-end Lean verification;
- no manuscript, release, DOI, priority-attestation, or publication action;
- no movement or rewrite of `main`;
- no silent replacement of the current formal-status or provenance records.

## 4. Source status

The sole external non-elementary logical input is:

P. D. Seymour, “Nowhere-zero 6-flows”, *Journal of Combinatorial Theory, Series B* **30** (1981), 130–135, DOI `10.1016/0095-8956(81)90058-7`.

No indispensable source locator remains unresolved for the logical chain. Tutte's historical equal-order existence/counting provenance should be retained, but the proof no longer depends on an exact primary-page locator.

## 5. Formal status and exact refs

The companion formal anchor inspected is:

`Yuren-Tang/affine-cdc@ebd7098a7a8b824e8c0a511d3c71f61705672aa8`.

It machine-checks substantial internal slices, including local family classification, gluing, indexed dart supports, exact two-point coverage, partner/rotation structure, graph-level support extraction, generic even-support decomposition, and a cubic-flow CDC macro-Port.

The invariant A0–A10 spine at `8bee1678…` is not thereby an end-to-end checked theorem. The Curator should preserve the exact distinction stated in A10.

## 6. Permitted canonical destinations

On a dedicated Curator branch, the packet may be integrated into:

- `projects/affine-cdc/MATHEMATICAL_ARCHITECTURE.md`;
- `projects/affine-cdc/THEOREM_DEPENDENCY_MAP.md`;
- `projects/affine-cdc/FORMAL_STATUS.md`;
- `projects/affine-cdc/PROVENANCE.md` or the controlling provenance map;
- `projects/affine-cdc/reduction/outer-shell-and-binary-flow.md`;
- `projects/affine-cdc/reduction/even-cover-and-collapse.md`;
- `projects/affine-cdc/core/affine-incidence-and-obstruction.md`;
- `projects/affine-cdc/core/rank-three-fano-compatibility.md`;
- a retained proof-development/provenance namespace if full dossiers should remain intact.

The Curator determines the natural exposition and may preserve the dossiers as a proof family rather than copying them mechanically into every active chapter.

## 7. Alternative and historical material to preserve

Preserve, where useful and correctly classified:

- the pair-complex, quotient-sheaf, and stress-dual formulations;
- the quadratic-Lagrangian, cross-bit, and support-parity views as resolutions of one compatibility mechanism;
- the explicit dart rotation as additional structure, even though the final proof decomposes only after collapse;
- the companion Lean macro-Port as a formal projection with a different internal factorization;
- historical Tutte provenance and prior architecture notes that remain evidentially valuable.

Do not treat alternate presentations as separate stronger theorems unless their extra hypotheses and outputs are explicit.

## 8. Curator success test

The intake succeeds when:

1. the immutable checkpoint `8bee1678…` remains the exact consumed source;
2. the natural theorem statement and all hypotheses are preserved;
3. each A0–A10 arrow has a recoverable proof/provenance pointer;
4. all seven material boundary corrections are visible in the active corpus;
5. Seymour 1981 is the sole external non-elementary logical input;
6. authorial completion, audit, formalization, manuscript, and publication states remain distinct;
7. later Programme B work is excluded;
8. no default-branch movement is implied by staging;
9. any mathematical defect is returned as an exact AC-PDL repair unit.

## 9. Genuine stop conditions

Stop and return rather than guessing if integration reveals:

- a contradiction between two A0–A10 statements;
- a hidden hypothesis required by the final theorem;
- a source statement materially weaker than A3 uses;
- a formal/paper correspondence defect that changes the mathematical claim;
- a canonical architecture decision requiring destructive supersession of valuable proof-family material;
- a need to consume a later live-branch commit not named in this packet.

Routine exposition, deduplication, dependency linking, and status synchronization do not require a stop.

## 10. Curator verification checklist

- [ ] live branch and immutable checkpoint distinguished
- [ ] exact checkpoint reachable
- [ ] packet range explicit
- [ ] canonical base resolved
- [ ] active writer and later-delta exclusion explicit
- [ ] theorem scope and hypotheses preserved
- [ ] authorial completeness and independent-review state preserved
- [ ] source and formal boundaries preserved
- [ ] destination and proof-family map explicit
- [ ] no destructive branch/history operation
- [ ] no default-branch movement implied
- [ ] GitHub TeX normalized where material is integrated
