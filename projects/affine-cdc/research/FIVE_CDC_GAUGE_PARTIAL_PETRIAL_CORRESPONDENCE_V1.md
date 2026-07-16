# Gauge words as code-filtered partial Petrials

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level topological bridge; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_COLORED_SURFACE_DUAL_HALFCUBE_V1.md`, `FIVE_CDC_GAUGE_AS_PIECEWISE_ROOT_TRANSLATION_V1.md`, canonical `topology/README.md`

## 1. Purpose

A root lift determines a cycle-face embedding of the cubic source graph. The active canonical topology inventory records that an older exact gauge–embedding and code-filtered partial-Petrial programme existed, but its source bodies are absent.

The present packet derives the basic correspondence directly from the current root and gauge definitions:

\[
\boxed{
\text{the binary gauge word }\lambda
\text{ records exactly which source edges receive a face-side swap.}
}
\]

Equivalently, every compatible gauge move changes the cycle-face embedding by a partial Petrial on the support of `\lambda`; the admissible gauge code is precisely the code of partial edge-twist sets available while the projected Fano flow is held fixed.

No absent historical theorem is presumed or reconstructed beyond what is proved here.

## 2. Local face sides of a root edge

Let

\[
g:E(G)\to E(K_8)
\]

be a root lift of a nowhere-zero Fano flow

\[
f:E(G)\to\Gamma=\mathbf F_2^3.
\]

For a source edge `e=uv`, write

\[
g(e)=\{s,s+h\},\qquad h=f(e)\ne0.
\]

In the cycle-face embedding `S_g`, the edge `e` has two incident face sides, one belonging to the support component with index `s` and one belonging to the support component with index `s+h`.

At either endpoint, the local target triangle contains these two support indices. The base embedding glues equal support labels through the source edge.

## 3. Gauge translations and the edge bit

Let

\[
k:V(G)\to\Gamma
\]

be an admissible translation field. Thus for every edge `e=uv`,

\[
k_u+k_v\in\langle h\rangle,
\]

so there is a unique bit

\[
\lambda_e\in\mathbf F_2
\]

such that

\[
\boxed{k_u+k_v=\lambda_e h.}
\]

The translated root pair at endpoint `u` is

\[
\{s+k_u,s+h+k_u\}.
\]

At endpoint `v` it is

\[
\{s+k_v,s+h+k_v\}.
\]

These unordered pairs agree by admissibility.

### Theorem 3.1 — local face-side swap rule

Across the source edge `e`:

1. if `\lambda_e=0`, the two translated face labels match without interchange;
2. if `\lambda_e=1`, the two translated face labels match after interchanging the two sides.

#### Proof

If `\lambda_e=0`, then `k_v=k_u`, so

\[
s+k_u=s+k_v,
\qquad
s+h+k_u=s+h+k_v.
\]

The two sides glue label to equal label.

If `\lambda_e=1`, then `k_v=k_u+h`. Hence

\[
s+k_u=s+h+k_v,
\qquad
s+h+k_u=s+k_v.
\]

The two labels are exchanged across the edge. ∎

Thus the edge bit does not merely say that a root label changed. It records the topological gluing choice of the two face sides.

## 4. Partial Petrial theorem

For a cycle-face embedding `S`, define an **edge twist** at `e` to mean: keep the two endpoint neighbourhoods and the edge band, but interchange the two face-side identifications across that band. For a set `P\subseteq E(G)`, perform this operation at every edge in `P`. This is the partial Petrial operation on `P` in ribbon-graph language.

### Theorem 4.1 — gauge–Petrial correspondence

Let `g^k` be the root lift obtained from `g` by the admissible translation field `k`, and put

\[
P(k):=\{e:\lambda_e=1\}.
\]

Then the cycle-face embedding determined by `g^k` is exactly the partial Petrial of `S_g` on `P(k)`:

\[
\boxed{
S_{g^k}=S_g^{\tau(P(k))}.
}
\]

Here equality means equality of the face-side gluing system on the fixed cubic one-skeleton, up to the global relabeling of support indices induced by adding a constant to `k`.

#### Proof

At every source vertex, translating the local target triangle by `k_v` preserves the three local edge incidences and the disk neighbourhood. The only possible change in tracing support faces occurs when a local face side crosses a source edge.

By Theorem 3.1, an edge with `\lambda_e=0` preserves the original side matching, while an edge with `\lambda_e=1` swaps the two side matchings. Performing these swaps independently on all edges in `P(k)` is precisely the stated partial Petrial. A constant translation has `\lambda=0` and only globally relabels support indices, so it does not change the embedding. ∎

## 5. The gauge code is an embedding-move code

For connected `G`, the admissible fields fit into

\[
0\longrightarrow\Gamma
\longrightarrow H_f^0
\longrightarrow B_f
\longrightarrow0,
\]

where constants form the kernel and `B_f` is the reduced gauge code of edge bits `\lambda`.

Theorem 4.1 gives an intrinsic topological interpretation:

\[
\boxed{
B_f
=
\{\text{partial-Petrial edge sets accessible while }f\text{ is fixed}\}.
}
\]

The code is not the full power set of source edges. Its linear constraints are exactly the compatibility conditions needed for the twisted gluing to carry another root lift projecting to the same Fano flow.

Low-weight gauge circuits therefore have two simultaneous readings:

- harmonic cut quotients in the affine/gauge theory;
- elementary partial-Petrial surgeries in the embedding theory.

For example, the weight-six `2K_3` circuit in the thirty-vertex fixed obstruction is a six-edge partial Petrial. It changes the number of support-cycle faces from eleven to thirteen, and hence changes the Euler characteristic of the associated closed surface from

\[
30-45+11=-4
\]

to

\[
30-45+13=-2.
\]

The projected Fano flow remains fixed throughout.

## 6. Horizontal pivots versus vertical Petrials

The colored-surface model now separates the two operations exactly.

### Support-cycle pivot

A support-cycle pivot recolors one dual vertex. It preserves:

- the cycle-face embedding;
- the uncolored dual triangulation;
- the truth value of `T_g\to\mathscr A_5`.

It changes the old eight-color quotient and the projected Fano flow.

### Gauge move

A gauge move performs a code-filtered partial Petrial. It may change:

- the face decomposition;
- the number of support components;
- the surface Euler characteristic and orientability;
- the uncolored dual triangulation;
- the truth value of `T_g\to\mathscr A_5`.

It preserves the projected Fano flow.

Thus the two directions are genuinely complementary:

\[
\boxed{
\begin{array}{c|c|c}
\text{move}&\text{embedding}&\text{Fano flow}\\
\hline
\text{support pivot}&\text{fixed}&\text{changes}\\
\text{gauge / partial Petrial}&\text{changes}&\text{fixed}
\end{array}
}
\]

## 7. Corrected five-support mechanism

The componentwise criterion depends only on the uncolored dual triangulation:

\[
T_g\to\mathscr A_5.
\]

Consequently, recoloring the old eight support indices on a fixed embedding cannot alter componentwise compressibility. The role of a horizontal cycle switch is indirect: it changes the downstairs flow and therefore changes which code-filtered partial Petrials are available in the new gauge fibre.

The five-support programme should therefore be organized as follows.

1. Start with one AffineCDC cycle-face embedding.
2. Explore its fixed-flow code-filtered partial-Petrial orbit.
3. Test the dual triangulations for homomorphisms to `\mathscr A_5`.
4. If the whole orbit is obstructed, perform a horizontal flow switch to change the admissible Petrial code.
5. Repeat or extract a coherent topological obstruction.

This replaces the earlier picture of two loosely coupled affine motions by a precise coloring-versus-embedding decomposition.

## 8. Current global obstruction

For the thirty-vertex fixed-Fano example, the two available partial-Petrial states are exactly the two reduced gauge lifts. Their dual triangulations contain `K_7` and `K_6`, respectively, so neither maps to `\mathscr A_5`.

After many horizontal cycle switches, the new gauge codes permit additional partial Petrials. The corrected componentwise census in the private workbench shows that these new embedding states are much more successful than the global-index-factorable quotient test suggests.

The next structural target is therefore:

> classify or destroy the minimal uncolored dual-triangulation obstructions to `\mathscr A_5`, beginning with `K_6` cliques, under code-filtered partial Petrials.

This is the topological form of the remaining AffineCDC-to-five-support problem.
