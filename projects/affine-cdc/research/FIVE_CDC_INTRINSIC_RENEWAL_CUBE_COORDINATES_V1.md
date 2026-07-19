# Intrinsic parity coordinates for the universal renewal cube

**Programme:** `AffineCDC — Research Lead`  
**Status:** exact finite theorem on the universal weighted-dual template; intrinsic formulas verified computationally, conceptual derivation still open  
**Parents:** `FIVE_CDC_UNIVERSAL_RENEWAL_CUBE_TEMPLATE_V1.md`, `FIVE_CDC_RENEWAL_SKELETON_AND_RESERVE_CODE_CENSUS_V1.md`

## 1. Purpose

The universal renewal-cube packet proved that the five three-dimensional residual fibres have the same eight weighted-dual types up to affine relabelling of their gauge states.

That statement still used the arbitrary coordinates supplied by a basis of the gauge code. The next target was to recover the affine state directly from intrinsic observables of the weighted dual graph.

This packet gives such coordinates.

## 2. Three graph-parity observables

Let `D` be one of the weighted dual one-skeletons in the universal cube. Write `D_s` for its underlying simple graph.

Define

\[
p_4(D)
:=
\#\{K_4\subseteq D_s\}\pmod2,
\]

\[
p_{\ge6}(D)
:=
\#\{v\in V(D):\deg_{D_s}(v)\ge6\}\pmod2,
\]

and

\[
p_{11}(D)
:=
\#\{v\in V(D):\deg_D^{\mathrm{wt}}(v)=11\}\pmod2.
\]

The weighted degree is the number of source edges on the corresponding support-cycle face boundary. Thus `p_{11}` is the parity of the number of eleven-sided faces.

Put

\[
\boxed{
I(D)
:=
\bigl(
 p_{\ge6}(D)+p_4(D),
 1+p_4(D),
 1+p_{11}(D)
\bigr)
\in\mathbf F_2^3.
}
\]

The constants are part of the chosen intrinsic normalization of the universal template.

## 3. Intrinsic-coordinate theorem

### Computational Theorem 3.1

On the eight weighted-dual isomorphism types

\[
\mathsf T_0,\ldots,\mathsf T_7,
\]

the map

\[
I:\{\mathsf T_0,\ldots,\mathsf T_7\}
\longrightarrow
\mathbf F_2^3
\]

is a bijection.

Moreover, two weighted dual graphs among the forty states of the five renewal fibres are isomorphic if and only if they have the same intrinsic coordinate `I`.

Thus the three displayed parity observables completely distinguish the eight universal types.

### Exact verification

The verifier:

1. constructs the five complete eight-state fibres;
2. evaluates the three graph parities without graph hashes;
3. checks that all eight coordinates occur in every fibre;
4. checks weighted graph isomorphism for equal coordinates;
5. checks nonisomorphism for distinct coordinates.

The result is exact finite computation.

## 4. Affine dynamics

Let one of the five fibres have gauge state space

\[
B_f\cong\mathbf F_2^3.
\]

For each gauge state `\beta`, let `D_\beta` be the weighted dual graph.

### Theorem 4.1 — intrinsic affine state map

The map

\[
\Phi_f:B_f\longrightarrow\mathbf F_2^3,
\qquad
\Phi_f(\beta)=I(D_\beta),
\]

is an affine isomorphism.

Equivalently, there are an invertible linear map

\[
L_f:B_f\longrightarrow\mathbf F_2^3
\]

and an offset `c_f` such that

\[
\boxed{
I(D_\beta)=L_f(\beta)+c_f.
}
\]

Consequently, for every gauge move `\lambda`,

\[
\boxed{
I(D_{\beta+\lambda})+I(D_\beta)
=
L_f(\lambda),
}
\]

and the right-hand side is independent of the starting state `\beta`.

#### Proof status

For each of the five exact fibres, the eight-value sequence `\beta\mapsto I(D_\beta)` is checked to be an affine permutation of `\mathbf F_2^3`. The state-independence identity then follows algebraically. ∎

