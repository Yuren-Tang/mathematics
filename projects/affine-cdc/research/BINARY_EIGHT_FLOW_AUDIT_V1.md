# Binary Eight-Flow interface and convention audit V1

**Workstream:** M2 — Binary Eight-Flow Audit  
**Base:** `749e0579581fcc838685138b3582f4de306b8e72`  
**Owned branch:** `research/affine-cdc-binary-eight-flow-v1`  
**Audit target:** M1 `OUTER_SHELL_RESEARCH_V1.md`, especially Theorem 1.1, External Theorems 4.1–4.2, and Corollary 4.3  
**Closure:** decisive correction identified; the proposed route is valid after a loop/convention correction and a source-statement split

## 1. Executive verdict

The proposed route

\[
\text{Seymour integer 6-flow}
\Longrightarrow
\text{integer 8-flow}
\Longrightarrow
\text{nowhere-zero }\mathbf F_2^3\text{-flow}
\]

is mathematically valid for the graph actually produced by M1: a finite, loopless, bridgeless multigraph, with parallel edges allowed and connectedness not required.

Two corrections are necessary.

1. **M1 Corollary 4.3 must say “finite loopless bridgeless multigraph”.**  
   The standard oriented group-flow theorem can harmlessly admit loops, but the AffineCDC port does not use the oriented boundary. It uses the unoriented sum over `incidenceSet`, in which a loop is counted once. Hence a nonzero loop value does not cancel. The one-vertex one-loop graph is bridgeless under the usual cut-edge convention but has no `Port.NowhereZeroFlow`: conservation would force the loop value to be zero. Thus the unqualified wording is false under the project convention if “multigraph” permits loops.

2. **M1 External Theorem 4.2 must split existence from counting.**  
   The needed statement is the existence equivalence between an integer \(k\)-flow and a nowhere-zero flow over any finite abelian group of order \(k\). The separate theorem that the number of nowhere-zero group flows depends only on the group order is stronger and is not logically “equivalent” to the existence statement. It also does not say that the number of bounded integer \(k\)-flows equals the number of group flows.

With those corrections, M1 Theorem 1.1 is correct as written. No obstruction remains to exposing a single classical `BinaryEightFlow` interface for finite-active-edge loopless graphs with no singleton cut.

## 2. Sources and exact theorem forms

### 2.1 Seymour's six-flow theorem

The original source is:

- P. D. Seymour, “Nowhere-zero 6-flows”, *Journal of Combinatorial Theory, Series B* **30** (1981), 130–135.

For an exact accessible primary-proof formulation matching the M1 expansion, use:

- Matt DeVos, Edita Rollová, and Robert Šámal, “A new proof of Seymour's 6-flow theorem”, arXiv:1512.06214, §§1–2.

That paper states its conventions before the theorem:

- parallel edges are permitted;
- loops are forbidden;
- a \(\Gamma\)-flow is an oriented edge function satisfying the signed Kirchhoff law;
- an integer \(k\)-flow is a \(\mathbb Z\)-flow with \(|\varphi(e)|<k\);
- “nowhere-zero” adds \(\varphi(e)\neq0\) on every edge;
- orientation reversal together with value negation preserves the notion.

Its Theorem 2 states:

> Every 2-edge-connected graph has a nowhere-zero 6-flow.

In that paper “2-edge-connected” means connected and without a cut-edge, not 2-vertex-connected: the reduction proof explicitly considers a cut vertex. Thus the exact form suitable for this audit is:

> **Seymour interface, connected loopless form.**  
> Every finite connected loopless multigraph with no cut-edge, allowing parallel edges, admits an orientation and an integer circulation \(\varphi\) such that
> \[
> 0<|\varphi(e)|<6
> \]
> for every edge \(e\).

A second primary-proof source confirms the modular formulation and broader loop convention:

- Matt DeVos, Jessica McDonald, and Kathryn Nurse, “Another proof of Seymour's 6-flow theorem”, arXiv:2302.08625.

It explicitly permits loops and parallel edges and states Seymour's theorem as existence of a nowhere-zero \(\mathbb Z_6\)-flow on every 2-edge-connected digraph. It then invokes Tutte to obtain the bounded integer 6-flow formulation. This is equivalent for existence, but the loopless 2015 formulation is the cleaner source boundary for M1 because the expansion \(H\) is loopless.

### 2.2 Tutte's equal-order group-flow theorem

The classical source is:

- W. T. Tutte, “A contribution to the theory of chromatic polynomials”, *Canadian Journal of Mathematics* **6** (1954), 80–91, DOI `10.4153/CJM-1954-010-9`.

