# AffineCDC theorem dependency map

This map separates the complete Cycle Double Cover theorem from the open five-support strengthening and records the exact B1 object/quantifier layer.

## 1. Complete theorem DAG

```text
A0  finite-active multigraph, cut, intrinsic parity, circuit, and occurrence semantics
├── A1  loop deletion and exact two-occurrence reinsertion
└── A2  loopless port-cycle cubic expansion and collapse data
    └── A3  Seymour six-flow boundary and internal order-eight group-flow transport
        └── A4  affine pair complex, quotient equation, and stress obstruction
            └── A5  rank-three quadratic-Lagrangian compatibility
                └── A6  graph/dart indexed even-support extraction
A0 + A6 ── A7  loopless vertex/boundary/cut parity equivalence
A2 + A6 + A7 ── A8  cut-even collapse and exact occurrence transport
A0 + A8 ── A9  terminating finite circuit decomposition
A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 ── A10 final theorem
```

Preferred integrated chapters:

- [`complete-cdc/foundations-expansion-and-flow.md`](complete-cdc/foundations-expansion-and-flow.md): A0–A3;
- [`complete-cdc/affine-compatibility-and-extraction.md`](complete-cdc/affine-compatibility-and-extraction.md): A4–A7;
- [`complete-cdc/collapse-decomposition-and-assembly.md`](complete-cdc/collapse-decomposition-and-assembly.md): A8–A10.

Exact Programme A provenance is in [`PROGRAMME_A_INTEGRATION_MAP.md`](PROGRAMME_A_INTEGRATION_MAP.md).

## 2. Complete-theorem output chain

```text
finite-active no-singleton-cut multigraph
→ loopless core
→ cubic expansion
→ F₂³ flow
→ compatible affine family
→ indexed intrinsic even cover upstairs
→ indexed intrinsic even cover downstairs
→ circuit double cover of the core
→ circuit double cover after loop reinsertion
```

Seymour’s six-flow theorem is the sole external non-elementary logical input. Programme A proves the order-eight group-flow transport internally.

## 3. Programme B1 graph-level equivalence DAG

For a finite loopless cubic multigraph $G$:

```text
B1.1  five indexed even supports
  ↔   R₅-valued E₅ flow
  ↔   K₅-triangle edge labelling

B1.2  above object
  ↔   even supports B,D + matching M=B∩D + nowhere-zero F₂²-flow on G−M
  ↔   even B + matching M⊆B + four-flow on G−M
       + even M-endpoint parity in every component of G−B

B1.3  above object
  ↔   ∃ Fano flow f and plane W with empty component-obstruction profile

B1.4  above object
  ↔   ∃ cycle-face embedding S with T_S^(1) → 𝒜₅
```

All auxiliary data in this box are existential. The graph-level arrows do not preserve a previously fixed flow, plane, lift, or embedding.

## 4. B1 fixed-flow DAG

Fix a nowhere-zero Fano flow $f$ and a plane $W$. Let $G_W$ be the $W$-valued subgraph and let $\chi_W(K)$ be the common outside-colour cut parity of a component $K$.

```text
fixed (f,W) global five-coordinate slice
↔ even support D with B_W∩D=M_a
↔ even M_a-endpoint parity in every component of G_W
↔ one outside-colour parity vanishes on every component
↔ all outside-colour parities vanish on every component
↔ outside-colour classes are Eulerian after contraction
↔ local affine component obstruction Ω_W vanishes
```

For fixed $f$:

```text
factorable five-coordinate lift above f
↔ ∃ plane W with 𝔒_f(W)=∅.
```

This criterion may fail for a prescribed flow. Such failure is not a graph-level counterexample.

## 5. B1 fixed-lift and prescribed-surface DAG

Fix a compatible root lift $g$.

```text
compatible root lift g
↔ properly face-coloured cycle-face surface S_g
↔ properly vertex-coloured full dual triangulation T_g
```

The exact fixed-lift biconditional is:

```text
componentwise compression of the same face components
↔ T_g^(1) → 𝒜₅.
```

For an externally supplied root flow $\lambda$ on the prescribed dual:

```text
λ integrates to a dual potential
↔ every dual cycle has zero λ-holonomy.
```

Triangular-face conservation alone is insufficient.

## 6. Full dual versus old-colour quotient

The old support-colour map gives

```text
T_g^(1) → J_g.
```

A half-cube map factors through $J_g$ exactly when it is constant on all face components carrying the same old support index.

```text
J_g → 𝒜₅
= old-colour-factorable subclass only.
```

It is not the complete fixed-lift criterion.

## 7. Half-cube parity adapter

If $\mathscr A_5$ denotes the even half-cube, singleton words $\varepsilon_i$ are not vertices. Choose one odd word $t$ and use

$$
t+\varepsilon_i\in E_5.
$$

The pairwise differences remain the roots $\varepsilon_i+\varepsilon_j$.

## 8. Safe fixed-data implication hierarchy

For corresponding fixed flow and lift:

```text
global five-point slice
→ J_g → 𝒜₅
→ T_g^(1) → 𝒜₅
→ five-support cover.
```

The converses need not hold for the same fixed data.

## 9. Six B1 corrections

1. A support-coordinate inverse image is even; a root-label inverse image is a matching.
2. Bare matching plus four-flow is insufficient; $(B,D)$ or component $T$-join data are required.
3. The fixed-$g$ biconditional concerns componentwise compression of the same embedding.
4. An external cover integrates on a prescribed dual only after zero dual holonomy is proved.
5. $J_g$ classifies only old-colour-factorable compression.
6. Singleton words require an odd translation when the target is the even half-cube.

## 10. Boundary with B2+

Programme B1 closes the root object, matching/four-flow, fixed-plane, fixed-lift, surface, holonomy, quotient-scope, and parity layers.

It does not consume or close the later dossiers for:

- singular, quadratic, Schur, cographic, orthogonal, or Fourier/stress formulations;
- target link and finite-certificate corrections;
- gauge/reconfiguration closure;
- four-pole, defect, atom, or localization theorems.

These remain B2+ obligations and must be integrated from separately named immutable checkpoints.

## 11. Exact provenance and assurance

- Programme A source: `8bee16780b549f51e1f29343671a059961ec4172`;
- Programme A candidate: `68715fb29bb4b6555e2bc3e089603c5390d01566`;
- Programme B1 source: `778b09ac8260192e022f512f24cdef1d04871f37`;
- B1 exact map: [`PROGRAMME_B1_INTEGRATION_MAP.md`](PROGRAMME_B1_INTEGRATION_MAP.md);
- quantifier control: [`PROGRAMME_B1_QUANTIFIER_BOUNDARIES.md`](PROGRAMME_B1_QUANTIFIER_BOUNDARIES.md).

Programme A and B1 are integrated authorial mathematics. Independent audit, Lean verification, manuscript acceptance, peer review, publication, release, arXiv, DOI, and timestamp status remain separate axes.
