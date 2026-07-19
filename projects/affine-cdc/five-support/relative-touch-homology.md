# Relative touch homology and its shadow collapse

## 1. Purpose

The route-capped line-graph carrier initially expresses scalar common cuts as relative touch cycles. This formulation is correct, but for partitions arising from cubic even subgraphs the apparent complementary boundary closes automatically.

Every scalar circuit has one distinguished circuit and one shadow circuit in the line-graph partition. Selected touch edges form a dipole between them. Therefore boundary at the shadow is identical to boundary at the distinguished circuit.

The only genuine relative boundary is terminal, and it is closed by the two fixed route-cap edges. This chapter records the relative formulation and its exact collapse to ordinary touch cycles.

## 2. Relative formulation

Let

$$
F=\mathcal L(\widehat Q)
$$

be the route-capped flag-line graph, and let

$$
P_\phi=P(\widehat H_\phi)
$$

be one scalar circuit partition.

Restrict the touch-graph to internal `g`-edges:

$$
\Theta_\phi
=\operatorname{Tch}(P_\phi)[E_g^{\mathrm{int}}].
$$

Let `I_\phi` be the vertices corresponding to closed scalar circuits. If all other touch vertices are provisionally treated as boundary, the relative boundary map is

$$
\partial^{\mathrm{rel}}_\phi:
\mathbf F_2^{E_g^{\mathrm{int}}}
\to
\mathbf F_2^{I_\phi},
$$

with

$$
(\partial^{\mathrm{rel}}_\phi x)_C
=|x\cap C|\pmod2.
$$

### Theorem 2.1 — scalar cuts as relative cycles

For `x\subseteq E_g^{\mathrm{int}}`, the following are equivalent:

1. `x` is a cut vector in `H_\phi`;
2. `x` meets every closed scalar component evenly;
3. `\partial^{\mathrm{rel}}_\phi x=0`.

Hence

$$
\mathcal Z_{\mathrm{com}}
=
\bigcap_{\phi\in U^*}
\ker\partial^{\mathrm{rel}}_\phi.
$$

## 3. Terminal boundary and curvature

For `x\in\mathcal Z_{\mathrm{com}}`, define

$$
\beta_\phi(x)
=
\bigl(
|x\cap P^{12}_\phi|,
|x\cap P^{34}_\phi|
\bigr).
$$

Then

$$
\boxed{
\Omega(x)=\sum_\phi\beta_{\phi,34}(x).
}
$$

Because all closed-component intersections are even,

$$
\beta_{\phi,12}(x)+\beta_{\phi,34}(x)
=|x|\pmod2.
$$

Summing over four sheets gives

$$
\boxed{
\sum_\phi\beta_{\phi,12}(x)
=
\sum_\phi\beta_{\phi,34}(x)
=
\Omega(x).
}
$$

## 4. Shadow collapse

For an even subgraph `H` of a cubic graph, the canonical line-graph partition has:

- one distinguished circuit `D_C` for every circuit component `C` of `H`;
- one shadow circuit `S_C` following the complementary track around the same `C`;
- triangle circuits at isolated vertices of `H`.

Every selected touch edge labelled by `e\in C` joins `D_C` to `S_C`. Therefore the selected touch subgraph is a disjoint union of dipoles.

### Theorem 4.1 — no independent complementary boundary

For `x\subseteq H`, touch boundary at `D_C` and `S_C` is the same bit

$$
|x\cap C|\pmod2.
$$

Thus vanishing at a distinguished closed scalar circuit automatically gives vanishing at its shadow. No uncontrolled complementary-circuit syndrome remains.

The earlier relative boundary space is therefore only terminal-relative for the selected `g`-edge chain.

## 5. Bounded cap closure

Let `z_{12},z_{34}` be the fixed route-cap edges. Define

$$
\widehat x_\phi
=
x
+
\beta_{\phi,12}(x)z_{12}
+
\beta_{\phi,34}(x)z_{34}.
$$

### Theorem 5.1 — ordinary touch closure

`\widehat x_\phi` is an ordinary cycle of the selected touch subgraph of `P_\phi`.

#### Proof

Closed scalar circuits meet `x` evenly. On each terminal circuit, the corresponding cap coefficient makes the total intersection even. Shadow parity duplicates distinguished parity. ∎

Hence every common-cut witness gives four ordinary touch cycles, one in each scalar partition.

Under

$$
M_\tau(F)|\tau(P_\phi)
\cong
M^*(\operatorname{Tch}(P_\phi)),
$$

the cap-completed transition support is a cocycle vector of the corresponding transverse restriction. It need not be a cocircuit.

## 6. Pointed curvature packet

The pointed curvature coextension may now be viewed as four cap-completed touch cocycles together with their cap-choice words.

The odd terminal functional no longer measures a failure of touch closure. It measures the parity with which the two fixed caps are used across the four closures. For a nonflat witness, each cap is used in an odd number of sheets.

## 7. Four-sheet transition residue

At every internal `g`-edge, the four scalar transitions cancel in the free binary transition space:

- aligned: one cross transition occurs four times;
- crossed: each cross transition occurs twice.

Therefore the sum of the four cap-completed transition-support vectors is supported only at the two cap vertices.

The exact residue theorem is developed in
[`touch-shadows-and-cap-residue.md`](touch-shadows-and-cap-residue.md): for `\Omega(x)=1`, the residue consists of exactly one cross transition at each cap vertex.

## 8. Updated matroid frontier

The relative-boundary closure problem is solved. The remaining questions are:

1. whether the cap-completed cocycle vectors admit bounded cocircuit representatives in the full transition matroid;
2. whether the two-transition cap residue forces a low-order transition separation;
3. whether such a separation projects to a terminal-even cut or two-sum in `\Gamma_g`;
4. whether a nonseparating residue can be compared with the physical DDD support-label class.

Three symmetry spaces must remain distinct until a comparison theorem is proved:

- sheet-coordinate `S_4\cong AGL(2,2)`;
- the terminal-route coordinate group on the four semiedges;
- the support-label `D_8` stabiliser of a DDD one-factor.

## 9. Reliability boundary

Proved here:

- the relative touch formulation of scalar common cuts;
- terminal relative-boundary evaluation of curvature;
- exact shadow duplication of distinguished boundary;
- absence of an independent complementary syndrome;
- bounded route-cap closure to ordinary touch cycles;
- reduction of the remaining four-sheet obstruction to the cap residue.

Corrected here:

- complementary partition circuits do not carry an uncontrolled boundary for selected edges; they are canonical shadows of scalar circuits.

Not proved here:

- full transition-matroid cocircuit status;
- a split or separator forced by the cap residue;
- comparison with the physical DDD support-label cocycle;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, DOI, or merge status is implied.
