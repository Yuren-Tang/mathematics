# Petersen relative channel profiles and exact endpoint calibration

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `d3e1a723c394da8067331b16670d6c84edb6d5e8`  
**Parents:**

- `projects/affine-cdc/research/QUADRATIC_CHANNEL_PROJECTION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_IDENTITY_HEXAGON_QUADRATIC_SINGULAR_FIBRES_V1.md`;
- `projects/affine-cdc/research/PETERSEN_IDENTITY_HEXAGON_TRANSVERSE_CHANNEL_TRANSVERSAL_V1.md`;
- `projects/affine-cdc/research/RELATIVE_WITNESS_SUBTRACTION_V1.md`.

**Status:** exact coefficient/root-fibre calibration theorem. The projective six-channel profile of an identity-return displacement is exactly the base-independent change of the actual endpoint repair-channel fibres. Modulo the full-channel complement, the quadratic channel projection linearises to a canonical isomorphism

\[
E_5/\langle r\rangle
\cong
B^1(K_{2,3};\mathbf F_2)/\langle\mathbf1\rangle.
\]

The Type-X sector is one canonical four-point affine plane whose translation space is the DDD/channel triality plane.  
**Not implied:** simultaneous route-witness lifting, admissible regional surgery, strict descent, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Six repair channels and the unsafe profile

Let

\[
E_5=\left\{x\in\mathbf F_2^5:\sum_i x_i=0\right\},
\qquad
q(x)=\frac{|x|}{2}\pmod2,
\]

and let

\[
b(x,y)=q(x+y)+q(x)+q(y)
\]

be the polar form. The ten roots are the vectors with `q=1`.

Fix an active root

\[
r=uv.
\]

Write

\[
W=[5]\setminus\{u,v\}=\{x,y,z\}.
\]

The six repair channels are

\[
S_r=\{uw,vw:w\in W\},
\]

the edge set of

\[
K_r=K_{\{u,v\},W}\cong K_{2,3}.
\]

For an ambient coefficient value `a in E5`, define its actual unsafe repair-channel profile

\[
\mathsf A_r(a)
=\{s\in S_r:a+s\notin R_5\}.
\]

Equivalently, as a binary word on `S_r`,

\[
\mathsf A_r(a)(s)=1+q(a+s).
\]

### Theorem 1.1 — exact quadratic profile formula

For every `a in E5` and `s in S_r`,

\[
\boxed{
\mathsf A_r(a)(s)=q(a)+b(a,s).
}
\]

Thus

\[
\mathsf A_r(a)=U_r(a),
\]

where `U_r` is the quadratic channel profile from the channel-projection theorem.

### Proof

Because

\[
q(a+s)=q(a)+q(s)+b(a,s)
=q(a)+1+b(a,s),
\]

one has

\[
1+q(a+s)=q(a)+b(a,s).
\]

∎

---

## 2. Projective linearisation

Identify `E5` with the even representative of the vertex-potential space of the connected graph `K_r`. Let

\[
\delta:E_5\longrightarrow B^1(K_r;\mathbf F_2)
\]

be the cut map.

The quadratic-channel theorem gives

\[
U_r(a)=\delta\Psi_r(a),
\qquad
\Psi_r(a)=a+q(a)r.
\]

The active root potential satisfies

\[
\boxed{
\delta r=\mathbf1_{S_r},
}
\]

because every channel edge joins one endpoint of `r` to one vertex of `W`.

Define the projective cut code

\[
\overline B_r
=
B^1(K_r;\mathbf F_2)/\langle\mathbf1_{S_r}\rangle.
\]

### Theorem 2.1 — quadratic projection becomes linear modulo complement

For every `a in E5`,

\[
\boxed{
[U_r(a)]
=[\delta a]
\in\overline B_r.
}
\]

Consequently the map

\[
\boxed{
\overline U_r:
E_5/\langle r\rangle
\longrightarrow
\overline B_r,
\qquad
[a]\longmapsto[U_r(a)]
}
\]

is a canonical linear isomorphism.

### Proof

Since

\[
U_r(a)=\delta(a+q(a)r)
=\delta a+q(a)\mathbf1_{S_r},
\]

the two cut words have the same class in `overline B_r`.

The connected graph `K_r` has five vertices, hence its cut space has dimension four. The even-potential map

\[
\delta:E_5\to B^1(K_r)
\]

is an isomorphism. Quotienting the source by `<r>` and the target by `<delta r>=<1>` therefore gives an isomorphism of three-dimensional spaces. ∎

### Corollary 2.2 — projective additivity

For all `a,c in E5`,

\[
\boxed{
[U_r(a+c)]
=[U_r(a)]+[U_r(c)].
}
\]

Before quotienting, the exact defect from linearity is the full-channel word:

\[
\boxed{
U_r(a+c)
=U_r(a)+U_r(c)+b(a,c)\mathbf1_{S_r}.
}
\]

### Proof

Polarisation gives

\[
q(a+c)=q(a)+q(c)+b(a,c),
\]

