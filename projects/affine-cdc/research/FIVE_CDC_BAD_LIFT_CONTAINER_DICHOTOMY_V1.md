# Bad-lift container dichotomy and exact pivot dynamics

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level structural checkpoint; not canonical pending Director review  
**Parents:** `FIVE_CDC_HALFCUBE_SUBGRAPH_CLASSIFICATION_V1.md`, `FIVE_CDC_SUPPORT_CYCLE_PIVOT_AND_FLOW_RECONFIGURATION_V1.md`

## 1. Purpose

The half-cube classification says that a used-root graph is noncompressible exactly
when it contains either `K_6` or `K_8-C_5`. Passing to the complementary unused-root
graph turns these two dense obstructions into two sparse containers.

This gives an exact geometric description of every bad root lift and an exact update
formula for support-cycle pivots. The reconfiguration problem can therefore be viewed
as escaping two families of sparse containers rather than decreasing an undifferentiated
root-count statistic.

## 2. Used and unused root graphs

Let

\[
g:E(G)\to E(K_8)
\]

be a root lift. Write

\[
J_g\subseteq K_8
\]

for its used-root graph and

\[
U_g:=K_8-J_g
\]

for its unused-root graph.

A root lift is called **half-cube compressible** when `J_g` admits a cut-continuous
map to `K_5`, equivalently when the corresponding indexed even double cover can be
recombined into five supports.

The exact half-cube classification gives

\[
g\text{ compressible}
\iff
U_g\text{ contains }3K_2,\ K_3\sqcup K_2,\text{ or }K_4.
\]

Equivalently,

\[
g\text{ noncompressible}
\iff
J_g\text{ contains }K_6\text{ or }K_8-C_5.
\]

## 3. The sparse-container form

For a graph `U`, let `tau(U)` denote its vertex-cover number.

### Theorem 3.1 — bad-lift container dichotomy

For every root lift `g`, the following are equivalent.

1. `g` is not half-cube compressible.
2. One of the following holds:
   - `tau(U_g)<=2`;
   - `U_g` is contained in the edge set of a five-cycle on the eight support indices.

Thus

\[
\boxed{
 g\text{ is compressible}
 \iff
 \tau(U_g)\ge3
 \text{ and }
 U_g\not\subseteq C_5
 \text{ for every five-cycle }C_5.
}
\]

#### Proof

The used graph `J_g` contains a `K_6` on a six-set `S` if and only if `U_g` has no
edge with both endpoints in `S`. If `T=V(K_8)-S`, then `|T|=2`, and this condition is
exactly that every edge of `U_g` meets `T`, i.e. `T` is a vertex cover of `U_g`.
Hence

\[
J_g\supseteq K_6
\iff
\tau(U_g)\le2.
\]

Likewise, `J_g` contains `K_8-C_5` if and only if every unused edge belongs to the
corresponding five-cycle, i.e.

\[
J_g\supseteq K_8-C_5
\iff
U_g\subseteq C_5.
\]

Combine these two equivalences with the exact half-cube classification. ∎

The two bad containers have different geometry.

- **Two-cover type:** every unused root is incident with one of two support indices.
- **Pentagon type:** every unused root lies on one fixed five-cycle.

The second type is needed because a full five-cycle has vertex-cover number three but
is still noncompressible.

## 4. Witness counts and a discrete obstruction potential

Define

\[
w_2(U):=
\#\{T\in\binom{V(K_8)}2:T\text{ is a vertex cover of }U\},
\]

and

\[
w_5(U):=
\#\{C:C\text{ is a five-cycle and }U\subseteq E(C)\}.
\]

Then

\[
\boxed{
 g\text{ is noncompressible}
 \iff
 w_2(U_g)+w_5(U_g)>0.
}
\]

This suggests the lexicographic or weighted potential

\[
\Phi_0(g):=(w_2(U_g),w_5(U_g)),
\]

or any positive scalar weighting of the two coordinates. Unlike the number of used
roots, this potential records the exact obstruction containers.

For the thirty-vertex fixed-flow obstruction, each reduced lift has exactly one unused
root. A single edge has thirteen two-vertex covers and lies in one hundred twenty
five-cycles, so

\[
(w_2,w_5)=(13,120).
\]

The large witness counts explain why the state is highly noncompressible even though
its unused graph has only one edge.

## 5. Exact update under a support-cycle pivot

Let `C` be a connected component of the indexed support `F_c`. Every edge of `C` has
root label

\[
\{c,s\}
\]

for some leaf `s`. Choose `d\ne c` such that root `cd` is absent on `C`, and pivot

\[
\{c,s\}\longmapsto\{d,s\}
\]

on every edge of `C`.

For a root `r`, let `m_g(r)` be its multiplicity in the root lift. For each leaf `s`
occurring on `C`, let `m_C(s)` be the number of edges of `C` labelled `cs`.

Define the released-old-root set

\[
R_C:=
\{cs:m_g(cs)=m_C(s)>0\},
\]

and the consumed-new-root set

\[
A_{C,d}:=
\{ds:m_g(ds)=0\text{ and }m_C(s)>0\}.
\]

### Theorem 5.1 — unused-graph pivot formula

If `g'` is obtained from `g` by the support-cycle pivot `c->d` on `C`, then

\[
\boxed{
U_{g'}=(U_g\cup R_C)\setminus A_{C,d}.
}
\]

#### Proof

A root `cs` disappears from the used graph precisely when all of its occurrences were
on `C`; these are exactly the roots in `R_C`, so they become unused. A root `ds`
enters the used graph precisely when it was previously unused and is created by the
pivot; these are exactly the roots in `A_{C,d}`, so they cease to be unused. Every
other root keeps at least one occurrence status unchanged. ∎

Thus a pivot has two opposed effects.

- Adding `R_C` to the unused graph can destroy two-cover and pentagon containers.
- Removing `A_{C,d}` can create or restore such containers.

The correct local descent question is therefore not whether the total number of used
roots decreases. It is whether the released star edges destroy all current sparse
containers faster than the consumed star edges restore them.

## 6. Immediate matching escape criterion

### Corollary 6.1

Suppose `U_g` contains a two-edge matching `M`, and there is a support-cycle pivot
`c->d` on `C` with a released root `cs in R_C` such that

1. `cs` is disjoint from the four endpoints of `M`;
2. `M` is disjoint from `A_{C,d}`.

Then `g'` is half-cube compressible.

#### Proof

By Theorem 5.1, both edges of `M` remain unused and `cs` becomes unused. These three
edges form `3K_2` in `U_{g'}`. Apply the half-cube classification. ∎

This is the first direct local criterion by which a support-cycle pivot creates one of
the positive compression templates.

## 7. Strategic consequence

The base-space problem can now be phrased as a container-escape problem on the
nowhere-zero `F_2^3`-flow reconfiguration graph.

For a Fano flow `f`, define

\[
\Phi(f):=
\min_{g\text{ above }f}
\bigl(w_2(U_g)+\lambda w_5(U_g)\bigr)
\]

for a fixed positive weight `lambda`, or retain the ordered pair `(w_2,w_5)`.
A flow is good exactly when `Phi(f)=0`.

The next target is a descent/certificate theorem:

> every bad Fano flow either admits a cycle switch whose new fibre has strictly fewer
> sparse-container witnesses, or all such switches are blocked by a compact family of
> support, cut, or harmonic-quotient constraints.

The fixed thirty-vertex obstruction and its successful five-, seven-, and ten-cycle
switches show that both container families can be escaped in concrete examples. The
present theorem does not prove that every reconfiguration component meets the good
set, nor does it prove the five-cycle double-cover conjecture.