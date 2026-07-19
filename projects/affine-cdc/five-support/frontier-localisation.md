# The current five-support frontier: cap cocircuits and physical composition

## 1. Closed layers

The active corpus now closes, within stated scopes:

- five-support/root-flow equivalences and fixed-plane lifting;
- surface/dual/halfcube formulations;
- gauge and horizontal switch laws;
- three-cut gluing and ten-state four-cut interfaces;
- Type T/Type H reduction and Tait escape from the soluble Type H branch;
- BBD/DDD defect geometry, Petersen transport, unique bad route, and rank-two escape;
- full-rank curvature/common-cut duality and flat-potential equivalence;
- odd witness circuits and singleton/transition/quartic localisation;
- unbounded abstract quartic designs and strict split-or-peel recursion;
- quotient Tait phase, marked transition skeletons, and elementary interval/Kempe-ladder theory;
- the physical `g`-component quotient `\Gamma_g`;
- the canonical route-capped `4`-regular line-graph carrier;
- touch-shadow closure and the bounded two-transition cap residue;
- IAS local degenerations and the coupled/separated minimal-cocycle theorem;
- the exact cocircuit rank/cut-rank formulas.

The global five-support theorem remains open.

## 2. Global proof routes

For a bridgeless cubic graph, graph-level success may occur by:

1. **escape:** one Fano flow and compatible lift satisfy
   $$
   T_g^{(1)}\longrightarrow\mathscr A_5;
   $$
2. **decomposition:** every persistent bad region produces a proper interface across which smaller five-support covers glue.

The sharp current bottleneck is source-side physical composition, not a larger finite obstruction census.

## 3. Route-locked nonflat endpoint

A blocked co-root atom gives a full-rank quotient flow with terminal colour `g` and four scalar sheets routed as `12\mid34`.

For `\Omega(c)\ne0`, a support-minimal witness

$$
\eta\subseteq E_g
$$

is a curvature-odd circuit of the closed-component incidence matrix and has one of:

1. singleton aligned/crossed atom;
2. marked two-edge scalar transition;
3. quartic core `|\eta|=4k+1`.

The witness need not be a cut in the original four-pole.

## 4. Incidence progress and symmetry trust boundary

The quartic terminal nucleus is a canonical minus-type four-space

$$
S\cong O^-(4,2),
\qquad
S/s_\infty^\perp\cong\mathbf F_2.
$$

Terminal distributions give bounded coefficient gadgets or a strict peel `k\mapsto k-1`.

The natural symmetry of the sheet labels is `AGL(2,2)\cong S_4`. This sheet group is not canonically identified with either:

- the physical terminal-route stabiliser of `12\mid34`;
- the support-label `D_8` stabiliser of a DDD one-factor.

A graph-level comparison map is an open theorem, not a convention.

## 5. Physical carriers

### 5.1 `g`-component quotient

Contract the components of `Q-E_g` to obtain an even-total-degree four-pole `\Gamma_g`. Scalar sheets become transition systems. Every internal quotient cut lifts exactly:

$$
\delta^{\mathrm{int}}_{\Gamma_g}(\mathcal U)
=
\delta^{\mathrm{int}}_Q(X_\mathcal U),
$$

with terminal-sensitive parity

$$
|\delta^{\mathrm{int}}(\mathcal U)|\equiv t(\mathcal U)\pmod2.
$$

A terminal-even separator found in `\Gamma_g` is therefore already a physical separator in `Q`.

### 5.2 Route-capped `4`-regular carrier

Close terminals according to `12\mid34` and take

$$
F=\mathcal L(\widehat Q).
$$

Every scalar even subgraph gives a circuit partition of this common `4`-regular graph. The four sheets are four transition transversals of one transition matroid.

### 5.3 Touch-shadow closure

Every scalar circuit has one distinguished circuit and one shadow circuit in the line-graph partition. Selected touch edges form dipoles between them. Therefore closed-component parity kills both distinguished and complementary boundary.

