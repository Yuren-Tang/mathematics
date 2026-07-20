# AC-PD-B1.2 — exact matching/four-flow equivalence

**Proof-development state:** `COMPLETE-DRAFT / CORPUS-CORRECTION`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Recovered controlling packet:** `research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c:projects/affine-cdc/research/FIVE_CDC_MATCHING_FOUR_FLOW_BRIDGE_V1.md`  
**Depends on:** B1.1; elementary binary-flow and finite $T$-join lemmas  
**Immediate consumers:** B1.3 fixed-plane/component criterion; B2 equivalent-formulation normalization  
**External mathematical inputs:** none

## 0. Correction to the integrated summary

The integrated chapter currently says, in effect, that after choosing one distinguished support coordinate, roots incident with that coordinate form a matching and their deletion carries a nowhere-zero $\mathbf F_2^2$-flow. Taken literally, this is false.

At a local $K_5$ triangle, a fixed **support coordinate** occurs on either zero or two of the three root labels. Its inverse image is therefore an even support, not generally a matching.

The correct matching/four-flow theorem uses two even distinguished supports. In the affine-plane presentation below, one is the outside-plane binary support $B$ and the other is a selected support $D$; their intersection

$$
M=B\cap D
$$

is a matching. Equivalently, in a pure $K_5$ root labelling, the inverse image of one fixed **root label** is a matching, but a four-flow on its complement is not by itself sufficient: compatible root-fibre or boundary data must also be supplied. The pair $(B,D)$ records exactly that missing datum.

## 1. The five allowed affine indices

Let

$$
\Gamma=\mathbf F_2^3,
\qquad
W\leq\Gamma,
\qquad
\dim W=2,
$$

and choose $a\in\Gamma\setminus W$. Define the five-point set

$$
A=\{0\}\sqcup(a+W).
$$

A five-support affine family indexed by $A$ assigns to every edge an unordered two-element subset of $A$ and is locally even at every cubic vertex. Its edge difference is a nonzero vector of $\Gamma$.

For a $\Gamma$-valued flow $f$, write uniquely

$$
f=w+ba,
$$

with

$$
w:E(G)\to W,
\qquad
b:E(G)\to\mathbf F_2.
$$

Both $w$ and $b$ are flows whenever $f$ is a flow.

## 2. The exact matching/four-flow datum

### Definition 2.1

An **exact matching/four-flow datum** on a finite loopless cubic multigraph $G$ consists of:

1. two even edge supports $B,D\subseteq E(G)$;
2. their intersection
   $$
   M=B\cap D,
   $$
   required to be a matching;
3. a nowhere-zero $W$-flow
   $$
   w:E(G-M)\longrightarrow W\setminus\{0\}.
   $$

Extend $w$ by zero on $M$. Since the conservation equations on $G-M$ are unchanged by adjoining zero-valued deleted edges, the extension remains a $W$-flow on $G$.

## 3. From a five-support cover to matching/four-flow data

Let $(F_s)_{s\in A}$ be a five-support affine family and let $f(e)$ be the difference of the two support indices assigned to $e$. By B1.1, $f$ is a nowhere-zero $\Gamma$-flow.

Write $f=w+ba$ and define

$$
B=\operatorname{supp}b,
\qquad
D=F_a,
\qquad
M=\{e:w(e)=0\}.
$$

### Proposition 3.1 — the projected zero set

One has:

1. $B$ is even;
2. $M\subseteq B$;
3. $M$ is a matching;
4. $w|_{G-M}$ is a nowhere-zero $W$-flow.

### Proof

The support of the binary flow $b$ is even. If $e\notin B$, then $b(e)=0$ and $f(e)=w(e)\ne0$, so every zero of $w$ lies in $B$.

At a cubic vertex, $b$ has either zero or two incident one-edges. If two incident edges belonged to $M$, their $w$-values would both be zero; conservation of $w$ would force the third $w$-value to be zero. The third edge is outside $B$, because $B$ has local degree two, and hence $f=w=0$ there, contradicting nowhere-zeroness. Thus at most one incident edge lies in $M$, so $M$ is a matching. Deleting precisely the zero-valued edges makes the restriction of $w$ nowhere zero. $\square$

### Proposition 3.2 — distinguished support identity

$$
F_0=B,
\qquad
F_a\cap F_0=M.
$$

Consequently $M=B\cap D$.

### Proof

If $b(e)=0$, then $f(e)=w(e)\in W\setminus\{0\}$. The two assigned indices have difference in $W$, so they both lie in the affine plane $a+W$; hence $0$ is not assigned.

If $b(e)=1$, then $f(e)=a+w(e)\notin W$. Among the five allowed points $A$, the unique pair with this difference and one endpoint outside $a+W$ is

$$
\{0,a+w(e)\}.
$$

