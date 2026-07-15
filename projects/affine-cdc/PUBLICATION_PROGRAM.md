# AffineCDC publication programme

Paper boundaries should follow mathematical closure, not the order in which the
notes were discovered. The present corpus contains three immediate paper-sized
blocks, one conditional abstract programme, and one deferred topological
programme.

## Recommended order

1. **Affine Fano compatibility and cycle double covers**;
2. **Dual-Fano residues and the rank hierarchy**;
3. **Gauge circuits, harmonic quotients, and cut interfaces**;
4. **Tensor and code-flag homology**, after literature and payoff tests;
5. **Embedding and Petrial state spaces**, after source restoration.

Papers A and B form the conceptual core. Paper C is a coherent graph-theoretic
sequel. Paper D should not delay them.

## Paper A — Affine Fano compatibility and cycle double covers

### Central theorem

For a finite cubic graph with a nowhere-zero $\mathbf F_2^3$-flow, the local
affine-family torsors admit a globally compatible choice. With the original
dart-level source data, a compatible choice yields a cycle double cover.

### Mathematical contents

1. **Source and local families**
   - cubic binary flows and local Fano planes;
   - quotient coefficients $Q_e$;
   - the invariant local affine coset $\kappa_v+L_v$;
   - exact correspondence with the formal local-family API.

2. **Affine incidence compatibility**
   - incidence space $E_f$;
   - vertex and edge subspaces;
   - pair complex

     $$
     L_{\mathrm{vert}}\oplus L_{\mathrm{edge}}
     \longrightarrow E_f;
     $$

   - obstruction class $[\kappa]$ and solution torsor;
   - quotient-sheaf and equilibrium-stress presentations.

3. **Rank-three Fano geometry**
   - canonical anisotropic quadratic forms on the edge quotients;
   - local Fano Lagrangians;
   - characteristic torsors;
   - legal dual configurations and the cross-bit;
   - global totally singular edge Lagrangian.

4. **Compatibility theorem**
   - the abstract characteristic-torsor intersection theorem;
   - automatic intersection with a totally singular Lagrangian;
   - equivalence with quadratic handshaking and support-boundary cancellation;
   - full moduli torsor and Fano duality.

5. **CDC extraction and formal contract**
   - what the reduced incidence object does and does not remember;
   - the dart pairing and orbit extraction from the companion Lean repository;
   - explicit theorem correspondence between the paper and formal APIs.

### Canonical sources

