# Three reconnections reduce cap-lift failure to one fixed route

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `c200ff4f073d0517ca478f2386f0cc04c1fbaa19`  
**Parents:**

- `projects/affine-cdc/five-support/cuts-four-poles-and-routing.md`;
- `projects/affine-cdc/research/FOUR_POLE_CAP_LIBRARY_TEN_STATE_PROFILES_V1.md`;
- `projects/affine-cdc/research/FOUR_PORT_TAIT_DIPOLE_PEELING_V1.md`;
- `projects/affine-cdc/research/SHIFT_MATCHING_BANDS_ROUTE_TAIT_PEELING_V1.md`;
- `projects/affine-cdc/research/TYPE_H_PHYSICAL_COMMUTATION_ELIMINATION_V1.md`.

**Status:** exact finite reduction for the remaining bounded inverse-lift obstruction. The three zero-vertex reconnections of a four-terminal interface have profiles `J_i={A,B_i,C_i}`. If all three smaller reconnection graphs are soluble but one standard two-vertex cap profile `K_i` is still blocked, Kempe closure leaves only two possible complete boundary sectors: `J_i`, or `J_i` together with the opposite outer `P_3`. In either case every complementary support-pair challenge is physically routed by the same matching `M_i`. Thus equality, adjacent-root, and co-root/DDD failures do not form three independent composition mechanisms; they collapse to one globally fixed-route outer-sector problem.  
**Not implied:** elimination of that fixed-route sector, automatic bridgelessness of all three reconnections, the individual full-cap theorem for arbitrary four-poles, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Three terminal matchings

Let the ordered terminals be

\[
\{1,2,3,4\}.
\]

Write

\[
M_0,M_1,M_2
\]

for the three perfect matchings of the terminals.

For each `i`, define two standard completion gadgets.

### Zero-vertex reconnection `E_i`

Join the two terminal pairs of `M_i` by two independent edges. There are no new cubic vertices.

### Two-vertex cap `C_i`

Attach the standard cubic two-vertex cap indexed by `M_i` in the existing four-pole convention.

Their complete support-unordered boundary profiles are denoted

\[
\Sigma(E_i),
\qquad
\Sigma(C_i).
\]

---

## 2. Profile of a zero-vertex reconnection

Let the two new edges of `E_i` carry roots

\[
p,q\in R_5.
\]

Cutting the two edges gives equal root values at the two terminals in each block of `M_i`.

Exactly one of the following holds.

1. `p=q`;
2. `p,q` are distinct intersecting roots;
3. `p,q` are disjoint roots.

The corresponding support-unordered four-terminal states are respectively

\[
A,
\qquad
B_i,
\qquad
C_i.
\]

### Theorem 2.1 — direct-pairing profile

\[
\boxed{
\Sigma(E_i)=J_i:=\{A,B_i,C_i\}.
}
\]

### Proof

The two edge values may be chosen arbitrarily in `R_5`, and the three possible intersection types above exhaust ordered root pairs up to support permutation. Their boundary-trace multiplicities are exactly the states `A,B_i,C_i`. ∎

### Root interpretation

Inside `J_i`:

- `A` is the equality branch;
- `B_i` is the adjacent-root branch;
- `C_i` is the disjoint-root/co-root branch.

Thus the three inverse-dipole value cases already lie on one three-state boundary path.

---

## 3. Profile of the two-vertex cap

The established exact cap table gives

\[
\boxed{
\Sigma(C_i)=K_i
=
\{B_j,D_j:j\ne i\}.
}
\]

Explicitly,

\[
\begin{aligned}
K_0&=\{B_1,B_2,D_1,D_2\},\\
K_1&=\{B_0,B_2,D_0,D_2\},\\
K_2&=\{B_0,B_1,D_0,D_1\}.
\end{aligned}
\]

The profiles `J_i` and `K_i` are disjoint:

\[
\boxed{J_i\cap K_i=\varnothing.}
\]

This is the boundary form of the equality/co-root obstruction to restoring the original cap after one particular reconnection.

---

## 4. Three-reconnection forcing

Let `P` be a four-pole and form the three closed graphs

\[
G_r=P\cup E_r,
\qquad
r=0,1,2.
\]

Assume each `G_r` belongs to the smaller soluble graph category. Restrict a five-support cover of `G_r` back to `P`.

### Lemma 4.1 — reconnection forcing

