# AffineCDC mathematical architecture

This file is the canonical dependency architecture for the reconstructed mathematical corpus. It distinguishes the complete Cycle Double Cover theorem line from the open five-support strengthening and places every secondary theory downstream of its natural object.

## 1. Project scopes

The project has three nested but logically distinct scopes.

1. **Affine compatibility core**  
   Given a finite cubic graph with a nowhere-zero binary flow, classify the local affine families and prove a globally compatible choice in rank three.

2. **Complete CDC shell**  
   Supply the cubic flow object from an arbitrary bridgeless finite-active-edge multigraph, transport the affine even cover through collapse, decompose once, and reinsert loops.

3. **Five-support strengthening**  
   Ask whether the compatible cover can be chosen with only five indexed supports, equivalently as a root-valued $E_5$ flow.

Scope 3 is open. It must not be used as a premise for Scope 2.

## 2. Affine compatibility centre

Let

$$
f:E(G)\to\Gamma\setminus\{0\}
$$

be a nowhere-zero binary flow on a finite cubic graph. For an edge $e$, put

$$
Q_e=\Gamma/\langle f(e)\rangle.
$$

The incidence space is

$$
E_f=\bigoplus_{(v,e)}Q_e.
$$

Local homogeneous vertex choices form $L_{\mathrm{vert}}$, edge matching forms $L_{\mathrm{edge}}$, and the distinguished local affine data give $\kappa\in E_f$.

The pair complex is

$$
\mathcal P_f:
L_{\mathrm{vert}}\oplus L_{\mathrm{edge}}
\longrightarrow E_f,
\qquad
(\ell,m)\mapsto\ell+m.
$$

Then

$$
H^0(\mathcal P_f)=L_{\mathrm{vert}}\cap L_{\mathrm{edge}},
$$

and

$$
H^1(\mathcal P_f)=E_f/(L_{\mathrm{vert}}+L_{\mathrm{edge}}).
$$

Compatibility is exactly

$$
[\kappa]=0\in H^1(\mathcal P_f),
$$

and the solution set is a torsor under $H^0(\mathcal P_f)$.

This is the complete centre of the compatibility question. The graph, dart, and local-family data remain necessary for extracting even supports.

## 3. Rank-three Fano compatibility

For $\Gamma\cong\mathbf F_2^3$, every edge quotient $Q_e$ is a binary plane with canonical anisotropic quadratic form

$$
q_e(x)=1_{x\ne0}.
$$

The global incidence space becomes quadratic symplectic. The vertex space and edge diagonal are Lagrangians; the edge diagonal is totally singular. The local affine family is the characteristic torsor of the vertex Lagrangian.

For Lagrangians $L,M$ in a quadratic symplectic space,

$$
\operatorname{Char}_q(L)\cap M\ne\varnothing
\iff
q|_{L\cap M}=0.
$$

Since the edge Lagrangian is totally singular, intersection is automatic.

Equivalent proof presentations are:

- quadratic-Lagrangian intersection;
- quadratic handshaking;
- cross-bit/support-boundary cancellation.

The invariant proof and the existing Lean branching proof are corresponding presentations; their exact bridge is not yet formalized.

## 4. Natural affine output

A compatible family produces indexed even edge supports with exact double coverage. Flattening the internal rank-three index gives a graph-level multiset even double cover.

The natural implication is

$$
\boxed{
\text{compatible affine family}
\Longrightarrow
\text{graph-level multiset even double cover}.
}
$$

Circuit minimality is not imposed at this stage.

## 5. Full CDC shell

For a bridgeless multigraph $G$ with finite active edge set:

1. delete loops to obtain the loopless core $G_0$;
2. supply a nowhere-zero binary flow using the isolated classical flow input;
3. build a cubic port-cycle expansion $H$ with collapse data;
4. apply rank-three affine compatibility on $H$;
5. convert the affine output to a graph-level even double cover of $H$;
6. pass from vertex-even to cut-even on $H$;
7. transport cut-even supports through collapse to $G_0$;
8. decompose each finite cut-even support into circuits once;
9. add two singleton circuit occurrences for every removed loop.

The preferred paper route chooses the binary flow first and uses adaptive ordering. The selected first Lean route expands first and isolates a `BinaryEightFlow` boundary. Neither route changes the assurance boundary.

## 6. Five-support object

Put

$$
E_5=\{x\in\mathbf F_2^5:\sum_i x_i=0\},
\qquad
R_5=\{e_i+e_j:i<j\}.
$$

An indexed five-support cover is equivalent to a nowhere-zero root-valued flow

$$
E(G)\to R_5.
$$

At a cubic vertex the three roots form a triangle of $K_5$.

Equivalent global formulations include:

- $K_5$ triangle labelling;
- cographic/cycle-continuous map;
- matching plus nowhere-zero $\mathbf F_2^2$ flow;
- quadratic cycle equation.

The universal rank-three theorem always gives an eight-support root lift in the plus-type orthogonal model. The five-support problem is orthogonal confinement to the minus-type four-dimensional root model.

## 7. Fixed projection and lifting obstruction

Fix a Fano flow $f$ and a plane $W\le\Gamma$. Let $G_W$ be the subgraph of $W$-valued edges. Every component $K$ has one common outside-colour boundary parity $\chi_W(K)$.

A five-coordinate lift in this slice exists exactly when

$$
\chi_W(K)=0
$$

for every component.

Equivalent forms are:

- singular quotient holonomy;
- Eulerian outside-colour classes after contraction;
- vanishing of $\partial(x*y)$;
- trivial pairing with every relative stress.

