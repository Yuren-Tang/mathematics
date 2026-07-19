# The rainbow choice-parity square

**Programme:** `AffineCDC — Research Lead`  
**Status:** exact finite theorem for the two BBD Type H triangles; DDD is a separately verified degenerate shadow; interior common-witness theorem remains open  
**Parents:** `FIVE_CDC_TYPE_H_TAIT_ESCAPE_V1.md`, `FIVE_CDC_GENUINE_RAINBOW_PATH_FAMILY_REDUCTION_V1.md`

## 1. Purpose

A BBD rainbow triangle has three quotient transitions.  At each transition the ordered-signature lift has two binary choices:

1. a **role bit**, choosing between repeated trace roles in the indexed support signature;
2. a **path-component bit**, choosing one of the two terminal path components of the relevant symmetric-difference subgraph.

Thus the raw boundary lift data form six bits

\[
q=(\alpha_0,\beta_0,\alpha_1,\beta_1,\alpha_2,\beta_2)
\in F_2^6,
\]

where `alpha_j` is the role bit and `beta_j` is the path-component bit at stage `j`.

The exact ordered-signature computation has `64` raw choices but only `16` distinct support monodromies.  This packet identifies the quotient mechanism.

Define

\[
\boxed{
\nu:=\alpha_0+\alpha_1+\alpha_2,
\qquad
\rho:=\beta_0+\beta_1+\beta_2.
}
\]

Then the support cycle type depends only on the parity pair `(nu,rho)`:

\[
\boxed{
\begin{array}{c|c|c}
\nu&\rho&\operatorname{type}(\pi)\\
\hline
0&0&2^2 1\\
1&0&3 2\\
0&1&4 1\\
1&1&5.
\end{array}
}
\]

Thus:

- `rho` is the **geometric rank bit**: even path-component parity gives the rank-one path branch, odd parity gives the full-rank XOR-cover branch;
- `nu` is the **support-role bit**: within the same geometric rank, it determines whether the support permutation has a fixed support.

This is the finite control layer linking boundary choices to the two graph-theoretic mechanisms proved in the genuine path-family packet.

No five-cycle double cover theorem is claimed.

## 2. The ordered BBD lift table

Use the canonical BBD triangle

\[
B_1\xrightarrow{0}B_2\xrightarrow{1}D_0\xrightarrow{2}B_1.
\]

For each transition, the four ordered support identifications are listed in the verifier in the order

\[
(\alpha_j,\beta_j)
=
(0,0),(0,1),(1,0),(1,1).
\]

The same ordering is obtained for the second BBD triangle after simultaneous routing-colour permutation.

Composing the three transition identifications gives a map

\[
\Phi:F_2^6\longrightarrow S_5.
\]

It is not a linear map into `S_5`; nevertheless its fibres and cycle-type projection have affine structure.

## 3. The common four-point fibres

### Computational Theorem 3.1 — uniform fibre kernel

The map `Phi` has exactly `16` values, and every value has exactly four raw representatives.

For every monodromy, the difference set of its four representatives is the same two-dimensional subspace

\[
\boxed{
K_{\mathrm{raw}}
=
\left\langle
(0,1,0,0,0,1),
(1,0,1,0,0,0)
\right\rangle
\le F_2^6.
}
\]

Explicitly,

\[
K_{\mathrm{raw}}
=
\{
000000,
010001,
101000,
111001
\}.
\]

Hence the set of distinct boundary monodromies is naturally indexed by the affine quotient

\[
\boxed{
F_2^6/K_{\mathrm{raw}}
\cong F_2^4
}
\]

as a set of raw-choice classes.

#### Proof status

Exact dependency-free Wolfram enumeration of all `64` raw choices.  The same four-point difference set occurs in all sixteen fibres. ∎

The two generators have a direct redundancy interpretation:

- `010001` toggles the outer path-component choices together;
- `101000` toggles the first two role choices together.

They alter the raw description without altering the resulting support monodromy.

## 4. The parity square

Both `nu` and `rho` vanish on `K_raw`, so they descend to the quotient `F_2^6/K_raw`.

### Computational Theorem 4.1 — cycle-type parity law

For every raw BBD lift choice,

\[
\boxed{
\operatorname{type}(\Phi(q))
=
\begin{cases}
2^2 1,&(\nu,\rho)=(0,0),\\
3 2,&(\nu,\rho)=(1,0),\\
4 1,&(\nu,\rho)=(0,1),\\
5,&(\nu,\rho)=(1,1).
\end{cases}
}
\]

Each of the four parity cells contains:

- `16` raw choices;
- `4` distinct monodromies;
- one support cycle type only.

#### Proof status

Exact enumeration.  The assertion is checked on all `64` choices, not inferred from aggregate counts. ∎

### Corollary 4.2 — path parity is the rank selector

\[
\boxed{
\rho=0
\iff
\dim(W\cap\operatorname{im}(1+\pi))=1,
}
\]

and

\[
\boxed{
\rho=1
\iff
W\cap\operatorname{im}(1+\pi)=W.
}
\]

Thus the parity of the three physical path-component choices determines which graph theorem applies:

\[
\begin{array}{c|c}
\rho=0&\text{rank-one spanning-middle-path theorem},\\
\rho=1&\text{full-rank XOR path-cover theorem}.
\end{array}
\]

