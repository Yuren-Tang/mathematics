# Essential obstruction-renewal quotient

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level structural checkpoint with finite low-dimensional classification; not canonical pending review  
**Parents:** `FIVE_CDC_FACE_TRANSITION_OBSTRUCTION_ARRANGEMENT_V1.md`, `FIVE_CDC_K6_ESCAPE_OR_FROZEN_CYCLE_CERTIFICATE_V1.md`

## 1. Motivation

For a fixed nowhere-zero Fano flow `f`, every marked certified obstruction core `C` occurs on an affine subspace

\[
A_C=\beta_C+L_C\subseteq B_f
\]

of the reduced gauge / partial-Petrial code. The full bad region associated with a chosen obstruction library is the union of these affine loci.

Many gauge directions may be invisible to every marked core. They should be quotiented out before studying clique renewal or deeper half-cube obstructions.

## 2. Common lineality

Let `\mathfrak C_f` be a finite family of marked obstruction cores occurring somewhere in the gauge fibre, and write

\[
A_C=\beta_C+L_C,
\qquad C\in\mathfrak C_f,
\]

where `L_C\leq B_f` is the direction space of the occurrence locus.

Define the **common lineality space**

\[
L_{\mathrm{com}}
:=
\bigcap_{C\in\mathfrak C_f}L_C.
\]

Every occurrence locus is invariant under translation by `L_{\mathrm{com}}`.

Define the **essential renewal quotient**

\[
Q_f(\mathfrak C_f)
:=
B_f/L_{\mathrm{com}}.
\]

Let

\[
\pi:B_f\longrightarrow Q_f(\mathfrak C_f)
\]

be the quotient map.

### Theorem 2.1 — exact descent of the obstruction arrangement

For every marked core `C`, there is a unique affine subspace

\[
\overline A_C
\subseteq
Q_f(\mathfrak C_f)
\]

such that

\[
A_C=\pi^{-1}(\overline A_C).
\]

Moreover,

\[
\bigcup_{C\in\mathfrak C_f}A_C=B_f
\iff
\bigcup_{C\in\mathfrak C_f}\overline A_C=Q_f(\mathfrak C_f).
\]

The codimension of each occurrence locus is preserved:

\[
\operatorname{codim}_{B_f}A_C
=
\operatorname{codim}_{Q_f}\overline A_C.
\]

#### Proof

Since `L_{\mathrm{com}}\leq L_C`, the affine set `A_C=\beta_C+L_C` is a union of cosets of `L_{\mathrm{com}}`; hence it is the inverse image of the affine subspace

\[
\overline A_C
=
\pi(\beta_C)+L_C/L_{\mathrm{com}}.
\]

The covering equivalence follows because `\pi` is surjective. Finally,

\[
\dim B_f-\dim L_C
=
\dim(B_f/L_{\mathrm{com}})-\dim(L_C/L_{\mathrm{com}}).
\]

∎

Thus all gauge directions in `L_{\mathrm{com}}` can be forgotten without losing any information about the selected obstruction arrangement.

Call

\[
d_{\mathrm{ren}}
:=
\dim Q_f(\mathfrak C_f)
\]

the **essential renewal dimension**.

## 3. Essentiality

The descended arrangement has trivial common lineality:

\[
\bigcap_{C\in\mathfrak C_f}\operatorname{dir}(\overline A_C)=0.
\]

Hence `Q_f` is the smallest linear quotient through which every occurrence indicator factors simultaneously.

Equivalently, if `\rho_C:B_f\to V_C` is any linear restriction map with `L_C=\ker\rho_C`, then

\[
L_{\mathrm{com}}
=
\ker\Bigl(\bigoplus_C\rho_C\Bigr),
\]

and therefore

\[
\boxed{
 d_{\mathrm{ren}}
 =
 \operatorname{rank}\Bigl(\bigoplus_C\rho_C\Bigr).
}
\]

This realizes the essential renewal quotient as the joint image of all obstruction-exposure maps.

## 4. Renewal dimension zero and one

### Proposition 4.1

If `d_{\mathrm{ren}}=0`, every selected occurrence locus is either empty or the whole gauge fibre. In particular, any nonempty core in the library is pointwise rigid.

### Proposition 4.2 — the two-point renewal model

Assume:

1. the selected obstruction loci cover the gauge fibre;
2. no individual occurrence locus is the whole fibre;
3. `d_{\mathrm{ren}}=1`.

Then

\[
Q_f\cong\mathbf F_2
\]

