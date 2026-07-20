# AffineCDC Programme A — Independent Audit A

**Role:** `AffineCDC — Independent Audit A` (`AC-AUDIT-A`)  
**Audit class:** temporary independent mathematical review  
**Fixed candidate:** `curation/affine-cdc-programme-a-v1@68715fb29bb4b6555e2bc3e089603c5390d01566`  
**Immutable authorial source:** `proof-development/affine-cdc-rigour-v1@8bee16780b549f51e1f29343671a059961ec4172`  
**Review branch:** `audit/affine-cdc-complete-cdc-spine-v1`  
**Receiver / closure owner:** `AffineCDC — Director` (`AC-DIR`)

## 1. Overall classification

`VERIFIED SUBJECT TO NAMED EXTERNAL THEOREMS / NON-BLOCKING EXPLICITNESS REPAIRS`

The complete theorem line is mathematically valid at expoundable paper-proof level, conditional only on the correctly stated external theorem of Seymour. I found no circular dependency, false scope, hidden connectedness or simplicity hypothesis, material gap, or requirement for new programme-level mathematics.

No stop condition in issue #35 was triggered. In particular:

- no load-bearing theorem is missing or materially under-hypothesized;
- Seymour's theorem is available in the scope required here;
- the A0–A10 chain is acyclic;
- no repair requires contact with `AC-RL` or mutation of the fixed candidate;
- no `MATHEMATICAL-REPAIR`, `BLOCKED-SOURCE`, or `GENUINE-FRONTIER` finding was identified.

The qualifications in the overall classification are conservative and exact:

1. Seymour's nowhere-zero six-flow theorem remains the sole non-elementary external logical input.
2. Three presentation/source-synchronization repairs would make the preferred integrated proof more self-contained, but none changes a theorem, hypothesis, construction, or implication.

## 2. Material audited

I independently reconstructed the proof from both required layers:

- the preferred integrated three-chapter proof under `projects/affine-cdc/complete-cdc/`;
- the retained authorial dossiers `AC_PD_A0_*` through `AC_PD_A10_*` and the checkpoint `OBLIGATION_DAG.md`.

I also checked the mechanism-level companions named in issue #35:

- `core/affine-incidence-and-obstruction.md`;
- `core/rank-three-fano-compatibility.md`;
- `reduction/outer-shell-and-binary-flow.md`;
- `reduction/even-cover-and-collapse.md`.

The control, provenance, and assurance surfaces were checked to ensure that later Programme B mathematics was not consumed and that Curator integration was not treated as proof evidence.

## 3. Headline theorem

The candidate proves:

> Every multigraph with finite active edge set and no singleton cut has a finite indexed family of circuits covering each active edge object exactly twice.

Here a circuit is a nonempty inclusion-minimal finite cut-even support. This includes singleton loops, two-edge parallel digons, and ordinary simple cycle supports. The theorem allows disconnected graphs, isolated vertices, parallel edge objects, loops, and an arbitrary ambient vertex carrier.

The hypotheses are the weakest justified hypotheses used by the proof. For a nonloop edge, singleton-cut status is equivalent to bridge status. Loops are never cut edges and are handled by an exact deletion/reinsertion interface rather than by the loopless incidence convention.

## 4. Audit result by proof unit

| Unit | Result | Independent finding |
|---|---|---|
| A0 — foundations | `PASS` | The finite-active model, cut/bridge equivalence, intrinsic half-edge parity, cut-even equivalence, circuit characterization, and indexed occurrence semantics are correct. The maximal-path cycle-existence argument handles loops, parallel digons, disconnected supports, and isolated ambient vertices. |
| A1 — loops | `PASS` | Loop deletion preserves every cut exactly. Circuits containing loops are precisely singleton loops. Two forced singleton occurrences per deleted loop give an exact two-way CDC witness normalization. |
| A2 — cubic expansion | `PASS` | The port-cycle expansion is finite, loopless, and cubic. Degree-two fibres correctly require two distinct parallel internal edges. External-edge nonbridge lifting through connected fibre arcs is valid. Component correspondence, collapse data, and cut pullback are exact. |
| A3 — binary flow | `EXPOSITORY-REPAIR` | The mathematical implication is valid: Seymour gives an integral six-flow componentwise; range inclusion and mod-eight reduction give a nowhere-zero `Z/8Z` flow; the internal forest count and inclusion–exclusion transfer existence to `F₂³`. The preferred chapter should state the parallel-edge/multigraph convention more explicitly at the Seymour invocation. |
| A4 — pair complex | `EXPOSITORY-REPAIR` | The quotient spaces, local torsor, edge diagonal, affine intersection, pair-complex obstruction, quotient equation, and stress dual are correct. The converse half of the finite local-family classification is load-bearing and should be expanded algebraically or by a complete eight-family table in the preferred chapter. The retained dossier and checked local classification support the claim. |
| A5 — rank-three compatibility | `PASS` | The canonical anisotropic quadratic planes, determinant polar pairing, local Fano Lagrangian, transgression, cross-pairing, characteristic torsor, abstract intersection criterion, and total-singular edge diagonal form a complete proof of global compatibility. |
| A6 — support extraction | `PASS` | Retained graph/dart pairing makes endpoint descent well defined. Local evenness gives 0-or-2 incidence parity, and each two-point affine edge line gives exact coverage by two point indices. Equal and empty supports remain indexed occurrences. |
| A7 — parity adapter | `PASS` | On loopless graphs, once-per-edge incidence degree equals intrinsic half-edge degree; the latter is equivalent to cut parity. The dossier correctly refuses to extend this adapter across loops. |
| A8 — collapse | `PASS` | The pulled-back-cut identity gives a memberwise cut-intersection bijection. Projection preserves cut-evenness and exact original-edge occurrence multiplicity; auxiliary fibre edges disappear harmlessly. No circuit projection is asserted. |
| A9 — decomposition | `PASS` | Every nonempty finite cut-even support contains a circuit. Symmetric-difference closure and strict cardinality descent give a finite edge-disjoint circuit decomposition. Decomposing each indexed parent separately preserves repeated-parent multiplicity exactly. |
| A10 — assembly | `PASS` | The invocation order is valid and noncircular. The proof ends with a CDC of the loopless core and exact two-occurrence loop reinsertion. All stated boundary cases are covered. |

