# Component-chain review packet

## 1. Frozen source

Review exactly:

`Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1@02b37476198e9eaa2b4cd8d2a2edd76782bdcd49`.

Primary files:

1. `FIXED_CHANNEL_COMPONENT_CHAIN_ROOT_NNI_THEOREM_V1.md`;
2. `CO_ROOT_XI_EQUAL_NEIGHBOUR_AUDIT_CORRECTION_AND_CHAIN_REPAIR_V1.md`;
3. `PURE_NNI_ZERO_PARENT_ESCAPE_MASTER_THEOREM_V1.md`;
4. `ONE_CROSS_PROOF_DAG_AND_SUPERSESSION_INDEX_V9_COMPONENT_CHAIN_REPAIR.md`.

Permanent negative audit:

`Yuren-Tang/mathematics:audit/affine-cdc-xi-co-root-v1@53be22a0f65b85068b11e5f781579618967db9dd`.

## 2. The proposed theorem

For one fixed support pair $h=ab$, let $H_h=F_a\triangle F_b$. Channel components and inactive vertices form a connected physical quotient. A shortest witnessed path between two distinguished channel paths is contracted one edge at a time by ordinary root NNIs. The final connector changes the terminal matching.

The proposed rank is the length of one retained physical path, not the distance in a finite state graph.

## 3. Local tables to verify

### Unique inactive triangle

A cubic support triangle has channel degree zero exactly when it is $[5]\setminus h$; every other triangle has degree two.

### Active/inactive row

If an active triangle and the inactive triangle share a non-channel root, the opposite root NNI should make both vertices active and extend the selected channel passage through the formerly inactive vertex.

Check:

- all support-index cases, not only the displayed $H_{35}$ normal form;
- new central root meets $h$ once;
- the two non-channel frontier roots remain stable;
- later quotient connectors remain attached to the enlarged component.

### Active/active row

At a physical non-channel edge between active components, the root alternative should cross-connect local $H_h$ passages. Check separately:

- distinct endpoint triangles;
- equal endpoint triangles and the choice of the root branch;
- path-cycle merge;
- cycle-cycle merge;
- terminal-path matching change;
- loops, parallel quotient edges and category outputs.

## 4. Quotient and inheritance

The quotient includes inactive vertices as singleton nodes. This is essential: collapsing only nontrivial channel components can make a physical path disappear.

For a selected shortest path

$$
X_0,X_1,\ldots,X_\ell,
$$

verify that after contracting $X_0X_1$ the specific edges witnessing

$$
X_1X_2,\ldots,X_{\ell-1}X_\ell
$$

still exist with the claimed endpoint components and stable identities. Existence of some new shortest path is insufficient for strict descent of the retained witness.

## 5. Final matching

When $\ell=1$, the connector joins the two distinguished paths. Verify that the root NNI changes the perfect matching of their four terminal ends rather than:

- preserving it;
- joining two ends of one path;
- creating one common path with the same marked cyclic order;
- producing a zero/non-root central value;
- triggering an unrecorded graph-category failure.

## 6. Co-root challenge

The old theorem failed because an equal face could have both marked edges on the same outside arc.

The new theorem must use the actual marked arcs. In the frozen Heawood witness:

- unproductive equal face: `9-14:23`;
- proposed productive connector: `6-7:23`;
- proposed root NNI: `123+234 -> 124+134`;
- proposed route change: `(1,2)|(3,6) -> (1,3)|(2,6)`.

Independently verify all stable darts, root labels, graph category, cap disjointness and route order.

## 7. Zero-parent challenge

Normalize to `(13,13,23,23)` and $H_{35}$. Verify:

1. category-safe carrier connectivity after deleting the active cell;
2. initial full-lock matching `AB|CD`;
3. chain contraction to a crossed matching;
4. alignment of the active crossed root sheet;
5. exactly one legal closed $H_{35}$ switch;
6. active word `(15,13,25,23)` up to the stated symmetry;
7. central root $35$ on the literal parent NNI;
8. preservation of target topology, cap, route, darts and stored prefix.

## 8. Integration challenge

Even if the standalone chain theorem is correct, test whether its outputs match the complete prescribed-parent state expected by the stored-prefix consumer. In particular:

- are all category exits explicitly consumed?
- can a chain move change the selected cap or active parent cell?
- can support labels or missing-index data migrate?
- does the chain rank interact with the target-topology rank without reset?
- after the literal parent NNI, is the next stored source move exactly the one claimed?

## 9. Acceptable review outcomes

1. `INDEPENDENTLY SUPPORTED COMPONENT` with exact scope and dependencies;
2. `BOUNDED REPAIR REQUIRED` with the smallest corrected statement and witness maps;
3. `MATERIAL FAILURE` with a complete source state and the precise broken implication.

A broad statement that the mechanism is plausible is not a useful outcome.