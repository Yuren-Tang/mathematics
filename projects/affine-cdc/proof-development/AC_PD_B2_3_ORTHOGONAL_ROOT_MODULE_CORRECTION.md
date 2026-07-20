# AC-PD-B2.3 — correction of the universal orthogonal root-module claim

**Proof-development state:** `COMPLETE-DRAFT / MATHEMATICAL-CORRECTION`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Affected recovered packet:** `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md` at `research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`  
**Affected integrated chapter:** `five-support/equivalent-formulations-and-proof-families.md`, universal orthogonal hierarchy discussion  
**Depends on:** B1.1 and elementary quadratic linear algebra  
**Immediate consumers:** B2 orthogonal hierarchy; B3 target geometry; future Curator repair  
**External mathematical inputs:** none

## 0. Correction summary

The recovered packet claims a rank-free construction in

$$
V=\Gamma\oplus\Gamma^*,
\qquad
\dim V=2r,
$$

encoding all unordered pairs of the $2^r$ points of $\Gamma=\mathbf F_2^r$ as anisotropic roots and preserving the triangle relation.

This claim is false for every $r\geq4$.

There are two independent defects.

1. The displayed formula
   $$
   d_h(a)=([a],\operatorname{ev}_a)
   $$
   is not type-correct: a vector $a\in\Gamma$ canonically defines an evaluation element of $\Gamma^{**}$, not a functional in $\Gamma^*$. No canonical map $\Gamma\to\Gamma^*$ exists without additional structure.
2. More decisively, no alternative construction in dimension $2r$ can satisfy the required additive triangle law once $r\geq4$. A sharp dimension lower bound is $2^r-2$.

The correct universal additive root module is the deleted permutation module of dimension $2^r-2$. The exceptional equality

$$
2^3-2=2\cdot3=6
$$

explains why the rank-three eight-support theory fits $O^+(6,2)$; it does not extend as a $2r$-dimensional rank-free hierarchy.

## 1. Abstract additive root representation

Let $I$ be a finite set of cardinality $q\geq3$. An **additive root representation** of the complete graph on $I$ in a quadratic space $(V,Q)$ is a map

$$
r:\binom I2\longrightarrow V
$$

such that:

1. every root is anisotropic:
   $$
   Q(r_{ab})=1;
   $$
2. every target triangle satisfies
   $$
   r_{ab}+r_{bc}+r_{ca}=0
   $$
   for distinct $a,b,c\in I$.

This is exactly the structure needed to turn local $K_I$ triangles into vector-flow conservation by edgewise root addition.

## 2. Triangle relations force point potentials

Fix a base point $0\in I$ and define

$$
p_0=0,
\qquad
p_a=r_{0a}\quad(a\ne0).
$$

### Lemma 2.1

For every distinct $a,b\in I$,

$$
\boxed{r_{ab}=p_a+p_b.}
$$

### Proof

Apply the triangle relation to $0,a,b$:

$$
r_{0a}+r_{ab}+r_{b0}=0.
$$

Since the edge is unordered, $r_{b0}=r_{0b}$, giving the formula. $\square$

Thus every additive root representation is a difference representation of $q$ point potentials.

## 3. Sharp dimension lower bound

Let $B$ be the polar form of $Q$.

For $a\ne0$,

$$
Q(p_a)=Q(r_{0a})=1.
$$

For distinct nonzero $a,b$,

$$
1=Q(r_{ab})=Q(p_a+p_b)
=Q(p_a)+Q(p_b)+B(p_a,p_b)
=B(p_a,p_b).
$$

Therefore the Gram matrix of the $q-1$ vectors $(p_a)_{a\ne0}$ is

$$
A=J+I,
$$

with zero diagonal and one in every off-diagonal entry.

### Lemma 3.1 — rank of the off-diagonal matrix

If $q$ is even, then $q-1$ is odd and

$$
\operatorname{rank}_{\mathbf F_2}(J+I)=q-2.
$$

### Proof

Let $n=q-1$ and let $x\in\mathbf F_2^n$. Then

$$
(J+I)x=(\sum_i x_i)\mathbf1+x.
$$

If this is zero, then $x=(\sum_i x_i)\mathbf1$. The zero vector is a solution. Since $n$ is odd, the all-one vector also satisfies the equation, and these are the only possibilities. Thus the kernel is one-dimensional and the rank is $n-1=q-2$. $\square$

### Theorem 3.2 — additive root dimension bound

For even $q$, every additive root representation of $K_q$ satisfies

$$
\boxed{\dim V\geq q-2.}
$$

### Proof

The rank of the Gram matrix of vectors in $V$ cannot exceed $\dim V$. Lemma 3.1 gives Gram rank $q-2$. $\square$

### Corollary 3.3 — impossibility of the claimed $2r$ hierarchy

For $q=2^r$, a $2r$-dimensional additive root representation can exist only if

$$
2r\geq2^r-2.
$$

This fails for every $r\geq4$; already

$$
8<14
$$

when $r=4$.

Hence the recovered rank-free theorem is mathematically impossible, independent of its displayed formula.

## 4. The correct deleted permutation module

Let $I$ have even cardinality $q=2^r$ with $r\geq2$. In the permutation space $\mathbf F_2^I$, define the even-weight subspace

$$
E_I=
\left\{z:\sum_{i\in I}z_i=0\right\}.
$$

The all-one word $\mathbf1_I$ belongs to $E_I$. Put

