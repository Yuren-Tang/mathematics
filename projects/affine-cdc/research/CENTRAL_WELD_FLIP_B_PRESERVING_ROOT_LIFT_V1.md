# A `B`-preserving active weld diagonal has a bounded root-valued source lift

## Research Lead innermost-bubble local theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `MARKED_WELD_PACHNER_OVERLAP_SCOPE_V1.md`;
- `WELD_RELATION_FIRST_EXIT_V1.md`;
- the four-root pairing-sum classification.

**Status:** exact source-level repair of the main active-diagonal overlap in an innermost cancellation bubble. Suppose one lower-order root `2--2` flip has old diagonal `p` and new diagonal `p'`, and one weld insertion uses the old diagonal together with a second disjoint marked edge of root `q`. If the transported pair remains weld-admissible after the flip, so `q` intersects both `p` and `p'`, then inserting before and after the lower-order flip gives two predecessor-order eight-port cubic trees joined by a root-valued NNI movie of length five or six. Thus a `B`-preserving central mark crossing admits an actual bounded source lift even though the old diagonal itself cannot be preserved pointwise.

The theorem treats the generic overlap in which the second marked edge and the active flip support have distinct endpoints. Endpoint identifications are bounded lower-port degenerations and require separate disposition.

---

## 1. Lower-order flip and second marked edge

Let the four ordered branch roots around one lower-order root flip be

\[
A,B,C,D\in R_5
\]

with old and new diagonal roots

\[
\boxed{
A+B=C+D=p,
\qquad
A+C=B+D=p'.
}
\]

Then `p,p'` are disjoint roots.

Let the second marked edge have root `q`. At its two endpoints write the other branch roots as

\[
\boxed{
E+F=q,
\qquad
G+H=q.
}
\]

Assume all eight exterior branch incidences are distinct and that

\[
\boxed{
q\sim p,
\qquad
q\sim p',
}
\]

where `x sim y` means distinct intersecting roots.

The four roots intersecting both disjoint roots `p,p'` are exactly the four exterior roots

\[
\boxed{q\in\{A,B,C,D\}.}
\]

---

## 2. Expanded before and after topologies

Insert an equal-face pair on the two marked edges `p,q` before the lower-order flip. The resulting predecessor-order eight-leaf tree has internal split system

\[
\boxed{
\Sigma_0=\{AB,CD,EF,GH,ABEF\}.
}
\]

The corresponding internal root values are

\[
p,\ p,\ q,\ q,\ p+q.
\]

All are roots.

Transport the active mark through the lower-order flip, so its root becomes `p'`, and insert on `p',q`. The expanded after topology has split system

\[
\boxed{
\Sigma_*=\{AC,BD,EF,GH,ACEF\},
}
\]

with internal roots

\[
p',\ p',\ q,\ q,\ p'+q.
\]

All are roots by the two `B` assumptions.

For a subset word such as `ABEF`, its edge value is the xor-sum of the displayed boundary roots. Complementary subsets give the same value because the total boundary sum is zero.

---

## 3. Five-move movie

Assume

\[
A+q\in R_5.
\]

Since `q` is one of `A,B,C,D`, this is exactly the orbit

\[
q\in\{B,C\}.
\]

Use the following split systems:

\[
\begin{aligned}
\Sigma_0&=\{AB,ABEF,CD,EF,GH\},\\
\Sigma_1&=\{ABEF,AEF,CD,EF,GH\},\\
\Sigma_2&=\{AEF,BCD,CD,EF,GH\},\\
\Sigma_3&=\{AEF,BCD,BD,EF,GH\},\\
\Sigma_4&=\{ACEF,AEF,BD,EF,GH\},\\
\Sigma_5&=\{AC,ACEF,BD,EF,GH\}=\Sigma_*.
\end{aligned}
\]

Consecutive systems differ in one internal split and are one ordinary NNI apart.

The nonconstant split values are:

\[
\begin{array}{c|c}
\text{split}&\text{root value}\\
\hline
ABEF&p+q\\
AEF&A+q\\
BCD&B+C+D=B+p=A\\
BD&p'\\
ACEF&p'+q\\
AC&p'.
\end{array}
\]

Together with the fixed roots `p,q` on `CD,EF,GH`, every intermediate internal edge is root-valued.

### Theorem 3.1

