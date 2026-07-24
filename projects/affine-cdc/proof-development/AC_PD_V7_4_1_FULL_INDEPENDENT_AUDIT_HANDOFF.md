# AC-PD v7.4.1 — full independent audit handoff

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Receiver:** a new independent mathematical auditor; then AC-DIR  
**Classification:** `READY FOR INDEPENDENT V7.4.1 FULL AUDIT / NOT ACCEPTED`.

---

## 1. Frozen candidate and authority map

The exact audit candidate is the final head of

`Yuren-Tang/mathematics:proof-development/affine-cdc-rigour-v1`

returned in issue #83.  The issue return records the exact self-containing head
SHA.

The controlling v7.4.1 packet is:

1. `AC_PD_V7_4_1_APPLICATION_SCOPED_COMPONENT_CHAIN.md`;
2. `AC_PD_V7_4_1_CO_ROOT_AND_ZERO_RECLOSURE.md`;
3. `AC_PD_V7_4_1_INVERSE_TABLE_PREFIX_AND_INDUCTION_RECLOSURE.md`;
4. `AC_PD_V7_4_1_SCOPE_CALLSITE_AND_SUPERSESSION_AUDIT.md`;
5. updated `AC_PD_5CDC_PROOF_DAG_AND_STATUS.md`;
6. this handoff.

Local row/dart source retained without rewriting:

- `AC_PD_V7_4_COMPONENT_CHAIN_ROW_AND_DART_TABLES.md`;
- `AC_PD_V7_4_INHERITED_CHAIN_AND_FINAL_MATCHING.md`, only under the explicit
  exact-two-terminal-path hypothesis.

Frozen independent authorities:

- terminal exhaustion:
  `audit/affine-cdc-terminal-exhaustion-v1@c954f2220c082bc3b47821657b7a1164876aeaab`;
- component-chain/local rows:
  `audit/affine-cdc-component-chain-v1@a4f20f05532c307a3a8f9d98ac4c5162e7b8ad57`;
- permanent `Xi` negative audit:
  `audit/affine-cdc-xi-co-root-v1@53be22a0f65b85068b11e5f781579618967db9dd`;
- provenance/status baseline only:
  `curation/affine-cdc-global-rebaseline-v2@24f777d45693ff7e031dc93137a4aec5b879a7b3`.

The Curator branch is not proof authority.

---

## 2. Mandatory negative reproduction

Before assessing the repair, independently reproduce the #81 general-theorem
counterexample:

```text
h=14
cut stable edges 1-14:13, 10-11:12, 13-14:12
six terminal darts
three terminal paths P_0, X_1, P_1
chain P_0 -- 3-8:14 -- X_1 -- 9-14:23 -- P_1.
```

Verify:

- `X_1` is a third terminal path;
- the root NNI at `3-8` splits the old `P_0` terminal pair;
- the output is category-safe;
- no inherited length-one chain for the original `P_0,P_1` remains;
- the exhaustive certificate has thirty-six category-safe labelled NNI movies
  and zero successful inherited length-one chains;
- digest
  `d24c63ab56320803b9c795ac08389674b6f67edf89dc5c4ef9a729c5436a3e61`.

The auditor must confirm that the v7.4.1 packet never weakens or “repairs” this
negative theorem.  It must remain false for arbitrary rooted carriers.

---

## 3. Audit the conditional chain, not the failed theorem

Audit theorem:

`FC-EXACT-TWO-TERMINAL-PATH-COMPONENT-CHAIN`.

Its explicit hypothesis is

\[
H_h(R)=P_0\dot\cup P_1\dot\cup\text{closed channel cycles},
\]

with complete stable-dart, cap, route, parent and prefix fields.

Independently verify:

1. fixed-channel degree `0/2` and unique inactive triangle;
2. quotient nodes include exactly `P_0,P_1`, closed cycles and inactive
   singletons;
3. the quotient is connected when the physical application carrier is connected;
4. one initial shortest simple connector list is fixed once;
5. inactive-singleton absorption preserves the next stable connector, including
   the case where both connectors meet the modified singleton;
