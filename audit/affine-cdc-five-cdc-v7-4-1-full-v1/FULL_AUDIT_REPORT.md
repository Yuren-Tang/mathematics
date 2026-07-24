# AC-5CDC-AUD-V741 — full independent audit report

**Issue:** `Yuren-Tang/research-workbench#84`  
**Role:** `AffineCDC — Independent V7.4.1 Full-Proof Auditor` (`AC-5CDC-AUD-V741`)  
**Frozen candidate:** `Yuren-Tang/mathematics@f90a068fbcc81d34850bb53426f4c2efb4cb5388`  
**Audit branch:** `audit/affine-cdc-five-cdc-v7-4-1-full-v1`  
**Base:** `f90a068fbcc81d34850bb53426f4c2efb4cb5388`  
**Disposition:** `MATERIAL GAP`.

## 1. Independence and audit method

The audit was conducted from the frozen candidate and its frozen independent authorities.  No explanation, repair proposal or informal assurance was requested from the Proof Development Lead.  Statements labelled `complete`, `reclosed` or `no known gap` were treated only as claims to be tested.

The review covered:

1. the complete v7.4.1 packet named in `AC_PD_V7_4_1_FULL_INDEPENDENT_AUDIT_HANDOFF.md`;
2. the retained v7.4 row/dart and inherited-chain files;
3. the v7.2 first-cancellation, single-pop, state-walk and terminal-boundary files;
4. the v7.3 prescribed-parent interfaces;
5. R1, R2.1, R2.2 and the conditional general-graph outer shell;
6. the frozen #78, #81 and #82 independent audit records.

Finite root arithmetic was recomputed directly with roots represented as the ten two-subsets of `[5]` and addition as symmetric difference.  The graph certificate in Section 2 was reconstructed from the twenty-one labelled Heawood edges, retaining stable dart identities through every NNI.

## 2. Mandatory negative reproduction

The #81 counterexample remains valid and is not weakened by v7.4.1.

Use the fourteen-vertex labelled Heawood root state and fix `h=14`.  Cut

```text
1-14:13, 10-11:12, 13-14:12.
```

The selected channel has exactly three terminal paths:

```text
P_0 = (1-14@1, 10-11@11)
X_1 = (10-11@10, 13-14@13)
P_1 = (1-14@14, 13-14@14),
```

and the shortest witnessed quotient chain

```text
P_0 -- 3-8:14 -- X_1 -- 9-14:23 -- P_1.
```

At `3-8`, the unique root-valued opposite row is

```text
134+124 -> 234+123, central 14 -> 23.
```

It splits the old `P_0` terminal pair.  The output remains connected, simple, cubic and bridgeless, with girth five and cyclic edge-connectivity five.

A fresh labelled enumeration of every non-cut central edge and both assignments of its root-valued opposite pairing gave:

```text
18 non-cut central edges
36 labelled root-valued NNI movies
36 connected, simple, cubic, bridgeless outputs
36 outputs of girth 5 and cyclic edge-connectivity 5
0 inherited length-one P_0--P_1 chains
24 preserve all three old terminal pairs but expose no direct P_0--P_1 connector
10 split P_0 and X_1
2 split P_1 and X_1.
```

The frozen canonical certificate identifier remains

`d24c63ab56320803b9c795ac08389674b6f67edf89dc5c4ef9a729c5436a3e61`.

Accordingly the general rooted-carrier theorem is false.  The v7.4.1 packet correctly leaves it false and does not use it as active authority.

## 3. Application-scoped component chain

Within the literal hypothesis

```text
H_h(R) = P_0 disjoint-union P_1 disjoint-union closed channel cycles,
```

the retained contraction argument passed the requested attacks:

- fixed-channel degree is `0/2`, with `[5]\h` the unique inactive triangle;
- the quotient retains both terminal paths, every closed cycle and every inactive singleton;
- physical connectivity projects to quotient connectivity;
- one shortest simple connector list is chosen once and thereafter shortened only by deleting its first named stable edge;
- inactive-singleton absorption preserves the successor connector even when entry and exit meet the same source vertex;
- entry and exit of a closed active cycle cannot meet the same vertex, because an active cubic vertex has exactly one nonchannel incidence;
- the active/active central root stays outside the channel, so no later component is silently merged;
- the final root alternative, including the equal-endpoint branch swap, changes the ordered terminal matching;
- the zero placement is not used.

