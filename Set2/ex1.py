def fibonacci(n):
    """Returns a list with the first n numbers of the Fibonacci sequence."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def generalized_fibonacci(num_terms, n):
    """1* (bonus): generalized Fibonacci-like sequence where each term is
    the sum of the last `n` terms. The sequence starts with (n-1) zeros
    followed by a 1 (e.g. n=5 -> starting sequence: 0 0 0 0 1).
    Returns the first `num_terms` terms."""
    sequence = [0] * (n - 1) + [1]

    while len(sequence) < num_terms:
        next_term = sum(sequence[-n:])
        sequence.append(next_term)

    return sequence[:num_terms]


if __name__ == "__main__":
    print(fibonacci(8))                    # [0, 1, 1, 2, 3, 5, 8, 13]
    print(generalized_fibonacci(10, 5))     # starts 0 0 0 0 1 1 2 4 8 16
