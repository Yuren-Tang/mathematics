# The Type H local-to-global holonomy stack

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level reformulation and complete classification of zero-norm root-lifting obstructions for the genuine rainbow switch flow; strict graph reduction remains open  
**Parents:** `FIVE_CDC_RAINBOW_SWITCH_FLOW_TAIT_RESOLUTION_V1.md`, `FIVE_CDC_TYPE_H_TAIT_ESCAPE_V1.md`, `FIVE_CDC_INTERIOR_AFFINE_HOLONOMY_NORM_V1.md`

## 1. Purpose

The Type H Tait-escape theorem removes every zero-norm rainbow loop whose root-fibre lifting problem has a global solution.  The remaining failures were previously listed as:

- a zero edge;
- an all-zero cubic vertex;
- an odd component of a matching-complement degree-two system.

These are not three unrelated graph configurations.  They are the three local-to-global failure levels of one finite root-fibre system:

1. an empty edge fibre;
2. a nonempty collection of edge fibres with an empty vertex relation;
3. locally nonempty vertex relations with nontrivial component holonomy and no global section.

Together with the earlier nonzero ambient norm defect, the complete Type H residual mechanism is therefore a two-level holonomy stack:

\[
\boxed{
\text{ambient affine holonomy}
\quad\text{over}\quad
\text{root-fibre local-system holonomy}.
}
\]

If both levels are trivial and every local fibre is nonempty, a Tait resolution exists and the boundary profile escapes.  Thus a minimal Type H kernel must carry a genuine obstruction at one of these levels.

No strict decomposition or five-cycle double cover theorem is claimed.

## 2. The root-fibre constraint system

Fix a lifted genuine rainbow loop with support monodromy `pi`, switch flow

\[
t=t_\gamma,
\]

and assume its ambient norm defect vanishes.  Let

\[
Q_\pi=1+\pi.
\]

For every edge `e`, define the finite root fibre

\[
\boxed{
\mathcal R_e
=
\{r\in R_5:Q_\pi r=t(e)\}.
}
\]

For every internal cubic vertex `v`, incident with `e_1,e_2,e_3`, define the local conservation relation

\[
\boxed{
\mathcal V_v
=
\left\{
(r_1,r_2,r_3)\in
\mathcal R_{e_1}\times\mathcal R_{e_2}\times\mathcal R_{e_3}:
 r_1+r_2+r_3=0
\right\}.
}
\]

Terminal edges carry the root values prescribed by the initial cover.

### Theorem 2.1 — root lifts are global sections

A root-admissible linearization of the zero-norm loop is exactly a choice

\[
r(e)\in\mathcal R_e
\]

for every edge such that:

- `(r(e_1),r(e_2),r(e_3))\in\mathcal V_v` at every internal vertex;
- the prescribed terminal values are respected.

#### Proof

The quotient-flow lifting theorem identifies root-admissible linearization with a root-valued flow satisfying

\[
Q_\pi r=t.
\]

The edge equation is precisely membership in `R_e`; flow conservation is precisely membership in each `V_v`. ∎

This finite system is called the **root-fibre section problem** of the lifted loop.

## 3. Full-rank monodromies: empty edge fibres are complete

Let `pi` have support cycle type `4` or `5`.  On the genuine switch plane `W`, the root-fibre table is:

\[
\begin{array}{c|c|c}
\text{type}&t=0&t\ne0\\
\hline
5&0&1\\
4&0&2.
\end{array}
\]

Hence

\[
\mathcal R_e=\varnothing
\quad\Longleftrightarrow\quad
 t(e)=0.
\]

### Theorem 3.1 — full-rank local-to-global collapse

For support types `4` and `5`, the root-fibre system has a global section if and only if every edge fibre is nonempty.

#### Proof

This is the full-rank part of the Tait-resolution theorem.  For type `5`, the nonzero fibres are singletons and form the unique root triangle at every cubic vertex.  For type `4`, each fibre is a two-point affine line; after choosing a root-valued linear section, the remaining choices form a binary flow extension, and the prescribed terminal imbalance has even total and therefore extends on the connected four-pole. ∎

Thus the only zero-norm root-lifting obstruction in these types is the first local level:

\[
\boxed{
\text{empty edge fibre}
\iff
	ext{zero switch-flow edge}.
}
\]

## 4. Rank-one monodromies: matching and transport

