# Componentwise patching of root-flow differences

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Status:** exact source-localisation theorem; profile consequences remain conditional on the ten-state boundary quotient.

---

## 1. Difference support

Let `P` be a cubic multipole. Let

\[
x_0,x_1:E(P)\longrightarrow R_5
\]

be two root-valued `E_5` flows on all internal vertices, with possibly different terminal values.

Put

\[
h=x_0+x_1.
\]

Then `h` is an `E_5` relative flow. Let

\[
H=\operatorname{supp}(h)
=\{e:x_0(e)\ne x_1(e)\}.
\]

Let `C_1,...,C_m` be the edge-connected components of `H`, and let

\[
h_i=h1_{C_i}.
\]

---

## 2. Independent patching

### Theorem 2.1 — componentwise hybrid cube

For every subset `J subseteq {1,...,m}`, define

\[
x_J=x_0+\sum_{i\in J}h_i.
\]

Then `x_J` is a root-valued flow on every internal vertex. Equivalently, it uses `x_1` on the selected difference components and `x_0` everywhere else.

### Proof

At an internal vertex, all incident nonzero `h`-edges belong to one connected component of `H`; their `h`-values sum to zero because `h` is a flow. Thus each `h_i` separately satisfies the internal flow equations. Hence so does `x_J`.

Edgewise,

\[
x_J(e)\in\{x_0(e),x_1(e)\}.
\]

Both alternatives are roots, so `x_J` is root-valued.

### Corollary 2.2

Two root-valued witnesses generate a cube of `2^m` root-valued hybrids, one bit for each connected component of their difference support.

This patching theorem requires no assumption that the difference values themselves are roots.

---

## 3. Constant four-terminal difference

Assume the multipole has four terminals `T={1,2,3,4}` and that

\[
h(e)=d\ne0
\qquad(e\in T).
\]

For one support component `C_i`, sum the flow equation over its internal vertices. Internal edges cancel and give

\[
\sum_{e\in C_i\cap T}d=0.
\]

Therefore:

### Theorem 3.1 — even terminal incidence

Every connected component of the difference support meets the four terminals in

\[
0,\quad2,\quad\text{or}\quad4
\]

terminal edges.

Consequently the terminal-changing support has exactly one of two forms:

1. one connected component contains all four terminals;
2. two connected components contain two terminals each, defining one perfect matching of the terminal set.

Other difference components are internal gauge components.

---

## 4. Two-terminal hybrids

In the second case, let the terminal components be `C` and `C'`. The four patchings

\[
x_0,\qquad x_0+h_C,\qquad x_0+h_{C'},\qquad x_1
\]

are root-valued. The two middle covers change exactly one pair of terminal values by `d`.

### Corollary 4.1 — component localisation alternative

For any pair of root-valued witnesses with constant full terminal difference, either

- there are genuine two-terminal hybrid root covers; or
- all four terminals lie in one connected component of the difference support.

This is an exact source-side alternative before quotienting by support permutations.

### Boundary-profile caveat

A two-terminal hybrid need not automatically be a new support-unordered ten-state profile: in a misaligned Kempe situation it may be support-gauge equivalent to the original state. The existing cap/Kempe alignment theorem decides this after the physical challenge and cap matching are specified.

Thus the exact conclusion is existence of hybrid covers, not unconditional profile expansion.

---

## 5. Application to repair-witness subtraction

Suppose

\[
x_0=\lambda+s1_A,
\qquad
x_1=\lambda+t1_B
\]

are two root-valued route witnesses with

\[
\partial A=\partial B=T.
\]

Then

\[
h=x_0+x_1=s1_A+t1_B
\]

and the terminal difference is the constant value

\[
d=s+t.
\]

Combining the patching theorem with the adjacent/disjoint subtraction theorem gives:

### Theorem 5.1 — connected-carrier reduction

Every repair-witness collision has one of the following outcomes.

1. The difference support splits into two terminal-pair components, producing two independent two-terminal hybrid root covers.
2. A unique connected difference component contains all four terminals; all other components are internal gauge components.

In Outcome 2:

- the adjacent-coefficient branch gives one connected four-terminal root-supported coefficient carrier;
- the disjoint-coefficient branch gives one connected four-terminal carrier whose overlap carries the octahedral enriched co-root transport.

Hence irreducible physical collision analysis may be restricted to one connected four-terminal carrier.

---

## 6. Relation to Type T and Type H

The theorem does not identify the connected carrier with one of the exact finite routing kernels. It supplies the missing localisation step needed before that comparison.

- If a two-terminal hybrid is aligned with the current cap challenge, the cap/Kempe theorem gives boundary-profile expansion.
- If it is misaligned, the support-unordered boundary state may be unchanged by a global support transposition.
- If no two-terminal carrier exists, the unique four-terminal component is the natural source of unique-linkage/serial Type T behaviour or enriched-holonomy Type H behaviour.

A complete theorem must combine the component alternative with the ten-state transition table and the actual route matching.

---

## 7. Next obligations

### Obligation A — finite boundary disposition

For each ten-state boundary state and full terminal difference `d`, classify when the two-terminal hybrids are genuinely new profiles and when they are support-gauge copies. Reconcile the result with the fixed-routing graphs `P_3 union C_4 union P_3`.

### Obligation B — connected carrier anatomy

For the single four-terminal component, prove either

- serial/nested reduction;
- bounded four-pole replacement;
- enriched octahedral return and DDD localisation;
- or a smaller cyclic separator.

### Obligation C — global use

Show that the horizontal bad-flow induction can choose witness pairs whose component patching gives strict progress, rather than cycling among gauge-equivalent hybrids.

---

## 8. Trust boundary

### Exact here

- independent patching by difference-support components;
- the hybrid cube;
- even terminal incidence under constant terminal difference;
- the two-pair versus one-four-terminal carrier dichotomy;
- reduction of irreducible witness collision to one connected four-terminal carrier.

### Open

- unconditional support-unordered profile expansion from a two-terminal hybrid;
- Type T/Type H identification of the connected carrier;
- strict graph reduction and global five-support closure.
