# Kempe blocker sides form one matching plus a rank-two Tait network

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `55f232b0abf7854d9c7c6cb01d73e796e9d3f67a`  
**Parents:**

- `projects/affine-cdc/research/MINIMAL_RIGID_CYCLE_KEMPE_INTERVAL_EMISSION_V1.md`;
- `projects/affine-cdc/research/CONNECTED_CYCLE_FLEXIBLE_SWITCH_NORMAL_FORM_V1.md`;
- `projects/affine-cdc/five-support/root-flow-lifting.md`;
- `projects/affine-cdc/five-support/cuts-four-poles-and-routing.md`.

**Status:** exact local and component decomposition for the side semantics of an emitted ordinary Kempe system. For a root shift `s=ab`, the unsafe side graph consists of isolated `s`-edges between Kempe vertices together with multipoles carrying the three roots of the complementary `K3`, hence a genuine rank-two/Tait flow. The remaining strict-descent problem may therefore be posed on matching-plus-Tait side networks rather than arbitrary five-support signatures.  
**Not implied:** boundedness of a Tait multipole, existence of a separator for every attachment pattern, composition-safe contraction, a decreasing global complexity, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Safe and blocked roots for one root shift

Fix

\[
s=ab\in R_5,
\qquad
W=[5]\setminus\{a,b\}.
\]

Let

\[
H_s=\{e:\lambda(e)+s\in R_5\}
=F_a\triangle F_b
\]

be the safe Kempe subgraph of a root-valued flow

\[
\lambda:E(G)\to R_5.
\]

Its blocked root alphabet is

\[
B(s)=\{s\}\sqcup E(K_W).
\]

Write

\[
D_s=G-E(H_s)
\]

for the spanning blocked-edge subgraph.

---

## 2. Exact local triangle classification

Every cubic source vertex carries one root triangle in `K5`.

### Theorem 2.1 — safe-degree dichotomy

At every cubic vertex,

\[
\boxed{\deg_{H_s}(v)\in\{0,2\}.}
\]

More precisely, exactly one of the following occurs.

### Type A — complementary Tait vertex

The local root triangle is the triangle on `W`:

\[
uv,\ vw,\ wu
\qquad(\{u,v,w\}=W).
\]

All three incident edges are blocked, so

\[
\deg_{H_s}(v)=0,
\qquad
\deg_{D_s}(v)=3.
\]

### Type B — same-shore Kempe turn

For distinct `u,v in W`, the local triangle is

\[
au,\ av,\ uv
\]

or

\[
bu,\ bv,\ uv.
\]

The first two roots are safe and the side root `uv` is blocked. Hence

\[
\deg_{H_s}(v)=2,
\qquad
\deg_{D_s}(v)=1.
\]

### Type C — cross-shore Kempe turn

For `u in W`, the local triangle is

\[
au,\ bu,\ ab.
\]

The first two roots are safe and the side root is `s=ab`. Again

\[
\deg_{H_s}(v)=2,
\qquad
\deg_{D_s}(v)=1.
\]

### Proof

Every root triangle in `K5` is the edge set of a three-vertex subset of `[5]`. Its intersection with `{a,b}` has size `0`, `1`, or `2`, giving exactly Types A, B, and C. The root-shift criterion says that a root is safe precisely when it contains exactly one of `a,b`. The displayed degree counts follow. ∎

### Corollary 2.2

`H_s` is an even subgraph and therefore a disjoint union of Kempe cycles in a closed cubic source graph. Every vertex on one Kempe cycle has exactly one blocked side edge.

---

## 3. The blocked side graph

The local theorem gives

\[
\deg_{D_s}(v)\in\{1,3\}.
\]

Degree-one vertices of `D_s` are exactly the vertices lying on `H_s`. Degree-three vertices are exactly complementary Tait vertices carrying the three roots of `E(K_W)`.

### Theorem 3.1 — isolated matching direction

Every edge labelled

\[
s=ab
\]

is an isolated one-edge component of `D_s` joining two degree-one vertices of `D_s`.

Equivalently, every `s`-edge joins two vertices lying on Kempe cycles of `H_s`.

### Proof

No root triangle containing `s=ab` can be the complementary triangle on `W`. The only local triangle containing `s` is

\[
ab,\ au,\ bu
\]

for some `u in W`, which is Type C. Thus both endpoints of an `s`-edge have blocked degree one. No other blocked edge is incident with either endpoint. ∎

### Corollary 3.2

The `s`-labelled blocked edges form a matching on the vertices of the Kempe system `H_s`.

---

## 4. Complementary components are Tait multipoles

Delete the isolated `s`-edges from `D_s` and write

\[
T_s=D_s-\lambda^{-1}(s).
\]

Every edge of `T_s` has one of the three labels

\[
E(K_W)=\{uv,vw,wu\}.
\]

### Theorem 4.1 — rank-two side-network theorem

Every connected component `T` of `T_s` is a properly three-edge-coloured multipole with colour set `E(K_W)`:

1. every internal cubic vertex of `T` is incident with the three distinct colours;
2. every boundary vertex has degree one in `T` and lies on a Kempe cycle of `H_s`;
3. the edge labels satisfy the nowhere-zero `F_2^2` flow law on `T`.