Thus $e\in F_0$ exactly when $e\in B$. Such an edge also lies in $F_a$ exactly when $a+w(e)=a$, equivalently $w(e)=0$, equivalently $e\in M$. $\square$

Since $F_0$ and $F_a$ are even supports, $(B,D,M,w)$ is exact matching/four-flow data.

## 4. Direct reconstruction from exact data

Now start from even supports $B,D$, the matching $M=B\cap D$, and a nowhere-zero $W$-flow $w$ on $G-M$. Extend $w$ by zero on $M$, define

$$
b=\mathbf1_B,
\qquad
f=w+ba.
$$

### Proposition 4.1 — reconstructed Fano flow

The map $f$ is a nowhere-zero $\Gamma$-flow.

### Proof

Since $B$ is even, $b$ is a binary flow. The extended $w$ is a $W$-flow, so $f$ is a $\Gamma$-flow.

If $e\notin B$, then $e\notin M$ and $f(e)=w(e)\ne0$. If $e\in B$, the $a$-coordinate of $f(e)$ is one, so $f(e)\ne0$. $\square$

We now assign one unordered pair $P_e\subseteq A$ to every edge.

### Definition 4.2 — edge pairs

- If $e\in B$, set
  $$
  P_e=\{0,a+w(e)\}.
  $$
- If $e\notin B$, then $h=w(e)\in W\setminus\{0\}$. The affine plane $a+W$ has exactly two lines of direction $h$. Choose the unique one containing $a$ when $e\in D$, and the unique one not containing $a$ when $e\notin D$.

In both cases, the difference of the two points of $P_e$ is $f(e)$.

### Theorem 4.3 — local triangle law

At every vertex, the three pairs $P_e$ are the three edges of a triangle on the five-point set $A$.

### Proof

Because $B$ is even and the graph is cubic, the local $B$-degree is zero or two.

**Case 1: no incident edge lies in $B$.**  
The three nonzero $w$-values sum to zero in the binary plane $W$, so they are the three distinct nonzero directions of $W$. The three selected pairs are one affine line in each direction inside $a+W$. Membership of $a$ in the selected line is exactly membership of the source edge in $D$. Since $D$ is even, zero or two selected lines contain $a$.

If none contains $a$, the three lines are the three edges joining the other three points of $a+W$. If exactly two contain $a$, they join $a$ to two other points and the third selected line is the edge joining those two points. In either subcase the three pairs form a triangle.

**Case 2: exactly two incident edges $e_1,e_2$ lie in $B$.**  
Let $e_3$ be the remaining edge. Then

$$
P_{e_1}=\{0,a+w_1\},
\qquad
P_{e_2}=\{0,a+w_2\},
$$

where $w_1+w_2=w_3\ne0$. The points $a+w_1$ and $a+w_2$ are distinct. The third side of their triangle with $0$ is

$$
\{a+w_1,a+w_2\},
$$

an affine line of direction $w_3$ in $a+W$.

Because $M$ is a matching, at most one of $w_1,w_2$ is zero. The displayed third side contains $a$ exactly when one of them is zero, equivalently when exactly one of $e_1,e_2$ lies in $M=B\cap D$. Evenness of $D$ then says exactly that $e_3\in D$. Definition 4.2 therefore chooses precisely this third side. $\square$

### Corollary 4.4 — reconstructed five-support cover

For $s\in A$, define

$$
F_s=\{e:s\in P_e\}.
$$

Then $(F_s)_{s\in A}$ is an indexed five-support even double cover, with

$$
F_0=B,
\qquad
F_a=D.
$$

### Proof

Every pair $P_e$ contains exactly two indices, giving exact double coverage. Theorem 4.3 gives local degree zero or two for every support index. The definitions show that $0\in P_e$ exactly for $e\in B$ and $a\in P_e$ exactly for $e\in D$. $\square$

## 5. Exact equivalence theorem

### Theorem 5.1

For a finite loopless cubic multigraph $G$, the following are equivalent.

1. $G$ has an indexed five-support even double cover.
2. For some $\Gamma\cong\mathbf F_2^3$, plane $W\leq\Gamma$, and $a\notin W$, $G$ has a compatible affine family using only the five indices $\{0\}\sqcup(a+W)$.
3. $G$ has exact matching/four-flow data $(B,D,M,w)$ as in Definition 2.1.

### Proof

B1.1 labels any five support indices by the five points of $A$ and turns every local support pattern into a triangle of pairs; their differences give the compatible affine family, proving $(1)\Rightarrow(2)$. Forgetting unused ambient indices gives $(2)\Rightarrow(1)$.

Propositions 3.1 and 3.2 prove $(2)\Rightarrow(3)$. Proposition 4.1 and Corollary 4.4 prove $(3)\Rightarrow(2)$. $\square$

