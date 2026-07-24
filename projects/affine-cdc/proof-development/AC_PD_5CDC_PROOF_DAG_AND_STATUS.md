# AC-PD-5CDC — v7.4.1 application-scoped proof DAG and status

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**PDL branch:** `proof-development/affine-cdc-rigour-v1`  
**v7.4.1 exact start:** `e36ba22f09e3a9fc6358f3b03615f8fde6c00d96`  
**Terminal-exhaustion audit:** `audit/affine-cdc-terminal-exhaustion-v1@c954f2220c082bc3b47821657b7a1164876aeaab`  
**Component-chain/local-row audit:** `audit/affine-cdc-component-chain-v1@a4f20f05532c307a3a8f9d98ac4c5162e7b8ad57`  
**Permanent `Xi` negative audit:** `audit/affine-cdc-xi-co-root-v1@53be22a0f65b85068b11e5f781579618967db9dd`  
**Curator provenance baseline:** `curation/affine-cdc-global-rebaseline-v2@24f777d45693ff7e031dc93137a4aec5b879a7b3`  
**Classification:** `V7.4.1 APPLICATION-SCOPED COMPLETE PROOF-DEVELOPMENT CANDIDATE / READY FOR NEW FULL AUDIT / NOT AN ACCEPTED THEOREM`.

---

## 1. Corrected authority boundary

The broad theorem

`FC-COMPONENT-CHAIN-ROOT-NNI`

for an arbitrary rooted carrier with merely two distinguished terminal paths is
**FAILED OUTSIDE APPLICATION SCOPE** and is not active authority.

Audit #81 provides a complete category-safe third-terminal-path counterexample:

- fixed channel `H_14`;
- three cut channel edges;
- six terminal darts and three terminal paths;
- shortest chain `P_0--X_1--P_1` with internal terminal path `X_1`;
- thirty-six category-safe labelled root-NNI movies;
- zero inherited length-one chains for the original distinguished terminal
  pairs;
- digest
  `d24c63ab56320803b9c795ac08389674b6f67edf89dc5c4ef9a729c5436a3e61`.

The active replacement is the conditional theorem

`FC-EXACT-TWO-TERMINAL-PATH-COMPONENT-CHAIN`,

which assumes literally

\[
H_h(R)=P_0\dot\cup P_1\dot\cup\text{closed channel cycles}.
\]

It may be called only after one of the two independently verified #82
application constructors below.

---

## 2. Corrected controlling proof DAG

```text
R0 root-flow / indexed five-support equivalence
        |
R1 valid smaller cross and specified cross root-flow input
        |
R2.1 exact boundary / ten states / fixed physical route
        |
R2.2 target-synchronised root-NNI prefix
        |
route/category terminal OR first equal-face cancellation
        |
actual smaller target cap closure (order N-2)
        |
unique lower-order call opened by the return module
        |
one arbitrary lower target root flow
        |
one inverse pop
        |
root state / one standard co-root atom / exact terminal
        |
one-atom run / seam / backtrack coherence
        |
complete root-valued prescribed-parent state
        |
        +---------------- root parent
        |                     |
        |             literal stored root NNI
        |
        +---------------- co-root / DDD (4,2,2)
        |                     |
        |             Phase-B nonlocked consumer
        |                     |
        |        cut exactly two marked H_h edges
        |                     |
        |       #82 CO-ROOT TERMINAL CENSUS
        |                     |
        |  exactly two ordered marked arcs + closed cycles
        |                     |
        |  conditional exact-two-path component chain
        |                     |
        |       final matching: separation / opposite route
        |                     |
        |       Phase-B switch+parent / K_i / exact terminal
        |
        +---------------- zero parent (0,2,2)
                              |
                  normalize (13,13,23,23), H_35
                              |
                 delete exactly active two-vertex cell
                              |
                   #82 ZERO TERMINAL CENSUS
                              |
       exactly two ordered paths + closed cycles
                              |
          crossed outside matching immediate
             OR residual AB|CD exact lock
                              |
          conditional exact-two-path component chain
                              |
                 crossed outside matching
                              |
          zero/one active-sheet alignment
                              |
             two closed H_35 components
                              |
                one legal component switch
                              |
            literal parent central root 35
                              |
                lower stored-prefix length
                              |
                 ordinary strong induction
                              |
             cubic five-support candidate
                              |
       support-count-preserving conditional outer shell
                              |
        finite bridgeless five-CDC candidate
```

Every component-chain edge in this DAG has one explicit #82 constructor as its
immediate logical parent.  There is no direct edge from “two distinguished
paths” to chain contraction.

---

## 3. Independently retained local component mathematics

Audit #81 independently retains:

1. `H_h` degree `0/2` and unique inactive triangle `[5]\setminus h`;
2. all six canonical active/inactive rows;
3. preservation of the next stable connector in all twenty-four ordered
   inactive-singleton continuation cases;
