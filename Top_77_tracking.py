from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k == 0:
            return []
        candidates = [i for i in range(1, n + 1)]
        res = []
        self.dfs(candidates, 0, [], res, k)
        return res

    def dfs(self, candidates, index, comb, res, k):
        if len(comb) == k:
            res.append(comb[:])
            return
        for i in range(index, len(candidates)):
            comb.append(candidates[i])
            # index += 1
            # self.dfs(candidates, index, comb, res, k)
            # 一开始没有index +=1
            # 参数通过


            comb.pop()
        for i in range(index, len(candidates)):
            comb.append(candidates[i])
            print('index', index)
            print('comb1', comb)
            # ---------------- 记录了正确做法和错误做法 ---------------
            # ---------------- 记录了正确做法和错误做法 ---------------
            # ---------------- 记录了正确做法和错误做法 ---------------
            # 正确写法如下
            index += 1
            self.dfs(candidates, index, comb, res, k)

            # 下面是一开始的错误写法
            # self.dfs(candidates, index + 1, comb, res, k)

            # 错误原因:
            # 一开始传入的index的值一只都没有变，只能从一开始的位置加1，而不能往前推进

            # ---------------- 记录了正确做法和错误做法 ---------------
            # ---------------- 记录了正确做法和错误做法 ---------------
            # ---------------- 记录了正确做法和错误做法 ---------------
            comb.pop()
            print('comb2', comb)
            print('--------------')

a = Solution()
print(a.combine(3,2))