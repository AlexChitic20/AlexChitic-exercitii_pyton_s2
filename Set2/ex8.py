def my_zip(*lists):
  
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
