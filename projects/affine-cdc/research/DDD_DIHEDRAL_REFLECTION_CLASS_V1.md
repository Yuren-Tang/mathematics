# The DDD dihedral affine class is reflection-supported

## Research correction dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `73470fa8a6623878abcb1b5223f741448f0d9c29`  
**Parents:**

- `projects/affine-cdc/research/PETERSEN_CYCLE_MONODROMY_V1.md`;
- `projects/affine-cdc/research/PETERSEN_RESOLUTION_PARITY_V1.md`;
- `projects/affine-cdc/research/SIX_OUTPUT_RETURN_CELL_NORMAL_FORM_V1.md`;
- the retained theorem `H^1(D_8,E_5) ~= F_2`;
- the retained cyclic theorem `H^1(C_4,E_5)=0` for type-`41` support monodromy.

**Status:** exact cohomological correction and sharper physical calibration target. The unique nontrivial DDD affine class vanishes on the rotation subgroup and is detected only by a reflection comparison.  
**Supersedes:** every suggestion that one Petersen five-cycle affine computation by itself can distinguish the trivial and nontrivial `D8` affine classes.  
**Not implied:** physical realization of the required reflection loop, source-graph replacement, canonical acceptance, Lean verification, or the global five-support theorem.

---

## 1. The DDD stabiliser

Fix one DDD/Petersen-edge state

\[
F=\{\infty i,X,Y\},
\]

where `X,Y` are disjoint roots on the complementary four-set

\[
Q=[5]\setminus\{i\}.
\]

Its support stabiliser is

\[
D=\operatorname{Stab}_{S_5}(F)\cong D_8.
\]

Choose an order-four rotation

\[
\rho\in D
\]

whose cyclic action on `Q` has `X,Y` as the two opposite pairs. Let

\[
R=\langle\rho\rangle\cong C_4.
\]

Then

\[
1\longrightarrow R
\longrightarrow D
\longrightarrow C_2
\longrightarrow1
\]

is the usual rotation/reflection extension.

---

## 2. The fixed line of the rotation subgroup

Let

\[
E_5=\{x\in\mathbf F_2^5:\sum_jx_j=0\}
\]

with its natural `S5` action. Put

\[
q_i=\mathbf1+e_i,
\]

the weight-four co-root supported on `Q`.

### Lemma 2.1 — rotation fixed space

\[
\boxed{E_5^R=\langle q_i\rangle.}
\]

### Proof

A vector fixed by the four-cycle `rho` has one common coordinate `b` on the four points of `Q` and one coordinate `a` at `i`. The even-weight condition gives

\[
a+4b=a=0.
\]

Thus the fixed vectors are `0` and the vector equal to one on `Q`, namely `q_i`. ∎

The complete dihedral stabiliser fixes `q_i`, because it fixes `i` and permutes the four points of `Q`.

---

## 3. Inflation-restriction calculation

The cyclic affine-holonomy theorem gives

\[
\boxed{H^1(R,E_5)=0.}
\]

Apply inflation-restriction to the normal subgroup `R`:

\[
0\longrightarrow
H^1(D/R,E_5^R)
\longrightarrow
H^1(D,E_5)
\longrightarrow
H^1(R,E_5)^{D/R}.
\]

The right-hand term is zero, so inflation is an isomorphism:

\[
H^1(D,E_5)
\cong
H^1(C_2,\langle q_i\rangle).
\]

The quotient reflection acts trivially on `q_i`. In characteristic two,

\[
H^1(C_2,\mathbf F_2)\cong\mathbf F_2.
\]

Therefore:

### Theorem 3.1 — reflection-support theorem

\[
\boxed{H^1(D,E_5)\cong\mathbf F_2,}
\]

and its unique nonzero class is inflated from the reflection quotient

\[
D/R\cong C_2.
\]

Equivalently, after adding a coboundary so that a cocycle `c` vanishes on the rotation subgroup,

\[
\boxed{
 c(\rho^k)=0,
 \qquad
 c(\sigma\rho^k)=q_i
}
\]

for every reflection `sigma rho^k`.

### Uniqueness of the normalisation

Because the ambiguity in killing the restriction to `R` is an `R`-fixed vector and

\[
E_5^R=\langle q_i\rangle\subseteq E_5^D,
\]

changing the normalising origin by that ambiguity adds zero coboundary on all of `D`. Hence the normalised reflection value `0` or `q_i` is canonical.

---

## 4. Consequence for Petersen five-cycles

Every simple Petersen five-cycle has type-`41` support monodromy. Relative to its canonical invariant DDD state, that monodromy is an order-four rotation

