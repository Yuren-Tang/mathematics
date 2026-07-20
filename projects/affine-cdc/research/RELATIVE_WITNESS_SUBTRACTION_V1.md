# Relative witness subtraction and the coefficient one-factor skeleton

## Research dossier v1.1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parent mechanism:** `projects/affine-cdc/research/QUADRATIC_CHANNEL_PROJECTION_V1.md`  
**Status:** exact chain-level theorem; physical transport semantics and strict graph reduction remain open  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, or the global five-support theorem.

### Correction from v1

The first version correctly classified the **difference coefficients**, but over-interpreted their repeated one-factor pattern as a physically uniform DDD network with immediately reusable crossed resolutions. That conclusion is not justified. The actual two root-valued witnesses carry base-dependent root-pair states and side-root outputs along the overlap. The exact physical object is an **enriched co-root transducer with a uniform coefficient skeleton**. Repeated coefficient state alone does not permit pumping, deletion, or contraction.

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

Let `s,t\in R_5` be two repair coefficients. Define the relative `E_5` chain

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

This formula gives the complete coefficient-level subtraction classification.

---

## 2. Root branch

### Theorem 2.1 — adjacent-coefficient subtraction

Suppose either `s=t` or the two roots `s,t` meet in the `K_5` edge model. Then every nonzero value of `h` is a root.

- If `s=t`, the overlap cancels and
  \[
  h=s1_{A\triangle B}.
  \]
- If `s\ne t` and the roots meet, then `s+t` is the third root of their `K_5` triangle. The only trivalent nonzero coefficient state is
  \[
  (s,t,s+t).
  \]

Hence the subtraction is a root-supported relative chain. Its equal-value degree-two pieces are coefficient equality wires.

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

Therefore both of these collision types lie in the root-supported coefficient branch.

### Trust boundary

A root-supported **difference chain** does not by itself prove an admissible Kempe switch relative to a chosen base cover. The two endpoint witnesses are genuine, but converting their subtraction into a third route, a profile-expanding transition, or a source reduction still requires boundary-state and edgewise-admissibility control.

---

## 3. Co-root branch

### Theorem 3.1 — disjoint-coefficient subtraction

Suppose `s` and `t` are disjoint roots. Put

\[
c=s+t.
\]

Then `c` is a co-root and the co-root support of the difference chain `h` is exactly

\[
I=A\cap B.
\]

At an internal cubic vertex, the only possible nonzero coefficient patterns are

\[
(0,s,s),\qquad
(0,t,t),\qquad
(0,c,c),\qquad
(s,t,c).
\]

The last triple is one perfect matching of the `K_6` edge model. Consequently:

- vertices of co-root degree two have coefficient pattern `(0,c,c)`;
- vertices of co-root degree one have coefficient pattern `(s,t,c)`;
- the co-root support is a union of paths and cycles;
- every internal endpoint of a co-root path is a one-factor vertex in the coefficient difference flow.

### Proof

Both `A` and `B` have internal degree zero or two. If both use the same local pair, their intersection has degree two and `h` has two `c`-edges. If they use distinct local pairs, the two pairs meet in one edge because the source is cubic; that common edge receives `c`, and the two exclusive edges receive `s,t`. If only one chain is present, the two used edges receive two equal roots. These exhaust all possibilities.

---

## 4. Uniform coefficient core versus enriched physical transport

Delete zero coefficients from `h` and suppress every degree-two vertex whose two nonzero difference coefficients agree. Every remaining trivalent internal vertex in the disjoint branch carries the same coefficient one-factor

\[
\{s,t,c\}.
\]

### Theorem 4.1 — uniform coefficient one-factor reduction

The suppressed **difference-coefficient** core has the following structure:

1. the `c`-edges form a matching, with possible terminal ends;
2. the `s`- and `t`-edges form alternating cycles and terminal paths;
3. every internal vertex carries the same one-factor coefficient state `(s,t,c)`.

This is exact for the subtraction chain.

### Theorem 4.2 — retained base semantics

Assume there is a base `E_5` flow `lambda` and that

\[
\lambda_A=\lambda+s1_A,
\qquad
\lambda_B=\lambda+t1_B
\]

are root-valued on the relevant witness region. For every overlap edge `e\in I`, put

\[
y_e=\lambda(e)+s,
\qquad
z_e=\lambda(e)+t.
\]

Then `y_e,z_e` are roots and

\[
y_e+z_e=c.
\]

Hence they are a disjoint root pair above the co-root direction `c`. The unordered pair

\[
\{y_e,z_e\}
\]

is an enriched transport state; it is not determined by the constant difference coefficient `c`.

At a degree-two overlap vertex, let `e_1,e_2` be the overlap edges and let `f` be the third edge. The two root witnesses have the same value on `f`, say `w`. Conservation gives

\[
y_{e_1}+y_{e_2}=w,
\qquad
z_{e_1}+z_{e_2}=w.
\]

