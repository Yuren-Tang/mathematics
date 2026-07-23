# The ten-state boundary graph and fixed-route rigidity

## Research Lead compression theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `9d01429fc635dc314d04d555be5606c8f3fd8b4d`.

**Parents:**

- `FOUR_POLE_CAP_LIBRARY_TEN_STATE_PROFILES_V1.md`;
- `THREE_RECONNECTION_FIXED_ROUTE_REDUCTION_V1.md`;
- `five-support/cuts-four-poles-and-routing.md`.

**Purpose:** replace the repeated ten-state route tables in the main proof architecture by one labelled boundary graph theorem. The complete row table remains a finite certificate, but the logical content needed by the five-CDC proof is the decomposition

\[
P_3\sqcup C_4\sqcup P_3
\]

for every fixed terminal route.

**Status:** exact authorial compression of the existing finite classification. This dossier adds no independent assurance. PDL must still reconstruct the ten support-unordered states, verify every labelled route row, and prove that physical Kempe switching induces the stated graph.

---

## 1. The ten support-unordered states

Let

\[
\mathcal S
=
\{A,B_0,B_1,B_2,C_0,C_1,C_2,D_0,D_1,D_2\}
\]

be the complete support-unordered boundary state set of an ordered cubic four-pole.

Let

\[
M_0,M_1,M_2
\]

be the three perfect matchings of its four ordered terminal incidences.

For a fixed matching index `i`, write

\[
\{i,j,k\}=\{0,1,2\}.
\]

Define

\[
\boxed{
J_i=\{A,B_i,C_i\},
}
\]

\[
\boxed{
K_i=\{B_j,B_k,D_j,D_k\},
}
\]

and

\[
\boxed{
L_i=\{C_j,D_i,C_k\}.
}
\]

These sets are pairwise disjoint and partition `mathcal S`.

Their graph shapes will be written

\[
J_i:\quad A-B_i-C_i,
\]

\[
K_i:\quad B_j-B_k-D_j-D_k-B_j,
\]

and

\[
L_i:\quad C_j-D_i-C_k.
\]

The cyclic order displayed for `K_i` is immaterial up to reversal and exchange of `j,k`.

---

## 2. The fixed-route transition graph

For one matching `M_i`, define the undirected graph

\[
\Gamma_i
\]

on vertex set `mathcal S` as follows. Two distinct states are adjacent when one complementary support-pair challenge, routed physically through terminal matching `M_i`, changes one state to the other. Multiple challenge rows with the same state endpoints are collapsed to one graph edge.

### Theorem 2.1 — boundary graph decomposition

For every `i`,

\[
\boxed{
\Gamma_i
=
J_i\sqcup K_i\sqcup L_i
\cong
P_3\sqcup C_4\sqcup P_3.
}
\]

More explicitly:

1. the first component is
   \[
   A-B_i-C_i;
   \]
2. the middle component is the four-cycle on
   \[
   B_j,B_k,D_j,D_k;
   \]
3. the last component is
   \[
   C_j-D_i-C_k.
   \]

No `M_i`-routed challenge edge joins two different displayed components.

### Proof certificate

For `i=0`, the complete route table reduces to

\[
A-B_0-C_0,
\]

\[
B_1-B_2-D_1-D_2-B_1,
\]

and

\[
C_1-D_0-C_2.
\]

The cases `i=1,2` follow by permuting the three terminal matchings. The full labelled route rows, including repeated challenge instances, remain the reproducible finite certificate.

---

## 3. Completion gadgets are graph components

Let `E_i` be the zero-vertex reconnection using matching `M_i`, and let `cap_i` be the standard two-vertex cap using the same matching.

Their exact profiles are

\[
\boxed{
\Sigma(E_i)=J_i
}
\]

and

\[
\boxed{
\Sigma(cap_i)=K_i.
}
\]

Thus the direct reconnection and the cap are not arbitrary subsets of the ten-state space. They are respectively:

- one outer path of `Gamma_i`;
- the middle four-cycle of `Gamma_i`.

The remaining outer path `L_i` is the only complete boundary sector not realised by either of these two matching-`i` completion gadgets.

---

## 4. Physical profiles and challenge closure

Let `P` be an ordered four-pole and

\[
\Sigma(P)\subseteq\mathcal S
\]

its complete physical boundary profile.

For every realised labelled boundary trace and every complementary support-pair challenge, the actual symmetric-difference subgraph has one physical terminal matching. Switching the relevant component produces another realised state of `P`.

Consequently `Sigma(P)` is not merely an abstract set of coefficient orbits. It is closed under the targets of all actual labelled challenge rows.

This distinction is essential: the graph `Gamma_i` records the `M_i` target of each row, while physical route rigidity additionally asserts that the other two matching targets are not physically chosen in the blocked sector.

---

## 5. Blocked-cap rigidity from the graph

Assume

