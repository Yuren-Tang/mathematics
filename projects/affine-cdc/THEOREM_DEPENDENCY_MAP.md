# AffineCDC theorem dependency map

This map separates the complete Cycle Double Cover spine from the open five-support strengthening and records the active natural dependency chain.

## 1. Complete CDC spine

$$
\text{bridgeless finite-active-edge multigraph}
\to
\text{cubic binary-flow shell}
\to
\text{rank-three affine compatibility}
\to
\text{even double cover}
\to
\text{collapse transport}
\to
\text{cycle double cover}.
$$

Controlling chapters:

- [`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md);
- [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md);
- [`reduction/outer-shell-and-binary-flow.md`](reduction/outer-shell-and-binary-flow.md);
- [`reduction/even-cover-and-collapse.md`](reduction/even-cover-and-collapse.md).

## 2. Five-support object

$$
\text{five indexed even supports}
\Longleftrightarrow
\text{root-valued }E_5\text{ flow}
\Longleftrightarrow
\text{$K_5$ triangles / matching--four-flow / quadratic-cycle data}.
$$

For a fixed compatible lift, the complete target is

$$
T_g^{(1)}\longrightarrow\mathscr A_5,
$$

not merely the factorable quotient through `J_g`.

Controlling chapters:

- [`five-support/root-flow-lifting.md`](five-support/root-flow-lifting.md);
- [`five-support/surfaces-and-halfcube.md`](five-support/surfaces-and-halfcube.md).

## 3. Gauge, routing, and defect reduction

$$
\text{gauge / horizontal switches}
\to
\text{three-cut and ten-state four-cut interfaces}
\to
P_5\mid P_5\text{ or }P_4\mid C_3
\to
\text{holonomy / defect forest / Petersen atoms}.
$$

The soluble Type H branch escapes by Tait colouring. A blocked co-root atom gives the route-locked quotient endpoint.

## 4. Route-locked dichotomy

For the equal-terminal-colour quotient flow:

$$
\begin{cases}
\operatorname{rank}=2&\Rightarrow\text{Tait escape},\\
\operatorname{rank}=3,\ \Omega=0&\Rightarrow\text{eight-state flat potential},\\
\operatorname{rank}=3,\ \Omega\ne0&\Rightarrow\text{support-minimal common-cut witness}.
\end{cases}
$$

## 5. Nonflat localisation

$$
\boxed{
\begin{cases}
|\eta|=1&\Rightarrow\text{aligned/crossed enriched atom},\\
|C\cap\eta|=2&\Rightarrow\text{marked scalar transition pair},\\
|\eta|=4k+1&\Rightarrow\text{quartic near-resolution core}.
\end{cases}}
$$

Controlling chapter:
[`five-support/common-cut-circuit-localisation.md`](five-support/common-cut-circuit-localisation.md).

## 6. Quartic incidence progress

Abstract designs exist for every `k`, but each has a canonical terminal nucleus

$$
S\cong O^-(4,2),
\qquad
S/s_\infty^\perp\cong\mathbf F_2.
$$

Terminal distribution gives bounded equality/one-factor/root-triangle coefficient gadgets, or an all-concentrated peel

$$
\boxed{k\longmapsto k-1.}
$$

The natural sheet symmetry is `AGL(2,2)\cong S_4`; comparison with terminal-route and DDD support-label symmetries is open.

## 7. Quotient phase and elementary paths

After quotient by `\langle g\rangle`, the flow is a degenerate `\mathbf F_2^2` Tait flow plus one binary phase. The four scalar sheets form an affine plane and differ by three quotient Kempe systems.

Elementary paths between consecutive full `g` incidences have finite transfer states and cap-or-periodic-ladder normal form. Whole witness arcs may pass through additional `g`-edges and are transition walks.

## 8. Physical cut quotient

Contract the components of `Q-E_g` to obtain `\Gamma_g`. Scalar sheets become transition systems and every internal quotient cut lifts exactly:

$$
\delta^{\mathrm{int}}_{\Gamma_g}(\mathcal U)
=
\delta^{\mathrm{int}}_Q(X_\mathcal U),
$$

with parity

$$
|\delta^{\mathrm{int}}(\mathcal U)|\equiv t(\mathcal U)\pmod2.
$$

## 9. Route-capped transition carrier

Close the terminals according to `12\mid34` and put

$$
F=\mathcal L(\widehat Q).
$$

Every scalar even subgraph gives a circuit partition of this common `4`-regular graph. Each selected scalar circuit has one distinguished circuit and one shadow circuit; selected touch edges form a dipole. Thus complementary touch boundary closes automatically.

Adding the two route caps closes every scalar common cut to an ordinary touch cycle.

## 10. Bounded cap residue

Summing the four cap-completed transition-support vectors cancels all internal witness transitions and leaves

$$
\boxed{R=\{r_p,r_q\},}
$$

one cross transition at each cap vertex.

The bare residue is not a full cocycle. Local loop/parallel/twin/pendant cases are classified exactly.

## 11. Minimal full completion

Except for a loop degeneration, a full cocycle containing `R` exists. An inclusion-minimal completion is exactly

$$
\boxed{
\begin{cases}
\text{one cocircuit containing }r_p,r_q,&\text{coupled},\\
D_p\sqcup D_q\text{ with disjoint one-cap cocircuits},&\text{separated}.
\end{cases}}
$$

The separated cocircuits have disjoint isotropic vertex supports.

## 12. Isotropic cut-rank mechanism

For a cocircuit `D` with active vertex support `L(D)`,

$$
\boxed{
r(D)=|L(D)|+\rho(L(D)),
\qquad
n(D)=|L(D)|-\rho(L(D)).
}
$$

Thus cut-rank zero is disconnected, cut-rank one is a Cunningham split, and only cut-rank at least two is prime.

## 13. Natural physical projection

The canonical local-transition transversal of `F` has circuit partition equal to the vertex triangles of `\widehat Q`; its touch-graph is canonically `\widehat Q`.

Therefore every full cocycle projects to a physical cycle vector. The cap local-transition coordinates determine whether uncapping gives an internal cycle, a one-pair terminal join, or a four-terminal routing subgraph.

Controlling chapter:
[`five-support/natural-transversal-physical-projection.md`](five-support/natural-transversal-physical-projection.md).

## 14. Cycle--cut exact sequence

The kernel of the natural projection is exactly the physical cut space. For every vertex shore `S`, the corresponding kernel cocycle contains both cross transitions precisely on `\delta_{\widehat Q}(S)`.

Hence

$$
\boxed{
0\to\operatorname{Cut}(\widehat Q)
\to\operatorname{Cocycle}(M_\tau(F))
\to\operatorname{Cycle}(\widehat Q)\to0.
}
$$

A zero-projection cocircuit is therefore a physical bond. Coupled zero projection yields a terminal-even separator; separated one-cap zero projection yields a one-ended bond.

Controlling chapter:
[`five-support/natural-transversal-cycle-cut-exact-sequence.md`](five-support/natural-transversal-cycle-cut-exact-sequence.md).

## 15. Physical response form

Order the two cross transitions at every edge and write a cocycle triple as

$$
(z_e,a_e,z_e+a_e).
$$

The full cocycle code is Lagrangian. Its image is the physical cycle space and its kernel is the cut space, so it is determined by a symmetric response form

$$
\mathcal B_{\widehat Q}:
\operatorname{Cycle}(\widehat Q)^2\to\mathbf F_2
$$

through

$$
\boxed{
(z,a)\text{ is a full cocycle}
\iff
z\in\operatorname{Cycle}(\widehat Q),
\quad
a\cdot z'=\mathcal B_{\widehat Q}(z,z')
\ \forall z'.
}
$$

Cross-transition relabelling changes `\mathcal B` only by diagonal gauge.

The cube certificate shows that cocircuit minimality does not force `z` to be connected.

Controlling chapters:

- [`five-support/physical-cycle-cut-response-form.md`](five-support/physical-cycle-cut-response-form.md);
- [`five-support/cube-multicycle-cocircuit-certificate.md`](five-support/cube-multicycle-cocircuit-certificate.md).

## 16. Exact open bridge

The only potentially irreducible nonflat branch is

$$
\boxed{
\text{coupled prime cap cocircuit}
+
z\ne0
+
a\bmod\operatorname{Cut}=\mathcal B(z,-)
+
\text{locked cap response}.
}
$$

The next theorem must use the common Fano flow, four affine scalar sheets, three Kempe systems, endpoint selectors, fixed route, and `\Gamma_g` to yield:

1. a physical separator or transition two-sum;
2. a crossed route and root escape;
3. a bounded replacement or horizontal switch;
4. or a genuine comparison with the DDD support-label cocycle.

After this bridge come the flat-potential interface, defect-forest pruning, four-pole transfer, and horizontal escape/decomposition.

Controlling frontier chapter:
[`five-support/frontier-localisation.md`](five-support/frontier-localisation.md).

## 17. Assurance axes

No arrow in this map automatically transfers Lean status, independent audit, peer review, novelty, release, DOI, arXiv, or publication status. See [`FORMAL_STATUS.md`](FORMAL_STATUS.md).