Thus the overlap transports the disjoint-root-pair state while emitting the side-root output `w`. This is precisely the enriched co-root/Petersen transport phenomenon.

At a divergence vertex, the coefficient difference has pattern `(s,t,c)`, but the actual two root triangles depend on the base labels. The constant coefficient one-factor therefore does **not** imply identical physical DDD endpoint states or automatic crossed resolutions.

### Consequence 4.3

The disjoint subtraction branch is an enriched co-root transducer whose coefficient shadow is uniform. It may enter the DDD mechanism after localisation, but it is not already a contractible DDD blossom.

### Minimal-witness refinement

If `A` and `B` are chosen without redundant common closed components, then `I=A\cap B` has no closed component common to both witnesses. Its co-root coefficient support is a forest of paths whose endpoints are terminals or route-divergence vertices. The enriched state and side-root word along each path must still be retained.

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

Then `u=k\ell` is a root disjoint from `r`. Define the coefficient chain

\[
h^\sharp=h+r1_I.
\]

On `A\setminus B`, `B\setminus A`, and `I`, the nonzero coefficients of `h^\sharp` are respectively

\[
s,\qquad t,\qquad u,
\]

and are all roots.

Let

\[
D=\{v\in V_{\mathrm{int}}(P):\deg_I(v)=1\}
\]

be the route-divergence set. Since both witnesses use every terminal semiedge,

\[
\partial I=T+D.
\]

### Theorem 5.1 — exact root-plus-binary coefficient decomposition

\[
\boxed{
h=h^\sharp+r1_I,}
\]

where `h^sharp` is root-supported as a coefficient chain and

\[
\boxed{
\partial h^\sharp=uT+rD.
}
\]

The entire failure of `h^sharp` to be a root-valued relative **flow** is the binary `r`-boundary on the divergence set `D`. The overlap `I` is an explicit `T\cup D`-join carrying that binary coefficient fibre.

### Trust boundary

The operation `h -> h^sharp` is a coefficient identity. It does not assert that adding `r` on every overlap edge preserves root-admissibility relative to the base flow. The enriched states of Theorem 4.2 determine that edgewise question.

---

## 6. Exact collision classification

For repair channels in `S_r`, subtraction has only the following coefficient outcomes.

### Corollary 6.1

1. **Same resolution class:** root-supported subtraction.
2. **Different classes, same orientation:** root-supported subtraction.
3. **Different classes, opposite orientation:** co-root-overlap subtraction with a uniform coefficient one-factor shadow, equivalently a root-supported coefficient chain plus one binary `r`-fibre.

No fourth coefficient-value mechanism can appear.

This closes the finite algebraic part of witness subtraction. It does not close graph composition, because Case 3 retains the full enriched root-pair and side-output word of the base witnesses.

---

## 7. Relation to route automata

Suppose a current four-pole state and challenge admit more than one physical route witness.

- In Cases 1 and 2, their difference is root-supported at coefficient level. A deterministic residual kernel should then either admit a profile-expanding genuine transition or expose a smaller source interface, but this must be proved with the actual base cover.
- In Case 3, the coefficient difference has only one co-root direction, but the overlap carries an enriched transport state. Localisation may end in a DDD atom, a flat equality/defect strip, a smaller separator, or a solvable route switch; the repeated coefficient shadow alone does not choose among them.

Accordingly, a non-permutation resolution-route relation cannot create a new **coefficient alphabet**, but its physical composition semantics remain nontrivial.

---

## 8. Remaining proof obligations

### Obligation A — boundary-transition compatibility

Prove that a root-supported subtraction between two genuine route witnesses gives an actual Kempe/profile transition or exposes a smaller cyclic separator. Preserve edgewise admissibility relative to the base cover and the support-unordered boundary state.

### Obligation B — enriched-overlap localisation

For the disjoint branch, retain the state sequence

\[
\{y_e,z_e\}
\]

and side-root output word along every overlap component. Prove one of:

1. the enriched word admits a crossed/root resolution and profile escape;
2. a first repeated enriched state with compatible side semantics yields a composition-safe contraction;
3. incompatible return produces a nontrivial `C_2`/DDD holonomy on a bounded blossom;
4. a smaller separator, zero-equality tree, or defect-forest unit is exposed.

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
- the adjacent/disjoint coefficient dichotomy;
- the complete local coefficient-pattern classification;
- the uniform coefficient one-factor reduction;
- the base-dependent disjoint-root-pair transport law;
- the root-plus-binary coefficient decomposition;
- the three-case coefficient collision classification for `S_r`.

### Still open

- automatic profile expansion from every root-supported subtraction;
- contraction or resolution of the enriched overlap transducer;
- localisation of every nontrivial return to a bounded DDD blossom;
- the physical permutation-connection theorem;
- Type T strict descent, Type H closure, horizontal/global induction, and the global five-support theorem.
