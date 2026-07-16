# MP1 outer-shell promotion report

**Workstream:** `AC-MP1-01` — AffineCDC MP1 Outer Shell Promotion  
**Authoritative issue:** `Yuren-Tang/research-workbench#11`  
**Repository:** `Yuren-Tang/mathematics`  
**Owned branch:** `research/affine-cdc-outer-shell-promotion-v1`  
**Controlling base:** `749e0579581fcc838685138b3582f4de306b8e72`  
**Lifecycle:** bounded re-issued canonical-promotion candidate  
**Final branch tip:** supplied in the authoritative issue handoff; a commit cannot contain its own SHA.

## 1. Result

The bounded promotion unit is substantively complete and ready for
`AffineCDC — Director` disposition.

The branch adds:

- `projects/affine-cdc/reduction/outer-shell-and-binary-flow.md`;
- `projects/affine-cdc/research/MP1_OUTER_SHELL_PROMOTION_REPORT.md`.

No Lean file, frozen M1/M2/adaptive source, canonical `main`, release, tag, DOI,
or manuscript-submission surface was modified.

## 2. Source map

| Role | Exact source | Use in promotion |
|---|---|---|
| canonical base | `main@749e0579581fcc838685138b3582f4de306b8e72` | architecture, reliability, cut-even handoff, publication boundary |
| M1 reviewed source | `research/affine-cdc-outer-shell-v1@3f79773e6ddb7d3a816a1a47120fa0696a7d0b52` | port-cycle expansion, exact sizes, bridgelessness, collapse data, expansion-first route, fixed-order criterion and degree-eight example |
| M2 accepted audit | `research/affine-cdc-binary-eight-flow-v1@8b17ebb4077b5bb00a96ddb83a5f46c799489fdb` | loopless flow interface, componentwise Seymour, literal `6 -> 8`, Tutte statement split, source and Mathlib boundary |
| accepted adaptive source | `research/affine-cdc-adaptive-ordering-v1@04f9a37052406f760a31b725945cfa52dce6c2d8` | adaptive prefix avoidance and flow-preserving expansion |
| cut-even handoff | `projects/affine-cdc/reduction/even-cover-and-collapse.md` on the base | vertex-even/cut-even bridge, projection, final decomposition, loop reinsertion |
| reliability control | `projects/affine-cdc/FORMAL_STATUS.md` on the base | machine-checked/paper/external separation |
| publication control | `projects/affine-cdc/PUBLICATION_PROGRAM.md` on the base | Paper A endpoint and placement |

The frozen research branches were read only.

## 3. Theorem packet promoted

### 3.1 Elementary graph layer

The candidate chapter gives complete paper proofs of:

- finite active edge set implies finite active vertex set;
- loopless bridgeless active vertices have finite degree at least two;
- port-cycle expansion with empty isolated fibres and two parallel internal edges
  in a degree-two fibre;
- exact collapse data `(π, λ)`;
- exact sizes
  \[
  |V(H)|=2|E(G)|,\qquad |E(H)|=3|E(G)|;
  \]
- preservation of bridgelessness without connectedness.

### 3.2 External binary-flow layer

The chapter exposes the weakest consumed interface:

> Every finite-active-edge loopless multigraph with no singleton cut, allowing
> parallel edges and not necessarily connected, has a nowhere-zero
> \(\mathbf F_2^3\)-flow in the current unoriented incidence-sum convention.

The exact external boundary is:

1. Seymour on each edge-bearing connected component;
2. literal range inclusion from integer `6-flow` to integer `8-flow`;
3. Tutte's existence theorem for the arbitrary order-eight abelian group
   \(\mathbf F_2^3\);
4. the loopless characteristic-two adapter from signed to unoriented
   conservation.

Tutte's group-flow counting theorem is stated separately and is not used.

### 3.3 Two valid outer-shell routes

**Expansion-first**

\[
G\to H\to(H,f).
\]

This is flow-independent, uses arbitrary local cyclic orders, needs no adaptive
theorem, and remains an independent M1 theorem.

**Adaptive flow-first**

\[
G\to(G,f)\to(H,\widetilde f,\pi,\lambda).
\]

The chapter proves the general finite binary-rank-at-least-two adaptive
prefix-avoidance theorem, including the empty multiset, and aligns it with:

