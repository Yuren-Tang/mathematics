# Equality-channel functoriality defects are rank one or rank two

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `e8ec1f66da341d1b5a5a878e740745a93265610e`  
**Parents:**

- `projects/affine-cdc/research/EQUALITY_ROOT_RIGIDITY_FUNCTORIALITY_CORRECTION_V1.md`;
- `projects/affine-cdc/research/EQUALITY_LOCK_S5_ROOT_RIGIDITY_V1.md`;
- `projects/affine-cdc/research/ORIENTED_CHANNEL_LOCK_BOUNDARY_CALIBRATION_V1.md`;
- `projects/affine-cdc/research/INVERSE_DIPOLE_KEMPE_RESCUE_V1.md`;
- `projects/affine-cdc/five-support/frontier-localisation.md`.

**Status:** exact finite-rank classification of the missing physical functoriality in an equality full-channel lock. After normalising every common-component switch back to the same indexed equality boundary, each channel generator is an involution and disjoint generators commute. The failure of one generator to act affinely between two locked covers is exactly one single-root closed cycle flow. The failure of one adjacent Coxeter braid relation is a zero-boundary flow in one root triangle plane. Thus equality-channel nonfunctoriality creates only the already localised rank-one scalar or rank-two Tait carriers; it cannot create a new rank-three or unbounded channel alphabet.  
**Not implied:** strict elimination of every scalar cycle or Tait defect, construction of a global affine `S_5` action in the zero-defect branch, resolution of DDD pivot-change incidence, global induction, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Normalised equality fibre

Let `G` be the connected reduced cubic graph and let

\[
\lambda:E(G)\to R_5
\]

be a root-valued cover with marked reconnection edges

\[
e,f
\]

satisfying

\[
\lambda(e)=\lambda(f)=r=uv.
\]

Assume that the corresponding two-vertex cap remains blocked and that the complete boundary profile is in the fixed-route outer sector for matching `M_i`.

Let

\[
\mathscr L_r
\]

be the set of all reachable locked covers whose marked values have been reindexed to the same root `r` and whose ordered terminal route is `M_i`.

For every channel

\[
s\in S_r
=\{uw,vw:w\in[5]\setminus\{u,v\}\},
\]

and every `lambda in mathscr L_r`, let

\[
Z_s(\lambda)
\]

be the connected component of `H_s(lambda)` containing `e,f`.

Switching this component changes the marked root from `r` to

\[
r+s=\tau_s r,
\]

where `tau_s` is the support transposition associated with `s`.

### Definition 1.1 — normalised generator

Define

\[
\boxed{
T_s(\lambda)
=
\tau_s\bigl(\lambda+s1_{Z_s(\lambda)}\bigr).
}
\]

Then

\[
T_s(\lambda)(e)=T_s(\lambda)(f)=r,
\]

so

\[
T_s:\mathscr L_r\to\mathscr L_r.
\]

The dependence of `Z_s(lambda)` on the current cover is the complete physical functoriality issue.

---

## 2. Exact relations requiring no functoriality assumption

### Theorem 2.1 — involution law

For every `s in S_r` and every `lambda in mathscr L_r`,

\[
\boxed{T_s^2(\lambda)=\lambda.}
\]

### Proof

Switching `Z_s(lambda)` by `s` leaves the binary subgraph `H_s` unchanged: on that component it merely exchanges the two support names defining `H_s`. The global reindexing `tau_s` also fixes the root `s` and therefore preserves the edge set `H_s`. Hence the component through `e,f` after one normalised switch is again the same edge set `Z_s(lambda)`. A second switch adds `s` on the same set, and a second `tau_s` is the identity. ∎

### Theorem 2.2 — disjoint commutation

If

\[
s\cap t=\varnothing,
\]

then

\[
\boxed{T_sT_t(\lambda)=T_tT_s(\lambda)}
\]

for every `lambda in mathscr L_r`.

### Proof

The channel-conjugation law gives

\[
H_t(\lambda+s1_{Z_s})=H_t(\lambda)
\]

because `tau_s(t)=t`. Thus switching `Z_s` does not alter the `t`-component through the marked edges, and conversely. The support transpositions commute and fix one another's coefficients. Expanding both normalised compositions gives the same cover. ∎

These are the exact right-angled relations supplied by the channel-disjointness graph.

