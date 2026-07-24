# Universal zero-parent escape by an `S_3`-switch-invariant rank

## Research Lead theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-03`  
**Frozen start:** `research/affine-cdc-five-cdc-v1@212d789a5967813e7277fb3e269060926c99cb0e`  
**PDL obstruction consumed:** `proof-development/affine-cdc-rigour-v1@fee97446ee8b99f07740f394e99ef4a2ecc3e40e`  
**Classification:** `COMPLETE AUTHORIAL UNIVERSAL THEOREM / PDL RECONSTRUCTION REQUIRED`.

This theorem closes the zero prescribed-parent row isolated by PDL.  It uses no
`2--0` cancellation, no lower-order call, no other-parent substitution, no
track erasure, no finiteness/SCC distance and none of `Q_N`, `M_N`, `d_N`,
nested bubbles or terminal frames.

The fixed-channel idea admits a stronger equality analogue than was requested:
one rank is invariant under the entire support-permutation group on the common
support and the two unused supports.  Thus equal rows may choose either physical
rescue channel without restarting or comparing different ranks.

---

## 1. Exact zero-parent state

Let `x,y,s,u,v` be the five support indices, all distinct.  Put

\[
a=xs,\qquad b=ys,\qquad r=a+b=xy.
\]

The ordered active word is

\[
(A,B,C,D)=(a,a,b,b),
\]

with current crossed central root `r` and prescribed parent

\[
P=AB\mid CD
\]

of central value zero.  The two active source vertices both have support
triangle

\[
\{x,y,s\}.
\]

In canonical notation this is

\[
(x,y,s,u,v)=(1,2,3,4,5),
\qquad
(A,B,C,D)=(13,13,23,23),
\qquad r=12.
\]

A complete state retains the tuple of
`PURE_NNI_PRESCRIBED_PARENT_STATE_INTERFACE_NORMAL_FORM_V1.md`: labelled graph,
ordered darts, root assignment, crossed sheet, literal parent `P`, cap block,
route/profile field, support-component attachments, terminal/category flag and
prefix identity `alpha`.

The two physical rescue channels are

\[
h_u=su,\qquad h_v=sv.
\]

For either channel, all four active exterior roots lie in `H_h`, while the
current central root `xy` does not.

### Immediate separating-channel repair

On either crossed sheet, if one `H_h` component contains exactly one occurrence
of `a` and one occurrence of `b`, switch that complete component.  Exactly one
root in each equal parent pair is translated by `h`, so

\[
(a+h)+a=h,
\qquad
(b+h)+b=h.
\]

The literal parent NNI is then root-valued with central root `h`.

A route/profile change, cyclic `2/3/4` cut or bounded category output is consumed
immediately by its named existing consumer.  The remainder of the proof treats
the common full-channel branch.

---

## 2. The intrinsic four-orbit alphabet

The ordered equal pairs distinguish `x` from `y`.  The remaining support set is

\[
U=\{s,u,v\}=[5]\setminus\{x,y\}.
\]

No ordering of `U` is required.  The ten support triangles split into four
orbits under the full permutation group `Sym(U)`:

\[
\begin{aligned}
\mathcal X&=\{xyi:i\in U\},\\
\mathcal Y&=\{xij:i,j\in U,\ i\ne j\},\\
\mathcal Z&=\{yij:i,j\in U,\ i\ne j\},\\
\mathcal S&=\{suv\}.
\end{aligned}
\]

In canonical coordinates:

\[
\begin{aligned}
\mathcal X&=\{123,124,125\},\\
\mathcal Y&=\{134,135,145\},\\
\mathcal Z&=\{234,235,245\},\\
\mathcal S&=\{345\}.
\end{aligned}
\]

Define vertex weights

\[
e(T)=
\begin{cases}
2,&T\in\mathcal X,\\
1,&T\in\mathcal Y\cup\mathcal Z,\\
0,&T\in\mathcal S,
\end{cases}
\qquad
q(T)=
\begin{cases}
1,&T\in\mathcal Y,\\
0,&\text{otherwise}.
\end{cases}
\]

