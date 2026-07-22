# Connected Kempe cycles: constant-channel root lifts and bounded blocker certificates

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `42a485ebe707764d70b53501d176d801bb9287e8`  
**Parents:**

- `projects/affine-cdc/research/TYPE_X_SELECTOR_RANK_REDUCTION_V1.md`;
- `projects/affine-cdc/research/QUADRATIC_CHANNEL_PROJECTION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_RELATIVE_CHANNEL_PROFILE_CALIBRATION_V1.md`;
- `projects/affine-cdc/five-support/gauge-and-reconfiguration.md`.

**Status:** exact sufficient root-lift theorem and exact finite classification of failure of every constant repair-channel lift on one connected cycle. Failure has an inclusion-minimal coefficient certificate on at most four cycle edges, in exactly five `Aut(K_{2,3})` orbits. Their root geometry is triangle, star/co-root, or a `K_5` five-cycle.  
**Not implied:** that every root-admissible lift must use one constant repair channel, that the selected certificate edges are consecutive on the source cycle, composition-safe replacement, separator extraction, strict descent, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Constant-channel cycle switches

Let

\[
\lambda:E(G)\to R_5
\]

be a root-valued `E5` flow on a cubic graph or multipole. Fix an active root

\[
r=uv
\]

and its six repair channels

\[
S_r=\{uw,vw:w\in W\},
\qquad
W=[5]\setminus\{u,v\}.
\]

Let

\[
C\subseteq E(G)
\]

be one connected binary cycle.

For an edge `e in C`, define its safe repair fibre

\[
\operatorname{Safe}_r(e)
=
\{s\in S_r:\lambda(e)+s\in R_5\}
\]

and unsafe profile

\[
\operatorname{Unsafe}_r(e)
=S_r\setminus\operatorname{Safe}_r(e)
=U_r(\lambda(e)).
\]

### Theorem 1.1 — common safe channel gives an actual root-flow switch

If

\[
\bigcap_{e\in C}\operatorname{Safe}_r(e)
e\varnothing,
\]

choose

\[
s\in\bigcap_{e\in C}\operatorname{Safe}_r(e)
\]

and define

\[
\lambda'(e)=
\begin{cases}
\lambda(e)+s,&e\in C,\\
\lambda(e),&e\notin C.
\end{cases}
\]

Then

\[
\boxed{
\lambda':E(G)\to R_5
}
\]

is another root-valued `E5` flow with the same boundary values.

### Proof

Every switched edge remains root-valued by the choice of `s`. At every vertex of the binary cycle, exactly zero or two incident edges are switched. Adding the same coefficient `s` twice contributes zero in characteristic two, so the Kirchhoff equation is preserved. No terminal boundary changes because `C` is closed. ∎

### Terminology

Such a switch is a **constant-channel root lift** of the connected binary cycle.

It is a sufficient physical lift. A more general lift may use additional root-fibre data and is not excluded when no constant channel works.

---

## 2. Failure is a six-channel cut cover

The common safe fibre is empty exactly when

\[
\bigcup_{e\in C}U_r(\lambda(e))=S_r.
\]

Each unsafe profile is a cut of

\[
K_r=K_{\{u,v\},W}\cong K_{2,3}.
\]

Choose an inclusion-minimal set of cycle edges

\[
B=\{e_1,\ldots,e_m\}\subseteq C
\]

whose unsafe profiles still cover `S_r`.

### Theorem 2.1 — four-edge blocker bound

\[
\boxed{m\le4.}
\]

### Proof

The family

\[
U_r(\lambda(e_1)),\ldots,U_r(\lambda(e_m))
\]

is an inclusion-minimal cut cover of the connected five-vertex graph `K_(2,3)`. The cut-cover theorem gives

\[
m\le |V(K_{2,3})|-1=4.
\]

∎

### Corollary 2.2

Failure of every constant repair-channel switch on an arbitrarily long connected cycle always has a coefficient witness involving at most four cycle-edge values.

The selected edges need not be consecutive. The theorem bounds the coefficient certificate, not yet the length of a replaceable source interval.