---

## 3. Affine transport defect between two covers

Let

\[
\lambda,\mu\in\mathscr L_r.
\]

If `T_s` were one fixed affine map with linear part `tau_s`, it would satisfy

\[
T_s(\lambda)+T_s(\mu)
=\tau_s(\lambda+\mu).
\]

### Definition 3.1 — generator transport defect

Put

\[
\mathcal D_s(\lambda,\mu)
=
T_s(\lambda)+T_s(\mu)
+	au_s(\lambda+\mu).
\]

### Theorem 3.2 — exact scalar-cycle formula

\[
\boxed{
\mathcal D_s(\lambda,\mu)
=
s1_{Z_s(\lambda)\triangle Z_s(\mu)}.
}
\]

### Proof

Using

\[
T_s(\lambda)
=	au_s\lambda+s1_{Z_s(\lambda)}
\]

and the corresponding formula for `mu`, the two linear terms cancel with `tau_s(lambda+mu)`. ∎

### Corollary 3.3 — rank-one defect

The transport defect is an `E_5`-valued flow with zero terminal boundary. Its only nonzero value is the root `s`. Therefore

\[
Z_s(\lambda)\triangle Z_s(\mu)
\]

is a disjoint union of closed binary cycles.

In particular:

\[
\boxed{
\mathcal D_s\ne0
\Longrightarrow
\text{one explicit rank-one scalar-cycle carrier}.}
\]

No co-root, transverse rank-three, or new channel value occurs.

### Corollary 3.4 — exact affine criterion

For a family `X subseteq mathscr L_r`, the generator `T_s` is the restriction of one affine map with linear part `tau_s` on `X` if and only if

\[
Z_s(\lambda)=Z_s(\mu)
\qquad(\forall\lambda,\mu\in X).
\]

Thus physical affine functoriality is exactly constancy of the selected marked component, not an additional abstract condition.

---

## 4. A four-generator Coxeter path

Write

\[
W=\{x,y,z\}.
\]

Choose the four channels

\[
s_1=ux,
\qquad
s_2=uy,
\qquad
s_3=vy,
\qquad
s_4=vz.
\]

As support transpositions they correspond to the path of support vertices

\[
x-u-y-v-z.
\]

Hence:

- consecutive `s_j,s_(j+1)` meet in one support index;
- nonconsecutive generators are disjoint;
- the four transpositions have the standard Coxeter diagram `A_4` and generate `S_5`.

The involution and nonadjacent-commutation relations already hold physically by Theorems 2.1 and 2.2. The only missing Coxeter relations are the three adjacent braids.

---

## 5. Braid defect

Let `s,t` be two adjacent generators, so they are distinct intersecting roots. Put

\[
d=s+t.
\]

Then

\[
W_{s,t}=\langle s,t\rangle
=\{0,s,t,d\}
\]

is one root-triangle plane.

The support permutations satisfy

\[
\tau_s\tau_t\tau_s
=	au_t\tau_s\tau_t.
\]

### Definition 5.1 — physical braid defect

For `lambda in mathscr L_r`, define

\[
\mathcal B_{s,t}(\lambda)
=
T_sT_tT_s(\lambda)
+
T_tT_sT_t(\lambda).
\]

Both endpoint covers have the same indexed boundary and the same support permutation, so `mathcal B_(s,t)` has zero terminal boundary.

### Theorem 5.2 — rank-two braid plane

\[
\boxed{
\mathcal B_{s,t}(\lambda)(a)
\in W_{s,t}
\qquad(\forall a\in E(G)).
}
\]

### Proof

Expand either three-step word. Its linear part is the common permutation

\[
\tau_s\tau_t\tau_s.
\]

Every translation coefficient appearing in the expansion is a conjugate of `s` or `t` under the subgroup they generate. The nonzero conjugates are exactly

\[
s,t,d.
\]

Subtracting the two endpoint covers cancels the common linear part and leaves values in their span `W_(s,t)`. ∎

### Corollary 5.3 — Tait defect

Every nonzero value of `mathcal B_(s,t)` is one of the three roots

\[
s,t,d.
\]

At a cubic vertex, conservation gives only:

- a degree-two equal-root continuation;
- or the three-colour triangle `(s,t,d)`.

