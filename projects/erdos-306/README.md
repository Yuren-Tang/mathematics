# Erdős 306 — rolling current-best mathematical corpus

## 1. Current state

This directory is the Curator-maintained mathematical architecture for the proof of Erdős Problem 306.

The current theorem is:

> A positive rational number is a finite sum of reciprocals of distinct squarefree semiprimes if and only if its reduced denominator is squarefree.

The immutable released formal theorem proves the sufficiency direction in the community finite-tuple formulation. The elementary necessity direction and the natural set-valued statement are retained here as mathematical architecture.

**Curator candidate:** `curation/erdos-306-proof-architecture-v1`  
**Exact branch base:** `Yuren-Tang/mathematics:main@960c92b7ff231c78b387894149779083060a75eb`

This corpus is organized by mathematical object and dependency, not by:

- released Lean file order;
- frozen-refactor module order;
- proof-development dossier order;
- manuscript section order.

## 2. Exact source authorities

1. **Immutable released formal authority**  
   `Yuren-Tang/erdos-306:v0.0.3@4582185de1e0e27416e9362e0cc7943c3d2fb4fe`.

2. **Frozen refactor / architectural comparison source**  
   `Yuren-Tang/erdos-306:codex/pushlinter@e55ef359a8b98525f0bac6c7a510fcad94469bff`.

3. **Authorial proof-development source**  
   `Yuren-Tang/erdos-306:proof-development/e306-rigour-v1@cecd3c351302e49577d180ebf42ad7fa784508dc`.

4. **Read-only manuscript projection**  
   `Yuren-Tang/erdos-306:paper/arxiv-v1-revision-v3@94615a5c860be9ce04c2be0153759a4e66fc25ab`.

These repositories are cross-repository sources and are pinned by exact SHA. They are not Git ancestors of this curation branch.

## 3. Reading order

1. [`CURRENT_BEST.md`](CURRENT_BEST.md)
2. [`MATHEMATICAL_ARCHITECTURE.md`](MATHEMATICAL_ARCHITECTURE.md)
3. [`THEOREM_DEPENDENCY_MAP.md`](THEOREM_DEPENDENCY_MAP.md)
4. [`ANALYTIC_INTERFACE_AND_PROVIDERS.md`](ANALYTIC_INTERFACE_AND_PROVIDERS.md)
5. [`CONTROL_AND_GLOBAL_LOCALISATION.md`](CONTROL_AND_GLOBAL_LOCALISATION.md)
6. [`MASS_VARIANCE_AND_DENOMINATOR_FAMILY.md`](MASS_VARIANCE_AND_DENOMINATOR_FAMILY.md)
7. [`FOURIER_POSITIVITY_AND_ARITHMETIC_CLOSURE.md`](FOURIER_POSITIVITY_AND_ARITHMETIC_CLOSURE.md)
8. [`PROOF_FAMILIES_AND_HANDOFFS.md`](PROOF_FAMILIES_AND_HANDOFFS.md)
9. [`SOURCE_PROVENANCE_AND_SUPERSESSION.md`](SOURCE_PROVENANCE_AND_SUPERSESSION.md)
10. [`FINITE_CERTIFICATES_AND_RELIABILITY.md`](FINITE_CERTIFICATES_AND_RELIABILITY.md)
11. [`OPEN_OBLIGATIONS_AND_STATUS.md`](OPEN_OBLIGATIONS_AND_STATUS.md)
12. [`MANUSCRIPT_CONSUMER_CHECKPOINT.md`](MANUSCRIPT_CONSUMER_CHECKPOINT.md)
13. [`E306_CUR_ARCH_INTEGRATION_MANIFEST.md`](E306_CUR_ARCH_INTEGRATION_MANIFEST.md)

## 4. Controlling distinctions

### Released theorem authority versus human proof architecture

The release is Lean-closed relative to exactly two nonstandard Rosser–Schoenfeld assumptions. The preferred human article backend uses PNT plus Abel summation. The two backends meet only at the construction-facing analytic interface.

No status transfers silently:

- the PNT proof is not part of the archived release;
- the frozen refactor's structural analytic axioms are not the v0.0.3 authority;
- a human proof-development derivation is not automatically independently reviewed;
- a manuscript assertion is not proof authority merely because it mirrors the Lean construction.

### Symbolic mechanism versus finite certificate

The current mathematical architecture uses symbolic constants and a non-circular dependency order. Concrete released values remain exact finite certificates, not intrinsic invariants.

### Principle nodes versus handoff nodes

Every major layer is expressed as:

```text
natural principle
-> concrete construction handoff
-> exact downstream consumer.
```

This prevents implementation modules, manuscript chapters, or historical names from becoming the mathematical ontology.

## 5. Global assurance

Current classification:

`CURATOR-INTEGRATED / RELEASE-AUTHORITY-PRESERVED / HUMAN-PROOF-ARCHITECTURE-SYNTHESIZED / MANUSCRIPT-CONSUMER-READY / SOURCE-GATES-EXPLICIT`.

This is not:

- an independent rerun of Lean or CI;
- independent mathematical review of every PDL unit;
- human certification of the two Rosser–Schoenfeld transcriptions against the publisher scan;
- approval of REV3 or any later manuscript;
- a release, publication, arXiv, DOI, novelty, or priority disposition.
