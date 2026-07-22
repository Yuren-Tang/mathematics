# A forced pair in a binary tight three-class route minor gives a local cocircuit

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `1af6a39306277bbfd84da4a504e7469de1cc1905`  

**Parents:**

- `projects/affine-cdc/research/PIVOT_CHANGE_SIX_PORT_STAR_COMPLETION_V1.md`;
- `projects/affine-cdc/research/LAGRANGIAN_FORCED_COORDINATE_SMALL_SUPPORT_V1.md`;
- the transition-matroid / tight-multimatroid model of a cubic line graph;
- the physical cycle--cut response form.

**Status:** exact finite theorem for the three transition classes of one universal six-port route carrier. In a binary tight three-matroid minor, restrict each transition class to the two states belonging to the left--right matching slice. If some transversal using the distinguished bad state is a basis and every transversal using the corresponding good state is dependent, then the bad state is a coloop of the restricted sheltering matroid. Lifting the singleton cocircuit through the deleted transitions and using even parity on every transition triple gives a two-element cocircuit inside one physical edge triple. In the physical line-graph response this is a one-edge cut or one-edge cycle, hence impossible in the bridgeless loopless category.  

**Not implied:** that actual six-port composition compatibility has already been calibrated as basis-transversal feasibility in the contracted tight three-matroid, completion of the global induction, canonical acceptance, Lean verification, manuscript integration, or the global five-support theorem.

---

## 1. Three transition classes

Let

\[
\Omega_i=\{L_i,X_i,Y_i\},
\qquad i=0,1,2,
\]

be three skew classes of a binary sheltering matroid `M` for a tight three-matroid.

For the universal pivot-change route triangle, the classes have the following interpretation.

- `Omega_0` is the switch at the distinguished terminal pair `s,t`;
- `Omega_1` is the switch at the terminal pair `x,z`;
- `Omega_2` is the switch at the terminal pair `w,y`.

The exact route table uses only

\[
\{L_0,Y_0\},
\qquad
\{X_1,Y_1\},
\qquad
\{X_2,Y_2\}.
\]

The excluded transitions are

\[
D=\{X_0,L_1,L_2\}.
\]

Write

\[
N=M\setminus D.
\]

The eight transversals of the three retained pairs split into:

### Bad / forced-backbone transversals

\[
\mathcal B
=
\bigl\{
\{L_0,U_1,U_2\}:
U_1\in\{X_1,Y_1\},
U_2\in\{X_2,Y_2\}
\bigr\}.
\]

These are the transition settings whose terminal matching contains the pair

\[
s\mathbin{-}t.
\]

### Good / star transversals

\[
\mathcal G
=
\bigl\{
\{Y_0,U_1,U_2\}:
U_1\in\{X_1,Y_1\},
U_2\in\{X_2,Y_2\}
\bigr\}.
\]

These are the four root-valued star routes avoiding `s--t`.

The third state `X_0` and the local states `L_1,L_2` belong to route partitions with a same-side terminal pair and are deleted in the cross-route minor.

---

## 2. Binary representation and tightness

Because `M` shelters a binary tight three-matroid, after contraction of any already fixed exterior independent set the three classes admit a binary representation in which

\[
L_i+X_i+Y_i=0
\qquad(i=0,1,2).
\]

If one transversal in `mathcal B` is a basis, the contracted cap minor has rank three. Thus all column vectors may be represented in

\[
\mathbf F_2^3.
\]

Tightness is the following local condition.

Let `S` be an independent subtransversal choosing one element from two skew classes and omitting the third class `Omega_i`. Then exactly one element of `Omega_i` lies in the span of `S`; the other two extend `S` to bases.

This is the order-three form of the tightness axiom.

---

## 3. Forced-pair theorem

### Theorem 3.1 — coloop in the cross-route minor

Assume:

1. at least one bad transversal is a basis:
   \[
   \exists B\in\mathcal B,
   \qquad B\text{ a basis of }M;
   \]
2. no good transversal is a basis:
   \[
   \forall G\in\mathcal G,
   \qquad G\text{ dependent in }M.
   \]

Then

\[
\boxed{
L_0\text{ is a coloop of }N=M\setminus\{X_0,L_1,L_2\}.}
\]

Equivalently,

\[
\boxed{
\operatorname{rank}(N\setminus L_0)=2,
\qquad
\operatorname{rank}(N)=3.}
\]

Hence every basis of the restricted cross-route matroid contains `L_0`.

### Exact finite certificate

Every labelled binary representation is obtained by choosing two vectors in `F_2^3` for each skew class; the third is their sum. Therefore the complete labelled search space has

\[
8^6=262144
\]

assignments.

The enumeration applies the following exact filters.

1. the full represented matroid has rank three;
2. the order-three tightness axiom holds for every two-element subtransversal;
3. at least one bad transversal is a basis;
4. no good transversal is a basis.

Exactly

\[
2520
\]

representations survive. They split according to the number of bad bases as

\[
\begin{array}{c|cccc}
\#\text{ bad bases}&1&2&3&4\\
\hline
\#\text{ representations}&672&1008&672&168.
\end{array}
\]

In all `2520` representations,

\[
\operatorname{rank}(N\setminus L_0)=2.
\]

There are no counterexamples.

The count distribution is

\[
168(4,6,4,1),
\]

which is consistent with the four labelled bad transversals and their possible basis supports.

### Proof status

The theorem is exact by exhaustive enumeration of all binary labelled representations, including zero columns, parallel columns, and singular contracted skew classes. No simplicity assumption is used.

