# Even covers, cut parity, and collapse transport

This chapter isolates the graph-theoretic output of the affine compatibility
construction and the invariant naturally preserved by graph collapse. It is a
mathematical chapter, not a Lean implementation plan. The public formal
statement in the companion repository is unchanged at the current checkpoint.

The purpose is to prevent four distinct layers from being conflated:

1. the affine construction of a family of even edge supports;
2. transport of those supports through graph expansion and collapse;
3. final decomposition of finite even supports into circuits;
4. deletion and reinsertion of loops around the loopless proof core.

The first layer belongs to the AffineCDC core, the second to the outer
unconditional reduction, the third is general finite graph theory, and the
fourth identifies the natural full multigraph theorem with its loopless core.

## 1. Cut-even supports and circuits

Let $G$ be a multigraph and let $F\subseteq E(G)$ be a finite edge support.
Define

$$
\operatorname{CutEven}_G(F)
\iff
\forall S\subseteq V(G),
\quad |F\cap\delta_G(S)|\equiv0\pmod2,
$$

where $\delta_G(S)$ is the set of edges with one end in $S$ and one end outside
$S$.

A **circuit** is a nonempty inclusion-minimal cut-even edge set contained in
$E(G)$. This is the natural cycle object for multigraphs with loops:

- a loop crosses no cut, so a singleton loop is a circuit;
- two parallel edges form a circuit;
- on a loopless graph, finite circuits agree with minimal nonempty vertex-even
  supports under the vertex-even/cut-even bridge below.

The natural finiteness condition for the full theorem is `E(G).Finite`. Finite
ambient vertex and edge types are a stronger representation convention used by
the current Lean checkpoint, not part of the mathematical theorem.

## 2. Vertex-even supports and even double covers

Under the loopless incidence convention used by the present companion
formalization, a support is **vertex-even** when every vertex is incident with an
even number of selected edge objects.

An **even double cover** of a loopless graph $G$ is a finite multiset

$$
\mathcal F=[F_1,\dots,F_m]
$$

of edge supports such that:

1. every $F_i$ lies in $E(G)$;
2. every $F_i$ is vertex-even;
3. every edge of $G$ occurs in exactly two members of $\mathcal F$, counted with
   multiset multiplicity.

For a general graph the intrinsic variant uses cut-even supports instead of the
current vertex-incidence convention.

Empty supports and repeated supports are allowed. They are natural before
circuit decomposition:

- an empty support contributes no edge coverage;
- equal supports occurring twice are two distinct cover occurrences;
- projection through a graph gadget may turn a nonempty support into the empty
  support.

For a graph with finite active edge set, every finite cut-even support decomposes
into circuits. Thus a cut-even double cover becomes a cycle double cover by
performing decomposition memberwise and concatenating the resulting multisets.
Conversely, forgetting minimality turns any cycle double cover into an even
double cover. These are equivalent existence statements in the finite setting,
but their witnesses serve different compositional roles.

## 3. Output of a compatible affine family

Let $(G,\Gamma,f)$ be a finite cubic graph, not necessarily connected, with a
nowhere-zero rank-three binary flow and a globally compatible affine family.
The retained graph-and-dart data canonically produce a $\Gamma$-indexed family
of edge supports

$$
(F_s)_{s\in\Gamma}
$$

such that:

1. each $F_s$ is an edge subset of $G$;
2. each $F_s$ is vertex-even in the present loopless graph representation;
3. every edge belongs to exactly two supports $F_s$.

Flattening the finite index set $\Gamma$ gives an unlabelled graph-level multiset
even double cover. The $\Gamma$-labels, dart pairing, partner data, and rotation
data remain useful internal structure, but the outer graph reduction does not
need them.

The natural graph-level conclusion of the affine core is therefore

$$
\boxed{
\text{compatible affine family}
\Longrightarrow
\text{graph-level multiset even double cover}.
}
$$

Immediate circuit decomposition gives a CDC of the cubic flow graph, but that is
only an optional corollary. The full proof performs circuit decomposition once,
after graph collapse.

## 4. The loopless vertex-even/cut-even bridge

For a finite support in a loopless multigraph,

$$
\boxed{
F\text{ is vertex-even}
\iff
F\text{ is cut-even}.
}
$$

The forward direction sums selected incidence counts over the vertices of $S$:
selected edges internal to $S$ are counted twice and selected crossing edges
once. The reverse direction applies cut parity to the singleton cut $S=\{v\}$,
which equals the incidence set at $v$ under looplessness.

Looplessness belongs precisely to these bridge statements under the current
once-per-edge incidence convention. It is not an affine/Fano hypothesis and it
is not needed for pure cut transport.

If loops are counted only once in a vertex incidence set, vertex-evenness need
not imply cut-evenness. For example, take two vertices joined by one ordinary
edge and place one loop at each vertex. The support consisting of all three
edges is vertex-even under the current incidence count, but the cut separating
the vertices contains exactly one selected edge.

