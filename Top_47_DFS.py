def permuteUnique(arr):
    if not arr:
        return [[]]
    visited1 = [0] * len(arr)
    visited2 = {}
    res = []
    dfs(arr, visited1, visited2, [], res)
    return res


def hashSubset(one_set):
    return '-'.join([str(i) for i in one_set])


def dfs(arr, visited1, visited2, subset, res):
    if len(subset) == len(arr):
        print(subset)
        hash_subset = hashSubset(subset)

        if hash_subset in visited2:
            return

        visited2[hash_subset] = True
        res.append(list(subset))
        return

    for idx, val in enumerate(arr):
        if visited1[idx] == 0:
            # 刚才这个地方判断条件错了
            # 就一直都进不去

            # 用过了这个idx的才跳过
            # 刚才写成没用过就continue了，所以全部数据都没执行
            continue

        visited1[idx] = 1
        subset.append(val)
        dfs(arr, visited1, visited2, subset, res)
        subset.pop()
        visited1[idx] = 0
