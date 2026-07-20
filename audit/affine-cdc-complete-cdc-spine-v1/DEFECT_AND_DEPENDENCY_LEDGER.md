# AffineCDC Programme A — Defect and Dependency Ledger

**Audit:** `AC-AUDIT-A`  
**Fixed candidate:** `68715fb29bb4b6555e2bc3e089603c5390d01566`  
**Overall classification:** `VERIFIED SUBJECT TO NAMED EXTERNAL THEOREMS / NON-BLOCKING EXPLICITNESS REPAIRS`

## 1. Severity summary

| Class | Count | Effect on theorem |
|---|---:|---|
| `PASS` | 10 proof units / all 12 load-bearing arrows verified | none |
| `EXPOSITORY-REPAIR` | 3 ledger items | non-blocking; no theorem or hypothesis change |
| `MATHEMATICAL-REPAIR` | 0 | none |
| `BLOCKED-SOURCE` | 0 | none |
| `GENUINE-FRONTIER` | 0 | none |

There is no material mathematical defect in the complete-CDC theorem spine.

## 2. External dependency ledger

### DEP-1 — Seymour nowhere-zero six-flow theorem

- **Classification:** `PASS — NAMED EXTERNAL THEOREM`
- **Load-bearing use:** A3, hence A10 Step 4.
- **Exact statement used:** every finite graph without an isthmus has a nowhere-zero integral six-flow, equivalently an oriented integer circulation with every edge value in `±1,…,±5`.
- **Primary source:** P. D. Seymour, “Nowhere-zero 6-flows”, *Journal of Combinatorial Theory, Series B* **30** (1981), 130–135, DOI `10.1016/0095-8956(81)90058-7`.
- **Input supplied by candidate:** the expanded graph `H` is finite, loopless, and has no singleton cut; therefore each edge-bearing component has no isthmus.
- **Scope check:** disconnected graphs are handled componentwise; isolated vertices and the empty graph are inert; modern proof sources explicitly allow parallel edges.
- **Conclusion:** the theorem implies exactly the integral six-flow input claimed by A3.
- **Unresolved source gate:** none.

### DEP-2 — equal-order group-flow transport

- **Classification:** `PASS — INTERNAL, NOT EXTERNAL`
- **Load-bearing use:** transfer from a nowhere-zero `Z/8Z` flow to a nowhere-zero `F₂³` flow.
- **Candidate proof:** for every finite abelian group `A` and spanning edge set `B`, a spanning-forest restriction bijection gives

  `|ker ∂_A| = |A|^(|B|-|V|+c(B))`.

  Inclusion–exclusion over zero coordinates gives the nowhere-zero flow count, which depends only on `|A|`.
- **Conclusion:** Tutte's equal-order theorem is provenance only and is not an unresolved premise.

### DEP-3 — finite-dimensional quadratic and symplectic linear algebra

- **Classification:** `PASS — PROVED IN CORPUS`
- **Load-bearing use:** A4–A5.
- **Candidate proof:** nondegeneracy, Lagrangian dimension arguments, characteristic-torsor nonemptiness, `(L∩M)⊥=L+M`, and the intersection criterion are proved directly.
- **Conclusion:** no separate external theorem is required.

## 3. Non-blocking repair ledger

### XR-1 — make Seymour's multigraph convention explicit

- **Classification:** `EXPOSITORY-REPAIR`
- **Location:** controlling A3 statement in `complete-cdc/foundations-expansion-and-flow.md`, with corresponding source note in A3.
- **Current wording:** “Every finite graph with no isthmus has a nowhere-zero integral six-flow.”
- **Issue:** the candidate applies the theorem to a loopless multigraph that may have parallel edges. This scope is valid, and the retained source discussion cites modern proofs with explicit multigraph conventions, but the preferred controlling chapter leaves the convention implicit.
- **Repair:** add one sentence that “graph” permits parallel edge objects here, or cite an explicit loopless-multigraph formulation beside Seymour's primary source.
- **Mathematical effect:** none.
- **Suggested route:** ordinary AC-PDL source/explicitness repair after AC-DIR disposition.

### XR-2 — expand the converse local-family classification

- **Classification:** `EXPOSITORY-REPAIR`
- **Location:** A4 Proposition 4.2 / integrated affine chapter Theorem 2.1.
- **Current proof:** the forward deleted-point construction and injectivity are explicit; the converse is compressed into a short finite-pattern argument.
- **Issue:** this is a load-bearing bridge from combinatorial local even families to the affine torsor `κ_v+L_v`. The statement is correct and independently reconstructible, and the companion Lean checkpoint proves the classification, but the preferred paper proof should not require consultation of the formal anchor to expand the converse.
- **Repair:** add either:
  1. a complete eight-family table indexed by the deleted point `m∈F₂³`; or
  2. an algebraic reconstruction showing directly that every even triple of affine direction lines determines the unique `m` satisfying `P_h=κ_h+[m]_h`.
- **Mathematical effect:** none.
- **Suggested route:** ordinary AC-PDL explicitness repair after AC-DIR disposition.

