import re


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def largest_prime_in_string(text):
   
    numbers = [int(match) for match in re.findall(r"\d+", text)]
    primes = [number for number in numbers if is_prime(number)]
    return max(primes) if primes else -1


if __name__ == "__main__":
    print(largest_prime_in_string("ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda"))  # 271
    print(largest_prime_in_string("no digits here"))            # -1
