# AC-PD v7.4.1 — scope callsite and supersession audit

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Workstream:** `AC-PD-5CDC-V7.4.1-01`  
**Scanned snapshot:** `proof-development/affine-cdc-rigour-v1@e36ba22f09e3a9fc6358f3b03615f8fde6c00d96`  
**Negative authority:** `audit/affine-cdc-component-chain-v1@a4f20f05532c307a3a8f9d98ac4c5162e7b8ad57`  
**Application authority:** `audit/affine-cdc-terminal-exhaustion-v1@c954f2220c082bc3b47821657b7a1164876aeaab`  
**Classification:** `COMPLETE CONTROLLING-V7.4 CALLSITE SCAN / NO UNRESOLVED BROAD CALL`.

---

## 1. Scope failure being corrected

The statement

> a connected category-safe rooted carrier with two distinguished terminal paths
> admits an inherited component-chain contraction to a changed matching

is false.  It permits a third terminal path as an internal quotient node.  The
#81 Heawood certificate has six terminal darts, three terminal paths, a shortest
length-two quotient chain, thirty-six category-safe root NNI movies and no
inherited length-one chain for the original distinguished pair.  Permanent
digest:

`d24c63ab56320803b9c795ac08389674b6f67edf89dc5c4ef9a729c5436a3e61`.

The repair is not a wording change to the general theorem.  Active authority is
now the conditional theorem

`FC-EXACT-TWO-TERMINAL-PATH-COMPONENT-CHAIN`,

called only after one of the two #82 constructors proves exactly two ordered
terminal paths and closed remaining channel components.

---

## 2. Exhaustiveness of the scanned v7.4 surface

The exact v7.4 delta from the pre-v7.4 PDL head to
`e36ba22f09e3a9fc6358f3b03615f8fde6c00d96` consists of the following nine
controlling proof-development paths:

1. `AC_PD_V7_4_COMPONENT_CHAIN_THEOREM_RECONSTRUCTION.md`;
2. `AC_PD_V7_4_COMPONENT_CHAIN_ROW_AND_DART_TABLES.md`;
3. `AC_PD_V7_4_INHERITED_CHAIN_AND_FINAL_MATCHING.md`;
4. `AC_PD_V7_4_CO_ROOT_COMPONENT_CHAIN_COROLLARY.md`;
5. `AC_PD_V7_4_ZERO_PARENT_COMPONENT_CHAIN_COROLLARY.md`;
6. `AC_PD_V7_4_COMPLETE_INVERSE_PARENT_AND_INDUCTION.md`;
7. `AC_PD_V7_4_COMPONENT_CHAIN_ANTECEDENT_AND_NOVELTY_LEDGER.md`;
8. `AC_PD_5CDC_PROOF_DAG_AND_STATUS.md`;
9. `AC_PD_V7_4_INDEPENDENT_AUDIT_HANDOFF.md`.

Every one was read in full or through all load-bearing sections.  The table below
classifies every active or potentially active reference to the broad theorem.

---

## 3. Per-file callsite classification

