# Equivalent formulations and proof families

## 1. Purpose

The public research surface contains many exact reformulations discovered at different stages. Their value is not that one must choose a single winner. Different formulations expose different operations:

- root geometry exposes local triangles;
- quadratic and Schur equations expose linear correction;
- stresses expose dual certificates;
- surfaces expose componentwise support freedom;
- gauge codes expose affine arrangements;
- four-pole states expose gluing;
- holonomy exposes composition failure.

This chapter records which formulations are genuinely equivalent, which are only sufficient subroutes, and which proof families should remain independently recoverable.

## 2. Global equivalence package

The following are equivalent for a finite cubic graph $G$.

1. An indexed five-support even double cover.
2. A root-valued flow
   $$
   E(G)\to R_5\subset E_5.
   $$
3. A labelling of source edges by edges of $K_5$ such that every cubic vertex maps to a triangle.
4. A cycle-continuous/cographic map into the $K_5$ triangle geometry.
5. A matching together with a nowhere-zero $\mathbf F_2^2$ flow on the matching complement, with the corresponding boundary conditions.
6. A solution of the quadratic cycle equation in the chosen binary coordinates.

These formulations describe the final five-support object itself.

## 3. Projection and lifting package

A compatible eight-support root lift projects to a Fano flow. Conversely, every cubic Fano flow has a compatible eight-support lift by the rank-three affine theorem.

Fixing a five-coordinate slice or quotient gives equivalent obstruction presentations:

1. singular-line quotient lifting;
2. component parity on $G_W$;
3. equal outside-colour cut parity;
4. Eulerian colour classes in the contracted quotient;
5. boundary of a Schur product;
6. pairing with relative stresses;
7. Fourier character obstruction;
8. affine-subspace arrangement avoidance.

These are complete only after the projection/slice has been fixed. They do not by themselves exhaust the componentwise surface criterion.

## 4. The direct geometric proof family

The most economical proof of the fixed-plane criterion is the colour-cut argument.

- Contract each $W$-component.
- The four outside colours form one affine $W$-plane.
- Their only binary relation is the total sum.
- Hence their degree-parity vector at a quotient vertex is $0000$ or $1111$.
- The affine lifting obstruction is exactly this common bit.

Advantages:

- coordinate-free after choosing $W$;
- no local-family enumeration;
- gives explicit cut certificates;
- interacts directly with cycle switches and graph decomposition.

This should be the default proof in a general exposition.

## 5. The singular-fibre proof family

The singular quotient treats every edge as a finite root fibre and every cubic vertex as a local relation. Component parity is the holonomy of this finite local system.

Advantages:

- extends naturally to monodromy quotients $1+\pi$;
- explains empty edge fibres, empty vertex relations, and component holonomy uniformly;
- is the correct language for the Type H rainbow branch.

This proof family should remain independent because it supplies the later local-to-global obstruction stack.

## 6. The quadratic/Schur proof family

Choose cycle coordinates $x,y$. The root condition becomes a quadratic relation, and the obstruction is the boundary of

$$
x*y.
$$

Advantages:

- makes fixed-direction correction linear after differentiation;
- gives exact images for admissible cycle switches;
- interfaces with code theory, tensor products, and cographic quotients;
- isolates the nonlinear part in one Schur word.

The Schur complex is a useful computational and algebraic presentation. It should not replace the affine or surface object as the conceptual centre.

## 7. The stress/Fourier proof family

Dualizing the affine lifting map gives equilibrium stresses. A bad slice has a stress evaluating nontrivially on the distinguished affine class.

Fourier expansion over the affine choice torsor separates:

- the uniform orbit average;
- nontrivial characters supported by relative stresses.

The Fourier-zero term is the orbit-average argument; low-weight stress characters give the first nonuniform corrections. Möbius inversion on affine-subspace intersections supplies a Fourier-free count.

Advantages:

- proves counting and density statements;
- detects when local controllability is enough;
- provides exact dual certificates;
- connects to the existing tensor/stress corpus.

Limit:

- it does not solve the source composition problem merely by showing that one finite arrangement is sparse.

## 8. The orthogonal-group proof family

The universal compatible lift belongs to the anisotropic orbit of a plus-type quadratic space. The five-support object is the root orbit of a minus-type four-space.

Advantages:

- explains the support counts $28$ and $10$;
- identifies the five-support problem as orthogonal rank reduction;
- unifies the $K_8$ and $K_5$ triangle complexes;
- clarifies why local triangles persist under projection.

