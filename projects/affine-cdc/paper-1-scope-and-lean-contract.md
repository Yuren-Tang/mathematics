# AffineCDC Paper 1 scope and Lean contract

**Date:** 2026-07-15  
**Status:** proposed scope freeze for paper/Lean co-design; subject to one adversarial review before implementation.

This document separates the theorem kernel that should be shared literally by
the paper and Lean from the expository and forward-looking material that may
remain flexible.

---

## 1. Guiding rule

The order of work should be

\[
\boxed{
\text{freeze the Paper Kernel}
\longrightarrow
\text{formalize the same kernel}
\longrightarrow
\text{write the flexible exposition around it}.
}
\]

The paper should not be written around an obsolete Lean proof, and Lean should
not formalize every intermediate research representation. The common target is
a small theorem-and-definition contract.

The existing branching formalization remains a verified regression oracle
until the paper-aligned proof is complete. It is not deleted merely because a
cleaner proof is found.

---

## 2. The theorem hierarchy

### Theorem A — Affine Fano compatibility (structural core)

Let \(G\) be a finite cubic graph and let

\[
f:E(G)\to\Gamma,
\qquad
\Gamma=\mathbf F_2^3,
\]

be a nowhere-zero flow. At each vertex take the canonical local affine-family
torsor determined by the three incident flow directions. Then the local affine
families admit a globally compatible choice.

Equivalent formulations are:

\[
(\kappa+L_{\mathrm{vert}})\cap L_{\mathrm{edge}}\ne\varnothing,
\]

\[
\delta_fm=c_f\text{ is solvable},
\]

and

\[
[c_f]=0\in H^1(G;\mathscr Q_f).
\]

This is the principal new structural theorem and the mathematical heart of the
paper.

### Theorem B — Quadratic Lagrangian form of Theorem A

In the global incidence quadratic space, the vertex homogeneous space is a
Lagrangian \(L_{\mathrm{vert}}\), the local affine-family space is its
characteristic torsor, and the edge-matching space is a totally singular
Lagrangian \(L_{\mathrm{edge}}\). Hence

\[
\operatorname{Char}(L_{\mathrm{vert}})
\cap L_{\mathrm{edge}}\ne\varnothing.
\]

This should be the main paper proof of Theorem A. It is not a separate headline
result but the natural geometric form of the compatibility theorem.

### Theorem C — Cubic-flow cycle double cover

Every finite loopless cubic multigraph carrying a nowhere-zero
\(\mathbf F_2^3\)-flow has a cycle double cover.

This follows from Theorem A together with the local-family-to-cover extraction
and decomposition of the resulting even supports into circuits.

This is the main graph-theoretic theorem proved by the current public Lean
port.

### Theorem D / Corollary — Unconditional cycle double cover

The standard cycle double cover statement for finite loopless bridgeless
multigraphs follows from Theorem C together with the classical reduction to the
cubic case and the classical nowhere-zero 8-flow input.

Before the paper is frozen, this layer must be assigned one of two explicit
statuses:

1. **included and proved/cited in the paper**, with every reduction hypothesis
   checked and exact references supplied; or
2. **outside the formalized kernel**, with Theorem C stated as the formally
   verified endpoint and the unconditional conclusion stated only after a
   separately audited classical reduction.

The paper must never blur these two layers. The current Lean audit surface
states the unconditional conjecture, while the current port proves Theorem C.

### Theorem E — Dual-Fano residue criterion (sharpness layer)

For an equilibrium stress \(\psi\),

\[
\psi(c_f)=\sum_v\rho_v(\psi),
\]

where \(\rho_v=1\) exactly when the three local stress covectors form the three
nonzero points of a two-dimensional subspace of
\(\operatorname{Ann}(W_v)\), called a **dual Fano line**.

In rank three no such line fits in the one-dimensional annihilator, giving
another proof of Theorem A. Rank four is the first possible residue layer, and
the canonical \(K_{3,3}\) flow gives sharpness.

Recommended status: include the criterion and one rank-four sharpness example
in the paper, but keep the full counting formula and Pfaffian development in an
appendix or companion work if they disrupt the main line.

---

## 3. Minimal Paper Kernel

The definitions and results that should be shared by paper and Lean are:

1. cubic flow datum and vertex planes;
2. local affine-family classification;
3. incidence quotient spaces \(Q_e\);
4. \(L_{\mathrm{vert}}\), \(\kappa+L_{\mathrm{vert}}\), and
   \(L_{\mathrm{edge}}\);
5. equivalence with the affine equation \(\delta_fm=c_f\);
6. canonical rank-three quadratic forms on the edge quotients;
7. the local characteristic-torsor identity;
8. the global Lagrangian intersection proof;
9. extraction of a compatible family to the indexed dart cover/even supports;
10. decomposition into genuine cycles and Theorem C.

