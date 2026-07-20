# AffineCDC mathematical architecture

This file separates the complete Cycle Double Cover theorem from the open five-support strengthening and identifies the current controlling proof interfaces.

## 1. Three mathematical scopes

1. **Affine compatibility core**  
   For a finite loopless cubic graph carrying a nowhere-zero binary flow, classify local affine families and prove a globally compatible choice in rank three.

2. **Complete CDC theorem**  
   Starting from an arbitrary finite-active multigraph with no singleton cut, supply the cubic binary-flow object, extract a graph-level even cover, transport it through collapse, decompose once, and reinsert loops.

3. **Five-support strengthening**  
   Ask whether a compatible cover can be chosen with only five indexed supports, equivalently as a root-valued `E₅` flow.

Scope 3 is open and is not used in Scope 2.

## 2. Natural complete theorem

The controlling Programme A theorem is:

> Every multigraph with finite active edge set and no singleton cut has a finite circuit double cover.

A circuit is a nonempty inclusion-minimal finite cut-even support. Circuits are exactly singleton loops, parallel-edge digons, and ordinary simple cycles.

For nonloop edges, singleton-cut status is equivalent to bridge status. The cut formulation is controlling because loops cross no cuts and cut parity is the invariant transported through collapse.

## 3. Foundations and occurrence semantics

The natural local parity of a finite support counts endpoint occurrences. Loops contribute two. A support is cut-even exactly when its intrinsic half-edge boundary is empty.

The cover witness is a finite indexed family or finite multiset of occurrences. Equal support values at distinct indices remain distinct occurrences; empty supports are allowed. Every active edge object must belong to exactly two occurrences.

Circuit characterization and circuit decomposition are separate interfaces:

- foundations characterize minimal cut-even supports;
- the terminal decomposition theorem proves that every finite cut-even support is a disjoint union of circuits.

## 4. Loop normalization

Delete all loops to form the loopless core `G₀`.

- every cut is unchanged;
- no-singleton-cut status is equivalent for `G` and `G₀`;
- every nonloop circuit has identical status in both graphs;
- every circuit containing a loop is exactly that singleton loop.

A circuit double cover of `G₀` extends uniquely up to reindexing by adding two singleton occurrences for every deleted loop. Conversely, every circuit double cover of `G` contains exactly those forced loop occurrences.

## 5. Port-cycle cubic expansion

For every active vertex of the loopless core, choose a cyclic order on its incidence set. Replace the vertex by a cycle of incidence ports and lift each original edge between its two corresponding ports.

The result is a finite loopless cubic multigraph `H` with:

- collapse map `π:V(H) → V(G₀)`;
- injective original-edge lift `λ:E(G₀) → E(H)`;
- internal fibre edges and external lifted edges as a disjoint partition;
- degree-two fibres represented by two distinct parallel internal edges;
- exact size formulae `|V(H)|=2|E(G₀)|` and `|E(H)|=3|E(G₀)|`;
- exact edge-bearing component correspondence;
- preservation of the no-singleton-cut condition;
- cut pullback `δ_H(π⁻¹(S)) = λ(δ_{G₀}(S))`.

## 6. Binary-flow boundary

Seymour’s nowhere-zero six-flow theorem is the sole external non-elementary logical input.

Programme A proves the remaining transport internally:

1. a six-flow is literally an eight-flow by range inclusion;
2. modular reduction gives a nowhere-zero `Z/8Z` flow;
3. a spanning-forest argument counts all flows over any finite abelian group;
4. inclusion–exclusion counts nowhere-zero flows;
5. the count depends only on the group order;
6. order eight transports existence from `Z/8Z` to `F₂³`.

Tutte’s equal-order group-flow theorem is historical provenance, not a logical black box.

On the loopless graph, characteristic two removes orientation and gives the once-per-edge incidence-sum representation.

## 7. Affine compatibility centre

For every edge `e`, put

`Q_e = Γ / <f(e)>`.

The incidence space `E_f` is the direct sum of one copy of `Q_e` for every dart.

- `L_vert` records homogeneous vertex translations;
- `κ + L_vert` is the product of local affine-family torsors;
- `L_edge` is the direct sum of endpoint diagonals.

The pair complex is

`P_f : L_vert ⊕ L_edge → E_f`.

Compatibility is equivalent to each of:

