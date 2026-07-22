# Physical weight-two translation classes admit strict source descent

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `40abd7a1d4b4b969b2ff5de395b8b426b178e6dd`.

**Parents:**

- `PHYSICAL_A3_TRANSLATION_CHAIN_MAP_V1.md`;
- `PHYSICAL_TRANSLATION_CELL_ANALYSIS_V1.md`;
- `LOCKED_SCALAR_COMPONENT_ROUTING_V1.md`;
- `MINIMAL_LAMINAR_INTERVAL_SURGERY_V1.md`;
- `NONCROSSING_SIDE_SIGNATURE_WINDOW_V1.md`;
- `FOUR_PORT_TAIT_DIPOLE_PEELING_V1.md`;
- `SHIFT_MATCHING_BANDS_ROUTE_TAIT_PEELING_V1.md`;
- `TYPE_T_PHYSICAL_COMMUTATION_ELIMINATION_V1.md`;
- `TYPE_H_PHYSICAL_COMMUTATION_ELIMINATION_V1.md`;
- the equality/DDD inverse-lift and contextual-transfer dossiers;
- the cyclic three-/four-cut gluing theorems.

**Status:** exact composition synthesis for the nonconstant flat rank-three classes. A weight-two physical challenge word selects one canonical nonzero quotient direction `delta` and one closed scalar Kempe system `H_delta`. A pair-changing component gives immediate route/profile escape or a previously classified root-lift defect. If all components are pair-preserving, their attachments are laminar. The complete side network splits into complementary Tait multipoles and private-shift matching bands; both admit category-safe one-dipole peeling. Every inverse expansion is exactly root/equality/DDD. Root lifts continue the peeling, equality and DDD enter the established contextual-transfer programme, and category failure exposes a two-/three-/four-cut or bounded degeneration. Hence the weight-two class cannot support an unbounded prime rank-three carrier.

**Not implied:** physical triviality of the zero or constant-one translation classes, composition-safe separation of an odd curvature torsor core, final rank-three theorem, global five-support theorem, canonical acceptance, independent audit, Lean verification, manuscript integration, release, or publication.

---

## 1. Exact physical input

Let

\[
B_{\mathrm{phys}}\in\operatorname{Aff}(\Lambda_g,\mathbf F_2)
\]

be the physical four-challenge word of one identity-return full-rank overlap region. By the physical `A3` chain-map theorem,

\[
B_{\mathrm{phys}}(\lambda)
=
\lambda(C_{\mathrm{phys}})
\]

for one physical translation vector

\[
C_{\mathrm{phys}}\in V\cong\mathbf F_2^3.
\]

Assume

\[
|B_{\mathrm{phys}}|=2.
\]

Then

\[
C_{\mathrm{phys}}\notin\{0,g\}.
\]

The affine-plane duality gives a unique nonzero

\[
\delta\in g^\perp
\]

whose parallel pairs are the zero and one fibres of `B_phys`.

For any locked challenge `lambda`, put

\[
A=H_\lambda,
\qquad
A'=H_{\lambda+\delta},
\qquad
Z=H_\delta.
\]

Then

