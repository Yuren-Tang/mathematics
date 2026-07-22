# Control geometry, local rigidity, and global localisation

## 1. Exact control system

Take finite prime blocks $P_k\subseteq[2^k,2^{k+1})$. The control-pair family is:

- all unordered pairs inside one block;
- all pairs between consecutive blocks.

For a residue assignment $a=(a_p)$, let $H_{pq}(a)$ be the centred CRT representative:

$$
H_{pq}(a)\equiv a_p\pmod p,
\qquad
H_{pq}(a)\equiv a_q\pmod q,
\qquad
-\frac{pq}{2}<H_{pq}(a)\le\frac{pq}{2}.
$$

Define

$$
Q_{\mathrm{ctrl}}(a)
=
\sum_{(p,q)}
\left(\frac{H_{pq}(a)}{pq}\right)^2,
\qquad
\sigma_{\mathrm{ctrl}}^2
=
\sum_{(p,q)}\frac1{(pq)^2}.
$$

For a Fourier frequency $h$, the centred residue identity gives

$$
Q_{\mathrm{ctrl}}(a(h))\le Q_E(h).
$$

## 2. Reciprocal load and deviation scale

An elementary dyadic primorial argument gives a block reciprocal upper bound $S_k=O(1/k)$. Consequently,

$$
\operatorname{load}(E_{\mathrm{ctrl}})
=
O(1/k_0).
$$

The human explicit certificate is

$$
\operatorname{load}(E_{\mathrm{ctrl}})
\le\frac{32}{k_0-1},
$$

while the released coarse certificate is $512/(k_0-1)$.

Bottom-block density gives

$$
\sigma_{\mathrm{ctrl}}
\ge
\frac{c_\sigma}{k_0 2^{k_0}}
$$

for one fixed $c_\sigma>0$. The released convenient value is $c_\sigma=1/100$.

The mechanism needs the asymptotic forms, not these exact integers.

## 3. Single-block rigidity

Fix $0<\rho<1/2$. A label $m$ is dominant when at least $(1-\rho)|P|$ primes carry residue $m$, with $m$ in the stated centred size range.

### Principle

Low energy without a dominant label forces

$$
Q_P(a)
\ge
c_w(\rho)\frac{X}{\log^3X}.
$$

The proof is a finite covering-and-dispersion argument:

```text
energy -> base prime with few large representatives
-> short list of candidate labels
-> substantial/tiny class dichotomy
-> cross-label energy or counting contradiction.
```

### Handoff

A cold block has:

- one unique dominant label;
- a quantitatively bounded exception set;
- a quantitative label-size bound.

The exception count can be forced to zero in the localisation regime by choosing the cold-forcing normalization before the final scale.

## 4. Corrected adjacent-label theorem

Distinct adjacent integer labels do not alone force energy.

The valid theorem also requires:

- residue agreement off named exception sets;
- reduced block-cardinality lower bounds;
- quantitative label-size bounds;
- the prime-divisor exclusion used in the phase argument.

Under those hypotheses, unequal consecutive labels force the boundary floor

$$
\Pi_k=
\frac{(|P_{k+1}|-e_0-1)(|P_k|-e_0)^3}
     {2^{13}(2^k)^2}.
$$

The source contains an explicit counterexample to the hypothesis-free version. This correction is load-bearing and must remain visible in every consumer.

## 5. Global level-set encoder

For

$$
\mathcal L(R)=\{a:Q_{\mathrm{ctrl}}(a)\le R\},
$$

record:

1. hot blocks;
2. mismatch boundaries;
3. integer energy shells;
4. dominant segment labels and exceptions.

This data injectively encodes the assignment. The resulting bound is naturally written:

> for every $\gamma>0$, after a scale threshold,
> $$
> \#\mathcal L(R)
> \le
> e^{A_\gamma J}e^{\gamma R}
> \left(1+\frac{\sqrt R}{\sigma_{\mathrm{ctrl}}}\right).
> $$

The factor $e^{A_\gamma J}$ is structural bounded entropy per block. It is not removable by declaring a block-system-dependent constant.

Wrapped large-label fibres are controlled by an injection into a fixed small-label fibre; nonwrapped large-label fibres are empty.

## 6. Localisation below the forcing floor

Let the global floor be the minimum of the bottom hot-block and bottom boundary scales.

Below that floor:

- no block is hot;
- no adjacent cold labels differ;
- the small-constant refinement eliminates all exceptions.

Hence every block coordinate has one common integer label $m$. The centred range then gives the exact identity

$$
Q_{\mathrm{ctrl}}(a)
=
m^2\sigma_{\mathrm{ctrl}}^2.
$$

Therefore every off-main assignment is either:

1. above the growing floor; or
2. globally diagonal with $|m|>C/\sigma_{\mathrm{ctrl}}$.

## 7. Partition-function handoff

The high-floor sector is bounded by Laplace absorption:

$$
\sum_{Q_{\mathrm{ctrl}}\ge\mathcal F_0}
e^{-cQ_{\mathrm{ctrl}}}
\le
\frac{\eta}{\sigma_{\mathrm{ctrl}}}.
$$

The diagonal sector is one-dimensional and has a Gaussian tail:

$$
\sum_{\mathrm{diag}}
e^{-cQ_{\mathrm{ctrl}}}
\le
\frac{C_{\mathrm{tail}}(c)e^{-cC^2/2}}
     {\sigma_{\mathrm{ctrl}}}.
$$

Thus

$$
\sum_{a\notin\mathfrak M(C)}
e^{-cQ_{\mathrm{ctrl}}(a)}
\le
\frac{\eta+C_{\mathrm{tail}}e^{-cC^2/2}}
     {\sigma_{\mathrm{ctrl}}}.
$$

The constants are fixed before the block system and final bottom scale.
