# AffineCDC mathematical architecture

This file is the canonical dependency map for the mathematical project.
Definitions, proofs, examples, and limitations live in the linked chapters.
Engineering plans and implementation prompts do not control this file.

The project has two nested scopes:

1. the **affine compatibility core** attached to a cubic binary flow;
2. the **full finite bridgeless-multigraph CDC shell**, which separates loops,
   supplies a cubic flow object for the loopless core, transports the affine
   output back, decomposes once, and reinserts singleton loop circuits.

The first scope contains the principal new affine/Fano mathematics. The second
is necessary for the complete theorem and must be formalized independently in
the companion Lean project.

The natural external theorem is:

> Every multigraph with finite active edge set and no bridges has a cycle double
> cover.

Loops are allowed. A circuit is a nonempty inclusion-minimal cut-even edge set,
so a singleton loop is a circuit. The current companion `Statement.lean` is
still loopless and ambient-finite. It is an implementation checkpoint awaiting
the approved Path A migration; it is not the final natural statement and has
not yet been proved.

## 1. Source and compatibility image

The affine source is a finite cubic graph, not necessarily connected, with a
nowhere-zero binary flow

$$
(G,\Gamma,f).
$$

For every edge $e$, put

$$
Q_e:=\Gamma/\langle f(e)\rangle.
$$

The source determines:

- an incidence space $E_f$;
- a homogeneous vertex space $L_{\mathrm{vert}}$;
- a canonical affine translate $\kappa+L_{\mathrm{vert}}$ of local families;
- an edge-matching space $L_{\mathrm{edge}}$.

The compatibility problem is

$$
(\kappa+L_{\mathrm{vert}})\cap L_{\mathrm{edge}}\neq\varnothing.
$$

Equivalently, it is the pointed pair complex

$$
\mathcal P_f:
L_{\mathrm{vert}}\oplus L_{\mathrm{edge}}
\xrightarrow{+}
E_f,
\qquad
[\kappa]\in H^1(\mathcal P_f).
$$

Compatibility is $[\kappa]=0$; the solution set is then a torsor under
$H^0(\mathcal P_f)$.

The pair complex is the complete image of the **compatibility question**, but it
is not the full graph source. The graph, dart pairing, and local-family
interpretation are retained for the graph-level even-cover construction.

**Canonical chapter:**
[`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md).

## 2. Equivalent presentations of the compatibility core

The pair complex has two canonical presentations.

### Primal quotient presentation

Cancelling the contractible edge-diagonal summand gives

$$
\Gamma^V
\xrightarrow{\delta_f}
\bigoplus_eQ_e,
\qquad
(\delta_fm)_e=[m_u+m_v].
$$

The image of $\kappa$ is the quotient-sheaf cochain $c_f$. Thus

$$
[c_f]=0
\iff
[\kappa]=0.
$$

### Dual presentation

The dual obstruction space is the equilibrium-stress space:

$$
(H^1(\mathcal P_f))^*
\cong
L_{\mathrm{vert}}^\perp
\cap
L_{\mathrm{edge}}^\perp
=
\operatorname{Stress}(f).
$$

Hence

$$
[\kappa]=0
\iff
\psi(\kappa)=0
\text{ for every equilibrium stress }\psi.
$$

Quotient sheaf and stresses are the primal and dual presentations of the same
affine incidence pair, not competing foundations.

## 3. Rank-three Fano compatibility

When

$$
\Gamma=\mathbf F_2^3,
$$

every $Q_e$ is a binary plane with canonical quadratic form

$$
q_e(x)=\mathbf1_{x\neq0}.
$$

The direct-sum quadratic space has:

- $L_{\mathrm{vert}}$ Lagrangian;
- $\kappa+L_{\mathrm{vert}}$ equal to the characteristic torsor of
  $L_{\mathrm{vert}}$;
- $L_{\mathrm{edge}}$ totally singular Lagrangian.

For Lagrangians $L,M$ in a nondegenerate quadratic space,

$$
\operatorname{Char}_q(L)\cap M\neq\varnothing
\iff
q|_{L\cap M}=0.
$$

The condition is automatic when $M$ is totally singular. Therefore

$$
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
\cap
L_{\mathrm{edge}}
\neq\varnothing,
$$

and the rank-three affine obstruction vanishes.

The following are equivalent resolutions of the same proof:

$$
\text{Lagrangian intersection}
\Longleftrightarrow
\text{quadratic handshaking}
\Longleftrightarrow
\text{cross-bit/support-boundary cancellation}.
$$

The Lagrangian formulation is the canonical paper geometry. The existing
branching/cross-bit argument remains the machine-checked anchor until the
invariant bridge and proof are themselves formalized.

**Canonical chapter:**
[`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md).

