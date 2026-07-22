# AC-PD-OR1.3 — the `K_4` counterexample and orientation through the outer shell

**Proof-development state:** `COMPLETE-DRAFT / COUNTEREXAMPLE / TRANSPORT-BOUNDARY`  
**Depends on:** OR1.1 and OR1.2; Programme-A collapse datum and circuit decomposition  
**Scope:** exact `K_4` fixed-fibre example; enriched oriented collapse; loop reinsertion convention

## 0. Purpose

This unit performs two logically separate tasks.

1. It independently checks the issue-#49 `K_4` example and determines exactly what it refutes.
2. It determines whether oriented structure survives the Programme-A expansion/collapse/decomposition shell.

The second question has two answers depending on what data are retained:

- the current support-only outer shell discards orientation and therefore proves no oriented conclusion;
- an enriched shell retaining directed face occurrences does transport an oriented CDC through collapse and final directed decomposition.

## 1. The standard `K_4` Fano flow

Let

\[
W=\{0,x,y,z\}\leq\Gamma=\mathbf F_2^3,
\qquad z=x+y,
\]

and take the vertex set of `K_4` to be `W`. Define

\[
f(uv):=u+v.
\]

Every edge receives a nonzero value. At a vertex `u`, the three incident edge values are the three nonzero elements `x,y,z` of `W`, whose sum is zero. Hence `f` is a nowhere-zero Fano flow.

## 2. A nonorientable compatible lift

Define

\[
g_0(uv):=W\setminus\{0,f(uv)\}.
\]

This is a two-element root. Its two elements sum to `f(uv)`, because the three nonzero elements of `W` sum to zero.

At every source vertex, as the incident directions run through `x,y,z`, the three roots are

\[
\{y,z\},\qquad \{z,x\},\qquad \{x,y\},
\]

which form the triangle on the three indices `x,y,z`. Therefore `g_0` is a compatible affine/root lift.

For `a in {x,y,z}`, an edge belongs to `F_a` exactly when its Fano direction is not `a`. The `a`-direction edges form one perfect matching of `K_4`; its complement is one Hamiltonian four-cycle. Thus:

- `F_x,F_y,F_z` are three connected four-cycles;
- `F_0` and every support indexed outside `W` are empty.

The cycle-face surface has

\[
|V|=4,
\qquad |E|=6,
\qquad |F|=3,
\]

so

\[
\chi(S_{g_0})=4-6+3=1.
\]

The surface is closed and connected. Every closed orientable surface has even Euler characteristic `2-2h`, so `S_{g_0}` is nonorientable. By the classification of closed surfaces it is the projective plane, but only nonorientability is needed.

### Theorem 2.1

Affine/Fano compatibility and exact indexed double coverage do not force one prescribed compatible lift to be orientable.

## 3. An orientable lift in the same fibre

Define a vertex field

\[
k_u:=u.
\]

For every edge `uv`,

\[
k_u+k_v=u+v=f(uv),
\]

so `k in H_f^0` and

\[
\Lambda_f(k)=\mathbf1_E.
\]

Translate `g_0` by `k`. Since translation by `u` sends

\[
W\setminus\{0,u+v\}
\]

to

\[
W\setminus\{u,v\},
\]

one obtains

\[
g_1(uv)=W\setminus\{u,v\}.
\]

For `a in W`, the support `F_a` consists exactly of the three edges whose endpoints lie in `W-{a}`. Hence every `F_a` is the triangle on the other three vertices. There are four triangular face occurrences, and

\[
\chi(S_{g_1})=4-6+4=2.
\]

This is the tetrahedral sphere, so `S_{g_1}` is orientable.

The all-edge word is not a binary cut of `K_4`: its pairing with any triangle is

\[
3\equiv1\pmod2,
\]

whereas every cut pairs trivially with every cycle. The OR1.2 gauge law therefore gives

\[
\omega(g_0)=[\mathbf1_E]\neq0,
\qquad
\omega(g_1)=0.
\]

### Theorem 3.1 — exact `K_4` conclusion

The same fixed Fano-flow fibre contains both a nonorientable and an orientable compatible lift.

Consequently:

1. **per-lift automatic orientability is false**;
2. the gauge action genuinely changes the orientation class;
3. this example is **not** a counterexample to fixed-fibre orientable-lift existence, since its fixed-fibre class `Omega_f` vanishes.

The example is an explicit theorem, not a finite-census inference.

## 4. What the present Programme-A outer shell retains

The integrated outer-shell route deliberately retains only:

1. indexed even edge supports on the cubic expansion `H`;
2. cut parity of their projections to the original loopless core `G_0`;
3. exact multiset double-coverage multiplicity;
4. an undirected circuit decomposition performed after collapse.

It explicitly declares that the labels, dart pairings, partner maps, and rotations are not needed by that route. The checked Lean `Port.cubic_flow_cdc` likewise discards `rho` and calls a generic undirected support decomposition.

### Proposition 4.1 — support-only boundary

The present Programme-A collapse/decomposition theorem does not, by itself, transport an oriented CDC or an orientation class.

### Reason

A projected cut-even support remembers which edge objects occur but forgets:

