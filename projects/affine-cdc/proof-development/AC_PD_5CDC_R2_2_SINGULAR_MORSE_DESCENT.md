# AC-PD-5CDC-R2.2 — singular-carrier Morse descent

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Programme:** compressed five-support proof, extension unit `R2`  
**Classification:** `COMPLETE-DRAFT / CURRENT-FLOW TERMINATION CLOSED / RETURN ACTIVE`.

This dossier independently reconstructs the current-flow root-surgery termination theorem used by the selected-cross extension proof. It consumes the root-triangle/Pachner definitions but does not treat the RL termination summaries as accepted mathematics.

Controlling RL sources:

- `SINGULAR_CARRIER_DISCRETE_MORSE_UNIFICATION_V1.md`;
- `EQUALITY_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `ROOT_FLOW_TRIANGLE_COMPLEX_PACHNER_V1.md`.

The thirty-side finite tables were independently recomputed in Wolfram Language.

---

## 1. Root triangles and the flip involution

The ten local cubic root states are the three-subsets

\[
T\in\binom{[5]}3.
\]

At a vertex of type `T={a,b,c}`, the three incident root labels are

\[
ab,ac,bc.
\]

Two distinct local types `T,U` may be adjacent precisely when

\[
|T\cap U|=2;
\]

their common two-subset is the label on the joining edge. Write

\[
T=\{a,b,c\},
\qquad
U=\{a,b,d\}.
\]

The unique nontrivial root-valued `2--2` move replaces this side by the opposite side of the four-support tetrahedron:

\[
\{T,U\}
\longleftrightarrow
\bigl\{\{a,c,d\},\{b,c,d\}\bigr\}.
\]

There are thirty unordered adjacent distinct sides, paired into fifteen flip involutions. Equal adjacent types admit the root-preserving `2--0` equal-face cancellation.

---

## 2. Equality boundary

Normalize the equality root to `12`; all four boundary semiedges are labelled `12`.

Define

\[
\nu(T)=
\begin{cases}
3,&12\subset T,\\
0,&T=345,\\
2,&\text{otherwise},
\end{cases}
\]

and

\[
\phi(124)=1,
\qquad
\phi(125)=3,
\qquad
\phi(T)=0\text{ otherwise}.
\]

Put

\[
w_Z(T)=\nu(T)+\phi(T)+1.
\]

The table is

\[
\begin{array}{c|cccccccccc}
T&123&124&125&134&135&145&234&235&245&345\\
\hline
w_Z(T)&4&5&7&3&3&3&3&3&3&1.
\end{array}
\]

For a finite carrier `R`, let

\[
\mathcal M_Z(R)=\sum_{v\in V(R)}w_Z(\Delta_v).
\]

### Proposition 2.1 — exact equality flip census

For each of the thirty current sides, compare its `\nu`-sum with the opposite side.

The exact result is

\[
9\text{ lower }E,
\qquad
12\text{ preserve }E,
\qquad
9\text{ raise }E.
\]

On the twelve `E`-neutral sides, `\phi` gives

\[
6\text{ decreasing},
\qquad
6\text{ increasing},
\qquad
0\text{ ties}.
\]

Moreover

\[
\Delta E<0\Longrightarrow\Delta\Phi\le0.
\]

Hence the scalar weight satisfies

\[
\boxed{
15\text{ sides have }\Delta\mathcal M_Z<0,
\quad
15\text{ have }\Delta\mathcal M_Z>0,
\quad
0\text{ ties}.}
\]

This independently confirms that the coefficient of `\phi` may be one; no larger lexicographic simulation coefficient is needed.

### Proposition 2.2 — equality nondecreasing table

If the current side does not admit a strictly `\mathcal M_Z`-decreasing flip, the complete list, grouped by common root, is

\[
\begin{array}{c|l}
12&\varnothing\\
13&123-134,\ 123-135\\
14&124-145\\
15&\varnothing\\
23&123-234,\ 123-235\\
24&124-245\\
25&\varnothing\\
34&134-234,\ 134-345,\ 234-345\\
35&135-235,\ 135-345,\ 235-345\\
45&145-245,\ 145-345,\ 245-345.
\end{array}
\]

### Theorem 2.3 — no nonempty equality local minimum

Let `R` be a nonempty connected root-labelled cubic four-pole whose boundary semiedges all have label `12`. Then `R` contains either an equal adjacent triangle pair or an `\mathcal M_Z`-decreasing root `2--2` move.

### Proof

Assume neither exists. Every internal edge must therefore occur in Proposition 2.2.

1. The `12` row is empty, so every `12` incidence is a boundary incidence.
2. The `15` row is empty and `15` is not a boundary label; hence `125,135,145` are absent.
3. The `25` row is empty; hence `125,235,245` are absent.
4. For root `14`, the only allowed side is `124-145`; since `145` is absent, any `14` incidence is impossible. Thus `124,134` are absent.
5. For root `24`, the only allowed side is `124-245`; both ends are absent, and consequently `234` cannot realize its `24` incidence.
6. Only `123,345` remain. A `123` vertex needs internal `13,23` neighbours, all among the already eliminated mixed types. A `345` vertex needs `34,35,45` neighbours; equal adjacency is excluded and every allowed distinct neighbour has already been eliminated.

Thus no vertex remains, contradiction. ∎

### Corollary 2.4 — equality termination

Every selected root flip strictly lowers `\mathcal M_Z`. Every equal-face cancellation deletes two vertices of the same positive weight and lowers it by `2w_Z(T)>0`. Therefore every adaptively selected decreasing equality surgery sequence is finite.

---

## 3. DDD boundary

Normalize the disjoint roots to

\[
12,12,34,34.
\]

Define

\[
\begin{array}{c|cccccccccc}
T&123&124&125&134&135&145&234&235&245&345\\
\hline
\omega(T)&3&0&1&3&0&1&1&3&3&3
\end{array}
\]

and the positive weight

\[
w_D(T)=\omega(T)+1.
\]

Thus

\[
\begin{array}{c|cccccccccc}
T&123&124&125&134&135&145&234&235&245&345\\
\hline
w_D(T)&4&1&2&4&1&2&2&4&4&4.
\end{array}
\]

Put

\[
\mathcal M_D(R)=\sum_{v\in V(R)}w_D(\Delta_v).
\]

### Proposition 3.1 — exact DDD flip census

The thirty current sides split as

\[
\boxed{
15\text{ with }\Delta\mathcal M_D<0,
\quad
15\text{ with }\Delta\mathcal M_D>0,
\quad
0\text{ ties}.}
\]

### Proposition 3.2 — DDD nondecreasing table

The complete nondecreasing list is

\[
\begin{array}{c|l}
12&123-124,\ 124-125\\
13&123-135,\ 134-135\\
14&124-134,\ 124-145\\
15&125-135,\ 125-145,\ 135-145\\
23&234-235\\
24&124-234,\ 234-245\\
25&\varnothing\\
34&234-345\\
35&135-235,\ 135-345\\
45&\varnothing.
\end{array}
\]

### Theorem 3.3 — no nonempty DDD local minimum

Let `R` be a nonempty connected root-labelled cubic four-pole whose boundary root multiset is `12,12,34,34`. Then `R` contains an equal adjacent pair or an `\mathcal M_D`-decreasing root flip.

### Proof

Assume neither exists.

1. Roots `25` and `45` are not boundary roots and have empty nondecreasing rows. Thus every triangle containing either root is absent:
   \[
   125,145,235,245,345.
   \]
2. The only allowed `23` side is `234-235`. Since `235` is absent and `23` is not a boundary root, both `123,234` are absent.
3. Every allowed `35` side uses `135` with `235` or `345`; hence `135` is absent.
4. The only allowed `13` neighbours of `134` are `123` or `135`, both absent; hence `134` is absent.
5. Only `124` remains. Its nonboundary `14` incidence would require `134` or `145`, and its nonboundary `24` incidence would require `234`; all are absent.

No source vertex remains, contradiction. ∎

### Corollary 3.4 — DDD termination

Every selected root flip lowers `\mathcal M_D`; every equal-face cancellation deletes two vertices of positive weight. Hence every decreasing DDD surgery sequence is finite.

---

## 4. Unified singular Morse theorem

Let `\sigma` be equality or DDD, and transport the normalized table by a support permutation to the actual boundary roots.

### Theorem 4.1

Every nonempty connected singular root carrier contains one of:

1. an equal-face `2--0` cancellation;
2. a root-valued `2--2` move strictly decreasing the corresponding positive additive Morse function.

Every sequence that repeatedly chooses one of these decreasing moves is finite.

The theorem uses two finite orbit certificates but one proof schema.

---

## 5. Exact scope

This closes the **current-flow termination** part of R2. It proves that no unbounded equality or DDD carrier can be a local minimum or support an infinite adaptive root-surgery sequence.

It does not prove that an arbitrary root flow found on a surgery descendant returns through the history. In particular it does not yet close:

- first failed inverse-transfer localization;
- uniqueness and transport of a co-root token;
- full-state forced-backbone exhaustiveness;
- orientation-hardened odd recurrence exclusion;
- `C6/C8` source-movie cancellation;
- cap-compatible contextual return.

Those are the remaining singular-return obligations.