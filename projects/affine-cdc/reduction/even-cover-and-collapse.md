# Even covers, cut parity, and collapse transport

This chapter isolates the graph-theoretic output of the affine compatibility
construction and the invariant naturally preserved by graph collapse.  It is a
mathematical chapter, not a Lean implementation plan.  The public formal
statement in the companion repository is unchanged.

The purpose of the chapter is to prevent three distinct layers from being
conflated:

1. the affine construction of a family of even edge supports;
2. transport of those supports through a graph expansion or collapse;
3. final decomposition of finite even supports into circuits.

The first layer belongs to the AffineCDC core, the second to the outer
unconditional reduction, and the third is general finite graph theory.

## 1. Even supports and even double covers

Let $G$ be a multigraph and let $F\subseteq E(G)$ be an edge support.  In the
loopless convention used by the companion formalization, $F$ is **vertex-even**
when every vertex is incident with an even number of edges of $F$.

An **even double cover** of $G$ is a finite multiset

$$
\mathcal F=[F_1,\dots,F_m]
$$

of edge supports such that:

1. every $F_i$ lies in $E(G)$;
2. every $F_i$ is vertex-even;
3. every edge of $G$ occurs in exactly two members of $\mathcal F$, counted with
   multiset multiplicity.

Empty supports and repeated supports are allowed.  They are mathematically
natural before circuit decomposition:

- an empty support contributes no edge coverage;
- two equal supports occurring twice are two different cover occurrences;
- projection through a graph gadget may turn a nonempty support into the empty
  support.

For finite graphs, the existence of an even double cover is equivalent to the
existence of a cycle double cover.  The witness notions are not identical:
cycle members are required to be support-minimal nonempty even sets, whereas an
even support may contain several circuits.  The existence equivalence follows by
decomposing each finite even support into circuits and concatenating the
resulting multisets.

Thus the even double cover is not a stronger existence theorem than CDC.  Its
importance is structural: it is the natural output of the affine construction
and the natural input to graph surgery.

## 2. Output of a compatible affine family

Let $(G,\Gamma,f)$ be a finite cubic graph with a nowhere-zero binary
rank-three flow, together with a globally compatible affine family supplied by
the rank-three Fano theorem.

The retained graph-and-dart data canonically produce a $\Gamma$-indexed family
of edge supports

$$
(F_s)_{s\in\Gamma}
$$

with the following properties:

1. each $F_s$ is an edge subset of $G$;
2. each $F_s$ is vertex-even;
3. every edge belongs to exactly two of the supports $F_s$.

Flattening the finite index set $\Gamma$ gives an unlabelled multiset even
double cover.  The $\Gamma$-labels, dart pairing, partner data, and rotation data
remain useful internal structure, but they are not required by the outer graph
reduction.

The natural graph-level conclusion of the affine core is therefore

$$
\boxed{
\text{compatible affine family}
\Longrightarrow
\text{even double cover}.
}
$$

Applying circuit decomposition immediately also gives a cycle double cover of
the cubic graph.  That statement is a correct corollary, but it is not a
necessary node in the unconditional proof: decomposition is more naturally
performed once, after all graph surgery has finished.

## 3. Cut-even supports

For a finite edge support $F\subseteq E(G)$, define **cut-evenness** by

$$
\operatorname{CutEven}_G(F)
\iff
\forall S\subseteq V(G),
\quad |F\cap\delta_G(S)|\equiv0\pmod2,
$$

where $\delta_G(S)$ is the set of edges with one end in $S$ and one end outside
$S$.

Cut-evenness is the intrinsic transport invariant for graph collapse.  It does
not mention cubicity, flows, darts, affine families, or circuit minimality.

### Loopless bridge

For a finite support in a loopless multigraph,

$$
\boxed{
F\text{ is vertex-even}
\iff
F\text{ is cut-even}.
}
$$

The forward direction is the usual parity sum over the vertices of $S$:
selected edges internal to $S$ are counted twice and selected crossing edges
once.  The reverse direction applies cut parity to the singleton cut
$S=\{v\}$, which equals the incidence set of $v$ in a loopless graph.

The loopless condition belongs precisely to this bridge under the current
incidence convention.  It is not an affine/Fano hypothesis and it is not needed
for pure cut transport.

