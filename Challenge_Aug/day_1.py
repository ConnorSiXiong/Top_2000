"""
Leetcode 827
这个题目的思路反过来了，从0开始找
DFS

暂时还不知道能不能用DP做

Author: Alex
Date: 02/08/2021 - NZ Auckland
      4:41 am -
"""
import numpy as np
from collections import deque

D = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]


def isLegal(grid, x, y):
    rows = grid.shape[0]
    cols = grid.shape[1]

    if not (0 <= x < rows and 0 <= y < cols):
        return False
    return True


class Solution:
    def largestIsland(self, grid):
        if not grid:
            return 0
        grid = np.array(grid)
        if np.all(grid):
            return np.sum(grid)
        rows = grid.shape[0]
        cols = grid.shape[1]

        visited1 = []

        islands_dict = {}
        islands_dict2 = {}
        island_id = 1
        for i in range(0, rows):
            for j in range(0, cols):
                visited2 = []
                if isLegal(grid, i, j) and grid[i][j] == 1 and (i, j) not in visited1:
                    visited2.append((i, j))
                    island_area = self.getArea(grid, i, j, visited2)
                    self.write_into_dict(visited2, island_area, islands_dict, islands_dict2, island_id)
                    island_id += 1
                    visited1 += visited2

        max_island = 0

        for i in range(0, rows):
            for j in range(0, cols):
                if isLegal(grid, i, j) and grid[i][j] == 0:
                    max_island = max(max_island, self.count_area_in_dict(grid, i, j, islands_dict, islands_dict2))

        return max_island


    def getArea(self, grid, x, y, visited_box):
        area = 1
        q = deque([])
        visited = [(x, y)]
        q.append((x, y))
        while q:
            cur = q.popleft()
            (x, y) = cur
            for dx, dy in D:
                next_x = x + dx
                next_y = y + dy
                if isLegal(grid, next_x, next_y) and grid[next_x][next_y] == 1 and (next_x, next_y) not in visited:
                    visited.append((next_x, next_y))
                    q.append((next_x, next_y))
                    area += 1
                    visited_box.append((next_x, next_y))
        return area

    def write_into_dict(self, arr, cur_area, island_dict, island_dict2, island_id):
        for i in arr:
            island_dict[i] = cur_area
            island_dict2[i] = island_id

    def count_area_in_dict(self, grid, x, y, island_area_dict, island_id_dict):
        area = 1
        counted_island = []

        for dx, dy in D:
            next_x = x + dx
            next_y = y + dy
            if isLegal(grid, next_x, next_y) and grid[next_x][next_y] == 1 and island_id_dict[(next_x, next_y)] not in counted_island:
                area += island_area_dict[(next_x, next_y)]
                counted_island.append(island_id_dict[(next_x, next_y)])

        return area


test_arr = [
    [1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1]
]

# test_arr = [
#     [1, 1],
#     [1, 1
# ]

a = Solution()
print(a.largestIsland(test_arr))
# print(a.getArea(test_arr, 2,2))

print(np.all(np.array([1,1,0])))