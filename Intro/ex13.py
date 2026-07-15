def is_palindrome(number):
    """Checks whether a number reads the same forwards and backwards."""
    text = str(number)
    return text == text[::-1]


def has_even_number_of_digits(number):
    """Checks whether a number has an even number of digits."""
    return len(str(number)) % 2 == 0


def palindromes_with_even_digits(numbers):
    """Returns a new list containing only the palindromes from `numbers`
    that have an even number of digits."""
    result = []
    for number in numbers:
        if is_palindrome(number) and has_even_number_of_digits(number):
            result.append(number)
    return result


if __name__ == "__main__":
    print(palindromes_with_even_digits([121, 1221, 3, 44, 555, 6996]))
    # [1221, 44, 6996]
