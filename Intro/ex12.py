def largest_first_half_smallest_second_half(numbers):
    
    middle = len(numbers) // 2
    first_half = numbers[:middle]
    second_half = numbers[middle:]

    return max(first_half), min(second_half)


if __name__ == "__main__":
    result = largest_first_half_smallest_second_half([5, 2, 8, 1, 9, 3])
    print(result)  # (8, 1)