6. path-plus-closed-cycle contraction preserves the two path terminals;
7. active-cycle entry and exit cannot share the modified vertex;
8. later connector roots remain nonchannel and stable;
9. no later component is silently merged;
10. the final distinct/equal endpoint root move changes the ordered terminal
    matching;
11. the zero placement is never used;
12. every category failure is consumed immediately.

Reject any proof that reselects a quotient path, recomputes distance, resets the
connector rank, or invokes the theorem on an internal terminal path.

---

## 4. Co-root application audit

Audit the exact constructor before the chain call:

1. start with the complete closed current co-root state;
2. identify the two marked physical `H_h` edges with distinct disjoint roots;
3. verify they lie on one locked channel cycle and are nonadjacent;
4. cut exactly those two edges and no other physical incidence;
5. confirm cap, exterior, route, parent and prefix fields create no extra port;
6. reproduce #82's exactly four terminal darts and exactly two ordered marked
   arcs;
7. verify all other channel components are closed;
8. verify disconnected carriers are bridge/two-cut/bounded outputs before the
   chain call.

Then audit the scoped contraction and the final matching classification:

- separate marked components -> switch one -> literal parent;
- opposite route -> current-descendant `K_i`/cap consumer;
- exact category terminal.

Mandatory models:

### #78 negative model

Reproduce the unproductive equal face `9-14:23` and unchanged route
`(1,2)|(3,6)`.  Confirm it remains a counterexample to arbitrary-equal-face
`Xi` totality.

### `6-7` local model

Recompute

```text
123+234 -> 124+134
central 23 -> 14
5-6@6 -> vertex 7
7-8@7 -> vertex 6
route (1,2)|(3,6) -> (1,3)|(2,6).
```

Confirm this is only a model of a connector between the two actual arcs, not a
universal provider.

---

## 5. Zero-parent application audit

Normalize:

```text
(A,B,C,D)=(13,13,23,23)
current central root 12
selected channel H_35
stored parent AB|CD.
```

Audit the exact constructor:

1. delete exactly the active two-vertex cell;
2. verify the central edge is nonchannel;
3. retain exactly four ordered branch terminal darts;
4. confirm no hidden cap/exterior/route/sheet/prefix terminal;
5. reproduce #82's exactly two terminal paths and closed remaining cycles;
6. consume a disconnected complement through exact bridge/two-cut/bounded rows;
7. consume a crossed outside matching immediately;
8. invoke the conditional chain only in residual `AB|CD` with paths `A--B` and
   `C--D`.

Then verify:

1. the final outside matching is crossed;
2. zero or one active equal-face root NNI aligns the crossed sheet;
3. the full `H_35` system has exactly two closed components;
4. each component contains one `13` and one `23` active branch;
5. one closed-component switch gives `(15,13,25,23)` up to ordered symmetry;
6. the literal stored parent NNI has central root `35`;
7. branch darts, cap, route, category and prefix ancestry remain literal.

Mandatory Heawood model:

```text
branch swap at 13-14
-> H_35 split
-> switch Z_0=1-2-3-4-13-1
-> active word (15,13,25,23)
-> literal parent at 4-5, central root 35.
```

Recompute equations and graph categories rather than trusting digests.

---

## 6. Complete callsite audit

Independently inspect the exact branch snapshot for every reference to:

- `FC-COMPONENT-CHAIN-ROOT-NNI`;
- “component-chain theorem”;
- “two distinguished terminal paths”;
- quotient distance or shortest chain;
- co-root marked-arc chain;
- zero-parent terminal-path chain.

Confirm every active call is preceded literally by one #82 application
constructor.  Classify every occurrence as:

1. replaced by co-root application lemma;
2. replaced by zero-parent application lemma;
3. historical/failed candidate only;
4. unused;
5. unresolved defect.

Compare against

`AC_PD_V7_4_1_SCOPE_CALLSITE_AND_SUPERSESSION_AUDIT.md`.

Any active occurrence in category 5 blocks the candidate.

---

## 7. Inverse table and complete-state audit

Verify algebraic exhaustiveness:

- identical roots -> zero;
- distinct intersecting roots -> root;
- disjoint roots -> co-root;
- no fourth central value.

Audit source flow:

```text
one arbitrary lower target root flow
-> one inverse pop
-> root / one standard atom / exact terminal
-> one-atom coherence only
-> complete root-valued prescribed-parent state
-> root/co-root/zero table
-> literal stored parent or exact terminal.
```

Check specifically:

- the missing-index row leaves at most one atom;
- no implicit recolouring produces the complete parent state;
- run/seam replacement is coherence, not target progress;
- active parent darts and stable ancestry are never replaced by graph
  isomorphism;
- support switches occur only after matching progress in the singular fibres.

---

## 8. No-rank-reset audit

Let `L` be stored-prefix length and `C` the active connector-list length.

Verify the exact protocol:

1. one parent obligation is selected;
2. its fibre is classified once;
3. one application carrier and one connector list are constructed;
4. every chain step removes the first named connector;
5. while `L` is fixed, no channel/list/distance reset is permitted;
6. final matching progress is immediately consumed;
7. literal parent success lowers `L`;
8. only then may a new local connector rank be initialized.

Search for every phrase suggesting “choose a new shortest path”, “recompute the
quotient distance”, “migrate to another channel” or “restart the chain”.  Any
such active operation requires a new proof and blocks the candidate.

---

## 9. Lower-order and recursion audit

The controlling v7.2 module enters with one specified cross root flow.  Audit the
composition of that upstream R1/minimal-counterexample input with the module.
Inside the return module, confirm:

- the first cancellation actual target is the unique fresh lower-order
  existence call;
- exactly one inverse pop follows;
- no second lower-order call occurs after the pop;
- cut consumers do not hide same-order recursion;
- no fixed-order root-solubility theorem is called;
- no finite-state, SCC or generic connectivity assertion supplies reachability.

This module-boundary accounting is one of the highest-priority full-audit
questions.  If the specified cross-flow input and actual-target call cannot be
composed under the claimed ordinary-induction convention, return a bounded exact
blocker rather than accepting the wording.

---

## 10. Terminal and prefix audit

Recheck every active consumer:

- `K_i` / cap-compatible route;
- separating channel;
- bridge and cyclic two-cut;
- cyclic three-cut and four-cut completion;
- loop, parallel, triangle, theta and direct-matching categories;
- acyclic low-port shores;
- single-pop coincidence and unavailable-borrow outcomes.

For every consumer confirm:

1. it is invoked on the current descendant;
2. its exact cut/category hypotheses hold;
3. cap and ordered darts are literal;
4. any smaller completion is strictly lower order;
5. no inherited-flow recolouring is assumed.

Then verify each successful parent return lowers the exact stored-prefix length
and the seam/run history reconnects literally.

---

## 11. Cubic and outer-shell audit

Only after the complete cubic induction is accepted, verify the conditional
outer shell:

- loops are inserted in two fixed supports;
- port-cycle cubic expansion uses the same five support indices across
  components;
- memberwise collapse preserves evenness;
- support count remains five;
- no ordinary CDC theorem is substituted for five indexed supports.

The outer shell may not bridge any unresolved cubic implication.

---

## 12. Forbidden hidden dependencies

The full audit must reject any active use of:

- the failed general rooted-carrier component-chain theorem;
- the #81-invalid terminal-exhaustion inference;
- arbitrary-equal-face route-or-split;
- `Xi` or `Omega` as unconditional source selection;
- a second fixed-order cancellation;
- a second lower-order call after the target call;
- same-level root-solubility recursion;
- track erasure as parent progress;
- generic root/NNI connectivity;
- finite-state/SCC distance;
- `Q_N`, `M_N`, `d_N`, nested bubbles or terminal frames.

---

## 13. Candidate claim and assurance boundary

The exact v7.4.1 PDL candidate claims, subject to successful new independent
verification of every displayed dependency:

> every finite bridgeless multigraph has a five-cycle double cover using at most
> five indexed even subgraphs.

This handoff does not assert:

- an accepted five-support or five-CDC theorem;
- Lean verification;
- Curator/canonical movement;
- manuscript readiness;
- release, tag, arXiv, DOI, peer review or publication.

The independent auditor should return one precise disposition:

- independently verified at full proof level;
- verified subject to bounded explicitness repairs;
- bounded mathematical revision required;
- blocked by a material gap;
- counterexample.

The PDL author is not the independent auditor.