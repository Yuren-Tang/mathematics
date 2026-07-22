# Simple Petersen cycle cores are exactly identity hexagons or DDD octagons

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `fee5d3abcebbebe9a2748ae21e36ea7273dee7c7`  
**Parents:**

- `projects/affine-cdc/research/FORCED_DDD_BACKBONE_BINARY_TRANSPORT_V1.md`;
- `projects/affine-cdc/research/PETERSEN_IDENTITY_HEXAGON_SIX_CHANNEL_TRIALITY_V1.md`;
- `projects/affine-cdc/research/PETERSEN_PIVOT_RESOLUTION_V1.md`;
- `projects/affine-cdc/research/DDD_ROUTE_LOCK_TRANSGRESSION_V1.md`.

**Status:** exact classification of every simple Petersen pivot-cycle core and its emitted side-root word. The Petersen graph has one `S_5` orbit of simple cycles in each length `5,6,8,9`, with counts `12,10,15,20`. Odd cycles carry orientation-reversing return and cannot survive in an oriented lock. Every six-cycle is the identity hexagon of one root and emits one complementary root triangle twice. Every eight-cycle is canonically labelled by one Petersen edge/DDD atom: it emits all six roots of the corresponding `K_4` once and emits the atom's disjoint root pair once more. Thus every even simple-cycle core is already an equality/identity or DDD atom carrier; there is no additional bounded Petersen-cycle obstruction species.  
**Not implied:** composition-safe deletion of the identity or DDD carrier, separator extraction from attached side components, strict elimination of a Type-T backtrack, global induction, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Pivot cycle and emitted word

Let

\[
C=(s_0,s_1,\ldots,s_{m-1},s_0)
\]

be a simple cycle in the Petersen graph

\[
P=KG(5,2).
\]

At the pivot `s_i`, the two cycle neighbours are

\[
s_{i-1},
\qquad
s_{i+1}.
\]

Since `P` is cubic, there is one third neighbour. Denote it by

\[
z_i.
\]

In the Petersen transport interpretation, `z_i` is exactly the side root emitted at the turn through pivot `s_i`.

The three Petersen neighbours of `s_i` are the three roots of the triangle on the complementary three-set. Hence

\[
\boxed{z_i=s_{i-1}+s_{i+1}.}
\]

### Corollary 1.1 — zero total output

\[
\boxed{
\sum_{i=0}^{m-1}z_i=0.
}
\]

### Proof

Every pivot root occurs twice in the sum of the two-neighbour formula. ∎

---

## 2. Complete simple-cycle census

### Theorem 2.1 — Petersen cycle lengths

The simple cycles of `P` have exactly the lengths

\[
\boxed{5,6,8,9.}
\]

Their counts are

\[
\boxed{
N_5=12,
\qquad
N_6=10,
\qquad
N_8=15,
\qquad
N_9=20.
}
\]

For each length, `S_5=Aut(P)` acts transitively on the set of cycles of that length.

### Exact finite certificate

Complete enumeration of the simple cycles gives fifty-seven cycles in total, partitioned as

\[
12+10+15+20=57.
\]

Applying all `120` support permutations confirms one orbit at every occurring length.

---

## 3. Transport monodromy

Let

\[
\pi_C
=
\tau_{z_{m-1}}\cdots\tau_{z_1}\tau_{z_0}
\in S_5
\]

be the support monodromy of the cycle transport.

### Theorem 3.1 — parity and exact cycle type

For the four simple-cycle orbits:

\[
\begin{array}{c|c}
|C|&\text{cycle type of }\pi_C\\
\hline
5&41\\
6&1^5\\
8&1^5\\
9&41
\end{array}
\]

In particular:

\[
\boxed{
|C|\text{ even}
\Longrightarrow
\pi_C=1,
}
\]

whereas every odd simple cycle reverses the crossed-route orientation.

### Consequence 3.2 — oriented-lock exclusion

A simple pivot-cycle core inside an oriented inverse-dipole lock must have even length. Therefore only the six- and eight-cycle orbits survive.

The five- and nine-cycle orbits enter the already classified odd-return/orientation-switch branch.

---

## 4. Six-cycles are identity hexagons

Let `C` be a simple six-cycle.

### Theorem 4.1 — doubled Tait triangle output

There is a unique root

\[
r=uv
\]

such that the six pivots of `C` are exactly the six channels meeting `r`:

\[
S_r=E(K_{\{u,v\},[5]\setminus\{u,v\}}).
\]

The emitted word consists of the three roots on the complementary three-set, each occurring exactly twice.

Thus, after support permutation,

\[
(z_0,\ldots,z_5)
=(xy,xz,yz,xy,xz,yz)
\]

up to cyclic order and reversal.

Consequently:

\[
\boxed{
\operatorname{span}\{z_i\}
\cong\mathbf F_2^2.
}
\]

### Corollary 4.2

The ten six-cycles are exactly the ten Petersen identity hexagons, one for every root `r`.

Their side semantics are rank-two/Tait. Their three antipodal splits are the existing six-channel triality directions.

No new finite core occurs at length six.

