# Star-expanded Petersen pentagons are the six-turn DDD reflection cores

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `bda5296621fe1702a4ecf915171064a565362525`  
**Parents:**

- `projects/affine-cdc/research/SIX_OUTPUT_FULL_STATE_CYCLE_CORRECTION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_PIVOT_RESOLUTION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_FIVE_CYCLE_REFLECTION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_STAR_REFLECTION_V1.md`;
- `projects/affine-cdc/research/DDD_REFLECTION_SUBSTITUTION_V1.md`.

**Status:** exact structural and support-monodromy theorem for the sixty mixed six-cycles in `L(P)`. Every such cycle is one Petersen pentagon with one direct turn expanded through the third state of its pivot star; its total monodromy is the corresponding DDD reflection.  
**Not implied:** physical source realisability of every abstract state cycle, affine translation value, graph replacement, canonical acceptance, Lean verification, or the global five-support theorem.

---

## 1. State-cycle setup

Let

\[
P=KG(5,2)
\]

be the Petersen graph and `L(P)` its line graph. A state vertex of `L(P)` is a Petersen edge

\[
F=\{x,y\}.
\]

For adjacent states `F,G`, let

\[
s=F\cap G
\]

be their transition pivot. Let

\[
i(F)=[5]\setminus\bigcup F
\]

be the omitted support index of the DDD state `F`.

The support transport across one state transition is

\[
\tau(F,G)=(i(F)\ i(G))\in S_5.
\]

For a closed state walk `C`, its full support monodromy is the ordered product of its transition transpositions.

---

## 2. Expanding one pentagon turn

Let

\[
C_5=(F_0,F_2,F_3,F_4,F_5,F_0)
\]

be the state five-cycle induced by one Petersen pentagon.

Suppose the direct transition

\[
F_0\longrightarrow F_2
\]

has pivot `s`. Since `P` is cubic, there is a unique third Petersen edge `F_1` incident with `s` and distinct from `F_0,F_2`.

Insert that state:

\[
C_6=(F_0,F_1,F_2,F_3,F_4,F_5,F_0).
\]

This is the **star-expanded pentagon** at the chosen pivot.

### Theorem 2.1 — bijection

There is an `S5`-equivariant bijection

\[
\boxed{
\{\text{star-expanded pentagons in }L(P)\}
\cong
\{(C,v):C\text{ a Petersen five-cycle},\ v\in V(C)\}.
}
\]

Hence there are

\[
12\cdot5=60
\]

such six-cycles, forming one `S5` orbit.

### Proof

The short-cycle correction theorem shows that every mixed six-cycle has cyclic pivot-run pattern

\[
(2,1,1,1,1).
\]

The unique length-two run consists of three consecutive state edges through one cubic Petersen pivot. Removing the middle, third incident edge leaves a simple Petersen pentagon. Conversely the cubic third edge gives a unique insertion at every chosen pentagon pivot. Equivariance is immediate. ∎

---

## 3. Direct turn and expanded detour

Write

\[
a=i(F_0),
\qquad
b=i(F_1),
\qquad
c=i(F_2).
\]

These are the three support indices complementary to the common pivot root `s`.

The direct turn has support transport

\[
d=(a\ c).
\]

The expanded two-transition detour has transport

\[
e=(b\ c)(a\ b).
\]

Define the relative detour element

\[
\sigma=d^{-1}e.
\]

### Lemma 3.1 — detour reflection

\[
\boxed{\sigma=(b\ c).}
\]

Thus the difference between the expanded and direct turns is precisely the single-transposition star reflection at the chosen pivot.

### Proof

In the symmetric group on `{a,b,c}`,

\[
(a\ c)(b\ c)(a\ b)=(b\ c),
\]

with the opposite multiplication convention giving the conjugate orientation form. The resulting transposition is exactly the support monodromy of the local star triangle based at the direct-turn DDD state. ∎

---

## 4. Pentagon rotation times star reflection

Let

\[
\rho=\Pi(C_5)
\]

be the monodromy of the collapsed pentagon, based compatibly with the expanded cycle. The Petersen cycle theorem gives

\[
\rho\text{ of cycle type }4\,1.
\]

Let

\[
\mu=\Pi(C_6)
\]

be the full monodromy of the star-expanded six-cycle.

### Theorem 4.1 — reflection factorisation

\[
\boxed{
\mu=\rho\sigma.
}
\]

Moreover

\[
\boxed{
\sigma\rho\sigma=\rho^{-1},
\qquad
\mu\rho\mu=\rho^{-1}.
}
\]

Consequently both `sigma` and `mu` are reflections in the same DDD stabiliser generated with `rho`.

### Proof

All transitions outside the expanded turn are identical in `C5` and `C6`. Replacing the direct factor `d` by the expanded factor `e=d sigma` multiplies the total based monodromy on the right by `sigma`, giving `mu=rho sigma`.

The local star transposition reverses the cyclic order of the four moved support indices of `rho`; hence `sigma rho sigma=rho^{-1}`. Then

\[
\mu\rho\mu
=(\rho\sigma)\rho(\rho\sigma)
=\rho(\sigma\rho\sigma)\rho\sigma^2
=\rho\rho^{-1}\rho^{-1}\rho
=\rho^{-1}.
\]

