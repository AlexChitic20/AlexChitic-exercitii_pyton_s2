def list_operations(a, b):
    
    intersection = []
    for item in a:
        if item in b and item not in intersection:
            intersection.append(item)

    union = []
    for item in a + b:
        if item not in union:
            union.append(item)

    a_minus_b = []
    for item in a:
        if item not in b and item not in a_minus_b:
            a_minus_b.append(item)

    b_minus_a = []
    for item in b:
        if item not in a and item not in b_minus_a:
            b_minus_a.append(item)

    return intersection, union, a_minus_b, b_minus_a


if __name__ == "__main__":
    result = list_operations([1, 2, 3, 4], [3, 4, 5, 6])
    print(result)
    # ([3, 4], [1, 2, 3, 4, 5, 6], [1, 2], [5, 6])
