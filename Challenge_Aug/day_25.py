"""
day 25
LeeCode.633  没做过

没想到这个题能转换成 2 pointer的解法

Author: Alex
Date: 25/08/2021 - NZ Auckland
      8:00 -

      思路：
      看代码
"""
from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))
        while left <= right:
            cur = left ** 2 + right ** 2
            if cur == c:
                return True
            elif cur > c:
                right -= 1
            else:
                left += 1
        return False
