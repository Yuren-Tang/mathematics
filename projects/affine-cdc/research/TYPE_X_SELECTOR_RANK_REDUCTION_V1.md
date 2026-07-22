# Type-X selector rank and reduction to the laminar interior-cycle branch

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `4a7f060ab7fbcfe583f3a4c8f80e8398c7242416`  
**Parents:**

- `projects/affine-cdc/research/PETERSEN_TYPE_X_CROSSED_SELECTOR_COMPARISON_V1.md`;
- `projects/affine-cdc/research/PETERSEN_RELATIVE_CHANNEL_PROFILE_CALIBRATION_V1.md`;
- `projects/affine-cdc/five-support/route-locked-quotient-phase.md`;
- `projects/affine-cdc/research/LOCKED_SCALAR_COMPONENT_ROUTING_V1.md`;
- `projects/affine-cdc/research/MINIMAL_LAMINAR_INTERVAL_SURGERY_V1.md`.

**Status:** exact selector-rank theorem and exact reduction of the only rank-one comparison failure to an internal quotient-Kempe cycle system. Full-rank selector data calibrate the entire four-point Type-X challenge plane. Rank-one data have one invisible sheet difference whose physical difference is a closed scalar cycle system disjoint from every relevant `g`-incidence.  
**Not implied:** componentwise root-admissible switching, minimal-interval replacement, separator extraction, strict descent, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Relevant `g`-incidences and selector map

Let

\[
c:E(Q)\to V\setminus\{0\},
\qquad
V=\langle g\rangle\oplus U,
\qquad
U\cong\mathbf F_2^2,
\]

be a full-rank route-locked quotient flow.

The four scalar sheets are indexed by

\[
\phi\in U^*.
\]

Fix a source region `R` carrying the identity-return or minimal-interval semantics under study. Let

\[
\mathcal I(R)
\]

be the set of endpoints of `g`-edges whose scalar continuation choices participate in the external or internal route interface of `R`.

At every incidence

\[
i\in\mathcal I(R),
\]

the two non-`g` continuation edges have one common quotient colour

\[
q_i\in U\setminus\{0\}.
\]

After ordering those two continuation edges, the physical selector bit is

\[
s_i(\phi)=\varepsilon_i+\phi(q_i)
\]

for one fixed

\[
\varepsilon_i\in\mathbf F_2.
\]

### Definition 1.1 — regional selector map

\[
\boxed{
S_R:U^*\longrightarrow\mathbf F_2^{\mathcal I(R)},
\qquad
S_R(\phi)=(s_i(\phi))_{i\in\mathcal I(R)}.
}
\]

Its linear part is

\[
L_R(\phi)=(\phi(q_i))_{i\in\mathcal I(R)}.
\]

---

## 2. Exact selector-rank theorem

Put

\[
Q_R=\langle q_i:i\in\mathcal I(R)\rangle
\subseteq U.
\]

### Theorem 2.1 — selector rank equals quotient-colour rank

\[
\boxed{
\operatorname{rank}L_R
=
\dim Q_R.
}
\]

### Proof

The kernel of `L_R` is

\[
\ker L_R
=
\{\phi\in U^*: \phi(q_i)=0\text{ for every }i\}
=
Q_R^\perp.
\]

Since `U` is finite-dimensional,

\[
\dim\operatorname{Im}L_R
=
\dim U^*-\dim Q_R^\perp
=
\dim Q_R.
\]

∎

Because every `q_i` is nonzero and `dim U=2`, only two cases occur:

\[
\boxed{
\operatorname{rank}L_R=1
\quad\text{or}\quad
\operatorname{rank}L_R=2.
}
\]

There is no rank-zero selector region.

---

## 3. Rank two gives complete Type-X calibration

Assume

\[
\dim Q_R=2.
\]

Then there exist incidences

\[
i,j\in\mathcal I(R)
\]

with

\[
q_i\ne q_j.
\]

The two nonzero vectors form a basis of `U`.

### Theorem 3.1 — two-incidence affine chart

The map

\[
\boxed{
S_{i,j}:U^*\longrightarrow\mathbf F_2^2,
\qquad
\phi\longmapsto(s_i(\phi),s_j(\phi))
}
\]

is an affine bijection.

### Proof

Its linear part is evaluation on the ordered basis `(q_i,q_j)`:

\[
\phi\longmapsto(\phi(q_i),\phi(q_j)).
\]

This is a linear isomorphism `U* -> F2^2`. Adding the constant selector vector `(epsilon_i,epsilon_j)` gives an affine bijection. ∎

### Corollary 3.2 — one crossed edge is sufficient but not necessary

Rank two occurs in either of the following bounded ways:

1. one crossed `g`-edge has two endpoint colours `q_i != q_j`;
2. two aligned `g`-edges, or two incidences on different edges, carry distinct quotient colours.

Thus a crossed edge is the smallest one-edge certificate, but any two distinct observed quotient colours calibrate the four challenges completely.

### Theorem 3.3 — complete challenge/profile comparison in rank two

Choose the complement-invariant Type-X chart

\[
\chi:\overline{\mathcal T}_r\xrightarrow{\sim}\mathbf F_2^2
\]

from the crossed-selector comparison theorem. Then

\[
\boxed{
J_{i,j}
=
\chi^{-1}\circ S_{i,j}
:
\Lambda_g\xrightarrow{\sim}\overline{\mathcal T}_r
}
\]

is a complete affine comparison of the four physical challenges with the four projective Type-X profiles.

Its linear part sends the three nonzero sheet differences to the three channel-triality translations according to their two-incidence switch signatures.

