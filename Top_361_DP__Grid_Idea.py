from typing import List
import pprint

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        res = [[0] * cols for _ in range(rows)]
        dp = [[0] * cols for _ in range(rows)]

        # kill up
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'W':
                    dp[i][j] = 0
                else:
                    if grid[i][j] == 'E':
                        dp[i][j] = 1
                    if i != 0:
                        dp[i][j] += dp[i-1][j]
                res[i][j] += dp[i][j]
        print(res)
        # kill down
        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows-1, -1, -1):

            for j in range(cols):
                if grid[i][j] == 'W':
                    dp[i][j] = 0
                else:
                    if grid[i][j] == 'E':
                        dp[i][j] = 1
                    if i+1 < rows:
                        dp[i][j] += dp[i+1][j]
                res[i][j] += dp[i][j]
        print(res)
        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'W':
                    dp[i][j] = 0
                else:
                    if grid[i][j] == 'E':
                        dp[i][j] = 1
                    if j-1 >= 0:
                        dp[i][j] += dp[i][j-1]
                res[i][j] += dp[i][j]
        print(res)
        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols-1,-1,-1):
                if grid[i][j] == 'W':
                    dp[i][j] = 0
                else:
                    if grid[i][j] == 'E':
                        dp[i][j] = 1
                    if j+1 < cols:
                        dp[i][j] += dp[i][j + 1]
                res[i][j] += dp[i][j]
        print(res)
        result = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0":
                    if res[i][j] > result:
                        result = res[i][j]
        return result


grid = [["0", "E", "0", "0"],
        ["E", "0", "W", "E"],
        ["0", "E", "0", "0"]]
a = Solution()
print(a.maxKilledEnemies(grid))
