# Six-port star completions for one DDD pivot change

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `16dba585b67c9b4b2905508c025ec086685db498`  
**Parents:**

- `projects/affine-cdc/research/PETERSEN_PIVOT_RESOLUTION_V1.md`;
- `projects/affine-cdc/research/CONSTANT_PIVOT_ORIENTED_ROOT_SECTION_V1.md`;
- `projects/affine-cdc/research/FOUR_POLE_CAP_LIBRARY_TEN_STATE_PROFILES_V1.md`;
- `projects/affine-cdc/research/TYPE_H_PHYSICAL_COMMUTATION_ELIMINATION_V1.md`.

**Status:** exact six-port root-completion table for the smallest source cell containing one DDD pivot change and its two adjacent transport turns. The original four-vertex path has three co-root internal edges. A four-vertex three-cherry star with the same six boundary roots is root-valued for exactly four of the six left-to-right terminal matchings. The two forbidden matchings are precisely those pairing the two distinct pivots directly. Thus a pivot-change cell is root-completable unless external incidence forces one distinguished `s--t` DDD backbone.  
**Not implied:** that one of the four star matchings is always admitted by the ambient locked profile, that the forced `s--t` backbone automatically gives a small separator, strict graph descent, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. One pivot change with adjacent turns

Let

\[
s,t\in R_5
\]

be distinct disjoint Petersen vertices. Thus

\[
F=\{s,t\}
\]

is the central DDD state of one pivot change.

Choose a previous state and a next state

\[
F^-=\{s,x\},
\qquad
F^+=\{t,y\},
\]

where:

- `x` is a Petersen neighbour of `s` distinct from `t`;
- `y` is a Petersen neighbour of `t` distinct from `s`.

Let `z` be the side root emitted by the left turn and `w` the side root emitted by the right turn. The pivot-resolution theorem gives

\[
\boxed{x+t+z=0,}
\]

and

\[
\boxed{s+y+w=0.}
\]

The left constant-pivot run forces the central state to resolve as `t`, while the right run forces it to resolve as `s`.

---

## 2. The minimal four-vertex co-root path

The source cell containing the two turns and the central state has four internal vertices:

1. a left one-factor leaf;
2. a left co-root transport vertex;
3. a right co-root transport vertex;
4. a right one-factor leaf.

Its six boundary roots, grouped by the two resolved runs, are

\[
\boxed{(s,x,z\mid w,t,y).}
\]

The boundary sum is zero:

\[
(s+x+z)+(w+t+y)
=(s+t)+(s+t)=0.
\]

In the original defect path, the three internal edges are co-roots. The central one carries the DDD state `{s,t}`. Hence this path is not itself a root-valued completion of its six-port boundary.

### Standard coordinate certificate

By `S_5` symmetry choose

\[
s=12,
\qquad
t=34,
\qquad x=35,
\qquad z=45,
\qquad y=15,
\qquad w=25.
\]

The boundary word is

\[
\boxed{12,\ 35,\ 45\mid25,\ 34,\ 15.}
\]

The three forced co-root path values are

\[
q_4=1235,
\qquad q_5=1234,
\qquad q_2=1345.
\]

---

## 3. Three-cherry star topology

Take one central cubic vertex and three outer cubic vertices. Each outer vertex receives two boundary ports and one internal edge to the centre.

A left-to-right perfect matching

\[
\sigma:\{s,x,z\}\longrightarrow\{w,t,y\}
\]

specifies the three boundary pairs placed at the outer vertices.

For a pair `(a,b)`, conservation forces its internal star edge to have value

\[
a+b.
\]

Thus the star is root-valued exactly when all three matched pairs consist of intersecting roots.

If the three internal values are roots, their sum is the total boundary sum, hence zero. Three nonzero roots of `K_5` summing to zero form one root triangle, so the central vertex is automatically root-valued.

### Theorem 3.1 — star-completion criterion

A cross matching `sigma` gives a root-valued four-vertex completion if and only if

\[
\boxed{a\cap\sigma(a)\ne\varnothing}
\]

for each of the three left ports `a in {s,x,z}`.

No further central condition is required.

---

## 4. The exact four-of-six table

The intersection pattern is rigid.

- The pivot root `s` is disjoint from `t`.
- The root `s` intersects both `w` and `y`.
- Each of `x,z` intersects all three roots `w,t,y`.

Therefore the only forbidden pair in the complete left-right bipartite incidence graph is

\[
\boxed{s\mathbin{-}t.}
\]

### Theorem 4.1 — four admissible routes

Among the six perfect matchings between

\[
\{s,x,z\}
\quad\text{and}\quad
\{w,t,y\},
\]

exactly four are root-valued star completions. They are precisely the matchings avoiding the pair `s--t`.

The two non-root-completable matchings are

\[
\boxed{
(s,t),\ (x,w),\ (z,y),
}
\]

and

\[
\boxed{
(s,t),\ (x,y),\ (z,w).
}
\]

