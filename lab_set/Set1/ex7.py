def check_word_chain(char_len, *words):
    """Checks that every two neighboring strings follow the word-chain
    rule: the second string starts with the last `char_len` characters
    of the first one (like the word game, e.g. "pheasant" -> "antelope").
    Returns True if the whole chain is valid, False otherwise."""
    for first, second in zip(words, words[1:]):
        ending = first[-char_len:]
        if not second.startswith(ending):
            return False
    return True


if __name__ == "__main__":
    print(check_word_chain(3, "pheasant", "antelope", "opeland"))  # True
    print(check_word_chain(3, "pheasant", "elephant"))             # False
