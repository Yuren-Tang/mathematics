# Two boundary constraints have one crossed component obstruction, which exchanges the defect

## Research Lead two-boundary switching dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `812b39ecf5392004f2b155d8f56abc80c7d89967`.

**Parents:**

- `INVERSE_DIPOLE_KEMPE_RESCUE_V1.md`;
- `WELD_B_ORBIT_SWITCH_AND_MOBILE_MARK_GRAPH_V1.md`;
- `WELD_RELATION_FIRST_EXIT_V1.md`;
- `ADAPTIVE_C6_WELD_CHANNEL_MINIMIZATION_V1.md`.

**Status:** exact component-linear theorem. Fix one support-pair channel which is a one-switch rescue channel for an outer equality/DDD pair and is simultaneously eligible on both roots of an internal weld-admissible `B` pair. Component switches can satisfy outer one-sided rescue and weld simultaneous/no switching except in one precise configuration: the outer pair and weld pair are separated by the same two channel components, each component containing exactly one edge from each pair. In that unique crossed kernel, switching one component changes the outer pair from `A/C` to `B` and the weld pair from `B` to `A/C`. Thus it transports one singular inverse-dipole obstruction from the outer boundary to the inner weld boundary without creating a second defect or new coefficient type.

---

## 1. Two marked pairs in one even channel

Let `H_h` be one support-pair symmetric-difference subgraph. It is even, so each connected component may be switched independently.

Mark two ordered edge pairs:

\[
O=(o_0,o_1)
\]

and

\[
W=(w_0,w_1).
\]

Assume:

1. the outer pair `O` is in equality or DDD relation `A/C`;
2. `h` is a rescue channel for `O`, so switching exactly one of `o_0,o_1` changes `O` to `B`;
3. the weld pair `W` is in `B`;
4. both weld roots are eligible for `h`, so switching both or neither preserves `B`, while switching exactly one changes `W` to `A/C`.

Let

\[
c(e)
\]

denote the connected component of `H_h` containing a marked edge `e`.

A component-switch choice is one Boolean variable

\[
x_C\in\mathbf F_2
\]

for every component `C`.

---

## 2. The two linear requirements

Outer rescue requires

\[
\boxed{
x_{c(o_0)}+x_{c(o_1)}=1.}
\]

Weld preservation requires

\[
\boxed{
x_{c(w_0)}+x_{c(w_1)}=0.}
\]

All equations are over `F_2`.

### Preliminary outer condition

If

\[
c(o_0)=c(o_1),
\]

then `h` is not a separating outer rescue channel. Hence assume throughout that the two outer components are distinct.

---

## 3. Complete compatibility theorem

### Theorem 3.1 — unique inconsistent component pattern

The two equations of Section 2 are simultaneously solvable unless:

\[
\boxed{
\{c(o_0),c(o_1)\}
=
\{c(w_0),c(w_1)\}
}
\]

and the weld edges are also separated.

Equivalently, incompatibility occurs exactly when there are two relevant components `C_0,C_1` such that, after possibly exchanging indices,

\[
\boxed{
C_0\supset\{o_0,w_0\},
\qquad
C_1\supset\{o_1,w_1\}.
}
\]

Every relevant component contains one outer marked edge and one weld marked edge.

### Proof

If the weld edges are in the same component, the weld equation is identically zero and any one-sided outer rescue works.

Assume the weld edges are separated. Each equation is then the sum of two distinct component variables. Two affine equations over `F_2` with right sides `1` and `0` are inconsistent exactly when their left sides are identical. This is precisely equality of the two unordered component pairs. ∎

---

## 4. Constructive switches in every compatible case

If Theorem 3.1's obstruction is absent, one may choose switches explicitly.

### Weld pair in one component

Switch the component containing exactly one outer edge. If it also contains the common weld component, add any second component containing neither outer edge when necessary; the weld parity remains even.

### Four distinct relevant components

Switch one outer component. If that toggles exactly one weld component, also switch the other weld component.

### Three relevant components

One component identity is shared between the two pairs, but the unordered component pairs differ. Switch the outer-only component or the appropriate shared-plus-weld-only pair.

In all cases:

\[
\boxed{
O:A/C\longrightarrow B,
\qquad
W:B\longrightarrow B.
}
\]

No coefficient-specific case split beyond the parity equations is needed.

---

## 5. The crossed exchange kernel

