# AC-PD-OR1 — orientation obstruction proof map

**State:** `READY-FOR-CURATOR / FIXED-FIBRE CLASSIFICATION COMPLETE / GLOBAL OPEN`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Priority insert:** research-workbench issue #37 comment `5049496439`  
**Direct-execution decision:** AC-PDL took OR1 directly at the safe boundary `9ce8de5ca5b7b41e139be4c94572de7725446046`; no child branch or worker was created  
**Audit return status:** issue #49 is a triggering review input only; every promoted statement is reproved in OR1.1--OR1.3

## 1. Exact objects

For a finite loopless cubic multigraph `G`, a nowhere-zero Fano flow `f`, and a compatible labelled root lift `g`:

- `S_g` is the cycle-face surface reconstructed from the indexed support occurrences and the dart permutations `partner`, `sigma`, `rho`;
- `w(g) in C^1(G)` is the signed-rotation edge-twist word after choosing vertex-disc orientations;
- `omega(g)=[w(g)] in C^1(G)/Cut(G)` is the fixed-lift orientation class;
- `H_f^0` is the compatible-lift translation space;
- `Lambda_f:H_f^0 -> C^1(G)` is defined by
  \[
  k_u+k_v=\Lambda_f(k)_e f(e);
  \]
- `B_f=im Lambda_f` is the accessible partial-Petrial code;
- `Omega_f` is the base-independent fixed-fibre class
  \[
  \Omega_f=[w(g)]_f
  \in C^1(G)/(Cut(G)+B_f).
  \]

## 2. Theorem spine

### OR1-A — retained-data surface reconstruction

The checked Lean dart layer retains enough information to reconstruct the exact indexed cycle-face embedding:

\[
(M_a,\operatorname{partner}_a,\sigma,\rho_a)
\longmapsto
S_g.
\]

The graph-level theorem `Port.cubic_flow_cdc` is not this reconstruction: it discards `rho` and replaces the retained face circuits by a generic undirected decomposition.

### OR1-B — fixed-lift orientation theorem

For one fixed lift `g`, the following are equivalent:

\[
\begin{array}{c}
S_g\text{ orientable}\\
\Updownarrow\\
w(g)\in Cut(G)\\
\Updownarrow\\
\omega(g)=0\\
\Updownarrow\\
\langle w(g),z\rangle=0\quad(z\in Z_1(G))\\
\Updownarrow\\
\text{the retained face occurrences form an oriented CDC.}
\end{array}
\]

This equivalence is specific to the cubic cycle-face surface whose vertex links are circles. Independently orienting arbitrary circuits of an undirected CDC is weaker.

### OR1-C — exact gauge law

For transported local orientations,

\[
\boxed{
w(g^k)=w(g)+\Lambda_f(k).
}
\]

Without fixing representatives,

\[
\boxed{
\omega(g^k)=\omega(g)+[\Lambda_f(k)]
\quad\text{in }C^1/Cut.
}
\]

This is derived from the integrated partial-Petrial theorem: one gauge bit exchanges the two face sides of one edge band and therefore toggles exactly one twist bit.

### OR1-D — fixed-fibre classification

The orientable labelled lifts are

\[
\mathcal O_g
=
\{k:\Lambda_{or}(k)=\omega(g)\},
\qquad
\Lambda_{or}=q\circ\Lambda_f.
\]

Hence

\[
\boxed{
\mathcal O_g=\varnothing
\quad\text{or}\quad
k_0+\ker\Lambda_{or}.
}
\]

Existence is equivalent to

\[
\boxed{
w(g)\in Cut(G)+B_f}
\]

or, base-independently,

\[
\boxed{\Omega_f=0.}
\]

Unlabelled orientable Petrial words form either the empty set or

\[
\lambda_0+(B_f\cap Cut(G)).
\]

### OR1-E — dual criterion

Define

\[
Stress_{or}(f)
:=Z_1(G)\cap B_f^\perp.
\]

Then

\[
\boxed{
\Omega_f=0
\iff
\langle w(g),z\rangle=0
\text{ for every }z\in Stress_{or}(f).
}
\]

Using the integrated code identity,

\[
Stress_{or}(f)
=
\mathcal C(G)
\cap
(\mathcal C(G)*\mathcal F_f).
\]

This orientation stress is not the Programme-A affine compatibility stress. Compatibility vanishing supplies a nonempty root-lift fibre; orientation stress decides whether that fibre meets the orientable locus.

### OR1-F — `K_4` nonautomaticity theorem

For the standard `K_4` Tait flow on the affine plane `W`:

- `g_0(uv)=W-{0,u+v}` has three four-cycle faces and `chi=1`, hence is nonorientable;
- the field `k_u=u` has `Lambda_f(k)=1_E`;
- `g_1(uv)=W-{u,v}` has four triangular faces and is the tetrahedral sphere.

Thus one fixed fibre contains both surface types. Per-lift automatic orientability is false, while the fixed-fibre obstruction of this example vanishes.

### OR1-G — collapse/decomposition boundary

The existing Programme-A support-only route does not preserve an orientation witness, because it forgets directed face occurrences before collapse and uses an arbitrary undirected decomposition afterward.

An enriched theorem does hold:

1. project each oriented face circuit through the collapse datum;
2. delete auxiliary edges;
3. obtain an empty word or a directed closed trail downstairs;
4. decompose the directed trail into directed circuits without reversing edges;
5. preserve the two opposite occurrences of every original edge.

Therefore an orientable affine lift on the cubic expansion yields an oriented CDC of the collapsed loopless graph. Deleted loops may then be reinserted as two oppositely directed singleton-loop occurrences under the stated dart convention.

## 3. Exact implication diagram

\[
\begin{array}{c}
\text{fixed Fano flow }f\\
\downarrow\quad\text{Programme-A compatibility}\\
\text{nonempty lift torsor }g+H_f^0\\
\downarrow\quad\text{OR1 fibre obstruction}\\
\Omega_f\in C^1/(Cut+B_f)\\
\begin{cases}
\Omega_f=0 &\Rightarrow \text{orientable lift / oriented face CDC},\\
\Omega_f\neq0 &\Rightarrow \text{orientation-stress certificate}.
\end{cases}
\end{array}
\]

If `Omega_f=0` on a cubic expansion, the enriched collapse theorem passes the oriented CDC to the original graph.

## 4. Classification table

| Claim | State after OR1 | Assurance |
|---|---|---|
| dart/support data reconstruct `S_g` | proved | authorial proof + checked Lean ingredients |
| `omega(g) in C^1/Cut` is the fixed-lift obstruction | proved | authorial signed-rotation proof |
| `w(g^k)=w(g)+Lambda_f(k)` | proved | authorial consequence of integrated B4 Petrial theorem |
| orientable lifts are empty or a kernel torsor | proved | exact finite linear algebra |
| fixed-fibre obstruction is `Omega_f in C^1/(Cut+B_f)` | proved | base-independent quotient theorem |
| dual orientation-stress criterion | proved | exact annihilator duality |
| every compatible lift is orientable | false | explicit `K_4` counterexample |
| every fixed Fano-flow fibre has an orientable lift | open | no universal vanishing theorem |
| every bridgeless cubic graph has some orientable affine lift | open | graph/flow existential frontier |
| existing support-only collapse carries orientation | not established; witness data are discarded | architecture boundary |
| enriched oriented collapse carries an oriented CDC | proved | directed-trail projection and decomposition |
| OR1 is Lean-verified | no | Lean supplies reconstruction ingredients only |
| issue-#49 review is itself accepted mathematics | no | triggering audit only |

## 5. New exact proof obligations

OR1 closes the structural orientation-obstruction theory but exposes two genuine existence questions.

### `AC-RL-OR-FIXED-FIBRE-VANISHING`

Determine whether

\[
\Omega_f=0
\]

for every nowhere-zero `F_2^3`-flow on every finite bridgeless cubic multigraph, or construct an exact fixed-fibre counterexample.

### `AC-RL-OR-GRAPH-EXISTENCE`

If fixed-fibre vanishing fails, determine whether every finite bridgeless cubic multigraph admits **some** Fano flow `f` with `Omega_f=0`.

These are new-mathematics obligations. They must not be recorded as consequences of OR1.

## 6. Relation to existing Programme A/B DAG

- Programme A compatibility and ordinary CDC truth are unchanged.
- B1--B8 and the six existing five-support frontier obligations are unchanged.
- OR1 is orthogonal to the five-support target: it refines the eight-support cycle-face output by an orientation class.
- The enriched collapse lemma is reusable in any future oriented Programme-A projection, but it does not alter the current ordinary-CDC theorem.
- No manuscript, Lean, candidate, Curator, audit, Research Lead, release, publication, arXiv, DOI, tag, or default-branch surface is changed by this proof unit.

## 7. Completion assessment

`AC-PD-OR1` is

`READY-FOR-CURATOR / FIXED-FIBRE CLASSIFICATION COMPLETE / COUNTEREXAMPLE TO PER-LIFT AUTOMATICITY / GLOBAL ORIENTED EXISTENCE OPEN`.
