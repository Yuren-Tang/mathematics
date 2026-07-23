# Four-terminal matching closures need only two- and three-cut reduction

## Research Lead structural compression v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `a35fc9c6705180401a6093972a53595479c1363f`.

**Correctly sharpens:** `ARBITRARY_EDGE_THREE_RECONNECTION_CATEGORY_V1.md`.

**Purpose:** isolate the elementary four-terminal partition lemma behind all three reconnection closures and determine the weakest global reductions actually required. The result removes cyclic four-cut gluing, Type T, and Type H from the controlling five-CDC proof spine.

**Status:** exact authorial graph-theoretic sharpening. No root-flow or profile theorem is used. PDL must independently reconstruct the endpoint-coincidence cases and the low-port shore classification.

---

## 1. Setup

Let `G` be a finite connected loopless bridgeless cubic multigraph and let

\[
uv\in E(G).
\]

Delete `u,v` and all incident edges. Retain the four exposed terminal incidences

\[
a,b\mid c,d,
\]

where `a,b` came from `u` and `c,d` came from `v`.

Let

\[
H=G-\{u,v\}.
\]

For each perfect matching `M` of the four terminal incidences, form

\[
G_M=H\cup M
\]

by joining the two pairs with two new edges.

There are exactly three such closures.

---

## 2. Exterior connectedness uses only the two-cut reduction

Every connected component of `H` contains at least one terminal incidence because `G` is connected.

It cannot contain exactly one terminal incidence: the corresponding old edge to `u` or `v` would be a bridge of `G`.

Since there are four terminal incidences in total, if `H` is disconnected it has exactly two components and each contains exactly two terminals.

Each component is a nonempty cubic shore with two boundary semiedges. If it were acyclic, the cubic shore identity

\[
3n=2(n-1)+2
\]

would give

\[
n=0,
\]

impossible. Thus both components contain cycles.

### Theorem 2.1 — exterior connectedness criterion

If `G` has no cyclic two-edge cut, then

\[
\boxed{H\text{ is connected}.}
\]

No four-cut hypothesis is involved.

---

## 3. Endpoint coincidences use only two-/three-port bounded reductions

A matching closure contains a loop exactly when two exposed terminal incidences have the same exterior endpoint and are paired together.

### Same-side coincidence

If the two coincident incidences both came from `u` or both came from `v`, the original graph contains a parallel two-port neighbourhood. The two deleted-side edges form the internal parallel pair of a two-port shore. This is either:

- a cyclic two-cut branch; or
- the explicit bounded parallel/theta degeneration.

### Opposite-side coincidence

If one incidence came from `u` and the other from `v`, their common exterior endpoint together with `u,v` forms a triangle. Its outgoing boundary has size three. This is either:

- a cyclic three-cut branch; or
- the explicit bounded triangle/`K_4` degeneration.

More extensive coincidences reduce to the same parallel, triangle, theta, or bridge bases.

### Theorem 3.1 — distinct terminals in the reduced branch

After cyclic two-/three-cut reduction and the explicit bounded parallel/triangle bases, the four terminal incidences have distinct exterior endpoints. Hence every matching closure is loopless.

Again no four-cut hypothesis is required.

---

## 4. The abstract matching-closure bridge lemma

Let `H` be any connected graph with four distinguished terminal incidences having distinct endpoints. Let

\[
M=P_1\mid P_2
\]

be one perfect matching of the terminals, and add the two matching edges.

### Lemma 4.1 — new edges are nonbridges

Each new matching edge joins two vertices already connected by a path in `H`. Therefore it lies on a cycle and is not a bridge.

### Lemma 4.2 — old bridge partition

Suppose an old edge

\[
h\in E(H)
\]

is a bridge of `H union M`. Since `H` is connected,

\[
H-h=A\sqcup B
\]

has exactly two connected shores.

No matching edge crosses between `A` and `B`; otherwise the closure would remain connected after deleting `h`. Therefore every matching block `P_1,P_2` lies wholly in one shore.

If both matching blocks lie in the same shore, the other shore contains no terminal and meets the original graph `G` only through `h`. Then `h` is a bridge of `G`, impossible.

Hence one matching block lies in `A` and the other lies in `B`.

### Corollary 4.3 — old bridge gives a three-cut

One shore, say `A`, has exactly two terminal incidences. In the original graph its boundary consists of:

1. the edge `h`;
2. the two old attachment edges from those terminal incidences to `u` and/or `v`.

Thus

