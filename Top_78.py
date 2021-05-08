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


def bfs(arr):
    if not arr:
        return [[]]
    res = []
    # deque的初始化按下面这样写，
    # 如果初始化写成q = collections.deque([[[], 0]]) 会 confusing
    q = collections.deque([])
    q.append([[], 0])

    while q:
        subset, index = q.popleft()
        res.append(subset)
        for i in range(index, len(arr)):
            q.append([subset + [arr[i]], i + 1])  # 注意这个地方往下一层是i+1，不是index+1，写错了
    return res


"""
another bfs
https://leetcode.com/problems/subsets/discuss/277064/bfs-to-generate-subset
"""

# print(subsets([1, 2, 3]))
print(bfs([1, 2, 3]))
print(subsets2([1, 2, 3]))
