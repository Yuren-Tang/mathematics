# AffineCDC note map and status ledger

This ledger assigns every active note a mathematical role.  It is not a chronology.  A later invariant formulation may control the architecture even when an earlier note remains the verified or more detailed implementation record.

## Status vocabulary

- **Core theorem dossier** — belongs to the direct compatibility-to-CDC chain.
- **Equivalent presentation** — gives the same core object in another language.
- **Refinement** — strengthens or makes precise an earlier statement.
- **Specialization/example** — instantiates a general theorem.
- **Downstream theorem** — follows from the core or from its homogeneous reduction but is not needed for compatibility.
- **Generalization program** — abstracts the construction beyond the graph problem; novelty and usefulness require external validation.
- **Archived program** — substantive older material whose source bodies are not in the current `main` tree.

Reliability labels:

- **Lean anchor** — implemented in the companion Lean repository.
- **T** — theorem-level manuscript draft; argument written, not necessarily independently audited or formalized in this presentation.
- **C** — exact finite computation or exhaustive check.
- **P** — programmatic, provisional, or conjectural.
- **A** — archived by manifest/hash; source body must be restored before detailed audit.

## A. Controlling syntheses

| File | Role | Status | Architectural decision |
|---|---|---:|---|
| `README.md` | Human entry point | — | Rewritten to state the single spine and reading order. |
| `MATHEMATICAL_ARCHITECTURE.md` | Controlling mathematical synthesis | T/P | Governs dependency and terminology; not itself a substitute for proof audit. |
| `NOTE_MAP_AND_STATUS.md` | This ledger | — | Controls the status of dossiers. |
| `PUBLICATION_PROGRAM.md` | Natural paper decomposition | P | Paper labels follow theorem blocks, not history. |
| `current-synthesis.md` | Detailed working synthesis | T/P | Retained as a rich technical map; subordinate to the controlling architecture where terminology conflicts. |
| `theory-map-v1-affine-incidence-pair.md` | First incidence-centred theory map | T | Historically decisive; refined by the pair-complex and chain-bridge notes. |

## B. Compatibility core

| File | Mathematical content | Role | Status | Deduplication decision |
|---|---|---|---:|---|
| `affine-incidence-pair-complex.md` | Pair complex \(L_{\mathrm{vert}}\oplus L_{\mathrm{edge}}\to E_f\); \(H^0\), \(H^1\), affine class; quotient and dual presentations | **Central core object** | T | Canonical rank-independent compatibility formulation. |
| `fano-quadratic-lagrangian-package.md` | Local six-dimensional quadratic space, Fano Lagrangian, characteristic torsor, legal dual configurations, support/cross-bit identity | **Canonical local rank-three theorem** | T | Absorbs separate local case tables and branching narratives. |
| `affine-lagrangian-intersection.md` | Abstract characteristic-torsor/Lagrangian intersection criterion and global application | **Canonical global rank-three theorem** | T | Main invariant proof of compatibility. |
| `fano-quadratic-transgression.md` | Sum of quotient quadratics equals outside-plane linear bit; support-boundary proof | Core lemma / equivalent proof view | T | Keep as the shortest local identity and bridge to the verified support proof; do not present as a competing foundation. |

The companion Lean repository supplies the machine-checked anchor for the original AffineCDC theorem and CDC extraction.  The invariant package above is newer and must be matched explicitly to that implementation before it inherits the same formal status.

## C. Rank hierarchy and obstruction theory

| File | Mathematical content | Role | Status | Relation |
|---|---|---|---:|---|
| `rank-three-coincidence-principle.md` | Support degree, local half-dimension, and global index all single out \(r=3\) | Structural explanation | T | Canonical explanation of exceptional rank three. |
| `higher-degree-fano-transgression.md` | All-rank degree-lowering support identity and global outside-plane parity | Positive all-rank theorem | T | Generalizes the quadratic transgression, but alone is insufficient for compatibility when \(r>3\). |
| `dual-fano-residue-theorem.md` | Complete all-rank obstruction formula via hidden planes in annihilators | **Canonical higher-rank theorem** | T/C | Controls the rank hierarchy; finite identities checked in small ranks. |
| `rank-four-cubic-directional-residue.md` | Alternating-form model, Pfaffian, cubic residue, exact rank-four obstruction | Rank-four specialization | T/C | Algebraic equation of the general dual-Fano residue. |
| `rank-four-k33-residue-example.md` | Explicit \(K_{3,3}\) flow, essential stress, one residue vertex, incompatibility | Canonical negative example | T/C | Detailed computation; should eventually be an example section, not a separate ontology. |
| `rank-four-six-vertex-dichotomy.md` | Prism compatible, \(K_{3,3}\) incompatible despite equal index data | Minimal comparative theorem | T/C | Preferred expository statement; uses the detailed \(K_{3,3}\) dossier. |
| `symplectic-vertex-plane-parity.md` | Global symplectic forms have even Lagrangian-plane parity; essential local fields can violate it | Corollary / interpretation | T | Interprets rank-four incompatibility as a descent anomaly. |

