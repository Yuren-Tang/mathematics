# Support-cycle pivots and the Fano-flow reconfiguration graph

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level structural checkpoint, exact finite census, and literature-aligned agenda; not canonical pending Director review  
**Parents:** `FIVE_CDC_FLOW_SWITCH_HARMONIC_QUOTIENT_SURGERY_V1.md`, `FIVE_CDC_FIXED_FANO_ORBIT_OBSTRUCTION_V1.md`, `FIVE_CDC_GAUGE_AS_PIECEWISE_ROOT_TRANSLATION_V1.md`

## 1. Purpose

The previous packet showed that one rank-one cycle switch can move a fixed-Fano
root-lift orbit from complete half-cube obstruction to complete compressibility.
This packet identifies a direct root-level realization of such switches, relates the
move to the newly developed theory of nowhere-zero flow reconfiguration, and records
an exact census on the thirty-vertex obstruction graph.

The central new move is a **support-cycle pivot**: on one cycle component of an
indexed support, replace its common root-star centre by an unused support index.
This is a root-level Kempe move whose downstairs projection is exactly a rank-one
cycle switch.

## 2. Support components are root stars

Let

\[
g:E(G)\to E(K_8)
\]

be an AffineCDC root lift. For a support index `c\in\mathbf F_2^3`, put

\[
F_c:=\{e\in E(G):c\in g(e)\}.
\]

At a cubic source vertex, the three incident root labels form a target triangle.
If that triangle contains `c`, exactly two of its three root edges contain `c`; if it
does not contain `c`, none do. Hence `F_c` is an even subgraph. Every nonempty
connected component of `F_c` is therefore a source cycle.

On a component `C\subseteq F_c`, every source edge has root label

\[
\{c,s_e\}
\]

for some `s_e\neq c`. Thus the entire component is a root star with common target
centre `c`.

## 3. The support-cycle pivot theorem

### Theorem 3.1 — root-Kempe pivot

Let `C` be a connected cycle component of `F_c`. Choose a support index `d\neq c`
such that

\[
\{c,d\}
\]

is not used on `C`. Replace every root label on `C` by

\[
\boxed{\{c,s_e\}\longmapsto\{d,s_e\}.}
\]

Leave all root labels outside `C` unchanged. Then the resulting labelling `g'` is a
root-valued flow.

If `f=\mu\circ g` is the projected Fano flow and

\[
a=c+d,
\]

then

