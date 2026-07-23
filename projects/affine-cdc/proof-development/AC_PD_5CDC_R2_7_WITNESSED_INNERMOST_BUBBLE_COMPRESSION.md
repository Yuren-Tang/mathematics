# AC-PD-5CDC R2.7 — witnessed innermost-bubble compression

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Programme:** compressed five-support proof, global-return unit `R2.7`  
**Classification:** `COMPLETE-DRAFT / GENERATOR LIFT AND CONCATENATION CLOSED / UNCONDITIONAL FOC REQUIRES HISTORY-WITNESS AUDIT`.

This dossier consumes the corrected Research Lead frontier after
`VARIABLE_ORDER_PERIODIC_EPISODE_COMPRESSION_GAP_V1.md` and separates two
statements which must not be conflated:

1. an explicit lower-order move history can be lifted through one raw
   equal-face insertion at predecessor order;
2. two arbitrary lower-order root flows need not be joined by such a history.

The first statement is proved here.  The second is neither assumed nor needed
provided the recursive theorem is strengthened to return a finite move witness
from the inherited child flow.

---

## 1. Raw insertion

Let `H` be a cubic child context carrying a root-valued `E_5` flow `lambda`.
Let two ordered distinguished edge lineages carry roots

\[
p,q\in R_5.
\]

Split the two edges, insert two cubic vertices, and join them by one central
edge of value

\[
x=p+q.
\]

Call the resulting predecessor-order assignment

\[
I(H,\lambda;p,q).
\]

It is an `E_5` flow.  Every noncentral edge is a root and the central edge is:

\[
\begin{array}{c|c}
\text{relation of }p,q&x\\
\hline
p=q&0,\\
p\sim q&\text{root},\\
p\perp q&\text{co-root}.
\end{array}
\]

Thus a raw insertion has at most one non-root edge.

For an actual forward equal-face cancellation, the inherited reconnecting
roots are distinct intersecting; hence the raw insertion of the inherited
child state is literally the original root-valued parent state.

---

## 2. Fixed-order child histories

A **witnessed innermost child history** is a finite sequence

\[
(H_0,\lambda_0;p_0,q_0)
\longrightarrow\cdots\longrightarrow
(H_m,\lambda_m;p_m,q_m)
\]

at one fixed child order, with complete ordered-incidence, support, cap, route
and side data retained, in which every nonexit step is one of:

1. a support-pair component switch;
2. a root-valued labelled `2--2` Pachner NNI;
3. an identity or deterministic bookkeeping step.

The two marked lineages are transported through a root NNI by ordered
incidences; if a marked edge is the active diagonal it continues as the
opposite diagonal.

There is no `2--0/0--2` pair inside an innermost child history.  If an accepted
route, bounded, separator or category exit occurs, the enclosing proof branch
terminates and no bubble compression is required.

---

## 3. Support-switch lift

Fix a support-pair direction `h` and one lower channel component `Z`.  Let

\[
\delta_p=1_{p\in Z},\qquad \delta_q=1_{q\in Z}.
\]

On the expanded source retain the lifted copy of `Z`, both half-edges of each
selected marked edge, and the inserted central edge precisely when

\[
\delta_p\oplus\delta_q=1.
\]

At each inserted vertex the selected degree is

\[
\delta_p+\delta_q+(\delta_p\oplus\delta_q),
\]

which is even.  Adding `h` on this lifted even edge set preserves every flow
equation and changes the central value to

\[
\begin{aligned}
x'
&=p+q+(\delta_p\oplus\delta_q)h\\
&=(p+\delta_p h)+(q+\delta_q h).
\end{aligned}
\]

Hence the output is exactly the raw insertion of the switched child flow.
Every noncentral edge remains a root and the central edge remains the unique
possible atom.

### Theorem 3.1 — universal switch functoriality

Every lower support-pair component switch lifts at predecessor order between
the corresponding raw insertions, for all `A/B/C` marked relations, with at
most one non-root central edge.

This is an even-correction cell when the central value is singular and an
ordinary circuit-switch history when all selected values are root-channel
eligible.

---

## 4. Root-`2--2` generator lift

Let one lower root flip have old and new diagonal roots

