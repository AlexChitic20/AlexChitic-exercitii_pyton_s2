def highest(a, b, c):
    """Returns the highest of 3 numbers, without using max()."""
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result


if __name__ == "__main__":
    print(highest(3, 9, 5))   # 9
    print(highest(-1, -2, -3))  # -1