\[
\boxed{|\delta_G(A)|=3.}
\]

If `A` and its complement both contain cycles, this is a cyclic three-edge cut. If one shore is acyclic, the cubic shore identity gives the explicit one-vertex three-port gadget, producing the local parallel/triangle bounded case.

### Theorem 4.4 — matching-closure principle

If `G` is bridgeless and has no unresolved cyclic three-cut or bounded three-port degeneration, then no old edge of `H` is a bridge in `H union M`.

Together with Lemma 4.1, every matching closure is bridgeless.

---

## 5. Simultaneous three-reconnection theorem, sharpened

### Theorem 5.1

Let `G` be a finite connected loopless bridgeless cubic multigraph. Let `uv` be any edge. Assume only that:

1. `G` has no cyclic two-edge cut;
2. `G` has no cyclic three-edge cut;
3. the explicit parallel, theta, triangle, `K_4`, and acyclic low-port bases have been removed.

Then all three perfect-matching closures of

\[
G-\{u,v\}
\]

are connected loopless bridgeless cubic multigraphs with

\[
\boxed{|V(G_M)|=|V(G)|-2.}
\]

### Proof

- Theorem 2.1 gives connected `H`.
- Theorem 3.1 gives distinct terminal endpoints and hence loopless closures.
- Adding a matching preserves connectedness and cubicity.
- Lemma 4.1 excludes bridges among new edges.
- Theorem 4.4 excludes bridges among old edges.
- Two vertices were deleted and none added. ∎

---

## 6. Consequence for the minimal-counterexample proof

Choose a vertex-minimal connected bridgeless cubic counterexample after only the two-/three-cut and bounded-base reductions.

For every edge `uv`, Theorem 5.1 supplies all three smaller reconnection closures. Minimality gives a root-valued flow on each. Restriction to the complementary four-pole `P` yields

\[
\boxed{
\Sigma(P)\cap J_r\ne\varnothing
\qquad(r=0,1,2).
}
\]

The ten-state boundary theorem and the repaired full-channel theorem then restore the original cap.

No cyclic four-cut reduction is used in this implication.

---

## 7. Architectural deletion

The controlling cubic proof can therefore be ordered as:

1. bounded bases;
2. cyclic two-cut gluing;
3. cyclic three-cut gluing;
4. Theorem 5.1 for all three reconnections;
5. ten-state fixed-route rigidity;
6. singular contextual confluence;
7. original cap restoration.

The following results remain correct independent strengthenings but are not logically required by this route:

- cyclic four-cut cap forcing;
- disjoint shore-profile classification;
- Type T physical commutation elimination;
- Type H BBD/DDD physical commutation elimination;
- the conclusion that a minimal counterexample is cyclically five-edge-connected.

They should be removed from the controlling PDL theorem DAG unless a later reconstruction discovers an actual hidden dependence.

---

## 8. Why four-cuts looked relevant earlier

Earlier category packets grouped every local failure under a broad alternative:

\[
\text{cut of size at most four or bounded degeneration}.
\]

That grouping was safe but not sharp.

For the specific operation of deleting two adjacent cubic vertices and adding a terminal matching:

- disconnected exterior means a `2+2` terminal component partition and hence a two-cut;
- an old bridge means a matching-block `2+2` shore partition and hence a three-cut;
- a loop means a repeated terminal endpoint and hence a parallel two-port or triangle three-port gadget.

There is no mechanism producing an essential four-cut.

---

## 9. PDL reconstruction obligations

PDL should prove the sharpened Package B in this order:

1. cubic shore identity for two- and three-port acyclic shores;
2. disconnected exterior implies cyclic two-cut;
3. terminal coincidences imply the explicit two-/three-port bases;
4. the abstract matching-closure bridge lemma;
5. simultaneous application to all three matchings;
6. restriction of the three smaller root flows to the three profile sets `J_r`.

This replaces the previous dependence on the complete four-cut mismatch programme.

---

## 10. Trust boundary

### Exact authorial claim here

- the all-three reconnection theorem needs only two-/three-cut and bounded-base reduction;
- every old bridge in a matching closure yields a three-cut, independently of which matching is used;
- cyclic four-cut gluing and Type T/H elimination are noncontrolling for the repaired global route.

### Not added here

- independent verification of endpoint coincidences;
- PDL reconstruction;
- any change to the mathematical validity of the four-cut results themselves;
- canonical acceptance, Lean verification, manuscript integration, release, peer review, or publication.
