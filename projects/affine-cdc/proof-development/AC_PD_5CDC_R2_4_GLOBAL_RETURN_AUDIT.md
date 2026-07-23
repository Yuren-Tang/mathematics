# AC-PD-5CDC-R2.4 — global contextual-return audit

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Standing issue:** `Yuren-Tang/research-workbench#37`  
**Research source:** `research/affine-cdc-five-cdc-v1`  
**Classification:** `BLOCKED-PROOF / EXACT RETURN-ORDER GAP / BEST-ROUTE RETAINED`.

This dossier audits the global part of the compressed one-cross five-support proof after independent closure of:

- `R1`: one-cross structural reduction;
- `R2.1`: ten-state boundary and fixed-route certificate;
- `R2.2`: equality/DDD current-flow Morse termination;
- `R2.3`: first-failure localisation and bounded local confluence.

It reads the latest master theorem backwards and distinguishes:

1. finite-state logic that is correct once its hypotheses hold;
2. concrete hypotheses already reconstructed;
3. concrete hypotheses still needing expansion;
4. one invalid well-foundedness simplification.

---

## 1. Abstract finite-condensation step

For one fixed finite history `H` and one fixed complete contextual state alphabet, the following argument is correct.

1. The complete state graph is finite.
2. Prefix level never increases and is constant on strongly connected components.
3. A nonterminal sink SCC containing a root state is impossible, because the next inverse move succeeds or creates a token.
4. If every persistent token SCC contains a physically admissible even Petersen core and every such core has an exit, no nonterminal sink SCC exists.
5. The condensation graph is a finite DAG, hence every state has a finite path to some terminal or designated recursive exit.

This part of `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V3.md` is elementary and sound. It does not itself prove that a designated recursive exit is well founded.

---

## 2. Concrete hypotheses already closed or substantially reconstructed

### 2.1 First failure `F`

Closed in `AC_PD_5CDC_R2_3_FIRST_FAILURE_AND_LOCAL_CONFLUENCE.md`:

- one failed central edge only;
- value `0` or one co-root;
- complete exterior and cap data retained.

### 2.2 Local grammar `L`

Closed locally:

- inverse-flip zero has an alternate root NNI;
- inverse-cancellation zero is the separate quadruple-equality row;
- co-root critical overlaps relocate one token;
- the unique bad overlap creates only a transient two-co-root three-vertex tree and has a root-lowering NNI;
- no persistent token branching;
- all nonzero root/co-root NNI states are connected and bridgeless.

### 2.3 Current-flow termination

Closed in `AC_PD_5CDC_R2_2_SINGULAR_MORSE_DESCENT.md` by positive scalar Morse weights and complete finite tables.

### 2.4 Petersen finite geometry

Independently checked:

- the Petersen graph on the ten roots has simple cycle lengths exactly `5,6,8,9`;
- counts are `12,10,15,20` respectively;
- every simple `C6` has emitted side word one repeated root triangle;
- constant-pivot transitions transport the nonpivot root section uniquely.

The complete physical forced-backbone reduction `P` still needs one consolidated source-incidence proof, but its finite target geometry and local transport are not in doubt.

### 2.5 Even-core local algebra

For every `C6`:

- its six side roots have word `(a,b,c,a,b,c)` with `a+b+c=0`;
- each two-turn boundary has the `(0,2,2)` triality;
- the root cross and canonical star are related by one root NNI;
- the star has an equal-face dipole;
- adjacent turn corollas agree literally.

Every `C8` has the stated two-`C6` seam decomposition. The remaining issue is not these finite root identities but how their exit is used in the global induction.

---

## 3. Orientation hypothesis `O+`

The linear resolution statement is exact:

\[
\operatorname{Hol}_{\rm res}(\gamma)
=|\gamma|\pmod2.
\]

An odd Petersen cycle exchanges the two crossed resolutions. To exclude an odd **pivot-closed subtrack**, however, one must additionally prove that the physical transport from the beginning to the end of that subtrack compares the same distinguished cap block, even when the complete contextual state has not yet closed.

The research branch states this as:

\[
\text{every physical pivot-closed segment lies in the cap-block stabiliser}.
\]

This is stronger than the proved endpoint parity calculation. It is plausible from the fixed-route lock and transported crossed-route local system, but PDL has not yet reconstructed a single theorem whose hypotheses and conclusion establish it for every descendant complete state.

Therefore `O+` is retained as:

`HIGH-CONFIDENCE / REQUIRES FULL-LABELLED EXPANSION`,

not yet as a closed PDL theorem.

---

## 4. The exact target-order problem

The master theorem v3 states that a genuine cancellation lowers the contextual target order `N` by two and therefore permits induction only on `N`.

This is not valid without an additional relative recursion theorem.

Let

\[
P_0\to P_1\to\cdots\to P_m
\]

be the forward four-pole history, and let

\[
\widehat G_s=P_s\cup cap_i
\]

