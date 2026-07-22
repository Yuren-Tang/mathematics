# Equivalent formulations and proof families

## 1. Purpose

Programme B2 classifies five-support formulations by witness content.

1. **Full graph-level witnesses** reconstruct the five indexed supports.
2. **Fixed-data solvability criteria** are equivalent only while the quotient flow, kernel or plane, quotient graph, and lift torsor are retained.
3. **Dual and counting layers** decide prescribed or nonlinear fixed-orbit problems but are not independent source witnesses.
4. **Historical or finite evidence** remains recoverable without being promoted beyond its proved scope.

The controlling detailed chapter is [`b2-formulation-and-witness-hierarchy.md`](b2-formulation-and-witness-hierarchy.md).

## 2. Complete graph-level witness box

For a finite loopless cubic multigraph $G$, the following are equivalent:

1. five indexed even supports;
2. an $R_5$-valued flow;
3. a $K_5$-triangle edge labelling;
4. an anisotropic flow in the minus-type four-space $(H_5,q_5)$;
5. cycle words $b,d,x,y\in\mathcal C(G)$ satisfying $b*d=(\mathbf1+x)*(\mathbf1+y)$;
6. a cycle-continuous edge map $E(G)\to E(K_5)$ whose inverse image sends every target cut to a source binary cycle.

The coordinate isomorphism is

$$
\Phi(b,d,x,y)=(b,d,b+d+y,b+d+x,b+d+x+y).
$$

The cographic phrase means only the inverse-cycle condition for a ground-set map $M(G)\to M^*(K_5)$. No strong-map, quotient, embedding, injectivity, or surjectivity property is implied.

The B1 matching/four-flow and existential Fano-plane descriptions remain additional graph-level equivalences with their exact data and quantifiers.

## 3. Fixed singular and Schur package

Fix a four-dimensional minus-type space $(H,q)$, a nonzero singular kernel vector $k$, and a nowhere-zero quotient Fano flow in $\Gamma=H/\langle k\rangle$.

The following are equivalent for this fixed data:

1. an anisotropic $H$-flow lift;
2. vanishing kernel-line defect on each plane-subgraph component;
3. vanishing B1 fixed-plane colour-cut obstruction;
4. existence of the eliminated cycle word $d$;
5. the Schur condition $x*y\in\mathcal C(Q_b)$.

When solutions exist they form the same lift torsor in different coordinates. A Schur boundary word, quotient residue, or component bit alone is not a five-support witness.

## 4. Direct colour-cut proof family

For fixed $(f,W)$, contract each $W$-valued component. The four outside colours form one affine $W$-plane, and their only nonzero binary relation is their total sum. Therefore the four colour parities at every quotient vertex are either $0000$ or $1111$. This gives the shortest proof of the fixed-plane criterion and identifies the same obstruction seen by singular lifting and the Schur boundary.

## 5. Quadratic and Schur proof family

The quadratic equation is a complete graph-level witness because all four cycle coordinates are retained and $\Phi$ reconstructs the five supports. The Schur quotient eliminates $d$; it is a complete fixed-data solvability criterion, but not a full witness until the incidence equation is solved.

## 6. Cographic proof family

The cographic edge map retains the complete edgewise root label. Its star preimages are the five supports, and its inverse-cut condition is exactly coordinatewise flow conservation. Cycle-continuous edge maps compose, but every intermediate theorem still requires its own hypotheses and source audit.

## 7. Stress/Fredholm proof family

For a fixed evaluation map, relative stresses form the orthogonal complement of the attainable code. A prescribed target is attainable exactly when every relative stress annihilates its displacement from the base lift. When attainable, a primal preimage reconstructs the translated lift. The stress space is therefore an exact dual criterion, not a source witness by itself.

## 8. Fourier proof family

For an evaluation code $\mathcal C_F$ and allowed set $A$,

$$
|\mathcal C_F\cap A|=
\frac{|\mathcal C_F|}{|Q_F|}
\sum_{y\in\mathcal C_F^\perp}\widehat{\mathbf1_A}(y).
$$

The nonzero frequencies are relative stresses. Positive count proves existence in the fixed orbit; an explicit witness still requires a codeword and primal preimage. Zero count gives aggregate spectral cancellation; one separating stress need not exist for a nonlinear product set.

## 9. Orthogonal proof family: exact source and separate correction

### Exact rank-three/eight-support source

`FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`, blob `2043ada9d28789ecc5f4f0028e62133f37835bc1`, is retained as theorem-level historical provenance for:

- $H_8$, the Hamming kernel, and the moment map;
- the six-dimensional plus-type quotient $O^+(6,2)$;
- its twenty-eight complete-graph roots;
- rank-three compatible root lifts;
- five-coordinate $O^-(4,2)$ slices and omitted-triple orthogonality.

It is not false in toto and is not history-only. Its scope is fixed-dimensional.

### Source-unreconstructed extrapolation

No committed source was recovered for the arbitrary-rank $\Gamma\oplus\Gamma^*$ / $d_h(a)$ / $O^+(2r,2)$ complete-root tower. That proposition is a separate non-packet item:

`SOURCE-UNRECONSTRUCTED / INFERRED-EXTRAPOLATION OR UNCOMMITTED DRAFT / MATHEMATICALLY REFUTED BY B2.3`.

Triangle addition forces a Gram matrix of rank $q-2$, hence

$$
\dim V\ge q-2.
$$

The correct universal additive module is

$$
\overline E_I=\left\{z\in\mathbf F_2^I:\sum_i z_i=0\right\}/\langle\mathbf1_I\rangle,
$$

with roots $[\varepsilon_a+\varepsilon_b]$ and dimension $q-2$. The equality $8-2=6=2\cdot3$ makes rank three exceptional. There is no universal $O^+(2r,2)$ tower.

The genuine all-rank transgression/residue hierarchy remains a distinct valid proof family; it does not supply the extrapolated complete-root theorem.

## 10. Surface and half-cube proof family

The B1 full-dual criterion remains

$$
\text{componentwise compression of the fixed embedding}
\Longleftrightarrow T_g^{(1)}\to\mathscr A_5.
$$

The old-colour quotient $J_g$ classifies only fibre-constant factorable maps. An external root flow integrates on a prescribed dual only when all dual cycle holonomies vanish.

## 11. Sufficient templates and later families

The following remain sufficient subroutes rather than necessary formulations:

- one global-index-factorable map $J_g\to\mathscr A_5$;
- an unused three-matching;
- a vanishing affine-plane residue;
- an orientable good lift;
- a target pivot with separately proved source realization.

Gauge motion, target-link corrections, four-pole routing, defects, atoms, and localisation belong to B3 and later exact intakes.

## 12. Preservation and assurance

The exact B1 and source-fidelity-repaired B2 dossiers remain under `proof-development/`; the controlling repair checkpoint is `9ce8de5ca5b7b41e139be4c94572de7725446046`. Retired public packets remain recoverable as source and priority history.

Programme B2 integration is substantive mathematical curation. It is not independent audit, Lean formalization, manuscript approval, peer review, publication, release, arXiv, DOI, or novelty determination. Programme A, B1, B3–B8, the six frontier obligations, and the open global five-support status are unchanged.