\[
\rho\in R.
\]

### Corollary 4.1 — rotation blindness

The restriction map

\[
H^1(D,E_5)\longrightarrow H^1(R,E_5)
\]

is zero. Therefore one physical loop whose support monodromy is `rho` or `rho^(-1)` cannot distinguish the trivial and nontrivial `D8` affine classes.

Any translation part measured on that single cyclic loop can be removed by an affine-origin change on the cyclic subgroup.

### Corollary 4.2 — resolution parity is linear, not affine

The Petersen five-cycle exchanges the two crossed root resolutions of its invariant DDD state. This endpoint exchange is the linear action of the order-four rotation on the two resolution endpoints.

It occurs independently of whether the ambient `D8` affine cocycle is trivial or nontrivial.

Hence the odd resolution-sheet parity is an exact linear monodromy invariant, but it is **not** a detector of the nonzero class in `H^1(D,E5)`.

---

## 5. Correct physical calibration object

A complete DDD affine calibration must contain both kinds of dihedral motion.

### Definition 5.1 — dihedral calibration pair

A physical calibration pair consists of:

1. one bounded loop or core with support monodromy the rotation `rho`;
2. one compatible bounded comparison with support monodromy a reflection `sigma` stabilising the same DDD state `F`.

The reflection may arise as:

- a physical comparison between a five-cycle realization and its reflected/reversed realization;
- a bounded route loop representing a DDD reflection;
- or the difference between two bounded cores whose support actions differ by `sigma`.

### Theorem 5.2 — one-bit reflection test

First change affine origin so that the rotation cocycle vanishes:

\[
c(\rho)=0.
\]

Then the full `D8` affine class is determined by the single reflection value

\[
\boxed{c(\sigma)\in\{0,q_i\}.}
\]

- `c(sigma)=0` gives the trivial affine class;
- `c(sigma)=q_i` gives the unique nontrivial DDD affine class.

No further group element is required.

### Proof

Theorem 3.1 identifies the cohomology with the quotient `C2` and its fixed coefficient line `<q_i>`. The reflection coset generates the quotient. ∎

---

## 6. Revised interpretation of the six-output five-cycle core

The six-output return-cell theorem remains valid at coefficient and linear-monodromy level:

- the only cyclic reduced core in such a cell is one Petersen five-cycle;
- it has type-`41` rotation monodromy;
- it exchanges the two root resolutions of a canonical DDD state.

What changes is the affine conclusion.

The five-cycle supplies the **rotation half** of the bounded DDD object. To decide the physical affine class, the graph-side incidence semantics must also supply or obstruct a compatible **reflection half**.

Therefore the corrected alternatives for a five-cycle return cell are:

1. a bounded reflection comparison exists and has translation `0`, so the dihedral affine class is trivial;
2. a bounded reflection comparison exists and has translation `q_i`, giving the unique DDD class;
3. no compatible reflection comparison exists, and that failure itself localises an empty fibre, route obstruction, smaller separator, or bounded defect interface.

This is a stricter and more useful target than computing the rotation loop alone.

---

## 7. Corrected next obligation

### Target 7.1 — reflection realisation or obstruction

For one physical Petersen five-cycle core with invariant state `F`, construct a bounded reflected/reversed comparison preserving the same four-port boundary semantics, or prove that the attempt yields one of:

- a root-fibre edge or vertex defect;
- a route/profile escape;
- a smaller cyclic separator/four-pole;
- a bounded DDD/co-root atom.

If the reflection exists, normalise the rotation cocycle to zero and compute whether its reflection translation is `0` or `q_i`.

Because `S5` acts transitively on DDD states and on Petersen five-cycles, one equivariant reflection calculation suffices once physical realisability is proved.

---

## 8. Trust boundary

### Exact here

- `E5^<rho>=<q_i>` for the type-`41` rotation;
- the inflation-restriction isomorphism
  \[
  H^1(D_8,E_5)\cong H^1(C_2,\langle q_i\rangle)\cong\mathbf F_2;
  \]
- vanishing of the unique nonzero class on the rotation subgroup after canonical normalisation;
- value `q_i` on the reflection coset;
- impossibility of detecting the `D8` affine class from one five-cycle rotation alone;
- separation of linear resolution parity from affine DDD cohomology;
- the corrected rotation-plus-reflection calibration target.

### Still open

- a physical bounded reflection realization for the Petersen five-cycle core;
- transfer of forward/reversed five-cycle semantics through the original source graph;
- whether reflection failure always yields strict separator/defect progress;
- source-graph contraction and gluing;
- horizontal induction and the global five-support theorem.
