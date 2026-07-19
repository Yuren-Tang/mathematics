# AC-PD-A10 — complete finite-active-edge Cycle Double Cover assembly

**Proof-development state:** `READY-FOR-CURATOR`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Depends on:** `AC-PD-A0` through `AC-PD-A9`  
**External mathematical input:** Seymour's nowhere-zero six-flow theorem  
**Assurance:** complete authorial paper-proof checkpoint; not independent audit; not end-to-end Lean verification

## 0. Natural theorem

### Theorem 0.1 — finite-active-edge Cycle Double Cover theorem

Let

$$
G=(V,E,\partial)
$$

be a multigraph, allowing loops, parallel edge objects, disconnected components, isolated vertices, and an arbitrary ambient vertex carrier. Assume:

1. the active edge set $E$ is finite;
2. $G$ has no singleton cut.

Equivalently, by A0, no nonloop active edge is a bridge. Then there exists a finite indexed family, equivalently a finite multiset, of circuits of $G$ such that every active edge object belongs to exactly two circuit occurrences.

A circuit is a nonempty inclusion-minimal finite cut-even support. By A0, the circuits are exactly singleton loops, two-edge parallel digons, and ordinary simple cycle edge sets.

## 1. Exact proof assembly

### Step 1 — foundational semantics

A0 fixes the finite-active-edge multigraph model, intrinsic half-edge boundary parity, cut-even supports, circuits, components, and indexed/multiset occurrence multiplicity. It proves that cut-evenness is equivalent to empty intrinsic boundary, that singleton cuts are exactly bridges, and that all cut questions see only the finite active vertex set.

### Step 2 — delete loops

Let

$$
G_0=G[E\setminus L(G)]
$$

be the loopless core. A1 proves that all cuts are unchanged, so $G_0$ again has no singleton cut. Every core circuit remains a circuit of $G$, every circuit containing a loop is the singleton support of that loop, and a CDC of $G_0$ extends to one of $G$ by adding exactly two singleton occurrences for every deleted loop.

### Step 3 — cubic port-cycle expansion

Apply A2 to $G_0$. At every active vertex choose a cyclic order on its finite incidence set. The no-singleton-cut hypothesis excludes active degree one. The port-cycle construction gives a finite loopless cubic multigraph $H$ and maps

$$
\pi:V(H)\to V(G_0),
\qquad
\lambda:E(G_0)\hookrightarrow E(H).
$$

A2 proves:

- degree-two fibres are two-edge parallel cycles;
- edge-bearing components of $H$ correspond exactly to those of $G_0$;
- $H$ has no singleton cut;
- original edges are exactly the inter-fibre edges;
- collapsing fibres recovers the active graph $G_0$;
- for every $S\subseteq V(G_0)$,
  $$
  \delta_H(\pi^{-1}(S))=\lambda(\delta_{G_0}(S)).
  $$

### Step 4 — obtain a nowhere-zero binary rank-three flow

Apply A3 to $H$. Seymour's theorem gives a nowhere-zero integral six-flow on every edge-bearing component. Its value range is literally contained in the integral eight-flow range. Reducing modulo eight gives a nowhere-zero $\mathbf Z/8\mathbf Z$-flow.

A3 proves internally that the number of nowhere-zero flows over a finite abelian group depends only on the order of the group: a spanning forest gives the full flow-kernel count, and inclusion–exclusion removes zero coordinates. Since

$$
|\mathbf Z/8\mathbf Z|=|\mathbf F_2^3|=8,
$$

$H$ has a nowhere-zero $\mathbf F_2^3$-flow. On a loopless graph in characteristic two, orientation disappears and conservation is the once-per-edge incidence sum.

### Step 5 — form the affine compatibility object

Apply A4 to $(H,f)$. For every edge $a$, put

$$
Q_a=\mathbf F_2^3/\langle f(a)\rangle.
$$

The incidence space, vertex translation subspace, characteristic offset, and edge diagonal are

$$
E_f,
\qquad
L_{\mathrm{vert}},
\qquad
\kappa,
\qquad
L_{\mathrm{edge}}.
$$

The compatible local affine families are exactly

$$
(\kappa+L_{\mathrm{vert}})\cap L_{\mathrm{edge}}.
$$

A4 also identifies the pair-complex obstruction $[\kappa]$, the quotient equation $\delta_fm=c_f$, and the equilibrium-stress dual. The graph and dart data remain attached for support extraction.

### Step 6 — prove automatic rank-three compatibility

