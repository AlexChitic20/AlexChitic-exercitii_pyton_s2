def count_occurrences(needle, haystack):
    """Returns the number of (non-overlapping) occurrences of `needle`
    inside `haystack`."""
    return haystack.count(needle)


if __name__ == "__main__":
    print(count_occurrences("ab", "ababab"))  # 3
    print(count_occurrences("xyz", "hello"))  # 0
