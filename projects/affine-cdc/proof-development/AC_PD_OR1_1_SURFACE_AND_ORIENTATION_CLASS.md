# AC-PD-OR1.1 — cycle-face reconstruction and the fixed-lift orientation class

**Proof-development state:** `COMPLETE-DRAFT / AUTHORIAL-RECONSTRUCTION`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Priority authority:** research-workbench issue #37 comment `5049496439`  
**Audit inputs, not accepted mathematics:** issue #49 comments `5048974400`, `5049236646`  
**Controlling integrated mathematics:** `curation/affine-cdc-programme-a-b1-b8-unified-v1@ec765cd03271abd3588ec36faec3d53d0f8aa03b`  
**Checked reconstruction source:** `Yuren-Tang/affine-cdc:main@ebd7098a7a8b824e8c0a511d3c71f61705672aa8`  
**Scope:** finite loopless cubic multigraphs, possibly disconnected, with a nowhere-zero `F_2^3`-flow and one compatible labelled affine/root lift

## 0. Status and source discipline

The issue-#49 return is used only as a list of claims to verify. The proofs below are reconstructed from:

1. the integrated root-lift/surface theorem;
2. the exact Lean dart objects `Msupp`, `partnerD`, `rho`, and `rhoInv`;
3. elementary signed-rotation and binary cochain arguments.

The graph-level Lean theorem `Port.cubic_flow_cdc` is **not** a reconstruction source for orientation: it explicitly discards the returned rotation and invokes an undirected generic decomposition of even supports.

## 1. Fixed root-lift data

Let `G=(V,E)` be a finite loopless cubic multigraph, not necessarily connected, and let

\[
f:E\longrightarrow \Gamma\setminus\{0\},
\qquad \Gamma=\mathbf F_2^3,
\]

be a nowhere-zero flow. A compatible labelled root lift is a map

\[
g:E\longrightarrow \binom I2,
\qquad I=\Gamma,
\]

such that the sum/difference of the two root endpoints is `f(e)`, and at each cubic vertex the three incident roots are the three edges of one triangle on three distinct indices.

For `a in I`, put

\[
F_a:=\{e\in E:a\in g(e)\}.
\]

The following occurrence conventions are structural, not cosmetic.

- An empty `F_a` remains an indexed empty support but contributes no face.
- Distinct connected components of one `F_a` are distinct face occurrences.
- Equal edge supports at different indices remain distinct indexed occurrences.
- No component or index is flattened before the surface is constructed.

## 2. Exact dart reconstruction

Let `Delta` be the dart set and let `sigma` reverse an edge. For a dart `d` in the `a`-support, Lean defines

\[
\operatorname{partner}_a(d)
\]

as the unique other `a`-support dart at the same cubic vertex. It proves:

1. `partner_a(d)` has the same vertex as `d`;
2. it lies in the same support;
3. it differs from `d`;
4. `partner_a` is an involution on that support;
5. every other same-vertex support dart is `d` or `partner_a(d)`.

Define

\[
\rho_a=\operatorname{partner}_a\circ\sigma,
\qquad
\rho_a^{-1}=\sigma\circ\operatorname{partner}_a.
\]

The checked source proves that these are inverse permutations on the `a`-support. A `rho_a`-orbit traverses one support component in one direction; applying `sigma` gives the reverse traversal and conjugates `rho_a` to its inverse. Thus one unoriented face occurrence is the pair of opposite directed dart orbits, not merely the underlying edge set.

The theorem `exists_indexed_dart_cover` retains, simultaneously:

- the index `a`;
- sigma-closure;
- exact two-support membership of every dart;
- the unique partner at each vertex;
- the explicit mutually inverse rotations.

These data are sufficient for the following reconstruction.

## 3. Surface reconstruction theorem

At a vertex whose local roots are `ab`, `bc`, and `ca`, take a vertex disc with three corners labelled `a,b,c`. The `a`-corner is the sector between the two darts paired by `partner_a`, and similarly for `b,c`. The three named sectors determine the cyclic order of the incident edge arcs up to reversal.

For every edge with root `{a,b}`, attach an edge band whose two long sides carry the face labels `a` and `b`, using the endpoint corner incidences determined above. The boundary circuits of the resulting ribbon graph are exactly the directed `rho_a`-orbits. Cap every nonempty boundary component by its indexed face disc.

### Theorem 3.1 — retained-data reconstruction

The construction produces a closed cellular surface `S_g`, componentwise over `G`, with the following properties.

1. Its embedded one-skeleton is `G`.
2. Its face occurrences are exactly the connected components of the indexed supports `F_a`.
3. Its directed face boundaries are exactly the `rho_a`-orbits.
4. Every source edge is incident with exactly the two face occurrences indexed by the two elements of `g(e)`.
5. Reversing the local cyclic order at any vertex changes only a choice of signed-rotation representative; it does not change the underlying signed-rotation class.

### Proof

