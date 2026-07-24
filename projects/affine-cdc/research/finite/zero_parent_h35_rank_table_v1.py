from __future__ import annotations

from itertools import combinations
import hashlib
import json

SUPPORTS = range(1, 6)
TRIANGLES = [tuple(c) for c in combinations(SUPPORTS, 3)]

ZETA = {
    "123": 1,
    "124": 2,
    "125": 1,
    "134": 1,
    "135": 0,
    "145": 1,
    "234": 1,
    "235": 0,
    "245": 1,
    "345": 0,
}

SELECTED = {
    "123": "12",
    "125": "12",
    "134": "14",
    "145": "14",
    "234": "24",
    "245": "24",
}


def roots_of(triangle: tuple[int, int, int]) -> list[tuple[int, int]]:
    return [tuple(c) for c in combinations(triangle, 2)]


def root_string(root: tuple[int, int]) -> str:
    return "".join(map(str, root))


def triangle_string(triangle: tuple[int, int, int]) -> str:
    return "".join(map(str, triangle))


def parse_root(value: str) -> tuple[int, int]:
    return tuple(map(int, value))  # type: ignore[return-value]


def parse_triangle(value: str) -> tuple[int, int, int]:
    return tuple(map(int, value))  # type: ignore[return-value]


def xor_root(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, ...]:
    return tuple(sorted(set(a) ^ set(b)))


def distinct_flip(
    left: tuple[int, int, int], right: tuple[int, int, int]
) -> tuple[tuple[int, int], tuple[tuple[int, int], tuple[tuple[int, int, int], tuple[int, int, int]]]] | None:
    common = set(roots_of(left)) & set(roots_of(right))
    if len(common) != 1:
        return None
    central = next(iter(common))
    exterior = [r for r in roots_of(left) if r != central] + [
        r for r in roots_of(right) if r != central
    ]
    current = tuple(sorted((left, right)))
    targets = []
    for pair in ((0, 1), (0, 2), (0, 3)):
        other = tuple(i for i in range(4) if i not in pair)
        first = xor_root(exterior[pair[0]], exterior[pair[1]])
        second = xor_root(exterior[other[0]], exterior[other[1]])
        if first != second or len(first) != 2:
            continue
        new_root = tuple(first)  # type: ignore[assignment]
        first_triangle = tuple(
            sorted(set(exterior[pair[0]]) | set(exterior[pair[1]]) | set(new_root))
        )
        second_triangle = tuple(
            sorted(set(exterior[other[0]]) | set(exterior[other[1]]) | set(new_root))
        )
        target = tuple(sorted((first_triangle, second_triangle)))
        if target != current:
            targets.append((new_root, target))
    assert len(targets) == 1, (left, right, targets)
    return central, targets[0]


def tau_35(triangle: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(
        sorted(5 if x == 3 else 3 if x == 5 else x for x in triangle)
    )  # type: ignore[return-value]


def in_h35(root: tuple[int, int]) -> bool:
    return len(set(root) & {3, 5}) == 1


def build_certificate() -> dict:
    orbit_rows = []
    for triangle in TRIANGLES:
        image = tau_35(triangle)
        orbit_rows.append(
            {
                "triangle": triangle_string(triangle),
                "tau35": triangle_string(image),
                "zeta": ZETA[triangle_string(triangle)],
                "zeta_tau": ZETA[triangle_string(image)],
            }
        )

    strict_rows = []
    for triangle_name, central_name in SELECTED.items():
        triangle = parse_triangle(triangle_name)
        selected_root = parse_root(central_name)
        for neighbour in TRIANGLES:
            if neighbour == triangle or selected_root not in roots_of(neighbour):
                continue
            result = distinct_flip(triangle, neighbour)
            if result is None or result[0] != selected_root:
                continue
            new_root, target = result[1]
            source_weight = ZETA[triangle_name] + ZETA[triangle_string(neighbour)]
            target_weight = sum(ZETA[triangle_string(t)] for t in target)
            row = {
                "central": central_name,
                "source": sorted([triangle_name, triangle_string(neighbour)]),
                "target": [triangle_string(t) for t in target],
                "target_central": root_string(new_root),
                "zeta_source": source_weight,
                "zeta_target": target_weight,
                "delta": target_weight - source_weight,
            }
            if row not in strict_rows:
                strict_rows.append(row)
    strict_rows.sort(key=lambda row: (row["central"], row["source"]))

    plateau_rows = []
    for triangle in TRIANGLES:
        h_roots = [root for root in roots_of(triangle) if in_h35(root)]
        non_h_roots = [root for root in roots_of(triangle) if not in_h35(root)]
        plateau_rows.append(
            {
                "triangle": triangle_string(triangle),
                "H35_degree": len(h_roots),
                "H35_roots": [root_string(root) for root in h_roots],
                "non_H35_roots": [root_string(root) for root in non_h_roots],
                "zeta": ZETA[triangle_string(triangle)],
                "selected": SELECTED.get(triangle_string(triangle)),
            }
        )

    zero_node_rows = []
    zero_types = [parse_triangle(name) for name in ("135", "235", "345")]
    for left, right in combinations(zero_types, 2):
        result = distinct_flip(left, right)
        assert result is not None
        central, (new_root, target) = result
        zero_node_rows.append(
            {
                "source": [triangle_string(left), triangle_string(right)],
                "central": root_string(central),
                "other_root_transition": [triangle_string(t) for t in target],
                "other_central": root_string(new_root),
            }
        )

    certificate = {
        "tau35_invariance": orbit_rows,
        "strict_rows": strict_rows,
        "plateau_types": plateau_rows,
        "zero_node_transitions": zero_node_rows,
        "claims": {
            "zeta_nonnegative": True,
            "zeta_max": 2,
            "strict_rows_count": len(strict_rows),
            "strict_delta_multiset": sorted(row["delta"] for row in strict_rows),
            "only_H35_degree_zero_type": [
                row["triangle"] for row in plateau_rows if row["H35_degree"] == 0
            ],
            "zero_types": [
                row["triangle"]
                for row in plateau_rows
                if row["H35_degree"] == 2 and row["zeta"] == 0
            ],
        },
    }
    return certificate


if __name__ == "__main__":
    certificate = build_certificate()
    canonical = json.dumps(certificate, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode()).hexdigest()
    expected = "aa6446dd5a01f8d4048807ff81b5f596c148f5b92224f529220277cf862e6eff"
    assert digest == expected, (digest, expected)
    print(json.dumps(certificate, sort_keys=True, indent=2))
    print(f"sha256={digest}")
