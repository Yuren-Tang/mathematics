# Prefix-directed one-atom local macro certificate

## AC-RL-ONE-ATOM-01 / research dossier v1

**Depends on:**

- `ONE_ATOM_COMPLETE_STATE_INTERFACE_AND_QUANTIFIER_MAP_V1.md`;
- `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`;
- `FIVE_LEAF_PACHNER_PENTAGON_ROOT_INTERVAL_V1.md`;
- `FIVE_LEAF_ROOT_TOPOLOGY_CYCLE_CLASSIFICATION_V1.md`;
- `FIVE_LEAF_C5_C6_CONTEXTUAL_RETURN_V1.md`;
- the v7.2 single-pop and state-walk files.

**Purpose:** prove one bounded macro which transports one standard co-root atom
past the next **literal** stored source NNI, or produces a complete root endpoint
or exact terminal.

---

## 1. Stable local input

Let `a` be the named standard atom edge and let `f` be the head of the remaining
source word.  The input records:

- the two labelled vertices supporting `a`;
- the two labelled vertices supporting `f`;
- every external stable dart of their union;
- the literal predecessor pairing of `f`;
- the two crossed root resolutions of `a`;
- the complete parent, cap, route, support and ancestry fields.

The macro is required to end on the other-order side of `f`.  That side is
fixed by the source word and is not chosen by a root-connectivity search.

---

## 2. Disjoint and coincident supports

### 2.1 Disjoint supports

If the vertex supports are disjoint, the two local replacements commute
strictly.  Their edge-value assignments agree off the two supports and their
stable dart maps are the product of the two disjoint maps.

The square moves the atom collar to the predecessor side of `f`.  The atom
remains standard, the exact head entry `f` is deleted, and no local rank is
opened.

### 2.2 Identical support

If the supports are the same two labelled vertices, the literal predecessor
pairing is one of the two crossed resolutions of the standard co-root atom.
That resolution is root-valued.  Taking it gives a complete root endpoint on
the exact predecessor topology.

A loop, forbidden parallel incidence, invalid target reconnection or route
change is returned immediately through the existing exact terminal ledger.

There is no third two-vertex intersection type.

---

## 3. One shared vertex gives one labelled five-leaf problem

Assume the supports meet in exactly one source vertex.  Their union is a
three-vertex path with five ordered exterior darts.  Forgetting no label, it is
one five-leaf associahedral overlap.

For a fixed conserved five-root boundary word, a five-leaf topology is
root-valued exactly when its two cherries are root-valued.  The fifteen labelled
topologies therefore form the size-two-matching graph of the exact
root-adjacency graph on the five boundary positions.

The retained classification gives only:

\[
\varnothing,\qquad C_5,\qquad C_6.
\]

Because the input standard atom has two crossed root resolutions, the local
root sector is nonempty.  Hence it is exactly one labelled `C5` or one labelled
`C6`, with every internal root value forced by the exterior word.

No unrelated recolouring is selected.

---

## 4. Atom edges of the local cycle

Every root NNI edge of the local root cycle has one third binary resolution.

- If that value is a co-root, the third resolution is one standard co-root
  atom.
- If it is zero, the retained inverse-flip zero alternative rootifies
  immediately.
- A root third resolution is simply an all-root local triality and gives a
  complete root route through the cell.

Thus a persistent standard atom is represented by a **co-root-labelled edge**
of the local root cycle.

The current operation order determines one entry atom edge `e_in`.  The literal
predecessor pairing of `f`, together with the same five stable exterior darts,
determines one exit resolution `e_out`: it is the unique local singular collar
obtained when the atom operation is placed on the other side of the named
source NNI.

`e_out` is topology data, not a chosen endpoint.

---

## 5. Canonical local path and rank

Order the five exterior stable darts by their stored source identities.  Among
the two cyclic paths from `e_in` to `e_out`, choose:

1. the shorter path;
2. if the lengths tie, the path whose first moved stable dart is earlier in the
   stored order.

This defines a literal finite path in the exact labelled `C5` or `C6`.  Let

\[
\mu=\text{number of atom-edge advances still required on this path}.
\]

The cycle diameter gives

\[
0\le \mu\le3.
\]

One atom-edge advance uses the shared root topology between two consecutive
cycle edges as its root slice.  The corresponding labelled pentagon cell has
exactly one of:

1. a fully root-valued advance;
2. a co-root first failure, normalized to one standard atom;
3. a zero third resolution, which rootifies and terminates;
4. an exact route/category terminal.

In the persistent co-root branch, the advance lowers `mu` by one.  The unique
bad overlap may transiently contain two adjacent co-roots, but the retained
root-lowering NNI is part of the same atomic advance; no scheduler state is
recorded before normalization.

When `mu=0`, the atom collar is on the other-order side of the literal source
NNI.  Delete exactly that head source obligation.  No alternate source step is
substituted.

---

## 6. Human exhaustion of the cycle types

### 6.1 Support-five-cycle sector

For a support-five-cycle boundary, the root topology sector is `C5`.  Every one
of its five NNI edges has co-root third resolution.  Therefore every local
advance is a standard co-root relocation.  The edge-cycle diameter is two, so
the chosen exit is reached after at most two persistent relocations.

### 6.2 Mixed triangle-plus-double sector

For a noncomplementary triangle-plus-double boundary which contains a co-root
atom edge, the root sector is a mixed `C6`:

```text
4 co-root singular edges
2 zero singular edges.
```

A chosen path either reaches the exact exit after at most three co-root
relocations, or meets a zero edge first.  In the latter event the immediate
zero alternative supplies the required complete root endpoint.  It is success,
not a persistent zero-token state.

### 6.3 All-zero `C6` and empty sector

The all-zero `C6` has no co-root singular edge, and the empty sector has no root
resolution.  Neither can contain the input standard co-root atom.  They are
therefore excluded by the input type, not by a scheduling choice.

---

## 7. Independent finite certificate

`finite/one_atom_prefix_overlap_census_v1.py` exhausts:

- the ten roots;
- all fifteen labelled five-leaf topologies;
- all `6240` ordered conserved five-root boundary words;
- every root NNI edge and its third-resolution type;
- the directed standard-co-root rows on one labelled pentagon.

It returns:

```text
sector counts
    empty            600
    C5 all co-root  1440
    C6 all zero      600
    C6 mixed        3600

directed standard-co-root pentagon rows
    01000            360
    01100            120
    01110            240

maximum root-cycle diameter
    3
```

Canonical digest:

`6d51dab3f1fe4cf10411fdf8d7137e22d0d061b9ca0fac941ad922b673df04f3`.

The script is an exhaustion check.  The controlling proof is the
Eulerian-boundary/matching classification and the explicit source-dart path
above.

---

## 8. Source-step crossing theorem

### Theorem `ONE-ATOM-NEXT-SOURCE-STEP-MACRO`

Let a complete contextual state carry at most one standard co-root atom and let
`f` be the next literal stored root-NNI predecessor obligation.  Then a bounded
source-faithful local comparison, using no cancellation and no lower-order call,
ends in exactly one of:

1. a complete root-valued crossed endpoint retaining the live parent, cap,
   route, support, dart and ancestry fields;
2. one standard co-root atom on the other-order side of `f`, with `f` deleted
   from the literal source word;
3. an exact current-descendant route/cut/bounded terminal.

In Case 2 the only scheduler decrease is deletion of the named source step.
All root detours and atom relocations occur inside the bounded local macro and
are controlled by `mu<=3`.

### Proof

The supports are disjoint, identical or meet in one vertex.  Sections 2 and 3
exhaust the topology.  In the one-vertex case, the atom and the desired
other-order collar are singular edges of the same exact labelled nonempty root
cycle.  The canonical path is of length at most three.  Every edge advance is
one retained local critical-overlap cell and immediate normalization; a zero
edge rootifies, a category failure terminalizes, and otherwise the standard
atom advances.  At the exit the uncoloured operation order is exactly the
literal predecessor order, because `e_out` was defined by the stored source
pairing and five stable darts.  Therefore the head source step is crossed
literally.  ∎

---

## 9. What this theorem does not use

The local macro does not use:

- a general root/NNI connectivity theorem;
- a global finite-state or SCC argument;
- a full `C5` or `C6` lap as recurrence;
- track erasure as progress;
- a support switch;
- the component-chain theorem;
- an arbitrary equal-face selector;
- same-order root solubility;
- a second cancellation or lower-order call.

The `C5/C6` objects are exact bounded five-leaf coefficient tables with a fixed
entry edge and fixed exit edge.  Their use is a finite local macro, not a global
reconfiguration principle.