and `b` is bilinear. ∎

---

## 3. Relative endpoint calibration

Let an identity-linear affine return carry one coefficient section from

\[
a
\]

to

\[
a+\Delta.
\]

The endpoint repair-channel change is the symmetric difference

\[
\mathsf R_{r,a}(\Delta)
=
\mathsf A_r(a)\triangle\mathsf A_r(a+\Delta).
\]

### Theorem 3.1 — exact relative profile identity

For every `a,Delta in E5`,

\[
\boxed{
\mathsf R_{r,a}(\Delta)
=
U_r(\Delta)
+b(a,\Delta)\mathbf1_{S_r}.
}
\]

Equivalently,

\[
\boxed{
[\mathsf R_{r,a}(\Delta)]
=
[U_r(\Delta)]
=
[\delta\Delta]
\in\overline B_r.
}
\]

Thus the projective endpoint fibre change depends only on the displacement class

\[
[\Delta]\in E_5/\langle r\rangle,
\]

not on the base coefficient `a`.

### Proof

For one channel `s`, Theorem 1.1 gives

\[
\begin{aligned}
\mathsf A_r(a)(s)
+\mathsf A_r(a+\Delta)(s)
&=q(a)+b(a,s)+q(a+\Delta)+b(a+\Delta,s)\\
&=q(\Delta)+b(a,\Delta)+b(\Delta,s)\\
&=U_r(\Delta)(s)+b(a,\Delta).
\end{aligned}
\]

The extra term is independent of `s`, hence is either zero or the full-channel word. ∎

### Corollary 3.2 — the old calibration target splits

The equality between a coefficient displacement and the **endpoint root-fibre profile change** is no longer an open physical calibration problem: it is exact and base-independent modulo full complement.

What remains open is the regional composition theorem:

- transport the six endpoint fibre changes through actual side components;
- realise compatible channel changes by route witnesses;
- localise failure as an empty fibre/relation, DDD holonomy, separator, or defect unit;
- obtain strict descent.

---

## 4. The projective `Z/D/X` shape theorem

For `w in W`, put

\[
P_w=\{uw,vw\}.
\]

These are the three resolution pairs.

Let `d=xy` be a root disjoint from `r`, and let `z` be the third vertex of `W`.

### Theorem 4.1 — Type Z

If

\[
\Delta\in\{0,r\},
\]

then

\[
\boxed{
[\mathsf R_{r,a}(\Delta)]=0.
}
\]

The two endpoint unsafe profiles are equal or globally complementary.

### Proof

Both `U_r(0)` and `U_r(r)` are zero: for every channel `s`,

\[
q(r)+b(r,s)=1+1=0.
\]

Apply Theorem 3.1. ∎

### Theorem 4.2 — Type D

If

\[
\Delta\in\{d,d+r\},
\]

then

\[
\boxed{
[\mathsf R_{r,a}(\Delta)]
=[P_z].
}
\]

Thus the relative endpoint profile singles out one unique resolution pair, modulo full complement.

### Proof

For the four channels incident with `x` or `y`, the root `d=xy` meets the channel, so

\[
U_r(d)(s)=q(d)+b(d,s)=1+1=0.
\]

The two channels in `P_z` are disjoint from `d`, so their value is `1`. Hence

\[
U_r(d)=P_z.
\]

The quadratic singular-fibre theorem gives

\[
U_r(d+r)=U_r(d).
\]

Now apply Theorem 3.1. ∎

### Theorem 4.3 — Type X

If

\[
b(\Delta,r)=1,
\]

then

\[
\boxed{
|\mathsf R_{r,a}(\Delta)\cap P_w|=1
\qquad(w\in W).
}
\]

Thus the actual relative endpoint fibre change is one three-channel transversal of the three resolution pairs; changing the base coefficient can only replace it by its full complement, which is again a transversal.

### Proof

The projective profile `U_r(Delta)` is a transversal by the transverse-profile theorem. Theorem 3.1 says the actual relative profile is `U_r(Delta)` or its complement. Complementation exchanges the two members of every pair, so it preserves the transversal property. ∎

### Corollary 4.4 — physically observable `2+6+8`

The complete displacement classification has the following endpoint root-fibre meaning:

\[
\boxed{
\begin{array}{c|c|c}
\text{type}&\Delta\text{-count}&\text{projective endpoint profile change}\\
\hline
Z&2&0\\
D&6&\text{one unique resolution pair}\\
X&8&\text{one resolution transversal}
\end{array}}
\]

There is no additional endpoint channel alphabet.

---

## 5. The canonical Type-X affine plane

Put

\[
V_r=E_5/\langle r\rangle.
\]

The functional

\[
\ell_r:V_r\to\mathbf F_2,
\qquad
\ell_r([a])=b(a,r)
\]

is well defined, because `b(r,r)=0`.

Its kernel is

\[
H_r
=
 r^\perp/\langle r\rangle
\cong\mathbf F_2^2.
\]

The four projective Type-X displacement classes form the affine plane