| v7.4 path / occurrence | Old role | v7.4.1 classification | Active replacement or disposition |
|---|---|---|---|
| `AC_PD_V7_4_COMPONENT_CHAIN_THEOREM_RECONSTRUCTION.md`, §§2--8 and theorem `FC-COMPONENT-CHAIN-ROOT-NNI` | universal rooted-carrier theorem | **historical/failed candidate only** | file receives a status override; active theorem is `FC-EXACT-TWO-TERMINAL-PATH-COMPONENT-CHAIN` |
| same file, parity, inactive type, local contractions, stable-dart contracts | local ingredients | **unused as theorem authority; retained local source only** | cited only through the independently audited local-row package |
| `AC_PD_V7_4_COMPONENT_CHAIN_ROW_AND_DART_TABLES.md`, references to “the component-chain theorem” | finite local tables | **unused broad wording** | tables retained by exact citation; application totality supplied separately |
| same file, closed-cycle + closed-cycle row | general quotient possibility | **unused** | not needed by either shortest chain from a distinguished path; retained historical local topology |
| `AC_PD_V7_4_INHERITED_CHAIN_AND_FINAL_MATCHING.md`, witnessed-chain definition requiring internal inactive/cycle nodes | conditional proof | **historical conditional lemma, absorbed into active scoped theorem** | valid only after #82 census; no standalone general call |
| same file, final two-path matching theorem | local terminal row | **unused as totality; retained audited local lemma** | invoked after exact two-path constructor and inherited contraction |
| `AC_PD_V7_4_CO_ROOT_COMPONENT_CHAIN_COROLLARY.md`, §3 `Apply FC-COMPONENT-CHAIN-ROOT-NNI` | co-root totality call | **replaced by co-root application lemma** | `FC-PURE-NNI-CO-ROOT-APPLICATION-ESCAPE`, importing `CO_ROOT_TERMINAL_CENSUS.md@c954...` |
| same file, universal co-root theorem | corollary conclusion | **replaced by co-root application lemma** | conclusion retained only with explicit constructor provenance |
| `AC_PD_V7_4_ZERO_PARENT_COMPONENT_CHAIN_COROLLARY.md`, §4 broad call | zero totality call | **replaced by zero-parent application lemma** | `FC-PURE-NNI-ZERO-PARENT-APPLICATION-ESCAPE`, importing `ZERO_PARENT_TERMINAL_CENSUS.md@c954...` |
| same file, universal zero theorem | corollary conclusion | **replaced by zero-parent application lemma** | conclusion retained only with active-cell constructor provenance |
| `AC_PD_V7_4_COMPLETE_INVERSE_PARENT_AND_INDUCTION.md`, header/general integration | end-to-end reliance | **historical/failed candidate only** | superseded by `AC_PD_V7_4_1_INVERSE_TABLE_PREFIX_AND_INDUCTION_RECLOSURE.md` |
| same file, co-root §§5,7 | broad chain in inverse table/prefix | **replaced by co-root application call** | #82 co-root constructor -> conditional chain -> Phase-B |
| same file, zero §§6,7 | broad chain in inverse table/prefix | **replaced by zero-parent application call** | #82 zero constructor -> conditional chain -> alignment/switch/parent |
| same file, connector-rank reset wording in §7 | nested rank control | **historical wording superseded** | one list per active obligation; no reset until parent/terminal; next initialization only after prefix decreases |
| same file, ordinary-induction conclusion | downstream candidate | **historical failed candidate until reclosure** | re-established only by the v7.4.1 scoped dependency file |
| `AC_PD_V7_4_COMPONENT_CHAIN_ANTECEDENT_AND_NOVELTY_LEDGER.md`, claims that the v9 broad theorem is new load-bearing mathematics | provenance/novelty | **historical/failed candidate only** | local novelty remains; universal quantifier classified as a new scope regression by #81 |
| same ledger, local antecedent classifications | provenance | **unused by proof / retained historical source** | useful only for provenance and supersession, not theorem authority |
| `AC_PD_5CDC_PROOF_DAG_AND_STATUS.md`, §§1,3--7,9--10 broad totality | controlling DAG | **replaced by co-root and zero application calls** | DAG rewritten so each chain edge follows a named #82 constructor |
| `AC_PD_V7_4_INDEPENDENT_AUDIT_HANDOFF.md`, §2 primary universal theorem and §§4--6 callsites | audit target | **historical/failed candidate only** | superseded by v7.4.1 full-audit handoff |

---

## 4. Classification totals

### Replaced by co-root application lemma

1. co-root corollary §3 and theorem statement;
2. inverse-table co-root row;
3. prefix-return co-root call;
4. DAG co-root branch;
5. old audit-handoff co-root chain call.

### Replaced by zero-parent application lemma

1. zero corollary §4 and theorem statement;
2. inverse-table zero row;
3. prefix-return zero call;
4. DAG zero branch;
5. old audit-handoff zero chain call.

### Historical/failed candidate only

1. broad theorem reconstruction and theorem name;
2. old complete inverse/induction packet as a no-known-gap candidate;
3. broad novelty/totality claims in the antecedent ledger;
4. old DAG classification;
5. old v7.4 audit handoff.

### Unused

1. closed-cycle plus closed-cycle contraction row in the exact two-path
   applications;
2. general quotient loops and multi-terminal path transitions as progress rows;
3. local tables as independent totality providers;
4. Heawood `6-7` and zero-parent movies as universal proofs;
5. Curator baseline as mathematical proof authority.

