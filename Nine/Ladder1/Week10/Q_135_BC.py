candidates = [2, 3, 6, 7]
# candidates = [7]
target = 7


def combinationSum(candidates, target):
    candidates = set(candidates)
    candidates = sorted(list(candidates))
    res = []
    visited = {}
    dfs(candidates, 0, target, [], res, visited)
    print(res)
    return res

def hashComb(arr):
    return '-'.join([str(x) for x in arr])

def dfs(candidates, index, target, comb, res, visited):
    print(comb)
    if sum(comb) > target:
        return
    if sum(comb) == target:

        comb = sorted(comb)

        if hashComb(comb) not in visited:
            visited[hashComb(comb)] = 1
            res.append(comb[:])
            return
        else:
            return

    for i in range(index, len(candidates)):
        comb.append(candidates[i])
        dfs(candidates, index, target, comb, res, visited)
        # dfs(candidates, index+1, target, comb, res)
        comb.pop()

combinationSum(candidates, target)
print('--------')

"""
非常好的back tracing的例子
"""
def combinationSum2(candidates, target):

    res = []
    dfs2(candidates, target, 0, [], res)
    print(res)
    return res


def dfs2(candidates, remain, start, comb, res):
    print(comb)
    if remain < 0:
        return
    if remain == 0:
        res.append(comb[:])
        return

    for i in range(start, len(candidates)):
        comb.append(candidates[i])
        dfs2(candidates, remain-candidates[i], i, comb, res)
        comb.pop()



combinationSum2(candidates, target)

