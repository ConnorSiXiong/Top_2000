from typing import List

import numpy as np


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        temp = [[float('-inf') for _ in range(len(nums))] for _ in range(len(nums))]
        memo = np.array(temp)
        res = self.winner(nums, 0, len(nums) - 1, memo)

        return res >= 0

    def winner(self, nums, head, tail, memo):
        print(memo)
        if head == tail:
            return nums[head]
        if memo[head][tail] != float('-inf'):
            return memo[head][tail]

        a = nums[head] - self.winner(nums, head + 1, tail, memo)
        b = nums[tail] - self.winner(nums, head, tail - 1, memo)

        memo[head][tail] = max(a, b)
        return memo[head][tail]


#
# a = Solution()
#
# print(a.PredictTheWinner([1, 5, 233, 7]))


class Solution2:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = np.array([[float('-inf') for _ in range(len(nums))] for _ in range(len(nums))])
        res = self.winner(nums, 0, len(nums) - 1, memo) >= 0
        print(memo)
        return res

    def winner(self, nums, left, right, memo):
        # 这里的left, right代表区间
        # 所以memo的是left, right 区间里，player 1 的最大取值
        print(memo)
        if left == right:
            memo[left][right] = nums[left]
            return memo[left][right]

        if memo[left][right] != float('-inf'):
            return memo[left][right]

        left_score = nums[left] - self.winner(nums, left + 1, right, memo)
        right_score = nums[right] - self.winner(nums, left, right - 1, memo)

        memo[left][right] = max(left_score, right_score)
        return memo[left][right]


# a = Solution2()
# print(a.PredictTheWinner([1, 5, 233, 7]))
