# A forced response coordinate produces a small-support physical cocycle

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `23266dc24af4447fc1e3dd282d9dcd124e392674`  

**Parents:**

- `FINAL_COMPOSITION_BRIDGE_SYNTHESIS_V1.md`;
- the physical cycle--cut response form;
- the ribbon-intersection response geometry;
- `PIVOT_CHANGE_SIX_PORT_STAR_COMPLETION_V1.md`;
- `ORIENTED_CHANNEL_LOCK_BOUNDARY_CALIBRATION_V1.md`.

**Status:** exact symplectic/Lagrangian forcing lemma and exact small-support physical consequence. If a nonempty affine slice of the physical response code is defined by `k` local boundary-coordinate conditions and one further local response coordinate is constant on the whole slice, the full response code contains a nonzero word supported on at most `k+1` physical edge triples. For `k<=3`, its physical cycle projection is zero or a cycle of length at most four; the zero projection is a cut of size at most four. Thus, after the required route-cap calibration, a genuinely forced four- or six-port response can only produce a small separator or a bounded short-cycle carrier.  

**Not implied:** that every forced DDD backbone has already been calibrated as one extra local coordinate in a single fixed capped response graph, automatic category-safe gluing of every short-cycle carrier, a completed global induction, canonical acceptance, Lean verification, manuscript integration, or the global five-support theorem.

---

## 1. Symplectic response space

Let

\[
V=\mathbf F_2^E\oplus\mathbf F_2^E
\]

with alternating form

\[
\omega((z,a),(z',a'))
=z\cdot a'+a\cdot z'.
\]

Let

\[
L\le V
\]

be a Lagrangian subspace:

\[
\boxed{L=L^\perp.}
\]

In the physical response application, `L` is the full transition-cocycle code in `(z,a)` coordinates.

A local transition coordinate is one linear functional

\[
\phi(v)=\omega(u,v)
\]

whose representing vector `u` is supported on one physical edge triple.

Different physical edge triples give linearly independent local coordinate vectors.

---

## 2. Affine response slices

Fix local coordinate functionals

\[
\phi_i(v)=\omega(u_i,v),
\qquad i=1,\ldots,k,
\]

and bits

\[
b_i\in\mathbf F_2.
\]

Define the affine slice

\[
A
=
\{v\in L:\phi_i(v)=b_i\text{ for }1\le i\le k\}.
\]

Assume

\[
A\ne\varnothing.
\]

Put

\[
K=\bigcap_{i=1}^k\ker\phi_i.
\]

Then for any `v_0 in A`,

\[
\boxed{A=v_0+(L\cap K).}
\]

Thus the translation space of the admissible response slice is exactly

\[
T_A=L\cap K.
\]

---

## 3. Forced-coordinate lemma

Let

\[
\phi_0(v)=\omega(u_0,v)
\]

be one further local response coordinate.

Assume `phi_0` is constant on `A`.

Then for all

\[
t\in T_A=L\cap K
\]

one has

\[
\phi_0(t)=0.
\]

Equivalently,

\[
u_0\in(L\cap K)^\perp.
\]

### Theorem 3.1 — Lagrangian forced-coordinate theorem

\[
\boxed{
 u_0
 \in
 L+\operatorname{span}\{u_1,\ldots,u_k\}.}
\]

Hence there exist bits

\[
\epsilon_1,\ldots,\epsilon_k
\]

such that

\[
\boxed{
 w
 =
 u_0+\sum_{i=1}^k\epsilon_i u_i
 \in L.}
\]

### Proof

Because

\[
K=\bigcap_i u_i^\perp,
\]

one has

\[
K^\perp=\operatorname{span}\{u_1,\ldots,u_k\}.
\]

For finite-dimensional subspaces,

\[
(L\cap K)^\perp=L^\perp+K^\perp.
\]

Since `L` is Lagrangian,

\[
L^\perp=L.
\]

Therefore

\[
(L\cap K)^\perp
=
L+\operatorname{span}\{u_1,\ldots,u_k\}.
\]

The constancy of `phi_0` gives

\[
u_0\in(L\cap K)^\perp,
\]

which is the claimed decomposition. ∎

---

## 4. Support bound

Assume the local coordinates