### Proof

There are `3!=6` cross matchings. A matching containing `s--t` has an internal edge value

\[
s+t,
\]

which is a co-root, so it is not root-valued. There are exactly two such matchings, according to the two pairings of `{x,z}` with `{w,y}`.

Every other matching uses only intersecting pairs. Its three forced internal values are roots and sum to zero, hence form a root triangle. ∎

---

## 5. Explicit standard table

For

\[
(s,x,z\mid w,t,y)
=(12,35,45\mid25,34,15),
\]

the four admissible star pairings and their internal root triangles include:

\[
(12,25),\ (35,34),\ (45,15)
\]

with internal roots

\[
15,\ 45,\ 14;
\]

\[
(12,25),\ (35,15),\ (45,34)
\]

with internal roots

\[
15,\ 13,\ 35;
\]

\[
(12,15),\ (35,25),\ (45,34)
\]

with internal roots

\[
25,\ 23,\ 35;
\]

and

\[
(12,15),\ (35,34),\ (45,25)
\]

with internal roots

\[
25,\ 45,\ 24.
\]

Each displayed triple is one `K_5` root triangle.

The two missing matchings pair `12` with `34` and therefore force the co-root `1234`.

### Exact finite certificate

Complete enumeration of all six-leaf cubic trees gives:

- four root-valued three-cherry star completions;
- thirty-two ordered path-shape root completions after arbitrary reassignment of boundary ports;
- no root completion on the original path with its six ports kept at their original vertices.

The star theorem is the minimal symmetric part of this table.

---

## 6. Why the four-cycle square does not solve the pivot change

The central DDD atom alone has four terminal roots in the `(2,2,4)` orbit and therefore admits four-cycle square completions.

However, the adjacent constant-pivot turns distinguish two additional side ports and force the two opposite resolutions `s` and `t`.

### Theorem 6.1 — no marked square bridge

For the four-root DDD rectangle, there are 144 ordered root labelings of a four-cycle completion. In none of them do `s` and `t` occur as adjacent or opposite internal cycle edges.

Hence:

\[
\boxed{
\text{the square is a boundary-profile envelope,
not a marked pivot-change bridge}.}
\]

The six-port star table is the correct bounded completion object.

---

## 7. Composition meaning

The two adjacent constant-pivot runs have already been root-resolved, including their complete emitted side-root words. The six-port boundary therefore retains all coefficient semantics needed at the switch.

Theorem 4.1 gives the exact alternative:

\[
\boxed{
\begin{array}{c}
\text{one of four cross matchings is admitted}\
\Downarrow\
\text{root-valued four-vertex star completion}
\end{array}
}
\]

or

\[
\boxed{
\begin{array}{c}
\text{all admitted incidence matchings contain }s\mathbin{-}t\
\Downarrow\
\text{one forced DDD backbone plus a binary pairing of the other four ports}.
\end{array}
}
\]

Thus a pivot change does not leave a general six-port profile problem. Its residual profile has one mandatory pair and only two remaining terminal matchings.

---

## 8. Relation to unique bad route

The forced pair

\[
s\mathbin{-}t
\]

has internal sum

\[
q=s+t,
\]

the central co-root direction. It is therefore the six-port lift of the original bad DDD route.

The four star completions are the source-level analogues of crossed rootification: each avoids the unique co-root pair and replaces the path by a root triangle at the centre.

The remaining comparison theorem is now explicit:

> Show that an ambient locked profile cannot force the `s--t` pair in both binary completions of the other four ports, unless it exposes a smaller separator, a repeated-pivot Type-T unit, or a profile-changing disjoint-support switch.

This is a finite linkage statement, not an unbounded Petersen-transducer problem.

---

## 9. Revised DDD pivot frontier

After constant-pivot resolution and the six-port star theorem, every pivot change enters one of:

1. **star resolution:** one of four root-valued cross matchings is composition-compatible;
2. **forced DDD backbone:** every compatible matching contains `s--t`;
3. **separator/profile escape:** external incidence cannot consistently choose one of the two residual binary matchings.

The only unresolved case is Branch 2.

A chain of pivot changes therefore carries an ordinary binary backbone word, rather than a general six-port state at every switch.

---

## 10. Trust boundary

### Exact here

- the four-vertex six-port source model of one pivot change plus its adjacent turns;
- the six boundary roots `(s,x,z | w,t,y)`;
- the three-cherry star completion criterion;
- the exact four admissible and two forbidden cross matchings;
- identification of `s--t` as the unique forbidden root pair;
- explicit standard-coordinate completion table;
- nonexistence of a marked square bridge;
- reduction of the residual six-port profile to one forced DDD backbone and one binary pairing bit.

### Still open

- proof that an ambient complete locked profile admits one of the four star routes;
- elimination of the forced `s--t` backbone;
- preservation of bridgelessness under the star replacement, or extraction of a separator;
- composition of several adjacent pivot-change cells;
- global induction and horizontal bookkeeping;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
