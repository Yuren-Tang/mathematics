# A fixed Fano flow whose entire root-lift orbit is half-cube noncompressible

**Programme:** `AffineCDC — Research Lead`  
**Status:** exact finite counterexample checkpoint with two independent GF(2) verifications; not canonical pending Director review  
**Parents:** `FIVE_CDC_HALFCUBE_SUBGRAPH_CLASSIFICATION_V1.md`, `FIVE_CDC_GAUGE_AS_PIECEWISE_ROOT_TRANSLATION_V1.md`, `FIVE_CDC_AFFINE_PLANE_K4_RESIDUE_V1.md`

## 1. Statement and scope

The exact half-cube theorem gives a source-dependent compression of a fixed root
lift whenever its used-label graph avoids both dense obstructions

\[
K_6
\qquad\text{and}\qquad
K_8-C_5.
\]

Equivalently, the unused-root graph must contain one of

\[
3K_2,
\qquad
K_3\sqcup K_2,
\qquad
K_4.
\]

Earlier examples showed that one noncompressible root lift can sometimes escape
through its compatible-family / gauge torsor. The example below proves that this
is not automatic.

### Theorem 1.1 — fixed-Fano orbit obstruction

There is a connected loopless cubic multigraph `G`, a nowhere-zero flow

\[
f:E(G)\to\mathbf F_2^3,
\]

and a root lift `g` of `f` such that:

1. the admissible translation space has dimension
   \[
   \dim H_f^0=4;
   \]
2. modulo the three-dimensional space of global support translations, the root-lift
   torsor has exactly two elements;
3. one reduced lift has used-label graph
   \[
   K_8-\{26\};
   \]
4. the other has used-label graph
   \[
   K_8-\{24\};
   \]
5. neither reduced lift admits a source-dependent cut-continuous compression to
   five supports.

Consequently:

\[
\boxed{
\text{A fixed nowhere-zero Fano flow need not have any half-cube-compressible root lift.}
}
\]

This is not a counterexample to `5-CDC`. The underlying graph may admit another
Fano flow, a direct `O^-(4,2)` flow, a decomposed/glued construction, or a
five-support cover not obtained from this fixed downstairs flow.

## 2. Source vertices and local root triangles

The source graph has thirty vertices. At source vertex `v`, the three incident
root half-edges are the three edges of the displayed target triangle `T_v`.

| `v` | `T_v` | `v` | `T_v` | `v` | `T_v` |
|---:|:---:|---:|:---:|---:|:---:|
| 1 | `135` | 11 | `024` | 21 | `237` |
| 2 | `137` | 12 | `047` | 22 | `134` |
| 3 | `357` | 13 | `247` | 23 | `147` |
| 4 | `014` | 14 | `025` | 24 | `347` |
| 5 | `016` | 15 | `057` | 25 | `013` |
| 6 | `046` | 16 | `257` | 26 | `013` |
| 7 | `146` | 17 | `012` | 27 | `457` |
| 8 | `156` | 18 | `013` | 28 | `457` |
| 9 | `167` | 19 | `023` | 29 | `136` |
| 10 | `567` | 20 | `127` | 30 | `136` |

A label such as `13` denotes the root

\[
e_1+e_3
\]

of the eight-coordinate even-weight module. Its projected Fano direction is

\[
1\mathbin{\mathrm{xor}}3=2.
\]

## 3. Equal-label occurrence pairing

The following table pairs the two occurrences of every source edge. Each row is

\[
(u,v;ab;h),
\qquad
h=a\mathbin{\mathrm{xor}}b.
\]

| source edge | root | direction | source edge | root | direction | source edge | root | direction |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `22-30` | `13` | `2` | `25-26` | `13` | `2` | `2-29` | `13` | `2` |
| `18-1` | `13` | `2` | `8-1` | `15` | `4` | `1-3` | `35` | `6` |
| `20-23` | `17` | `6` | `2-9` | `17` | `6` | `3-24` | `37` | `4` |
| `2-21` | `37` | `4` | `27-16` | `57` | `2` | `15-10` | `57` | `2` |
| `3-28` | `57` | `2` | `26-4` | `01` | `1` | `17-18` | `01` | `1` |
| `25-5` | `01` | `1` | `12-11` | `04` | `4` | `4-6` | `04` | `4` |
| `4-7` | `14` | `5` | `22-23` | `14` | `5` | `5-6` | `06` | `6` |
| `5-30` | `16` | `7` | `29-7` | `16` | `7` | `9-8` | `16` | `7` |
| `7-6` | `46` | `2` | `8-10` | `56` | `3` | `10-9` | `67` | `1` |
| `17-14` | `02` | `2` | `19-11` | `02` | `2` | `13-11` | `24` | `6` |
| `12-15` | `07` | `7` | `24-12` | `47` | `3` | `23-28` | `47` | `3` |
| `27-13` | `47` | `3` | `13-16` | `27` | `5` | `20-21` | `27` | `5` |
| `15-14` | `05` | `5` | `16-14` | `25` | `7` | `20-17` | `12` | `3` |
| `26-19` | `03` | `3` | `25-18` | `03` | `3` | `21-19` | `23` | `1` |
| `22-24` | `34` | `7` | `28-27` | `45` | `1` | `30-29` | `36` | `5` |

