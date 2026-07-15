from collections import Counter


def unique_and_duplicate_counts(collection):
    """Receives a collection of elements and returns a tuple (a, b)
    where a is the number of unique (distinct) elements and b is the
    number of duplicate elements (i.e. the extra occurrences beyond
    the first one for each repeated element).
    Note: a real Python `set` can never contain duplicates (b will
    always be 0 for one) - this works on any iterable, including
    lists, where repeated elements can actually occur."""
    counts = Counter(collection)
    unique_count = len(counts)
    duplicate_count = sum(count - 1 for count in counts.values() if count > 1)
    return unique_count, duplicate_count


if __name__ == "__main__":
    print(unique_and_duplicate_counts([1, 1, 2, 3, 3, 3]))  # (3, 3)
    print(unique_and_duplicate_counts({1, 2, 3}))            # (3, 0)
