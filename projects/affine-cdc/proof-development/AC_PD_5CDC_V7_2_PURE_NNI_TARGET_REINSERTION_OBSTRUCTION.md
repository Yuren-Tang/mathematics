# AC-PD-5CDC v7.2 — pure-NNI target-reinsertion obstruction

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Frozen research input:** `research/affine-cdc-five-cdc-v1@094ca09f6d3982b785a3f3428d9ec079dbba0855`  
**Classification:** `BLOCKED-PROOF / MINIMAL FIXED-ORDER TARGET-SUCCESS INTERFACE`.

This dossier isolates the first v7.2 node which cannot be reconstructed from the
frozen source.  The obstruction is not graph-order recursion: v7.2 successfully
removes `Q_N`, nested bubbles, `M_N`, `d_N` and terminal frames.  The remaining
gap is entirely fixed-order.

---

## 1. Claimed downstream implication

After the single inverse pop, v7.1 stores a required predecessor topology
`C_ell`.  A target-rooted ordinary `2--2` arborescence selects a parent edge

\[
T\longrightarrow p(T).
\]

If the forced parent diagonal is root-valued, the step succeeds and
`d_top` decreases.  If it is zero or a co-root, the source claims that local
one-atom continuation, state-walk cellwise erasure and periodic crosscuts define
a finite atom rank `rho_atom`; after that rank terminates, the same parent
obligation is said to succeed.

The required conclusion is therefore:

> every failed ordinary parent edge has a finite fixed-order root/one-atom
> relative realization whose terminal root topology is the prescribed parent
> `p(T)`, or an exact terminal occurs.

Cellwise track erasure is weaker: it removes a supplied singular track while
fixing its root-valued long histories.  It does not identify the root crosscut
with the prescribed non-root parent pairing.

---

## 2. Exact four-port witness

Take the ordered exterior root word

\[
(A,B,C,D)=(12,34,13,24).
\]

Its sum is zero.  The three ordinary binary topologies have central values

\[
\begin{aligned}
AB\mid CD &: 12+34=1234=Q_5,\\
AC\mid BD &: 12+13=23,\\
AD\mid BC &: 12+24=14.
\end{aligned}
\]

Thus the exact pairing-weight pattern is

\[
\boxed{(4,2,2)}.
\]

Let the required arborescence parent topology be

\[
P=AB\mid CD.
\]

The topology `P` is one co-root atom with the displayed fixed exterior word.
The two crossed resolutions

\[
R_0=AC\mid BD,
\qquad
R_1=AD\mid BC
\]

are both fully root-valued.

Consequently:

1. attempting `R_0 -> P` fails with the co-root `Q_5` and exposes `R_1` as the
   other root resolution;
2. attempting `R_1 -> P` fails with the same co-root and exposes `R_0`;
3. with this complete exterior word fixed, no root-valued state exists on `P`.

This is the exact local two-state distance-restoring cycle anticipated by the
return audit.  It is not a counterexample to global cap restoration: surrounding
root moves might change the local boundary word.  It is a counterexample to the
claim that the listed local fixed-order theorems alone force the prescribed
parent step.

---

## 3. Why the cellwise theorem does not close the witness

The singular comparison between `R_0` and `R_1` has two root-valued long-side
restrictions and one co-root target pairing `P`.  If the complete unresolved
endpoint repeats, the v7.2 cellwise theorem may:

1. identify the two endpoint collars;
2. erase the resulting closed track to a root cylinder;
3. choose a legal root `1`-skeleton crosscut;
4. cut back to a root rectangle.

The short root side produced by the crosscut is a root history between the two
root-valued boundary histories.  In the four-port witness it can only bypass
the co-root topology through the crossed root resolutions.  It does not change

\[
12+34=Q_5
\]

and therefore does not produce a root flow on `P` with the fixed exterior word.

This is exactly the distinction already stated in the older endpoint scope
correction:

\[
\text{closed-track erasure}
\not\Rightarrow
\text{strict progress of an unresolved outer target}.
\]

The periodic theorem removes two occurrences of an unresolved endpoint in a
supplied diagram; without an additional target-side gluing theorem it does not
supply a directed scheduler edge to `P` or to a lower `d_top` state.

---

## 4. Missing construction in the v7.2 files

The frozen v7.2 source contains:

- the ordinary uncoloured arborescence;
- the root/zero/co-root alternative for one attempted edge;
- total local critical-overlap tables;
- one-token nonbranching;
- cellwise erasure of a supplied finite track;
- periodic root crosscuts for a supplied repeated endpoint.

It does not construct a theorem with all of the following fields:

1. **active parent obligation:** the exact ordinary pairing `P` remains a
   distinguished target side throughout every local continuation cell;
2. **continuation totality:** every nonterminal atom state has a declared next
   comparison cell, not merely a coefficient transition;
3. **target-side boundary map:** every seam/run/crosscut replacement states what
   happens on the `P` side, not only on the two root long sides;
4. **success re-splicing:** after a repeated endpoint is cut, the new root short
   side glues to a root state on `P` or to a state of strictly smaller ordinary
   target distance;
5. **strict measure:** a proved finite rank decreases even in the local
   `R_0 <-> R_1` pattern above.

The symbol `rho_atom` in the no-reopening file is not defined by such a theorem.
Saying that the complete target-parent boundary is retained is not enough: the
four-port witness retains it and still has no root value on the target pairing.

---

## 5. Smallest repair theorem required

Call the missing statement

\[
\boxed{\texttt{AC-PD-V7.2-PURE-NNI-TARGET-REINSERTION}.}
\]

A sufficient repair must prove one of the following.

### A. Prescribed-parent realization

For every failed target-tree parent edge, use surrounding fixed-order root NNIs
to change the local boundary word and return a root flow on the prescribed
parent topology, with a source-faithful finite history and no cancellation.

### B. Strict alternative topology measure

Replace `d_top` by an explicit well-founded measure on complete root/atom
obligations such that the crossed alternative in every `(0,2,2)` or `(2,2,4)`
row strictly decreases it, including the displayed two-state local cycle.

### C. Target-side cellwise theorem

Strengthen the seam/run/periodic package to a relative theorem whose boundary
contains the prescribed parent topology and whose crosscut is proved to give a
root state on that topology, not merely a root path between crossed side
histories.

### D. Exact terminal consequence

Prove that the local two-state cycle forces a route/profile, small-cut or bounded
terminal in the ambient complete graph.  No such ambient implication is present
in the frozen source.

Any repair must be independent of lower-order calls, since v7.2 promises no
cancellation reopening.

---

## 6. Consequences for the requested epoch

The following issue #73 nodes are reconstructed:

- first-cancellation target synchronization;
- arbitrary-flow single pop;
- doubled-disjoint source theorem;
- state-walk maximal-run/switch decomposition;
- six-port seams;
- two-seam backtrack repair.

The following node is blocked:

- pure-NNI no-reopening **return to the prescribed target topology**.

Therefore the exact terminal census can be listed, but it cannot yet be proved
exhaustive for all fixed-order executions: a nonterminal unresolved
parent-obligation state remains.  Ordinary strong-induction closure is
conditional on the missing theorem and cannot be declared.

---

## 7. Assurance boundary

This dossier does not claim a graph counterexample to five-CDC or to v7.2's
headline existential statement.  It proves that the frozen v7.2 dependency set
does not establish the load-bearing pure-NNI return theorem.  The obstruction
is source-local, finite, and independent of the superseded mixed-order route.
