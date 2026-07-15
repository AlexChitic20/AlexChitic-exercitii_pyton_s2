def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def primes_in_list(numbers):
    """Returns a list with the prime numbers found in `numbers`."""
    return [number for number in numbers if is_prime(number)]


if __name__ == "__main__":
    print(primes_in_list([4, 7, 9, 11, 15, 17, 20]))  # [7, 11, 17]