$$
\overline E_I=E_I/\langle\mathbf1_I\rangle.
$$

Then

$$
\dim\overline E_I=q-2.
$$

For an even-weight representative $z$, define

$$
q_I(z)=\frac{\operatorname{wt}(z)}2\pmod2.
$$

### Lemma 4.1 — descent of the quadratic form

The function $q_I$ descends to a well-defined quadratic form on $\overline E_I$.

### Proof

The polar form on $E_I$ is the standard dot product. The all-one word lies in its radical because every $z\in E_I$ has even weight.

Replacing $z$ by $z+\mathbf1_I$ complements its support, so

$$
q_I(z+\mathbf1_I)-q_I(z)
=\frac q2-\operatorname{wt}(z)\pmod2.
$$

Here $q/2=2^{r-1}$ is even for $r\geq2$, and $\operatorname{wt}(z)$ is even. Thus the difference is zero. $\square$

### Proposition 4.2 — canonical complete-graph roots

For distinct $a,b\in I$, let

$$
\rho_{ab}=[\varepsilon_a+\varepsilon_b]
\in\overline E_I.
$$

Then:

1. $q_I(\rho_{ab})=1$;
2. for distinct $a,b,c$,
   $$
   \rho_{ab}+\rho_{bc}+\rho_{ca}=0;
   $$
3. the roots span $\overline E_I$;
4. the dimension $q-2$ attains Theorem 3.2's lower bound.

### Proof

The representative has weight two, proving anisotropy. The triangle sum cancels every coordinate twice. Differences of basis vectors span the even-weight space, and quotienting by $\mathbf1_I$ gives the stated span. $\square$

This is the correct universal additive root module for the complete graph on $2^r$ support indices.

## 5. Exceptional rank three

When $q=8$,

$$
\dim\overline E_I=6=2r.
$$

The quadratic space is the familiar plus-type six-space $O^+(6,2)$. It has exactly twenty-eight anisotropic vectors, equal to

$$
\binom82=28,
$$

so the complete-graph roots exhaust the anisotropic orbit. This is the exceptional orthogonal realization used by the eight-support AffineCDC core.

When $q=16$, the correct additive module has dimension fourteen, not eight. The root set has $120$ elements but no eight-dimensional quadratic space can carry it with the triangle-addition law.

Thus the valid hierarchy is:

$$
\text{rank-three eight supports}
\longleftrightarrow
O^+(6,2)\text{ anisotropic roots},
$$

not

$$
2^r\text{ supports}
\longleftrightarrow
O^+(2r,2)\text{ anisotropic roots}
$$

for arbitrary $r$.

## 6. Relation to the five-support target

For five support indices, the even-weight space

$$
H_5=\{z\in\mathbf F_2^5:\sum z_i=0\}
$$

already has dimension four because the all-one word has odd weight and does not lie in it. Its ten weight-two roots exhaust the anisotropic orbit of $O^-(4,2)$. This is the B2.1 five-support mother space.

The eight-to-five problem is therefore the exceptional orthogonal reduction

$$
O^+(6,2)\text{ root flow}
\rightsquigarrow
O^-(4,2)\text{ root flow}.
$$

It is not the first step of a universal $O^+(2r,2)$ tower.

## 7. What remains valid from the affected packet

The packet's broad conceptual lesson remains useful in corrected form:

- support pairs are naturally root vectors;
- local triangle compatibility is additive root conservation;
- orthogonal geometry organizes the exceptional eight- and five-support targets;
- quotient and residue constructions can reduce rank when their kernel and lift data are explicit.

The following claims must be withdrawn or rewritten:

1. the type-incorrect formula $d_h(a)=([a],\operatorname{ev}_a)$;
2. the canonical $2r$-dimensional universal construction;
3. the rank-free automatic affine compatibility theorem based on that construction;
4. the assertion that the rank-three core is merely the first case of this $2r$ hierarchy.

Any separate rank-reduction theorem in a genuine orthogonal space must be re-audited independently; it cannot cite the false universal construction as its parent.

## 8. Consequences for the active proof DAG

- B2.3 is closed as a correction unit, not as confirmation of the integrated hierarchy.
- The valid rank-three $O^+(6,2)$ and rank-four $O^-(4,2)$ targets remain intact.
- B2's remaining orthogonal work must concern the specific exceptional reduction $6\to4$, singular quotients, residues, and retained lift data.
- No new mathematical invention is required to repair the false universal claim; the correct lower bound and permutation module are now proved.
- Any hoped-for higher-rank small-dimensional analogue is a new research question and must not be treated as an existing theorem.

## 9. Curator correction requirement

Before Programme B orthogonal material is promoted:

1. remove the universal $\Gamma\oplus\Gamma^*$ theorem from the active theorem layer;
2. replace it with the deleted permutation module and dimension lower bound;
3. mark rank three as exceptional;
4. reclassify later orthogonal-rank-reduction packets by their actual fixed dimension and hypotheses;
5. preserve the affected packet only as historical provenance with a superseded/false-theorem warning.

## 10. Completion assessment

`AC-PD-B2.3` is `COMPLETE-DRAFT / MATHEMATICAL-CORRECTION`. The next active unit is B2.4: audit the stress and Fourier duals as solvability criteria for fixed root-lift equations, proving their equivalence to the primal obstruction while determining exactly which transforms preserve the full witness and which retain only obstruction data.