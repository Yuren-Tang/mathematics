# Component-chain local theory: refutation, salvage, and surviving scope

## Reading rule

A broad false claim, its exact counterexample, the retained local mathematics and the valid narrower theorem are kept together here. No positive local table is promoted to universal continuation.

## 1. Broad rooted-carrier claim — false

**Unit:** `math.graph-theory.cycle-covers.component-chain-broad-rooted-carrier`.

The failed claim treated a shortest component chain between two distinguished terminal paths as though every internal quotient node were either an inactive singleton or a closed channel component. That omitted the possibility of a third terminal path.

### Exact counterexample

**Unit:** `math.graph-theory.cycle-covers.component-chain-third-terminal-counterexample`.

In the `h=14` six-terminal Heawood carrier, take

```text
cut edges: 1-14:13, 10-11:12, 13-14:12
P_0 = {1,2,3,4,5,6,11}
X_1 = {7,8,9,10,12,13}
P_1 = {14}
chain: P_0 -- 3-8:14 -- X_1 -- 9-14:23 -- P_1.
```

Here `X_1` is itself a third terminal path. The first legal NNI splits the old `P_0` terminal darts. Independent enumeration found 36 category-safe labelled outputs and no inherited length-one chain for the original terminal pair. Thus physical connector labels and correct local arithmetic do not preserve a terminal path after its distinguished darts split.

Authority: `audit/affine-cdc-component-chain-v1/CHAIN_INHERITANCE_AND_COROLLARY_LEDGER.md@a4f20f05532c307a3a8f9d98ac4c5162e7b8ad57`, digest `d24c63ab56320803b9c795ac08389674b6f67edf89dc5c4ef9a729c5436a3e61`.

## 2. Retained local tables

**Unit:** `math.graph-theory.cycle-covers.component-chain-local-tables`.

The counterexample does not invalidate:

- channel parity and the unique inactive triangle;
- inactive-singleton and path-plus-closed-cycle contractions;
- stable connector inheritance in those exact local rows;
- equal- and distinct-endpoint active/active root rows;
- all 84 ordered final two-terminal matching cases;
- the explicit co-root `6-7` and zero-parent `H_35` models.

These are independently reproduced finite statements. They require the carrier geometry in which their rows apply.

## 3. Valid exact-two theorem

**Unit:** `math.graph-theory.cycle-covers.component-chain-exact-two-terminal-path`.

> Let a connected application carrier have exactly two terminal channel paths, with every other nontrivial channel component closed. Then a single fixed connector list contracts the carrier to a changed terminal matching without resetting the connector rank.

This theorem uses the retained local tables. It is a specialization of the false broad claim obtained by adding the exact missing geometric hypothesis; it is not a silent repair of the broad statement.

## 4. Why the application fibres satisfy the hypothesis

Two independently reviewed terminal-exhaustion theorems provide the exact-two premise only in the genuine downstream application carriers.

### Co-root application

**Unit:** `math.graph-theory.cycle-covers.co-root-terminal-exhaustion`.

Cutting the two nonadjacent marked channel edges in the complete co-root application gives exactly four terminals, exactly two ordered marked arcs, and only closed remaining nontrivial channel components.

### Zero-parent application

**Unit:** `math.graph-theory.cycle-covers.zero-parent-terminal-exhaustion`.

The complete zero-parent application likewise has exactly two terminal channel paths and only closed remaining nontrivial channel components in its audited scope.

These results close terminal exhaustion for the two genuine singular fibres. They do not establish the earlier one-atom complete endpoint that is needed before either fibre is entered.

## 5. Surviving downstream theorem

Once a complete root-valued prescribed-parent endpoint has independently been reached, the inverse-parent value trichotomy is exhaustive: root, co-root, or zero. In the co-root and zero cases, the application terminal-exhaustion theorem supplies the exact-two premise, the component-chain theorem applies, and the conditional singular-parent move returns the literal parent or an exact terminal.

The surviving chain is therefore:

```text
complete one-atom endpoint [OPEN prerequisite]
  -> inverse-parent root/co-root/zero trichotomy
  -> application-scoped terminal exhaustion
  -> exact-two component-chain theorem
  -> conditional singular-parent move
  -> connector-prefix no-reset
  -> stored-prefix inversion.
```

The open prerequisite may not be moved below the component-chain layer.

## 6. Xi totality — false, with narrower mathematics retained

A second local warning has the same logical form.

### False broad claim

`math.graph-theory.cycle-covers.xi-arbitrary-equal-face-totality` asserted that every equal bad face forces a route change or separates the marked edges. It is false.

### Exact same-arc witness

`math.graph-theory.cycle-covers.xi-same-arc-counterexample` is the Heawood state with `h=14`, marks `1-6:12` and `2-3:34`, and equal face `9-14:23`. Both marks lie on the same outside arc; the branch swap preserves the marked route and may leave `Xi` unchanged.

Authority: audit `53be22a0f65b85068b11e5f781579618967db9dd`, digest `ff115bd13027ba947f6724e1ba861f9e9682605f955b5e2a0a42399283d5f5b1`.

### Retained replacement

The frame definition, whole-component invariance, six strict rows and bad-free route contradiction survive in their stated local scopes. Any later totality theorem must use actual marked-arc geometry; equal-face matching data alone do not determine exterior placement.

## 7. Forbidden inferences

- two distinguished terminal paths do not imply there are only two terminal paths;
- a correct local row does not supply its global hypothesis;
- a positive Heawood model does not prove universal totality;
- terminal exhaustion does not prove the prior one-atom endpoint;
- physical connector identity does not preserve a path whose terminal darts have split;
- an equal face does not by itself force strict `Xi` decrease.

## 8. Exact provenance

- component-chain audit: `a4f20f05532c307a3a8f9d98ac4c5162e7b8ad57`;
- terminal-exhaustion audit: `c954f2220c082bc3b47821657b7a1164876aeaab`;
- full v7.4.1 audit: `1e7ee9d14608bfdd3524d588d96bfc3470654686`;
- Xi audit: `53be22a0f65b85068b11e5f781579618967db9dd`;
- normalized units and relations: the fixed registry snapshot named in `../CORPUS_AUTHORITY.md`.