### Corollary 4.3 — role parity selects the algebraic fibre type

For fixed `rho`, changing `nu` changes only the precise support cycle type:

\[
\begin{array}{c|c|c}
\rho&\nu=0&\nu=1\\
\hline
0&2^2 1&3 2\\
1&4 1&5.
\end{array}
\]

The graph-level success criterion is unchanged within each row, while root-fibre cardinalities and ambient norm channels may differ.

## 5. Integration with the genuine path theorem

For one physical BBD lift let its selected switch paths be

\[
P_0,P_1,P_2
\]

and let

\[
t_\gamma
=(P_0\triangle P_2)\otimes u+P_1\otimes v.
\]

Assume first that the ambient norm defect vanishes.

### Even path parity: `rho=0`

The support type is `2^2 1` or `3 2`.  The genuine path theorem gives

\[
P_1=P_0\triangle P_2.
\]

Hence:

\[
\boxed{
P_1\text{ spanning}
\Rightarrow
\text{Tait resolution and profile escape};
}
\]

otherwise the missed internal vertices give empty local root relations.

### Odd path parity: `rho=1`

The support type is `4 1` or `5`.  The genuine path theorem gives

\[
\boxed{
E(P)=P_1\cup(P_0\triangle P_2)
\Rightarrow
\text{Tait resolution and profile escape};
}
\]

otherwise the complement is a nonempty uncovered-edge set.

Therefore the parity square is not merely a classification of permutations.  It routes each lifted loop into one of two composition-level geometric tests.

## 6. The remaining two quotient coordinates

The parity projection

\[
F_2^6/K_{\mathrm{raw}}
\longrightarrow
F_2^2,
\qquad
[q]\longmapsto(\nu,\rho)
\]

has four elements in every fibre.  These remaining two quotient coordinates distinguish the four actual monodromies inside each parity cell.

They are expected to control:

- the precise interior norm-defect channel;
- which physical terminal path components are selected after support transport;
- the residual role of repeated traces.

No canonical geometric interpretation is claimed yet.  The next interior-family theorem should attach the obstruction signature

\[
(d_\lambda,U_\lambda,X_\lambda)
\]

to these four lifts in each cell and seek a common witness.

## 7. The DDD triangle as a degenerate shadow

For the DDD triangle

\[
D_0\xrightarrow{2}D_1\xrightarrow{0}D_2\xrightarrow{1}D_0,
\]

the ordered-signature enumeration gives only four distinct lifted loops:

- two support permutations of type `2^2 1`;
- two of type `4 1`.

The three support-pair coefficients are fixed and still have the form

\[
u,v,u.
\]

Thus DDD retains the rank-one/full-rank dichotomy, but it does not possess the full BBD six-bit choice bundle.  It should be treated as a degenerate one-dimensional shadow of the parity square, not forced into the same raw-coordinate theorem.

The downstream conclusions are unchanged:

- a successful zero-norm root lift gives a Tait resolution and immediately creates a `B_i` state outside the DDD profile;
- an obstructed lift is recorded by ambient norm, uncovered edges, or missed vertices.

## 8. Mechanism diagram

For a BBD Type H triangle:

\[
\boxed{
\begin{array}{c}
q\in F_2^6
\\ \downarrow/ K_{\mathrm{raw}}\\
[q]\in F_2^4
\\ \downarrow\\
(\nu,\rho)\in F_2^2
\\ \downarrow\\
\begin{cases}
\rho=0:&\text{rank-one spanning-path mechanism},\\
\rho=1:&\text{full-rank XOR-cover mechanism}.
\end{cases}
\\ \downarrow\\
\begin{cases}
\text{success}:&\text{Tait resolution and profile escape},\\
\text{failure}:&\text{missed vertices / uncovered edges / ambient translation}.
\end{cases}
\\ \downarrow\\
\text{common-witness and strict decomposition target.}
\end{array}
}
\]

This is the current finite mechanism interface.  It compresses `64` raw choices to four geometric cells without discarding the four interior monodromies in each cell.

## 9. Trust boundary

The following are exact finite results:

- the `64 -> 16` raw-choice-to-monodromy count;
- uniform fibre size four;
- the common two-dimensional fibre kernel;
- descent of `nu,rho` to the quotient;
- the complete cycle-type parity table;
- four monodromies in each parity cell;
- the DDD counts `2+2` and `4`, two each.

The following are theorem-level consequences when combined with earlier packets:

- `rho` selects the rank-one or full-rank graph mechanism;
- successful zero-norm lifts force Tait escape;
- residual zero-norm failures are missed-vertex or uncovered-edge certificates.

The following remain open:

- a canonical interpretation of the two residual quotient coordinates;
- lifting the parity square from ordered boundary signatures to the full interior path-component groupoid;
- proving a common-witness theorem across the four monodromies in each cell;
- converting the common witness into dot-product factorisation, smaller separator, or bounded replacement;
- eliminating nonzero norm translations.

## 10. Next exact tasks

1. Compute the interior norm and path obstruction signatures of the four monodromies in each parity cell.
2. Determine whether the two residual quotient coordinates form an affine action on a pair of path-component torsors.
3. Prove that four obstructed lifts in one cell have a common connected witness region.
4. Compare that region with the four-pole factor in snark dot-product decomposition.
5. Treat DDD separately as the degenerate two-type line and then unify only at the common-witness level.