---

## 5. Eight-cycles and duplicated one-factors

Let `C` be a simple eight-cycle.

### Theorem 5.1 — exact output multiset

There is a unique four-element support set

\[
U\subset[5]
\]

and a unique perfect matching

\[
F=\{a,b\}
\]

of `K_U` such that the emitted side-root multiset is

\[
\boxed{
E(K_U)\sqcup F.
}
\]

Equivalently:

- every one of the six roots supported in `U` occurs at least once;
- the two roots `a,b` of one disjoint pair occur twice;
- the other four roots occur once;
- no root using the fifth support index occurs.

Hence

\[
\boxed{
\operatorname{rank}\langle z_i\rangle=3.
}
\]

### Standard certificate

For one representative eight-cycle the emitted word is

\[
24,\ 34,\ 23,\ 12,\ 13,\ 34,\ 14,\ 12.
\]

Thus

\[
U=\{1,2,3,4\},
\]

all six roots of `K_U` occur, and the repeated disjoint pair is

\[
F=\{12,34\}.
\]

### Proof by orbit classification

The representative has the stated property. The property is `S_5`-equivariant. Since all fifteen eight-cycles form one orbit, it holds for every eight-cycle. Uniqueness follows because the missing support index and the two roots of multiplicity two are read directly from the output multiset. ∎

---

## 6. Eight-cycles are canonically DDD atoms

The repeated pair

\[
F=\{a,b\}
\]

consists of two disjoint roots. Hence it is one Petersen edge, equivalently one DDD/co-root atom state.

Define

\[
\Phi_8(C)=F.
\]

### Theorem 6.1 — octagon/DDD bijection

\[
\boxed{
\Phi_8:
\{\text{simple Petersen eight-cycles}\}
\longrightarrow
E(P)
}
\]

is an `S_5`-equivariant bijection.

### Proof

The map is well-defined and equivariant by Theorem 5.1. There are fifteen eight-cycles and fifteen Petersen edges. The `S_5` action is transitive on both sets, and the representative maps to the representative edge `{12,34}`. Hence the map is bijective. ∎

### Interpretation

A simple eight-cycle is not a new rank-three obstruction core. It is the canonical **DDD octagon** attached to one DDD atom. Its output word is the complete `K_4` root system together with that atom's bad root matching repeated.

The stabiliser is the same `D_8` that stabilises the DDD atom.

---

## 7. Odd cycles

For completeness:

### Five-cycle

The five emitted roots are distinct and span `E_5` with rank four. The monodromy has type `41`.

### Nine-cycle

The emitted word spans rank four; one root occurs three times and six further roots occur once. The monodromy again has type `41`.

Both have odd crossed-route orientation character and therefore cannot be closed residual cores in an oriented lock.

If they occur in an unoriented local calculation, they enter the established Möbius/odd-return orientation-switch branch rather than a new finite classification.

---

## 8. Complete even-core classification

Combining the preceding theorems:

\[
\boxed{
\begin{array}{c|c|c}
\text{simple even pivot core}&\text{canonical label}&\text{existing mechanism}\\
\hline
6\text{-cycle}&r\in R_5&\text{identity hexagon / rank-two Tait}\\
8\text{-cycle}&F\in E(P)&\text{DDD atom / }K_4\text{ octagon}
\end{array}
}
\]

Thus every bounded simple-cycle core of a forced DDD backbone is already one of the two singular-channel mechanisms:

\[
\boxed{
\text{Type Z/equality identity carrier}
\quad\text{or}\quad
\text{Type D/DDD atom carrier}.}
\]

There is no third even-cycle obstruction species.

---

## 9. Revised forced-backbone frontier

After:

- crossed-route binary transport;
- oriented-return trivialisation;
- formal Type-T backtrack reduction;
- and simple-cycle classification;

the forced-backbone branch has only:

1. a short open reduced Petersen path with at most nine DDD switch states;
2. one identity-hexagon carrier;
3. one DDD octagon carrier;
4. side-root attachments that may force a separator or prevent replacement.

The remaining difficulty is entirely composition and enclosure. The coefficient and finite-state classification is complete.

---

## 10. Trust boundary

### Exact here

- the side-output formula `z_i=s_(i-1)+s_(i+1)`;
- the complete simple-cycle lengths, counts, and `S_5` orbits;
- the exact monodromy types;
- exclusion of odd cycle cores in an oriented lock;
- identification of six-cycles with root-labelled identity hexagons;
- doubled Tait-triangle output of six-cycles;
- exact `K_4` plus duplicated one-factor output of eight-cycles;
- the `S_5`-equivariant bijection between eight-cycles and DDD atoms.

### Finite/computational boundary

The complete cycle census and representative output tables were exhaustively enumerated. The orbit arguments promote the representative identities to every cycle in each orbit.

### Still open

- composition-safe elimination of identity-hexagon and DDD-octagon carriers with arbitrary attached side semantics;
- strict elimination of embedded Type-T backtracks;
- separator extraction from blocked star routes;
- rank-one/rank-two equality-defect composition;
- global well-founded induction;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