be the parallel cap closures. If the first inverse failure lies behind `c` earlier cancellations, then

\[
|V(\widehat G_{s})|
=|V(\widehat G_0)|-2c.
\]

If the relevant cancellation is the first cancellation encountered in the forward prefix, then `c=0` before that step. The predecessor context to be restored may therefore still have order

\[
|V(\widehat G_0)|,
\]

not `N-2`.

This is exactly the correction already recorded in

`CONTEXTUAL_TRANSFER_TARGET_ORDER_CORRECTION_V1.md`:

a pure-flip prefix may remain at the same cap-target order, and one may not identify the smaller reconnection closure with the cap-attached predecessor.

### Proposition 4.1 — v3 simplification is unsupported

The implication

\[
\boxed{
\text{equal-face cancellation exit}
\Longrightarrow
\text{a recursive contextual obligation of target order }N-2
}
\]

is not established by vertex counting alone.

Consequently the v3 claim

\[
\text{one induction on }N
+
\text{condensation rank}
\]

is presently unsupported.

---

## 5. Why ordinary existence on the smaller graph is insufficient

An equal-face cancellation removes two identical root triangles and reconnects two pairs of equally labelled edges for the **current inherited flow**.

Suppose the smaller graph is known abstractly to admit some root flow. Its two reconnection edges may carry:

1. distinct intersecting roots — inverse insertion succeeds;
2. equal roots — inverse insertion gives zero;
3. disjoint roots — inverse insertion gives a co-root.

Therefore a nonrelative induction hypothesis saying only

\[
\text{the smaller graph has some root flow}
\]

does not supply the boundary labels required to reverse the cancellation.

The missing input is a relative theorem preserving the two cancellation-interface roots, or a different same-order rootification that never leaves the original context.

---

## 6. Status of versions v1 and v2

Versions v1 and v2 use lexicographic induction on

\[
(N,m).
\]

But both still classify the cancellation branch as lowering `N`. Merely restoring the history-length coordinate does not repair the missing interface.

A valid lexicographic repair would need an additional proof that the cancellation branch produces either:

1. a same-order obligation with strictly shorter normalized history;
2. a same-order obligation with a strictly smaller relative carrier/enclosure measure;
3. or a genuinely lower-order obligation together with an explicit boundary-preserving expansion back to the predecessor.

None of these implications is presently supplied by the master theorem statements.

---

## 7. Three viable repair targets

### Repair A — same-order even-core rootification

Strengthen the relative `C6/C8` movie so that an even persistent track is replaced directly by a fully root-valued history/context at the same target order. Then the SCC has a rootification exit and no cancellation recursion is needed.

Required statement:

\[
\boxed{
\text{relative even-track co-root context}
\rightsquigarrow
\text{same-boundary root context}
}
\]

with the complete history prefix and cap block retained.

The existing canonical-star theorem gives a root-valued local section, but the current consumer uses only its internal dipole cancellation. It must be checked whether the star section itself already yields the stronger rootification.

### Repair B — relative cancellation-lift theorem

Prove that the lower-order recursive solution can be chosen with the exact two interface roots needed for inverse equal-face insertion.

This is a relative profile theorem, not ordinary smaller-graph existence.

### Repair C — genuine same-order descent

Retain the cancellation as a new contextual problem of the same target order, but define and prove decrease of a source-level measure such as:

- remaining history prefix;
- enclosed carrier size;
- number of uncancelled source vertices before the token;
- laminar interval depth;
- or a multiset of component orders.

The measure must be attached to the complete contextual state and shown to decrease across the recursive return, not merely across the forward surgery.

---

## 8. Current PDL verdict

The compressed proof is not rejected. Its strongest current classification is:

\[
\boxed{
\text{R1 CLOSED}
+
\text{R2 finite/local core CLOSED}
+
\text{GLOBAL RETURN BLOCKED AT ONE EXACT RELATIVE WELL-FOUNDEDNESS INTERFACE}.}
\]

The global five-support theorem is therefore **not yet `COMPLETE-DRAFT` or `READY-FOR-CURATOR`** at PDL assurance level.

The preferred next attack is Repair A, because it would simplify the proof and delete the entire questionable cancellation-recursion layer. If Repair A fails, Repair C is more likely than Repair B to preserve the present source-level dynamics without requiring a new global profile theorem.

---

## 9. Nonessential but retained mathematics

The following remain valuable independently even if omitted from the shortest final proof:

- gauge/Petrial and orientation obstruction theory;
- equality and DDD Morse functions;
- Petersen resolution double cover and side-word geometry;
- relative coloured-Pachner/weld interpretation;
- full-state correction distinguishing pivot skeleton from support monodromy;
- `C6/C8` source movies;
- higher-rank defect-tree NNI descent;
- A3/flat-code and regional Stokes structures.

They should be curated only after the shortest rigorous 5-CDC spine is settled.