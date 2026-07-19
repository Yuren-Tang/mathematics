# AffineCDC frontier status

This file records the exact theorem boundary on the active corpus. It is not an assurance upgrade.

## 1. Closed route-locked layers

Within their stated scopes, the active line now closes:

- full-rank curvature/common-cut duality and flat-potential equivalence;
- support-minimal odd-circuit localisation;
- singleton/transition/quartic trichotomy;
- unbounded abstract quartic designs and their symplectic form;
- quotient Tait-phase representation and affine sheet/Kempe relations;
- connected pairwise marked transition skeletons;
- canonical `O^-(4,2)` terminal nucleus, intrinsic `E_5/K_5`, and one-dimensional curvature carrier;
- exact split-or-peel recursion and bounded `K_6` coefficient gadgets;
- canonical `S_4`-equivariant nucleus transport and pairwise marked shell;
- elementary scalar transfer, caps, periodic cells, and Kempe ladders;
- physical `g`-component transition quotient `\Gamma_g` and exact internal-cut lifting;
- canonical route-capped `4`-regular line-graph carrier;
- touch-shadow decomposition and automatic complementary-boundary closure;
- the bounded two-transition cap residue;
- IAS loop/parallel/twin/pendant cap classification;
- existence and coupled/separated decomposition of minimal full cap-cocycle completions.

The global five-support theorem remains open.

## 2. Nonflat localisation

For the locked full-rank nonflat flow, choose a support-minimal witness

$$
\eta\subseteq E_g.
$$

It is a curvature-odd circuit of the closed-component incidence matroid and has exactly one form:

1. singleton enriched atom;
2. a closed scalar component meets `\eta` in two edges;
3. quartic core `|\eta|=4k+1`.

A scalar-common cut need not be a cut in the original four-pole. The exact full-rank singleton certificate proves this.

## 3. Quartic incidence progress and symmetry correction

Every quartic design contains a canonical nondegenerate minus-type four-space

$$
S=\langle1_X+e_0,\ldots,1_X+e_3\rangle.
$$

Its five singular points and ten roots form intrinsic `E_5/K_5` geometry. Curvature is carried by

$$
S/s_\infty^\perp\cong\mathbf F_2.
$$

Terminal distribution yields:

- `3`: co-root equality transport;
- `2+1`: one `K_6` perfect-matching vertex;
- `1+1+1`: a perfect-matching vertex followed by a root triangle.

Hence every quartic core satisfies

$$
\boxed{
\text{bounded root-exposed split}
\quad\text{or}\quad
\text{canonical nucleus peel }k\mapsto k-1.
}
$$

The natural symmetry of the four sheet labels is `AGL(2,2)\cong S_4`. It is not canonically identical to either the terminal-route stabiliser or the support-label `D_8` stabiliser of a DDD one-factor. A comparison map remains part of the open graph-level theorem.

## 4. Scope correction for scalar intervals

A scalar circuit block may contain additional `g`-edges outside `\eta`. Therefore its four marked witness edges determine four witness arcs, not necessarily four non-`g` intervals.

An elementary scalar interval lies between consecutive full `g` incidences. Such an interval has:

- one of eighteen quotient transfer states;
- telescoping side-output sum;
- either a bounded backtrack cap or a periodic triangle-cell chain;
- rigid three-Kempe ladder wiring in the periodic case.

A witness arc may concatenate arbitrarily many elementary intervals separated by edges of `E_g\setminus\eta`.

## 5. Physical cut carrier: `\Gamma_g`

Delete all `g`-edges and contract each remaining connected component. The quotient `\Gamma_g` is an even-total-degree four-pole whose edges are the `g`-edges and whose four scalar sheets give four transition systems.

Every internal quotient cut lifts exactly:

$$
\delta^{\mathrm{int}}_{\Gamma_g}(\mathcal U)
=
\delta^{\mathrm{int}}_Q(X_\mathcal U).
$$

The correct parity law is

$$
|\delta^{\mathrm{int}}(\mathcal U)|
\equiv t(\mathcal U)\pmod2,
$$

where `t(\mathcal U)` counts original terminal flags on the shore. Thus terminal-free and two-terminal shores have even internal boundary.

## 6. Standard `4`-regular carrier

Close the terminals according to the locked route `12\mid34` and take the flag-line graph

$$
F=\mathcal L(\widehat Q).
$$

Every scalar even subgraph gives a canonical circuit partition of this common `4`-regular graph. The four sheets are four transition transversals of one transition matroid.

At every edge of `\widehat Q`, the four transition choices obey the unified local law:

- non-`g` aligned: `2+2+0`;
- non-`g` crossed: `2+1+1`;
- `g` aligned: all four use one cross transition;
- `g` crossed: two use each cross transition.

## 7. Touch closure and bounded residue

For one scalar even subgraph, every scalar circuit gives one distinguished circuit and one shadow circuit in the line-graph partition. Selected touch edges form dipoles between the two. Therefore even intersection at a scalar component kills both distinguished and shadow boundary.

The two fixed route caps close every scalar common cut to an ordinary touch cycle. Summing the four cap-completed transition-support vectors cancels every internal `g`-edge transition and leaves

$$
\boxed{R=\{r_p,r_q\},}
$$

one cross transition at each cap vertex.

The complementary-boundary problem is therefore closed. The size and location of the original witness no longer appear in the four-sheet residue.

## 8. Full cocycle completion

Every full IAS cocycle meets each vertex triple in zero or two elements, so `R` is not itself a cocycle.

If a selected residue transition is a loop, there is an immediate one-element degeneration. Otherwise a cocycle containing both elements exists by binary linear algebra.

Choose an inclusion-minimal such cocycle `C`. Exactly one of:

1. **coupled:** `C` is one cocircuit containing both cap residues;
2. **separated:**
   $$
   C=D_p\sqcup D_q,
   $$
   where `D_p,D_q` are disjoint cocircuits, each carrying one cap residue.

In the separated case their isotropic vertex supports are disjoint.

All completions confined to the two cap triples are already classified: they occur only through loop, parallel, twin, or pendant interlacement configurations.

## 9. Immediate theorem target

The primary frontier is now:

$$
\boxed{
\text{minimal cap-cocycle completion}
\Longrightarrow
\begin{cases}
\text{terminal-even separator / serial composition in }\Gamma_g,\\
\text{alternate route and root escape},\\
\text{or a graph-level comparison with the DDD class.}
\end{cases}}
$$

The two branches should be treated separately.

- **Separated branch:** project two disjoint one-cap cocircuits to two independent terminal interfaces or a proper separator.
- **Coupled branch:** use its local-set/cut-rank structure. Low cut-rank should force an isotropic split; only a prime coupled carrier can remain a candidate for an irreducible DDD-type obstruction.

## 10. Secondary open lines

After this primary bridge:

- compose singleton and marked two-edge interfaces;
- extract a finite interface from the flat potential;
- prune defect forests;
- complete Type T/Type H four-pole composition;
- prove horizontal escape/decomposition;
- enlarge target certificates only where required.

## 11. Status

No active source proves the global five-support theorem. No Lean, independent-review, peer-review, merge, release, arXiv, DOI, or publication status is implied.
