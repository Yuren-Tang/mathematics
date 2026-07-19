# Isotropic completion of the two-transition cap residue

## 1. Purpose

Every nonflat common-cut witness determines, after bounded touch closure, a two-transition residue

$$
R=\{r_p,r_q\},
$$

where `p=v_{z_{12}}` and `q=v_{z_{34}}` are the two route-cap vertices of the canonical `4`-regular carrier, and `r_p,r_q` are one cross transition at each vertex.

This chapter determines the first full-transition-matroid obstruction carried by `R`.

1. `R` is never a cocycle of the full transition matroid.
2. Any cocycle completion must add at least one further transition at each cap vertex.
3. A completion supported only on the two cap vertex triples exists exactly in a finite list of twin/pendant interlacement configurations.
4. A direct two-element circuit residue is also possible only in a finite twin/pendant list.

Thus the bounded residue yields an exact dichotomy:

- a low-order interlacement split is already visible at the two cap vertices; or
- every full cocycle completion must leave the cap region and carry a global connection certificate.

## 2. IAS representation

Let

$$
F=\mathcal L(\widehat Q)
$$

be the route-capped `4`-regular graph. Choose an Euler system and let

$$
G=\mathcal I(C)
$$

be its interlacement graph, with adjacency matrix `A` over `\mathbf F_2`.

The transition matroid is represented by

$$
IAS(G)
=
\bigl(I\mid A\mid I+A\bigr).
$$

At every vertex `v` the three transition columns are denoted

$$
\phi_v,
\qquad
\chi_v,
\qquad
\psi_v,
$$

with

$$
\phi_v=e_v,
\qquad
\chi_v=A_v,
\qquad
\psi_v=e_v+A_v.
$$

They satisfy

$$
\boxed{
\phi_v+\chi_v+\psi_v=0.
}
$$

The labels depend on the Euler system, but the vertex triple is intrinsic.

## 3. Vertex-triple parity of cocycles

A cocycle vector of the represented binary matroid is a row-space vector. For a row coefficient vector `y`, its three coordinates at vertex `v` are

$$
\boxed{
\bigl(y_v,(yA)_v,y_v+(yA)_v\bigr).
}
$$

### Theorem 3.1 — even triple law

Every full transition-matroid cocycle meets each vertex triple in `0` or `2` elements.

#### Proof

The sum of the three displayed coordinates is zero. Equivalently, every cocycle is orthogonal to the vertex-triple dependence. ∎

### Corollary 3.2 — the cap residue is not a cocycle

The two-transition residue `R` has one element in the triple at `p` and one in the triple at `q`. Hence

$$
\boxed{R\text{ is not a full cocycle of }M_\tau(F).}
$$

Any cocycle containing the prescribed residue transitions must contain at least one additional transition in each of the two cap triples.

This corrects the tempting but false interpretation of the cap residue as a two-element cocircuit.

## 4. Cocycles supported on two vertex triples

Suppose a cocycle has no support outside the triples at distinct vertices `p,q`. Then for every `v\notin\{p,q\}`,

$$
y_v=0,
\qquad
(yA)_v=0.
$$

Therefore

$$
\operatorname{supp}(y)\subseteq\{p,q\}.
$$

There are three nonzero possibilities.

### Case A: `y=e_p`

For every outside vertex `v`,

$$
A_{pv}=0.
$$

Thus `p` has no neighbour outside `q`. To have nonzero support at the `q` triple, `p` and `q` must be adjacent. Hence

$$
N_G(p)=\{q\}.
$$

The cocycle pairs are

$$
\{\phi_p,\psi_p\}
\quad\text{and}\quad
\{\chi_q,\psi_q\}.
$$

### Case B: `y=e_q`

Symmetrically,

$$
N_G(q)=\{p\},
$$

and the pairs are

$$
\{\chi_p,\psi_p\}
\quad\text{and}\quad
\{\phi_q,\psi_q\}.
$$

### Case C: `y=e_p+e_q`

For every outside vertex `v`,

$$
A_{pv}=A_{qv}.
$$

Thus `p,q` have identical neighbourhoods outside the pair.

- If `p,q` are nonadjacent, the cocycle pairs are
  $$
  \{\phi_p,\psi_p\},
  \qquad
  \{\phi_q,\psi_q\}.
  $$
- If `p,q` are adjacent, the pairs are
  $$
  \{\phi_p,\chi_p\},
  \qquad
  \{\phi_q,\chi_q\}.
  $$

### Theorem 4.1 — local cocycle-completion classification

A nonzero full cocycle supported exactly on the two cap vertex triples exists if and only if one of:

1. `p` is adjacent only to `q`;
2. `q` is adjacent only to `p`;
3. `p,q` are nonadjacent twins;
4. `p,q` are adjacent twins.

For a specified residue pair `R=\{r_p,r_q\}`, such a local completion exists precisely when `r_p,r_q` belong to the corresponding two transition pairs listed above.

#### Proof

The preceding row-space calculation is necessary and sufficient. ∎

### Corollary 4.2 — local split or global support

