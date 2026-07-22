# The three equality Tait projections are jointly faithful

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `a8360ccf520c17ccbeaf585efc633e25db3e260c`.

**Parents:**

- `EQUALITY_LOCK_PRIVATE_MATCHING_TAIT_DECOMPOSITION_V1.md`;
- `ROOT_FLOW_TRIANGLE_COMPLEX_PACHNER_V1.md`;
- the standard nondegenerate bilinear pairing on `E_5`.

**Status:** exact simultaneous coefficient theorem for the three adjacent-channel difference flows attached to one equality root. Each individual projection is rank two and has one private root as its unique zero root. The direct sum of the three projections has full rank four on `E_5`; hence the three matching-decorated Tait systems jointly recover the complete original coefficient. Every root edge is visible in at least two projections, and every source triangle except the complementary triangle is a genuine branch triangle in at least two projections.

**Not implied:** automatic simultaneous profile transfer, a common response-preserving compression sequence for all three projections, elimination of the connected equality carrier, global proof-DAG closure, canonical acceptance, Lean verification, manuscript integration, or the global five-support theorem.

---

## 1. Setup

Fix the active equality root

\[
r=uv.
\]

Write

\[
W=[5]\setminus\{u,v\}=\{x,y,z\}.
\]

For every

\[
w\in W
\]

put

\[
s_w=uw,
\qquad
t_w=vw,
\qquad s_w+t_w=r.
\]

Let

\[
b(a,c)=a\cdot c
\]

be the standard mod-two dot product on

\[
E_5=\{a\in\mathbf F_2^5:\sum_i a_i=0\}.
\]

Because `5` is odd, the restriction of the dot product to `E_5` is nondegenerate.

For a root-valued flow

\[
\lambda:E(G)\to R_5,
\]

the scalar safety indicator is

\[
1_{H_c}(e)=b(\lambda(e),c)
\]

for every root channel `c`: two roots have dot product one exactly when they are distinct and intersect.

---

## 2. The three rank-two coefficient maps

Define

\[
\boxed{
L_w(a)
=
s_w b(a,s_w)+t_w b(a,t_w)
\in\langle s_w,t_w\rangle.}
\]

Then the adjacent-channel difference flow is exactly

\[
h_w=L_w\circ\lambda.
\]

### Theorem 2.1 — rank two

For every `w`, the map

\[
L_w:E_5\to\langle s_w,t_w\rangle
\]

is surjective and has rank two.

### Proof

The two functionals

\[
b(-,s_w),
\qquad
b(-,t_w)
\]

are independent because `s_w,t_w` are independent and the pairing is nondegenerate. Their coefficient vectors `s_w,t_w` form a basis of the target plane. ∎

---

## 3. Unique private root in each root alphabet

Let

\[
\{p_w,q_w\}=W\setminus\{w\}
\]

and define

\[
d_w=p_wq_w.
\]

### Theorem 3.1 — singleton zero root

For a root

\[
a\in R_5,
\]

one has

\[
\boxed{L_w(a)=0\iff a=d_w.}
\]

### Proof

The two coordinates of `L_w(a)` vanish exactly when `a` is orthogonal to both `uw` and `vw`.

Among roots, the unique edge of `K_5` disjoint from both channels is the edge joining the two unused elements of `W`, namely `p_wq_w`. The channels themselves are not orthogonal to the other member of the pair, and every other root meets at least one channel in one endpoint. ∎

Thus the zero set of `h_w` in a root flow is exactly the private-root matching

\[
\lambda^{-1}(d_w).
\]

For

\[
W=\{3,4,5\},
\qquad r=12,
\]

the three private roots are

\[
\boxed{d_3=45,\qquad d_4=35,\qquad d_5=34.}
\]

---

## 4. Joint faithfulness

Define the direct-sum map

\[
\boxed{
L=(L_x,L_y,L_z):
E_5
\longrightarrow
\bigoplus_{w\in W}\langle s_w,t_w\rangle.}
\]

### Theorem 4.1 — full rank four

\[
\boxed{\ker L=0.}
\]

Equivalently,

\[
\boxed{\operatorname{rank}L=4=\dim E_5.}
\]

### Proof

If `L(a)=0`, then for every `w in W`,

\[
b(a,uw)=b(a,vw)=0.
\]

The six channel roots

\[
\{uw,vw:w\in W\}
\]

span `E_5`. For example, after normalising `u=1,v=2,W={3,4,5}`, the four roots

\[
13,\ 14,\ 15,\ 23
\]

are independent in `E_5`.

