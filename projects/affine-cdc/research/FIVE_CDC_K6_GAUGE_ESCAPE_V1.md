# An explicit gauge escape from the `K_6` label obstruction

**Programme:** `AffineCDC — Research Lead`  
**Status:** exact finite certificate with computational rank check; not canonical pending independent review  
**Parents:** `FIVE_CDC_K6_LABEL_GRAPH_OBSTRUCTION_V1.md`, `FIVE_CDC_GAUGE_AS_PIECEWISE_ROOT_TRANSLATION_V1.md`

## 1. Purpose

The connected cubic root flow constructed in
`FIVE_CDC_K6_LABEL_GRAPH_OBSTRUCTION_V1.md` has used-label graph exactly `K_6` and
therefore does not itself admit source-dependent half-cube compression.

This packet shows that the obstruction is not stable under the root-lift gauge
torsor of its projected Fano flow. An explicit admissible vertex translation
field moves the root lift to one whose unused-root graph contains a `K_4`, and
hence to a five-support-compressible lift.

Moreover, an exact binary rank computation shows that, modulo global support
translations, this is the unique nontrivial gauge direction. Its gauge word has
weight fourteen.

## 2. The source root flow

Use the source graph from the `K_6` obstruction packet.

- Source vertices are the twenty triples
  \[
  ijk\in\binom{\{0,1,2,3,4,5\}}3.
  \]
- At vertex `ijk`, the three incident root half-edges are labelled
  \[
  ij,\quad ik,\quad jk.
  \]
- The explicit pairing table in the parent packet pairs equal-labelled
  half-edges into thirty source edges.
- Every one of the fifteen labels of `K_6` occurs on exactly two source edges.

Let

\[
g:E(G)\longrightarrow E(K_6)\subseteq E(K_8)
\]

be the resulting root flow, and project by the Fano moment map

\[
f(e)=\mu(g(e)).
\]

Writing the support indices as the binary vectors `0,1,...,7`, a root label
`ij` projects to

\[
f(e)=i+j=i\mathbin{\mathtt{xor}}j.
\]

## 3. The admissible translation field

Define `k:V(G)→F_2^3` by the following table.

| source vertex | `k` | source vertex | `k` |
|---|---:|---|---:|
| `012` | `0` | `123` | `5` |
| `013` | `0` | `124` | `3` |
| `014` | `7` | `125` | `5` |
| `015` | `7` | `134` | `2` |
| `023` | `3` | `135` | `5` |
| `024` | `3` | `145` | `3` |
| `025` | `2` | `234` | `3` |
| `034` | `3` | `235` | `4` |
| `035` | `3` | `245` | `3` |
| `045` | `3` | `345` | `2` |

The integers denote the corresponding binary vectors in `F_2^3`.

### Proposition 3.1 — admissibility

For every source edge `e=uv` with root label `ij` and Fano direction

\[
h=i\mathbin{\mathtt{xor}}j,
\]

one has

\[
\boxed{k_u+k_v\in\{0,h\}.}
\]

Hence `k` is an admissible vertex translation field and defines another root
lift

\[
g^k(e)=\tau_{k_u}(g(e))
\]

of the same projected Fano flow.

The assertion is a direct check against the thirty pairings in the parent
construction. It is also covered by the standalone verifier recorded in the
private research workbench.

## 4. The transformed used-label graph

Applying the translation field gives the following set of seventeen used root
labels:

\[
\begin{aligned}
E(J_{g^k})=\{&01,02,03,04,06,07,\\
             &12,13,16,17,\\
             &26,27,36,37,\\
             &46,47,67\}.
\end{aligned}
\]

Every transformed edge retains its original Fano moment, because translation of
both endpoints of a root pair preserves their difference.

The six root edges on the four support indices

\[
\{2,3,4,5\}
\]

are all unused:

\[
23,24,25,34,35,45\notin E(J_{g^k}).
\]

Thus the unused-root graph contains

\[
\boxed{K_4[\{2,3,4,5\}].}
\]

By the exact half-cube classification,

\[
J_{g^k}\longrightarrow\mathscr A_5,
\]

so the translated root lift compresses to a five-support double cover.

### Theorem 4.1 — `K_6` gauge escape

The explicit connected cubic root flow with used-label graph `K_6` and its
translated lift `g^k` project to the same nowhere-zero `F_2^3`-flow, but:

\[
J_g=K_6
\]

is not half-cube compressible, whereas

\[
K_8-J_{g^k}
\]

contains a `K_4` and is compressible.

Therefore the presence of the `K_6` used-label obstruction is not invariant under
the compatible-family / Hamming-gauge torsor of a fixed Fano flow.

## 5. Exact gauge-space computation

For this source graph, the admissible translation fields are solutions of sixty
binary linear equations in sixty vertex-coordinate variables: every one of the
thirty source edges imposes the two quotient equations

\[
k_u+k_v\in\langle f(e)\rangle.
\]

Direct row reduction gives rank

\[
\boxed{56.}
\]

Consequently

\[
\dim H_f^0=60-56=4.
\]

The source graph is connected, so the three-dimensional space of constant fields
is the global support-translation kernel. Hence

\[
\boxed{\dim\mathcal B_f=1.}
\]

The field in Section 3 represents the unique nonzero reduced gauge class. Its
gauge word

\[
\lambda_e=1
\iff
k_u+k_v=f(e)
\]

has

\[
\boxed{\operatorname{wt}(\lambda)=14.}
\]

Thus, modulo global affine relabelling, the fixed Fano flow has exactly two root
lifts: the displayed `K_6` lift and the compressible lift above.

The rank and weight statements are exact finite computations. They are supported
by the dependency-free verifier

`research-workbench:research/affine-cdc-five-cdc-notebook-v1/projects/affine-cdc/private-notes/verify_k6_gauge_escape.py`.

They have not yet been replaced by a conceptual hand proof or Lean certificate.
The existence of the gauge escape itself is certified by the explicit field and
label lists independently of the dimension claim.

## 6. Strategic consequences

### 6.1 Dense obstructions are orbit properties, not point properties

The exact target classification detects whether one chosen root lift is
compressible. It does not define an invariant of the projected Fano flow. One
must study the complete `H_f^0` orbit.

### 6.2 Weight eight is not a privileged closure point

The canonical gauge classification is complete through weight six, and weight
eight is the next unclassified cardinality. This example shows that a natural
minimal gauge orbit may instead have its unique nonzero circuit at weight
fourteen, and that this high-weight circuit performs the required dense-pattern
escape.

Therefore a programme focused only on classifying weight-eight circuits cannot
by itself settle fixed-flow compressibility.

### 6.3 Correct next question

The sharpened fixed-flow problem is:

> Does every nowhere-zero Fano flow have at least one root lift in its
> `H_f^0`-torsor whose used-label graph avoids `K_6` and `K_8-C_5`?

The present example gives positive evidence: its apparently extremal `K_6` lift
is paired with a compressible lift by the only nontrivial gauge class.

A genuine fixed-flow obstruction would have to force both dense patterns across
every point of an entire gauge torsor, not merely exhibit one noncompressible
root lift.
