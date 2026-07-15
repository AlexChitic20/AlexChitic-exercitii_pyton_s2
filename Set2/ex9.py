def sort_by_third_char(pairs):
    """Sorts a list of tuples of strings by the 3rd character of the
    2nd element of each tuple."""
    return sorted(pairs, key=lambda pair: pair[1][2])


if __name__ == "__main__":
    print(sort_by_third_char([("abc", "bcd"), ("abc", "zza")]))
    # [('abc', 'zza'), ('abc', 'bcd')]
