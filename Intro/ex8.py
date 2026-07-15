def is_palindrome(number):
    """Checks whether a number reads the same forwards and backwards."""
    text = str(number)
    return text == text[::-1]


if __name__ == "__main__":
    print(is_palindrome(12321))  # True
    print(is_palindrome(12345))  # False