## 4. Natural affine output

A compatible affine family does not intrinsically produce a minimal circuit
decomposition. It first produces a finite indexed family of even edge supports
in which every graph edge occurs exactly twice.

Flattening the internal $\Gamma$-index gives a graph-level multiset **even double
cover**. This is the natural output of the affine core:

$$
\boxed{
\text{compatible affine family}
\Longrightarrow
\text{graph-level multiset even double cover}.
}
$$

The even-cover witness is the correct compositional object because:

- it is what the affine construction already produces before decomposition;
- it does not expose $\Gamma$-labels, darts, partner, or rotation data to the
  outer reduction;
- it is transported naturally through graph collapse;
- it postpones circuit decomposition until the original loopless core is
  recovered.

A CDC of the already cubic flow graph is an optional immediate corollary, not a
necessary node in the full proof and not a separate mathematical centre.

**Canonical chapter:**
[`reduction/even-cover-and-collapse.md`](reduction/even-cover-and-collapse.md).

## 5. Cut parity and graph collapse

For a finite support $F\subseteq E(G)$, define

$$
\operatorname{CutEven}_G(F)
\iff
\forall S\subseteq V(G),
\quad |F\cap\delta_G(S)|\equiv0\pmod2.
$$

Cut-evenness is the invariant directly preserved by graph collapse. It is
independent of cubicity, flows, affine families, looplessness, connectedness,
and circuit minimality.

Under the current loopless incidence convention, a finite support is
vertex-even if and only if it is cut-even. Looplessness belongs to this bridge,
not to the affine compatibility theorem or the pure collapse theorem.

A collapse datum consists of vertex clusters and an injective lift of original
edges such that every auxiliary edge stays inside one cluster and the lifted
edges are exactly the inter-cluster edges. Projection of an upstairs support is
defined by retaining the original edges whose lifts lie in the support.

For every original vertex subset $S$, lifted cut edges identify