If loops are counted only once in a vertex incidence set, vertex-evenness need
not imply cut-evenness.  For example, take two vertices joined by one ordinary
edge and place one loop at each vertex.  The support consisting of all three
edges is vertex-even under the once-per-edge incidence count, but the cut
separating the two vertices contains exactly one selected edge.

## 4. Collapse data

Let $H$ be an expanded graph and $G$ the graph obtained by collapsing vertex
clusters.  The transport theorem needs only the following graph-theoretic data.

1. A vertex map

   $$
   \pi:V(H)\longrightarrow V(G),
   $$

   whose fibres are the collapse clusters.  Surjectivity is unnecessary:
   isolated vertices of $G$ may have empty fibres.

2. An injective edge lift

   $$
   \lambda:E(G)\hookrightarrow E(H)
   $$

   preserving endpoints under $\pi$.

3. Every edge of $H$ joining two different $\pi$-fibres is a lifted original
   edge, and every auxiliary edge has both ends in one fibre.

These conditions imply, for every vertex subset $S\subseteq V(G)$,

$$
e\in\delta_G(S)
\iff
\lambda(e)\in\delta_H(\pi^{-1}S).
$$

No cubic, bridgeless, flow, affine, or global ambient-finiteness hypothesis is
part of this transport datum.

For an edge support $F'\subseteq E(H)$, define its projection by

$$
\operatorname{proj}(F')
:=
\{e\in E(G):\lambda(e)\in F'\}.
$$

If $F'$ is finite, then $\operatorname{proj}(F')$ is finite.

## 5. Pure cut-parity transport

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

Their cardinalities are equal, so their parities agree.

This proof does not sum over a cluster and does not require finite vertex
clusters.  The only finiteness needed is finiteness of the transported support,
so that ordinary parity of its cut intersections is defined.

Extending projection memberwise to a multiset preserves exact double coverage:
for every original edge $e$ and every support occurrence $F'$, one has

$$
e\in\operatorname{proj}(F')
\iff
\lambda(e)\in F'.
$$

Thus a cut-even double cover of $H$ projects to a cut-even double cover of $G$.
The support projection itself need not be injective; distinct upstairs support
occurrences may have the same downstairs image, and multiset multiplicity keeps
them distinct.

## 6. The unconditional route

The clean graph-theoretic spine is therefore

$$
\begin{array}{c}
\text{finite loopless bridgeless multigraph }G\\
\downarrow\\
\text{cubic expansion }H\text{ with a rank-three binary flow}\\
\downarrow\\
\text{rank-three affine compatibility on }H\\
\downarrow\\
\text{vertex-even double cover of }H\\
\downarrow\quad\text{loopless bridge}\\
\text{cut-even double cover of }H\\
\downarrow\quad\text{pure collapse transport}\\
\text{cut-even double cover of }G\\
\downarrow\quad\text{loopless bridge}\\
\text{vertex-even double cover of }G\\
\downarrow\quad\text{finite circuit decomposition}\\
\text{cycle double cover of }G.
\end{array}
$$

The outer reduction must independently supply the expansion, the relevant flow,
and the collapse datum.  Those results are outside the affine compatibility
kernel but inside the complete unconditional CDC proof.

## 7. Finiteness layers

Several different finiteness conditions must not be conflated.

- The public CDC problem concerns a finite active graph.
- The affine global compatibility theorem uses finite dart and vertex indexing
  in the finite-graph application.
- The even-cover predicate itself need not bundle an ambient-carrier finiteness
  condition.
- Circuit decomposition needs each support to be finite; it does not
  mathematically require the entire ambient edge type to be finite.
- Cut transport needs finite transported supports, not finite ambient vertex
  carriers or finite collapse fibres.

A formal implementation may retain stronger finite-type corollaries for
convenience, but the mathematical architecture is controlled by the active and
support-level hypotheses above.

## 8. Relation to the companion formalization

The companion Lean repository currently machine-checks:

- the local affine-family classification;
- the rank-three compatibility conclusion through the branching/cross-bit
  presentation;
- the dart-level support construction;
- cycle-double-cover extraction for an already cubic graph carrying the
  required flow.

It does not yet machine-check the factorization through a named graph-level even
double cover, the cut-even collapse transport, the full outer reduction, or the
final unconditional theorem inhabiting the public `CDCStatement`.

No public statement is changed by this chapter.  It records the internal
mathematical factorization that future paper and Lean work should follow.