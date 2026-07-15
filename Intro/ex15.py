def sorted_main_diagonal_descending(matrix):
    """Takes a square matrix (list of lists) and returns the elements of
    the main diagonal, sorted in descending order."""
    diagonal = [matrix[i][i] for i in range(len(matrix))]
    diagonal.sort(reverse=True)
    return diagonal


if __name__ == "__main__":
    matrix = [
        [5, 1, 2],
        [3, 9, 4],
        [7, 8, 1],
    ]
    print(sorted_main_diagonal_descending(matrix))  # [9, 5, 1]
