# Quartic terminal nucleus and recursive peeling

## 1. Purpose

A quartic witness design on a set `X`, with

$$
|X|=4k+1,
$$

consists of four near-resolutions

$$
\mathcal R_i
\qquad(i\in I),
\qquad |I|=4,
$$

where `\mathcal R_i` partitions `X\setminus\{e_i\}` into `k` four-element blocks, the omitted points `e_i` are distinct, and all `4k` block vectors form a basis of the even-weight space

$$
E_X=
\left\{x\in\mathbf F_2^X:\sum_{u\in X}x_u=0\right\}.
$$

Abstract quartic designs exist for every `k`. This chapter identifies their canonical four-dimensional nucleus and proves the exact split-or-peel recursion.

The four indices are the scalar sheets

$$
I=\Lambda_g\cong AG(2,2).
$$

Their natural coordinate symmetry is

$$
AGL(2,2)\cong S_4.
$$

No distinguished `D_8` subgroup of this sheet symmetry is produced merely by the physical terminal route `12\mid34`; terminal labels and sheet labels are different four-point sets. The `D_8` stabiliser of a physical DDD one-factor belongs to a separate support-label geometry and requires an additional comparison map.

## 2. Quadratic structure

For `x\in E_X`, define

$$
q_X(x)=\frac{|x|}{2}\pmod2.
$$

Its polar form is

$$
b_X(x,y)=|x\cap y|\pmod2.
$$

Because `|X|` is odd,

$$
E_X^\perp=\langle1_X\rangle,
\qquad
1_X\notin E_X,
$$

so `(E_X,q_X)` is nondegenerate of dimension `4k`.

## 3. The terminal nucleus

For each sheet put

$$
s_i=\sum_{B\in\mathcal R_i}1_B.
$$

Since `\mathcal R_i` partitions `X\setminus\{e_i\}`,

$$
\boxed{s_i=1_X+1_{e_i}.}
$$

### Theorem 3.1 — canonical minus-type nucleus

The four vectors `s_i` are linearly independent and span a nondegenerate four-dimensional minus-type quadratic subspace

$$
S=\langle s_i:i\in I\rangle\le E_X.
$$

More precisely,

$$
q_X(s_i)=0,
\qquad
b_X(s_i,s_j)=1
\quad(i\ne j).
$$

#### Proof

Every `s_i` has weight `4k`, hence `q_X(s_i)=2k=0` in `\mathbf F_2`. For distinct `i,j`,

$$
(1_X+e_i)\cdot(1_X+e_j)
=|X|+1+1
=1.
$$

Thus the Gram matrix in the ordered basis `(s_i)` is

$$
K=
\begin{pmatrix}
0&1&1&1\\
1&0&1&1\\
1&1&0&1\\
1&1&1&0
\end{pmatrix}.
$$

If `Ka=0` and `A=\sum_i a_i`, then the `i`-th equation gives `a_i=A` for every `i`; summing gives `A=4A=0`, so `a=0`. Hence `K` is nonsingular.

For a sum of `m` distinct basis vectors the quadratic value is `\binom m2` modulo two. The nonzero singular vectors are therefore the four `s_i` and

$$
s_\infty=\sum_{i\in I}s_i.
$$

There are five nonzero singular vectors and ten anisotropic vectors, which is the four-dimensional minus type. ∎

Since `S` is nondegenerate,

$$
\boxed{E_X=S\perp S^\perp.}
$$

## 4. Intrinsic `E_5/K_5` geometry

The five nonzero singular vectors

$$
\{s_i:i\in I\}\cup\{s_\infty\}
$$

may be regarded as the five vertices of a `K_5`. Their ten pairwise sums are exactly the anisotropic vectors of `S`.

For `i\ne j`,

$$
\boxed{s_i+s_j=e_i+e_j.}
$$

The remaining four roots are

$$
s_i+s_\infty
=1_X+\sum_{j\ne i}e_j.
$$

