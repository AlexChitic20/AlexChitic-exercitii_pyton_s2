from collections import Counter


def unique_and_duplicate_counts(collection):
  
    counts = Counter(collection)
    unique_count = len(counts)
    duplicate_count = sum(count - 1 for count in counts.values() if count > 1)
    return unique_count, duplicate_count


if __name__ == "__main__":
    print(unique_and_duplicate_counts([1, 1, 2, 3, 3, 3]))  # (3, 3)
    print(unique_and_duplicate_counts({1, 2, 3}))            # (3, 0)
