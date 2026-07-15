def mean_and_geomean_of_extremes(numbers):
    
    elements of the list."""
    smallest = min(numbers)
    largest = max(numbers)

    mean = (smallest + largest) / 2
    geometric_mean = (smallest * largest) ** 0.5

    return mean, geometric_mean


if __name__ == "__main__":
    mean, geomean = mean_and_geomean_of_extremes([4, 1, 9, 3])
    print(f"mean={mean}, geometric mean={geomean}")