- the directed cyclic order of each face occurrence;
- which of the two occurrences of an edge traverses which direction;
- the pairing of projected segments through one collapsed vertex cluster.

An arbitrary later undirected circuit decomposition can choose circuits unrelated to the original face boundaries. Therefore no orientation conclusion follows from the existing support-only witness.

This is a data-loss boundary, not a counterexample to oriented collapse.

## 5. Enriched oriented collapse datum

Let `H` be a finite loopless expanded graph and `G_0` its loopless collapsed graph. Assume the Programme-A collapse datum:

- a vertex map `pi:V(H)->V(G_0)`;
- an injective edge lift `lambda:E(G_0)->E(H)` preserving endpoints;
- every non-lifted auxiliary edge of `H` lies within one `pi`-fibre;
- every edge joining distinct fibres is one lifted original edge.

Suppose now that `H` carries an **oriented circuit double cover** `D`: a finite multiset of directed circuit occurrences in which each edge of `H` occurs once in each direction.

For one directed circuit occurrence `C` of `H`, delete all auxiliary edges from its cyclic dart sequence and replace every remaining lifted edge `lambda(e)` by `e`, with the induced direction between the corresponding collapse fibres.

### Lemma 5.1 — projected directed trail

The result is either empty or a finite directed closed trail in `G_0` with no repeated edge object.

### Proof

Between two consecutive lifted edges in `C`, every intervening edge is auxiliary and therefore remains in one collapse fibre. Hence the terminal fibre of the first projected edge equals the initial fibre of the next. Closure follows from cyclicity of `C`. Injectivity of `lambda` and the circuit property upstairs prevent repeated projected edge objects. `square`

The trail may revisit a collapsed vertex, so it need not be one circuit.

## 6. Directed decomposition after collapse

### Lemma 6.1 — directed trail decomposition

Every finite nonempty directed closed trail in a multigraph decomposes into a finite multiset of directed circuits, using every directed edge occurrence exactly once and preserving its direction.

### Proof

If the trail has no repeated vertex except its endpoint, it is already a directed circuit. Otherwise split at a repeated vertex into two shorter nonempty directed closed trails and argue by induction on the number of edge occurrences. `square`

Apply this decomposition separately to every nonempty projected face circuit.

### Theorem 6.2 — oriented collapse transport

Under the enriched datum above, an oriented circuit double cover of `H` induces an oriented circuit double cover of `G_0`.

### Proof

Every original edge `e` has one lifted edge `lambda(e)`. Upstairs, `lambda(e)` occurs in exactly two directed circuit occurrences, once in each direction. Projection preserves these two opposite directions. Directed decomposition partitions projected trail occurrences but never reverses an edge. Therefore downstairs `e` still occurs exactly twice, once in each direction. Empty projections are discarded and repeated resulting circuits retain multiset multiplicity. `square`

### Corollary 6.3

If a compatible affine lift on the cubic expansion has orientable cycle-face surface, then the original loopless collapsed graph has an oriented CDC.

This corollary requires the retained oriented face occurrences from OR1.1. It does not follow from the existing support-only collapse file without the enriched theorem.

## 7. Loop deletion and oriented reinsertion

The complete Programme-A theorem deletes loops before the loopless cubic reduction. For the natural dart convention on a loop, the singleton loop circuit has two opposite traversal directions, corresponding to its two half-edge orientations.

After obtaining an oriented CDC of the loopless core, reinsert every deleted loop by adding two singleton loop-circuit occurrences, one in each direction. This preserves the once-each-direction rule and does not affect nonloop edges.

### Boundary

Any external oriented-CDC statement for multigraphs with loops must state this dart convention explicitly. The current Lean public statement is loopless and does not formalize this reinsertion.

## 8. Corrected unconditional orientation route

The orientation-aware logical spine is therefore:

\[
\begin{array}{c}
\text{loopless bridgeless core }G_0\\
\downarrow\\
\text{cubic expansion }H\text{ with a Fano flow}\\
\downarrow\\
\text{choose a compatible lift }g\text{ with }\Omega_f=0\\
\downarrow\\
\text{orient the retained face occurrences of }S_g\\
\downarrow\quad\text{enriched oriented collapse}\\
\text{directed closed trails on }G_0\\
\downarrow\quad\text{directed decomposition}\\
\text{oriented CDC of }G_0\\
\downarrow\quad\text{opposite singleton-loop reinsertion}\\
\text{oriented CDC of the original multigraph.}
\end{array}
\]

The unresolved theorem is not collapse transport. It is the existence of a suitable orientable compatible lift on the cubic expansion—either in a prescribed Fano-flow fibre or after choosing the flow.

## 9. Exact classification

| Statement | OR1 status |
|---|---|
| every compatible lift is orientable | false; refuted by `g_0` on `K_4` |
| one fixed fibre may contain both surface types | proved by `g_0,g_1` |
| every fixed Fano-flow fibre contains an orientable lift | open |
| every bridgeless cubic graph has some orientable affine lift | open |
| support-only collapse preserves orientation data | false as a witness claim; the data are discarded |
| enriched oriented collapse preserves an oriented CDC | proved |
| loop reinsertion preserves the oriented rule under the stated dart convention | proved |