- [`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md);
- [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md);
- [`FORMAL_STATUS.md`](FORMAL_STATUS.md).

### Exclusions

Do not include:

- the abstract code-flag theory;
- the rank-four calculations beyond a brief sharpness remark;
- circuit classifications;
- embedding or Petrial state spaces.

### Publication readiness

The mathematical paper structure is closed. The remaining critical work is:

1. match the invariant local characteristic torsor explicitly to the Lean API;
2. state the exact CDC extraction theorem without relying on informal prose;
3. add graph-flow and cycle-double-cover bibliography;
4. obtain independent proof review.

## Paper B — Dual-Fano residues and the rank hierarchy

### Central theorem

For a cubic nowhere-zero binary flow of arbitrary rank, the affine compatibility
pairing against an equilibrium stress is exactly the parity of its hidden
annihilator-plane residues:

$$
\psi(\kappa)=\sum_v\rho_v(\psi_v).
$$

Rank three is automatically compatible because the local annihilator cannot
contain a plane. Rank four is the first obstructed layer and has a canonical
Pfaffian cubic equation.

### Mathematical contents

1. the nonzero-indicator polynomial and its degree;
2. the coincidence of quadraticity, half-dimension, and zero index at rank
   three;
3. the all-rank Fano degree-lowering transgression;
4. global outside-plane parity and its information loss;
5. legal dual configurations, cross-bit, support parity, and residue;
6. exact residue counting;
7. the complete global residue theorem;
8. rank-four alternating-form quotient and Pfaffian cubic;
9. symplectic vertex-plane parity;
10. the triangular-prism/$K_{3,3}$ six-vertex dichotomy.

### Canonical sources

- [`rank-hierarchy/transgression-and-dual-fano-residue.md`](rank-hierarchy/transgression-and-dual-fano-residue.md);
- [`rank-hierarchy/rank-four-first-obstruction.md`](rank-hierarchy/rank-four-first-obstruction.md).

### Exclusions

Do not make the tensor complex the paper's organizing object. It may appear in a
short index or stress-dimension remark, but the theorem is about the affine
incidence obstruction and its complete dual residue.

### Publication readiness

The theorem block is coherent. Remaining work:

1. independently audit the local cross-bit criterion and residue count;
2. formalize at least the rank-four local identity or supply a transparent
   coordinate appendix;
3. compare the obstruction with existing characteristic-two quadratic and
   symplectic invariants;
4. decide whether higher-rank decorated residue planes belong in the paper or
   only in future work.

## Paper C — Gauge circuits, harmonic quotients, and cut interfaces

### Central theme

The homogeneous solution space has an intrinsic graph geometry. Gauge words are
exactly harmonic cut quotients, their minimal supports are constraint-matroid
circuits, and graph decomposition is governed by the same labelled interface
objects.

### Mathematical contents

1. gauge code as the tensor kernel and reduced global-section space;
2. harmonic cut-quotient theorem;
3. bicycle-space and Laplacian interpretation;
4. third-order orthogonality and evenness in rank at most three;
5. the sharp rank-four $K_6$ example;
6. low-weight circuit classification through weight six;
7. cycle-space fiber products and cographic pushouts;
8. theta interfaces and mixed variance;
9. the common interface line

   $$
   L_S=\bigcap_i\langle h_i\rangle;
   $$

10. matching obstructions $\Gamma/L_S$ and sewing modes $L_S$;
11. two-edge and three-edge moduli and torsion laws;
12. exact scope of the cap-extension hypothesis.

### Canonical sources

- [`gauge/gauge-modes-and-circuits.md`](gauge/gauge-modes-and-circuits.md);
- [`gauge/interface-gluing.md`](gauge/interface-gluing.md);
- selected rigidity statements from
  [`tensor/torsion-and-rigidity.md`](tensor/torsion-and-rigidity.md).

### Publication readiness

This is a plausible independent graph-theory paper after:

1. literature comparison for graph bicycle spaces and harmonic labellings;
2. verification that the weight-four and weight-six classifications use the
   weakest natural hypotheses;
3. a clean statement of cap extension;
4. computational tables separated from the proofs;
5. a decision whether weight eight is an open problem section or omitted.

## Paper D — Tensor and code-flag homology

### Conditional thesis

A nested binary code flag

$$
D\subseteq C\subseteq\mathbf F_2^E
$$

has a natural complex

$$
\Lambda^2D
\longrightarrow
D\otimes C
\xrightarrow{*}
\mathbf F_2^E,
$$

whose homology, constraint matroid, divided-square exact sequence, coefficient
functoriality, and balanced torsion recover the reduced graphical structures.

### Canonical sources

- [`reduction/incidence-to-tensor-complex.md`](reduction/incidence-to-tensor-complex.md);
- [`tensor/code-flag-complex.md`](tensor/code-flag-complex.md);
- [`tensor/exact-sequences-and-functoriality.md`](tensor/exact-sequences-and-functoriality.md);
- [`tensor/torsion-and-rigidity.md`](tensor/torsion-and-rigidity.md).

### Required tests before treating this as a paper

1. **Recognition:** compare with Schur-product syzygies, Koszul complexes,
   diagonal/Khatri–Rao constructions, and represented matroid quotients.
2. **External examples:** find natural code flags not reverse-engineered from
   AffineCDC.
3. **Payoff:** prove a theorem that is materially shorter or stronger in the
   abstract language.
4. **Functorial closure:** stabilize morphisms, coefficient quotients, and graph
   correspondences.
5. **Terminology:** retain “mixed Schur–Koszul” only if the literature supports
   or clearly distinguishes it.

Until these tests succeed, this is a strong internal theory and a possible
paper, not a publication priority.

## Paper E — Embedding and Petrial state spaces

The snapshot names substantial material on embeddings, rotation systems,
partial Petrials, orientability, transition invariants, delta-matroid slices,
and surface polynomials. The source bodies are absent from the current tree.

No paper outline should be presented as theorem-complete until those sources are
restored and classified under the protocol in
[`topology/README.md`](topology/README.md).

## Immediate programme

The correct immediate sequence is:

1. finish the formal bridge and exposition for Paper A;
2. independently audit and prepare Paper B;
3. develop Paper C if the graph-theory comparisons are favourable;
4. run recognition tests for Paper D without allowing it to block A or B;
5. restore the topological sources before making claims about Paper E.

This order follows the mathematics: existence first, sharp obstruction second,
homogeneous graph consequences third, abstraction and topology afterward.