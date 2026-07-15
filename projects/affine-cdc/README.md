# AffineCDC

This directory studies the affine incidence geometry attached to nowhere-zero
binary flows on cubic graphs and its role in the Cycle Double Cover problem.

> A cubic rank-three flow determines local affine families. Their Fano
> quadratic geometry forces a globally compatible choice. The retained graph
> and dart data then produce an even double cover, which is transported through
> the outer graph reduction and decomposed into a cycle double cover only at the
> end.

The natural public theorem is:

> Every finite bridgeless multigraph has a cycle double cover.

Loops are allowed. A circuit is a nonempty inclusion-minimal cut-even edge set,
so a singleton loop is a circuit. The natural finiteness condition is finiteness
of the active edge set. Finite ambient carrier types describe the current Lean
checkpoint only.

The active tree is organized by mathematical dependency. Discovery order and
superseded formulations remain available in Git history and dated snapshots.

## Canonical reading order

1. [`MATHEMATICAL_ARCHITECTURE.md`](MATHEMATICAL_ARCHITECTURE.md)  
   The dependency map for the affine core, the even-cover output, the
   unconditional outer shell, and the downstream theories.

2. [`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md)  
   The rank-independent compatibility object: incidence space, affine pair
   complex, quotient sheaf, obstruction class, and equilibrium stresses.

3. [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md)  
   Canonical quadratic planes, local Fano Lagrangians, characteristic torsors,
   affine Lagrangian intersection, and automatic rank-three compatibility.

4. [`reduction/even-cover-and-collapse.md`](reduction/even-cover-and-collapse.md)  
   The natural graph-level output of the affine construction, cut-evenness as
   the collapse invariant, projection through graph surgery, final circuit
   decomposition, and loop reinsertion.

5. [`rank-hierarchy/transgression-and-dual-fano-residue.md`](rank-hierarchy/transgression-and-dual-fano-residue.md)  
   Why rank three is the unique balanced quadratic point, the all-rank support
   transgression, and the complete dual-Fano residue criterion.

6. [`rank-hierarchy/rank-four-first-obstruction.md`](rank-hierarchy/rank-four-first-obstruction.md)  
   The Pfaffian cubic residue, symplectic parity, and the triangular-prism versus
   $K_{3,3}$ sharpness theorem.

7. [`reduction/incidence-to-tensor-complex.md`](reduction/incidence-to-tensor-complex.md)  
   The exact chain-level zigzag from affine incidence geometry to the tensor
   complex, including what the reduction preserves and forgets.

8. [`tensor/code-flag-complex.md`](tensor/code-flag-complex.md),
   [`tensor/exact-sequences-and-functoriality.md`](tensor/exact-sequences-and-functoriality.md), and
   [`tensor/torsion-and-rigidity.md`](tensor/torsion-and-rigidity.md)  
   The downstream based-quotient/code-flag theory, exact sequences, and balanced
   torsion.

9. [`gauge/gauge-modes-and-circuits.md`](gauge/gauge-modes-and-circuits.md) and
   [`gauge/interface-gluing.md`](gauge/interface-gluing.md)  
   Harmonic cut quotients, parity and low-weight circuits, interface lines, and
   sewing laws.

## The compatibility centre

Let $G=(V,E)$ be a finite cubic graph, not necessarily connected, let $\Gamma$
be a binary vector space, and let

$$
f:E\longrightarrow\Gamma
$$

be a nowhere-zero flow. For every edge put

$$
Q_e:=\Gamma/\langle f(e)\rangle.
$$

Let $E_f$ be the direct sum of the incidence copies of the $Q_e$. Local
homogeneous families form $L_{\mathrm{vert}}\leq E_f$, edge matching forms
$L_{\mathrm{edge}}\leq E_f$, and the actual local families form the affine
coset

$$
\kappa+L_{\mathrm{vert}}.
$$

The compatibility problem is the pointed two-term complex

$$
\boxed{
\mathcal P_f:
L_{\mathrm{vert}}\oplus L_{\mathrm{edge}}
\xrightarrow{+}
E_f,
\qquad
\kappa\in E_f.
}
$$

It has

$$
H^0(\mathcal P_f)
\cong
L_{\mathrm{vert}}\cap L_{\mathrm{edge}}
$$

and

$$
H^1(\mathcal P_f)
\cong
E_f/(L_{\mathrm{vert}}+L_{\mathrm{edge}}).
$$

Compatibility is exactly

$$
[\kappa]=0\in H^1(\mathcal P_f),
$$

and the compatible-family space is then a torsor under $H^0(\mathcal P_f)$.

In rank three, each $Q_e$ is a canonical anisotropic quadratic plane. The vertex
space is Lagrangian, the affine coset is its characteristic torsor, and the
edge-matching space is a totally singular Lagrangian. The characteristic-torsor
intersection theorem forces $[\kappa]=0$.

## The existence spine

The affine incidence pair is the complete centre of the compatibility question,
but it is not the whole unconditional CDC proof. The full spine is:

- a multigraph $G$ with finite active edge set and no bridges;
- deletion of all loops, giving a loopless bridgeless core $G_0$;
- an independently constructed cubic expansion carrying the required
  rank-three binary flow;
- affine incidence compatibility on the cubic graph;
- a graph-level multiset even double cover;
- the vertex-even/cut-even bridge on the loopless expansion;
- pure cut-even transport through collapse;
- an even double cover of $G_0$;
- one final decomposition into circuits;
- two singleton circuit occurrences for every removed loop;
- a cycle double cover of the original multigraph $G$.

A cycle double cover of the already cubic flow graph is an immediate corollary
of the even-cover construction, not a necessary intermediate node.

## Logical levels

### Compatibility spine

- cubic binary flow and local affine families;
- affine incidence-pair complex;
- quotient-sheaf and stress presentations;
- rank-three Fano quadratic-Lagrangian theorem;
- compatible-family torsor.

### Cover and reduction spine

- compatible family to indexed even supports;
- graph-level multiset even double cover;
- vertex-even/cut-even bridge on loopless graphs;
- pure cut-parity transport through graph collapse;
- finite circuit decomposition once, after collapse;
- singleton-loop reinsertion.

### Rank hierarchy

- degree-lowering Fano support transgression;
- rank-three coincidence of quadraticity, half-dimension, and zero index;
- complete all-rank dual-Fano residue;
- rank-four Pfaffian equation and first counterexample.

### Downstream reductions and consequences

- tensor and code-flag homology;
- constraint matroid and balanced torsion;
- harmonic cut quotients and circuit classification;
- cut interfaces and sewing exact sequences.

These are generated by the compatibility geometry but are not alternative
centres of the existence proof.

## Reliability and provenance

- [`FORMAL_STATUS.md`](FORMAL_STATUS.md) separates machine-checked anchors,
  paper proofs, exact computations, and programmes.
- [`MIGRATION_LEDGER.md`](MIGRATION_LEDGER.md) maps every former active dossier
  to its canonical destination.
- [`PUBLICATION_PROGRAM.md`](PUBLICATION_PROGRAM.md) gives natural paper-sized
  blocks.
- [`topology/README.md`](topology/README.md) records the hash-only embedding and
  surface programme without pretending to reconstruct missing sources.

The historical title “flow tensor datum as the master object” is obsolete. The
affine incidence-pair complex is the compatibility centre; the tensor complex
is its canonical chain-level reduction. The public companion formalization's
current `Statement.lean` is still loopless and ambient-finite and remains
unchanged. It is an implementation checkpoint awaiting the separately approved
Path A migration packet; it is not the final natural mathematical statement.