\[
\boxed{A'=A\triangle Z,}
\qquad
\boxed{\partial Z=0.}
\]

The same closed scalar system `Z` compares the two challenge sheets in each of the two parallel pairs selected by the physical translation word.

---

## 2. Component cube and the first escape

Write

\[
Z=Z_1\sqcup\cdots\sqcup Z_m
\]

as the disjoint union of its connected even components. Every partial toggle

\[
A_I=A\triangle\bigtriangleup_{i\in I}Z_i
\]

has the same four-terminal boundary as `A`.

### Theorem 2.1 — pair-changing component

If some `Z_i` changes the terminal pairing or the ordered continuation of the locked paths, then exactly one of:

1. the corresponding support/Kempe switch is root-admissible and gives a physical route/profile escape;
2. its first root-admissibility failure is one zero/equality edge atom;
3. its first failure is one co-root/DDD edge atom;
4. the attempted switch exposes an empty local relation or a small separator.

### Proof

The binary route change is the component-toggle theorem. If the root lift exists, the boundary state leaves the locked route sector. If it does not, the complete inverse-lift table has only equality and disjoint-root/DDD failures; the local relation and category alternatives are the established cap/inverse-dipole cases. ∎

All four outcomes are already progress branches. Hence a prime surviving weight-two region may be assumed **pair-preserving componentwise**.

---

## 3. Laminarity and the four-port interval

If every component `Z_i` is pair-preserving, no two attachment pairs interlace on the two locked terminal paths. Otherwise toggling one component reconnects the terminal ends crosswise.

Thus the attachment intervals form a laminar family. Choose one minimal active interval `R`.

At the binary route level, `R` has at most four ordered route ports. Its external side-root attachments are the only potentially unbounded datum.

Three cases occur.

1. **Crossing signature:** an outside component violates the common interval order. This returns to Theorem 2.1.
2. **Split signature:** the side incidence factors through an edge cut of size at most four.
3. **Separated/noncrossing signature:** the side network is confined to the interval and admits the Tait/matching decomposition below.

### Theorem 3.1 — split intervals are not prime

In a vertex-minimal counterexample, the split-signature case is discharged by cyclic three-/four-cut gluing or is a bounded acyclic appendage.

### Proof

Cyclic three-cuts glue by the cubic local boundary law. Cyclic four-cuts have intersecting physical profiles because every abstract disjoint cap-forced mismatch kernel is Type T or Type H and both are physically impossible. Hence a vertex-minimal counterexample is cyclically five-edge-connected. A cut shore without a cycle is a bounded acyclic appendage. ∎

---

## 4. Matching-plus-Tait decomposition

Inside a separated pair-preserving interval, the root-labelled side network has exactly the established two sectors.

### Complementary Tait sector

Vertices whose blocked side root is complementary to the active shift form properly three-edge-coloured Tait multipoles. Every connected higher-port component has a coloured one-dipole and enters the universal four-port Tait peeling theorem.

### Private-shift matching sector

Vertices whose side edge is the private shift root form maximal shift-matching bands. Each band has one matching colour and two alternating route colours. Every higher-port band has a route-Tait one-dipole.

Closed bands give a global three-edge-colouring; two-port bands glue; higher-port bands peel.

### Theorem 4.1 — strict side-network coordinate

Let

\[
N_T(R)
\]

be the number of vertices in complementary Tait components and

\[
N_M(R)
\]

be the number in shift-matching bands. Every successful nonseparating peel lowers

\[
\boxed{N_T(R)+N_M(R)}
\]

by two.

If a peel fails to remain in the bridgeless cubic category, it exposes a cyclic three-cut, a bounded appendage, a loop/parallel degeneration, or a low-port interface.

---

## 5. Complete inverse-expansion alphabet

After cancelling one Tait or route-Tait dipole, let the two reconnected edges in an arbitrary root-valued cover of the smaller graph have values

\[
p,q\in R_5.
\]

Reinsertion forces the central value

\[
r=p+q.
\]

Exactly one of:

1. `p,q` are distinct and intersecting: `r` is a root and expansion succeeds;
2. `p=q`: `r=0`, one equality atom;
3. `p,q` are disjoint: `r` is one co-root, one DDD atom.

No fourth root-lifting state occurs.

### Theorem 5.1 — shared-interval bookkeeping

Several Tait or matching bands may lie in the same four-port interval, but they need no simultaneous replacement. Choose one available dipole and proceed sequentially.

- A successful inverse root lift continues with strictly smaller `N_T+N_M`.
- An equality or DDD first failure is localized to one edge atom and is consumed by the established horizontal rescue/full-channel/contextual-transfer programme.
- A route change leaves the locked profile.
- A category failure exits through a proved cut or bounded degeneration.

Thus sharing one outer interval cannot create an additional composition state or a cyclic dependence among peeled bands.

### Proof

The graph reduction is one dipole at a time, so minimality is invoked only on the immediately smaller closed cubic graph. The inverse-expansion table localises every failure before a second band is reinserted. Equality/DDD transfer is well founded under its corrected target-order and same-order track analysis. Therefore no simultaneous enclosure hypothesis is required. ∎

---

## 6. Bounded residual cells

After maximal peeling, the interval contains only the finite residual list:

- one root dipole/cap;
- one Type-T square/backtrack cell;
- one zero/equality unit;
- one co-root/DDD unit;
- one low-port or cut interface;
- or a profile-changing route.

Their consumers are:

1. **Type T:** physical disjoint-support route invariance forces immediate profile escape;
2. **Type H/DDD triangle:** the same commutation law forces profile escape;
3. **equality:** horizontal rescue or the equality contextual-transfer theorem;
4. **DDD:** horizontal rescue, oriented-lock reduction, or DDD contextual transfer;
5. **cut/low port:** two-/three-/four-cut gluing or bounded completion;
6. **root cap:** direct root expansion.

Hence no bounded residual reopens an unbounded weight-two branch.

---

## 7. Main theorem

### Theorem 7.1 — weight-two physical consumption

Let a prime locked rank-three physical region have nonconstant affine challenge word of weight two. Then it enters one of:

\[
\boxed{
\begin{array}{l}
\text{physical route/profile escape},\\
\text{strict graph-vertex descent},\\
\text{cyclic cut gluing or bounded degeneration},\\
\text{one equality/DDD atom consumed by contextual transfer},\\
\text{global three-colour solution}.
\end{array}}
\]

It cannot remain an unbounded dual-rank-three hyperbolic norm carrier.

### Well-founded measure

A compatible local measure is

\[
\boxed{
\bigl(
|V(G)|,
N_T(R)+N_M(R),
\mathcal D_{\mathrm{eq/DDD}}
\bigr),}
\]

with the multiset extension over cut shores. Here `D_(eq/DDD)` is the established contextual-transfer ordering. Every nonexit move lowers one coordinate without increasing an earlier one.

---

## 8. Trust boundary

### Exact here

- exact physical selection of `delta` by a weight-two `A3` translation word;
- componentwise toggle cube;
- pair-change/laminar dichotomy;
- elimination of split signatures by established three-/four-cut gluing;
- matching-plus-Tait decomposition of a separated interval;
- strict `N_T+N_M` peeling;
- complete root/equality/DDD inverse-expansion alphabet;
- sequential consumption of several bands sharing one interval;
- disposition of every bounded residual cell;
- well-founded weight-two source descent.

### Still open

- zero physical translation class;
- constant-one/global-complement class;
- odd-curvature torsor composition;
- integration of the physical class theorem with the dual-rank-three hyperbolic norm carrier;
- reverse global proof-DAG audit and final theorem packaging;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication;
- the global five-support theorem.
