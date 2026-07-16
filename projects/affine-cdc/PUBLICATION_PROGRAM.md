# AffineCDC publication programme

Paper boundaries should follow mathematical closure, not discovery order or the
historical Lean module endpoint. The present corpus contains three immediate
paper-sized blocks, one conditional abstract programme, and one deferred
topological programme.

## Recommended order

1. **Affine Fano compatibility and the Cycle Double Cover theorem**;
2. **Dual-Fano residues and the rank hierarchy**;
3. **Gauge circuits, harmonic quotients, and cut interfaces**;
4. **Tensor and code-flag homology**, after literature and payoff tests;
5. **Embedding and Petrial state spaces**, after source restoration.

Papers A and B form the conceptual core. Paper C is a coherent graph-theoretic
sequel. Paper D should not delay them.

## Paper A — Affine Fano compatibility and the Cycle Double Cover theorem

### Final headline theorem

The paper's final graph-theoretic theorem is:

> Every multigraph with finite active edge set and no bridges has a cycle double
> cover.

Loops are allowed. They are deleted before the loopless proof core and restored
at the end by adding two occurrences of each singleton loop circuit. A circuit
is a nonempty inclusion-minimal cut-even edge set. The paper must prove this full
endpoint through the project's own graph model and reduction.

The current companion Lean `Statement.lean` is still loopless and ambient-finite.
It is an implementation checkpoint awaiting the approved Path A migration and
must not be presented as the final natural mathematical statement or as already
proved.

### Principal new structural theorem

For a finite cubic graph, not necessarily connected, with a nowhere-zero
$\mathbf F_2^3$-flow, the local affine-family torsors admit a globally compatible
choice. In the invariant presentation, the characteristic torsor of the vertex
Lagrangian intersects the totally singular edge Lagrangian.

The retained graph-and-dart data turn a compatible family into a graph-level
multiset even double cover. Circuit decomposition is postponed until after the
outer graph reduction.

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
   - the characteristic-torsor intersection theorem;
   - automatic intersection with a totally singular Lagrangian;
   - equivalence with quadratic handshaking and support-boundary cancellation;
   - the compatible-family moduli torsor.

5. **Natural affine output**
   - compatible family to indexed even edge supports;
   - flattening to a graph-level multiset even double cover;
   - exact double coverage and allowance of repeated or empty supports;
   - a cubic-flow CDC only as an optional immediate corollary.

6. **Full outer graph-theoretic shell**
   - active-edge finiteness and preliminary loop separation;
   - the isolated loopless binary-eight-flow input, with componentwise Seymour,
     literal integer `6-flow -> 8-flow`, and Tutte's equal-order existence
     theorem;
   - adaptive prefix avoidance in every finite binary rank at least two;
   - the preferred adaptive flow-first route
     `G -> (G,f) -> (H,\widetilde f,\pi,\lambda)`;
   - the independent expansion-first route `G -> H -> (H,f)`;
   - exact expansion sizes `|V(H)|=2|E(G)|` and `|E(H)|=3|E(G)|`;
   - vertex-even/cut-even bridge on the loopless expansion;
   - pure cut-even collapse transport;
   - a multiset cut-even double cover of the loopless original core.

7. **Final decomposition and loop reinsertion**
   - one finite circuit decomposition after collapse;
   - two singleton circuit occurrences for every removed loop;
   - conclusion of the full finite bridgeless-multigraph CDC theorem.

8. **Formal correspondence**
   - exact relation between the paper's characteristic torsor and the existing
     Lean local-family API;
   - exact relation between the current dart-level construction and the
     graph-level even-cover theorem;
   - theorem-by-theorem status and axiom audit;
   - explicit separation between the unchanged Lean checkpoint and the approved
     but unimplemented public-statement migration.

### Canonical sources

