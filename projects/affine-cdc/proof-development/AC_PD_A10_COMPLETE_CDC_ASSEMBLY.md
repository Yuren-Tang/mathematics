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

\[
G=(V,E,\partial)
\]

be a multigraph, allowing loops, parallel edge objects, disconnected components, isolated vertices, and an arbitrary ambient vertex carrier. Assume:

1. the active edge set `E` is finite;
2. `G` has no singleton cut.

Equivalently, by A0, assume that no nonloop active edge is a bridge.

Then there exists a finite indexed family, equivalently a finite multiset, of circuits of `G` such that every active edge object belongs to exactly two circuit occurrences.

Here a circuit is a nonempty inclusion-minimal finite cut-even support. By A0, the circuits are exactly:

- singleton loops;
- two-edge parallel digons;
- ordinary simple cycle edge sets.

This is the natural finite-active-edge multigraph form of the Cycle Double Cover statement.

## 1. Exact proof assembly

### Step 1 — foundational semantics

Apply A0. All cut questions reduce to the finite active vertex set. Intrinsic cut-evenness is equivalent to empty half-edge boundary, with loops counted twice. Singleton cuts are exactly bridges. Indexed occurrences, rather than distinct support values, govern coverage multiplicity.

### Step 2 — delete loops

Let

\[
G_0:=G[E\setminus L(G)]
\]

be the loopless core. By A1:

- `G_0` has finite active edge set;
- every cut of `G_0` is exactly the corresponding cut of `G`;
- `G_0` has no singleton cut;
- every nonloop circuit of `G_0` remains a circuit of `G`;
- every circuit of `G` containing a loop is the singleton support of that loop.

It is therefore enough to construct a CDC of `G_0`; two singleton occurrences of every deleted loop will then restore a CDC of `G`.

### Step 3 — cubic port-cycle expansion

Apply A2 to `G_0`. Choose one cyclic order on the finite incidence set of every active vertex. Since the no-singleton-cut condition excludes active degree one, every active degree is at least two.

Construct the port-cycle expansion

\[
H
\]

with collapse data

\[
\pi:V(H)\to V(G_0),
\qquad
\lambda:E(G_0)\hookrightarrow E(H).
\]

A2 proves:

- `H` is finite, loopless, and cubic;
- degree-two fibres consist of two distinct parallel auxiliary edges;
- edge-bearing components of `H` correspond exactly to those of `G_0`;
- `H` has no singleton cut;
- original edges are exactly the inter-fibre edges;
- collapsing complete fibres recovers the active graph `G_0`;
- for every `S\subseteq V(G_0)`,
  \[
  \delta_H(\pi^{-1}(S))=\lambda(\delta_{G_0}(S)).
  \]

### Step 4 — obtain a nowhere-zero binary rank-three flow

Apply A3 to `H`. Seymour's theorem gives a nowhere-zero integral six-flow on every edge-bearing component. The value range is literally contained in the integral eight-flow range. Reduction modulo eight gives a nowhere-zero `\mathbf Z/8\mathbf Z`-flow.

A3 proves internally, by spanning-forest kernel counting and inclusion–exclusion, that the number of nowhere-zero flows over a finite abelian group depends only on the order of the group. Since

\[
|\mathbf Z/8\mathbf Z|
=|\mathbf F_2^3|=8,
\]

`H` has a nowhere-zero `\mathbf F_2^3`-flow. In characteristic two and on a loopless graph, orientation disappears and the conservation law is the once-per-edge incidence sum.

### Step 5 — form the affine compatibility object

Apply A4 to the cubic flow graph `(H,f)`. For every edge `a`, put

\[
Q_a:=\mathbf F_2^3/\langle f(a)\rangle.
\]

The incidence space, vertex translation subspace, local characteristic offset, and edge diagonal are

\[
E_f,
\qquad
L_{\mathrm{vert}},
\qquad
\kappa,
\qquad
L_{\mathrm{edge}}.
\]

