def sublist_between_extremes(numbers):
  
    smallest_pos = numbers.index(min(numbers))
    largest_pos = numbers.index(max(numbers))

    start = min(smallest_pos, largest_pos)
    end = max(smallest_pos, largest_pos)

    return numbers[start:end + 1]


if __name__ == "__main__":
    print(sublist_between_extremes([4, 7, 1, 9, 2, 8]))
    # smallest (1) at index 2, largest (9) at index 3 -> [1, 9]

    print(sublist_between_extremes([9, 3, 6, 1, 5]))
    # largest (9) at index 0, smallest (1) at index 3 -> [9, 3, 6, 1]
