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


print(subsets([1, 2, 3]))


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


print(subsets2([1, 2, 3]))
