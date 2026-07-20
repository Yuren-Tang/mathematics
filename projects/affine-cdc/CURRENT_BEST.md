# AffineCDC current mathematical state

This file gives the compact current-best picture. Proofs live in the active chapters; historical discovery packets remain recoverable from Git.

## 1. Complete Cycle Double Cover line

At paper level the project has a complete existence spine

$$
\text{finite-active-edge bridgeless multigraph}
\longrightarrow
\text{cycle double cover}.
$$

The natural theorem allows loops and finite active edge set. The present Lean checkpoint is earlier, loopless, and ambient-finite.

## 2. Five-support object

The open strengthening is equivalent to a root-valued flow

$$
E(G)\longrightarrow R_5\subset E_5,
$$

or to the `K_5` triangle, matching/four-flow, quadratic-cycle, and cographic formulations. The complete fixed-lift target is

$$
T_g^{(1)}\longrightarrow\mathscr A_5,
$$

not merely the factorable quotient through `J_g`.

## 3. Durable route-locked chain

The active backbone now includes:

- curvature/common-cut duality and singleton/transition/quartic localisation;
- unbounded quartic designs with canonical nucleus and strict split-or-peel recursion;
- quotient Tait phase, affine scalar sheets, Kempe systems, marked transition skeletons, and finite elementary intervals;
- physical `g`-component quotient `\Gamma_g`;
- route-capped flag-line carrier and touch-shadow closure;
- the bounded two-transition cap residue;
- coupled/separated minimal completion and cocircuit cut-rank;
- canonical natural projection to `\widehat Q`;
- the exact physical cycle--cut sequence;
- the Lagrangian response code;
- ribbon-intersection, boundary-radical, Euler-genus, orientability, and Petrial interpretations;
- admissible gauge-radicalisation duality;
- hyperbolic dual-flow norm representation;
- rank-one scalar-interval localisation;
- rank-two Tait-permutation defect localisation.

## 4. Controlling corrections

The following shortcuts are false or unsupported:

- a scalar-common-cut witness must be a graph cut;
- quartic incidence axioms bound `k`;
- consecutive witness edges are consecutive full `g`-edges;
- sheet `S_4`, terminal-route symmetry, and DDD support-label `D_8` are canonically identical;
- cocircuit minimality forces one connected physical cycle projection;
- abstract isotropic primeness alone identifies the physical obstruction.

The exact cube certificate gives a cocircuit projecting to two disjoint four-cycles.

## 5. Physical cycle--cut response

For the route-capped carrier

$$
F=\mathcal L(\widehat Q),
$$

full cocycles fit into

$$
\boxed{
0\to\operatorname{Cut}(\widehat Q)
\to\operatorname{Cocycle}(M_\tau(F))
\to\operatorname{Cycle}(\widehat Q)\to0.
}
$$

In local/cross coordinates a cocycle is

$$
(z,a,z+a),
$$

with

$$
a\cdot z'=\mathcal B(z,z')
$$

for every physical cycle `z'`.

The form `\mathcal B` is the mod-two intersection pairing of the corresponding signed ribbon surface. Hence

$$
\operatorname{rad}\mathcal B
=
\text{boundary-homology image},
$$

$$
\operatorname{rank}\mathcal B
=
\text{Euler genus},
$$

and `\mathcal B` is alternating exactly in the orientable case. A partial Petrial `\lambda` acts by

$$
\mathcal B_\lambda(z,z')
=
\mathcal B(z,z')+
\sum_e\lambda_ez_ez'_e.
$$

The zero-cycle branch is closed structurally: a zero-projection cocircuit is a physical bond.

## 6. Gauge-rigid odd-intersection pair

Let `C` be the admissible Petrial/gauge code. A response cycle `z` can be moved into the radical exactly when

$$
[a]\in
\operatorname{Im}
\bigl(\lambda\mapsto[\lambda\odot z]\bigr).
$$

Failure has the exact dual certificate

$$
\boxed{
\mathcal B(z,z')=1,
\qquad
w=z\odot z'\in C^\perp.
}
$$

For the active Fano-flow gauge code,

$$
C^\perp
=
\mathcal C(G)*\mathcal F_f.
$$

Equivalently there is a dual-valued flow

$$
u:E(G)\to\Gamma^*
$$

such that

$$
\boxed{w_e=\langle u(e),f(e)\rangle.}
$$

Thus `w` is the quadratic norm support of a hyperbolic flow `(f,u)`.

## 7. Dual-rank localisation

Define the dual rank of `w` as the minimum dimension of the span of an auxiliary dual flow `u` representing it.

### Rank one

$$
w=c*(\alpha\circ f).
$$

The support decomposes on scalar circuits into complete circuits and marked intervals. Odd total ribbon intersection localises to one odd scalar circuit or one odd marked interval.

### Rank two

Let `h` annihilate the image plane of `u`. Then `w` is controlled by the quotient four-flow

$$
\bar f:E\to\Gamma/\langle h\rangle
$$

and the dual four-flow `u`. At a vertex where both are Tait triples, their local correspondence is a permutation of three colours; the norm support is its moved-point set. The forbidden local word `111` excludes three-cycles, leaving only identity or transposition. Hence every path endpoint lies at the colour matching `E_h` or the zero locus of `u`. Odd intersection localises to one closed norm circuit or one defect-to-defect path.

## 8. Exact frontier

Dual ranks one and two are now localised. The first genuinely unlocalised nonflat branch is

$$
\boxed{
\text{dual rank three hyperbolic norm carrier}
+
\text{prime coupled cap response}
+
\text{locked route}.
}
$$

In parallel, the already localised rank-one and rank-two carriers still need composition-safe replacements or horizontal switches.

The next theorem should identify the full-rank hyperbolic carrier with a proper separator, bounded handle, flow switch, or a genuine DDD support-label class. Pure incidence, pure isotropic connectivity, and unrestricted response classification are no longer the correct level.

## 9. Downstream lines and assurance

The flat-potential interface, defect-forest pruning, four-pole gluing, and horizontal bad-flow theorem remain downstream. No Lean, independent-review, peer-review, merge, release, DOI, arXiv, or publication status is implied.

Reading entrypoints:

- [`ACTIVE_MATHEMATICAL_SURFACE.md`](ACTIVE_MATHEMATICAL_SURFACE.md);
- [`THEOREM_DEPENDENCY_MAP.md`](THEOREM_DEPENDENCY_MAP.md);
- [`five-support/README.md`](five-support/README.md);
- [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md);
- [`FORMAL_STATUS.md`](FORMAL_STATUS.md).
