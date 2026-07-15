# AffineCDC publication program

This plan derives paper boundaries from mathematical closure.  Existing labels such as “Paper 1” are retained only where they coincide with a natural theorem block.

## Executive judgment

The present material does not form one paper.  It contains at least two strong, coherent theorem papers, one plausible graph-theory sequel, one conditional abstract-algebra programme, and one topological/computational programme whose sources must first be restored.

The recommended order is:

1. **Affine Fano compatibility and cycle double covers**;
2. **Dual-Fano residues and the rank hierarchy**;
3. **Gauge circuits, harmonic quotients, and cut interfaces**;
4. **Flow tensor/code-flag homology**, only after recognition and payoff tests;
5. **Embedding and Petrial state spaces**, only after source restoration and audit.

The first two are already natural mathematical units.  They should not be delayed until the broader tensor or topological frameworks are finished.

---

## Paper A — Affine Fano compatibility and cycle double covers

### Central theorem

For a finite cubic graph with a nowhere-zero \(\mathbf F_2^3\)-flow, the local affine-family torsors admit a globally compatible choice.  The compatible choice yields a cycle double cover.

### Natural contents

1. **Source datum and local affine families**
   - cubic binary flow;
   - local Fano plane \(W_v\);
   - quotient labels \(Q_e=\Gamma/\langle f(e)\rangle\);
   - local classification \(\kappa_v+L_v\).

2. **Affine incidence-pair complex**
   - \(E_f\), \(L_{\mathrm{vert}}\), \(L_{\mathrm{edge}}\);
   - \(H^0=L_{\mathrm{vert}}\cap L_{\mathrm{edge}}\);
   - \(H^1=E_f/(L_{\mathrm{vert}}+L_{\mathrm{edge}})\);
   - affine obstruction \([\kappa]\).

3. **Local Fano quadratic package**
   - canonical anisotropic forms on binary edge quotients;
   - diagonal Fano Lagrangian;
   - quadratic transgression;
   - local affine family as characteristic torsor;
   - legal dual configurations and cross/support identity.

4. **Global affine Lagrangian intersection**
   - abstract exact criterion;
   - edge diagonal as totally singular Lagrangian;
   - automatic intersection;
   - full compatible-solution torsor.

5. **Equivalent presentations**
   - quotient sheaf;
   - equilibrium stresses/Fredholm criterion;
   - support-boundary cancellation;
   - Fano Hodge duality.

   These should be presented as translations of one theorem, not as parallel foundations.

6. **CDC extraction**
   - reconstruction from quotient labels to local dart pairings;
   - global cycles;
   - double coverage.

7. **Formal correspondence**
   - exact map from manuscript definitions to the companion Lean development;
   - statement equivalence;
   - list of invariant lemmas not yet formalized.

### What should be excluded

- general code flags and abstract tensor categories;
- rank-four residue theory beyond a brief sharpness remark;
- circuit classifications;
- Petrial/state-sum material;
- broad claims that tensor theory is the master object.

### Why this is a complete paper

It begins with a graph-theoretic input, isolates the exact affine compatibility problem, proves compatibility by a concise invariant theorem, describes all solutions, and returns to the graph-theoretic CDC output.  No later generalization is needed for closure.

### Current risk

The new Lagrangian compression is not yet the Lean proof itself.  The paper must either formalize the compression or include a precise correspondence to the verified implementation.  Elegance alone is not proof transport.

### Recommended title candidates

- *Affine Fano compatibility and cycle double covers*
- *Characteristic Fano torsors on cubic flows*
- *A Lagrangian compatibility theorem for cubic binary flows*

The first is the clearest.

---

## Paper B — Dual-Fano residues and the rank hierarchy

### Central theorem

For a cubic graph with a nowhere-zero binary flow in arbitrary rank, the affine obstruction evaluated on an equilibrium stress equals the parity of vertices carrying a hidden dual Fano plane in the local annihilator.

This yields:

- automatic compatibility in rank three;
- the cubic/Pfaffian obstruction in rank four;
- a decorated-plane residue geometry in higher rank.

### Natural contents

1. **All-rank support transgression**
   - nonzero-indicator polynomial on \(Q_h\);
   - Fano summation lowers degree by one;
   - global outside-plane parity;
   - explanation of what the scalar identity forgets beyond rank three.