This is the clean invariant overview. Coordinate proofs remain necessary for component parity and switch effects.

## 9. The surface/half-cube proof family

The root lift produces a coloured cycle-face surface and dual triangulation. A five-support cover is a graph homomorphism

$$
T_g^{(1)}\to\mathscr A_5.
$$

Advantages:

- retains individual support-cycle components;
- exposes partial Petrials and orientability;
- gives target-link obstruction theory;
- converts marked certificates into exact source face circuits.

The global-colour quotient $J_g$ is a strict factorable subroute. Any proof using only $J_g$ must state that restriction.

## 10. The finite-interface proof family

Restrict a cover to a cut and classify its boundary trace.

- three-edge cuts have a unique local support law and glue directly;
- four-edge cuts have the ten-state alphabet;
- cap forcing, Kempe closure, and routing weights reduce possible disjoint shore profiles;
- routing automata expose unique-linkage and holonomy mechanisms.

Advantages:

- produces valid inductive and replacement interfaces;
- separates local algebra from graph transfer;
- supplies the language needed to turn defect localisation into a global proof.

This is the proof family most directly tied to the remaining closure gap.

## 11. The holonomy/cohomology proof family

Boundary loops lift to affine actions in

$$
(Z_1(P)\otimes E_5)\rtimes S_5.
$$

Cyclic norms, root-fibre local systems, $S_5$ cohomology, and the exceptional $D_8$ class organize the residual Type H branch.

Advantages:

- distinguishes support-name monodromy from genuine interior obstruction;
- eliminates the BBD pure-translation branch by root rigidity;
- produces one canonical defect flow;
- identifies the precise one-bit DDD exception.

Limit:

- cohomology vanishing gives an ambient origin, not automatically a root-valued or composition-safe graph replacement.

## 12. Sufficient templates that are not equivalences

The following statements provide useful sufficient routes only.

### 12.1 Global-index-factorable compression

$$
J_g\to\mathscr A_5
$$

implies five supports, but the converse fails at the fixed-lift level because $T_g$ has componentwise freedom.

### 12.2 Unused three-matching

Three disjoint unused root labels imply factorable compression. This is not a necessary condition.

### 12.3 Affine-plane $K_4$ residues

Vanishing of one of seven plane residues produces an unused affine-plane $K_4$. These tests do not exhaust all maps $T_g\to\mathscr A_5$.

### 12.4 Orientable good lift

An orientable five-support cover produces a nowhere-zero $\mathbf Z_5$ flow. Nonorientable five-support covers remain valid for the five-support problem.

### 12.5 Ideal target pivot

Abstract target-side pivots escape every cover-number-two or pentagon quotient core. Source realizability is a separate condition.

## 13. Negative results that control proof choice

Any future proof must respect the following exact boundaries.

1. A fixed Fano flow may require six supports.
2. There is no universal homomorphism $K_8\to K_5$ or universal source-independent compression.
3. $J_g$ is not the complete fixed-lift object.
4. $K_6$-free does not imply a half-cube map, even for compatible duals.
5. A bad fixed-flow fibre does not imply a bad graph.
6. A disconnected binary-cycle switch is not one reconfiguration edge.
7. Route-lock does not imply a graph two-cut.
8. Route-lock does not imply flatness.
9. Rank-two route-lock is not residual; it has Tait escape.
10. Repeated Petersen transport state does not imply a replaceable strip.
11. Boundary monodromy alone is not an obstruction; interior action matters.
12. Exact finite census does not establish universal realizability or completeness.

## 14. Recommended exposition choices

For the main narrative:

1. state root-flow equivalence first;
2. introduce the universal eight-support lift and fixed-plane colour-cut criterion;
3. pass immediately to the surface/dual criterion;
4. distinguish vertical gauge from horizontal flow motion;
5. introduce source interfaces before finite laboratories;
6. use holonomy only after the four-pole routing reduction;
7. end with the atom curvature/localisation problem.

For appendices or independent companion notes:

- orthogonal-group comparison;
- Schur/tensor complexes;
- Fourier and Möbius arrangements;
- orientation transgression and five-flow extraction;
- exhaustive laboratory tables;
- monodromy coordinate enumerations.

## 15. Preservation rule

Equivalent proofs should not be erased when one becomes the preferred exposition. The source packets remain exact historical and priority records. The corpus records:

- the preferred proof for readability;
- the alternate proof's mathematical role;
- the precise equivalence or implication;
- its assurance and computation boundary.

This avoids both proof loss and false inflation of one coordinate presentation into the theorem's natural object.