The exact existence theorem needed here is:

> **Tutte existence theorem.**  
> Let \(X\) be a finite graph, let \(k\ge2\), and let \(A\) be a finite abelian group with \(|A|=k\). Then \(X\) has a nowhere-zero integer \(k\)-flow if and only if \(X\) has a nowhere-zero \(A\)-flow.

The cyclic special case
\[
\text{integer }k\text{-flow}\iff \mathbb Z/k\mathbb Z\text{-flow}
\]
is not enough by itself at \(k=8\), because
\[
\mathbb Z/8\mathbb Z\not\cong(\mathbb Z/2\mathbb Z)^3.
\]
The arbitrary equal-order abelian-group statement is the required step.

DeVos–Rollová–Šámal, arXiv:1512.06214, Theorem 3 and the sentence immediately following it, records exactly this distinction: Theorem 3 gives the cyclic equivalence, and the paper notes Tutte's more general theorem for every abelian group of order \(k\).

Tutte's flow-polynomial theory also gives a separate counting result:

> For a fixed finite graph \(X\), the number of nowhere-zero \(A\)-flows depends only on \(|A|\), not on the isomorphism type of \(A\).

This counting statement is not needed for AffineCDC. It must not be conflated with equality between the number of group flows and the number of bounded integer flows. For example, on a consistently oriented cycle, a group \(A\) has \(|A|-1\) nowhere-zero \(A\)-flows, whereas the same fixed orientation has \(2(k-1)\) nowhere-zero integer \(k\)-flows.

## 3. Convention table

| Topic | Audited classical source boundary | M1 expansion \(H\) | AffineCDC `Port.NowhereZeroFlow` | Audit result |
|---|---|---|---|---|
| Finiteness | finite graph | finite active graph, with exact finite \(V(H),E(H)\) | current Lean checkpoint assumes finite ambient vertex and edge types | compatible |
| Connectedness | Seymour source theorem is connected (`2-edge-connected`) | not necessarily connected | port theorem does not require connectedness | apply componentwise |
| Bridge condition | no cut-edge in each connected graph | no singleton cut globally | no bridge hypothesis inside the structure; supplied externally | equivalent componentwise |
| Parallel edges | explicitly allowed | required for degree-two fibre cycles | Mathlib `Graph α β` distinguishes edge objects | compatible |
| Loops | 2015 Seymour source forbids loops; 2023 modular source permits them | loopless | unoriented incidence sum counts a loop once | interface must remain loopless |
| Orientation | chosen arbitrarily; signed Kirchhoff law | no orientation stored | orientation-free sum in characteristic two | compatible only for loopless graphs |
| Integer \(k\)-flow | \(0<|\varphi(e)|<k\) | used only externally | not represented | monotonicity is immediate |
| Group flow | signed \(A\)-valued boundary \(0\) | external intermediate | \(A=\mathbf F_2^3\), unsigned incidence sum | compatible in exponent two and loopless |
| Isolated vertices | normally absent from a connected theorem | allowed through empty fibres / ambient carriers | conservation only on actual vertices | vacuous |
| Empty graph | outside nontrivial connected theorem wording | possible when the original graph has no active edges | unique empty active-edge datum | handle separately, trivially |

## 4. Required reductions for the M1 expansion graph

Let \(H\) be the graph supplied by M1 Theorem 3.2. It is finite, loopless, cubic, bridgeless, and may be disconnected.

### 4.1 Reduction to connected components

Every edge of \(H\) lies in a connected component containing an edge. Since \(E(H)\) is finite, there are finitely many such components. The global no-singleton-cut condition implies that no edge is a cut-edge in its component: if deleting \(e\) separates its component, one side of that separation has cut exactly \(\{e\}\) in the whole graph.

Each edge-bearing component is therefore a finite connected loopless multigraph with no cut-edge. Parallel edges are allowed. Apply Seymour's theorem independently to every such component. Isolated vertices impose no condition, and if \(H\) has no edges the desired flow is vacuous.

The component flows combine into one integer 6-flow on all active edges of \(H\). No compatibility across components is required because Kirchhoff conservation is vertex-local.

### 4.2 Parallel edges and two-cycles

Seymour's audited source convention permits parallel edges. A degree-two fibre in M1 is a two-cycle formed by two distinct parallel edge objects, not by loops. Each edge receives its own flow value and is counted separately at both endpoints. No reduction to a simple graph is needed and none should be inserted.

### 4.3 Monotonicity \(6\)-flow \(\Rightarrow 8\)-flow