If Theorem E remains a numbered theorem in the main paper, its local residue
identity and global handshaking formula also belong to the formalization
kernel.

The following do **not** belong to the first formalization kernel:

- flow tensor and code-flag theory;
- Koszul homology;
- divided-square and coefficient-quotient exact sequences;
- chain-level incidence--tensor comparison;
- interface and cut-gluing theory;
- gauge-code circuit classifications;
- higher-rank decorated residue geometry beyond the chosen sharpness theorem.

These may be mentioned as outlooks without moving the paper/Lean spine.

---

## 4. Proposed paper architecture

### 1. Introduction and provenance

- state the cycle double cover problem and the paper's exact endpoint;
- identify the initial OpenAI proof and Lean development as the source of the
  construction and proof strategy;
- state the present paper's contributions: coordinate-free local
  classification, intrinsic affine incidence formulation, quadratic
  Lagrangian proof, residue/sharpness analysis, and independent Lean
  reconstruction;
- give a precise formalization-status paragraph.

### 2. Reductions and theorem statements

- distinguish the unconditional CDC statement, the cubic-flow theorem, and the
  affine compatibility theorem;
- state exactly which classical reductions are used and which are formalized.

### 3. Local affine Fano geometry

- classify all local even families;
- define the canonical local affine datum;
- identify the local family space as a torsor.

### 4. The affine incidence pair

- define the incidence space, vertex subspace, affine coset, and edge diagonal;
- prove that compatibility is the affine intersection problem and equivalently
  \(\delta_fm=c_f\).

### 5. Quadratic Lagrangian compatibility

- construct the canonical quotient quadratics;
- prove that flow conservation is the isotropy identity;
- identify the characteristic torsor;
- prove Theorem A in the shortest geometric form.

### 6. Duality, residue, and sharpness

- give the stress interpretation;
- state/prove the dual-Fano residue identity;
- explain why rank three is automatic and rank four is first sharp;
- include the canonical \(K_{3,3}\) example if it remains concise.

### 7. From compatibility to cycle double covers

- construct the indexed dart cover/even supports;
- decompose them into circuits;
- prove Theorem C;
- append or cite the classical reduction for Theorem D with exact status.

### 8. Formal verification

- theorem-to-Lean map;
- trust boundary and axiom audit;
- explain whether the paper's Lagrangian proof itself is formalized or whether
  the release still uses the equivalent branching proof.

### Appendix A. Comparison with the initial OpenAI proof

Give a compact but explicit dictionary between the ordered coordinate proof
and the intrinsic formulation. This preserves provenance without burdening the
main proof.

---

## 5. Lean strategy

The intended final state is not a permanent paper/Lean split. The paper-aligned
Lagrangian proof should be formalized if a bounded feasibility pass confirms
that the specialised \(\mathbf F_2\) framework is technically reasonable.

The development order should be:

1. freeze definitions and theorem statements from the Paper Kernel;
2. write detailed paper proofs down to Lean-sized lemmas;
3. implement one vertical Lean slice from local quadratic geometry to the
   existing gluing conclusion;
4. revise the paper kernel only when Lean exposes a genuine hidden assumption
   or a strictly cleaner lemma;
5. complete the new proof if the measured cost is reasonable;
6. retain the existing branching proof as an independent checked route until
   after release.

Acceptance is based on the total framework cost and elaboration behaviour, not
only on the final theorem's line count.

---

## 6. Relation to the initial OpenAI work

The relationship is substantive, not merely inspirational. The initial proof
already contains the local construction, affine compatibility equation,
dual separation, parity interpretation, and double-counting closure. The
present work changes the ontology and strengthens the explanation, but it does
not erase the origin of the proof strategy.

Recommended presentation:

- prominent attribution in the introduction;
- exact citation to the stable proof and Lean artefacts;
- a contribution list distinguishing reconstruction from new results;
- a comparison appendix or section;
- no claim of independent discovery of the CDC proof;
- contact or coordination with the original authors/releasers before final
  submission if publication/authorship status is not already explicit.

The main proof need not constantly refer back to the coordinate version. Once
proven equivalent, the paper may proceed entirely in the intrinsic language.

---

## 7. Immediate decision sequence

Do not launch the full Lagrangian Lean spike yet. First complete:

1. exact theorem statements for A--E;
2. a dependency list of paper lemmas;
3. a decision on the status of the unconditional reduction;
4. a decision on whether Theorem E is main text or appendix;
5. a detailed paper proof of the local characteristic-torsor identity and the
   global intersection theorem;
6. a theorem-to-existing-Lean map identifying reusable APIs.

After one adversarial review, the resulting Paper Kernel becomes the input to
the bounded Lean vertical slice.
