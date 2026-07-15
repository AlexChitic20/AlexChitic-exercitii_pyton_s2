from itertools import combinations


def pairwise_set_operations(*sets):
    """Receives a variable number of sets and returns a dictionary with
    the result sizes of the union (|), intersection (&), a-b and b-a
    operations for every pair of sets (two by two). Keys look like
    "a op b" (using the string representation of each set)."""
    result = {}
    for a, b in combinations(sets, 2):
        result[f"{a} | {b}"] = len(a | b)
        result[f"{a} & {b}"] = len(a & b)
        result[f"{a} - {b}"] = len(a - b)
        result[f"{b} - {a}"] = len(b - a)
    return result


if __name__ == "__main__":
    print(pairwise_set_operations({1, 2}, {2, 3}))
    # {'{1, 2} | {2, 3}': 3, '{1, 2} & {2, 3}': 1,
    #  '{1, 2} - {2, 3}': 1, '{2, 3} - {1, 2}': 1}