\[
p=A+B=C+D,
\qquad
p'=A+C=B+D.
\]

Then `p,p'` are disjoint roots.  We classify the position of the two insertion
lineages relative to the active diagonal.

### 4.1 Neither marked edge is the active diagonal

Perform the same root NNI on the expanded graph.  A marked exterior branch is
represented by the corresponding split half-edge with the same root, so the
four-root flip calculation is unchanged.  The inserted central value is
untouched.

Thus the move strictly commutes with raw insertion, even when a marked edge is
one exterior branch of the flip.  Any loop, parallel or low-port incidence
identification is an accepted bounded/category branch.

### 4.2 One marked edge is active; the other is disjoint from the flip support

Write the second marked root as `q`.  The ten possibilities split exactly into:

1. `q=p` or `q=p'`;
2. four roots intersecting both `p,p'`;
3. two roots intersecting `p` and disjoint from `p'`;
4. two roots disjoint from `p` and intersecting `p'`.

The corresponding predecessor-order movies are:

- common-neighbour case: a root-valued movie of length five or six;
- old-`B`/new-`C` case: a five-move movie with defect sequence
  \[
  0,0,0,0,1,1;
  \]
- reverse `C`/`B` case: the reverse movie;
- `q=p` or `q=p'`: the equal/opposite five-move movie with defect sequence
  \[
  1,1,1,0,1,1.
  \]

These four classes exhaust `R_5`.  Every intermediate state has at most one
zero/co-root edge.

### 4.3 One marked edge is active; the other is an exterior branch

If the second mark is, say, the branch `A`, then

\[
p+A=B,
\qquad
p'+A=C.
\]

Both endpoint pairs are automatically distinct intersecting.  The expanded
before and after sources are joined by the explicit three-NNI
triangle--square--square--triangle movie.  Every intermediate edge is a root.

### Theorem 4.1 — complete ordinary root-flip lift

Every ordinary root-valued lower `2--2` step has a finite predecessor-order
lift between the corresponding raw inserted states, fixing the complete
exterior incidence data and carrying at most one atom.  The only excluded
incidence coincidences are precisely the already accepted bounded, triangle,
small-cut or category cases.

---

## 5. Concatenation

For every child generator edge, Sections 3--4 produce a path whose initial and
final states are exactly

\[
I(H_i,\lambda_i;p_i,q_i)
\quad\text{and}\quad
I(H_{i+1},\lambda_{i+1};p_{i+1},q_{i+1}).
\]

Therefore consecutive local lifts have literally identical complete endpoint
states.  Concatenating them gives a finite predecessor-order history

\[
I(H_0,\lambda_0;p_0,q_0)
\rightsquigarrow
I(H_m,\lambda_m;p_m,q_m)
\]

with:

- the same complete exterior incidences;
- the transported ordered marked lineages;
- the lower support/cap/route changes reproduced exactly;
- at most one non-root edge in every state;
- no change of graph order.

The singular locus may enter and leave the path more than once, but it is
finite and never branches into two simultaneous persistent atoms.  No new
coefficient alphabet appears.

### Theorem 5.1 — witnessed fixed-order lift

Every witnessed innermost child history generated by root NNIs and
support-pair component switches admits a boundary-faithful predecessor-order
lift with at most one atom at every time.

---

## 6. Endpoint normalization

At the returned child state, append the exact inverse-cancellation endpoint
macro.

### `B` endpoint

If `p_m,q_m` are distinct intersecting, the raw insertion is already the
original root-valued inverse insertion.

### `A` endpoint

If `p_m=q_m`, borrow one adjacent root triangle.  The direct alternative
insertion theorem replaces the raw zero insertion by a root-valued
predecessor-order insertion on the same five exterior incidences.

### `C` endpoint

If `p_m\perp q_m`, the borrowing dichotomy gives:

- a good case with one direct root-valued alternative insertion;
- the unique missing-index case, producing one standard
  `(Q_i,Q_j,ij)` transport unit and, after local normalization, at most one
  co-root atom.

All ordinary outputs are connected, loopless and bridgeless because they are
connected root-valued local replacements; bounded identifications remain
accepted exits.