4. all six distinct active/active nonchannel rows;
5. all nine equal-endpoint root branch swaps, with the zero placement excluded;
6. path-plus-closed-cycle contraction;
7. final matching change in all eighty-four ordered two-terminal configurations;
8. complete co-root `6-7` and zero-parent Heawood local movies;
9. exact category and stable-dart move contracts.

Local-row digest:

`75ed977851a944f2cd80577e629a2f6936da5dfce49ad9d5a9e0e82c8b2494d4`.

These facts are not totality providers by themselves.

---

## 4. The conditional contraction node

### `FC-EXACT-TWO-TERMINAL-PATH-COMPONENT-CHAIN`

Assume a connected category-safe carrier whose selected channel is exactly two
ordered terminal paths plus closed cycles.  Form the physical quotient with
nodes for:

- the two distinguished paths;
- every closed channel cycle;
- every inactive singleton.

Choose one shortest simple connector list once and retain every stable physical
edge/dart witness.

- An inactive singleton is absorbed by the audited active/inactive row; the next
  connector survives even when both connectors meet the same source vertex.
- A closed cycle is merged into the distinguished path; entry and exit cannot
  meet the same active vertex because that vertex has exactly one nonchannel
  incidence.
- Every nonterminal move deletes the first named connector and preserves all
  later witnesses.
- No quotient distance is recomputed.
- The final connector between the two distinct named terminal paths changes the
  ordered matching.

A category, route or cap failure is consumed immediately on the current
descendant.

The theorem has no domain containing a third terminal path.

Controlling file:

`AC_PD_V7_4_1_APPLICATION_SCOPED_COMPONENT_CHAIN.md`.

---

## 5. Co-root application constructor and return

The co-root chain is invoked only after the complete-state operation audited in
`CO_ROOT_TERMINAL_CENSUS.md@c954f222...`:

1. begin with a complete closed category-safe co-root state;
2. choose the current locked rescue channel;
3. cut exactly the two distinct nonadjacent marked channel edges whose roots are
   disjoint;
4. retain exactly their four ordered endpoint darts;
5. consume any disconnected carrier by bridge/two-cut/bounded rows;
6. obtain exactly two ordered marked arcs and closed remaining channel cycles.

The conditional chain changes the marked terminal matching.  Reinsertion of the
marked edges gives:

- distinct marked components: separating-channel switch and literal parent;
- one component with opposite route: exact `K_i`/cap-compatible consumer;
- an exact graph/category terminal.

The #78 same-arc face `9-14:23` remains a permanent counterexample to arbitrary-
equal-face `Xi` totality.  Stable edge `6-7:23` is retained only as a checked
route-changing model.

Controlling theorem:

`FC-PURE-NNI-CO-ROOT-APPLICATION-ESCAPE` in
`AC_PD_V7_4_1_CO_ROOT_AND_ZERO_RECLOSURE.md`.

---

## 6. Zero-parent application constructor and return

Normalize

\[
(A,B,C,D)=(13,13,23,23),\qquad h=35,
\]

with current central root `12` and stored parent `AB|CD`.

Invoke the chain only after the complete-state operation audited in
`ZERO_PARENT_TERMINAL_CENSUS.md@c954f222...`:

1. delete exactly the active two-vertex cell;
2. retain exactly four ordered channel branch darts;
3. the nonchannel central edge creates no selected-channel terminal;
4. consume disconnected complements by bridge/two-cut/bounded rows;
5. obtain exactly two ordered terminal paths and closed remaining cycles;
6. consume crossed outside matchings immediately;
7. only residual `AB|CD` invokes the conditional chain.

After the final connector:

1. align the active crossed sheet with zero or one root NNI;
2. obtain two closed `H_35` components, each with one `13` and one `23` branch;
3. switch one complete component by `35`;
4. obtain active word `(15,13,25,23)` up to ordered symmetry;
5. perform the literal stored parent NNI with central root `35`.

The explicit Heawood movie remains a checked model, not the universal provider.

Controlling theorem:

`FC-PURE-NNI-ZERO-PARENT-APPLICATION-ESCAPE` in
`AC_PD_V7_4_1_CO_ROOT_AND_ZERO_RECLOSURE.md`.

---

## 7. Exhaustive inverse-parent table

The symmetric difference of two roots has weight `0`, `2`, or `4`.  Hence:

| value | active disposition |
|---|---|
| root | literal stored NNI |
| co-root | #82 co-root constructor -> conditional chain -> Phase-B |
| zero | #82 zero constructor -> conditional chain -> alignment/switch/parent |
| route/category | exact current-descendant consumer |

There is no fourth value and no singular row requiring the failed broad theorem.

Controlling integration:

