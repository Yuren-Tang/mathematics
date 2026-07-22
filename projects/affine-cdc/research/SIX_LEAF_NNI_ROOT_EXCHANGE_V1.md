# Six-leaf NNI exchange has one root branch and one equality/DDD branch

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `34458640966187a58cd607b870b488d320493b96`  

**Parents:**

- `projects/affine-cdc/research/SIX_LEAF_TOPOLOGY_ENERGY_TRIALITY_V1.md`;
- `projects/affine-cdc/research/FOUR_ROOT_INTERFACE_TYPE_T_SQUARE_V1.md`;
- `projects/affine-cdc/research/INVERSE_DIPOLE_KEMPE_RESCUE_V1.md`;
- `projects/affine-cdc/research/PIVOT_CHANGE_SIX_PORT_STAR_COMPLETION_V1.md`.

**Status:** exact local exchange theorem. Around one internal edge of a root-valued six-leaf cubic tree, the three NNI topologies have central labels equal to the three pairing sums of four incident branch roots. The four-root pairing-sum classification implies that if one topology is root-valued, exactly one of the other two topologies is root-valued with the same complete boundary word. The remaining topology has central label zero or co-root. Thus every root topology has one canonical root-preserving NNI direction at every internal edge, while the opposite direction is exactly the equality/DDD inverse-dipole branch. Exhaustive ordered-boundary profiles confirm that adjacent tree profiles intersect in exactly half their states and that no distinct six-leaf tree profile contains another.  

**Not implied:** that the canonical NNI is a legal operation on a fixed source graph, that a root cover of an alternative topology automatically transfers to the original topology, strict graph descent, global induction, canonical acceptance, Lean verification, manuscript integration, or the global five-support theorem.

---

## 1. Four branch values at an NNI edge

Let `T` be a cubic tree and let `e=uv` be one internal edge. Removing `e` exposes four rooted branches:

\[
A,
\quad B
\]

at `u`, and

\[
C,
\quad D
\]

at `v`.

Let the `E_5` boundary sums carried by the four branch incidences be denoted by the same letters.

In a root-valued completion,

\[
A,B,C,D\in R_5
\]

and conservation gives

\[
\boxed{A+B+C+D=0.}
\]

The three unrooted binary resolutions of these four branches are:

\[
AB\mid CD,
\qquad
AC\mid BD,
\qquad
AD\mid BC.
\]

Their central edge labels are respectively

\[
\boxed{
p=A+B,
\qquad
q=A+C,
\qquad
r=A+D.
}
\]

They satisfy

\[
\boxed{p+q+r=0.}
\]

---

## 2. Pairing-sum classification

For four roots with total sum zero, the three pairing sums have one of the exact weight patterns

\[
(0,0,0),
\qquad
(0,2,2),
\qquad
(0,4,4),
\qquad
(2,2,4).
\]

Therefore:

### Theorem 2.1 — two-root rule

If one of

\[
p,q,r
\]

is a root, then exactly one of the other two is a root.

The third has weight:

- zero in the pattern `(0,2,2)`;
- four in the pattern `(2,2,4)`.

### Proof

The only pairing-sum patterns containing a weight-two entry are `(0,2,2)` and `(2,2,4)`. Both contain exactly two weight-two entries. ∎

### Corollary 2.2 — no three-way root resolution

The three NNI topologies can never all be root-valued for the same four branch roots.

Likewise, exactly one root-valued NNI topology is impossible: root-valued resolutions occur in pairs.

---

## 3. Canonical root-preserving NNI

Assume the current topology `AB|CD` is root-valued, so

\[
p=A+B\in R_5.
\]

By Theorem 2.1, exactly one of

\[
q=A+C,
\qquad
r=A+D
\]

is a root.

### Theorem 3.1 — unique root-preserving exchange

At every internal edge of a root-valued cubic tree, exactly one of the two NNI alternatives is root-valued with the same complete external boundary labels.

The root values on every unchanged edge and branch are preserved; only the central split changes from `p` to the unique root among `{q,r}`.

Thus every root-valued topology has one canonical root-preserving NNI direction at each internal edge.

---

## 4. The opposite direction is equality or DDD

Let `h` be the non-root element among `{q,r}`.

Exactly one of:

### Equality branch

\[
\boxed{h=0.}
\]

The non-root NNI topology contains one zero internal edge. This is the equality/identity singular fibre.

### DDD branch

\[
\boxed{|h|=4.}
\]

The non-root NNI topology contains one co-root internal edge. Its two crossed root resolutions are precisely the two root-valued NNI topologies.

### Theorem 4.1 — NNI/inverse-dipole identification

The local NNI triality and the inverse-dipole lift table are the same coefficient object:

\[
\boxed{
\text{two root resolutions}
\quad+\quad
\text{one equality or DDD state}.}
\]

No fourth local exchange state occurs.

---

## 5. NNI triangles and profile parity

Fix a labelled six-leaf topology and one internal edge. The current topology and its two NNI alternatives form a triangle in the full NNI graph.

For an ordered conserved six-root boundary word satisfying the common branch conditions, let

\[
\epsilon_i\in\{0,1\}
\]

record whether the `i`-th topology in this triangle is root-valued.

### Corollary 5.1 — even triangle rule

