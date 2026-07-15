def fibonacci(n):
   
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def generalized_fibonacci(num_terms, n):
    
    sequence = [0] * (n - 1) + [1]

    while len(sequence) < num_terms:
        next_term = sum(sequence[-n:])
        sequence.append(next_term)

    return sequence[:num_terms]


if __name__ == "__main__":
    print(fibonacci(8))                    # [0, 1, 1, 2, 3, 5, 8, 13]
    print(generalized_fibonacci(10, 5))     # starts 0 0 0 0 1 1 2 4 8 16
