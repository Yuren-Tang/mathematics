# AC-SCOPE-TERMINALS-01 — terminal-exhaustion scope audit

**Role:** `AffineCDC — Terminal-Exhaustion Scope Auditor` (`AC-TE-AUD`)  
**Role class:** temporary independent mathematical scope auditor  
**Lifecycle:** one bounded application-specific audit  
**Receiver:** `AffineCDC — Director` (`AC-DIR`)  
**Overall return:** `[BOTH-FIBRES-SCOPED AC-SCOPE-TERMINALS-01]`

## 1. Exact controls

### Frozen authorities

1. `Yuren-Tang/mathematics:curation/affine-cdc-global-rebaseline-v2@24f777d45693ff7e031dc93137a4aec5b879a7b3`;
2. `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1@02b37476198e9eaa2b4cd8d2a2edd76782bdcd49`;
3. `Yuren-Tang/mathematics:proof-development/affine-cdc-rigour-v1@e36ba22f09e3a9fc6358f3b03615f8fde6c00d96`;
4. `Yuren-Tang/mathematics:audit/affine-cdc-component-chain-v1@a4f20f05532c307a3a8f9d98ac4c5162e7b8ad57`;
5. `Yuren-Tang/mathematics:audit/affine-cdc-xi-co-root-v1@53be22a0f65b85068b11e5f781579618967db9dd`.

Permanent negative certificate:

`d24c63ab56320803b9c795ac08389674b6f67edf89dc5c4ef9a729c5436a3e61`.

### Owned branch and write boundary

- exact branch: `audit/affine-cdc-terminal-exhaustion-v1`;
- exact base: `24f777d45693ff7e031dc93137a4aec5b879a7b3`;
- only added directory: `audit/affine-cdc-terminal-exhaustion-v1/`;
- final branch SHA is recorded in the issue return because a commit cannot contain its own SHA.

Required files added exactly:

1. `TERMINAL_EXHAUSTION_REPORT.md`;
2. `CO_ROOT_TERMINAL_CENSUS.md`;
3. `ZERO_PARENT_TERMINAL_CENSUS.md`;
4. `HEAWOOD_WITNESS_APPLICATION_SCOPE_LEDGER.md`.

## 2. Audit question and inference guard

The only question audited is:

> In the genuine co-root marked-arc carrier and the genuine zero-parent active-cell-deleted carrier, are the two distinguished terminal paths all terminal path components of the selected fixed channel, with every other nontrivial channel component closed?

The following forbidden implication was not used:

```text
two distinguished terminal paths
=> no third terminal path.
```

Instead, each application was reconstructed from its complete closed physical source graph, the exact operation creating semiedges, and a complete ledger of every source field which might otherwise hide an extra channel endpoint.

The failed universal `FC-COMPONENT-CHAIN-ROOT-NNI` conclusion was not trusted.  Its local parity, inactive/cycle contraction, ordered final-matching and stable-dart results were used only after the application-specific terminal census had excluded the omitted third internal node type.

## 3. Complete-state definition assurance

No local definition repair is required.

Across the frozen RL/PDL sources, a complete application state contains a **complete labelled cubic source topology** `G`, not an unclosed four-pole.  The physically glued cap vertices, cap edge, cap darts and exterior attachments are vertices/edges of `G`; route/profile, prescribed-parent, support transport and stored prefix are state fields on the same graph.

This reading is fixed by four independent source interfaces:

1. the proof-development state explicitly retains the complete cubic source topology and every edge root/incidence;
2. the RL zero-parent state is written as a complete tuple containing `G` and all cap/route/support/prefix fields;
3. the `Xi` audit defines its invariant as a complete closed-graph vertex sum including exterior and cap vertices;
4. both exact Heawood certificates display cap vertices and cap edges as ordinary physical graph data.

Therefore neither application begins with a pre-existing terminal semiedge.  All channel terminals are created by the one displayed cut/deletion operation, and the census can be decided in exact complete-state scope.

## 4. Co-root claim census

