# Component-chain failure and repair packet

## 1. Exact sources

- RL theorem source: `research/affine-cdc-five-cdc-v1@02b37476198e9eaa2b4cd8d2a2edd76782bdcd49`;
- PDL reconstruction: `proof-development/affine-cdc-rigour-v1@e36ba22f09e3a9fc6358f3b03615f8fde6c00d96`;
- independent audit: `audit/affine-cdc-component-chain-v1@a4f20f05532c307a3a8f9d98ac4c5162e7b8ad57`;
- permanent earlier `Xi` audit: `53be22a0f65b85068b11e5f781579618967db9dd`.

The general theorem is a failed candidate, not an open unreviewed proposal.

## 2. Failed scope

The source chooses distinguished terminal paths $P_0,P_1$ and a shortest quotient chain between them. It handles an internal node only when it is:

- an inactive singleton; or
- a closed channel component.

It omits the possibility of another terminal path component internally.

## 3. Exact audit witness

```text
h=14
cut channel edges: 1-14:13, 10-11:12, 13-14:12

P_0={1,2,3,4,5,6,11}
X_1={7,8,9,10,12,13}
P_1={14}

chain:
P_0 -- 3-8:14 -- X_1 -- 9-14:23 -- P_1.
```

Here $X_1$ is a third terminal path. The first root NNI

```text
134+124 -> 234+123, central 14 -> 23
retain 2-3@3, 8-9@8
move 7-8@8 -> 3, 3-4@3 -> 8
```

splits the old $P_0$ terminal darts between two $H_{14}$ components. No inherited $P_0'$ remains.

Finite enumeration:

```text
18 non-cut central edges
36 labelled root-NNI movies
36 category-safe outputs
0 inherited length-1 chains for the original terminal pairs.
```

Digest:

`d24c63ab56320803b9c795ac08389674b6f67edf89dc5c4ef9a729c5436a3e61`.

## 4. Independently retained local core

Audit `a4f20f05...` verified:

- channel degree `0/2` and unique inactive triangle;
- six active/inactive rows and twenty-four ordered continuation cases;
- six distinct active/active rows;
- nine equal-endpoint root branch swaps;
- eighty-four final two-terminal configurations, with forty-two per crossed matching and zero preserving the old matching;
- co-root `6-7` route-changing model;
- zero-parent Heawood `H_35` model.

Local-row digest:

`75ed977851a944f2cd80577e629a2f6936da5dfce49ad9d5a9e0e82c8b2494d4`.

Aggregate digest:

`2353b22b111c9dd47319b2c14637c08d93ae2f4eac10605a00f29c5f46842fe8`.

## 5. Exact repair alternatives

### Repair A — application-specific terminal exhaustion

Prove for both co-root and zero-parent carriers:

- exactly two terminal path components occur;
- every other nontrivial channel component is closed;
- all inactive vertices are singleton quotient nodes;
- every selected connector avoids splitting the distinguished terminal darts.

### Repair B — generalized internal-terminal contraction

Allow an internal terminal path and prove a move/rank that:

- preserves the identities of $P_0,P_1$;
- does not split their terminal dart sets;
- updates or eliminates the internal terminal path;
- retains a strictly shorter physical witness;
- preserves cap, route, category, parent and prefix fields.

### Repair C — alternative return mechanism

Give a different literal source history for both singular fibres, without arbitrary equal-face, generic-connectivity, SCC-distance or lower-flow shortcuts.

## 6. Co-root review target

The explicit `6-7:23` movie is valid locally and changes

```text
(1,2)|(3,6) -> (1,3)|(2,6).
```

A repair must prove that every category-safe co-root carrier reaches an equivalent two-arc geometry or another named terminal. One positive Heawood movie is not totality.

## 7. Zero-parent review target

The exact `H_35` Heawood movie is valid locally. A repair must prove that every zero-parent carrier reaches the required two-terminal crossed matching, or give a different universal route. The old direct-terminal inherited-flow shortcut remains forbidden.

## 8. Integration requirements

Any repaired theorem must supply exact maps for:

- distinguished terminal dart sets;
- physical connector ancestry;
- source/target topology;
- support labels and stable darts;
- cap and route/profile;
- graph category and every terminal output;
- stored prefix and next inverse source move.

## 9. Required future verdicts

A new reviewer should return separately:

1. repaired standalone chain/return theorem;
2. universal co-root corollary;
3. universal zero-parent corollary;
4. complete inverse-table integration;
5. ordinary induction;
6. compatibility with the accepted outer shell.

The old general theorem may not be restored by adding prose unless the exact third-terminal-path witness is excluded or handled.