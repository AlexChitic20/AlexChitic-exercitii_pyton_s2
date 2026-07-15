from math import gcd
from itertools import combinations


def _line_through(p1, p2):
    """Returns the (a, b, c) coefficients of the line ax + by + c = 0
    passing through points p1 and p2, in a normalized (canonical) form
    so that the same line always produces the same tuple."""
    x1, y1 = p1
    x2, y2 = p2

    a = y2 - y1
    b = x1 - x2
    c = -(a * x1 + b * y1)

    # Normalize: divide by the gcd of the (non-zero) coefficients and
    # fix the sign so the first non-zero coefficient is positive.
    divisor = gcd(gcd(abs(a), abs(b)), abs(c))
    if divisor == 0:
        divisor = 1
    a, b, c = a // divisor, b // divisor, c // divisor

    for value in (a, b, c):
        if value != 0:
            if value < 0:
                a, b, c = -a, -b, -c
            break

    return (a, b, c)


def unique_lines(points):
    """Receives a list of points (tuples (x, y)) and returns a list of
    unique (a, b, c) tuples representing the unique lines determined by
    those points (ax + by + c = 0)."""
    lines = set()
    for p1, p2 in combinations(points, 2):
        lines.add(_line_through(p1, p2))
    return list(lines)


if __name__ == "__main__":
    points = [(0, 0), (1, 1), (2, 2), (0, 2)]
    print(unique_lines(points))
