# CURATION-HANDOFF — AffineCDC Programme A Audit A repairs

**Project:** AffineCDC  
**Prepared by:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Controlling repair intake:** `Yuren-Tang/research-workbench#37`, comment `5019649863`  
**Audit source:** `AC-AUDIT-A`, `Yuren-Tang/research-workbench#35`  
**Live source branch:** `Yuren-Tang/mathematics:proof-development/affine-cdc-rigour-v1`  
**Immutable Programme A source:** `8bee16780b549f51e1f29343671a059961ec4172`  
**Immutable Audit A repair checkpoint:** `06bce656dcf5bfd6491ec08f51a702ea56d2470d`  
**DAG registration checkpoint:** `d3ef3696eac021ccf887709479bcc9b7ce849d64`  
**Included repair dossier:** `projects/affine-cdc/proof-development/AC_PD_A_AUDIT_A_EXPLICITNESS_REPAIRS.md`  
**Classification:** `PROOF-DEVELOPMENT / PROGRAMME-A / AUDIT-A / EXPOSITORY-REPAIR / READY-FOR-CURATOR`  
**Theorem change:** none  
**New-mathematics gap:** none  
**Live branch continues:** yes, under the standing proof-obligation DAG  
**Staging authorized:** dedicated Curator branch only  
**Canonical/default-branch movement:** not authorized by this handoff

## 1. Intake objective

Integrate the three non-blocking explicitness repairs returned by Independent Audit A into the preferred Programme A corpus while preserving exact provenance and theorem status.

Audit A's overall result remains:

`VERIFIED SUBJECT TO NAMED EXTERNAL THEOREMS / NON-BLOCKING EXPLICITNESS REPAIRS`.

The bounded repair epoch is complete. This handoff does not ask Curator to redo the mathematics, extend the five-support frontier, modify Lean, or move any release/publication surface.

## 2. Exact repair packet

### 2.1 Seymour multigraph convention

The controlling A3 external theorem is now explicit:

- finite connected loopless multigraph;
- parallel edge objects permitted;
- no isthmus / 2-edge-connected in the source convention;
- apply independently to each edge-bearing component of the disconnected A3 input;
- isolated vertices and the empty graph are inert;
- loops have already been removed by A1.

The accessible source convention is DeVos–Rollová–Šámal, §1 and Theorem 2: parallel edges permitted, loops forbidden, every 2-edge-connected graph has a nowhere-zero six-flow.

No simple-graph reduction and no connectedness assumption remain implicit.

### 2.2 A4 reverse local-family reconstruction

The compressed converse in A4 Proposition 4.2 is replaced by a complete algebraic proof.

For directions

\[
h_1+h_2+h_3=0,
\]

an even triple of affine lines `L_i` has unique pairwise intersection points

\[
x_{12},x_{13},x_{23}.
\]

Parity forces

\[
x_{13}=x_{12}+h_1,
\qquad
x_{23}=x_{12}+h_2,
\]

and the third direction identity gives

\[
x_{13}+x_{23}=h_3.
\]

With

\[
m=x_{12}+h_3,
\]

the three lines are exactly

\[
\begin{aligned}
L_1&=\{m+h_2,m+h_3\},\\
L_2&=\{m+h_1,m+h_3\},\\
L_3&=\{m+h_1,m+h_2\}.
\end{aligned}
\]

Thus every even family is uniquely `\Phi_v(m)`. For `\Gamma=\mathbf F_2^3` there are exactly eight families, but the repaired proof works over every finite-dimensional ambient `\mathbf F_2`-space.

### 2.3 Old Tutte route status

The derivation in

`projects/affine-cdc/reduction/outer-shell-and-binary-flow.md`, §§4.1–4.2,

is to be retained only as a historical alternative.

The controlling proof is A3:

\[
\text{integral 6-flow}
\to
\text{integral 8-flow}
\to
\mathbf Z/8\mathbf Z\text{-flow}
\to
\mathbf F_2^3\text{-flow},
\]

where equal-order transport is proved internally by the explicit nowhere-zero-flow count formula.

The old Tutte route is not a logical premise of Programme A and must not override the A3 dependency statement.

## 3. Required integration locations

Curator should incorporate the repaired content into the rolling Programme A corpus at all applicable representations:

1. the retained A3 dossier and the preferred integrated binary-flow chapter: add the exact multigraph/source convention;
2. the retained A4 dossier and the preferred integrated affine-incidence chapter: replace the compressed converse by the complete reconstruction or an exactly equivalent proof;
3. the old outer-shell companion: add a prominent historical-route notice at §§4.1–4.2;
4. integration/dependency/status maps: record Audit A repairs as closed without changing theorem strength.

The authorial repair overlay must remain recoverable even after prose is absorbed.

## 4. Curator success test

The intake is successful exactly when:

1. A3 states, without implication or convention gap, that the Seymour input permits parallel edges and forbids loops, and explains componentwise assembly;
2. A4 contains a complete reverse proof from arbitrary even local line family to a unique deleted point;
3. every active corpus reader can distinguish the controlling A3 proof from the historical Tutte route;
4. the complete CDC theorem remains subject only to the named classical Seymour input and no new external premise is introduced;
5. Audit A's three findings are marked closed as `EXPOSITORY-REPAIR`, not silently deleted;
6. the immutable source `8bee167...` and repair checkpoint `06bce65...` remain recoverable;
7. Programme B and the six B9/AC-RL frontier obligations remain unchanged;
8. no Lean, manuscript, release, publication, arXiv, DOI, tag, or `main` movement is implied.

## 5. Non-authorizations

This handoff does not authorize:

- rewriting or force-moving the PDL branch;
- editing Research Lead or audit branches;
- declaring the Programme A proof Lean-formalized;
- declaring the repair independently re-audited;
- promoting the five-support strengthening to proved;
- canonical/default-branch integration without the receiving governance disposition;
- release, manuscript, submission, arXiv, DOI, or publication action.

## 6. Continuing proof-development state

After this bounded repair epoch, AC-PDL returns to the standing DAG.

Programme A is `READY-FOR-CURATOR / AUDIT-A-REPAIRED`.

Programme B9 remains `BLOCKED-FRONTIER / CORRECTED-ASSEMBLY / AC-RL-DEPENDENT` with the same six exact unresolved obligations. No further authorial action is justified on those arrows until a genuine AC-RL proof packet, Curator repair request, or other authorized assurance return arrives.

Staging is authorized; canonical movement is not.