"""
day 24
LeeCode.537  没做过

看了一下，就是一个数学题，应该很简单，不知道为什么是medium

Author: Alex
Date: 25/08/2021 - NZ Auckland
      16:00 - 16:13

      思路：
      1.用字符串把各个️部分分开去做数学运算



      感觉还可以做更快，中间有一些数据转换的地方的思路不够清晰导致的中间修改，额外花费了一点时间

"""

num1a = "1+1i"
num2a = "1+1i"
# res = "0+2i"

num1b = "1+-1i"
num2b = "1+-1i"


# res = "0+-2i"

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_left, num1_right = num1.split('+')
        num2_left, num2_right = num2.split('+')

        num1_left = int(num1_left)
        num2_left = int(num2_left)

        num1_right = int(num1_right[:-1])
        num2_right = int(num2_right[:-1])

        part1_1 = int(num1_left) * int(num2_left)
        part1_2 = int(num1_right) * int(num2_right) * -1
        part1 = part1_1 + part1_2
        print(part1)
        print(num1_left)
        print(num2_right)
        part2 = num1_left * num2_right + num2_left * num1_right

        return str(part1) + '+' + str(part2) + 'i'


a = Solution()
print(a.complexNumberMultiply(num1b, num2b))


class Solution2:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        """
        添加了小明的解法，这个写法很简洁
        """
        a1, b1 = map(int, num1[:-1].split('+'))
        a2, b2 = map(int, num2[:-1].split('+'))
        return '%d+%d' % (a1 * a1 - b1 * b2, a2 * b2 + a2 * b1)
