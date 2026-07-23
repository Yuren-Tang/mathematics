# The same-matching direct terminal resolves from a zero bridge to a root theta

## Research dossier v1 — bounded-terminal scope repair

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `4cea8916262f310dffd81aad765817392a3eabfd`.

**Parents:**

- `BOUNDED_DIRECT_PAIRING_CAP_TERMINAL_V1.md`;
- `PACHNER_HISTORY_FIRST_FAILURE_ONE_EDGE_ATOM_V1.md`;
- `ROOT_SURGERY_AUTOMATIC_CATEGORY_SAFETY_V1.md`;
- `CONTEXTUAL_TRANSFER_REPAIRED_AUTHORITY_V2.md`;
- the four-root `(0,2,2)` pairing-sum classification.

**Corrects:** the reading of the cap-block terminal `M_i` as an immediate descendant “category exit” sufficient for the original cap problem.

**Status:** exact repair of the zero-vertex same-matching terminal. Closing the direct matching `M_i` by the original cap gives two loops joined by one bridge. Assign distinct intersecting roots `p,q` to the two loops and value zero to the central bridge. This is an `E_5` flow with one zero atom. The four branch values around that atom are `p,p,q,q`; either crossed topology has central root `p+q` and turns the graph into the two-vertex theta multigraph with three root-valued parallel edges. Hence every direct-pairing terminal—same or cross matching—supplies a cap-compatible root-valued theta terminal. That terminal is then returned through the finite surgery history by contextual inverse transfer. No descendant category exit is required.

**Assurance boundary:** this theorem repairs the terminal interface only. It assumes the repaired contextual-transfer theorem for return to the original four-pole.

---

## 1. Same-matching cap closure

Let the original two-vertex cap have blocks

\[
M_i=12\mid34.
\]

Suppose the reduced zero-vertex four-pole is the same matching `M_i`.

Closing by the cap produces two cap vertices `x,y`:

- the matching edge `12` becomes one loop at `x`;
- the matching edge `34` becomes one loop at `y`;
- the cap central edge joins `x` and `y`.

As an unlabelled graph this is two loops joined by one bridge.

It has no nowhere-zero root flow, because the bridge of any flow must carry zero. This fact alone does not solve the original cap problem; it only identifies the exact singular terminal topology.

---

## 2. A one-zero terminal flow

Choose roots

\[
p,q\in R_5
\]

which are distinct and intersect in exactly one support index. For example,

\[
p=12,
\qquad
q=13.
\]

Assign:

\[
\boxed{
\text{loop at }x=p,
\qquad
\text{loop at }y=q,
\qquad
xy=0.}
\]

### Lemma 2.1 — terminal flow equation

This is an `E_5` flow on the loop-bridge graph.

### Proof

At `x`, the loop contributes its value twice and hence contributes zero in characteristic two. The central edge also has value zero. Thus the vertex sum is zero. The same holds at `y`. ∎

Every edge except the central bridge is root-valued. The central edge is one normalized zero atom.

---

## 3. The local `(0,2,2)` triality

Cut the central zero edge. At `x`, the two remaining incidences are the two ends of the `p` loop; at `y`, they are the two ends of the `q` loop. Hence the ordered four-branch multiset is

\[
\boxed{p,p,q,q.}
\]

Its three binary topologies have central values:

1. pair `p` with `p` and `q` with `q`:
   \[
   0;
   \]
2. first crossed pairing:
   \[
   p+q;
   \]
3. second crossed pairing:
   \[
   p+q.
   \]

Because `p,q` are distinct intersecting roots,

\[
\boxed{r=p+q\in R_5.}
\]

Thus the exact triality is

\[
\boxed{(0,2,2).}
\]

---

## 4. Cross resolution gives theta

Perform either crossed NNI resolution of the zero central topology.

Each former loop is opened and paired crosswise with one incidence from the other cap vertex. The two matching edges now both join `x` to `y`. Together with the new central edge of value `r=p+q`, the graph is the theta multigraph

\[
\Theta_3
\]

with three parallel edges.

Their root values are

\[
\boxed{p,q,p+q.}
\]

At both vertices,

\[
p+q+(p+q)=0.
\]

### Theorem 4.1 — same-matching terminal rootification

The loop-bridge direct terminal admits one root NNI to a root-valued theta terminal.

The move changes no exterior data, since the zero-vertex four-pole has no internal exterior attachment beyond the four cap incidences.

By `ROOT_SURGERY_AUTOMATIC_CATEGORY_SAFETY_V1.md`, the root-valued theta output is connected and bridgeless.

---

## 5. Unified direct-terminal theorem

There are three zero-vertex matchings.

### Cross terminal `M_j` or `M_k`

Closing by the cap is already `Theta_3`; assign any root triangle to its three parallel edges.

### Same terminal `M_i`

Closing by the cap is the zero bridge terminal of Section 2; resolve it by Theorem 4.1 to `Theta_3`.

Therefore:

### Theorem 5.1 — every direct terminal is cap-compatible

Every zero-vertex direct-pairing terminal yields, after at most one zero-to-root NNI, a root-valued flow on a cap-attached two-vertex theta descendant.

There is no residual bridge/category endpoint.

---

## 6. Return through the history

Let

\[
P_0\to P_1\to\cdots\to P_m
\]

be the forward equality/DDD root-surgery history and suppose `P_m` is a zero-vertex direct matching.

Theorem 5.1 supplies a root-valued cap-compatible terminal state on the bounded descendant. Apply `CONTEXTUAL_TRANSFER_REPAIRED_AUTHORITY_V2.md` to the reverse history.

Exactly one of:

1. the theta state returns to a root-valued state on `P_0` in the original cap profile;
2. a route/profile terminal is reached and returned;
3. strict target-order descent occurs.

All outcomes produce the original cap lift after the established well-founded recursion.

### Corollary 6.1 — corrected bounded-terminal disposition

The bounded direct-pairing branch is not

\[
\text{theta solution or category exit}.
\]

Its exact authorial disposition is

\[
\boxed{
\text{cap-compatible theta terminal}
\longrightarrow
\text{contextual return}.}
\]

---

## 7. Correction to older wording

Read the same-matching branch of `BOUNDED_DIRECT_PAIRING_CAP_TERMINAL_V1.md` as follows:

- the loop/bridge census is correct;
- the bridge identifies a zero singular fibre, not a final original-graph discharge;
- choose distinct intersecting loop roots;
- cross-resolve the zero bridge to the root theta;
- use the theta as the bounded terminal input for contextual transfer.

This removes the final descendant-category shortcut from the full-channel proof.

---

## 8. Trust boundary

### Exact here

- explicit one-zero flow on the loop-bridge graph;
- exact `p,p,q,q` local boundary;
- `(0,2,2)` pairing table;
- one-step root NNI to the theta graph;
- unified cap-compatible theta terminal for all three direct matchings;
- corrected contextual-return interface.

### Imported authorial mathematics

- first-failure zero-atom grammar;
- root NNI category safety;
- repaired contextual inverse transfer.

### Not claimed

- downstream proof development or independent verification;
- canonical acceptance;
- Lean verification;
- manuscript integration;
- release, arXiv, DOI, peer review, or publication.
