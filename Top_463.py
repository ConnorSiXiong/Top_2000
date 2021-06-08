from typing import List
import numpy as np
from collections import deque


def islandPerimeter(grid: List[List[int]]) -> int:
    result = 0

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):

            if grid[i][j] == 1:
                # print('i', i, 'j', j)
                result += 4
                if i - 1 >= 0:
                    if grid[i - 1][j] == 1:
                        result -= 1
                if i + 1 < rows:
                    if grid[i + 1][j] == 1:
                        result -= 1
                if j - 1 >= 0:
                    if grid[i][j - 1] == 1:
                        result -= 1
                if j + 1 < cols:
                    if grid[i][j + 1] == 1:
                        result -= 1
    return result


a = [[1, 1, 1, 1]]

print(islandPerimeter(a))

DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def islandPerimeter2(grid: List[List[int]]) -> int:
    # 这种做法出不来，因为没考虑多相邻小正方形
    # 比如：[[1, 1], [1, 1]] 就没法处理
    # 接下来用数学方法做

    # 反思：
    # 这个BFS方法没通过
    # 在打草稿的时候没有分情况把岛屿的分布情况考虑清楚，
    # 漏掉了上面那种几个岛屿挤在一起的情况

    # 题目已经保证了有岛屿
    grid = np.array(grid)
    rows = grid.shape[0]
    cols = grid.shape[1]
    res = 4
    visited = set()
    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 0:
                continue
            q = deque([])
            q.append((i, j))
            visited.add((i, j))
            while q:
                x, y = q.popleft()
                for dx, dy in DIRECTIONS:
                    x2 = x + dx
                    y2 = y + dy
                    if isValid(grid, x2, y2, visited):
                        q.append((x2, y2))
                        visited.add((x2, y2))
                        res += 2
            return res


def isValid(grid, x, y, visited):
    rows = grid.shape[0]
    cols = grid.shape[1]

    if not (0 <= x < rows and 0 <= y < cols):
        return False
    if (x, y) in visited:
        return False
    if grid[x, y] == 0:
        return False
    return True


def islandPerimeter3(grid: List[List[int]]) -> int:
    # 用数学方法做就是
    # n * 4 - n_black * 2
    # 小正方形个数 * 4 - 共享黑边个数 * 2
    return 0

print(4 - 1 - 1 + 3 - 1 + 3 - 1 + 3 - 1 + 3 - 1 + 3)

print(4 - 2 + 4 - 2 + 4 - 2 + 4 - 2 + 4 - 2 + 4 - 2 + 4)
print(4 - 2 + 4 - 2 + 4)

b = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
c = [[1]]
d = [[1, 1], [1, 1]]
print(islandPerimeter2(b))
print(islandPerimeter2(c))

print(islandPerimeter(d))
print(islandPerimeter2(d))
print('------R')
print(4 - 2 + 4 - 2 + 4)
print(4 - 2 + 4 - 2 + 4 - 2 - 2 + 4)

print(4 * 7 - 2 * 6)
print(4 * 1)
print(4*4 - 4 * 2)