# AC-PD-B3 — target, dual, quotient, and defect-core scope map

**Proof-development state:** `READY-FOR-CURATOR / PROVENANCE-REPAIRED`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Constituent units:** B1.4 and B3.1–B3.3  
**External mathematical inputs:** none  
**Assurance:** authorial proof-development checkpoint; finite certificate data remain separately classified

## 0. Four target objects

The five-support target programme uses four distinct graphs or spaces.

1. **Full dual triangulation** $T_g^{(1)}$: one vertex for every support-cycle face component.
2. **Old-colour quotient** $J_g$: one vertex for every original support index; distinct face components of one colour are identified.
3. **Five-coordinate half-cube** $\mathscr A_5$: the anisotropic Cayley graph of the minus-type four-space.
4. **Common links** $\operatorname{Lk}(Q_r)$: residual targets after fixing a source dominating clique.

There is a canonical quotient homomorphism

$$
T_g^{(1)}\longrightarrow J_g.
$$

Hence

$$
J_g\to\mathscr A_5
\Longrightarrow
T_g^{(1)}\to\mathscr A_5,
$$

but not conversely in general.

## 1. Complete same-embedding criterion

For a fixed compatible root lift $g$, a componentwise relabelling of its face components by five-coordinate words is exactly a graph homomorphism

$$
T_g^{(1)}\to\mathscr A_5.
$$

An independently chosen root flow integrates as a potential on this same dual exactly when its sum around every dual cycle is zero. Local source-vertex conservation checks only triangular face boundaries; residual dual holonomy may remain.

At graph level, five-support existence is equivalent to the existence of some cycle-face embedding whose dual maps to $\mathscr A_5$.

## 2. Exact half-cube link table

For a target $r$-clique $Q_r$, all cliques of the same size are target-automorphic and

$$
\begin{array}{c|c|c}
r&\operatorname{Lk}(Q_r)&\chi\\
\hline
1&L(K_5)&5\\
2&K_3\square K_2&3\\
3&K_2\sqcup K_1&2\\
4&K_1&1\\
5&\varnothing&0.
\end{array}
$$

More generally, in any quadratic Cayley target a common link is a quadratic slice

$$
\alpha+
\{z\in z_0+D^\perp:q(z)=1\}
$$

of an affine linear solution space.

## 3. Exact dominating-clique capacity

For every finite loopless graph $H$ and $2\le r\le5$,

$$
\boxed{
K_r\vee H\to\mathscr A_5
\quad\Longleftrightarrow\quad
\chi(H)\le5-r.}
$$

For $r=1$ the exact condition is

$$
H\to L(K_5).
$$

Consequences include:

- $K_6\not\to\mathscr A_5$;
- $K_3\vee C_{2m+1}\not\to\mathscr A_5$;
- $K_2\vee H\not\to\mathscr A_5$ exactly when $\chi(H)\ge4$;
- $K_6$-free non-homomorphic graphs exist, such as $M(K_5)$ and $K_3\vee C_5$.

## 4. Exact factorable eight-colour classification

For every graph $J$ on the eight old support indices,

$$
\boxed{
J\to\mathscr A_5
\quad\Longleftrightarrow\quad
K_6\nsubseteq J
\text{ and }
K_8-C_5\nsubseteq J.}
$$

Equivalently, $K_8-J$ contains $3K_2$, $K_3\sqcup K_2$, or $K_4$.

This completely classifies the old-colour-factorable route. It does not classify the full dual $T_g^{(1)}$.

## 5. Unused-root and defect-core reformulation

Put

$$
U_g=K_8-J_g.
$$

Then factorable badness is equivalent to

$$
\tau(U_g)\le2
\quad\text{or}\quad
U_g\cong C_5.
$$

Thus the static factorable bad cores are:

1. marked two-apex cores;
2. one exceptional pentagon core.

There are exactly 100 marked two-apex count types under bulk permutation and apex interchange. The reported 88 unmarked isomorphism types remain computational evidence.

An unused $3K_2$ is an immediate factorable compression witness. Its affine matching types have three $\operatorname{AGL}(3,2)$ orbits of sizes $28,168,224$. The correct all-parallel standard representative is $\{01,23,45\}$; an earlier displayed representative had the wrong direction pattern.

## 6. Target-side pivot depth

The ideal target pivot changes only two stars in the unused graph and satisfies

$$
\tau(U')\le\tau(U)+1.
$$

Among factorably bad cores, every ideal pivot remains bad exactly for one-star cores with $\tau(U)\le1$. Exact two-cover cores and the pentagon have abstract one-step target escapes.

This is not an actual source-cycle existence theorem. Failure to realize an ideal escape belongs to B4–B7 and must be explained by support-component, multiplicity, gauge, cut, or holonomy constraints.

## 7. Full-dual compatible obstruction

The flower $J_5$ packet supplies, subject to its explicit finite certificate, a compatible full dual $D_9$ containing

$$
K_3\vee C_5.
$$

The human target proof then gives

$$
D_9\not\to\mathscr A_5
$$

while $D_9$ is $K_6$-free. This proves that $K_6$ is not a complete full-dual obstruction language.

The explicit flow, fibre, dual graph, and neighbourhood counts remain certificate data rather than independently regenerated AC-PDL proofs.

## 8. Validity and assurance map

| Family | Mathematical status | Scope |
|---|---|---|
| cycle-face surface and full dual | theorem | full dual |
| half-cube link table | theorem | target graph |
| dominating-clique capacity | theorem | target graph |
| exact eight-vertex classification | theorem | factorable quotient |
| unused matching compression | theorem | factorable sufficient route |
| matching orbit sizes | theorem; one display corrected | finite affine geometry |
| two-apex/pentagon cores | theorem | factorable quotient |
| ideal-pivot depth | theorem | abstract factorable target dynamics |
| flower $D_9$ logic | theorem conditional on certificate data | full dual |
| flower/census numerical tables | exact certificate; not independently regenerated | evidence |

## 9. Curator normalization requirements

1. Keep $T_g$ and $J_g$ distinct throughout.
2. Preserve the exact link and eight-vertex theorem packets as valid sources.
3. Qualify unused-root, container, core, and ideal-pivot statements as factorable.
4. Correct the all-parallel matching representative only; retain its orbit theorem.
5. Keep certificate counts on their own assurance axis.
6. Do not infer full-dual failure from $J_g$ failure.
7. Do not treat $K_6$ as a complete full-dual obstruction family.

## 10. Programme transition

B3 closes the target and object-scope layer. B4 becomes active and must prove the exact motion laws:

- vertical gauge translation and partial Petrials;
- support-cycle pivots;
- horizontal connected-cycle Fano-flow switches;
- which structures and obstructions are preserved, transported, created, or destroyed;
- the difference between one reconfiguration edge and a commuting composition over disconnected switch support.

## 11. Completion assessment

`AC-PD-B3` is `READY-FOR-CURATOR / PROVENANCE-REPAIRED`. No genuine new-mathematics gap arose. The active frontier remains downstream in global reconfiguration/localisation, not in the target classification.