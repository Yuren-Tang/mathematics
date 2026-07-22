# Equality locks project to one complete-profile identity hexagon

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parent surface:** current branch head containing `FULL_DEFECT_TREE_NNI_DESCENT_V1.md`.  

**Status:** exact rank-two projection and finite root calibration for the only residual one-edge equality lock. Two adjacent equality-repair channels produce a three-colour Tait difference carrier. After cutting the two marked equal-root edges, its two open bicoloured responses are the same terminal matching. Every connected four-port carrier with this response compresses to the canonical six-vertex equal-matching gadget. That gadget, as an uncoloured cubic four-pole, realises all `640` ordered conserved root boundaries and hence the complete ten-state profile. For the fixed equality colouring it has exactly seven root lifts: three rank-two triangle lifts and four `K_4`/DDD lifts. Therefore the bounded identity-hexagon core is not intrinsically locked; a genuine equality lock can survive only because physical side attachments prevent enclosure or profile transfer.  

**Not implied:** automatic transfer of the complete profile from the canonical gadget to an arbitrary larger physical carrier, elimination of every attachment pattern, final global proof-DAG closure, canonical acceptance, independent audit, Lean verification, manuscript integration, or the global five-support theorem.

---

## 1. Equality full-channel setup

Let

\[
x:E(G')\to R_5
\]

be a root-valued flow on the smaller graph obtained after one two-vertex cancellation. Let the two marked reconnected edges be

\[
e,f
\]

with common value

\[
x(e)=x(f)=r=uv.
\]

For every repair root

\[
s\in S_r=\{uw,vw:w\in[5]\setminus\{u,v\}\},
\]

put

\[
H_s=\{a:x(a)+s\in R_5\}.
\]

In a pure-gauge equality lock, the established full-component theorem gives:

1. every `H_s` is one connected Kempe cycle;
2. every `H_s` contains `e` and `f`;
3. cutting `e,f` gives the same oriented terminal matching
   \[
   M_i
   \]
   for all six channels.

No affine or cohomological ambiguity remains at this stage.

---

## 2. The adjacent-channel Tait difference

Choose one resolution pair

\[
s=uw,
\qquad
t=vw.
\]

Then

\[
s+t=r.
\]

Define the zero-boundary `E_5` flow

\[
\boxed{
h_{s,t}=s1_{H_s}+t1_{H_t}.
}
\]

Edgewise:

\[
h_{s,t}(a)=
\begin{cases}
0,&a\notin H_s\cup H_t,\\
s,&a\in H_s\setminus H_t,\\
t,&a\in H_t\setminus H_s,\\
r,&a\in H_s\cap H_t.
\end{cases}
\]

Thus every nonzero value belongs to the root triangle

\[
\{s,t,r\},
\qquad s+t+r=0.
\]

At a source vertex, flow conservation leaves only:

- a degree-two continuation with two equal nonzero values;
- a trivalent Tait vertex carrying exactly `s,t,r`.

Suppress every equal-value degree-two continuation. Record every edge incident to a suppressed vertex but absent from the support as an external side attachment. The remaining branch vertices and coloured segments form the **equality Tait core**

\[
T_{s,t}.
\]

It is properly three-edge-coloured by

\[
\{s,t,r\}.
\]

The suppressed side signature is retained as physical composition data; it is not discarded.

---

## 3. Exact four-port response

The marked edges `e,f` belong to both `H_s` and `H_t`, because their value is `r` and

\[
r+s=t,
\qquad
r+t=s.
\]

Cut `e,f` at their interiors. The four resulting marked semiedges all have Tait colour `r`.

The bicoloured systems of `T_(s,t)` satisfy:

\[
T_{sr}=H_t,
\qquad
T_{tr}=H_s,
\]

up to the suppressed equal-value continuations. Hence both open responses are the same matching:

\[
\boxed{
M_{sr}=M_{tr}=M_i.
}
\]

The `st` system has no marked boundary semiedge.

Therefore the marked equality core has ordered Tait response

\[
\boxed{
(r,r,r,r;\ M_i,M_i,\varnothing).
}
\]

### Connectivity alternative

After cutting `e,f`, exactly one of:

1. the marked Tait core is connected and has four boundary semiedges;
2. it has two marked connected components, each with two `r`-coloured boundary semiedges.

The second case is the abstract two-rail/direct-pairing response. Every connected two-port component is response-equivalent to one coloured dipole. Any physical connection between the two rails that is absent from the Tait core is necessarily carried by the recorded side signature.

---

## 4. Canonical connected equal-response gadget

The four-port Tait response-compression theorem supplies a unique minimal size for the connected response

\[
(r^4;M_i,M_i,\varnothing).
\]

It has six internal vertices.

Label the four boundary vertices

\[
v_1,v_2,v_3,v_4
\]

and the two boundary-free vertices

\[
p,q.
\]

Assume

\[
M_i=(12)(34).
\]

Use one internal `r`-edge

\[
pq,
\]

three `s`-edges

\[
v_1v_2,
\qquad
v_3p,
\qquad
v_4q,
\]

and three `t`-edges

\[
v_1p,
\qquad
v_2q,
\qquad
v_3v_4.
\]

The `sr` and `tr` endpoint matchings are both `(12)(34)`, while the `st` subgraph is one closed six-cycle. This is the canonical **identity-hexagon four-pole**.

It is vertex-minimal: with only four internal vertices, the `s`- and `t`-matchings would coincide and their union would have two connected components.

---

## 5. Fixed equality-colouring root lifts

Normalise

\[
r=12,
\qquad
s=13,
\qquad
t=23.
\]

The roots are partitioned by membership in the two Kempe systems:

### Both-safe / Tait colour `r`

\[
X=\{12,34,35\}.
\]

### `s`-only / Tait colour `s`

\[
Y=\{14,15,23\}.
\]

### `t`-only / Tait colour `t`

\[
Z=\{13,24,25\}.
\]

Fix all four boundary labels to be the physical root `12`.

Let

\[
A\in Y
\]

be the root on `v_1v_2`, and let

\[
B\in Z
\]

be the root on `v_3v_4`.

All other internal labels are forced by the six vertex equations:

\[
\begin{aligned}
 x(v_1p)=x(v_2q)&=r+A,\\
 x(v_3p)=x(v_4q)&=r+B,\\
 x(pq)&=A+B.
\end{aligned}
\]

The extension is root-valued exactly when

\[
A+B\in X.
\]

### Theorem 5.1 — seven fixed-colouring lifts

There are exactly seven root-valued lifts.

#### Three diagonal lifts

\[
B=r+A,
\qquad
A+B=r.
\]

Explicitly:

\[
(A,B,A+B)
=
(14,24,12),
(15,25,12),
(23,13,12).
\]

Each lift uses one root triangle only and is rank two.

#### Four off-diagonal lifts

\[
\begin{aligned}
(A,B,A+B)
=&(14,13,34),\\
 &(23,24,34),\\
 &(15,13,35),\\
 &(23,25,35).
\end{aligned}
\]

In each case the boundary root `r` and the central root `A+B` are disjoint. The labels are the six roots of one `K_4` support set. Thus every off-diagonal lift is canonically a `K_4`/DDD identity-hexagon lift.

The two remaining pairs in `Y\times Z` force the same co-root and are not root-valued.

Hence:

\[
\boxed{
\text{fixed equality hexagon}
\Longrightarrow
\text{rank-two triangle or one DDD-labelled }K_4.
}
\]

There is no third bounded root-lift species.

---

## 6. Complete root profile of the uncoloured gadget

Forget the distinguished Tait colouring but retain the six-vertex cubic four-pole.

Let the ordered boundary roots be

\[
(b_1,b_2,b_3,b_4)\in R_5^4,
\qquad
b_1+b_2+b_3+b_4=0.
\]

Choose roots

\[
A=x(v_1v_2),
\qquad
B=x(v_3v_4).
\]

Every other internal value is forced:

\[
\begin{aligned}
 x(v_1p)&=b_1+A,\\
 x(v_2q)&=b_2+A,\\
 x(v_3p)&=b_3+B,\\
 x(v_4q)&=b_4+B,\\
 x(pq)&=b_1+A+b_3+B.
\end{aligned}
\]

The last vertex equation is equivalent to boundary conservation. Therefore extension is the finite test that these five forced values are roots.

### Theorem 6.1 — complete ordered-root coverage

Every ordered conserved root quadruple extends across the six-vertex gadget.

Equivalently:

\[
\boxed{
\Sigma(\mathrm{Hex}_{=})=\mathcal S.
}
\]

More strongly, the gadget realises all

\[
\boxed{640}
\]

ordered conserved root boundaries.

### Exact finite certificate

Enumerate:

- the `640` ordered quadruples in `R_5^4` with zero sum;
- the `100` choices `(A,B)\in R_5^2`;
- the five forced internal values above.

The result is:

\[
\boxed{
\begin{array}{c|c}
\text{conserved ordered boundaries}&640\\
\text{boundaries with at least one extension}&640\\
\text{total root-valued extensions}&5700\\
\text{minimum extensions per boundary}&2\\
\text{maximum extensions per boundary}&23.
\end{array}}
\]

The extension-count distribution is

\[
\begin{array}{c|ccccccccc}
\#\text{ extensions}&2&3&6&7&8&12&18&20&23\\
\#\text{ boundaries}&60&120&120&60&60&120&10&30&60.
\end{array}
\]

The ten support-unordered states all occur.

---

## 7. Consequence for the one-edge equality frontier

The connected bounded equality core is not itself a locked profile:

\[
\boxed{
\text{canonical connected identity hexagon}
\Longrightarrow
\text{complete ten-state profile}.
}
\]

In particular it realises every cap set `K_i` and every direct-pairing set `J_i`.

Therefore a genuine pure-gauge equality lock cannot be explained by:

- a missing finite root boundary state;
- an affine or cohomological bit;
- a new bounded Tait response;
- or an intrinsic identity-hexagon root obstruction.

It can survive only because the physical side attachments carried by suppressed degree-two continuations prevent one of:

1. enclosing the connected four-port core;
2. replacing it while preserving the relevant source category;
3. transferring one of its extra root states back to the original region.

The disconnected abstract core is exactly two two-port rails. Thus the remaining geometry is precisely the passage from two separated rails to one connected identity hexagon.

---

## 8. Revised final attachment theorem

After the full-defect-tree NNI theorem, every defect component is one edge. The equality atom is now reduced to the following source statement.

### Target 8.1 — identity-hexagon enclosure

Let a cyclically reduced one-edge equality lock produce the marked double-equal Tait response

\[
(r^4;M_i,M_i,\varnothing)
\]

and let `Sigma_side` be the complete ordered side-attachment signature along its suppressed Tait core. Prove one of:

1. **connected enclosure:** a connected four-port identity-hexagon region is isolated; its complete profile gives a state in `K_i` and the inverse dipole lifts;
2. **crossing attachment:** a side component interlaces the two rails and gives a route-changing Kempe switch, a rank-two Tait escape, or a DDD pivot carrier;
3. **split attachment:** the side signature exposes a two-, three-, or four-edge separator;
4. **serial peeling:** a minimal noncrossing attachment interval can be removed with strict decrease of the side-network measure;
5. **direct-pairing terminal:** all connections disappear and the physical carrier is the bounded two-rail `J_i` gadget, which must be discharged by the category lemma for the three reconnections.

No coefficient or finite-core branch remains outside this list.

A natural well-founded local measure is

\[
\boxed{
\mathcal E_{=}
=
(N_{\mathrm{side}},
 N_{\mathrm{branch}},
 D_{\mathrm{nest}},
 |V_{\mathrm{core}}|),
}
\]

ordered lexicographically, where:

- `N_side` counts physical side attachments on suppressed continuations;
- `N_branch` counts trivalent vertices of the equality Tait core;
- `D_nest` is the maximal noncrossing attachment depth;
- the final coordinate distinguishes the connected six-vertex core from the two-rail degeneration.

---

## 9. Trust boundary

### Exact here

- the adjacent-channel difference flow `h_(s,t)`;
- its root-triangle coefficient alphabet `{s,t,r}`;
- the suppressed three-colour Tait core with retained side signature;
- the double-equal marked response `(r^4;M_i,M_i,empty)`;
- the connected/disconnected marked-core alternative;
- the canonical six-vertex equal-response gadget;
- the exact seven fixed-colouring root lifts;
- their `3+4` rank-two/DDD classification;
- complete realisation of all ten boundary states;
- complete ordered coverage of all `640` conserved root quadruples;
- the exact `5700` extension count and distribution.

### Still open

- composition-safe enclosure of the connected identity hexagon inside arbitrary physical side attachments;
- proof that every crossing attachment gives one of the already eliminated escape/DDD branches;
- strict serial peeling with preservation of the four marked root incidences;
- the final direct-pairing/category degeneration;
- global well-founded packaging and proof-DAG audit;
- canonical acceptance, independent review, Lean verification, manuscript integration, release, and publication status;
- the global five-support theorem.