Assume the unique obstruction:

\[
C_0\supset\{o_0,w_0\},
\qquad
C_1\supset\{o_1,w_1\}.
\]

Switch only `C_0`. Then:

\[
\boxed{
O:A/C\longrightarrow B
}
\]

because exactly one outer edge changes, while

\[
\boxed{
W:B\longrightarrow A/C
}
\]

because exactly one weld edge changes.

### Theorem 5.1 — one-defect exchange

A switch on either component of the crossed kernel exchanges the location of the unique inverse-dipole obstruction:

\[
\boxed{
(\text{outer singular},\text{weld regular})
\longrightarrow
(\text{outer regular},\text{weld singular}).
}
\]

The switched weld failure is:

- equality `A` for the unique equality channel `h=p+q` of the current weld triangle;
- DDD `C` for either of the other two common eligible weld channels.

No second singular edge and no new coefficient type occurs.

### Switching both components

Switching `C_0` and `C_1` preserves the relation types:

\[
O:A/C\longrightarrow A/C,
\qquad
W:B\longrightarrow B.
\]

It changes the support labels but does not repair the outer obstruction.

Thus the crossed kernel offers exactly:

1. defect exchange by one component;
2. relation-preserving transport by both components;
3. no simultaneous outer repair and weld preservation in that channel.

---

## 6. Source topology after cutting the marked edges

Each `H_h` component is a cycle in the closed root-valued graph. In the crossed kernel each relevant cycle contains:

- one outer marked edge;
- one weld marked edge.

Cutting all four marked edges opens the two cycles into four paths joining the outer four-incidence boundary to the weld four-incidence boundary. Hence the obstruction is a bounded two-boundary response object, not a general unstructured full-channel lock.

Its physical data are:

\[
\boxed{
\text{two channel cycles}
+
\text{one outer edge and one weld edge on each cycle}
+
\text{their cyclic incidence orders}.}
\]

This is the exact two-boundary exchange kernel.

---

## 7. Causal interpretation in cancellation return

In the cancellation-reentry setting:

- the outer singular pair belongs to the currently active lower-order return frame;
- the weld pair is the boundary through which that frame must return to its parent order.

Therefore Theorem 5.1 moves the singular obstruction from the active outer boundary to the parent weld boundary.

The result is exactly the first-`B`-exit zero/co-root atom of `WELD_RELATION_FIRST_EXIT_V1.md`, now with a source witness:

\[
\boxed{
\text{two crossed channel components connecting the two return boundaries}.}
\]

The failing switch has been performed and the outer relation is solved. What remains is one internal weld atom on a strictly earlier/topologically restored source stage.

---

## 8. What remains for a global rank

The defect exchange is directed by the nesting of return boundaries, but a theorem must still prove that repeated exchanges cannot cycle through newly created cancellation frames.

A sufficient rank may record a stack of return frames. Each exchange should:

1. solve and remove the active outer boundary obligation;
2. pop that frame;
3. create at most one ordinary atom at the parent weld;
4. resume the parent at a strict shorter causal prefix.

The local theorem proves Items 1 and 3. The exact frame-pop and prefix comparison must be established in the contextual state definition.

---

## 9. Exact next theorem

### Target 9.1 — exchange-frame pop theorem

Let one lower-order return frame terminate through the crossed exchange kernel. Prove that after switching one component and inserting the now-root-valued outer cap:

1. the lower-order frame has no remaining terminal obligation;
2. its internal weld `A/C` state is exactly one first-failure atom on the parent source graph;
3. every child-only history mark can be discarded;
4. the parent remaining prefix is strictly shorter than before the cancellation frame was opened.

If all four statements hold, crossed exchange becomes a strict stack-pop transition and cannot participate in a same-frame recurrence.

---

## 10. Trust boundary

### Exact here

- the two component-switch equations;
- the unique crossed inconsistent partition;
- explicit compatible switch choices in all other cases;
- exact one-defect exchange in the crossed kernel;
- preservation of a single zero/co-root alphabet;
- the two-boundary cycle/path interpretation;
- identification of the new atom with the weld first-exit state.

### Not proved

- the exchange-frame pop theorem;
- strict comparison with the parent causal prefix;
- nested stack well-foundedness;
- inherited-flow relative return or cancellation macro-return;
- R2 global return, cap restoration, or global five-support closure;
- independent audit, curation, Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.
