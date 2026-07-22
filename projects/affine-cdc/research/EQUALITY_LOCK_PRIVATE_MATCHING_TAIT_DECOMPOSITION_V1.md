# Equality locks are private-matching-decorated Tait systems

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `7854061724a294b965254f1f5f2bf45dbafb51e5`  

**Parents:**

- `projects/affine-cdc/research/EQUALITY_LOCK_IDENTITY_HEXAGON_CORE_V1.md`;
- `projects/affine-cdc/research/EQUALITY_LOCK_S5_ROOT_RIGIDITY_V1.md`;
- `projects/affine-cdc/research/KEMPE_BLOCKER_TAIT_SIDE_NETWORK_V1.md`;
- `projects/affine-cdc/research/SHIFT_MATCHING_BANDS_ROUTE_TAIT_PEELING_V1.md`.

**Status:** exact global coefficient decomposition of a pure-gauge one-edge equality lock. For any one of the three adjacent resolution pairs, the difference of the two locked Kempe cycles is a rank-two Tait flow whose zero set is exactly the edge matching carrying one private root disjoint from the three Tait supports. Every source vertex is either a genuine Tait branch vertex or a private-matching subdivision vertex. Thus the surviving equality lock has no arbitrary side-root attachment system: it is precisely a rank-two Tait skeleton decorated by one fixed-root matching. The seven possible branch sections are exactly the seven support triangles not containing the private root.

**Not implied:** that the matching-decorated Tait system always contains a composition-safe physical dipole, that every peeling step decreases a cover-independent global measure, elimination of the final one-edge equality lock, proof-DAG closure, canonical acceptance, independent audit, Lean verification, manuscript integration, or the global five-support theorem.

---

## 1. Pure-gauge equality lock

Let

