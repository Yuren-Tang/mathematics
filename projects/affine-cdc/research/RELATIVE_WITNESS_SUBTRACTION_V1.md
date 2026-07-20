# Relative witness subtraction and the uniform DDD network

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parent mechanism:** `projects/affine-cdc/research/QUADRATIC_CHANNEL_PROJECTION_V1.md`  
**Status:** exact chain-level theorem; conversion to strict graph reduction remains open  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Relative route witnesses

Let `P` be a cubic multipole with terminal set `T`. A binary relative even subgraph is a chain

\[
A\in C_1(P;\mathbf F_2)
\]

whose internal boundary vanishes. In the four-terminal routing application,

\[
\partial A=T,
\]

and its boundary-connected part consists of two terminal paths, possibly together with closed cycles.

Let `A,B` be two relative even subgraphs with the same terminal boundary

\[
\partial A=\partial B=T.
\]

Let `s,t in R_5` be two repair coefficients. Define the relative `E_5` chain

\[
h=s1_A+t1_B.
\]

At every internal vertex, `h` satisfies Kirchhoff conservation because `A` and `B` are individually even there. Its terminal boundary is

\[
\partial h=(s+t)T.
\]

Partition the edge set into

\[
A\setminus B,\qquad B\setminus A,\qquad I=A\cap B.
\]

Then

\[
h(e)=
\begin{cases}
s,&e\in A\setminus B,\\
t,&e\in B\setminus A,\\
s+t,&e\in I,\\
0,&e\notin A\cup B.
\end{cases}
\]

This elementary formula gives the complete subtraction classification.

---

## 2. Root branch

### Theorem 2.1 — adjacent-coefficient subtraction

Suppose either `s=t` or the two roots `s,t` meet in the `K_5` edge model. Then every nonzero value of `h` is a root.

- If `s=t`, the overlap cancels and
  \[
  h=s1_{A\triangle B}.
  \]
- If `s neq t` and the roots meet, then `s+t` is the third root of their `K_5` triangle. The only trivalent nonzero local state is
  \[
  (s,t,s+t).
  \]

Hence the subtraction is a root-supported relative chain. Its zero-side degree-two pieces are ordinary equality wires.

### Repair-channel interpretation

Fix an active root `r=ab` and write the six oriented repair channels as

\[
s_{k,\epsilon}=ak+\epsilon r,
\qquad
k\notin\{a,b\},\quad\epsilon\in\mathbf F_2.
\]

Two channels are adjacent whenever

1. they belong to the same algebraic resolution class `k`; or
2. they belong to different classes but have the same orientation bit.

Therefore both of these collision types lie entirely in the root branch.

---

## 3. Co-root branch

### Theorem 3.1 — disjoint-coefficient subtraction

Suppose `s` and `t` are disjoint roots. Put

\[
c=s+t.
\]

Then `c` is a co-root and the co-root support of `h` is exactly

\[
I=A\cap B.
\]

At an internal cubic vertex, the only possible nonzero local patterns are

\[
(0,s,s),\qquad
(0,t,t),\qquad
(0,c,c),\qquad
(s,t,c).
\]

The last triple is one perfect matching of the `K_6` edge model. Consequently:

- vertices of co-root degree two have pattern `(0,c,c)`;
- vertices of co-root degree one have the fixed one-factor pattern `(s,t,c)`;
- the co-root support is a union of paths and cycles;
- every internal endpoint of a co-root path is a one-factor vertex of the same DDD type.

### Proof

Both `A` and `B` have internal degree zero or two. If both use the same local pair, their intersection has degree two and `h` has two `c`-edges. If they use distinct local pairs, the two pairs meet in one edge because the source is cubic; that common edge receives `c`, and the two exclusive edges receive `s,t`. If only one chain is present, the two used edges receive two equal roots. These exhaust all possibilities.

---

## 4. Uniform DDD core

Delete zero edges from the support of `h` and suppress every degree-two vertex whose two nonzero incident values agree. In the disjoint-coefficient branch, every remaining trivalent internal vertex carries exactly the same one-factor

\[
\{s,t,c\}.
\]

### Theorem 4.1 — uniform one-factor reduction

The suppressed subtraction core has the following structure:

1. the `c`-edges form a matching (with possible terminal ends);
2. the `s`- and `t`-edges form alternating cycles and terminal paths;
3. every internal vertex is a copy of one fixed DDD one-factor state;
4. each suppressed `c`-path is a stretched co-root atom with the same two crossed root resolutions as the elementary DDD atom.

Thus the non-root subtraction branch is not a general co-root transducer. It is a uniform DDD network governed by one binary crossed-resolution choice.

### Minimal-witness refinement

