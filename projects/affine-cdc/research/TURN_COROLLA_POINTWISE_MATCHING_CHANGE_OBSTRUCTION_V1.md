# Pointwise-fixed turn corollas cannot change the alternating star matching

## Research Lead local impossibility theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `PRE_CANCELLATION_C6_MOVIE_AND_MIXED_SCC_SCOPE_CORRECTION_V1.md`;
- `R2_6_LEGAL_HISTORY_SECTION_SCOPE_CORRECTION_V1.md`.

**Status:** exact obstruction to the strongest proposed legal-history section. Let one turn corolla be a cubic vertex with two marked pivot incidences and one spoke into the local star/cross completion. Along any ordinary NNI history which fixes the corolla and both pivot incidences pointwise at every state, the endpoint of the third spoke is invariant. Consequently the even and odd alternating three-star matchings of the six identity-hexagon turn corollas cannot be connected by a root-NNI history which keeps all six turn corollas pointwise fixed.

This does not show that the naked minimal six-output carriers are root-disconnected. In fact they are root-connected once the pivot rails may deform. It shows that the later annulus claim cannot be repaired by an asynchronous matching change while retaining every resolved constant-run carrier as a pointwise fixed exterior branch.

---

## 1. One marked cubic corolla

Let `R` be a cubic source vertex with incident branches

\[
a,\quad b,\quad c.
\]

The branches `a,b` are the two pivot incidences of a resolved turn corolla. The branch `c` is its outgoing spoke into the local pivot-change completion.

A **pointwise-relative history at `R`** requires at every source state:

1. the same vertex `R`;
2. the same two incident edge germs `a,b`;
3. the same exterior rooted subgraphs on those germs;
4. the same cyclic/ordered incidence data at `R`.

The third incident edge may a priori be expected to change its remote endpoint when the alternating star matching changes.

---

## 2. Local NNI incidence lemma

An ordinary cubic NNI is supported on one internal edge

\[
uv.
\]

At the endpoint `u`, let the other two incident branches be `x,y`; at `v`, let them be `z,w`. The two alternative NNIs retain exactly one of `x,y` at `u` and exchange the other with one of `z,w`.

### Lemma 2.1 — an incident NNI moves one of the two fixed branches

If `u=R` and the active edge is the third spoke `c`, every nontrivial NNI on `Rc` changes the incidence at `R` of at least one of the two branches `a,b`.

### Proof

The two NNI alternatives partition the four exterior branches into

\[
(a,z)\mid(b,w)
\]

or

\[
(a,w)\mid(b,z)
\]

up to exchange of `a,b` and `z,w`. At `R`, one of `a,b` stays and the other is replaced by a branch from the opposite endpoint. No nontrivial alternative keeps both `a` and `b` at `R`. ∎

### Lemma 2.2 — a disjoint NNI cannot change the third neighbour

If the active edge is not incident with `R`, the complete incidence set at `R`, including the remote endpoint of its third edge, is unchanged.

This is literal locality of the NNI.

---

## 3. Third-neighbour invariance

### Theorem 3.1 — pointwise-fixed corolla invariant

Along any finite ordinary NNI history which fixes `R,a,b` pointwise at every state, the third edge incident with `R` has the same remote endpoint at every state.

### Proof

Consider one history step.

- If its support is disjoint from `R`, use Lemma 2.2.
- If its support contains `R`, the active edge must be the third edge, because `a,b` are exterior fixed branches. Lemma 2.1 says every nontrivial NNI would move one of `a,b`, forbidden.

Thus no step changes the third edge. Induct on the history length. ∎

The theorem is purely topological; root labels cannot evade it.

---

## 4. Alternating star states

For the identity hexagon, let

\[
R_0,\ldots,R_5
\]

be the six turn corollas. A canonical star in Cell `i` attaches the third spokes of

\[
R_i,\ R_{i+1}
\]

to one star centre.

The two disjoint perfect matchings of the six-cycle are

\[
M_{\rm ev}=\{01,23,45\},
\]

and

\[
M_{\rm odd}=\{12,34,50\}.
\]

In the even alternating state, the third neighbour of every `R_i` is the centre associated with its edge of `M_ev`. In the odd state it is the centre associated with the different edge of `M_odd`.

### Corollary 4.1 — no pointwise-relative alternating conversion

There is no ordinary NNI history from the even alternating star state to the odd alternating star state which fixes all six turn corollas and their two pivot incidences pointwise throughout.

### Proof

Every `R_i` changes its matched partner, hence its third spoke must change remote endpoint. This contradicts Theorem 3.1. ∎

---

## 5. Consequence for the `C6` annulus proposal

The statement

> each local cross state canonicalises to a star by an NNI fixing its turn corollas, therefore all cells can be scheduled asynchronously to produce a common global star history while every turn carrier remains fixed

is false without an additional operation.

Local pointwise-relative canonicalisation is valid inside one cell. The obstruction appears when the global matching of the six turn spokes must change between the two checkerboard parities.

Any successful global repair must permit at least one of:

1. temporary deformation of the pivot incidences/constant-run carriers;
2. a larger source move not generated by ordinary NNIs relative to the corollas;
3. a cancellation/return macro with an independently proved strict rank;
4. a separator, route change or bounded enclosure;
5. a full decorated lift showing that the required carrier deformation is source-faithful and returns all exterior data.

---

## 6. Relation to the naked minimal carrier

If the two pivot rails are included inside the mutable source region rather than fixed as exterior branches, the even and odd alternating states are not separated by this theorem. A finite root-NNI path may move pivot branches temporarily and restore them at the end.

Such a naked-carrier path does not automatically lift over arbitrary resolved constant-pivot decorations. Every NNI which uses a rail edge must be replaced by a relative movie on the full decorated carrier.

Thus the remaining target is narrower than arbitrary annulus gluing:

\[
\boxed{
\text{lift a finite naked-carrier root path over the six resolved pivot rails}.}
\]

---

## 7. Assurance boundary

### Exact here

- local incidence effect of a cubic NNI;
- invariance of the third neighbour under pointwise-fixed pivot incidences;
- impossibility of pointwise-relative even-to-odd star matching conversion;
- identification of the necessary relaxation in any R2.6 repair.

### Not claimed

- root-disconnectedness of the naked alternating carriers;
- impossibility of a decorated carrier lift;
- falsity of R2.6 or five-CDC;
- PDL completion or independent audit;
- Lean, manuscript, curation, release or publication status.