Thus every quartic design contains a canonical copy of the same minus-type root geometry that defines five-support flows. This is an incidence-coefficient statement, not yet a physical `E_5` flow on the original four-pole.

## 5. Correct sheet symmetry

Every permutation of the four sheets permutes the basis vectors `s_i` and fixes `s_\infty`. Hence

$$
S_4
=
\operatorname{Stab}_{O^-(S)}(s_\infty)
$$

acts on the nucleus.

The affine structure on `I=\Lambda_g` has full automorphism group

$$
AGL(2,2)\cong S_4,
$$

so the nucleus and its labelling are canonical under the full sheet-coordinate group.

### Reliability correction

The terminal route `12\mid34` is a matching on the physical terminal set. It does not, without an additional theorem, select a matching or parallel class on the sheet set `\Lambda_g`. Consequently this chapter does not define a canonical `D_8` subgroup of the sheet symmetry.

The physical DDD group

$$
\operatorname{Stab}_{S_5}(\text{one-factor})\cong D_8
$$

acts in support-label geometry. Identifying it with a subgroup acting on the quartic nucleus remains an open comparison problem.

## 6. Curvature carrier

For a word

$$
w=(w_i)_{i\in I}\in\mathbf F_2^I,
$$

there is a unique vector `\Psi(w)\in S` satisfying

$$
b_X(\Psi(w),s_i)=w_i.
$$

If `W=\sum_iw_i`, then `K^{-1}=K`, so

$$
\boxed{
\Psi(w)=\sum_i(W+w_i)s_i.
}
$$

The affine functions on `AG(2,2)` are exactly the even-weight four-bit words. Moreover,

$$
b_X\left(s_\infty,\sum_i a_is_i\right)=\sum_i a_i.
$$

Hence

$$
\boxed{
\Psi\bigl(\operatorname{Aff}(AG(2,2),\mathbf F_2)\bigr)
=s_\infty^\perp.
}
$$

### Theorem 6.1 — one-dimensional curvature quotient

There is a canonical `S_4`-equivariant identification

$$
\boxed{
\mathbf F_2^I/
\operatorname{Aff}(AG(2,2),\mathbf F_2)
\cong
S/s_\infty^\perp.
}
$$

An odd terminal-side word represents the unique nonzero element. The full sheet symmetry acts trivially on this one-dimensional quotient.

This identifies the coefficient carrier of curvature. It does not identify it with

$$
H^1(D_8,E_5)\cong\mathbf F_2;
$$

that comparison still requires a map between sheet-coordinate geometry and the physical DDD support-label geometry.

## 7. Projection of individual blocks

Let

$$
\operatorname{pr}_S:E_X\to S
$$

be orthogonal projection. For `B\in\mathcal R_i`, define

$$
J(B)=\{j\in I\setminus\{i\}:e_j\in B\}.
$$

Since

$$
b_X(1_B,s_j)=1_{j\in J(B)},
$$

one has

$$
\operatorname{pr}_S(1_B)=\Psi(1_{J(B)}).
$$

### Theorem 7.1 — terminal-block projection table

$$
\begin{array}{c|c}
J(B)&\operatorname{pr}_S(1_B)\\
\hline
\varnothing&0\\
\{j\}&s_\infty+s_j\\
\{j,\ell\}&s_j+s_\ell\\
I\setminus\{i\}&s_i.
\end{array}
$$

The middle two cases are anisotropic roots; the last is the singular sheet vector.

Because the blocks of `\mathcal R_i` partition the three points `e_j` with `j\ne i`, each sheet has exactly one terminal-distribution type:

1. concentrated `3`;
2. split `2+1`;
3. fully split `1+1+1`.

## 8. Concentrated peeling

Assume every sheet is concentrated. Let `D_i\in\mathcal R_i` be the block containing all three `e_j` with `j\ne i`. Then

$$
D_i=\{e_j:j\ne i\}\cup\{y_i\}
$$

for some

$$
y_i\in Y:=X\setminus\{e_i:i\in I\}.
$$