This criterion is complete after $f$ and $W$ are fixed, not at the graph level.

## 8. Cycle-face surface and full target object

A compatible root lift $g$ determines a properly face-coloured cycle-face embedding $S_g$. Its dual $T_g$ is a closed triangular cellulation.

The complete fixed-lift criterion is

$$
\boxed{
T_g^{(1)}\to\mathscr A_5.
}
$$

The used old-colour graph $J_g$ is only a quotient:

$$
T_g^{(1)}\to J_g.
$$

Thus $J_g\to\mathscr A_5$ classifies global-index-factorable compression. The exact $K_6/K_8-C_5$ theorem remains valid only in this scope.

Target obstruction is organized by:

- dominating-clique links;
- common-neighbour chromatic cores;
- marked finite dual certificates;
- projective and exposed-cycle geometry of visible $K_6$ cores.

## 9. Vertical gauge geometry

For fixed $f$, compatible lifts form a torsor under $H_f^0$; modulo global translations this is the reduced gauge code $B_f$.

A gauge word is simultaneously:

- a homogeneous affine difference;
- a piecewise root translation;
- a code-filtered partial Petrial of the cycle-face surface.

Every fixed marked obstruction core has occurrence locus

$$
\beta+(B_f\cap\mathbf F_2^R),
$$

where $R$ is the reserve outside its face zone. A finite certificate library therefore yields an affine-subspace arrangement in $B_f$.

Renewal cubes are exact finite examples of arrangement coverage; they are not universal fibre structure.

## 10. Horizontal Fano-flow geometry

All $\Gamma$-valued flows form

$$
Z_1(G)\otimes\Gamma.
$$

Nowhere-zero flows are an arrangement complement. A connected-cycle switch is a rank-one tensor move and one reconfiguration edge. Disconnected cycle switches are compositions.

Relative to a fixed plane $W$:

- internal switch directions $t\in W$ give a linear correction map on the fixed quotient;
- external directions $t\notin W$ reslice the quotient while preserving lower-rank flow data.

The graph-level five-support question depends on the decorated two-level system consisting of horizontal flow states and their vertical obstruction arrangements.

## 11. Source interfaces

Three-edge cuts are completely reducible: five-support covers glue after matching the unique local pair-support law.

Four-edge cuts have the ten-state alphabet

$$
\{A,B_i,C_i,D_i:i=0,1,2\}.
$$

Gluing is exact profile intersection. Minimality gives cap forcing; Kempe path pairing gives closure. Routing-weight coordinates identify the three matching directions of $AG(2,2)$.

Uniform routing is eliminated. The four abstract residual kernels reduce to:

- Type T: $P_5\mid P_5$ unique linkage;
- Type H: $P_4\mid C_3$ rainbow holonomy.

## 12. Interior holonomy and Tait resolution

A lifted Type H loop has affine datum

$$
(\pi,z)\in(Z_1(P)\otimes E_5)\rtimes S_5.
$$

The cyclic norm $N_\pi z$ is the ambient obstruction. When it vanishes, root-admissible linearization is a finite root-fibre section problem.

The genuine three-switch word reduces the problem to a low-rank switch flow. Root lifting is equivalent to a Tait resolution. In a minimal Type H kernel, every Tait resolution forces boundary-profile escape.

For the BBD family, root rigidity kills the full translation kernel, $H^1(S_5,E_5)=0$, and one canonical $E_5$ flow controls all loops.

## 13. Defects and atoms

The canonical or energy-minimal $E_5$ flow has zero and co-root defects.

- the complete defect support is an induced forest;
- co-root paths carry an $L(\mathrm{Petersen})$ transducer with side-root output;
- one-factor endpoints are the fifteen Petersen-edge states;
- the smallest co-root component is a DDD atom with one co-root and two root resolutions.

If both crossed atom resolutions are blocked, unique-bad-route reduction gives a locked $K_{2,4}$ orbit and a quotient $\mathbf F_2^3$ flow with equal terminal colour.

Rank two escapes through a Tait root lift. In full rank:

- $\Omega\ne0$ gives a common-cut dual witness with odd terminal parity;
- $\Omega=0$ gives an eight-state affine potential.

The DDD subgroup retains one exceptional class in $H^1(D_8,E_5)$.

## 14. Current frontier

The missing theorem is a strict localization/composition result. It must convert one of:

- Type T unique linkage;
- Type H ambient or root-fibre obstruction;
- zero network;
- co-root strip;
- nonflat common-cut witness;
- flat potential partition;
- exceptional DDD class;

into one of:

- profile expansion or orbit escape;
- smaller cyclic separator;
- serial or bounded four-pole replacement;
- transition-matroid split;
- gluing of smaller instances.

The sharpest current target is support-minimal common-cut localization together with a finite interface for the flat potential branch.

## 15. Secondary theories

The following are downstream projections and do not replace the main architecture:

- tensor/code-flag homology;
- gauge circuits and harmonic quotients;
- rank-four residue hierarchy;
- orientation transgression and five-flow extraction;
- planar Fano-line flattening;
- embedding/Petrial theories whose older sources may be incomplete.

## 16. Canonical reading map

- complete CDC spine: `core/` and `reduction/`;
- five-support corpus: [`five-support/README.md`](five-support/README.md);
- dependency graph: [`THEOREM_DEPENDENCY_MAP.md`](THEOREM_DEPENDENCY_MAP.md);
- open boundary: [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md);
- assurance: [`FORMAL_STATUS.md`](FORMAL_STATUS.md).

No structural placement in this architecture upgrades formal, independent-review, peer-review, publication, release, or DOI status.