## 5. Normal forms of the five fibres

With the gauge bases produced by the exact solver, one fibre has

\[
\Phi_f(\beta)=\beta.
\]

The other four have the same affine permutation

\[
(0,1,2,3,4,5,6,7)
\longmapsto
(7,6,4,5,2,3,1,0).
\]

Its offset is `7`, and its linear part sends the standard basis vectors

\[
1\mapsto1,
\qquad
2\mapsto3,
\qquad
4\mapsto5.
\]

These formulas depend on the solver's gauge bases, while `I(D)` itself is intrinsic to the weighted dual graph.

## 6. Mechanism interpretation

The universal renewal cube is therefore not merely an affine parameter set imposed from outside.

Its affine coordinates are visible in the obstruction graph itself:

- one coordinate is controlled by the parity of eleven-sided faces;
- one by the parity of simple `K_4` subgraphs;
- one by a combination of `K_4` parity and the parity of high-degree dual vertices.

Gauge addition becomes translation of these observable parity coordinates.

The local obstruction module can now be written as

\[
\boxed{
\text{gauge code }B_f
\xrightarrow[\text{affine iso}]{\ \Phi_f\ }
\text{intrinsic weighted-dual parity state}
\xrightarrow{}
\text{one private }K_6.
}
\]

This is stronger than saying that eight bad graphs happen to form a cube. It exhibits the cube as an observable dynamical system.

## 7. Relation to the harmonic circuit

Every universal cube has minimum gauge circuit of weight six and quotient type `2K_3`.

The intrinsic-coordinate theorem implies that the action of this circuit on weighted dual parity data is a fixed nonzero translation. The same holds for every linear combination of the three gauge generators.

What is not yet understood is why the face-transition surgery generated by the `2K_3` harmonic quotient forces precisely the three displayed parity laws.

A conceptual proof should derive the linear map `L_f` directly from:

- the six-edge partial Petrial;
- the face permutation before and after the surgery;
- parity changes in weighted face lengths, clique counts, and high simple degrees.

## 8. Existing mechanism and remaining obstruction

### Existing mechanism

The sequence is now:

\[
\text{harmonic gauge word}
\longrightarrow
\text{partial Petrial}
\longrightarrow
\text{affine change of three intrinsic graph parities}
\longrightarrow
\text{replacement weighted-dual type}
\longrightarrow
\text{new private }K_6.
\]

Every step except the conceptual parity-update formula is exact.

### Remaining obstruction

The intrinsic coordinates describe renewal but do not yet break it. The cube remains fully covered because every one of its eight observable states has one private clique.

The next missing theorem is therefore not another classification. It is an update or incompatibility principle showing that a horizontal connected-cycle switch cannot preserve this intrinsic affine module indefinitely unless the source graph decomposes.

## 9. Next targets

### 9.1 Conceptual parity-update theorem

Derive, without enumeration,

\[
I(D_{\beta+\lambda})+I(D_\beta)=L_f(\lambda)
\]

from the face-transition permutation and the harmonic quotient of `\lambda`.

### 9.2 Rotation-system refinement

Determine whether the eight full cycle-face embeddings, including rotation data, are also intrinsically classified by the same three coordinates.

### 9.3 Horizontal action

For a connected-cycle flow switch `f\mapsto f+a1_C`, compute how the intrinsic coordinate system and its linear action change. The desired output is a finite transition rule between renewal modules.

### 9.4 Decomposition alternative

If the same intrinsic module persists across all reachable horizontal states, use the repeated `2K_3` interfaces and almost-global clique zones to extract a canonical cut or gluing decomposition.

## 10. Trust boundary

The three parity formulas, their bijectivity on the eight weighted-dual types, and their affine behaviour on all five exact fibres are finite verified facts.

No general theorem yet states that these formulas coordinatize every three-dimensional renewal fibre, that they follow formally from every `2K_3` gauge circuit, or that the universal cube can always be escaped horizontally.
