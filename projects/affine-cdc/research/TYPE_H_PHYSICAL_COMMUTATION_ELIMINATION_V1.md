# Physical commutation also eliminates Type H

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `1c9dd83c6d7078a34921e96b08d8a89b8e54ee7d`  
**Parents:**

- `projects/affine-cdc/five-support/cuts-four-poles-and-routing.md`;
- `projects/affine-cdc/five-support/holonomy-defects-and-atoms.md`;
- `projects/affine-cdc/research/TYPE_T_PHYSICAL_COMMUTATION_ELIMINATION_V1.md`;
- `projects/affine-cdc/research/FOUR_POLE_CAP_LIBRARY_TEN_STATE_PROFILES_V1.md`;
- `projects/affine-cdc/research/TAIT_SURFACE_DDD_ORIENTATION_COMPARISON_V1.md`.

**Status:** exact physical elimination of both Type-H triangle policies in the ten-state four-pole mismatch classification. The BBD triangle and the DDD triangle each require the terminal matching of an untouched disjoint support-pair challenge to change after a switch on another pair. Disjoint-support route invariance forbids this and forces immediate profile escape. Together with the preceding Type-T theorem, all abstract minimal disjoint cap-forced Kempe-closed mismatch kernels are physically impossible. Hence a vertex-minimal bridgeless cubic five-support counterexample has no cyclic four-edge cut and may be assumed cyclically five-edge-connected.  
**Not implied:** the individual full-cap theorem `exists i, K_i subset Sigma(P)` for every four-pole, elimination of every local DDD/equality inverse-lift cell, collapse of the abstract `D_8` cohomology calculation as a mathematical structure, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Recalled physical commutation law

For an indexed cover

\[
\mathcal F=(F_1,\ldots,F_5),
\]

let

\[
X_{rs}=F_r\triangle F_s
\]

be the symmetric-difference subgraph of one complementary support-pair challenge.

If a Kempe switch uses a disjoint support pair `{u,v}`, then `F_r,F_s` are unchanged. Therefore

\[
\boxed{
X_{rs}
\text{ and its terminal matching are unchanged.}
}
\]

The Type-T dossier used this law at the `A` state. The present dossier applies it to the two three-cycle policies that constitute the Type-H side of the exact abstract classification.

---

## 2. The two Type-H triangle orbits

The exact finite four-pole closure classification has Type-H form

\[
P_4\mid C_3.
\]

Up to permutation of the three terminal matchings, the triangle shore belongs to one of two orbits.

### BBD triangle

\[
\boxed{
\Delta_{\mathrm{BBD}}
=
\{B_1,B_2,D_0\}.
}
\]

The other two labelled representatives are obtained by cycling `0,1,2`.

### DDD triangle

\[
\boxed{
\Delta_{\mathrm{DDD}}
=
\{D_0,D_1,D_2\}.
}
\]

The first is the boundary rainbow triangle underlying the BBD monodromy calculation. The second is the exceptional DDD triangle associated with the `D_8` support-label sector.

It is enough to prove that neither triangle can be a physical Kempe-closed profile.

---

## 3. DDD triangle certificate

Use four-bit terminal masks and the labelled trace representative

\[
(S_1,S_2,S_3,S_4,S_5)
=
(12,3,0,10,5).
\]

Its support-unordered boundary state is

\[
D_2.
\]

Choose the disjoint challenges

\[
p=\{1,2\},
\qquad
q=\{4,5\}.
\]

Both are full four-terminal challenges because

\[
12\triangle3=15,
\qquad
10\triangle5=15.
\]

### Route row for `p`

The three route targets from `D_2` are

\[
\begin{array}{c|ccc}
& M_0&M_1&M_2\\
\hline
p& B_1&D_0&C_1.
\end{array}
\]

Inside

\[
\Delta_{\mathrm{DDD}}=\{D_0,D_1,D_2\},
\]

the unique safe route is

\[
M_1,
\]

and the switch reaches `D_0`.

### Route row for untouched `q` before the switch

At the initial `D_2` state,

\[
\begin{array}{c|ccc}
& M_0&M_1&M_2\\
\hline
q& D_1&B_0&C_0.
\end{array}
\]

Thus the unique safe DDD route for `q` is

\[
M_0.
\]

### The contradiction after switching `p`

The `p` switch changes only supports `1,2`. The traces of supports `4,5` remain exactly

\[
(10,5).
\]

Hence the physical route of `q` remains

\[
M_0.
\]

But in the resulting `D_0` state the route targets for the same unchanged challenge are

\[
\begin{array}{c|ccc}
& M_0&M_1&M_2\\
\hline
q& C_2&B_2&D_1.
\end{array}
\]

The DDD triangle would require route `M_2` to stay at `D_1`. The actual unchanged route `M_0` instead produces

