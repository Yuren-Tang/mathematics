# Programme A — Audit A explicitness repairs

## 1. Status and exact provenance

This chapter is the controlling integrated projection of the Programme A repair overlay

`proof-development/affine-cdc-rigour-v1@06bce656dcf5bfd6491ec08f51a702ea56d2470d`

from

`proof-development/AC_PD_A_AUDIT_A_EXPLICITNESS_REPAIRS.md`.

The immutable authorial Programme A source remains

`proof-development/affine-cdc-rigour-v1@8bee16780b549f51e1f29343671a059961ec4172`.

Independent Audit A classified the theorem spine as

`VERIFIED SUBJECT TO NAMED EXTERNAL THEOREMS / NON-BLOCKING EXPLICITNESS REPAIRS`.

The three repairs below are

`CLOSED / EXPOSITORY-REPAIR / NO-THEOREM-CHANGE / NO-NEW-MATHEMATICS`.

They alter no theorem statement, hypothesis, conclusion, affine construction, collapse argument, circuit decomposition, or multiplicity calculation.

## 2. Exact Seymour multigraph convention

The controlling A3 external input is used in the following form.

> **Seymour six-flow input.** Let $G$ be a finite connected loopless multigraph. Parallel edge objects are permitted. If $G$ has no isthmus, then, after orienting its edges, there is an integer circulation
> $$
> z:E(G)\to\mathbf Z
> $$
> satisfying
> $$
> \partial_{\mathbf Z}z=0,
> \qquad
> 0<|z_e|<6
> $$
> for every edge $e$.

The modern proof of DeVos–Rollová–Šámal fixes the required graph convention explicitly: parallel edges are allowed, loops are forbidden, and every 2-edge-connected graph has a nowhere-zero six-flow. The primary Seymour statement supplies the classical theorem; the modern source removes any silent simple-graph convention.

Programme A applies this input as follows.

Let $G$ be a finite loopless multigraph with no singleton cut. Write

$$
G_1,\ldots,G_r
$$

for its edge-bearing connected components. By the bridge/singleton-cut equivalence, every $G_j$ has no isthmus. Apply Seymour independently to each $G_j$ and take the disjoint union of the resulting oriented integer flows.

Parallel edges remain distinct coordinates throughout orientation, conservation, range inclusion, modular reduction, and the later flow-count formula. Isolated vertices contribute no edge coordinate and no nontrivial conservation equation. The empty active graph has the unique empty flow. Loops are absent because A1 has already passed to the loopless core.

Consequently the exact A3 boundary is

$$
\boxed{
\text{finite loopless multigraph, parallel edges allowed, no singleton cut}
\Longrightarrow
\text{componentwise nowhere-zero integral six-flow}.}
$$

There is no hidden connectedness hypothesis and no hidden prohibition of parallel edges.

After this external input, every remaining A3 step is internal:

$$
\begin{aligned}
&\text{integral six-flow}
\\&\Longrightarrow \text{integral eight-flow by literal range inclusion}
\\&\Longrightarrow \mathbf Z/8\mathbf Z\text{-flow by modular reduction}
\\&\Longrightarrow \mathbf F_2^3\text{-flow by the internal equal-order count formula}
\\&\Longrightarrow \text{unoriented characteristic-two incidence flow}.
\end{aligned}
$$

Thus Seymour remains the sole non-elementary external logical input.

## 3. Complete reverse reconstruction of local affine families

Fix a cubic vertex $v$ and write the three distinct nonzero flow directions as

$$
h_1,h_2,h_3\in\Gamma,
\qquad
h_1+h_2+h_3=0.
$$

Hence

$$
h_3=h_1+h_2,
\qquad
W_v=\{0,h_1,h_2,h_3\}.
$$

A local line family $P$ chooses, for each $i\in\{1,2,3\}$, one affine line

$$
L_i=a_i+\langle h_i\rangle
=\{a_i,a_i+h_i\}.
$$

The family is **even** when every point of $\Gamma$ lies on an even number of the three selected lines.

Two affine lines of distinct directions meet in at most one point. If they shared two distinct points, the difference of those points would lie in both one-dimensional direction spaces, forcing the directions to agree.

### 3.1 Forward construction

For $m\in\Gamma$, define

$$
\begin{aligned}
L_1(m)&=m+h_2+\langle h_1\rangle
      =\{m+h_2,m+h_3\},\\
L_2(m)&=m+h_1+\langle h_2\rangle
      =\{m+h_1,m+h_3\},\\
L_3(m)&=m+h_1+\langle h_3\rangle
      =\{m+h_1,m+h_2\}.
\end{aligned}
$$

The three points $m+h_1,m+h_2,m+h_3$ are each covered twice and every other point is covered zero times. Hence the family $\Phi_v(m)$ is even.

Equivalently, in the quotient by the direction $h_i$, its coordinate is

$$
[m]_{h_i}+\kappa_{h_i},
$$

where $\kappa_{h_i}$ is the common quotient class of the other two local directions.

### 3.2 Reverse reconstruction

Let $P=(L_1,L_2,L_3)$ be any even local family.

