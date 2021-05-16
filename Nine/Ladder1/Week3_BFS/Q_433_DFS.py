from typing import List

import numpy as np


def numIslands(grid):
    if not grid:
        return 0
    grid = np.array(grid)
    visited = np.zeros(grid.shape, int)
    rows = grid.shape[0]
    cols = grid.shape[1]

    res = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row, col] == 0 or visited[row, col] == 1:
                continue
            dfs(grid, visited, row, col)
            res += 1
    return res


def dfs(grid, visited, row, col):
    if not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]):
        return
    if visited[row, col] == 1:
        return
    visited[row, col] = 1
    if grid[row, col] == 0:
        return
    """
    一开始是这样写的, 没有if判断
        dfs(grid, visited, row + 1, col)
        dfs(grid, visited, row - 1, col)
        dfs(grid, visited, row, col + 1)
        dfs(grid, visited, row, col - 1)

    这样写的话，会出现死循环，走过的地方会重复走
    比如：
        [
            [1,1,0],
            [1,1,0],
            [0,0,0]
        ]

    """

    dfs(grid, visited, row + 1, col)
    dfs(grid, visited, row - 1, col)
    dfs(grid, visited, row, col + 1)
    dfs(grid, visited, row, col - 1)
    # if 0 <= row + 1 < grid.shape[0] and 0 <= col < grid.shape[1] and visited[row + 1, col] == 0:
    #     dfs(grid, visited, row + 1, col)
    # if 0 <= row < grid.shape[0] and 0 <= col + 1 < grid.shape[1] and visited[row, col + 1] == 0:
    #     dfs(grid, visited, row, col + 1)
    # if 0 <= row < grid.shape[0] and 0 <= col - 1 < grid.shape[1] and visited[row, col - 1] == 0:
    #     dfs(grid, visited, row, col - 1)
    # if 0 <= row - 1 < grid.shape[0] and 0 <= col < grid.shape[1] and visited[row - 1, col] == 0:
    #     dfs(grid, visited, row - 1, col)


#
# def dfs(grid, visited, row, col):
#     if not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]):
#         print('?')
#         return
#
#     visited[row, col] = random.randint(0, 100)
#
#     print(visited)
#     if grid[row, col] == 0:
#         print('??')
#         return
#     """
#     一开始是这样写的, 没有if判断
#         dfs(grid, visited, row + 1, col)
#         dfs(grid, visited, row - 1, col)
#         dfs(grid, visited, row, col + 1)
#         dfs(grid, visited, row, col - 1)
#
#     这样写的话，会出现死循环，走过的地方会重复走
#     在这个矩阵里
#     [
#         [1, 1, 0, 0, 0],
#         [0, 1, 0, 0, 1],
#         [0, 0, 0, 1, 1],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1]
#     ]
#
#     最后程序会在 [2,1] 和 [3,1] 两个位置不断来回调用
#         dfs(grid, visited, row + 1, col)
#         dfs(grid, visited, row - 1, col)
#
#     """
#
#     dfs(grid, visited, row + 1, col)
#     dfs(grid, visited, row - 1, col)
#     dfs(grid, visited, row, col + 1)
#     dfs(grid, visited, row, col - 1)


a = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1]
]

a1 = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]
print(numIslands(a1))


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        grid = np.array(grid)
        visited = np.zeros(grid.shape, int)
        rows = grid.shape[0]
        cols = grid.shape[1]

        res = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row, col] == "0" or visited[row, col] == 1:
                    continue
                self.dfs(grid, visited, row, col)
                res += 1
        return res

    def dfs(self, grid, visited, row, col):
        if not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]):
            return

        if visited[row, col] == 1:
            return
        visited[row, col] = 1

        if grid[row, col] == "0":
            return

        self.dfs(grid, visited, row + 1, col)
        self.dfs(grid, visited, row - 1, col)
        self.dfs(grid, visited, row, col + 1)
        self.dfs(grid, visited, row, col - 1)


bb = Solution()
a1 = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
print(bb.numIslands(a1))
#
# def numIslands2(grid):
#     grid = np.array(grid)
#     rows = grid.shape[0]
#     cols = grid.shape[1]
#     visited = np.zeros(grid.shape, int)
#
#     res = 0
#     for row in range(rows):
#         for col in range(cols):
#             if isLand(grid, visited, row, col):
#                 visited[row, col] = 1
#                 print(visited)
#                 dfs(grid, visited, row, col)
#                 res += 1
#     return res
#
#
# def isLand(grid, visited, row, col):
#     # 1。
#     if not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]):
#         return False
#
#     # 2。
#     if grid[row, col] == 0:
#         return False
#     """
#     # print(visited)
#     # print('row', row)
#     # print('col', col)
#     # print(not visited[row, col])
#     # print('----------')
#
#     为什么最后是return not visited[row, col]
#     前面的两种情况可以确定一定不是island
#     分别是
#     1。出界了
#     2。不是岛
#     那么
#     这个位置grid[row, col]一定等于1
#
#     如果它之前visited，那么就不用再次访问了
#     如果它没有visited，那么就在这一次访问
#     """
#     return not visited[row, col]
#
#
# def dfs(grid, visited, x, y):
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#     for direction in range(4):
#         newx = x + dx[direction]
#         newy = y + dy[direction]
#
#         if isLand(grid, visited, newx, newy):
#             visited[newx][newy] = True
#             dfs(grid, visited, newx, newy)


#
#
# def numIslands( grid):
#     if not grid or not grid[0]:
#         return 0
#
#     n, m = len(grid), len(grid[0])
#     visited = [[False] * m for _ in range(n)]
#
#     islands = 0
#     for row in range(n):
#         for col in range(m):
#             if is_island(grid, row, col, visited):
#                 visited[row][col] = True
#                 dfs(grid, row, col, visited)
#                 islands += 1
#
#     return islands
#
#
# def is_island(grid, x, y, visited):
#     n, m = len(grid), len(grid[0])
#     if not (0 <= x < n and 0 <= y < m):
#         return False
#     if not grid[x][y]:
#         return False
#     return not visited[x][y]
#
#
# def dfs(grid, x, y, visited):
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#     for direction in range(4):
#         newx = x + dx[direction]
#         newy = y + dy[direction]
#
#         if is_island(grid, newx, newy, visited):
#             visited[newx][newy] = True
#             dfs(grid, newx, newy, visited)
