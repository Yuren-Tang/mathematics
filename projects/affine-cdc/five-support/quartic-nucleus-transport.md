# Quartic nucleus transport and pairwise shell factorisation

## 1. Purpose

If all four sheets of a quartic witness design are concentrated, the abstract design peels from level `k` to level `k-1`.  This chapter records the exact algebraic and pairwise-incidence transport of that peel.

- The old and residual terminal nuclei are canonically isometric minus-type four-spaces.
- The four distinguished block vectors form the totally singular diagonal graph of that isometry.
- The `D_8` route structure and one-dimensional curvature carrier transport without algebraic twist.
- Every pairwise witness-incidence skeleton grows by one fixed two-vertex shell, adding exactly two cycles.

The shell theorem is a statement about the four marked witness edges on each distinguished scalar circuit.  The arcs between those marked edges may contain further edges of `E_g\setminus\eta`; physically they are transition walks in the `g`-component quotient `\Gamma_g`, not necessarily single non-`g` intervals.

## 2. Concentrated design

Let

$$
(X,(\mathcal R_i),(e_i))
$$

be a concentrated quartic design of level `k\ge2`.  Put

$$
E=\{e_0,e_1,e_2,e_3\},
\qquad
Y=X\setminus E.
$$

For sheet `i`, the distinguished block is

$$
D_i=(E\setminus\{e_i\})\cup\{y_i\},
$$

where the `y_i\in Y` are pairwise distinct.  The residual families

$$
\mathcal R_i'=\mathcal R_i\setminus\{D_i\}
$$

form a level-`k-1` quartic design on `Y`, omitting `y_i` in sheet `i`.

## 3. Successive terminal nuclei

Define

$$
S_X=\langle s_0,s_1,s_2,s_3\rangle,
\qquad
s_i=1_X+e_i,
$$

and

$$
S_Y=\langle t_0,t_1,t_2,t_3\rangle,
\qquad
 t_i=1_Y+y_i.
$$

Both ordered bases have zero quadratic values and polar Gram matrix

$$
K=
\begin{pmatrix}
0&1&1&1\\
1&0&1&1\\
1&1&0&1\\
1&1&1&0
\end{pmatrix}.
$$

### Theorem 3.1 — canonical nucleus isometry

There is a unique labelled quadratic isometry

$$
\boxed{
\varphi:S_X\longrightarrow S_Y,
\qquad
\varphi(s_i)=t_i.
}
$$

It sends `s_\infty` to `t_\infty` and is equivariant under all sheet relabellings, hence under the route stabiliser `D_8`.

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
L=\langle1_{D_0},1_{D_1},1_{D_2},1_{D_3}\rangle
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

Thus a concentrated extension glues two labelled copies of the same minus-type geometry along the singular diagonal; there is no hidden coefficient twist.

## 5. Curvature transport

The old and residual curvature carriers are

$$
\mathcal C_X=S_X/s_\infty^\perp,
\qquad
\mathcal C_Y=S_Y/t_\infty^\perp.
$$

### Corollary 5.1

The isometry induces a canonical `D_8`-equivariant isomorphism

$$
\boxed{
\bar\varphi:\mathcal C_X\longrightarrow\mathcal C_Y.
}
$$

It sends the unique nonzero parity class to the unique nonzero parity class.

This is incidence-level transport.  A physical peel must still identify the actual side word on the residual marked edges `y_i` with this transported class.

## 6. Pairwise witness-incidence skeletons

Fix sheets `i,j`, with complementary indices `\ell,m`.  Let

$$
T_{ij}(X)
$$

and

$$
T_{ij}(Y)
$$

be the pairwise transition skeletons of the large and residual quartic designs.  Their edges are the marked witness elements, not all `g`-edges of the physical scalar circuits.

In `T_{ij}(Y)`, the terminal leaves are `y_i,y_j`; in `T_{ij}(X)`, they are `e_i,e_j`.  The distinguished blocks `D_i,D_j` are block vertices.

### Theorem 6.1 — exact pairwise shell

