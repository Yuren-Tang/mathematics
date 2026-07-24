#!/usr/bin/env python3
"""Independent finite check for AC-5CDC-AUDIT-RETURN-01, unit G.

Roots are 2-subsets of {1,2,3,4,5}; Petersen adjacency is disjointness.
The script enumerates every ordered nonbacktracking path x-s-t-y and checks
z=x△t, w=s△y are distinct roots meeting in exactly one support.  It also
checks the three pairings of (z,z,w,w): one has central value 0 and two have
the root z△w.

This certificate is supplementary.  The human normal-form reduction
s=12,t=34 remains the mathematical proof.
"""

from itertools import combinations

ROOTS = tuple(frozenset(pair) for pair in combinations(range(1, 6), 2))


def is_root(value: frozenset[int]) -> bool:
    return len(value) == 2


def add(left: frozenset[int], right: frozenset[int]) -> frozenset[int]:
    return left.symmetric_difference(right)


def main() -> None:
    count = 0
    failures: list[tuple[object, ...]] = []

    for x in ROOTS:
        for s in ROOTS:
            if not x.isdisjoint(s):
                continue
            for t in ROOTS:
                if not s.isdisjoint(t) or x == t:
                    continue
                for y in ROOTS:
                    if not t.isdisjoint(y) or s == y:
                        continue

                    count += 1
                    z = add(x, t)
                    w = add(s, y)
                    u = add(z, w)

                    # Pairing equal labels gives 0; either crossed pairing gives u.
                    central_values = (add(z, z), add(z, w), add(z, w))
                    ok = (
                        is_root(z)
                        and is_root(w)
                        and z != w
                        and len(z.intersection(w)) == 1
                        and central_values[0] == frozenset()
                        and is_root(central_values[1])
                        and central_values[1] == central_values[2] == u
                    )
                    if not ok:
                        failures.append((x, s, t, y, z, w, central_values))

    assert count == 120, count
    assert not failures, failures
    print("120/120 ordered nonbacktracking four-pivot cases verified")


if __name__ == "__main__":
    main()