The unique-partner theorem makes every support vertex degree zero or two, while sigma-closure identifies the two endpoint views of each support edge. Therefore `rho_a` follows the boundary of the `a`-side of successive edge bands and its orbits are precisely the boundary components. Exact two-support membership gives exactly two long sides per edge. At a cubic vertex the three local support sectors form a circular link, so the ribbon complex is a surface rather than a singular two-complex. Capping all boundary components gives a closed cellular surface. The integrated root-lift/surface theorem identifies this object with the Programme-B cycle-face surface. `square`

## 4. The edge twist word

Choose one orientation on every vertex disc. For a nonloop edge `e=uv`, define

\[
w_e(g)=
\begin{cases}
0,&\text{if the two oriented vertex-disc attaching intervals extend over the edge band},\\
1,&\text{if one half-twist is required.}
\end{cases}
\]

This definition uses the actual band attachment and does not require an arbitrary ordering of the two root labels.

Put

\[
C^0(G):=\mathbf F_2^V,
\qquad
C^1(G):=\mathbf F_2^E,
\qquad
(\delta x)_{uv}:=x_u+x_v.
\]

Let

\[
\operatorname{Cut}(G):=\operatorname{im}\delta.
\]

For disconnected `G`, all spaces are direct sums over edge-bearing components and

\[
\ker\delta=\mathbf F_2^{\pi_0(G)}.
\]

Reversing the chosen orientation of the vertex disc at `v` toggles exactly the twist bits of the incident nonloop edges. Hence a change encoded by `x in C^0(G)` sends

\[
w(g)\longmapsto w(g)+\delta x.
\]

Therefore the intrinsic fixed-lift class is

\[
\boxed{
\omega(g):=[w(g)]\in C^1(G)/\operatorname{Cut}(G).
}
\]

It is the first Stiefel-Whitney class of `S_g` evaluated on the graph one-skeleton.

## 5. Fixed-lift orientation-obstruction theorem

Write

\[
Z_1(G):=\operatorname{Cut}(G)^\perp
\]

for the binary cycle space under the edge dot product.

### Theorem 5.1

For one fixed compatible lift `g`, the following are equivalent.

1. `S_g` is orientable.
2. Vertex-disc orientations can be chosen so that every edge band is untwisted.
3. `w(g) in Cut(G)`.
4. `omega(g)=0` in `C^1(G)/Cut(G)`.
5. Every source cycle has zero twist holonomy:
   \[
   \langle w(g),z\rangle=0
   \quad\text{for all }z\in Z_1(G).
   \]
6. The **retained indexed face occurrences** can be oriented so that the two occurrences of every source edge traverse it in opposite directions.

### Proof

A vertex-disc reversal is exactly a signed-rotation switch and adds one coboundary. Thus an all-untwisted representative exists exactly when `w(g)` is a coboundary, proving `1`--`4`. Binary cut-cycle orthogonality proves `3 iff 5`.

If the surface is oriented, orient each face by the boundary orientation induced from the surface; the two incident face boundaries run oppositely along every edge band. Conversely, suppose the retained face occurrences have orientations opposite on every common edge. Orient each face disc accordingly. Across every edge band the two boundary orientations then extend to one band orientation. At a cubic vertex the three face corners form a circular link, so the three adjacent oriented bands induce one orientation of the vertex disc. Hence the orientations extend over all cells and `S_g` is orientable. `square`

### Corollary 5.2 — exact directed-CDC interpretation

In this cubic compatible-root setting, orientability of `S_g` is equivalent to an oriented/directed cycle double cover in the sense that each undirected source edge is traversed once in each direction by its two retained face occurrences.

This is stronger than independently assigning an arbitrary direction to every circuit of an undirected CDC.

## 6. Boundary cases and conventions

1. **Disconnected graphs.** No new quotient is needed; the theorem is componentwise.
2. **Repeated supports.** They cause no change provided their occurrences remain distinct.
3. **Empty supports.** They contribute no face and no orientation condition.
4. **Loops.** The present theorem is loopless. In a signed-rotation extension with loops, a vertex-disc reversal acts twice on a loop attachment, so the loop coordinate is not changed by `delta`; a twisted loop is an immutable coordinate. Loop reinsertion is treated separately in OR1.3.
5. **Preassigned source orientation.** A reference orientation merely records which of the two opposite face traversals agrees with the reference. It creates no additional obstruction.
6. **Generic decomposition.** An arbitrary circuit decomposition of the supports need not reproduce the retained face occurrences and therefore cannot be substituted into Theorem 5.1 without extra data.

## 7. Exact source comparison

The checked Lean source establishes the dart-level reconstruction ingredients but does not define `w`, `omega`, or orientability. The integrated surface chapter establishes the root-lift/surface equivalence but does not state the signed-rotation obstruction. Theorem 5.1 is therefore a new authorial proof-development unit, not a restatement that was already accepted merely because issue #49 proposed it.
