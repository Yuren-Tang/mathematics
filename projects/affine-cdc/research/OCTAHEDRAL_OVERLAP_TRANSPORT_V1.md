# Octahedral overlap transport and the D8 return group

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parent:** `projects/affine-cdc/research/RELATIVE_WITNESS_SUBTRACTION_V1.md`  
**Status:** exact finite transport theorem; contraction and global class identification remain open.

---

## 1. Fixed co-root overlap

Let `s,t` be disjoint repair roots and put

\[
c=s+t.
\]

Let `A,B` be two relative route witnesses and suppose

\[
\lambda_A=\lambda+s1_A,
\qquad
\lambda_B=\lambda+t1_B
\]

are root-valued on their witness region. On an overlap edge `e in I=A cap B`, define

\[
y_e=\lambda_A(e)=\lambda(e)+s,
\qquad
z_e=\lambda_B(e)=\lambda(e)+t.
\]

Then

\[
y_e+z_e=c.
\]

Because `c` is a co-root, `y_e,z_e` are disjoint roots.

Represent `c` in the `K_6` model as the edge `infinity m`. Let

\[
U=[5]\setminus\{m\}.
\]

The roots `y` for which `y+c` is again a root are exactly the six edges of `K_4` on `U`; `y+c` is the opposite edge of the same perfect matching.

Thus an **oriented overlap state** is one edge

\[
y\in E(K_4(U)),
\]

and the second witness occupies its antipode

\[
z=y+c.
\]

---

## 2. The octahedral state graph

Consider a degree-two overlap vertex. Let `e,e'` be the two overlap edges and `f` the side edge. Put

\[
y=y_e,\quad y'=y_{e'},\quad z=y+c,\quad z'=y'+c,
\]

and let the common side-root value in both witnesses be `w`.

Root conservation in the two witnesses gives

\[
y+y'+w=0,
\qquad
z+z'+w=0.
\]

Hence

\[
w=y+y'=z+z'.
\]

Since `w` is a root, the `K_4` edges `y,y'` meet. Conversely, meeting edges have root sum equal to the third edge of their triangle.

### Theorem 2.1 — octahedral transport

The oriented overlap-state graph is

\[
\boxed{L(K_4),}
\]

the octahedral graph on six vertices. Its antipodal pairs are the three perfect matchings of `K_4`, i.e. the three unoriented disjoint-root-pair states above `c`.

The side-root output on a transition is not independent: for an oriented step `y -> y'`,