**Fibre classification:** `EXACTLY-TWO-TERMINAL-PATHS VERIFIED IN APPLICATION SCOPE`.

| Claim | Independent disposition |
|---|---|
| physical carrier before cut | current complete connected category-safe labelled cubic graph `G` with literal selected `H_h`, two distinct disjoint-root marked `H_h` edges `p,q`, cap, route/profile, parent and prefix fields |
| channel geometry before cut | every vertex has `H_h` degree `0/2`; hence `H_h(G)` is a disjoint union of closed cycles |
| marked component | the continuing lock requires `p,q` on one physical channel cycle with the blocked ordered route |
| cut operation | delete only the interiors of `p,q`; retain their four ordered endpoint darts as channel semiedges |
| hidden cap/exterior terminal | none: cap and exterior remain physical edges/vertices of `G` and are not cut |
| hidden route/profile terminal | none: route/profile is metadata/consumer data, not an incidence |
| hidden marked/prefix terminal | none: marked darts are the same four cut endpoint darts; prefix is an ancestry map |
| retained vertex degree | remains `0/2`, counting each retained semiedge at its incident vertex |
| exact terminal count | four and only four |
| exact path count | cutting two nonadjacent edges of one closed cycle gives exactly two canonically ordered marked arcs `P_0,P_1` |
| nonadjacency | disjoint marked roots cannot meet at one root-valued cubic vertex, whose incident roots pairwise intersect |
| other channel components | unchanged closed cycles |
| disconnected carrier | a component has one or two ports: bridge, exact two-edge cut, or bounded acyclic low-port shore; consumer fires before chain invocation |
| stable ancestry | ordered marked stable darts and parent/prefix fields remain literal boundary data; retained local rows cover exactly inactive singleton, closed cycle and final connector |
| #81 relation | violates exact two-cut operation, four-terminal count and disjoint marked-root datum; no application embedding |

The exact proof is in `CO_ROOT_TERMINAL_CENSUS.md`.

## 5. Zero-parent claim census

**Fibre classification:** `EXACTLY-TWO-TERMINAL-PATHS VERIFIED IN APPLICATION SCOPE`.

| Claim | Independent disposition |
|---|---|
| complete state | current complete labelled cubic graph with active two-vertex crossed cell, literal parent and all complete-state fields |
| normalized boundary | `(A,B,C,D)=(13,13,23,23)`, selected channel `H_35`, current central root `12`, stored parent `AB|CD` |
| active local channel data | all four branches lie in `H_35`; central edge `12` does not; each active vertex has exactly two selected branch incidences |
| deletion operation | delete the two active vertices/cell and retain exactly the four outside branch darts `A,B,C,D` as terminal semiedges |
| central-edge terminal | none: the central edge is nonchannel and both endpoints are deleted |
| hidden cap/exterior terminal | none: physically retained in the complete graph and not cut except when already identical to a named branch dart |
| hidden route/profile/support terminal | none: fields do not create incidences; the productive support switch occurs only later on a closed component |
| hidden stored-prefix terminal | none: ancestry data only |
| retained vertex degree | remains `0/2`, counting retained branch semiedges |
| exact terminal count | four and only four |
| exact path count | deleting two vertices from closed `H_35` cycles gives exactly two terminal paths, whether the active vertices lie on one channel cycle or two |
| common-cycle adjacency | an additional selected edge directly joining the active vertices would be parallel to the nonchannel central edge and is a prior bounded/category output |
| ordered matching | exactly one of `AB|CD`, `AC|BD`, `AD|BC`; all carry the literal ordered branch darts |
| residual chain scope | only `AB|CD` invokes the chain, with exactly paths `A--B`, `C--D` plus closed cycles |
| other channel components | unchanged closed cycles |
| disconnected complement | one-/two-port component yields bridge, exact two-cut, or bounded low-port consumer before invocation |
| stable ancestry | active boundary darts, literal parent and prefix remain fixed source identities; crossed alignment/switch/parent move uses those same darts |
| #81 relation | three remote cuts/six terminals are not the four-branch boundary of an active two-vertex cell; no application embedding |