The compatible local affine families are exactly

\[
(\kappa+L_{\mathrm{vert}})
\cap L_{\mathrm{edge}}.
\]

A4 also identifies the pair-complex obstruction `[\kappa]`, the quotient equation `\delta_fm=c_f`, and the equilibrium-stress dual. The original graph and dart data remain attached for the later support extraction.

### Step 6 — prove automatic rank-three compatibility

Apply A5. Each edge quotient `Q_a` is a canonical nondegenerate anisotropic quadratic plane. The global vertex space is Lagrangian, and its characteristic torsor is exactly

\[
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
=
\kappa+L_{\mathrm{vert}}.
\]

The global edge diagonal is a totally singular Lagrangian. The abstract characteristic-torsor intersection theorem therefore gives

\[
(\kappa+L_{\mathrm{vert}})
\cap L_{\mathrm{edge}}
e\varnothing.
\]

Choose one compatible collection of local affine even families.

### Step 7 — extract indexed graph supports upstairs

Apply A6. For every point

\[
s\in\mathbf F_2^3,
\]

let `F'_s\subseteq E(H)` be the set of edges whose common endpoint affine line contains `s`.

A6 proves:

- each `F'_s` is vertex-even;
- every edge of `H` belongs to exactly two indexed supports, because its affine line has exactly two points;
- empty supports and equal supports at different indices remain separate indexed occurrences;
- passing to the image multiset preserves occurrence multiplicity.

### Step 8 — convert upstairs vertex parity to intrinsic cut parity

Apply A7. Since `H` is loopless, the once-per-edge incidence degree equals the intrinsic half-edge degree. Therefore every `F'_s` is cut-even. Thus

