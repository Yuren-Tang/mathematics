# Equivalent formulations and proof families

## 1. Purpose

The five-support corpus contains many useful formulations. Programme B1 separates three classes:

1. graph-level witness equivalences proved in B1;
2. fixed-flow or fixed-lift equivalences whose quantifiers must be retained;
3. later B2+ formulations whose exact arrow status is not yet consumed by this intake.

Different proof families remain recoverable because they expose different operations, but shared vocabulary does not by itself prove equivalence.

## 2. B1 graph-level equivalence package

For a finite loopless cubic multigraph $G$, the following are equivalent.

1. An indexed five-support even double cover.
2. A root-valued flow
   $$
   E(G)\to R_5\subset E_5.
   $$
3. A $K_5$-triangle edge labelling.
4. Exact matching/four-flow data: even supports $B,D$, matching $M=B\cap D$, and a nowhere-zero $\mathbf F_2^2$ flow on $G-M$.
5. Equivalently, an even support $B$, matching $M\subseteq B$, nowhere-zero four-flow on $G-M$, and even $M$-endpoint parity in every component of $G-B$.
6. Existence of a Fano flow $f$ and plane $W$ with empty component-obstruction profile.
7. Existence of a cycle-face embedding $S$ whose full dual graph admits a homomorphism
   $$
   T_S^{(1)}\to\mathscr A_5.
   $$

All auxiliary data are existential at graph level. These arrows do not preserve a previously fixed flow, plane, root lift, or surface.

## 3. Matching/four-flow correction

A fixed support-coordinate inverse image is an even support. A fixed root-label inverse image is a matching.

Bare matching plus four-flow is not a complete converse. The missing datum is either:

- the second even support $D$ with $M=B\cap D$; or
- the explicit component endpoint-parity/$T$-join condition.

Any concise formulation must include one of these equivalent data packages.

## 4. Fixed-flow package

Fix a Fano flow $f$ and plane $W$. Let $G_W$ be the subgraph of $W$-valued edges. For every component $K$ of $G_W$, the four outside-colour cut parities are equal.

The following are equivalent for this fixed $(f,W)$:

1. a global five-coordinate slice;
2. a distinguished even support $D$;
3. the matching endpoint $T$-join condition;
4. vanishing of one outside-colour cut parity;
5. vanishing of all outside-colour cut parities;
6. Eulerian outside-colour classes after contraction;
7. vanishing of the local affine component obstruction.

For a prescribed $f$, factorable success means that some plane profile is empty. Failure for this fixed flow is not failure of the graph.

## 5. Fixed-lift surface package

Fix a compatible root lift $g$. It determines a properly face-coloured cycle-face surface $S_g$, its full dual triangular cellulation $T_g$, and the old-colour quotient $J_g$.

The exact same-embedding equivalence is:

$$
\text{componentwise compression of the face components of }g
\Longleftrightarrow
T_g^{(1)}\to\mathscr A_5.
$$

This does not say that every external five-support cover integrates on the prescribed surface. An externally supplied root flow is a dual potential exactly when all dual cycle holonomies vanish.

The quotient criterion

$$
J_g\to\mathscr A_5
$$

classifies only maps constant on old-colour fibres. It is a strict factorable subroute.

## 6. Half-cube parity convention

If $\mathscr A_5$ denotes the even component, singleton words $\varepsilon_i$ are not vertices. Embed the five colours by choosing an odd word $t$ and using

$$
t+\varepsilon_i\in E_5.
$$

Alternatively, name the odd component explicitly.

## 7. Safe fixed-data implication hierarchy

For corresponding fixed flow and fixed lift:

$$
\text{global five-point slice}
\Longrightarrow
J_g\to\mathscr A_5
\Longrightarrow
T_g^{(1)}\to\mathscr A_5
\Longrightarrow
\text{five-support cover}.
$$

No converse is automatic for the same fixed data.

## 8. B2 formulation queue

Programme B1 does not close the full arrows involving:

- cycle-continuous or cographic maps;
- quadratic-cycle equations;
- Schur-product equations;
- singular quotient lifting;
- orthogonal rank reduction;
- Fourier and stress duality.

Programme B2 must classify each arrow as one of:

1. full witness equivalence;
2. equivalence after fixed data are named;
3. quotient or projection with lost lift data;
4. dual obstruction criterion;
5. finite or computational evidence.

Until that classification is integrated, these formulations remain valuable proof families but are not all entries in the B1 graph-level equivalence box.

## 9. Direct colour-cut proof family

The fixed-plane criterion has a short geometric proof.

- Contract every $W$-component.
- The four outside colours form one affine $W$-plane.
- Their only nonzero binary relation is their total sum.
- Hence the four colour-degree parities at each quotient vertex are either $0000$ or $1111$.
- The affine component obstruction is this common bit.

This is the preferred proof of the fixed-$(f,W)$ theorem.

## 10. Singular-fibre proof family

The singular quotient treats every edge as a finite root fibre and every cubic vertex as a local relation. It is natural for later monodromy and Type H analysis.

Its use in B1 is limited to the same fixed-plane component obstruction. Broader equivalence claims await B2.

## 11. Quadratic and Schur proof family

Cycle coordinates and Schur products expose nonlinear correction and switch images. They are important algebraic and computational tools.

Programme B1 does not assert that every displayed quadratic or Schur equation retains the full five-support witness. The reconstruction and lost-data boundary are B2 obligations.

## 12. Stress and Fourier proof family

Dual stresses provide obstruction certificates; Fourier and Möbius methods organize counts over affine choice spaces.

These tools do not solve the graph-level composition problem merely by showing that one finite arrangement is sparse. Their exact equivalence or dual-only status belongs to B2.

## 13. Orthogonal proof family

The universal eight-support lift belongs to a plus-type quadratic space, while the five-support root set lies in a minus-type four-space. This is the clean invariant rank-reduction viewpoint.

It does not remove the need to track fixed-flow, fixed-lift, component, and holonomy quantifiers.

## 14. Surface and half-cube proof family

The full dual retains individual support-cycle components and therefore exposes componentwise freedom, partial Petrials, target links, and marked source circuits.

The old-colour quotient is useful only after the factorability restriction is stated.

## 15. Finite-interface and holonomy families

Cut traces, four-pole states, routing automata, affine holonomy, and defect flows belong to later B3–B7 layers. They remain active mathematical material but are not consumed as B1 equivalences.

## 16. Sufficient templates that are not equivalences

The following remain useful sufficient routes:

- a global-index-factorable map $J_g\to\mathscr A_5$;
- an unused three-matching of old root labels;
- vanishing of an affine-plane residue;
- an orientable good lift;
- an abstract target pivot whose source realization is separately proved.

No one of these is necessary at fixed lift or graph level.

## 17. Preservation and assurance

The exact B1 dossiers remain under `proof-development/`. Recovered source packets remain public provenance and priority records.

B1 curation is substantive mathematical integration, not independent audit, Lean formalization, manuscript approval, publication, release, arXiv, or DOI action. The global five-support theorem remains open.