If none of the four interlacement configurations occurs, every full cocycle extension compatible with the cap residue must use a transition at some vertex outside `\{p,q\}`.

Thus absence of a local twin/pendant split forces a genuinely global cocycle-support certificate.

## 5. Direct two-element circuits

The residue itself may still be a two-element **circuit**, i.e. the two selected transition columns may be equal.

Using

$$
\phi_v=e_v,
\qquad
\chi_v=A_v,
\qquad
\psi_v=e_v+A_v,
$$

one obtains the complete list.

### Theorem 5.1 — parallel cap-transition classification

For distinct vertices `p,q`, two transition columns are equal only in the following cases:

1. 
   $$
   \phi_p=\chi_q
   \quad\Longleftrightarrow\quad
   N_G(q)=\{p\};
   $$
2. 
   $$
   \chi_p=\phi_q
   \quad\Longleftrightarrow\quad
   N_G(p)=\{q\};
   $$
3. 
   $$
   \chi_p=\chi_q
   \quad\Longleftrightarrow\quad
   p,q\text{ are nonadjacent twins};
   $$
4. 
   $$
   \psi_p=\psi_q
   \quad\Longleftrightarrow\quad
   p,q\text{ are adjacent twins}.
   $$

All other equalities between columns from different vertex triples are impossible.

#### Proof

Compare the standard basis and adjacency columns coordinatewise.

For example, `\chi_p=\chi_q` means `A_p=A_q`. Looking at coordinates `p,q` forces nonadjacency, and all outside coordinates give equal neighbourhoods. Similarly,

$$
\psi_p=\psi_q
\Longleftrightarrow
A_p+A_q=e_p+e_q,
$$

which forces adjacency and equal outside neighbourhoods.

The mixed equalities `\phi_p=\chi_q` and `\chi_p=\phi_q` say that one adjacency column is the single basis vector of the other vertex. Every equality involving `\phi_p=\phi_q`, `\phi_p=\psi_q`, `\chi_p=\psi_q`, or their reverses contradicts one of the diagonal coordinates. ∎

### Corollary 5.2

The two-transition cap residue is a direct `2`-circuit only in a twin/pendant interlacement configuration. Otherwise it is independent.

## 6. Invariance and interpretation

The `\phi,\chi,\psi` names depend on the Euler system, but the following alternatives are matroid-invariant:

- the residue is a two-element circuit;
- a cocycle supported on the two cap triples and containing the residue exists;
- every compatible cocycle completion leaves the cap triples.

Changing the Euler system applies the standard compatible isomorphism of transition triples and transforms the listed interlacement configurations accordingly.

Twin and pendant vertices are classical low-connectivity signatures in interlacement/isotropic theory. Translating them into a composition-safe connected sum, balanced mutation, or terminal-even separator in `\Gamma_g` remains a separate physical theorem.

## 7. Boolean formula for the selected residue transitions

At one cap edge `z`, the scalar transition choice is an affine bit

$$
a_z:\Lambda_g\to\mathbf F_2,
$$

constant in the aligned case and nonconstant affine in the crossed case.

Let

$$
b_z(\phi)
$$

be the cap-inclusion bit in the touch closure. If cross transition `1` is selected when `a_z=1`, then the residue transition bit is

$$
\boxed{
r_z
=
\sum_{\phi\in\Lambda_g}
 b_z(\phi)a_z(\phi).
}
$$

Because

$$
\sum_\phi b_z(\phi)=\Omega=1,
$$

the other cross-transition coefficient is `1+r_z`. Thus exactly one cross transition remains.

This formula separates:

- the non-affine quadratic coefficient `\Omega` of the terminal side word;
- the affine endpoint-selector data at the physical cap;
- the resulting concrete cap transition.

It is a possible comparison coordinate for the future DDD map, but it does not identify the sheet-coordinate and support-label symmetry groups.

## 8. Updated frontier

The bounded residue now gives three exact cases.

1. **Parallel residue.**  `R` is a two-circuit; a low-order interlacement split is visible immediately.
2. **Locally cocycle-completable residue.**  A four-element cocycle supported on the two cap triples exists; again the cap vertices have twin/pendant structure.
3. **Globally completed residue.**  Every full cocycle completion uses other vertex triples. The support outside the caps is the next decomposition certificate to analyse and project to `\Gamma_g`.

The next theorem should show that the third case yields either:

- a terminal-even separator or transition two-sum;
- an alternate route breaking route-lock;
- or the physical DDD support-label class.

## 9. Reliability boundary

Proved here:

- even vertex-triple parity of every full transition-matroid cocycle;
- impossibility of the bare cap residue being a cocycle;
- complete IAS classification of cocycles supported on the two cap triples;
- complete classification of direct two-element cap circuits;
- Boolean correlation formula for the selected cap transitions.

Not proved here:

- physical separator or gluing consequences of the twin/pendant cases;
- existence or uniqueness of a minimal global cocycle completion;
- projection of a global completion to `\Gamma_g`;
- comparison with the DDD support-label cocycle;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, DOI, or merge status is implied.
