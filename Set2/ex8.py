def my_zip(*lists):
    """Implements the behaviour of zip() manually (without using zip).
    Receives a variable number of lists and returns a list of tuples:
    the first tuple contains the first elements of each list, the
    second tuple the second elements, etc. If the lists don't have the
    same length, missing elements are replaced with None so that
    max(len(x) for x in lists) tuples are generated."""
    if not lists:
        return []

    max_length = max(len(lst) for lst in lists)

    result = []
    for index in range(max_length):
        row = []
        for lst in lists:
            row.append(lst[index] if index < len(lst) else None)
        result.append(tuple(row))
    return result


if __name__ == "__main__":
    print(my_zip([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))
    # [(1, 5, 'a'), (2, 6, 'b'), (3, 7, 'c')]

    print(my_zip([1, 2], [5, 6, 7, 8]))
    # [(1, 5), (2, 6), (None, 7), (None, 8)]
