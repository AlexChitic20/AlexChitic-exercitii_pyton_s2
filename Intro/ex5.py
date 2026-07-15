def count_digits_of_power(base, exponent):
    number = base ** exponent
    return len(str(number))


if __name__ == "__main__":
    digits = count_digits_of_power(2, 1024)
    print(f"2^1024 has {digits} digits")