### Unresolved defect

**None found in the active v7.4.1 call graph.**

The #81 third-terminal-path defect remains unresolved for arbitrary rooted
carriers, but no active proof call has that domain.  It is a permanent negative
boundary, not an obligation needed by the two genuine applications.

---

## 5. Application-call proof obligations

Every active component-chain invocation now has the following syntactic and
mathematical guard:

### Co-root guard

```text
complete closed co-root state
-> cut exactly two marked nonadjacent H_h edges with disjoint roots
-> #82 co-root census
-> connected carrier with exactly two ordered marked arcs + closed cycles
-> conditional chain.
```

### Zero guard

```text
complete normalized zero state
-> delete exactly active two-vertex cell, central edge nonchannel
-> exactly four channel branch darts
-> #82 zero census
-> crossed matching immediate OR residual AB|CD with exactly two paths + closed cycles
-> conditional chain.
```

No helper theorem may infer these guards from the mere existence of four named
ports or two distinguished paths.

---

## 6. Permanent negative ledgers

### #78

The same-arc equal face `9-14:23` remains a genuine co-root counterexample to
arbitrary-equal-face `Xi` source selection.  `Xi` is retained only for its audited
frame, invariance and local strict rows.

### #81

The three-cut/six-terminal Heawood carrier remains a complete counterexample to
the broad component-chain theorem.  It is excluded only by the exact physical
constructors audited in #82.  Its source, digest and classification are not
weakened.

### Curator baseline

`24f777d...` is used only to preserve the mixed-assurance provenance that the
broad theorem failed and the global theorem was open before #82.  It is not a
proof premise and is not modified.

---

## 7. Downstream cone audit

After replacing the broad calls, the downstream sequence uses only:

1. accepted/retained root-flow semantics and structural cross input;
2. target-synchronized root-NNI prefix;
3. first-cancellation actual-target lower call;
4. one inverse pop;
5. one-atom coherence to a complete prescribed-parent state;
6. exhaustive root/co-root/zero table;
7. a #82 application constructor in each singular row;
8. the conditional exact-two-path chain;
9. literal parent realization or exact terminal;
10. strict decrease of stored-prefix length;
11. ordinary induction;
12. cubic theorem candidate;
13. support-count-preserving outer shell.

The scan found no active occurrence requiring:

- a third terminal path to be contracted;
- a reset or replacement of an active connector list;
- same-level root-solubility recursion;
- a second lower-order call after first cancellation;
- track erasure as parent progress;
- arbitrary-equal-face or `Xi` totality;
- generic NNI connectivity;
- `Q_N`, `M_N`, `d_N`, nested bubbles or terminal frames.

---

## 8. Supersession decisions

### Active controlling v7.4.1 authority

1. `AC_PD_V7_4_1_APPLICATION_SCOPED_COMPONENT_CHAIN.md`;
2. `AC_PD_V7_4_1_CO_ROOT_AND_ZERO_RECLOSURE.md`;
3. `AC_PD_V7_4_1_INVERSE_TABLE_PREFIX_AND_INDUCTION_RECLOSURE.md`;
4. the independently audited local rows at `a4f20f...`;
5. the independently audited terminal censuses at `c954f2...`;
6. the updated v7.4.1 proof DAG.

### Retained exact local dependencies

- v7.4 row/dart tables, within #81-audited rows;
- inherited stable-connector proofs, under the exact-two-path hypothesis;
- Phase-B, cap/route and terminal consumers;
- v7.2 first-cancellation, single-pop and one-atom coherence packets;
- conditional outer shell.

### Historical/failed authority only

- `FC-COMPONENT-CHAIN-ROOT-NNI` in its general rooted-carrier form;
- the old v7.4 no-known-gap classification and audit handoff;
- arbitrary-equal-face `Xi` totality;
- all prior mixed-order/global-distance completion routes.

No historical source is deleted.  Supersession changes only active logical
authority.

---

## 9. Final callsite verdict

Every controlling component-chain call has been mapped to exactly one genuine
application constructor.  No active proof edge requires the false broader
theorem, and no unresolved stale universal call remains.

This is a PDL callsite audit, not an independent acceptance of the repaired
candidate.