For every `r`,

\[
\boxed{
\Sigma(P)\cap J_r\ne\varnothing.
}
\]

### Proof

A cover of `G_r` restricts to one common boundary state of `P` and `E_r`. By Theorem 2.1, the latter state lies in `J_r`. ∎

### Category boundary

If one reconnection graph is not bridgeless, has a loop degeneration, or leaves the inductive category, the failure must be recorded separately as a separator or bounded degeneration. The present theorem concerns the branch in which all three reconnections are valid smaller inputs.

---

## 5. The cap-blocking question

Fix `i` and suppose the original cap still cannot be glued:

\[
\boxed{
\Sigma(P)\cap K_i=\varnothing.
}
\]

Because `\Sigma(P)` is a complete physical profile, it is abstractly Kempe-closed:

for every state in the profile and every complementary support-pair challenge, the actual route produces another state in the profile. In particular, at least one of the three route targets lies in the profile.

The problem is now finite:

classify all nonempty Kempe-closed subsets

\[
\Pi\subseteq\mathcal S
\]

such that

\[
\Pi\cap J_r\ne\varnothing
\quad(r=0,1,2),
\qquad
\Pi\cap K_i=\varnothing.
\]

---

## 6. Canonical finite proof for `i=0`

Assume

\[
\Pi\cap K_0=\varnothing.
\]

The allowed states are

\[
\{A,B_0,C_0,C_1,C_2,D_0\}.
\]

The exact challenge rows force two independent three-state components.

### First outer path

At `A`, the challenge row is

\[
(B_0,B_1,B_2).
\]

Since `B_1,B_2` are forbidden, closure forces `B_0`.

At `B_0`, its two challenge rows are

\[
(C_0,D_2,D_1),
\qquad
(A,B_2,B_1).
\]

Again the forbidden states leave only `C_0` and `A`.

At `C_0`, the row is

\[
(B_0,D_1,D_2),
\]

leaving only `B_0`.

Hence

\[
\boxed{
J_0=\{A,B_0,C_0\}
}
\]

is one forced closed component.

### Second outer path

At `C_1`, the row

\[
(D_0,B_1,D_2)
\]

forces `D_0`.

At `C_2`, the row

\[
(D_0,D_1,B_2)
\]

also forces `D_0`.

The two challenge rows at `D_0` are

\[
(C_2,B_2,D_1),
\qquad
(C_1,D_2,B_1),
\]

forcing `C_2` and `C_1`.

Thus the second forced component is

\[
\boxed{
L_0=\{C_1,D_0,C_2\}.
}
\]

### Meeting the three reconnection profiles

The condition

\[
\Pi\cap J_0\ne\varnothing
\]

forces inclusion of the whole component `J_0`.

Once `J_0` is included, its state `A` already meets both `J_1` and `J_2`. Therefore `L_0` is optional.

Consequently the only possibilities are

\[
\boxed{
\Pi=J_0
\quad\text{or}\quad
\Pi=J_0\cup L_0.
}
\]

---

## 7. Symmetric classification

For `\{i,j,k\}=\{0,1,2\}`, define

\[
\boxed{
L_i=\{C_j,D_i,C_k\}.
}
\]

Thus

\[
\begin{aligned}
L_0&=\{C_1,D_0,C_2\},\\
L_1&=\{C_0,D_1,C_2\},\\
L_2&=\{C_0,D_2,C_1\}.
\end{aligned}
\]

### Theorem 7.1 — three-reconnection cap-blocking classification

Let `\Pi` be a nonempty Kempe-closed ten-state profile satisfying

\[
\Pi\cap J_r\ne\varnothing
\quad(r=0,1,2)
\]

and

\[
\Pi\cap K_i=\varnothing.
\]

Then exactly one of

\[
\boxed{
\Pi=J_i,
\qquad
\Pi=J_i\cup L_i.
}
\]

### Proof

Section 6 gives `i=0`. Permute the matching indices. ∎

### Reproducible table

\[
\begin{array}{c|c}
\text{blocked cap}&\text{possible closed profiles}\\
\hline
K_0&\{A,B_0,C_0\},\quad\{A,B_0,C_0,C_1,C_2,D_0\}\\
K_1&\{A,B_1,C_1\},\quad\{A,B_1,C_0,C_1,C_2,D_1\}\\
K_2&\{A,B_2,C_2\},\quad\{A,B_2,C_0,C_1,C_2,D_2\}.
\end{array}
\]

