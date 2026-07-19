# Quartic nucleus transport and pairwise shell factorisation

## 1. Purpose

If all four sheets of a quartic witness design are concentrated, the abstract design peels from level `k` to level `k-1`.

This chapter records the exact algebraic and marked-incidence transport:

- old and residual nuclei are canonically isometric minus-type four-spaces;
- distinguished blocks form the totally singular diagonal graph of that isometry;
- the one-dimensional curvature carrier transports without algebraic twist;
- every pairwise marked witness skeleton grows by one fixed two-vertex shell, adding exactly two cycles.

The symmetry here is the full sheet-coordinate group

$$
AGL(2,2)\cong S_4.
$$

No identification with the support-label `D_8` of a DDD one-factor is assumed.

The shell theorem concerns marked witness edges. Arcs between them may contain further edges of `E_g\setminus\eta`; physically they are transition walks in `\Gamma_g`, not necessarily elementary non-`g` intervals.

## 2. Concentrated design

Let `(X,(\mathcal R_i),(e_i))` be a concentrated quartic design of level `k\ge2`. Put

$$
E=\{e_i:i\in I\},
\qquad
Y=X\setminus E.
$$

For sheet `i`, the distinguished block is

$$
D_i=(E\setminus\{e_i\})\cup\{y_i\},
$$

where the `y_i\in Y` are distinct. The residual families

$$
\mathcal R_i'=\mathcal R_i\setminus\{D_i\}
$$

form a level-`k-1` quartic design on `Y`, omitting `y_i` in sheet `i`.

## 3. Successive nuclei

Define

$$
S_X=\langle s_i:i\in I\rangle,
\qquad
s_i=1_X+e_i,
$$

and

$$
S_Y=\langle t_i:i\in I\rangle,
\qquad
t_i=1_Y+y_i.
$$

Both labelled bases have zero quadratic values and polar Gram matrix

$$
K=
\begin{pmatrix}
0&1&1&1\\
1&0&1&1\\
1&1&0&1\\
1&1&1&0
\end{pmatrix}.
$$

### Theorem 3.1 — canonical sheet-labelled isometry

There is a unique quadratic isometry

$$
\boxed{
\varphi:S_X\longrightarrow S_Y,
\qquad
\varphi(s_i)=t_i.
}
$$

It sends `s_\infty` to `t_\infty` and is equivariant under every permutation of the sheet labels. Hence it is `S_4\cong AGL(2,2)`-equivariant.

This theorem does not define a `D_8` action. The physical terminal set and the sheet index set are distinct.

## 4. Distinguished blocks as a singular diagonal

The peeling identity is

$$
1_{D_i}+s_i=t_i,
$$

or

$$
\boxed{1_{D_i}=s_i+t_i.}
$$

Since `S_X\perp S_Y`, the span

$$
L=\langle1_{D_i}:i\in I\rangle
$$

is the graph of `\varphi`:

$$
\boxed{
L=\{x+\varphi(x):x\in S_X\}.
}
$$

### Theorem 4.1 — diagonal gluing space

`L` is a four-dimensional maximal totally singular subspace of

$$
S_X\perp S_Y.
$$

#### Proof

For `x,x'\in S_X`,

$$
q(x+\varphi(x))=q(x)+q(\varphi(x))=0
$$

and

$$
b(x+\varphi(x),x'+\varphi(x'))
=b(x,x')+b(\varphi(x),\varphi(x'))=0.
$$

The graph has dimension four, equal to the Witt index of the orthogonal sum. ∎

Thus concentrated extension glues two identical sheet-labelled minus-type geometries without a coefficient twist.

## 5. Curvature transport

Let

$$
\mathcal C_X=S_X/s_\infty^\perp,
\qquad
\mathcal C_Y=S_Y/t_\infty^\perp.
$$

### Corollary 5.1 — `S_4`-equivariant curvature transport

The isometry descends to

$$
\boxed{
\bar\varphi:\mathcal C_X\longrightarrow\mathcal C_Y.
}
$$

It is `S_4`-equivariant and sends the unique nonzero parity class to the unique nonzero parity class.

