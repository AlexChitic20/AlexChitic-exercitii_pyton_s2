def sort_by_third_char(pairs):
  
    return sorted(pairs, key=lambda pair: pair[1][2])


if __name__ == "__main__":
    print(sort_by_third_char([("abc", "bcd"), ("abc", "zza")]))
    # [('abc', 'zza'), ('abc', 'bcd')]