Apply the corrected A5 checkpoint. Each quotient $Q_a$ is a canonical nondegenerate anisotropic quadratic plane. The global vertex space is Lagrangian and

$$
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
=\kappa+L_{\mathrm{vert}}.
$$

The global edge diagonal is a totally singular Lagrangian. The abstract characteristic-torsor intersection theorem therefore yields a point

$$
x\in
(\kappa+L_{\mathrm{vert}})
\cap L_{\mathrm{edge}}.
$$

Choose the corresponding globally compatible collection of local affine even families.

### Step 7 — extract indexed supports upstairs

Apply A6. For every $s\in\mathbf F_2^3$, let $F'_s\subseteq E(H)$ be the set of edges whose common endpoint affine line contains $s$. A6 proves:

- each $F'_s$ is vertex-even;
- every edge of $H$ lies in exactly two indexed supports, because its affine line has exactly two points;
- empty supports and equal supports at different indices remain separate occurrences;
- multiset flattening preserves the occurrence count.

### Step 8 — convert vertex parity to intrinsic cut parity

Apply A7. Since $H$ is loopless, the once-per-edge incidence degree equals the intrinsic half-edge degree. Hence every $F'_s$ is cut-even, and $(F'_s)_{s\in\mathbf F_2^3}$ is an intrinsic even double cover of $H$.

### Step 9 — collapse supports

Apply A8 memberwise. Define

