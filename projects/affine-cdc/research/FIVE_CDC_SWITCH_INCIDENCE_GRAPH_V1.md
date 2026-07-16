# The bipartite component-incidence graph of a five-support switch

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level research checkpoint; not canonical pending review  
**Parent:** `FIVE_CDC_ADMISSIBLE_SWITCH_IMAGE_V1.md`

## 1. From two colour subgraphs to a bipartite graph

Retain the notation of the admissible-switch image theorem. Thus `R=R_{W,t}`
is the refined quotient associated with a plane `W` and a nonzero switch
direction `t∈W`, and its edge set is partitioned into the spanning subgraphs

\[
R_0\sqcup R_1
\]

according to the remaining binary coordinate `y`.

Define a bipartite multigraph

\[
\mathscr I_{W,t}
\]

as follows.

- The left vertices are the connected components of `R_0`.
- The right vertices are the connected components of `R_1`.
- For every vertex `v∈V(R)`, introduce one edge `\epsilon_v` joining the
  `R_0`-component containing `v` to the `R_1`-component containing `v`.

Parallel edges are allowed. There are no loops because the two parts are kept
distinct even when the corresponding vertex sets coincide.

Hence there is a canonical identification

\[
\mathbf F_2^{V(R)}
\cong
\mathbf F_2^{E(\mathscr I_{W,t})},
\qquad
p\longleftrightarrow (p_v)_{\epsilon_v}.
\]

## 2. The correction space is an ordinary cycle space

### Theorem 2.1 — component-incidence cycle theorem

Under the canonical identification above,

\[
\boxed{
\mathsf B(R_0)\cap\mathsf B(R_1)
\cong
\mathcal C(\mathscr I_{W,t}).
}
\]

#### Proof

A vector `p∈F₂^{V(R)}` lies in `\mathsf B(R_0)` exactly when its coordinate sum
on every connected component of `R_0` is zero. Under the incidence-graph
identification, this is precisely the even-degree condition at every left
vertex of `\mathscr I_{W,t}`.

Similarly,

\[
p\in\mathsf B(R_1)
\]

is exactly the even-degree condition at every right vertex. Therefore `p` lies
in the intersection if and only if its corresponding edge word is a binary
cycle of the bipartite multigraph. ∎

The dimension formula from the switch-image theorem becomes the ordinary cycle
rank identity

\[
\dim\mathcal C(\mathscr I_{W,t})
=
|E(\mathscr I_{W,t})|-|V(\mathscr I_{W,t})|
+c(\mathscr I_{W,t}),
\]

because

\[
|E(\mathscr I_{W,t})|=|V(R)|,
\qquad
|V(\mathscr I_{W,t})|=c(R_0)+c(R_1),
\]

and the connected components of `\mathscr I_{W,t}` correspond to the connected
components of `R=R_0\cup R_1`.

## 3. Fibre parity and the full correction map

The quotient

\[
q:V(R)\twoheadrightarrow V(Q_W)
\]

partitions the edges `\epsilon_v` of `\mathscr I_{W,t}` into fibres. Define the
fibre-parity map

\[
\sigma_q:
\mathbf F_2^{E(\mathscr I_{W,t})}
\longrightarrow
\mathbf F_2^{V(Q_W)},
\qquad
(\sigma_q p)_K
=
\sum_{v\in q^{-1}(K)}p_{\epsilon_v}.
\]

### Corollary 3.1 — cycle-syndrome form of one-switch correction

The set of all five-support defect changes obtainable by admissible switches in
direction `t` is

\[
\boxed{
\operatorname{Im}\Delta_{W,t}
=
\sigma_q\bigl(\mathcal C(\mathscr I_{W,t})\bigr).
}
\]

Consequently the current defect is killed by one admissible `t`-switch if and
only if it is the fibre syndrome of a binary cycle in
`\mathscr I_{W,t}`.

This converts the correction problem into an ordinary cycle-code decoding
problem with a nonstandard parity-check map `\sigma_q`.

## 4. Dual form

A function

\[
\lambda:V(Q_W)\to\mathbf F_2
\]

pulls back to the edge word

\[
\widehat\lambda_{\epsilon_v}:=\lambda(q(v))
\]

on `\mathscr I_{W,t}`.

### Corollary 4.1 — cut certificate for switch failure

The functional `lambda` annihilates every admissible `t`-switch correction if
and only if

\[
\boxed{
\widehat\lambda
\in
\mathcal C(\mathscr I_{W,t})^\perp,
}
\]

that is, if and only if `\widehat\lambda` is a cut/tension word of the bipartite
component-incidence graph.

Thus failure of one-direction correction has a finite combinatorial certificate:
a nonzero quotient-vertex bit pattern whose fibre-constant edge word is an exact
tension on `\mathscr I_{W,t}` and pairs nontrivially with the current defect.

## 5. Minimal correction modes

Because `\mathscr I_{W,t}` is bipartite, every circuit of its cycle matroid has
even length. The primitive admissible correction modes are therefore alternating
component cycles of lengths

\[
2,4,6,8,\ldots.
\]

- A length-two mode consists of two vertices of `R` lying in the same
  `R_0`-component and the same `R_1`-component.
- A length-four mode alternates between two `R_0`-components and two
  `R_1`-components.
- Higher modes are the corresponding longer alternating chains.

Every one-switch correction decomposes into these ordinary bipartite circuits.
This gives a precise parity explanation for the evenness of switch modes; it is
not necessary to invoke the more elaborate gauge-code parity theorem at this
linear slice.

The resemblance to the existing weight-`2`, `4`, and `6` gauge-circuit
classification is nevertheless structurally suggestive. The two codes are not
identified here: the present code is the cycle code of a derived bipartite
component-incidence graph, whereas the gauge code consists of harmonic cut
quotients of the original flow constraint system.

## 6. Strategic consequence

For a fixed plane `W`, there are three possible nonzero switch directions
`t∈W`. Each direction produces a different deleted colour matching, refined
quotient, bipartite incidence graph, and fibre-syndrome code.

The next exact question is therefore

\[
\boxed{
\text{Must }d_W(f)
\text{ lie in at least one of the three codes }
\sigma_q\mathcal C(\mathscr I_{W,t})?
}
\]

If not, one obtains a simultaneous triple of cut certificates. Understanding the
compatibility among those three dual certificates is the natural next step before
introducing two successive switch directions and their bilinear interaction.