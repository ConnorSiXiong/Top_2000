import copy
from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()

    if candidates[0] > target:
        return res

    def dfs(start, arr, recr_target):
        nonlocal res
        if recr_target == 0:
            res.append(copy.deepcopy(arr))
            return

        for i in range(start, len(candidates)):
            if candidates[i] <= recr_target:
                arr.append(candidates[i])
                dfs(i, arr, recr_target-candidates[i])
                arr.pop()  # 关键


    dfs(0, [], target)
    return res


a = [1, 2]
target = 4

print(combinationSum(a, target))
