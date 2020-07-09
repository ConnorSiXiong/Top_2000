from typing import List


def islandPerimeter(grid: List[List[int]]) -> int:
    result = 0

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):

            if grid[i][j] == 1:
                print('i',i,'j',j)
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
