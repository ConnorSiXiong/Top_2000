import collections
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


def subsets2(nums):
    nums = sorted(nums)
    res = []
    q = [([], 0)]
    print(q)
    while q:

        arr, n = q.pop(0)
        print("arr and n:", arr, n)
        res.append(arr)

        for i in range(n, len(nums)):
            q.append((arr + [nums[i]], i + 1))

    return res


def dfs2(arr, index, subset, res):
    res.append(list(subset))

    for i in range(index, len(arr)):
        subset.append(arr[i])
        dfs2(arr, index + 1, subset, res)
        subset.pop()


print(subsets([1, 2, 3]))