\[
\phi_0,\phi_1,\ldots,\phi_k
\]

belong to pairwise distinct physical edge triples.

Then the representing vectors

\[
u_0,u_1,\ldots,u_k
\]

are linearly independent.

Consequently the word `w` from Theorem 3.1 is nonzero.

### Theorem 4.1 — small-support witness

The full Lagrangian response code contains a nonzero word

\[
\boxed{w\in L\setminus\{0\}}
\]

whose active physical support is contained in at most

\[
\boxed{k+1}
\]

edge triples.

### Proof

The word is a sum of at most `k+1` local coordinate vectors, each supported on one physical edge triple. Distinct support makes the sum nonzero. ∎

### Important special cases

For a four-port route cap with two prescribed cap coordinates:

\[
\boxed{k=2\Longrightarrow|\operatorname{supp}_{\rm phys}w|\le3.}
\]

For a six-port or three-cap carrier with three prescribed boundary coordinates:

\[
\boxed{k=3\Longrightarrow|\operatorname{supp}_{\rm phys}w|\le4.}
\]

---

## 5. Physical cycle--cut consequence

Now let

\[
w=(z,a)\in\mathscr L_G
\]

belong to the physical response code.

The exact sequence gives

\[
\boxed{z\in Z(G).}
\]

If

\[
z=0,
\]

then

\[
\boxed{a\in B(G).}
\]

### Theorem 5.1 — small support is a cut or short cycle

Assume

\[
|\operatorname{supp}_{\rm phys}w|\le q.
\]

Then exactly one of the following occurs.

1. **Cut branch.**  
   `z=0`, and `a` is a nonzero cut supported on at most `q` physical edges.

2. **Cycle branch.**  
   `z ne 0`, and `z` is a nonempty even subgraph supported on at most `q` physical edges.

For

\[
q\le4,
\]

the cycle branch is a union of loops, parallel two-cycles, triangles, or four-cycles.

### Proof

The cut statement is the kernel theorem for the response code. In the second branch, `z` lies in the ordinary binary cycle space and its support is contained in the active physical support of `w`. An even subgraph with at most four edges has only the listed cycle components. ∎

---

## 6. Cubic source interpretation

Let `G` be a loopless cubic source graph.

A simple cycle `C` of length `m` has one external incidence at each cycle vertex unless a parallel-edge degeneration is present. Therefore its vertex set has edge boundary of size at most `m`:

\[
|\delta_G(V(C))|\le m.
\]

### Corollary 6.1 — separator or bounded carrier

For

\[
q\le4,
\]

every nonzero small-support response word gives one of:

1. a cut of size at most four;
2. a loop or parallel-edge bounded degeneration;
3. a triangle or four-cycle enclosed by a cut of size at most four;
4. a graph with only a bounded number of vertices on one side of that cut.

Thus in the cyclically five-edge-connected minimal-counterexample regime, a forced local response coordinate cannot survive as an unbounded prime response.

It must enter:

- the existing two-/three-/four-cut gluing branch;
- a bounded cycle/cap library;
- or a category-degeneration branch.

### Trust note

Cyclic five-edge connectivity excludes a small cut only when both shores contain cycles. If one shore is acyclic or bounded, it must be discharged by the explicit bounded-carrier/category lemma rather than by connectivity alone.

---

## 7. Affine versus linear forcing

The response slice `A` is affine, and the forced value of `phi_0` may be zero or one.

Only differences of admissible responses enter the proof. Hence the theorem does not require the forced value itself to be zero.

The statement is:

\[
\phi_0|_A=\text{constant}
\]

rather than

\[
\phi_0|_A=0.
\]

This is essential for cap residues and forced terminal routes, whose prescribed coordinate is often one.

---

## 8. Gauge invariance

Changing the ordering of the two cross transitions at one physical edge applies one local symplectic transformation in

\[
Sp(2,2)=GL(2,2).
\]

The Lagrangian property, the codimension of the affine slice, and the conclusion that a witness is supported on at most `k+1` physical edge triples are invariant under such local gauge changes.

The precise coordinate vector `w` may change, but the existence of a small-support witness does not.

Thus the theorem is suitable for physical cap applications where cross-transition order is auxiliary.

---

## 9. Application template for the final bridge

