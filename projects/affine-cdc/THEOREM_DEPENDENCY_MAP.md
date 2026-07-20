# AffineCDC theorem dependency map

This map separates the complete Cycle Double Cover theorem from the open five-support strengthening and records the exact Programme A, B1, and B2 proof layers.

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

Preferred Programme A chapters are under [`complete-cdc/`](complete-cdc/). Exact provenance is in [`PROGRAMME_A_INTEGRATION_MAP.md`](PROGRAMME_A_INTEGRATION_MAP.md).

## 2. Programme B1 graph-level DAG

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

All auxiliary data in this box are existential.

## 3. B1 fixed-data DAG

For fixed $(f,W)$:

```text
global five-coordinate slice
↔ even distinguished support D
↔ component T-join condition
↔ one outside-colour parity vanishes
↔ all outside-colour parities vanish
↔ outside-colour classes Eulerian after contraction
↔ local affine component obstruction vanishes.
```

For fixed $f$:

```text
factorable five-coordinate lift above f
↔ ∃ plane W with 𝔒_f(W)=∅.
```

For fixed compatible lift $g$:

```text
compatible root lift g
↔ coloured cycle-face surface S_g
↔ coloured full dual triangulation T_g

componentwise compression of the same embedding
↔ T_g^(1) → 𝒜₅.
```

For an external root flow on a prescribed dual:

```text
root flow integrates to a dual potential
↔ every dual cycle has zero holonomy.
```

The old-colour quotient $J_g$ classifies only fibre-constant factorable maps.

## 4. Programme B2 complete-witness DAG

Programme B2.1 and B2.2 enlarge the graph-level equivalence box with explicit reconstruction maps:

```text
five indexed supports
↔ R₅-valued flow
↔ K₅-triangle labelling
↔ anisotropic O⁻(4,2) flow
↔ cycle words b,d,x,y with b*d=(1+x)*(1+y)
↔ cycle-continuous edge map M(G) → M*(K₅).
```

The coordinate reconstruction is

$$
\Phi(b,d,x,y)
=(b,d,b+d+y,b+d+x,b+d+x+y).
$$

The cographic map is an arbitrary ground-set map whose inverse image sends every target binary cycle, equivalently every cut of $K_5$, to a source binary cycle. No stronger matroid-map property is included.

## 5. B2 singular and Schur DAG

Fix a minus-type four-space $(H,q)$, a nonzero singular vector $k$, and a quotient Fano flow in $H/\langle k\rangle$.

```text
anisotropic H-flow lift
↔ kernel-line component defect vanishes
↔ B1 fixed-plane colour-cut obstruction vanishes
↔ eliminated cycle word d exists
↔ x*y is a cycle on the contracted quotient Q_b.
```

This box is an exact fixed-data equivalence only when the quotient flow, kernel or plane, quotient graph, and lift torsor are retained.

The boundary word alone is a projection with lost lift data.

## 6. B2 dual and counting DAG

For a fixed fibre-evaluation map $\rho_F$ with image code $\mathcal C_F$:

```text
prescribed target is attainable
↔ displacement lies in 𝒞_F
↔ every relative stress in 𝒞_F^⊥ annihilates it.
```

When attainable, a primal preimage reconstructs the translated lift.

For a nonlinear allowed set $A$:

```text
allowed lift exists in the fixed orbit
↔ 𝒞_F ∩ A ≠ ∅
↔ |𝒞_F ∩ A| > 0,
```

where

$$
|\mathcal C_F\cap A|
=
\frac{|\mathcal C_F|}{|Q_F|}
\sum_{y\in\mathcal C_F^\perp}\widehat{\mathbf1_A}(y).
$$

The Fourier spectrum is an exact count. A positive count does not exhibit a primal witness; a zero count need not yield one separating stress.

## 7. B2 orthogonal correction node

The source packet `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md` is not a theorem node. It is superseded by B2.3.

```text
additive anisotropic roots of K_q with triangle addition
→ point-potential representation
→ Gram matrix J+I of rank q−2
→ dimension lower bound dim V ≥ q−2
→ deleted permutation module attains q−2.
```

Consequences:

- the proposed dimension $2r$ for $q=2^r$ is impossible for $r\ge4$;
- the correct universal module is $\overline E_I$ of dimension $q-2$;
- the eight-support $O^+(6,2)$ model is exceptional because $8-2=6$;
- there is no universal $O^+(2r,2)$ tower.

## 8. Formulation classification

| Formulation | Scope | Full source witness? |
|---|---|---:|
| five supports | graph level | yes |
| $R_5$ roots / $K_5$ triangles | graph level | yes |
| anisotropic $O^-(4,2)$ flow | graph level | yes |
| quadratic cycle solution | graph level | yes |
| cographic cycle-continuous edge map | graph level | yes |
| singular quotient | fixed flow/kernel | only after lift solve |
| Schur quotient | fixed coordinate quotient | only after solving for $d$ |
| component obstruction | fixed quotient | no |
| relative stress | fixed evaluation map | no, dual criterion |
| Fourier spectrum/count | fixed orbit | existence/count only |
| deleted permutation module | target model | no source witness |

## 9. B3+ boundary

Programme B2 does not consume:

- B3 target-link, quotient, and finite-capacity corrections;
- B4 vertical/horizontal reconfiguration;
- B5 cuts, four-poles, and routing;
- B6/B7 defect and localization theorems;
- B8 finite-certificate normalization;
- B9 global assembly.

The global five-support theorem remains open.

## 10. Exact provenance and assurance

- Programme A source: `8bee16780b549f51e1f29343671a059961ec4172`;
- Programme A candidate: `68715fb29bb4b6555e2bc3e089603c5390d01566`;
- Programme B1 source: `778b09ac8260192e022f512f24cdef1d04871f37`;
- Programme B2 source: `d62974704d6dac77aaa00275a595fedf7f70cfd2`;
- B2 exact map: [`PROGRAMME_B2_INTEGRATION_MAP.md`](PROGRAMME_B2_INTEGRATION_MAP.md);
- B2 witness scope: [`PROGRAMME_B2_WITNESS_SCOPE.md`](PROGRAMME_B2_WITNESS_SCOPE.md).

Programme A, B1, and B2 are integrated authorial mathematics in their stated scopes. Independent audit, Lean verification, manuscript acceptance, peer review, publication, release, arXiv, DOI, novelty, and timestamp status remain separate axes.
