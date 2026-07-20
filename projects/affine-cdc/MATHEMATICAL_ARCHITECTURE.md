# AffineCDC mathematical architecture

This file separates the complete Cycle Double Cover theorem from the open five-support strengthening and records the controlling Programme A, B1, and B2 interfaces.

## 1. Three scopes

1. **Affine compatibility core** — rank-three compatible affine families on finite loopless cubic graphs with nowhere-zero binary flow.
2. **Complete CDC theorem** — the Programme A finite-active multigraph theorem, including loops, collapse, decomposition, and exact occurrence multiplicity.
3. **Five-support strengthening** — existence of five indexed even supports, equivalently an anisotropic root flow in the ten-root orbit of $O^-(4,2)$.

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

## 3. Programme B1 object and quantifier layer

For a finite loopless cubic multigraph $G$, graph-level five-support existence is equivalent to:

- an $R_5$-valued flow;
- a $K_5$-triangle edge labelling;
- exact matching/four-flow data $(B,D,M,w)$;
- the component $T$-join form;
- existential Fano-flow/plane data with empty obstruction profile;
- an existential cycle-face embedding whose full dual maps to the even half-cube.

All auxiliary data are existential at graph level.

B1 also separates:

- fixed $(f,W)$ component obstruction;
- fixed $f$ with variable plane;
- fixed compatible lift and same-embedding componentwise compression;
- prescribed-dual holonomy;
- old-colour-factorable compression through $J_g$.

The preferred B1 chapter is [`five-support/b1-object-quantifier-and-scope.md`](five-support/b1-object-quantifier-and-scope.md).

## 4. Programme B2 mother witness

Put

$$
H_5=\left\{z\in\mathbf F_2^5:\sum_i z_i=0\right\},
\qquad
q_5(z)=\sum_{i<j}z_iz_j.
$$

The ten anisotropic vectors of this minus-type four-space are exactly the weight-two roots $R_5$.

The full graph-level witness hierarchy is:

```text
five indexed supports
↔ R₅-valued flow
↔ K₅-triangle labelling
↔ anisotropic O⁻(4,2) flow
↔ quadratic cycle solution (b,d,x,y)
↔ cycle-continuous edge map M(G) → M*(K₅).
```

The coordinate reconstruction is

$$
\Phi(b,d,x,y)
=(b,d,b+d+y,b+d+x,b+d+x+y),
$$

with equation

$$
b*d=(\mathbf1+x)*(\mathbf1+y).
$$

The cographic map means only an edge map whose inverse image sends target binary cycles, equivalently cuts of $K_5$, to source binary cycles.

## 5. Fixed singular quotient and Schur layer

Fix a four-dimensional minus-type space $(H,q)$, a nonzero singular vector $k$, and a quotient Fano flow in

$$
\Gamma=H/\langle k\rangle.
$$

The following are equivalent for the retained fixed data:

- anisotropic lifting;
- vanishing kernel-line component defect;
- B1 fixed-plane colour-cut obstruction;
- existence of the eliminated cycle word $d$;
- the Schur condition $x*y\in\mathcal C(Q_b)$.

When nonempty, the lifts form a torsor under the cycle space of the plane subgraph.

This is a fixed-data equivalence. The quotient flow, kernel or plane, contracted graph, and lift torsor are load-bearing. A boundary word alone is not a graph-level witness.

## 6. Stress and Fourier dual layers

For a fixed evaluation map, relative stresses are the orthogonal complement of the attainable code. They give an exact Fredholm alternative for a prescribed target.

For an allowed set $A$ in one fixed orbit,

$$
|\mathcal C_F\cap A|
=
\frac{|\mathcal C_F|}{|Q_F|}
\sum_{y\in\mathcal C_F^\perp}\widehat{\mathbf1_A}(y).
$$

The nonzero frequencies are relative stresses.

- a positive count proves existence in the fixed orbit;
- an explicit lift still requires a codeword and primal preimage;
- a zero count is aggregate spectral cancellation and need not produce one separating stress.

Stress and Fourier data are exact dual/ counting interfaces, not independent source witnesses.

## 7. Correct universal additive root module

The retired universal packet claimed that the complete graph on $2^r$ support points has a canonical additive anisotropic-root model of dimension $2r$. The formula is type-invalid without a chosen self-duality, and the theorem is impossible for $r\ge4$.

Triangle addition forces point potentials whose Gram matrix has rank $q-2$. Therefore

$$
\dim V\ge q-2.
$$

The correct universal module is

$$
\overline E_I
=
\left\{z\in\mathbf F_2^I:\sum_i z_i=0\right\}/\langle\mathbf1_I\rangle,
$$

with dimension $q-2$, quadratic form $q_I([z])=\operatorname{wt}(z)/2\pmod2$, and roots $[\varepsilon_a+\varepsilon_b]$.

The eight-support $O^+(6,2)$ realization is exceptional because $8-2=6=2\cdot3$. There is no universal $O^+(2r,2)$ tower.

## 8. Fixed lift and full dual

A compatible root lift $g$ is equivalent to a properly face-coloured cycle-face surface $S_g$ and its full dual triangular cellulation $T_g$.

The exact fixed-lift statement is:

$$
\text{componentwise compression of the same embedding}
\Longleftrightarrow
T_g^{(1)}\to\mathscr A_5.
$$

An external root flow integrates on a prescribed dual exactly when its sum vanishes on every dual cycle. The quotient $J_g$ classifies only maps constant on old-colour fibres.

## 9. Controlling B1 corrections

1. Support-coordinate inverse images are even; root-label inverse images are matchings.
2. Matching plus four-flow requires the second support or component $T$-join datum.
3. Fixed-$g$ compression is same-embedding componentwise compression.
4. Prescribed-surface integration requires zero dual holonomy.
5. $J_g$ is only the old-colour-factorable subclass.
6. Singleton words require an odd translation in the even half-cube.

## 10. Wider Programme B architecture

The remaining dependency order is:

1. B3 surface/target correction and capacity layer;
2. B4 vertical and horizontal reconfiguration;
3. B5 cuts, four-poles, and routing;
4. B6 holonomy, defects, and atoms;
5. B7 localization consequences;
6. B8 finite certificates;
7. B9 global assembly, still blocked at the genuine localization/composition frontier.

Programme B2 consumes no B3+ checkpoint.

## 11. Provenance and assurance

- Programme A map: [`PROGRAMME_A_INTEGRATION_MAP.md`](PROGRAMME_A_INTEGRATION_MAP.md);
- Programme B1 map: [`PROGRAMME_B1_INTEGRATION_MAP.md`](PROGRAMME_B1_INTEGRATION_MAP.md);
- Programme B2 map: [`PROGRAMME_B2_INTEGRATION_MAP.md`](PROGRAMME_B2_INTEGRATION_MAP.md);
- B2 witness control: [`PROGRAMME_B2_WITNESS_SCOPE.md`](PROGRAMME_B2_WITNESS_SCOPE.md);
- exact authorial dossiers: [`proof-development/`](proof-development/).

Programme A, B1, and B2 are integrated authorial mathematics in their stated scopes. This does not create independent-review, Lean, manuscript, peer-review, publication, release, arXiv, DOI, novelty, or timestamp status.
