# AffineCDC current mathematical state

This file gives the compact current-best picture. Proofs live in the active chapters; historical discovery packets remain recoverable from Git.

## 1. Complete Cycle Double Cover line

At paper level the project has a complete existence spine

$$
\text{finite-active-edge bridgeless multigraph}
\longrightarrow
\text{cycle double cover}.
$$

The proof passes through loop removal, a cubic binary-flow outer shell, rank-three affine compatibility, graph-level even-cover extraction, cut-even collapse transport, and one final circuit decomposition. The natural theorem allows loops and finite active edge set. The present Lean checkpoint is earlier, loopless, and ambient-finite.

## 2. Five-support object

The open strengthening asks for five indexed even supports. It is equivalent to a root-valued flow

$$
E(G)\longrightarrow R_5\subset E_5,
$$

or to a `K_5` triangle labelling, matching/four-flow structure, quadratic-cycle solution, or cographic map.

Above any cubic Fano flow a compatible eight-support lift exists. The complete fixed-lift target is

$$
T_g^{(1)}\longrightarrow\mathscr A_5,
$$

not merely the factorable quotient route through `J_g`.

## 3. Durable closed blocks

The active backbone includes:

- fixed-plane parity and its singular, Schur, stress/Fourier, and colour-cut forms;
- root-lift/surface/dual and componentwise half-cube theory;
- gauge/Petrial occurrence loci and horizontal switch laws;
- three-cut gluing and the ten-state four-edge interface;
- Type T/Type H routing reduction and Tait escape from the soluble Type H branch;
- BBD origin, `K_6` completion, defect forests, Petersen transport, DDD triality, unique bad route, and rank-two escape;
- full-rank curvature/common-cut duality and flat-potential equivalence;
- odd witness circuits and the singleton/transition/quartic trichotomy;
- unbounded abstract quartic designs and their symplectic form;
- quotient Tait-phase representation, affine sheet plane, Kempe differences, and aligned/crossed signatures;
- connected pairwise marked transition skeletons;
- the canonical `O^-(4,2)` terminal nucleus, intrinsic `E_5/K_5` geometry, route `D_8` stabiliser, curvature carrier, and exact split-or-peel recursion;
- bounded `K_6` defect geometry for split terminal distributions;
- canonical transport between successive nuclei and the fixed pairwise marked shell;
- finite elementary scalar-interval transfer, backtrack caps, periodic cells, and rigid Kempe ladders;
- the physical `g`-component transition quotient `\Gamma_g`;
- the canonical route-capped `4`-regular flag-line graph;
- the fourfold relative touch-homology formulation of curvature witnesses.

## 4. Controlling negative boundaries and corrections

The following are false or unsupported:

- every fixed Fano flow has a five-support lift;
- `J_g` is the complete fixed-lift object;
- route-lock forces a graph two-cut or automatic flatness;
- a scalar-common-cut witness is necessarily a cut in the original four-pole;
- repeated Petersen state alone gives a replaceable strip;
- finite census proves universal closure;
- quartic near-resolution and rank axioms bound `k`;
- consecutive witness edges on a scalar circuit are necessarily consecutive full `g`-edges.

The last correction is essential. A quartic block has four marked witness arcs, but each arc may pass through arbitrarily many edges of `E_g\setminus\eta`. The cap/cell/ladder theorems apply to elementary non-`g` paths between consecutive full `g`-incidences. Whole witness arcs are transition walks in `\Gamma_g`.

## 5. Sharp nonflat endpoint

At the locked full-rank nonflat endpoint, a support-minimal witness

$$
\eta\subseteq E_g
$$

is a curvature-odd circuit of the closed-component incidence matroid. Exactly one of:

1. `|\eta|=1`, an aligned or crossed enriched atom;
2. one closed scalar component meets `\eta` in two edges, giving a marked transition pair;
3. `|\eta|=4k+1`, giving a quartic near-resolution core.

For a quartic core:

- abstract incidence is unbounded for all `k`;
- the four whole-sheet sums span a canonical minus-type four-space;
- a split terminal distribution is a bounded equality/one-factor/root-triangle gadget;
- an all-concentrated design peels canonically from level `k` to `k-1`;
- successive nuclei and curvature carriers are canonically `D_8`-equivariantly identified.

## 6. Three coordinated physical carriers

### 6.1 Physical cut carrier

Delete the `g`-edges and contract each connected component. The result is an even-total-degree four-pole `\Gamma_g` whose edges are the `g`-edges and whose four scalar sheets give four transition systems.

Every internal quotient cut lifts exactly to a `g`-coloured cut in the original four-pole:

$$
\delta^{\mathrm{int}}_{\Gamma_g}(\mathcal U)
=
\delta^{\mathrm{int}}_Q(X_\mathcal U).
$$

Its parity is

$$
|\delta^{\mathrm{int}}(\mathcal U)|
\equiv t(\mathcal U)\pmod2,
$$

where `t(\mathcal U)` is the number of original terminal flags on that shore.

### 6.2 Standard `4`-regular carrier

Close terminals according to `12\mid34` and take the flag-line graph

$$
F=\mathcal L(\widehat Q).
$$

Every scalar even subgraph gives a canonical circuit partition of the same `4`-regular graph. The four sheets are four transition transversals, with exact local transition distributions determined by the edge colour and aligned/crossed endpoint type. Scalar component incidence is one-sided touch-graph incidence.

### 6.3 Relative touch carrier

In each scalar touch-graph, the common-cut witness is a relative `1`-cycle: its boundary vanishes at closed scalar-circuit vertices but may remain at terminal and complementary partition circuits.

The common kernel is

$$
\mathcal Z_{\mathrm{com}}
=
\bigcap_{\phi\in U^*}
Z_1(\Theta_\phi,B_\phi),
$$

and curvature is terminal relative-boundary evaluation

$$
\Omega(x)
=
\sum_{\phi}\beta_{\phi,34}(x).
$$

Therefore the pointed curvature circuit is not yet proved to be a circuit or cocircuit of the transition matroid. Direct appeal to isotropic connectivity is not yet justified.

## 7. Exact current frontier

The immediate theorem is a complementary-boundary closure/decomposition theorem:

$$
\boxed{
\text{fourfold relative curvature circuit}
\Longrightarrow
\begin{cases}
\text{bounded closure to an ordinary touch cycle / transverse dependence},\\
\text{terminal-even separator or transition two-sum in }\Gamma_g,\\
\text{physical }D_8\text{ class}.
\end{cases}}
$$

The terminal boundary is finite and already carried by the canonical nucleus. The uncontrolled part is boundary on complementary partition circuits.

The full-rank flat branch remains separate: its eight-state potential still needs a finite physical interface.

## 8. Source and assurance state

The active line uses the completed migration

`960c92b7ff231c78b387894149779083060a75eb`

and later Research Lead commits on `research/affine-cdc-five-cdc-v1`. The seventy-eight discovery-order packets are retired from the current tip but recoverable from ancestry.

Current-best inclusion does not add Lean verification, independent review, peer review, manuscript approval, release, DOI, arXiv, or publication status.

Reading entrypoints:

- [`ACTIVE_MATHEMATICAL_SURFACE.md`](ACTIVE_MATHEMATICAL_SURFACE.md);
- [`THEOREM_DEPENDENCY_MAP.md`](THEOREM_DEPENDENCY_MAP.md);
- [`five-support/README.md`](five-support/README.md);
- [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md);
- [`FORMAL_STATUS.md`](FORMAL_STATUS.md).
