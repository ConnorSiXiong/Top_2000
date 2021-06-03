import numpy as np


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

print(uniquePaths(3, 3))


def uniquePaths2(m, n):
    if m == 1 or n == 1:
        return 1
    dp = np.zeros((m, n), int)

    dp[m - 1, :] = 1
    dp[: n - 1] = 1
    dp[-1, -1] = 0
    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            dp[i][j] = dp[i+1][j] + dp[i][j+1]
    return dp[0][0]