Let the two active parent vertices be omitted from the sum and put

\[
E(S)=\sum_{w\notin\{p_0,p_1\}}e(\Delta_w),
\qquad
Q(S)=\sum_{w\notin\{p_0,p_1\}}q(\Delta_w).
\]

For graph order `N`, define the single nonnegative integer

\[
\boxed{
\mathcal R(S)=(N-1)E(S)+Q(S).}
\]

Since there are `N-2` exterior vertices,

\[
0\le \mathcal R(S)\le (N-2)(2N-1).
\]

### Lemma 2.1 — support-switch invariance

Both `e` and `q` are invariant under every permutation of `U`.  In particular
they are invariant under the support transpositions induced by switches of
`H_{su}`, `H_{sv}` and `H_{uv}`.

- If a switched component contains no active marked occurrence, only vertices on
  that component are acted on, and every summand is unchanged.
- If a nonabsorbing switched rescue component contains all active marked
  occurrences, the physical common support changes from `s` to `u` or `v`.
  The ordered differing supports `x,y` and the unordered set `U` are unchanged,
  so the same four orbit classes still define the rank.  Equivalently, transport
  the support frame by the same transposition; vertices on the component are
  acted on twice and exterior vertices off it once, but `e,q` are invariant.
- If the component contains a mixed proper set of active occurrences, it is the
  separating parent-repair branch already consumed above.

Therefore every nonexit complete component switch used below preserves
`mathcal R` over the entire closed graph, including cap and exterior vertices.

This is the equality counterpart of complete-component `Xi` invariance, but it
does not reuse or reopen the co-root `Xi` theorem.

---

## 3. The twelve strict distinct-neighbour rows

The finite root-NNI table needed by the deterministic strategy is:

\[
\begin{array}{c|c|c|c|c}
\text{central root}&\text{source}&\text{target}&\Delta E&\Delta Q\\
\hline
12&123+124&134+234&-2&+1\\
12&123+125&135+235&-2&+1\\
12&124+125&145+245&-2&+1\\
\hline
13&123+134&124+234&0&-1\\
13&123+135&125+235&0&-1\\
13&134+135&145+345&-1&-1\\
\hline
14&124+134&123+234&0&-1\\
14&124+145&125+245&0&-1\\
14&134+145&135+345&-1&-1\\
\hline
15&125+135&123+235&0&-1\\
15&125+145&124+245&0&-1\\
15&135+145&134+345&-1&-1.
\end{array}
\]

Each target is the unique root-valued opposite pairing in its four-support
tetrahedron; the third pairing is the corresponding co-root.

Orbit-theoretically there are only three row types:

\[
\mathcal X+\mathcal X\longrightarrow\mathcal Y+\mathcal Z,
\]

which lowers `E` by two;

\[
\mathcal X+\mathcal Y\longrightarrow\mathcal X+\mathcal Z,
\]

which preserves `E` and lowers `Q` by one; and

\[
\mathcal Y+\mathcal Y\longrightarrow\mathcal Y+\mathcal S,
\]

which lowers `E` and `Q` by one.

Consequently every displayed row strictly lowers `mathcal R`.  In the first
row type

\[
\Delta\mathcal R=-2(N-1)+1<0;
\]

in the second it is `-1`, and in the third it is `-N`.

### Source fields

Every strict NNI below is performed on one labelled exterior edge.  It keeps the
active central edge and all four active darts fixed.  It preserves graph order,
all coefficients outside its two-vertex cell, the literal parent topology and
the active prefix identity.  If an off-edge dart is moved, its physical edge
identity and exterior dart survive and `alpha` is updated explicitly.

The cap vertices and cap darts remain the same labelled objects.  The affected
support components, route/profile field and graph category are recomputed.  The
result is exactly one of:

1. separating rescue and literal parent repair;
2. cap-compatible route/profile output;
3. named cyclic `2/3/4` cut or bounded terminal;
4. another complete prime zero-parent state with smaller `mathcal R`.

