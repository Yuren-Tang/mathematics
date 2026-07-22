# Petersen pivot resolution and the DDD switch skeleton

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `132c34cc834792a2970435e9b1712b2130d6800c`  
**Parents:**

- `projects/affine-cdc/five-support/holonomy-defects-and-atoms.md`;
- the retained theorem `FIVE_CDC_DEFECT_MINIMAL_FOREST_PETERSEN_TRANSPORT_V1.md`;
- the retained theorem `FIVE_CDC_DDD_ATOM_RESOLUTION_TRIALITY_V1.md`;
- `projects/affine-cdc/research/SIDE_SIGNATURE_CONTROL_TARGET_V1.md`.

**Status:** exact coefficient-side decomposition of every enriched co-root strip into rank-two root-resolvable runs and DDD pivot-switch states; graph-side replacement and strict descent remain open.  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Petersen state and output notation

Let

\[
P=KG(5,2)
\]

be the Petersen graph. Its vertices are the ten roots

\[
R_5=\{e_i+e_j:i<j\},
\]

and two roots are adjacent in `P` exactly when their support pairs are disjoint.

A virtual one-factor state of a co-root strip is an edge

\[
F=\{a,b\}\in E(P).
\]

By the co-root atom triality theorem, the two endpoints `a,b` are exactly the two crossed root resolutions of the state `F`.

Let two consecutive strip states be

\[
F^- = \{s,x\},
\qquad
F^+ = \{s,y\},
\]

so they are adjacent in the line graph `L(P)` and share the Petersen vertex `s`.

The vertex `s` has exactly three Petersen neighbours. Write `z` for the third neighbour distinct from `x,y`. The Petersen transport theorem identifies `z` with the side-root emitted at this turn.

### Definition 1.1 — transition pivot

The common endpoint

\[
\boxed{s=F^-\cap F^+}
\]

is the **pivot** of the transition.

---

## 2. The local root triangle

### Theorem 2.1 — nonshared-endpoint triangle

For every transition

\[
\{s,x\}\longrightarrow\{s,y\}
\]

with emitted side root `z`, one has

\[
\boxed{x+y+z=0.}
\]

Equivalently, `x,y,z` are the three roots of one triangle of `K_5`.

### Proof

Regard the Petersen vertices as two-subsets of `[5]`. The neighbours of `s` are exactly the three two-subsets of the complementary three-set

\[
[5]\setminus s.
\]

Thus `x,y,z` are the three edges of the triangle on that complementary three-set. Their binary incidence vectors sum to zero. ∎

### Theorem 2.2 — unique root resolution of one transition

Choose a root resolution

\[
r^-\in F^-,
\qquad
r^+\in F^+.
\]

Then

\[
r^-+r^++z=0
\]

if and only if

\[
\boxed{r^-=x,\qquad r^+=y.}
\]

In words: a transport turn becomes a root triangle only by choosing the two **nonshared** endpoints of the consecutive Petersen states.

### Proof

The choice `(x,y)` works by Theorem 2.1.

The other possibilities do not:

- choosing `(s,s)` gives sum `z\ne0`;
- choosing `s` and one of `x,y` sums two disjoint roots, hence gives the co-root completing their `K_6` one-factor, not the root `z`.

Therefore the nonshared pair is unique. ∎

---

## 3. Resolution of a state walk

Let

\[
F_0,F_1,\ldots,F_m
\]

be the Petersen-edge state walk of a co-root strip segment. For `1\le t\le m`, define its transition pivot

\[
s_t=F_{t-1}\cap F_t.
\]

A simultaneous root resolution is a choice

\[
r_t\in F_t
\qquad(0\le t\le m)
\]

such that every transport turn, together with its actual emitted side root, is a root triangle.

### Theorem 3.1 — constant-pivot criterion

The state walk admits a simultaneous root resolution if and only if

\[
\boxed{s_1=s_2=\cdots=s_m.}
\]

When it exists, the resolution is unique.

### Proof

At an interior state `F_t`, the transition on its left forces

\[
r_t=F_t\setminus\{s_t\},
\]

while the transition on its right forces

\[
r_t=F_t\setminus\{s_{t+1}\}.
\]

These two forced choices agree exactly when

\[
s_t=s_{t+1}.
\]

Hence all consecutive pivots must agree, and then every state has one forced nonpivot endpoint. The endpoint choices are forced by the first and last turns. ∎

### Corollary 3.2 — star-clique form

A root-resolvable strip state walk lies entirely in the three-state clique of `L(P)` consisting of the Petersen edges incident with one fixed vertex `s`.

Conversely, every walk in this star clique has the unique root resolution of Theorem 3.1.

---

## 4. Rank-two meaning of a constant-pivot run

Fix a pivot root `s`. Its three Petersen neighbours are the three roots on the complementary three-set

\[
[5]\setminus s.
\]

They form the three nonzero elements of one binary plane

\[
W_s\cong\mathbf F_2^2.
\]

### Theorem 4.1 — Tait-sector resolution

The unique root resolution of a constant-pivot run uses only the three roots of `W_s`; every emitted side root of the run also lies in `W_s`.

Therefore the resolved coefficient chain is a rank-two/Tait chain, and the two support coordinates contained in `s` are absent throughout the resolved run.

### Consequence 4.2