\[
x:E(G')\to R_5
\]

be the root-valued flow on the smaller graph after one inverse-dipole cancellation. Let the two marked reconnection edges be

\[
e,f
\]

with common root value

\[
x(e)=x(f)=r=uv.
\]

Assume the one-edge equality expansion is locked. The established pure-gauge theorem gives, for every repair channel

\[
a\in S_r=\{uz,vz:z\in[5]\setminus\{u,v\}\},
\]

one connected Kempe cycle

\[
H_a=\{g:x(g)+a\in R_5\}
\]

containing both marked edges and inducing the same oriented terminal matching after `e,f` are cut.

Choose one index

\[
w\in[5]\setminus\{u,v\}
\]

and put

\[
s=uw,
\qquad
t=vw.
\]

Then

\[
\boxed{s+t=r.}
\]

Let the remaining two support indices be

\[
\{p,q\}=[5]\setminus\{u,v,w\}
\]

and define the private root

\[
\boxed{d=pq.}
\]

The roots `r,s,t` form the triangle on `{u,v,w}`, while `d` is disjoint from that three-support plane.

---

## 2. Adjacent-channel difference flow

Define

\[
\boxed{
h=s1_{H_s}+t1_{H_t}.}
\]

Because `H_s,H_t` are binary cycles, `h` is an `E_5`-valued zero-boundary flow. Its values lie in

\[
\langle s,t\rangle=\{0,s,t,r\}.
\]

For a root label `a`, the value is determined by the two safety bits:

\[
h(a)=
\begin{cases}
0,&a\notin H_s\cup H_t,\\
s,&a\in H_s\setminus H_t,\\
t,&a\in H_t\setminus H_s,\\
r,&a\in H_s\cap H_t.
\end{cases}
\]

### Theorem 2.1 — exact four-fibre root partition

The ten roots split as

\[
\boxed{
\begin{array}{c|c}
h\text{-value}&x\text{-root labels}\
\hline
0&\{pq\}\\[2mm]
r&\{uv,wp,wq\}\\[2mm]
s&\{up,uq,vw\}\\[2mm]
t&\{vp,vq,uw\}.
\end{array}}
\]

In particular:

\[
\boxed{h(g)=0\iff x(g)=d.}
\]

### Proof

A root is safe for a channel exactly when the two `K_5` edges are distinct and intersect.

- The root `d=pq` is disjoint from both `s=uw` and `t=vw`, so both safety bits vanish.
- The three roots `uv,wp,wq` meet both channels once, giving `h=r`.
- The roots `up,uq` meet `s` but are disjoint from `t`, while `vw=t` is unsafe for `t` and meets `s`; these give `h=s`.
- The last class is symmetric and gives `h=t`.

The four displayed classes have sizes `1,3,3,3` and exhaust `R_5`. ∎

---

## 3. Complete local vertex dichotomy

Every cubic source vertex of `x` carries one root triangle of `K_5`.

### Type B — branch triangle

If the local root triangle does not contain `d=pq`, all three incident edges have nonzero `h`-value. Since they sum to zero in the rank-two plane and are nonzero, the three values are exactly

\[
\boxed{r,s,t.}
\]

Thus the vertex is a genuine properly three-edge-coloured Tait vertex for `h`.

### Type M — private-matching subdivision

If the local root triangle contains `d=pq`, it has the form

\[
\{pq,pz,qz\}
\]

for a unique

\[
z\in\{u,v,w\}.
\]

The `d`-edge has `h`-value zero, while the other two roots lie in one common fibre of Theorem 2.1. Hence the local `h`-values are

\[
\boxed{(0,c,c)}
\]

for exactly one

\[
c\in\{r,s,t\}.
\]

### Theorem 3.1 — equality matching--Tait decomposition

At every source vertex exactly one of:

\[
\boxed{(r,s,t)}
\qquad\text{or}\qquad
\boxed{(0,c,c)}
\]

occurs.

No other local state exists.

---

## 4. The zero edges form one fixed-root matching

By Theorem 2.1,

\[
E_0(h)=x^{-1}(d).
\]

A fixed root can occur on at most one incidence of a cubic root triangle. Therefore:

### Theorem 4.1 — private matching

\[
\boxed{x^{-1}(d)\text{ is a matching in }G'.}
\]

Every endpoint of one `d`-edge is a Type-M vertex. Deleting the `d`-matching leaves every such endpoint of degree two in the support of `h`, and the two surviving incidences have the same Tait colour.

Suppress all maximal degree-two equal-colour runs. The resulting topological skeleton is properly three-edge-coloured by

\[
\{r,s,t\}.
\]

The deleted `d`-edges remember pairings between subdivision points on the coloured skeleton. Thus:

\[
\boxed{
G'
=
\text{rank-two Tait skeleton}
+
\text{one private-root matching }x^{-1}(d).}
\]

This is an equality, not merely a projection of the side semantics.

---

## 5. Seven branch-section states

Normalise

\[
r=12,
\qquad s=13,
\qquad t=23,
\qquad d=45.
\]

At a Type-B vertex choose one original root from each nonzero `h`-fibre. The three chosen roots must sum to zero.

The exact possibilities, written in Tait-colour order `(r,s,t)`, are:

\[
\boxed{
\begin{array}{c}
(12,14,24),\\
(12,15,25),\\
(12,23,13),\\
(34,14,13),\\
(34,23,24),\\
(35,15,13),\\
(35,23,25).
\end{array}}
\]

### Theorem 5.1 — seven-state branch alphabet

The seven branch states are exactly the seven support triangles of `K_5` which do not contain the private edge `45`:

\[
123,\ 124,\ 125,\ 134,\ 135,\ 234,\ 235.
\]

The three omitted support triangles

\[
145,\ 245,\ 345
\]

are precisely the Type-M subdivision states containing the private root `45`.

Thus contraction of the private root `d` sends the complete ten local root triangles to:

- seven genuine Tait branch states;
- three monochromatic subdivision states.

There is no eighth branch section or additional local coefficient bit.

---

## 6. Marked response

The marked roots satisfy

\[
x(e)=x(f)=r.
\]

Since

\[
r+s=t,
\qquad r+t=s,
\]

both marked edges belong to both `H_s` and `H_t`, and therefore carry Tait colour `r` in `h`.

Cut `e,f`. The `rs` bicoloured response is the route of `H_t`, while the `rt` response is the route of `H_s`. The equality lock gives the same oriented matching `M_i` for both.

Hence the marked skeleton has the exact double-equal response

\[
\boxed{(r,r,r,r;M_i,M_i,\varnothing).}
\]

This is the response whose connected minimal representative is the complete-profile identity hexagon of `EQUALITY_LOCK_IDENTITY_HEXAGON_CORE_V1.md`.

---

## 7. Relation to the existing peeling modules

Relative to the private root `d=pq`, the source vertices have exactly the familiar safe/blocked types.

- Type-B branch states with support triangle on `{u,v,w}` are complementary Tait vertices.
- Type-M vertices are private-root matching vertices.
- The remaining branch states are the transition vertices coupling the private matching bands to the complementary Tait components.

Therefore the whole equality lock factors through the existing matching-plus-Tait incidence quotient. The all-size peeling theorems apply to its two unbounded sectors:

\[
\boxed{
\text{complementary Tait components}
\quad+\quad
\text{private-root route-Tait bands}.}
\]

What remains nonautomatic is not coefficient classification or dipole existence. It is the cover-independent consumption of the bounded equality/DDD/Type-T event produced by peeling.

---

## 8. Revised final equality target

The one-edge equality lock is now reduced to the following theorem.

### Target 8.1 — universal matching--Tait transfer

Let a connected cyclically reduced four-pole carry the private-matching-decorated Tait structure above and the marked response

\[
(r^4;M_i,M_i,\varnothing).
\]

Prove one of:

1. a matching or Tait band exposes a source dipole whose complete inverse profile lifts the original cap;
2. a nonserial incidence changes one of the two equal responses and produces a state in `K_i`;
3. the incidence quotient splits across a two-, three-, or four-edge separator;
4. the private matching localises one DDD/Type-T carrier already eliminated by the pivot theorem;
5. the connected identity-hexagon core is enclosed, and its complete ten-state profile transfers;
6. the physical four-pole is the disconnected direct-pairing terminal, which is itself a separator/category degeneration.

The local alphabet in this theorem is finite and complete. The only remaining issue is universal profile transfer through the matching--Tait incidence quotient.

---

## 9. Trust boundary

### Exact here

- the adjacent-channel difference flow `h`;
- the exact `1+3+3+3` partition of all ten roots;
- the singleton zero fibre `h=0 iff x=d`;
- the local `(r,s,t)` / `(0,c,c)` dichotomy;
- matching structure of the private-root edges;
- the global private-matching-decorated Tait decomposition;
- the exact seven branch-section states;
- identification of the three subdivision triangles;
- the double-equal marked Tait response;
- factorisation through the established matching-plus-Tait incidence quotient.

### Still open

- a cover-independent universal transfer theorem on that incidence quotient;
- strict consumption of the bounded equality/DDD/Type-T event after peeling;
- proof that the disconnected two-rail terminal always exposes the relevant small separator;
- final global well-founded proof-DAG assembly;
- canonical acceptance, independent review, Lean verification, manuscript integration, release, and publication status;
- the global five-support theorem.