Canonical order:

\[
\text{higher-degree transgression}
\to
\text{dual-Fano residue}
\to
\text{rank-four Pfaffian}
\to
\text{six-vertex examples}.
\]

The rank-four notes are not independent general theories.

## D. Incidence-to-tensor comparison

| File | Mathematical content | Role | Status | Relation |
|---|---|---|---:|---|
| `incidence-tensor-comparison.md` | Exact cohomological comparison; constants, wedge moment, essential stresses, affine class | Canonical cohomology dictionary | T | Retain for explicit short exact sequences. |
| `chain-level-incidence-tensor-bridge.md` | Universal tension resolution and zigzag from extended quotient sheaf to tensor complex | **Canonical chain-level refinement** | T/C | Supersedes vague “reduced compression” language. |

The precise hierarchy is:

1. affine incidence-pair complex;
2. quotient-sheaf presentation;
3. extended quotient sheaf with wedge moment;
4. lifted incidence resolution;
5. tensor complex as a quotient.

Neither tensor homology nor the code flag replaces the source graph/dart structure needed for CDC extraction.

## E. Tensor, code, and torsion branch

| File | Mathematical content | Role | Status | Architectural decision |
|---|---|---|---:|---|
| `flow-tensor-datum.md` | Tensor complex, homology dictionary, constraint matroid, Schur code, harmonic quotients, torsion | Broad theorem dossier | T | The phrase “master object” is obsolete; treat as a comprehensive downstream dossier. |
| `flow-tensor-theory-foundations-v0.md` | Abstract based quotient data, index, affine/Hodge enhancements, theorem hierarchy | Generalization program | T/P | Useful foundation draft; publishability depends on recognition and payoff tests stated in the note. |
| `code-flag-schur-koszul.md` | Equivalence with nested binary code flags; mixed Schur–Koszul complex and syzygies | Dual abstract formulation | T/P | Terminology explicitly provisional; requires literature review. |
| `divided-square-exact-sequence.md` | \(0\to\Gamma\otimes K\to\ker W\to D^2\Gamma\to0\); Veronese quotient and determinant factorization | Canonical structural theorem | T | Explains basis-packing formula invariantly. |
| `coefficient-quotient-exact-sequence.md` | Functorial rank quotient and long exact tensor-homology sequence | Functorial theorem | T | Natural later section or separate note; not core P1. |
| `flow-tensor-morphisms-and-automorphisms.md` | Diagonal coalgebra, strict morphisms, code-flag automorphisms, partial maps | Foundational/categorical program | T/P | Retain as framework exploration; graph cuts still require correspondences. |
| `fano-torsion.md` | Basis-free top wedge, rigidity criterion, basis-packing expansion, cut multiplicativity | Downstream invariant theorem | T | Natural bridge between tensor exactness and decomposition. |

The abstract branch has a real theorem core, but its claim to be a new general theory remains conditional.  Before publication it needs:

1. comparison with existing Schur-product, Koszul, matroid-quotient, rigidity, and sheaf literature;
2. at least one external example not reverse-engineered from AffineCDC;
3. a theorem materially shortened or strengthened by the framework;
4. stable morphisms, especially for deletion/contraction and graph interfaces.

## F. Homogeneous graphical branch

| File | Mathematical content | Role | Status | Relation |
|---|---|---|---:|---|
| `harmonic-cut-quotients.md` | Gauge modes iff contracted support quotient carries a nowhere-zero flow–tension bicycle | **Canonical geometric interpretation of gauge code** | T | Unifies tensor dependencies, cuts, harmonic labellings, and low weights. |
| `even-gauge-code.md` | Every gauge word has even weight for rank at most three; sharp rank-four example | General graph theorem | T | Strong independent payoff of the framework. |
| `weight6-circuit-classification.md` | Exactly \(6K_2\), doubled \(K_3\), and affine-plane \(K_4\) quotient circuits | Classification theorem | T | Continues low-weight circuit programme; weight eight remains open. |
| `interface-correspondence.md` | Cycle fiber product, cographic pushout, theta interface, 2/3-edge gluing | Structural gluing theorem | T | Canonical mixed-variance/Mayer–Vietoris view. |
| `interface-line-duality.md` | Universal line \(L_S\), sewing modes versus matching obstructions | Refinement / local coefficient theorem | T | Provides the clean local exact sequence and general interface formula under cap-extension. |

Internal consolidation:

- harmonic cut quotients are the circuit geometry;
- the labelled theta graph is the interface quotient;
- weight-two circuits and the two-edge sewing bit are the same local object;
- absence of weight-three circuits and absence of a three-edge sewing bit have the same cause;
- interface-line duality is the local kernel/quotient form of the pullback–pushout correspondence.

## G. Embedding, Petrial, transition, and surface programme