### Consequence 3.4

In selector rank two there is no remaining finite calibration ambiguity. Any obstruction is already graph-side:

- failure to realise the calibrated channel change by a route witness;
- incompatible side-component attachment;
- DDD/defect holonomy;
- separator or strict-descent failure.

---

## 4. Rank one is monochromatic at every relevant incidence

Assume

\[
\dim Q_R=1.
\]

Since every `q_i` is nonzero and a one-dimensional binary space has only one nonzero element, there is a unique

\[
q\in U\setminus\{0\}
\]

such that

\[
\boxed{
q_i=q
\qquad(i\in\mathcal I(R)).
}
\]

Let

\[
0\ne\delta_0\in U^*
\]

be the unique nonzero functional satisfying

\[
\delta_0(q)=0.
\]

### Theorem 4.1 — invisible sheet direction

For every challenge `phi` and every relevant incidence `i`,

\[
\boxed{
s_i(\phi+\delta_0)=s_i(\phi).}
\]

Thus the regional selector map identifies the two pairs

\[
\{\phi,\phi+\delta_0\}.
\]

Its image has two points and its kernel is

\[
\langle\delta_0\rangle.
\]

### Proof

For every relevant incidence,

\[
s_i(\phi+\delta_0)+s_i(\phi)
=\delta_0(q_i)
=\delta_0(q)
=0.
\]

∎

---

## 5. The invisible direction is a pure internal cycle system

The two scalar sheets differ by the quotient Kempe system

\[
K_{\delta_0}
=
\{e:\delta_0(\bar c(e))=1\}.
\]

The quotient-phase theorem gives:

- `K_(delta0)` is a disjoint union of graph cycles;
- it contains no `g`-edge.

The rank-one selector condition gives more.

### Theorem 5.1 — endpoint avoidance

At every relevant `g`-incidence, neither of the two non-`g` continuation edges belongs to

\[
K_{\delta_0}.
\]

Hence `K_(delta0)` is disjoint from a neighbourhood of every relevant `g`-edge endpoint.

### Proof

The two continuation edges at incidence `i` both have quotient colour `q_i=q`. Their `K_(delta0)` indicator is

\[
\delta_0(q)=0.
\]

Thus neither edge is present. ∎

### Corollary 5.2 — exact rank-one residual object

The only sheet difference invisible to all regional endpoint selectors is a closed scalar cycle system lying strictly inside the non-`g` components.

It is not a new affine or channel-profile obstruction. It is exactly the internal component-toggle object already analysed by locked scalar component routing.

---

## 6. Reduction to pair-changing or laminar routing

Write

\[
K_{\delta_0}=Z_1\sqcup\cdots\sqcup Z_m
\]

as its connected even components.

Fix one of the two scalar sheets

\[
A=H_\phi,
\]

so that

\[
H_{\phi+\delta_0}
=A\triangle K_{\delta_0}.
\]

Each component toggle

\[
A\triangle Z_k
\]

has the same four-terminal boundary as `A`.

### Theorem 6.1 — binary routing dichotomy

Exactly the existing scalar-component alternatives remain:

1. **pair-changing component:** some `Z_k` changes the terminal pairing of `A`;
2. **all pair-preserving:** every `Z_k` preserves the locked matching, and its attachment intervals to the two terminal paths are noninterlacing; an irreducible family is laminar.

### Proof

Boundary preservation is the component-toggle theorem. If an attachment pair interlaces between the two terminal paths, toggling reconnects the four terminal ends crosswise and changes the matching. Therefore pair preservation excludes interlacing. The locked scalar component theorem then gives the laminar partial order. ∎

### Trust boundary

The dichotomy is exact at the binary scalar-route level.

In the pair-changing branch, converting one component toggle into an admissible five-support/Kempe switch still requires the root-fibre lift. Failure belongs to the already classified empty-relation, DDD, or defect branches.

In the pair-preserving branch, root-admissible minimal-interval surgery and separator extraction remain open.

---

## 7. Master selector-rank reduction

### Theorem 7.1 — no third comparison branch

For every relevant Type-X identity-return or four-port region, exactly one of the following holds.

#### Rank-two comparison

\[
\dim\langle q_i\rangle=2.
\]

Two incidences give a complete affine identification

\[
\Lambda_g
\cong
\overline{\mathcal T}_r.
\]

All four challenges and all three triality directions are physically distinguished.

#### Rank-one interior-cycle reduction

\[
q_i=q
\quad\text{for all relevant incidences}.
\]

One sheet difference `delta0` is invisible at every endpoint, and its entire physical residue is the closed internal cycle system

\[
K_{\delta_0}.
\]

That system is pair-changing or reduces to the existing pair-preserving laminar interval branch.

There is no third selector-rank or finite calibration mechanism.

---

## 8. Revised route to strict progress

The remaining proof programme is now:

1. **Rank two:** use the calibrated Type-X profile to construct an actual route/profile transition; if the lift fails, localise the known root-fibre/DDD defect.
2. **Rank one, pair-changing:** prove componentwise root-admissible lifting or extract the failure as a bounded defect.
3. **Rank one, pair-preserving:** apply minimal laminar interval surgery:
   - crossing side semantics gives escape;
   - split signature gives a quotient separator, which lifts exactly to the source graph;
   - separated signature gives a smaller replacement or bounded atom.
4. Prove strict decrease of the side-signature/interval complexity.
5. Assemble horizontal/global induction.

The finite challenge/profile comparison problem is therefore closed except for the already identified laminar composition theorem.