# ONE-ATOM operation-order exit and endpoint-collar addendum

## AC-RL-ONE-ATOM-01 / source-semantics clarification v1

**Purpose:** make explicit two source-level points used by
`ONE_ATOM_COMPLETE_ENDPOINT_TOTALITY_THEOREM_V1.md`:

1. immediate normalization of the unique bad overlap does not lose the literal
   other-order source exit;
2. the two root short sides at `L=0` are restrictions of standard atom collars,
   not unlicensed moves out of a non-root graph.

---

## 1. Comparison semantics

A one-atom comparison cell is not a path whose vertices must all be root flows.
It is a labelled source 2-cell with:

- one singular interior arc carrying the standard atom;
- root-valued long-side restrictions;
- fixed exterior darts;
- exact operation-order labels on its two ends.

The retained v7.2 state-walk theorem acts on such supplied cells.  The new
scheduler's job is to build them in a finite ordered strip.

Therefore a phrase such as “take a crossed resolution of the atom” means:

> select the corresponding root-valued boundary restriction of the standard
> singular collar.

It does not mean performing a legal root NNI starting from a graph whose
central edge is co-root.

---

## 2. Literal other-order exit

Let `A` be the atom operation and `f` the next literal source NNI.

### Disjoint case

The boundary of the commuting square is labelled

```text
A f  =  f A'.
```

The right atom collar `A'` is the literal other-order exit.

### One-vertex overlap

The union of the supports has five exterior darts.  The two operation orders
are two labelled boundary arcs of the associahedral five-leaf cell:

```text
entry:  A followed by f
exit :  f followed by A'.
```

The exit collar `A'` is fixed before any coefficient calculation by:

- the five stable exterior dart identities;
- the literal predecessor pairing of `f`;
- the operation order.

The coefficient calculation decides only whether this boundary arc is:

1. all-root;
2. zero and immediately rootifiable;
3. one standard co-root atom;
4. an exact terminal.

It does not choose a different topology.

---

## 3. Bad-overlap normalization keeps the exit boundary

In the unique bad co-root row, one intermediate local assignment contains two
adjacent co-root edges and three source vertices.  The retained normalization
NNI:

- is supported strictly inside the same five-dart carrier;
- fixes all five exterior darts;
- fixes the already selected operation-order boundary;
- replaces one internal co-root edge by a root;
- leaves at most one standard co-root collar on that same boundary arc.

Thus the transient defect tree changes the internal subdivision of the
comparison cell, not its entry or exit operation order.

The scheduler records no state before this normalization.  One complete
“advance” is the composite:

```text
pentagon relocation
    + (when required) three-vertex root-lowering normalization.
```

Its output remains the designated next edge of the fixed local path.

---

## 4. Root short sides at the exhausted prefix

When `L=0`, the singular track has two endpoint collars.

At each endpoint a standard co-root collar has exactly two crossed
root-valued restrictions.  The scheduler chooses the restriction determined by
the stored orientation of the four active darts and retains that choice through
the strip.

Attach these two restrictions as the short sides of the normalized-open
comparison.  This operation:

- adds no source move;
- changes no graph order;
- makes no support switch;
- introduces no recolouring choice;
- does not assert that the prescribed parent is root;
- is exactly the boundary datum required by the v7.2 open-track theorem.

The root rectangle produced by that theorem therefore has literal labelled
short sides already present in the comparison.  Its root `1`-skeleton gives a
source-faithful history between them.

---

## 5. Consequence

The endpoint-totality proof uses the following exact sequence:

```text
construct labelled comparison cells with a fixed operation-order exit
    -> immediately normalize the only transient two-co-root interior
    -> exhaust the literal source word
    -> cap both open atom ends by their canonical crossed root restrictions
    -> compile the supplied normalized-open comparison.
```

No non-root graph is treated as a vertex of the final root history.  No
normalization move is allowed to alter the literal source predecessor pairing.