\[
\boxed{\mu\circ g'=f+a\mathbf1_C.}
\]

In particular, the pivot is a nowhere-zero rank-one cycle switch.

#### Proof

At each source vertex of `C`, the two cycle edges are precisely the two local root
edges incident with `c`. Replace `c` by `d` in the local target triangle. The third
root edge, joining the other two triangle vertices, is unchanged. Hence the three
new incident roots again form a target triangle and sum to zero.

For a source edge of `C`, both endpoint triangles replace the same root-star centre
`c` by `d`, so edge compatibility is preserved. Its projected direction changes by

\[
(d+s_e)+(c+s_e)=c+d=a.
\]

Outside `C` nothing changes. Since `d\neq s_e` by the hypothesis that root `cd` is
absent on `C`, every new root and every new projected direction remains nonzero. ∎

This is a direct lift of the downstairs rank-one switch: no affine-system re-solving
is required.

## 4. Relation to nowhere-zero flow reconfiguration

For a finite abelian group `A`, recent work defines two nowhere-zero `A`-flows to be
adjacent when they agree outside one connected source cycle. See:

- L. Esperet, K. Hendrey, A. Lagoutte, M. Marseloo, S. Norin, and R. Steiner,
  *Nowhere-zero flow reconfiguration*, arXiv:2512.17342, revised 3 July 2026;
- D. W. Cranston, J. Li, B. Su, Z. Wang, and N. Xu,
  *Reconfiguration of Nowhere-zero Flows*, arXiv:2606.24685, 23 June 2026.

### Proposition 4.1 — adjacency in exponent two

Let `A` have exponent two. If two `A`-flows differ only on a connected cycle `C`,
then their difference is constant on `C`. Consequently every adjacency in the
nowhere-zero `A`-flow reconfiguration graph has the form

\[
f\longmapsto f+a\mathbf1_C
\]

for one nonzero `a\in A`.

#### Proof

The difference of the two flows is an `A`-flow supported on `C`. At every degree-two
vertex of `C`, conservation says that the two incident nonzero difference values are
equal, since signs coincide in an exponent-two group. Connectedness propagates one
constant value around the whole cycle. ∎

Thus the rank-one switches used in the present AffineCDC programme are exactly the
edges of

\[
\mathcal F(G,\mathbf F_2^3),
\]

not merely a selected subclass.

The cited reconfiguration literature proves universal connectedness for
`\mathbf Z_2^8` on two-edge-connected graphs and gives a reduction of the universal
`A`-flow-connectedness question to two-edge-connected cubic graphs. Those theorems
do not settle `A=\mathbf F_2^3`, which is precisely the AffineCDC coefficient group.

## 5. A five-cycle support pivot in the obstruction graph

Return to the base root lift in the thirty-vertex fixed-Fano obstruction packet.
The support `F_6` has a five-cycle component

\[
C=5-6-7-29-30-5.
\]

Its source edges, in parent-certificate numbering, are

\[
\{21,22,23,25,45\}.
\]

The corresponding root labels are

\[
06,\ 16,\ 16,\ 46,\ 36,
\]

all incident with the common centre `6`. Root `26` is absent on the component.
Apply Theorem 3.1 with

\[
c=6,
\qquad d=2,
\qquad a=c+d=4.
\]

The five root labels become

\[
02,\ 12,\ 12,\ 24,\ 23,
\]

and the projected Fano flow is switched by `4` on `C`.

The directly pivoted root lift itself remains half-cube noncompressible and uses
`24` distinct roots. However, the new Fano flow has

\[
\operatorname{rank}(\delta_{f'})=84,
\qquad
\dim H_{f'}^0=6,
\qquad
\dim(H_{f'}^0/\mathbf F_2^3)=3.
\]

Hence it has eight reduced root lifts. Exact enumeration gives:

- four half-cube-compressible lifts;
- four noncompressible lifts;
- the compressible lifts use respectively `14,14,17,17` distinct roots.

One compressible lift leaves unused the matching

\[
\boxed{04,\ 12,\ 35.}
\]

This example shows that a support-cycle pivot and a subsequent gauge move can work
cooperatively even when neither the original flow fibre nor the directly pivoted
root lift is compressible.

## 6. Complete rank-one-switch census for the fixed obstruction

For each nonzero `a\in\mathbf F_2^3`, an admissible rank-one switch uses a nonzero
binary cycle in

\[
G-E_a,
\qquad
E_a:=\{e:f(e)=a\}.
\]

For the thirty-vertex obstruction flow, the seven cycle-space dimensions are

\[
10,\ 6,\ 9,\ 11,\ 10,\ 11,\ 10.
\]

Therefore the total number of nonzero admissible pairs `(a,C)` is

\[
\sum_{a\neq0}\left(2^{\dim\mathcal C(G-E_a)}-1\right)
=
\boxed{7737}.
\]

Every switched flow was solved exactly over `\mathbf F_2`, and every reduced
root-lift torsor was exhaustively enumerated. The outcomes are:

| outcome for the switched flow | count |
|---|---:|
| no reduced lift is compressible | `3453` |
| some but not all reduced lifts are compressible | `3060` |
| every reduced lift is compressible | `1224` |

Thus

\[
\boxed{4284}
\]

of the `7737` adjacent flows have at least one compressible root lift.

Additional exact observations:

- the shortest switch with at least one compressible lift has cycle length `5`;
- the shortest switch for which every reduced lift is compressible has cycle length
  `7`;
- the ten-cycle quotient-surgery example in the parent packet preserves reduced
  torsor dimension one and makes both lifts compressible;
- the reduced torsor dimensions among all switched flows range from `0` to `5`.

These are finite data for one graph and one starting flow. They are evidence, not a
general theorem about `\mathbf F_2^3`-flow connectedness.

## 7. The compression-labelled reconfiguration graph

For a cubic graph `G`, define a nowhere-zero Fano flow `f` to be **good** when at
least one root lift above `f` has used-label graph mapping to the five-support
half-cube. Equivalently, some lift avoids both complete obstruction graphs

\[
K_6
\qquad\text{and}\qquad K_8-C_5.
\]

Mark the good vertices inside the reconfiguration graph

\[
\mathcal F(G,\mathbf F_2^3).
\]

The five-support problem can now be separated into two levels.

1. **Fibre problem:** determine whether one fixed Fano-flow fibre contains a good
   lift. The fixed-Fano obstruction proves that the answer can be no.
2. **Base problem:** determine whether the reconfiguration graph contains a good
   flow, or more strongly whether every reconfiguration component meets the good
   set.

The present examples show an edge from a bad flow to a good flow and exhibit both a
root-level pivot mechanism and a harmonic-quotient surgery mechanism producing such
edges.

A natural quantitative potential is

\[
\Phi(f):=\min_{g\text{ above }f}\Phi_0(J_g),
\]

where `\Phi_0(J)=0` exactly when `J` avoids `K_6` and `K_8-C_5`. Possible choices of
`\Phi_0` include the number of dense obstruction copies, a weighted obstruction
packing number, or the minimum number of root deletions needed to create one of the
three positive unused templates

\[
3K_2,
\qquad K_3\sqcup K_2,
\qquad K_4.
\]

The next structural target is a descent or component-hitting theorem:

> every bad Fano flow either has an adjacent flow of smaller compression potential,
> or carries a compact reconfiguration obstruction that can be attacked by graph
> decomposition and interface gluing.

## 8. Scope and verification

The support-cycle pivot theorem and exponent-two adjacency proposition are hand
proofs. The thirty-vertex five-cycle example and the `7737`-switch census were checked
by dependency-free exact `GF(2)` code. The census is retained as research evidence;
only the displayed finite certificates are theorem-level without the exhaustive
search.

No statement here proves that every bridgeless cubic graph is
`\mathbf F_2^3`-flow-connected, that every reconfiguration component contains a good
flow, or that every graph has a five-support cover. The packet identifies the correct
base-space dynamics after the fixed-fibre strategy has been shown insufficient.
