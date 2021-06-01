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
            print('cur_arr', cur_arr)
            dfs(start + 1, cur_arr)
            cur_arr.pop()
            """
            假设 nums = [1,2]
            
            
            说一下这个pop是怎么用的
            
            当i = 0 时，cur_arr放进去了一个1
            然后就进入dfs了
            然后这个cur_arr刚刚放进去的1要拿出来，因为下一轮给2用，这样cur_arr就只有一个2了
            
            
            """

    dfs(0, [])

    return result


nums = [1, 2, 3]


# print(subsets(nums))


def subsets2(nums):
    if not nums:
        return [[]]

    visited = set([])
    res = []
    dfs(nums, [], visited, res)
    print(res)
    return res


def dfs(nums, one_set, visited, res):
    one_set = sorted(one_set)
    if one_set not in res:
        res.append(one_set.copy())

    if len(visited) == len(nums):
        return

    for i in nums:
        if i in visited:
            continue
        visited.add(i)
        one_set.append(i)
        dfs(nums, one_set, visited, res)
        visited.remove(i)
        one_set.pop()


print(subsets2([1, 2, 3]))


def subsets3(arr):
    arr = sorted(arr)

    res = []
    dfs3(arr, 0, [], res)
    return res


def dfs3(arr, index, one_set, res):
    res.append(one_set[:])
    for i in range(index, len(arr)):
        one_set.append(arr[i])
        dfs3(arr, i + 1, one_set, res)
        one_set.pop()


print(subsets3([1, 2, 3]))
