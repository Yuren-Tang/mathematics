# AffineCDC mathematical architecture

This file is a dependency map. Definitions, proofs, examples, and limitations
live in the linked canonical chapters; they are not repeated here.

## 1. Source, compatibility image, and output

The full source is a finite connected cubic graph with a nowhere-zero binary
flow:

$$
(G,\Gamma,f).
$$

For every edge $e$, put

$$
Q_e:=\Gamma/\langle f(e)\rangle.
$$

The source determines:

- an incidence space $E_f$;
- a homogeneous vertex space $L_{\mathrm{vert}}$;
- a canonical affine translate $\kappa+L_{\mathrm{vert}}$ of local families;
- an edge-matching space $L_{\mathrm{edge}}$.

The compatibility problem is

$$
(\kappa+L_{\mathrm{vert}})\cap L_{\mathrm{edge}}\neq\varnothing.
$$

Equivalently, it is the pointed pair complex

$$
\mathcal P_f:
L_{\mathrm{vert}}\oplus L_{\mathrm{edge}}
\xrightarrow{+}
E_f,
\qquad
[\kappa]\in H^1(\mathcal P_f).
$$

Compatibility is $[\kappa]=0$; the solution set is then a torsor under
$H^0(\mathcal P_f)$.

The pair complex is the complete image of the **compatibility question**, but it
is not the full source object. The graph, dart structure, and local-family
interpretation are still required to extract a cycle double cover:

$$
(G,\Gamma,f)
\longrightarrow
(\mathcal P_f,\kappa)
\longrightarrow
\text{compatible family},
$$

followed by

$$
(G,\Gamma,f,\text{compatible family})
\longrightarrow
\text{cycle double cover}.
$$

**Canonical chapter:**
[`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md).

## 2. Equivalent presentations of the compatibility core

The pair complex has two canonical presentations.

### Primal quotient presentation

Cancelling the contractible edge-diagonal summand gives

$$
\Gamma^V
\xrightarrow{\delta_f}
\bigoplus_eQ_e,
\qquad
(\delta_fm)_e=[m_u+m_v].
$$

The image of $\kappa$ is the quotient-sheaf cochain $c_f$. Thus

$$
[c_f]=0
\iff
[\kappa]=0.
$$

### Dual presentation

The dual obstruction space is the equilibrium-stress space:

$$
(H^1(\mathcal P_f))^*
\cong
L_{\mathrm{vert}}^\perp
\cap
L_{\mathrm{edge}}^\perp
=
\operatorname{Stress}(f).
$$

Hence

$$
[\kappa]=0
\iff
\psi(\kappa)=0
\text{ for every equilibrium stress }\psi.
$$

Quotient sheaf and stresses are not competing theories. They are the primal and
dual presentations of the same affine incidence pair.

## 3. Rank-three Fano compatibility

When

$$
\Gamma=\mathbf F_2^3,
$$

every $Q_e$ is a binary plane with canonical quadratic form

$$
q_e(x)=\mathbf1_{x\neq0}.
$$

The direct-sum quadratic space has:

- $L_{\mathrm{vert}}$ Lagrangian;
- $\kappa+L_{\mathrm{vert}}$ equal to the characteristic torsor of
  $L_{\mathrm{vert}}$;
- $L_{\mathrm{edge}}$ totally singular Lagrangian.

For Lagrangians $L,M$ in a nondegenerate quadratic space,

$$
\operatorname{Char}_q(L)\cap M\neq\varnothing
\iff
q|_{L\cap M}=0.
$$

The condition is automatic when $M$ is totally singular. Therefore

$$
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
\cap
L_{\mathrm{edge}}
\neq\varnothing,
$$

and the rank-three affine obstruction vanishes.

The following are equivalent resolutions of the same proof:

$$
\text{Lagrangian intersection}
\Longleftrightarrow
\text{quadratic handshaking}
\Longleftrightarrow
\text{cross-bit/support-boundary cancellation}.
$$

**Canonical chapter:**
[`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md).

