def _deep_equal(a, b):
    """Recursively compares two values. == is only used directly on
    primitive types (int, float, str); containers (dict, list, tuple,
    set) are compared element by element / key by key."""
    if type(a) != type(b):
        return False

    if isinstance(a, dict):
        if len(a) != len(b):
            return False
        for key in a:
            if key not in b:
                return False
            if not _deep_equal(a[key], b[key]):
                return False
        return True

    if isinstance(a, (list, tuple)):
        if len(a) != len(b):
            return False
        for item_a, item_b in zip(a, b):
            if not _deep_equal(item_a, item_b):
                return False
        return True

    if isinstance(a, set):
        if len(a) != len(b):
            return False
        for item in a:
            if item not in b:
                return False
        return True

    # primitive type: int, float, str, bool, None...
    return a == b


def compare_dicts(dict1, dict2):
    """Compares two dictionaries (recursively, since values can be
    other containers) without using == / != on anything but primitive
    types. Returns a tuple of lists:
    (keys_common_but_different_values,
     keys_only_in_first_dict,
     keys_only_in_second_dict)."""
    common_but_different = []
    only_in_first = []
    only_in_second = []

    for key in dict1:
        if key in dict2:
            if not _deep_equal(dict1[key], dict2[key]):
                common_but_different.append(key)
        else:
            only_in_first.append(key)

    for key in dict2:
        if key not in dict1:
            only_in_second.append(key)

    return common_but_different, only_in_first, only_in_second


if __name__ == "__main__":
    d1 = {"a": 1, "b": [1, 2, 3], "c": "same", "only1": True}
    d2 = {"a": 1, "b": [1, 2, 4], "c": "same", "only2": True}
    print(compare_dicts(d1, d2))
    # (['b'], ['only1'], ['only2'])
