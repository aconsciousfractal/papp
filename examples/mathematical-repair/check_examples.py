"""Selected finite examples for the mathematical-repair worked example.

Worked example contributed by Alexandre Couret, prepared with AI assistance and adapted for PAPP by Oleksiy Babanskyy.

Package: PAPP/math-repair-example-0.1.0. See ATTRIBUTION.md and REUSE_NOTICE.md.
The specific permission is not an unqualified MIT grant for this contribution.
Standard library only; finite checks, not general proofs or PAPP efficacy.
"""
import json
from itertools import combinations


def square(n, support):
    """Integer ordered sum counts, including diagonal pairs, on labelled C_n."""
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")
    support = tuple(support)
    if len(set(support)) != len(support) or any(
        type(a) is not int or not 0 <= a < n for a in support
    ):
        raise ValueError("support must contain distinct labels in 0,...,n-1")
    return tuple(sum((a + b) % n == x for a in support for b in support)
                 for x in range(n))


def decode_known_domain(n, observed, allowed):
    """Recover a binary subset only on a supplied domain with injective doubling."""
    allowed = tuple(allowed)
    square(n, allowed)  # Validate the declared labels.
    observed = tuple(observed)
    if len(observed) != n or any(type(v) is not int or v < 0 for v in observed):
        raise ValueError("one nonnegative integer count per label is required")
    if len({2 * a % n for a in allowed}) != len(allowed):
        raise ValueError("doubling must be injective on the known allowed domain")
    candidate = frozenset(a for a in allowed if observed[2 * a % n] % 2)
    if square(n, candidate) != observed:
        raise ValueError("decoded bits do not reproduce the full integer data")
    return candidate


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def run():
    c6 = square(6, (0, 1, 2))
    require(c6 == square(6, (3, 4, 5)) == (1, 2, 3, 2, 1, 0), "C6 collision")
    require({(a + 3) % 6 for a in (0, 1, 2)} == {3, 4, 5}, "C6 translation")
    unknown = square(6, (0,))
    require(unknown == square(6, (3,)) == (1, 0, 0, 0, 0, 0),
            "unknown antipodal representative")

    domain = (0, 1, 2)
    supports = [s for k in range(4) for s in combinations(domain, k)]
    for support in supports:
        require(decode_known_domain(6, square(6, support), domain) == set(support),
                "known C6 domain recovery")
    odd_support = (0, 2, 4)
    require(decode_known_domain(5, square(5, odd_support), range(5)) == set(odd_support),
            "selected odd-order example")

    return {
        "status": "PASS",
        "scope": "Selected finite examples only; the general argument is in README.md.",
        "C6_exact_collision": {"S": [0, 1, 2], "T": [3, 4, 5],
                               "square": list(c6), "translation": 3},
        "C6_unknown_representative_collision": {"S": [0], "T": [3],
                                                "square": list(unknown)},
        "C6_known_domain": {"D": list(domain), "subsets_checked": len(supports)},
        "C5_selected_odd_example": {"S": list(odd_support),
                                    "square": list(square(5, odd_support))},
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
