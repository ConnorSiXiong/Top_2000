from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    if not nums:
        return []
    res = []
    visited = [0] * len(nums)
    dfs(nums, visited, [], res)
    return res


def dfs(arr, visited, one_set, res):
    if len(one_set) == len(arr):
        res.append(one_set.copy())
        return

    for idx, val in enumerate(arr):
        if visited[idx] == 0:
            visited[idx] = 1
            one_set.append(val)
            dfs(arr, visited, one_set, res)
            one_set.pop()
            visited[idx] = 0


a = [1, 0]
print(permute(a))