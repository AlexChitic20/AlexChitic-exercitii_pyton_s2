def is_prime(number):
    """Checks whether a number is prime."""
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


if __name__ == "__main__":
    print(is_prime(7))    # True
    print(is_prime(9))    # False
