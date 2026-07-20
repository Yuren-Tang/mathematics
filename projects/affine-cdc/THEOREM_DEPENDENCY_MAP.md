# AffineCDC theorem and obligation dependency map

## 1. Complete CDC DAG

```text
A0 foundational finite-active multigraph semantics
├─ A1 loop deletion/reinsertion
└─ A2 cubic expansion/collapse data
   └─ A3 Seymour six-flow + internal order-eight transport
      └─ A4 affine pair complex
         └─ A5 rank-three compatibility
            └─ A6 graph/dart even-support extraction
A0 + A6 → A7 parity bridge
A2 + A6 + A7 → A8 collapse and multiplicity transport
A0 + A8 → A9 circuit decomposition
A1–A9 → A10 complete CDC theorem.
```

Programme A remains fixed at `68715fb29bb4b6555e2bc3e089603c5390d01566`.

## 2. B1 graph-level and fixed-data nodes

```text
five supports
↔ R₅ flow
↔ K₅ triangles
↔ exact matching/four-flow data
↔ ∃ Fano flow/plane with empty profile
↔ ∃ cycle-face embedding with full dual → 𝒜₅.
```

Fixed-data branches:

- fixed `(f,W)` component obstruction;
- fixed `f`, variable plane;
- fixed lift `g`, same-embedding componentwise map;
- external root flow on prescribed dual, subject to zero holonomy;
- old-colour-factorable quotient `J_g`.

## 3. B2 witness and correction nodes

```text
R₅ flow
↔ anisotropic O⁻(4,2) flow
↔ quadratic cycle solution
↔ cographic cycle-continuous edge map.
```

```text
fixed singular quotient lift
↔ component defect vanishes
↔ fixed-plane obstruction vanishes
↔ eliminated coordinate exists
↔ Schur quotient condition.
```

Stress is the linear dual criterion for a prescribed target. Fourier is an exact count for one fixed affine orbit.

The false universal `2r` theorem is not a node. Its replacement DAG is:

```text
additive K_q roots + triangle addition
→ point potentials
→ Gram rank q−2
→ dim V ≥ q−2
→ deleted permutation module attains q−2.
```

## 4. B3 target DAG

```text
fixed compatible lift g
↔ cycle-face surface S_g
↔ full dual T_g
→ componentwise same-embedding problem T_g^(1) → 𝒜₅.
```

The old colouring gives

```text
T_g^(1) → J_g.
```

Hence

```text
J_g → 𝒜₅
→ T_g^(1) → 𝒜₅
→ five-support cover.
```

No reverse implication from full dual to `J_g` is automatic.

Target theorem nodes:

```text
quadratic common-link formula
→ exact half-cube link table
→ dominating-clique capacity.
```

```text
eight old colours
→ exact forbidden K₆ / K₈−C₅ classification
→ unused 3K₂ sufficient route
→ factorable two-apex/pentagon core
→ ideal target pivot depth.
```

The flower full-dual no-go is theorem-level conditional on its explicit dual certificate.

## 5. B4 motion DAG

```text
fixed f
→ H_f^0 torsor of labelled lifts
→ reduced gauge code H_f^0 / Γ^{π₀(G)}
→ accessible partial Petrials.
```

```text
connected source cycle C + direction a
→ one nowhere-zero horizontal switch
→ solve/construct new lift fibre.
```

```text
disconnected cycle word
→ edge-disjoint connected components
→ commuting path of connected switches.
```

A support-cycle pivot is a special connected switch:

```text
support component C + absent root cd
→ explicit new lift
→ fixed uncoloured dual
→ exact used/unused-root update.
```

After any switch, the new gauge fibre is recomputed.

Fixed-plane transport splits:

```text
internal direction
→ fixed quotient
→ composite linear correction image
→ connected-neighbour subset.
```

```text
external direction
→ quotient reslicing
→ even supports B' ⊇ M for composite endpoints
→ connected symmetric difference for one adjacency.
```

## 6. B5 separator/interface DAG

```text
cubic local support law
→ cyclic three-cut gluing
→ cyclically four-edge-connected minimal case.
```

```text
four-pole
→ ten boundary states / 640 ordered assignments
→ exact profile intersection for gluing
→ cap forcing
→ terminal path-pairing alignment
→ routing weights and fixed-route sectors
→ uniform-routing elimination
→ residual Type T or Type H mechanism.
```

Finite mismatch kernels and policy tables do not imply source realizability.

## 7. B6 corrected holonomy DAG

Unconditional:

```text
individual physical loop
→ affine monodromy + cyclic norm
→ root-fibre local system
→ genuine three-path switch flow
→ root lifting iff Tait resolution
→ soluble Type H escape.
```

DDD branch:

```text
co-root atom
→ three resolution pairings
→ unique bad route
→ locked quotient, conditional on finite challenge table.
```

Conditional BBD branch:

```text
AC-RL-BBD-GROUPOID-CLOSURE
→ physical root-preserving groupoid
→ global translation-kernel/cohomology argument
→ simultaneous common origin.
```

The old nontrivial forest node is removed. Any replacement requires:

```text
AC-RL-BBD-VARIATION-SLICE
→ valid nontrivial variation domain
→ possible defect-pruning theorem.
```

## 8. B7 rank/curvature DAG

```text
universally route-locked quotient
├─ rank 1 → impossible
├─ rank 2 → Tait/root-triangle section → Type H escape
└─ full rank → curvature Ω(c).
```

```text
Ω(c)=0
↔ affine local words
↔ eight-state potential.
```

```text
Ω(c)≠0
↔ common terminal-colour support
   cut in all four scalar sheets
   with odd terminal parity.
```

Localization arrows are open:

- `AC-RL-COMMON-CUT-LOCALISATION`;
- `AC-RL-FLAT-POTENTIAL-INTERFACE`;
- `AC-RL-TYPE-H-COMMON-WITNESS`;
- `AC-RL-TYPE-T-SERIALISATION`.

## 9. B8 assurance node

Every finite input is classified as `F-PROVED`, `F-CERT-PUBLIC`, `F-CERT-PRIVATE`, `F-CENSUS`, `CODE-PARTIAL`, or `AFFECTED`.

B8 changes assurance metadata, not mathematical truth or publication status.

## 10. B9/global frontier

Programme B9 is blocked on exact source implications:

```text
persistent bad state/component
→ good escape
or
→ strict source progress and composition.
```

Strict progress requires a smaller separator, bounded replacement, composition-safe factor, or exact gluing theorem. Target counts, finite automata, scalar-sheet cuts, and finite potential ranges are not sufficient alone.

## 11. Exact source checkpoints

- B3 `d806168bb579dbc13f267f44f631e07de909b706`;
- B4 `345074690b7a8658c1208ae84f10d709f8b74bcf`;
- B5 `274970ef9c56cafdbfceeed3c0cc08238d3dfd40`;
- B6 `404f7511f16d1225e066a91842a57e2084943c72`;
- B7 `164f7655f9ec7c0e0a73d49303cf66230fb26487`;
- B8 `989cb002598fd91786029be201c2747c697bb476`.

Exact map: `PROGRAMME_B3_B8_INTEGRATION_MAP.md`.

## 12. Assurance

These are Curator-integrated authorial theorem, correction, frontier, and assurance layers in their stated scopes. They are not independent audit, end-to-end Lean verification, manuscript acceptance, peer review, publication, release, arXiv, DOI, novelty, or timestamp status.