\[
\boxed{C_2\notin\Delta_{\mathrm{DDD}}.}
\]

Therefore the DDD triangle escapes.

---

## 4. DDD elimination theorem

### Theorem 4.1 — no locked DDD triangle

No physical four-pole profile can realise

\[
\{D_0,D_1,D_2\}
\]

as a Kempe-closed deterministic routing triangle.

### Proof

The labelled certificate in Section 3 gives two disjoint challenges. Switching the first leaves the second symmetric-difference subgraph unchanged, but the abstract DDD policy requires the second route to change from `M_0` to `M_2`. The unchanged physical route produces `C_2` outside the triangle. ∎

### Interpretation

The nontrivial class

\[
H^1(D_8,E_5)\cong\mathbf F_2
\]

remains a genuine affine support-label phenomenon. What fails is the stronger claim that its three boundary states can form a physically closed four-pole mismatch profile.

The cohomology class may still appear inside a bounded local DDD carrier or along a Type-H transport calculation. It cannot protect a cyclic four-cut by itself.

---

## 5. BBD triangle certificate

Use the labelled trace representative

\[
(S_1,S_2,S_3,S_4,S_5)
=
(0,5,10,15,0).
\]

Its support-unordered state is

\[
B_1.
\]

Choose the disjoint challenges

\[
p=\{1,4\},
\qquad
q=\{2,3\}.
\]

They are full challenges because

\[
0\triangle15=15,
\qquad
5\triangle10=15.
\]

### Route row for `p`

At `B_1`:

\[
\begin{array}{c|ccc}
& M_0&M_1&M_2\\
\hline
p& D_2&C_1&D_0.
\end{array}
\]

Inside

\[
\Delta_{\mathrm{BBD}}=\{B_1,B_2,D_0\},
\]

the unique safe route is

\[
M_2,
\]

and the switch reaches `D_0`.

### Route row for untouched `q` before the switch

At the initial `B_1` state:

\[
\begin{array}{c|ccc}
& M_0&M_1&M_2\\
\hline
q& B_2&A&B_0.
\end{array}
\]

Thus the unique safe BBD route for `q` is

\[
M_0.
\]

### The contradiction after switching `p`

The `p` switch changes only supports `1,4`. The traces of supports `2,3` remain exactly

\[
(5,10).
\]

Hence the physical route of `q` remains

\[
M_0.
\]

At the resulting `D_0` state, the same unchanged challenge has route targets

\[
\begin{array}{c|ccc}
& M_0&M_1&M_2\\
\hline
q& C_2&B_2&D_1.
\end{array}
\]

The BBD triangle would require `M_1` to remain at `B_2`. The actual unchanged route `M_0` produces

\[
\boxed{C_2\notin\Delta_{\mathrm{BBD}}.}
\]

Therefore the BBD triangle escapes.

---

## 6. BBD elimination theorem

### Theorem 6.1 — no locked BBD triangle

No physical four-pole profile can realise

\[
\{B_1,B_2,D_0\}
\]

as a Kempe-closed deterministic routing triangle.

The same holds for its two matching-index permutations.

### Proof

Section 5 gives the canonical contradiction. Permuting the three terminal matchings gives the other two BBD triangles. ∎

### Relation to earlier BBD holonomy

The BBD affine holonomy and its `S_5` generation remain exact statements about the abstract lifted triangle.

The present theorem acts earlier in the proof chain: before a physical four-pole can sustain the full rainbow loop, two disjoint support-pair rows already violate route invariance and force boundary-profile expansion.

Thus the global root-rigidity and simultaneous-origin theorems remain mathematically valid alternate structure, but are no longer needed to eliminate the four-pole Type-H mismatch kernel.

---

## 7. Complete kernel elimination

The exact abstract mismatch classification has only two dynamical types:

1. Type T: `P_5 | P_5`;
2. Type H: `P_4 | C_3`.

The preceding dossier eliminates Type T.

Theorems 4.1 and 6.1 eliminate both Type-H triangle orbits.

### Theorem 7.1 — no physical abstract mismatch kernel

None of the four minimal disjoint cap-forced Kempe-closed profile-pair kernels from the exact ten-state classification is physically realisable.

### Proof

Every kernel pair is, after matching permutation and shore exchange, Type T or Type H.

- Type T is excluded by the `A`-state two-disjoint-challenge theorem.
- Type H has a triangle shore. Its triangle is BBD or DDD, both excluded above.

Therefore no kernel pair survives physical route consistency. ∎

---

## 8. Four-cut gluing consequence

Let a cyclic four-edge cut separate shores `P,Q` in a vertex-minimal bridgeless cubic counterexample.

The existing four-pole theory gives:

1. each complete shore profile is cap-forced;
2. the profiles are closed under every physical support-pair Kempe switch;
3. if the profiles intersect, the shore covers glue;
4. if two cap-forced profiles are disjoint, the exact finite closure reduction contains one of the four minimal mismatch kernel pairs.

Theorem 7.1 rules out the last alternative.

### Theorem 8.1 — physical four-cut intersection

For every cyclic four-edge cut in the minimal-counterexample regime,

\[
\boxed{
\Sigma(P)\cap\Sigma(Q)\ne\varnothing.
}
\]

Hence the shore covers glue.

### Corollary 8.2 — no cyclic four-cut

A vertex-minimal bridgeless cubic counterexample to the five-support statement has no cyclic four-edge cut.

Combined with the established cyclic three-cut gluing theorem, it may be assumed

\[
\boxed{
\text{cyclically five-edge-connected.}
}
\]

### Important scope

This proves the pairwise gluing conclusion needed for minimal-counterexample reduction.

It does not by itself prove the stronger individual profile statement

\[
\forall P\ \exists i:\mathcal K_i\subseteq\Sigma(P).
\]

That full-cap theorem may follow from a refined single-profile analysis, but it is not required for Corollary 8.2 and is not claimed here.

---

## 9. What remains of Type H and DDD

The four-pole mismatch branch is now closed, but several bounded structures remain elsewhere.

### Still meaningful

- one-co-root DDD atoms arising in inverse dipole expansion;
- crossed root resolutions and matching flips;
- the exact identification
  \[
  w_1=\kappa=\nu_X;
  \]
- the exceptional `D_8` affine class as a local orientation-lift phenomenon;
- local Petersen transport inside a bounded defect strip;
- `Y`-route sheet exchange, where
  \[
  \nu_Y=\kappa+\chi.
  \]

### Removed

- an unbounded Type-H four-pole profile protected solely by a BBD or DDD triangle;
- a cyclic four-cut mismatch whose only certificate is the abstract deterministic routing kernel.

Thus DDD has been demoted from an unbounded four-pole obstruction language to a bounded inverse-lift and orientation-transfer atom.

---

## 10. Revised global frontier

After the current sequence of reductions:

1. three-cuts glue;
2. four-cut mismatch kernels are physically impossible;
3. complementary Tait side components peel by one-dipoles;
4. shift-matching bands peel by route-Tait one-dipoles;
5. loss of bridgelessness exposes three-cuts or bounded appendages;
6. low-port negative-Euler cores glue;
7. Type-T and Type-H abstract profile locks both escape.

The remaining burden is no longer an unbounded four-pole routing problem.

It consists of:

\[
\boxed{
\text{bounded equality/DDD/matching-flip transfer}
+
\text{global ordering of graph descent and horizontal flow escape}.
}
\]

A candidate lexicographic measure may now begin with

\[
\bigl(
|V(G)|,
N_T+N_M,
N_{\mathrm{eq}}+N_{\mathrm{DDD}}+N_{\mathrm{flip}},
N_{\mathrm{frame}},
D
\bigr),
\]

without separate Type-T or Type-H four-pole coordinates.

---

## 11. Reproducibility certificate

The two canonical contradictions use only the following finite target triples.

### DDD

Start state `D_2`:

\[
p:(B_1,D_0,C_1),
\qquad
q:(D_1,B_0,C_0).
\]

Switch `p` by `M_1` to `D_0`. The unchanged `q` then has targets

\[
(C_2,B_2,D_1).
\]

Its physical route stays `M_0`, forcing `C_2`.

### BBD

Start state `B_1`:

\[
p:(D_2,C_1,D_0),
\qquad
q:(B_2,A,B_0).
\]

Switch `p` by `M_2` to `D_0`. The unchanged `q` then has targets

\[
(C_2,B_2,D_1).
\]

Its physical route stays `M_0`, again forcing `C_2`.

The matching permutations generate all labelled Type-H triangles.

---

## 12. Trust boundary

### Exact here

- the two Type-H triangle orbits in the exact ten-state kernel classification;
- explicit labelled DDD and BBD disjoint-challenge certificates;
- physical elimination of both triangle policies;
- elimination of every abstract minimal mismatch kernel when combined with the Type-T theorem;
- signature intersection across every cyclic four-cut in the minimal-counterexample regime;
- cyclic five-edge-connectivity of a vertex-minimal counterexample.

### Still open

- the individual universal full-cap-profile theorem for every four-pole;
- composition-safe elimination of bounded equality cells;
- composition-safe elimination of bounded one-co-root DDD cells and matching flips;
- a single global induction theorem combining graph reduction, separator decomposition, and horizontal reconfiguration;
- global five-support existence;
- canonical acceptance, independent audit, Lean verification, manuscript status, release, and publication.
