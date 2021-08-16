"""
day 4
leetcode 79 没做过

看了一下，用dfs backtracking

Author: Alex
Date: 16/08/2021 - NZ Auckland
      19:30 pm - 20:24 pm
      做出基本解法

      20:24 pm - 20:40 pm
      没有考虑target里面全是重复的单词的情况

      最后一个case没过，需要优化

      思路：
      1.while 循环的边界, 是 <=
        切片操作的时候，index是算左，不算右

      2.left和right pointers

      2.1 先移动right，扩大窗口，当t全部存在时，记录一下
      2.2 移动left，缩小窗口，开始打擂台
      2.3 当t无法全部存在的时候，left停止移动，又开始移动right（回到2.1）

      Q - 我想，可能是打擂台的算法优化一下就能通过最后TEL的case


"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = len(t)

        candidates = []
        shortest = float('inf')
        res = ''
        t_dict = self.generateTargetDict(t)
        print(t_dict)
        while left != right and right <= len(s):
            sub = s[left: right]
            print('sub', sub)
            if self.checkExist(sub, t_dict.copy()):
                candidates.append(sub)
                if len(sub) < shortest:
                    res = sub
                    shortest = len(sub)
                left += 1
            else:
                if right < len(s):
                    right += 1
                else:
                    left += 1
        print(candidates)
        print('res', res)
        return res

    def checkExist(self, comb, target_dict):
        print('comb', comb)
        for i in comb:
            if i in target_dict.keys():
                target_dict[i] -= 1

        for i in target_dict.keys():
            if target_dict[i] > 0:
                return False
        return True

    def generateTargetDict(self, target):
        target_dict = {}

        for i in target:
            if i in target_dict.keys():
                target_dict[i] += 1
            else:
                target_dict[i] = 1
        return target_dict


S = "ADOBECODEBANC"
T = "ABC"

# S = 'aa'
# T = 'aa'

a = Solution()
a.minWindow(S, T)