Equivalently, `rho sigma` is another reflection in the same dihedral group. ∎

---

## 5. Monodromy type

### Corollary 5.1 — mixed sector type

For every star-expanded pentagon,

\[
\boxed{
\operatorname{type}(\sigma)=2\,1^3,
\qquad
\operatorname{type}(\rho)=4\,1,
\qquad
\operatorname{type}(\mu)=2^2\,1.
}
\]

The total six-cycle monodromy is a double-transposition reflection, not the central half-turn of the DDD rotation subgroup.

### Proof

The first two types are the star-reflection and pentagon theorems. Since `mu=rho sigma` lies in the reflection coset and is not a single transposition, its `S5` cycle type is `2^2 1`. Exact enumeration confirms this for all sixty cycles. ∎

---

## 6. Representative certificate

Take

\[
C_6=
(\{12,34\},
 \{12,35\},
 \{12,45\},
 \{13,45\},
 \{13,25\},
 \{25,34\}).
\]

The repeated pivot is `12`. Collapsing the middle state `\{12,35\}` gives the Petersen pentagon

\[
C_5=
(\{12,34\},
 \{12,45\},
 \{13,45\},
 \{13,25\},
 \{25,34\}).
\]

The omitted-index triple on the expanded turn is

\[
5,4,3.
\]

Hence

\[
d=(3\ 5),
\qquad
e=(4\ 3)(5\ 4),
\qquad
\sigma=d^{-1}e=(3\ 4).
\]

The collapsed pentagon monodromy is

\[
\rho=(1\ 4\ 2\ 3),
\]

while the expanded cycle has

\[
\boxed{
\mu=\rho\sigma=(1\ 4)(2\ 3).
}
\]

Thus `mu` is exactly the canonical cycle-axis reflection previously obtained abstractly from reversal of the based pentagon.

---

## 7. The six-turn reflection theorem

### Theorem 7.1 — intrinsic reflection cell

Every mixed six-cycle in a six-output return window is already a complete coefficient/support reflection object:

\[
\boxed{
\text{pentagon rotation}
+\text{one local star detour}
=\text{DDD cycle-axis reflection}.
}
\]

It is unnecessary to append a separate three-turn star loop to the pentagon in order to generate a reflection. The expanded pentagon contains both ingredients in one six-transition state cycle.

### Consequence 7.2

The four cyclic short-state sectors now have the sharper interpretation:

\[
\begin{array}{c|c}
\text{state core}&\text{dihedral role}\\
\hline
\text{star triangle}&\text{single-transposition reflection}\\
\text{Petersen pentagon}&\text{order-four rotation}\\
\text{star-expanded pentagon}&\text{double-transposition reflection}\\
\text{Petersen hexagon}&\text{identity return}.
\end{array}
\]

These are exactly the bounded support motions needed for the DDD rotation/reflection and flat identity sectors.

---

## 8. Affine calibration target

Let `c` be the physical affine cocycle when the relevant bounded state cycles are physically realised with compatible source semantics.

After normalising the pentagon rotation so that

\[
c(\rho)=0,
\]

the reflection substitution theorem gives

\[
\boxed{
 c(\sigma)=c(\mu)\in\{0,q_i\}.
}
\]

Thus the star-expanded pentagon can directly measure the same one-bit DDD affine class as either star reflection or the abstract pentagon-reversal reflection.

### Physical alternatives

For a mixed six-output cell, prove one of:

1. the entire expanded cycle is physically realisable and gives reflection value `0` or `q_i`;
2. the direct pentagon turn and expanded detour are both realisable, so their quotient gives the local star reflection;
3. one of the two realisations fails by an empty root fibre or empty vertex relation;
4. their route discrepancy gives profile escape;
5. their incidence discrepancy factors through a smaller separator/four-pole or bounded DDD atom.

This is the exact finite comparison erased by collapsing the length-two pivot run.

---

## 9. Wolfram certificate

Exact enumeration of all sixty mixed six-cycles verifies simultaneously:

\[
\mu=\rho\sigma,
\]

\[
\sigma\rho\sigma=\rho^{-1},
\qquad
\mu\rho\mu=\rho^{-1},
\]

and the type triple

\[
(2\,1^3,\ 4\,1,\ 2^2\,1)
\]

for

\[
(\sigma,\rho,\mu).
\]

The exact count is

\[
60/60
\]

with no exceptional orbit.

---

## 10. Trust boundary

### Exact here

- the `12*5=60` star-expanded-pentagon classification;
- the direct-turn versus expanded-detour formula;
- identification of the relative detour with a star reflection;
- factorisation `mu=rho sigma`;
- inversion of the pentagon rotation by both reflections;
- type `2^2 1` as a reflection rather than central rotation;
- equality of the mixed-cell affine detector with the other DDD reflection detectors after rotation normalisation.

### Still open

- physical source realisability of the expanded six-cycle;
- affine value `0` or `q_i` in an actual return cell;
- composition-safe transfer between direct and expanded turns;
- identity-hexagon affine displacement;
- source-graph contraction, separator extraction, horizontal induction, and the global five-support theorem.
