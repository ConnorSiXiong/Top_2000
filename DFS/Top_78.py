import copy
from typing import List


# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         self.nums = list(set(nums))
#         output = self.backtracking([], 0, [])
#         return output
#
#
#     def backtracking(self, output, start, tmp):
#         output.append(list(tmp))
#         print('output', output)
#         for i in range(start, len(self.nums)):
#             tmp.append(self.nums[i])
#             self.backtracking(output, i + 1, tmp)
#             tmp.pop()
#         return output


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def dfs(start, cur_arr):
        nonlocal result

        to_be_add = copy.deepcopy(cur_arr)
        list.sort(to_be_add)

        if to_be_add not in result:
            result.append(to_be_add)

        for i in range(start, len(nums)):
            if nums[i] in cur_arr:
                continue
            cur_arr.append(nums[i])
            dfs(start + 1, cur_arr)
            cur_arr.pop()

    dfs(0, [])

    return result



print(subsets(nums))
