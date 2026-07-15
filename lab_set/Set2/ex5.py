def combinations(x, k):
    """Returns a list of tuples representing all combinations of len(x)
    elements taken k at a time from list x (implemented manually,
    without using itertools.combinations)."""
    if k == 0:
        return [()]
    if k > len(x):
        return []

    result = []
    for i in range(len(x) - k + 1):
        first = x[i]
        # combine `first` with every combination of k-1 elements
        # taken from the remaining elements (after position i)
        for rest in combinations(x[i + 1:], k - 1):
            result.append((first,) + rest)
    return result


if __name__ == "__main__":
    print(combinations([1, 2, 3, 4], 3))
    # [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