## 4. Why rank three is exceptional

Three independent dimension and degree conditions coincide:

1. the support function on $Q_e$ has degree $r-1$, so it is quadratic exactly
   at $r=3$;
2. the local homogeneous image has dimension $r$ inside dimension $3(r-1)$ and
   is half-dimensional exactly when $2r=3(r-1)$;
3. the cubic quotient-sheaf index is

   $$
   \frac{3-r}{2}|V|,
   $$

   and vanishes exactly at $r=3$.

Rank three is therefore the unique balanced quadratic point of the hierarchy.

## 5. All-rank transgression and complete obstruction

For a plane $W\leq\Gamma$ and its three nonzero points,

$$
\sum_{h\in W\setminus\{0\}}
\nu_{\Gamma/\langle h\rangle}([x]_h)
=
\nu_{\Gamma/W}([x]_W).
$$

This lowers support degree by one in every rank. It gives a universal
outside-plane parity law, but for rank greater than three the scalar law forgets
directional information.

The missing information is recovered dually. A legal local stress triple has a
cross-bit $\beta$, support parity $\sigma$, and hidden-plane residue $\rho$
with

$$
\sigma=\beta+\rho.
$$

For every global equilibrium stress,

$$
\boxed{
\psi(\kappa)=\sum_v\rho_v(\psi_v).
}
$$

Hence compatibility holds exactly when every equilibrium stress has even
residue parity. This is the complete all-rank criterion.

- in rank three, $\operatorname{Ann}(W)$ is one-dimensional and contains no
  residue plane;
- in rank four, it is a plane and the first residue becomes possible;
- in higher rank, residues carry additional annihilator-plane decorations.

**Canonical chapter:**
[`rank-hierarchy/transgression-and-dual-fano-residue.md`](rank-hierarchy/transgression-and-dual-fano-residue.md).

## 6. Rank-four first failure

For $\Gamma=\mathbf F_2^4$, legal local stresses are alternating two-forms modulo
one quotient-form line. The residue is represented by the cubic expression

$$
\rho_W=(1+\beta_W)\operatorname{Pf}.
$$

It equals one precisely when the local flow plane is isotropic and the induced
cross-pairing with its quotient is perfect.

The two connected simple cubic graphs on six vertices give the minimal
comparison:

| graph | gauge code | essential-stress dimension | compatibility |
|---|---:|---:|---|
| triangular prism | $0$ | $1$ | compatible |
| $K_{3,3}$ | $0$ | $1$ | incompatible |

Thus rigidity and homology dimension alone do not decide compatibility; the
residue character does.

**Canonical chapter:**
[`rank-hierarchy/rank-four-first-obstruction.md`](rank-hierarchy/rank-four-first-obstruction.md).

## 7. Chain-level reduction to the tensor complex

Let

$$
Q_G:=\mathbf F_2^E/\mathcal C(G)^\perp
$$

and define

$$
T_f(\lambda)=\sum_e\lambda_ef(e)\otimes\bar e,
$$

$$
W_f(a\otimes q)=a\wedge F_f(q).
$$

The tensor complex is

$$
\mathbf F_2^E
\xrightarrow{T_f}
\Gamma\otimes Q_G
\xrightarrow{W_f}
\Lambda^2\Gamma.
$$

It is related to the incidence geometry by a canonical zigzag

$$
\widehat{\mathscr Q}_f
\xleftarrow{\simeq}
\widehat{\mathcal R}_f
\twoheadrightarrow
\mathcal T_f,
$$

where the left arrow removes a contractible flow-line lift and the right arrow
quotients the universal tension resolution.

The exact comparison is

$$
0\to\Gamma\to H_f^0\to\ker T_f\to0,
$$

$$
H_f^1\cong\operatorname{coker}T_f,
$$

and