This is incidence-level transport. A physical peel must still show that the actual residual side word realizes this transported class.

## 6. Pairwise marked skeletons

Fix distinct sheets `i,j`, with complementary indices `\ell,m`. Let

$$
T_{ij}(X),
\qquad
T_{ij}(Y)
$$

be the pairwise marked transition skeletons of the large and residual designs. Their edges are witness elements, not all `g`-edges of the physical scalar circuits.

### Theorem 6.1 — exact marked shell

`T_{ij}(X)` is obtained from `T_{ij}(Y)` by:

1. replacing residual terminal leaf `y_i` by block vertex `D_i`;
2. replacing `y_j` by `D_j`;
3. adding parallel witness edges `e_\ell,e_m` between `D_i,D_j`;
4. attaching new leaf `e_i` to `D_j`;
5. attaching new leaf `e_j` to `D_i`.

#### Proof

This is exactly the membership table

$$
D_i=(E\setminus\{e_i\})\cup\{y_i\},
\qquad
D_j=(E\setminus\{e_j\})\cup\{y_j\}.
$$

All other residual incidences are unchanged. ∎

## 7. Cycle-rank increment

The residual skeleton has

$$
|V|=2k,
\qquad
|E|=4k-3.
$$

The shell adds two vertices and four edges.

### Corollary 7.1

$$
\boxed{
\beta_1(T_{ij}(X))
=
\beta_1(T_{ij}(Y))+2.
}
$$

Each concentrated nucleus layer contributes exactly two independent cycles to every pairwise marked skeleton.

## 8. Marked ribbon data and witness arcs

Each block vertex records the cyclic order of its four witness edges on the scalar circuit. The new marked port sets are

$$
D_i:\ e_j,e_\ell,e_m,y_i,
$$

and

$$
D_j:\ e_i,e_\ell,e_m,y_j.
$$

Up to reversal, each four-port cyclic order has three possibilities.

### Corollary 8.1 — bounded marked shell

All new pairwise **marked** ribbon data are concentrated at two four-valent vertices and are finite-state.

A marked arc between consecutive ports may nevertheless contain:

- elementary non-`g` intervals;
- additional `g`-edges in `E_g\setminus\eta`;
- transition vertices of `\Gamma_g`;
- external side attachments and Kempe closures.

Thus the marked shell is not automatically a bounded physical multipole.

## 9. Correct physical transport layer

The physical concentrated layer consists of:

1. the fixed two-vertex marked shell on `E\cup Y`;
2. four transition walks in `\Gamma_g` around each distinguished scalar circuit;
3. finite elementary transfers inside contracted non-`g` components;
4. the four scalar transition systems at quotient vertices;
5. the requirement that the residual marked edges `y_i` become new terminal positions after a valid transition decomposition.

## 10. Descent target

A composition-safe peel must prove one of:

1. the marked shell lies in a proper terminal-even region of `\Gamma_g`, yielding a two-cut or four-cut;
2. the witness arcs factor through a transition-matroid two-sum;
3. an elementary segment exposes a bounded Tait cap or smaller separator;
4. crossing Kempe transitions break route-lock;
5. failure of descent yields a bounded exceptional interface.

The strict abstract measure is

$$
k\mapsto k-1,
$$

but the descent must be implemented on the physical transition quotient.

Identifying an exceptional interface with DDD requires an additional comparison between sheet-coordinate `S_4`, terminal-route symmetry, and the support-label DDD stabiliser.

## 11. Reliability boundary

Proved here:

- canonical `S_4`-equivariant quadratic isometry between successive nuclei;
- diagonal totally singular description of distinguished blocks;
- transport of the one-dimensional curvature carrier;
- exact pairwise marked-shell factorisation;
- cycle-rank increment by two.

Corrected here:

- no `D_8` action on the sheet-labelled nuclei is assumed.

Not proved here:

- a physical separator or transition two-sum supporting the shell;
- promotion of `y_i` to residual terminal trails;
- comparison with the physical DDD support-label class;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, DOI, or merge status is implied.