Every source vertex occurs in exactly three rows, and its three incident labels
are exactly the three edges of `T_v`. Therefore the inherited root labelling is
a root-valued flow. The source graph is connected, cubic, and loopless. Its
projection by the Fano moment map is a nowhere-zero `F_2^3`-flow.

## 4. The base used-label graph

Inspection of the forty-five source edges shows that the set of distinct root
labels is

\[
\boxed{E(J_g)=E(K_8)\setminus\{26\}.}
\]

Thus exactly twenty-seven of the twenty-eight roots occur.

Since the unused-root graph consists of one edge, it contains none of

\[
3K_2,
\qquad
K_3\sqcup K_2,
\qquad
K_4.
\]

By the exact half-cube classification, the base root lift is not compressible.

## 5. Exact admissible-translation dimension

An admissible vertex field

\[
k:V(G)\to\mathbf F_2^3
\]

satisfies

\[
k_u+k_v\in\langle f(e)\rangle
\qquad(e=uv).
\]

Each of the forty-five source edges imposes the two quotient equations obtained
by pairing with a basis of

\[
\operatorname{Ann}(f(e)).
\]

This gives a binary matrix with ninety rows and ninety vertex-coordinate
variables. Exact row reduction gives

\[
\boxed{\operatorname{rank}=86.}
\]

Hence

\[
\boxed{\dim H_f^0=90-86=4.}
\]

Because the source graph is connected, the kernel of the passage from vertex
translation fields to reduced root lifts is exactly the three-dimensional space
of constant fields. Therefore

\[
\boxed{\dim(H_f^0/\Gamma)=1.}
\]

There are exactly two root lifts modulo global support translation.

The rank calculation was performed independently in:

1. a dependency-free Python GF(2) verifier;
2. a Wolfram Language `MatrixRank[..., Modulus->2]` computation.

Both return rank `86`.

## 6. The unique nontrivial reduced translation

The following nonconstant field represents the unique nonzero class modulo
constants. Unlisted vertices carry `0`.

\[
\begin{array}{c|l}
\text{value}&\text{source vertices}\\
\hline
2&1,2,3,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28\\
1&25,26\\
0&4,5,6,7,29,30
\end{array}
\]

Here the integers are the corresponding binary vectors in `F_2^3`.

For every source edge `e=uv`, direct checking gives

\[
\boxed{k_u+k_v\in\{0,f(e)\}.}
\]

Hence the field is admissible and defines the second reduced root lift `g^k`.

## 7. The translated used-label graph

Translating each root pair at either endpoint gives

\[
\boxed{E(J_{g^k})=E(K_8)\setminus\{24\}.}
\]

Again exactly twenty-seven roots occur, and the unused-root graph is one edge.
Therefore the translated lift also contains none of the three positive templates
and is not half-cube compressible.

Since Section 5 proves that the reduced torsor has only these two elements,
Theorem 1.1 follows.

## 8. Consequences for the five-support programme

This example closes a hierarchy of overstrong fixed-flow strategies.

1. A fixed Fano flow need not admit a lift omitting three original support
   indices.
2. A fixed root lift need not admit any source-dependent global target
   compression.
3. Even the complete compatible-family / gauge orbit of a fixed Fano flow need
   not contain a half-cube-compressible lift.
4. There is no graph-independent universal `K_8 -> K_5` target compression.

Therefore a proof of `5-CDC` through the AffineCDC architecture must exploit at
least one freedom beyond the lift torsor of an arbitrary fixed downstairs flow:

- choose or alter the nowhere-zero `F_2^3`-flow itself;
- decompose the source graph and glue different local target maps;
- construct a direct anisotropic `O^-(4,2)` flow;
- or use a five-support mechanism not factoring through a single fixed Fano
  projection.

The previous orbit-averaging / relative-stress formula remains useful, but it
cannot prove that every fixed Fano-flow orbit meets the half-cube-compressible
region: this orbit is a concrete counterexample.

## 9. Relation to the seven plane residues

Neither reduced lift has an unused `K_4`, affine or tetrahedral. In particular,
for all seven linear planes `W<=F_2^3`, the affine-plane residue

\[
R_W(f)
\]

is nonzero. Hence the question posed in
`FIVE_CDC_AFFINE_PLANE_K4_RESIDUE_V1.md` has a negative answer.

The stronger orbit obstruction supersedes the plane-only computational search as
the controlling counterexample.

## 10. Reliability boundary

The graph, local triangles, pairing table, and explicit nonconstant translation
are finite certificates. Connectivity, cubicity, local root-flow conservation,
admissibility, and the two used-root sets are direct checks.

The only matrix statement is the exact binary rank `86`; it has been independently
verified in Python and Wolfram Language. The complete dependency-free verifier is
stored in the private research workbench at

`research/affine-cdc-five-cdc-notebook-v1/projects/affine-cdc/private-notes/verify_fixed_fano_orbit_obstruction.py`.

No claim is made that the underlying source graph lacks a five-support CDC or
that all possible Fano flows on it are obstructed.
