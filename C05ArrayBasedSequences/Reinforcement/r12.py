def matrix_sum(matrix):
    return sum(sum(row) for row in matrix)


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(matrix_sum(matrix))
