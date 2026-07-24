# AC-PD-5CDC v7.3 — fixed-channel switch-invariant Xi reconstruction

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Frozen Research Lead input:** `research/affine-cdc-five-cdc-v1@212d789a5967813e7277fb3e269060926c99cb0e`  
**Classification:** `COMPLETE-DRAFT FOR THE CO-ROOT/DDD PRESCRIBED-PARENT SECTOR / DOES NOT ADDRESS A ZERO PRESCRIBED PARENT`.

This dossier independently reconstructs the new fixed-channel repair from
`DDD_LOCK_H14_SWITCH_INVARIANT_DESCENT_THEOREM_V1.md`.  It replaces, rather
than repairs, the quarantined `Omega` plateau-orbit argument.  No `2--0`
cancellation, lower-order call, finite-SCC distance, `Q_N`, `M_N`, `d_N`,
nested bubble or terminal frame is used.

---

## 1. Complete co-root prescribed-parent state

Fix one complete prime fixed-order state with live prescribed parent.  The two
marked roots are disjoint:

\[
p\cap q=\varnothing,
\qquad p+q=Q_m,
\]

where `m` is the unique unused support index.  The complete state retains the
labelled graph, ordered darts, both crossed sheets, literal prescribed-parent
topology `P`, cap block, route/profile field, all support-component attachment
data, terminal flags and the identity map `alpha` to the stored pure-NNI
prefix.

A **rescue root** is a root meeting both `p` and `q`.  There are exactly four.
In a nonterminal oriented DDD full-channel lock, every rescue system joins the
two marked occurrences in one physical component and has the prescribed
oriented route.

Choose one rescue root and keep that support pair fixed during the descent:

\[
h_*.
\]

This is a chosen support channel, not a quotient by support permutations and
not an assertion that an arbitrary missing-index migration preserves a
numerical rank.

---

## 2. Unique transported `H_14` frame

Write

\[
p=\{p_0,p_1\},\qquad q=\{q_0,q_1\},
\]

and suppose

\[
h_*=\{p_0,q_0\}.
\]

There is exactly one support bijection `eta` satisfying

\[
\eta(p)=12,\qquad
\eta(q)=34,\qquad
\eta(m)=5,\qquad
\eta(h_*)=14.
\]

Indeed the selected support of `p` must go to `1`, the other support of `p` to
`2`, the nonselected support of `q` to `3`, the selected support of `q` to `4`,
and the unused support to `5`.  These five assignments exhaust the support
set, proving uniqueness.

Let `tau_14` be the support transposition `(1 4)`.  A switch of the common
marked `H_{h_*}` component changes the marked roots in canonical coordinates
as

\[
12\longmapsto24=\tau_{14}(12),
\qquad
34\longmapsto13=\tau_{14}(34).
\]

Transport the canonical frame by

\[
\eta'=\tau_{14}\circ\eta.
\]

Then the new marked roots again map to `12,34`, the unused support maps to `5`,
and the same support channel maps to `14`.  This is the exact common-marked
migration law.

### Scope of all-index transport

The proof does not assert that one numerical `Xi` is invariant under every one
of the ten possible support switches.  At a given locked state choose one
physical rescue support `h_*` and run the deterministic descent using only:

- switches of closed `H_{h_*}` components;
- the displayed ordinary root NNIs;
- exact absorbing consumers.

If an independently chosen all-index migration is considered elsewhere in the
complete transition graph, its endpoint is simply another complete state at
which a new rescue support and canonical frame may be chosen.  A terminal-free
SCC would have to contain the deterministic fixed-channel path from each of
its states, so this scope is sufficient for SCC exclusion.

---

## 3. The vertex weight and complete-component invariance

For a canonical support triangle `T`, define

\[
\begin{array}{c|cccccccccc}
T&123&124&125&134&135&145&234&235&245&345\\
\hline
\xi(T)&1&0&1&0&0&0&1&2&1&0.
\end{array}
\]

The `tau_14` orbits are

\[
123\leftrightarrow234,\qquad
125\leftrightarrow245,\qquad
135\leftrightarrow345,
\]

with `124,134,145,235` fixed.  Therefore

\[
\boxed{\xi(\tau_{14}T)=\xi(T)}
\]

for every one of the ten triangle types.

For a complete closed root state `S`, put

\[
\boxed{
\Xi(S)=\sum_{v\in V(G)}\xi\bigl(\eta(\Delta_v)\bigr).}
\]