A coordinate-free proof should derive the same conclusion from tightness plus basis exchange; that proof is desirable for manuscript compression but is not required for the finite research certificate.

---

## 4. Cocircuit lift

Since `L_0` is a coloop of `N`,

\[
\{L_0\}
\]

is a cocircuit of `N`.

Cocircuits of a deletion minor are minimal nonempty restrictions of cocircuits of the original matroid. Hence there is a cocircuit

\[
C^*\in\mathcal C^*(M)
\]

such that

\[
C^*\setminus D=\{L_0\}.
\]

For a binary transition matroid, every cocycle meets each transition triple in even cardinality because

\[
L_i+X_i+Y_i=0.
\]

At `Omega_1` and `Omega_2`, the only deleted element is respectively `L_1` and `L_2`. Including either would require a second retained element from the same class, contradicting

\[
C^*\setminus D=\{L_0\}.
\]

Thus

\[
C^*\cap\Omega_1
=
C^*\cap\Omega_2
=
\varnothing.
\]

At `Omega_0`, the cocircuit contains `L_0`. The only deleted transition in that class is `X_0`, while `Y_0` is retained. Even parity therefore forces

\[
C^*\cap\Omega_0
=
\{L_0,X_0\}.
\]

Consequently:

### Theorem 4.1 — local two-transition cocircuit

\[
\boxed{
C^*=\{L_0,X_0\}.}
\]

The forced pair creates a cocircuit supported entirely inside the distinguished physical edge triple.

---

## 5. Physical interpretation

At one physical source edge `e_0`, write the transition triple as

\[
\{\ell_{e_0},x_{e_0}^0,x_{e_0}^1\}.
\]

Every nonzero even two-transition word on this triple has one of the physical response coordinates

\[
(z_{e_0},a_{e_0})
\in
\{(0,1),(1,0),(1,1)\}.
\]

If the local cocircuit has

\[
z_{e_0}=0,
\]

it belongs to the physical cut kernel and gives a cut supported on the single edge `e_0`. Thus `e_0` is a bridge.

If

\[
z_{e_0}=1,
\]

its physical cycle projection is the one-edge even subgraph `{e_0}`. Thus `e_0` is a loop.

Therefore:

### Corollary 5.1 — bridgeless loopless exclusion

A binary tight three-class route minor satisfying the hypotheses of Theorem 3.1 cannot occur in the transition matroid of a bridgeless loopless cubic source graph.

Indeed its forced pair would create either:

\[
\boxed{\text{a bridge}}
\]

or

\[
\boxed{\text{a loop}.}
\]

Both are excluded by the source category.

---

## 6. Relation to the naive cap-coordinate argument

The universal three-cherry route carrier has a cap-local three-edge bond. Therefore one must not identify a route transversal directly with a local cocycle word and apply the Lagrangian forced-coordinate theorem without contraction of the exterior transition semantics.

That naive identification can return only the artificial cap bond and says nothing about the original six-pole.

The tight-three-class theorem avoids this error:

1. fix / contract the exterior semantic set first;
2. retain the three genuine transition skew classes;
3. interpret compatible routes as basis transversals of the contracted sheltering matroid;
4. use tightness, not the artificial cap cut, to obtain the local cocircuit.

Thus the theorem isolates the exact correct calibration target.

---

## 7. Exact remaining calibration

To consume Corollary 5.1 in the five-support proof, establish the following statement.

### Target 7.1 — physical basis-transversal calibration

For one support-minimal pivot-change carrier with fixed exterior side semantics, construct an exterior subtransversal `S` in the transition matroid such that:

1. `S` is independent;
2. after contracting `S` and deleting transitions excluded by the left--right route slice, the three pivot-cap switch classes form the tight minor of Sections 1--2;
3. a six-port route is composition-compatible exactly when its retained three-element transversal completes `S` to a basis;
4. the four root-valued star routes are the `Y_0` transversals;
5. the two forced-backbone routes are the `L_0` transversals.

Then Theorem 3.1 and Corollary 5.1 eliminate the forced-backbone branch immediately.

### Trust boundary

The finite theorem does not assert Target 7.1. A route partition may contain additional closed circuits, and those must be absorbed into `S` or shown irrelevant before basis feasibility is exact.

This is now the only distinction between:

\[
\text{route compatibility}
\]

and

\[
\text{basis-transversal compatibility}.
\]

---

## 8. Revised probability assessment

The forced-backbone branch has been reduced from an unbounded source-composition problem to one of two sharply separated outcomes.

1. **Basis calibration succeeds.**  
   Tightness gives a forbidden one-edge bridge/loop cocircuit, so the branch closes.
2. **Basis calibration fails because extra closed circuits remain.**  
   The failure itself is a nontrivial circuit component disjoint from the six route terminals. Such a component should enter the existing scalar-cycle, Tait-band, or laminar-enclosure descent.

Thus even failure of exact basis calibration has a prescribed structural output; it does not reopen the finite obstruction alphabet.

---

## 9. Reliability boundary

### Exact here

- the three retained transition pairs of the universal route triangle;
- the bad and good transversal families;
- the complete binary tight-representation enumeration;
- the coloop conclusion in every one of the `2520` surviving representations;
- the lift to the two-transition cocircuit `{L_0,X_0}`;
- bridge/loop interpretation of one-edge physical support;
- identification of the artificial cap-bond pitfall.

### Still open

- physical basis-transversal calibration after contracting exterior side semantics;
- removal or localisation of additional closed route circuits;
- direct coordinate-free proof of Theorem 3.1;
- global well-founded induction;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