`T_{ij}(X)` is obtained from `T_{ij}(Y)` by:

1. replacing the residual terminal leaf `y_i` by the block vertex `D_i`;
2. replacing `y_j` by `D_j`;
3. adding two parallel witness edges `e_\ell,e_m` between `D_i,D_j`;
4. attaching the new leaf `e_i` to `D_j`;
5. attaching the new leaf `e_j` to `D_i`.

Equivalently, the new marked-incidence shell has two degree-four vertices, two parallel middle edges, two residual inner ports, and two new outer ports.

#### Proof

This is the exact membership table of the distinguished blocks:

$$
D_i=(E\setminus\{e_i\})\cup\{y_i\},
\qquad
D_j=(E\setminus\{e_j\})\cup\{y_j\}.
$$

All residual incidences other than `y_i,y_j` are unchanged. ∎

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

Thus every concentrated nucleus layer contributes exactly two independent cycles to every pairwise marked-incidence skeleton.

## 8. Marked ribbon data and physical witness arcs

Each block vertex records the cyclic order of its four **witness** edges on the corresponding scalar circuit.  At the new shell vertices the marked port sets are

$$
D_i:\quad e_j,e_\ell,e_m,y_i,
$$

and

$$
D_j:\quad e_i,e_\ell,e_m,y_j.
$$

Up to reversal, each four-port cyclic order has three possibilities.

### Corollary 8.1 — bounded marked shell

The new pairwise marked ribbon data are concentrated at two four-valent vertices and are finite-state.

However, a marked arc between consecutive ports may contain:

- elementary non-`g` intervals;
- additional `g`-edges from `E_g\setminus\eta`;
- transition vertices of the physical quotient `\Gamma_g`;
- external side attachments and Kempe closures.

Therefore the marked shell is not yet a bounded physical multipole in `Q`.  Its four witness arcs are transition walks in `\Gamma_g`, not automatically four elementary non-`g` paths.

## 9. Correct physical transport layer

The quotient Tait-phase model labels every `g`-edge by an endpoint quotient pair and supplies three Kempe systems.  The elementary non-`g` pieces of each witness arc have finite eighteen-state transfers and cap-or-cell normal forms, but the number of intervening `g`-edges is unrestricted.

The physical concentrated layer consequently separates into:

1. the fixed two-vertex **marked** shell on `E\cup Y`;
2. four transition walks in `\Gamma_g` around each distinguished scalar circuit;
3. finite elementary transfers inside the contracted non-`g` components;
4. the four transition systems at quotient vertices;
5. the requirement that the residual marked edges `y_i` become the new terminal positions after a valid transition decomposition.

## 10. Updated descent target

A composition-safe peel must prove one of:

1. the marked shell is supported in a proper terminal-even region of `\Gamma_g`, yielding a two-cut or four-cut that lifts to `Q`;
2. the four witness arcs factor through a transition-matroid two-sum, so the shell can be removed and `y_i` promoted to residual boundary positions;
3. an elementary segment exposes a bounded Tait cap or smaller separator;
4. crossing Kempe transitions create an alternate route and break route-lock;
5. failure of descent is exactly the physical `D_8` class.

The strict abstract measure remains

$$
k\mapsto k-1,
$$

but the descent must now be implemented on the physical transition quotient rather than by deleting four presumed non-`g` intervals.

## 11. Reliability boundary

Proved here:

- canonical quadratic isometry between successive terminal nuclei;
- diagonal totally singular description of the distinguished block vectors;
- `D_8`-equivariant transport of the curvature carrier;
- exact pairwise marked-shell factorisation;
- exact cycle-rank increment by two;
- concentration of new marked ribbon data at two four-valent vertices.

Explicitly not claimed:

- that a distinguished scalar circuit contains only its four witness `g`-edges;
- that its four witness arcs are elementary non-`g` intervals;
- a physical separator or transition two-sum supporting the shell;
- promotion of `y_i` to actual residual terminal trails;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, or DOI status is implied.