The sum includes every labelled vertex, including fixed cap vertices and all
vertices exterior to the local equal-face or NNI cell.  Hence

\[
0\le \Xi(S)\le 2|V(G)|.
\]

### Lemma 3.1 — unmarked component switch

Let `Z` be a closed `H_{h_*}` component containing neither marked root
occurrence.  Switching `Z` applies `tau_14` to the canonical triangle at every
vertex of `Z` and changes no triangle outside `Z`.  Since `xi` is
`tau_14`-invariant, every summand is unchanged and

\[
\Xi(S^Z)=\Xi(S).
\]

### Lemma 3.2 — common-marked component switch

Suppose `Z` contains both marked root occurrences and the switch is nonabsorbing.
The physical switch applies `tau_14` to every triangle on `Z`; the transported
frame applies a further `tau_14` to every triangle in the complete graph.
Consequently:

- vertices on `Z` are acted on twice and return to their former canonical type;
- vertices outside `Z` are acted on once, but `xi` is invariant.

Thus again

\[
\boxed{\Xi(S^Z)=\Xi(S).}
\]

If a component contains exactly one marked occurrence, it is a separating
rescue component and is absorbed by the literal parent-repair movie rather
than treated as a nonexit switch.

This vertexwise proof is the exact repair of the old `Omega` error: no exterior
component contribution is omitted or assumed to cancel.

---

## 4. Six exhaustive distinct-neighbour rows

Call

\[
\mathcal B=\{123,234,125,245\}
\]

the bad channel types.  At a bad vertex select root `23` for types `123,234`
and root `25` for types `125,245`.  Since the four boundary roots of the
canonical DDD carrier are `12,12,34,34`, neither selected root is a boundary
semiedge.  The selected incidence is therefore an internal carrier edge.

There are three triangles containing a fixed root, hence three unordered
distinct pairs.  The complete table is

\[
\begin{array}{c|c|c|c|c}
\text{central root}&\text{source pair}&\text{opposite root pair}
&\Xi_{\rm source}&\Xi_{\rm target}\\
\hline
23&123+234&124+134&2&0\\
23&123+235&125+135&3&1\\
23&234+235&245+345&3&1\\
25&125+245&124+145&2&0\\
25&125+235&123+135&3&1\\
25&245+235&234+345&3&1.
\end{array}
\]

For example, in the first row the four exterior roots are `12,13,24,34`.
The root-valued opposite pairing is

\[
12\mathbin{-}24,\qquad13\mathbin{-}34,
\]

with common new central root `14`, producing triangles `124,134`.  The other
pairing uses `12,34` and is co-root-valued, so the displayed opposite pair is
unique.  The remaining five rows are identical tetrahedral calculations.

Every row satisfies

\[
\boxed{\Delta\Xi=-2.}
\]

A fresh finite enumeration of the ten triangles independently recovered these
six rows, their unique root-valued opposite pairings and the six values `-2`.

### Source-field preservation

The NNI is performed on one labelled internal edge.  It fixes every exterior
dart of the two-vertex cell, every coefficient outside the cell, the literal
parent obligation and the prefix map `alpha`.  The cap vertices and cap darts
remain the same labelled objects.  The resulting component partitions and
route field are recomputed.  The exact category test then gives one of:

1. separating channel and literal parent repair;
2. cap-compatible `K_i` state;
3. named cyclic `2/3/4`-cut or bounded terminal;
4. another complete prime oriented lock with `Xi` smaller by two.

There is no coefficient-only transition.

---

## 5. Four equal-neighbour root-only macros

The equal cases are exactly

\[
123+123,\quad234+234,\quad125+125,\quad245+245
\]

on central root `23` or `25`.

### 5.1 Exact branch placements

For an equal pair of triangle type `T`, let the central root be `r` and the two
other roots be `x,y`.  The four exterior darts are

\[
u_x,u_y,v_x,v_y.
\]

The three pairings are:

1. `u_x u_y | v_x v_y`, the current root equal-face placement;
2. `u_x v_y | u_y v_x`, the other root branch-swap placement;
3. `u_x v_x | u_y v_y`, whose two central sums are zero.

Only the first two are used.  Suppress the exterior `H_14` system to its
matching on the four local ports.  If its matching is the third matching, the
root branch swap changes the oriented channel route and is absorbing.  If its
matching equals one of the two root placements, that placement has the two
local `H_14` passages in two distinct closed components.  Thus zero or one
root-valued branch-swap reaches a split placement.

