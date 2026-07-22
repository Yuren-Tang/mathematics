# Petersen resolution parity and the canonical DDD double cover

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `096b15e6fdd692c1344889fc65d6b34c2206d1c6`  
**Parents:**

- `projects/affine-cdc/research/PETERSEN_PIVOT_RESOLUTION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_BACKTRACK_TYPE_T_REDUCTION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_CYCLE_MONODROMY_V1.md`.

**Status:** exact canonical resolution-double-cover and parity-holonomy theorem for every reduced Petersen pivot skeleton; identification with the physical affine `D8` cohomology class remains open.  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, graph-side replacement, or the global five-support theorem.

---

## 1. Resolution fibres of DDD switch states

A pivot-change state is a Petersen edge

\[
F=\{s,t\}.
\]

By DDD atom triality, its two endpoints `s,t` are exactly its two crossed root resolutions. Define the two-point resolution fibre

\[
\mathcal E_F=\{s,t\}.
\]

Suppose the pivot skeleton traverses `F` from pivot `s` to pivot `t`.

- the constant-`s` run on the left forces resolution `t`;
- the constant-`t` run on the right forces resolution `s`.

Thus traversal across the switch exchanges the two elements of `E_F`.

### Definition 1.1 — local resolution flip

Every oriented switch occurrence carries the nontrivial involution

\[
\epsilon_F:s\longleftrightarrow t.
\]

The involution is independent of orientation: reversing the switch applies the same transposition.

---

## 2. Resolution holonomy of a skeleton

Let

\[
\gamma=(s_0,F_1,s_1,\ldots,F_k,s_k)
\]

be a pivot skeleton. Its resolution transport is the composite of the `k` local flips.

### Theorem 2.1 — parity law

The resolution transport of `gamma` is

\[
\boxed{
\operatorname{Hol}_{\mathrm{res}}(\gamma)
=
(-1)^k\in C_2.
}
\]

Equivalently:

- an even number of DDD switch states preserves the resolution sheet;
- an odd number exchanges the two sheets.

### Proof

Every switch contributes the unique nontrivial permutation of a two-point resolution fibre. Their composite is trivial exactly when the number of factors is even. ∎

### Corollary 2.2 — Type-T invariance

A Petersen backtrack

\[
s\to t\to s
\]

contains two flips and has trivial resolution holonomy. Therefore formal Type-T cancellation preserves `Hol_res`.

The resolution parity depends only on the reduced pivot skeleton.

---

## 3. The canonical double cover

Assign one bit to the two resolution sheets. Traversing any Petersen switch edge toggles the bit.

This defines the canonical bipartite double cover of the Petersen pivot graph:

\[
\widetilde P_{\mathrm{res}}
=
P\times\mathbf F_2,
\]

with

\[
(s,b)\sim(t,b+1)
\qquad(st\in E(P)).
\]

### Theorem 3.1 — lifting criterion

A pivot walk lifts to a closed walk in `P_res` if and only if it has even length.

An odd pivot cycle exchanges the two resolution sheets and cannot carry a globally consistent choice of DDD root resolution.

### Interpretation

The obstruction is not the ordinary state repetition of `L(P)`. It is the nontrivial holonomy of the resolution double cover after all rank-two runs have been collapsed.

---

## 4. Relation to simple-cycle support monodromy

For a simple reduced pivot cycle `C`, the cycle-monodromy theorem gives:

- lengths six and eight: support monodromy `Pi(C)=1`;
- lengths five and nine: support monodromy of type `41`.

### Theorem 4.1 — endpoint action

Let `F_0` be the initial DDD/Petersen-edge state of a simple pivot cycle.

1. If `|C|` is even, `Pi(C)=1` fixes both elements of `E_(F_0)`.
2. If `|C|` is odd, `Pi(C)` stabilises `F_0` setwise and exchanges its two Petersen endpoints.

Thus the action of the full support monodromy on the two root resolutions of `F_0` is exactly

\[
\boxed{
\Pi(C)|_{\mathcal E_{F_0}}
=
\operatorname{Hol}_{\mathrm{res}}(C).
}
\]

### Proof

The even case is immediate from identity monodromy.

In the odd case, `Pi(C)` is a four-cycle fixing one support index. Since the state walk closes, it stabilises `F_0`. A four-cycle cannot fix separately the two disjoint root endpoints of `F_0`; it exchanges them as the two opposite pairs of its invariant square matching. This is the nontrivial permutation of `E_(F_0)`. ∎

---

## 5. The linear shadow of the DDD affine class

The DDD stabiliser satisfies

\[
H^1(D_8,E_5)\cong\mathbf F_2.
\]

The resolution parity theorem supplies a canonical graph-level `C2` holonomy:

\[
\chi_{\mathrm{res}}:\pi_1(P)\to\mathbf F_2,
\qquad
\chi_{\mathrm{res}}(\gamma)=|\gamma|\pmod2.
\]

It is nonzero because the Petersen graph has five-cycles.

### Exact relation proved here

On every simple odd core, the type-`41` support monodromy acts nontrivially on the two DDD root resolutions, and this action is exactly `chi_res`.

### Boundary not crossed

The physical affine DDD class contains translation/side-root data in `E5`, whereas `chi_res` records only the permutation of the two root resolutions. Hence:

\[
\boxed{
\chi_{\mathrm{res}}
\text{ is a canonical linear shadow and candidate detector, not yet an identification of the affine }H^1\text{ class.}
}
\]

To prove equality one must compute the physical affine cocycle on one odd bounded core and show that its nonzero class maps to the resolution-sheet exchange.

---

## 6. Consequences for localisation

### Corollary 6.1 — exact Type-T / DDD parity split

After cancelling all Type-T backtracks:

- an even closed reduced skeleton has trivial resolution holonomy and belongs to the identity-return/flat-composition branch;
- an odd closed reduced skeleton has nontrivial resolution holonomy and contains a bounded DDD core whose support monodromy exchanges the two root resolutions.

### Corollary 6.2 — no hidden third branch

At the resolution-sheet level, every reduced closed core is completely classified by one bit. Any further obstruction must lie in:

1. physical affine translation/side semantics within the even branch;
2. the lift of the nontrivial resolution bit to the unique DDD affine class within the odd branch;
3. graph-side four-pole composition.

---

## 7. Next bounded calibration

Choose one explicit Petersen five-cycle. Compute the complete physical side-root/full-frame affine cocycle around it. The target theorem is:

\[
\boxed{
\text{five-cycle resolution flip}
\Longleftrightarrow
\text{nontrivial physical }D_8\text{ affine class}.
}
\]

Because all Petersen five-cycles form one `S5` orbit, one successful equivariant calibration closes the odd simple-core identification.

The even six-cycle then supplies the smallest identity-return calibration for the flat branch.

---

## 8. Reliability boundary

### Exact here

- every DDD switch traverses the nontrivial involution of its two root resolutions;
- resolution holonomy equals pivot-skeleton length parity;
- Type-T backtrack cancellation preserves resolution holonomy;
- the canonical resolution double cover and its lifting criterion;
- agreement between resolution parity and the endpoint action of simple-cycle support monodromy;
- nontriviality of the odd-core resolution class.

### Still open

- equality with the physical affine `D8` cohomology class;
- calculation of the five-cycle affine cocycle;
- even-core flat displacement;
- source-graph contraction and separator transfer;
- strict global descent, horizontal induction, and the global five-support theorem.
