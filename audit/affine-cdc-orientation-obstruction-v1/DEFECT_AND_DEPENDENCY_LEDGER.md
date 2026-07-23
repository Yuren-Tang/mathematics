# AC-OR1-AUDIT-01 defect and dependency ledger

## 1. Defect ledger

| ID | Severity | Candidate location | Finding | Exact repair | Mathematical effect |
|---|---|---|---|---|---|
| `OR1-D1` | non-blocking mathematical wording | `orientation/surface-and-fixed-lift-obstruction.md`, Section 2 and Theorem 3.1(3) | One geometric indexed face boundary is represented by two reverse `rho_a`-orbits exchanged by `sigma`. A literal statement that the directed face boundaries “are the `rho_a`-orbits” double-counts faces. | State that a face occurrence is a connected component of `F_a`, equivalently a `sigma`-paired class `{O,sigma O}` of reverse `rho_a`-orbits; either orbit may be chosen as an orientation of that face boundary. | No proof or quantifier changes. Surface, Euler counts, and orientation theorem remain valid. |
| `OR1-D2` | non-blocking classification wording | `orientation/fixed-fibre-gauge-and-duality.md`, Section 5, especially the explanatory bullet after Corollary 5.1 | The coset is a set of accessible Petrial words, equivalently labelled lifts modulo `ker Lambda_f`. It is not automatically a set of homeomorphism/isomorphism classes of unlabelled surfaces. | Replace “unlabelled orientable partial-Petrial surfaces are a coset” with “accessible orientable partial-Petrial words are a coset,” and explain the quotient by componentwise affine translations. | Formula and torsor/coset distinction remain unchanged. |
| `OR1-D3` | expository dependency gap | `orientation/fixed-fibre-gauge-and-duality.md`, Section 6 | The alternate code form uses `C(G)`, `F_f`, and `*` without local definitions. | Define `C(G)` as the binary cycle space, `F_f` as the span of the binary coordinate words of `f`, and `U*V` as the span of coordinatewise products `u*v`. Cite the exact B4/tensor identity. | No mathematical change. |
| `OR1-D4` | terminology ambiguity | `orientation/k4-and-oriented-collapse.md`, Section 1, and global references to a “rank-three flow” | The `K_4` flow is `F_2^3`-valued but its values span the plane `W`, not all of `F_2^3`. | Use “nowhere-zero `F_2^3`-valued flow” or “ambient-rank-three flow”; reserve “full-span rank three” for span dimension three. | No change to compatibility or the example. |
| `OR1-D5` | terminology ambiguity | `orientation/surface-and-fixed-lift-obstruction.md`, Corollary 5.2; `orientation/k4-and-oriented-collapse.md` | “Oriented CDC” can vary across the literature. The argument proves the directed CDC condition. | Declare once that “oriented/directed CDC” means a multiset of directed circuits in which every edge occurs exactly once in each direction. | No mathematical change. |
| `OR1-D6` | assurance clarification | `orientation/k4-and-oriented-collapse.md`, Section 7 | Loop reinsertion is correct only under the stated two-dart singleton-loop convention and lies outside the current Lean public statement. | Repeat the loop convention in any external theorem that includes loops and retain the non-formalized status. | No change to the loopless obstruction package. |

No blocking defect, false quantifier, invalid example, or missing new lemma was found.

## 2. Theorem dependency ledger

### `DEP-01` — rank-three compatible-lift existence

- source: `projects/affine-cdc/core/rank-three-fano-compatibility.md`;
- exact base: `curation/affine-cdc-programme-a-b1-b8-unified-v1@ec765cd03271abd3588ec36faec3d53d0f8aa03b`;
- consumed statement: Theorem 7.1 and the compatible-family torsor under `H_f^0`;
- role in OR1: guarantees that the fixed-flow fibre is nonempty and identifies its vertical parameter space;
- assurance: controlling Programme A mathematics, not re-proved by OR1.

### `DEP-02` — retained dart/support/rotation data

- source repository: `Yuren-Tang/affine-cdc`;
- exact checkpoint: `main@ebd7098a7a8b824e8c0a511d3c71f61705672aa8`;
- exact file: `lean/AffineCDC/Cycle.lean`;
- declarations consumed: `partnerD`, `partnerD_vtx`, `partnerD_mem`, `partnerD_ne`, `partnerD_partnerD`, `eq_or_eq_partnerD`, `Msupp_vertex_unique`, `rho`, `rhoInv`, `rho_mem`, `rhoInv_rho`, `rho_rhoInv`, `exists_indexed_dart_cover`;
- role in OR1: verifies the unique same-index turn at a cubic vertex and the inverse dart rotations;
- non-consumed conclusion: Lean does not construct `S_g`, `w`, `omega`, `Omega_f`, orientation stress, the `K_4` classification, or enriched directed collapse.

### `DEP-03` — vertical torsor and partial Petrial