- [`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md);
- [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md);
- [`reduction/outer-shell-and-binary-flow.md`](reduction/outer-shell-and-binary-flow.md);
- [`reduction/even-cover-and-collapse.md`](reduction/even-cover-and-collapse.md);
- [`MATHEMATICAL_ARCHITECTURE.md`](MATHEMATICAL_ARCHITECTURE.md);
- [`FORMAL_STATUS.md`](FORMAL_STATUS.md).

### Exclusions

Do not include:

- the abstract code-flag theory;
- the rank-four calculations beyond a brief sharpness remark;
- gauge-circuit classifications;
- embedding or Petrial state spaces;
- a separate numbered cubic-flow CDC theorem unless exposition genuinely needs
  the immediate corollary.

### Outer-shell exposition and implementation decision

Use the adaptive flow-first route as the primary concise Paper A proof. State the
general binary-rank adaptive ordering theorem, specialize it to
$\mathbf F_2^3$, and retain the degree-eight Gray-tour example as sharpness for
a preselected cyclic order. Adaptive ordering belongs to Paper A and is not a
separately authorized present paper.

Retain the expansion-first route as an independent flow-free theorem. It is also
the selected first Lean outer-shell implementation route, because it avoids the
initial formalization cost of the adaptive multiset-ordering and extension
witnesses. The first Lean route must expose one exact isolated external
`BinaryEightFlow` theorem boundary; neither route, Seymour, nor Tutte is thereby
machine-checked.

### External source status

The verified six-flow citation is P. D. Seymour, “Nowhere-zero 6-flows”,
*Journal of Combinatorial Theory, Series B* **30** (1981), 130–135, DOI
`10.1016/0095-8956(81)90058-7`. The exact primary theorem and page pinpoint for
Tutte's equal-order group-flow existence result remain an unresolved publication
source gate. The existence theorem and the group-flow counting theorem must be
kept distinct.

### Publication readiness

The affine compatibility core and the outer-shell packet are mathematically
coherent at paper level, but Paper A is not yet closed because canonical
acceptance, formal correspondence, independent proof review, bibliography, and
the Lean endpoint remain unfinished. Remaining critical work:

1. independently audit the invariant characteristic-torsor proof;
2. match the invariant local characteristic torsor explicitly to the Lean API;
3. state and prove the exact graph-level even-cover extraction theorem;
4. after canonical acceptance of `outer-shell-and-binary-flow.md`, independently
   review the outer-shell proof and integrate it with the loop reduction and
   cut-even handoff; formalization remains separately open;
5. prove the full unconditional endpoint in Lean after the exact Path A migration
   packet is approved and implemented;
6. complete graph-flow and cycle-double-cover bibliography, including the exact
   Tutte primary theorem/page source gate;
7. obtain independent line-by-line review of adaptive ordering, the outer shell,
   collapse compatibility, and final assembly;
8. complete author decisions on title, authorship, affiliation, ORCID, AI
   disclosure, acknowledgements, novelty language, and publication mode;
9. complete the final source/PDF package and obtain explicit later `AC-DIR`,
   author, and arXiv authorization.

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
short index or stress-dimension remark, but the theorem concerns the affine
incidence obstruction and its dual residue.

### Publication readiness

The theorem block is coherent. Remaining work:

1. independently audit the local cross-bit criterion and residue count;
2. formalize at least the rank-four local identity or supply a transparent
   coordinate appendix;
3. compare the obstruction with existing characteristic-two quadratic and
   symplectic invariants;
4. decide whether higher-rank decorated residue planes belong in the paper or
   future work.

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
4. computational tables separated from proofs;
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
3. **Payoff:** prove a theorem materially shorter or stronger in the abstract
   language.
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

1. close the mathematical and formal spine of Paper A through the full theorem;
2. independently audit and prepare Paper B;
3. develop Paper C if the graph-theory comparisons are favourable;
4. run recognition tests for Paper D without allowing it to block A or B;
5. restore the topological sources before making claims about Paper E.

This order follows the mathematics: unconditional existence first, sharp
obstruction second, homogeneous graph consequences third, abstraction and
topology afterward.