---

## 3. Root-only unsafe profiles

The base flow is root-valued. This removes two of the twelve ambient `E5` channel profiles.

### Theorem 3.1 — exact root-profile list

For a root

\[
x\in R_5,
\]

exactly one of the following occurs.

#### (R0) Active root

If

\[
x=r,
\]

then

\[
\boxed{U_r(x)=\varnothing.}
\]

#### (R2) Root disjoint from `r`

Let

\[
x=ab\subset W
\]

and let `c` be the third element of `W`. Then

\[
\boxed{U_r(x)=\{uc,vc\}=P_c.}
\]

Thus the unsafe set is one complete resolution pair and has size two.

#### (R3) Root meeting `r`

Let

\[
x=aw,
\qquad
a\in\{u,v\},
\qquad w\in W,
\]

and write `bar a` for the other endpoint of `r`. Then

\[
\boxed{
U_r(x)
=
\{aw\}
\cup
\{\bar a z:z\in W\setminus\{w\}\}.
}
\]

This is a mixed transversal: it contains one channel from each resolution pair and has size three.

### Proof

For a root `x`,

\[
U_r(x)(s)=q(x)+b(x,s)=1+b(x,s).
\]

Hence a channel is unsafe exactly when its root is disjoint from `x`, with the alternating exception `b(x,x)=0`, which includes `x` itself when `x in S_r`.

- If `x=r`, every channel meets `r`, so the profile is empty.
- If `x=ab` lies in `W`, the only channels disjoint from it are the two channels through the remaining vertex `c`.
- If `x=aw`, the unsafe channels are `aw` itself and the two channels from `bar a` to the other two vertices of `W`.

∎

### Corollary 3.2 — root-profile census

There are exactly ten distinct root-valued profiles:

\[
\boxed{
1\text{ empty}
+
3\text{ resolution pairs}
+
6\text{ mixed transversals}.}
\]

The two uniform transversals

\[
\{ux,uy,uz\},
\qquad
\{vx,vy,vz\}
\]

are not produced by any root-valued ambient edge.

---

## 4. Exact minimal blocker orbit classification

Let the stabiliser of the active root act on the six channels:

\[
\operatorname{Stab}_{S_5}(r)
\cong S_2\times S_3
\cong\operatorname{Aut}(K_{2,3}).
\]

### Theorem 4.1 — five blocker orbits

Every inclusion-minimal root-profile cover of `S_r` is in exactly one of the following five orbits.

### `B_2` — one root-triangle completion

Certificate size:

\[
2.
\]

For one

\[
w\in W,
\]

the two ambient root values are

\[
\boxed{uw,\ vw.}
\]

They satisfy

\[
uw+vw=r,
\]

so

\[
\{r,uw,vw\}
\]

is one root triangle of `K_5`.

Their two unsafe profiles are complementary mixed transversals. There are three certificates, one for each `w`.

### `B_{3,	riangle W}` — complementary-support triangle

Certificate size:

\[
3.
\]

The root values are

\[
\boxed{xy,xz,yz}
\]

for

\[
W=\{x,y,z\}.
\]

They form the root triangle on `W` and sum to zero. Their unsafe profiles are the three resolution pairs.

There is one such certificate.

### `B_{3,	riangle a}` — endpoint triangle

Certificate size:

\[
3.
\]

Choose

\[
a\in\{u,v\}
\]

and distinct

\[
x,y\in W.
\]

The root values are

\[
\boxed{xy,ax,ay.}
\]

They form the root triangle on the three-set `{a,x,y}` and sum to zero.

There are

\[
2\binom32=6
\]

such certificates.

### `B_{3,\star a}` — endpoint star and co-root sum

Certificate size:

\[
3.
\]

Choose

\[
a\in\{u,v\}
\]

and take

\[
\boxed{ax,ay,az.}
\]

The three roots form the complete star at `a` over `W`. Their sum is the co-root missing the other endpoint of `r`:

\[
ax+ay+az=q_{\bar a}.
\]

There are two such certificates.

### `B_4` — a five-cycle through the active root

