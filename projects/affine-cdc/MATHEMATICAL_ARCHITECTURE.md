# AffineCDC mathematical architecture

This file separates the complete Cycle Double Cover theorem from the open five-support strengthening and identifies the current controlling proof interfaces.

## 1. Three scopes

1. **Affine compatibility core** — rank-three compatible affine families on finite loopless cubic graphs with nowhere-zero binary flow.
2. **Complete CDC theorem** — the Programme A finite-active multigraph theorem, including loops, collapse, decomposition, and exact occurrence multiplicity.
3. **Five-support strengthening** — existence of five indexed even supports, equivalently a root-valued $E_5$ flow.

Scope 3 remains open and is not used in Scope 2.

## 2. Programme A architecture

The controlling theorem is:

> Every multigraph with finite active edge set and no singleton cut has a finite circuit double cover.

The preferred proof chain is:

```text
foundational multigraph and occurrence semantics
→ loop deletion
→ port-cycle cubic expansion
→ Seymour six-flow
→ internal order-eight group-flow transport
→ affine pair complex
→ rank-three compatibility
→ graph/dart indexed even-support extraction
→ loopless parity adapter
→ cut-even collapse
→ finite circuit decomposition
→ loop reinsertion.
```

Programme A remains the fixed Audit A candidate at

`curation/affine-cdc-programme-a-v1@68715fb29bb4b6555e2bc3e089603c5390d01566`.

This B1 descendant does not modify that branch or its audit target.

## 3. Programme B1 root object

For a finite loopless cubic multigraph $G$, the following graph-level existence data are equivalent:

- five indexed even supports with exact double coverage;
- an $R_5$-valued $E_5$ flow;
- a $K_5$-triangle edge labelling;
- exact matching/four-flow data $(B,D,M,w)$;
- the equivalent component $T$-join formulation;
- existence of a Fano flow and plane with empty component-obstruction profile;
- existence of a cycle-face embedding whose full dual maps to the even half-cube.

All auxiliary data are existential at graph level.

The preferred B1 chapter is [`five-support/b1-object-quantifier-and-scope.md`](five-support/b1-object-quantifier-and-scope.md).

## 4. Matching/four-flow boundary

A fixed support-coordinate inverse image is an even support. A fixed root-label inverse image is a matching.

The exact converse requires:

$$
B,D\text{ even},\qquad M=B\cap D\text{ a matching},
$$

and a nowhere-zero $\mathbf F_2^2$ flow on $G-M$.

Equivalently, replace $D$ by even $M$-endpoint parity in every component of $G-B$. Bare matching plus four-flow is insufficient.

## 5. Fixed Fano flow and plane

Fix a nowhere-zero Fano flow $f$ and a plane $W$. Let $G_W$ be the subgraph of $W$-valued edges.

For every component $K$ of $G_W$, the four outside-colour cut parities are equal. Their common bit is the component obstruction $\chi_W(K)$.

For fixed $(f,W)$, the following are equivalent:

- a global five-coordinate slice;
- the distinguished even support;
- the matching endpoint $T$-join condition;
- vanishing of one or all outside-colour cut parities;
- Eulerian outside-colour classes after contraction;
- vanishing of the local affine component obstruction.

For fixed $f$, factorable success requires some plane with empty profile. A prescribed flow may fail; this does not imply that the graph fails.

## 6. Fixed lift and full dual

A compatible root lift $g$ is equivalent to a properly face-coloured cycle-face surface $S_g$ and its properly vertex-coloured full dual triangular cellulation $T_g$.

The exact fixed-lift statement is:

$$
\text{componentwise compression of the same embedding}
\Longleftrightarrow
T_g^{(1)}\to\mathscr A_5.
$$

This does not classify arbitrary five-support covers on $G$ relative to the prescribed surface.

## 7. Prescribed-surface holonomy

An externally supplied root flow integrates to a potential on a fixed dual graph if and only if its sum vanishes on every dual cycle.

Local conservation checks triangular dual faces only. Residual dual holonomy may remain.

## 8. Old-colour factorability

The old-colour map gives

$$
T_g^{(1)}\to J_g.
$$

A half-cube map factors through $J_g$ exactly when it is constant on all face components carrying the same old support index.

Thus $J_g\to\mathscr A_5$ classifies only global-index-factorable compression. It is not the complete fixed-lift object.

## 9. Even-halfcube convention

If $\mathscr A_5$ denotes the even component, singleton words are not vertices. Choose one odd word $t$ and use

$$
t+\varepsilon_i\in E_5.
$$

Alternatively, name the odd component explicitly.

## 10. Safe fixed-data hierarchy

For corresponding fixed flow and lift:

```text
global five-point slice
→ J_g → 𝒜₅
→ T_g^(1) → 𝒜₅
→ five-support cover.
```

The converses need not hold at the same fixed data.

## 11. Boundary with B2 and later programmes

B1 closes the root object and quantifier layer. It does not consume the B2 singular/quadratic/Schur/cographic/orthogonal/Fourier dossiers or B3 target-correction dossiers.

Later formulations must be classified as full witness equivalences, fixed-data equivalences, quotients with lost lift data, dual obstructions, or evidence before entering the graph-level equivalence box.

The wider five-support architecture remains:

1. B1 root object and quantifiers;
2. B2 equivalent-formulation classification;
3. B3 surface/target construction and correction layer;
4. gauge and horizontal reconfiguration;
5. cuts, four-poles, and routing;
6. holonomy, defects, and atoms;
7. localization/composition frontier;
8. finite certificates.

## 12. Provenance and assurance

- Programme A map: [`PROGRAMME_A_INTEGRATION_MAP.md`](PROGRAMME_A_INTEGRATION_MAP.md);
- Programme B1 map: [`PROGRAMME_B1_INTEGRATION_MAP.md`](PROGRAMME_B1_INTEGRATION_MAP.md);
- B1 quantifier control: [`PROGRAMME_B1_QUANTIFIER_BOUNDARIES.md`](PROGRAMME_B1_QUANTIFIER_BOUNDARIES.md);
- exact authorial dossiers: [`proof-development/`](proof-development/).

Programme A and B1 are integrated authorial mathematics. This does not create independent-review, Lean, manuscript, peer-review, publication, release, arXiv, DOI, or timestamp status.
