import random

"""
    整个程序记录了每一层dfs的进入和退出
    帮助理解整个流程
"""


def subsets(arr):
    if not arr or len(arr) == 0:
        return [[]]
    arr = sorted(arr)
    res = []
    dfs(arr, 0, [], res)
    return res


def dfs(arr, index, subset, res):
    random_label = random.randint(0, 100)
    if index != len(arr):
        print('--------In', random_label, '--------')
        print('index', index)
    else:
        print('+++++++++Output+++++++')

    if index == len(arr):
        print('to be add', subset)
        print('+++++++++Output+++++++')
        res.append(list(subset))
        return

    subset.append(arr[index])
    print('subset', subset)
    dfs(arr, index + 1, subset, res)

    print('------ Out', random_label, '--------')
    subset.pop()

    print('subset after pop', subset)
    print('index', index)
    dfs(arr, index + 1, subset, res)


print(subsets([1, 2, 3]))
