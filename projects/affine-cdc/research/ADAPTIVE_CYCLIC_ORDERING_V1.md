# Adaptive cyclic ordering and flow-preserving cubic expansion

**Programme:** `AffineCDC — Research Lead`  
**Standing issue:** `AC-RL-01`  
**Base:** `749e0579581fcc838685138b3582f4de306b8e72`  
**Status:** theorem-level direct-research checkpoint; not canonical pending Director review

## 1. Problem

Let \(\Gamma\) be a finite vector space over \(\mathbf F_2\), and let

\[
A=[a_1,\dots,a_d]
\]

be a finite multiset of nonzero elements with total sum zero. Given an ordering of
its occurrences, put

\[
s_0=0,
\qquad
s_i=a_1+\cdots+a_i.
\]

For a port-cycle cubic expansion, the internal edge values have the form

\[
x_i=t+s_i.
\]

Thus the fixed external flow extends nowhere-zero across the fibre exactly when
one can order the occurrences and choose \(t\in\Gamma\) outside the proper-prefix
set

\[
\{s_0,\dots,s_{d-1}\}.
\]

M1 showed that an arbitrary fixed order can fail in \(\mathbf F_2^3\) at degree
eight. The question here is whether the order can always be chosen adaptively.

## 2. Main theorem

### Theorem 2.1 — adaptive prefix avoidance in binary vector spaces

Let \(\Gamma\) be a finite \(\mathbf F_2\)-vector space with
\(|\Gamma|\ge4\). Let \(A\) be a finite multiset in
\(\Gamma\setminus\{0\}\) whose sum is zero. Then the occurrences of \(A\) can
be ordered as

\[
a_1,\dots,a_d
\]

and there is a nonzero \(q\in\Gamma\) such that

\[
q\notin\{0,a_1,a_1+a_2,\dots,a_1+\cdots+a_{d-1}\}.
\]

Equivalently, every zero-sum multiset of nonzero binary vectors admits a cyclic
ordering whose proper prefix sums omit a nonzero group element.

The assertion is valid in every rank at least two, not only in rank three.

### Proof

For each \(a\ne0\), let \(n_a\) be its multiplicity and define the odd support

\[
P:=\{a\ne0:n_a\equiv1\pmod2\}.
\]

Because the total multiset sum is zero and pairs cancel in characteristic two,

\[
\sum_{a\in P}a=0.
\]

Write

\[
n_a=\mathbf 1_P(a)+2m_a.
\]

We first treat \(P\ne\varnothing\). Order the elements of \(P\) arbitrarily as

\[
b_1,\dots,b_k.
\]

They sum to zero. Their proper-prefix sequence has only \(k\) entries, including
zero. Since

\[
P\subseteq\Gamma\setminus\{0\},
\qquad
1\le k\le |\Gamma|-1,
\]

these proper prefixes cannot exhaust \(\Gamma\). Choose an omitted element
\(q\). Since zero is a proper prefix, \(q\ne0\).

Now insert the even remainder without changing any later prefix state:

1. for every \(a\ne q\), insert the adjacent pair \(a,a\) exactly \(m_a\)
   times while the current state is zero;
2. traverse the first odd-support step \(b_1\), reaching the nonzero state
   \(b_1\);
3. insert the adjacent pair \(q,q\) exactly \(m_q\) times at that state;
4. continue with \(b_2,\dots,b_k\).

Every pair is a closed two-step excursion. An \(a,a\) excursion from zero with
\(a\ne q\) avoids \(q\). The \(q,q\) excursion from \(b_1\) visits
\(b_1+q\), which cannot equal \(q\) because \(b_1\ne0\); and \(b_1\ne q\)
because \(q\) was omitted by the base prefix sequence. Hence all inserted
excursions avoid \(q\), and the later base prefixes are unchanged.

