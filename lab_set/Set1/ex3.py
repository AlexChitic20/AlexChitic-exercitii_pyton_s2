import re


def count_words(text):
    """Returns the number of words in a string. Words are separated by
    spaces and/or punctuation (, ; ? ! .), possibly combined in any way
    between two words."""
    # Split on one-or-more separators (space or punctuation) in a row.
    tokens = re.split(r"[ ,;?!.]+", text)
    words = [token for token in tokens if token != ""]
    return len(words)


if __name__ == "__main__":
    print(count_words("Hello, world!"))              # 2
    print(count_words("One,  two ; three... four!")) # 4
    print(count_words("  ..,, "))                      # 0