Let `R` be a four- or six-port residual carrier.

### Step A — choose one fixed route cap

Close the carrier by a fixed cap gadget so that all relevant terminal route choices are represented by local transition coordinates in one physical response code

\[
\mathscr L_{\widehat R}.
\]

### Step B — identify the admissible affine slice

Express the inherited ordered boundary state by at most three independent local affine coordinate conditions:

\[
\phi_i=b_i.
\]

### Step C — calibrate the forced backbone

Show that the statement

\[
\text{every admissible completion contains the same backbone pair}
\]

is exactly the constancy of one additional local transition coordinate

\[
\phi_0.
\]

### Step D — apply Theorem 4.1

Obtain a nonzero response word supported on at most four physical edge triples.

### Step E — discharge

Use Theorem 5.1 and Corollary 6.1 to obtain:

- a small separator;
- a bounded short-cycle carrier;
- or a contradiction to the minimal prime-response assumption.

---

## 10. Six-port calibration frontier

For the pivot-change boundary

\[
(s,x,z\mid w,t,y),
\]

the six cross matchings split into:

- four root-valued star completions;
- two forced-backbone matchings containing `s--t`.

The remaining calibration theorem must place all six route responses in one fixed three-cap transition model and prove:

\[
\boxed{
\text{the `s--t` pairing is present}
\Longleftrightarrow
\phi_0=1}
\]

for one local transition coordinate `phi_0`, while the inherited outer state imposes at most three independent affine coordinates.

Once this dictionary is established, the small-support theorem gives a witness on at most four physical edges and closes the prime forced-backbone branch up to the already isolated bounded-degeneration lemma.

### Why this is now the exact missing bridge

All coefficient-side facts of the six-port table are already exact. The only unproved datum is the transition-matroid realisation of the six terminal matchings in one capped graph.

This is finite and topological, not another unbounded source-graph problem.

---

## 11. Four-port corollary

For an ordinary four-pole with two cap coordinates, suppose one further route coordinate is forced throughout a nonempty physical response slice.

Then

\[
\boxed{
\mathscr L_{\widehat Q}
\text{ contains a nonzero word on at most three physical edges}.}
\]

Hence the response produces:

- a cut of size at most three;
- a loop/parallel degeneration;
- or a triangle carrier.

This gives a direct Lagrangian explanation for why a genuinely prime four-port fixed route cannot survive after the physical Type-T/Type-H mismatch kernels have been eliminated.

The exact identification of each ten-state forced route with the appropriate cap coordinate should be recorded when the theorem is consumed.

---

## 12. Relation to the radical strategy

The forced-coordinate theorem is stronger and more elementary than the initially proposed radical lemma in the small-cap regime.

It does not first construct a large radical cycle. Instead it uses Lagrangian self-duality to produce a response word supported near the forced coordinates.

The two strategies are compatible:

- if the small-support word has zero cycle projection, it is directly a cut;
- if it has nonzero short-cycle projection, that cycle is often boundary-parallel and hence radical in the ribbon model;
- if it is not radical, the response pairing supplies a witnessing crossed route and therefore profile escape.

Thus the radical theorem is needed only for a residual short-cycle carrier not already discharged by its small separator.

---

## 13. Revised first attack

The next task is no longer the general forced-backbone radical lemma.

It is the finite cap-calibration theorem:

> Construct one fixed three-cap transition carrier for the six-port pivot-change cell and identify the six terminal perfect matchings with its local transition words. Prove that the two non-root-completable matchings are exactly the affine slice on which one distinguished cap coordinate is forced.

After that theorem, the present small-support result converts the forced branch to a cut/cycle on at most four physical edges.

---

## 14. Trust boundary

### Exact here

- the Lagrangian forced-coordinate theorem;
- the support bound `k+1`;
- the physical cut/cycle dichotomy;
- the short-cycle classification for support at most four;
- gauge invariance of the support bound;
- the four-port support-three corollary;
- the conditional six-port support-four corollary after cap calibration.

### Still open

- one fixed transition model containing all six pivot-change matchings;
- exact identification of the forced `s--t` pair with one additional local coordinate;
- bounded-category handling of every loop/parallel/short-cycle output;
- global well-founded induction;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
