def char_frequencies(text):
    """Returns a dictionary where the keys are the characters found in
    `text` and the values are how many times each character occurs."""
    frequencies = {}
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies


if __name__ == "__main__":
    print(char_frequencies("Ana are mere."))
    # {'A': 1, 'n': 1, 'a': 2, ' ': 2, 'r': 2, 'e': 3, 'm': 1, '.': 1}
