from typing import List


# 这个题不能和62题一样直接写入row和col为0的初始值
# 因为在边界上可能有障碍


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        mat = [[0] * cols for _ in range(rows)]

        mat[0][0] = 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    continue
                if row == 0 and col == 0:
                    continue
                # 初始化 row = 0 和 col = 0卡了一下
                # 当row = 0 时，移动col
                # 当col = 0 时，移动row
                # 一开始没写对
                if row == 0:
                    mat[row][col] += mat[row][col - 1]
                elif col == 0:
                    mat[row][col] += mat[row - 1][col]
                else:
                    mat[row][col] = mat[row - 1][col] + mat[row][col - 1]

        return mat[-1][-1]

"""
测试集
[[0,1]]
[[0,0],[1,1],[0,0]]
[[1,0]]
[[0,0,0],[0,1,0],[0,0,0]]

"""