$$
\operatorname{proj}(F')\cap\delta_G(S)
$$

with

$$
F'\cap\delta_H(\pi^{-1}S).
$$

Hence finite cut-even supports, and therefore cut-even double covers, project
without any loopless, cubic, bridgeless, flow, affine, ambient-finiteness, or
finite-cluster assumption in the pure transport theorem.

This separates the outer shell into three clean pieces:

1. vertex-even to cut-even on the loopless expansion;
2. pure cut-even transport through collapse;
3. cut-even cover of the loopless original core, followed directly by intrinsic
   circuit decomposition.

**Canonical chapter:**
[`reduction/even-cover-and-collapse.md`](reduction/even-cover-and-collapse.md).

## 6. Loop separation and the full CDC spine

Let $G$ be a bridgeless multigraph with finite active edge set. Delete all loop
edges to obtain $G_0$.

- loops cross no cut and are not bridges;
- deletion preserves bridgelessness on the nonloop core;
- $G_0$ is loopless and has finite active edge set;
- a singleton loop is a cut-even circuit.

The complete chain is

$$
\boxed{
\begin{array}{c}
\text{bridgeless multigraph }G\text{ with }E(G)\text{ finite}\\
\downarrow\;\text{delete loops}\\
\text{loopless bridgeless core }G_0\\
\downarrow\\
\text{cubic expansion }H\text{ with rank-three binary flow}\\
\downarrow\\
(\mathcal P_f,\kappa)\\
\downarrow\\
\text{rank-three Fano compatibility}\\
\downarrow\\
\text{graph-level multiset even double cover of }H\\
\downarrow\\
\text{vertex-even/cut-even bridge on }H\\
\downarrow\\
\text{pure cut-even transport through collapse}\\
\downarrow\\
\text{even double cover of }G_0\\
\downarrow\\
\text{one final finite circuit decomposition}\\
\downarrow\\
\text{cycle double cover of }G_0\\
\downarrow\;\text{two singleton circuits per removed loop}\\
\text{cycle double cover of }G.
\end{array}
}
$$

This shell is part of the complete AffineCDC project even though its principal
new geometry lies in the affine rank-three core. The companion Lean repository
must prove its own version of the shell and may not discharge the final theorem
by importing an external CDC endpoint.

## 7. Finiteness and loop layers

The architecture distinguishes several logically different conditions.

### Looplessness

- It is not an affine/Fano hypothesis.
- The abstract dart structure permits two distinct paired darts at one vertex.
- The current Mathlib graph-to-dart port uses looplessness because its incidence
  pair does not distinguish the two half-incidences of a loop.
- The current Lean `Statement.lean` uses looplessness because the present
  vertex-incidence parity convention counts a loop edge once.
- The approved natural statement removes this representation restriction and
  uses cut-even circuits.
- Pure cut-even collapse transport does not require looplessness.

### Finiteness

- The natural public theorem requires `E(G).Finite`.
- The current Lean checkpoint uses finite ambient vertex and edge types.
- The finite-graph affine compatibility theorem uses finite global indexing.
- The even-cover notion itself need not bundle ambient-carrier finiteness.
- Circuit decomposition mathematically needs finite supports.
- Cut transport needs finite transported supports, not finite ambient vertex
  types or finite collapse fibres.

Implementation-level finite-type corollaries may be useful, but they do not
control the mathematical node.

## 8. Why rank three is exceptional

Three independent dimension and degree conditions coincide:

1. the support function on $Q_e$ has degree $r-1$, so it is quadratic exactly
   at $r=3$;
2. the local homogeneous image has dimension $r$ inside dimension $3(r-1)$ and
   is half-dimensional exactly when $2r=3(r-1)$;
3. the cubic quotient-sheaf index is

   $$
   \frac{3-r}{2}|V|,
   $$

   and vanishes exactly at $r=3$.

Rank three is therefore the unique balanced quadratic point of the hierarchy.

## 9. All-rank transgression and complete obstruction

For a plane $W\leq\Gamma$ and its three nonzero points,

$$
\sum_{h\in W\setminus\{0\}}
\nu_{\Gamma/\langle h\rangle}([x]_h)
=
\nu_{\Gamma/W}([x]_W).
$$

This lowers support degree by one in every rank. It gives a universal
outside-plane parity law, but for rank greater than three the scalar law forgets
directional information.

The missing information is recovered dually. A legal local stress triple has a
cross-bit $\beta$, support parity $\sigma$, and hidden-plane residue $\rho$ with

$$
\sigma=\beta+\rho.
$$

For every global equilibrium stress,

$$
\boxed{
\psi(\kappa)=\sum_v\rho_v(\psi_v).
}
$$

Hence compatibility holds exactly when every equilibrium stress has even
residue parity. This is the complete all-rank criterion.

- in rank three, $\operatorname{Ann}(W)$ is one-dimensional and contains no
  residue plane;
- in rank four, it is a plane and the first residue becomes possible;
- in higher rank, residues carry additional annihilator-plane decorations.

**Canonical chapter:**
[`rank-hierarchy/transgression-and-dual-fano-residue.md`](rank-hierarchy/transgression-and-dual-fano-residue.md).

## 10. Rank-four first failure

For $\Gamma=\mathbf F_2^4$, legal local stresses are alternating two-forms modulo
one quotient-form line. The residue is represented by

$$
\rho_W=(1+\beta_W)\operatorname{Pf}.
$$

It equals one precisely when the local flow plane is isotropic and the induced
cross-pairing with its quotient is perfect.

The two connected simple cubic graphs on six vertices give the minimal
comparison:

| graph | gauge code | essential-stress dimension | compatibility |
|---|---:|---:|---|
| triangular prism | $0$ | $1$ | compatible |
| $K_{3,3}$ | $0$ | $1$ | incompatible |

Here connectedness describes these two specific comparison graphs; it is not a
hypothesis of the affine compatibility source.

**Canonical chapter:**
[`rank-hierarchy/rank-four-first-obstruction.md`](rank-hierarchy/rank-four-first-obstruction.md).

## 11. Chain-level reduction to the tensor complex

Let

$$
Q_G:=\mathbf F_2^E/\mathcal C(G)^\perp
$$

and define

$$
T_f(\lambda)=\sum_e\lambda_ef(e)\otimes\bar e,
\qquad
W_f(a\otimes q)=a\wedge F_f(q).
$$

The tensor complex is

$$
\mathbf F_2^E
\xrightarrow{T_f}
\Gamma\otimes Q_G
\xrightarrow{W_f}
\Lambda^2\Gamma.
$$

It is related to the incidence geometry by a canonical zigzag

$$
\widehat{\mathscr Q}_f
\xleftarrow{\simeq}
\widehat{\mathcal R}_f
\twoheadrightarrow
\mathcal T_f.
$$

The exact comparison is

$$
0\to\Gamma\to H_f^0\to\ker T_f\to0,
$$

$$
H_f^1\cong\operatorname{coker}T_f,
$$

and

$$
0\to\mathcal K_f\to H_f^1\xrightarrow{\mu_f}\Lambda^2\Gamma\to0,
\qquad
\mathcal K_f=\ker W_f/\operatorname{im}T_f.
$$

The affine class lies canonically in $\mathcal K_f$. Thus the tensor complex
preserves compatibility but forgets constants, nonzero wedge moment, a preferred
vertex realization, and the dart-level cover data.

**Canonical chapter:**
[`reduction/incidence-to-tensor-complex.md`](reduction/incidence-to-tensor-complex.md).

## 12. Tensor, code, gauge, and interface branches

Dualizing a based quotient datum gives a nested code flag

$$
D\subseteq C\subseteq\mathbf F_2^E
$$

and a dual complex

$$
\Lambda^2D
\longrightarrow
D\otimes C
\xrightarrow{*}
\mathbf F_2^E.
$$

This downstream branch contains Schur multiplication, syzygies, constraint
matroids, divided-square and coefficient exact sequences, strict morphisms, and
balanced determinant-line torsion. Its recognition as an independent general
framework remains conditional on literature comparison and external payoff.

The homogeneous kernel has a direct graph interpretation through harmonic cut
quotients, gauge circuits, and interface gluing. These results are genuine
mathematics, but they emanate from the compatibility core and do not replace the
existence spine.

**Canonical chapters:**

- [`tensor/code-flag-complex.md`](tensor/code-flag-complex.md);
- [`tensor/exact-sequences-and-functoriality.md`](tensor/exact-sequences-and-functoriality.md);
- [`tensor/torsion-and-rigidity.md`](tensor/torsion-and-rigidity.md);
- [`gauge/gauge-modes-and-circuits.md`](gauge/gauge-modes-and-circuits.md);
- [`gauge/interface-gluing.md`](gauge/interface-gluing.md).

## 13. Trust and archive boundary

The companion Lean repository currently machine-checks the original local
classification, the compatibility conclusion through the branching/cross-bit
presentation, the indexed support construction, and the cubic-flow CDC
corollary for a graph already carrying the required flow.

It does **not** yet machine-check:

- the invariant characteristic-torsor identification and Lagrangian proof;
- the named graph-level even-cover factorization;
- cut-even collapse transport;
- loop deletion and singleton-loop reinsertion;
- the independent outer reduction;
- the current loopless `CDCStatement` or the approved full theorem.

The snapshot-only embedding, Petrial, transition, and surface sources are not
reconstructed. Their inventory and restoration protocol are in
[`topology/README.md`](topology/README.md).

See:

- [`FORMAL_STATUS.md`](FORMAL_STATUS.md) for reliability;
- [`MIGRATION_LEDGER.md`](MIGRATION_LEDGER.md) for the disposition of former
  active sources;
- [`PUBLICATION_PROGRAM.md`](PUBLICATION_PROGRAM.md) for paper boundaries.

## 14. Dependency graph

$$
\boxed{
\begin{array}{c}
\text{full finite bridgeless-multigraph CDC theorem}\\
\uparrow\\
\text{loop reinsertion after one final decomposition}\\
\uparrow\\
\text{outer expansion, flow, and cut-even collapse transport}\\
\uparrow\\
\text{graph-level multiset even double cover}\\
\uparrow\\
\text{compatible affine family}\\
\uparrow\\
\text{rank-three Fano intersection}\\
\uparrow\\
(\mathcal P_f,\kappa)\\
\uparrow\\
(G,\Gamma,f).
\end{array}
}
$$

The rank hierarchy branches from the affine obstruction. The tensor/code and
gauge/interface theories branch from reductions and homogeneous structures of
the same core. None of those branches replaces the unconditional existence
spine.
