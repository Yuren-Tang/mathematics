# Support-pair switches lift through raw insertion with at most one atom

## Research Lead innermost-bubble local theorem v2

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Supersedes:** v1 of this file.

**Parents:**

- `WELD_RELATION_FIRST_EXIT_V1.md`;
- `WELD_MARK_EQUAL_FACE_OVERLAP_V1.md`;
- the support-pair identity `A_h=F_i triangle F_j`;
- the raw insertion equation `x=p+q`.

**Status:** exact source-level lift of one ordinary support-pair component switch through a raw two-edge insertion, without assuming that the inserted central value is a root. Let the two marked lower-order edges carry roots `p,q`, and insert two cubic vertices with central `E_5` value `x=p+q`. The expanded state has at most one non-root edge, namely the central edge. If a lower-order channel component switch changes the marked edges with indicators `delta_p,delta_q`, lift its inherited edge set and add the inserted central edge exactly when `delta_p xor delta_q=1`. The lifted correction is even, preserves the flow equations, and changes the central value to the new raw sum

\[
(p+\delta_p h)+(q+\delta_q h).
\]

All noncentral edges remain roots. Hence every lower support-pair switch lifts to a predecessor-order history cell with at most one atom, for all `A/B/C` marked-pair relations.

---

## 1. Raw insertion

Let `H` carry a root-valued flow `lambda`, and let two distinguished edges `e_p,e_q` have root values

\[
p,q\in R_5.
\]

Split both edges, insert two cubic vertices and join them by one central edge. Assign

\[
\boxed{x=p+q\in E_5}
\]

to the central edge.

At both inserted vertices the incident values are

\[
(p,q,x),
\qquad
p+q+x=0.
\]

Thus the expanded assignment is an `E_5` flow. Every edge is root-valued except possibly the central edge:

\[
\begin{array}{c|c}
\text{relation of }p,q&x=p+q\\
\hline
p=q&0\\
p\sim q&\text{root}\\
p\perp q&\text{co-root}.
\end{array}
\]

Call this raw expanded state

\[
I(H,\lambda;e_p,e_q).
\]

---

## 2. One lower support-pair switch

Fix a root direction

\[
h=ij
\]

and one connected component

\[
Z\subseteq A_h(H)=F_i\triangle F_j.
\]

Switch `Z`, obtaining the lower-order root flow

\[
\lambda'=\lambda+h1_Z.
\]

Let

\[
\delta_p=1_{e_p\in Z},
\qquad
\delta_q=1_{e_q\in Z}.
\]

The returned marked roots are

\[
p'=p+\delta_p h,
\qquad
q'=q+\delta_q h.
\]

Because `Z` is a root channel component, every toggled lower-order edge remains a root.

---

## 3. Lifted correction subgraph

Construct an edge set

\[
\widehat Z\subseteq E(I(H))
\]

as follows.

1. Retain every edge of `Z` not equal to a marked edge.
2. If `delta_p=1`, retain both split half-edges descended from `e_p`.
3. If `delta_q=1`, retain both split half-edges descended from `e_q`.
4. Retain the inserted central edge exactly when
   \[
   \delta_p\oplus\delta_q=1.
   \]

### Lemma 3.1 — evenness

`widehat Z` is an even subgraph of the expanded source.

### Proof

At every old vertex, replacing a marked edge by its incident half-edge preserves the degree contributed by `Z`, so the degree remains even.

At either inserted vertex, the number of selected incident edges is

\[
\delta_p+\delta_q+(\delta_p\oplus\delta_q),
\]

which is even. ∎

Add `h` to every edge of `widehat Z`.

---

## 4. Exact lifted output

Every inherited noncentral edge in `widehat Z` is an edge of the lower channel component and changes to the root prescribed by `lambda'`.

The marked half-edge values become

\[
p'=p+\delta_p h,
\qquad
q'=q+\delta_q h.
\]

The central value becomes

\[
\begin{aligned}
x'
&=x+(\delta_p\oplus\delta_q)h\\
&=p+q+(\delta_p+\delta_q)h\\
&=(p+\delta_p h)+(q+\delta_q h)\\
&=p'+q'.
\end{aligned}
\]

Thus both inserted vertex equations remain valid.

### Theorem 4.1 — universal raw switch lift

The lifted assignment is exactly the raw insertion

\[
\boxed{I(H,\lambda';e_p,e_q).}
\]

Every noncentral edge is root-valued. The central edge is the only possible zero/co-root atom.

No assumption on the initial relation of `p,q` is required.

---

## 5. Relation-specific consequences

### Neither or both marked edges switched

If

\[
\delta_p=\delta_q,
\]

the central edge is not toggled. Its value remains

\[
x'=x.
\]

This includes:

- strict commutation when neither mark lies in `Z`;
- simultaneous switching when both lie in one component.

### Exactly one marked edge switched

If

\[
\delta_p\oplus\delta_q=1,
\]

the central edge is toggled by `h` and becomes the new pair sum.

If the initial pair is weld-admissible and both roots are common-channel eligible, then:

- `h=p+q` gives `x'=0`;
- the other two one-sided common channels give one co-root.

This recovers the equality/DDD first-exit table.

If only one marked root is channel-eligible, the new pair remains intersecting and `x'` is a root; the lifted correction is an ordinary root-valued switch passing through the central edge.

---

## 6. Component splitting and merging are harmless

In the root-valued `B` case, expanding the two marked edges may merge two lower channel components or split one component into two circuits. The controlling object is not one expanded connected component but the even edge set `widehat Z`.

Every finite even subgraph of a cubic graph is a disjoint union of circuits. When all values on `widehat Z` are channel-eligible, its circuit components may be switched successively and give the same result.

In a one-sided common-channel exit, the central edge is not root-channel eligible; the operation is instead the displayed `E_5` one-atom correction. Evenness still proves the vertex equations.

---

## 7. Complete source-lift table

For every lower root support-pair component switch:

\[
\boxed{
I(H,\lambda;e_p,e_q)
\longrightarrow
I(H,\lambda';e_p,e_q)
}
\]

is realised on the same predecessor-order topology by adding `h` on `widehat Z`.

The central relation may move among

\[
A\leftrightarrow B\leftrightarrow C,
\]

but the expanded state always has at most one non-root edge.

There is no new defect alphabet and no dependence on root/Kempe connectivity between unrelated flows.

---

## 8. Consequence for one innermost bubble

Raw insertion is functorial for every support-pair switch:

- input lower state `lambda` lifts to one predecessor-order state with at most one central atom;
- the switch lifts by one even correction cell;
- output is the raw insertion of `lambda'`;
- no second atom appears.

Together with the complete root-flip source movies, this supplies local predecessor-order lifts for every edge of a lower history generated by root `2--2` moves and support-pair component switches.

The remaining task is the global strip assembly and the treatment of any other terminal recolouring primitive not generated by these moves.

---

## 9. Assurance boundary

### Exact here

- raw insertion for arbitrary `A/B/C` marked relation;
- parity formula for the lifted correction edge set;
- exact central-value update;
- at most one central atom;
- component merging/splitting independence;
- universal support-switch source lift.

### Not claimed

- that arbitrary root flows are connected by support switches;
- lifting of an unspecified terminal recolouring not presented as a move history;
- complete innermost-bubble compression;
- nested variable-order compression;
- R2.7 closure, cap restoration or global five-support closure;
- PDL reconstruction, audit, Lean, manuscript, curation, release or publication.
