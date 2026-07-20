# AC-PD-A — Audit A explicitness repairs for Programme A

**Proof-development state:** `COMPLETE-DRAFT / AUDIT-A-REPAIR`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Controlling intake:** `Yuren-Tang/research-workbench#37`, comment `5019649863`  
**Audit source:** `AC-AUDIT-A`, issue `Yuren-Tang/research-workbench#35`  
**Immutable authorial Programme A source:** `proof-development/affine-cdc-rigour-v1@8bee16780b549f51e1f29343671a059961ec4172`  
**Initial canonical baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Classification:** `EXPOSITORY-REPAIR / NO-THEOREM-CHANGE / NO-NEW-MATHEMATICS`  
**Immediate consumer:** `Mathematics — Curator` (`MATH-CUR`)

## 0. Repair scope and authority

Independent Audit A classified the complete CDC theorem spine as

`VERIFIED SUBJECT TO NAMED EXTERNAL THEOREMS / NON-BLOCKING EXPLICITNESS REPAIRS`.

The present bounded epoch closes exactly the three returned explicitness items:

1. make the multigraph convention of the Seymour six-flow input explicit in controlling A3;
2. replace the compressed reverse direction of the A4 local-family classification by a complete algebraic reconstruction;
3. mark the older Tutte route in `reduction/outer-shell-and-binary-flow.md` as a non-controlling historical alternative.

This dossier is a controlling repair overlay for Programme A on the owned PDL branch. For interpretation of the live branch, the three passages identified below are to be read with the exact replacements in this file. The immutable source checkpoint remains recoverable and is not rewritten.

No theorem statement, hypothesis, conclusion, affine construction, collapse argument, circuit decomposition, or multiplicity calculation is changed. No B-programme claim is altered. No `main`, Curator, Research Lead, audit, Lean, manuscript, release, tag, arXiv, DOI, or publication surface is moved.

## 1. Repair A-AUDIT-A-1 — exact Seymour multigraph convention

### 1.1 Passage repaired

This subsection supplies the explicit convention required at `AC_PD_A3_BINARY_EIGHT_FLOW_BOUNDARY.md`, External Theorem 3.1 and its componentwise application.

### 1.2 Exact external input used by A3

The external theorem is used in the following form.

> **Seymour six-flow input, exact graph class.** Let `G` be a finite connected loopless multigraph. Parallel edge objects are permitted. If `G` has no isthmus, then, after orienting its edges, there is an integer circulation
> \[
> z:E(G)\to\mathbf Z
> \]
> satisfying
> \[
> \partial_{\mathbf Z}z=0,
> \qquad
> 0<|z_e|<6
> \]
> for every edge `e`.

The accessible proof of DeVos–Rollová–Šámal fixes exactly this convention at the start of §1: parallel edges are permitted and loops are forbidden; its Theorem 2 states that every 2-edge-connected graph has a nowhere-zero six-flow. Thus no silent simple-graph reduction is being used.

The primary Seymour abstract states the theorem for every graph with no isthmus. The modern source above supplies the explicit graph convention needed by the present multigraph corpus.

### 1.3 Translation to the A3 input class

A3 begins with a finite loopless multigraph `G` having no singleton cut, without assuming connectedness.

Let

\[
G_1,\ldots,G_r
\]

be its edge-bearing connected components. By A0's bridge/singleton-cut equivalence, each `G_j` has no isthmus. Since each `G_j` is connected, this is exactly the 2-edge-connected condition used in the modern six-flow source. Apply the theorem independently to each `G_j` and take the disjoint union of the resulting oriented integer flows.

Parallel edges remain distinct coordinates throughout. They create no ambiguity in orientation, Kirchhoff conservation, range bounds, modular reduction, or the later flow-count formula.

Isolated vertices contribute no edge coordinate and no nontrivial conservation equation. The empty active graph has the unique empty flow. Loops are absent because A1 has already passed to the loopless core.

Consequently the exact A3 external boundary is:

\[
\boxed{
\text{finite loopless multigraph, parallel edges allowed, no singleton cut}
\Longrightarrow
\text{nowhere-zero integral six-flow componentwise}.}
\]

There is no hidden connectedness assumption and no hidden prohibition of parallel edges.

### 1.4 Logical dependency remains unchanged

