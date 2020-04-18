from typing import List


def minPathSum(grid: List[List[int]]) -> int:
    row = len(grid)
    col = len(grid[0])

    for i in range(1, row):
        grid[i][0] += grid[i-1][0]

    for i in range(1, col):
        grid[0][i] += grid[0][i-1]

    for i in range(1, row):
        for j in range(1, col):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[-1][-1]


a = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

print(minPathSum(a))