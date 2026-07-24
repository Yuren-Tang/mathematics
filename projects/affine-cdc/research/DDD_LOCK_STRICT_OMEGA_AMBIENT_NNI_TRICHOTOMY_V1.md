# Strict `Omega` ambient NNIs either escape, terminate, or descend inside the DDD lock

## Research Lead theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-02`  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `3f9908f3afbba1f20633bcd1cd0047eefb909d7e`

**Parents:**

- `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `PURE_NNI_PRESCRIBED_PARENT_PHASE_B_SUPPORT_CHANNEL_TRANSITION_OBJECT_V1.md`;
- `PURE_NNI_PRESCRIBED_PARENT_STATE_INTERFACE_NORMAL_FORM_V1.md`;
- the exact root-NNI category and terminal ledger.

**Status:** complete strict-descent layer for issue `research-workbench#75`. It does not use equal-face cancellation. The only remaining input after this theorem is an `Omega`-minimal locked plateau.

---

## 1. Oriented DDD normalisation

Let `S` be a complete prime prescribed-parent state whose four marked cut semiedges have ordered DDD values

\[
p,p,q,q,
\qquad p\cap q=\varnothing,
\]

and whose four rescue channels form the oriented full-channel lock for the prescribed parent matching `M_i`.

Choose one support normalisation carrying the ordered marked roots to

\[
p=12,
\qquad q=34.
\]

The cap orientation and complete dart ancestry are transported with this normalisation. On the internal DDD carrier put

\[
\Omega(S)=\sum_v\omega(\Delta_v),
\]

where

\[
\begin{array}{c|cccccccccc}
T&123&124&125&134&135&145&234&235&245&345\\
\hline
\omega(T)&3&0&1&3&0&1&1&3&3&3.
\end{array}
\]

No graph-order coordinate is used.

---

## 2. One strict ambient root NNI

Let `e=uv` be an internal edge of the DDD carrier, not a deleted marked semiedge. Suppose the two incident root triangles are distinct and the opposite tetrahedral `2--2` move is root-valued and strictly lowers `Omega`.

Perform that labelled NNI while retaining:

- every stable exterior dart identity;
- the prescribed-parent topology as a live obligation;
- the cap block and its ordered darts;
- every coefficient outside the two-vertex cell;
- the identity map to the stored pure-NNI prefix.

If the reattachment creates a loop, parallel incidence, bridge, or invalid reconnection category, the exact NNI category theorem returns the corresponding named cut or bounded terminal. Otherwise the output is another connected loopless bridgeless cubic graph of the same order.

---

## 3. Complete output trichotomy

### Theorem 3.1 — strict ambient-NNI disposition

Every strict `Omega`-lowering ambient root NNI from an oriented DDD full-channel lock has exactly one of the following outputs.

1. **Lock break.**  
   For at least one of the four crossed support roots, the two marked parent roots lie in different channel components, or the oriented route ceases to be `M_i`. The Phase-B conjugated rescue gives
   
   \[
   \text{zero or one crossed-sheet NNI}
   \to
   \text{one separating closed component switch}
   \to
   \text{the literal prescribed parent}.
   \]

2. **Cap-compatible profile.**  
   The complete boundary state enters `K_i`. The supplied root boundary glues the stored cap after one global support permutation, and the current target is returned through the stored source identity.

3. **Named category terminal.**  
   The NNI category test produces one exact cyclic `2`-, `3`-, or `4`-cut, or one named bounded loop/parallel/triangle/theta/acyclic low-port object. The existing terminal ledger consumes it on the exact current graph.

4. **Strict locked descent.**  
   The output remains a complete prime oriented DDD full-channel lock with the same live parent obligation, and
   
   \[
   \boxed{\Omega(S')<\Omega(S).}
   \]

No fifth output exists.

### Proof

The move is already a witnessed root NNI on the complete source state. The graph-category theorem first divides its output into a named invalid-category result or a prime same-order state. In the prime branch, recompute the complete four channel-component partitions and the ten-state route coordinate.

- If one marked pair separates or the oriented route changes, this is exactly the Phase-B escape condition.
- If the route/profile enters `K_i`, the cap consumer applies.
- If neither occurs and no terminal flag is present, all four same-component conditions and their `M_i` cyclic order remain; hence the output is again the same kind of oriented lock.

The final branch has the displayed strict inequality by the selected tetrahedral row. The alternatives are mutually exclusive by their complete-state fields. ∎

---

## 4. Finite iteration before the plateau

### Corollary 4.1

Starting from any oriented DDD lock, repeatedly choose a strict `Omega`-lowering ambient root NNI whenever one is present.

Because `Omega` is a nonnegative integer and graph order is fixed, after finitely many steps one obtains exactly one of:

- prescribed-parent repair after a channel break;
- cap-compatible route/profile success;
- a named cut/bounded terminal;
- a prime locked state with no `Omega`-lowering root NNI.

This is a genuine well-founded descent. Finiteness is not used to infer an exit; it is used only after every selected edge has an explicit strict inequality.

---

## 5. Relation to the fourteen-vertex movie

In `G14_AMBIENT_DDD_LOCK_ESCAPE_SOURCE_MOVIE_CERTIFICATE_V1.md`, the ambient NNI on stable edge `24` has

\[
234+123\longrightarrow124+134
\]

and therefore

\[
\Omega:29\longrightarrow28.
\]

Its output is Theorem 3.1(1): both `H_14` and `H_23` separate the marked roots. The subsequent closed `H_14` switch and active parent NNI are the exact Phase-B consumer, not part of the strict-energy step.

---

## 6. Exact remaining interface

After Theorem 3.1, `FC-PURE-NNI-ESCAPE` is reduced to:

> classify a complete prime oriented DDD lock with no strict `Omega`-lowering root NNI, using only fixed-order equal-face branch swaps, legal support-component switches, root-valued neutral NNIs, one-atom/seam/run coherence, and named exits.

The DDD potential theorem guarantees an equal-face pair in every such nonempty carrier. The next dossier treats this `Omega`-minimal plateau without performing its `2--0` cancellation.

---

## 7. Trust boundary

### Proved here

- exact same-order disposition of every strict `Omega`-lowering ambient root NNI;
- preservation of parent, cap, dart and prefix coordinates;
- immediate attachment of every nonlocked output to the existing Phase-B repair;
- well-founded finite iteration to an `Omega`-minimal locked plateau.

### Not yet proved here

- the equal-face plateau theorem;
- `FC-PURE-NNI-ESCAPE`;
- v7.2 induction closure;
- any five-support/five-CDC theorem;
- Lean, Curator, manuscript, release or publication status.