The pivot `s` is not merely an automaton state. It is the omitted support pair of one local rank-two resolution sector.

Thus a long constant-pivot run contains no new coefficient holonomy: all of its coefficient data lie in one three-root triangle.

---

## 5. Pivot change is exactly a DDD atom conflict

Consider an interior state `F_t` with distinct left and right pivots:

\[
s_t\ne s_{t+1}.
\]

Since both pivots are endpoints of `F_t`, one has

\[
\boxed{F_t=\{s_t,s_{t+1}\}.}
\]

### Theorem 5.1 — opposite forced resolutions

At a pivot change, the left transition forces the root resolution

\[
r_t=s_{t+1},
\]

whereas the right transition forces

\[
r_t=s_t.
\]

These are exactly the two crossed root resolutions of the DDD/co-root atom represented by the Petersen edge `F_t`.

### Proof

The left transition shares `s_t`, so Theorem 2.2 forces the other endpoint of `F_t`, namely `s_{t+1}`. The right transition shares `s_{t+1}`, so it forces the other endpoint `s_t`. The co-root atom triality theorem identifies the endpoints of `F_t` with its two crossed root resolutions. ∎

### Interpretation

A pivot change is not an unclassified failure of the Petersen transducer. It is the precise point where the two shores demand opposite resolutions of one already known DDD atom.

---

## 6. Canonical pivot decomposition

Partition the pivot word

\[
s_1,s_2,\ldots,s_m
\]

into maximal constant runs.

### Theorem 6.1 — root-run / DDD-switch factorisation

Every co-root strip state walk has a canonical coefficient-side factorisation into:

1. maximal constant-pivot runs, each carrying a unique rank-two root resolution and preserving its complete emitted side-root word; and
2. pivot-change states, each carrying one DDD/Petersen-edge atom whose two root resolutions are forced oppositely by the adjacent runs.

No coefficient state beyond the existing root triangle and DDD atom alphabets occurs.

### Proof

Theorem 3.1 resolves each maximal constant block uniquely. Theorem 5.1 identifies every boundary between two distinct blocks with one DDD atom resolution conflict. Maximality makes the decomposition unique. ∎

### Definition 6.2 — pivot skeleton

Collapse every constant-pivot run to its pivot. At every change from pivot `s` to pivot `t`, retain the switch state

\[
F=\{s,t\}.
\]

The resulting sequence is an ordinary walk in the Petersen graph `P`:

\[
s_0,F_1,s_1,F_2,\ldots,F_k,s_k.
\]

The edges of this walk are exactly the DDD switch states.

### Corollary 6.3 — finite coefficient skeleton

A pivot-skeleton segment with no repeated pivot has at most ten pivot vertices and at most nine DDD switch states.

If a pivot repeats, the intervening coefficient obstruction contains a closed Petersen subwalk. Choosing a shortest repeated-pivot segment localises the coefficient skeleton to a simple Petersen cycle of bounded size.

This bound concerns the coefficient skeleton only. External attached components may still carry unbounded graph-side semantics.

---

## 7. Relation to the side-signature frontier

The previous enriched-state warning was necessary:

\[
\text{repeated }L(P)\text{ state}
\not\Rightarrow
\text{replaceable strip segment}.
\]

The present theorem does not contradict it. It identifies exactly what the additional output word can do at coefficient level.

### Exact reduction obtained here

The side-root output word of a co-root strip is generated by two known mechanisms only:

- inside one constant-pivot run, it is the boundary word of a rank-two root-triangle chain;
- at a pivot change, the two adjacent rank-two chains demand the two opposite root resolutions of one DDD atom.

Hence the unbounded coefficient alphabet has disappeared. The remaining unbounded datum is purely compositional:

- how external root components identify or separate the emitted side edges of the rank-two runs;
- whether a DDD switch state may be resolved, split, or isolated without changing the original incidence semantics.

### Revised first composition target

For one support-minimal laminar four-port interval, prove one of:

1. a constant-pivot rank-two run is composition-safely serialisable or contractible;
2. external attachments crossing such a run produce the existing route/profile escape;
3. attachment separation produces a cyclic separator/four-pole;
4. the interval reduces to a bounded Petersen pivot skeleton of DDD atoms;
5. failure of all resolutions realises the physical `D_8` class.

This is strictly sharper than treating the whole `L(P)` walk and side-output word as one unstructured state.

---

## 8. Trust boundary

### Exact here

- the transition-pivot definition;
- the nonshared-endpoint root triangle;
- uniqueness of one-turn root resolution;
- the constant-pivot criterion for simultaneous strip resolution;
- confinement of each resolved run to one rank-two/Tait root plane;
- identification of every pivot change with opposite forced resolutions of one DDD atom;
- the canonical factorisation into rank-two runs and a Petersen pivot skeleton;
- the bounded size of a pivot skeleton with no repeated pivot.

### Still open

- a graph-incidence-preserving replacement for a constant-pivot run;
- proof that a crossed atom resolution transfers through the original four-pole composition;
- control of external components joining several emitted side edges;
- extraction of a separator from a repeated pivot with nontrivial attached semantics;
- identification of a closed pivot skeleton with the physical `D_8` cohomology class;
- strict Type-T/Type-H descent, horizontal induction, and the global five-support theorem.