If `A` and `B` are chosen without redundant closed components, then `I=A cap B` has no closed component common to both witnesses. Its co-root support is a forest of paths whose endpoints are terminals or one-factor divergence vertices.

This refinement is exact for path-system witnesses after deleting irrelevant common cycles. It does not by itself justify contraction of a long stretched atom inside the original source graph.

---

## 5. Rootification and the binary fibre

Return to the active-root parametrisation. The disjoint case occurs exactly when

\[
s=s_{k,\epsilon},\qquad
t=s_{\ell,\epsilon+1},\qquad k\ne\ell.
\]

Set

\[
u=c+r.
\]

Then `u=k\ell` is a root disjoint from `r`. Define

\[
h^\sharp=h+r1_I.
\]

On `A\setminus B`, `B\setminus A`, and `I`, the nonzero values of `h^sharp` are respectively

\[
s,\qquad t,\qquad u,
\]

and are all roots.

Let

\[
D=\{v\in V_{\mathrm{int}}(P):\deg_I(v)=1\}
\]

be the divergence set. Since both route witnesses use every terminal semiedge,

\[
\partial I=T+D.
\]

Therefore:

### Theorem 5.1 — exact root-plus-binary decomposition

\[
\boxed{
h=h^\sharp+r1_I,}
\]

where `h^sharp` is root-supported and

\[
\boxed{
\partial h^\sharp=uT+rD.
}
\]

The entire failure of `h^sharp` to be a genuine root-valued relative flow is the binary `r`-boundary on the divergence set `D`. The overlap `I` is an explicit `T union D`-join carrying that binary fibre.

At each `v in D`, the three root labels of `h^sharp` sum to `r`; restoring the `r`-fibre changes the common-edge root `u` back to the co-root `c` and recovers the one-factor state `(s,t,c)`.

---

## 6. Exact collision classification

For repair channels in `S_r`, subtraction has only the following outcomes.

### Corollary 6.1

1. **Same resolution class:** root-supported subtraction.
2. **Different classes, same orientation:** root-supported subtraction.
3. **Different classes, opposite orientation:** uniform DDD subtraction, equivalently a root-supported chain plus one binary `r`-fibre.

No fourth edge-value mechanism can appear.

This proves the finite algebraic part of the proposed collision-or-progress theorem. What remains is graph composition: showing that the first two branches force a profile-expanding/Kempe move or a smaller separator, and that the third branch can be localised or contracted without changing the relevant four-pole semantics.

---

## 7. Relation to route automata

Suppose a current four-pole state and challenge admit more than one physical route witness.

- If the corresponding repair coefficients fall in Cases 1 or 2 of Corollary 6.1, their subtraction is root-supported. In a deterministic residual routing kernel, the second genuine route is expected to leave the kernel profile; proving this requires matching the chain subtraction to the exact support-unordered boundary transition.
- If they fall in Case 3, their subtraction is a uniform DDD network. Its only local non-root datum is the crossed-resolution bit of the fixed one-factor `(s,t,c)`.

Accordingly, a non-permutation resolution-route relation cannot create a new finite obstruction alphabet. It must be discharged by either root/Kempe composition or DDD composition.

This is a mechanism theorem, not yet the strict-progress theorem.

---

## 8. Remaining proof obligations

### Obligation A — boundary-transition compatibility

Prove that a root-supported subtraction between two genuine route witnesses gives an actual Kempe/profile transition or exposes a smaller cyclic separator. The fact that the chain is root-supported is not alone sufficient; edgewise admissibility relative to the base cover and support-unordered boundary bookkeeping must be retained.

### Obligation B — stretched-atom composition

For a uniform DDD network, prove one of:

1. crossed resolutions can be chosen consistently, yielding a root-valued route witness and profile escape;
2. the first inconsistent cycle carries the unique `C_2` holonomy and may be isolated as a bounded blossom;
3. a long co-root path plus its zero equality attachments admits a composition-safe replacement;
4. a smaller separator or defect-forest unit is exposed.

### Obligation C — relation-to-connection

After Obligations A and B, prove that every irreducible resolution-route relation is a bijection. Only then apply the oriented-route exact sequence

\[
1\to S_4\to C_2^3\rtimes S_3\to C_2\to1
\]

as the complete physical lifting model.

---

## 9. Trust boundary

### Exact here

- the edgewise subtraction formula;
- the adjacent/disjoint dichotomy;
- the complete local pattern classification;
- the uniform one-factor reduction;
- the root-plus-binary overlap decomposition;
- the three-case collision classification for `S_r`.

### Still open

- automatic profile expansion from every root-supported subtraction;
- composition-safe contraction of every stretched DDD atom;
- the physical permutation-connection theorem;
- Type T strict descent, Type H closure, horizontal/global induction, and the global five-support theorem.