No counterexample was found in this exact-two-terminal-path domain.  This verifies the conditional chain lemma itself, not the old universal theorem.

## 4. Application constructors and local singular fibres

The #82 co-root and zero-parent terminal censuses supply the required exact domain:

- cutting exactly two nonadjacent disjoint-root marked edges on one locked channel cycle creates exactly four terminal darts and exactly two marked arcs;
- deleting the normalized active two-vertex zero cell creates exactly four selected-channel branch darts, because the central edge is nonchannel, and leaves exactly two terminal paths;
- cap, route, parent, support and prefix fields are metadata or retained physical data and create no additional channel endpoint;
- disconnected carriers are returned to bridge, exact two-cut or bounded low-port consumers before the chain call.

The permanent #78 equal face `9-14:23` still preserves route `(1,2)|(3,6)` and remains a counterexample to arbitrary-equal-face or unconditional `Xi` totality.  The `6-7` row

```text
123+234 -> 124+134, central 23 -> 14
5-6@6 -> 7, 7-8@7 -> 6
(1,2)|(3,6) -> (1,3)|(2,6)
```

is valid only as a connector between the two actual marked arcs.

For the zero model, the component switch gives

```text
13 -> 15, 23 -> 25,
(13,13,23,23) -> (15,13,25,23),
15+13 = 25+23 = 35,
```

followed by the literal stored parent NNI with central root `35`.  These local and application-scoped results are not the blocker.

## 5. Finite algebra checks

Independent enumeration reproduced:

```text
10 equal unordered root pairs
30 distinct intersecting unordered root pairs
15 disjoint unordered root pairs
640 conserved ordered four-root boundary words
state counts 10, 60,60,60, 30,30,30, 120,120,120
180 ordered doubled-disjoint borrowing data
120 good borrowing rows
60 missing-index rows
120 ordered nonbacktracking six-port seam cells.
```

In every seam cell the two derived side roots are distinct intersecting roots, as required.  The inverse central-value table `0/root/co-root` is exhaustive.

## 6. Material blocker

The load-bearing failure occurs before the root/co-root/zero prescribed-parent table is available.

The v7.4.1 reclosure asserts the implication

```text
one standard co-root atom after the single inverse pop
    -> apply the retained v7.2 one-token coherence layer
    -> complete root-valued prescribed-parent state or exact terminal.
```

But the controlling v7.2 state-walk theorem expressly does **not** prove:

1. a finite continuation comparison from every arbitrary one-atom target-parent failure;
2. that an endpoint root strip realizes the prescribed parent rather than another root detour;
3. a well-founded pure-NNI target scheduler.

The v7.2 terminal/ordinary-induction boundary correspondingly states that pure-NNI target reinsertion is open and that ordinary induction is conditional upon it.  R2.3 closes only the local first-failure and critical-overlap algebra; it also leaves global continuation/return open.  The v7.3 co-root file and the v7.4/v7.4.1 integration files reassert that a finite comparison is supplied, but no new theorem in the six-commit v7.4.1 delta proves the missing continuation.

The smallest missing implication is therefore:

> From every complete labelled one-standard-co-root-atom state arising after the single pop, with literal prescribed-parent, cap, route, support, dart and prefix data, construct a finite source-faithful same-order history to either a complete root-valued crossed endpoint carrying those same fields or an exact current-descendant terminal, under a well-founded measure and without same-order root-solubility, finite-state/SCC recurrence, generic NNI connectivity, or track erasure counted as target progress.

This is not a bounded exposition repair.  It is a new global totality/well-foundedness theorem at the exact interface on which both singular parent fibres and the stored-prefix return depend.

## 7. Downstream effect

Because the complete prescribed-parent root state is not established for every one-atom output:

- the root/co-root/zero table is not universally reached;
- the co-root and zero application lemmas do not close every inverse-pop outcome;
- stored-prefix return is incomplete;
- ordinary cubic induction is incomplete;
- the cubic five-support theorem is not proved;
- the otherwise valid conditional outer shell cannot be applied to obtain five-CDC.

No counterexample to the final five-CDC statement is produced by this audit.  The disposition concerns the submitted proof candidate.

## 8. Final conclusion

The application-scoped repair successfully removes the #81 false-scope defect from active component-chain calls.  It does not, however, close the independently documented one-atom continuation and prescribed-parent endpoint obligation inherited from v7.2.  The exact candidate is therefore **blocked by a material proof gap**.