The current `main` tree does not contain the source bodies below.  The 2026-07-14 manifest commits their filenames, sizes, and SHA-256 hashes.  They are therefore preserved as provenance but cannot be treated as audited active notes until restored.

### Substantive manuscript sources named in the snapshot

| Snapshot source | Content class inferred from the active synthesis | Status |
|---|---|---:|
| `affine-cdc-gauge-embedding-correspondence-2026-07-14.md` | Gauge choices and compatible embeddings/rotation systems | A |
| `affine-cdc-code-filtered-petrial-polynomial-2026-07-14.md` | Gauge-filtered surface state sum | A/C |
| `affine-cdc-partial-petrial-surface-census-2026-07-14.md` | Finite surface census and orientability/genus data | A/C |
| `affine-cdc-syndrome-transition-universal-invariant-2026-07-14.md` | Transition/syndrome invariant | A/P |
| `affine-cdc-transition-matroid-code-slice-2026-07-14.md` | Relation with transition/delta-matroid data | A/P |
| `affine-cdc-two-edge-cut-factorization-2026-07-14.md` | Two-edge state and moduli factorization | A/T |
| `affine-cdc-three-edge-cut-factorization-2026-07-14.md` | Three-edge factorization | A/T |
| `affine-cdc-flow-sheaf-index-duality-2026-07-14.md` | Earlier quotient-sheaf/index/Hodge formulation | A; largely absorbed |
| `affine-cdc-flow-tensor-complex-2026-07-14.md` | Earlier tensor complex | A; absorbed |
| `affine-cdc-fano-basis-packing-determinant-2026-07-14.md` | Coordinate determinant expansion | A; absorbed by divided-square/torsion notes |
| `affine-cdc-higher-rank-obstruction-note-2026-07-14.md` | Earlier higher-rank failure analysis | A; absorbed by residue theory |
| `affine-cdc-rank4-K33-counterexample.md` | Earlier explicit counterexample | A; absorbed by active rank-four examples |

### Historical and operational sources

Architecture freezes, archive indices, master navigation files, handoffs, mining logs, research logs, scripts, CSV/JSON reports, and verification outputs are provenance or evidence.  They should not be copied into active exposition unless they contain a theorem or counterexample not already extracted.

### Required restoration audit

When the source bodies are rematerialized, each item must be classified as:

1. already absorbed verbatim by an active theorem;
2. containing an additional lemma/example that must be extracted;
3. computational evidence only;
4. speculative connection requiring literature review;
5. obsolete or false.

Until that audit, no active document should claim that every detailed topological result has been reconstructed from the hash-only snapshot.

## H. Literature and provenance status

The active repository has almost no proper external bibliography.  This is a material gap, not a cosmetic one.

The following comparisons are required before the corresponding blocks are publication-ready:

- cycle-double-cover and nowhere-zero-flow background;
- graph sheaves and cellular/coefficient-system formulations;
- equilibrium stresses and rigidity complexes;
- binary code Schur products and syzygies;
- Koszul and Khatri–Rao/diagonal tensor constructions;
- represented matroid quotients and strong maps;
- graph bicycle spaces and higher-order orthogonality;
- transition matroids, delta-matroids, circuit partitions, Petrials, and topological graph polynomials;
- determinant-line torsion in characteristic two.

A bibliography should distinguish three claims:

1. standard background being reused;
2. a known construction under new notation;
3. a genuinely new theorem or synthesis.

No provisional term should be promoted merely because the internal structure is elegant.

## I. What is verified, and what is not

### Machine-checked anchor

The companion Lean repository verifies the original AffineCDC construction and headline CDC theorem.  It is the formal source of truth until the invariant presentation is itself formalized.

### Manuscript theorem layer

Most active notes explicitly label themselves theorem-level drafts.  Their arguments are concrete and often basis-free, but they have not all received independent line-by-line audit.

### Finite computational layer

Rank-three through rank-six residue identities, the rank-four examples, and historical small-graph censuses include exact computations.  Such checks are evidence and examples; they do not replace the general proofs.

### Programmatic layer

The abstract code-flag category, external recognition, higher-rank decorated residues, and restored topological state-space theory remain research programmes.

## J. Immediate editorial actions after this reorganization

1. Add an architectural warning to `flow-tensor-datum.md` so its historical title cannot mislead readers.
2. Use the pair-complex notation consistently in all new notes.
3. Present the local Fano package once; downstream notes should cite it instead of rebuilding the same support table.
4. Present the all-rank residue theorem before the rank-four Pfaffian specialization.
5. Fold the detailed \(K_{3,3}\) computation into the six-vertex comparison in publication prose, retaining the standalone dossier for checking.
6. Cite the chain-level bridge whenever calling the tensor complex a reduction.
7. Restore the hash-only topological sources before claiming their detailed results are active.
8. Build a real bibliography before asserting novelty for the general code/tensor or topological frameworks.
