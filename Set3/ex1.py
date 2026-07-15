def set_operations(a, b):
   
    set_a, set_b = set(a), set(b)
    return (set_a & set_b, set_a | set_b, set_a - set_b, set_b - set_a)


if __name__ == "__main__":
    print(set_operations([1, 2, 3, 4], [3, 4, 5, 6]))
    # ({3, 4}, {1, 2, 3, 4, 5, 6}, {1, 2}, {5, 6})
