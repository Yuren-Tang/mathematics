# AC-PD-5CDC EQ-RETURN 5 — bounded-depth nested weld-return stack order

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Research inputs:** `WELD_RELATION_FIRST_EXIT_V1.md`; `WELD_MARK_EQUAL_FACE_OVERLAP_V1.md`  
**State:** `ABSTRACT WELL-FOUNDEDNESS THEOREM / CONCRETE LOCAL-RANK VERIFICATION OPEN`.

---

## 1. Return frames

Fix one outer target order

\[
N_0.
\]

A return frame records a tuple

\[
\boxed{
\tau=(N,m,a,r;\Xi),}
\]

where:

- `N` is the current closed target vertex order;
- `m` is the remaining prefix rank of the finite return history currently being consumed;
- `a` is the number of active ordered weld-mark lineages;
- `r` is a finite local progress rank inside the current fixed-prefix complete-state graph;
- `Xi` denotes the complete source incidence, cap, route, token and ordered-mark data.

Only the numerical key

\[
k(\tau)=(N,m,a,r)
\]

enters the well-founded order. `Xi` is retained to make transitions physical and deterministic.

Order frame keys lexicographically:

\[
(N,m,a,r)<(N',m',a',r')
\]

when the first unequal coordinate is smaller.

---

## 2. Stacks and bounded depth

A recursive cancellation creates a child frame whose target order is at least two smaller:

\[
N_{i+1}\le N_i-2.
\]

Hence every live stack

\[
S=(\tau_0,\tau_1,\ldots,\tau_d)
\]

satisfies

\[
N_0>N_1>\cdots>N_d\ge0
\]

and has uniformly bounded depth

\[
\boxed{d+1\le \lfloor N_0/2\rfloor+1.}
\]

Order stacks lexicographically from the outermost frame. At the first frame position where they differ, compare frame keys. If one stack is a proper prefix of the other, the shorter stack is smaller.

### Lemma 2.1 — stack order is well founded

The outer-to-inner lexicographic order on these stacks is well founded.

### Proof

Stack length is bounded by a fixed finite number `D=floor(N_0/2)+1`. Pad every stack to length `D` by a terminal symbol smaller than every live frame. The stack order becomes a finite lexicographic product of well-founded frame-key orders. A finite lexicographic product of well-orders is well ordered. ∎

The bounded-depth hypothesis is essential: unrestricted finite words with the ordinary lexicographic order need not be well founded.

---

## 3. Continuation-normalized transition types

A recursive execution is **continuation-normalized** when a cancellation call stores the parent continuation only after the parent has consumed one strict local progress step. Thus the stored parent key is strictly smaller than the key before the call.

The exact transition types are the following.

### Type I — internal progress

The top frame remains at the same stack depth and one of

\[
m,\quad a,\quad r
\]

strictly decreases while all earlier coordinates remain fixed.

This includes successful inverse-prefix traversal and finite same-order condensation progress.

### Type II — cancellation push

Replace the top parent frame `tau` by a stored continuation `tau^-` with

\[
k(\tau^-)<k(\tau),
\]

and append a child frame `sigma` satisfying

\[
N(\sigma)\le N(\tau)-2.
\]

The child history length and local rank may be arbitrary finite numbers.

### Type III — successful pop

Delete the completed child frame. The stored continuation remains.

### Type IV — first `A/C` pop

Delete the child frame and replace the stored parent continuation by the zero/co-root predecessor state supplied by weld-relation first exit. Its remaining prefix satisfies

\[
\boxed{m'<m_{\rm child}.}
\]

In the normalized parent representation this is stored as a strict prefix decrease before any new same-order normalization begins.

### Type V — mark-consuming cancellation

A marked central edge is deleted by a genuine `2--0` move. Either:

- a lower-order child frame is pushed; or
- at fixed frame order the active mark count strictly decreases:
  \[
  a' < a.
  \]

The ordered-incidence theorem ensures that no external `2--0` overlap creates an additional mark lineage.

---

## 4. Strict descent theorem

### Theorem 4.1 — bounded-depth stack descent

Every continuation-normalized transition of Types I--V strictly decreases the stack order.

### Proof

- **Type I:** the outer stack prefix is unchanged and the top frame key decreases.
- **Type II:** at the first differing frame position, `tau^-<tau`; the appended lower-order child is later in the lexicographic comparison and cannot reverse the decrease.
- **Type III:** the resulting stack is a proper prefix of the old stack and is smaller.
- **Type IV:** at the first frame position surviving the pop, the stored prefix coordinate is strictly smaller.
- **Type V:** either it is Type II, or the first changed key has smaller `a` with `N,m` fixed.

Thus every transition strictly decreases a well-founded order. ∎

### Corollary 4.2

No infinite execution is possible in any concrete marked-weld return system satisfying the continuation-normalization conditions above.

Nested lower-order histories may be arbitrarily long; their length cannot defeat descent because every push is lexicographically dominated by the already-consumed parent continuation step.

---

## 5. Why this is stronger than raw `(N,m)` induction

A bare pair

\[
(N,m)
\]

cannot control cancellation re-entry: a lower-order solver may construct a history longer than the parent history, and a failed weld pop may return to order `N`.

The stack theorem records the consumed parent continuation before the child is entered. The arbitrary child data occur only in a later lexicographic coordinate. Therefore no comparison between child and parent history lengths is required.

This is the standard well-founded mechanism behind nested recursive calls with stored continuations, made explicit for the weld-return system.

---

## 6. Exact concrete obligations remaining

The abstract stack problem is closed. To instantiate Theorem 4.1 in AffineCDC, PDL must still verify:

1. **finite parent local rank:** the complete mixed root/token fixed-prefix state graph has a finite rank in which every chosen cancellation consumes one strict step before push;
2. **continuation fidelity:** after a successful weld pop, the stored parent continuation is still the correct complete cap/route continuation;
3. **first-exit embedding:** the strict child-prefix result of `WELD_RELATION_FIRST_EXIT_V1.md` is represented as a strict parent-frame prefix coordinate rather than a fresh unranked history;
4. **mark genealogy:** `WELD_MARK_EQUAL_FACE_OVERLAP_V1.md` gives the complete ordered-incidence transition and no hidden mark duplication;
5. **same-order exits:** route/profile and bounded terminals leave the stack game rather than resetting an earlier frame key.

Items 2 and 4 are substantially supplied by the RL marked-incidence dossiers. Items 1 and 3 are the remaining load-bearing theorem-engineering interface.

---

## 7. Revised blocker

The phrase

> nested histories may reset forever

is no longer an independent mathematical blocker.

The exact blocker is now:

\[
\boxed{
\text{construct one continuation-normalized finite local rank for the complete mixed state graph}.}
\]

Once that rank is proved, the nested cancellation/weld recursion terminates by Theorem 4.1.

---

## 8. Trust boundary

### Exact here

- uniform bound on recursive stack depth;
- well-founded outer-to-inner stack lexicographic order;
- strict descent for normalized internal, push, pop, first-exit and mark-consuming transitions;
- explanation of why arbitrary child history lengths are harmless;
- reduction of global nested well-foundedness to continuation-normalized local rank.

### Not proved here

- existence of the required mixed-state local rank in the concrete root-surgery system;
- continuation fidelity through all route/profile terminals;
- full marked-weld return;
- R2 cap restoration or universal five-CDC.