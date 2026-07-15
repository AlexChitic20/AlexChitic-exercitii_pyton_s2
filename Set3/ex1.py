def set_operations(a, b):
    """Receives two lists a and b and returns a tuple of sets containing:
    (a intersected with b, a union b, a - b, b - a)."""
    set_a, set_b = set(a), set(b)
    return (set_a & set_b, set_a | set_b, set_a - set_b, set_b - set_a)


if __name__ == "__main__":
    print(set_operations([1, 2, 3, 4], [3, 4, 5, 6]))
    # ({3, 4}, {1, 2, 3, 4, 5, 6}, {1, 2}, {5, 6})
