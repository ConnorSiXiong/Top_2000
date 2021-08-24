"""
contest 255 第二题

LeeCode 1980 没做过
一开始的思路是

比赛思路1：
TLE
DFS permutation所有的可能性，最后在比较
超时了

比赛思路2:
permutation可以创造出非常多的可能性
题目里面给出的可能性只有n个，n <= 16，所以可能出现的组合可以【轻松】超过n

那么用一个for循环去构建一个长度n的排列，然后随意改变其中一些位置的数就能很快得到可能解

思路3:
backtracking, 这个是网友的思路,

- 使用了Counter对set中的可能组合进行计数，这个办法我不知道, 导致了我最后不ok
使用这个的时候注意终止条件，网友用的flag很好，成功的剪枝了！


Author: Alex
Date:
22/08/2021 - NZ Auckland
14:20 - 14:50

24/08/2021 - NZ Auckland
12:00 - 12:30
"""
from collections import Counter


class Solution2:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        box = Counter(set(nums))
        cur = ''
        res = ''
        flag = True

        def dfs(cur_str, box, index, n):
            print('comb', cur_str)
            nonlocal flag
            nonlocal res
            if not flag:
                return

            if index == n:
                if box[cur_str] == 0:
                    res = cur_str
                    flag = False
                return

            for i in range(2):
                cur_str += str(i)
                dfs(cur_str, box, index + 1, n)
                cur_str = cur_str[:-1]

        dfs(cur, box, 0, len(nums))
        print(res)
        return res


class Solution3:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ''
        stop = False
        n = len(nums)
        box = Counter(set(nums))

        def dfs(comb, box, n):
            print('comb', comb)
            nonlocal res
            nonlocal stop
            if stop is True:
                return

            if len(comb) == n:
                if box[comb] == 0:
                    res = comb
                    stop = True
                    return
                return

            for i in range(2):
                comb += str(i)
                dfs(comb, box, n)
                comb = comb[:-1]

        dfs('', box, n)
        print(res)
        return res