Hence `a` is orthogonal to all of `E_5`. Nondegeneracy gives `a=0`. ∎

### Corollary 4.2 — coefficient reconstruction

For every edge `e`, the triple

\[
\bigl(h_x(e),h_y(e),h_z(e)\bigr)
\]

uniquely determines the original coefficient

\[
\lambda(e)\in E_5.
\]

No root label, co-root label, or zero value is invisible to all three equality Tait projections.

---

## 5. Root visibility table

Normalise

\[
r=12,
\qquad W=\{3,4,5\}.
\]

### Active root

\[
L_3(12)=L_4(12)=L_5(12)=12.
\]

### Complementary roots

\[
\begin{array}{c|ccc}
 a&L_3(a)&L_4(a)&L_5(a)\\
\hline
34&r&r&0\\
35&r&0&r\\
45&0&r&r
\end{array}
\]

Thus a complementary root is invisible in exactly one projection and visible in the other two.

### Repair-channel roots

Every root meeting the active pair in exactly one support index has nonzero image in all three projections.

### Corollary 5.1

Every root edge belongs to the support of at least two of

\[
h_3,h_4,h_5.
\]

Hence a physical side attachment cannot be suppressed simultaneously from all three matching--Tait systems.

---

## 6. Simultaneous local triangle types

At a source vertex, let

\[
T\subset[5],
\qquad |T|=3,
\]

be its support triangle.

For one projection `w`, the vertex is:

- a **branch vertex** when `T` does not contain the private edge `d_w`;
- a **matching subdivision vertex** when `T` contains `d_w`.

The ten triangles split simultaneously as follows.

### Class A — active triangles

\[
123,\ 124,\ 125.
\]

Each contains the active root `12` and contains none of the three private roots as a complete edge. Therefore it is a branch vertex in all three projections.

### Class M — mixed triangles

\[
134,\ 135,\ 145,\ 234,\ 235,\ 245.
\]

Each contains exactly one of the private roots

\[
34,\ 35,\ 45.
\]

Therefore it is a matching subdivision in exactly one projection and a branch vertex in the other two.

### Class C — complementary triangle

\[
345.
\]

It contains all three private roots and is a matching subdivision in all three projections.

### Theorem 6.1 — two-projection branch visibility

Every source vertex other than a `345` complementary-Tait vertex is a genuine branch vertex in at least two of the three equality projections.

The only vertex hidden from all three branch skeletons is the complementary root triangle

\[
\{34,35,45\},
\]

which is itself the standard rank-two Tait vertex of the active-shift blocked network.

---

## 7. Consequences for the connected equality carrier

The connected equality carrier has three simultaneous descriptions

\[
\text{Tait skeleton}_w
+
\text{private matching }\lambda^{-1}(d_w),
\qquad w\in W.
\]

Theorem 4.1 implies that these are not three unrelated quotients. Together they are a faithful encoding of the original root-labelled source.

Consequently:

1. an attachment hidden as a private edge in one projection is visible in the other two;
2. every mixed source vertex remains available for branch Pachner surgery in two projections;
3. the only fully private region is a complementary `K_3` Tait component, already in the all-size Tait peeling branch;
4. any proposed universal transfer theorem may use the three projections adaptively without losing coefficient information.

This removes the possibility that an unbounded side-attachment alphabet survives solely in the common kernel of the equality projections.

---

## 8. Exact Wolfram certificate

Using the standard basis

\[
e_1+e_5,\ e_2+e_5,\ e_3+e_5,\ e_4+e_5
\]

of `E_5`, exact mod-two evaluation gives

\[
\operatorname{rank}(L_3\oplus L_4\oplus L_5)=4.
\]

The root table verifies:

- one zero root in each projection;
- every root visible in at least two projections;
- simultaneous branch multiplicities `3`, `2`, and `0` for Classes A, M, and C respectively.

The human proof above is the controlling proof; the computation is a finite certificate.

---

## 9. Trust boundary

### Exact here

- the linear maps `L_w`;
- rank two of every individual projection;
- the unique private zero root in each root alphabet;
- full rank four and joint injectivity;
- reconstruction of the original coefficient from the three projected values;
- complete root visibility table;
- complete simultaneous triangle-type classification;
- identification of `345` as the sole all-private vertex type.

### Still open

- a simultaneous response-preserving compression theorem using the three faithful projections;
- proof that adaptive Pachner surgery strictly decreases a cover-independent equality measure;
- transfer of a cap-lifting boundary state back through all surgeries;
- global proof-DAG closure;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication, and the global five-support theorem.