After suppressing equal-root degree-two runs, every nonzero component is a properly three-edge-coloured Tait carrier.

Thus

\[
\boxed{
\mathcal B_{s,t}\ne0
\Longrightarrow
\text{one explicit rank-two Tait composition carrier}.}
\]

Again, equality-channel braid failure creates no new finite alphabet.

---

## 6. Complete functoriality dichotomy

Let `mathscr C` be a connected reconfiguration family inside the complete equality lock.

Exactly one of the following occurs.

### Branch R1 — generator transport defect

For some `s` and some `lambda,mu in mathscr C`,

\[
\mathcal D_s(\lambda,\mu)\ne0.
\]

Then the failure of affine transport is a rank-one scalar-cycle carrier.

### Branch R2 — braid defect

Every selected component is constant across `mathscr C`, but for one adjacent Coxeter pair and one cover,

\[
\mathcal B_{s,t}(\lambda)\ne0.
\]

Then the failure of word independence is a rank-two Tait carrier.

### Branch F — functorial affine sector

All generator transport defects and all three adjacent braid defects vanish throughout `mathscr C`.

Then:

1. each `T_(s_j)` is one fixed affine transformation on `mathscr C`;
2. the four transformations satisfy the `A_4` Coxeter presentation;
3. their products define a physical affine `S_5` action on `mathscr C`;
4. the conditional equality root-rigidity theorem applies.

In Branch F, the affine part reduces to a pure-gauge action. The remaining boundary-neutral motions belong to the stabiliser-fixed Type-Z scalar-cycle sector, especially components of `H_r` and the three channels disjoint from `r`.

### Theorem 6.1 — no unlocalised equality functoriality

Every failure of the equality-channel local system to become a functorial affine `S_5` action is already one of:

\[
\boxed{
\text{rank-one scalar cycle}
\quad\text{or}\quad
\text{rank-two Tait carrier}.}
\]

If no such failure occurs, the equality branch contains no affine/cohomological obstruction beyond the already identified Type-Z scalar cycles.

Hence the six-channel lock is not a genuinely new rank-three mechanism.

---

## 7. Relation to the endpoint fan

The endpoint fan theorem gives a second, boundary-visible rank-two certificate.

At a marked `r=uv` endpoint of local type `w`, the two arms carry the Type-X transversals `A_w,B_w`. For two endpoint types `w,w'`:

\[
A_w\triangle A_{w'}
=\Gamma_{ww'}.
\]

Thus the equality branch has two compatible rank-two detectors:

1. **interior detector:** a nonzero braid defect `mathcal B_(s,t)`;
2. **boundary detector:** a nonzero endpoint DDD class `Gamma_(ww')`.

The remaining comparison theorem should prove that a nonzero interior braid defect either reaches the corresponding endpoint class or is enclosed behind a smaller scalar/Tait separator.

---

## 8. Revised global meaning

The equality full-channel obstruction has now been reduced as follows:

\[
\text{six-channel component dependence}
\longrightarrow
\begin{cases}
\text{rank-one scalar cycles},\\
\text{rank-two Tait carriers},\\
\text{functorial pure-gauge Type-Z sector}.
\end{cases}
\]

All three outputs already occur elsewhere in the programme. The equality lock supplies no independent higher-rank state.

The remaining burden is composition:

- scalar-cycle interval/circuit descent;
- rank-two Tait carrier peeling and enclosure;
- comparison of internal braid defects with endpoint DDD classes;
- DDD pivot-change resolution;
- global well-founded packaging.

---

## 9. Trust boundary

### Exact here

- the normalised equality generator;
- involution and disjoint-commutation laws;
- exact generator transport-defect formula;
- scalar-cycle character of every nonaffine transport defect;
- the four-channel `A_4` generator path;
- rank-two plane bound for every physical braid defect;
- reduction of braid defects to Tait carriers;
- the rank-one/rank-two/functorial trichotomy.

### Conditional here

- application of root rigidity in Branch F assumes the vanishing relations throughout the complete reachable family, so that the four generators are fixed affine transformations rather than cover-dependent correspondences.

### Still open

- strict elimination of every scalar-cycle transport defect;
- strict elimination or enclosure of every rank-two braid defect;
- interior-to-endpoint DDD comparison;
- DDD pivot-change composition;
- global induction and horizontal bookkeeping;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
