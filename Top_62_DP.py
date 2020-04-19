def uniquePaths(m: int, n: int) -> int:
    matrix = [[1] * col for _ in range(row)]
    for i in range(1, row):
        for j in range(1, col):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    return matrix[row - 1][col - 1]


col = 3
row = 3
matrix = [[1] * col for _ in range(row)]
print(matrix)

print(uniquePaths(3,3))