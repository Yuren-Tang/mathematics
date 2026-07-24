# AC-PD v7.4.1 — application-scoped fixed-channel component chain

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Workstream:** `AC-PD-5CDC-V7.4.1-01`  
**Exact PDL start:** `e36ba22f09e3a9fc6358f3b03615f8fde6c00d96`  
**Terminal-exhaustion audit:** `audit/affine-cdc-terminal-exhaustion-v1@c954f2220c082bc3b47821657b7a1164876aeaab`  
**Local-row/component-chain audit:** `audit/affine-cdc-component-chain-v1@a4f20f05532c307a3a8f9d98ac4c5162e7b8ad57`  
**Permanent `Xi` negative audit:** `audit/affine-cdc-xi-co-root-v1@53be22a0f65b85068b11e5f781579618967db9dd`  
**Classification:** `APPLICATION-SCOPED COMPLETE-DRAFT / GENERAL ROOTED-CARRIER THEOREM FAILED OUTSIDE APPLICATION SCOPE`.

---

## 1. Permanent withdrawal and exact retained content

The v7.4 theorem `FC-COMPONENT-CHAIN-ROOT-NNI` is false for an arbitrary rooted
carrier having merely two distinguished terminal paths.  Audit #81 gives a
complete category-safe carrier with a third terminal path as an internal quotient
node; no one-NNI inherited chain between the original distinguished pairs exists.
The permanent certificate digest is

`d24c63ab56320803b9c795ac08389674b6f67edf89dc5c4ef9a729c5436a3e61`.

Accordingly this packet does not repair, weaken by prose, or retain that general
theorem as active authority.

Independently retained from #81 are only:

1. fixed-channel degree `0/2` and the unique inactive triangle;
2. the six active/inactive rows and their exact stable-dart continuation;
3. the six distinct active/active rows;
4. the nine equal-endpoint root branch swaps, with the zero placement excluded;
5. path-plus-closed-cycle contraction;
6. final two-terminal-path matching change in all ordered rows;
7. exact category, cap and stable-dart move contracts.

The controlling local table is the independently audited content of

`AC_PD_V7_4_COMPONENT_CHAIN_ROW_AND_DART_TABLES.md`

as checked at `a4f20f05532c307a3a8f9d98ac4c5162e7b8ad57`, local-row digest

`75ed977851a944f2cd80577e629a2f6936da5dfce49ad9d5a9e0e82c8b2494d4`.

---

## 2. Exact conditional object

Fix one complete labelled current root state and one physical support channel

\[
H_h=F_a\triangle F_b.
\]

Let `R` be a connected category-safe carrier with four ordered selected-channel
terminal darts.  Assume the following **exact-two-path hypothesis**:

\[
\boxed{
H_h(R)=P_0\ \dot\cup\ P_1\ \dot\cup\ C_1\ \dot\cup\cdots\dot\cup\ C_s,
}
\]

where:

- `P_0,P_1` are the two ordered distinguished terminal paths;
- each `C_i` is a closed nontrivial `H_h` cycle;
- every remaining channel-inactive vertex is represented individually;
- no third selected-channel terminal path exists;
- every terminal dart, stable edge identity, cap datum, parent datum and stored-
  prefix ancestry is literal current-state data.

This hypothesis is not inferred from the phrase “two distinguished paths”.  It
must be supplied by one of the two independently verified application
constructors in Sections 7 and 8 below.

---

## 3. Fixed-channel quotient under the exact hypothesis

The physical quotient `Q_h(R)` has:

### Nodes

1. one node for `P_0`;
2. one node for `P_1`;
3. one node for every closed cycle `C_i`;
4. one singleton node for every channel-inactive vertex of type
   `[5]\setminus h`.

### Edges

Every stable physical edge outside `H_h` becomes a witnessed quotient edge with:

- stable edge id;
- ordered endpoint darts;
- current root;
- current endpoint nodes;
- stored-prefix ancestry.

Parallel quotient edges and quotient loops remain represented.  A quotient loop
is not used in a simple path.  A physical loop, forbidden parallel degeneration,
bridge, cyclic `2/3/4` cut or bounded low-port object is returned to its exact
consumer before continuation.

Connectivity follows by projecting any physical path in connected `R`; inactive
vertices are retained as singleton nodes and no path segment disappears.

---

## 4. One inherited witnessed chain

Choose once a shortest simple quotient path

\[
P_0=X_0,c_1,X_1,c_2,\ldots,c_\ell,X_\ell=P_1,
\]

retaining every exact stable connector `c_i` and both endpoint darts.

Because of the exact-two-path hypothesis, each internal node `X_i` is exactly:

1. one inactive singleton; or
2. one closed channel cycle.

The #81 third-terminal-path type is excluded by hypothesis, not by local
contraction.

Define the stage rank as the number of remaining connectors in this one inherited
list.  The list is never reselected and quotient distance is never recomputed.

---

## 5. Inactive-singleton contraction

Suppose the first internal node is inactive.  Apply the independently audited
active/inactive root NNI at `c_1`.

The move:

- makes both source vertices channel-active;
- inserts the new channel central edge into the passage from `X_0`;
- absorbs the inactive singleton into the enlarged distinguished path;
- preserves the next stable connector even if `c_1,c_2` both meet the same source
  vertex;
- leaves the root of `c_2` unchanged and outside `H_h`;
- fixes the outside endpoint/dart and transfers only the displayed inside dart;
- leaves every later stable connector unchanged.

Thus the literal inherited chain is

\[
X_0',c_2,X_2,\ldots,c_\ell,P_1.
\]

The rank drops by deletion of the named edge `c_1`, not by a new distance
calculation.

---

## 6. Closed-cycle contraction and final connector

Suppose the first internal node is one closed channel cycle.  The connector is
the unique nonchannel incidence at its active endpoint.  Therefore the next
distinct connector cannot leave at the same modified active vertex.

Use the audited distinct root NNI or equal root branch swap:

- path plus closed cycle becomes one path with the same two terminal darts;
- the new central root remains outside `H_h`;
- later connectors remain at untouched stable vertices;
- only the first two quotient nodes are joined;
- no later component is silently merged.

Again the old stable connector list with its first witness deleted is the
inherited chain.

When one connector remains, it joins the two distinct named terminal paths.
The audited ordered-dart table proves that the root alternative changes

\[
AB\mid CD
\]

to exactly one of

\[
AC\mid BD,\qquad AD\mid BC.
\]

For equal endpoint triangles the move is the other root placement, never the
zero placement.  The #78 same-arc obstruction does not apply because the two
local passages are different named terminal components.

---

## 7. Co-root application constructor

The conditional theorem may be invoked in the co-root fibre only after the exact
constructor audited in

`CO_ROOT_TERMINAL_CENSUS.md@c954f2220c082bc3b47821657b7a1164876aeaab`:

1. begin with a complete closed category-safe co-root state;
2. choose the current locked physical channel `H_h`;
3. cut exactly the two distinct nonadjacent marked channel edges with disjoint
   root labels;
4. retain their four ordered endpoint darts;
5. test disconnected-carrier bridge/two-cut/bounded consumers first;
6. obtain exactly two ordered marked arcs and only closed remaining channel
   components.

Only then may the conditional chain of Sections 3--6 be called.

The #81 carrier cuts three channel edges, has six channel terminals and has no
pair of distinct disjoint marked parent roots among its cut labels.  It is not an
instance of this constructor.

---

## 8. Zero-parent application constructor

The conditional theorem may be invoked in the zero fibre only after the exact
constructor audited in

`ZERO_PARENT_TERMINAL_CENSUS.md@c954f2220c082bc3b47821657b7a1164876aeaab`:

1. begin with the complete normalized state `(13,13,23,23)` and current central
   root `12`;
2. select the physical channel `H_35`;
3. delete exactly the active two-vertex cell;
4. retain exactly the four ordered outside branch darts `A,B,C,D`;
5. note that the active central edge is nonchannel and creates no terminal;
6. test disconnected-complement bridge/two-cut/bounded consumers first;
7. consume a crossed outside matching immediately;
8. in the residual `AB|CD` lock obtain exactly paths `A--B`, `C--D` and closed
   remaining cycles.

Only the residual lock invokes the conditional chain.

The #81 three-cut/six-terminal carrier is not the boundary of any active
two-vertex cell and cannot be transported into this constructor by a support
permutation.

---

## 9. Complete source-field contract

At every contraction step retain or update literally:

- graph order;
- every stable edge identity and ordered dart;
- the four application terminal darts;
- the fixed physical channel;
- cap vertices, cap edge and ordered cap darts;
- route/profile and current channel-component partition;
- literal prescribed-parent topology;
- category and terminal flags;
- support transport and missing-index coordinates;
- stored-prefix ancestry.

After each move recompute the exact current graph/category, route, cap and parent
fields.  Any named output is consumed on the current descendant.

No support switch occurs inside the conditional contraction.  No cancellation,
lower-order call, track erasure, generic NNI connectivity, finite-state/SCC
distance, `Q_N`, `M_N`, `d_N`, nested bubble or terminal frame is used.

---

## 10. Conditional theorem

### Theorem `FC-EXACT-TWO-TERMINAL-PATH-COMPONENT-CHAIN`

Under the explicit decomposition

\[
H_h(R)=P_0\dot\cup P_1\dot\cup\text{closed channel cycles}
\]

and the complete labelled source-field contract above, there is a finite
same-order history of audited root NNIs/equal root branch swaps which ends in:

1. an exact named route/category/cut/bounded terminal; or
2. a category-safe state whose ordered matching on the four terminal darts is
   different from the initial matching.

Every pre-final move deletes the first witness in one inherited stable-connector
list.  The theorem has no claim outside the exact-two-terminal-path domain.

---

## 11. Assurance boundary

Closed here at PDL reconstruction level:

- the conditional exact-two-path contraction;
- explicit import of both #82 application constructors;
- exclusion and preservation of the #81 counterexample;
- use of only #81-retained local rows;
- stable-dart, cap, parent, route and prefix contracts;
- no rank reset within one parent obligation.

Not claimed:

- the failed general rooted-carrier theorem;
- independent end-to-end acceptance;
- a five-support or five-CDC theorem.