- nonempty affine intersection `(κ+L_vert) ∩ L_edge`;
- vanishing of `[κ]` in `E_f/(L_vert+L_edge)`;
- solvability of the quotient equation `δ_f m = c_f`;
- annihilation of `κ` by every equilibrium stress.

The pair complex is the complete compatibility object. It does not retain named graph edges, darts, local-line semantics, or indexed-support extraction. The source graph and flow remain attached.

## 8. Rank-three Fano theorem

For `Γ=F₂³`, every quotient `Q_e` is a canonical anisotropic quadratic plane.

- each local vertex translation space is Lagrangian;
- its affine family is the characteristic torsor;
- the global edge diagonal is a totally singular Lagrangian.

The characteristic-torsor intersection theorem states that `Char_q(L) ∩ M` is nonempty exactly when `q` vanishes on `L∩M`. Total singularity of the edge diagonal makes the condition automatic.

Therefore every cubic nowhere-zero `F₂³` flow has a globally compatible affine family. The solution set is a torsor under `L_vert ∩ L_edge`.

## 9. Graph-level even-support extraction

A compatible family assigns one common two-point affine line to every graph edge. For each point `s∈F₂³`, define the support of edges whose assigned line contains `s`.

- local family evenness gives zero or two selected edges at every cubic vertex;
- every edge line contains exactly two points, so every edge belongs to exactly two indexed supports;
- empty and repeated indexed supports remain distinct occurrences;
- graph and dart data supply the endpoint-independent descent from incidence lines to edge objects.

On a loopless graph, once-per-edge vertex parity equals intrinsic half-edge boundary parity and hence cut parity. The extracted family is therefore an intrinsic even double cover of `H`.

## 10. Collapse and decomposition

Project a support `F'⊆E(H)` to

`{e∈E(G₀):λ(e)∈F'}`.

The pulled-back-cut identity preserves cut parity memberwise. For every original edge, membership in a projected support is equivalent to membership of its lifted edge upstairs, so indexed occurrence multiplicity remains exactly two.

Circuit structure is not projected: an upstairs circuit may disappear, cease to be minimal, or split. The invariant transported through collapse is cut-even support plus occurrence multiplicity.

After collapse, decompose every finite cut-even support by induction on its cardinality. Choose a circuit sub-support, remove it by symmetric difference, and iterate. Concatenating memberwise decompositions preserves every edge multiplicity exactly.

Finally reinsert loops with two forced singleton occurrences each.

## 11. Complete dependency chain

```text
foundational finite-active multigraph semantics
→ loop deletion
→ port-cycle cubic expansion
→ Seymour six-flow
→ internal order-eight group-flow transport
→ affine pair complex
→ rank-three characteristic-torsor intersection
→ graph/dart indexed support extraction
→ loopless parity adapter
→ cut-even collapse
→ terminating circuit decomposition
→ loop reinsertion
→ finite circuit double cover
```

The preferred detailed reading is [`complete-cdc/README.md`](complete-cdc/README.md).

## 12. Five-support architecture

The five-support programme begins with a root-valued flow into the ten roots of `E₅`. The complete fixed-lift object is the full cycle-face dual triangulation, not only the global support-colour quotient.

Its active architecture remains:

1. root-flow lifting;
2. surfaces and half-cube target;
3. vertical gauge and horizontal reconfiguration;
4. cuts, four-poles, and routing;
5. holonomy, defects, and atoms;
6. localization/composition frontier;
7. independent proof families;
8. finite laboratories.

Programme A consumes no Programme B checkpoint.

## 13. Provenance and assurance

- exact Programme A map: [`PROGRAMME_A_INTEGRATION_MAP.md`](PROGRAMME_A_INTEGRATION_MAP.md);
- assurance boundary: [`PROGRAMME_A_ASSURANCE_BOUNDARY.md`](PROGRAMME_A_ASSURANCE_BOUNDARY.md);
- exact intake manifest: [`PROGRAMME_A_INTEGRATION_MANIFEST.md`](PROGRAMME_A_INTEGRATION_MANIFEST.md);
- authorial dossiers: [`proof-development/`](proof-development/);
- five-support corpus: [`five-support/README.md`](five-support/README.md).

Programme A is Curator-integrated authorial paper-proof mathematics. It is not independently audited, end-to-end Lean verified, manuscript-approved, peer reviewed, published, released, or DOI-dispositioned.