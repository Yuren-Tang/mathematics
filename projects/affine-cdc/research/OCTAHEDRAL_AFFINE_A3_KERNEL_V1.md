# Octahedral frame lift and the affine A3 identity kernel

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parents:**

- `projects/affine-cdc/research/OCTAHEDRAL_OVERLAP_TRANSPORT_V1.md`;
- `projects/affine-cdc/research/DDD_ROUTE_ORIENTATION_COVER_V1.md`;
- `projects/affine-cdc/research/OCTAHEDRAL_CURVATURE_NORMAL_FORM_V1.md`.

**Status:** exact finite/group-theoretic identity-kernel theorem; physical realisation of the bounded relations remains open.  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. The full frame lift

Fix the base oriented overlap state

\[
y_0=12
\]

in the octahedral state graph

\[
\mathcal O=L(K_4).
\]

At `y0` the four possible side-root transitions are

\[
S=\{13,14,24,23\}.
\]

Write

\[
a=(13),\qquad b=(14),\qquad c=(24),\qquad d=(23)
\]

for the corresponding transpositions of the four active support names.

A transported frame is an element

\[
g\in S_4.
\]

Its visible octahedral state is

\[
p(g)=g(y_0).
\]

If the next generator in the base frame is `s in S`, then the actual side-root label is `g(s)` and the next frame is

\[
gs.
\]

### Theorem 1.1 — frame-lift Cayley graph

The full oriented-frame lift of the octahedral connection is the right Cayley graph

\[
\boxed{
\widetilde{\mathcal O}
=\operatorname{Cay}(S_4,\{a,b,c,d\}).
}
\]

The projection

\[
p:\widetilde{\mathcal O}\to\mathcal O,
\qquad g\mapsto g(y_0),
\]

is a four-sheeted graph covering. Its fibre over `y0` is

\[
H=\operatorname{Stab}_{S_4}(12)\cong V_4.
\]

An octahedral state word has identity transport exactly when its lift closes at the same frame, not merely at the same visible state.

### Proof

For a frame `g` and a base generator `s`, the physical side-root transposition is

\[
\tau_{g(s)}=g\tau_sg^{-1}.
\]

Hence left physical transport gives

\[
\tau_{g(s)}g=g\tau_s=gs.
\]

The four generators send `y0` to its four neighbours, so the Cayley adjacency projects locally bijectively to the octahedral adjacency. The fibre size is

\[
|S_4|/|E(K_4)|=24/6=4.
\]

---

## 2. A first boundedness theorem

The frame graph has twenty-four vertices and is bipartite, since every generator is an odd permutation.

### Theorem 2.1 — shortest identity-return bound

Let

\[
g_0,g_1,\ldots,g_n=g_0
\]

be a nonempty identity-transport frame word with no proper nonempty identity-return subword. Then

\[
\boxed{n\le24}
\]

and `n` is even.

### Proof

Minimality implies that

\[
g_0,g_1,\ldots,g_{n-1}
\]

are pairwise distinct. There are only twenty-four frames. Bipartiteness gives even length.

### Consequence 2.2

Every identity-holonomy overlap word of length greater than twenty-four contains a proper identity-holonomy subsegment. Thus repeated **full frame**, unlike repeated visible octahedral state, gives a bounded localisation certificate.

This does not by itself justify deletion: the localised segment still carries physical side attachments. It does bound the number of transport vertices and side ports of a support-minimal identity-return atom.

---

## 3. The affine Coxeter structure

The four generators satisfy

\[
a^2=b^2=c^2=d^2=1,
\]

\[
(ab)^3=(bc)^3=(cd)^3=(da)^3=1,
\]

and

\[
(ac)^2=(bd)^2=1.
\]

Thus their Coxeter diagram is a four-cycle, the affine diagram `A~3`.

Let

\[
W_{\mathrm{aff}}
=\langle a,b,c,d\mid
 a^2,b^2,c^2,d^2,
 (ab)^3,(bc)^3,(cd)^3,(da)^3,
 (ac)^2,(bd)^2\rangle.
\]

### Theorem 3.1 — affine A3 identification

