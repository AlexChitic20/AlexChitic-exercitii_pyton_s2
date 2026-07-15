def filter_by_ascii(*strings, x=1, flag=True):
    """For each string received, builds a list with the characters whose
    ASCII code is divisible by x (if flag is True) or NOT divisible by x
    (if flag is False). Returns a tuple with one list per input string."""
    result = []
    for text in strings:
        if flag:
            chars = [char for char in text if ord(char) % x == 0]
        else:
            chars = [char for char in text if ord(char) % x != 0]
        result.append(chars)
    return tuple(result)


if __name__ == "__main__":
    print(filter_by_ascii("test", "hello", "lab002", x=2, flag=False))
    # (['e', 's'], ['e', 'o'], ['a'])