Under the exact integer definition, a nowhere-zero 6-flow is an integer circulation \(\varphi\) satisfying
\[
0<|\varphi(e)|<6
\]
for all \(e\). The same orientation and the same integer function satisfy
\[
0<|\varphi(e)|<8.
\]
Thus it is an integer 8-flow. This implication is literal inclusion of allowed ranges; no rescaling, modular reduction, or new theorem is involved.

More generally, an integer \(k\)-flow is an integer \(\ell\)-flow whenever \(\ell\ge k\).

### 4.4 Transfer to \(\mathbf F_2^3\)

Apply Tutte's theorem at \(k=8\) and
\[
A=(\mathbb Z/2\mathbb Z)^3=\mathbf F_2^3.
\]
Since \(|A|=8\), the integer 8-flow gives a nowhere-zero \(A\)-flow on the same graph.

This use requires the arbitrary-group theorem, not an isomorphism with \(\mathbb Z/8\mathbb Z\).

### 4.5 Forgetting orientation in characteristic two

For an oriented loopless graph, group-flow conservation at a vertex \(v\) is
\[
\sum_{e\in\delta^+(v)}f(e)-\sum_{e\in\delta^-(v)}f(e)=0.
\]
In \(\mathbf F_2^3\), \(-a=a\). Because every nonloop edge incident with \(v\) occurs exactly once, the equation becomes
\[
\sum_{e\ni v}f(e)=0,
\]
which is exactly the AffineCDC port convention.

No orientation data needs to be retained. Reorienting an edge would replace \(f(e)\) by \(-f(e)=f(e)\), so in this coefficient group even the edge value is unchanged.

### 4.6 Why loops are a genuine mismatch

For a loop at \(v\), the oriented boundary contains one outgoing and one incoming occurrence, hence contribution
\[
f(e)-f(e)=0.
\]
Mathlib's `Graph.incidenceSet v` is a set of edge objects, so the same loop occurs once in the AffineCDC unoriented sum. It contributes \(f(e)\), not zero.

Therefore the oriented characteristic-two equation and the current port equation agree only after imposing looplessness. On the one-vertex one-loop graph, standard group-flow conservation permits any nonzero value, while `Port.NowhereZeroFlow` demands \(f(e)=0\). This is the decisive convention correction.

## 5. Recommended external project interface

### 5.1 Weakest mathematical interface

The project should expose exactly the following paper-level theorem and no integer or orientation machinery above it:

> **BinaryEightFlow.**  
> Let \(G\) be a loopless multigraph with finite active edge set. Assume
> \[
> \forall S\subseteq V(G),\qquad |\delta_G(S)|\ne1.
> \]
> Then there exists
> \[
> f:E(G)\to\mathbf F_2^3\setminus\{0\}
> \]
> such that for every active vertex \(v\),
> \[
> \sum_{e\ni v}f(e)=0.
> \]

Hypotheses and non-hypotheses:

- finite active edge set: required;
- loopless: required by the current unoriented port;
- no singleton cut: required;
- parallel edges: allowed;
- connectedness: not required;
- simplicity: not required;
- cubicity: not required;
- finite ambient vertex carrier: not required;
- an orientation: not part of the output.

This is the weakest exact external node consumed by M1 Theorem 1.1.

### 5.2 Declaration-level Lean boundary

At the current companion checkpoint, where `Port.NowhereZeroFlow` is already defined and ambient types are finite, the intended isolated axiom/theorem boundary is schematically:

```lean
/-- Classical binary eight-flow interface; no proof is supplied here. -/
theorem binaryEightFlow
    {α β : Type*} [Finite α] [Finite β] (G : Graph α β)
    (hloop : Loopless G)
    (hbridge : NoSingletonCut G) :
    ∃ f : β → Port.Γ, Port.NowhereZeroFlow G f
```

`NoSingletonCut G` should be defined by the existing cut semantics, not silently replaced by a connectedness predicate. The theorem should constrain only `e ∈ E(G)` and actual vertices, as `Port.NowhereZeroFlow` already does.

A later active-edge-finite migration may weaken `[Finite α] [Finite β]` to finiteness of the actual active edge set and derive finiteness of active vertices. That migration is not part of M2.

### 5.3 Unresolved formalization boundary

The classical theorem remains external. A formal proof would require at least:

1. an oriented-boundary/group-flow API for Mathlib multigraphs;
2. integer \(k\)-flows and the monotonicity adapter;
3. Tutte's integer/group existence theorem;
4. Seymour's six-flow theorem;
5. a proved adapter from oriented \(\mathbf F_2^3\)-flow to `Port.NowhereZeroFlow` under looplessness;
6. componentwise assembly for disconnected graphs.

