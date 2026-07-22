# Finite Fourier positivity and arithmetic closure

## 1. Finite Fourier principle

For a finite denominator set $E$, weights $\theta_e\in[0,1]$, and a common period $L$, character orthogonality gives

$$
LW_{L,q_0}
=
\sum_{h\bmod L}
\prod_{e\in E}
\bigl((1-\theta_e)+\theta_e e^{2\pi ih/e}\bigr)
e^{-2\pi ihq_0/L}.
$$

If the real main sum is larger than the total norm of the minor sum, the nonnegative weighted count is positive.

For the reciprocal problem $q_0=L/b$. Since the total load is below $1$, the resulting congruence modulo $1$ is an equality.

## 2. Major-frequency mechanism

Put

$$
N=\left\lceil\frac{C}{\sigma_{\mathrm{ctrl}}}\right\rceil.
$$

Choose Taylor data

$$
0<r_T<1/4,
\qquad
0<\delta_T<\pi/2.
$$

For $|m|\le N$, every Bernoulli factor lies in the open right half-plane, so the principal logarithm is valid. Uniformly,

$$
\log\bigl((1-\theta)+\theta e^{2\pi iz}\bigr)
=
2\pi i\theta z
-
2\pi^2\theta(1-\theta)z^2
+
R_\theta(z).
$$

The exact expected-mass identity cancels the sum of linear terms.

If the aggregate cubic remainder is at most $\delta_T$, then

$$
\Re T_m
\ge
a_Te^{-2\pi^2m^2\sigma_E^2},
\qquad
a_T=e^{-\delta_T}\cos\delta_T>0.
$$

A coarse count of central integer labels gives

$$
\Re\sum_{|m|\le N}T_m
\ge
\frac{c_{\mathrm{maj}}}{\sigma_E}
$$

for one fixed $c_{\mathrm{maj}}>0$.

The released values $r_T=1/10$, aggregate error $1/10$, and coefficient $0.8$ are safety/finite certificates.

## 3. Universal Fourier damping

The one-factor identity and centred sine inequality give

$$
|F(h)|
\le
e^{-c_FQ_E(h)},
\qquad
c_F=8v_*=\frac{16}{9}.
$$

This exponent is derived from the weight normalization; it is not an independent tuning parameter.

## 4. Exact minor partition

Let $S_M$ be the genuine Fourier-main frequencies represented by $|m|\le N$, and $S_m$ its complement.

Partition only inside $S_m$:

$$
S_{\mathrm{blk}}
=
S_m\cap\{h:a(h)\notin\mathfrak M(C)\},
$$

$$
S_{\mathrm{sib}}
=
S_m\cap\{h:a(h)\in\mathfrak M(C)\}.
$$

The intersection with $S_m$ is load-bearing: no genuine main frequency may be counted as a minor.

## 5. Block-minor handoff

Fixing all block residues leaves at most $b$ frequencies modulo

$$
L=b\prod_{p\in\mathcal B}p.
$$

Therefore global localisation gives

$$
\sum_{h\in S_{\mathrm{blk}}}|F(h)|
\le
\frac{b\left(\eta+C_{\mathrm{tail}}e^{-c_FC^2/2}\right)}
     {\sigma_{\mathrm{ctrl}}}.
$$

The fibre factor $b$ is exact.

## 6. Sibling-minor handoff

For $h\in S_{\mathrm{sib}}$, choose its main block label $m$. Since $h$ is not the corresponding genuine main frequency, squarefreeness of $b$ gives a prime $r\mid b$ with

$$
h\not\equiv m\pmod r.
$$

For every high reservoir prime $s$, the auxiliary denominator $rs$ contributes at most

$$
\sqrt{1-\frac{4v_*}{r^2}}
\le
\beta_b
:=
\sqrt{1-\frac{4v_*}{b^2}}
=
\sqrt{1-\frac{8}{9b^2}}
<1.
$$

Using one common $G$-prime reservoir,

$$
|F(h)|\le\beta_b^G.
$$

There are at most $2N+1$ labels and at most $b$ frequencies in each block fibre:

$$
|S_{\mathrm{sib}}|\le b(2N+1).
$$

Hence

$$
\sum_{h\in S_{\mathrm{sib}}}|F(h)|
\le
b(2N+1)\beta_b^G.
$$

## 7. Symbolic terminal budget

Choose

$$
q_{\mathrm{blk}},q_{\mathrm{gauss}},q_{\mathrm{sib}}>0,
\qquad
q_{\mathrm{blk}}+q_{\mathrm{gauss}}+q_{\mathrm{sib}}<1.
$$

Let

$$
M_0=\frac{c_{\mathrm{maj}}}{K_\sigma}.
$$

Choose in order:

$$
\eta=\frac{q_{\mathrm{blk}}M_0}{b},
$$

then $C$ with

$$
bC_{\mathrm{tail}}e^{-c_FC^2/2}
<
q_{\mathrm{gauss}}M_0,
$$

then

$$
D_{\mathrm{sib}}
=
\frac{q_{\mathrm{sib}}M_0}{b(2C+3)},
$$

then $G$ with $\beta_b^G\le D_{\mathrm{sib}}$, and only then $k_0$.

The three minor contributions are strictly less than

$$
\frac{M_0}{\sigma_{\mathrm{ctrl}}}
=
\frac{c_{\mathrm{maj}}}
     {K_\sigma\sigma_{\mathrm{ctrl}}}
\le
\frac{c_{\mathrm{maj}}}{\sigma_E},
$$

which is at most the major sum.

## 8. Arithmetic closure

Positivity produces a finite avoiding representation of $1/b$ for squarefree $b\ge3$.

Then:

- $1/2=1/3+1/6$;
- $1=1/2+1/3+1/6$;
- numerator induction repeatedly invokes the avoiding unit theorem with the previously used denominators added to $T$.

The resulting finite set is enumerated increasingly. The formal community statement prepends $1$ as a dummy initial value and excludes it from the sum.

## 9. Necessity and semiprime criterion

A reciprocal sum of squarefree integers has squarefree reduced denominator because its reduced denominator divides their squarefree lcm.

For $n\ge1$,

$$
n=pq\text{ with distinct primes}
\Longleftrightarrow
\omega(n)=\Omega(n)=2.
$$

The release proves the forward direction needed by its tuple bridge; the converse is elementary and retained in the human theorem statement.
