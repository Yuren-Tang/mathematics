# Active weld diagonals admit a bounded six-leaf predecessor-order lift

## Research Lead local source-fidelity theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `MARKED_WELD_PACHNER_OVERLAP_SCOPE_V1.md`;
- `WELD_RELATION_FIRST_EXIT_V1.md`;
- `WELD_B_ORBIT_SWITCH_AND_MOBILE_MARK_GRAPH_V1.md`;
- the ordinary six-leaf NNI/Pachner tree graph.

**Status:** exact bounded local lift for the sole `2--2` overlap at which pointwise weld-edge lineage fails. Let one reconnecting weld edge be the active diagonal of a lower-order root flip. Insert the equal-face weld before and after that flip. The two predecessor-order expansions have the same ordered six-port boundary. Exhaustive six-leaf topology analysis, together with explicit split paths, gives:

- if the transported weld pair remains in the adjacent-root orbit `B`, the two expansions are connected by a root-valued NNI history of length at most six;
- if the active flip is the first `B -> C` exit, they are connected by a length-five history carrying at most one co-root edge, and the final co-root is exactly the expected missing-index first-exit atom;
- no zero, two-defect state or new coefficient type occurs.

Thus an active marked diagonal does not destroy source-level continuation fidelity. It is not pointwise mark preservation; it is a bounded mobile-envelope lift on the full six-port region.

This theorem does not alone prove the nested return rank, support-switch compatibility, marked-central cancellation pop, R2.7, cap restoration or five-CDC.

---

## 1. Normal form for one active diagonal

Use support indices

\[
a,b,c,d,e
\]

and normalize the lower-order root flip to

\[
\boxed{p=ab\longleftrightarrow s=cd.}
\]

The four ordered exterior roots are

\[
A=ac,
\qquad
B=bc,
\qquad
D=ad,
\qquad
E=bd.
\]

Let the other reconnecting weld edge have root

\[
q\in R_5,
\qquad
q\ne p,
\qquad
|q\cap p|=1.
\]

Split that edge into its two ordered incidences

\[
X=q_L,
\qquad
Y=q_R,
\]

both carrying the root `q`.

The common ordered six-port boundary is therefore

\[
\boxed{(A,B,X,Y,D,E)=(ac,bc,q,q,ad,bd).}
\]

Its total sum is zero because

\[
A+B=D+E=ab=p,
\qquad
X+Y=0.
\]

---

## 2. The two endpoint expansions

### Before the lower-order flip

Insert the equal-face pair along the two lower-order edges `p,q`. The four internal vertices form the caterpillar

\[
AB\mid X\mid Y\mid DE.
\]

Its three internal splits are

\[
\boxed{
\mathcal T_p=
\{AB,\ ABX,\ DE\}.
}
\]

The corresponding internal values are

\[
p,\quad p+q,\quad p,
\]

all roots because `(p,q)` is in `B`.

### After the lower-order flip

The active diagonal is now `s=cd`. Expanding along `s,q` gives

\[
AD\mid X\mid Y\mid BE,
\]

with split set

\[
\boxed{
\mathcal T_s=
\{AD,\ ADX,\ BE\}.
}
\]

Its internal values are

\[
s,\quad s+q,\quad s.
\]

Thus:

- if `(s,q)` is in `B`, `T_s` is root-valued;
- if `s` is disjoint from `q`, `s+q` is one co-root and `T_s` is the standard first-exit state.

The active-overlap problem is to connect `T_p` and `T_s` at predecessor order while fixing all six exterior incidences.

---

## 3. Split notation and the six-leaf NNI graph

For a six-leaf unrooted binary tree, each of its three internal edges determines one nontrivial split of the leaf set. We record the smaller side of each split; in a `3|3` tie use the displayed side. A triple of pairwise compatible splits determines the labelled tree uniquely.

Two such trees are adjacent by one NNI exactly when their split triples have two splits in common and differ in the third.