---

## 4. Root-only replacement of every selected equal row

The deterministic strategy below encounters only equal faces of orbit type
`mathcal X` or `mathcal Y`, and always on a root fixed by a rescue
transposition.

### 4.1 Equal `mathcal X` face

Let the equal type be

\[
T=xyk\in\mathcal X,
\]

on central root `xy`.  Choose a physical rescue transposition as follows:

- if `k=s`, choose either `h=su` or `h=sv`;
- if `k=u` or `v`, choose `h=sk`.

The transposition fixes `xy` and sends `T` to a distinct member `T'` of
`mathcal X`.  The two off-edge roots of the equal face are exactly the two local
`H_h` darts.

### 4.2 Equal `mathcal Y` face

The only anchored types required later are

\[
T=xsu\quad\text{or}\quad xsv.
\]

Select central root `xu` or `xv`, respectively, and use the other rescue
channel:

\[
xsu\xrightarrow{\tau_{sv}}xuv,
\qquad
xsv\xrightarrow{\tau_{su}}xuv.
\]

More generally, for `T=xij` select a root `xi` so that the transposition of the
other support `j` with the third member of `U` involves the current common
support.  Again the central root is fixed and the two off-edge roots are the
local rescue-channel passage.

### 4.3 The complete equal-face macro

Suppress the selected rescue-channel system outside the equal face to its
matching on the four local ports.

- If that matching equals one of the two root placements, zero or one
  root-valued branch-swap reaches a split placement with the two local passages
  in distinct complete components.
- If it is the third matching, the branch-swap changes the marked rescue route,
  because the selected local passage contains the anchored active `xs` dart.
  This is an exact route/profile output.

In the split case switch the complete component containing the anchored local
passage.

- A mixed marked component rootifies the literal parent.
- A route/category event is consumed.
- Otherwise the switch is unmarked or common-marked, preserves `mathcal R` by
  Lemma 2.1, and changes exactly one of the two local orbit representatives
  relative to the other.

The local pair is now distinct in the same orbit.  Perform the corresponding
strict NNI of Section 3:

\[
\mathcal X+\mathcal X\to\mathcal Y+\mathcal Z
\]

or

\[
\mathcal Y+\mathcal Y\to\mathcal Y+\mathcal S.
\]

Thus every selected equal face gives parent/route/category absorption or a
strict same-order decrease.  Every state and intermediate source topology is
root-valued.  No zero insertion, co-root track, cancellation or lower-order
call occurs.

---

## 5. Deterministic anchored descent

Choose one physical active dart of root `a=xs`; in canonical coordinates take

\[
A:13.
\]

Let `w` be its exterior endpoint.  The root on `A` never changes under the
strict exterior NNIs; under a common rescue switch the same physical dart is
transported to `xu` or `xv` and remains the distinguished `x`-side active dart.

The triangle at `w` contains `x` and the current common support.  Therefore it
is exactly one of:

\[
\mathcal X\quad\text{or}\quad\mathcal Y.
\]

In canonical coordinates the three possibilities are `123,134,135`.

### Case X

If `w` has type `123`, select its `12` edge.  This edge is not the active
central edge: each active vertex already uses its unique `12` incidence on the
edge joining the two active vertices.  The other endpoint is another
`mathcal X` triangle.

- Distinct neighbour: use an `XX -> YZ` row.
- Equal neighbour: use the equal-`mathcal X` macro.

### Case Y

If `w` has type `134`, select its `14` edge.  If it has type `135`, select its
`15` edge.  In intrinsic notation, for `w=xst` select `xt`, the `x`-root not
carried by the active dart `xs`.

The other endpoint is in `mathcal X` or `mathcal Y`.

- `X/Y` distinct neighbour: use an `XY -> XZ` row.
- `Y/Y` distinct neighbour: use a `YY -> YS` row.
- Equal neighbour: use the equal-`mathcal Y` macro with the other rescue
  channel.