It remains to treat \(P=\varnothing\). If \(A\) is empty, the conclusion is
immediate. Otherwise choose a colour \(b\) with \(n_b>0\), so \(n_b\ge2\), and
choose

\[
q\in\Gamma\setminus\{0,b\};
\]

this is possible because \(|\Gamma|\ge4\). Reserve one pair \(b,b\) as a
scaffold. Insert every remaining pair of colour \(a\ne q\) at state zero;
traverse the first scaffold step \(b\); insert every \(q,q\) pair at state
\(b\); then traverse the second scaffold step \(b\) back to zero. The same
argument shows that neither the zero-based excursions nor the excursions based
at \(b\) visit \(q\).

Thus an ordering and an omitted nonzero \(q\) always exist. \(\square\)

## 3. Sharp rank boundary

The rank assumption is necessary. For

\[
\Gamma=\mathbf F_2
\]

and the multiset \([1,1]\), every ordering has proper prefixes \(0,1\), so no
group element is omitted. Hence rank two is the first valid rank.

## 4. Port-cycle consequence

### Corollary 4.1 — every fixed binary flow admits an adaptive port order

Let \(G\) be a finite-active-edge loopless multigraph carrying a nowhere-zero
\(\Gamma\)-flow, where \(\Gamma\) is a finite binary vector space of rank at
least two. At every active vertex \(v\), the incident flow-value multiset is
zero-sum and contains no zero.

For each vertex independently, choose the cyclic order given by Theorem 2.1 and
let \(q_v\) be the omitted proper-prefix value. Construct the port-cycle fibre in
that order. If

\[
s_{v,0}=0,\qquad s_{v,i}=a_{v,1}+\cdots+a_{v,i},
\]

define the internal edge values by

\[
x_{v,i}:=q_v+s_{v,i}.
\]

Then every internal value is nonzero, and at the port carrying external value
\(a_{v,i}\),

\[
x_{v,i-1}+a_{v,i}+x_{v,i}=0.
\]

Together with the unchanged values on the lifted original edges, these values
form a nowhere-zero \(\Gamma\)-flow on the cubic port-cycle expansion.

Thus every preselected nowhere-zero binary flow extends over **some adaptively
ordered** port-cycle expansion. Expansion and flow need not be produced
simultaneously, but the cyclic orders may be chosen from the flow.

## 5. Consequence for the AffineCDC outer shell

For \(\Gamma=\mathbf F_2^3\), the corrected classical binary-eight-flow theorem
may be applied downstairs to the original finite loopless bridgeless multigraph
\(G\). Corollary 4.1 then gives a flow-preserving cubic expansion.

This yields a second exact outer-shell route:

\[
G
\longrightarrow
(G,f)
\longrightarrow
(H,\widetilde f,\pi,\lambda),
\]

in addition to M1's accepted route

\[
G
\longrightarrow
H
\longrightarrow
(H,f).
\]

The new route does not replace M1: M1's expansion-first construction remains
flow-independent and already closed. The present theorem resolves the open
strengthening left by M1: the degree-eight Gray-tour example obstructs an
arbitrary preselected order, but there is always a suitable adaptive order.

## 6. Reliability and promotion boundary

- The proof is elementary and self-contained at paper level.
- No canonical file, frozen M1/M2 dossier, Lean file, engineering contract, or
  public Statement is changed here.
- Formalization would require a finite-multiset enumeration API, odd-support
  decomposition, pair insertion, cyclic-order packaging, and the port-cycle
  conservation adapter.
- Canonical promotion requires Director review.

## 7. Recommended next mathematical questions

1. Determine whether the adaptive construction can be made canonical or
   equivariant under automorphisms of the local flow multiset.
2. Minimize the number of distinct internal flow values or control the omitted
   value \(q_v\).
3. Compare the expansion-first and flow-first outer shells for formalization
   cost and functoriality.
4. Determine whether analogous ordering theorems survive for finite abelian
   groups not of exponent two.
