def _middle_is_inside(value, middle):
    """Checks that `middle` appears inside `value`, strictly between the
    start and the end (not touching either boundary)."""
    if middle == "":
        return True

    for start in range(len(value) - len(middle) + 1):
        end = start + len(middle)
        if start == 0 or end == len(value):
            continue  # touches a boundary, doesn't count
        if value[start:end] == middle:
            return True
    return False


def validate_dict(rules, data):
    """`rules` is a collection of tuples (key, prefix, middle, suffix).
    A value is valid if it starts with "prefix", contains "middle"
    strictly inside it (not at the start or end), and ends with
    "suffix". Returns True if `data` satisfies every rule AND contains
    no keys other than the ones mentioned in the rules; False otherwise."""
    rules_by_key = {key: (prefix, middle, suffix) for key, prefix, middle, suffix in rules}

    # Any key in data that isn't covered by a rule invalidates everything.
    for key in data:
        if key not in rules_by_key:
            return False

    for key, (prefix, middle, suffix) in rules_by_key.items():
        if key not in data:
            return False
        value = data[key]
        if not value.startswith(prefix):
            return False
        if not value.endswith(suffix):
            return False
        if not _middle_is_inside(value, middle):
            return False

    return True


if __name__ == "__main__":
    rules = [
        ("key1", "", "inside", ""),
        ("key2", "start", "middle", "winter"),
    ]
    data_valid = {
        "key2": "starting the engine in the middle of the winter",
        "key1": "come inside, it's too cold outside",
    }
    data_invalid = {
        "key2": "starting the engine in the middle of the winter",
        "key1": "come inside, it's too cold outside",
        "key3": "this is not valid",
    }
    print(validate_dict(rules, data_valid))    # True
    print(validate_dict(rules, data_invalid))  # False (key3 not in rules)
