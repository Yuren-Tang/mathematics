# An identity-hexagon cancellation can minimise dangerous return channels

## Research Lead adaptive-weld dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `3ee4925d6dba5f230c2106c4197839f89311d1e2`.

**Parents:**

- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `WELD_B_ORBIT_SWITCH_AND_MOBILE_MARK_GRAPH_V1.md`;
- `WELD_RELATION_FIRST_EXIT_V1.md`.

**Status:** exact finite choice theorem. One Petersen identity-hexagon has six canonical equal-face dipoles, but only three coefficient-distinct weld pairs: the three unordered pairs of one root triangle, each repeated twice. Relative to any outer equality or DDD rescue alphabet, one may choose the cancellation cell so that the weld has a minimal dangerous-channel intersection. For equality the minimum is at most two; for DDD it is at most one. The extremal support orbits are explicit. Thus a future inherited-flow return theorem need only handle at most two dangerous equality channels or one dangerous DDD channel after adaptive cancellation choice.

---

## 1. Three available weld pairs

Let the repeated side-root word of one identity `C6` be

\[
(a,b,c,a,b,c),
\qquad
 a+b+c=0.
\]

The six canonical star cells expose weld pairs

\[
(a,b),
(b,c),
(c,a),
(a,b),
(b,c),
(c,a).
\]

Thus there are exactly three coefficient-distinct choices:

\[
\boxed{
W_{ab}=\{a,b\},
\quad
W_{bc}=\{b,c\},
\quad
W_{ca}=\{c,a\}.
}
\]

Every pair is weld-admissible because the three roots form one root triangle.

Write the support triangle as

\[
S=\{1,2,3\},
\]

so, after support permutation,

\[
\{a,b,c\}=\{12,13,23\}.
\]

---

## 2. Dangerous channels of one weld pair

For a weld pair

\[
p=ij,
\qquad
q=ik
\]

with common support `i`, let `{l,m}` be the remaining two support indices. The channels eligible on both weld edges are exactly

\[
\boxed{
D(p,q)=\{jk,il,im\}.
}
\]

Only these channels can destroy the `B` relation by a one-sided switch. Every other support-pair switch affects at most one eligible weld root and preserves `B`.

Each weld pair therefore has exactly three dangerous channels.

---

## 3. Equality rescue alphabet

Let the outer equality pair have common root `t`. Its six rescue channels are

\[
E(t)=\{h\in R_5:h\ne t,\ |h\cap t|=1\}.
\]

For the three available weld choices, define

\[
d_W(t)=|D(W)\cap E(t)|.
\]

### Theorem 3.1 — equality overlap vectors

After sorting the three values

\[
\bigl(d_{W_{ab}}(t),d_{W_{bc}}(t),d_{W_{ca}}(t)\bigr),
\]

exactly one of the following occurs:

\[
\boxed{
(0,3,3),
\qquad
(1,2,2),
\qquad
(2,2,2).
}
\]

The support interpretation is:

1. **`t` is one edge of the side triangle `S`:**
   \[
   (0,3,3).
   \]
   Choose the weld formed by the other two side roots; it has no dangerous equality channel.

2. **`t` has one support in `S` and one support outside `S`:**
   \[
   (1,2,2).
   \]
   One weld choice has exactly one dangerous channel.

3. **`t` is the complementary root on the two supports outside `S`:**
   \[
   (2,2,2).
   \]
   Every weld choice has exactly two dangerous channels.

### Exact census

Across the ten side triangles and ten possible equality roots:

\[
\boxed{
\begin{array}{c|c}
\min_W d_W(t)&\text{number of cases}\\
\hline
0&30\\
1&60\\
2&10.
\end{array}}
\]

Consequently:

\[
\boxed{
\text{an equality return always has at least four safe rescue channels.}
}
\]

In the extremal `(2,2,2)` orbit it has exactly four safe and two dangerous channels for every weld choice.

---

## 4. DDD rescue alphabet

Let the outer DDD pair be two disjoint roots

\[
x\perp y.
\]

Its four rescue channels are the four cross roots

\[
C(x,y)=\{h:|h\cap x|=|h\cap y|=1\}.
\]

For one weld choice `W`, put

\[
d_W(x,y)=|D(W)\cap C(x,y)|.
\]