- active vertices;
- degree-two parallel fibres;
- chosen port indices and cyclic starts;
- the exact conservation equation;
- preservation of the downstairs flow on lifted edges.

The degree-eight Gray-tour example is retained as a sharp fixed-order
obstruction, not as an obstruction to adaptive ordering.

### 3.4 Cut-even handoff

The natural compositional output is a multiset cut-even double cover of the
loopless core. Projection through `λ` preserves cut parity and exact double
coverage while allowing repeated and empty support occurrences.

The chapter explicitly rejects circuit-by-circuit projection and performs no
upstairs decomposition. One final finite circuit decomposition and loop
reinsertion remain delegated to `even-cover-and-collapse.md`.

## 4. Route comparison and recommendation

| Criterion | Expansion-first | Adaptive flow-first |
|---|---|---|
| proof spine | `G -> H -> (H,f)` | `G -> (G,f) -> (H,f~,π,λ)` |
| adaptive combinatorics | none | essential |
| selected downstairs flow | not preserved by claim | preserved exactly |
| cyclic-order choice | arbitrary | flow-dependent |
| external theorem placement | on `H` | on `G` |
| functoriality burden | cyclic orders | flow, ordering, omitted point, cyclic start |
| likely local Lean cost | lower | higher |
| paper exposition | independent but longer | preferred concise spine |

**Paper A recommendation:** use adaptive flow-first as the primary proof, and
retain expansion-first as an independent alternative theorem or remark.

**Lean recommendation:** leave undecided. On present evidence expansion-first
likely has lower local formalization cost. Adaptive flow-first must not be
silently added to L1 without a new engineering disposition.

## 5. Source and external-input boundary

The chapter distinguishes four reliability classes:

1. **elementary paper proofs** — active finiteness, expansion, exact sizes,
   collapse data, bridgelessness, local extension equations, adaptive ordering;
2. **classical external theorems** — Seymour and Tutte, composed into the
   isolated `BinaryEightFlow` interface;
3. **existing machine-checked companion results** — the affine core and
   already-cubic flow corollary in their current implementation presentation;
4. **paper-level canonical architecture not yet checked in that form** — the
   graph-level even-cover factorization, cut-even handoff, full outer shell, and
   unconditional endpoint.

No external theorem is represented as machine-checked. The current public
`Statement.lean` remains unproved and unchanged.

## 6. Exact proposed update to `FORMAL_STATUS.md`

Do not apply these edits on the worker branch. After Director acceptance and
canonical promotion, apply the following exact changes.

### 6.1 Add the new paper-proof chapter

In section **5. Paper-proof layer**, insert immediately before
`reduction/even-cover-and-collapse.md`:

```markdown
- [`reduction/outer-shell-and-binary-flow.md`](reduction/outer-shell-and-binary-flow.md);
```

### 6.2 Replace the obsolete outer-shell-gap paragraph

Replace:

```markdown
The outer expansion/flow theorem packet required for the full CDC shell is not
yet a closed canonical chapter in this repository. Its absence is a mathematical
and formalization gap, not merely an editorial gap.
```

with:

```markdown
The chapter
[`reduction/outer-shell-and-binary-flow.md`](reduction/outer-shell-and-binary-flow.md)
now gives the paper-level outer-shell packet. It proves the finite-active-edge
port-cycle expansion, exact collapse data, preservation of bridgelessness, the
adaptive binary ordering theorem, and both the expansion-first and adaptive
flow-first routes. Its `BinaryEightFlow` node remains a classical external
Seymour--Tutte input. None of the outer shell, adaptive ordering, or the
Seymour--Tutte input is thereby machine-checked.
```

### 6.3 Extend the unformalized list in section 4

Replace:

```markdown
- the independent cubic expansion and flow shell;
```

with:

```markdown
- the independent port-cycle expansion and the expansion-first outer shell;
- adaptive prefix avoidance and the flow-preserving adaptive expansion;
- the isolated classical `BinaryEightFlow` interface, including componentwise
  assembly and the loopless characteristic-two adapter;
```

### 6.4 Add a reliability rule

Append to section **8. Reliability rules**:

```markdown
7. Director-reviewed paper proofs of adaptive ordering and the outer shell do not
   acquire Lean status; Seymour and Tutte remain external until an explicit
   formal theorem boundary or implementation is accepted.
```

