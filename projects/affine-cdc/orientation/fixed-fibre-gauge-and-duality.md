# Gauge motion, the fixed-fibre obstruction, and orientation duality

## 1. Vertical lift torsor and gauge code

Fix a finite loopless cubic multigraph $G$ and a nowhere-zero flow

$$
f:E(G)\longrightarrow \Gamma\setminus\{0\},
\qquad \Gamma=\mathbf F_2^3.
$$

Define

$$
H_f^0=
\left\{
k:V(G)\to\Gamma:
 k_u+k_v\in\langle f(e)\rangle
 \text{ for every }e=uv
\right\}.
$$

For $k\in H_f^0$, the nonzero vector $f(e)$ determines a unique bit $\lambda_e(k)$ by

$$
k_u+k_v=\lambda_e(k)f(e).
$$

Hence there is a linear map

$$
\Lambda_f:H_f^0\longrightarrow C^1(G),
\qquad
k\longmapsto \lambda(k),
$$

with accessible gauge/Petrial code

$$
\mathcal B_f=\operatorname{im}\Lambda_f.
$$

The compatible labelled lifts above $f$ form a torsor under $H_f^0$. On a graph with several edge-bearing components,

$$
\ker\Lambda_f\cong\Gamma^{\pi_0(G)},
\qquad
\mathcal B_f\cong H_f^0/\Gamma^{\pi_0(G)}.
$$

Componentwise constant translations preserve the unlabelled surface and translate every affine face label on the corresponding component.

## 2. Gauge/partial-Petrial law

The integrated B4 theorem identifies the gauge word $\Lambda_f(k)$ with the partial Petrial that exchanges the two indexed face sides of precisely those edge bands where the gauge bit is one.

Choose vertex-disc orientations for $S_g$ and transport the local triangle orientations under the vertex translations $k_v$.

### Theorem 2.1 — chain-level gauge law

For transported local orientations,

$$
\boxed{
w(g^k)=w(g)+\Lambda_f(k).
}
$$

A fresh independent orientation choice on the new vertex discs differs by a coboundary, so for some $x\in C^0(G)$,

$$
w_{\mathrm{fresh}}(g^k)
=w(g)+\Lambda_f(k)+\delta x.
$$

Therefore the representative-free law is

$$
\boxed{
\omega(g^k)=\omega(g)+[\Lambda_f(k)]
\quad\text{in }C^1(G)/\operatorname{Cut}(G).
}
$$

The equality is a consequence of the integrated partial-Petrial theorem, not an independent naturality assumption.

## 3. Labelled orientable lifts

Let

$$
q:C^1(G)\longrightarrow C^1(G)/\operatorname{Cut}(G)
$$

be the quotient and put

$$
\Lambda_{\mathrm{or}}=q\circ\Lambda_f.
$$

For a base lift $g$, define

$$
\mathcal O_g=
\{k\in H_f^0:S_{g^k}\text{ is orientable}\}.
$$

By the fixed-lift theorem and the gauge law,

$$
k\in\mathcal O_g
\iff
\Lambda_{\mathrm{or}}(k)=\omega(g).
$$

### Theorem 3.1 — empty-or-torsor classification

The orientable labelled lifts in the fixed $f$-fibre form either the empty set or one affine torsor:

$$
\boxed{
\mathcal O_g=\varnothing
\quad\text{or}\quad
k_0+\ker\Lambda_{\mathrm{or}}.
}
$$

Equivalently, an orientable lift exists exactly when

$$
\boxed{
w(g)\in\operatorname{Cut}(G)+\mathcal B_f.
}
$$

This is a classification of labelled lifts, with the full $H_f^0$ action retained.

## 4. Base-independent fixed-fibre obstruction

Replacing the base lift $g$ by $g^{k_1}$ changes its twist representative by an element of $\mathcal B_f$ modulo cuts. Consequently

$$
\boxed{
\Omega_f
=[w(g)]_f
\in
C^1(G)/(\operatorname{Cut}(G)+\mathcal B_f)
}
$$

is independent of the base compatible lift.

### Corollary 4.1

The fixed Fano-flow fibre contains an orientable lift if and only if

$$
\boxed{\Omega_f=0.}
$$

The two obstruction objects have different quantifiers:

- $\omega(g)\in C^1/\operatorname{Cut}$ tests one prescribed compatible lift;
- $\Omega_f\in C^1/(\operatorname{Cut}+\mathcal B_f)$ tests whether the whole fixed-flow fibre meets the orientable locus.

Per-lift nonautomaticity therefore does not decide fixed-fibre existence.

## 5. Unlabelled Petrial coset

The gauge word forgets componentwise constant affine relabelling. Define

$$
\mathcal P_g
=
\{\lambda\in\mathcal B_f:
  w(g)+\lambda\in\operatorname{Cut}(G)\}.
$$

### Corollary 5.1 — unlabelled orientable words

One has

$$
\boxed{
\mathcal P_g=\varnothing
\quad\text{or}\quad
\lambda_0+\bigl(\mathcal B_f\cap\operatorname{Cut}(G)\bigr).
}
$$

This is the corrected formula. It repairs the malformed control character before `\bigl` in the PDL source rendering.

Thus:

- labelled orientable lifts are a torsor under
  $$
  \Lambda_f^{-1}(\operatorname{Cut}(G));
  $$
- unlabelled orientable partial-Petrial surfaces are a coset under
  $$
  \mathcal B_f\cap\operatorname{Cut}(G).
  $$

The two classifications are related by the quotient $H_f^0\twoheadrightarrow\mathcal B_f$ but are not the same object.

## 6. Dual orientation-stress criterion

Use the standard edge dot product on $C^1(G)$. Since all spaces are finite dimensional,

$$
(\operatorname{Cut}(G)+\mathcal B_f)^\perp
=
\operatorname{Cut}(G)^\perp\cap\mathcal B_f^\perp.
$$

Define

$$
Z_1(G)=\operatorname{Cut}(G)^\perp
$$

and

$$
\boxed{
\operatorname{Stress}_{\mathrm{or}}(f)
=Z_1(G)\cap\mathcal B_f^\perp.
}
$$

### Theorem 6.1 — dual criterion

The fixed $f$-fibre contains an orientable lift if and only if

$$
\boxed{
\langle w(g),z\rangle=0
\quad
\text{for every }z\in\operatorname{Stress}_{\mathrm{or}}(f).
}
$$

A vector $z$ with nonzero pairing is simultaneously:

1. a source-cycle twist-holonomy witness;
2. a functional annihilating every accessible gauge/Petrial word;
3. a certificate that $\Omega_f\ne0$.

Using the integrated B4 code identity,

$$
\mathcal B_f
=(\mathcal C(G)*\mathcal F_f)^\perp,
$$

one obtains the equivalent form

$$
\boxed{
\operatorname{Stress}_{\mathrm{or}}(f)
=
\mathcal C(G)\cap
(\mathcal C(G)*\mathcal F_f).
}
$$

This equality does not by itself localize or classify the stresses.

## 7. Compatibility stress versus orientation stress

Programme A's compatibility stress tests whether the affine/root-lift fibre is nonempty. Its vanishing is already supplied in rank three by the Fano characteristic-torsor theorem.

The orientation stress above instead:

- lives in the source edge-word space;
- annihilates the image of accessible partial Petrials;
- tests whether an already nonempty compatible-lift fibre contains an orientable member.

Thus

$$
\text{compatibility vanishing}
\not\Rightarrow
\text{orientation vanishing}.
$$

No identification between the two stress theories is permitted without an explicit comparison map.

## 8. Exact open boundary

Closed authorially in the fixed-fibre theory:

- the chain-level and quotient gauge laws;
- the labelled empty-or-torsor classification;
- the base-independent class $\Omega_f$;
- the unlabelled Petrial coset;
- the dual orientation-stress criterion.

Open as genuine Research Lead obligations:

1. `AC-RL-OR-FIXED-FIBRE-VANISHING` — decide whether $\Omega_f=0$ for every nowhere-zero rank-three flow on every finite bridgeless cubic multigraph, or construct an exact fixed-fibre counterexample;
2. `AC-RL-OR-GRAPH-EXISTENCE` — if universal fixed-fibre vanishing fails, decide whether every such graph admits at least one flow $f$ with $\Omega_f=0$.

No horizontal reconfiguration theorem is silently inferred from the fixed-fibre linear algebra.
