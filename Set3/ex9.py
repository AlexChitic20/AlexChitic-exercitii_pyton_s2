from itertools import combinations


def pairwise_set_operations(*sets):
  
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