---

## 8. Exact fixed-route consequence

For one fixed matching `M_i`, the ten-state transition graph under route `M_i` is

\[
P_3\sqcup C_4\sqcup P_3.
\]

The middle `C_4` is `K_i`.

The two outer `P_3` components are exactly

\[
J_i
\qquad\text{and}\qquad
L_i.
\]

Moreover, in both profiles from Theorem 7.1, every challenge has a unique route target inside the profile, and that route is `M_i`.

### Theorem 8.1 — fixed-route collapse

Under the hypotheses of Theorem 7.1, every complementary support-pair challenge in every realised state of `\Pi` is routed by

\[
\boxed{M_i.}
\]

Thus `P` is globally `i`-routed on the blocked sector.

### Proof

The canonical rows in Section 6 show that only the `M_0` entry remains inside `J_0` and `L_0`. Apply matching-index symmetry. ∎

---

## 9. Equality and DDD are one outer-sector mechanism

The direct-pairing path

\[
J_i=\{A,B_i,C_i\}
\]

contains:

- equality (`A`);
- intersecting-root transport (`B_i`);
- disjoint-root/co-root transport (`C_i`).

The finite theorem shows that a blocked cap cannot preserve these as separate local cases. Kempe closure joins them into one globally fixed-route component.

If the second outer path `L_i` is also present, it has the same route `M_i` and adds no new routing colour or holonomy.

Therefore

\[
\boxed{
\text{equality / adjacent-root / DDD cap failure}
\Longrightarrow
\text{one fixed terminal route }M_i.
}
\]

This is the correct common source-side target for the remaining bounded inverse-lift problem.

---

## 10. Graph-inductive use

Consider a two-vertex neighbourhood removed during Tait or route-Tait dipole descent.

There are three zero-vertex reconnections of its four external incidences.

### Alternative 10.1 — category failure

Some reconnection is not a valid smaller bridgeless cubic graph. Then extract:

- a bridge;
- a cyclic three-cut;
- a cyclic four-cut;
- a loop/parallel-edge bounded degeneration;
- or an acyclic appendage.

The current corpus already eliminates cyclic three- and four-cut branches. The precise local category lemma for all three reconnections remains to be packaged.

### Alternative 10.2 — all three reconnections soluble

Then `\Sigma(P)` meets every `J_r`.

- If it meets the original cap profile `K_i`, glue and lift the reduction.
- If it does not, Theorem 8.1 forces global `i`-routing.

Hence every failed inverse expansion now produces one of:

\[
\boxed{
\text{small separator / degeneration},
\quad
\text{successful cap lift},
\quad
\text{globally fixed-route outer sector}.
}
\]

No fourth bounded response mechanism occurs.

---

## 11. Revised final local target

The next source theorem should not separately attack zero edges and co-root edges.

It should prove:

### Target 11.1 — local fixed-route elimination

Let `P` be the outside four-pole obtained by deleting one adjacent two-vertex neighbourhood from a cyclically five-edge-connected minimal counterexample. If all three zero-vertex reconnections are valid smaller bridgeless graphs and `P` is globally `i`-routed, then one of:

1. `P` has a transition split or serial decomposition;
2. the original graph has a smaller cyclic separator;
3. a connected-cycle switch produces a state in `K_i`;
4. `P` is a bounded direct-pairing carrier;
5. the original cap glues after all.

This is now the unique local composition target left by equality/DDD inverse expansion.

---

## 12. Trust boundary

### Exact here

- the direct-pairing profiles `J_i={A,B_i,C_i}`;
- the cap profiles `K_i` and disjointness `J_i cap K_i=empty`;
- three-reconnection forcing when all smaller closures are soluble;
- complete finite classification of Kempe-closed cap-blocking profiles;
- decomposition into the two outer `P_3` components `J_i,L_i`;
- unique global route `M_i` on both possible profiles;
- unification of equality, adjacent-root, and DDD failures as one fixed-route sector.

### Still open

- category safety or separator extraction simultaneously for all three reconnections;
- elimination of the globally fixed-route outer sector in the local adjacent-pair setting;
- the individual universal full-cap theorem;
- the global descent theorem combining all local reductions;
- global five-support existence;
- canonical acceptance, independent audit, Lean verification, manuscript, release, and publication status.