\[
\boxed{
W_{\mathrm{aff}}\cong W(\widetilde A_3)
\cong Q(A_3)\rtimes S_4,
}
\]

where

\[
Q(A_3)=\{(m_1,m_2,m_3,m_4)\in\mathbf Z^4:
 m_1+m_2+m_3+m_4=0\}
\cong\mathbf Z^3
\]

is the `A3` root lattice.

The homomorphism

\[
\rho:W_{\mathrm{aff}}\to S_4
\]

sending the abstract generators to the four physical transpositions has

\[
\boxed{\ker\rho=Q(A_3).}
\]

### Concrete affine model

After relabelling the four support names in cyclic order, take

\[
a=s_1=(12),\quad
b=s_2=(23),\quad
c=s_3=(34)
\]

as the finite simple reflections. Let `d=s0` be the affine reflection in

\[
x_1-x_4=1.
\]

On

\[
V=\{x\in\mathbf R^4:\sum x_i=0\}
\]

it acts by

\[
d(x_1,x_2,x_3,x_4)
=(x_4+1,x_2,x_3,x_1-1).
\]

Its linear part is `(14)`. This is the standard affine-Weyl realisation, and forgetting translations is exactly `rho`.

### Interpretation

The ordinary backtrack, square, and braid relations do **not** yet reduce the physical frame system to finite `S4`. Their residual group is the full translation lattice

\[
Q(A_3)\cong\mathbf Z^3.
\]

Thus the rank-three flat remainder is intrinsic to the frame connection; it is not an artefact of a finite census.

---

## 4. Three explicit translation hexagons

The following six-letter words have trivial finite permutation image but nonzero affine translation:

\[
u_1=abcdcb,
\]

\[
u_2=bacdca,
\]

\[
u_3=cbadab.
\]

### Theorem 4.1 — simple-root translations

In the affine model above,

\[
\boxed{
u_1=t_{e_2-e_1},}
\]

\[
\boxed{
u_2=t_{e_3-e_2},}
\]

and

\[
\boxed{
u_3=t_{e_4-e_3}.}
\]

Consequently `u1,u2,u3` generate the full translation kernel `Q(A3)`.

### Proof

Direct multiplication of the four affine reflections gives identity linear part and translation vectors

\[
(-1,1,0,0),
\qquad
(0,-1,1,0),
\qquad
(0,0,-1,1).
\]

These are the three simple roots of `A3` up to the chosen signs.

### State-space form

Starting at visible state `12`, the three words project respectively to

\[
12,23,24,34,14,24,12,
\]

\[
12,24,23,13,34,23,12,
\]

and

\[
12,14,24,34,23,24,12.
\]

After cyclically rebasing at the repeated midpoint, each is the concatenation of two triangular octahedral faces of the same curvature type:

- `u1`: two star faces;
- `u2`: two star faces;
- `u3`: two `K4`-triangle faces.

Each individual face has nontrivial internal-twist holonomy, but the paired faces have equal twist and hence identity finite transport. Their uncancelled datum in the affine Coxeter system is precisely a root-lattice translation.

---

## 5. Complete word-level generation of the identity kernel

### Theorem 5.1 — affine-kernel presentation

Every word in `a,b,c,d` with identity physical transport in `S4` is a product of conjugates of the following bounded relators and their inverses:

1. involution/backtrack cells
   \[
   s^2,
   \qquad s\in\{a,b,c,d\};
   \]
2. commuting-square cells
   \[
   (ac)^2,
   \qquad
   (bd)^2;
   \]
3. adjacent braid/doubled-face cells
   \[
   (ab)^3,
   (bc)^3,
   (cd)^3,
   (da)^3;
   \]
4. the three paired-curvature translation cells
   \[
   u_1,u_2,u_3.
   \]

Equivalently,

\[
\boxed{
S_4
\cong
W(\widetilde A_3)/\langle u_1,u_2,u_3\rangle.
}
\]

### Proof

The Coxeter relators present

\[
W(\widetilde A_3)=Q(A_3)\rtimes S_4.
\]

A word with trivial finite transport represents an element of `Q(A3)`. The three words `u1,u2,u3` generate `Q(A3)`, so killing them kills the complete kernel and no more finite permutation data.