$$
F_s=\{e\in E(G_0):\lambda(e)\in F'_s\}.
$$

For every $S\subseteq V(G_0)$, the A2 cut identity gives a bijection

$$
F_s\cap\delta_{G_0}(S)
\longrightarrow
F'_s\cap\delta_H(\pi^{-1}(S)),
$$

so every $F_s$ is cut-even. For every original edge $e$,

$$
\{s:e\in F_s\}
=
\{s:\lambda(e)\in F'_s\},
$$

so $e$ remains covered exactly twice. Internal auxiliary edges disappear; empty and repeated projected occurrences remain harmless and correctly counted. Thus $(F_s)$ is an intrinsic even double cover of $G_0$.

### Step 10 — decompose once, downstairs

Apply A9 to each projected support. A9 proves by induction on $|F_s|$ that every finite cut-even support is a disjoint union of finitely many circuits. Concatenate the memberwise decompositions. For every core edge, the number of resulting circuit occurrences equals the number of parent supports containing it, namely two. Therefore $G_0$ has a cycle double cover.

### Step 11 — reinsert loops

Apply A1. Regard every core circuit as a circuit of $G$ and add exactly two occurrences of the singleton circuit $\{\ell\}$ for every deleted loop $\ell$. Nonloop and loop edge objects are now each covered exactly twice. This proves Theorem 0.1. $\square$

## 2. Boundary-case ledger

- **Empty active graph.** The empty family is a CDC; the general chain also degenerates correctly.
- **Loop-only graph.** The loopless core is empty and A1 returns two singleton occurrences per loop.
- **Isolated vertices and infinite ambient carrier.** Only endpoints of finitely many active edges enter the proof; isolated vertices are inert.
- **Disconnected graph.** Every stage is componentwise or a direct sum; connectedness is never assumed.
- **Parallel edges.** Edge-object identities are preserved through ports, flow coordinates, quotient summands, supports, collapse, and multiplicity.
- **Loops.** They are excluded only from the loopless incidence/flow adapter and are handled exactly by A1.

## 3. Dependency and checkpoint ledger

| Unit | State | Exact checkpoint | Principal output |
|---|---|---|---|
| `A0` | `COMPLETE-DRAFT` | `0d8c9102fa117e5f58b5d1617f3fae782c164097` | multigraph, cut, circuit, parity, and multiplicity semantics |
| `A1` | `COMPLETE-DRAFT` | `b193d55461040a6b6b7692e4f24e91d88c97a663` | exact loop deletion and reinsertion |
| `A2` | `COMPLETE-DRAFT` | `7c271c41f9d442ddb14034fb40b730fcc61c83a5` | finite loopless cubic expansion and collapse datum |
| `A3` | `COMPLETE-DRAFT` | `6817896a301157db886f7c016866748a9161d15f` | binary eight-flow boundary and internal equal-order transport |
| `A4` | `COMPLETE-DRAFT` | `93bd8019099f0fa10ee53928681167f81506c407` | affine pair complex, quotient, and stress obstruction |
| `A5` | `COMPLETE-DRAFT` | `6ce41bd87b5700346c572f701c40c8ac6f374e3f` | rank-three quadratic-Lagrangian compatibility |
| `A6` | `COMPLETE-DRAFT` | `f953619d6fda7105fef406892530496c7d72178a` | graph-level indexed even-support extraction |
| `A7` | `COMPLETE-DRAFT` | `b0755c3b95939482c6e223c24e4d8327c53f02e8` | loopless vertex/boundary/cut parity bridge |
| `A8` | `COMPLETE-DRAFT` | `d9718c6204d4f11aa853ee2f6e350d5c08444820` | collapse parity and exact multiplicity transport |
| `A9` | `COMPLETE-DRAFT` | `400404e5413dfc933668aa0ec152010bae5a742c` | finite circuit decomposition and concatenation |
| `A10` | `READY-FOR-CURATOR` | this corrected checkpoint | final theorem assembly and assurance ledger |

The persistent branch history is the authoritative exact sequence.

## 4. Source ledger

The sole external non-elementary existence theorem is:

P. D. Seymour, “Nowhere-zero 6-flows”, *Journal of Combinatorial Theory, Series B* **30** (1981), 130–135, DOI `10.1016/0095-8956(81)90058-7`.

It is used only for the componentwise existence of a nowhere-zero integral six-flow on a graph without an isthmus.

Tutte's equal-order finite-abelian-group flow theorem is historically relevant but is not a logical black box here: A3 proves the stronger counting statement required by the argument. All other graph, parity, affine, finite-dimensional linear-algebra, quadratic, collapse, and multiplicity assertions are proved in A0–A10.

## 5. Formal-status ledger

This checkpoint does **not** assert end-to-end machine verification. The companion `Yuren-Tang/affine-cdc` repository machine-checks substantial internal slices, including local affine-family classification, dart gluing, indexed dart supports, exact two-point coverage, same-vertex partner structure, and a graph-level cubic-flow CDC macro-Port.

The following invariant complete-spine layers are not thereby verified as one natural theorem:

- the finite-active-edge multigraph interface with loops and arbitrary ambient vertex carrier;
- the exact port-cycle expansion/collapse dossier used here;
- A3's internal flow-count proof in this organization;
- the invariant pair-complex and quadratic-Lagrangian global presentation;
- the even-cover-first collapse factorization;
- the final outer-shell and loop-reinsertion composition.

Therefore:

$$
\text{authorial proof-development completion}
\quad\text{is distinct from}\quad
\text{independent audit, Lean verification, peer review, and publication}.
$$

## 6. Load-bearing clarifications

The programme found no contradiction in the controlling theorem spine, but it made seven material clarifications.

1. Circuit semantics and characterization belong to A0; finite decomposition belongs to A9.
2. Intrinsic half-edge boundary parity is the natural multigraph notion; once-per-edge incidence parity is a loopless representation only.
3. Equal-order group-flow transport is proved internally, so historical Tutte page localization is not a logical gate.
4. The pair complex captures compatibility but not graph/dart/indexed-support semantics.
5. Cut-even supports and occurrence multiplicity collapse; circuits do not.
6. Equal support values at different indices remain distinct occurrences.
7. The natural hypotheses are finite active edge set and no singleton cut, without connectedness, looplessness, ambient-vertex finiteness, or simplicity.

## 7. Curator integration recommendation

This is a coherent Programme A checkpoint for bounded Curator intake. The Curator should consume the exact branch SHA named in the standing handoff, preserve the ten proof dossiers and DAG as provenance, integrate the natural theorem spine without collapsing assurance axes, record Seymour 1981 as the sole external non-elementary logical input, and route any mathematical defect back to AC-PDL as a repair unit.

No movement of `main`, merge, release, DOI, manuscript, or formalization surface is requested or authorized by this dossier.

## 8. Independent-review targets

A later independent audit should test at least:

1. A2's external-edge nonbridge lift through arbitrary port-cycle fibres;
2. A3's spanning-forest kernel count and inclusion–exclusion;
3. A4's local-classification identification;
4. A5's cross-pairing and characteristic-torsor intersection;
5. A6's dart-to-edge descent and exact occurrence count;
6. A8's pulled-back-cut identity;
7. A9's count under repeated parent occurrences;
8. final loop/core circuit reinsertion.

These are assurance targets, not known defects.

## 9. Programme transition

Programme A is complete at the authorial proof-development level and ready for Curator intake. The persistent role continues. The next active dependency-respecting unit is Programme B1: normalize and prove the root-flow, fixed-plane, and fixed-lift equivalence chain for the open five-support programme, while the global B9 implication remains `BLOCKED-FRONTIER` until a genuine new-mathematics bridge is supplied.
