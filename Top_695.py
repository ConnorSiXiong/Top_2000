from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    result = 0
    rows = len(grid)
    cols = len(grid[0])

    def dfs(grid, i, j):
        if i < 0 or j < 0 or i == rows or j == cols or grid[i][j] == 0:
            return 0

        grid[i][j] = 0
        return 1 + dfs(grid, i + 1, j) + dfs(grid, i - 1, j) + dfs(grid, i, j + 1) + dfs(grid, i, j - 1)

    for i in range(rows):
        for j in range(cols):
            result = max(result, dfs(grid, i, j))

    return result


def maxAreaOfIsland2(grid: List[List[int]]) -> int:
    result = 0
    rows = len(grid)
    cols = len(grid[0])

    def dfs(i, j):
        if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1:
            grid[i][j] = 0
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
        return 0

    for i in range(rows):
        for j in range(cols):
            result = max(result, dfs(i, j))

    return result