Certificate size:

\[
4.
\]

The four ambient roots together with `r` are exactly the five edges of one simple five-cycle in `K_5` containing `r`.

Equivalently, after relabelling they are

\[
\boxed{
45,\ 35,\ 24,\ 13
}
\]

with

\[
r=12,
\]

and

\[
45,35,13,12,24,45
\]

is a `K_5` five-cycle.

There are six such certificates.

### Completeness certificate

Exact enumeration of the ten root profiles gives:

\[
\boxed{
3\text{ minimal two-covers}
+
9\text{ minimal three-covers}
+
6\text{ minimal four-covers}.}
\]

Under `Aut(K_(2,3))` these split into

\[
\boxed{
1+3+1=5
}
\]

orbits by certificate size:

- one orbit of size two;
- three orbits of size three;
- one orbit of size four.

The orbit cardinalities are respectively

\[
3;\quad1,6,2;\quad6,
\]

matching the five families above.

### Proof

The root-profile list leaves only ten binary words on the six channels. Direct exact enumeration of all subsets of size at most four identifies all inclusion-minimal covers. The `S_2 x S_3` action gives five orbits. Reading back the unique root value producing each profile yields the displayed root geometries.

Each geometry can also be checked directly:

- the `B_2` pair sums to `r`;
- the first two `B_3` families are ordinary root triangles;
- the star family sums to one co-root;
- in `B_4`, adjoining `r` makes every support index degree two, hence a five-cycle, and the explicit representative proves the orbit.

∎

---

## 5. Relation to the established finite alphabet

### Corollary 5.1 — no new blocker geometry

Every failure of a constant-channel cycle lift is witnessed by one of:

1. a root triangle;
2. a three-root star with co-root sum;
3. a `K_5` five-cycle through the active root.

These are already present in the established programme as:

- rank-two/Tait root triangles;
- zero/co-root/DDD defect geometry;
- Petersen five-cycle/reflection geometry.

The theorem does not yet identify a selected source-edge certificate with a contractible physical atom. It identifies its complete coefficient geometry.

### Corollary 5.2 — maximal blocker refinement

The general four-cut blocker theorem has two spanning-tree orbits on `K_(2,3)`. Under the additional requirement that every cut arise from a **root-valued** ambient edge, only one four-certificate orbit survives. It is the five-cycle family `B4`.

Thus the second abstract spanning-tree orbit requires non-root ambient values and cannot appear as a minimal constant-channel blocker inside a root-valued flow.

---

## 6. Revised component-lifting frontier

For a connected rank-one invisible Kempe component `C`, the first root-admissible test is now exact:

### Success

A common safe repair channel exists. Then Theorem 1.1 gives an actual root-valued connected-cycle switch and therefore a genuine horizontal/route transition candidate.

### Failure

No common safe channel exists. Then at most four edges of `C` carry one of the five blocker geometries in Theorem 4.1.

The remaining source theorem should prove one of:

1. a triangle certificate yields an admissible local/Tait rerouting or profile escape;
2. a star certificate localises a co-root/DDD defect unit;
3. a five-cycle certificate localises the established Petersen reflection class;
4. the selected certificate edges separate along the cycle and expose a smaller interval or quotient cut;
5. one root-fibre relation is empty, giving a bounded defect vertex.

---

## 7. Trust boundary

### Exact here

- a common constant repair channel gives an actual root-valued cycle switch;
- failure is equivalent to a complete cover by unsafe channel cuts;
- every minimal failure certificate uses at most four cycle edges;
- the complete root-only unsafe-profile list;
- the `3/9/6` minimal-cover census;
- the five `Aut(K_(2,3))` blocker orbits;
- their exact root geometries.

### Still open

- completeness of constant-channel lifts among all possible root-fibre lifts;
- localisation when the selected certificate edges are far apart on the source cycle;
- composition-safe triangle/star/pentagon replacement;
- root-admissible pair-changing component toggle in every case;
- minimal laminar interval surgery and separator extraction;
- strict side-signature descent;
- horizontal/global induction and the global five-support theorem.