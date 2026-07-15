def filter_by_ascii(*strings, x=1, flag=True):
    
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
