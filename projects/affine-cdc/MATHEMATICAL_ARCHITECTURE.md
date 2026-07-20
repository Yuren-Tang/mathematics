# AffineCDC mathematical architecture

## 1. Project scopes

1. **Affine compatibility core** — compatible affine families above nowhere-zero binary flows.
2. **Complete Cycle Double Cover theorem** — Programme A.
3. **Five-support strengthening** — five indexed even supports, equivalently an `R_5`-valued flow.

The complete CDC theorem is authorially proved. The five-support strengthening remains open and is not used in Programme A.

## 2. Programme A — complete CDC

Controlling theorem:

> Every multigraph with finite active edge set and no singleton cut has a finite circuit double cover.

Fixed Audit A candidate:

`curation/affine-cdc-programme-a-v1@68715fb29bb4b6555e2bc3e089603c5390d01566`.

The proof chain remains under `complete-cdc/`; the B3–B8 intake changes neither that branch nor its assurance status.

## 3. B1 — exact object and quantifiers

For a finite loopless cubic multigraph, graph-level five-support existence is equivalent to:

- an `R_5` root flow;
- a `K_5`-triangle labelling;
- exact matching/four-flow data;
- the component `T`-join formulation;
- existential Fano-flow/plane data with empty obstruction profile;
- an existential cycle-face surface whose full dual maps to the even half-cube.

B1 separately controls fixed `(f,W)`, fixed `f`, fixed lift, prescribed-dual holonomy, and old-colour-factorable scopes.

## 4. B2 — witness hierarchy and orthogonal correction

Complete graph-level witnesses are:

```text
five supports
↔ R₅ root flow
↔ K₅ triangles
↔ anisotropic O⁻(4,2) flow
↔ quadratic cycle solution
↔ cycle-continuous edge map M(G) → M*(K₅).
```

Singular and Schur formulations are complete fixed-data criteria only with the quotient flow, kernel/plane, quotient graph, and lift torsor retained. Stress and Fourier are dual solvability/counting layers.

The false universal `2r` orthogonal-root theorem is superseded by the sharp dimension lower bound `q-2` and the deleted permutation module. The eight-support `O^+(6,2)` model is exceptional.

## 5. B3 — target hierarchy

For fixed compatible lift `g`:

$$
J_g\to\mathscr A_5
\Longrightarrow
T_g^{(1)}\to\mathscr A_5
\Longrightarrow
\text{five-support cover}.
$$

- `T_g^{(1)}` is the full componentwise dual.
- `J_g` is the old-colour quotient.
- factorable failure does not imply full-dual failure.

B3 integrates:

- quadratic common-link formula;
- exact half-cube link table;
- dominating-clique capacity;
- exact eight-vertex factorable classification;
- factorable unused-matching and core theory;
- conditional full-dual flower obstruction.

The all-parallel matching representative is corrected to `\{01,23,45\}`; the orbit theorem remains unchanged.

## 6. B4 — two-level motion

The total state space has vertical fibres over nowhere-zero Fano flows.

### Vertical

Labelled lifts above `f` form a torsor under `H_f^0`; the reduced gauge code is

$$
H_f^0/\Gamma^{\pi_0(G)}.
$$

Gauge bits are exactly accessible partial Petrials.

### Horizontal

One reconfiguration edge is a constant switch on one connected source cycle. A disconnected cycle word is a commuting path. A support-cycle pivot is a special connected switch preserving the uncoloured embedding and providing one explicit new lift.

After switching, the new gauge fibre must be recomputed.

Internal fixed-plane correction is a composite fixed-quotient linear problem. External correction is quotient reslicing. Connected adjacency is an extra nonlinear support condition.

## 7. B5 — cuts and interfaces

The source-interface spine is:

```text
cubic local support law
→ cyclic three-cut gluing
→ ten four-pole states
→ exact profile-intersection gluing
→ cap forcing
→ Kempe path-pairing alignment
→ routing weights
→ uniform-routing elimination.
```

Cap forcing does not imply full-cap containment. The four residual mismatch kernels and Type T/Type H policies are finite state classifications; source path realizability remains separate.

## 8. B6 — corrected holonomy and atoms

Unconditional theorem layer:

- individual-loop affine holonomy and norm;
- genuine path-family switch flow;
- root-fibre section problem;
- root lifting iff Tait resolution;
- Type H soluble-branch escape;
- DDD atom triality and unique bad route;
- local `K_6`/Petersen geometry when a defect strip is independently supplied.

### Correction

BBD simultaneous origin is conditional on `AC-RL-BBD-GROUPOID-CLOSURE`.

The nontrivial defect-minimal forest is removed from the active theorem layer because the stated fixed-terminal variation domain contains the original root cover as a zero-defect competitor. A replacement needs `AC-RL-BBD-VARIATION-SLICE`.

## 9. B7 — rank, curvature, and localization

- rank one is impossible;
- rank two is a Tait/root-triangle escape;
- full rank has an exact flat/nonflat curvature dichotomy;
- flatness gives an eight-state affine potential;
- nonflatness gives a common scalar-sheet cut with odd terminal parity.

These results do not yet provide source graph localization or bounded composition data.

Exact open returns:

- `AC-RL-TYPE-T-SERIALISATION`;
- `AC-RL-FLAT-POTENTIAL-INTERFACE`;
- `AC-RL-COMMON-CUT-LOCALISATION`;
- `AC-RL-TYPE-H-COMMON-WITNESS`.

Together with the two BBD gaps, these are the six controlling open obligations.

## 10. B8 — finite assurance

Finite claims are classified as:

- `F-PROVED`;
- `F-CERT-PUBLIC`;
- `F-CERT-PRIVATE`;
- `F-CENSUS`;
- `CODE-PARTIAL`;
- `AFFECTED`.

B8 propagates the B2, B3, B4, and B6 corrections to every finite table. It is not independent mathematical review or a reproducibility upgrade.

## 11. Global frontier

The remaining theorem must convert persistent vertically and horizontally bad data into either:

1. an escaping good state; or
2. strict source progress through a smaller separator, bounded replacement, composition-safe factor, or exact gluing theorem.

A target census, scalar-sheet cut, finite potential range, or finite routing automaton is not sufficient by itself.

Programme B9/global assembly remains blocked at this localization/composition frontier.

## 12. Exact provenance

- B3: `d806168bb579dbc13f267f44f631e07de909b706`;
- B4: `345074690b7a8658c1208ae84f10d709f8b74bcf`;
- B5: `274970ef9c56cafdbfceeed3c0cc08238d3dfd40`;
- B6: `404f7511f16d1225e066a91842a57e2084943c72`;
- B7: `164f7655f9ec7c0e0a73d49303cf66230fb26487`;
- B8: `989cb002598fd91786029be201c2747c697bb476`.

See `PROGRAMME_B3_B8_INTEGRATION_MAP.md` and `PROGRAMME_B3_B8_STATUS_AND_GAPS.md`.

## 13. Assurance boundary

Programme A and B1–B8 are Curator-integrated authorial mathematics or assurance layers in their stated scopes. This does not create independent-review, Lean, manuscript, peer-review, publication, release, arXiv, DOI, novelty, or timestamp status.