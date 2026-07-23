# Quadruple equality rootifies by borrowing one adjacent root triangle

## Research Lead local repair theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parents:**

- `PACHNER_HISTORY_FIRST_FAILURE_ONE_EDGE_ATOM_V1.md`;
- `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`;
- `FIVE_LEAF_PACHNER_PENTAGON_ROOT_INTERVAL_V1.md`;
- `EQUALITY_RECURSION_VERTEX_DESCENT_V1.md` read through its target-order correction;
- the bridge-zero lemma for group-valued flows.

**Status:** exact local elimination of the unique quadruple-equality first-failure atom. A zero edge whose two endpoints are both `(0,a,a)` need not invoke recursive equality descent. Unless the whole component is the bounded two-vertex parallel terminal, borrow one adjacent root-valued vertex `(a,d,e)` with `a=d+e`. The resulting three-vertex/five-leaf region has boundary `(a,a,a,d,e)`. Two consecutive NNI moves around its five-leaf pentagon change the singular topology

\[
aa\mid a\mid de
\]

first to another one-zero topology and then to the unique root-valued topology

\[
ae\mid a\mid ad.
\]

The final graph is connected and carries a root on every edge, hence is bridgeless. Thus quadruple equality is a bounded two-NNI same-order rootification, not a recursive lower-order branch.

---

## 1. The quadruple-equality atom

Let

\[
c=uv
\]

be the unique zero edge after a failed inverse equal-face cancellation. Assume the quadruple-equality case:

\[
\lambda(c)=0,
\]

and at both endpoints the remaining two incident edges carry the same root

\[
a\in R_5.
\]

Thus the two local vertex equations are

\[
(0,a,a)
\qquad\text{and}\qquad
(0,a,a).
\]

The direct NNI triality on `c` has central value zero in all three pairings, so the two-vertex atom alone has no root resolution.

---

## 2. Borrow one adjacent root vertex

Choose one `a`-edge incident with `u` whose other endpoint is a root-valued vertex

\[
w\ne v.
\]

At `w`, let the other two incident roots be

\[
d,e.
\]

Since `w` is root-valued,

\[
\boxed{a=d+e.}
\]

Therefore `d,e` are distinct intersecting roots, and neither equals `a`.

### Bounded exception

If every `a`-edge at both zero endpoints joins `u` directly to `v`, then the connected component is the two-vertex multigraph consisting of the zero edge and two parallel `a`-edges. This is a bounded singular theta terminal. Replace its three edge values by any root triangle

\[
p,q,p+q
\]

and the component is root-solved.

A loop at a zero endpoint or any other nonordinary identification is likewise one of the already accepted bounded loop/parallel degenerations.

Hence the unbounded loopless branch always has an eligible adjacent root vertex `w`.

---

## 3. The exact five-leaf boundary

Take the three-vertex region

\[
\{v,u,w\}.
\]

Label its five exterior rooted branches:

\[
A=a,
\qquad
B=a,
\qquad
C=a,
\qquad
D=d,
\qquad
E=e,
\]

so that:

- `v` is the cherry `BC`;
- `u` is the central singleton `A`;
- `w` is the cherry `DE`.

The original topology is

\[
\boxed{T_0=BC\mid A\mid DE.}
\]

Its two internal values are

\[
B+C=a+a=0,
\]

and

\[
D+E=d+e=a.
\]

Thus `T_0` is precisely the three-vertex realization of the quadruple-equality zero atom.

The total boundary sum is

\[
A+B+C+D+E
=3a+d+e
=a+a
=0.
\]

---

## 4. Two consecutive pentagon moves

Use the standard five-leaf pentagon

\[
\begin{aligned}
T_0&=BC\mid A\mid DE,\\
T_1&=AC\mid B\mid DE,\\
T_2&=AC\mid E\mid BD,\\
T_3&=AE\mid C\mid BD,\\
T_4&=AE\mid D\mid BC.
\end{aligned}
\]

Take the two-step path

\[
\boxed{T_0\longrightarrow T_4\longrightarrow T_3.}
\]

### First move

In

\[
T_4=AE\mid D\mid BC,
\]

the cherry values are

\[
A+E=a+e=d,
\]

and

\[
B+C=a+a=0.
\]

The central singleton is `D=d`. Hence `T_4` still has exactly one zero edge and every other edge is root-valued.

This is the adjacent-zero propagation move from the critical-overlap theorem.

### Second move

In

\[
T_3=AE\mid C\mid BD,
\]

the two cherry values are

\[
A+E=a+e=d,
\]

and

\[
B+D=a+d=e.
\]

The central singleton is

\[
C=a.
\]

Since

\[
d+a+e=0,
\]

the central vertex is the root triangle

