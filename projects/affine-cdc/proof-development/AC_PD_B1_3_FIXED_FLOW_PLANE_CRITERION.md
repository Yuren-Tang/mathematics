# AC-PD-B1.3 — exact fixed-flow/fixed-plane five-coordinate criterion

**Proof-development state:** `COMPLETE-DRAFT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Recovered controlling packets:** `FIVE_CDC_FIXED_FLOW_REDUCTION_V1.md`, `FIVE_CDC_COLOUR_CUT_REFINEMENT_V1.md`, and `FIVE_CDC_MATCHING_FOUR_FLOW_BRIDGE_V1.md` at `research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`  
**Depends on:** B1.1 and B1.2  
**Immediate consumers:** B1.4 fixed-lift/surface scope; B2 singular/Schur/stress equivalences; B4 horizontal flow motion  
**External mathematical inputs:** none

## 0. Scope and quantifiers

Let $G$ be a finite loopless cubic multigraph and fix a nowhere-zero Fano flow

$$
f:E(G)\longrightarrow\Gamma\setminus\{0\},
\qquad
\Gamma=\mathbf F_2^3.
$$

Fix a linear plane $W\leq\Gamma$. This unit gives a complete criterion for a **global five-coordinate affine slice above the fixed pair $(f,W)$**.

It does not claim that every five-support compression of one fixed compatible root lift factors through one global five-point subset of $\Gamma$; the full componentwise surface object is treated separately. Nor does failure for this fixed $f$ imply failure for the graph, because a different Fano flow may succeed.

## 1. The plane subgraph and outside decomposition

Choose $a\in\Gamma\setminus W$. Every flow value decomposes uniquely as

$$
f(e)=w(e)+b(e)a,
$$

where $w(e)\in W$ and $b(e)\in\mathbf F_2$. Since the decomposition is linear, both $w$ and $b$ are flows.

Define

$$
B_W=\operatorname{supp}b
=
\{e:f(e)\notin W\},
$$

and

$$
G_W=G-B_W
=
\bigl(V(G),\{e:f(e)\in W\}\bigr).
$$

The binary support $B_W$ is even. At each cubic vertex its local degree is zero or two; consequently every nonisolated vertex of $G_W$ has degree three or one respectively.

For each outside colour $c\in\Gamma\setminus W$, define the colour matching

$$
M_c=\{e:f(e)=c\}.
$$

### Lemma 1.1 — outside colour classes are matchings

Every $M_c$ is a matching and is contained in $B_W$.

### Proof

Containment is immediate. If two edges of the same nonzero colour $c$ met at one cubic vertex, conservation would force the third incident value to be zero. $\square$

For the chosen $a$, one also has

$$
M_a=\{e:w(e)=0\}.
$$

The restriction of $w$ to $G-M_a$ is a nowhere-zero $W$-flow.

## 2. The normalized five-coordinate slice

After translating support labels, every forbidden three-point set of direction $W$ may be normalized to

$$
T=W\setminus\{0\}.
$$

The five allowed indices are then

$$
A_W=\{0\}\sqcup(a+W).
$$

Translation of all support labels changes neither edge differences nor local support parity. Hence the criterion depends only on the direction plane $W$, not on the particular affine translate of the omitted triple.

### Definition 2.1

A **global five-coordinate slice above $(f,W)$** is a compatible affine family for the fixed flow $f$ whose edge pairs use only the five indices $A_W$.

By B1.2, such a slice exists exactly when there is an even support $D$ satisfying

$$
B_W\cap D=M_a.
$$

The distinguished supports are then

$$
F_0=B_W,
\qquad
F_a=D.
$$

## 3. Equal outside-colour cut parities

Let $K$ be a connected component of $G_W$. No $W$-valued edge crosses $\delta_G(K)$. For $c\notin W$, define

$$
n_c(K)
=
|M_c\cap\delta_G(K)|\pmod2.
$$

### Theorem 3.1 — common outside parity

The four bits $n_c(K)$, for $c\in\Gamma\setminus W$, are all equal.

### Proof

Sum the flow equations over all vertices of $K$. Internal edges cancel in characteristic two, giving

$$
\sum_{e\in\delta_G(K)}f(e)=0.
$$

Thus the parity vector

$$
(n_c(K))_{c\notin W}\in\mathbf F_2^4
$$

is a linear relation among the four outside colours. These four vectors form the affine plane $a+W$. They span $\Gamma$: one of them lies outside $W$, and their pairwise differences span $W$. Hence the linear relation space among the four columns has dimension $4-3=1$.

Their total sum is zero, so the unique nonzero relation is $1111$. The parity vector is therefore either $0000$ or $1111$. $\square$

Denote the common bit by

$$
\chi_W(K).
$$

## 4. Distinguished-support and $T$-join criterion

B1.2 proves that an even support $D$ with $B_W\cap D=M_a$ exists exactly when every component $K$ of $G-B_W=G_W$ contains an even number of endpoints of $M_a$. Modulo two, this endpoint count equals the number of $M_a$-edges crossing the component boundary.

### Theorem 4.1 — exact fixed-plane equivalence

For the fixed pair $(f,W)$, the following are equivalent.

1. There is a global five-coordinate slice above $(f,W)$.
2. There is an even support $D$ with
   $$
   B_W\cap D=M_a.
   $$
3. Every component $K$ of $G_W$ contains an even number of endpoints of $M_a$.
4. For every component $K$,
   $$
   n_a(K)=0.
   $$
5. For every component $K$ and every outside colour $c\notin W$,
   $$
   n_c(K)=0.
   $$
6. After contracting every component of $G_W$, each of the four outside-colour classes is an Eulerian edge support in the quotient multigraph.

### Proof

The equivalence $(1)\Longleftrightarrow(2)$ is B1.2. The finite $T$-join criterion there proves $(2)\Longleftrightarrow(3)$. Endpoint parity in a component equals boundary-edge parity, giving $(3)\Longleftrightarrow(4)$. Theorem 3.1 gives $(4)\Longleftrightarrow(5)$. In the contracted quotient, the degree parity of colour $c$ at the vertex representing $K$ is exactly $n_c(K)$, proving $(5)\Longleftrightarrow(6)$. $\square$

### Corollary 4.2 — one colour suffices

For each component it is enough to test one outside colour. If its cut parity is even, all four are even; if it is odd, all four are odd.

## 5. Identification with the local affine obstruction

The recovered fixed-flow packet defines a local boundary bit $\beta_W(v)$ at every degree-one vertex of $G_W$ and a component obstruction

$$
\Omega_W(K)
=
\sum_{\substack{v\in V(K)\\\deg_{G_W}(v)=1}}
\beta_W(v).
$$

### Proposition 5.1 — colour-cut formula

For every component $K$,

$$
\Omega_W(K)=\chi_W(K).
$$

### Proof

At a leaf $v$ of $G_W$, let the unique $W$-edge have value $h$, and write the two outside incident values as

$$
a+w_1,
\qquad
a+w_2,
\qquad
w_1+w_2=h.
$$

The local forbidden-triple classification gives

$$
\beta_W(v)=1+\ell_h(w_1),
$$

where $\ell_h$ is the unique nonzero functional on $W$ with kernel $\langle h\rangle$. In a binary plane this bit is one exactly when one of $w_1,w_2$ is zero, equivalently when one of the two outside edges has colour $a$.

Summing over all leaves of $K$ counts the $a$-coloured edge incidences on $K$. An $a$-edge with both endpoints in $K$ contributes twice; an $a$-edge crossing $\delta_G(K)$ contributes once. Therefore

$$
\Omega_W(K)=n_a(K)=\chi_W(K).
$$

$\square$

### Corollary 5.2

The fixed-plane local-bit criterion

$$
\Omega_W(K)=0
\quad\text{for every }K
$$

is identical to every item of Theorem 4.1.

Thus the following are not separate obstructions:

- singular local-family parity;
- the second distinguished even support $D$;
- the $M_a$ endpoint $T$-join;
- one outside-colour cut parity;
- all four outside-colour parities;
- Eulerian colour classes in the quotient.

They are resolutions of one component obstruction.

## 6. Fixed-flow criterion

For fixed $f$, define

$$
\mathfrak O_f(W)
=
\{K\in\pi_0(G_W):\chi_W(K)=1\}.
$$

### Theorem 6.1 — global-index-factorable criterion above a fixed flow

The fixed Fano flow $f$ admits a compatible affine family with at most five nonempty point-indexed supports if and only if

$$
\exists W\leq\Gamma,
\qquad
\dim W=2,
\qquad
\mathfrak O_f(W)=\varnothing.
$$

### Proof

If at most five of the eight point-indexed supports are nonempty, choose three absent indices. Three distinct points in $\mathbf F_2^3$ have a two-dimensional affine span; let $W$ be its direction plane. After translation, the family is a slice using $A_W$, so Theorem 4.1 applies.

Conversely, if one plane profile is empty, Theorem 4.1 gives a compatible family omitting a forbidden triple of direction $W$, hence using at most five point indices. $\square$

### Negative boundary

The criterion is not automatically true for every fixed flow. A fixed Fano flow may have

$$
\mathfrak O_f(W)\ne\varnothing
$$

for all seven planes. Exact finite computation in the recovered cube packet exhibits such a flow. That certificate is not re-proved here and remains a computation-backed negative boundary.

## 7. Graph-level quantifier

### Theorem 7.1 — graph-level existence in factorable form

A finite loopless cubic multigraph has an indexed five-support even double cover if and only if there exist a nowhere-zero Fano flow $f$ and a plane $W\leq\mathbf F_2^3$ such that

$$
\mathfrak O_f(W)=\varnothing.
$$

### Proof

A five-support cover may be labelled by the five points $A_W$ for any chosen affine-plane model. B1.1 turns its edge pairs into a nowhere-zero Fano flow, and Theorem 4.1 gives an empty plane profile.

Conversely an empty profile produces a five-coordinate affine family, hence a five-support cover. $\square$

This is a complete graph-level existence equivalence because the flow is existentially quantified together with the plane. It is not a theorem that one prescribed flow or one prescribed compatible eight-support lift must succeed.

## 8. Fixed flow, fixed lift, and surface scope

Three levels must remain distinct.

1. **Fixed $(f,W)$.** Theorem 4.1 is complete for one global point-index slice.
2. **Fixed $f$, variable compatible point-index lift.** Theorem 6.1 is complete for globally factorable five-coordinate slices in the affine torsor above $f$.
3. **Fixed compatible root lift $g$ with split support-cycle components.** A map
   $$
   T_g^{(1)}\to\mathscr A_5
   $$
   may relabel distinct support-cycle components independently and need not factor through one global five-point subset of $\Gamma$. Its exact equivalence with five supports is a separate B1.4 surface theorem.

A successful componentwise surface compression over a fixed $g$ still yields a graph-level five-support cover. By Theorem 7.1 that cover defines some factorable Fano-flow presentation, but not necessarily the original $f$ or original point-index lift.

## 9. Easy sufficient cases

- If $G_W$ is connected, its unique component has empty boundary, so every outside-colour parity is zero.
- If all values of $f$ lie in $W$, then $G_W=G$ and the criterion holds. This is the Tait/nowhere-zero four-flow sector.
- More generally, the criterion holds exactly when the contracted outside-colour classes are all Eulerian.

## 10. Components and edge objects

- All component statements include isolated vertices of $G_W$ only when they are incident with outside edges; the cut-parity formula remains valid.
- Parallel source edge objects are counted separately in colour classes and cut multiplicities.
- No connectedness of $G$ is assumed.
- No loop extension is asserted.

## 11. Corpus normalization

The theorem-level claims in `five-support/root-flow-lifting.md`, §§4–6 are correct when read as the global-index-factorable criterion above a fixed flow. The following phrases should be retained explicitly during curation:

- fixed $f$ and fixed $W$;
- global five-coordinate slice;
- dependence only on the direction plane of the forbidden triple;
- existential variation of $f$ at graph level;
- strict separation from the full componentwise surface criterion above a fixed lift.

The fixed-flow cube certificate remains exact finite evidence for failure of the universal fixed-flow strengthening, not a counterexample to graph-level five-support existence.

## 12. Completion assessment

`AC-PD-B1.3` is `COMPLETE-DRAFT`. The next active unit is B1.4: prove the exact correspondence among a compatible root lift, its coloured cycle-face surface, the full dual triangulation, and a componentwise map $T_g^{(1)}\to\mathscr A_5$, while distinguishing the strict global-colour quotient $J_g\to\mathscr A_5$ subroute.