## 5. External theorem verification

The sole non-elementary external premise is:

> Every finite graph with no isthmus admits a nowhere-zero integral six-flow, with nonzero values of absolute value less than six.

Primary source:

P. D. Seymour, “Nowhere-zero 6-flows”, *Journal of Combinatorial Theory, Series B* **30** (1981), 130–135, DOI `10.1016/0095-8956(81)90058-7`.

The use is exact. The expanded graph is finite, loopless, and has no singleton cut; therefore every edge-bearing component has no isthmus. Seymour is applied componentwise, while isolated vertices and the empty graph are inert. Modern proof sources explicitly permit parallel edges, which covers the multigraph convention of the expansion.

Tutte's equal-order group-flow theorem is not an unresolved premise. A3 internally proves

`|Flow_A(G[B])| = |A|^(|B|-|V|+c(B))`

by a spanning-forest restriction bijection and then applies inclusion–exclusion. Hence the number of nowhere-zero flows depends only on `|A|`, which validly transfers existence from `Z/8Z` to `F₂³`.

## 6. Required challenge cases

### Disconnected graphs

Every edge-bearing component is treated separately for bridges and Seymour flows; the affine spaces are direct sums; support parity, collapse, and circuit decomposition are componentwise. No step needs connectedness.

### Parallel edges

Parallel edges remain distinct edge objects throughout ports, external lifts, flow coordinates, quotient summands, support membership, collapse, and occurrence counting. Degree-two fibres use two parallel internal edge objects, and two original parallel edges may form a digon circuit.

### Loops

Loops cross no cuts. They are removed before the loopless flow/incidence machinery, cannot mix with another edge in a circuit, and are reinserted as exactly two singleton circuit occurrences each.

### Empty and isolated components

The empty graph has the empty CDC. A loop-only graph reduces to the empty core and is restored explicitly. Vertices not incident with active edges have empty fibres and impose no cut, flow, affine, or multiplicity condition.

### Bridges versus loop edges

Only nonloop edges can be bridges. A nonloop edge is a bridge exactly when it is the unique edge of a cut. The theorem's no-singleton-cut hypothesis is therefore exact and loop-insensitive.

### Finite active edges with non-finite ambient carriers

Finitely many edge endpoint occurrences imply finitely many active vertices. Every construction and induction uses only this finite active subgraph or finite supports. Infinite isolated ambient carriers are inert.

### Repeated supports and multiset multiplicity

Coverage is counted by indices, not distinct support values. Equal supports at distinct point indices remain separate occurrences before and after collapse and decomposition. Empty indexed supports contribute no edge multiplicity and may disappear only at the final memberwise decomposition stage.

### Collapse fibres and auxiliary edges

Internal edges remain within complete fibres and never cross a pulled-back cut. They have no downstairs counterpart. The proof transports only cut-even supports and exact original-edge occurrences, not circuit minimality or upstairs circuit structure.

## 7. Non-blocking repairs

The exact repair ledger is in `DEFECT_AND_DEPENDENCY_LEDGER.md`. In summary:

1. make the Seymour multigraph/parallel-edge convention explicit at the controlling A3 invocation;
2. expand the converse local-family classification in the preferred A4 exposition;
3. mark the older Tutte-based route in the mechanism-level outer-shell companion as a non-controlling alternative and cross-link it to the controlling internal A3 count.

All three are `EXPOSITORY-REPAIR`. None changes the theorem, proof architecture, dependency DAG, or headline scope.

## 8. Independence and mutation statement

This audit did not infer correctness from corpus status, Git ancestry, Curator integration, or the partial Lean checkpoint. Those were used only for provenance and cross-checking.

No candidate corpus file was modified. No change was made to `main`, PDL/RL branches, Curator branches, Lean, manuscripts, releases, tags, arXiv, DOI, or publication surfaces. The review branch contains only the three authorized audit deliverables.

**Lifecycle on return:** `RETURNED-AWAIT-DIR`.