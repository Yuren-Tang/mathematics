# Symmetry correction for the cap-residue comparison

## 1. Scope

This note supersedes any wording in earlier active frontier chapters that canonically identifies the following three symmetry objects:

1. the affine symmetry of the four scalar sheets;
2. the coordinate stabiliser of the physical terminal route `12\mid34`;
3. the support-label stabiliser of a DDD `K_6` one-factor.

They have isomorphic subgroups in relevant coordinates, but they are not the same labelled group without a constructed comparison map.

In particular, Section 9 of [`touch-shadows-and-cap-residue.md`](touch-shadows-and-cap-residue.md) must be read with the correction below.

## 2. Sheet symmetry

The four scalar sheets are indexed by

$$
\Lambda_g
=
\{\lambda\in V^*: \lambda(g)=1\}
\cong AG(2,2).
$$

Their natural affine automorphism group is

$$
\boxed{
AGL(2,2)\cong S_4.
}
$$

The ordered basis of the quartic terminal nucleus is indexed by these four sheets.  Consequently the canonical sheet-equivariance of the nucleus and of successive nucleus transport is `S_4`-equivariance.

No physical pairing of the four terminal semiedges canonically chooses a perfect matching on the sheet-index set.

## 3. Physical terminal-route symmetry

The four physical terminal semiedges form a different four-element set.  The locked route

$$
12\mid34
$$

selects one perfect matching of this terminal set.  Its setwise coordinate stabiliser is abstractly

$$
S_2\wr S_2\cong D_8.
$$

This `D_8` acts on terminal labels and on the two route caps.  It is not, by definition alone, an action on the sheet labels or on the support labels of `E_5`.

The bounded residue

$$
R=\{r_p,r_q\}
$$

is canonical relative to the labelled route caps.  Its covariance is therefore a physical terminal-route statement, not yet a DDD statement.

## 4. DDD support-label symmetry

A DDD state is a perfect matching of the support-label `K_6`.  Its stabiliser inside the support permutation group is

$$
\boxed{
\operatorname{Stab}(F_*)\cong D_8.
}
$$

This group acts on support labels and on the three resolutions of one co-root atom.  It is the physical DDD one-factor stabiliser established in the atom-triality theorem.

It is not canonically identified with the terminal-route coordinate stabiliser merely because both groups are abstractly dihedral of order eight.

## 5. Correct comparison problem

The present data are:

1. a sheet-indexed curvature class
   $$
   [w]\in
   \mathbf F_2^{\Lambda_g}/\operatorname{Aff}(\Lambda_g,\mathbf F_2);
   $$
2. a terminal-route cap residue
   $$
   R=\{r_p,r_q\};
   $$
3. a possible DDD support-label cocycle/class.

The open theorem is to construct a graph-level map or correspondence among these data and prove its compatibility with the relevant group actions.

Thus the correct statement is:

$$
\boxed{
\text{same one-dimensional obstruction pattern and abstract group type}
\not\Rightarrow
\text{canonical identification}.
}
$$

Only after a comparison map is constructed may one claim that a prime coupled cap cocircuit carries the physical DDD class.

## 6. Consequences for the active frontier

The correction does not affect:

- the terminal-nucleus theorem;
- the curvature-carrier quotient;
- split-or-peel recursion;
- touch-shadow closure;
- the bounded two-transition cap residue;
- IAS loop/parallel/twin/pendant classification;
- coupled/separated cocircuit decomposition;
- cocircuit cut-rank formulas.

It changes only the interpretation of the irreducible branch.  The final branch must be described as a **candidate for comparison with DDD**, not as an already identified `D_8` class.

## 7. Reliability boundary

This is a theorem-scope correction. It does not assert that the comparison map exists, that the prime coupled branch is unique, or that the global five-support theorem is proved.