Let `pi` have type `3+2` or `2+2`.  The genuine switch flow takes values

\[
t(e)\in\{0,\kappa\}.
\]

The edge fibres are nonempty for both values.  Cubic conservation of `t` permits only

\[
(0,0,0)
\qquad\text{or}\qquad
(0,\kappa,\kappa).
\]

### Proposition 4.1 — the all-zero local relation is empty

If all three incident switch-flow values are zero, then

\[
\boxed{
\mathcal V_v=\varnothing.
}
\]

#### Proof

For type `3+2`, the zero fibre is a singleton `\{a\}` with `a\ne0`; the only triple sums to `a`.

For type `2+2`, the zero fibre is `\{a,b\}` with `a,b` independent.  No sum of three choices from `\{a,b\}` is zero. ∎

Assume every vertex has pattern `(0,kappa,kappa)`.  Then

\[
M=t^{-1}(0)
\]

is a perfect matching and

\[
F=t^{-1}(\kappa)
\]

is degree two at every internal vertex.  Its components are closed cycles and one terminal path.

The local vertex relation transports root choices along each component of `F`.

## 5. Type `3+2`: deterministic two-sheeted holonomy

For type `3+2`, write

\[
\mathcal R_0=\{a\},
\qquad
\mathcal R_\kappa=\{r,r+a\}.
\]

At a vertex with matching root `a`, conservation forces the two incident `F` roots to differ by `a`:

\[
s_{\mathrm{out}}=s_{\mathrm{in}}+a.
\]

Thus every vertex acts on the two-point fibre `R_kappa` by the fixed-point-free involution

\[
\tau(s)=s+a.
\]

### Theorem 5.1 — component holonomy

On an `F` component with `n` internal vertices, the transport holonomy is

\[
\boxed{
\tau^n(s)=s+n a.
}
\]

A closed component has a section exactly when its holonomy has a fixed point, equivalently when `n` is even.  The terminal path has equal prescribed endpoint roots and is compatible exactly when `n` is even.

Thus an odd component is precisely a nontrivial two-sheeted root-fibre holonomy.

## 6. Type `2+2`: affine correspondence holonomy

For type `2+2`, write

\[
\mathcal R_0=\{a,b\},
\]

where `a,b` are independent.  At a vertex, after choosing the matching root `m\in\{a,b\}`, conservation transports an incoming `F` root by

\[
s_{\mathrm{out}}=s_{\mathrm{in}}+m.
\]

The one-step transport is therefore the affine correspondence generated by translations by `a` and `b`.

On a component with `n` internal vertices, the possible total translations are

\[
\boxed{
\mathcal H_n
=
\left\{
 m_1+\cdots+m_n:m_i\in\{a,b\}
\right\}.
}
\]

### Theorem 6.1 — parity of the correspondence holonomy

\[
0\in\mathcal H_n
\quad\Longleftrightarrow\quad
n\text{ is even}.
\]

#### Proof

If `n` is even, choose every `m_i=a`; the sum is zero.

If `n` is odd, the numbers of `a` and `b` choices have opposite parity.  The sum is therefore either `a` or `b`, never zero. ∎

A closed component has a section exactly when the identity translation belongs to its holonomy correspondence.  The equal prescribed roots at the two endpoints of the terminal path give the same criterion.

Hence an odd component is again exactly nontrivial root-fibre holonomy, now for a two-generator affine correspondence rather than one deterministic involution.

## 7. Complete zero-norm local-to-global trichotomy

### Theorem 7.1 — zero-norm obstruction stack

For every genuine zero-norm lifted Type H rainbow loop, exactly one of the following occurs:

1. **empty edge fibre:** support type `4` or `5` and `t(e)=0` for some edge;
2. **empty vertex relation:** support type `3+2` or `2+2` and some cubic vertex is all-zero under `t`;
3. **nontrivial component holonomy:** every local relation is nonempty, but some matching-complement component has odd order;
4. **global section:** a root lift exists, equivalently the switch flow has a Tait resolution.

In case `4`, the Type H Tait-escape theorem forces boundary-profile expansion.  Therefore a minimal Type H kernel can realize only cases `1`--`3`.

#### Proof

The full-rank classification is Theorem 3.1.  The rank-one local classification is Proposition 4.1.  If all rank-one local relations are nonempty, Sections 5 and 6 show that a global section exists exactly when every component holonomy contains the identity, equivalently when every component is even.  The Tait-resolution theorem identifies this global section with root linearization, and the Tait-escape theorem eliminates it from a minimal kernel. ∎