`AC_PD_V7_4_1_INVERSE_TABLE_PREFIX_AND_INDUCTION_RECLOSURE.md`.

---

## 8. Prefix, dart and rank discipline

At fixed graph order control the return by:

- `L`: number of stored source NNIs remaining;
- `C`: remaining connectors in the one active application chain.

For one parent obligation:

1. inspect its value once;
2. if singular, construct one audited application carrier;
3. choose one connector list once;
4. delete one named connector at every nonterminal chain step;
5. do not reset the channel, quotient path, shortest distance or connector list
   while `L` is fixed;
6. consume final matching progress immediately;
7. lower `L` by literal parent success before another local rank is initialized.

Every active dart, cap field, route/profile, parent topology and prefix ancestry
is carried on the current descendant.  One-atom run/seam replacement is
coherence only and never counts as parent progress.

---

## 9. Lower-order and recursion boundary

The v7.2 first-cancellation module begins with one specified root flow on the
valid smaller cross supplied by the upstream R1/minimal-counterexample input.
Inside the return module exactly one fresh lower-order existence invocation is
opened: the genuine actual target cap closure at first cancellation.

After that:

- exactly one inverse pop occurs;
- no second lower-order call occurs;
- no same-level root-solubility recursion occurs;
- every singular repair is same-order finite source surgery;
- cut/bounded branches use their already named strictly-smaller consumers;
- no track erasure, SCC distance or generic connectivity substitutes for
  reachability.

This module boundary is a primary target for the new independent full audit.

---

## 10. Terminal consumers

Active consumers remain:

- `K_i` / cap-compatible route;
- separating support-channel parent repair;
- bridge and exact cyclic two-cut;
- cyclic three-cut and four-cut completions;
- loop, forbidden parallel, triangle, theta and direct-matching bases;
- acyclic low-port bounded shores;
- single-pop coincidence and unavailable-borrow rows.

Component-chain moves create no new terminal type.  Every output is read from
the current complete descendant with literal dart identities.

---

## 11. Ordinary induction, cubic candidate and outer shell

The reclosed chain is:

```text
specified valid-cross root flow
-> synchronized prefix
-> first cancellation / unique actual-target lower call
-> one inverse pop
-> at most one atom / complete parent state
-> exhaustive root/co-root/zero table
-> one #82 application constructor in each singular row
-> conditional exact-two-path chain
-> literal stored parent / exact terminal
-> strict stored-prefix decrease
-> ordinary strong induction
-> cubic five-support candidate
-> support-count-preserving outer shell.
```

The cubic candidate is a root-valued `E_5` flow, equivalently five indexed even
supports covering each cubic edge twice.

The previously accepted conditional outer shell:

- treats loops in two fixed supports;
- uses port-cycle cubic expansions;
- solves all cubic components with the same five support indices;
- collapses memberwise while preserving cut-evenness and support count.

It is applied only after the cubic candidate is reclosed and does not bridge a
missing cubic implication.

---

## 12. Supersession and permanent negatives

### Failed outside application scope

- general `FC-COMPONENT-CHAIN-ROOT-NNI`;
- old v7.4 no-known-gap status based on that theorem;
- old v7.4 full-audit handoff targeting the broad theorem.

### Permanently false

- arbitrary-equal-face route-or-split;
- `Xi` as unconditional totality;
- `Omega` orbit-minimum source selection;
- any inference that two distinguished paths imply terminal exhaustion.

### Retained locally

- audited component rows and final matching table;
- one-atom run/seam coherence;
- Phase-B and exact terminal consumers;
- first-cancellation and single-pop source contracts;
- conditional support-count-preserving outer shell.

Complete callsite classification:

`AC_PD_V7_4_1_SCOPE_CALLSITE_AND_SUPERSESSION_AUDIT.md`.

---

## 13. Current exact classification

\[
\boxed{
\begin{array}{c}
\text{first cancellation / actual target / single pop: reconstructed}\\
+\ \text{one-atom state-walk coherence: reconstructed}\\
+\ \text{broad component-chain theorem: FAILED OUTSIDE APPLICATION SCOPE}\\
+\ \text{#82 co-root terminal constructor: independently verified}\\
+\ \text{#82 zero terminal constructor: independently verified}\\
+\ \text{conditional exact-two-path contraction: reconstructed from audited rows}\\
+\ \text{co-root and zero prescribed-parent fibres: application-reclosed}\\
+\ \text{inverse table / prefix / induction / outer shell: reclosed}\\
\hline
\text{NO KNOWN PDL GAP IN V7.4.1 ACTIVE SCOPE}\\
\text{READY FOR NEW INDEPENDENT V7.4.1 FULL AUDIT.}
\end{array}}
\]

This status does not establish five-support or five-CDC, authorize canonical
movement, or promote Lean, manuscript, release, tag, arXiv, DOI, peer-review or
publication status.