and every nonempty descended occurrence locus is a singleton. A minimal irredundant subcover consists exactly of the two points

\[
\{0\},\qquad\{1\}.
\]

Thus every one-dimensional nonrigid obstruction is a literal two-state renewal system: one family of marked cores occupies one essential state and another family occupies the other.

#### Proof

The only proper nonempty affine subspaces of `\mathbf F_2` are its two singleton points. Covering requires both, and irredundancy leaves exactly one representative locus at each point. ∎

### Example 4.3 — the thirty-vertex fixed-flow obstruction

Its reduced gauge code has dimension one. In the base state, the dual contains one `K_7` and hence seven marked `K_6` subcliques. In the other state it contains exactly two marked `K_6` cliques. Every marked clique has singleton occurrence locus.

Consequently

\[
Q_f\cong\mathbf F_2,
\]

with the seven old cliques supported at one point and the two replacement cliques supported at the other. The obstruction is exactly the two-point renewal model of Proposition 4.2.

## 5. Complete two-dimensional classification

Assume now

\[
Q_f\cong\mathbf F_2^2
\]

and consider a minimal irredundant cover of `Q_f` by proper nonempty affine subspaces. Proper affine subspaces are points or affine lines.

### Theorem 5.1 — irredundant covers of `AG(2,2)`

Up to affine automorphism, exactly five types occur:

1. **parallel pair**
   \[
   \{00,01\},\qquad\{10,11\};
   \]
2. **one line plus its two complementary points**
   \[
   \{00,01\},\qquad\{10\},\qquad\{11\};
   \]
3. **two nonparallel lines plus their missing point**
   \[
   \{00,01\},\qquad\{00,10\},\qquad\{11\};
   \]
4. **three concurrent lines**
   \[
   \{00,01\},\qquad\{00,10\},\qquad\{00,11\};
   \]
5. **four singleton points**
   \[
   \{00\},\qquad\{01\},\qquad\{10\},\qquad\{11\}.
   \]

#### Proof

Classify by the number of lines in the cover.

- With no lines, all four points are necessary.
- With one line, the two points of its complementary parallel line must each be covered; irredundancy gives Type 2.
- With two lines, if they are parallel they already partition the plane, giving Type 1. If they are nonparallel, their union has three points and the unique missing point is necessary, giving Type 3.
- With three lines, a parallel pair would already cover the plane and make the third redundant. Hence the lines have the three distinct directions. They form an irredundant cover exactly when they are concurrent, giving Type 4; otherwise two of them together with the third contain a redundant member.
- Four or more members cannot be irredundant unless all four are singleton points: once a line occurs, the preceding cases already contain a proper subcover.

These five families are pairwise inequivalent because their multisets of member cardinalities and incidence patterns differ. ∎

The classification has also been exhaustively checked over all ten proper nonempty affine subspaces of `\mathbf F_2^2`: there are twenty-six labelled irredundant covers, falling into exactly these five affine-isomorphism classes.

## 6. Interpretation for obstruction renewal

After quotienting common lineality, low-dimensional persistent obstruction has a finite list of mechanisms.

- `d_{\mathrm{ren}}=0`: rigid core.
- `d_{\mathrm{ren}}=1`: two-point replacement.
- `d_{\mathrm{ren}}=2`: one of the five affine cover types in Theorem 5.1.

Thus the next computational census should not merely record fibre sizes and numbers of bad lifts. For every wholly bad fibre it should compute:

1. the complete marked-core occurrence arrangement;
2. the common lineality `L_{\mathrm{com}}`;
3. the essential renewal dimension `d_{\mathrm{ren}}`;
4. the minimal irredundant affine-cover type;
5. the topology attached to the private points or private cosets of that cover.

This is a much smaller state space than the original gauge torsor whenever many gauge directions are invisible to all active obstruction cores.

## 7. Beyond K6

The construction is not specific to cliques. Enlarge `\mathfrak C_f` to any finite certified library of graphs that do not map to `\mathscr A_5`, including compatible realizations of deeper `K_6`-free cores when found. The same common-lineality quotient simultaneously removes all gauge directions invisible to the whole library.

The correct global programme is therefore:

\[
\boxed{
\text{gauge fibre}
\longrightarrow
\text{essential renewal quotient}
\longrightarrow
\text{finite affine cover}
\longrightarrow
\text{topological certificate or escape}.
}
\]

No statement here proves that the full half-cube-bad locus is generated by a finite predetermined obstruction library, that every essential renewal quotient has small dimension, or that every compatible dual triangulation maps to `\mathscr A_5` after reconfiguration.
