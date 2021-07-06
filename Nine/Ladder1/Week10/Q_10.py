from typing import List
import pprint

a = "abb"


# 123
# 132
# 213
# 231
# 312
# 321


def permute(nums: List[int]) -> List[List[int]]:
    if not nums:
        return []

    res = []
    visited = [0] * len(nums)
    dfs(nums, visited, [], res)
    print(res)
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


# permute([1, 2, 3])


def p2(arr):
    res = []
    visited = [0] * len(arr)
    dfs(arr, visited, [], res)
    print(res)
    return res


def dfs(arr, visited, comb, res):
    if len(visited) == len(comb):
        res.append(comb[:])
        return

    for idx, val in enumerate(arr):
        if visited[idx] == 0:
            visited[idx] = 1
            comb.append(arr[idx])
            dfs(arr, visited, comb, res)
            comb.pop()
            visited[idx] = 0


# p2([1, 2, 3])


def p3(arr):
    visited1 = [0] * len(arr)
    visited2 = {}
    res = []

    dfs3(arr, visited1, visited2, [], res)
    print(res)
    return res


def hashSubset(one_comb):
    return '-'.join(one_comb)


def dfs3(arr, visited1, visited2, comb, res):
    if len(comb) == len(visited1):
        cur_comb = hashSubset(comb)
        if cur_comb in visited2:
            return
        visited2[cur_comb] = 1
        res.append(comb[:])
        return

    for idx, val in enumerate(arr):
        if visited1[idx] == 1:
            continue

        if idx > 0 and arr[idx] == arr[idx - 1] and visited1[idx - 1] == 1:
            continue
        visited1[idx] = 1
        comb.append(val)
        dfs3(arr, visited1, visited2, comb, res)
        comb.pop()
        visited1[idx] = 0


# p3(['a', 'a', 'b'])



def p4(word):
    res = []
    comb = ''
    visited = set()

    word = sorted(word)
    dfs4(word, comb, visited, res)
    print(res)
    return res

from time import sleep

def dfs4(s, comb, visited, res):
    print('comb', comb)
    if len(comb) == len(s):
        res.append(comb)
        return
    for i in range(len(s)):
        print(visited)
        print('i', i)

        if i in visited:
            print('visited before')
            continue
        if i > 0 and i - 1 not in visited and s[i] == s[i - 1]:
            print(comb)
            print(visited)
            print('skip')
            continue
        visited.add(i)
        print(visited)
        print('-----------')
        dfs4(s, comb+s[i], visited, res)
        visited.remove(i)

p4("aaab")