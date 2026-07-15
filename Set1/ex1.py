def gcd_two(a, b):
   
    while b:
        a, b = b, a % b
    return a


def gcd_multiple(*numbers):
    
    if not numbers:
        raise ValueError("At least one number is required")

    result = numbers[0]
    for number in numbers[1:]:
        result = gcd_two(result, number)
    return result


if __name__ == "__main__":
    print(gcd_multiple(12, 18, 24))   # 6
    print(gcd_multiple(20, 30))       # 10
    print(gcd_multiple(7))            # 7