\[
\Sigma(P)\cap J_r\ne\varnothing
\qquad(r=0,1,2)
\]

and fix `i` such that

\[
\Sigma(P)\cap K_i=\varnothing.
\]

Since

\[
\mathcal S\setminus K_i=J_i\sqcup L_i,
\]

all realised states lie on the two outer paths of `Gamma_i`.

### Lemma 5.1 — the first outer path is forced

Because `Sigma(P)` meets `J_i`, challenge closure and the exact labelled rows force the complete path

\[
\boxed{J_i\subseteq\Sigma(P).}
\]

In particular

\[
A\in\Sigma(P).
\]

Since `A` belongs to every direct-reconnection profile `J_r`, the already forced component `J_i` meets all three `J_r`. No additional component is required by the three-reconnection hypotheses.

### Lemma 5.2 — the second outer path is all or nothing

If `Sigma(P)` contains any state of `L_i`, the exact challenge rows force both adjacent states and hence

\[
\boxed{L_i\subseteq\Sigma(P).}
\]

If it contains none, the entire component is absent.

### Theorem 5.3 — graph form of the cap-blocking classification

Under the stated hypotheses,

\[
\boxed{
\Sigma(P)=J_i
\quad\text{or}\quad
\Sigma(P)=J_i\cup L_i.
}
\]

There is no third Kempe-closed physical profile avoiding `K_i` and meeting all three direct-reconnection profiles.

---

## 6. Why the route is uniquely `M_i`

The decomposition into connected components of `Gamma_i` is not by itself the entire physical theorem. The complete labelled row table has the stronger property:

> for every complementary support-pair challenge based at a state of `J_i\cup L_i`, exactly one of its three matching targets remains in `J_i\cup L_i`, and that target is the `M_i` target.

The other two route targets lie in the forbidden middle component `K_i` or outside the selected outer component in a way excluded by closure.

### Theorem 6.1 — physical fixed-route rigidity

If

\[
\Sigma(P)=J_i
\quad\text{or}\quad
\Sigma(P)=J_i\cup L_i,
\]

then every realised complementary support-pair challenge in `P` has physical terminal matching

\[
\boxed{M_i.}
\]

Thus

\[
\boxed{
\text{three soluble reconnections}
+
\text{blocked }cap_i
\Longrightarrow
\text{one globally fixed physical route }M_i.
}
\]

### Proof

For one labelled challenge row, the actual switch target must remain in the complete physical profile. The exact finite table shows that among its three matching targets only the `M_i` target lies in the permitted outer sector. Therefore the actual route is `M_i`. Apply this to every realised row. ∎

---

## 7. Conceptual meaning

The ten-state theorem is a boundary convexity statement in a finite transition graph.

- `J_i` is the direct-pairing singular path:
  \[
  \text{equality}
  -
  \text{intersecting roots}
  -
  \text{disjoint roots};
  \]
- `K_i` is the cap-compatible middle cycle;
- `L_i` is the opposite singular outer path.

Meeting all three smaller reconnections supplies access to the outer state space. Avoiding the cap removes the middle cycle. Kempe closure then leaves one or both complete outer paths, and the route label is forced.

This is the finite boundary mechanism behind the full-channel theorem. Equality and DDD are already joined on the same outer path before any global descent begins.

---

## 8. Main-proof use

The eventual proof should use this theorem in one line:

> The three smaller reconnection covers make `Sigma(P)` meet every `J_r`. If the original cap profile `K_i` is missed, Theorems 5.3 and 6.1 force `Sigma(P)=J_i` or `J_i union L_i`, with every challenge physically routed by `M_i`.

The full ten-state route table should be moved to a finite-certificate appendix or machine-checkable enumeration.

---

## 9. PDL reconstruction obligations

PDL should verify Package C in this order:

1. derive the ten support-unordered states from five even terminal traces;
2. derive every direct-reconnection profile `J_i`;
3. derive every cap profile `K_i`;
4. enumerate the labelled complementary support-pair challenge rows;
5. prove `Gamma_i=P_3 sqcup C_4 sqcup P_3`;
6. prove the all-or-nothing closure of its outer components;
7. prove that the unique surviving target in every blocked-sector row is the physical `M_i` route.

Only Item 7 uses physical labelled-route information beyond abstract graph adjacency.

---

## 10. Trust boundary

### Exact authorial content compressed here

- the ten-state partition `J_i sqcup K_i sqcup L_i`;
- the fixed-route graph `P_3 sqcup C_4 sqcup P_3`;
- direct reconnection as one outer path;
- cap compatibility as the middle cycle;
- blocked-profile classification `J_i` or `J_i union L_i`;
- unique physical route `M_i` on the blocked outer sector.

### Not added here

- independent verification of the route table;
- a replacement for the labelled finite certificate;
- the all-three reconnection category theorem;
- elimination of the fixed-route lock;
- canonical acceptance, Lean verification, manuscript integration, release, peer review, or publication.
