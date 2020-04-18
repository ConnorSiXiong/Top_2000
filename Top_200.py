from typing import List


def numIslands(grid: List[List[str]]) -> int:

    if len(grid) == 0 or grid is None:
        return 0

    def dfs(grid: List[List[str]], i: int, j: int):
        if (
            # grid[i][j] == '0' or
            # 上面这一句不能放在这里，可能有range out of index error
            i < 0 or
            j < 0 or
            i == rows or
            j == cols or
            grid[i][j] == '0'
        ): return

        grid[i][j] = '0'

        # 顺时针 - 上右下左
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i + 1, j)
        dfs(grid, i, j - 1)

    count = 0

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                dfs(grid, i, j)

    return count