\[
\Lambda_r^X
=
\{[a]\in V_r:\ell_r([a])=1\}.
\]

### Theorem 5.1 — Type-X profile plane

\[
\boxed{
\Lambda_r^X
\text{ is an affine torsor over }
H_r.
}
\]

Under the projective channel isomorphism `overline U_r`, it is identified with the four complement-pairs of resolution transversals.

### Proof

`V_r` has dimension three and `ell_r` is nonzero, so its level-one set is an affine plane with translation space `ker ell_r=H_r`.

Theorem 2.1 identifies `V_r` with the projective cut code. The Type-X profile theorem identifies the four level-one points with the four complement-pairs of transversals. ∎

### Theorem 5.2 — triality translation action

For a disjoint root `d=xy`, let

\[
\Gamma_d
=\{ux,uy,vx,vy\}
\]

be the corresponding four-cycle of `K_r`.

For every Type-X class `[Delta]`,

\[
\boxed{
\overline U_r([\Delta+d])
=
\overline U_r([\Delta])
+[\Gamma_d].
}
\]

The three nonzero elements of `H_r` therefore act freely and transitively on the four projective Type-X profiles.

### Proof

The projective map is linear and

\[
\delta d=\Gamma_d.
\]

The three nonzero classes of `H_r` are the three disjoint roots modulo `<r>`. Translation by the two-dimensional space `H_r` is free and transitive on its affine coset `Lambda_r^X`. ∎

### Corollary 5.3 — oriented double cover

The eight actual Type-X displacements form the two-sheeted cover of `Lambda_r^X` whose deck involution is

\[
\Delta\longmapsto\Delta+r.
\]

On channel profiles,

\[
\boxed{
U_r(\Delta+r)
=\mathbf1_{S_r}+U_r(\Delta),
}
\]

so the deck involution is full complement.

The two orientation-parity orbits are exchanged by this involution; the projective four-point plane is intrinsic to the unordered active root.

---

## 6. Comparison with the four locked challenges

Let a physical full-rank locked quotient have terminal colour

\[
g\in V\setminus\{0\},
\]

and challenge plane

\[
\Lambda_g
=
\{\lambda\in V^*:\lambda(g)=1\}.
\]

Its translation space is

\[
g^\perp
=
\{\delta\in V^*:\delta(g)=0\}
\cong\mathbf F_2^2.
\]

The Type-X profile plane has exactly the same affine form:

\[
\Lambda_r^X
=
\{\xi\in V_r:\ell_r(\xi)=1\},
\qquad
\operatorname{Trans}(\Lambda_r^X)=H_r.
\]

### Theorem 6.1 — one-origin affine comparison

Fix a linear triality isomorphism

\[
\phi:H_r\xrightarrow{\sim}g^\perp.
\]

For any chosen base profile and challenge

\[
\xi_0\in\Lambda_r^X,
\qquad
\lambda_0\in\Lambda_g,
\]

there is a unique affine isomorphism

\[
\boxed{
J_{\xi_0,\lambda_0}:\Lambda_r^X\xrightarrow{\sim}\Lambda_g
}
\]

such that

\[
J(\xi_0)=\lambda_0
\]

and

\[
J(\xi+h)=J(\xi)+\phi(h)
\qquad(h\in H_r).
\]

### Proof

Define

\[
J(\xi_0+h)=\lambda_0+\phi(h).
\]

The action of `H_r` on `Lambda_r^X` is free and transitive, so this is well defined and unique. ∎

### Consequence 6.2 — calibration burden

The comparison with the four locked challenges no longer requires eight independent Type-X checks.

It requires only:

1. a correspondence between the three nonzero triality directions `H_r^times` and `(g^perp)^times`;
2. one bounded base-profile/base-challenge calibration.

Any bijection between the three nonzero elements of two-dimensional binary spaces extends uniquely to a linear isomorphism, since the sum of any two distinct nonzero elements is the third.

If the physical construction supplies the triality correspondence equivariantly, one basepoint closes the entire four-point comparison.

---

## 7. Revised composition frontier

### Closed here

- the quadratic unsafe profile is the actual endpoint root-fibre profile;
- projective nonlinearity is only the full-channel complement;
- the displacement class in `E5/<r>` is exactly the projective endpoint profile change;
- the `Z/D/X` classes have exact observable channel shapes;
- Type X is one four-point affine plane, not eight unrelated states;
- the DDD/channel triality plane acts as its complete translation group;
- comparison with the four locked challenges is reduced to a triality map plus one origin.

### Still open

The remaining theorem is genuinely regional and compositional:

1. lift the endpoint channel toggles to simultaneous relative route witnesses along the actual source region;
2. if a required channel fibre or local relation is empty, enter the existing defect branch;
3. if a nonzero triality loop remains, localise the existing DDD orientation/holonomy class;
4. if all toggles lift, obtain a route/profile escape, serial replacement, or four-pole separator;
5. prove strict decrease of the side-signature/interval complexity;
6. assemble horizontal/global induction.

No further coefficient-to-endpoint calibration map is required.