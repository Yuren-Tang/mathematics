# AC-PD v7.4 — independent full-candidate audit handoff

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Receiver:** one new independent mathematical auditor, AC-DIR and Curator only after audit disposition  
**Classification:** `READY FOR INDEPENDENT V7.4 AUDIT / NOT YET ACCEPTED`.

---

## 1. Candidate packet

The v7.4 controlling PDL packet is:

1. `AC_PD_V7_4_COMPONENT_CHAIN_THEOREM_RECONSTRUCTION.md`;
2. `AC_PD_V7_4_COMPONENT_CHAIN_ROW_AND_DART_TABLES.md`;
3. `AC_PD_V7_4_INHERITED_CHAIN_AND_FINAL_MATCHING.md`;
4. `AC_PD_V7_4_CO_ROOT_COMPONENT_CHAIN_COROLLARY.md`;
5. `AC_PD_V7_4_ZERO_PARENT_COMPONENT_CHAIN_COROLLARY.md`;
6. `AC_PD_V7_4_COMPLETE_INVERSE_PARENT_AND_INDUCTION.md`;
7. `AC_PD_V7_4_COMPONENT_CHAIN_ANTECEDENT_AND_NOVELTY_LEDGER.md`;
8. updated `AC_PD_5CDC_PROOF_DAG_AND_STATUS.md`;
9. this handoff.

Frozen RL input:

`research/affine-cdc-five-cdc-v1@02b37476198e9eaa2b4cd8d2a2edd76782bdcd49`.

Permanent negative audit input:

`audit/affine-cdc-xi-co-root-v1@53be22a0f65b85068b11e5f781579618967db9dd`.

The old same-arc Heawood counterexample remains valid and must be reproduced by
the new auditor before testing the repair.

---

## 2. Primary audit theorem

### `FC-COMPONENT-CHAIN-ROOT-NNI`

Independently verify:

1. `H_h` degree is `0/2` at every support triangle;
2. `[5]\setminus h` is the unique inactive triangle;
3. the physical quotient includes all channel components, inactive singleton
   vertices, parallel edges and loops with exact stable edge witnesses;
4. the quotient is connected for a connected carrier;
5. active/inactive absorption is the unique root row;
6. active/active distinct contraction has one root opposite pairing;
7. equal endpoints use only the root branch swap;
8. the initial shortest path is retained as a stable connector list;
9. every move deletes its first connector and preserves all later witnesses;
10. the final connector changes the ordered terminal matching.

No finite-state or SCC-distance substitute is acceptable.

---

## 3. Highest-priority adversarial points

### A. Inactive singleton collision

Construct the case in which both adjacent quotient connectors meet the same
inactive source vertex.  Check that after absorbing the first edge:

- the second stable edge still exists;
- its root remains nonchannel;
- its outside dart is unchanged;
- its inside dart lies in the enlarged component.

### B. Active-cycle entry/exit

Try to realize entry and exit at one modified active vertex.  The proposed
proof excludes it because an active cubic vertex has exactly one nonchannel
incidence.  Check graph loops and quotient parallel edges separately.

### C. Silent later merge

Verify that the new channel cross-connections join only the first two quotient
nodes and that the new active/active central root is outside `H_h`.

### D. Equal final endpoints

Attack the claim that the root branch swap changes the terminal matching.
Darts are labelled and the two local passages must belong to two distinct
terminal paths.  The audit-#78 same-arc configuration is not sufficient.

### E. Rank fidelity

Confirm that the rank is the number of remaining edges in one inherited
connector list, not a newly recomputed shortest distance.

---

## 4. Co-root audit

1. reproduce the old unproductive Heawood face `9-14:23` and its unchanged route;
2. cut marked edges `1-6:12`, `2-3:34` and identify the two marked arcs;
3. verify stable edge `6-7:23` joins different arcs;
4. independently reconstruct
   `123+234 -> 124+134`, central `23 -> 14`;
5. check dart reattachments `5-6 -> 5-7`, `7-8 -> 6-8`;
6. check route change `(1,2)|(3,6) -> (1,3)|(2,6)`;
7. check graph category and cap/prefix identities;
8. verify the final matching census gives separation or the exact opposite
   cap-compatible route;
9. audit the existing Phase-B consumer at the literal current descendant.

The audit must not restore arbitrary-equal-face or unconditional `Xi` totality.

---

## 5. Zero-parent audit

Normalize `(13,13,23,23)` and `H_35`.

1. prove complement connectivity or exact bridge/two-cut/bounded output;
2. classify the three outside terminal matchings;
3. contract an `AB|CD` residual lock by the component-chain theorem;
4. verify the final outside matching is crossed;
5. align the active crossed sheet by zero or one root NNI;
6. verify there are two closed `H_35` components, each with one `13` and one
   `23` occurrence;
7. switch one whole component;
8. verify active word `(15,13,25,23)` up to ordered symmetry;
9. perform the literal `AB|CD` parent NNI with central root `35`;
10. verify all cap, stable dart and prefix identities.

### Mandatory Heawood model

Recompute the complete movie at active edge `4-5:12`:

```text
13-14 root branch swap
    -> H_35 split
    -> switch Z_0=1-2-3-4-13-1
    -> active word (15,13,25,23)
    -> literal parent, central root 35.
```

Recompute every root equation and graph category rather than trusting supplied
digests.

---

## 6. End-to-end audit

Verify the exact interfaces:

```text
arbitrary lower target root flow
    -> one inverse pop
    -> root / one-atom / terminal
    -> one-atom coherence only
    -> complete prescribed-parent root state
    -> root/co-root/zero exhaustive table
    -> component-chain repair
    -> literal stored parent
    -> decrease stored-prefix length
    -> ordinary strong induction.
```

Attack specifically:

- hidden second lower-order call;
- same-level root-solubility recursion;
- use of track erasure as target progress;
- implicit recolouring at terminals;
- cap or dart isomorphism substituted for literal identity;
- route change returned on an earlier rather than current descendant;
- generic root/NNI connectivity;
- `Q_N`, `M_N`, `d_N`, nested bubbles or terminal frames.

---

## 7. Supersession checks

The auditor must confirm that none of the following appears as a hidden lemma:

- arbitrary-equal-face route-or-split;
- `Xi` totality;
- `Omega` orbit minimum;
- finite-state/SCC distance;
- target-boundary wording as target realization;
- a second equality cancellation during fixed-order return.

The audited portions of `Xi` may be cited only as optional local arithmetic.

---

## 8. Candidate claim and assurance boundary

PDL returns the following no-known-gap proof-development candidate:

> every finite bridgeless multigraph has a five-cycle double cover, conditional
> only on successful independent verification of the displayed PDL chain and
> already accepted outer-shell implication.

This handoff does **not** assert independent acceptance, peer review, Lean
verification, canonical/corpus movement, manuscript readiness, release,
arXiv, DOI or publication status.

A future auditor should return one of:

- independently verified at expoundable proof level;
- verified subject to bounded explicitness repairs;
- bounded mathematical revision required;
- blocked by a material gap or counterexample.

The PDL author must not serve as that independent auditor.