The selected edge is never the active central edge and never one of the four
active exterior darts.  An NNI may move the exterior endpoint of `A`, but the
edge identity, root and active dart of `A` survive.  Following the same physical
`A` dart therefore supplies the next anchored vertex.

### Exhaustiveness

There is no bad-free branch: every nonterminal zero-parent state has the
physical active `x`-side dart `A`, and its exterior endpoint is necessarily in
`mathcal X` or `mathcal Y`.  Sections 3--4 exhaust every possible neighbour at
the selected nonactive root.

Hence every nonabsorbing anchored macro strictly lowers the nonnegative integer
`mathcal R`.

---

## 6. Universal theorem

### Theorem `FC-PURE-NNI-ZERO-PARENT-ESCAPE`

Every complete category-safe fixed-order state with ordered zero-parent word

\[
(a,a,b,b),
\qquad a\ne b,
\qquad a\cap b\ne\varnothing,
\]

and two root-valued crossed topologies has a finite source-faithful same-order
history, using only ordinary root NNIs, root-valued equal-face branch swaps,
legal complete support-component switches and exact terminal consumers, ending
in exactly one of:

1. a root flow on the literal prescribed-parent topology;
2. a cap-compatible route/profile state;
3. a named cyclic `2/3/4`-cut or bounded terminal.

### Proof

Normalize to `(13,13,23,23)` and run the separating-channel tests.  On the
remaining common-lock branch apply the deterministic anchored macro of Section
5.  Every nonabsorbing execution preserves the complete zero-parent interface
and strictly lowers `mathcal R`.  Since

\[
0\le\mathcal R\le(N-2)(2N-1),
\]

a terminal-free infinite or recurrent execution is impossible.  The only
possible finite stopping events are the three displayed theorem outputs. ∎

A crude bound is at most `(N-2)(2N-1)` strict macros; no optimal bound is
claimed.

---

## 7. Effect on the inverse-parent table

At Research Lead authorial level the fixed-order inverse root-NNI table is now:

\[
\begin{array}{c|c}
\text{forced parent value}&\text{same-order disposition}\\
\hline
\text{root}&\text{literal parent NNI},\\
\text{co-root}&\text{retained PDL-reconstructed fixed-channel Xi theorem},\\
0&\text{the present }S_3\text{-invariant anchored descent}.
\end{array}
\]

Therefore the exact node

`FC-PURE-NNI-ZERO-PARENT-ESCAPE`

is closed at Research Lead authorial level, and the earlier overstatement is
repaired without altering the co-root theorem.

Conditional downstream effects, subject to independent PDL reconstruction and
audit, are:

- pure fixed-order return through every stored prefix edge;
- exhaustiveness of the inverse-parent terminal table;
- closure of the ordinary strong-induction draft;
- reactivation of the already accepted outer-shell implication.

---

## 8. Finite certificate and PDL reconstruction surface

The script

`projects/affine-cdc/research/certificates/zero_parent_heawood_and_s3_rank_v1.py`

recomputes the four orbit weights, invariance under the three transpositions of
`U`, all twelve strict rows and their `(Delta E,Delta Q)` values.

Canonical finite-certificate digest:

`d22bce5ea026f5c461575f05ed81ed6e68c71a0c3c459ce6ada93d96f458422e`.

PDL should independently reconstruct, in this order:

1. the intrinsic ordered `(x,y;U)` orbit frame;
2. complete-component invariance, including common-marked frame transport;
3. all twelve distinct rows;
4. the equal-`X` three-matching macro;
5. the equal-`Y` three-matching macro;
6. preservation of the active parent cell and dart `A` under every strict NNI;
7. cap/route/category recomputation and exact consumers;
8. integer descent and the inverse-parent-table integration;
9. ordinary-induction and terminal-census integration.

---

## 9. Assurance boundary

This is an authorial Research Lead theorem, not independent acceptance.  It does
not by itself establish an accepted universal five-support/five-CDC theorem.
No Lean theorem, Curator/canonical movement, manuscript update, release, tag,
arXiv, DOI, peer-review or publication status is changed.