- source: `projects/affine-cdc/five-support/gauge-and-reconfiguration.md`;
- exact base: `ec765cd03271abd3588ec36faec3d53d0f8aa03b`;
- consumed statements: Theorem 2.1 (`H_f^0` torsor and `B_f`) and Theorem 3.1 (gauge/partial-Petrial correspondence);
- role in OR1: converts the affine endpoint translation bit into one edge-band Petrial toggle;
- independent audit action: the edgewise translation/swap calculation was reconstructed rather than accepted from the theorem label.

### `DEP-04` — gauge code / Schur-product identity

- sources:
  - `projects/affine-cdc/reduction/incidence-to-tensor-complex.md`;
  - `projects/affine-cdc/gauge/gauge-modes-and-circuits.md`;
- exact base: `ec765cd03271abd3588ec36faec3d53d0f8aa03b`;
- consumed identity: `B_f=(C(G)*F_f)^perp`;
- role in OR1: alternate expression for orientation stress;
- audit note: the primary annihilator criterion does not depend on this alternate expression.

### `DEP-05` — collapse datum

- source: `projects/affine-cdc/reduction/even-cover-and-collapse.md`;
- exact base: `ec765cd03271abd3588ec36faec3d53d0f8aa03b`;
- consumed data: vertex collapse map, injective edge lift, all cross-fibre edges lifted, all auxiliary edges internal to fibres;
- role in OR1: endpoint matching and multiplicity preservation under directed projection;
- non-consumed result: the support-only cut-parity transport theorem is not treated as an oriented-collapse theorem.

### `DEP-06` — standard signed rotation systems

- public anchor: Gross–Tucker, *Topological Graph Theory* (1987), signed rotation/band decomposition and switching equivalence;
- role in OR1: confirms that reversing one local vertex orientation reverses the rotation and toggles incident edge signs, and that orientability is equivalent to a switch-equivalent all-untwisted presentation;
- audit status: standard external topology, not a project-specific theorem.

### `DEP-07` — directed CDC terminology

- public anchor: Jiménez–Loebl, *Directed cycle double covers and cut-obstacles* (2014);
- consumed definition: a family of oriented cycles covering every edge in two opposite directions;
- role in OR1: fixes the exact meaning of the oriented-face conclusion.

### `DEP-08` — closed surface classification

- consumed fact: a closed connected surface with Euler characteristic `1` is the projective plane, and one with Euler characteristic `2` is the sphere if orientable/under the direct tetrahedral realization;
- role in OR1: identifies the two `K_4` surfaces after connected cellular reconstruction;
- audit note: Euler counts are not used without the T1 closed-connected-cellular theorem.

### `DEP-09` — finite directed-trail decomposition

- consumed fact: every finite nonempty directed closed trail splits into directed circuits while partitioning directed edge occurrences;
- role in OR1: final step of enriched collapse;
- proof status: independently reproved by splitting at a repeated vertex and induction.

## 3. Non-dependencies explicitly excluded

The audit did not use any of the following as correctness authority:

- issue #49 or its exploratory return;
- issue #56;
- AC-PDL's authorial status;
- Curator integration or `AC_OR1_FINAL_AUDIT.md` conclusions;
- Git ancestry beyond exact corpus identification and branch-base checking;
- `Port.cubic_flow_cdc` as an orientation theorem;
- the existence of partial Lean ingredients as evidence for unformalized topology;
- Paper A, Research Lead moving work, release, arXiv, DOI, or publication surfaces.

## 4. Open-obligation ledger

| ID | Exact question | Status | What the audited package provides | What remains |
|---|---|---|---|---|
| `AC-RL-OR-FIXED-FIBRE-VANISHING` | Is `Omega_f=0` for every nowhere-zero `F_2^3`-valued flow on every finite bridgeless cubic multigraph? | open | a complete obstruction class, torsor/coset classification, and dual stress certificate | a universal vanishing proof or an exact fixed-fibre counterexample |
| `AC-RL-OR-GRAPH-EXISTENCE` | If universal fixed-fibre vanishing fails, does every such graph admit at least one flow `f` with `Omega_f=0`? | open | conditional implication from a favourable flow/lift to a directed CDC | a graph-level flow-selection or reconfiguration theorem |

The two obligations are logically distinct. The first quantifies over every fixed flow; the second existentially quantifies over flows for each graph. The `K_4` example closes neither.

## 5. Assurance ledger

| Layer | Audit conclusion |
|---|---|
| retained Lean ingredients | exact and adequate as input, but partial |
| surface reconstruction | independently verified subject to `OR1-D1` wording repair |
| fixed-lift obstruction | independently verified |
| gauge law | independently verified from endpoint translation |
| fixed-fibre class and labelled torsor | independently verified |
| Petrial-word coset | independently verified subject to `OR1-D2` wording repair |
| orientation stress | independently verified; alternate code notation needs `OR1-D3` |
| `K_4` example | independently verified; terminology needs `OR1-D4` |
| enriched directed collapse | independently verified |
| loop reinsertion | verified under explicit convention, outside Lean |
| global oriented existence | open |

## 6. Final ledger classification

`VERIFIED SUBJECT TO NAMED NON-BLOCKING REPAIRS`

The required repairs are bounded editorial corrections to the immutable candidate. This audit records them but performs no candidate mutation.