### Proof

Every degree-three vertex of `D_s` is Type A and therefore carries exactly the three roots of the complementary `K3`. Every degree-one vertex is a Type B Kempe vertex whose unique blocked edge has one complementary root label. The three complementary roots are the three nonzero elements of their binary span and sum to zero, giving the Tait flow law. ∎

### Corollary 4.2 — boundary parity

Let the three complementary roots be `r_1,r_2,r_3`. For every component `T`, the three boundary counts have the same parity:

\[
\boxed{
|\partial_{r_1}T|
\equiv
|\partial_{r_2}T|
\equiv
|\partial_{r_3}T|
\pmod2.
}
\]

### Proof

Sum the `F_2^2` flow equations over all internal vertices. Internal edges cancel, so the sum of the boundary colours is zero. Since `r_1+r_2+r_3=0` is the unique relation among the three nonzero colours, their multiplicities have equal parity. ∎

### Corollary 4.3 — smallest interfaces

A nonempty Tait component cannot have exactly one boundary attachment. Its smallest possible boundary signatures are:

- two boundary edges of the same complementary root colour;
- three boundary edges, one of each colour.

These are respectively two-pole and three-pole interfaces. Larger components retain a rank-two boundary word rather than arbitrary five-support side data.

---

## 5. Incidence quotient

Contract every Kempe cycle component of `H_s` to a black vertex. Contract the internal cubic vertices and edges of every Tait component of `T_s` to a white multipole vertex, retaining one incidence for each boundary attachment. Retain every isolated `s`-edge as an edge between black vertices.

The resulting object is a finite matching-plus-hypergraph incidence quotient

\[
\mathcal I_s.
\]

### Theorem 5.1 — exact recovery interface

The original source graph is obtained from `mathcal I_s` by expanding:

1. each black vertex to one support-pair Kempe cycle;
2. each white vertex to one rank-two Tait multipole;
3. each black-black edge to one `s`-labelled matching edge.

No other local coefficient type occurs.

### Interpretation

For an emitted Kempe interval, every external side attachment factors through exactly one of:

- a single `s`-matching edge;
- a rank-two Tait component with parity-controlled boundary.

Thus the side-signature problem has dropped from an arbitrary root-fibre local system to a matching-plus-four-flow composition problem.

---

## 6. Consequences for a minimal laminar interval

Let `R` be a pair-preserving minimal interval emitted from a rigid cycle by `MINIMAL_RIGID_CYCLE_KEMPE_INTERVAL_EMISSION_V1.md`.

All side attachments of its Kempe boundary interval are carried by the blocked network `D_s`.

### Theorem 6.1 — low-rank side-signature reduction

The external side signature of `R` is generated by:

1. incidences of isolated `s`-matching edges;
2. boundary incidences of complementary Tait multipoles.

In particular, arbitrary five-root enriched co-root transport cannot occur at this stage.

### Corollary 6.2 — revised strict-descent alternatives

To close strict descent it is enough to prove the following matching-plus-Tait composition lemma.

For a support-minimal pair-preserving interval `R`, one of:

1. an `s`-matching edge crosses the laminar order and gives route escape;
2. a Tait component crosses the order and one of its bicoloured paths gives route escape;
3. a Tait component attaches through two or three boundary edges and yields a two-cut/three-cut or a bounded cap;
4. the boundary attachments split into a four-pole separator;
5. all components are serially nested and a minimal one admits contraction lowering the side-signature measure.

The coefficient alphabet supplies no sixth branch.

---

## 7. Why coefficient label count is not a descent measure

For each of the four minimal rigid orbits, switching all edges which are safe for the private root shift sends the certificate to another certificate in the same `S5` orbit:

- a four-star renews as a four-star;
- `K3 sqcup K2` renews as `K3 sqcup K2`;
- a bull renews as a bull;
- a five-cycle renews as a five-cycle.

Hence neither the number of distinct root labels nor the rigid-orbit type decreases under the natural Kempe renewal.

The strict measure must therefore record source-side data such as

\[
\mathcal D(R)
=
\bigl(
 |\Sigma(R)|,
 N_{\mathrm{frame}}(R),
 |V(R)|,
 \beta(R),
 D(R)
\bigr),
\]

or a refinement on the incidence quotient `mathcal I_s`.

---

## 8. Trust boundary

### Exact here

- the complete local safe/blocked triangle classification;
- the decomposition of blocked labels into one isolated root direction and one complementary root triangle;
- matching structure of the `s`-edges;
- rank-two/Tait structure of every other blocked component;
- parity law for its boundary colours;
- factorisation of all emitted side semantics through the matching-plus-Tait incidence quotient;
- failure of coefficient label count and rigid-orbit type as strict descent measures.

### Still open

- a separator theorem for every nonserial incidence quotient;
- contraction of a serially nested Tait multipole preserving the four-port root boundary;
- conversion of boundary parity into a composition-safe two-cut, three-cut, or four-cut in every case;
- a strict well-founded measure on the incidence quotient;
- horizontal/global induction and the global five-support theorem.
