# AffineCDC current mathematical state

## 1. Complete Cycle Double Cover line

Programme A supplies a complete authorial paper-proof of:

> Every multigraph with finite active edge set and no singleton cut has a finite circuit double cover.

The fixed Audit A candidate remains

`curation/affine-cdc-programme-a-v1@68715fb29bb4b6555e2bc3e089603c5390d01566`.

The controlling proof remains under [`complete-cdc/`](complete-cdc/). Programme B1 and B2 descendants do not modify that candidate or its audit status.

## 2. Programme B1 object and quantifier layer

Exact immutable B1 source:

`proof-development/affine-cdc-rigour-v1@778b09ac8260192e022f512f24cdef1d04871f37`.

For a finite loopless cubic multigraph, graph-level five-support existence is equivalent to:

- an $R_5$-valued flow;
- a $K_5$-triangle edge labelling;
- exact matching/four-flow data $(B,D,M,w)$;
- the component $T$-join formulation;
- existential Fano-flow/plane data with empty obstruction profile;
- an existential cycle-face embedding whose full dual maps to the even half-cube.

B1 separately controls fixed $(f,W)$, fixed $f$, fixed lift, prescribed-dual holonomy, and old-colour quotient scopes.

## 3. Programme B2 witness hierarchy

Exact immutable B2 source:

`proof-development/affine-cdc-rigour-v1@d62974704d6dac77aaa00275a595fedf7f70cfd2`.

The complete graph-level witness box is now:

$$
\boxed{
\begin{array}{c}
\text{five indexed supports}\\
\Updownarrow\\
R_5\text{-valued flow}\\
\Updownarrow\\
K_5\text{-triangle labelling}\\
\Updownarrow\\
O^-(4,2)\text{ anisotropic flow}\\
\Updownarrow\\
\exists(b,d,x,y)\in\mathcal C(G)^4:\ b*d=(\mathbf1+x)*(\mathbf1+y)\\
\Updownarrow\\
M(G)\to M^*(K_5)\text{ cycle-continuous edge map}.
\end{array}}
$$

The cographic map is an arbitrary ground-set map whose inverse image sends every target binary cycle, equivalently every cut of $K_5$, to a source binary cycle. No strong-map, quotient, embedding, injectivity, or surjectivity property is implied.

## 4. Fixed-data and dual boundaries

For a fixed singular quotient, the following are equivalent only with the quotient flow, singular line or plane, quotient graph, and lift torsor retained:

- anisotropic lifting;
- vanishing component lift defect;
- fixed-plane colour-cut obstruction;
- existence of the eliminated cycle word $d$;
- the Schur condition $x*y\in\mathcal C(Q_b)$.

A Schur boundary word alone is not a five-support witness.

Relative stresses give an exact Fredholm criterion for one prescribed target. Fourier gives an exact count of allowed assignments in one fixed affine orbit. Neither layer alone is a source witness:

- positive Fourier count proves existence but not an exhibited lift;
- an explicit lift still requires a codeword and primal preimage;
- zero count gives aggregate spectral cancellation and need not yield one separating stress.

## 5. Orthogonal mathematical correction

The retired packet `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md` contains a false theorem. Its displayed evaluation map is type-invalid without a chosen self-duality, and no $2r$-dimensional model can realize all additive roots of $K_{2^r}$ for $r\ge4$.

Every additive anisotropic representation of $K_q$ satisfying triangle addition obeys

$$
\dim V\ge q-2.
$$

The correct universal module is the deleted permutation module

$$
\overline E_I
=
\left\{z\in\mathbf F_2^I:\sum_i z_i=0\right\}/\langle\mathbf1_I\rangle,
$$

of dimension $q-2$, with roots $[\varepsilon_a+\varepsilon_b]$.

The eight-support $O^+(6,2)$ model is exceptional because $8-2=6$. It is not the first member of a universal $O^+(2r,2)$ hierarchy. The false packet is retained only as `SUPERSEDED / FALSE THEOREM / HISTORICAL PROVENANCE`.

## 6. B1 scope corrections retained

1. A support-coordinate inverse image is even; a root-label inverse image is a matching.
2. Bare matching plus four-flow is insufficient without the second even support or component $T$-join datum.
3. The fixed-$g$ half-cube biconditional concerns componentwise compression of the same embedding.
4. An external root flow integrates on a prescribed dual only when all dual cycle holonomies vanish.
5. $J_g$ classifies only old-colour-factorable compression.
6. Singleton words require an odd translation when the target is the even half-cube.

## 7. B3+ exclusion and frontier

This candidate consumes no B3 target correction, B4 reconfiguration, B5 cut/routing, or later PDL delta. Those remain separate immutable-intake units.

The global five-support theorem remains open. The wider sharp endpoint remains graph-level localization and composition of full-rank route-locked defects.

## 8. Assurance state

Programme B2 is:

`CURATOR-INTEGRATED / AUTHORIAL B2 PROOF LAYER COMPLETE / MATHEMATICAL CORRECTION INSTALLED`.

Programme B1 remains integrated in its prior scope. Neither B1 nor B2 has received dedicated independent audit or end-to-end Lean verification. No manuscript, peer-review, publication, release, arXiv, DOI, novelty, or timestamp status is created.

## 9. Reading order

- complete theorem: [`complete-cdc/README.md`](complete-cdc/README.md);
- B1 object and quantifiers: [`five-support/b1-object-quantifier-and-scope.md`](five-support/b1-object-quantifier-and-scope.md);
- B2 witness hierarchy: [`five-support/b2-formulation-and-witness-hierarchy.md`](five-support/b2-formulation-and-witness-hierarchy.md);
- B2 exact map: [`PROGRAMME_B2_INTEGRATION_MAP.md`](PROGRAMME_B2_INTEGRATION_MAP.md);
- B2 witness scope: [`PROGRAMME_B2_WITNESS_SCOPE.md`](PROGRAMME_B2_WITNESS_SCOPE.md);
- theorem DAG: [`THEOREM_DEPENDENCY_MAP.md`](THEOREM_DEPENDENCY_MAP.md);
- architecture: [`MATHEMATICAL_ARCHITECTURE.md`](MATHEMATICAL_ARCHITECTURE.md);
- assurance: [`FORMAL_STATUS.md`](FORMAL_STATUS.md).