### Theorem 4.1 — DDD overlap vectors

After sorting the three weld values, exactly one of:

\[
\boxed{
(0,2,2),
\qquad
(1,1,1)
}
\]

occurs.

For the standard side support triangle `S={1,2,3}`:

1. **easy orbit `(0,2,2)`:** at least one of the DDD roots uses zero or two supports of `S`, or their four-support matching otherwise contains a root entirely inside `S`;
2. **extremal orbit `(1,1,1)`:** both DDD roots are cross roots from `S` to its two-point complement, and they use distinct endpoints on both sides. A representative is
   \[
   14\perp25.
   \]

### Exact census

Across the ten side triangles and fifteen DDD pairs:

\[
\boxed{
\begin{array}{c|c}
\min_W d_W(x,y)&\text{number of cases}\\
\hline
0&90\\
1&60.
\end{array}}
\]

Hence:

\[
\boxed{
\text{a DDD return always has at least three safe rescue channels.}
}
\]

Even in the extremal orbit every weld choice has only one dangerous channel.

---

## 5. Adaptive cancellation rule

At a recurrent `C6` core, do not choose an arbitrary canonical star cell for cancellation. Given the current outer equality or DDD return alphabet:

1. compute the dangerous-channel count of the three coefficient-distinct weld pairs;
2. choose a cell realizing a minimum pair;
3. retain the antipodal duplicate as a second source-location option when incidence or category considerations distinguish the two occurrences.

### Corollary 5.1 — reduced inherited-flow frontier

After adaptive choice, the only potentially weld-destroying separated channels are:

\[
\boxed{
\le2\text{ in the equality branch},
\qquad
\le1\text{ in the DDD branch}.
}
\]

All other horizontal rescue channels preserve the weld `B` relation coefficient-wise, regardless of whether their switched component contains zero or one marked weld edge.

---

## 6. Extremal equality normal form

The unique equality orbit with unavoidable minimum two is:

\[
\{a,b,c\}=\{12,13,23\},
\qquad
 t=45.
\]

For the weld

\[
W=\{12,13\},
\]

its dangerous channels are

\[
\boxed{14,15,}
\]

while the four safe equality channels are

\[
\boxed{24,25,34,35.}
\]

The safe set is one `K_(2,2)` square between supports `{2,3}` and `{4,5}`. The two dangerous channels are the two spokes from the weld-common support `1` to the outer equality supports `{4,5}`.

This is the sole equality support geometry which must be treated without a zero- or one-dangerous weld choice.

---

## 7. Extremal DDD normal form

Take

\[
\{a,b,c\}=\{12,13,23\},
\qquad
 x=14,
\qquad
 y=25.
\]

The three weld choices each meet the DDD cross-channel square in exactly one dangerous channel. Thus cancellation location cannot eliminate danger entirely, but it localises it to one known support pair.

The antipodal duplicate of the chosen weld remains available for source-incidence optimisation.

---

## 8. Exact next theorem

### Target 8.1 — safe-channel lock versus dangerous separation

After adaptive weld choice, suppose every safe outer rescue channel keeps the outer marked pair in one component, while one dangerous channel separates it and conflicts with weld preservation.

Prove one of:

1. the safe-channel lock forces route/profile escape by disjoint-support route invariance;
2. the dangerous separation is one bounded two-boundary exchange kernel;
3. the antipodal occurrence of the same weld avoids the source conflict;
4. the exchange transfers one singular atom to a strictly shorter causal frame.

Only the extremal equality and DDD support normal forms of Sections 6--7 require a genuinely new argument.

---

## 9. Trust boundary

### Exact here

- the three available coefficient-distinct weld choices in one `C6`;
- the three dangerous channels of each weld pair;
- complete equality overlap-vector classification and census;
- complete DDD overlap-vector classification and census;
- equality minimum at most two;
- DDD minimum at most one;
- exact extremal support normal forms;
- the adaptive cancellation rule.

### Not proved

- safe-channel lock elimination;
- source-level superiority of one antipodal weld occurrence;
- the two-boundary exchange-kernel theorem;
- inherited-flow relative return or cancellation macro-return;
- R2 global return, cap restoration, or global five-support closure;
- independent audit, curation, Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.