2. **Legal dual configurations**
   - annihilator constraints;
   - cross-bit;
   - support parity;
   - hidden dual Fano plane.

3. **Dual-Fano residue theorem**
   - local identity \(\sigma=\beta+\rho\);
   - global handshaking cancellation;
   - complete compatibility criterion.

4. **Rank-three coincidence principle**
   - quadratic support degree;
   - local half-dimension;
   - global index balance;
   - no room for a residue plane.

5. **Rank-four Pfaffian specialization**
   - alternating forms modulo \(\Lambda^2(\Gamma/W)^*\);
   - divided square/Pfaffian;
   - cubic directional residue;
   - symplectic-transversality interpretation.

6. **Minimal examples**
   - canonical rank-four \(K_{3,3}\) obstruction;
   - triangular prism versus \(K_{3,3}\);
   - gauge rigidity and obstruction dimension are insufficient;
   - symplectic parity anomaly.

7. **Higher-rank questions**
   - residue vertices decorated by annihilator planes;
   - possible global incidence geometry among residue planes;
   - relation to higher-degree polarizations.

### Why this is a separate paper

Paper A proves the exceptional positive theorem.  Paper B explains the exceptionalism and gives a complete obstruction law in every rank.  Combining them would obscure both narratives and make the core CDC result hostage to a much broader hierarchy.

### Current risk

The all-rank theorem-level drafts need independent proof audit.  The finite rank-three-through-six checks should be reported as validation, not as the theorem proof.

### Recommended title candidates

- *Dual-Fano residues in binary flow compatibility*
- *The rank hierarchy of affine Fano compatibility*
- *Pfaffian residues beyond the Fano rank*

The first best reflects the general theorem.

---

## Paper C — Gauge circuits, harmonic quotients, and cut interfaces

### Central theorem block

The homogeneous gauge code of a flow-labelled graph is the code of harmonic cut quotients: its nonzero words correspond exactly to connected contracted quotients on which the induced labels are simultaneously a nowhere-zero flow and an exact tension.

For coefficient rank at most three the code is even, its low-weight circuits admit concrete classifications, and two-edge/three-edge gluing is governed by the gauge space of a labelled theta interface.

### Natural contents

1. gauge code from reduced global sections;
2. harmonic cut-quotient characterization;
3. constraint-matroid circuit interpretation;
4. third-order graph-bicycle orthogonality;
5. evenness theorem and sharp rank-four counterexample;
6. low-weight classification through weight six;
7. interface line \(L_S\) and matching quotient \(\Gamma/L_S\);
8. cycle-space pullback and cographic pushout;
9. exact two-edge and three-edge gluing laws;
10. torsion and state-count factorization.

### Independence from Paper A

This paper uses the homogeneous reduction of the incidence complex, but not the affine compatibility theorem or CDC extraction.  It should be written as graph theory/coding theory, with AffineCDC as its source rather than its entire justification.

### Strongest publishable results

- general evenness of the rank-at-most-three gauge code;
- exact harmonic quotient characterization;
- complete weight-six circuit classification;
- universal interface line formula;
- multiplicativity/vanishing of Fano torsion across low cuts.

These results provide the “payoff” test that the tensor/constraint viewpoint needs.

### Open endpoint

Weight eight is the next circuit layer.  It is not necessary for publication if the weight-six classification and interface theorem are complete and audited.

### Recommended title candidates

- *Harmonic cut quotients of binary flows*
- *Even gauge codes and harmonic interfaces*
- *Flow–tension circuits in binary flow-labelled graphs*

The first is the most intrinsic.

---

## Paper D — Flow tensor and code-flag homology

### Proposed subject

For a nested binary code flag

\[
D\subseteq C\subseteq\mathbf F_2^E,
\]

study the complex

\[
\Lambda^2D
\longrightarrow
D\otimes C
\xrightarrow{*}
\mathbf F_2^E,
\]

its homology, constraint matroid, balanced torsion, divided-square sequence, coefficient quotients, and graphical realizations.

### Why this is not yet a settled paper

The internal formalism is coherent, but four validation tests remain unmet or only partly met:

1. **Recognition.**  Determine whether the exact complex and its quotient-by-commutativity syzygy space already have a standard home in coding, Koszul, Rees, or matroid literature.
2. **External examples.**  Compute meaningful cases from Reed–Muller, cyclic, evaluation, or projective-geometry code flags not derived from graphs.
3. **Payoff.**  Prove a theorem that is new and clearer in the abstract framework.
4. **Functoriality.**  Stabilize ordinary morphisms and the correspondence formalism needed for deletion, contraction, and gluing.

### Core material if the tests succeed

1. based quotient data and dual code flags;
2. tensor/Schur–Koszul complex;
3. index and balancedness;
4. divided-square exact sequence;
5. constraint matroid and syzygies;
6. determinant-line torsion;
7. coefficient-quotient long exact sequence;
8. strict morphisms and automorphisms;
9. graphical realization and chain-level bridge;
10. external examples.

### Editorial warning

Do not publish this as a grand general theory merely because many AffineCDC objects fit into it.  The name “mixed Schur–Koszul complex” must remain provisional until the literature search is complete.

### Possible alternative

If external novelty is thin, the best material can be folded into Paper C as a concise algebraic framework, with the divided-square and torsion results presented as tools rather than a separate theory.

---

## Paper E — Gauge embeddings and code-filtered Petrial state spaces

### Proposed subject

Compatible/gauge states as embedding modifications, partial Petrials, orientability constraints, transition structures, and code-filtered surface polynomials, together with low-cut factorization.

### Present status

Not ready for paper design.  The 2026-07-14 snapshot records the source filenames and hashes, but their bodies are absent from `main`.  Some active synthesis survives, but it is insufficient to guarantee that every lemma, convention, and computational condition has been preserved.

### Required work before outlining the paper

1. rematerialize all topological manuscript sources and scripts;
2. separate proved correspondences from census observations;
3. identify which state space is affine compatibility and which is homogeneous gauge freedom;
4. normalize rotation, Petrial, orientability, and transition conventions;
5. compare with established ribbon-graph, delta-matroid, transition-matroid, and circuit-partition literature;
6. rerun computational tables from the preserved scripts;
7. determine whether one invariant genuinely subsumes the others.

### Likely natural split after restoration

The material may divide into two papers rather than one:

- an algebraic/topological correspondence paper;
- a state-sum/factorization and census paper.

No decision should be made from filenames alone.

---

## Short-note possibilities

Some results may be cleaner as short independent notes if they do not fit the main papers.

### Fano torsion

A concise note could present:

- the basis-free determinant-line invariant;
- rigidity criterion;
- divided-square factorization;
- basis-packing expansion;
- two-edge vanishing and three-edge multiplicativity.

It is mathematically complete, but may have greater impact as a section of Paper C or D.

### Symplectic vertex-plane parity

The global parity theorem and its local-field anomaly are elegant, but currently too small alone.  They belong naturally in Paper B.

### Six-vertex rank-four dichotomy

This is an excellent example/corollary, not a separate paper unless connected to a wider small-order classification.

---

## Recommended immediate sequence

### First manuscript

Write Paper A now, using the incidence-pair/Lagrangian architecture.  Keep the original Lean theorem as the formal anchor and explicitly map the compressed proof to it.

### Parallel audit

Audit Paper B's residue theorem and rank-four examples.  This can proceed independently of the CDC extraction prose.

### Then graph consequences

Consolidate harmonic quotients, evenness, weight-six circuits, interfaces, and torsion into Paper C.  This provides a clear external theorem payoff.

### Defer broad frameworks

Do not spend the publication-critical path polishing categorical vocabulary or the topological state programme before Papers A and B are stable.

---

## Dependency among papers

The logical dependency is lighter than the discovery history suggests.

\[
\text{Paper A}
\quad\text{and}\quad
\text{Paper B}
\]

share the source incidence geometry and local Fano notation, but neither requires the full tensor/code theory.

\[
\text{Paper C}
\]

uses the homogeneous reduction and can cite Paper A for origin, but its theorems stand independently.

\[
\text{Paper D}
\]

abstracts the algebra behind Papers A and C; it should follow them unless the literature review reveals an existing framework.

\[
\text{Paper E}
\]

uses the state spaces and cut laws but has its own topological prerequisites.

This order prevents the strongest finished theorem from being buried under the least mature generalization.