\[
(F'_s)_{s\in\mathbf F_2^3}
\]

is an intrinsic even double cover of `H`.

### Step 9 — collapse the even supports

Apply A8 memberwise. Define

\[
F_s:=\{e\in E(G_0):\lambda(e)\in F'_s\}.
\]

For each vertex subset `S\subseteq V(G_0)`, the A2 cut pullback gives a bijection

\[
F_s\cap\delta_{G_0}(S)
\xrightarrow{\sim}
F'_s\cap\delta_H(\pi^{-1}(S)).
\]

Hence every `F_s` is cut-even. For every original edge `e`,

\[
\{s:e\in F_s\}
=
\{s:\lambda(e)\in F'_s\},
\]

so `e` is covered exactly twice. Internal auxiliary edges disappear; empty and repeated projected occurrences remain harmless and correctly counted.

Thus `(F_s)` is an intrinsic even double cover of `G_0`.

### Step 10 — decompose downstairs, once

Apply A9 to every projected support `F_s`. A9 proves by induction on `|F_s|` that each finite cut-even support is a disjoint union of finitely many circuits. Empty supports contribute no circuits.

Concatenate the memberwise decompositions. For every core edge `e`, the number of resulting circuit occurrences containing `e` equals the number of parent supports containing `e`, namely two. Therefore `G_0` has a cycle double cover.

### Step 11 — reinsert loops

Apply A1. Regard every core circuit as a circuit of `G`. For every deleted loop `\ell`, append exactly two occurrences of the singleton circuit

\[
\{\ell\}.
\]

Every nonloop edge remains covered exactly twice, and every loop is covered exactly twice. The resulting finite circuit family is a cycle double cover of `G`. This proves Theorem 0.1. ∎

## 2. Boundary-case ledger

### Empty active graph

The empty family is a CDC. The general chain also remains valid: the loopless core and its expansion are empty, the empty flow is nowhere-zero vacuously, the affine spaces are zero, and no decomposition occurrence is produced.

### Loop-only graph

The loopless core is empty. A1 returns the explicit CDC consisting of two singleton occurrences for each loop.

### Isolated vertices and infinite ambient vertex carrier

Only endpoints of finitely many active edges enter the proof. Isolated vertices do not affect cuts, flows, affine data, supports, or circuits. No finiteness assumption on the whole ambient vertex set is required.

### Disconnected graph

Every stage is componentwise or a direct sum:

- no-singleton-cut and bridge status;
- port-cycle expansion;
- Seymour flow application;
- affine incidence and quadratic compatibility;
- support parity;
- circuit decomposition.

No connectedness hypothesis is used.

### Parallel edges

Parallel edge objects remain distinct through ports, lifted edges, flow coordinates, quotient summands, support membership, collapse, and circuit multiplicity. Degree-two fibres deliberately use two distinct parallel auxiliary edges.

### Loops

Loops are absent from the once-per-edge incidence adapter and the cubic flow graph. Their intrinsic parity and circuit status are handled solely by exact deletion and forced singleton reinsertion.

## 3. Dependency and commit ledger

| Unit | State | Exact checkpoint | Principal output |
|---|---|---|---|
| `A0` | `COMPLETE-DRAFT` | `0d8c9102fa117e5f58b5d1617f3fae782c164097` | multigraph, cut, circuit, parity, multiplicity semantics |
| `A1` | `COMPLETE-DRAFT` | `b193d55461040a6b6b7692e4f24e91d88c97a663` | exact loop deletion and reinsertion |
| `A2` | `COMPLETE-DRAFT` | `7c271c41f9d442ddb14034fb40b730fcc61c83a5` | finite loopless cubic expansion and collapse datum |
| `A3` | `COMPLETE-DRAFT` | `6817896a301157db886f7c016866748a9161d15f` | `BinaryEightFlow` boundary and internal equal-order transport |
| `A4` | `COMPLETE-DRAFT` | `93bd8019099f0fa10ee53928681167f81506c407` | affine pair complex, quotient, and stress obstruction |
| `A5` | `COMPLETE-DRAFT` | `75828cc134321f56f0b0260cbb88ae8a436a967f` | rank-three quadratic-Lagrangian compatibility |
| `A6` | `COMPLETE-DRAFT` | `f953619d6fda7105fef406892530496c7d72178a` | graph-level indexed even-support extraction |
| `A7` | `COMPLETE-DRAFT` | `b0755c3b95939482c6e223c24e4d8327c53f02e8` | loopless vertex/boundary/cut parity bridge |
| `A8` | `COMPLETE-DRAFT` | `d9718c6204d4f11aa853ee2f6e350d5c08444820` | collapse parity and exact multiplicity transport |
| `A9` | `COMPLETE-DRAFT` | `400404e5413dfc933668aa0ec152010bae5a742c` | finite circuit decomposition and concatenation |
| `A10` | `READY-FOR-CURATOR` | this checkpoint | final theorem assembly and assurance ledger |

The persistent branch history, not this table alone, is the authoritative exact sequence.

## 4. Source ledger

### Sole external non-elementary existence theorem

P. D. Seymour, “Nowhere-zero 6-flows”, *Journal of Combinatorial Theory, Series B* **30** (1981), 130–135, DOI `10.1016/0095-8956(81)90058-7`.

The proof uses only the theorem that every finite graph without an isthmus has a nowhere-zero integral six-flow. It is applied componentwise.

### Not an external logical dependency

Tutte's equal-order finite-abelian-group flow theorem is historically relevant but no longer a logical black box in this chain. A3 proves the stronger counting statement needed here by:

1. counting the full flow kernel over an arbitrary finite abelian group using a spanning forest;
2. applying inclusion–exclusion over zero coordinates.

### Internal elementary proof blocks

All remaining graph, parity, finite-dimensional linear-algebra, quadratic, affine, and multiplicity statements are proved in A0–A10.

## 5. Formal-status ledger

This checkpoint does **not** assert end-to-end machine verification.

The companion `Yuren-Tang/affine-cdc` repository currently machine-checks substantial internal slices, including:

- local affine-family classification and torsor equivariance;
- dart gluing and indexed dart supports;
- exact two-point edge coverage;
- same-vertex partner and rotation structure;
- a graph-level cubic-flow CDC macro-Port, including generic even-support decomposition.

The following complete-spine layers are not thereby verified as one natural theorem in the invariant form used here:

- the finite-active-edge multigraph interface with loops and arbitrary ambient vertex carrier;
- the exact port-cycle expansion/collapse dossier as written here;
- the internal equal-order flow-count proof in this paper organization;
- the invariant pair-complex and quadratic-Lagrangian global presentation;
- the deliberate even-cover-first collapse factorization;
- the final outer-shell composition and exact loop reinsertion.

Accordingly the status is:

\[
\boxed{
\text{complete authorial proof-development checkpoint}
\ne
\text{independent audit}
\ne
\text{end-to-end formal proof}
\ne
\text{peer-reviewed publication}.
}
\]

## 6. Corrections and sharpenings relative to the initial corpus

This programme did not find a contradiction in the controlling theorem spine. It did make several load-bearing clarifications.

1. **A0/A9 separation.** Circuit semantics and characterization belong to A0; finite decomposition belongs to A9.
2. **Loop parity boundary.** Intrinsic half-edge boundary parity is the natural multigraph notion. The companion once-per-edge incidence predicate is valid only on the loopless core.
3. **Tutte boundary.** Equal-order group-flow transport is proved internally; unresolved historical page localization is not a logical blocker.
4. **Compatibility information boundary.** The pair complex completely captures compatibility but not graph/dart/indexed-support semantics.
5. **Collapse boundary.** Cut-even supports and exact multiplicity collapse; circuits are not projected.
6. **Multiplicity boundary.** Equal support values at different indices remain different occurrences throughout transport and decomposition.
7. **Natural hypotheses.** The theorem requires finite active edge set and no singleton cut, not connectedness, looplessness, finiteness of the ambient vertex carrier, or simplicity.

## 7. Curator integration recommendation

This is a coherent Programme A checkpoint suitable for bounded Curator intake. Recommended integration behavior:

1. consume the exact branch head containing A0–A10, not a moving later tip;
2. preserve the ten proof dossiers and persistent DAG as proof-development provenance;
3. integrate the natural theorem spine into the existing architecture rather than replacing formal-status or provenance records wholesale;
4. record Seymour 1981 as the sole external non-elementary logical input;
5. retain the distinction between authorial proof completion, independent audit, Lean projection, manuscript projection, release, and publication;
6. expose the sharpened parity, compatibility-image, collapse, and multiplicity boundaries in the natural chapters;
7. route any integration-discovered mathematical defect back to AC-PDL as a repair unit.

No `main` movement, merge, release, DOI, manuscript, or formalization action is requested or authorized by this dossier.

## 8. Independent-review targets

A later independent audit should at minimum test:

1. A2's external-edge nonbridge lift through arbitrary disconnected port-cycle fibres;
2. A3's spanning-forest flow-kernel count and inclusion–exclusion transport;
3. A4's exact identification of the local classification with `κ_v+L_v`;
4. A5's local cross-pairing identity and characteristic-torsor intersection theorem;
5. A6's descent from `σ`-closed dart supports to edge supports and exact occurrence count;
6. A8's pulled-back-cut identity and memberwise parity transport;
7. A9's decomposition count under repeated parent occurrences;
8. the final loop/core circuit classification used in reinsertion.

These are assurance targets, not known defects.

## 9. Programme transition

Programme A is complete at the authorial proof-development level and is ready for Curator intake. The persistent AC-PDL role does not end. After emitting the exact checkpoint, the next dependency-respecting active programme is Programme B, beginning with `AC-PD-B1`: normalize and prove the root-flow, fixed-plane, and fixed-lift equivalence chain for the open five-support theorem, while retaining the global `B9` frontier as `BLOCKED-FRONTIER` until its exact missing implication is closed.