## 7. Exact proposed update to `PUBLICATION_PROGRAM.md`

Do not apply these edits on the worker branch. After Director acceptance and
canonical promotion, apply the following exact changes.

### 7.1 Replace Paper A mathematical contents, item 6

```markdown
6. **Full outer graph-theoretic shell**
   - active-edge finiteness and preliminary loop separation;
   - the isolated loopless binary-eight-flow input, with componentwise Seymour,
     literal integer `6-flow -> 8-flow`, and Tutte's equal-order existence
     theorem;
   - adaptive prefix avoidance in every finite binary rank at least two;
   - the preferred adaptive flow-first route
     `G -> (G,f) -> (H,\widetilde f,\pi,\lambda)`;
   - the independent expansion-first route `G -> H -> (H,f)`;
   - exact expansion sizes `|V(H)|=2|E(G)|` and `|E(H)|=3|E(G)|`;
   - vertex-even/cut-even bridge on the loopless expansion;
   - pure cut-even collapse transport;
   - a multiset cut-even double cover of the loopless original core.
```

### 7.2 Add the promoted chapter to Paper A canonical sources

Insert before `even-cover-and-collapse.md`:

```markdown
- [`reduction/outer-shell-and-binary-flow.md`](reduction/outer-shell-and-binary-flow.md);
```

### 7.3 Insert the exposition decision after Paper A exclusions

```markdown
### Outer-shell exposition decision

Use the adaptive flow-first route as the primary concise proof. State the
general binary-rank adaptive ordering theorem, specialize it to
\(\mathbf F_2^3\), and retain the degree-eight Gray-tour example as sharpness
for fixed cyclic order. Retain the expansion-first route as an independent
flow-free theorem and possible alternative formalization route. Do not present
adaptive ordering as Lean-formalized, and do not split it into a separate paper
under the present programme.
```

### 7.4 Replace the outer-shell readiness item

Replace:

```markdown
4. close the loop reduction, cubic expansion, flow, collapse, and cut-parity
   theorem packets;
```

with:

```markdown
4. after canonical acceptance of `outer-shell-and-binary-flow.md`, independently
   review the promoted outer-shell proof and integrate it with the loop
   reduction and cut-even handoff; formalization remains separately open;
```

### 7.5 Replace the Paper A readiness opening sentence

Replace:

```markdown
The affine compatibility core is mathematically coherent, but Paper A is not yet
closed because the complete outer shell and formal correspondence are unfinished.
```

with:

```markdown
The affine compatibility core and the proposed outer-shell packet are
mathematically coherent at paper level, but Paper A is not yet closed because
canonical acceptance, formal correspondence, independent proof review,
bibliography, and the Lean endpoint remain unfinished.
```

## 8. Unresolved Director decisions

1. Accept, revise, or reject the candidate chapter for canonical promotion.
2. Decide whether `BinaryEightFlow` may be an explicit external theorem/axiom
   boundary in future Lean work, or must await/import a formal flow library.
3. Select the Lean outer-shell route when L1 is issued: expansion-first,
   adaptive flow-first, or staged implementation of both.
4. Decide whether the route-comparison table belongs in the canonical chapter,
   Paper A only, or both.
5. Authorize the proposed edits to `FORMAL_STATUS.md` and
   `PUBLICATION_PROGRAM.md`; this worker has not applied them.
6. Route independent source/proof review before publication claims are upgraded.

No mathematical obstruction was found within the accepted scope.

## 9. Restrictions audit

- Lean edits: none.
- Frozen M1/M2/adaptive branch edits: none.
- Direct write to canonical `main`: none.
- Public theorem broadening: none.
- Merge, rebase, force-push, tag, release, DOI, or arXiv action: none.
- External input represented as machine-checked: no.
- Issue #11 closure: not requested; it remains open for Director disposition.

## 10. Requested disposition

**Requested:** `AffineCDC — Director` review for acceptance as the corrected
outer-shell canonical-promotion packet, with separate authorization for the
proposed canonical-file updates.

**Bounded unit complete:** yes, subject to Director audit and disposition.

## 11. Higher possibility found

**Yes, outside scope.** A canonical or automorphism-equivariant adaptive
ordering could reduce the functoriality gap and alter the Lean-route comparison.
Further possible directions are control of the omitted point/internal values and
extensions beyond exponent-two groups. No claim on these questions is made.