M2 does not begin any of these formalizations.

## 6. Mathlib and public AffineCDC availability

### 6.1 Current Mathlib graph substrate

The public Mathlib `Graph α β` substrate supports exactly the needed multigraph shape:

- vertices and edges are separate ambient types;
- edges are distinct objects;
- parallel edges are permitted;
- loops are representable;
- `incidenceSet` records incident edge objects.

Relevant file:

- `Mathlib/Combinatorics/Graph/Basic.lean` at inspected public commit `805e37bcd56717e0be3ca2cbc4117e5e5590460f`.

Repository-wide searches at that checkpoint for `NowhereZeroFlow`, graph-level `Kirchhoff`, and a graph-flow namespace found no reusable nowhere-zero flow interface or Seymour/Tutte theorem. Mathlib supplies the multigraph substrate, not the required classical flow package.

### 6.2 Public AffineCDC repository

The companion repository `Yuren-Tang/affine-cdc` already contains:

- `lean/AffineCDC/Port.lean`;
- `Port.Γ := Fin 3 → ZMod 2`;
- `Port.NowhereZeroFlow`, with nonzero active-edge values and the unoriented `incidenceSet` conservation law;
- `CubicFlowCDCStatement`, requiring `Loopless G`, cubicity, and a `Port.NowhereZeroFlow`.

This is the correct consumer-side interface. It does not contain a theorem producing such a flow from bridgelessness. The new external theorem should therefore be isolated above `Port.NowhereZeroFlow`, rather than duplicating or changing the port structure.

The structure itself does not include a `Loopless` field. This is acceptable provided every theorem that interprets it as an ordinary group flow retains an explicit loopless hypothesis. A future loop-aware API would need an oriented boundary or a loop-counted-with-signs incidence object.

## 7. Corrections required in M1

### 7.1 Theorem 1.1

**Verdict: correct as written.**

Its graph \(H\) is explicitly finite and loopless; parallel edges are intentionally used; connectedness is not assumed; and the target flow equation is exactly obtained by the audited componentwise route.

The proof should cite the corrected loopless version of Corollary 4.3.

### 7.2 External Theorem 4.1

**Verdict: correct after source/convention precision.**

Recommended replacement:

> Every finite connected loopless multigraph with no cut-edge, allowing parallel edges, has a nowhere-zero integer 6-flow. For a finite loopless graph with no singleton cut but several components, apply the theorem independently to each edge-bearing connected component; isolated vertices and the empty graph are vacuous.

This avoids using “bridgeless” and “2-edge-connected” as though their connectedness conventions were universal.

### 7.3 External Theorem 4.2

**Verdict: mathematically sufficient, but wording must be split.**

Recommended replacement:

> Let \(X\) be a finite graph, \(k\ge2\), and \(A\) a finite abelian group of order \(k\). Then \(X\) has a nowhere-zero integer \(k\)-flow if and only if it has a nowhere-zero \(A\)-flow.

Then add separately, if desired:

> Tutte's flow-polynomial theorem also implies that the number of nowhere-zero \(A\)-flows depends only on \(|A|\). This counting fact is not used and is not an equality with the number of bounded integer flows.

### 7.4 Corollary 4.3

**Verdict: correct after a precise wording change; false under a loop-allowing reading of the project convention.**

Recommended replacement:

> **Binary eight-flow input.** Every finite loopless bridgeless multigraph, allowing parallel edges and not necessarily connected, has a nowhere-zero \(\mathbf F_2^3\)-flow in the AffineCDC unoriented incidence-sum sense.

The proof should explicitly mention:

1. componentwise Seymour;
2. literal \(6\to8\) range inclusion;
3. Tutte for the arbitrary order-eight group \(\mathbf F_2^3\);
4. looplessness when converting signed conservation to the incidence sum.

## 8. Audit closure

The bounded unit closes at a necessary correction rather than an obstruction.

- The `BinaryEightFlow` route is verified.
- M1's outer-shell theorem remains valid.
- The unqualified loop convention in Corollary 4.3 is unsafe and admits a one-loop counterexample under the current port semantics.
- The Tutte existence theorem and group-flow counting theorem must be stated separately.
- No current Mathlib theorem supplies the external flow input.
- No formalization of Seymour or Tutte was started.

## 9. Higher possibility found

**Yes, not pursued.** A generic oriented finite-abelian-group flow interface, together with a proved characteristic-two loopless adapter to `Port.NowhereZeroFlow`, would be reusable beyond \(\mathbf F_2^3\) and would make the loop convention impossible to obscure. It is a separate engineering/formalization workstream, not part of this audit.