The exact proof is in `ZERO_PARENT_TERMINAL_CENSUS.md`.

## 6. The application-scoped lemma now justified

For either genuine application carrier `R` and its selected channel `H_h`:

```text
H_h(R)
  = P_0 disjoint-union P_1 disjoint-union closed channel cycles,
```

where `P_0,P_1` are the two ordered distinguished terminal paths and every retained source vertex has selected-channel degree `0` or `2` with boundary semiedges counted.

Consequently a shortest physical quotient path from `P_0` to `P_1` has internal nodes only of the two types already independently checked:

1. an inactive singleton;
2. a closed channel cycle.

The omitted third-terminal-path case cannot occur in either application.  This is an application restriction of the frozen local mechanism, not a restoration of the failed general theorem for arbitrary rooted carriers.

## 7. Exact relation to Heawood evidence

The detailed ledger is `HEAWOOD_WITNESS_APPLICATION_SCOPE_LEDGER.md`.

### #78 same-arc witness

It is a genuine co-root complete state.  Cutting exactly its two marked edges gives four terminals and two arcs.  It remains a counterexample to arbitrary-equal-face `Xi` totality, not to terminal exhaustion.

### #81 third-terminal witness

It cuts three channel edges, creates six terminals and has three terminal paths.  It remains a complete labelled counterexample to the broad rooted-carrier chain theorem.  It violates the exact physical operation in both genuine applications and is not discarded or weakened.

### Zero-parent Heawood model

It is a genuine active-cell boundary with exactly four `H_35` branches and two terminal paths.  Its finite escape movie is valid but is not used as the universal census proof.

## 8. Falsification ledger

| Mandatory attack | Result |
|---|---|
| hidden cap terminal | none; cap is physically glued and uncut |
| hidden exterior terminal | none; exterior is part of closed `G` |
| pre-existing cut semiedge | excluded by complete cubic source-state type |
| route/profile creates endpoint | no; metadata only |
| stored prefix creates endpoint | no; ancestry map only |
| support switch creates endpoint | no; preserves topology and is later than census |
| active deletion exposes more than four selected incidences | no; active central edge is nonchannel and each active vertex has exactly two selected branches |
| marked path is split before invocation | no; initial marked cycle is cut only at the two marked edges, producing exactly two arcs |
| disconnected carrier bypasses consumer | no; one-/two-port shore gives named bridge/two-cut/bounded output |
| #81 genuine application embedding | none in either fibre |

No application-scope counterexample was found.  No dependency or complete-state definition blocker remains.

## 9. Assurance and downstream boundary

This audit verifies exactly the omitted terminal-exhaustion hypothesis in both actual applications.  It authorizes the next step stated in issue #82:

> one narrowly application-scoped PDL addendum which invokes only the independently retained local contraction rows under the proved co-root/zero carrier hypotheses, followed by a new independent verification.

It does **not** independently re-audit or promote:

- the general rooted-carrier component-chain theorem;
- arbitrary-equal-face `Xi` totality;
- the complete inverse-parent table;
- stored-prefix return as a whole;
- ordinary induction;
- the cubic five-support theorem;
- the five-cycle-double-cover theorem.

The user's ultimate five-CDC objective remains open at this audit boundary.

## 10. No-source-mutation confirmation

Only the four required audit reports were added under

`audit/affine-cdc-terminal-exhaustion-v1/`.

No Curator baseline, RL, PDL, prior audit, `main`, Lean, manuscript, workflow, release, tag, arXiv, DOI or publication surface was modified.  No merge, rebase, squash, force-push, branch deletion or canonical movement occurred.

## 11. Final return

`[BOTH-FIBRES-SCOPED AC-SCOPE-TERMINALS-01]`.

Per-fibre returns:

```text
co-root:
  EXACTLY-TWO-TERMINAL-PATHS VERIFIED IN APPLICATION SCOPE

zero-parent:
  EXACTLY-TWO-TERMINAL-PATHS VERIFIED IN APPLICATION SCOPE
```

The permanent #81 digest remains controlling negative evidence outside this exact application scope.