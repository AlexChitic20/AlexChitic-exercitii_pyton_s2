def is_palindrome(number):

    text = str(number)
    return text == text[::-1]


if __name__ == "__main__":
    print(is_palindrome(12321))  # True
    print(is_palindrome(12345))  # False