\[
\boxed{
(\epsilon_0,\epsilon_1,\epsilon_2)
\in
\{(0,0,0),(1,1,0),(1,0,1),(0,1,1)\}.}
\]

In particular,

\[
\boxed{
\epsilon_0+\epsilon_1+\epsilon_2=0
\pmod2.}
\]

Thus every boundary word selects either no edge or one edge of every NNI triangle.

This is the topology-level form of the binary tight-triality relation.

---

## 6. Exact ordered-boundary profile census

Let

\[
\mathcal W_6
=
\{(r_1,\ldots,r_6)\in R_5^6:
 r_1+\cdots+r_6=0\}.
\]

There are

\[
\boxed{|\mathcal W_6|=62560}
\]

ordered conserved six-root boundary words.

For a labelled six-leaf tree `T`, let

\[
\Sigma_6(T)\subseteq\mathcal W_6
\]

be its complete root-valued boundary profile.

Exact enumeration of all `105` labelled topologies gives:

### Theorem 6.1 — equal profile sizes

\[
\boxed{
|\Sigma_6(T)|=12960
\qquad
\text{for every labelled tree }T.}
\]

### Theorem 6.2 — adjacent half intersection

If `T,T'` differ by one NNI move, then

\[
\boxed{
|\Sigma_6(T)\cap\Sigma_6(T')|=6480.
}
\]

Thus exactly half the boundary states of either topology transfer root-valuedly across a specified NNI edge.

### Theorem 6.3 — triangle `0/2` rule

For every one of the `105` NNI triangles:

- `19440` ordered boundary words extend through exactly two of its three topologies;
- `43120` extend through none;
- none extend through exactly one or all three.

This is the exhaustive profile version of Corollary 5.1.

---

## 7. No tree is a universal profile reducer

The `105` complete profiles are pairwise distinct.

Because all have the same cardinality `12960`, one has:

### Theorem 7.1 — profile incomparability

For distinct labelled six-leaf trees `T,T'`,

\[
\boxed{
\Sigma_6(T)\not\subseteq\Sigma_6(T'),
\qquad
\Sigma_6(T')\not\subseteq\Sigma_6(T).
}
\]

Thus no different six-leaf tree topology is a universal boundary-profile reducer for another.

### Strategic consequence

A same-size topology replacement cannot be justified by local state coverage alone.

Any successful physical NNI argument must use at least one of:

- the actual exterior linkage/route semantics;
- a Kempe or root-fibre switch changing the boundary state;
- graph descent through a dipole cancellation;
- a separator exposed by failure of the exchange;
- a bounded equality/DDD singular fibre.

This eliminates the tempting but invalid quantifier swap

\[
\forall\sigma\ \exists T'
\quad\Longrightarrow\quad
\exists T'\ \forall\sigma.
\]

---

## 8. Connected root-topology sector for the pivot boundary

For the standard pivot boundary

\[
(12,35,45\mid25,34,15),
\]

exactly twenty labelled six-leaf trees are root-valued.

Under canonical root-preserving NNI moves their induced graph has:

\[
20\text{ vertices},
\qquad
30\text{ edges},
\qquad
\deg=3,
\]

and is connected.

### Interpretation

Once one root-valued topology for this fixed boundary is available, every other root-valued topology in the same twenty-state sector is reachable through boundary-preserving root-valued NNI exchanges.

This does not reach a topology outside the profile, but it proves that the root sector itself has no internal reconfiguration obstruction.

---

## 9. Relation to the final composition bridge

The NNI theorem separates the remaining physical burden cleanly.

### Coefficient side — complete

For a fixed four-branch boundary:

- root exchange is unique;
- the opposite exchange is equality or DDD;
- the triality parity is exact;
- no universal tree-profile inclusion exists.

### Source side — still required

Given a desired root-preserving NNI exchange, prove one of:

1. it is realised by an exterior linkage or local source surgery;
2. dipole cancellation gives strict graph descent and inverse expansion chooses the root branch;
3. failure exposes a small separator;
4. failure localises the equality/DDD singular branch;
5. a horizontal Kempe switch changes the boundary into the original topology profile.

Thus the remaining theorem is genuinely composition/linkage, not finite coefficient classification.

---

## 10. Trust boundary

### Exact here

- the three central NNI labels `p,q,r`;
- the two-root pairing-sum rule;
- uniqueness of the root-preserving NNI direction;
- equality/DDD classification of the opposite direction;
- even triality parity on every NNI triangle;
- the `62560` ordered conserved boundary count;
- profile size `12960` for all `105` trees;
- adjacent intersection size `6480`;
- the exhaustive triangle `0/2` profile rule;
- pairwise distinction and incomparability of all tree profiles;
- connectivity of the twenty-state root sector for the standard pivot boundary.

### Finite/computational boundary

The ordered-profile counts, profile distinctness, and connected-sector statement were exhaustively enumerated. The local two-root rule and triality classification are theorem-level consequences of the four-root pairing-sum classification.

### Still open

- physical source realisation of the canonical NNI exchange;
- separator extraction when it is blocked;
- profile transfer from a smaller reconnection graph;
- elimination of the equality/DDD singular exchange in the complete ambient lock;
- global well-founded induction;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
