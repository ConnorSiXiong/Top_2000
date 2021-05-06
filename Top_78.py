import random


def subsets(arr):
    if not arr or len(arr) == 0:
        return [[]]
    arr = sorted(arr)
    res = []
    dfs(arr, 0, [], res)
    return res


def dfs(arr, index, subset, res):
    if index == len(arr):
        res.append(list(subset))
        return

    subset.append(arr[index])
    dfs(arr, index + 1, subset, res)
    subset.pop()
    dfs(arr, index + 1, subset, res)


print(subsets([1, 2, 3]))