### XR-3 — synchronize the older outer-shell companion with controlling A3

- **Classification:** `EXPOSITORY-REPAIR`
- **Location:** `reduction/outer-shell-and-binary-flow.md` §4.1.
- **Current state:** this mechanism-level companion retains an older classical route invoking Tutte's equal-order existence theorem, while the controlling integrated A3 proves the required transport internally.
- **Issue:** the control surfaces correctly state that the integrated A0–A10 chain supersedes this dependency choice, so there is no logical conflict. A reader entering through the companion chapter could nevertheless mistake Tutte for a second unresolved logical dependency.
- **Repair:** mark the Tutte route explicitly as a retained alternative/historical route and cross-link to the controlling A3 forest-count and inclusion–exclusion proof.
- **Mathematical effect:** none.
- **Suggested route:** ordinary AC-PDL/Curator synchronization repair after AC-DIR disposition.

## 4. Examined potential defects resolved as `PASS`

### P-1 — external-edge alternate path in the expansion

An alternate original path in `G-e` lifts edgewise; connected fibre cycles join consecutive lifted ports. The resulting walk avoids `λ(e)` and reduces to a path. Degree-two fibres have a parallel internal mate. No gap.

### P-2 — disconnected use of Seymour

No global connectedness is required. Apply the theorem to each edge-bearing component and concatenate the coordinate assignments. No gap.

### P-3 — forest count with isolated vertices

The spanning forest has `|V|-c(B)` edges, including isolated components in `c(B)`. Chord assignments extend uniquely by leaf elimination, and each component's root equation follows from total boundary zero. The exponent is correct. No gap.

### P-4 — local Fano cross-pairing

With independent `a,b∈W`, `c=a+b`, and `t∉W`, the determinant computation gives three copies of the coefficient of `t`, hence the unique functional with kernel `W`. The quotient representatives are well defined. No gap.

### P-5 — characteristic-torsor intersection

If `q` vanishes on `L∩M`, a characteristic representative lies in `(L∩M)⊥=L+M`; removing its `L` component produces an element of `M` in the same characteristic coset. The converse follows from isotropy of `M`. No gap.

### P-6 — graph/dart descent

Compatibility equates the two endpoint quotient labels, hence the actual affine lines. The selected dart set is edge-reversal closed, so it descends to named edge objects. The pair complex alone is not used as a graph substitute. No gap.

### P-7 — repeated support values

The cover remains indexed through extraction and collapse. Image-multiset flattening preserves one occurrence per index. Memberwise circuit decomposition treats repeated parents separately. No gap.

### P-8 — collapse of auxiliary edges

Internal edges lie within complete fibres and never meet a pulled-back cut. Their loss does not affect cut parity or original-edge multiplicity. The candidate correctly avoids claiming that circuits project to circuits. No gap.

### P-9 — finite circuit decomposition

A circuit sub-support exists in every nonempty finite cut-even support. Removing it preserves cut-evenness and strictly decreases cardinality. The resulting circuits are edge-disjoint within each parent, so the global multiplicity equation is exact. No gap.

### P-10 — loop/core normalization

A circuit containing a loop is exactly that singleton loop. Thus every CDC contains exactly two singleton occurrences per loop, and core circuits survive unchanged. No gap.

## 5. Hidden-hypothesis ledger

| Suspected hidden hypothesis | Finding |
|---|---|
| connectedness | not used; all stages are componentwise or direct sums |
| simplicity | not used; parallel edge objects are preserved and counted separately |
| looplessness of headline theorem | not used; looplessness is only an internal reduction condition |
| finite ambient vertex carrier | not used; finite active edges imply finite active vertices |
| absence of isolated vertices | not used; isolated vertices are inert and may have empty fibres |
| distinct support values | not used; occurrences are indexed and repetitions are retained |
| circuit preservation under collapse | explicitly not asserted |
| Programme B/five-support theorem | not used |
| end-to-end Lean verification | not claimed or used as proof evidence |

## 6. Stop-condition ledger

| Stop condition from issue #35 | Triggered? | Reason |
|---|---:|---|
| load-bearing theorem missing or under-hypothesized | no | every arrow has an exact proved interface |
| external theorem unavailable or too weak | no | Seymour's theorem matches the required flow input |
| circular theorem chain | no | A0–A10 dependency order is acyclic |
| programme-level new mathematics required | no | no mathematical repair was found |
| audit requires candidate/live-branch interference | no | all findings fit the authorized audit branch |

## 7. Routing recommendation

- `XR-1`, `XR-2`, and `XR-3`: route to AC-PDL as ordinary explicitness/source-synchronization repairs only after AC-DIR disposition.
- No item should be routed to AC-RL.
- No candidate, `main`, Lean, manuscript, release, arXiv, DOI, or publication movement follows from this audit alone.

## 8. Final ledger state

`NO MATERIAL DEFECT / NO BLOCKED SOURCE / NO GENUINE FRONTIER`

The review branch is an assurance record only and is ready for AC-DIR reception as `RETURNED-AWAIT-DIR`.