Put

$$
\mathcal R_i'=\mathcal R_i\setminus\{D_i\}.
$$

### Theorem 8.1 — strict nucleus peel

For `k\ge2`:

1. the four `y_i` are distinct;
2. `\mathcal R_i'` partitions `Y\setminus\{y_i\}` into `k-1` four-element blocks;
3. the `4(k-1)` residual block vectors form a basis of `E_Y`;
4. inside `E_X` they form a basis of `S^\perp`;
5. therefore `(Y,(\mathcal R_i'),(y_i))` is a quartic witness design of level `k-1`.

#### Proof

Removing `D_i` from the partition of `X\setminus\{e_i\}` leaves exactly `Y\setminus\{y_i\}`.

If `y_i=y_j` for distinct `i,j`, then the sums of all residual blocks in sheets `i,j` are both `1_Y+y_i`, giving a nontrivial relation among the original block basis. Hence the `y_i` are distinct.

Every residual block contains none of the four old omitted points, so its nucleus projection is zero. Thus all residual block vectors lie in `S^\perp`. They are independent and their number is

$$
4(k-1)=\dim S^\perp=\dim E_Y,
$$

so they are bases of both spaces. ∎

The distinguished block identity is

$$
\boxed{
1_{D_i}+s_i
=1_Y+1_{y_i}
=\sum_{B\in\mathcal R_i'}1_B.
}
$$

For `k=1`, the five-point nucleus is the recursion base.

## 9. Inverse extension

### Theorem 9.1 — canonical concentrated extension

Given a level-`k-1` quartic design `(Y,(\mathcal R_i'),(y_i))`, adjoin four new points `e_i` and define

$$
D_i=\{e_j:j\ne i\}\cup\{y_i\},
\qquad
\mathcal R_i=\mathcal R_i'\cup\{D_i\}.
$$

Then `(X,(\mathcal R_i),(e_i))` is a concentrated level-`k` quartic design.

#### Proof

The partition property is immediate. In a putative linear relation, the four new coordinates `e_j` give the nonsingular `K` system on the coefficients of the `D_i`, forcing all of them to zero. Residual independence then forces all remaining coefficients to zero. The `4k` even block vectors therefore form a basis of `E_X`. ∎

## 10. Split-or-peel dichotomy

### Corollary 10.1

Every quartic witness design satisfies exactly one of:

1. **root-exposed split:** some sheet has type `2+1` or `1+1+1`, exposing anisotropic root projections;
2. **nucleus recursion:** every sheet is concentrated; the design is the five-point base when `k=1`, and peels to level `k-1` when `k\ge2`.

Thus every abstract unbounded quartic design is obtained by iterating canonical `S_4`-equivariant minus-type nucleus extensions until reaching either the five-point nucleus or a first split layer.

## 11. Updated physical frontier

The coefficient theorem has two branches.

- A split layer must be lifted to a bounded physical defect factor, transition pair, separator, or four-pole transfer.
- A concentrated layer must descend through the physical transition quotient, or its failure must expose a bounded exceptional interface.

Any identification of that exceptional interface with DDD must additionally compare:

1. the sheet-coordinate `S_4` geometry of this nucleus;
2. the terminal-route coordinate group on the four semiedges;
3. the support-label `D_8` stabiliser of the DDD one-factor.

No such comparison is assumed here.

## 12. Reliability boundary

Proved here:

- the canonical nondegenerate minus-type four-space;
- its five singular points and ten anisotropic roots;
- full `S_4\cong AGL(2,2)` sheet-coordinate symmetry;
- the one-dimensional curvature carrier;
- the block projection table;
- concentrated peeling and inverse extension;
- the split-or-peel dichotomy.

Corrected here:

- the physical route matching does not by itself select a `D_8` subgroup on the sheet index set.

Not proved here:

- a physical split or peel;
- a canonical map to the DDD support-label cohomology class;
- singleton or two-edge composition;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, DOI, or merge status is implied.
