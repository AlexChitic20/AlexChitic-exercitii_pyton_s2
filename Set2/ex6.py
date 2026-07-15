def elements_in_exactly_x_lists(*lists, x):
    """Receives a variable number of lists and an integer x. Returns a
    list with the elements that appear in exactly x of the given lists
    (an element counts once per list it appears in, no matter how many
    times it's repeated inside that list)."""
    result = []
    seen = []
    for lst in lists:
        for item in lst:
            if item in seen:
                continue
            seen.append(item)
            count = sum(1 for other_list in lists if item in other_list)
            if count == x:
                result.append(item)
    return result


if __name__ == "__main__":
    print(elements_in_exactly_x_lists(
        [1, 2, 3], [2, 3, 4], [4, 5, 6], [7, 1, "test"], x=2))
    # [1, 2, 3, 4]