Choose either point $x$ of $L_1$. Since $x$ already lies on one selected line, evenness forces it to lie on exactly one of $L_2$ and $L_3$: lying on neither would give multiplicity one, while lying on both would give multiplicity three.

Apply the same argument to the other point of $L_1$. A line of direction $h_2$ or $h_3$ can meet $L_1$ in at most one point, so the two points of $L_1$ are distributed one to $L_2$ and one to $L_3$. Therefore there are unique points

$$
x_{12}=L_1\cap L_2,
\qquad
x_{13}=L_1\cap L_3,
$$

and, after naming them in this way,

$$
x_{13}=x_{12}+h_1.
$$

The second point of $L_2$ is

$$
x_{23}:=x_{12}+h_2.
$$

It is not on $L_1$, since $L_1$ and $L_2$ have already met at $x_{12}$ and have distinct directions. At $x_{23}$ the line $L_2$ contributes multiplicity one, so evenness forces $x_{23}\in L_3$. Hence

$$
L_3=\{x_{13},x_{23}\}.
$$

This has the prescribed direction because

$$
x_{13}+x_{23}
=(x_{12}+h_1)+(x_{12}+h_2)
=h_1+h_2
=h_3.
$$

Define

$$
m:=x_{12}+h_3.
$$

Then

$$
\begin{aligned}
x_{12}&=m+h_3,\\
x_{13}&=m+h_2,\\
x_{23}&=m+h_1.
\end{aligned}
$$

Therefore

$$
\begin{aligned}
L_1&=\{m+h_3,m+h_2\}=m+h_2+\langle h_1\rangle,\\
L_2&=\{m+h_3,m+h_1\}=m+h_1+\langle h_2\rangle,\\
L_3&=\{m+h_2,m+h_1\}=m+h_1+\langle h_3\rangle.
\end{aligned}
$$

Thus

$$
P=\Phi_v(m).
$$

### 3.3 Uniqueness

If $\Phi_v(m)=\Phi_v(m')$, then for every $i$

$$
[m+m']_{h_i}=0,
$$

so

$$
m+m'\in
\langle h_1\rangle\cap
\langle h_2\rangle\cap
\langle h_3\rangle
=\{0\}.
$$

Hence $m=m'$.

We have proved the exact bijection

$$
\boxed{
\Gamma\xrightarrow{\ \sim\ }
\{\text{even local line families at }v\},
\qquad
m\longmapsto\Phi_v(m).}
$$

When $\Gamma=\mathbf F_2^3$, there are exactly eight local families. The proof works uniformly in every finite-dimensional ambient $\mathbf F_2$-space used by A4.

## 4. Historical status of the older Tutte route

The derivation in

`reduction/outer-shell-and-binary-flow.md`, §§4.1–4.2,

which passes from an integral eight-flow to an $\mathbf F_2^3$-flow by citing Tutte's equal-order theorem, is retained only as a historical alternative.

It is not the controlling Programme A proof route and is not a logical dependency of the complete CDC spine.

The controlling route is A3:

$$
\text{Seymour integral six-flow}
\Longrightarrow
\text{integral eight-flow}
\Longrightarrow
\mathbf Z/8\mathbf Z\text{-flow}
\Longrightarrow
\mathbf F_2^3\text{-flow}.
$$

The final implication is proved internally by

$$
N_G(A)
=
\sum_{B\subseteq E(G)}
(-1)^{|E|-|B|}
|A|^{|B|-|V|+c(B)},
$$

which shows that the number, and therefore the existence, of nowhere-zero $A$-flows depends only on $|A|$.

Accordingly:

- Tutte's equal-order theorem is provenance, not an opaque premise;
- the older outer-shell chain must not be cited as controlling;
- source-localisation ambiguity in that companion does not block Programme A;
- the historical derivation has no authority to override A3.

> **Historical-route notice.** Sections 4.1–4.2 of `reduction/outer-shell-and-binary-flow.md` retain an earlier Tutte-based derivation for provenance only. The controlling complete-CDC proof uses `proof-development/AC_PD_A3_BINARY_EIGHT_FLOW_BOUNDARY.md` together with this integrated repair chapter, where modular reduction and equal-order transport are proved internally. No theorem in the active Programme A spine depends on the old Tutte route.

## 5. Closure and assurance boundary

| Audit item | Controlling repaired object | Closure |
|---|---|---|
| Seymour graph convention | A3 external boundary | finite connected loopless multigraph; parallel edges allowed; componentwise extension explicit |
| A4 reverse classification | A4 local-family converse | complete intersection reconstruction and uniqueness proof |
| old Tutte route | outer-shell §§4.1–4.2 | historical alternative; non-controlling; A3 authoritative |

Programme A remains a complete authorial paper-level proof, subject only to the named Seymour six-flow input. Audit A independently verified the original theorem spine and returned these three non-blocking explicitness items. The repaired passages are now integrated, but this curation act does not claim a second independent re-audit of the repaired prose.

No Lean, manuscript, peer-review, publication, release, arXiv, DOI, novelty, or timestamp status follows from this chapter. Programme B1–B8 and the six open five-support obligations are unchanged.