\[
\boxed{w=y+y'.}
\]

Thus the full side-root word is determined by the oriented state walk.

### Relation to the general transducer

The general co-root-strip theory uses a walk in `L(Petersen)` together with side-root outputs. The two-witness subtraction branch with fixed difference co-root `c` lies in the six-state octahedral fibre described above. This is a strict reduction of the finite state space, not a justification for deleting the physical strip.

---

## 3. Canonical local support transposition

Let `y,y'` be adjacent edges of `K_4(U)` and put

\[
w=y+y'.
\]

The two endpoints in the symmetric difference of `y` and `y'` are exactly the endpoints of `w`. Let

\[
\tau_w\in S(U)\cong S_4
\]

be the transposition of those two endpoints.

### Theorem 3.1 — local frame transport

\[
\boxed{
\tau_w(y)=y',
\qquad
\tau_w(y+c)=y'+c,
\qquad
\tau_w(w)=w.
}
\]

Hence every overlap transport vertex carries a canonical terminal/support relabelling that simultaneously transports both root sheets and fixes the physical side-root output.

### Proof

If `y=pq` and `y'=pr`, then `w=qr`; the transposition `(qr)` sends `pq` to `pr`, sends the opposite edge of `pq` to the opposite edge of `pr`, and fixes the edge `qr` setwise.

---

## 4. Path transport and holonomy

Let an oriented overlap path have states

\[
y_0,y_1,\ldots,y_n
\]

and side roots

\[
w_i=y_{i-1}+y_i.
\]

Define

\[
\pi_\gamma
=\tau_{w_n}\cdots\tau_{w_1}
\in S_4.
\]

### Theorem 4.1 — cumulative transport

\[
\boxed{
\pi_\gamma(y_0)=y_n,
\qquad
\pi_\gamma(y_0+c)=y_n+c.
}
\]

Thus the enriched overlap word has a canonical `S_4` transport product.

This product retains more information than the unoriented three-state path, but less than the literal side-root word. It is a finite endpoint invariant of the physical transport.

---

## 5. The D8 return group

Let

\[
M=\{y,y+c\}
\]

be one antipodal pair, equivalently one perfect matching of `K_4`.

The setwise stabiliser of `M` in `S_4` is

\[
\operatorname{Stab}_{S_4}(M)\cong D_8.
\]

The subgroup fixing the two edges `y` and `y+c` separately is

\[
V_4\cong C_2\times C_2.
\]

### Theorem 5.1 — return exact sequence

If an overlap word returns to the same **unoriented** disjoint-root-pair state, then

\[
\pi_\gamma\in D_8.
\]

Moreover there is an exact sequence

\[
\boxed{
1\longrightarrow V_4
\longrightarrow D_8
\xrightarrow{\chi}C_2
\longrightarrow1,
}
\]

where

- `chi(pi)=0` when `pi` returns each oriented root sheet to itself;
- `chi(pi)=1` when `pi` exchanges the two sheets `y` and `y+c`.

This is the canonical orientation-return bit of the enriched overlap transport.

### Mechanistic significance

The same group `D_8` is the stabiliser of an elementary DDD atom. The theorem therefore supplies a direct physical route from an overlap state word to a DDD stabiliser element. It does **not** yet prove that the return bit is the previously identified nontrivial class in `H^1(D_8,E_5)`, nor that a segment with nontrivial return can be contracted to a bounded atom.

---

## 6. Two distinct binary quotients

The return quotient

\[
D_8/V_4\cong C_2
\]

must not be confused with the earlier local oriented-route quotient

\[
(C_2^3\rtimes S_3)/S_4\cong C_2.
\]

- The first is a **physical transport return bit inside `S_4`**: it records whether a disjoint-root pair returns with its two sheets exchanged.
- The second is a **local realisability bit outside terminal relabellings**: it records whether an abstract six-object pairing preserves the triangle/star class.

A transgression relation between these two bits is plausible and would explain the repeated `C_2` phenomena, but it is not proved here.

---

## 7. Why repeated state still does not imply contraction

If the oriented state repeats, the intervening transport lies in `V_4`. If only the unoriented state repeats, it lies in `D_8`, with the additional bit `chi`.

Nevertheless, the overlap segment may have arbitrarily many side attachments. Although each local transposition fixes its own side-root label, replacing or deleting the segment may alter the attachment geometry and the allocation of support labels to external components. Therefore:

- repeated state alone is insufficient;
- endpoint state plus `pi_gamma` is a sharper finite interface;
- a composition theorem must still show that this interface can be realised by a bounded replacement, a gauge transfer across a separated region, or a DDD/defect blossom.

---

## 8. Next obligations

### Obligation A — transfer sufficiency

Determine whether the triple

\[
(y_0,y_n,\pi_\gamma)
\]

is a complete interface for root-admissible replacement once the side attachments are treated as fixed ports. If not, identify the smallest additional physical datum.

### Obligation B — return localisation

For a support-minimal overlap segment returning to one unoriented state, prove one of:

1. `chi=0` gives a gauge/serial reduction or profile escape;
2. `chi=1` localises the exceptional `C_2` return to a bounded DDD blossom;
3. failure of either exposes a smaller cyclic separator or a zero/co-root defect unit.

### Obligation C — class identification

Compare the return bit `chi`, the DDD class in

\[
H^1(D_8,E_5)\cong\mathbf F_2,
\]

the full-channel curvature word, and the local triangle/star quotient. Any equality must be established by a canonical chain map, not by dimension counting.

---

## 9. Trust boundary

### Exact here

- the six-state fixed-co-root fibre;
- the octahedral transition graph;
- determination of the side-root output by the oriented transition;
- the canonical transposition at each transport vertex;
- the cumulative `S_4` transport product;
- the `D_8` return group and `V_4` kernel;
- distinction between the two binary quotients.

### Open

- bounded replacement from finite transport data;
- identification with the exceptional DDD cohomology class;
- contraction of nontrivial returns;
- Type T/Type H composition and global five-support closure.