There are exactly

\[
\boxed{105}
\]

labelled unrooted binary trees on six fixed leaves, and their NNI graph has

\[
\boxed{315}
\]

edges; every vertex has degree six.

For a split `S`, its internal edge value is

\[
\lambda(S)=\sum_{z\in S}\lambda(z)
\]

over `E_5`. Since the total boundary sum is zero, either side gives the same value.

---

## 4. Root-preserving active lift: first good incidence type

Take the representative

\[
q=ac=A.
\]

Then `(s,q)=(cd,ac)` remains in `B`.

The following is a six-NNI path from `T_p` to `T_s`:

\[
\begin{aligned}
&\{AB,ABX,DE\}\\
\to{}&\{ABX,BX,DE\}\\
\to{}&\{ADE,BX,DE\}\\
\to{}&\{AD,ADE,BX\}\\
\to{}&\{AYD,AD,BX\}\\
\to{}&\{AYD,AD,BE\}\\
\to{}&\{AXD,AD,BE\}.
\end{aligned}
\]

The final triple is exactly `T_s`, because `AXD=ADX`.

The internal values at the seven stages are respectively

\[
\begin{array}{c|c}
\text{stage}&\text{three internal values}\\
\hline
0&(ab,bc,ab)\\
1&(bc,ab,ab)\\
2&(bc,ab,ab)\\
3&(cd,bc,ab)\\
4&(ad,cd,ab)\\
5&(ad,cd,cd)\\
6&(ad,cd,cd).
\end{array}
\]

Every value is a root. Hence the complete path is root-valued.

The mirror case `q=bd` has the same six-step disposition after reversing the ordered six-port picture.

---

## 5. Root-preserving active lift: second good incidence type

Take

\[
q=ad=D.
\]

Again `(s,q)=(cd,ad)` is in `B`.

A five-NNI path is

\[
\begin{aligned}
&\{AB,ABX,DE\}\\
\to{}&\{ABX,AX,DE\}\\
\to{}&\{AX,AXY,DE\}\\
\to{}&\{AX,AXY,BE\}\\
\to{}&\{AX,AXD,BE\}\\
\to{}&\{AXD,AD,BE\}.
\end{aligned}
\]

Its internal values are

\[
\begin{array}{c|c}
\text{stage}&\text{three internal values}\\
\hline
0&(ab,bd,ab)\\
1&(bd,cd,ab)\\
2&(cd,ac,ab)\\
3&(cd,ac,cd)\\
4&(cd,ac,cd)\\
5&(ac,cd,cd).
\end{array}
\]

Again every value is a root.

The mirror case `q=bc` has the same five-step disposition.

Together Sections 4--5 cover all four roots `q` which meet both `p=ab` and `s=cd`.

---

## 6. First `B -> C` exit

Take the representative

\[
q=ae.
\]

It meets `p=ab` but is disjoint from `s=cd`. The same five-topology pattern as Section 5 gives

\[
\begin{aligned}
&\{AB,ABX,DE\}\\
\to{}&\{ABX,AX,DE\}\\
\to{}&\{AX,AXY,DE\}\\
\to{}&\{AX,AXY,BE\}\\
\to{}&\{AX,AXD,BE\}\\
\to{}&\{AXD,AD,BE\}.
\end{aligned}
\]

The internal values are now

\[
\begin{array}{c|c}
\text{stage}&\text{three internal values}\\
\hline
0&(ab,be,ab)\\
1&(be,ce,ab)\\
2&(ce,ac,ab)\\
3&(ce,ac,cd)\\
4&(ce,Q_b,cd)\\
5&(Q_b,cd,cd).
\end{array}
\]

Thus:

1. Stages `0--3` are fully root-valued.
2. Stages `4--5` contain exactly one co-root edge.
3. The co-root is
   \[
   \boxed{Q_b=ae+cd,}
   \]
   whose missing index is the nonshared endpoint `b` of the old marked root `ab`.