No zero edge is inserted.

### 5.2 Switch one local passage

Switch the closed `H_14` component containing exactly one local passage.  If
it separates the marked parent roots, enters `K_i`, or creates a named
category terminal, absorb the result.  Otherwise it is a nonexit complete
component switch and preserves `Xi` by Section 3.

Locally it changes exactly one triangle by `tau_14`:

\[
123\leftrightarrow234,\qquad
125\leftrightarrow245.
\]

The pair is consequently `123+234` or `125+245`.

### 5.3 Final strict NNI

For `123+234`, the exterior roots are `12,13,24,34`; pair them as

\[
12\mathbin{-}24,\qquad13\mathbin{-}34
\]

to obtain `124+134` with central root `14`.

For `125+245`, the exterior roots are `12,15,24,45`; pair them as

\[
12\mathbin{-}24,\qquad15\mathbin{-}45
\]

to obtain `124+145`, again with central root `14`.

The unused opposite pairing is co-root-valued and is not traversed.  Every
endpoint and every intermediate source state in the macro is root-valued.
The total change is

\[
\Delta\Xi=-2.
\]

Hence each equal bad face gives route/parent/category absorption or a strict
same-order locked descent.  No quadruple-equality insertion, co-root track,
`2--0` cancellation or lower-order call occurs.

---

## 6. Bad-free route contradiction

Assume an oriented `H_14` full-channel lock contains no type in `mathcal B`.
Follow one of the physical `H_14` paths beginning at a marked boundary root
`12`.

A triangle containing root `12` is one of

\[
123,124,125.
\]

The bad types are absent, so the first vertex is `124`.  Its other `H_14` root
is `24`.  A triangle containing `24` is one of

\[
124,234,245.
\]

Again the bad types are absent, so the next vertex is `124`.  Induction shows
that the entire component alternates roots `12,24` through vertices of type
`124`.  It can never meet a marked boundary root `34`.

But an oriented DDD full-channel lock requires the chosen channel path to join
one `12` occurrence to one `34` occurrence in the prescribed route.  This is
a contradiction.  Therefore every nonterminal lock contains a bad vertex.

---

## 7. Well-founded fixed-channel escape

At a complete oriented lock:

1. choose a bad vertex by Section 6;
2. if its selected neighbour is distinct, use Section 4;
3. if equal, use Section 5.

Every nonabsorbing macro returns a complete prime oriented lock and lowers the
nonnegative integer `Xi` by exactly two.  Therefore only finitely many strict
macros occur.  Quantitatively, at most `|V(G)|` strict macros are possible.
The terminal result is exactly one of:

- a separating rescue channel followed by the literal prescribed-parent NNI;
- a cap-compatible `K_i` state;
- a named cyclic `2/3/4`-cut or bounded terminal;
- a root flow on the literal prescribed-parent topology.

A terminal-free SCC of complete co-root/DDD locks is impossible: from any state
in it the fixed-channel strategy would remain inside the SCC while strictly
lowering `Xi` until no nonnegative value remained.

---

## 8. Independent finite checks

The finite arithmetic was independently recomputed.

1. `tau_14` has exactly the seven triangle orbits listed in Section 3 and `xi`
   is invariant on all ten types.
2. The six distinct-neighbour rows of Section 4 are exhaustive; each has one
   root-valued opposite pairing and `Delta Xi=-2`.
3. In the four equal cases, after switching one local passage:
   - `123+234` has one root opposite pairing with central `14` and one co-root
     opposite pairing;
   - `125+245` has the same dichotomy.
   No additional local type occurs.

The RL-provided SHA-256 digest is a reproducibility label for its chosen JSON
serialization.  The proof here depends on the displayed tables, not on an
unspecified JSON field naming convention.

---

## 9. Exact status boundary

Closed at PDL reconstruction level in this dossier:

- uniqueness and common-marked transport of the fixed `H_14` frame;
- complete physical-component `Xi` invariance;
- all six strict rows;
- all four equal-neighbour root-only macros;
- absence of zero overlap in those macros;
- bad-free route contradiction;
- finite co-root/DDD all-index SCC escape;
- literal preservation of the parent, cap objects, exterior darts and prefix
  identity subject to the exact category/route consumers.

Not closed here:

- a prescribed-parent failure whose forced parent value is zero rather than a
  co-root;
- the complete v7.3 end-to-end induction;
- independent adversarial audit or an established five-CDC theorem.
