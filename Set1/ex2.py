def count_vowels(text):
    """Returns how many vowels (a, e, i, o, u - case insensitive)
    are in the given string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


if __name__ == "__main__":
    print(count_vowels("Hello World"))  # 3
    print(count_vowels("Python"))       # 1