\[
(d,a,e).
\]

Thus every internal edge of `T_3` is root-valued.

### Theorem 4.1 — two-NNI rootification

The sequence

\[
\boxed{
aa\mid a\mid de
\longrightarrow
ae\mid d\mid aa
\longrightarrow
ae\mid a\mid ad
}
\]

preserves all five exterior incidences and root values and replaces the quadruple-equality atom by a fully root-valued three-vertex tree.

No cancellation, new root selection, or recursive call is used.

---

## 5. Exact finite certificate

For every ordered root-triangle triple

\[
(a,d,e)
\]

with

\[
a=d+e,
\]

there are sixty ordered choices in `R_5`.

Exhaustive evaluation of the five pentagon topologies for the boundary

\[
(a,a,a,d,e)
\]

gives the validity word

\[
\boxed{(0,0,0,1,0)}
\]

in all sixty cases.

Therefore:

- `T_3` is the unique root-valued five-leaf topology for this boundary;
- `T_0,T_4` are the stated one-zero intermediate topologies;
- there is no exceptional support choice.

The algebraic proof in Section 4 is controlling; the enumeration is an independent finite certificate.

---

## 6. Source-category preservation

The final local replacement `T_3` is one connected cubic tree meeting exactly the same five exterior incidences as `T_0`.

### Connectivity

Remove the interiors of the three-vertex region. The exterior graph may have several components incident with the five terminals. Both `T_0` and `T_3` connect all five terminals through one connected local tree. Replacing `T_0` by `T_3` therefore preserves connectivity of the complete graph.

### Cubicity and looplessness

Every new local vertex has degree three. All exterior edges retain their exterior endpoints. The replacement introduces only the two internal edges of a tree, so no local loop is created. Any pre-existing loop/parallel exceptional identification was already separated in the bounded branch of Section 2.

### Bridgelessness

The final graph carries a root-valued flow on every edge. In any abelian-group flow, a bridge must have value zero by the shore cut-sum equation. Every root is nonzero. Hence the connected final graph has no bridge.

### Theorem 6.1 — automatic category safety

In the ordinary connected loopless branch, the two-NNI borrowing movie produces another connected loopless bridgeless cubic graph carrying a root-valued `E_5` flow.

---

## 7. Consequence for inverse-cancellation equality

The old cancellation trichotomy was:

\[
\begin{array}{c|c}
\text{marked roots }a,b&\text{inverse result}\\
\hline
\text{distinct intersecting}&\text{root success}\\
a=b&\text{quadruple equality}\\
a\cap b=\varnothing&\text{co-root atom}.
\end{array}
\]

The middle row now has the exact same-order disposition:

\[
\boxed{
a=b
\Longrightarrow
\text{two-NNI rootification or bounded theta terminal}.
}
\]

Thus quadruple equality is not a recursive equality call and does not require a claimed target-order decrease.

---

## 8. Repair of the equality-recursion correction

Read the equality first-failure programme as follows.

### Retained

- quadruple equality occurs only at an inverse cancellation;
- inverse-flip zero atoms are immediately rootifiable;
- the cancellation trichotomy is complete.

### Superseded

The disposition

\[
\text{quadruple equality}
\Longrightarrow
\text{lower-order recursive equality problem}
\]

is no longer needed and should not be used.

### Replacement

\[
\boxed{
\text{quadruple equality}
\Longrightarrow
\text{bounded local two-NNI rootification}.
}
\]

This removes the only genuinely zero-valued recursive row from contextual inverse transfer.

---

## 9. Remaining first-failure frontier

After this theorem, every inverse-move failure has one of:

1. **inverse flip, zero:** immediate alternative root NNI;
2. **inverse cancellation, quadruple equality:** two-NNI borrowing rootification;
3. **zero bounded theta:** explicit root triangle;
4. **co-root:** oriented DDD/root-triality track;
5. **route, separator, or bounded exit.**

There is no remaining recursive zero atom.

The sole unbounded same-order issue is now the global scheduling of co-root discrepancy tracks, for which closed components are removed by `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md`.

---

## 10. Assurance boundary

### Exact here

- the five-leaf model of one quadruple-equality atom plus one adjacent root vertex;
- the explicit two-NNI path `T_0 -> T_4 -> T_3`;
- complete root-label calculation;
- the `60`-case exact finite certificate;
- connectivity, looplessness, and bridgelessness of the rootified output;
- bounded two-vertex exception;
- elimination of quadruple equality as a recursive branch.

### Not proved here

- complete scheduling of the resulting alternative root topology through every earlier history move;
- open co-root defect-arc termination;
- full contextual transfer, cap restoration, or global five-support closure;
- downstream proof development or independent verification;
- Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.