Adding the two fixed route caps closes each scalar common cut to an ordinary touch cycle.

## 6. Bounded cap residue

Sum the four cap-completed transition-support vectors. At every internal `g`-edge:

- aligned transitions occur four times;
- crossed transitions occur twice in each cross state.

All internal support cancels, leaving

$$
\boxed{R=\{r_p,r_q\},}
$$

one selected cross transition at each route-cap vertex.

Thus arbitrary witness size, quartic level, and internal transition walks disappear from the four-sheet residue.

## 7. Local isotropic degenerations

Every IAS cocycle meets each vertex triple in zero or two elements, so `R` is not itself a full cocycle.

The following cases are completely classified:

- a selected residue transition is a loop;
- the two selected transitions are parallel;
- a full cocycle completion is supported only at the two cap triples.

They occur exactly through isolated, pendant, adjacent-twin, or nonadjacent-twin interlacement configurations. These are immediate low-connectivity cases.

## 8. Minimal full completion

Outside the loop case, a full cocycle containing both residue elements exists by binary linear algebra. Choose one inclusion-minimal under support.

### Theorem — coupled/separated dichotomy

Exactly one of:

1. **coupled:** one cocircuit `D` contains both `r_p,r_q`;
2. **separated:**
   $$
   C=D_p\sqcup D_q,
   $$
   where `D_p,D_q` are disjoint cocircuits, each carrying one residue.

In the separated case their isotropic vertex supports are disjoint.

Only the coupled branch can carry a genuinely irreducible two-ended obstruction.

## 9. Cut-rank mechanism

For an IAS cocircuit `D`, let `L(D)` be the set of vertex triples it meets. Then

$$
\operatorname{span}D=\operatorname{span}\tau(L(D)),
$$

and

$$
\boxed{
 r(D)=|L(D)|+\rho_G(L(D)),
 \qquad
 n(D)=|L(D)|-\rho_G(L(D)).
}
$$

For a cocircuit,

$$
\boxed{
\lambda_M(D)=|L(D)|+\rho_G(L(D))-1.
}
$$

Hence, for a nontrivial shore:

- `\rho=0`: interlacement disconnection;
- `\rho=1`: Cunningham split;
- `\rho\ge2`: prime-side carrier.

The separated branch has two disjoint one-cap carriers, each with its own cut-rank. The coupled branch has one cap-to-cap carrier.

## 10. Primary theorem target

The exact frontier is now:

$$
\boxed{
\text{coupled/separated cap cocircuit}
\Longrightarrow
\begin{cases}
\text{terminal-even separator or serial composition in }\Gamma_g,\\
\text{alternate transition and root escape},\\
\text{or graph-level comparison with the DDD class.}
\end{cases}}
$$

Recommended order:

1. transport interlacement disconnections and rank-one splits through the route-capped line graph to `Q` and `\Gamma_g`;
2. eliminate two disjoint prime one-cap carriers in the separated branch;
3. analyse the prime coupled cap-to-cap cocircuit;
4. construct the sheet/terminal/support comparison only on that final branch.

The irreducible candidate is therefore no longer an arbitrary quartic core. It is precisely:

$$
\boxed{
\text{one coupled cap cocircuit}
+
\text{one prime local carrier }L
+
\rho_G(L)\ge2.
}
$$

## 11. Secondary programmes

After this primary bridge:

1. compose singleton and marked-pair interfaces;
2. extract a finite flat-potential interface;
3. prune defect forests;
4. complete Type T/Type H four-pole composition;
5. prove horizontal escape/decomposition;
6. enlarge target certificates only where the source theorem requires it.

Planar Fano-line flattening, orientable good lifts, and coefficient holonomy remain valuable projections but are not the current bottleneck.

## 12. Reliability boundary

No active source proves the global five-support theorem. No Lean, independent-review, peer-review, merge, release, arXiv, DOI, or publication status is implied.