## 6. Elimination of the second even support

The datum $D$ may be replaced by a component parity condition.

Let $H=G-B$. Since $M\subseteq B$, every endpoint of an edge of $M$ is a vertex of $H$. Let $T\subseteq V(H)$ be the set of vertices incident with an odd number of edges of $M$. Because $M$ is a matching, this is simply the endpoint set of $M$, with an edge whose two endpoints lie in the same $H$-component contributing two vertices there.

### Lemma 6.1 — finite $T$-join criterion

For a finite graph $H$ and $T\subseteq V(H)$, there exists an edge set $P\subseteq E(H)$ whose odd-degree vertex set is exactly $T$ if and only if every connected component of $H$ contains an even number of vertices of $T$.

### Proof

Necessity is the handshaking lemma in each component. For sufficiency, pair the vertices of $T$ arbitrarily within each component, choose one path for every pair, and take the symmetric difference of all chosen path edge sets. Internal path vertices occur evenly; the paired endpoints occur oddly. $\square$

### Proposition 6.2 — component form of the matching datum

Let $B$ be even and let $M\subseteq B$ be a matching. There exists an even support $D$ with

$$
B\cap D=M
$$

if and only if every connected component $K$ of $G-B$ contains an even number of endpoints of $M$. Equivalently,

$$
|M\cap\delta_G(K)|\equiv0\pmod2
$$

for every component $K$ of $G-B$.

### Proof

Write $D=M\sqcup P$ with $P\subseteq E(G-B)$. The support $D$ is even exactly when the odd-degree set of $P$ equals the endpoint-parity set of $M$. Apply Lemma 6.1.

For one component $K$, an $M$-edge with both endpoints in $K$ contributes two endpoints and no cut edge; an $M$-edge with one endpoint in $K$ contributes one endpoint and one cut edge. Hence endpoint parity equals $|M\cap\delta_G(K)|$ modulo two. $\square$

### Corollary 6.3 — corrected concise matching/four-flow criterion

A finite loopless cubic multigraph has an indexed five-support even double cover if and only if there exist:

1. an even support $B$;
2. a matching $M\subseteq B$;
3. a nowhere-zero $\mathbf F_2^2$-flow on $G-M$;
4. even $M$-endpoint parity in every component of $G-B$.

The fourth item is the precise “terminal behaviour” omitted by the integrated one-line formulation.

## 7. Relation to a fixed root label

In any $K_5$ triangle labelling, the inverse image of one fixed target edge $r\in E(K_5)$ is indeed a matching, because a triangle contains each target edge at most once. However, deleting that matching and retaining only a projected $\mathbf F_2^2$ value on the remaining source edges forgets which root in each projection fibre was chosen. The exact lift or component-parity datum above is required for the converse.

Thus the valid statements are:

- fixed **root label** inverse image $\Rightarrow$ matching;
- fixed **support coordinate** inverse image $\Rightarrow$ even support;
- matching plus four-flow plus exact boundary/lift datum $\Longleftrightarrow$ five supports.

Conflating these three levels creates a false converse.

## 8. Components and degenerate cases

- **Disconnected graph.** The theorem is componentwise, including the $T$-join criterion.
- **Empty graph.** Take $B=D=M=\varnothing$ and the empty $W$-flow.
- **Parallel edges.** All supports, matchings, flows, and path symmetric differences count edge objects separately.
- **Repeated supports.** $B$ and $D$ may coincide only when their common support is itself a matching and even; in a loopless cubic graph this forces it to be empty. Other support indices may repeat freely.
- **Loops.** No loop extension is asserted.

## 9. Corpus correction recommendation

The following integrated statements require correction before Curator promotion of Programme B:

1. `five-support/root-flow-lifting.md`, §3.3: replace “choose one support coordinate; roots incident with it form a matching” by the exact $(B,D,M,w)$ theorem or Corollary 6.3.
2. Theorem 3.1 there: replace the undefined phrase “appropriate terminal behaviour” by the explicit component-parity condition.
3. `five-support/equivalent-formulations-and-proof-families.md`, global item 5: point to the exact datum, not a bare matching and four-flow.
4. `THEOREM_DEPENDENCY_MAP.md`, object layer: annotate the matching/four-flow node with the required even-support/component boundary datum.

The recovered source packet already contained the stronger correct theorem. The error arose in synthesis compression, not in the controlling research checkpoint.

## 10. Completion assessment

`AC-PD-B1.2` is `COMPLETE-DRAFT / CORPUS-CORRECTION`. The next active unit is B1.3: normalize the fixed Fano-flow/fixed-plane criterion and prove its exact equivalence with the component parity and distinguished-support/$T$-join forms, while keeping the fixed-flow quantifier separate from the graph-level five-support theorem.