### Significance

This is a nonabelian word-level theorem, not merely a mod-two cycle-space calculation. There is no unclassified long identity-holonomy language beyond the affine translation lattice.

---

## 6. Physical meanings of the Coxeter cells

The frame presentation has direct octahedral interpretations.

### Backtrack

A relation `s^2` is an immediate reversal of one overlap transition.

### Commuting square

If `s,t` are disjoint transpositions, then

\[
st=ts.
\]

The two paths have the same endpoints and transport. In a starting frame `g`, their side-root output words are

\[
(g(s),g(t))
\]

and

\[
(g(t),g(s)).
\]

Thus a square move preserves the two side-root labels and only reverses their order. Its visible projection is an equatorial flat square.

### Braid hexagon

If `s,t` meet, let

\[
u=sts=tst
\]

be the third transposition on their three support names. The two length-three paths have side-root words

\[
(g(s),g(u),g(t))
\]

and

\[
(g(t),g(u),g(s)).
\]

Again the side-root multiset is unchanged; only the outer order is reversed. Closing the two paths gives the six-cycle `(st)^3`, whose visible projection is one triangular curvature face traversed twice.

### Translation hexagon

Each `ui` is a pair of distinct triangular curvature faces with cancelling finite holonomy. Unlike the square and braid cells, it records a genuine `A3` translation before passage to the finite physical frame group.

### Consequence 6.1

The locally Coxeter-flat moves are pure order moves on a bounded side-root word:

\[
(s,t)\leftrightarrow(t,s),
\]

or

\[
(s,u,t)\leftrightarrow(t,u,s).
\]

The only additional identity relations are the three rank-one translation directions generated by paired curvature cells.

This is the first exact algebraic bridge from the identity-holonomy kernel toward Type-T serial/order rigidity.

---

## 7. Revised physical frontier

The state/frame language is now complete. What remains is a source-graph theorem about side attachments.

### Target 7.1 — Coxeter cell surgery

For a physical overlap segment realising one side of a commuting-square or braid relation, prove one of:

1. the alternative order is realised by an admissible route witness;
2. a Kempe/profile escape occurs;
3. the inability to exchange the bounded side attachments exposes nested/serial linkage or a smaller separator.

### Target 7.2 — translation-cell localisation

For a physical realisation of one of the three paired-curvature translation hexagons, prove one of:

1. the two curvature cells cancel by an admissible crossed-route surgery;
2. their separation gives a flat-potential/zero-equality unit;
3. one curvature cell localises as a bounded DDD blossom;
4. a cyclic cut or four-pole interface separates the two cells.

### Target 7.3 — rank-three comparison

Construct a canonical map from the affine translation lattice

\[
Q(A_3)
\]

or its mod-two quotient

\[
Q(A_3)/2Q(A_3)\cong\mathbf F_2^3
\]

to the rank-three locked quotient/flat-potential data in the source graph. The shared rank is now structurally motivated, but equality still requires a physical chain map.

### Target 7.4 — bounded atom extraction

Combine Theorem 2.1 with the cell presentation to show that every support-minimal identity-holonomy physical remainder is either reducible by a bounded Coxeter cell or is a bounded multipole with at most twenty-four transport vertices. Then apply the six-channel/four-certificate machinery to lower the physical interface to a four-pole or a DDD/defect unit.

---

## 8. Trust boundary

### Exact here

- the `S4` Cayley frame lift;
- the four-sheeted covering of the octahedral state graph;
- the length-at-most-24 bound for a minimal identity return;
- the affine `A~3` Coxeter presentation;
- identification of the identity kernel with the `A3` root lattice;
- three explicit six-step translation generators;
- the complete word-level presentation of identity transport;
- side-root order formulas for commuting-square and braid moves.

### Still open

- admissible physical surgery for the bounded Coxeter cells;
- separation or cancellation of paired-curvature translation cells with arbitrary side attachments;
- canonical identification of the translation lattice with graph-level flat-potential data;
- conversion of the 24-vertex bound to a four-pole/defect reduction;
- Type T strict descent, Type H closure, horizontal/global induction, and the global five-support theorem.