### Corollary 6.1 — one witnessed bubble

A forward equal-face cancellation, followed by one witnessed innermost child
history and its returned insertion, can be replaced by a finite
predecessor-order history with the same complete outer data and at most one
atom per state.

---

## 7. Induction on cancellation pairs

Let a finite variable-order history be equipped with explicit matching of each
forward `2--0` cancellation to its returned `0--2` original/alternative
insertion.  Ordered incidence genealogy makes the order changes properly
nested.

Choose an innermost matched pair.  Its interior has fixed child order.  If its
interior is a witnessed generator history, Corollary 6.1 replaces the complete
bubble by a predecessor-order history and removes one matched order-changing
pair.

Iterating on the finite number of matched pairs yields a fixed-order lifted
history.

### Theorem 7.1 — witnessed variable-order compression

Assume every innermost child segment is supplied as an explicit finite history
in the generator alphabet of Section 2, with complete context and ordered-mark
witnesses.  Then every finite properly nested continuation episode admits a
boundary-preserving fixed-order compression.  No arbitrary comparison between
unrelated child history lengths is required.

This is the constructive content needed by the fixed-order episode-compression
hypothesis, subject to the consumer checks in Section 9.

---

## 8. The required strengthened recursive statement

The remaining distinction is:

\[
\text{existence of a terminal child flow}
\quad\ne\quad
\text{a witnessed history from the inherited child flow}.
\]

The correct recursive proposition should be strengthened to:

> For every admissible contextual instance and every inherited starting root
> flow, there exists either an accepted exit or a finite decorated history,
> generated by the declared root NNI, support-switch and equal-face moves,
> reaching a cap-compatible terminal.

This strengthening is structurally conservative if every proof branch already
selects a concrete current-flow move and every recursive call is made on the
inherited cancellation output.  The recursive witness returned by the smaller
instance is then part of the induction data, not an arbitrary recolouring.

A bare induction hypothesis asserting only that the smaller graph possesses
some root flow is insufficient and must not be used here.

---

## 9. Exact remaining assurance interfaces

### `AC-PD-5CDC-HW1` — history-witness audit

Check every invocation of the lower-order theorem in the controlling R2 route.
It must:

1. start from the inherited post-cancellation root flow;
2. return an explicit finite move history, not only a terminal flow;
3. use no opaque terminal recolouring primitive;
4. expose every route, bounded or separator outcome as an exit.

### `AC-PD-5CDC-HW2` — complete genealogy gluing

Verify that concatenation retains all ancestor ordered incidences, cap blocks,
route sheets and side attachments.  Passive marks transport canonically
through root NNIs; a mark-consuming cancellation must be represented by the
already established ordered-incidence frame rule, not silently recreated.

### `AC-PD-5CDC-HW3` — fixed-order consumer alphabet

Verify that the fixed-order no-sink/track theorem accepts:

- root NNI paths;
- lifted support-switch even corrections;
- the bounded one-atom movies;
- endpoint alternative-insertion macros.

If its stated Ptolemy cylinder permits only pure `2--2` cells, either enlarge
its legal fixed-order history alphabet or refine each horizontal correction
into the already calibrated switch/first-exit cells.

---

## 10. Supersession and trust boundary

### Closed here

- raw insertion as a one-atom functor;
- universal support-switch lift;
- complete ten-root active-diagonal flip table;
- adjacent-mark root lift;
- strict lift when the active edge is unmarked;
- concatenation of local lifts;
- endpoint normalization;
- compression of a witnessed innermost bubble;
- induction on the number of witnessed matched cancellation pairs.

### Not closed here

- the history-witness audit `HW1`;
- full ancestor-mark/cap gluing `HW2`;
- compatibility with the exact fixed-order consumer alphabet `HW3`;
- unconditional fixed-order episode compression;
- R2.7, cap restoration or the global five-support theorem;
- independent audit, Lean verification, curation, manuscript integration,
  release, arXiv, DOI, peer review or publication.

### Current classification

\[
\boxed{
\text{WITNESSED BUBBLE COMPRESSION CLOSED}
\;/\;
\text{UNCONDITIONAL FOC AWAITS HW1--HW3}.
}