## 8. Add the ambient level

Before the root-fibre section problem can be posed, the interior affine norm must vanish.

For an affine lifted loop

\[
A(u)=\pi u+z,
\]

the norm defect

\[
d=N_\pi z
\]

is the complete ambient affine-conjugacy obstruction.  If `d\ne0`, repeated traversal yields a nontrivial pure interior translation.

Combining this with Theorem 7.1 gives the complete residual Type H stack.

### Theorem 8.1 — two-level Type H obstruction stack

Every lifted rainbow loop in a minimal Type H kernel has at least one of the following:

\[
\boxed{
\begin{array}{ll}
\text{Level A:}&N_\pi z\ne0
\quad\text{(ambient affine holonomy);}
\\[1mm]
\text{Level B1:}&\mathcal R_e=\varnothing
\quad\text{(empty edge fibre);}
\\[1mm]
\text{Level B2:}&\mathcal V_v=\varnothing
\quad\text{(empty vertex relation);}
\\[1mm]
\text{Level B3:}&\operatorname{Hol}(C)\not\ni 1
\quad\text{(component root-fibre holonomy).}
\end{array}
}
\]

If none occurs, a Tait resolution exists and forces profile escape.

This is a complete classification of the residual **mechanism types**, not an elimination of them.

## 9. Family-level consequence

A physical rainbow triangle has several lifted loops, obtained by selecting terminal path components and repeated trace roles.  The individual obstruction stack applies to every lift.

Thus in a minimal Type H kernel:

\[
\boxed{
\text{every lifted loop must carry an obstruction at Level A or Level B.}
}
\]

The choices are correlated because all lifts arise from the same three complementary support-pair symmetric differences.  The next global theorem must exploit this family correlation:

\[
\boxed{
\begin{array}{c}
\text{some lift has no obstruction}
\Rightarrow
\text{Tait resolution and profile escape};
\\[1mm]
\text{all lifts obstructed}
\Rightarrow
\text{common path-overlap, odd-ring, or translation structure}.
\end{array}
}
\]

This is the correct composition-level target.  Enumerating more isolated lifted loops cannot establish it.

## 10. Updated global picture

The cyclic four-cut branch now reads

\[
\boxed{
\begin{array}{c}
\text{minimal counterexample with cyclic four-cut}
\\ \downarrow
\\
\text{unique deterministic routing policy}
\\ \downarrow
\\
\begin{cases}
\text{Type T: acyclic unique linkage},
\\
\text{Type H: rainbow lift family}.
\end{cases}
\\ \downarrow
\\
\begin{cases}
\text{Type T}
&\Rightarrow\text{nested linkage / replacement target},
\\
\text{Type H}
&\Rightarrow
\text{ambient or root-fibre holonomy stack}.
\end{cases}
\\ \downarrow
\\
\text{common strict progress theorem:
replacement, smaller separator, or orbit escape.}
\end{array}
}
\]

The two branches are not yet eliminated, but their residual information has become compositional:

- Type T stores uniqueness of terminal linkage;
- Type H stores failure of a finite local system to admit a section.

Both should be expressible as transfer data of a bounded-boundary fragment.

## 11. Trust boundary

The edge-fibre and vertex-relation formulation, the type `3+2` deterministic holonomy, the type `2+2` correspondence parity theorem, and the complete zero-norm trichotomy are theorem-level consequences of the established root-fibre table.

The exact physical lift families and their monodromy counts are finite computations in the private verifiers.

Still open:

- proving that all-obstructed lift families share one decomposable path structure;
- converting nonzero ambient translation into profile escape;
- converting odd component holonomy into a smaller separator or bounded replacement;
- integrating the local-system transfer data with the opposite shore under gluing;
- Type T decomposition;
- the five-cycle double cover conjecture.

## 12. Next exact tasks

1. Construct the obstruction signature of an entire lifted-loop family, not one loop.
2. Express changes between two component choices as a cycle-supported coboundary in the root-fibre system.
3. Prove that simultaneous odd holonomy for all choices forces a common odd ring or serial path strip.
4. Determine whether the resulting transfer signature has finite index under four-terminal gluing.
5. Seek the same transfer-signature formalism for Type T unique linkage.