4. The final topology is exactly the failed expansion along `s,q`.

The case `q=be` is the mirror image and produces `Q_a`.

No all-root path reaches the failed endpoint: among the 105 trees, the root-valued sector for this boundary has 18 vertices, and the target lies outside it. Allowing at most one non-root edge gives a connected path of minimum length five. This finite fact is supplementary; the displayed path is the controlling proof.

---

## 7. Complete six-case census

For the six possible roots `q` adjacent to `p=ab`, the exact shortest dispositions are:

\[
\begin{array}{c|c|c|c}
q&\text{relation to }s=cd&\text{shortest length}&\text{maximum persistent defects}\\
\hline
ac&B&6&0\\
ad&B&5&0\\
ae&C&5&1\\
bc&B&5&0\\
bd&B&6&0\\
be&C&5&1.
\end{array}
\]

Every one-defect state carries a co-root; zero never appears.

### Theorem 7.1 — active-diagonal six-leaf lift

Let one weld-admissible output edge be the active central diagonal of a lower-order root-valued `2--2` flip. Inflate the move by the intended inverse equal-face insertion along that edge and the other weld edge.

Then the two predecessor-order endpoint expansions are joined, relative to the complete ordered six-port boundary, by:

1. a root-valued NNI path of length at most six if the transported pair remains in `B`;
2. a path of length five with at most one co-root edge if the move is the first `B -> C` exit.

In the second case the final atom is exactly the ordinary missing-index co-root predicted by the mobile-weld coefficient table.

---

## 8. Source-category safety

Every intermediate local topology is a connected four-vertex cubic tree on the same six exterior incidences.

In the ordinary six-port branch:

- every local NNI preserves cubicity;
- every internal edge joins distinct local vertices, so no local loop is created;
- the local replacement remains connected on the same boundary;
- every edge value is nonzero, being a root or the unique co-root;
- a bridge in an abelian-group flow must carry zero, hence the complete connected output remains bridgeless.

Any pre-existing identification of exterior incidences which creates a loop, parallel two-vertex collapse or smaller separator belongs to the already accepted bounded/category branch and is not an unbounded exception to the theorem.

---

## 9. Consequence for nested return

The old pointwise statement was false:

\[
\text{active old diagonal }ab
\not\mapsto
\text{the same marked edge after }ab\leftrightarrow cd.
\]

The correct source statement is the bounded mobile-envelope lift:

\[
\boxed{
\text{one lower-order active-diagonal step}
\Longrightarrow
\text{at most six predecessor-order NNIs}
\text{ or one standard first-exit atom}.
}
\]

Therefore the active flip has genuinely been crossed before a first `B -> C` pop is returned. The residual atom lies after that child-history step, not before it. This supplies the source-level strict-prefix datum needed by the nested-frame architecture for active `2--2` overlaps.

It does not yet supply:

- support-pair switch lifting;
- the crossed exchange frame-pop theorem;
- mark-consuming `2--0` continuation normalization;
- one complete finite mixed-state local rank.

---

## 10. Assurance boundary

### Exact here

- the common six-port boundary of the before/after expansions;
- the two endpoint split triples;
- the complete 105-tree/315-edge NNI census;
- explicit root-valued paths for all `B`-preserving active flips;
- explicit one-co-root paths for both first `B -> C` active flips;
- the exact missing-index co-root identification;
- source-category safety in the ordinary branch;
- predecessor-order crossing of the active lower-order history step.

### Not claimed

- pointwise preservation of an active marked edge;
- arbitrary mobile-envelope return;
- support-switch or nested-cancellation compression;
- the concrete local rank required by the PDL stack theorem;
- R2.7 completion, cap restoration or universal five-CDC;
- PDL reconstruction, independent audit, Lean verification, manuscript integration, curation, release, arXiv, DOI, peer review or publication.