After the external input, every remaining A3 step is internal:

\[
\begin{aligned}
&\text{integral six-flow}
\\&\Longrightarrow \text{integral eight-flow by range inclusion}
\\&\Longrightarrow \mathbf Z/8\mathbf Z\text{-flow by reduction modulo eight}
\\&\Longrightarrow \mathbf F_2^3\text{-flow by the proved equal-order count formula}
\\&\Longrightarrow \text{unoriented characteristic-two incidence flow}.
\end{aligned}
\]

Thus this repair adds an explicit source convention; it does not add a new theorem premise.

## 2. Repair A-AUDIT-A-2 — complete reverse reconstruction in A4

### 2.1 Passage repaired

This subsection replaces the compressed converse paragraph in `AC_PD_A4_AFFINE_PAIR_COMPLEX.md`, Proposition 4.2, proving that every local even line family is uniquely a deleted-point family `\Phi_v(m)`.

### 2.2 Local notation

Fix a cubic vertex `v`. Write the three distinct nonzero flow directions as

\[
h_1,h_2,h_3\in\Gamma,
\qquad
h_1+h_2+h_3=0.
\]

Hence

\[
h_3=h_1+h_2,
\qquad
W_v=\{0,h_1,h_2,h_3\}.
\]

A local line family `P` chooses, for each `i\in\{1,2,3\}`, one affine line

\[
L_i=a_i+\langle h_i\rangle
=\{a_i,a_i+h_i\}.
\]

The family is **even** when every point of `\Gamma` lies on an even number of the three selected lines.

Two affine lines of distinct directions meet in at most one point: if they shared two distinct points, the difference of those points would be the unique nonzero vector in both direction subspaces, forcing the directions to be equal.

### 2.3 Forward direction

For `m\in\Gamma`, define

\[
\begin{aligned}
L_1(m)&=m+h_2+\langle h_1\rangle
      =\{m+h_2,m+h_3\},\\
L_2(m)&=m+h_1+\langle h_2\rangle
      =\{m+h_1,m+h_3\},\\
L_3(m)&=m+h_1+\langle h_3\rangle
      =\{m+h_1,m+h_2\}.
\end{aligned}
\]

Equivalently, the quotient coordinate in direction `h_i` is

\[
[m]_{h_i}+\kappa_{h_i},
\]

where `\kappa_{h_i}` is the common quotient class of the other two local directions.

The three points

\[
m+h_1,\quad m+h_2,\quad m+h_3
\]

are each covered twice, and every other point is covered zero times. Hence `\Phi_v(m)` is even.

### 2.4 Reverse direction: explicit intersection reconstruction

Let `P=(L_1,L_2,L_3)` be any even local family.

Choose either point `x` of `L_1`. Since `x` already lies on one selected line, evenness forces it to lie on exactly one of `L_2` and `L_3`: it cannot lie on neither, which would give multiplicity one, and it cannot lie on both, which would give multiplicity three.

Apply the same argument to the other point of `L_1`. Because a line of direction `h_2` or `h_3` can meet `L_1` in at most one point, the two points of `L_1` are distributed one to `L_2` and one to `L_3`. Therefore there are unique points

\[
x_{12}=L_1\cap L_2,
\qquad
x_{13}=L_1\cap L_3,
\]

and, after naming them in this way,

\[
x_{13}=x_{12}+h_1.
\]

The second point of `L_2` is

\[
x_{23}:=x_{12}+h_2.
\]

It is not on `L_1`, since `L_1` and `L_2` already meet at `x_{12}` and their directions are distinct. At `x_{23}`, the line `L_2` contributes multiplicity one, so evenness forces `x_{23}\in L_3`. Hence

\[
L_3=\{x_{13},x_{23}\}.
\]

This is consistent with its prescribed direction because

\[
x_{13}+x_{23}
=(x_{12}+h_1)+(x_{12}+h_2)
=h_1+h_2
=h_3.
\]

Define the deleted point

\[
m:=x_{12}+h_3.
\]

Then

\[
\begin{aligned}
x_{12}&=m+h_3,\\
x_{13}&=x_{12}+h_1=m+h_2,\\
x_{23}&=x_{12}+h_2=m+h_1.
\end{aligned}
\]

Therefore