## 5. Collapse data

Let $H$ be an expanded graph and $G$ the graph obtained by collapsing vertex
clusters. The transport theorem needs only:

1. a vertex map

   $$
   \pi:V(H)\longrightarrow V(G),
   $$

   whose fibres are the collapse clusters; surjectivity is unnecessary because
   isolated vertices of $G$ may have empty fibres;

2. an injective edge lift

   $$
   \lambda:E(G)\hookrightarrow E(H)
   $$

   preserving endpoints under $\pi$;

3. every edge of $H$ joining different $\pi$-fibres is a lifted original edge,
   and every auxiliary edge stays inside one fibre.

Then for every $S\subseteq V(G)$,

$$
e\in\delta_G(S)
\iff
\lambda(e)\in\delta_H(\pi^{-1}S).
$$

No loopless, cubic, bridgeless, flow, affine, connectedness, or global
ambient-finiteness hypothesis belongs to this pure transport datum.

For $F'\subseteq E(H)$ define

$$
\operatorname{proj}(F')
:=
\{e\in E(G):\lambda(e)\in F'\}.
$$

Finite supports project to finite supports.

## 6. Pure cut-parity transport

For every finite support $F'\subseteq E(H)$,

$$
\boxed{
\operatorname{CutEven}_H(F')
\Longrightarrow
\operatorname{CutEven}_G(\operatorname{proj}(F')).
}
$$

Indeed, for every $S\subseteq V(G)$, the edge lift identifies

$$
\operatorname{proj}(F')\cap\delta_G(S)
$$

with

$$
F'\cap\delta_H(\pi^{-1}S).
$$

Their cardinalities and parities agree. The proof does not sum over a cluster
and needs no finite-cluster hypothesis. It requires only finite transported
support.

Extending projection memberwise to a multiset preserves exact double coverage,
since

$$
e\in\operatorname{proj}(F')
\iff
\lambda(e)\in F'.
$$

Distinct upstairs support occurrences may have the same downstairs image;
multiset multiplicity keeps them distinct.

## 7. Loop deletion and reinsertion

Let $L$ be the set of loops of a graph $G$ with finite active edge set, and let
$G_0$ be obtained by deleting them.

- loops cross no cut;
- a loop is not a bridge;
- deleting loops preserves all cuts on nonloop edges and preserves
  bridgelessness;
- $G_0$ is loopless and still has finite active edge set.

After constructing a CDC of $G_0$, regard its circuits as circuits of $G$ and
add two occurrences of the singleton circuit $\{e\}$ for every $e\in L$. This
covers each loop exactly twice and leaves nonloop coverage unchanged.

Thus looplessness is a reduction condition for the current proof machinery, not
part of the natural external theorem.

## 8. The full unconditional route

The clean graph-theoretic spine is

$$
\begin{array}{c}
\text{bridgeless multigraph }G\text{ with }E(G)\text{ finite}\
\downarrow\quad\text{delete loops}\
\text{loopless bridgeless core }G_0\
\downarrow\
\text{cubic expansion }H\text{ with a rank-three binary flow}\
\downarrow\
\text{rank-three affine compatibility on }H\
\downarrow\
\text{graph-level vertex-even multiset double cover of }H\
\downarrow\quad\text{loopless bridge}\
\text{cut-even double cover of }H\
\downarrow\quad\text{pure collapse transport}\
\text{cut-even double cover of }G_0\
\downarrow\quad\text{one finite circuit decomposition}\
\text{cycle double cover of }G_0\
\downarrow\quad\text{two singleton circuits per removed loop}\
\text{cycle double cover of }G.
\end{array}
$$

The outer reduction must independently supply the expansion, the relevant flow,
and the collapse datum. These results are outside the affine compatibility
kernel but inside the complete unconditional CDC proof.

## 9. Finiteness layers

Several finiteness conditions must not be conflated.

- The public theorem requires finite active edge set.
- The affine global compatibility theorem uses finite dart and vertex indexing
  in its finite-graph application.
- The even-cover predicates need not bundle ambient-carrier finiteness.
- Circuit decomposition needs finite supports.
- Cut transport needs finite transported supports, not finite ambient vertex
  carriers or finite collapse fibres.

A formal implementation may retain stronger finite-type corollaries for
convenience, but the mathematical architecture is controlled by active-edge and
support-level hypotheses.

## 10. Relation to the companion formalization

The companion Lean repository currently machine-checks:

- the local affine-family classification;
- rank-three compatibility through the branching/cross-bit presentation;
- the dart-level indexed support construction;
- the cubic-flow CDC corollary for an already cubic loopless graph carrying the
  required flow.

It does not yet machine-check the approved graph-level even-cover factorization,
the cut-even collapse transport, loop deletion and reinsertion, the full outer
reduction, or the full finite bridgeless-multigraph theorem. The current
`Statement.lean` remains loopless and ambient-finite until the separate exact
Path A migration packet is implemented.