If `q=B` or `q=C`, the expanded before and after sources are joined by five root-valued relative NNIs fixing all eight exterior incidences.

---

## 4. Six-move movie

Assume instead

\[
C+q\in R_5.
\]

This is exactly

\[
q\in\{A,D\}.
\]

Use:

\[
\begin{aligned}
\Sigma_0&=\{AB,ABEF,CD,EF,GH\},\\
\Sigma_1&=\{AB,ABEF,CGH,EF,GH\},\\
\Sigma_2&=\{AB,ABD,CGH,EF,GH\},\\
\Sigma_3&=\{ABD,BD,CGH,EF,GH\},\\
\Sigma_4&=\{ACGH,BD,CGH,EF,GH\},\\
\Sigma_5&=\{AC,ACGH,BD,EF,GH\},\\
\Sigma_6&=\{AC,ACEF,BD,EF,GH\}=\Sigma_*.
\end{aligned}
\]

Again consecutive systems differ by one NNI split.

The nonconstant values are:

\[
\begin{array}{c|c}
\text{split}&\text{root value}\\
\hline
CGH&C+q\\
ABD&A+B+D=p+D=C\\
BD&p'\\
ACGH&A+C+q=p'+q\\
AC&p'\\
ACEF&p'+q.
\end{array}
\]

All are roots, together with the fixed `p,q` values.

### Theorem 4.1

If `q=A` or `q=D`, the expanded before and after sources are joined by six root-valued relative NNIs fixing all eight exterior incidences.

---

## 5. Complete generic central-overlap theorem

### Theorem 5.1 — `B`-preserving central lift

Let one weld edge be the active diagonal of a lower-order root-valued flip, and let the second weld edge be disjoint from that flip support. If the old pair `(p,q)` and transported pair `(p',q)` both lie in the weld-admissible `B` orbit, then the two predecessor-order inverse-weld insertions are connected by a boundary-preserving root-valued source movie of length at most six.

### Proof

The common-neighbour set of the disjoint roots `p,p'` is exactly `{A,B,C,D}`. Exactly one of the two predicates

\[
A+q\in R_5,
\qquad
C+q\in R_5
\]

holds in the relevant paired form:

- `q in {B,C}` gives the five-move movie;
- `q in {A,D}` gives the six-move movie.

Sections 3--4 verify every internal edge value. ∎

---

## 6. Finite certificate

Normalize

\[
p=12,
\qquad
p'=34.
\]

There are four ordered flip-boundary assignments `(A,B,C,D)`, four possible common-neighbour roots `q`, and six ordered root-triangle decompositions at each endpoint of the second marked edge. Thus there are

\[
4\cdot4\cdot6\cdot6=576
\]

support-labelled boundary cases.

For every case all `10,395` labelled eight-leaf cubic trees were enumerated and the root-valid induced NNI graph was computed.

The exact shortest distances from `Sigma_0` to `Sigma_*` are:

\[
\boxed{
288\text{ cases of distance }5,
\qquad
288\text{ cases of distance }6.
}
\]

The structural movies above realise those distances uniformly. The computation is a supplementary certificate; the split-value proof is controlling.

---

## 7. Interaction with bubble compression

This theorem supplies the missing source cell for a pure lower-order `2--2` step when:

- one weld lineage is the active central diagonal;
- the second marked edge is disjoint from the active support;
- the transported pair remains in `B`.

Together with strict commutation for disjoint/exterior moves, it proves predecessor-order lifting through every generic `B`-preserving root flip.

It does not yet handle:

1. the unique central move for which `(p',q)` leaves `B` and creates one co-root atom;
2. endpoint-identification degenerations when the second marked edge meets the active flip support;
3. support-pair component switches;
4. nested `2--0/0--2` bubbles.

---

## 8. Assurance boundary

### Exact here

- complete eight-port source model;
- the two universal split movies;
- root validity of every intermediate topology;
- maximum length six;
- exhaustive 576-case/10,395-topology certificate;
- source-level lifting of every generic `B`-preserving central diagonal crossing.

### Not claimed

- pointwise preservation of the old diagonal;
- the bad central `B`-exit lift;
- adjacent-mark degenerations;
- complete innermost-bubble compression;
- R2.7 closure, cap restoration or global five-support closure;
- PDL reconstruction, audit, Lean, manuscript, curation, release or publication.