\[
\begin{aligned}
L_1&=\{x_{12},x_{13}\}
   =\{m+h_3,m+h_2\}
   =m+h_2+\langle h_1\rangle,\\
L_2&=\{x_{12},x_{23}\}
   =\{m+h_3,m+h_1\}
   =m+h_1+\langle h_2\rangle,\\
L_3&=\{x_{13},x_{23}\}
   =\{m+h_2,m+h_1\}
   =m+h_1+\langle h_3\rangle.
\end{aligned}
\]

Thus

\[
P=\Phi_v(m).
\]

### 2.5 Uniqueness

If `\Phi_v(m)=\Phi_v(m')`, then in each direction `h_i`

\[
[m+m']_{h_i}=0,
\]

so

\[
m+m'\in
\langle h_1\rangle\cap
\langle h_2\rangle\cap
\langle h_3\rangle
=\{0\}.
\]

Hence `m=m'`.

We have therefore proved the exact bijection

\[
\boxed{
\Gamma\xrightarrow{\ \sim\ }
\{\text{even local line families at }v\},
\qquad
m\longmapsto\Phi_v(m).}
\]

When `\Gamma=\mathbf F_2^3`, this gives exactly eight local families. The proof above is stronger than an eight-row table because it works uniformly for every ambient finite-dimensional `\mathbf F_2`-space used by A4.

## 3. Repair A-AUDIT-A-3 — status of the old Tutte route

### 3.1 Passage reclassified

The route in

`projects/affine-cdc/reduction/outer-shell-and-binary-flow.md`, §§4.1–4.2,

which passes from an integral eight-flow to an `\mathbf F_2^3`-flow by citing Tutte's equal-order theorem, is retained only as a **historical alternative derivation**.

It is not the controlling Programme A proof route and is not a logical dependency of the current complete CDC spine.

### 3.2 Controlling route

The controlling authorial proof is A3:

\[
\text{Seymour integral six-flow}
\Longrightarrow
\text{integral eight-flow}
\Longrightarrow
\mathbf Z/8\mathbf Z\text{-flow}
\Longrightarrow
\mathbf F_2^3\text{-flow}.
\]

The final implication is proved internally by the explicit formula

\[
N_G(A)
=
\sum_{B\subseteq E(G)}
(-1)^{|E|-|B|}
|A|^{|B|-|V|+c(B)},
\]

which shows that the number, and therefore the existence, of nowhere-zero `A`-flows depends only on `|A|`.

Accordingly:

- Tutte's equal-order theorem is provenance, not an opaque premise;
- the old outer-shell §4.1 chain must not be cited as the controlling proof;
- any source-localization ambiguity in that old companion does not block Programme A;
- the old route remains mathematically compatible when stated with an exact equal-order theorem, but it has no authority to override A3.

### 3.3 Exact corpus status sentence

For all future integration and citation, the old companion is to carry the following status:

> **Historical-route notice.** Sections 4.1–4.2 retain an earlier Tutte-based derivation for provenance only. The controlling complete-CDC proof uses `AC_PD_A3_BINARY_EIGHT_FLOW_BOUNDARY.md`, where modular reduction and equal-order transport are proved internally. No theorem in the active Programme A spine depends on the old Tutte route.

## 4. Repair closure table

| Audit item | Repaired object | Closure |
|---|---|---|
| Seymour graph convention | A3 External Theorem 3.1 | finite connected loopless multigraph; parallel edges allowed; componentwise extension explicit |
| A4 reverse classification | A4 Proposition 4.2 converse | complete pairwise-intersection reconstruction and uniqueness proof |
| old Tutte route status | outer-shell §§4.1–4.2 | historical alternative; non-controlling; A3 is authoritative |

All three items are `CLOSED / EXPOSITORY-REPAIR`.

## 5. Theorem and assurance status after repair

Programme A remains a complete authorial paper-level proof of the finite-active-edge Cycle Double Cover theorem, subject only to its named classical Seymour six-flow input. Audit A's three returned items alter exposition and dependency visibility only.

This repair does not claim:

- Lean formalization of the complete theorem;
- independent re-audit of this repair checkpoint;
- canonical integration;
- manuscript acceptance;
- release, publication, arXiv, or DOI status;
- completion of the five-support strengthening.

The five-support frontier and its six exact AC-RL obligations remain unchanged.