$$
0\to\mathcal K_f\to H_f^1\xrightarrow{\mu_f}\Lambda^2\Gamma\to0,
$$

where

$$
\mathcal K_f=\ker W_f/\operatorname{im}T_f.
$$

The affine class lies canonically in $\mathcal K_f$. Thus the tensor complex
preserves compatibility but forgets constants, nonzero wedge moment, a preferred
vertex realization, and the dart-level output data.

**Canonical chapter:**
[`reduction/incidence-to-tensor-complex.md`](reduction/incidence-to-tensor-complex.md).

## 8. Tensor and code-flag branch

Dualizing a based quotient datum gives a nested code flag

$$
D\subseteq C\subseteq\mathbf F_2^E
$$

and a dual complex

$$
\Lambda^2D
\longrightarrow
D\otimes C
\xrightarrow{*}
\mathbf F_2^E.
$$

This branch contains:

- Schur multiplication and its first syzygies;
- the constraint matroid with cycle code $(C*D)^\perp$;
- strict morphisms and automorphisms;
- the divided-square exact sequence;
- coefficient-quotient long exact sequences;
- balanced determinant-line torsion.

It is a genuine downstream theory, but its recognition as an independent new
framework remains conditional on literature comparison and external payoff.

**Canonical chapters:**

- [`tensor/code-flag-complex.md`](tensor/code-flag-complex.md);
- [`tensor/exact-sequences-and-functoriality.md`](tensor/exact-sequences-and-functoriality.md);
- [`tensor/torsion-and-rigidity.md`](tensor/torsion-and-rigidity.md).

## 9. Gauge and cut geometry

The homogeneous tensor kernel has a direct graph interpretation. A nonzero
word with support $S$ is a gauge mode exactly when contracting the components of
$G-S$ produces a quotient on which the induced labels are simultaneously a
nowhere-zero flow and an exact tension.

Consequences include:

- the gauge code is even in rank at most three, sharply failing in rank four;
- gauge circuits are support-minimal harmonic cut quotients;
- circuits of weights two, four, and six have explicit classifications;
- cut gluing uses cycle-space fiber products and cographic pushouts;
- the common interface line

  $$
  L_S=\bigcap_i\langle h_i\rangle
  $$

  is the sewing-mode space, while $\Gamma/L_S$ is the matching-obstruction
  space;
- for proven cap-extension interfaces,

  $$
  b_G=b_A+b_B+\dim L_S.
  $$

**Canonical chapters:**

- [`gauge/gauge-modes-and-circuits.md`](gauge/gauge-modes-and-circuits.md);
- [`gauge/interface-gluing.md`](gauge/interface-gluing.md).

## 10. Trust and archive boundary

The original Lean implementation remains the machine-checked anchor for local
classification, compatibility, and CDC extraction. The invariant chapters are
paper proofs until separately formalized. Exact finite calculations support but
do not replace general arguments.

The snapshot-only embedding, Petrial, transition, and surface sources are not
reconstructed. Their inventory and restoration protocol are in
[`topology/README.md`](topology/README.md).

See:

- [`FORMAL_STATUS.md`](FORMAL_STATUS.md) for reliability;
- [`MIGRATION_LEDGER.md`](MIGRATION_LEDGER.md) for the disposition of every old
  active source;
- [`PUBLICATION_PROGRAM.md`](PUBLICATION_PROGRAM.md) for paper boundaries.

## 11. Dependency graph

$$
\boxed{
\begin{array}{c}
(G,\Gamma,f)\\
\downarrow\\
(\mathcal P_f,\kappa)\\
\downarrow\\
\text{rank-three Fano intersection}
\quad\text{or}\quad
\text{all-rank residue test}\\
\downarrow\\
\text{compatible affine family}\\
\downarrow\text{ using retained dart data}\\
\text{cycle double cover}
\end{array}
}
$$

The tensor/code, gauge/cut, and topological branches emanate from this chain;
they do not replace it.