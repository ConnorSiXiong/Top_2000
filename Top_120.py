from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = []
        self.dfs(triangle, 0, 0, 0, res)
        return min(res)

    def dfs(self, arr, x, y, cur_sum, res):
        if len(arr) == x:
            res.append(cur_sum)
            return

        cur_sum += arr[x][y]
        self.dfs(arr, x + 1, y, cur_sum, res)
        self.dfs(arr, x + 1, y + 1, cur_sum, res)


a = Solution()
triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(a.minimumTotal(triangle))
