def check_word_chain(char_len, *words):
    
    for first, second in zip(words, words[1:]):
        ending = first[-char_len:]
        if not second.startswith(ending):
            return False
    return True


if __name__ == "__main__":
    print(check_word_chain(3, "pheasant", "antelope", "opeland"))  # True
    print(check_word_chain(3, "pheasant", "elephant"))             # False
