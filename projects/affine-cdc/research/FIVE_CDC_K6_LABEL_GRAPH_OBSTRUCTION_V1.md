# A connected cubic root flow with noncompressible `K_6` label graph

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level counterexample checkpoint; not canonical pending review  
**Parent:** `FIVE_CDC_SOURCE_DEPENDENT_HALFCUBE_COMPRESSION_V1.md`

## 1. Purpose

The source-dependent half-cube theorem gives a flexible sufficient condition:
an AffineCDC root flow

\[
g:E(G)\to E(K_8)
\]

compresses to five supports whenever its used-label graph `J_g` admits a
homomorphism to the distance-two graph `\mathscr A_5`.

This packet shows that the condition is not automatic for every root flow. There
are connected cubic root flows with

\[
J_g=K_6,
\]

and `K_6` does not map to `\mathscr A_5` because the latter has clique number
five.

## 2. The triangle-vertex construction

Let the six target support indices be

\[
[6]=\{0,1,2,3,4,5\}.
\]

The source graph has one vertex

\[
v_T
\]

for every three-element subset `T⊂[6]`. Thus it has

\[
\binom63=20
\]

vertices.

At `v_{\{i,j,k\}}`, place three half-edges labelled by the three edges

\[
ij,\quad ik,\quad jk
\]

of the target triangle on `{i,j,k}`.

For each target edge `ij`, exactly four source vertices contain `{i,j}`. Pair
those four `ij`-half-edges in two pairs. Doing this independently for all fifteen
target edges produces a cubic loopless multigraph, and every resulting source
edge inherits its target label `ij`.

At every source vertex the three incident target roots are

\[
e_i+e_j,\qquad e_i+e_k,\qquad e_j+e_k,
\]

whose sum is zero. Hence the inherited edge labelling is a root-valued flow.
Every one of the fifteen labels of `K_6` occurs twice, so the used-label graph is
exactly `K_6`.

## 3. One explicit connected pairing

For each target edge `ij`, list the four triangle vertices `ijk` in increasing
order of the third element and use one of the three pairings of positions

\[
01|23,\qquad02|13,\qquad03|12.
\]

The following table specifies a connected instance.

| target edge | pairing |
|---|---|
| `01` | `01|23` |
| `02` | `03|12` |
| `03` | `01|23` |
| `04` | `02|13` |
| `05` | `01|23` |
| `12` | `02|13` |
| `13` | `02|13` |
| `14` | `02|13` |
| `15` | `03|12` |
| `23` | `02|13` |
| `24` | `01|23` |
| `25` | `01|23` |
| `34` | `02|13` |
| `35` | `01|23` |
| `45` | `02|13` |

For example, for target edge `01`, the four triangle vertices are

\[
012,013,014,015,
\]

and `01|23` pairs `012` with `013` and `014` with `015`.

Connectivity may be checked from the following nineteen source edges, which form
a spanning tree:

\[
\begin{aligned}
&012-013,\ 012-025,\ 012-124,\ 013-023,\ 013-134,\\
&014-015,\ 014-034,\ 014-134,\ 015-145,\\
&023-024,\ 023-234,\ 024-045,\ 025-125,\\
&034-035,\ 035-135,\ 045-245,\\
&123-125,\ 123-235,\ 134-345.
\end{aligned}
\]

Thus the constructed cubic multigraph is connected. Since it carries a
nowhere-zero binary root flow, it is bridgeless.

## 4. Noncompressibility of the fixed root flow

### Theorem 4.1

The root flow above cannot be compressed to five supports by any
source-dependent cut-continuous relabelling of its used target labels.

#### Proof

Its used-label graph is `K_6`. By the half-cube encoding theorem, such a
compression would give a graph homomorphism

\[
K_6\longrightarrow\mathscr A_5.
\]

A homomorphism sends a clique injectively to a clique. The clique number of
`\mathscr A_5` is five: after translating one clique vertex to zero, the other
vertices are weight-two words whose corresponding two-subsets are pairwise
intersecting, so there are at most four of them. Therefore `K_6` has no such
homomorphism. ∎

The same argument rules out compression through any fixed `K_5` cographic target
while preserving this particular root flow.

## 5. What the counterexample does and does not say

It proves that neither of the following is valid.

1. Every compatible eight-index family can be reduced to five by symmetric
   differences of its supports.
2. Every AffineCDC root flow has a used-label graph mapping to `\mathscr A_5`.

It does **not** give a counterexample to `5-CDC`. The underlying connected cubic
multigraph may admit another root flow, another five-support cover, or a
piecewise/glued target map not factoring through the fixed label graph `K_6`.

## 6. Strategic consequence

The hierarchy of failed universal strategies is now:

1. a fixed Fano flow need not admit a compatible lift omitting three original
   indices;
2. a fixed root flow need not admit any source-dependent global target
   compression to `K_5`;
3. there is no graph-independent target map `K_8→K_5` working for all root flows.

Therefore a proof through AffineCDC must exploit at least one deeper freedom:

- alter the root flow by Hamming/gauge deformation;
- choose the initial Fano flow with label-compressibility in mind;
- decompose the source graph and use compatible local target maps;
- or prove a direct existence theorem for an anisotropic `O^-(4,2)` flow.

The most promising remaining AffineCDC-specific route is to understand how the
Hamming-Lagrangian moduli of root lifts changes the used-label graph and whether
one can always leave the `K_6`-obstruction region.